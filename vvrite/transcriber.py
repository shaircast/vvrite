"""Qwen3 ASR transcription using mlx-audio."""

import os
import tempfile

import numpy as np
import soundfile as sf
from huggingface_hub import model_info, snapshot_download
from mlx_audio.stt.utils import load_model

from vvrite.preferences import Preferences, SAMPLE_RATE
from vvrite import audio_utils


_model = None
_warmed_up = False


def is_model_loaded() -> bool:
    """Return True if the ASR model is loaded in memory."""
    return _model is not None


def is_model_cached(model_id: str) -> bool:
    """Return True if the model is already downloaded locally."""
    try:
        snapshot_download(repo_id=model_id, local_files_only=True)
        return True
    except Exception:
        return False


def get_model_size(model_id: str) -> int:
    """Return total model size in bytes. Returns 0 on error."""
    try:
        info = model_info(model_id, files_metadata=True)
        return sum(s.size for s in info.siblings if s.size)
    except Exception:
        return 0


def download_model(model_id: str) -> str:
    """Download model files and return local path."""
    return snapshot_download(repo_id=model_id)


def load_from_local(local_path: str):
    """Load model from a local directory into memory."""
    global _model, _warmed_up
    _model = load_model(local_path)
    _warmed_up = False
    _safe_warm_up()


def load(prefs: Preferences = None):
    """Download + load in one step. Used by existing non-onboarding flow."""
    global _model, _warmed_up
    if prefs is None:
        prefs = Preferences()
    model_id = prefs.model_id
    print(f"Loading model: {model_id} ...")
    _model = load_model(model_id)
    _warmed_up = False
    _safe_warm_up()
    print("Model loaded.")


def _create_warmup_audio() -> str:
    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, np.zeros(SAMPLE_RATE // 2, dtype=np.float32), SAMPLE_RATE)
    return path


def warm_up():
    """Run a tiny silent transcription to trigger first-use compilation work."""
    global _warmed_up
    if _model is None or _warmed_up:
        return

    warmup_path = _create_warmup_audio()
    try:
        _model.generate(warmup_path, max_tokens=1)
        _warmed_up = True
    finally:
        try:
            os.unlink(warmup_path)
        except OSError:
            pass


def _safe_warm_up():
    try:
        warm_up()
    except Exception as e:
        print(f"Model warm-up skipped: {e}")


def transcribe(raw_wav_path: str, prefs: Preferences = None) -> str:
    """
    Normalize audio via ffmpeg, then transcribe with Qwen3-ASR.
    Cleans up temp files after processing.
    """
    if prefs is None:
        prefs = Preferences()

    from vvrite.locales import ASR_LANGUAGE_MAP

    normalized_path = audio_utils.normalize(raw_wav_path)
    try:
        kwargs = {"max_tokens": prefs.max_tokens}
        custom_words = prefs.custom_words.strip()
        if custom_words:
            kwargs["system_prompt"] = f"Use the following spellings: {custom_words}"

        asr_lang = prefs.asr_language
        if asr_lang != "auto":
            language_param = ASR_LANGUAGE_MAP.get(asr_lang)
            if language_param is None:
                print(f"Unknown ASR language code: {asr_lang}, falling back to auto-detect")
            else:
                kwargs["language"] = language_param

        result = _model.generate(
            normalized_path,
            **kwargs,
        )
        return result.text.strip()
    finally:
        for path in (raw_wav_path, normalized_path):
            try:
                os.unlink(path)
            except OSError:
                pass

"""Qwen3 ASR transcription using mlx-audio."""

import os

import miniaudio
import numpy as np
from huggingface_hub import model_info, snapshot_download

from vvrite.mlx_runtime import (
    install_qwen_only_model_namespace,
    install_qwen_tokenizer_registry,
)


install_qwen_only_model_namespace()
install_qwen_tokenizer_registry()

from mlx_audio.stt.utils import load_model  # noqa: E402

from vvrite.preferences import Preferences, SAMPLE_RATE  # noqa: E402


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


def _decode_audio(path: str) -> np.ndarray:
    """Decode and resample a recorded WAV to mono 16 kHz float32 audio."""
    decoded = miniaudio.decode_file(
        path,
        output_format=miniaudio.SampleFormat.FLOAT32,
        nchannels=1,
        sample_rate=SAMPLE_RATE,
    )
    return np.asarray(decoded.samples, dtype=np.float32)


def warm_up():
    """Run a tiny silent transcription to trigger first-use compilation work."""
    global _warmed_up
    if _model is None or _warmed_up:
        return

    silence = np.zeros(SAMPLE_RATE // 2, dtype=np.float32)
    _model.generate(silence, max_tokens=1)
    _warmed_up = True


def _safe_warm_up():
    try:
        warm_up()
    except Exception as e:
        print(f"Model warm-up skipped: {e}")


def transcribe(raw_wav_path: str, prefs: Preferences = None) -> str:
    """
    Transcribe a recorded WAV with Qwen3-ASR.

    miniaudio decodes and resamples the WAV to 16 kHz mono, so no external
    ffmpeg or SciPy runtime is needed. Cleans up the temp file after processing.
    """
    if prefs is None:
        prefs = Preferences()

    from vvrite.locales import ASR_LANGUAGE_MAP

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

        audio = _decode_audio(raw_wav_path)
        result = _model.generate(audio, **kwargs)
        return result.text.strip()
    finally:
        try:
            os.unlink(raw_wav_path)
        except OSError:
            pass

"""Microphone recording using sounddevice."""

import os
import tempfile
from typing import Callable

import numpy as np
import sounddevice as sd
import soundfile as sf

from vvrite.preferences import SAMPLE_RATE, CHANNELS


def _compute_rms(data: np.ndarray) -> float:
    """Compute RMS level normalized to 0.0-1.0 range for int16 audio."""
    float_data = data.astype(np.float64)
    rms = np.sqrt(np.mean(float_data ** 2))
    return min(rms / 32768.0, 1.0)


class Recorder:
    def __init__(self):
        self._frames: list[np.ndarray] = []
        self._stream = None
        self._level_callback: Callable[[float], None] | None = None

    def start(self, device=None, level_callback=None):
        """Start recording from the specified microphone.

        Args:
            device: Device name string or None for system default.
            level_callback: Called with RMS level (0.0-1.0) per audio chunk.
        """
        self._frames = []
        self._level_callback = level_callback

        device_idx = None
        if device is not None:
            devices = sd.query_devices()
            for i, d in enumerate(devices):
                if device in d["name"] and d["max_input_channels"] > 0:
                    device_idx = i
                    break
            if device_idx is None:
                raise RuntimeError(f"Microphone not found: {device}")

        self._stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",
            device=device_idx,
            callback=self._callback,
        )
        self._stream.start()

    def _callback(self, indata, frames, time_info, status):
        self._frames.append(indata.copy())
        if self._level_callback is not None:
            level = _compute_rms(indata)
            self._level_callback(level)

    def stop(self) -> str | None:
        """Stop recording and return path to the raw WAV file."""
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None

        self._level_callback = None

        if not self._frames:
            return None

        audio = np.concatenate(self._frames, axis=0)
        fd, path = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        sf.write(path, audio, SAMPLE_RATE, subtype="PCM_16")
        return path

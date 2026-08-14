"""Narrow mlx-audio's eager model package to the Qwen backend we ship.

mlx-audio 0.4.0 imports every STT backend from ``mlx_audio.stt.models``.
Importing the Qwen backend therefore also imports Whisper, whose timestamp
module pulls in numba and llvmlite.  vvrite supports one fixed model, so loading
those sibling backends only increases startup time and the frozen app size.

This module installs a namespace-package placeholder for the parent model
package.  Python can still import ``mlx_audio.stt.models.qwen3_asr`` normally,
but it does not execute the eager parent ``__init__.py`` first.  The matching
mlx-audio version is pinned in requirements.in so this workaround cannot drift
silently across upstream package layouts.
"""

from __future__ import annotations

import importlib.machinery
from pathlib import Path
import sys
import types


_MODELS_PACKAGE = "mlx_audio.stt.models"


def install_qwen_only_model_namespace() -> bool:
    """Install the lazy model namespace, returning whether it was installed."""
    if _MODELS_PACKAGE in sys.modules:
        return False

    import mlx_audio

    mlx_audio_dir = Path(mlx_audio.__file__).resolve().parent
    models_dir = mlx_audio_dir / "stt" / "models"

    namespace = types.ModuleType(_MODELS_PACKAGE)
    namespace.__file__ = str(models_dir / "__init__.py")
    namespace.__loader__ = None
    namespace.__package__ = _MODELS_PACKAGE
    namespace.__path__ = [str(models_dir)]

    spec = importlib.machinery.ModuleSpec(
        _MODELS_PACKAGE,
        loader=None,
        is_package=True,
    )
    spec.submodule_search_locations = list(namespace.__path__)
    namespace.__spec__ = spec

    sys.modules[_MODELS_PACKAGE] = namespace
    return True


def install_qwen_tokenizer_registry() -> bool:
    """Register Qwen's tokenizer without Transformers' broad model scan.

    Qwen3-ASR declares ``Qwen2Tokenizer`` while using a custom model type.
    Transformers 5 otherwise searches every model mapping that shares that
    tokenizer name, which is both unnecessary and incompatible with vvrite's
    deliberately minimal frozen bundle.
    """
    from transformers.models.auto.tokenization_auto import (
        REGISTERED_TOKENIZER_CLASSES,
    )
    from transformers.models.qwen2.tokenization_qwen2 import Qwen2Tokenizer

    already_registered = (
        REGISTERED_TOKENIZER_CLASSES.get("Qwen2Tokenizer") is Qwen2Tokenizer
    )
    REGISTERED_TOKENIZER_CLASSES["Qwen2Tokenizer"] = Qwen2Tokenizer
    return not already_registered

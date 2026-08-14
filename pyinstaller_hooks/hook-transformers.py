"""Minimal Transformers hook for Qwen3-ASR inference.

The upstream PyInstaller hook copies source files and metadata for every
optional Transformers integration found in the build environment.  vvrite uses
only the auto-loading helpers, Qwen2 tokenization, and Whisper feature
extraction.  Keep only their source trees on disk and let normal PyInstaller
analysis collect bytecode for the used modules.

Transformers 5 builds its lazy import structure by scanning ``models`` and
reading the selected packages' source files at runtime.  Those files therefore
must exist outside PyInstaller's PYZ archive even though vvrite does not use
TorchScript.
"""

from pathlib import Path

from PyInstaller.utils.hooks import copy_metadata, get_module_file_attribute


transformers_dir = Path(get_module_file_attribute("transformers")).resolve().parent
datas = [
    # Transformers 5 scans this package initializer from disk before resolving
    # any lazy model exports.  Keeping only child packages physical is not
    # sufficient: create_import_structure_from_path() opens this exact file.
    (str(transformers_dir / "models" / "__init__.py"), "transformers/models"),
]

module_collection_mode = {
    "transformers.models.auto": "pyz+py",
    "transformers.models.encoder_decoder": "pyz+py",
    "transformers.models.qwen2": "pyz+py",
    "transformers.models.whisper": "pyz+py",
}

for distribution in (
    "transformers",
    "tqdm",
    "regex",
    "requests",
    "packaging",
    "filelock",
    "numpy",
    "tokenizers",
    "huggingface-hub",
    "safetensors",
    "PyYAML",
):
    datas += copy_metadata(distribution)

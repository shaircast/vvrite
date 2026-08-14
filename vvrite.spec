"""PyInstaller spec for vvrite macOS app."""
import os
import sys
from pathlib import Path

ROOT_DIR = os.path.abspath(os.getcwd())
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from PyInstaller.utils.hooks import collect_submodules
import mlx
import soundfile
from vvrite import APP_BUNDLE_IDENTIFIER, __version__

block_cipher = None

SPARKLE_APPCAST_URL = os.environ.get(
    "SPARKLE_APPCAST_URL",
    "https://github.com/shaircast/vvrite/releases/latest/download/appcast.xml",
)
SPARKLE_PUBLIC_ED_KEY = os.environ.get("SPARKLE_PUBLIC_ED_KEY", "").strip()

info_plist = {
    "CFBundleName": "vvrite",
    "CFBundleShortVersionString": __version__,  # sourced from vvrite/__init__.__version__
    "CFBundleVersion": "11",  # monotonic build number; bump each release
    "LSUIElement": True,
    "NSMicrophoneUsageDescription": (
        "vvrite needs microphone access to record and transcribe your speech."
    ),
    "NSHighResolutionCapable": True,
    "NSSupportsAutomaticTermination": False,
    "NSSupportsSuddenTermination": False,
    "SUFeedURL": SPARKLE_APPCAST_URL,
    "SUEnableAutomaticChecks": True,
    "SUScheduledCheckInterval": 86400,
}

if SPARKLE_PUBLIC_ED_KEY:
    info_plist["SUPublicEDKey"] = SPARKLE_PUBLIC_ED_KEY

soundfile_data_dir = Path(soundfile.__file__).resolve().parent / "_soundfile_data"
mlx_package_dir = Path(next(iter(mlx.__path__))).resolve()
mlx_lib_dir = mlx_package_dir / "lib"

# PyObjC bridge modules need all submodules collected
pyobjc_hiddenimports = (
    collect_submodules("objc")
    + collect_submodules("AppKit")
    + collect_submodules("Foundation")
    + collect_submodules("Quartz")
    + collect_submodules("ApplicationServices")
    + collect_submodules("AVFoundation")
    + collect_submodules("ServiceManagement")
)

a = Analysis(
    ["vvrite/main.py"],
    pathex=[],
    binaries=[],
    datas=[
        # soundfile needs libsndfile
        (str(soundfile_data_dir), "_soundfile_data"),
        # MLX Metal shaders and native libs
        (str(mlx_lib_dir), os.path.join("mlx", "lib")),
    ],
    hiddenimports=pyobjc_hiddenimports + [
        # Locale modules (dynamically imported by vvrite.locales)
        *collect_submodules("vvrite.locales"),
        # MLX (namespace package — must be explicit)
        "mlx",
        "mlx._reprlib_fix",
        "mlx.core",
        "mlx.nn",
        "mlx.optimizers",
        "mlx.utils",
        # MLX ecosystem
        "mlx_lm",
        "mlx_audio",
        "mlx_audio.stt",
        "mlx_audio.stt.models.qwen3_asr",
        # WAV decode + 16k mono resample backend, lazy-imported by mlx_audio
        # at transcribe time (replaces the bundled ffmpeg normalization step)
        "mlx_audio.audio_io",
        "miniaudio",
        # Transformers
        "transformers",
        "transformers.models.qwen2.tokenization_qwen2",
        "transformers.models.whisper.feature_extraction_whisper",
        "tokenizers",
        # Audio
        "sounddevice",
        "soundfile",
        # Other
        "huggingface_hub",
        "safetensors",
        "numpy",
    ],
    hookspath=[os.path.join(ROOT_DIR, "pyinstaller_hooks")],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "tkinter",
        "pytest",
        # Heavy packages not needed (we use mlx, not torch)
        "torch",
        "torchaudio",
        "torchvision",
        "accelerate",
        "bitsandbytes",
        "datasets",
        "fastapi",
        "librosa",
        "llvmlite",
        "mistral_common",
        "mlx_audio.lid",
        "mlx_audio.server",
        "mlx_audio.sts",
        "mlx_audio.tts",
        "mlx_audio.vad",
        "mlx_audio.stt.models.glmasr",
        "mlx_audio.stt.models.lasr_ctc",
        "mlx_audio.stt.models.parakeet",
        "mlx_audio.stt.models.vibevoice_asr",
        "mlx_audio.stt.models.voxtral",
        "mlx_audio.stt.models.voxtral_realtime",
        "mlx_audio.stt.models.wav2vec",
        "mlx_audio.stt.models.whisper",
        "numba",
        "openai",
        "pyloudnorm",
        "sentencepiece",
        "sklearn",
        "scipy",
        "soxr",
        "tiktoken",
        "timm",
        "uvicorn",
        "pyarrow",
        "cv2",
        "opencv-python",
        "onnxruntime",
        "PIL",
        "matplotlib",
        "pandas",
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="vvrite",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    target_arch="arm64",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name="vvrite",
)

app = BUNDLE(
    coll,
    name="vvrite.app",
    icon="assets/vvrite.icns",
    bundle_identifier=APP_BUNDLE_IDENTIFIER,
    info_plist=info_plist,
)

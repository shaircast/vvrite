"""py2app build configuration for vvrite."""
import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

sys.setrecursionlimit(5000)

from setuptools import setup
from vvrite import APP_BUNDLE_IDENTIFIER

APP = ["vvrite/main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": False,
    "plist": {
        "CFBundleName": "vvrite",
        "CFBundleIdentifier": APP_BUNDLE_IDENTIFIER,
        "CFBundleShortVersionString": "1.0.5",  # keep in sync with vvrite/__init__.__version__
        "CFBundleVersion": "5",
        "LSUIElement": True,
        "NSMicrophoneUsageDescription": (
            "vvrite needs microphone access to record and transcribe your speech."
        ),
        "NSHighResolutionCapable": True,
    },
    "packages": [
        "vvrite",
        "mlx",
        "mlx_audio",
        "mlx_lm",
        "transformers",
        "sounddevice",
        "soundfile",
        "numpy",
        "huggingface_hub",
    ],
    "includes": [
        "Quartz",
        "AppKit",
        "Foundation",
        "ApplicationServices",
        "ServiceManagement",
        "objc",
    ],
    "excludes": [
        "tkinter",
        "unittest",
        "test",
    ],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)

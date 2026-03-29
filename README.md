<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="vvrite icon">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  macOS menu bar app that transcribes your voice and pastes the text — powered by on-device AI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.ko.md">한국어</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-Hans.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a>
</p>

---

## How It Works

1. Press the hotkey (default: `Option + Space`)
2. Speak — a recording overlay appears on screen
3. Press the hotkey again to stop
4. Your speech is transcribed locally and pasted into the active text field

Everything runs on-device using [MLX](https://github.com/ml-explore/mlx). No audio leaves your Mac.
The default model also brings strong multilingual ASR support, so supported languages such as Korean, English, Japanese, Chinese, Cantonese, French, German, and Spanish work out of the box.

## Features

- **On-device transcription** — Qwen3-ASR running via mlx-audio, no cloud API needed
- **Multilingual-ready** — the default Qwen3-ASR model supports language identification and transcription across 30 languages and 22 Chinese dialects, and vvrite does not lock transcription to a single language
- **Global hotkey** — trigger from any app, configurable in Settings
- **Menu bar app** — lives quietly in your status bar
- **Recording overlay** — visual feedback with audio level bars and timer
- **ESC to cancel** — press Escape during recording to dismiss without transcribing
- **Auto-paste** — transcribed text is pasted directly into the active field
- **Guided onboarding** — first launch walks you through permissions and model download

## Language Support

vvrite uses [`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit), which is an MLX conversion of [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B). According to the official Qwen model card, Qwen3-ASR-1.7B supports language identification and speech recognition for 30 languages and 22 Chinese dialects.

That includes Korean, English, Japanese, Chinese, Cantonese, Arabic, German, French, Spanish, Portuguese, Indonesian, Italian, Russian, Thai, Vietnamese, Turkish, Hindi, Malay, Dutch, Swedish, Danish, Finnish, Polish, Czech, Filipino, Persian, Greek, Hungarian, Macedonian, and Romanian, plus regional Chinese dialect support. Because vvrite uses that checkpoint directly through mlx-audio and does not force a fixed recognition language, multilingual dictation works well for the model's supported languages.

## Requirements

- macOS 15+ on Apple Silicon for pre-built .app; macOS 13+ when building from source
- ~2 GB disk space for the ASR model
- `ffmpeg` installed when running from source
- Microphone permission
- Accessibility permission (for global hotkey)

## Installation

### From Source

```bash
# Clone
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# Install dependencies
pip install -r requirements.txt
brew install ffmpeg

# Run
python -m vvrite
```

### Build as .app

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh` is the supported build path. It performs the PyInstaller build, code signing, notarization, stapling, and DMG creation. It requires a configured Apple Developer signing identity and `notarytool` profile.

## Usage

| Action | Shortcut |
|---|---|
| Start / stop recording | `Option + Space` (configurable) |
| Cancel recording | `Escape` |
| Open settings | Click menu bar icon → Settings |

On first launch, the onboarding wizard will guide you through:
1. Granting microphone and accessibility permissions
2. Setting your preferred hotkey
3. Downloading the ASR model (~1.7 GB)

## Tech Stack

| Component | Technology |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| ASR Model | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| Inference | [mlx-audio](https://github.com/ml-explore/mlx-audio) on Apple Silicon GPU |
| Audio | sounddevice + ffmpeg |
| Packaging | PyInstaller |

## License

MIT — see [LICENSE](LICENSE) for details.

This application bundles [ffmpeg](https://ffmpeg.org/), which is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html). The ffmpeg source code is available at https://ffmpeg.org/download.html. The ASR model [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) is licensed under Apache 2.0.

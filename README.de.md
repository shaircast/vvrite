<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="vvrite Symbol">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  macOS-Menüleisten-App, die Ihre Stimme transkribiert und den Text einfügt — angetrieben durch On-Device-KI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-Hans.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · Deutsch
</p>

---

## So funktioniert es

1. Drücken Sie die Tastenkombination (Standard: `Option + Space`)
2. Sprechen Sie — ein Aufnahme-Overlay erscheint auf dem Bildschirm
3. Drücken Sie die Tastenkombination erneut, um die Aufnahme zu beenden
4. Ihre Sprache wird lokal transkribiert und in das aktive Textfeld eingefügt

Alles läuft auf dem Gerät mit [MLX](https://github.com/ml-explore/mlx). Kein Audio verlässt Ihren Mac.
Das Standardmodell bietet zudem eine starke mehrsprachige Spracherkennungsunterstützung, sodass unterstützte Sprachen wie Koreanisch, Englisch, Japanisch, Chinesisch, Kantonesisch, Französisch, Deutsch und Spanisch sofort einsatzbereit sind.

## Funktionen

- **On-Device-Transkription** — Qwen3-ASR läuft über mlx-audio, keine Cloud-API erforderlich
- **Mehrsprachig einsatzbereit** — das Standard-Qwen3-ASR-Modell unterstützt Sprachidentifikation und Transkription in 30 Sprachen und 22 chinesischen Dialekten, und vvrite beschränkt die Transkription nicht auf eine einzelne Sprache
- **Globale Tastenkombination** — aus jeder App auslösbar, in den Einstellungen konfigurierbar
- **Menüleisten-App** — befindet sich unauffällig in Ihrer Statusleiste
- **Aufnahme-Overlay** — visuelles Feedback mit Audio-Pegelbalken und Timer
- **ESC zum Abbrechen** — drücken Sie Escape während der Aufnahme, um ohne Transkription abzubrechen
- **Automatisches Einfügen** — transkribierter Text wird direkt in das aktive Feld eingefügt
- **Geführte Einrichtung** — beim ersten Start werden Sie durch Berechtigungen und Modell-Download geleitet

## Sprachunterstützung

vvrite verwendet [`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit), eine MLX-Konvertierung von [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B). Laut der offiziellen Qwen-Modellkarte unterstützt Qwen3-ASR-1.7B Sprachidentifikation und Spracherkennung für 30 Sprachen und 22 chinesische Dialekte.

Dazu gehören Koreanisch, Englisch, Japanisch, Chinesisch, Kantonesisch, Arabisch, Deutsch, Französisch, Spanisch, Portugiesisch, Indonesisch, Italienisch, Russisch, Thai, Vietnamesisch, Türkisch, Hindi, Malaiisch, Niederländisch, Schwedisch, Dänisch, Finnisch, Polnisch, Tschechisch, Filipino, Persisch, Griechisch, Ungarisch, Mazedonisch und Rumänisch sowie regionale chinesische Dialekte. Da vvrite diesen Checkpoint direkt über mlx-audio verwendet und keine feste Erkennungssprache erzwingt, funktioniert mehrsprachiges Diktieren für die vom Modell unterstützten Sprachen gut.

## Voraussetzungen

- Vorgefertigte .app: macOS 15 oder neuer auf Apple Silicon (M1/M2/M3/M4); aus Quellcode: macOS 13+
- Ca. 2 GB Speicherplatz für das ASR-Modell
- `ffmpeg` muss bei Ausführung aus dem Quellcode installiert sein
- Mikrofonberechtigung
- Bedienungshilfen-Berechtigung (für die globale Tastenkombination)

## Installation

### Aus dem Quellcode

```bash
# Klonen
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# Abhängigkeiten installieren
pip install -r requirements.txt
brew install ffmpeg

# Starten
python -m vvrite
```

### Als .app kompilieren

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh` ist der empfohlene Build-Weg. Er führt den PyInstaller-Build, die Code-Signierung, Notarisierung, das Heften und die DMG-Erstellung durch. Es werden eine konfigurierte Apple Developer-Signieridentität und ein `notarytool`-Profil benötigt.

## Verwendung

| Aktion | Tastenkürzel |
|---|---|
| Aufnahme starten / stoppen | `Option + Space` (konfigurierbar) |
| Aufnahme abbrechen | `Escape` |
| Einstellungen öffnen | Klick auf das Menüleisten-Symbol → Einstellungen |

Beim ersten Start führt Sie der Einrichtungsassistent durch:
1. Erteilung der Mikrofon- und Bedienungshilfen-Berechtigungen
2. Einstellung Ihrer bevorzugten Tastenkombination
3. Download des ASR-Modells (ca. 1,7 GB)

## Technologie-Stack

| Komponente | Technologie |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| ASR-Modell | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| Inferenz | [mlx-audio](https://github.com/ml-explore/mlx-audio) auf Apple Silicon GPU |
| Audio | sounddevice + ffmpeg |
| Paketierung | PyInstaller |

## Lizenz

MIT — siehe [LICENSE](LICENSE) für Details.

Diese Anwendung enthält [ffmpeg](https://ffmpeg.org/), das unter der [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) lizenziert ist. Der ffmpeg-Quellcode ist unter https://ffmpeg.org/download.html verfügbar. Das ASR-Modell [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) ist unter Apache 2.0 lizenziert.

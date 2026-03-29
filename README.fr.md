<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="icône vvrite">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  Application de barre de menus macOS qui transcrit votre voix et colle le texte — propulsée par l'IA embarquée.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-Hans.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.es.md">Español</a> · Français · <a href="README.de.md">Deutsch</a>
</p>

---

## Comment ça marche

1. Appuyez sur le raccourci clavier (par défaut : `Option + Space`)
2. Parlez — une fenêtre superposée d'enregistrement apparaît à l'écran
3. Appuyez à nouveau sur le raccourci pour arrêter l'enregistrement
4. Votre voix est transcrite localement et collée dans le champ de texte actif

Tout s'exécute sur l'appareil grâce à [MLX](https://github.com/ml-explore/mlx). Aucun audio ne quitte votre Mac.
Le modèle par défaut offre également une prise en charge multilingue robuste de la reconnaissance vocale. Les langues prises en charge comme le coréen, l'anglais, le japonais, le chinois, le cantonais, le français, l'allemand et l'espagnol fonctionnent directement.

## Fonctionnalités

- **Transcription embarquée** — Qwen3-ASR s'exécute via mlx-audio, aucune API cloud nécessaire
- **Prêt pour le multilingue** — le modèle Qwen3-ASR par défaut prend en charge l'identification linguistique et la transcription dans 30 langues et 22 dialectes chinois, et vvrite ne verrouille pas la transcription sur une seule langue
- **Raccourci clavier global** — déclenchement depuis n'importe quelle application, configurable dans les Réglages
- **Application de barre de menus** — se loge discrètement dans votre barre d'état
- **Fenêtre superposée d'enregistrement** — retour visuel avec barres de niveau audio et minuteur
- **ESC pour annuler** — appuyez sur Échap pendant l'enregistrement pour annuler sans transcrire
- **Collage automatique** — le texte transcrit est collé directement dans le champ actif
- **Configuration guidée** — le premier lancement vous guide à travers les autorisations et le téléchargement du modèle

## Prise en charge linguistique

vvrite utilise [`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit), qui est une conversion MLX de [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B). Selon la fiche officielle du modèle Qwen, Qwen3-ASR-1.7B prend en charge l'identification linguistique et la reconnaissance vocale pour 30 langues et 22 dialectes chinois.

Cela inclut le coréen, l'anglais, le japonais, le chinois, le cantonais, l'arabe, l'allemand, le français, l'espagnol, le portugais, l'indonésien, l'italien, le russe, le thaï, le vietnamien, le turc, l'hindi, le malais, le néerlandais, le suédois, le danois, le finnois, le polonais, le tchèque, le philippin, le persan, le grec, le hongrois, le macédonien et le roumain, ainsi que la prise en charge des dialectes chinois régionaux. Comme vvrite utilise ce point de contrôle directement via mlx-audio et n'impose pas une langue de reconnaissance fixe, la dictée multilingue fonctionne bien pour les langues prises en charge par le modèle.

## Prérequis

- .app pré-compilée : macOS 15 ou supérieur sur Apple Silicon (M1/M2/M3/M4) ; compilation depuis les sources : macOS 13+
- Environ 2 Go d'espace disque pour le modèle ASR
- `ffmpeg` installé lors de l'exécution depuis le code source
- Autorisation du microphone
- Autorisation d'accessibilité (pour le raccourci clavier global)

## Installation

### Depuis le code source

```bash
# Cloner
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# Installer les dépendances
pip install -r requirements.txt
brew install ffmpeg

# Lancer
python -m vvrite
```

### Compiler en .app

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh` est la méthode de compilation recommandée. Elle effectue la compilation PyInstaller, la signature du code, la notarisation, l'agrafage et la création du DMG. Elle nécessite une identité de signature Apple Developer configurée et un profil `notarytool`.

## Utilisation

| Action | Raccourci |
|---|---|
| Démarrer / arrêter l'enregistrement | `Option + Space` (configurable) |
| Annuler l'enregistrement | `Escape` |
| Ouvrir les réglages | Clic sur l'icône de la barre de menus → Réglages |

Au premier lancement, l'assistant de configuration vous guidera à travers :
1. L'octroi des autorisations microphone et accessibilité
2. La configuration de votre raccourci clavier préféré
3. Le téléchargement du modèle ASR (environ 1,7 Go)

## Stack technique

| Composant | Technologie |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| Modèle ASR | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| Inférence | [mlx-audio](https://github.com/ml-explore/mlx-audio) sur GPU Apple Silicon |
| Audio | sounddevice + ffmpeg |
| Empaquetage | PyInstaller |

## Licence

MIT — voir [LICENSE](LICENSE) pour les détails.

Cette application inclut [ffmpeg](https://ffmpeg.org/), qui est sous licence [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html). Le code source de ffmpeg est disponible sur https://ffmpeg.org/download.html. Le modèle ASR [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) est sous licence Apache 2.0.

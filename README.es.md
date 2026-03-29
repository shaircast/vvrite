<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="ícono de vvrite">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  App de barra de menú de macOS que transcribe tu voz y pega el texto — impulsada por IA en el dispositivo.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-Hans.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · Español · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a>
</p>

---

## Cómo funciona

1. Presiona la tecla de acceso rápido (por defecto: `Option + Space`)
2. Habla — aparece una ventana superpuesta de grabación en pantalla
3. Presiona la tecla de acceso rápido nuevamente para detener la grabación
4. Tu voz se transcribe localmente y se pega en el campo de texto activo

Todo se ejecuta en el dispositivo usando [MLX](https://github.com/ml-explore/mlx). Ningún audio sale de tu Mac.
El modelo predeterminado también ofrece un sólido soporte multilingüe de reconocimiento de voz, por lo que idiomas compatibles como coreano, inglés, japonés, chino, cantonés, francés, alemán y español funcionan de inmediato.

## Características

- **Transcripción en el dispositivo** — Qwen3-ASR se ejecuta a través de mlx-audio, sin necesidad de API en la nube
- **Soporte multilingüe** — el modelo Qwen3-ASR predeterminado soporta identificación de idioma y transcripción en 30 idiomas y 22 dialectos chinos, y vvrite no bloquea la transcripción a un solo idioma
- **Tecla de acceso rápido global** — se activa desde cualquier app, configurable en Ajustes
- **App de barra de menú** — se ubica discretamente en tu barra de estado
- **Ventana superpuesta de grabación** — retroalimentación visual con barras de nivel de audio y temporizador
- **ESC para cancelar** — presiona Escape durante la grabación para cancelar sin transcribir
- **Pegado automático** — el texto transcrito se pega directamente en el campo activo
- **Configuración guiada** — el primer inicio te guía a través de los permisos y la descarga del modelo

## Soporte de idiomas

vvrite utiliza [`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit), que es una conversión MLX de [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B). Según la ficha oficial del modelo Qwen, Qwen3-ASR-1.7B soporta identificación de idioma y reconocimiento de voz para 30 idiomas y 22 dialectos chinos.

Esto incluye coreano, inglés, japonés, chino, cantonés, árabe, alemán, francés, español, portugués, indonesio, italiano, ruso, tailandés, vietnamita, turco, hindi, malayo, neerlandés, sueco, danés, finlandés, polaco, checo, filipino, persa, griego, húngaro, macedonio y rumano, además de soporte para dialectos regionales chinos. Dado que vvrite usa ese punto de control directamente a través de mlx-audio y no fuerza un idioma de reconocimiento fijo, el dictado multilingüe funciona bien para los idiomas compatibles del modelo.

## Requisitos

- .app precompilada: macOS 15 o superior en Apple Silicon (M1/M2/M3/M4); compilación desde fuente: macOS 13+
- Aproximadamente 2 GB de espacio en disco para el modelo ASR
- `ffmpeg` instalado cuando se ejecuta desde el código fuente
- Permiso de micrófono
- Permiso de accesibilidad (para la tecla de acceso rápido global)

## Instalación

### Desde el código fuente

```bash
# Clonar
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# Instalar dependencias
pip install -r requirements.txt
brew install ffmpeg

# Ejecutar
python -m vvrite
```

### Compilar como .app

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh` es la ruta de compilación recomendada. Realiza la compilación con PyInstaller, firma de código, notarización, grapado y creación del DMG. Requiere una identidad de firma de Apple Developer configurada y un perfil de `notarytool`.

## Uso

| Acción | Atajo |
|---|---|
| Iniciar / detener grabación | `Option + Space` (configurable) |
| Cancelar grabación | `Escape` |
| Abrir ajustes | Clic en el ícono de la barra de menú → Ajustes |

En el primer inicio, el asistente de configuración te guiará a través de:
1. Otorgar permisos de micrófono y accesibilidad
2. Configurar tu tecla de acceso rápido preferida
3. Descargar el modelo ASR (aproximadamente 1.7 GB)

## Stack tecnológico

| Componente | Tecnología |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| Modelo ASR | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| Inferencia | [mlx-audio](https://github.com/ml-explore/mlx-audio) en GPU de Apple Silicon |
| Audio | sounddevice + ffmpeg |
| Empaquetado | PyInstaller |

## Licencia

MIT — consulta [LICENSE](LICENSE) para más detalles.

Esta aplicación incluye [ffmpeg](https://ffmpeg.org/), que está licenciado bajo la [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html). El código fuente de ffmpeg está disponible en https://ffmpeg.org/download.html. El modelo ASR [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) está licenciado bajo Apache 2.0.

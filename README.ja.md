<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="vvrite アイコン">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  音声を文字起こしし、テキストを貼り付けるmacOSメニューバーアプリ — オンデバイスAIで動作します。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · 日本語 · <a href="README.zh-Hans.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a>
</p>

---

## 仕組み

1. ホットキーを押します（デフォルト: `Option + Space`）
2. 話します — 画面に録音オーバーレイが表示されます
3. ホットキーをもう一度押して録音を停止します
4. 音声がローカルで文字起こしされ、アクティブなテキストフィールドに貼り付けられます

すべての処理は[MLX](https://github.com/ml-explore/mlx)を使用してデバイス上で行われます。音声データがMacの外に出ることはありません。
デフォルトモデルは強力な多言語音声認識をサポートしており、韓国語、英語、日本語、中国語、広東語、フランス語、ドイツ語、スペイン語などの対応言語がそのまま使用できます。

## 機能

- **オンデバイス文字起こし** — mlx-audioを通じてQwen3-ASRが動作し、クラウドAPIは不要です
- **多言語対応** — デフォルトのQwen3-ASRモデルは30言語と22の中国語方言の言語識別と文字起こしをサポートしており、vvriteは文字起こし言語を1つに固定しません
- **グローバルホットキー** — どのアプリからでも起動でき、設定で変更可能です
- **メニューバーアプリ** — ステータスバーに静かに常駐します
- **録音オーバーレイ** — オーディオレベルバーとタイマーで視覚的なフィードバックを提供します
- **ESCでキャンセル** — 録音中にEscapeを押すと文字起こしせずにキャンセルできます
- **自動貼り付け** — 文字起こしされたテキストがアクティブなフィールドに直接貼り付けられます
- **ガイド付きオンボーディング** — 初回起動時に権限設定とモデルのダウンロードを案内します

## 言語サポート

vvriteは[`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit)を使用しています。これは[`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)のMLX変換版です。公式Qwenモデルカードによると、Qwen3-ASR-1.7Bは30言語と22の中国語方言の言語識別と音声認識をサポートしています。

対応言語には、韓国語、英語、日本語、中国語、広東語、アラビア語、ドイツ語、フランス語、スペイン語、ポルトガル語、インドネシア語、イタリア語、ロシア語、タイ語、ベトナム語、トルコ語、ヒンディー語、マレー語、オランダ語、スウェーデン語、デンマーク語、フィンランド語、ポーランド語、チェコ語、フィリピン語、ペルシア語、ギリシャ語、ハンガリー語、マケドニア語、ルーマニア語が含まれ、中国語の地域方言もサポートされています。vvriteはこのチェックポイントをmlx-audioを通じて直接使用し、特定の認識言語を強制しないため、モデルがサポートする言語であれば多言語の音声入力が適切に機能します。

## 必要条件

- ビルド済み.appはApple Silicon（M1/M2/M3/M4）搭載のmacOS 15以上、ソースからビルドする場合はmacOS 13以上
- ASRモデル用のディスク容量約2 GB
- ソースから実行する場合は`ffmpeg`が必要
- マイクの権限
- アクセシビリティの権限（グローバルホットキー用）

## インストール

### ソースから実行

```bash
# クローン
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# 依存関係のインストール
pip install -r requirements.txt
brew install ffmpeg

# 実行
python -m vvrite
```

### .appとしてビルド

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh`がサポートされているビルド方法です。PyInstallerビルド、コード署名、公証、ステープリング、DMG作成を行います。設定済みのApple Developer署名IDと`notarytool`プロファイルが必要です。

## 使い方

| 操作 | ショートカット |
|---|---|
| 録音開始 / 停止 | `Option + Space`（変更可能） |
| 録音キャンセル | `Escape` |
| 設定を開く | メニューバーアイコンをクリック → 設定 |

初回起動時、オンボーディングウィザードが以下を案内します:
1. マイクとアクセシビリティの権限の付与
2. お好みのホットキーの設定
3. ASRモデルのダウンロード（約1.7 GB）

## 技術スタック

| コンポーネント | 技術 |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| ASRモデル | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| 推論 | Apple Silicon GPUで[mlx-audio](https://github.com/ml-explore/mlx-audio) |
| オーディオ | sounddevice + ffmpeg |
| パッケージング | PyInstaller |

## ライセンス

MIT — 詳細は[LICENSE](LICENSE)をご覧ください。

このアプリケーションは[GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)ライセンスの[ffmpeg](https://ffmpeg.org/)をバンドルしています。ffmpegのソースコードは https://ffmpeg.org/download.html から入手できます。ASRモデル[Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit)はApache 2.0ライセンスです。

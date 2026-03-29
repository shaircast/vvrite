<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="vvrite 圖示">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  將語音轉錄為文字並貼上的 macOS 選單列應用程式 — 由裝置端 AI 驅動。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja.md">日本語</a> · <a href="README.zh-Hans.md">简体中文</a> · 繁體中文 · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a>
</p>

---

## 運作方式

1. 按下快速鍵（預設：`Option + Space`）
2. 開始說話 — 螢幕上會顯示錄音浮動視窗
3. 再次按下快速鍵停止錄音
4. 語音在本機完成轉錄，並貼上到目前使用中的文字輸入欄位

所有處理皆透過 [MLX](https://github.com/ml-explore/mlx) 在裝置端完成。沒有任何音訊資料會離開你的 Mac。
預設模型具備強大的多語言語音辨識能力，韓語、英語、日語、中文、粵語、法語、德語、西班牙語等支援語言均可直接使用。

## 功能特色

- **裝置端轉錄** — 透過 mlx-audio 執行 Qwen3-ASR，無需雲端 API
- **多語言支援** — 預設的 Qwen3-ASR 模型支援 30 種語言和 22 種中文方言的語言辨識與轉錄，vvrite 不會將轉錄鎖定為單一語言
- **全域快速鍵** — 可在任何應用程式中觸發，可在設定中自訂
- **選單列應用程式** — 安靜地常駐在狀態列中
- **錄音浮動視窗** — 透過音訊電平條和計時器提供視覺回饋
- **ESC 取消** — 錄音時按 Escape 可直接取消，不進行轉錄
- **自動貼上** — 轉錄後的文字直接貼上到目前使用中的輸入欄位
- **引導式入門** — 首次啟動時引導你完成權限設定和模型下載

## 語言支援

vvrite 使用 [`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit)，這是 [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) 的 MLX 轉換版本。根據 Qwen 官方模型卡片，Qwen3-ASR-1.7B 支援 30 種語言和 22 種中文方言的語言辨識與語音辨識。

支援的語言包括韓語、英語、日語、中文、粵語、阿拉伯語、德語、法語、西班牙語、葡萄牙語、印尼語、義大利語、俄語、泰語、越南語、土耳其語、印地語、馬來語、荷蘭語、瑞典語、丹麥語、芬蘭語、波蘭語、捷克語、菲律賓語、波斯語、希臘語、匈牙利語、馬其頓語和羅馬尼亞語，同時還支援中文地方方言。vvrite 透過 mlx-audio 直接使用該模型檢查點，不強制指定辨識語言，因此模型支援的語言均可良好地進行多語言聽寫。

## 系統需求

- 預建 .app 需要搭載 Apple Silicon（M1/M2/M3/M4）的 macOS 15 或更高版本；從原始碼建置時 macOS 13 或更高版本
- ASR 模型需要約 2 GB 磁碟空間
- 從原始碼執行時需要安裝 `ffmpeg`
- 麥克風權限
- 輔助使用權限（用於全域快速鍵）

## 安裝

### 從原始碼執行

```bash
# 複製儲存庫
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# 安裝相依套件
pip install -r requirements.txt
brew install ffmpeg

# 執行
python -m vvrite
```

### 建置為 .app

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh` 是建議的建置方式。它會執行 PyInstaller 建置、程式碼簽章、公證、裝訂和 DMG 建立。需要已設定的 Apple Developer 簽章憑證和 `notarytool` 設定檔。

## 使用方式

| 操作 | 快速鍵 |
|---|---|
| 開始 / 停止錄音 | `Option + Space`（可自訂） |
| 取消錄音 | `Escape` |
| 開啟設定 | 點選選單列圖示 → 設定 |

首次啟動時，入門精靈將引導你完成以下步驟：
1. 授予麥克風和輔助使用權限
2. 設定你偏好的快速鍵
3. 下載 ASR 模型（約 1.7 GB）

## 技術堆疊

| 元件 | 技術 |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| ASR 模型 | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| 推論 | 在 Apple Silicon GPU 上執行 [mlx-audio](https://github.com/ml-explore/mlx-audio) |
| 音訊 | sounddevice + ffmpeg |
| 封裝 | PyInstaller |

## 授權條款

MIT — 詳情請參閱 [LICENSE](LICENSE)。

本應用程式捆綁了 [ffmpeg](https://ffmpeg.org/)，其遵循 [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) 授權條款。ffmpeg 原始碼可在 https://ffmpeg.org/download.html 取得。ASR 模型 [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) 遵循 Apache 2.0 授權條款。

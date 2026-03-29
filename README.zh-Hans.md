<p align="center">
  <img src="assets/icon.png" width="128" height="128" alt="vvrite 图标">
</p>

<h1 align="center">vvrite</h1>

<p align="center">
  将语音转录为文字并粘贴的 macOS 菜单栏应用 — 由端侧 AI 驱动。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS_(Apple_Silicon)-blue" alt="macOS">
  <img src="https://img.shields.io/badge/model-Qwen3--ASR--1.7B--8bit-green" alt="Model">
  <img src="https://img.shields.io/badge/runtime-MLX-orange" alt="MLX">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja.md">日本語</a> · 简体中文 · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a>
</p>

---

## 工作原理

1. 按下快捷键（默认：`Option + Space`）
2. 开始说话 — 屏幕上会显示录音悬浮窗
3. 再次按下快捷键停止录音
4. 语音在本地完成转录，并粘贴到当前活动的文本输入框中

所有处理均通过 [MLX](https://github.com/ml-explore/mlx) 在设备端完成。没有任何音频数据会离开你的 Mac。
默认模型具备强大的多语言语音识别能力，韩语、英语、日语、中文、粤语、法语、德语、西班牙语等支持语言均可开箱即用。

## 功能特性

- **端侧转录** — 通过 mlx-audio 运行 Qwen3-ASR，无需云端 API
- **多语言支持** — 默认的 Qwen3-ASR 模型支持 30 种语言和 22 种中文方言的语言识别与转录，vvrite 不会将转录锁定为单一语言
- **全局快捷键** — 可在任意应用中触发，可在设置中自定义
- **菜单栏应用** — 安静地驻留在状态栏中
- **录音悬浮窗** — 通过音频电平条和计时器提供视觉反馈
- **ESC 取消** — 录音时按 Escape 可直接取消，不进行转录
- **自动粘贴** — 转录后的文字直接粘贴到当前活动的输入框中
- **引导式入门** — 首次启动时引导你完成权限设置和模型下载

## 语言支持

vvrite 使用 [`mlx-community/Qwen3-ASR-1.7B-8bit`](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit)，这是 [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) 的 MLX 转换版本。根据 Qwen 官方模型卡片，Qwen3-ASR-1.7B 支持 30 种语言和 22 种中文方言的语言识别与语音识别。

支持的语言包括韩语、英语、日语、中文、粤语、阿拉伯语、德语、法语、西班牙语、葡萄牙语、印度尼西亚语、意大利语、俄语、泰语、越南语、土耳其语、印地语、马来语、荷兰语、瑞典语、丹麦语、芬兰语、波兰语、捷克语、菲律宾语、波斯语、希腊语、匈牙利语、马其顿语和罗马尼亚语，同时还支持中文地方方言。vvrite 通过 mlx-audio 直接使用该模型检查点，不强制指定识别语言，因此模型支持的语言均可良好地进行多语言听写。

## 系统要求

- 预构建 .app 需要搭载 Apple Silicon（M1/M2/M3/M4）的 macOS 15 或更高版本；从源代码构建时 macOS 13 或更高版本
- ASR 模型需要约 2 GB 磁盘空间
- 从源码运行时需要安装 `ffmpeg`
- 麦克风权限
- 辅助功能权限（用于全局快捷键）

## 安装

### 从源码运行

```bash
# 克隆仓库
git clone https://github.com/shaircast/vvrite.git
cd vvrite

# 安装依赖
pip install -r requirements.txt
brew install ffmpeg

# 运行
python -m vvrite
```

### 构建为 .app

```bash
pip install -r requirements.txt
./scripts/build.sh
open dist/vvrite.dmg
```

`./scripts/build.sh` 是推荐的构建方式。它会执行 PyInstaller 构建、代码签名、公证、装订和 DMG 创建。需要已配置的 Apple Developer 签名证书和 `notarytool` 配置文件。

## 使用方法

| 操作 | 快捷键 |
|---|---|
| 开始 / 停止录音 | `Option + Space`（可自定义） |
| 取消录音 | `Escape` |
| 打开设置 | 点击菜单栏图标 → 设置 |

首次启动时，入门向导将引导你完成以下步骤：
1. 授予麦克风和辅助功能权限
2. 设置你喜欢的快捷键
3. 下载 ASR 模型（约 1.7 GB）

## 技术栈

| 组件 | 技术 |
|---|---|
| UI | PyObjC (AppKit, Quartz) |
| ASR 模型 | [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) |
| 推理 | 在 Apple Silicon GPU 上运行 [mlx-audio](https://github.com/ml-explore/mlx-audio) |
| 音频 | sounddevice + ffmpeg |
| 打包 | PyInstaller |

## 许可证

MIT — 详情请参阅 [LICENSE](LICENSE)。

本应用捆绑了 [ffmpeg](https://ffmpeg.org/)，其遵循 [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) 许可证。ffmpeg 源代码可在 https://ffmpeg.org/download.html 获取。ASR 模型 [Qwen3-ASR-1.7B-8bit](https://huggingface.co/mlx-community/Qwen3-ASR-1.7B-8bit) 遵循 Apache 2.0 许可证。

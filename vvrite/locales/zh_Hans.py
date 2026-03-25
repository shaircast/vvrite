"""Chinese Simplified locale strings for vvrite."""

strings = {
    "common": {
        "grant": "授权",
        "retry": "重试",
        "dismiss": "关闭",
        "download": "下载",
        "later": "稍后",
        "back": "返回",
        "next": "下一步",
        "done": "完成",
        "open": "打开",
        "change": "更改",
        "ok": "OK",
        "system_default": "系统默认",
        "automatic": "自动",
        "get_started": "开始使用",
    },
    "status": {
        "ready": "就绪",
        "recording": "录音中...",
        "transcribing": "转录中...",
        "loading_model": "模型加载中...",
        "waiting_permissions": "等待权限...",
        "error_model": "错误：模型失败",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "语音转文字，即时完成。",
        },
        "language": {
            "title": "语言",
        },
        "permissions": {
            "title": "权限",
            "accessibility": "辅助功能",
            "accessibility_desc": "用于全局快捷键",
            "microphone": "麦克风",
            "microphone_desc": "用于语音录制",
            "granted": "已授权",
            "not_granted": "未授权",
        },
        "hotkey": {
            "title": "快捷键",
            "subtitle": "按下以开始/停止录音",
        },
        "retract": {
            "title": "快速更正",
            "subtitle": "使用全局快捷键可选择性地撤回上次听写",
            "enable": "启用撤回上次听写快捷键",
            "hint": "仅对最近一次听写结果生效一次",
        },
        "model": {
            "title": "模型",
            "checking_size": "正在检查大小...",
            "size_gb": "约 {size_gb:.1f} GB 下载",
            "size_unknown": "大小未知",
            "downloading": "下载中...",
            "loading": "模型加载中...",
            "ready": "模型已就绪！",
            "failed_after_retries": "3次尝试后模型加载失败",
        },
    },
    "settings": {
        "title": "设置",
        "language": {
            "title": "语言",
            "ui_language": "界面",
            "asr_language": "识别",
            "restart_message": "重启 vvrite 以应用语言更改。",
            "restart_now": "立即重启",
        },
        "shortcut": {
            "title": "快捷键",
        },
        "correction": {
            "title": "更正",
            "enable": "启用撤回上次听写快捷键",
            "hint": "删除最近粘贴的听写结果",
        },
        "microphone": {
            "title": "麦克风",
        },
        "model": {
            "title": "模型",
        },
        "custom_words": {
            "title": "自定义词汇",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "用逗号分隔的词汇，以提高识别准确度",
        },
        "sound": {
            "title": "声音",
            "start": "开始",
            "stop": "停止",
            "custom": "自定义...",
            "hint": "调整滑块会自动播放所选声音",
            "choose_file": "选择声音文件",
        },
        "permissions": {
            "title": "权限",
            "accessibility_checking": "辅助功能：检查中...",
            "microphone_checking": "麦克风：检查中...",
            "accessibility_granted": "辅助功能：✅ 已授权",
            "accessibility_not_granted": "辅助功能：❌ 未授权",
            "microphone_granted": "麦克风：✅ 已授权",
        },
        "login": {
            "title": "登录时启动",
            "error": "无法更新登录时启动设置",
        },
        "update": {
            "title": "自动检查更新",
        },
    },
    "menu": {
        "hotkey": "快捷键：{hotkey}",
        "microphone": "麦克风：{microphone}",
        "settings": "设置...",
        "check_updates": "检查更新...",
        "update_available": "有可用更新 ({version})",
        "quit": "退出 vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "需要权限",
            "message": "vvrite 需要以下权限：\n\n{permissions}\n\n点击\u201c授权\u201d打开每个权限对话框。",
            "accessibility": "辅助功能（用于全局快捷键）",
            "microphone": "麦克风（用于语音录制）",
        },
        "model_failed": {
            "title": "模型加载失败",
        },
        "no_updates": {
            "title": "没有可用更新",
            "message": "vvrite {version} 已是最新版本。",
        },
        "update_available": {
            "title": "vvrite {version} 可用",
            "message": "您当前正在运行 {current_version}。",
        },
    },
    "overlay": {
        "transcribing": "转录中...",
    },
    "widgets": {
        "press_shortcut": "请按快捷键...",
    },
}

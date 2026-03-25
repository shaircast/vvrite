"""Chinese Traditional locale strings for vvrite."""

strings = {
    "common": {
        "grant": "授權",
        "retry": "重試",
        "dismiss": "關閉",
        "download": "下載",
        "later": "稍後",
        "back": "返回",
        "next": "下一步",
        "done": "完成",
        "open": "開啟",
        "change": "變更",
        "ok": "OK",
        "system_default": "系統預設",
        "automatic": "自動",
        "get_started": "開始使用",
    },
    "status": {
        "ready": "就緒",
        "recording": "錄音中...",
        "transcribing": "轉錄中...",
        "loading_model": "模型載入中...",
        "waiting_permissions": "等待權限...",
        "error_model": "錯誤：模型失敗",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "語音轉文字，即時完成。",
        },
        "language": {
            "title": "語言",
        },
        "permissions": {
            "title": "權限",
            "accessibility": "輔助使用",
            "accessibility_desc": "用於全域快捷鍵",
            "microphone": "麥克風",
            "microphone_desc": "用於語音錄製",
            "granted": "已授權",
            "not_granted": "未授權",
        },
        "hotkey": {
            "title": "快捷鍵",
            "subtitle": "按下以開始/停止錄音",
        },
        "retract": {
            "title": "快速更正",
            "subtitle": "使用全域快捷鍵可選擇性地撤回上次聽寫",
            "enable": "啟用撤回上次聽寫快捷鍵",
            "hint": "僅對最近一次聽寫結果生效一次",
        },
        "model": {
            "title": "模型",
            "checking_size": "正在檢查大小...",
            "size_gb": "約 {size_gb:.1f} GB 下載",
            "size_unknown": "大小未知",
            "downloading": "下載中...",
            "loading": "模型載入中...",
            "ready": "模型已就緒！",
            "failed_after_retries": "3次嘗試後模型載入失敗",
        },
    },
    "settings": {
        "title": "設定",
        "language": {
            "title": "語言",
            "ui_language": "介面",
            "asr_language": "辨識",
            "restart_message": "重新啟動 vvrite 以套用語言變更。",
            "restart_now": "立即重新啟動",
        },
        "shortcut": {
            "title": "快捷鍵",
        },
        "correction": {
            "title": "更正",
            "enable": "啟用撤回上次聽寫快捷鍵",
            "hint": "刪除最近貼上的聽寫結果",
        },
        "microphone": {
            "title": "麥克風",
        },
        "model": {
            "title": "模型",
        },
        "custom_words": {
            "title": "自訂詞彙",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "以逗號分隔的詞彙，以提高辨識準確度",
        },
        "sound": {
            "title": "聲音",
            "start": "開始",
            "stop": "停止",
            "custom": "自訂...",
            "hint": "調整滑桿會自動播放所選聲音",
            "choose_file": "選擇聲音檔案",
        },
        "permissions": {
            "title": "權限",
            "accessibility_checking": "輔助使用：檢查中...",
            "microphone_checking": "麥克風：檢查中...",
            "accessibility_granted": "輔助使用：✅ 已授權",
            "accessibility_not_granted": "輔助使用：❌ 未授權",
            "microphone_granted": "麥克風：✅ 已授權",
        },
        "login": {
            "title": "登入時啟動",
            "error": "無法更新登入時啟動設定",
        },
        "update": {
            "title": "自動檢查更新",
        },
    },
    "menu": {
        "hotkey": "快捷鍵：{hotkey}",
        "microphone": "麥克風：{microphone}",
        "settings": "設定...",
        "check_updates": "檢查更新...",
        "update_available": "有可用更新 ({version})",
        "quit": "結束 vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "需要權限",
            "message": "vvrite 需要以下權限：\n\n{permissions}\n\n點擊「授權」開啟每個權限對話框。",
            "accessibility": "輔助使用（用於全域快捷鍵）",
            "microphone": "麥克風（用於語音錄製）",
        },
        "model_failed": {
            "title": "模型載入失敗",
        },
        "no_updates": {
            "title": "沒有可用更新",
            "message": "vvrite {version} 已是最新版本。",
        },
        "update_available": {
            "title": "vvrite {version} 可用",
            "message": "您目前正在執行 {current_version}。",
        },
    },
    "overlay": {
        "transcribing": "轉錄中...",
    },
    "widgets": {
        "press_shortcut": "請按快捷鍵...",
    },
}

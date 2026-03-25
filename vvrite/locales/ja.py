"""Japanese locale strings for vvrite."""

strings = {
    "common": {
        "grant": "許可",
        "retry": "再試行",
        "dismiss": "閉じる",
        "download": "ダウンロード",
        "later": "後で",
        "back": "戻る",
        "next": "次へ",
        "done": "完了",
        "open": "開く",
        "change": "変更",
        "ok": "OK",
        "system_default": "システムデフォルト",
        "automatic": "自動",
        "get_started": "はじめる",
    },
    "status": {
        "ready": "準備完了",
        "recording": "録音中...",
        "transcribing": "文字起こし中...",
        "loading_model": "モデル読み込み中...",
        "waiting_permissions": "権限を待機中...",
        "error_model": "エラー: モデル失敗",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "音声をテキストに、瞬時に。",
        },
        "language": {
            "title": "言語",
        },
        "permissions": {
            "title": "権限",
            "accessibility": "アクセシビリティ",
            "accessibility_desc": "グローバルホットキー用",
            "microphone": "マイク",
            "microphone_desc": "音声録音用",
            "granted": "許可済み",
            "not_granted": "未許可",
        },
        "hotkey": {
            "title": "ホットキー",
            "subtitle": "押して録音の開始/停止",
        },
        "retract": {
            "title": "クイック修正",
            "subtitle": "グローバルショートカットで直前のディクテーションを取り消し",
            "enable": "直前のディクテーション取り消しショートカットを有効にする",
            "hint": "最新のディクテーション結果に対して一度だけ機能します",
        },
        "model": {
            "title": "モデル",
            "checking_size": "サイズを確認中...",
            "size_gb": "約{size_gb:.1f} GBのダウンロード",
            "size_unknown": "サイズ不明",
            "downloading": "ダウンロード中...",
            "loading": "モデル読み込み中...",
            "ready": "モデル準備完了！",
            "failed_after_retries": "3回の試行後、モデルの読み込みに失敗しました",
        },
    },
    "settings": {
        "title": "設定",
        "language": {
            "title": "言語",
            "ui_language": "UI",
            "asr_language": "認識",
            "restart_message": "言語の変更を適用するにはvvriteを再起動してください。",
            "restart_now": "今すぐ再起動",
        },
        "shortcut": {
            "title": "ショートカット",
        },
        "correction": {
            "title": "修正",
            "enable": "直前のディクテーション取り消しショートカットを有効にする",
            "hint": "最後に貼り付けたディクテーション結果を削除します",
        },
        "microphone": {
            "title": "マイク",
        },
        "model": {
            "title": "モデル",
        },
        "custom_words": {
            "title": "カスタムワード",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "認識精度を向上させるためのカンマ区切りの単語",
        },
        "sound": {
            "title": "サウンド",
            "start": "開始",
            "stop": "停止",
            "custom": "カスタム...",
            "hint": "スライダーを調整すると選択したサウンドが自動再生されます",
            "choose_file": "サウンドファイルを選択",
        },
        "permissions": {
            "title": "権限",
            "accessibility_checking": "アクセシビリティ: 確認中...",
            "microphone_checking": "マイク: 確認中...",
            "accessibility_granted": "アクセシビリティ: ✅ 許可済み",
            "accessibility_not_granted": "アクセシビリティ: ❌ 未許可",
            "microphone_granted": "マイク: ✅ 許可済み",
        },
        "login": {
            "title": "ログイン時に起動",
            "error": "ログイン時の起動を更新できませんでした",
        },
        "update": {
            "title": "自動的にアップデートを確認",
        },
    },
    "menu": {
        "hotkey": "ホットキー: {hotkey}",
        "microphone": "マイク: {microphone}",
        "settings": "設定...",
        "check_updates": "アップデートを確認...",
        "update_available": "アップデートあり ({version})",
        "quit": "vvriteを終了",
    },
    "alerts": {
        "permissions_required": {
            "title": "権限が必要です",
            "message": "vvriteには以下の権限が必要です:\n\n{permissions}\n\n「許可」をクリックして各権限ダイアログを開いてください。",
            "accessibility": "アクセシビリティ（グローバルホットキー用）",
            "microphone": "マイク（音声録音用）",
        },
        "model_failed": {
            "title": "モデルの読み込みに失敗しました",
        },
        "no_updates": {
            "title": "利用可能なアップデートはありません",
            "message": "vvrite {version}は最新バージョンです。",
        },
        "update_available": {
            "title": "vvrite {version}が利用可能です",
            "message": "現在{current_version}を実行中です。",
        },
    },
    "overlay": {
        "transcribing": "文字起こし中...",
    },
    "widgets": {
        "press_shortcut": "ショートカットを押してください...",
    },
}

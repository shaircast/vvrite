"""English locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Grant",
        "retry": "Retry",
        "dismiss": "Dismiss",
        "download": "Download",
        "later": "Later",
        "back": "Back",
        "next": "Next",
        "done": "Done",
        "open": "Open",
        "change": "Change",
        "ok": "OK",
        "system_default": "System Default",
        "automatic": "Automatic",
        "get_started": "Get Started",
    },
    "status": {
        "ready": "Ready",
        "recording": "Recording...",
        "transcribing": "Transcribing...",
        "loading_model": "Loading model...",
        "waiting_permissions": "Waiting for permissions...",
        "error_model": "Error: model failed",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Voice to text, instantly.",
        },
        "language": {
            "title": "Language",
        },
        "permissions": {
            "title": "Permissions",
            "accessibility": "Accessibility",
            "accessibility_desc": "For global hotkey",
            "microphone": "Microphone",
            "microphone_desc": "For voice recording",
            "granted": "Granted",
            "not_granted": "Not Granted",
        },
        "hotkey": {
            "title": "Hotkey",
            "subtitle": "Press to start/stop recording",
        },
        "retract": {
            "title": "Quick Correction",
            "subtitle": "Optionally remove the last dictation with a global shortcut",
            "enable": "Enable retract last dictation shortcut",
            "hint": "Works once for the most recent dictation result",
        },
        "model": {
            "title": "Model",
            "checking_size": "Checking size...",
            "size_gb": "~{size_gb:.1f} GB download",
            "size_unknown": "Size unknown",
            "downloading": "Downloading...",
            "loading": "Loading model...",
            "ready": "Model ready!",
            "failed_after_retries": "Model loading failed after 3 attempts",
        },
    },
    "settings": {
        "title": "Settings",
        "language": {
            "title": "Language",
            "ui_language": "UI",
            "asr_language": "Recognition",
            "restart_message": "Restart vvrite to apply language changes.",
            "restart_now": "Restart Now",
        },
        "shortcut": {
            "title": "Shortcut",
        },
        "correction": {
            "title": "Correction",
            "enable": "Enable retract last dictation shortcut",
            "hint": "Deletes the most recently pasted dictation result",
        },
        "microphone": {
            "title": "Microphone",
        },
        "model": {
            "title": "Model",
        },
        "custom_words": {
            "title": "Custom Words",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Comma-separated words to help recognition accuracy",
        },
        "sound": {
            "title": "Sound",
            "start": "Start",
            "stop": "Stop",
            "custom": "Custom...",
            "hint": "Adjusting the slider automatically plays the selected sound",
            "choose_file": "Choose a sound file",
        },
        "permissions": {
            "title": "Permissions",
            "accessibility_checking": "Accessibility: checking...",
            "microphone_checking": "Microphone: checking...",
            "accessibility_granted": "Accessibility: \u2705 Granted",
            "accessibility_not_granted": "Accessibility: \u274c Not Granted",
            "microphone_granted": "Microphone: \u2705 Granted",
        },
        "login": {
            "title": "Launch at login",
            "error": "Launch at login could not be updated",
        },
        "update": {
            "title": "Automatically check for updates",
        },
    },
    "menu": {
        "hotkey": "Hotkey: {hotkey}",
        "microphone": "Microphone: {microphone}",
        "settings": "Settings...",
        "check_updates": "Check for Updates...",
        "update_available": "Update Available ({version})",
        "quit": "Quit vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "Permissions Required",
            "message": "vvrite needs the following permissions:\n\n{permissions}\n\nClick 'Grant' to open each permission dialog.",
            "accessibility": "Accessibility (for global hotkey)",
            "microphone": "Microphone (for voice recording)",
        },
        "model_failed": {
            "title": "Model Loading Failed",
        },
        "no_updates": {
            "title": "No Updates Available",
            "message": "vvrite {version} is the latest version.",
        },
        "update_available": {
            "title": "vvrite {version} is available",
            "message": "You are currently running {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "Transcribing...",
    },
    "widgets": {
        "press_shortcut": "Press shortcut...",
    },
}

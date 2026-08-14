"""German locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Erlauben",
        "retry": "Erneut versuchen",
        "dismiss": "Schließen",
        "download": "Herunterladen",
        "later": "Später",
        "back": "Zurück",
        "next": "Weiter",
        "done": "Fertig",
        "open": "Öffnen",
        "change": "Ändern",
        "ok": "OK",
        "system_default": "Systemstandard",
        "automatic": "Automatisch",
        "get_started": "Loslegen",
    },
    "status": {
        "ready": "Bereit",
        "recording": "Aufnahme...",
        "transcribing": "Transkribieren...",
        "loading_model": "Modell wird geladen...",
        "waiting_permissions": "Warte auf Berechtigungen...",
        "error_model": "Fehler: Modell fehlgeschlagen",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Sprache zu Text, sofort.",
        },
        "language": {
            "title": "Sprache",
        },
        "permissions": {
            "title": "Berechtigungen",
            "accessibility": "Bedienungshilfen",
            "accessibility_desc": "Für globale Tastenkombination",
            "drag_hint": "Ziehe dieses Element in die Bedienungshilfen-Liste.",
            "microphone": "Mikrofon",
            "microphone_desc": "Für Sprachaufnahme",
            "granted": "Erteilt",
            "not_granted": "Nicht erteilt",
        },
        "hotkey": {
            "title": "Tastenkombination",
            "subtitle": "Drücken zum Starten/Stoppen der Aufnahme",
        },
        "retract": {
            "title": "Schnellkorrektur",
            "subtitle": "Letzte Diktierung optional mit globalem Tastenkürzel entfernen",
            "enable": "Tastenkürzel zum Widerrufen der letzten Diktierung aktivieren",
            "hint": "Funktioniert einmalig für das letzte Diktierergebnis",
        },
        "model": {
            "title": "Modell",
            "checking_size": "Größe wird überprüft...",
            "size_gb": "~{size_gb:.1f} GB Download",
            "size_unknown": "Größe unbekannt",
            "downloading": "Wird heruntergeladen...",
            "loading": "Modell wird geladen...",
            "ready": "Modell bereit!",
            "failed_after_retries": "Modell-Laden nach 3 Versuchen fehlgeschlagen",
        },
    },
    "settings": {
        "title": "Einstellungen",
        "language": {
            "title": "Sprache",
            "ui_language": "Oberfläche",
            "asr_language": "Erkennung",
            "restart_message": "Starten Sie vvrite neu, um die Sprachänderungen zu übernehmen.",
            "restart_now": "Jetzt neu starten",
        },
        "shortcut": {
            "title": "Tastenkürzel",
        },
        "tabs": {
            "general": "Allgemein",
            "audio": "Audio",
            "language": "Sprache",
            "system": "System",
        },
        "recording": {
            "title": "Aufnahmemodus",
            "mode": "Modus",
            "toggle": "Umschalten",
            "push_to_talk": "Push-to-Talk",
            "toggle_shortcut": "Tastenkürzel",
            "ptt_shortcut": "Push-to-Talk-Taste",
            "toggle_hint": "Einmal drücken zum Starten, erneut drücken zum Stoppen.",
            "ptt_hint": "Taste gedrückt halten zum Aufnehmen, loslassen zum Transkribieren.",
        },
        "startup": {
            "title": "Start & Updates",
        },
        "correction": {
            "title": "Korrektur",
            "enable": "Tastenkürzel zum Widerrufen der letzten Diktierung aktivieren",
            "hint": "Löscht das zuletzt eingefügte Diktierergebnis",
        },
        "microphone": {
            "title": "Mikrofon",
        },
        "model": {
            "title": "Modell",
        },
        "custom_words": {
            "title": "Benutzerdefinierte Wörter",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Kommagetrennte Wörter zur Verbesserung der Erkennungsgenauigkeit",
        },
        "sound": {
            "title": "Ton",
            "start": "Start",
            "stop": "Stopp",
            "custom": "Benutzerdefiniert...",
            "hint": "Beim Anpassen des Reglers wird der ausgewählte Ton automatisch abgespielt",
            "choose_file": "Audiodatei auswählen",
        },
        "permissions": {
            "title": "Berechtigungen",
            "accessibility_checking": "Bedienungshilfen: wird überprüft...",
            "microphone_checking": "Mikrofon: wird überprüft...",
            "accessibility_granted": "Bedienungshilfen: ✅ Erteilt",
            "accessibility_not_granted": "Bedienungshilfen: ❌ Nicht erteilt",
            "microphone_granted": "Mikrofon: ✅ Erteilt",
            "microphone_not_granted": "Mikrofon: ❌ Nicht erteilt",
        },
        "login": {
            "title": "Beim Anmelden starten",
            "error": "Automatischer Start konnte nicht aktualisiert werden",
        },
        "update": {
            "title": "Automatisch nach Updates suchen",
        },
    },
    "menu": {
        "hotkey": "Tastenkürzel: {hotkey}",
        "microphone": "Mikrofon: {microphone}",
        "settings": "Einstellungen...",
        "check_updates": "Nach Updates suchen...",
        "quit": "vvrite beenden",
    },
    "alerts": {
        "permissions_required": {
            "title": "Berechtigungen erforderlich",
            "message": "vvrite benötigt folgende Berechtigungen:\n\n{permissions}\n\nKlicken Sie auf \u201EErlauben\u201C, um jeden Berechtigungsdialog zu \u00F6ffnen.",
            "accessibility": "Bedienungshilfen (für globale Tastenkombination)",
            "microphone": "Mikrofon (für Sprachaufnahme)",
        },
        "model_failed": {
            "title": "Modell-Laden fehlgeschlagen",
        },
    },
    "overlay": {
        "transcribing": "Transkribieren...",
    },
    "widgets": {
        "press_shortcut": "Tastenkürzel drücken...",
    },
}

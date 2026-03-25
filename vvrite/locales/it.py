"""Italian locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Concedi",
        "retry": "Riprova",
        "dismiss": "Chiudi",
        "download": "Scarica",
        "later": "Più tardi",
        "back": "Indietro",
        "next": "Avanti",
        "done": "Fatto",
        "open": "Apri",
        "change": "Modifica",
        "ok": "OK",
        "system_default": "Predefinito di sistema",
        "automatic": "Automatico",
        "get_started": "Inizia",
    },
    "status": {
        "ready": "Pronto",
        "recording": "Registrazione...",
        "transcribing": "Trascrizione...",
        "loading_model": "Caricamento modello...",
        "waiting_permissions": "In attesa dei permessi...",
        "error_model": "Errore: modello fallito",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Dalla voce al testo, istantaneamente.",
        },
        "language": {
            "title": "Lingua",
        },
        "permissions": {
            "title": "Permessi",
            "accessibility": "Accessibilità",
            "accessibility_desc": "Per la scorciatoia globale",
            "microphone": "Microfono",
            "microphone_desc": "Per la registrazione vocale",
            "granted": "Concesso",
            "not_granted": "Non concesso",
        },
        "hotkey": {
            "title": "Tasto rapido",
            "subtitle": "Premi per avviare/interrompere la registrazione",
        },
        "retract": {
            "title": "Correzione rapida",
            "subtitle": "Rimuovi opzionalmente l'ultima dettatura con una scorciatoia globale",
            "enable": "Abilita scorciatoia per ritirare l'ultima dettatura",
            "hint": "Funziona una volta per il risultato di dettatura più recente",
        },
        "model": {
            "title": "Modello",
            "checking_size": "Verifica dimensione...",
            "size_gb": "~{size_gb:.1f} GB da scaricare",
            "size_unknown": "Dimensione sconosciuta",
            "downloading": "Download in corso...",
            "loading": "Caricamento modello...",
            "ready": "Modello pronto!",
            "failed_after_retries": "Caricamento del modello fallito dopo 3 tentativi",
        },
    },
    "settings": {
        "title": "Impostazioni",
        "language": {
            "title": "Lingua",
            "ui_language": "Interfaccia",
            "asr_language": "Riconoscimento",
            "restart_message": "Riavvia vvrite per applicare le modifiche alla lingua.",
            "restart_now": "Riavvia ora",
        },
        "shortcut": {
            "title": "Scorciatoia",
        },
        "correction": {
            "title": "Correzione",
            "enable": "Abilita scorciatoia per ritirare l'ultima dettatura",
            "hint": "Elimina il risultato di dettatura incollato più di recente",
        },
        "microphone": {
            "title": "Microfono",
        },
        "model": {
            "title": "Modello",
        },
        "custom_words": {
            "title": "Parole personalizzate",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Parole separate da virgola per migliorare la precisione del riconoscimento",
        },
        "sound": {
            "title": "Suono",
            "start": "Avvio",
            "stop": "Arresto",
            "custom": "Personalizzato...",
            "hint": "Regolando il cursore viene riprodotto automaticamente il suono selezionato",
            "choose_file": "Scegli un file audio",
        },
        "permissions": {
            "title": "Permessi",
            "accessibility_checking": "Accessibilità: verifica in corso...",
            "microphone_checking": "Microfono: verifica in corso...",
            "accessibility_granted": "Accessibilità: ✅ Concesso",
            "accessibility_not_granted": "Accessibilità: ❌ Non concesso",
            "microphone_granted": "Microfono: ✅ Concesso",
        },
        "login": {
            "title": "Avvia al login",
            "error": "Impossibile aggiornare l'avvio al login",
        },
        "update": {
            "title": "Controlla automaticamente gli aggiornamenti",
        },
    },
    "menu": {
        "hotkey": "Tasto rapido: {hotkey}",
        "microphone": "Microfono: {microphone}",
        "settings": "Impostazioni...",
        "check_updates": "Controlla aggiornamenti...",
        "update_available": "Aggiornamento disponibile ({version})",
        "quit": "Esci da vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "Permessi necessari",
            "message": "vvrite necessita dei seguenti permessi:\n\n{permissions}\n\nFai clic su 'Concedi' per aprire ogni finestra di dialogo dei permessi.",
            "accessibility": "Accessibilità (per la scorciatoia globale)",
            "microphone": "Microfono (per la registrazione vocale)",
        },
        "model_failed": {
            "title": "Caricamento del modello fallito",
        },
        "no_updates": {
            "title": "Nessun aggiornamento disponibile",
            "message": "vvrite {version} è la versione più recente.",
        },
        "update_available": {
            "title": "vvrite {version} è disponibile",
            "message": "Stai attualmente utilizzando {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "Trascrizione...",
    },
    "widgets": {
        "press_shortcut": "Premi una scorciatoia...",
    },
}

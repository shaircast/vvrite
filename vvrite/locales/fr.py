"""French locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Autoriser",
        "retry": "Réessayer",
        "dismiss": "Fermer",
        "download": "Télécharger",
        "later": "Plus tard",
        "back": "Retour",
        "next": "Suivant",
        "done": "Terminé",
        "open": "Ouvrir",
        "change": "Modifier",
        "ok": "OK",
        "system_default": "Par défaut du système",
        "automatic": "Automatique",
        "get_started": "Commencer",
    },
    "status": {
        "ready": "Prêt",
        "recording": "Enregistrement...",
        "transcribing": "Transcription...",
        "loading_model": "Chargement du modèle...",
        "waiting_permissions": "En attente des autorisations...",
        "error_model": "Erreur : échec du modèle",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "De la voix au texte, instantanément.",
        },
        "language": {
            "title": "Langue",
        },
        "permissions": {
            "title": "Autorisations",
            "accessibility": "Accessibilité",
            "accessibility_desc": "Pour le raccourci global",
            "microphone": "Microphone",
            "microphone_desc": "Pour l'enregistrement vocal",
            "granted": "Accordé",
            "not_granted": "Non accordé",
        },
        "hotkey": {
            "title": "Raccourci",
            "subtitle": "Appuyez pour démarrer/arrêter l'enregistrement",
        },
        "retract": {
            "title": "Correction rapide",
            "subtitle": "Supprimez la dernière dictée avec un raccourci global",
            "enable": "Activer le raccourci de retrait de la dernière dictée",
            "hint": "Fonctionne une seule fois pour le résultat de dictée le plus récent",
        },
        "model": {
            "title": "Modèle",
            "checking_size": "Vérification de la taille...",
            "size_gb": "~{size_gb:.1f} Go à télécharger",
            "size_unknown": "Taille inconnue",
            "downloading": "Téléchargement...",
            "loading": "Chargement du modèle...",
            "ready": "Modèle prêt !",
            "failed_after_retries": "Le chargement du modèle a échoué après 3 tentatives",
        },
    },
    "settings": {
        "title": "Réglages",
        "language": {
            "title": "Langue",
            "ui_language": "Interface",
            "asr_language": "Reconnaissance",
            "restart_message": "Redémarrez vvrite pour appliquer les changements de langue.",
            "restart_now": "Redémarrer maintenant",
        },
        "shortcut": {
            "title": "Raccourci",
        },
        "correction": {
            "title": "Correction",
            "enable": "Activer le raccourci de retrait de la dernière dictée",
            "hint": "Supprime le résultat de dictée collé le plus récemment",
        },
        "microphone": {
            "title": "Microphone",
        },
        "model": {
            "title": "Modèle",
        },
        "custom_words": {
            "title": "Mots personnalisés",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Mots séparés par des virgules pour améliorer la précision de la reconnaissance",
        },
        "sound": {
            "title": "Son",
            "start": "Démarrer",
            "stop": "Arrêter",
            "custom": "Personnalisé...",
            "hint": "Ajuster le curseur joue automatiquement le son sélectionné",
            "choose_file": "Choisir un fichier audio",
        },
        "permissions": {
            "title": "Autorisations",
            "accessibility_checking": "Accessibilité : vérification...",
            "microphone_checking": "Microphone : vérification...",
            "accessibility_granted": "Accessibilité : ✅ Accordé",
            "accessibility_not_granted": "Accessibilité : ❌ Non accordé",
            "microphone_granted": "Microphone : ✅ Accordé",
        },
        "login": {
            "title": "Lancer au démarrage",
            "error": "Impossible de mettre à jour le lancement au démarrage",
        },
        "update": {
            "title": "Vérifier automatiquement les mises à jour",
        },
    },
    "menu": {
        "hotkey": "Raccourci : {hotkey}",
        "microphone": "Microphone : {microphone}",
        "settings": "Réglages...",
        "check_updates": "Vérifier les mises à jour...",
        "update_available": "Mise à jour disponible ({version})",
        "quit": "Quitter vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "Autorisations requises",
            "message": "vvrite a besoin des autorisations suivantes :\n\n{permissions}\n\nCliquez sur « Autoriser » pour ouvrir chaque dialogue d'autorisation.",
            "accessibility": "Accessibilité (pour le raccourci global)",
            "microphone": "Microphone (pour l'enregistrement vocal)",
        },
        "model_failed": {
            "title": "Échec du chargement du modèle",
        },
        "no_updates": {
            "title": "Aucune mise à jour disponible",
            "message": "vvrite {version} est la dernière version.",
        },
        "update_available": {
            "title": "vvrite {version} est disponible",
            "message": "Vous utilisez actuellement {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "Transcription...",
    },
    "widgets": {
        "press_shortcut": "Appuyez sur un raccourci...",
    },
}

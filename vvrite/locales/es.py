"""Spanish locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Conceder",
        "retry": "Reintentar",
        "dismiss": "Cerrar",
        "download": "Descargar",
        "later": "Más tarde",
        "back": "Atrás",
        "next": "Siguiente",
        "done": "Listo",
        "open": "Abrir",
        "change": "Cambiar",
        "ok": "OK",
        "system_default": "Predeterminado del sistema",
        "automatic": "Automático",
        "get_started": "Comenzar",
    },
    "status": {
        "ready": "Listo",
        "recording": "Grabando...",
        "transcribing": "Transcribiendo...",
        "loading_model": "Cargando modelo...",
        "waiting_permissions": "Esperando permisos...",
        "error_model": "Error: modelo fallido",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Voz a texto, al instante.",
        },
        "language": {
            "title": "Idioma",
        },
        "permissions": {
            "title": "Permisos",
            "accessibility": "Accesibilidad",
            "accessibility_desc": "Para tecla de acceso rápido global",
            "microphone": "Micrófono",
            "microphone_desc": "Para grabación de voz",
            "granted": "Concedido",
            "not_granted": "No concedido",
        },
        "hotkey": {
            "title": "Tecla de acceso rápido",
            "subtitle": "Presiona para iniciar/detener la grabación",
        },
        "retract": {
            "title": "Corrección rápida",
            "subtitle": "Elimina opcionalmente el último dictado con un atajo global",
            "enable": "Activar atajo para retractar último dictado",
            "hint": "Funciona una vez para el resultado de dictado más reciente",
        },
        "model": {
            "title": "Modelo",
            "checking_size": "Verificando tamaño...",
            "size_gb": "~{size_gb:.1f} GB de descarga",
            "size_unknown": "Tamaño desconocido",
            "downloading": "Descargando...",
            "loading": "Cargando modelo...",
            "ready": "¡Modelo listo!",
            "failed_after_retries": "La carga del modelo falló después de 3 intentos",
        },
    },
    "settings": {
        "title": "Ajustes",
        "language": {
            "title": "Idioma",
            "ui_language": "Interfaz",
            "asr_language": "Reconocimiento",
            "restart_message": "Reinicia vvrite para aplicar los cambios de idioma.",
            "restart_now": "Reiniciar ahora",
        },
        "shortcut": {
            "title": "Atajo",
        },
        "correction": {
            "title": "Corrección",
            "enable": "Activar atajo para retractar último dictado",
            "hint": "Elimina el resultado de dictado pegado más recientemente",
        },
        "microphone": {
            "title": "Micrófono",
        },
        "model": {
            "title": "Modelo",
        },
        "custom_words": {
            "title": "Palabras personalizadas",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Palabras separadas por comas para mejorar la precisión del reconocimiento",
        },
        "sound": {
            "title": "Sonido",
            "start": "Inicio",
            "stop": "Detener",
            "custom": "Personalizado...",
            "hint": "Ajustar el deslizador reproduce automáticamente el sonido seleccionado",
            "choose_file": "Elegir un archivo de sonido",
        },
        "permissions": {
            "title": "Permisos",
            "accessibility_checking": "Accesibilidad: verificando...",
            "microphone_checking": "Micrófono: verificando...",
            "accessibility_granted": "Accesibilidad: ✅ Concedido",
            "accessibility_not_granted": "Accesibilidad: ❌ No concedido",
            "microphone_granted": "Micrófono: ✅ Concedido",
        },
        "login": {
            "title": "Iniciar al iniciar sesión",
            "error": "No se pudo actualizar el inicio de sesión automático",
        },
        "update": {
            "title": "Buscar actualizaciones automáticamente",
        },
    },
    "menu": {
        "hotkey": "Atajo: {hotkey}",
        "microphone": "Micrófono: {microphone}",
        "settings": "Ajustes...",
        "check_updates": "Buscar actualizaciones...",
        "update_available": "Actualización disponible ({version})",
        "quit": "Salir de vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "Permisos requeridos",
            "message": "vvrite necesita los siguientes permisos:\n\n{permissions}\n\nHaz clic en 'Conceder' para abrir cada diálogo de permisos.",
            "accessibility": "Accesibilidad (para tecla de acceso rápido global)",
            "microphone": "Micrófono (para grabación de voz)",
        },
        "model_failed": {
            "title": "Error al cargar el modelo",
        },
        "no_updates": {
            "title": "No hay actualizaciones disponibles",
            "message": "vvrite {version} es la última versión.",
        },
        "update_available": {
            "title": "vvrite {version} está disponible",
            "message": "Actualmente estás ejecutando {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "Transcribiendo...",
    },
    "widgets": {
        "press_shortcut": "Presiona un atajo...",
    },
}

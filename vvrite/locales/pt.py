"""Portuguese locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Conceder",
        "retry": "Tentar novamente",
        "dismiss": "Fechar",
        "download": "Baixar",
        "later": "Mais tarde",
        "back": "Voltar",
        "next": "Próximo",
        "done": "Concluído",
        "open": "Abrir",
        "change": "Alterar",
        "ok": "OK",
        "system_default": "Padrão do sistema",
        "automatic": "Automático",
        "get_started": "Começar",
    },
    "status": {
        "ready": "Pronto",
        "recording": "Gravando...",
        "transcribing": "Transcrevendo...",
        "loading_model": "Carregando modelo...",
        "waiting_permissions": "Aguardando permissões...",
        "error_model": "Erro: falha no modelo",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Voz para texto, instantaneamente.",
        },
        "language": {
            "title": "Idioma",
        },
        "permissions": {
            "title": "Permissões",
            "accessibility": "Acessibilidade",
            "accessibility_desc": "Para atalho global",
            "microphone": "Microfone",
            "microphone_desc": "Para gravação de voz",
            "granted": "Concedido",
            "not_granted": "Não concedido",
        },
        "hotkey": {
            "title": "Atalho",
            "subtitle": "Pressione para iniciar/parar a gravação",
        },
        "retract": {
            "title": "Correção rápida",
            "subtitle": "Remova opcionalmente o último ditado com um atalho global",
            "enable": "Ativar atalho para retroceder último ditado",
            "hint": "Funciona uma vez para o resultado de ditado mais recente",
        },
        "model": {
            "title": "Modelo",
            "checking_size": "Verificando tamanho...",
            "size_gb": "~{size_gb:.1f} GB de download",
            "size_unknown": "Tamanho desconhecido",
            "downloading": "Baixando...",
            "loading": "Carregando modelo...",
            "ready": "Modelo pronto!",
            "failed_after_retries": "O carregamento do modelo falhou após 3 tentativas",
        },
    },
    "settings": {
        "title": "Configurações",
        "language": {
            "title": "Idioma",
            "ui_language": "Interface",
            "asr_language": "Reconhecimento",
            "restart_message": "Reinicie o vvrite para aplicar as alterações de idioma.",
            "restart_now": "Reiniciar agora",
        },
        "shortcut": {
            "title": "Atalho",
        },
        "correction": {
            "title": "Correção",
            "enable": "Ativar atalho para retroceder último ditado",
            "hint": "Exclui o resultado de ditado colado mais recentemente",
        },
        "microphone": {
            "title": "Microfone",
        },
        "model": {
            "title": "Modelo",
        },
        "custom_words": {
            "title": "Palavras personalizadas",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Palavras separadas por vírgula para melhorar a precisão do reconhecimento",
        },
        "sound": {
            "title": "Som",
            "start": "Iniciar",
            "stop": "Parar",
            "custom": "Personalizado...",
            "hint": "Ajustar o controle deslizante reproduz automaticamente o som selecionado",
            "choose_file": "Escolher um arquivo de som",
        },
        "permissions": {
            "title": "Permissões",
            "accessibility_checking": "Acessibilidade: verificando...",
            "microphone_checking": "Microfone: verificando...",
            "accessibility_granted": "Acessibilidade: ✅ Concedido",
            "accessibility_not_granted": "Acessibilidade: ❌ Não concedido",
            "microphone_granted": "Microfone: ✅ Concedido",
        },
        "login": {
            "title": "Iniciar no login",
            "error": "Não foi possível atualizar a inicialização no login",
        },
        "update": {
            "title": "Verificar atualizações automaticamente",
        },
    },
    "menu": {
        "hotkey": "Atalho: {hotkey}",
        "microphone": "Microfone: {microphone}",
        "settings": "Configurações...",
        "check_updates": "Verificar atualizações...",
        "update_available": "Atualização disponível ({version})",
        "quit": "Sair do vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "Permissões necessárias",
            "message": "O vvrite precisa das seguintes permissões:\n\n{permissions}\n\nClique em 'Conceder' para abrir cada diálogo de permissão.",
            "accessibility": "Acessibilidade (para atalho global)",
            "microphone": "Microfone (para gravação de voz)",
        },
        "model_failed": {
            "title": "Falha ao carregar o modelo",
        },
        "no_updates": {
            "title": "Nenhuma atualização disponível",
            "message": "vvrite {version} é a versão mais recente.",
        },
        "update_available": {
            "title": "vvrite {version} está disponível",
            "message": "Você está usando a versão {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "Transcrevendo...",
    },
    "widgets": {
        "press_shortcut": "Pressione um atalho...",
    },
}

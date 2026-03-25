"""Turkish locale strings for vvrite."""

strings = {
    "common": {
        "grant": "İzin Ver",
        "retry": "Tekrar Dene",
        "dismiss": "Kapat",
        "download": "İndir",
        "later": "Sonra",
        "back": "Geri",
        "next": "İleri",
        "done": "Bitti",
        "open": "Aç",
        "change": "Değiştir",
        "ok": "OK",
        "system_default": "Sistem Varsayılanı",
        "automatic": "Otomatik",
        "get_started": "Başla",
    },
    "status": {
        "ready": "Hazır",
        "recording": "Kaydediliyor...",
        "transcribing": "Yazıya dökülüyor...",
        "loading_model": "Model yükleniyor...",
        "waiting_permissions": "İzinler bekleniyor...",
        "error_model": "Hata: model başarısız",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Sesten metne, anında.",
        },
        "language": {
            "title": "Dil",
        },
        "permissions": {
            "title": "İzinler",
            "accessibility": "Erişilebilirlik",
            "accessibility_desc": "Genel kısayol tuşu için",
            "microphone": "Mikrofon",
            "microphone_desc": "Ses kaydı için",
            "granted": "Verildi",
            "not_granted": "Verilmedi",
        },
        "hotkey": {
            "title": "Kısayol Tuşu",
            "subtitle": "Kaydı başlatmak/durdurmak için basın",
        },
        "retract": {
            "title": "Hızlı Düzeltme",
            "subtitle": "Son dikte işlemini genel kısayolla isteğe bağlı olarak kaldırın",
            "enable": "Son dikteyi geri alma kısayolunu etkinleştir",
            "hint": "En son dikte sonucu için bir kez çalışır",
        },
        "model": {
            "title": "Model",
            "checking_size": "Boyut kontrol ediliyor...",
            "size_gb": "~{size_gb:.1f} GB indirme",
            "size_unknown": "Boyut bilinmiyor",
            "downloading": "İndiriliyor...",
            "loading": "Model yükleniyor...",
            "ready": "Model hazır!",
            "failed_after_retries": "3 denemeden sonra model yüklenemedi",
        },
    },
    "settings": {
        "title": "Ayarlar",
        "language": {
            "title": "Dil",
            "ui_language": "Arayüz",
            "asr_language": "Tanıma",
            "restart_message": "Dil değişikliklerini uygulamak için vvrite'ı yeniden başlatın.",
            "restart_now": "Şimdi Yeniden Başlat",
        },
        "shortcut": {
            "title": "Kısayol",
        },
        "correction": {
            "title": "Düzeltme",
            "enable": "Son dikteyi geri alma kısayolunu etkinleştir",
            "hint": "En son yapıştırılan dikte sonucunu siler",
        },
        "microphone": {
            "title": "Mikrofon",
        },
        "model": {
            "title": "Model",
        },
        "custom_words": {
            "title": "Özel Kelimeler",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Tanıma doğruluğunu artırmak için virgülle ayrılmış kelimeler",
        },
        "sound": {
            "title": "Ses",
            "start": "Başlat",
            "stop": "Durdur",
            "custom": "Özel...",
            "hint": "Kaydırıcıyı ayarlamak seçilen sesi otomatik olarak çalar",
            "choose_file": "Ses dosyası seçin",
        },
        "permissions": {
            "title": "İzinler",
            "accessibility_checking": "Erişilebilirlik: kontrol ediliyor...",
            "microphone_checking": "Mikrofon: kontrol ediliyor...",
            "accessibility_granted": "Erişilebilirlik: ✅ Verildi",
            "accessibility_not_granted": "Erişilebilirlik: ❌ Verilmedi",
            "microphone_granted": "Mikrofon: ✅ Verildi",
        },
        "login": {
            "title": "Girişte başlat",
            "error": "Girişte başlatma güncellenemedi",
        },
        "update": {
            "title": "Güncellemeleri otomatik olarak kontrol et",
        },
    },
    "menu": {
        "hotkey": "Kısayol: {hotkey}",
        "microphone": "Mikrofon: {microphone}",
        "settings": "Ayarlar...",
        "check_updates": "Güncellemeleri Kontrol Et...",
        "update_available": "Güncelleme Mevcut ({version})",
        "quit": "vvrite'dan Çık",
    },
    "alerts": {
        "permissions_required": {
            "title": "İzinler Gerekli",
            "message": "vvrite aşağıdaki izinlere ihtiyaç duyar:\n\n{permissions}\n\nHer izin iletişim kutusunu açmak için 'İzin Ver'e tıklayın.",
            "accessibility": "Erişilebilirlik (genel kısayol tuşu için)",
            "microphone": "Mikrofon (ses kaydı için)",
        },
        "model_failed": {
            "title": "Model Yüklenemedi",
        },
        "no_updates": {
            "title": "Güncelleme Yok",
            "message": "vvrite {version} en son sürümdür.",
        },
        "update_available": {
            "title": "vvrite {version} mevcut",
            "message": "Şu anda {current_version} çalıştırıyorsunuz.",
        },
    },
    "overlay": {
        "transcribing": "Yazıya dökülüyor...",
    },
    "widgets": {
        "press_shortcut": "Kısayol tuşuna basın...",
    },
}

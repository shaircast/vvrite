"""Arabic locale strings for vvrite."""

strings = {
    "common": {
        "grant": "منح",
        "retry": "إعادة المحاولة",
        "dismiss": "إغلاق",
        "download": "تنزيل",
        "later": "لاحقاً",
        "back": "رجوع",
        "next": "التالي",
        "done": "تم",
        "open": "فتح",
        "change": "تغيير",
        "ok": "OK",
        "system_default": "الافتراضي للنظام",
        "automatic": "تلقائي",
        "get_started": "ابدأ الآن",
    },
    "status": {
        "ready": "جاهز",
        "recording": "جارٍ التسجيل...",
        "transcribing": "جارٍ التفريغ...",
        "loading_model": "جارٍ تحميل النموذج...",
        "waiting_permissions": "في انتظار الأذونات...",
        "error_model": "خطأ: فشل النموذج",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "من الصوت إلى النص، فوراً.",
        },
        "language": {
            "title": "اللغة",
        },
        "permissions": {
            "title": "الأذونات",
            "accessibility": "إمكانية الوصول",
            "accessibility_desc": "لاختصار لوحة المفاتيح العام",
            "microphone": "الميكروفون",
            "microphone_desc": "لتسجيل الصوت",
            "granted": "ممنوح",
            "not_granted": "غير ممنوح",
        },
        "hotkey": {
            "title": "اختصار لوحة المفاتيح",
            "subtitle": "اضغط لبدء/إيقاف التسجيل",
        },
        "retract": {
            "title": "تصحيح سريع",
            "subtitle": "إزالة آخر إملاء اختيارياً باستخدام اختصار عام",
            "enable": "تفعيل اختصار التراجع عن آخر إملاء",
            "hint": "يعمل مرة واحدة لأحدث نتيجة إملاء",
        },
        "model": {
            "title": "النموذج",
            "checking_size": "جارٍ التحقق من الحجم...",
            "size_gb": "~{size_gb:.1f} جيجابايت للتنزيل",
            "size_unknown": "الحجم غير معروف",
            "downloading": "جارٍ التنزيل...",
            "loading": "جارٍ تحميل النموذج...",
            "ready": "النموذج جاهز!",
            "failed_after_retries": "فشل تحميل النموذج بعد 3 محاولات",
        },
    },
    "settings": {
        "title": "الإعدادات",
        "language": {
            "title": "اللغة",
            "ui_language": "الواجهة",
            "asr_language": "التعرف",
            "restart_message": "أعد تشغيل vvrite لتطبيق تغييرات اللغة.",
            "restart_now": "إعادة التشغيل الآن",
        },
        "shortcut": {
            "title": "الاختصار",
        },
        "correction": {
            "title": "التصحيح",
            "enable": "تفعيل اختصار التراجع عن آخر إملاء",
            "hint": "يحذف أحدث نتيجة إملاء تم لصقها",
        },
        "microphone": {
            "title": "الميكروفون",
        },
        "model": {
            "title": "النموذج",
        },
        "custom_words": {
            "title": "كلمات مخصصة",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "كلمات مفصولة بفواصل لتحسين دقة التعرف",
        },
        "sound": {
            "title": "الصوت",
            "start": "بدء",
            "stop": "إيقاف",
            "custom": "مخصص...",
            "hint": "تعديل شريط التمرير يشغّل الصوت المحدد تلقائياً",
            "choose_file": "اختر ملف صوتي",
        },
        "permissions": {
            "title": "الأذونات",
            "accessibility_checking": "إمكانية الوصول: جارٍ التحقق...",
            "microphone_checking": "الميكروفون: جارٍ التحقق...",
            "accessibility_granted": "إمكانية الوصول: ✅ ممنوح",
            "accessibility_not_granted": "إمكانية الوصول: ❌ غير ممنوح",
            "microphone_granted": "الميكروفون: ✅ ممنوح",
        },
        "login": {
            "title": "التشغيل عند تسجيل الدخول",
            "error": "تعذر تحديث التشغيل عند تسجيل الدخول",
        },
        "update": {
            "title": "التحقق من التحديثات تلقائياً",
        },
    },
    "menu": {
        "hotkey": "الاختصار: {hotkey}",
        "microphone": "الميكروفون: {microphone}",
        "settings": "الإعدادات...",
        "check_updates": "التحقق من التحديثات...",
        "update_available": "تحديث متاح ({version})",
        "quit": "إنهاء vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "الأذونات مطلوبة",
            "message": "يحتاج vvrite إلى الأذونات التالية:\n\n{permissions}\n\nانقر على 'منح' لفتح كل مربع حوار أذونات.",
            "accessibility": "إمكانية الوصول (لاختصار لوحة المفاتيح العام)",
            "microphone": "الميكروفون (لتسجيل الصوت)",
        },
        "model_failed": {
            "title": "فشل تحميل النموذج",
        },
        "no_updates": {
            "title": "لا توجد تحديثات متاحة",
            "message": "vvrite {version} هو أحدث إصدار.",
        },
        "update_available": {
            "title": "vvrite {version} متاح",
            "message": "أنت تستخدم حالياً الإصدار {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "جارٍ التفريغ...",
    },
    "widgets": {
        "press_shortcut": "اضغط اختصاراً...",
    },
}

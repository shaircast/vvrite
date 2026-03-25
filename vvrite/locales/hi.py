"""Hindi locale strings for vvrite."""

strings = {
    "common": {
        "grant": "अनुमति दें",
        "retry": "पुनः प्रयास",
        "dismiss": "बंद करें",
        "download": "डाउनलोड",
        "later": "बाद में",
        "back": "पीछे",
        "next": "अगला",
        "done": "पूर्ण",
        "open": "खोलें",
        "change": "बदलें",
        "ok": "OK",
        "system_default": "सिस्टम डिफ़ॉल्ट",
        "automatic": "स्वचालित",
        "get_started": "शुरू करें",
    },
    "status": {
        "ready": "तैयार",
        "recording": "रिकॉर्डिंग...",
        "transcribing": "ट्रांसक्रिप्शन...",
        "loading_model": "मॉडल लोड हो रहा है...",
        "waiting_permissions": "अनुमतियों की प्रतीक्षा...",
        "error_model": "त्रुटि: मॉडल विफल",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "आवाज़ से टेक्स्ट, तुरंत।",
        },
        "language": {
            "title": "भाषा",
        },
        "permissions": {
            "title": "अनुमतियाँ",
            "accessibility": "एक्सेसिबिलिटी",
            "accessibility_desc": "ग्लोबल हॉटकी के लिए",
            "microphone": "माइक्रोफ़ोन",
            "microphone_desc": "आवाज़ रिकॉर्डिंग के लिए",
            "granted": "अनुमति दी गई",
            "not_granted": "अनुमति नहीं दी गई",
        },
        "hotkey": {
            "title": "हॉटकी",
            "subtitle": "रिकॉर्डिंग शुरू/बंद करने के लिए दबाएँ",
        },
        "retract": {
            "title": "त्वरित सुधार",
            "subtitle": "ग्लोबल शॉर्टकट से अंतिम डिक्टेशन को वैकल्पिक रूप से हटाएँ",
            "enable": "अंतिम डिक्टेशन वापस लेने का शॉर्टकट सक्षम करें",
            "hint": "सबसे हाल के डिक्टेशन परिणाम के लिए एक बार काम करता है",
        },
        "model": {
            "title": "मॉडल",
            "checking_size": "आकार जाँचा जा रहा है...",
            "size_gb": "~{size_gb:.1f} GB डाउनलोड",
            "size_unknown": "आकार अज्ञात",
            "downloading": "डाउनलोड हो रहा है...",
            "loading": "मॉडल लोड हो रहा है...",
            "ready": "मॉडल तैयार!",
            "failed_after_retries": "3 प्रयासों के बाद मॉडल लोडिंग विफल",
        },
    },
    "settings": {
        "title": "सेटिंग्स",
        "language": {
            "title": "भाषा",
            "ui_language": "UI",
            "asr_language": "पहचान",
            "restart_message": "भाषा परिवर्तन लागू करने के लिए vvrite पुनः आरंभ करें।",
            "restart_now": "अभी पुनः आरंभ करें",
        },
        "shortcut": {
            "title": "शॉर्टकट",
        },
        "correction": {
            "title": "सुधार",
            "enable": "अंतिम डिक्टेशन वापस लेने का शॉर्टकट सक्षम करें",
            "hint": "सबसे हाल में पेस्ट किया गया डिक्टेशन परिणाम हटाता है",
        },
        "microphone": {
            "title": "माइक्रोफ़ोन",
        },
        "model": {
            "title": "मॉडल",
        },
        "custom_words": {
            "title": "कस्टम शब्द",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "पहचान सटीकता में सुधार के लिए अल्पविराम से अलग किए गए शब्द",
        },
        "sound": {
            "title": "ध्वनि",
            "start": "शुरू",
            "stop": "रोकें",
            "custom": "कस्टम...",
            "hint": "स्लाइडर समायोजित करने पर चयनित ध्वनि स्वचालित रूप से बजती है",
            "choose_file": "ध्वनि फ़ाइल चुनें",
        },
        "permissions": {
            "title": "अनुमतियाँ",
            "accessibility_checking": "एक्सेसिबिलिटी: जाँच हो रही है...",
            "microphone_checking": "माइक्रोफ़ोन: जाँच हो रही है...",
            "accessibility_granted": "एक्सेसिबिलिटी: ✅ अनुमति दी गई",
            "accessibility_not_granted": "एक्सेसिबिलिटी: ❌ अनुमति नहीं दी गई",
            "microphone_granted": "माइक्रोफ़ोन: ✅ अनुमति दी गई",
        },
        "login": {
            "title": "लॉगिन पर लॉन्च करें",
            "error": "लॉगिन पर लॉन्च अपडेट नहीं किया जा सका",
        },
        "update": {
            "title": "स्वचालित रूप से अपडेट जाँचें",
        },
    },
    "menu": {
        "hotkey": "हॉटकी: {hotkey}",
        "microphone": "माइक्रोफ़ोन: {microphone}",
        "settings": "सेटिंग्स...",
        "check_updates": "अपडेट जाँचें...",
        "update_available": "अपडेट उपलब्ध ({version})",
        "quit": "vvrite बंद करें",
    },
    "alerts": {
        "permissions_required": {
            "title": "अनुमतियाँ आवश्यक",
            "message": "vvrite को निम्नलिखित अनुमतियों की आवश्यकता है:\n\n{permissions}\n\nप्रत्येक अनुमति डायलॉग खोलने के लिए 'अनुमति दें' पर क्लिक करें।",
            "accessibility": "एक्सेसिबिलिटी (ग्लोबल हॉटकी के लिए)",
            "microphone": "माइक्रोफ़ोन (आवाज़ रिकॉर्डिंग के लिए)",
        },
        "model_failed": {
            "title": "मॉडल लोडिंग विफल",
        },
        "no_updates": {
            "title": "कोई अपडेट उपलब्ध नहीं",
            "message": "vvrite {version} नवीनतम संस्करण है।",
        },
        "update_available": {
            "title": "vvrite {version} उपलब्ध है",
            "message": "आप वर्तमान में {current_version} चला रहे हैं।",
        },
    },
    "overlay": {
        "transcribing": "ट्रांसक्रिप्शन...",
    },
    "widgets": {
        "press_shortcut": "शॉर्टकट दबाएँ...",
    },
}

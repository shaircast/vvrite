"""Russian locale strings for vvrite."""

strings = {
    "common": {
        "grant": "Разрешить",
        "retry": "Повторить",
        "dismiss": "Закрыть",
        "download": "Скачать",
        "later": "Позже",
        "back": "Назад",
        "next": "Далее",
        "done": "Готово",
        "open": "Открыть",
        "change": "Изменить",
        "ok": "OK",
        "system_default": "Системный по умолчанию",
        "automatic": "Автоматически",
        "get_started": "Начать",
    },
    "status": {
        "ready": "Готов",
        "recording": "Запись...",
        "transcribing": "Транскрибирование...",
        "loading_model": "Загрузка модели...",
        "waiting_permissions": "Ожидание разрешений...",
        "error_model": "Ошибка: сбой модели",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "Голос в текст, мгновенно.",
        },
        "language": {
            "title": "Язык",
        },
        "permissions": {
            "title": "Разрешения",
            "accessibility": "Универсальный доступ",
            "accessibility_desc": "Для глобальной горячей клавиши",
            "microphone": "Микрофон",
            "microphone_desc": "Для записи голоса",
            "granted": "Разрешено",
            "not_granted": "Не разрешено",
        },
        "hotkey": {
            "title": "Горячая клавиша",
            "subtitle": "Нажмите для начала/остановки записи",
        },
        "retract": {
            "title": "Быстрая коррекция",
            "subtitle": "Удалите последнюю диктовку глобальным сочетанием клавиш",
            "enable": "Включить сочетание для отмены последней диктовки",
            "hint": "Работает один раз для последнего результата диктовки",
        },
        "model": {
            "title": "Модель",
            "checking_size": "Проверка размера...",
            "size_gb": "~{size_gb:.1f} ГБ загрузки",
            "size_unknown": "Размер неизвестен",
            "downloading": "Загрузка...",
            "loading": "Загрузка модели...",
            "ready": "Модель готова!",
            "failed_after_retries": "Загрузка модели не удалась после 3 попыток",
        },
    },
    "settings": {
        "title": "Настройки",
        "language": {
            "title": "Язык",
            "ui_language": "Интерфейс",
            "asr_language": "Распознавание",
            "restart_message": "Перезапустите vvrite для применения языковых изменений.",
            "restart_now": "Перезапустить сейчас",
        },
        "shortcut": {
            "title": "Сочетание клавиш",
        },
        "correction": {
            "title": "Коррекция",
            "enable": "Включить сочетание для отмены последней диктовки",
            "hint": "Удаляет последний вставленный результат диктовки",
        },
        "microphone": {
            "title": "Микрофон",
        },
        "model": {
            "title": "Модель",
        },
        "custom_words": {
            "title": "Пользовательские слова",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "Слова через запятую для улучшения точности распознавания",
        },
        "sound": {
            "title": "Звук",
            "start": "Начало",
            "stop": "Остановка",
            "custom": "Выбрать...",
            "hint": "При перемещении ползунка автоматически воспроизводится выбранный звук",
            "choose_file": "Выберите звуковой файл",
        },
        "permissions": {
            "title": "Разрешения",
            "accessibility_checking": "Универсальный доступ: проверка...",
            "microphone_checking": "Микрофон: проверка...",
            "accessibility_granted": "Универсальный доступ: ✅ Разрешено",
            "accessibility_not_granted": "Универсальный доступ: ❌ Не разрешено",
            "microphone_granted": "Микрофон: ✅ Разрешено",
        },
        "login": {
            "title": "Запускать при входе в систему",
            "error": "Не удалось обновить запуск при входе",
        },
        "update": {
            "title": "Автоматически проверять обновления",
        },
    },
    "menu": {
        "hotkey": "Горячая клавиша: {hotkey}",
        "microphone": "Микрофон: {microphone}",
        "settings": "Настройки...",
        "check_updates": "Проверить обновления...",
        "update_available": "Доступно обновление ({version})",
        "quit": "Завершить vvrite",
    },
    "alerts": {
        "permissions_required": {
            "title": "Требуются разрешения",
            "message": "vvrite необходимы следующие разрешения:\n\n{permissions}\n\nНажмите «Разрешить», чтобы открыть каждый диалог разрешений.",
            "accessibility": "Универсальный доступ (для глобальной горячей клавиши)",
            "microphone": "Микрофон (для записи голоса)",
        },
        "model_failed": {
            "title": "Ошибка загрузки модели",
        },
        "no_updates": {
            "title": "Обновлений нет",
            "message": "vvrite {version} — последняя версия.",
        },
        "update_available": {
            "title": "Доступна версия vvrite {version}",
            "message": "Вы используете версию {current_version}.",
        },
    },
    "overlay": {
        "transcribing": "Транскрибирование...",
    },
    "widgets": {
        "press_shortcut": "Нажмите сочетание клавиш...",
    },
}

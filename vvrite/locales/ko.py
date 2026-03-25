"""Korean locale strings for vvrite."""

strings = {
    "common": {
        "grant": "허용",
        "retry": "재시도",
        "dismiss": "닫기",
        "download": "다운로드",
        "later": "나중에",
        "back": "뒤로",
        "next": "다음",
        "done": "완료",
        "open": "열기",
        "change": "변경",
        "ok": "OK",
        "system_default": "시스템 기본값",
        "automatic": "자동",
        "get_started": "시작하기",
    },
    "status": {
        "ready": "준비됨",
        "recording": "녹음 중...",
        "transcribing": "변환 중...",
        "loading_model": "모델 로딩 중...",
        "waiting_permissions": "권한 대기 중...",
        "error_model": "오류: 모델 실패",
    },
    "onboarding": {
        "welcome": {
            "subtitle": "음성을 텍스트로, 즉시.",
        },
        "language": {
            "title": "언어",
        },
        "permissions": {
            "title": "권한",
            "accessibility": "손쉬운 사용",
            "accessibility_desc": "전역 단축키 사용",
            "microphone": "마이크",
            "microphone_desc": "음성 녹음 사용",
            "granted": "허용됨",
            "not_granted": "허용되지 않음",
        },
        "hotkey": {
            "title": "단축키",
            "subtitle": "눌러서 녹음 시작/중지",
        },
        "retract": {
            "title": "빠른 수정",
            "subtitle": "전역 단축키로 마지막 받아쓰기를 선택적으로 제거",
            "enable": "마지막 받아쓰기 취소 단축키 활성화",
            "hint": "가장 최근 받아쓰기 결과에 한 번만 작동합니다",
        },
        "model": {
            "title": "모델",
            "checking_size": "크기 확인 중...",
            "size_gb": "~{size_gb:.1f} GB 다운로드",
            "size_unknown": "크기 알 수 없음",
            "downloading": "다운로드 중...",
            "loading": "모델 로딩 중...",
            "ready": "모델 준비 완료!",
            "failed_after_retries": "3회 시도 후 모델 로딩 실패",
        },
    },
    "settings": {
        "title": "설정",
        "language": {
            "title": "언어",
            "ui_language": "UI",
            "asr_language": "인식",
            "restart_message": "언어 변경을 적용하려면 vvrite를 재시작하세요.",
            "restart_now": "지금 재시작",
        },
        "shortcut": {
            "title": "단축키",
        },
        "correction": {
            "title": "수정",
            "enable": "마지막 받아쓰기 취소 단축키 활성화",
            "hint": "가장 최근에 붙여넣은 받아쓰기 결과를 삭제합니다",
        },
        "microphone": {
            "title": "마이크",
        },
        "model": {
            "title": "모델",
        },
        "custom_words": {
            "title": "사용자 지정 단어",
            "placeholder": "MLX, Qwen, vvrite",
            "hint": "인식 정확도를 높이기 위한 쉼표로 구분된 단어",
        },
        "sound": {
            "title": "소리",
            "start": "시작",
            "stop": "중지",
            "custom": "사용자 지정...",
            "hint": "슬라이더를 조절하면 선택한 소리가 자동으로 재생됩니다",
            "choose_file": "소리 파일 선택",
        },
        "permissions": {
            "title": "권한",
            "accessibility_checking": "손쉬운 사용: 확인 중...",
            "microphone_checking": "마이크: 확인 중...",
            "accessibility_granted": "손쉬운 사용: ✅ 허용됨",
            "accessibility_not_granted": "손쉬운 사용: ❌ 허용되지 않음",
            "microphone_granted": "마이크: ✅ 허용됨",
        },
        "login": {
            "title": "로그인 시 실행",
            "error": "로그인 시 실행을 업데이트할 수 없습니다",
        },
        "update": {
            "title": "자동으로 업데이트 확인",
        },
    },
    "menu": {
        "hotkey": "단축키: {hotkey}",
        "microphone": "마이크: {microphone}",
        "settings": "설정...",
        "check_updates": "업데이트 확인...",
        "update_available": "업데이트 사용 가능 ({version})",
        "quit": "vvrite 종료",
    },
    "alerts": {
        "permissions_required": {
            "title": "권한 필요",
            "message": "vvrite에 다음 권한이 필요합니다:\n\n{permissions}\n\n'허용'을 클릭하여 각 권한 대화 상자를 여세요.",
            "accessibility": "손쉬운 사용 (전역 단축키 사용)",
            "microphone": "마이크 (음성 녹음 사용)",
        },
        "model_failed": {
            "title": "모델 로딩 실패",
        },
        "no_updates": {
            "title": "사용 가능한 업데이트 없음",
            "message": "vvrite {version}이 최신 버전입니다.",
        },
        "update_available": {
            "title": "vvrite {version}을 사용할 수 있습니다",
            "message": "현재 {current_version}을 실행 중입니다.",
        },
    },
    "overlay": {
        "transcribing": "변환 중...",
    },
    "widgets": {
        "press_shortcut": "단축키를 누르세요...",
    },
}

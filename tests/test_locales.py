"""Tests for vvrite.locales i18n core module."""

import unittest
from unittest.mock import patch


class TestSupportedLanguages(unittest.TestCase):
    def setUp(self):
        from vvrite.locales import _clear_cache

        _clear_cache()

    def test_supported_languages_is_list_of_tuples(self):
        from vvrite.locales import SUPPORTED_LANGUAGES

        self.assertIsInstance(SUPPORTED_LANGUAGES, list)
        self.assertGreaterEqual(len(SUPPORTED_LANGUAGES), 14)
        for item in SUPPORTED_LANGUAGES:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            code, name = item
            self.assertIsInstance(code, str)
            self.assertIsInstance(name, str)

    def test_supported_languages_exact_codes(self):
        from vvrite.locales import SUPPORTED_LANGUAGES
        codes = {code for code, _ in SUPPORTED_LANGUAGES}
        required = {"en","ko","ja","zh-Hans","zh-Hant","es","fr","de","pt","ru","ar","hi","tr","it"}
        self.assertEqual(codes, required)

    def test_asr_language_map_covers_all_supported(self):
        from vvrite.locales import SUPPORTED_LANGUAGES, ASR_LANGUAGE_MAP

        codes = {code for code, _ in SUPPORTED_LANGUAGES}
        for code in codes:
            self.assertIn(
                code,
                ASR_LANGUAGE_MAP,
                f"ASR_LANGUAGE_MAP missing entry for code '{code}'",
            )

    def test_asr_language_map_returns_correct_names(self):
        from vvrite.locales import ASR_LANGUAGE_MAP
        self.assertEqual(ASR_LANGUAGE_MAP["ko"], "Korean")
        self.assertEqual(ASR_LANGUAGE_MAP["en"], "English")
        self.assertEqual(ASR_LANGUAGE_MAP["zh-Hans"], "Chinese")
        self.assertEqual(ASR_LANGUAGE_MAP["zh-Hant"], "Chinese")

    def test_asr_language_map_unknown_code_returns_none(self):
        from vvrite.locales import ASR_LANGUAGE_MAP
        self.assertIsNone(ASR_LANGUAGE_MAP.get("xx"))


class TestTranslation(unittest.TestCase):
    def setUp(self):
        from vvrite.locales import set_locale, _clear_cache

        _clear_cache()
        set_locale("en")

    def test_t_returns_correct_string(self):
        from vvrite.locales import t

        self.assertEqual(t("common.retry"), "Retry")

    def test_t_nested_key(self):
        from vvrite.locales import t

        self.assertEqual(t("status.ready"), "Ready")

    def test_t_with_format_params(self):
        from vvrite.locales import t

        result = t("menu.hotkey", hotkey="\u2325Space")
        self.assertEqual(result, "Hotkey: \u2325Space")

    def test_t_missing_key_returns_key(self):
        from vvrite.locales import t

        self.assertEqual(t("nonexistent.key.path"), "nonexistent.key.path")

    def test_t_partially_missing_key_returns_key(self):
        from vvrite.locales import t

        self.assertEqual(t("common.nonexistent"), "common.nonexistent")


class TestLocaleManagement(unittest.TestCase):
    def setUp(self):
        from vvrite.locales import _clear_cache

        _clear_cache()

    def test_set_and_get_locale(self):
        from vvrite.locales import set_locale, get_locale

        set_locale("en")
        self.assertEqual(get_locale(), "en")

        set_locale("ko")
        self.assertEqual(get_locale(), "ko")

    def test_set_locale_unknown_falls_back_to_english(self):
        from vvrite.locales import set_locale, t

        set_locale("xx-FAKE")
        # Should still return English strings as fallback
        self.assertEqual(t("common.retry"), "Retry")

    def test_resolve_system_locale_returns_string(self):
        from vvrite.locales import resolve_system_locale

        result = resolve_system_locale()
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


class TestEnglishStringsCompleteness(unittest.TestCase):
    """Verify en.py strings dict has all required top-level groups."""

    def setUp(self):
        from vvrite.locales import _clear_cache

        _clear_cache()

    def test_all_groups_present(self):
        from vvrite.locales.en import strings

        required_groups = [
            "common",
            "status",
            "onboarding",
            "settings",
            "menu",
            "alerts",
            "overlay",
            "widgets",
        ]
        for group in required_groups:
            self.assertIn(group, strings, f"Missing group '{group}' in en.strings")

    def test_common_keys(self):
        from vvrite.locales.en import strings

        expected = [
            "grant", "retry", "dismiss", "download", "later", "back",
            "next", "done", "open", "change", "ok", "system_default",
            "automatic", "get_started",
        ]
        for key in expected:
            self.assertIn(key, strings["common"], f"Missing common.{key}")

    def test_status_keys(self):
        from vvrite.locales.en import strings

        expected = [
            "ready", "recording", "transcribing", "loading_model",
            "waiting_permissions", "error_model",
        ]
        for key in expected:
            self.assertIn(key, strings["status"], f"Missing status.{key}")

    def test_onboarding_keys(self):
        from vvrite.locales.en import strings

        ob = strings["onboarding"]
        # welcome
        self.assertIn("welcome", ob)
        self.assertIn("subtitle", ob["welcome"])
        # language
        self.assertIn("language", ob)
        self.assertIn("title", ob["language"])
        # permissions
        self.assertIn("permissions", ob)
        perms = ob["permissions"]
        for key in [
            "title", "accessibility", "accessibility_desc",
            "microphone", "microphone_desc", "granted", "not_granted",
        ]:
            self.assertIn(key, perms, f"Missing onboarding.permissions.{key}")
        # hotkey
        self.assertIn("hotkey", ob)
        self.assertIn("title", ob["hotkey"])
        self.assertIn("subtitle", ob["hotkey"])
        # retract
        self.assertIn("retract", ob)
        for key in ["title", "subtitle", "enable", "hint"]:
            self.assertIn(key, ob["retract"], f"Missing onboarding.retract.{key}")
        # model
        self.assertIn("model", ob)
        for key in [
            "title", "checking_size", "size_gb", "size_unknown",
            "downloading", "loading", "ready", "failed_after_retries",
        ]:
            self.assertIn(key, ob["model"], f"Missing onboarding.model.{key}")

    def test_settings_keys(self):
        from vvrite.locales.en import strings

        s = strings["settings"]
        self.assertIn("title", s)
        # language
        self.assertIn("language", s)
        for key in ["title", "ui_language", "asr_language", "restart_message", "restart_now"]:
            self.assertIn(key, s["language"], f"Missing settings.language.{key}")
        # shortcut
        self.assertIn("shortcut", s)
        self.assertIn("title", s["shortcut"])
        # correction
        self.assertIn("correction", s)
        for key in ["title", "enable", "hint"]:
            self.assertIn(key, s["correction"], f"Missing settings.correction.{key}")
        # microphone
        self.assertIn("microphone", s)
        self.assertIn("title", s["microphone"])
        # model
        self.assertIn("model", s)
        self.assertIn("title", s["model"])
        # custom_words
        self.assertIn("custom_words", s)
        for key in ["title", "placeholder", "hint"]:
            self.assertIn(key, s["custom_words"], f"Missing settings.custom_words.{key}")
        # sound
        self.assertIn("sound", s)
        for key in ["title", "start", "stop", "custom", "hint", "choose_file"]:
            self.assertIn(key, s["sound"], f"Missing settings.sound.{key}")
        # permissions
        self.assertIn("permissions", s)
        for key in [
            "title", "accessibility_checking", "accessibility_granted",
            "accessibility_not_granted", "microphone_granted",
        ]:
            self.assertIn(key, s["permissions"], f"Missing settings.permissions.{key}")
        # login
        self.assertIn("login", s)
        for key in ["title", "error"]:
            self.assertIn(key, s["login"], f"Missing settings.login.{key}")
        # update
        self.assertIn("update", s)
        self.assertIn("title", s["update"])

    def test_menu_keys(self):
        from vvrite.locales.en import strings

        expected = [
            "hotkey", "microphone", "settings", "check_updates",
            "update_available", "quit",
        ]
        for key in expected:
            self.assertIn(key, strings["menu"], f"Missing menu.{key}")

    def test_alerts_keys(self):
        from vvrite.locales.en import strings

        a = strings["alerts"]
        # permissions_required
        self.assertIn("permissions_required", a)
        for key in ["title", "message", "accessibility", "microphone"]:
            self.assertIn(
                key, a["permissions_required"],
                f"Missing alerts.permissions_required.{key}",
            )
        # model_failed
        self.assertIn("model_failed", a)
        self.assertIn("title", a["model_failed"])
        # no_updates
        self.assertIn("no_updates", a)
        for key in ["title", "message"]:
            self.assertIn(key, a["no_updates"], f"Missing alerts.no_updates.{key}")
        # update_available
        self.assertIn("update_available", a)
        for key in ["title", "message"]:
            self.assertIn(key, a["update_available"], f"Missing alerts.update_available.{key}")

    def test_overlay_keys(self):
        from vvrite.locales.en import strings

        self.assertIn("transcribing", strings["overlay"])

    def test_widgets_keys(self):
        from vvrite.locales.en import strings

        self.assertIn("press_shortcut", strings["widgets"])


class TestAllLocales(unittest.TestCase):
    def setUp(self):
        from vvrite.locales import _clear_cache

        _clear_cache()

    def test_all_supported_locales_load(self):
        from vvrite.locales import SUPPORTED_LANGUAGES, set_locale, t
        for code, _ in SUPPORTED_LANGUAGES:
            set_locale(code)
            result = t("common.retry")
            self.assertNotEqual(result, "common.retry", f"Locale {code} missing common.retry")

    def test_all_locales_have_same_keys_as_english(self):
        from vvrite.locales import SUPPORTED_LANGUAGES, _load_strings

        def collect_keys(d, prefix=""):
            keys = set()
            for k, v in d.items():
                full = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict):
                    keys.update(collect_keys(v, full))
                else:
                    keys.add(full)
            return keys

        en_keys = collect_keys(_load_strings("en"))
        for code, _ in SUPPORTED_LANGUAGES:
            if code == "en":
                continue
            locale_keys = collect_keys(_load_strings(code))
            missing = en_keys - locale_keys
            self.assertEqual(missing, set(), f"Locale {code} missing keys: {missing}")


if __name__ == "__main__":
    unittest.main()

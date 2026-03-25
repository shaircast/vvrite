"""Tests for settings sound customization behavior."""

import unittest
from unittest.mock import MagicMock, patch

from vvrite.settings import SettingsWindowController


class TestCustomSoundPanelResult(unittest.TestCase):
    def setUp(self):
        self.controller = SettingsWindowController.alloc().init()
        self.controller._prefs = MagicMock()
        self.controller._prefs.start_volume = 0.4
        self.controller._prefs.stop_volume = 0.6
        self.controller._populate_sounds = MagicMock()

    @patch("vvrite.settings.sounds.play")
    def test_handle_custom_sound_panel_result_saves_start_sound(self, mock_play):
        panel = MagicMock()
        panel.URL.return_value.path.return_value = "/Users/foo/start.wav"

        self.controller._handle_custom_sound_panel_result(1, panel, True)

        self.assertEqual(self.controller._prefs.sound_start, "/Users/foo/start.wav")
        mock_play.assert_called_once_with("/Users/foo/start.wav", 0.4)
        self.controller._populate_sounds.assert_called_once()

    @patch("vvrite.settings.sounds.play")
    def test_handle_custom_sound_panel_result_cancel_keeps_existing_value(self, mock_play):
        self.controller._prefs.sound_stop = "Purr"
        panel = MagicMock()

        self.controller._handle_custom_sound_panel_result(0, panel, False)

        self.assertEqual(self.controller._prefs.sound_stop, "Purr")
        mock_play.assert_not_called()
        self.controller._populate_sounds.assert_called_once()


class TestOpenCustomSoundPanel(unittest.TestCase):
    def setUp(self):
        self.controller = SettingsWindowController.alloc().init()
        self.controller._window = MagicMock()
        self.controller._handle_custom_sound_panel_result = MagicMock()

    @patch("vvrite.settings.NSOpenPanel")
    @patch("vvrite.settings.NSApp")
    def test_open_custom_sound_panel_uses_sheet_for_window(self, mock_app, mock_open_panel):
        panel = MagicMock()
        mock_open_panel.openPanel.return_value = panel

        self.controller._open_custom_sound_panel(True)

        mock_app.activateIgnoringOtherApps_.assert_called_once_with(True)
        self.controller._window.makeKeyAndOrderFront_.assert_called_once_with(None)
        panel.setAllowedFileTypes_.assert_called_once_with(["aiff", "wav", "mp3", "m4a", "caf"])
        panel.beginSheetModalForWindow_completionHandler_.assert_called_once()

        args = panel.beginSheetModalForWindow_completionHandler_.call_args[0]
        self.assertIs(args[0], self.controller._window)
        args[1](1)
        self.controller._handle_custom_sound_panel_result.assert_called_once_with(1, panel, True)


class TestSoundPopupActions(unittest.TestCase):
    def setUp(self):
        self.controller = SettingsWindowController.alloc().init()
        self.controller._prefs = MagicMock()
        self.controller._prefs.start_volume = 0.4
        self.controller._prefs.stop_volume = 0.6

    def test_start_sound_changed_schedules_custom_panel_after_menu_closes(self):
        sender = MagicMock()
        sender.titleOfSelectedItem.return_value = "Custom..."

        with patch("vvrite.settings.t", return_value="Custom..."), patch.object(
            self.controller, "performSelector_withObject_afterDelay_"
        ) as mock_schedule:
            self.controller.startSoundChanged_(sender)

        mock_schedule.assert_called_once_with("openStartCustomSoundPanel:", None, 0.0)

    def test_stop_sound_changed_schedules_custom_panel_after_menu_closes(self):
        sender = MagicMock()
        sender.titleOfSelectedItem.return_value = "Custom..."

        with patch("vvrite.settings.t", return_value="Custom..."), patch.object(
            self.controller, "performSelector_withObject_afterDelay_"
        ) as mock_schedule:
            self.controller.stopSoundChanged_(sender)

        mock_schedule.assert_called_once_with("openStopCustomSoundPanel:", None, 0.0)


if __name__ == "__main__":
    unittest.main()

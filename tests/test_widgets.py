"""Tests for shortcut formatting and active-shortcut selection."""

import types
import unittest
from unittest.mock import MagicMock, patch

from AppKit import NSDragOperationCopy, NSMakeRect
from Quartz import (
    kCGEventFlagMaskAlternate,
    kCGEventFlagMaskShift,
    kCGEventFlagMaskCommand,
)

from vvrite.widgets import (
    AppBundleDragView,
    active_shortcut,
    format_shortcut,
    packaged_app_bundle_path,
)


class TestFormatShortcut(unittest.TestCase):
    def test_regular_chord(self):
        self.assertEqual(format_shortcut(0x31, int(kCGEventFlagMaskAlternate)), "⌥Space")

    def test_regular_chord_multiple_modifiers(self):
        mods = int(kCGEventFlagMaskAlternate | kCGEventFlagMaskShift)
        self.assertEqual(format_shortcut(0x06, mods), "⌥⇧Z")

    def test_modifier_only_right_command(self):
        self.assertEqual(format_shortcut(0x36, 0), "Right ⌘")

    def test_modifier_only_left_command(self):
        self.assertEqual(format_shortcut(0x37, 0), "Left ⌘")

    def test_modifier_only_right_option(self):
        self.assertEqual(format_shortcut(0x3D, 0), "Right ⌥")

    def test_modifier_only_fn(self):
        self.assertEqual(format_shortcut(0x3F, 0), "fn")

    def test_unknown_keycode_falls_back_to_hex(self):
        self.assertEqual(format_shortcut(0x7A, 0), "0x7A")


class TestActiveShortcut(unittest.TestCase):
    def _prefs(self, mode):
        return types.SimpleNamespace(
            recording_mode=mode,
            hotkey_keycode=0x31,
            hotkey_modifiers=int(kCGEventFlagMaskAlternate),
            ptt_hotkey_keycode=0x36,
            ptt_hotkey_modifiers=0,
        )

    def test_toggle_mode_uses_main_hotkey(self):
        self.assertEqual(
            active_shortcut(self._prefs("toggle")),
            (0x31, int(kCGEventFlagMaskAlternate)),
        )

    def test_hold_mode_uses_ptt_hotkey(self):
        self.assertEqual(active_shortcut(self._prefs("hold")), (0x36, 0))


class TestPackagedAppBundlePath(unittest.TestCase):
    @patch("vvrite.widgets.NSBundle")
    def test_returns_packaged_app_path(self, mock_bundle_class):
        bundle = MagicMock()
        bundle.bundlePath.return_value = "/Applications/vvrite.app"
        mock_bundle_class.mainBundle.return_value = bundle

        self.assertEqual(packaged_app_bundle_path(), "/Applications/vvrite.app")

    @patch("vvrite.widgets.NSBundle")
    def test_returns_none_for_source_interpreter(self, mock_bundle_class):
        bundle = MagicMock()
        bundle.bundlePath.return_value = "/usr/local/bin"
        mock_bundle_class.mainBundle.return_value = bundle

        self.assertIsNone(packaged_app_bundle_path())


class TestAppBundleDragView(unittest.TestCase):
    def test_offers_copy_drag_operation(self):
        view = AppBundleDragView.alloc().init()

        self.assertEqual(
            view.draggingSession_sourceOperationMaskForDraggingContext_(None, 0),
            NSDragOperationCopy,
        )

    def test_icon_hint_and_grip_share_vertical_center(self):
        view = (
            AppBundleDragView.alloc()
            .initWithFrame_bundlePath_accessibilityLabel_(
                NSMakeRect(0, 0, 396, 44),
                "/Applications/vvrite.app",
                "Drag this item into the Accessibility list.",
            )
        )

        centers = [
            subview.frame().origin.y + subview.frame().size.height / 2.0
            for subview in view.subviews()
        ]
        self.assertEqual(len(centers), 3)
        for center in centers:
            self.assertAlmostEqual(center, 22.0)


if __name__ == "__main__":
    unittest.main()

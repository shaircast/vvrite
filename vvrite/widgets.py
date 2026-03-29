"""Shared UI widgets."""

import objc
from vvrite.locales import t
from AppKit import (
    NSTextField,
    NSFont,
    NSEventModifierFlagCommand,
    NSEventModifierFlagShift,
    NSEventModifierFlagControl,
    NSEventModifierFlagOption,
)
from Quartz import (
    kCGEventFlagMaskCommand,
    kCGEventFlagMaskShift,
    kCGEventFlagMaskControl,
    kCGEventFlagMaskAlternate,
)


_KEY_MAP = {
    0x00: "A", 0x01: "S", 0x02: "D", 0x03: "F", 0x04: "H",
    0x05: "G", 0x06: "Z", 0x07: "X", 0x08: "C", 0x09: "V",
    0x0B: "B", 0x0C: "Q", 0x0D: "W", 0x0E: "E", 0x0F: "R",
    0x10: "Y", 0x11: "T", 0x12: "1", 0x13: "2", 0x14: "3",
    0x15: "4", 0x16: "6", 0x17: "5", 0x18: "=", 0x19: "9",
    0x1A: "7", 0x1B: "-", 0x1C: "8", 0x1D: "0", 0x1F: "O",
    0x20: "U", 0x22: "I", 0x23: "P", 0x25: "L", 0x26: "J",
    0x28: "K", 0x2C: "/", 0x2D: "N", 0x2E: "M", 0x31: "Space",
    0x33: "Delete",
}


def format_shortcut(keycode: int, modifiers: int) -> str:
    """Format a keycode + CGEvent modifier flags into a human-readable string."""
    parts = []
    if modifiers & kCGEventFlagMaskControl:
        parts.append("⌃")
    if modifiers & kCGEventFlagMaskAlternate:
        parts.append("⌥")
    if modifiers & kCGEventFlagMaskShift:
        parts.append("⇧")
    if modifiers & kCGEventFlagMaskCommand:
        parts.append("⌘")
    key = _KEY_MAP.get(keycode, f"0x{keycode:02X}")
    parts.append(key)
    return "".join(parts)


class ShortcutField(NSTextField):
    """Text field that captures key combinations."""

    def initWithFrame_preferences_(self, frame, prefs):
        return self.initWithFrame_preferences_keycodeKey_modifiersKey_(
            frame,
            prefs,
            "hotkey_keycode",
            "hotkey_modifiers",
        )

    def initWithFrame_preferences_keycodeKey_modifiersKey_(
        self,
        frame,
        prefs,
        keycode_key,
        modifiers_key,
    ):
        self = objc.super(ShortcutField, self).initWithFrame_(frame)
        if self is None:
            return None
        self._prefs = prefs
        self._keycode_key = str(keycode_key)
        self._modifiers_key = str(modifiers_key)
        self._capturing = False
        self._on_change = None
        self.setEditable_(False)
        self.setSelectable_(False)
        self.setBezeled_(True)
        self.setFont_(NSFont.systemFontOfSize_(13.0))
        self._update_display()
        return self

    def _update_display(self):
        if self._capturing:
            self.setStringValue_(t("widgets.press_shortcut"))
        else:
            keycode = getattr(self._prefs, self._keycode_key)
            modifiers = getattr(self._prefs, self._modifiers_key)
            self.setStringValue_(format_shortcut(keycode, modifiers))

    def startCapture(self):
        self._capturing = True
        self._update_display()
        self.window().makeFirstResponder_(self)

    def keyDown_(self, event):
        if not self._capturing:
            return

        keycode = event.keyCode()
        ns_flags = event.modifierFlags()

        if keycode == 0x35:
            self._capturing = False
            self._update_display()
            return

        cg_flags = 0
        if ns_flags & NSEventModifierFlagCommand:
            cg_flags |= kCGEventFlagMaskCommand
        if ns_flags & NSEventModifierFlagShift:
            cg_flags |= kCGEventFlagMaskShift
        if ns_flags & NSEventModifierFlagControl:
            cg_flags |= kCGEventFlagMaskControl
        if ns_flags & NSEventModifierFlagOption:
            cg_flags |= kCGEventFlagMaskAlternate

        if not cg_flags:
            return

        setattr(self._prefs, self._keycode_key, keycode)
        setattr(self._prefs, self._modifiers_key, int(cg_flags))
        self._capturing = False
        self._update_display()
        if self._on_change:
            self._on_change()

    def acceptsFirstResponder(self):
        return True

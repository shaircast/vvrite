"""Shared UI widgets."""

import objc
from vvrite.locales import t
from AppKit import (
    NSColor,
    NSCursor,
    NSDraggingItem,
    NSDragOperationCopy,
    NSFont,
    NSImage,
    NSImageScaleProportionallyUpOrDown,
    NSImageView,
    NSMakeRect,
    NSView,
    NSTextField,
    NSWorkspace,
    NSEventModifierFlagCommand,
    NSEventModifierFlagShift,
    NSEventModifierFlagControl,
    NSEventModifierFlagOption,
    NSEventModifierFlagFunction,
)
from Foundation import NSBundle, NSURL
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
    # Modifier keys — used for modifier-only (push-to-talk) shortcuts. These
    # are stored with modifiers == 0, so the key label alone names the shortcut.
    0x37: "Left ⌘", 0x36: "Right ⌘",
    0x3A: "Left ⌥", 0x3D: "Right ⌥",
    0x38: "Left ⇧", 0x3C: "Right ⇧",
    0x3B: "Left ⌃", 0x3E: "Right ⌃",
    0x3F: "fn",
}

# CGEvent/virtual keycode -> the AppKit device-independent modifier flag that
# becomes set while that physical modifier key is held. Used to detect the
# press (vs release) transition during modifier-only shortcut capture.
_MODIFIER_KEYCODE_FLAG = {
    0x37: NSEventModifierFlagCommand,
    0x36: NSEventModifierFlagCommand,
    0x38: NSEventModifierFlagShift,
    0x3C: NSEventModifierFlagShift,
    0x3A: NSEventModifierFlagOption,
    0x3D: NSEventModifierFlagOption,
    0x3B: NSEventModifierFlagControl,
    0x3E: NSEventModifierFlagControl,
    0x3F: NSEventModifierFlagFunction,
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


def active_shortcut(prefs):
    """Return the (keycode, modifiers) pair for the active recording mode."""
    if prefs.recording_mode == "hold":
        return prefs.ptt_hotkey_keycode, prefs.ptt_hotkey_modifiers
    return prefs.hotkey_keycode, prefs.hotkey_modifiers


def packaged_app_bundle_path() -> str | None:
    """Return the running app bundle path, or None for a source interpreter."""
    bundle = NSBundle.mainBundle()
    path = str(bundle.bundlePath() or "") if bundle is not None else ""
    return path if path.endswith(".app") else None


class AppBundleDragView(NSView):
    """A draggable app-bundle tile with an explicit grab affordance."""

    def initWithFrame_bundlePath_accessibilityLabel_(
        self,
        frame,
        bundle_path,
        accessibility_label,
    ):
        self = objc.super(AppBundleDragView, self).initWithFrame_(frame)
        if self is None:
            return None

        self._bundle_path = str(bundle_path)
        self._bundle_icon = NSWorkspace.sharedWorkspace().iconForFile_(
            self._bundle_path
        )

        self.setWantsLayer_(True)
        layer = self.layer()
        layer.setCornerRadius_(9.0)
        layer.setBackgroundColor_(
            NSColor.labelColor().colorWithAlphaComponent_(0.055).CGColor()
        )
        layer.setBorderWidth_(1.0)
        layer.setBorderColor_(
            NSColor.controlAccentColor().colorWithAlphaComponent_(0.55).CGColor()
        )

        height = frame.size.height
        icon_size = min(30.0, height - 12.0)
        icon_view = NSImageView.alloc().initWithFrame_(
            NSMakeRect(12, (height - icon_size) / 2.0, icon_size, icon_size)
        )
        if self._bundle_icon is not None:
            icon_view.setImage_(self._bundle_icon)
        icon_view.setImageScaling_(NSImageScaleProportionallyUpOrDown)
        self.addSubview_(icon_view)

        hint_height = 18.0
        hint = NSTextField.labelWithString_(accessibility_label)
        hint.setFrame_(
            NSMakeRect(
                54,
                (height - hint_height) / 2.0,
                frame.size.width - 92,
                hint_height,
            )
        )
        hint.setFont_(NSFont.systemFontOfSize_(10.5))
        hint.setTextColor_(NSColor.labelColor())
        self.addSubview_(hint)

        grip = NSImageView.alloc().initWithFrame_(
            NSMakeRect(frame.size.width - 28, (height - 18) / 2.0, 18, 18)
        )
        grip_image = NSImage.imageWithSystemSymbolName_accessibilityDescription_(
            "circle.grid.2x3.fill",
            accessibility_label,
        )
        if grip_image is None:
            grip_image = NSImage.imageWithSystemSymbolName_accessibilityDescription_(
                "line.3.horizontal",
                accessibility_label,
            )
        if grip_image is not None:
            grip.setImage_(grip_image)
        grip.setImageScaling_(NSImageScaleProportionallyUpOrDown)
        grip.setContentTintColor_(NSColor.secondaryLabelColor())
        self.addSubview_(grip)

        self.setToolTip_(accessibility_label)
        self.setAccessibilityLabel_(accessibility_label)
        self.setAccessibilityHelp_(accessibility_label)
        return self

    def resetCursorRects(self):
        self.addCursorRect_cursor_(self.bounds(), NSCursor.openHandCursor())

    def mouseDragged_(self, event):
        bundle_url = NSURL.fileURLWithPath_isDirectory_(self._bundle_path, True)
        item = NSDraggingItem.alloc().initWithPasteboardWriter_(bundle_url)
        icon_size = min(32.0, self.bounds().size.height)
        item.setDraggingFrame_contents_(
            NSMakeRect(12, (self.bounds().size.height - icon_size) / 2.0,
                       icon_size, icon_size),
            self._bundle_icon,
        )
        session = self.beginDraggingSessionWithItems_event_source_(
            [item], event, self
        )
        if session is not None:
            session.setAnimatesToStartingPositionsOnCancelOrFail_(True)

    def draggingSession_sourceOperationMaskForDraggingContext_(
        self,
        session,
        context,
    ):
        return NSDragOperationCopy

    def acceptsFirstMouse_(self, event):
        return True

    def mouseDownCanMoveWindow(self):
        return False


class ShortcutField(NSTextField):
    """Text field that captures key combinations."""

    def initWithFrame_preferences_(self, frame, prefs):
        return self.initWithFrame_preferences_keycodeKey_modifiersKey_(
            frame,
            prefs,
            "hotkey_keycode",
            "hotkey_modifiers",
        )

    def initWithFrame_preferences_keycodeKey_modifiersKey_allowModifierOnly_(
        self,
        frame,
        prefs,
        keycode_key,
        modifiers_key,
        allow_modifier_only,
    ):
        self = self.initWithFrame_preferences_keycodeKey_modifiersKey_(
            frame, prefs, keycode_key, modifiers_key
        )
        if self is not None:
            self._allow_modifier_only = bool(allow_modifier_only)
        return self

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
        # When True, a lone modifier (e.g. Right Command) can be captured as the
        # shortcut. Only the push-to-talk field opts into this.
        self._allow_modifier_only = False
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

    def flagsChanged_(self, event):
        # Capture a lone modifier (e.g. Right Command) as a push-to-talk key.
        # A bare modifier press fires flagsChanged: rather than keyDown:.
        if not self._capturing or not self._allow_modifier_only:
            return

        keycode = event.keyCode()
        flag = _MODIFIER_KEYCODE_FLAG.get(keycode)
        if flag is None:
            return  # not a known modifier key — let keyDown: handle real keys

        # Commit only on the down transition (the modifier's flag is now set);
        # ignore the matching release event.
        if not (event.modifierFlags() & flag):
            return

        setattr(self._prefs, self._keycode_key, keycode)
        setattr(self._prefs, self._modifiers_key, 0)
        self._capturing = False
        self._update_display()
        if self._on_change:
            self._on_change()

    def resignFirstResponder(self):
        # Abort an in-progress capture if focus moves away, so the field never
        # gets stuck showing the "Press shortcut..." prompt.
        if self._capturing:
            self._capturing = False
            self._update_display()
        return objc.super(ShortcutField, self).resignFirstResponder()

    def acceptsFirstResponder(self):
        return True

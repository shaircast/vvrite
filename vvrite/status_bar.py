"""Menu bar status item and dropdown menu."""

import objc
from AppKit import (
    NSObject,
    NSStatusBar,
    NSVariableStatusItemLength,
    NSMenu,
    NSMenuItem,
    NSApp,
    NSImage,
    NSColor,
)

from vvrite.locales import t
from vvrite.widgets import format_shortcut

_READY_STATES = {"ready", "recording", "transcribing"}


class StatusBarController(NSObject):
    def initWithDelegate_(self, delegate):
        self = objc.super(StatusBarController, self).init()
        if self is None:
            return None
        self._delegate = delegate
        self._recording = False
        self._setup()
        return self

    def _setup(self):
        self._status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(
            NSVariableStatusItemLength
        )
        button = self._status_item.button()
        button.setImage_(self._sf_symbol("exclamationmark.triangle"))
        button.setTitle_("")

        self._menu = NSMenu.alloc().init()

        # App title
        title_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "vvrite", None, ""
        )
        title_item.setEnabled_(False)
        self._menu.addItem_(title_item)

        self._menu.addItem_(NSMenuItem.separatorItem())

        # Status
        self._status_menu_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "", None, ""
        )
        self._status_menu_item.setEnabled_(False)
        self._menu.addItem_(self._status_menu_item)
        self.setStatus_("ready")

        self._menu.addItem_(NSMenuItem.separatorItem())

        # Hotkey display
        prefs = self._delegate._prefs
        hotkey_str = format_shortcut(prefs.hotkey_keycode, prefs.hotkey_modifiers)
        self._hotkey_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            t("menu.hotkey", hotkey=hotkey_str), None, ""
        )
        self._hotkey_item.setEnabled_(False)
        self._menu.addItem_(self._hotkey_item)

        # Mic display
        self._mic_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            t("menu.microphone", microphone=t("common.system_default")), None, ""
        )
        self._mic_item.setEnabled_(False)
        self._menu.addItem_(self._mic_item)

        self._menu.addItem_(NSMenuItem.separatorItem())

        # Settings
        settings_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            t("menu.settings"), "openSettings:", ","
        )
        settings_item.setTarget_(self)
        self._menu.addItem_(settings_item)

        # Check for Updates
        self._update_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            t("menu.check_updates"), "checkForUpdates:", ""
        )
        self._update_item.setTarget_(self)
        self._menu.addItem_(self._update_item)

        self._menu.addItem_(NSMenuItem.separatorItem())

        # Quit
        quit_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            t("menu.quit"), "terminate:", "q"
        )
        self._menu.addItem_(quit_item)

        self._status_item.setMenu_(self._menu)

    def _sf_symbol(self, name):
        return NSImage.imageWithSystemSymbolName_accessibilityDescription_(name, None)

    def _update_icon(self, ready: bool):
        button = self._status_item.button()
        if ready:
            button.setImage_(self._sf_symbol("waveform"))
        else:
            button.setImage_(self._sf_symbol("exclamationmark.triangle"))

    def setStatus_(self, status_key: str):
        """Set status using a key (e.g. 'ready', 'recording'). Translates internally."""
        display_text = t(f"status.{status_key}")
        self._status_menu_item.setTitle_(f"● {display_text}")
        self._update_icon(status_key in _READY_STATES)

    def setRecording_(self, recording: bool):
        self._recording = recording

    def setDownloadProgress_(self, percent: int):
        """Show download percentage on menu bar button. -1 to clear."""
        button = self._status_item.button()
        if percent < 0:
            button.setTitle_("")
        else:
            button.setTitle_(f"{percent}%")

    def setUpdateAvailable_(self, version: str):
        """Update menu item text when an update is available."""
        self._update_item.setTitle_(t("menu.update_available", version=version))

    def setHotkeyDisplay_(self, hotkey_str: str):
        self._hotkey_item.setTitle_(t("menu.hotkey", hotkey=hotkey_str))

    def setMicDisplay_(self, device_name: str | None):
        display = device_name or t("common.system_default")
        self._mic_item.setTitle_(t("menu.microphone", microphone=display))

    @objc.typedSelector(b"v@:@")
    def openSettings_(self, sender):
        self._delegate.openSettings()

    @objc.typedSelector(b"v@:@")
    def checkForUpdates_(self, sender):
        self._delegate.checkForUpdates()

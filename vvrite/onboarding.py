"""First-run onboarding wizard."""

import threading

import objc
import ApplicationServices
import AVFoundation
from AppKit import (
    NSObject,
    NSMakeRect,
    NSWindow,
    NSWindowStyleMaskTitled,
    NSWindowStyleMaskClosable,
    NSBackingStoreBuffered,
    NSTextField,
    NSFont,
    NSFontWeightRegular,
    NSButton,
    NSButtonTypeSwitch,
    NSColor,
    NSApp,
    NSBezelStyleRounded,
    NSView,
    NSImage,
    NSImageView,
    NSImageScaleProportionallyUpOrDown,
    NSImageSymbolConfiguration,
    NSPopUpButton,
    NSProgressIndicator,
    NSProgressIndicatorStyleBar,
    NSSegmentedControl,
    NSWorkspace,
)
from Foundation import NSURL, NSTimer

from vvrite.locales import t, set_locale, SUPPORTED_LANGUAGES
from vvrite.widgets import AppBundleDragView, ShortcutField, packaged_app_bundle_path
from vvrite import transcriber

# Window dimensions
_WIDTH = 460
_HEIGHT = 430
_MARGIN = 32
_CONTENT_W = _WIDTH - 2 * _MARGIN

# Step indices
_WELCOME = 0
_PERMISSIONS = 1
_HOTKEY = 2
_RETRACT = 3
_MODEL = 4
_NUM_STEPS = 5

# SF Symbol shown in each step header.
_STEP_SYMBOLS = {
    _WELCOME: "waveform",
    _PERMISSIONS: "lock.shield",
    _HOTKEY: "keyboard",
    _RETRACT: "arrow.uturn.backward",
    _MODEL: "arrow.down.circle",
}


class OnboardingWindowController(NSObject):
    def initWithPreferences_statusBar_onComplete_(self, prefs, status_bar, on_complete):
        self = objc.super(OnboardingWindowController, self).init()
        if self is None:
            return None
        self._prefs = prefs
        self._status_bar = status_bar
        self._on_complete = on_complete
        self._step = _WELCOME
        self._window = None
        self._content_area = None
        self._dots = []
        self._back_btn = None
        self._next_btn = None
        self._permission_timer = None
        self._shortcut_field = None
        self._ptt_shortcut_field = None
        self._mode_segmented = None
        self._mode_hint_label = None
        self._retract_checkbox = None
        self._retract_shortcut_field = None
        self._retract_change_btn = None
        self._progress_bar = None
        self._progress_label = None
        self._size_label = None
        self._error_label = None
        self._retry_btn = None
        self._download_btn = None
        self._load_retries = 0
        self._local_model_path = None
        self._lang_popup = None
        self._acc_status = None
        self._mic_status = None
        self._app_drag_view = None
        self._build_window()
        return self

    # --- Window ---

    def _build_window(self):
        frame = NSMakeRect(0, 0, _WIDTH, _HEIGHT)
        self._window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame,
            NSWindowStyleMaskTitled | NSWindowStyleMaskClosable,
            NSBackingStoreBuffered,
            False,
        )
        self._window.setTitle_("vvrite")
        self._window.center()
        self._window.setDelegate_(self)

        root = self._window.contentView()

        # Step indicator (capsule pills) near the top.
        for _ in range(_NUM_STEPS):
            pill = NSView.alloc().initWithFrame_(NSMakeRect(0, _HEIGHT - 30, 6, 6))
            pill.setWantsLayer_(True)
            pill.layer().setCornerRadius_(3.0)
            root.addSubview_(pill)
            self._dots.append(pill)

        # Content area
        self._content_area = NSView.alloc().initWithFrame_(
            NSMakeRect(0, 56, _WIDTH, _HEIGHT - 100)
        )
        root.addSubview_(self._content_area)

        # Back / Next buttons
        self._back_btn = NSButton.alloc().initWithFrame_(NSMakeRect(_MARGIN, 18, 88, 32))
        self._back_btn.setTitle_(t("common.back"))
        self._back_btn.setBezelStyle_(NSBezelStyleRounded)
        self._back_btn.setTarget_(self)
        self._back_btn.setAction_("backClicked:")
        root.addSubview_(self._back_btn)

        self._next_btn = NSButton.alloc().initWithFrame_(
            NSMakeRect(_WIDTH - _MARGIN - 110, 18, 110, 32)
        )
        self._next_btn.setTitle_(t("common.get_started"))
        self._next_btn.setBezelStyle_(NSBezelStyleRounded)
        self._next_btn.setKeyEquivalent_("\r")  # Return triggers Next
        self._next_btn.setTarget_(self)
        self._next_btn.setAction_("nextClicked:")
        root.addSubview_(self._next_btn)

        self._show_step(_WELCOME)

    def show(self):
        self._window.makeKeyAndOrderFront_(None)
        NSApp.activateIgnoringOtherApps_(True)

    def windowWillClose_(self, notification):
        if self._permission_timer:
            self._permission_timer.invalidate()
            self._permission_timer = None
        NSApp.terminate_(None)

    # --- Shared building blocks ---

    def _symbol_image(self, symbol, point_size):
        img = NSImage.imageWithSystemSymbolName_accessibilityDescription_(symbol, None)
        if img is None:
            return None
        cfg = NSImageSymbolConfiguration.configurationWithPointSize_weight_(
            point_size, NSFontWeightRegular
        )
        configured = img.imageWithSymbolConfiguration_(cfg)
        return configured if configured is not None else img

    def _add_header(self, area, symbol, title_text, subtitle_text,
                    icon_size=46, title_size=20):
        """Place a centered icon + title + subtitle at the top of the content
        area. Returns the y baseline below which step controls can be placed."""
        ch = area.frame().size.height
        icon_y = ch - 14 - icon_size
        icon_view = NSImageView.alloc().initWithFrame_(
            NSMakeRect((_WIDTH - icon_size) / 2.0, icon_y, icon_size, icon_size)
        )
        img = self._symbol_image(symbol, icon_size * 0.6)
        if img is not None:
            icon_view.setImage_(img)
        icon_view.setImageScaling_(NSImageScaleProportionallyUpOrDown)
        icon_view.setContentTintColor_(NSColor.controlAccentColor())
        area.addSubview_(icon_view)

        title_h = title_size + 8
        title_y = icon_y - 10 - title_h
        title = NSTextField.labelWithString_(title_text)
        title.setFrame_(NSMakeRect(0, title_y, _WIDTH, title_h))
        title.setFont_(NSFont.boldSystemFontOfSize_(title_size))
        title.setAlignment_(1)
        area.addSubview_(title)

        sub_y = title_y - 24
        subtitle = NSTextField.labelWithString_(subtitle_text)
        subtitle.setFrame_(NSMakeRect(_MARGIN, sub_y, _CONTENT_W, 20))
        subtitle.setFont_(NSFont.systemFontOfSize_(13.0))
        subtitle.setTextColor_(NSColor.secondaryLabelColor())
        subtitle.setAlignment_(1)
        area.addSubview_(subtitle)
        return sub_y - 18

    def _make_card(self, area, rect):
        card = NSView.alloc().initWithFrame_(rect)
        card.setWantsLayer_(True)
        layer = card.layer()
        layer.setCornerRadius_(10.0)
        layer.setBackgroundColor_(
            NSColor.labelColor().colorWithAlphaComponent_(0.04).CGColor()
        )
        layer.setBorderWidth_(1.0)
        layer.setBorderColor_(NSColor.separatorColor().CGColor())
        area.addSubview_(card)
        return card

    # --- Navigation ---

    def _show_step(self, step):
        self._step = step
        self._update_dots()

        # Clear content area + drop stale per-step control references.
        for sub in list(self._content_area.subviews()):
            sub.removeFromSuperview()
        self._lang_popup = None
        self._mode_segmented = None
        self._shortcut_field = None
        self._ptt_shortcut_field = None
        self._mode_hint_label = None
        self._retract_checkbox = None
        self._retract_shortcut_field = None
        self._retract_change_btn = None
        self._acc_status = None
        self._mic_status = None
        self._app_drag_view = None

        # Stop permission timer if leaving permissions step
        if step != _PERMISSIONS and self._permission_timer:
            self._permission_timer.invalidate()
            self._permission_timer = None

        builders = {
            _WELCOME: self._build_welcome,
            _PERMISSIONS: self._build_permissions,
            _HOTKEY: self._build_hotkey,
            _RETRACT: self._build_retract,
            _MODEL: self._build_model,
        }
        builders[step]()
        self._update_buttons()

    def _update_dots(self):
        n = len(self._dots)
        widths = [22 if i == self._step else 7 for i in range(n)]
        gap = 6
        total = sum(widths) + gap * (n - 1)
        x = (_WIDTH - total) / 2.0
        y = _HEIGHT - 30
        accent = NSColor.controlAccentColor()
        done = accent.colorWithAlphaComponent_(0.45)
        future = NSColor.tertiaryLabelColor()
        for i, pill in enumerate(self._dots):
            w = widths[i]
            pill.setFrame_(NSMakeRect(x, y, w, 7))
            if i == self._step:
                color = accent
            elif i < self._step:
                color = done
            else:
                color = future
            pill.layer().setBackgroundColor_(color.CGColor())
            x += w + gap

    def _update_buttons(self):
        # Back button
        self._back_btn.setHidden_(self._step == _WELCOME)

        # Next button label
        labels = {
            _WELCOME: t("common.get_started"),
            _PERMISSIONS: t("common.next"),
            _HOTKEY: t("common.next"),
            _RETRACT: t("common.next"),
            _MODEL: t("common.done"),
        }
        self._next_btn.setTitle_(labels[self._step])

        # Next button enabled state
        if self._step == _PERMISSIONS:
            self._next_btn.setEnabled_(self._all_permissions_granted())
        elif self._step == _MODEL:
            self._next_btn.setEnabled_(transcriber.is_model_loaded())
        else:
            self._next_btn.setEnabled_(True)

    @objc.typedSelector(b"v@:@")
    def backClicked_(self, sender):
        if self._step > _WELCOME:
            self._show_step(self._step - 1)

    @objc.typedSelector(b"v@:@")
    def nextClicked_(self, sender):
        if self._step < _MODEL:
            self._show_step(self._step + 1)
        else:
            # Done — finish onboarding
            self._prefs.onboarding_completed = True
            if self._permission_timer:
                self._permission_timer.invalidate()
                self._permission_timer = None
            self._window.setDelegate_(None)
            self._window.close()
            self._on_complete()

    # --- Step 1: Welcome ---

    def _build_welcome(self):
        area = self._content_area
        controls_top = self._add_header(
            area,
            _STEP_SYMBOLS[_WELCOME],
            "vvrite",
            t("onboarding.welcome.subtitle"),
            icon_size=58,
            title_size=26,
        )

        caption = NSTextField.labelWithString_(t("onboarding.language.title"))
        caption.setFrame_(NSMakeRect(0, controls_top - 26, _WIDTH, 16))
        caption.setFont_(NSFont.systemFontOfSize_(11.0))
        caption.setTextColor_(NSColor.secondaryLabelColor())
        caption.setAlignment_(1)
        area.addSubview_(caption)

        self._lang_popup = NSPopUpButton.alloc().initWithFrame_pullsDown_(
            NSMakeRect((_WIDTH - 240) / 2.0, controls_top - 58, 240, 26), False
        )
        self._lang_popup.addItemWithTitle_(t("common.system_default"))
        for code, native_name in SUPPORTED_LANGUAGES:
            self._lang_popup.addItemWithTitle_(native_name)

        current = self._prefs.ui_language
        if current is None:
            self._lang_popup.selectItemAtIndex_(0)
        else:
            for i, (code, _) in enumerate(SUPPORTED_LANGUAGES):
                if code == current:
                    self._lang_popup.selectItemAtIndex_(i + 1)
                    break
        self._lang_popup.setTarget_(self)
        self._lang_popup.setAction_("onboardingLanguageChanged:")
        area.addSubview_(self._lang_popup)

    @objc.typedSelector(b"v@:@")
    def onboardingLanguageChanged_(self, sender):
        index = sender.indexOfSelectedItem()
        if index == 0:
            self._prefs.ui_language = None
            from vvrite.locales import resolve_system_locale
            set_locale(resolve_system_locale())
        else:
            code = SUPPORTED_LANGUAGES[index - 1][0]
            self._prefs.ui_language = code
            set_locale(code)

        # Refresh persistent buttons and current step
        self._back_btn.setTitle_(t("common.back"))
        self._show_step(self._step)

    # --- Step 2: Permissions ---

    def _all_permissions_granted(self):
        ax_ok = ApplicationServices.AXIsProcessTrusted()
        mic_ok = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        ) == 3
        return ax_ok and mic_ok

    def _build_permissions(self):
        area = self._content_area
        self._add_header(
            area,
            _STEP_SYMBOLS[_PERMISSIONS],
            t("onboarding.permissions.title"),
            t("onboarding.permissions.accessibility_desc"),
        )

        self._acc_status = self._build_permission_card(
            area, 128,
            t("onboarding.permissions.accessibility"),
            t("onboarding.permissions.accessibility_desc"),
            "openAccessibility:",
        )
        self._mic_status = self._build_permission_card(
            area, 56,
            t("onboarding.permissions.microphone"),
            t("onboarding.permissions.microphone_desc"),
            "openMicrophonePrivacy:",
        )

        bundle_path = packaged_app_bundle_path()
        if bundle_path:
            self._build_app_drag_item(area, bundle_path)

        self._update_permission_status()
        self._permission_timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            2.0, self, "pollPermissions:", None, True
        )

    def _build_app_drag_item(self, area, bundle_path):
        drag_label = t("onboarding.permissions.drag_hint")
        self._app_drag_view = (
            AppBundleDragView.alloc()
            .initWithFrame_bundlePath_accessibilityLabel_(
                NSMakeRect(_MARGIN, 0, _CONTENT_W, 44),
                bundle_path,
                drag_label,
            )
        )
        area.addSubview_(self._app_drag_view)

    def _build_permission_card(self, area, card_y, title_text, desc_text, button_action):
        card = self._make_card(area, NSMakeRect(_MARGIN, card_y, _CONTENT_W, 60))

        title = NSTextField.labelWithString_(title_text)
        title.setFrame_(NSMakeRect(18, 32, 200, 20))
        title.setFont_(NSFont.boldSystemFontOfSize_(13.0))
        card.addSubview_(title)

        desc = NSTextField.labelWithString_(desc_text)
        desc.setFrame_(NSMakeRect(18, 11, 240, 16))
        desc.setFont_(NSFont.systemFontOfSize_(11.0))
        desc.setTextColor_(NSColor.secondaryLabelColor())
        card.addSubview_(desc)

        btn = NSButton.alloc().initWithFrame_(
            NSMakeRect(_CONTENT_W - 18 - 72, 17, 72, 26)
        )
        btn.setTitle_(t("common.open"))
        btn.setBezelStyle_(NSBezelStyleRounded)
        btn.setTarget_(self)
        btn.setAction_(button_action)
        card.addSubview_(btn)

        status = NSTextField.labelWithString_("")
        status.setFrame_(
            NSMakeRect(_CONTENT_W - 18 - 72 - 8 - 96, 20, 96, 18)
        )
        status.setFont_(NSFont.systemFontOfSize_(11.0))
        status.setAlignment_(2)  # right
        card.addSubview_(status)
        return status

    def _update_permission_status(self):
        if self._acc_status is None or self._mic_status is None:
            return
        ax_ok = ApplicationServices.AXIsProcessTrusted()
        mic_ok = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        ) == 3

        self._acc_status.setStringValue_(
            t("onboarding.permissions.granted") if ax_ok
            else t("onboarding.permissions.not_granted")
        )
        self._acc_status.setTextColor_(
            NSColor.systemGreenColor() if ax_ok else NSColor.systemRedColor()
        )
        self._mic_status.setStringValue_(
            t("onboarding.permissions.granted") if mic_ok
            else t("onboarding.permissions.not_granted")
        )
        self._mic_status.setTextColor_(
            NSColor.systemGreenColor() if mic_ok else NSColor.systemRedColor()
        )
        self._update_buttons()

    @objc.typedSelector(b"v@:@")
    def pollPermissions_(self, timer):
        if self._step == _PERMISSIONS:
            self._update_permission_status()

    @objc.typedSelector(b"v@:@")
    def openAccessibility_(self, sender):
        url = NSURL.URLWithString_(
            "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
        )
        NSWorkspace.sharedWorkspace().openURL_(url)

    @objc.typedSelector(b"v@:@")
    def openMicrophonePrivacy_(self, sender):
        status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        )
        if status == 0:  # NotDetermined — trigger system dialog
            AVFoundation.AVCaptureDevice.requestAccessForMediaType_completionHandler_(
                AVFoundation.AVMediaTypeAudio, lambda granted: None
            )
        else:  # Denied/Restricted — open System Settings
            url = NSURL.URLWithString_(
                "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone"
            )
            NSWorkspace.sharedWorkspace().openURL_(url)

    # --- Step 3: Recording mode + hotkey ---

    def _build_hotkey(self):
        area = self._content_area
        self._add_header(
            area,
            _STEP_SYMBOLS[_HOTKEY],
            t("settings.recording.title"),
            t("onboarding.hotkey.subtitle"),
        )

        self._mode_segmented = NSSegmentedControl.alloc().initWithFrame_(
            NSMakeRect((_WIDTH - 280) / 2.0, 150, 280, 26)
        )
        self._mode_segmented.setSegmentCount_(2)
        self._mode_segmented.setLabel_forSegment_(t("settings.recording.toggle"), 0)
        self._mode_segmented.setLabel_forSegment_(t("settings.recording.push_to_talk"), 1)
        self._mode_segmented.setWidth_forSegment_(140, 0)
        self._mode_segmented.setWidth_forSegment_(140, 1)
        self._mode_segmented.setTarget_(self)
        self._mode_segmented.setAction_("recordingModeChanged:")
        area.addSubview_(self._mode_segmented)

        group_x = (_WIDTH - 288) / 2.0
        self._shortcut_field = ShortcutField.alloc().initWithFrame_preferences_(
            NSMakeRect(group_x, 102, 200, 30), self._prefs
        )
        self._shortcut_field.setFont_(NSFont.monospacedSystemFontOfSize_weight_(18.0, 0.5))
        self._shortcut_field.setAlignment_(1)
        area.addSubview_(self._shortcut_field)

        self._ptt_shortcut_field = (
            ShortcutField.alloc()
            .initWithFrame_preferences_keycodeKey_modifiersKey_allowModifierOnly_(
                NSMakeRect(group_x, 102, 200, 30),
                self._prefs,
                "ptt_hotkey_keycode",
                "ptt_hotkey_modifiers",
                True,
            )
        )
        self._ptt_shortcut_field.setFont_(NSFont.monospacedSystemFontOfSize_weight_(18.0, 0.5))
        self._ptt_shortcut_field.setAlignment_(1)
        area.addSubview_(self._ptt_shortcut_field)

        change_btn = NSButton.alloc().initWithFrame_(
            NSMakeRect(group_x + 208, 103, 80, 28)
        )
        change_btn.setTitle_(t("common.change"))
        change_btn.setBezelStyle_(NSBezelStyleRounded)
        change_btn.setTarget_(self)
        change_btn.setAction_("changeShortcut:")
        area.addSubview_(change_btn)

        self._mode_hint_label = NSTextField.labelWithString_("")
        self._mode_hint_label.setFrame_(NSMakeRect(_MARGIN, 60, _CONTENT_W, 20))
        self._mode_hint_label.setFont_(NSFont.systemFontOfSize_(12.0))
        self._mode_hint_label.setTextColor_(NSColor.secondaryLabelColor())
        self._mode_hint_label.setAlignment_(1)
        area.addSubview_(self._mode_hint_label)

        self._apply_onboarding_mode_ui()

    @objc.typedSelector(b"v@:@")
    def recordingModeChanged_(self, sender):
        self._prefs.recording_mode = "hold" if sender.selectedSegment() == 1 else "toggle"
        self._apply_onboarding_mode_ui()

    def _apply_onboarding_mode_ui(self):
        hold = self._prefs.recording_mode == "hold"
        if self._mode_segmented is not None:
            self._mode_segmented.setSelectedSegment_(1 if hold else 0)
        if self._shortcut_field is not None:
            self._shortcut_field.setHidden_(hold)
        if self._ptt_shortcut_field is not None:
            self._ptt_shortcut_field.setHidden_(not hold)
        if self._mode_hint_label is not None:
            self._mode_hint_label.setStringValue_(
                t("settings.recording.ptt_hint") if hold
                else t("settings.recording.toggle_hint")
            )

    @objc.typedSelector(b"v@:@")
    def changeShortcut_(self, sender):
        if self._prefs.recording_mode == "hold":
            self._ptt_shortcut_field.startCapture()
        else:
            self._shortcut_field.startCapture()

    # --- Step 4: Retract ---

    def _build_retract(self):
        area = self._content_area
        self._add_header(
            area,
            _STEP_SYMBOLS[_RETRACT],
            t("onboarding.retract.title"),
            t("onboarding.retract.subtitle"),
        )

        self._retract_checkbox = NSButton.alloc().initWithFrame_(
            NSMakeRect(_MARGIN + 20, 150, _CONTENT_W - 40, 20)
        )
        self._retract_checkbox.setButtonType_(NSButtonTypeSwitch)
        self._retract_checkbox.setTitle_(t("onboarding.retract.enable"))
        self._retract_checkbox.setState_(
            1 if self._prefs.retract_last_dictation_enabled else 0
        )
        self._retract_checkbox.setTarget_(self)
        self._retract_checkbox.setAction_("retractShortcutToggled:")
        area.addSubview_(self._retract_checkbox)

        group_x = (_WIDTH - 288) / 2.0
        self._retract_shortcut_field = (
            ShortcutField.alloc().initWithFrame_preferences_keycodeKey_modifiersKey_(
                NSMakeRect(group_x, 104, 200, 30),
                self._prefs,
                "retract_hotkey_keycode",
                "retract_hotkey_modifiers",
            )
        )
        self._retract_shortcut_field.setFont_(
            NSFont.monospacedSystemFontOfSize_weight_(18.0, 0.5)
        )
        self._retract_shortcut_field.setAlignment_(1)
        area.addSubview_(self._retract_shortcut_field)

        self._retract_change_btn = NSButton.alloc().initWithFrame_(
            NSMakeRect(group_x + 208, 105, 80, 28)
        )
        self._retract_change_btn.setTitle_(t("common.change"))
        self._retract_change_btn.setBezelStyle_(NSBezelStyleRounded)
        self._retract_change_btn.setTarget_(self)
        self._retract_change_btn.setAction_("changeRetractShortcut:")
        area.addSubview_(self._retract_change_btn)

        hint = NSTextField.labelWithString_(t("onboarding.retract.hint"))
        hint.setFrame_(NSMakeRect(_MARGIN, 66, _CONTENT_W, 16))
        hint.setFont_(NSFont.systemFontOfSize_(11.0))
        hint.setTextColor_(NSColor.secondaryLabelColor())
        hint.setAlignment_(1)
        area.addSubview_(hint)

        self._refresh_retract_controls()

    @objc.typedSelector(b"v@:@")
    def retractShortcutToggled_(self, sender):
        self._prefs.retract_last_dictation_enabled = sender.state() == 1
        self._refresh_retract_controls()

    @objc.typedSelector(b"v@:@")
    def changeRetractShortcut_(self, sender):
        self._retract_shortcut_field.startCapture()

    def _refresh_retract_controls(self):
        enabled = bool(self._prefs.retract_last_dictation_enabled)
        if self._retract_checkbox is not None:
            self._retract_checkbox.setState_(1 if enabled else 0)
        if self._retract_shortcut_field is not None:
            self._retract_shortcut_field.setEnabled_(enabled)
        if self._retract_change_btn is not None:
            self._retract_change_btn.setEnabled_(enabled)

    # --- Step 5: Model Download ---

    def _build_model(self):
        area = self._content_area
        self._add_header(
            area,
            _STEP_SYMBOLS[_MODEL],
            t("onboarding.model.title"),
            self._prefs.model_id,
        )

        # Size label
        self._size_label = NSTextField.labelWithString_(t("onboarding.model.checking_size"))
        self._size_label.setFrame_(NSMakeRect(_MARGIN, 150, _CONTENT_W, 18))
        self._size_label.setFont_(NSFont.systemFontOfSize_(11.0))
        self._size_label.setTextColor_(NSColor.secondaryLabelColor())
        self._size_label.setAlignment_(1)
        area.addSubview_(self._size_label)

        # Progress bar (hidden initially)
        self._progress_bar = NSProgressIndicator.alloc().initWithFrame_(
            NSMakeRect(_MARGIN, 120, _CONTENT_W, 8)
        )
        self._progress_bar.setStyle_(NSProgressIndicatorStyleBar)
        self._progress_bar.setMinValue_(0.0)
        self._progress_bar.setMaxValue_(100.0)
        self._progress_bar.setHidden_(True)
        area.addSubview_(self._progress_bar)

        # Progress text
        self._progress_label = NSTextField.labelWithString_("")
        self._progress_label.setFrame_(NSMakeRect(_MARGIN, 98, _CONTENT_W, 18))
        self._progress_label.setFont_(NSFont.systemFontOfSize_(11.0))
        self._progress_label.setTextColor_(NSColor.secondaryLabelColor())
        self._progress_label.setAlignment_(1)
        self._progress_label.setHidden_(True)
        area.addSubview_(self._progress_label)

        # Error label (hidden)
        self._error_label = NSTextField.labelWithString_("")
        self._error_label.setFrame_(NSMakeRect(_MARGIN, 74, _CONTENT_W, 18))
        self._error_label.setFont_(NSFont.systemFontOfSize_(11.0))
        self._error_label.setTextColor_(NSColor.systemRedColor())
        self._error_label.setAlignment_(1)
        self._error_label.setHidden_(True)
        area.addSubview_(self._error_label)

        # Download button
        self._download_btn = NSButton.alloc().initWithFrame_(
            NSMakeRect((_WIDTH - 120) / 2.0, 18, 120, 32)
        )
        self._download_btn.setTitle_(t("common.download"))
        self._download_btn.setBezelStyle_(NSBezelStyleRounded)
        self._download_btn.setTarget_(self)
        self._download_btn.setAction_("downloadClicked:")
        area.addSubview_(self._download_btn)

        # Retry button (hidden)
        self._retry_btn = NSButton.alloc().initWithFrame_(
            NSMakeRect((_WIDTH - 90) / 2.0, 18, 90, 32)
        )
        self._retry_btn.setTitle_(t("common.retry"))
        self._retry_btn.setBezelStyle_(NSBezelStyleRounded)
        self._retry_btn.setTarget_(self)
        self._retry_btn.setAction_("downloadClicked:")
        self._retry_btn.setHidden_(True)
        area.addSubview_(self._retry_btn)

        # If the model is already loaded (e.g. navigating back), reflect that.
        if transcriber.is_model_loaded():
            self._download_btn.setHidden_(True)
            self._progress_label.setHidden_(False)
            self._progress_label.setStringValue_(t("onboarding.model.ready"))

        # Check model size in background
        threading.Thread(target=self._fetch_model_size, daemon=True).start()

    def _fetch_model_size(self):
        size = transcriber.get_model_size(self._prefs.model_id)
        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "updateSizeLabel:", str(size), False
        )

    @objc.typedSelector(b"v@:@")
    def updateSizeLabel_(self, size_str):
        if self._size_label is None:
            return
        size = int(size_str)
        if size > 0:
            gb = size / (1024 ** 3)
            self._size_label.setStringValue_(t("onboarding.model.size_gb", size_gb=gb))
        else:
            self._size_label.setStringValue_(t("onboarding.model.size_unknown"))

    @objc.typedSelector(b"v@:@")
    def downloadClicked_(self, sender):
        self._download_btn.setHidden_(True)
        self._retry_btn.setHidden_(True)
        self._error_label.setHidden_(True)
        self._progress_bar.setHidden_(False)
        self._progress_bar.setIndeterminate_(True)
        self._progress_bar.startAnimation_(None)
        self._progress_label.setHidden_(False)
        self._progress_label.setStringValue_(t("onboarding.model.downloading"))
        threading.Thread(target=self._do_download, daemon=True).start()

    def _do_download(self):
        model_id = self._prefs.model_id
        try:
            local_path = transcriber.download_model(model_id)
        except Exception as e:
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "downloadFailed:", str(e), False
            )
            return

        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "downloadComplete:", local_path, False
        )

    @objc.typedSelector(b"v@:@")
    def downloadFailed_(self, error_msg):
        self._progress_bar.setHidden_(True)
        self._progress_label.setHidden_(True)
        self._error_label.setStringValue_(str(error_msg))
        self._error_label.setHidden_(False)
        self._retry_btn.setAction_("downloadClicked:")
        self._retry_btn.setHidden_(False)
        self._status_bar.setDownloadProgress_(-1)

    @objc.typedSelector(b"v@:@")
    def downloadComplete_(self, local_path):
        self._local_model_path = str(local_path)
        self._progress_label.setStringValue_(t("onboarding.model.loading"))
        threading.Thread(
            target=self._do_load_model,
            args=(self._local_model_path,),
            daemon=True,
        ).start()

    def _do_load_model(self, local_path):
        try:
            transcriber.load_from_local(local_path)
        except Exception as e:
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "modelLoadFailed:", str(e), False
            )
            return
        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "modelLoadComplete:", None, False
        )

    @objc.typedSelector(b"v@:@")
    def modelLoadFailed_(self, error_msg):
        self._load_retries += 1
        self._progress_bar.setIndeterminate_(False)
        self._progress_bar.stopAnimation_(None)
        if self._load_retries >= 3:
            self._progress_bar.setHidden_(True)
            self._progress_label.setHidden_(True)
            self._error_label.setStringValue_(t("onboarding.model.failed_after_retries"))
            self._error_label.setHidden_(False)
            return
        self._progress_bar.setHidden_(True)
        self._progress_label.setHidden_(True)
        self._error_label.setStringValue_(str(error_msg))
        self._error_label.setHidden_(False)
        self._retry_btn.setAction_("retryLoad:")
        self._retry_btn.setHidden_(False)

    @objc.typedSelector(b"v@:@")
    def retryLoad_(self, sender):
        if self._local_model_path is None:
            return
        self._retry_btn.setHidden_(True)
        self._error_label.setHidden_(True)
        self._progress_bar.setHidden_(False)
        self._progress_bar.setIndeterminate_(True)
        self._progress_bar.startAnimation_(None)
        self._progress_label.setStringValue_(t("onboarding.model.loading"))
        self._progress_label.setHidden_(False)
        threading.Thread(
            target=self._do_load_model,
            args=(self._local_model_path,),
            daemon=True,
        ).start()

    @objc.typedSelector(b"v@:@")
    def modelLoadComplete_(self, _):
        self._load_retries = 0
        self._progress_bar.setIndeterminate_(False)
        self._progress_bar.stopAnimation_(None)
        self._progress_bar.setDoubleValue_(100.0)
        self._progress_label.setStringValue_(t("onboarding.model.ready"))
        self._update_buttons()

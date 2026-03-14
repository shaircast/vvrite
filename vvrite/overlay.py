"""Floating overlay panel for recording/transcribing state."""

import random
import time

import objc
from AppKit import (
    NSObject,
    NSPanel,
    NSColor,
    NSView,
    NSTextField,
    NSFont,
    NSScreen,
    NSTimer,
    NSVisualEffectView,
    NSVisualEffectMaterialHUDWindow,
    NSVisualEffectBlendingModeBehindWindow,
    NSWindowStyleMaskBorderless,
    NSWindowStyleMaskNonactivatingPanel,
    NSFloatingWindowLevel,
    NSBackingStoreBuffered,
    NSProgressIndicator,
    NSProgressIndicatorSpinningStyle,
    NSCenterTextAlignment,
    NSAppearance,
)
from Foundation import NSMakeRect

# Panel dimensions
W = 220
H = 44
CY = H / 2  # vertical center

# Recording layout: [dot 10] 8 [timer 44] 12 [bars 38]  = 112
REC_W = 10 + 8 + 44 + 12 + 38  # 112
REC_X0 = (W - REC_W) / 2  # left edge of centered group

# Transcribing layout: [spinner 16] 8 [label ~100]
TRANS_W = 16 + 8 + 100  # 124
TRANS_X0 = (W - TRANS_W) / 2


class OverlayController(NSObject):
    def init(self):
        self = objc.super(OverlayController, self).init()
        if self is None:
            return None
        self._panel = None
        self._timer_label = None
        self._level_bars = []
        self._status_label = None
        self._spinner = None
        self._dot = None
        self._record_start_time = 0
        self._update_timer = None
        self._current_level = 0.0
        self._level_history = [0.0] * 8
        self._setup_panel()
        return self

    def _setup_panel(self):
        frame = NSMakeRect(0, 0, W, H)

        self._panel = NSPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            frame,
            NSWindowStyleMaskBorderless | NSWindowStyleMaskNonactivatingPanel,
            NSBackingStoreBuffered,
            False,
        )
        self._panel.setLevel_(NSFloatingWindowLevel)
        self._panel.setOpaque_(False)
        self._panel.setBackgroundColor_(NSColor.clearColor())
        self._panel.setHasShadow_(True)
        self._panel.setAlphaValue_(0.0)
        self._panel.setCollectionBehavior_(
            (1 << 1)  # NSWindowCollectionBehaviorMoveToActiveSpace
            | (1 << 8)  # NSWindowCollectionBehaviorFullScreenAuxiliary
        )

        # Visual effect background
        effect = NSVisualEffectView.alloc().initWithFrame_(frame)
        effect.setMaterial_(NSVisualEffectMaterialHUDWindow)
        effect.setBlendingMode_(NSVisualEffectBlendingModeBehindWindow)
        effect.setState_(1)  # NSVisualEffectStateActive
        effect.setAppearance_(NSAppearance.appearanceNamed_("NSAppearanceNameVibrantDark"))
        effect.setWantsLayer_(True)
        effect.layer().setCornerRadius_(16.0)
        effect.layer().setMasksToBounds_(True)
        effect.layer().setBackgroundColor_(
            NSColor.colorWithRed_green_blue_alpha_(0.0, 0.0, 0.0, 0.35).CGColor()
        )
        self._panel.contentView().addSubview_(effect)

        # --- Recording elements (centered as a group) ---
        x = REC_X0

        # Dot (10x10)
        dot_size = 10
        self._dot = NSView.alloc().initWithFrame_(
            NSMakeRect(x, CY - dot_size / 2, dot_size, dot_size)
        )
        self._dot.setWantsLayer_(True)
        self._dot.layer().setCornerRadius_(dot_size / 2)
        self._dot.layer().setBackgroundColor_(NSColor.redColor().CGColor())
        self._panel.contentView().addSubview_(self._dot)
        x += dot_size + 8

        # Timer label
        timer_w = 44
        timer_h = 20
        self._timer_label = NSTextField.labelWithString_("0:00")
        self._timer_label.setFrame_(NSMakeRect(x, CY - timer_h / 2, timer_w, timer_h))
        self._timer_label.setFont_(NSFont.monospacedDigitSystemFontOfSize_weight_(14.0, 0.5))
        self._timer_label.setTextColor_(NSColor.whiteColor())
        self._timer_label.setBezeled_(False)
        self._timer_label.setDrawsBackground_(False)
        self._timer_label.setEditable_(False)
        self._timer_label.setSelectable_(False)
        self._panel.contentView().addSubview_(self._timer_label)
        x += timer_w + 12

        # Level bars (8 bars, 3px wide, 5px spacing)
        bar_w = 3
        bar_spacing = 5
        for i in range(8):
            bar_h = 16
            bar = NSView.alloc().initWithFrame_(
                NSMakeRect(x + i * bar_spacing, CY - bar_h / 2, bar_w, bar_h)
            )
            bar.setWantsLayer_(True)
            bar.layer().setCornerRadius_(1.5)
            bar.layer().setBackgroundColor_(NSColor.redColor().CGColor())
            self._level_bars.append(bar)
            self._panel.contentView().addSubview_(bar)

        # --- Transcribing/error elements (centered as a group) ---
        tx = TRANS_X0

        # Spinner (16x16)
        spinner_size = 16
        self._spinner = NSProgressIndicator.alloc().initWithFrame_(
            NSMakeRect(tx, CY - spinner_size / 2, spinner_size, spinner_size)
        )
        self._spinner.setStyle_(NSProgressIndicatorSpinningStyle)
        self._spinner.setControlSize_(1)  # NSControlSizeSmall
        self._spinner.setHidden_(True)
        self._panel.contentView().addSubview_(self._spinner)

        # Status label
        label_x = tx + spinner_size + 8
        label_w = W - label_x - 10
        label_h = 20
        self._status_label = NSTextField.labelWithString_("")
        self._status_label.setFrame_(NSMakeRect(label_x, CY - label_h / 2, label_w, label_h))
        self._status_label.setFont_(NSFont.systemFontOfSize_(13.0))
        self._status_label.setTextColor_(NSColor.whiteColor())
        self._status_label.setBezeled_(False)
        self._status_label.setDrawsBackground_(False)
        self._status_label.setEditable_(False)
        self._status_label.setSelectable_(False)
        self._status_label.setHidden_(True)
        self._panel.contentView().addSubview_(self._status_label)

    def _position_panel(self):
        screen = NSScreen.mainScreen()
        if screen is None:
            return
        screen_frame = screen.visibleFrame()
        panel_frame = self._panel.frame()
        x = screen_frame.origin.x + (screen_frame.size.width - panel_frame.size.width) / 2
        y = screen_frame.origin.y + 60
        self._panel.setFrameOrigin_((x, y))

    def _show_recording_elements(self, show: bool):
        self._dot.setHidden_(not show)
        self._timer_label.setHidden_(not show)
        for bar in self._level_bars:
            bar.setHidden_(not show)

    def showRecording(self):
        self._record_start_time = time.time()
        self._show_recording_elements(True)
        self._status_label.setHidden_(True)
        self._spinner.setHidden_(True)
        self._spinner.stopAnimation_(None)
        self._position_panel()
        self._panel.setAlphaValue_(1.0)
        self._panel.orderFront_(None)

        self._update_timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            0.05, self, "updateDisplay:", None, True
        )

    def showTranscribing(self):
        if self._update_timer:
            self._update_timer.invalidate()
            self._update_timer = None
        self._show_recording_elements(False)
        self._status_label.setStringValue_("Transcribing...")
        self._status_label.setTextColor_(NSColor.whiteColor())
        self._status_label.setHidden_(False)
        self._spinner.setHidden_(False)
        self._spinner.startAnimation_(None)

    @objc.typedSelector(b"v@:@")
    def showError_(self, message):
        if self._update_timer:
            self._update_timer.invalidate()
            self._update_timer = None
        self._show_recording_elements(False)
        self._spinner.setHidden_(True)
        self._spinner.stopAnimation_(None)
        self._status_label.setStringValue_(str(message))
        self._status_label.setTextColor_(
            NSColor.colorWithRed_green_blue_alpha_(1.0, 0.4, 0.4, 1.0)
        )
        self._status_label.setHidden_(False)
        self._position_panel()
        self._panel.setAlphaValue_(1.0)
        self._panel.orderFront_(None)
        NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            3.0, self, "dismiss:", None, False
        )

    @objc.typedSelector(b"v@:@")
    def updateDisplay_(self, timer):
        elapsed = time.time() - self._record_start_time
        minutes = int(elapsed) // 60
        seconds = int(elapsed) % 60
        self._timer_label.setStringValue_(f"{minutes}:{seconds:02d}")

        # Shift history left, push new level on right
        level = min(self._current_level * 40.0, 1.0)
        self._level_history.pop(0)
        self._level_history.append(level)

        for i, bar in enumerate(self._level_bars):
            bar_height = max(3, self._level_history[i] * 18)
            frame = bar.frame()
            bar.setFrame_(NSMakeRect(
                frame.origin.x,
                CY - bar_height / 2,
                3,
                bar_height,
            ))

    @objc.typedSelector(b"v@:@")
    def dismiss_(self, _=None):
        if self._update_timer:
            self._update_timer.invalidate()
            self._update_timer = None
        self._panel.setAlphaValue_(0.0)
        self._panel.orderOut_(None)

    def dismiss(self):
        self.dismiss_(None)

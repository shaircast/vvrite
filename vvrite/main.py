"""vvrite macOS app — entry point."""

import os
import sys
import tempfile
import time
import threading

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import objc
from AppKit import (
    NSApplication,
    NSApp,
    NSObject,
    NSApplicationActivationPolicyAccessory,
    NSAlert,
    NSAlertFirstButtonReturn,
)
from AppKit import NSTimer
from Foundation import NSLog
import ApplicationServices

from vvrite import __version__
from vvrite.preferences import Preferences
from vvrite.status_bar import StatusBarController
from vvrite.hotkey import HotkeyManager
from vvrite.overlay import OverlayController
from vvrite.onboarding import OnboardingWindowController
from vvrite import transcriber, sounds, updater
from vvrite.recorder import Recorder
from vvrite.clipboard import paste_and_restore


class AppDelegate(NSObject):
    def init(self):
        self = objc.super(AppDelegate, self).init()
        if self is None:
            return None
        self._prefs = Preferences()
        self._recorder = Recorder()
        self._recording = False
        self._lock = threading.Lock()
        self._overlay = None
        self._status_bar = None
        self._hotkey = None
        self._settings_wc = None
        self._load_retries = 0
        self._onboarding_wc = None
        self._available_update = None  # (tag, release) tuple when update found
        return self

    def applicationDidFinishLaunching_(self, notification):
        self._status_bar = StatusBarController.alloc().initWithDelegate_(self)
        self._overlay = OverlayController.alloc().init()

        if not self._prefs.onboarding_completed or not transcriber.is_model_cached(self._prefs.model_id):
            self._prefs.onboarding_completed = False
            self._onboarding_wc = (
                OnboardingWindowController.alloc()
                .initWithPreferences_statusBar_onComplete_(
                    self._prefs,
                    self._status_bar,
                    self._onboarding_finished,
                )
            )
            self._onboarding_wc.show()
        else:
            self._check_permissions()

    def _onboarding_finished(self):
        """Called when onboarding wizard completes."""
        self._hotkey = HotkeyManager(self)
        self._status_bar.setStatus_("Ready")
        NSLog("vvrite ready.")
        self._maybe_check_for_updates()

    def _check_permissions(self):
        """Check all permissions and prompt user step by step."""
        import AVFoundation

        ax_ok = ApplicationServices.AXIsProcessTrustedWithOptions(
            {ApplicationServices.kAXTrustedCheckOptionPrompt: False}
        )
        mic_status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        )
        mic_ok = mic_status == 3  # Authorized

        if ax_ok and mic_ok:
            self._all_permissions_granted()
            return

        # Build permission prompt
        missing = []
        if not ax_ok:
            missing.append("• Accessibility (for global hotkey)")
        if not mic_ok:
            missing.append("• Microphone (for voice recording)")

        alert = NSAlert.alloc().init()
        alert.setMessageText_("Permissions Required")
        alert.setInformativeText_(
            "vvrite needs the following permissions:\n\n"
            + "\n".join(missing)
            + "\n\nClick 'Grant' to open each permission dialog."
        )
        alert.addButtonWithTitle_("Grant")
        alert.runModal()

        # Request accessibility first if needed
        if not ax_ok:
            ApplicationServices.AXIsProcessTrustedWithOptions(
                {ApplicationServices.kAXTrustedCheckOptionPrompt: True}
            )

        # Request microphone if needed
        if not mic_ok and mic_status == 0:  # NotDetermined
            AVFoundation.AVCaptureDevice.requestAccessForMediaType_completionHandler_(
                AVFoundation.AVMediaTypeAudio, lambda granted: None
            )

        # Poll until all permissions granted
        self._status_bar.setStatus_("Waiting for permissions...")
        NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            2.0, self, "pollPermissions:", None, True
        )

    @objc.typedSelector(b"v@:@")
    def pollPermissions_(self, timer):
        import AVFoundation
        ax_ok = ApplicationServices.AXIsProcessTrustedWithOptions(
            {ApplicationServices.kAXTrustedCheckOptionPrompt: False}
        )
        mic_ok = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        ) == 3
        if ax_ok and mic_ok:
            timer.invalidate()
            self._all_permissions_granted()

    def _all_permissions_granted(self):
        self._status_bar.setStatus_("Loading model...")
        threading.Thread(target=self._load_model, daemon=True).start()

    def _load_model(self):
        try:
            transcriber.load(self._prefs)
        except Exception as e:
            NSLog(f"Model load failed: {e}")
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "showModelError:", str(e), True
            )
            return

        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "modelDidLoad:", None, False
        )

    @objc.typedSelector(b"v@:@")
    def showModelError_(self, error_msg):
        self._load_retries += 1
        if self._load_retries > 3:
            self._status_bar.setStatus_("Error: model failed")
            return
        alert = NSAlert.alloc().init()
        alert.setMessageText_("Model Loading Failed")
        alert.setInformativeText_(str(error_msg))
        alert.addButtonWithTitle_("Retry")
        alert.addButtonWithTitle_("Dismiss")
        response = alert.runModal()
        if response == NSAlertFirstButtonReturn:
            threading.Thread(target=self._load_model, daemon=True).start()
        else:
            self._status_bar.setStatus_("Error: model failed")

    @objc.typedSelector(b"v@:@")
    def modelDidLoad_(self, _):
        self._hotkey = HotkeyManager(self)
        self._status_bar.setStatus_("Ready")
        NSLog("vvrite ready.")
        self._maybe_check_for_updates()

    def toggleRecording(self):
        with self._lock:
            if not self._recording:
                self._start_recording()
            else:
                self._stop_recording()

    def _start_recording(self):
        self._recording = True
        sounds.play(self._prefs.sound_start)

        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "showRecordingUI:", None, False
        )

        def level_cb(level):
            self._overlay._current_level = float(level)

        try:
            self._recorder.start(
                device=self._prefs.mic_device,
                level_callback=level_cb,
            )
        except RuntimeError as e:
            self._recording = False
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "showErrorUI:", str(e), False
            )

    def _stop_recording(self):
        self._recording = False
        sounds.play(self._prefs.sound_stop)

        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "showTranscribingUI:", None, False
        )

        try:
            raw_path = self._recorder.stop()
        except RuntimeError as e:
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "showErrorUI:", str(e), False
            )
            return

        if raw_path is None:
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "transcriptionComplete:", None, False
            )
            return

        threading.Thread(
            target=self._transcribe_and_paste,
            args=(raw_path,),
            daemon=True,
        ).start()

    def _transcribe_and_paste(self, raw_path: str):
        try:
            text = transcriber.transcribe(raw_path, self._prefs)
            if text:
                paste_and_restore(text)
                self.performSelectorOnMainThread_withObject_waitUntilDone_(
                    "transcriptionComplete:", text, False
                )
            else:
                self.performSelectorOnMainThread_withObject_waitUntilDone_(
                    "transcriptionComplete:", None, False
                )
        except Exception as e:
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "showErrorUI:", str(e), False
            )

    # --- UI update selectors (must run on main thread) ---

    @objc.typedSelector(b"v@:@")
    def showRecordingUI_(self, _):
        self._overlay.showRecording()
        self._status_bar.setStatus_("Recording...")
        self._status_bar.setRecording_(True)

    @objc.typedSelector(b"v@:@")
    def showTranscribingUI_(self, _):
        self._overlay.showTranscribing()
        self._status_bar.setStatus_("Transcribing...")
        self._status_bar.setRecording_(False)

    @objc.typedSelector(b"v@:@")
    def showErrorUI_(self, message):
        self._overlay.showError_(str(message))
        self._status_bar.setStatus_("Ready")
        self._status_bar.setRecording_(False)

    @objc.typedSelector(b"v@:@")
    def transcriptionComplete_(self, text):
        self._overlay.dismiss()
        self._status_bar.setStatus_("Ready")

    def cancelRecording(self):
        """Cancel recording: stop mic, discard audio, dismiss overlay."""
        with self._lock:
            if not self._recording:
                return
            self._recording = False

        try:
            raw_path = self._recorder.stop()
            if raw_path:
                try:
                    os.unlink(raw_path)
                except OSError:
                    pass
        except RuntimeError:
            pass

        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            "dismissAndResetUI:", None, False
        )

    @objc.typedSelector(b"v@:@")
    def dismissAndResetUI_(self, _):
        self._overlay.dismiss()
        self._status_bar.setStatus_("Ready")
        self._status_bar.setRecording_(False)

    # --- Update check ---

    def _maybe_check_for_updates(self):
        """Auto-check for updates if enabled and cooldown has passed."""
        if not self._prefs.auto_update_check:
            return
        if not updater.should_check(self._prefs.last_update_check):
            return
        threading.Thread(target=self._check_for_updates, daemon=True).start()

    def _check_for_updates(self):
        """Background: fetch latest release and compare versions."""
        self._prefs.last_update_check = time.time()
        release = updater.fetch_latest_release()
        if release is None:
            return
        tag = release.get("tag_name", "")
        if updater.is_newer(tag, __version__):
            self._available_update = (tag, release)
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "updateCheckComplete:", tag, False
            )

    def _check_for_updates_manual(self):
        """Background: manual check (no cooldown), shows 'up to date' if none."""
        self._prefs.last_update_check = time.time()
        release = updater.fetch_latest_release()
        if release and updater.is_newer(release.get("tag_name", ""), __version__):
            tag = release["tag_name"]
            self._available_update = (tag, release)
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "updateCheckComplete:", tag, False
            )
        else:
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "showUpToDate:", None, False
            )

    @objc.typedSelector(b"v@:@")
    def updateCheckComplete_(self, tag):
        """Main thread: update menu and show alert."""
        self._status_bar.setUpdateAvailable_(str(tag))
        self._show_update_alert()

    @objc.typedSelector(b"v@:@")
    def showUpToDate_(self, _):
        alert = NSAlert.alloc().init()
        alert.setMessageText_("No Updates Available")
        alert.setInformativeText_(f"vvrite {__version__} is the latest version.")
        alert.addButtonWithTitle_("OK")
        alert.runModal()

    def checkForUpdates(self):
        """Called from menu bar item click."""
        if self._available_update:
            self._show_update_alert()
        else:
            threading.Thread(target=self._check_for_updates_manual, daemon=True).start()

    def _show_update_alert(self):
        if not self._available_update:
            return
        tag, release = self._available_update
        body = release.get("body", "") or ""
        # Truncate long release notes
        if len(body) > 500:
            body = body[:500] + "..."

        alert = NSAlert.alloc().init()
        alert.setMessageText_(f"vvrite {tag} is available")
        alert.setInformativeText_(
            f"You are currently running {__version__}.\n\n{body}"
        )
        alert.addButtonWithTitle_("Download")
        alert.addButtonWithTitle_("Later")
        response = alert.runModal()
        if response == NSAlertFirstButtonReturn:
            asset = updater.find_dmg_asset(release)
            if asset:
                threading.Thread(
                    target=self._download_update, args=(asset,), daemon=True
                ).start()
            else:
                # No downloadable asset — open release page in browser
                from Foundation import NSURL, NSWorkspace
                html_url = release.get("html_url", "")
                if html_url:
                    NSWorkspace.sharedWorkspace().openURL_(
                        NSURL.URLWithString_(html_url)
                    )

    def _download_update(self, asset):
        """Background: download asset to temp dir, then open it."""
        name = asset.get("name", "vvrite-update.dmg")
        url = asset.get("browser_download_url", "")
        if not url:
            return
        dest = os.path.join(tempfile.gettempdir(), name)
        try:
            updater.download_asset(url, dest)
            self.performSelectorOnMainThread_withObject_waitUntilDone_(
                "updateDownloadComplete:", dest, False
            )
        except Exception as e:
            NSLog(f"Update download failed: {e}")

    @objc.typedSelector(b"v@:@")
    def updateDownloadComplete_(self, path):
        """Main thread: open downloaded .dmg/.zip in Finder."""
        from Foundation import NSURL, NSWorkspace
        url = NSURL.fileURLWithPath_(str(path))
        NSWorkspace.sharedWorkspace().openURL_(url)

    def openSettings(self):
        from vvrite.settings import SettingsWindowController
        if self._settings_wc is None:
            self._settings_wc = SettingsWindowController.alloc().initWithPreferences_(self._prefs)
        self._settings_wc.showWindow_(None)
        self._settings_wc.window().makeKeyAndOrderFront_(None)
        NSApp.activateIgnoringOtherApps_(True)


def main():
    # Single-instance check: exit immediately if already running
    from AppKit import NSRunningApplication, NSWorkspace
    bundle_id = "com.vvrite.app"
    running = NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle_id)
    my_pid = os.getpid()
    for r in running:
        if r.processIdentifier() != my_pid:
            sys.exit(0)

    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    app.run()


if __name__ == "__main__":
    main()

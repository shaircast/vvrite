#!/usr/bin/env bash
set -euo pipefail

# ── Configuration ──────────────────────────────────────────────
IDENTITY="Developer ID Application: Saturn Studio (449B2G47F7)"
BUNDLE="dist/vvrite.app"
ENTITLEMENTS="entitlements.plist"
NOTARY_PROFILE="notarytool-profile"
ZIP="dist/vvrite.zip"
DMG="dist/vvrite.dmg"

# ── Step 1: Build ──────────────────────────────────────────────
echo "▸ Building with PyInstaller..."
pyinstaller vvrite.spec --noconfirm
echo "  ✓ Build complete"

# ── Step 2: Sign all binaries inside the bundle ────────────────
echo "▸ Signing embedded binaries..."

# Sign .so and .dylib files first (innermost → outermost)
find "$BUNDLE" -type f \( -name "*.so" -o -name "*.dylib" \) | while read -r lib; do
    codesign --force --options runtime \
        --entitlements "$ENTITLEMENTS" \
        --sign "$IDENTITY" \
        --timestamp \
        "$lib"
done

# Sign embedded frameworks
find "$BUNDLE/Contents/Frameworks" -type f -perm +111 2>/dev/null | while read -r bin; do
    codesign --force --options runtime \
        --entitlements "$ENTITLEMENTS" \
        --sign "$IDENTITY" \
        --timestamp \
        "$bin"
done

# Sign the main executable
codesign --force --options runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" \
    --timestamp \
    "$BUNDLE/Contents/MacOS/vvrite"

# Sign the .app bundle itself
codesign --force --options runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" \
    --timestamp \
    "$BUNDLE"

echo "  ✓ Signing complete"

# ── Step 3: Verify signature ──────────────────────────────────
echo "▸ Verifying signature..."
codesign --verify --deep --strict "$BUNDLE"
echo "  ✓ Signature valid"

# ── Step 4: Notarize ──────────────────────────────────────────
echo "▸ Creating zip for notarization..."
ditto -c -k --keepParent "$BUNDLE" "$ZIP"

echo "▸ Submitting for notarization (this may take a few minutes)..."
xcrun notarytool submit "$ZIP" \
    --keychain-profile "$NOTARY_PROFILE" \
    --wait

# ── Step 5: Staple ────────────────────────────────────────────
echo "▸ Stapling notarization ticket..."
xcrun stapler staple "$BUNDLE"
echo "  ✓ Staple complete"

# ── Step 6: Final verification ────────────────────────────────
echo "▸ Final Gatekeeper check..."
spctl --assess --type exec --verbose "$BUNDLE"

# ── Step 7: Create distribution DMG ─────────────────────────
echo "▸ Creating DMG..."
rm -f "$DMG"
DMG_STAGE=$(mktemp -d)
cp -R "$BUNDLE" "$DMG_STAGE/"
ln -s /Applications "$DMG_STAGE/Applications"
hdiutil create -volname "vvrite" -srcfolder "$DMG_STAGE" \
    -ov -format UDZO "$DMG"
rm -rf "$DMG_STAGE"

echo "▸ Signing DMG..."
codesign --force --sign "$IDENTITY" --timestamp "$DMG"

echo "▸ Notarizing DMG..."
xcrun notarytool submit "$DMG" \
    --keychain-profile "$NOTARY_PROFILE" \
    --wait

echo "▸ Stapling DMG..."
xcrun stapler staple "$DMG"
echo "  ✓ DMG ready: $DMG"

echo ""
echo "✓ Done! $DMG is signed, notarized, and ready for distribution."

#!/bin/bash
set -e

# Cleanup previous builds
rm -rf build dist

# Install dependencies if needed (though they should be in the environment)
# pip install -r requirements.txt

# Create the .app bundle
# --windowed: No console window
# --noconfirm: Replace output directory without asking
# --name: Application name
# --add-data: Add assets if you had any (e.g., --add-data "assets:assets")
# Note: Since the script imports torch and transformers, PyInstaller will try to bundle them.
# The resulting app will be large.
pyinstaller --noconfirm --windowed --name "AI 文本人性化" "ai文本人性化.py"

# Verify the .app exists
if [ ! -d "dist/AI 文本人性化.app" ]; then
    echo "Error: .app bundle not found!"
    exit 1
fi

echo "Preparing DMG content..."

# Create a staging directory for DMG content
STAGING_DIR="dist/dmg_staging"
rm -rf "$STAGING_DIR"
mkdir -p "$STAGING_DIR"

# Copy App to staging
cp -R "dist/AI 文本人性化.app" "$STAGING_DIR/"

# Create /Applications symlink
ln -s /Applications "$STAGING_DIR/Applications"

# Copy instructions file
cp "提示_已损坏怎么办.txt" "$STAGING_DIR/"

echo "Creating DMG..."

# Create DMG from staging directory
hdiutil create -volname "AI Text Humanizer Installer" -srcfolder "$STAGING_DIR" -ov -format UDZO "dist/AI 文本人性化.dmg"

echo "Cleaning up..."
rm -rf "$STAGING_DIR"

echo "Build complete! DMG is located at dist/AI 文本人性化.dmg"

#!/bin/bash
set -euo pipefail

# Sync claude-code-synthesis guides into .claude/vendor/
# Source: https://github.com/griffinhilly/claude-code-synthesis
# Usage: bash .claude/scripts/sync-synthesis.sh

REPO_URL="https://github.com/griffinhilly/claude-code-synthesis.git"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENDOR_DIR="$(cd "$SCRIPT_DIR/.." && pwd)/vendor/claude-code-synthesis"
TEMP_DIR="$(mktemp -d)"

trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Fetching latest from claude-code-synthesis..."
git clone --depth 1 --quiet "$REPO_URL" "$TEMP_DIR/repo"

# Remove old vendored copy
rm -rf "$VENDOR_DIR"
mkdir -p "$VENDOR_DIR"

# Copy only CLAUDE.md and guides/ (skip examples/, data/, article.txt)
cp "$TEMP_DIR/repo/CLAUDE.md" "$VENDOR_DIR/CLAUDE.md"
cp -r "$TEMP_DIR/repo/guides" "$VENDOR_DIR/guides"

# Record sync metadata
cat > "$VENDOR_DIR/.sync-meta" <<EOF
synced: $(date -u +%Y-%m-%dT%H:%M:%SZ)
commit: $(git -C "$TEMP_DIR/repo" rev-parse HEAD)
source: $REPO_URL
EOF

echo "Synced to $VENDOR_DIR"
cat "$VENDOR_DIR/.sync-meta"

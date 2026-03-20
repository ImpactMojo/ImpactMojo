#!/bin/bash
set -euo pipefail

# Bootstrap API keys for Claude Code sessions
# Reads from .claude/.env.keys (gitignored) and writes to CLAUDE_ENV_FILE

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
KEYS_FILE="$SCRIPT_DIR/../.env.keys"

if [ -n "${CLAUDE_ENV_FILE:-}" ] && [ -f "$KEYS_FILE" ]; then
  cat "$KEYS_FILE" >> "$CLAUDE_ENV_FILE"
fi

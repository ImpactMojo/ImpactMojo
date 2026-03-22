#!/bin/bash
set -euo pipefail

# Bootstrap API keys for Claude Code sessions
# Reads from .claude/.env.keys (gitignored) and writes to CLAUDE_ENV_FILE
# Keys: GITHUB_PAT, SUPABASE_PAT, NETLIFY_PAT, GAMMA_API_KEY, GEMINI_API_KEY,
#        NAPKIN_API_KEY, GROK_API_KEY, DEEPSEEK_API_KEY, SARVAM_API_KEY

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
KEYS_FILE="$SCRIPT_DIR/../.env.keys"

if [ -f "$KEYS_FILE" ]; then
  if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    # Claude Code session — inject keys into environment
    cat "$KEYS_FILE" >> "$CLAUDE_ENV_FILE"
  else
    # Direct shell — export keys
    set -a
    source "$KEYS_FILE"
    set +a
  fi
fi

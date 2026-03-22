#!/bin/bash
# PreToolUse hook: Block destructive bash commands
# Fires before Claude executes a Bash tool call
# Returns {"decision": "block", "reason": "..."} to prevent execution

set -euo pipefail

INPUT=$(cat)
TOOL=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_name',''))" 2>/dev/null || echo "")

if [ "$TOOL" != "Bash" ]; then
  echo '{"decision": "allow"}'
  exit 0
fi

CMD=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null || echo "")

# Block patterns
case "$CMD" in
  *"rm -rf"*|*"rm -r /"*)
    echo '{"decision": "block", "reason": "Blocked: rm -rf is not allowed. Delete specific files instead."}'
    exit 0
    ;;
  *"git push --force"*|*"git push -f "*)
    echo '{"decision": "block", "reason": "Blocked: force-push is not allowed. Use normal push."}'
    exit 0
    ;;
  *"git reset --hard"*)
    echo '{"decision": "block", "reason": "Blocked: git reset --hard can destroy work. Use git stash or git checkout for specific files."}'
    exit 0
    ;;
  *"git clean -f"*)
    echo '{"decision": "block", "reason": "Blocked: git clean -f deletes untracked files permanently."}'
    exit 0
    ;;
  *"drop table"*|*"DROP TABLE"*|*"truncate"*|*"TRUNCATE"*)
    echo '{"decision": "block", "reason": "Blocked: destructive database operations are not allowed."}'
    exit 0
    ;;
esac

echo '{"decision": "allow"}'

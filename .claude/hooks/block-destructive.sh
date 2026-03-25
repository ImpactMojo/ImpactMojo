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

# Lowercase for case-insensitive matching
CMD_LOWER=$(echo "$CMD" | tr '[:upper:]' '[:lower:]')

# Block patterns — file system
case "$CMD" in
  *"rm -rf"*|*"rm -r /"*)
    echo '{"decision": "block", "reason": "Blocked: rm -rf is not allowed. Delete specific files instead."}'
    exit 0
    ;;
esac

# Block patterns — git destructive
case "$CMD" in
  *"git push --force"*|*"git push -f "*|*"git push "*"--force-with-lease"*)
    echo '{"decision": "block", "reason": "Blocked: force-push is not allowed. Use normal push."}'
    exit 0
    ;;
  *"git reset --hard"*)
    echo '{"decision": "block", "reason": "Blocked: git reset --hard can destroy work. Use git stash or git checkout for specific files."}'
    exit 0
    ;;
  *"git clean -f"*|*"git clean -d"*)
    echo '{"decision": "block", "reason": "Blocked: git clean deletes untracked files permanently."}'
    exit 0
    ;;
  *"git checkout -- ."*|*"git restore ."*)
    echo '{"decision": "block", "reason": "Blocked: this discards all uncommitted changes. Use specific file paths instead."}'
    exit 0
    ;;
esac

# Block patterns — database (case-insensitive)
case "$CMD_LOWER" in
  *"drop table"*|*"drop database"*|*"truncate"*|*"delete from"*" where 1"*|*"delete from"*" without"*)
    echo '{"decision": "block", "reason": "Blocked: destructive database operations are not allowed."}'
    exit 0
    ;;
esac

# Block patterns — secrets exposure
case "$CMD" in
  *"cat .env"*|*"cat .claude/.env.keys"*|*"echo \$"*"_PAT"*|*"echo \$"*"_KEY"*|*"printenv"*)
    echo '{"decision": "block", "reason": "Blocked: do not print secrets to stdout."}'
    exit 0
    ;;
esac

echo '{"decision": "allow"}'

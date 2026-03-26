#!/bin/bash
# PostToolUse hook: Auto-validate JSON files after Edit/Write
# Only fires for files in data/ directory

set -euo pipefail

INPUT=$(cat)
FILE=$(echo "$INPUT" | python3 -c "
import sys, json
data = json.load(sys.stdin)
# Extract file path from tool_input
ti = data.get('tool_input', {})
print(ti.get('file_path', ti.get('file', '')))
" 2>/dev/null || echo "")

# Only validate JSON files in data/
case "$FILE" in
  */data/*.json)
    if [ -f "$FILE" ]; then
      if ! python3 -m json.tool "$FILE" > /dev/null 2>&1; then
        echo '{"decision": "block", "reason": "JSON validation failed for '"$FILE"'. Fix the syntax before continuing."}'
        exit 0
      fi
    fi
    ;;
esac

echo '{"decision": "allow"}'

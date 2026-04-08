#!/usr/bin/env python3
# PostToolUse hook: Auto-validate JSON files in data/ after Edit/Write.
#
# Fires on every Edit/Write tool call. Exits silently with "allow" unless
# the edit touched a JSON file under data/ and left it with a syntax error.
# When it does block, the reason includes the exact line/column and parse
# error so the user can fix it immediately instead of re-running grep.
#
# Input (stdin): JSON with shape {"tool_name": str, "tool_input": {...}, ...}
# Output (stdout): JSON with shape {"decision": "allow"} or
#                  {"decision": "block", "reason": str}

import json
import os
import sys


def emit(decision, reason=None):
    payload = {"decision": decision}
    if reason:
        payload["reason"] = reason
    print(json.dumps(payload))
    sys.exit(0)


# Read hook input. Any parse failure → allow (don't block unrelated work).
try:
    data = json.load(sys.stdin)
except Exception:
    emit("allow")

tool_input = (data or {}).get("tool_input") or {}
file_path = tool_input.get("file_path") or tool_input.get("file") or ""

# Only care about JSON files under a data/ directory.
if not file_path.endswith(".json"):
    emit("allow")
if "/data/" not in file_path:
    emit("allow")
if not os.path.isfile(file_path):
    emit("allow")

# Validate. On failure, include the actual JSON parse error (file, line,
# column, message) so the user can jump straight to the broken token.
try:
    with open(file_path, "r", encoding="utf-8") as f:
        json.load(f)
except json.JSONDecodeError as e:
    rel = os.path.relpath(file_path)
    reason = (
        f"JSON syntax error in {rel} at line {e.lineno}, column {e.colno}: "
        f"{e.msg}. Open the file at that location and fix the token "
        f"(common causes: trailing comma, missing comma between entries, "
        f"unescaped quote inside a string, mismatched brace or bracket)."
    )
    emit("block", reason)
except Exception as e:
    # File readable but something else went wrong — don't block, just allow.
    emit("allow")

emit("allow")

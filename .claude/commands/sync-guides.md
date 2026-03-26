---
description: "Sync latest Claude Code best-practice guides from griffinhilly/claude-code-synthesis"
---

Run the sync script to pull the latest guides:

1. Execute `bash .claude/scripts/sync-synthesis.sh`
2. After sync completes, read `.claude/vendor/claude-code-synthesis/.sync-meta` and report the commit SHA and timestamp
3. Run `git diff --stat` to show what changed
4. If there are changes, stage and commit them with message: "chore: sync claude-code-synthesis guides"

---
description: Review the current branch diff for issues before merging
---

## Changes to Review

!`git diff --name-only main...HEAD`

## Detailed Diff

!`git diff main...HEAD`

Review the above changes for:
1. Broken links or missing cross-references
2. Content count inconsistencies (game/lab/course counts)
3. Invalid JSON in data files
4. Security issues (exposed keys, XSS)
5. Mobile responsiveness concerns
6. Missing documentation updates

Give specific, actionable feedback per file.

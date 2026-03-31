---
description: Investigate and fix a GitHub issue
argument-hint: [issue-number]
---

Look at issue #$ARGUMENTS in the ImpactMojo/ImpactMojo repo.

!`curl -s -H "Authorization: token $GITHUB_PAT" https://api.github.com/repos/ImpactMojo/ImpactMojo/issues/$ARGUMENTS`

Understand the issue, trace it to the root cause, fix it, and verify the fix.
If it involves content changes, follow the content management rules (update counts, search index, docs, etc.).

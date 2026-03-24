---
description: "Systematic debugging for ImpactMojo — HTML rendering issues, broken links, JSON errors, layout bugs, JavaScript failures, and cross-reference inconsistencies. Use when the user reports a bug, something looks wrong, or a page isn't working."
---

# Systematic Debugging Skill

Structured approach to finding and fixing issues on impactmojo.in.

## Debugging Framework

### Step 1 — Reproduce & Classify
Identify the issue type:

| Type | Symptoms | First Check |
|------|----------|-------------|
| **Broken link** | 404, wrong page | `grep -rn 'href="...' *.html` for the path |
| **Layout bug** | Overlapping, overflow, misaligned | Check CSS media queries, viewport meta |
| **JS error** | Feature not working, console error | Check inline `<script>` for syntax errors |
| **Data issue** | Wrong counts, missing items | Validate JSON: `python3 -m json.tool data/*.json` |
| **Content mismatch** | Counts don't match, stale text | Run content-auditor agent |
| **Form broken** | Submission fails | Verify Formspree endpoint `xpwdvgzp` |
| **Stale reference** | Old URL, 101.impactmojo.in | `grep -rn '101.impactmojo.in' *.html courses/` |

### Step 2 — Investigate

**For HTML/CSS issues:**
```bash
# Check for malformed HTML (unclosed tags)
grep -c '<div' file.html  # compare with
grep -c '</div>' file.html

# Find CSS specificity conflicts
grep -n 'important' file.html

# Check responsive breakpoints
grep -n '@media' file.html
```

**For data issues:**
```bash
# Validate all JSON
for f in data/*.json; do python3 -m json.tool "$f" > /dev/null && echo "OK: $f" || echo "FAIL: $f"; done

# Check search index completeness
python3 -c "import json; d=json.load(open('data/search-index.json')); print(f'{len(d)} entries'); [print(f'  {e[\"type\"]}: {e[\"id\"]}') for e in sorted(d, key=lambda x: x['id'])]"

# Count consistency
grep -rn '16 Games\|16 games\|16 Interactive' index.html catalog.html docs/
```

**For cross-reference issues:**
```bash
# Find all internal links
grep -oP 'href="(/[^"]+)"' index.html | sort -u

# Check each linked file exists
grep -oP 'href="(/[^"]+)"' index.html | sort -u | while read -r link; do
  path="${link#href=\"}"; path="${path%\"}";
  [ -f ".${path}" ] || echo "MISSING: $path"
done
```

### Step 3 — Fix
1. Make the minimal change that fixes the root cause
2. Don't refactor surrounding code unless it caused the bug
3. Test the fix in context (check related pages too)

### Step 4 — Verify
1. Re-run the same check that found the bug
2. Run the content-auditor agent if cross-references were involved
3. Validate JSON if data files were touched
4. Check mobile layout if CSS was changed

### Step 5 — Prevent
- If the bug was a missing cross-reference, check if `add-files` skill covers that case
- If it was a count mismatch, verify all count locations are documented
- Add the pattern to Known Issues in memory.md if it's likely to recur

## Common ImpactMojo-Specific Issues

### The "620KB index.html" Problem
- Always backup first: `cp index.html Backups/index-backup-$(date +%Y%m%d-%H%M).html`
- Use targeted edits, never rewrite the whole file
- Search for exact strings rather than line numbers (they shift frequently)

### Count Drift
Content counts appear in 4+ locations. When they drift:
1. `grep -rn 'N Games' index.html catalog.html README.md docs/` (where N is the expected count)
2. Fix ALL occurrences in one commit
3. Update memory.md with new counts

### Stale 101.impactmojo.in Links
Legacy links to the old subdomain:
1. `grep -rn '101.impactmojo.in' .`
2. Replace with self-hosted path (usually `/Handouts/` or `/courses/`)

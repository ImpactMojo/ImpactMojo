# Testing

No formal test framework — static HTML site with no build step.

## Manual verification checklist

Before considering any change complete:

1. **JSON validity**: Run `python3 -m json.tool data/search-index.json > /dev/null` after any data file changes
2. **Link check**: Grep for the new file path in `index.html` — confirm it resolves to a real file
3. **Count consistency**: `grep -c` the old and new count values across `index.html`, `catalog.html`, `README.md`, `docs/platform-overview.md`
4. **Form attributes**: Grep for `data-netlify="true"` in any new HTML files that contain forms — ensure forms have `name`, `data-netlify="true"`, and `netlify-honeypot="bot-field"`
5. **Responsive meta**: Every new HTML file must have `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

## Useful grep commands

```bash
# Find all content count references (replace 16 with current game count)
grep -rn "16 Games\|16 games\|16 Interactive" index.html catalog.html docs/

# Validate all JSON data files
for f in data/*.json; do python3 -m json.tool "$f" > /dev/null && echo "OK: $f" || echo "FAIL: $f"; done

# Check for broken internal links in index.html
grep -oP 'href="(/[^"]+)"' index.html | sort -u
```

## Related

- Agent `content-auditor` automates consistency checks across the platform
- Skill `housekeeping` includes quality checks as step 10
- Command `/project:deploy-check` runs a pre-deploy verification

# API Conventions

All external API calls use environment variables for authentication (loaded by `hooks/session-start.sh` from `.env.keys`):

| Service | Variable | Auth Pattern | Skill |
|---------|----------|-------------|-------|
| GitHub | `$GITHUB_PAT` | `Authorization: token $GITHUB_PAT` | `github-ops` |
| Supabase | `$SUPABASE_PAT` | `Authorization: Bearer $SUPABASE_PAT` | `supabase-ops` |
| Netlify | `$NETLIFY_PAT` | `Authorization: Bearer $NETLIFY_PAT` | `netlify-ops` |
| Gamma | `$GAMMA_API_KEY` | `Authorization: Bearer $GAMMA_API_KEY` | `gamma-ops` |
| Gemini | `$GEMINI_API_KEY` | Query param `?key=$GEMINI_API_KEY` | `gemini-ai` |
| Napkin.ai | `$NAPKIN_API_KEY` | `Authorization: Bearer $NAPKIN_API_KEY` | `napkin-ai` |
| Grok | `$GROK_API_KEY` | `Authorization: Bearer $GROK_API_KEY` | `grok-ai` |
| DeepSeek | `$DEEPSEEK_API_KEY` | `Authorization: Bearer $DEEPSEEK_API_KEY` | `deepseek-ai` |
| Sarvam AI | `$SARVAM_API_KEY` | `Authorization: Bearer $SARVAM_API_KEY` | `sarvam-ai` |
| InstantDB | `$INSTANTDB_APP_ID` + `$INSTANTDB_ADMIN_TOKEN` | Client: `init({ appId })`. Admin: `Authorization: Bearer $INSTANTDB_ADMIN_TOKEN` + `App-Id: $INSTANTDB_APP_ID` | `impactlex-ops` |

## Rules

- Always use `curl -s` with proper auth headers
- Check if a resource exists before creating duplicates (PRs, issues, etc.)
- Never expose API keys in committed files
- Keys are loaded at session start — if missing, check `.claude/.env.keys` exists

## GitHub auth — local proxy vs direct PAT

The session's git remote (`origin`) typically points at a local proxy (e.g. `http://local_proxy@127.0.0.1:PORT/git/...`). **The proxy is scoped to the session's authorised development branch.** It will reject:

- Tag pushes (`git push origin v10.x.y`) → HTTP 403
- Branch deletions (`git push origin --delete <name>`) → HTTP 403
- Wiki repo access (`*.wiki.git`) → 502 "repository not authorized"
- Operations on branches outside the authorised dev branch

**Fallback for these operations**: use direct GitHub HTTPS with `$GITHUB_PAT`:

```bash
# Push a tag
git push "https://x-access-token:${GITHUB_PAT}@github.com/ImpactMojo/ImpactMojo.git" v10.23.0

# Delete a stale branch
git push "https://x-access-token:${GITHUB_PAT}@github.com/ImpactMojo/ImpactMojo.git" --delete claude/old-branch

# Clone + push the wiki
git clone https://github.com/ImpactMojo/ImpactMojo.wiki.git /tmp/wiki
# (edits)
cd /tmp/wiki && git push "https://x-access-token:${GITHUB_PAT}@github.com/ImpactMojo/ImpactMojo.wiki.git" master
```

**Create a GitHub Release** (the MCP server has no `create_release` tool, so use the API directly):

```bash
curl -s -X POST \
  -H "Authorization: token ${GITHUB_PAT}" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/ImpactMojo/ImpactMojo/releases \
  -d "$(jq -n --arg body "$NOTES" '{tag_name: "v10.x.y", name: "...", body: $body, draft: false, prerelease: false}')"
```

**Wiki commits** need `-c commit.gpgsign=false` because the session's signing infra rejects unsourced commits:

```bash
git -c commit.gpgsign=false -c user.email=claude@anthropic.com -c user.name="Claude" commit -m "..."
```

For everything else (regular pushes to the authorised dev branch, GitHub MCP tool calls like `merge_pull_request`, `add_issue_comment`, `issue_write`), the local proxy + MCP tools work fine — prefer those over direct PAT.

## Key URLs

- **GitHub repo**: `https://api.github.com/repos/ImpactMojo/ImpactMojo/`
- **GitHub wiki**: `https://github.com/ImpactMojo/ImpactMojo.wiki.git` (clone via direct URL, push via PAT fallback)
- **Supabase project**: `ddyszmfffyedolkcugld`
- **Forms**: Netlify Forms (no external service — built into Netlify hosting)

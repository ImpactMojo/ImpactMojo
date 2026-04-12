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

## Rules

- Always use `curl -s` with proper auth headers
- Check if a resource exists before creating duplicates (PRs, issues, etc.)
- Never expose API keys in committed files
- Keys are loaded at session start — if missing, check `.claude/.env.keys` exists

## Key URLs

- **GitHub repo**: `https://api.github.com/repos/ImpactMojo/ImpactMojo/`
- **Supabase project**: `ddyszmfffyedolkcugld`
- **Forms**: Netlify Forms (no external service — built into Netlify hosting)

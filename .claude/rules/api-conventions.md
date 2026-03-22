---
paths:
  - ".claude/skills/**"
  - ".claude/hooks/**"
---

# API Conventions

All external API calls use environment variables for authentication:

| Service | Variable | Base URL |
|---------|----------|----------|
| GitHub | `$GITHUB_PAT` | `https://api.github.com/repos/Varnasr/ImpactMojo/` |
| Supabase | `$SUPABASE_PAT` | `https://api.supabase.com/v1/projects/ddyszmfffyedolkcugld/` |
| Netlify | `$NETLIFY_PAT` | Netlify API |
| Gamma | `$GAMMA_API_KEY` | Gamma API |
| Gemini | `$GEMINI_API_KEY` | Google Gemini API |
| Napkin.ai | `$NAPKIN_API_KEY` | Napkin API |

- Always use `curl` with proper auth headers for API calls
- Check if a resource exists before creating duplicates (PRs, issues, etc.)
- Never expose API keys in committed files

# ImpactMojo — Project-Specific Instructions

## Project Context

ImpactMojo is a free development education platform for South Asia. It covers MEL & Research, Data & Technology, Policy & Economics, Gender & Equity, Health & Communication, and Philosophy & Governance. Content includes courses, interactive games, labs, handouts, dojos, and data tools.

- Site: impactmojo.in
- Stack: Static HTML/CSS/JS, Supabase backend, Netlify hosting
- Docs: GitBook at `/docs/`
- Games: Self-contained HTML files in `/Games/`

## ImpactMojo Code Style

- Games are single self-contained HTML files (HTML + CSS + JS, no build step)
- Indian folk art styles for game illustrations (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)

## ImpactMojo API Endpoints

- **GitHub repo**: `https://api.github.com/repos/Varnasr/ImpactMojo/...`
- **Supabase project**: `https://api.supabase.com/v1/projects/ddyszmfffyedolkcugld/...`
- **Gamma**: Use `$GAMMA_API_KEY` for syncing course content to Gamma presentations
- **Napkin.ai**: Use `$NAPKIN_API_KEY` for generating visual content from course material
- **Formspree**: All forms submit to endpoint `xpwdvgzp`

## ImpactMojo Documentation

- Keep `docs/games-guide.md`, `docs/platform-overview.md`, `docs/content-guide.md` current
- Update `docs/changelog.md` for user-facing changes
- Update `data/search-index.json` if new searchable content was added

## ImpactMojo Housekeeping

- Copy current `index.html` to `Backups/` before major changes
- Verify backups are not stale
- Verify game, lab, course counts are consistent across all pages and docs
- Check for stale `101.impactmojo.in` links that should point to self-hosted files
- Test all forms submit to correct Formspree endpoint (`xpwdvgzp`)

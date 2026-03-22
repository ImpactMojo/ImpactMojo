# ImpactMojo

Free development education platform for South Asia covering MEL & Research, Data & Technology, Policy & Economics, Gender & Equity, Health & Communication, and Philosophy & Governance.

## Commands

No build step — static HTML/CSS/JS site.

```
# Deploy: auto-deploys on push to main via Netlify
# Tests: open HTML files directly in browser
```

## Architecture

- **Stack**: Static HTML/CSS/JS, Supabase backend, Netlify hosting
- **Site**: impactmojo.in
- **Games**: Self-contained HTML files in `/Games/` (no dependencies, single file each)
- **Labs**: Browser-based workbenches in `/courses/*-lab.html`
- **Courses**: 9 flagship in `/courses/{name}/`, 39 foundational via catalog
- **Handouts**: 400+ organized by track in `/Handouts/{Track}/`
- **Data**: JSON files in `/data/` (search-index, dataverse, BCT repository)
- **Docs**: GitBook markdown in `/docs/`

## Conventions

- Games are single self-contained HTML files (inline CSS + JS, no external deps)
- Indian folk art styles for game illustrations (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- All forms submit to Formspree endpoint `xpwdvgzp`
- Content counts are hardcoded in multiple places — grep to find all instances when updating

## Watch out for

- `index.html` is ~620KB — backup to `Backups/` before major changes
- Content counts appear in nav, hero, feature cards, sidebar — update ALL occurrences
- Some foundational courses link to `101.impactmojo.in` — check for stale external refs
- `data/search-index.json` must stay valid JSON — add entries for all new searchable content
- Update `docs/changelog.md` for user-facing changes

## API Endpoints

- **GitHub**: `https://api.github.com/repos/Varnasr/ImpactMojo/...` via `$GITHUB_PAT`
- **Supabase**: `https://api.supabase.com/v1/projects/ddyszmfffyedolkcugld/...` via `$SUPABASE_PAT`
- **Gamma**: `$GAMMA_API_KEY` for presentation sync
- **Gemini**: `$GEMINI_API_KEY` for AI content generation
- **Netlify**: `$NETLIFY_PAT` for deploy management
- **Napkin.ai**: `$NAPKIN_API_KEY` for visual content

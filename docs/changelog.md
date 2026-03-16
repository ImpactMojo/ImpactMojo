# Changelog

See the full [CHANGELOG.md](https://github.com/Varnasr/ImpactMojo/blob/main/CHANGELOG.md) in the repository.

## v10.1.0 — March 16, 2026

### Git Standards (29 repos)
- Propagated `.gitattributes`, `.editorconfig`, `.githooks/`, `.gitmessage`, `CODEOWNERS`, `SECURITY.md`, `dependabot.yml`, PR & issue templates across all 29 Varnasr repos
- Pre-commit hook blocks secrets, debugger, conflict markers; warns on console.log and large files
- Commit-msg hook enforces prefix convention (Add/Fix/Update/Translate/Docs/Refactor/Test/CI/Chore)
- Dependabot auto-configured per ecosystem (npm, pip, github-actions)

### GitBook Docs Fix
- Fixed broken sidebar links — added `/impactmojo/*` → `/docs/*` Netlify redirects

## v10.0.0 — March 16, 2026

### Typography Overhaul (80 files)
- Standardized fonts: **Amaranth** (body), **Inter** (headings), **JetBrains Mono** (code)
- Removed 6 one-off fonts (Poppins, Fraunces, Merriweather, Source Serif 4, Source Sans 3, Cormorant Garamond)
- Standardized Google Fonts URLs and CSS fallback chains

### Canvas Charts
- Admin dashboard and transparency page use smooth canvas line/area charts (Catmull-Rom splines, HiDPI support)

### Mobile Improvements
- What's New section and Wall of Love testimonials on mobile homepage
- Fixed hamburger menu and logo display across 4 pages

### Auth & Dashboard Fixes
- Fixed race condition in admin-gate.js and auth-gate.js (profile fetch timing)
- Fixed dashboard tabs showing wrong role/tier
- Polished org dashboard Create Learning Path modal

### Transparency Page Redesign
- Revenue model section with tier cards
- Simplified data model methodology (Legacy + GA4 = Totals)

### Repo Housekeeping
- Added ROADMAP.md with Q1-Q4 2026 priorities
- Standardized logo tagline to "Development Know-How" across all pages
- Cleaned up stale feature branches

## v9.5.0 — March 15, 2026

- Unified dashboard tab navigation
- Team training packages for organizations
- Full-text search, offline PWA, assessments

## v9.1.0 — March 7, 2026

- PolicyDhara integration
- Org dashboard content improvements
- Auth gate fixes

## v9.0.0 — March 6, 2026

- JWT-based premium access control
- Netlify Edge Functions auth-gate
- GitHub Wiki, Discussions, CI setup
- CHANGELOG.md added

## v8.0.0 — February 28, 2026

- Performance optimization (160KB inline JS extracted)
- Service worker upgrade
- Community channels integration

## v7.0.0 — February 15, 2026

- Premium membership tiers
- Supabase authentication
- 39 foundational courses, 12 games, 10 labs
- ImpactLex PWA, Dev Case Studies, DevDiscourses
- Multilingual support

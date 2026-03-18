# ImpactMojo — Claude Code Instructions

## Project Context

ImpactMojo is a free development education platform for South Asia. It covers MEL & Research, Data & Technology, Policy & Economics, Gender & Equity, Health & Communication, and Philosophy & Governance. Content includes courses, interactive games, labs, handouts, dojos, and data tools.

- Site: impactmojo.in
- Stack: Static HTML/CSS/JS, Supabase backend, Netlify hosting
- Docs: GitBook at `/docs/`
- Games: Self-contained HTML files in `/Games/`

## After Major Changes

When implementing major features, significant refactoring, or multi-file bug fixes, always complete these housekeeping tasks before finishing:

### 1. Git Cleanup
- Delete merged/stale local branches (`git branch -d`)
- Clean up remote tracking branches (`git fetch --prune`)
- Ensure working tree is clean

### 2. Documentation (GitBook)
- Update relevant files in `docs/` if architecture, features, or workflows changed
- Keep `docs/games-guide.md`, `docs/platform-overview.md`, `docs/content-guide.md` current
- Update `docs/changelog.md` for user-facing changes

### 3. GitHub Issues & Projects
- Close resolved issues with a reference to the commit/PR
- Update issue labels and milestones
- Move completed items on project boards

### 4. Roadmap
- Update `ROADMAP.md` — move completed items, add new planned work
- Update `CHANGELOG.md` with version-appropriate entries

### 5. Wiki & Discussions
- Document new architectural patterns or decisions in wiki
- Post updates to relevant GitHub Discussions if applicable

### 6. README & Meta
- Update `README.md` if project structure, setup, or scope changed
- Update `sitemap.xml` if new pages were added
- Update `data/search-index.json` if new searchable content was added

### 7. Backup
- Copy current `index.html` to `Backups/` before major changes
- Verify backups are not stale

### 8. Counts & References
- Verify game, lab, course counts are consistent across all pages and docs
- Check for stale `101.impactmojo.in` links that should point to self-hosted files

### 9. Quality Checks
- Ensure no broken links in navigation
- Verify mobile responsiveness for new UI
- Check text contrast/readability (WCAG AA minimum)
- No hardcoded secrets or credentials committed

## Code Style

- Games are single self-contained HTML files (HTML + CSS + JS, no build step)
- Use CSS custom properties for theming
- Indian folk art styles for game illustrations (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- All card/badge text must have high contrast — no white text on light backgrounds
- Mobile-first responsive design
- Prefer editing existing files over creating new ones

## Git Practices

- Write concise commit messages focused on "why" not "what"
- Never force-push to main
- Never commit .env files or secrets
- Stage files explicitly, avoid `git add -A`

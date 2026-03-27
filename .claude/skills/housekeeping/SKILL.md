---
name: housekeeping
description: Run post-feature housekeeping — clean branches, update docs, issues, roadmap, README. Use when the user says "clean up", "housekeeping", "we're done with this feature", or after completing a major change.
---

# Post-Change Housekeeping

Run through this checklist after completing major work on ImpactMojo.

## Steps

1. **Git cleanup**
   - List stale branches: `git branch -vv | grep gone`
   - Delete merged local branches: `git branch -d <branch>`
   - Prune remote refs: `git fetch --prune`
   - Verify working tree is clean: `git status`

2. **Update CHANGELOG.md**
   - Add entry under current version with date
   - Categorize as Added/Changed/Fixed/Removed

3. **Update docs/ (GitBook)**
   - Review `docs/` files for accuracy
   - Update `docs/games-guide.md` if games changed
   - Update `docs/platform-overview.md` if structure changed
   - Update `docs/content-guide.md` if content added

4. **Update ROADMAP.md**
   - Move completed items to done
   - Add new planned work if applicable

5. **Update README.md**
   - Verify project structure tree is current
   - Update feature descriptions if scope changed

6. **Update search & sitemap**
   - Add new content to `data/search-index.json`
   - Add new pages to `sitemap.xml`

7. **GitHub housekeeping**
   - Close resolved issues (link to commits/PRs)
   - Update project board
   - Post to Discussions if relevant

8. **Backup**
   - Copy current working `index.html` to `Backups/` with a descriptive name
   - Verify existing backups are not stale (delete if superseded)

9. **Update counts & references**
   - Verify game, lab, course counts are consistent across all docs, index, catalog, admin dashboards, and transparency pages
   - Check for stale `101.impactmojo.in` references that should now point to self-hosted files
   - **Update upgrade letter counts** (`upgrade.html`): Run these commands and update the stats in the letter if they've changed:
     ```bash
     echo "Flagship courses: $(ls -d courses/*/index.html | wc -l)"
     echo "101 courses: $(ls 101-courses/*.html | wc -l)"
     echo "Labs: $(ls Labs/*-lab.html | wc -l)"
     echo "Games: $(ls Games/*.html | wc -l)"
     echo "Book summaries: $(ls BookSummaries/*-companion.html | wc -l)"
     ```
     Update the stats banner numbers and the intro paragraph in `upgrade.html` to match.
     Also update any count references in `premium.html`, `index.html` hero/stats sections.
   - **Update upgrade letter counts** (`upgrade.html`): Run these commands and update the stats in the letter if they've changed:
     ```bash
     echo "Flagship courses: $(ls -d courses/*/index.html | wc -l)"
     echo "101 courses: $(ls 101-courses/*.html | wc -l)"
     echo "Labs: $(ls Labs/*-lab.html | wc -l)"
     echo "Games: $(ls Games/*.html | wc -l)"
     echo "Book summaries: $(ls BookSummaries/*-companion.html | wc -l)"
     ```
     Update the stats banner numbers and the intro paragraph in `upgrade.html` to match.
     Also update any count references in `premium.html`, `index.html` hero/stats sections.

10. **Quality checks**
    - Verify no broken navigation links
    - Check text contrast on new UI elements (WCAG AA)
    - Test all forms submit to correct Formspree endpoint
    - **Topbar layout check** — CRITICAL, this has broken 30+ pages before:
      ```bash
      # Find pages where im-topbar uses sticky (should be ZERO results)
      grep -rl 'position: sticky' --include="*.html" | xargs grep -l 'im-topbar' | grep -v Backups
      grep -rl 'position:sticky' --include="*.html" | xargs grep -l 'im-topbar' | grep -v Backups
      ```
      If any results: change `position: sticky; top: 0;` to `position: fixed; top: 0; left: 0; right: 0;`
      and add `padding-top: 44px` to body or `margin-top: 44px` to main content.

11. **Google Analytics check**
    - Verify ALL HTML pages include the Google Analytics snippet with ID `G-JRCMEB9TBW`
    - Check: `grep -rL "G-JRCMEB9TBW" *.html courses/*/*.html Games/*.html Labs/*.html`
    - The required snippet in `<head>`:
      ```html
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>
      <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JRCMEB9TBW');</script>
      ```
    - Add the snippet to any page missing it

12. **Branding & UX consistency check**
    Run these checks on ALL pages, especially new or modified ones. Every user-facing HTML page must include the full ImpactMojo branding stack:

    **a) Footer** (`class="footer"`)
    - 4-section footer: About, Legal (IT Act), Quick Links, Resources
    - Footer bottom with © year, PinPoint Ventures credit, MIT License
    - Check: `grep -L 'class="footer"' *.html courses/*/*.html`

    **b) Fonts** (Amaranth + Inter + JetBrains Mono)
    - Google Fonts import with preload pattern in `<head>`
    - Check: `grep -L 'fonts.googleapis.com' *.html courses/*/*.html Games/*.html Labs/*.html`
    - Required import: `Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500`

    **c) Language selector** (5 languages)
    - `data-i18n` attributes on all user-facing text elements
    - `js/translate.js` script included
    - Supported: English, Hindi (हिन्दी), Tamil (தமிழ்), Bengali (বাংলা), Marathi (मराठी)
    - Check: `grep -L 'translate.js\|data-i18n' *.html`

    **d) Theme toggle** (Light / Dark / System)
    - `.theme-selector` container with 3 buttons: `data-theme="system"`, `data-theme="light"`, `data-theme="dark"`
    - `body.dark-mode` CSS class with proper dark mode overrides
    - Check: `grep -L 'theme-selector' *.html courses/*/*.html`

    **e) Accessibility widget** (UserWay)
    - UserWay script with account ID `EksmhlPg9k`
    - Widget layout: `full`
    - Check: `grep -L 'EksmhlPg9k' *.html courses/*/*.html`

    **f) Paper plane SVGs** (`.v3-paper-plane`)
    - Decorative floating paper plane elements
    - Related classes: `.v3-big-plane`, `.v3-floating-elements`
    - Check: `grep -L 'v3-paper-plane' *.html`

    **g) Blob decorations** (`.v3-blob`)
    - 4 gradient blobs: `.v3-blob-1` (blue), `.v3-blob-2` (indigo), `.v3-blob-3` (green), `.v3-blob-4` (amber)
    - Container: `.v3-floating-elements`
    - Dark mode variants must have reduced opacity
    - Check: `grep -L 'v3-blob' *.html`

    **h) Cookie consent banner** (`#cookieConsent`)
    - Cookie icon button + expandable consent panel
    - Accept button stores `localStorage.cookieConsent = 'true'`
    - `data-i18n` attributes for multilingual support
    - Check: `grep -L 'cookieConsent' *.html`

    **i) Speed dial / FAB toolbox** (`#imxSpeedDial`)
    - Floating action button with tools: Mojini chatbot, Reading Lists, Analytics, Pomodoro, Lo-Fi Music, Compare
    - Check: `grep -L 'imxSpeedDial' *.html`

    **j) SVG icon sprite** (Sargam Icons)
    - Hidden SVG sprite block with `<symbol id="si_*">` definitions
    - Usage pattern: `<use href="#si_IconName"/>`
    - Check: `grep -L 'si_Activity\|si_Heart\|si_Book' *.html`

    **Exceptions:** Games (`/Games/*.html`) and Labs (`/Labs/*-lab.html`) are self-contained single-file tools — they need GA, fonts, theme toggle, and accessibility widget but may skip footer, speed dial, blobs, and cookie banner.

13. **GitHub "Alive Docs" sync**
    - **Wiki**: Clone `Varnasr/ImpactMojo.wiki.git`, update affected pages (Home, Content-Guide, Changelog, Roadmap, Architecture, Book-Summaries, 101-Course-Decks), push
    - **Discussions**: Post announcement in Announcements category for user-facing additions
    - **Issues**: Close resolved issues with commit/PR links; update tracking issues (#272 BookSummaries, etc.)
    - **Milestones**: Update milestone progress if applicable

14. **GitBook cross-check**
    - Verify `docs/changelog.md` has entries for all changes made
    - Verify `docs/platform-overview.md` counts match `index.html` counts
    - Verify `docs/content-catalog.md` tables include all new content
    - Verify `docs/roadmap.md` completed items match what was shipped

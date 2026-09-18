# Roadmap

What's coming next for ImpactMojo. This is a living document — we'd love your input. Suggest ideas in [GitHub Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas).

## Currently In Progress

### Vernacular Course Content
Full course content in regional languages. ([#29](https://github.com/ImpactMojo/ImpactMojo/issues/29))

**Where this stands:** The platform interface and quality-audited page translations are already live in **5 languages** — Hindi, Tamil, Bengali, Marathi, and Telugu. What remains in progress is deeper course-level localisation: complete course translations refined toward human quality, starting with the most-used flagship courses.

**What this means for you:** If you work with teams who are more comfortable in regional languages, you can already switch the interface and key pages today — and full course translations are on the way.

## Recently Shipped

These were previously listed as planned or in progress, and are now live. Each names the page, so you can check rather than take our word for it.

- **BookSummaries expansion** — the interactive reading companion library has grown to **172 companions** across development economics, statistics, research methods, communication, leadership, and productivity. ([#272](https://github.com/ImpactMojo/ImpactMojo/issues/272))
- **Native 101 deck migration** — all **58 foundational course decks** are now self-hosted HTML with ~100 slides each, interactive charts, and keyboard/touch navigation. No third-party presentation embeds remain.
- **Vernacular interface** — the UI and quality-audited page translations ship in 5 languages (Hindi, Tamil, Bengali, Marathi, Telugu); see "Currently In Progress" above for what's still open.
- **Practitioner voices** — this was listed as a planned "practitioner interview series". It shipped as **Field Radio**, a station of **19 clips** — voice notes and short videos from practitioners, each with a full transcript, playing back-to-back and filterable by track. Every clip is in site search, including its transcript, so a phrase you half-remember finds the clip. ([Listen](/field-radio.html))
- **Peer review system** — get feedback on your work from other practitioners, and give it. ([/peer-review.html](/peer-review.html))
- **Certificate verification for employers** — listed as a "certificate marketplace"; what shipped is the part that matters to a hiring manager, a page that checks whether a credential is real. ([/verify.html](/verify.html))
- **Partner API** — for organisations integrating ImpactMojo content into their own training platforms. ([/api-docs.html](/api-docs.html))
- **Community-contributed courses** — practitioners can put a course forward for publication. ([/contribute.html](/contribute.html))
- **Live workshop listings** — workshops with registration and a calendar file you can add to your own diary. ([/events.html](/events.html))
- **Impact measurement dashboard** — a public view of community outcomes, and a signed-in route to log your own. ([/impact-dashboard.html](/impact-dashboard.html))
- **Offline support, both halves** — browser notifications you can switch on from your account, and background sync, so progress recorded on a bad connection is replayed once you are back online rather than lost.

## Planned

**These are not dated.** This section used to carry quarter labels, and by September 2026 it still read "Planned — Q2 2026 (April–June)" over items that had either shipped months earlier or not started. A date we have already missed tells you less than no date at all, so the list below is ordered by what we expect to reach first, and nothing here is a commitment to a month.

### Next

**For learners and educators**
- **Analytics dashboard v2** — completion funnels, time-on-task and assessment scores, for yourself or your team
- **Video walkthroughs for the Studios** (the interactive labs) — short guided videos showing how to work through each one

**Content**
- **Survey Instrument Library** — browse and adapt *validated* instruments. Note this is not the existing [Designing a Survey Instrument](/practice-packs/survey-instrument/) Practice Pack, which teaches you to write one from scratch; the library would let you start from instruments that have already been tested.
- More foundational (101) courses across all six tracks
- Regional case study packs built on state-level Indian data

**Community**
- **Alumni directory** — connect with other ImpactMojo learners

### Later

**Indian-language tools.** Four open-weight models for Indian languages were released by Bodhan AI with AI4Bharat in September 2026 (speech to text, text to speech, OCR and translation across the 22 scheduled languages). Planned uses, in order:

- **Listen to a course in your language**: spoken versions of the 101 decks in Hindi, Tamil, Bengali, Marathi and Telugu, generated once and cached
- **Document OCR for field material**: scanned registers, forms and government PDFs in Indian scripts turned into text you can search and analyse
- **A second transcription engine in VaniScribe**, and a free notebook route that runs the open weights so transcription needs no paid key
- **A translation quality trial** against the site's existing translations before any switch

## Release history

What shipped in earlier releases. The counts in these entries are as they stood at the time, not today's totals.


### v10.82.2 — July 2026
- **Interactive assessments on every flagship** — all 18 flagship courses now end with a six-question auto-graded "Assess Yourself" self-check (90 questions in total), each grounded in the course's own material, with instant feedback and explanations.
- **Build Circles & the AI for M&E Certificate Track** — a four-week AI build-cohort programme and a self-paced, assessed certificate track, plus the free **AI Agents for Evaluators** module.

### v10.80.0 — July 2026
- **Counterfactual: The Evaluation Game** — the 18th simulation: eight impact claims, eight classic causal-inference traps, pick the strongest feasible evaluation design
- **Six new Live Case Challenges** — every flagship course now has a matching real-world challenge (15 in total)
- **Gender & Work in India timeline** — the sixth timeline, 18 citation-backed nodes across 6 eras (the collection now spans 113 nodes and 44 eras)

### July 2026 — 12 new labs + live-code course
- **12 new Interactive Labs** — Budget & Fiscal Analysis, Climate Risk & Adaptation, Conflict-Sensitive Programming, Data Feminism, Digital Public Infrastructure, Ethics & Research Integrity, Grant Writing, Participatory Methods, Policy Brief Writing, Stakeholder Mapping, Survey Design, and Systems Thinking. The labs collection grew from 15 to 28, with three new tracks.
- **R & Python for Development** — a new interactive course to learn R and Python from zero, running real code live in your browser (WebR + Pyodide, no install). All seven modules are live, using real NFHS, ASER, PLFS, and Budget data.

### v10.18.0 — April 2026
- **Sitemap expansion** — 84 → 171 indexed URLs (all courses, BookSummaries, blog posts, and public pages)
- **Stale link cleanup** — ~100 legacy `101.impactmojo.in` links migrated to self-hosted paths
- **Search index cleanup** — Removed phantom entries, added missing labs
- **Count drift fixes** across marketing kit, press kit, README, and docs

### v10.17.0 — April 2026
- **Formspree eliminated** — All 12 forms migrated to Netlify Forms. Platform now runs on 2 services (Netlify + Supabase) instead of 3
- **Engagement email pipeline** — 5-email drip sequence (Day 0/3/7/14/21) with streak reminders and cohort deadlines. ([#144](https://github.com/ImpactMojo/ImpactMojo/issues/144), [#145](https://github.com/ImpactMojo/ImpactMojo/issues/145))
- **Monthly newsletter** — Automated content roundup on the 15th of every month
- **Premium sales letter** and **Practitioner Starter Kit** pages
- **Branded email template** — Consistent design across all platform emails via Resend

### v10.16.0 — April 2026
- **Accessibility Statement** at `/accessibility.html` — Formal WCAG 2.1 Level AA conformance statement
- **Full accessibility audit** — axe-core + pa11y-ci CI pipeline, UserWay widget integration

### v10.15.0 — April 2026
- **Content count corrections** sitewide — all files now show canonical 69 courses / 15 labs / 134 games

### v10.14.0 — April 2026
- **Device-mode default theme** on 70 pages — OS dark/light preference on first paint
- **WCAG AA link underlines** across 74 content pages
- **CC BY-NC-ND 4.0 attribution** backfilled into all 89 handouts

### v10.13.0 — April 2026
- **4 native 101 slide decks** — Dev Econ, MEL, Climate, Inequality migrated from Gamma to self-hosted HTML (100 slides each, interactive charts, light/dark theme)

### v10.10.0 — March 2026
- **ImpactMojo MCP Server** — 11 tools and 3 resources exposing the full knowledge base via Model Context Protocol. Works with Claude Desktop, Claude Code, Cursor, and any MCP client. npm-publishable.

### v10.9.0 — March 2026
- Sitewide design audit: 242 pages updated with ImpactMojo fonts, 3-mode theme toggle, paper plane SVG, sticky topbar, and footer
- Full mobile responsiveness across all BookSummaries, Games, Handouts, Blog, Courses, Labs, Templates, and Premium Tools
- GitBook documentation link added to footer across all pages

### v10.1.0 — March 2026
- Git best-practice standards across all 29 repos
- GitBook docs sidebar link fix

### v10.0.0 — March 2026
- Font standardization (Amaranth + Inter + JetBrains Mono) across 80 files
- Canvas line charts on admin and transparency dashboards
- Mobile navigation fixes across all pages
- What's New and Wall of Love sections on mobile homepage
- 4 new flagship courses

### v9.x — March 2026
- JWT-based premium access control
- Supabase authentication (Email, Google OAuth, Magic Links)
- W3C Open Badges 3.0 verifiable credentials
- Learning Pathways with milestone progression
- Interactive assessments for flagship courses
- Full-text search (Ctrl+K)
- Offline PWA support
- ImpactMojo Dataverse (215+ tools and datasets)
- BCT Repository (203 behaviour change techniques)
- 134 learning games, 15 interactive labs
- Dark mode and high-contrast theme
- Multilingual support (6 languages)

## How to Suggest Features

1. Check [existing discussions](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas) to see if someone has already suggested it
2. Open a new discussion in the **Ideas** category
3. Describe the problem you're trying to solve — not just the feature you want. For example: "My team struggles to track who has completed which training module" is more helpful than "Add a dashboard"
4. Include examples from your development practice if possible — it helps us prioritize

You can also email suggestions to hello@impactmojo.in.

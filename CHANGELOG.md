# Changelog

All notable changes to ImpactMojo are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [10.23.20] - 2026-05-02

### Fixed
- **Fullscreen button no longer covers `www.impactmojo.in`** in slide-header. Added `padding-right:120px` to `.slide-header` across all 7 native decks, pushing the right-hand `header-url` text leftward so the fs-hint pill (positioned `right:18px`) sits in clear space and no longer obscures the URL text.

### Added
- **Auto-spacious mode** for sparse slides — symmetric counterpart to v10.23.19's auto-compact. JS heuristic adds `.slide.spacious` to any non-compact, non-divider slide with under 420 characters of text content (excluding chart canvases and tables). Spacious mode bumps `slide-title.sm` from 24px → 30px, `slide-body` from 15px → 17px, `bullet-list li` from 15px → 16px, and adds 18px padding on `hbox` callouts. Slides that previously looked underfilled with small fonts now read with appropriate visual weight.
- **One new ECharts data slide per native deck** (7 charts total), inserted just before the End slide:
  - **climate-essentials** — CO₂ per capita 2023 by region (horizontal bar). Africa 1.0 / India 1.9 / EU 6.4 / China 7.7 / Russia 11.4 / USA 14.4 t/cap. Source: Global Carbon Project / Our World in Data.
  - **dev-economics** — India sectoral GDP composition 1950-2023 (stacked area). Agri 51%→17%, Industry 14%→27%, Services 35%→56%. Source: World Bank / RBI.
  - **inequality-basics** — Top 1% pre-tax income share, cross-country comparison (horizontal bar). Sweden 11.7% → South Africa 21.9%, with India at 21.7%, USA 20.5%. Source: WID 2024.
  - **mel-basics** — Theory of Change as a 5-node directed graph (Inputs → Activities → Outputs → Outcomes → Impact) with arrow-labelled link types (efficiency, effectiveness, attribution, contribution).
  - **public-finance-budgeting** — Tax-to-GDP ratio cross-country bar. Bangladesh 8% / Indonesia 12% / India 17.8% → Brazil 32.5% / OECD 33.8% / Norway 39.8%. Source: World Bank / OECD / IMF.
  - **social-margins** — Multidimensional Poverty headcount by social group (India 2023). ST 21.4% / Muslims 14.4% / SC 14.0% / OBC 11.5% / National 11.3% / Hindus 11.6% / Others 7.5%. Source: NITI Aayog National MPI 2023.
  - **work-labour-livelihoods** — India female LFPR (15+) 2017-18 → 2022-23 (line with area). 17.5% → 33.0% trajectory. Source: PLFS annual rounds.
- Each new chart slide carries: section label, contextual paragraph, full-width canvas, and "what to see" amber-callout takeaway.
- End slide IDs renumbered from `s102` → `s103` (and `s112` → `s113` in social-margins) to make room.

### Fixed (drive-by)
- Typo `www.impacctmojo.in` → `www.impactmojo.in` in dev-economics deck slide-footer (one slide).

## [10.23.19] - 2026-05-02

### Fixed
- **Native deck formatting polish — fullscreen button, nav overlap, content overflow** across all 7 native decks.
  - **Fullscreen button (`#fs-hint`)**: previously rendered at 9px font with 25% white opacity — barely visible, sometimes mistaken for being clipped/cut off. Repositioned with safer margins (top:14px, right:18px), bumped font to 10px, raised contrast to 85% white, added a translucent dark pill background (with dark-mode counterpart) and 14px border-radius. Now obviously a clickable element.
  - **Bottom navigation overlap**: `#nav` fixed at `bottom:16px` was sitting visually on top of slide content because the slide-viewport scales to fill the browser window. Added a fade-on-idle behaviour (drops to 18% opacity after 2.2s of no input; full opacity on hover or any mouse/keyboard/touch activity). Also increased `.slide-content` bottom padding from 20px to 46px so content doesn't crowd into the nav strip even when nav is fully visible.
  - **Content overflow auto-compact**: added a JS heuristic that runs at load and adds the existing `.slide.compact` modifier to any slide with ≥11 `<li>` items, ≥2 `<table>`s, or >1900 characters of text. Skips title screens, section dividers, end screens, and TOC slides. Existing `.slide.compact` rules already shrink fonts and padding on dense slides; auto-application means content-heavy slides no longer overflow the 1280×720 viewport. Also tightened `.slide.compact` rules for tables (`.ctable td` 12px / 6px padding), info-boxes (`.hbox` 10px padding, 12.5px text), and bottom-padding on the content area.

### Known follow-ups (not in this PR)
- Some slides have **too little content** with small fonts on otherwise-empty slides — opposite of overflow. Needs per-slide content audit and either copy expansion or font promotion (`slide-title sm` → `lg`). Out of scope for a structural CSS fix.
- **Charts/diagrams density**: most decks currently carry only 2 ECharts data slides each (the v10.23.15 batch). User asked for more diagrams across decks — that's substantive content work (research, data sourcing, ECharts authoring per slide) and warrants its own PR.

## [10.23.18] - 2026-05-02

### Fixed
- **Native 101 deck tables — added inside borders + vertical alignment** across all 7 native decks (climate-essentials, dev-economics, inequality-basics, mel-basics, public-finance-budgeting, social-margins, work-labour-livelihoods). The `.ctable` class previously had only `border-bottom` on `<td>`, no vertical separators between columns, and no `vertical-align` rule — multi-line cells looked misaligned and columns blurred together. Added: outer 1px border, vertical right-borders on every `<th>`/`<td>` (with `:last-child` cleared), `vertical-align: top` so wrapped text in one cell doesn't drag adjacent cells with it, and `tr:last-child td { border-bottom: none }` for a clean bottom edge. Dark-mode counterparts also added. Tables now read as proper grids rather than horizontal-stripe blocks.
- **Slide-header logo links → 101 Series landing page** across every slide in all 7 native decks (724 links updated total: 102 per deck × 6 + 112 in social-margins). Previously the logo on every slide pointed to `https://www.impactmojo.in` (homepage), which made it hard to jump back to the 101 Series landing without navigating up two levels. Now the logo on every slide (including the end slide) points to `https://www.impactmojo.in/101-courses/` — the real landing page for the 101 deck context. Single click from any slide → browse all 40 101 courses.

## [10.23.17] - 2026-05-02

### Fixed
- **Browse button redesign across 118 inner pages.** The previous Browse-link styling was a flat text link with muted colour — visually weak next to the gradient Premium button. Replaced site-wide with an outline button: 1.5px border, uppercase Inter 700, 0.5rem padding, hover state that fills with the cyan accent + lifts on translateY + adds soft shadow. Dark-mode variant uses translucent white background. Result: better visual balance with the Premium button, more inviting interaction state. Affected: all flagship course pages, all 101 deck landing pages, all DeepDives pages, all BookSummary pages, all top-level pages.

## [10.23.16] - 2026-05-02

### Added
- **Universal "Resources & Practice" cross-link section** added to all 12 flagship course pages (SEL, dataviz, devai, devecon, gandhi, gender, law, media, mel, poa, pubchoice, pubpol). Each section carries 7 colour-coded resource cards: Hands-on Lab (course-specific or generic), NotebookLM AI Companion (with course-specific URL where available — 11 of 12 flagships have one), Foundational 101 Decks (course-specific recommendations + browse-all), BookCompanion Field Companions (course-specific + browse-all), Print-Friendly Reference Handouts, Live Dojo Practice Sessions, Premium Tools & Coaching. Closes the long-running flagship parity ask: every flagship now has a consistent baseline of cross-linked resources, regardless of how rich its main content is.
- Per-flagship customisation: dataviz cross-links the dataviz lab + storytelling/info-we-trust books; mel cross-links TOC Lab + MEL Plan Lab; gender cross-links 3 thematically-related 101 courses (SRHR, care economy, data feminism); pubchoice cross-links Political Economy + Public Finance 101 + Indian Constitution 101; etc.
- Bespoke Sargam-style SVGs replace 21 remaining body emojis (📚 📧 💬 👋 ♥ 🌐 📩 ⚠ 📏 🏆 🎓 🗓) across 7 files (`accessibility.html`, `blog.html`, `blog/sample-size-matters.html`, `blog/whats-coming-in-2026.html`, `catalog.html`, `content-marketing-kit.html`, `forgot-password.html`). Body emojis platform-wide now at zero.

## [10.23.15] - 2026-05-02

### Added
- **14 substantive ECharts data slides** across all 7 native ImpactMojo-hosted 101 decks (2 per deck). Each slide carries: contextual paragraph above the chart, full-width visualisation in a bordered canvas, and a "what to see" amber-callout takeaway below. Charts use the requested fancy types (no pies):
  - **climate-essentials**: Sankey of global CO₂ emissions (energy carrier → sector, ~37 GtCO₂); area chart of NASA GISTEMP temperature anomaly 1880-2023.
  - **dev-economics**: Multi-series line panel of South Asia per-capita GDP (PPP) trajectories 1990-2023 — India, Bangladesh, Pakistan, Sri Lanka, Nepal; Sankey of India's structural transformation (workforce 1991→2011→2023, by sector).
  - **inequality-basics**: Area chart of India top-10% income share 1922-2022 (V-shape); Lorenz curve of India wealth distribution 2023 (WID).
  - **mel-basics**: Bubble panel of evaluation methods (rigour × feasibility × cost) — RCT, DiD/RDD, PSM, pre-post survey, contribution analysis, outcome harvesting, qualitative, MSC; circular graph linking indicator types (input/output/outcome/impact) to MEL methods.
  - **public-finance-budgeting**: Union Budget Sankey (tax revenue → expenditure heads, FY24); multi-country debt/GDP panel (India, Bangladesh, Pakistan, Brazil, China, USA, Japan).
  - **social-margins**: Identity-intersection chord (caste/tribe/religion/gender/sexuality/disability/region/class with edge-weights reflecting empirical co-incidence); SC/ST PoA Act atrocity cases bar+line panel 1995-2022 (cases + conviction rate).
  - **work-labour-livelihoods**: Stacked area of India workforce share by sector 1983-2023; Sankey of formal/informal decomposition of India's workforce (PLFS 2022-23).
- ECharts 5.5.0 added to all 7 native decks — supports sankey, chord, area, beeswarm, parallel coordinates, custom layouts.
- New `.slide.compact` modifier: tighter font/spacing for slides with 11+ list items (PFB) or 14+ li / 320+ words (others). 51 slides marked compact across the 7 decks (PFB 18, climate-essentials 6, dev-economics 7, inequality-basics 5, mel-basics 4, social-margins 3, work-labour-livelihoods 8).

### Fixed
- **Work, Labour & Livelihoods 101 slides 13-15 overflow** marked compact.
- **All 7 native deck SLIDE_IDS arrays** rebuilt to include new chart slides — total slide counts now: climate-essentials 102, dev-economics 102, inequality-basics 102, mel-basics 102, public-finance-budgeting 102, social-margins 112, work-labour-livelihoods 102. Progress text + TOTAL constants synchronised.
- All chart slide IDs renamed from temporary `sN_chart` form to plain sequential `sN` for navigation continuity.

## [10.23.14] - 2026-05-02

### Added
- **Social Margins 101 Section 12: The Other Vectors — A South Asian Survey** (10 net-new slides). Substantively expands the deck from 100 to 110 slides with vector-specific primers on tribal/Adivasi, religion, gender (broader), sexuality & queer/trans, disability, region & language, class, migration & statelessness, plus a closing practitioner toolkit. Each primer includes structural framing, foundational voices, key indicators, constitutional/statutory architecture, and intersectional cautions. Honest accounting: caste sections (02-11) retain their depth, but the deck now genuinely delivers on its broader name.
- **101-courses/index.html** — new landing page for the ImpactMojo 101 Series. 40 courses with native HTML / Slide Deck / Coming Soon filter chips, search, tracks, hero stats, full SEO + GA. Sitemap entry, /101 short-URL redirect.
- **Standardised end slide** across all 7 native ImpactMojo-hosted 101 decks (climate-essentials, dev-economics, inequality-basics, mel-basics, public-finance-budgeting, social-margins, work-labour-livelihoods). New `.end-screen` template with gradient background, dot pattern, glow effect, gradient bar, gradient-text "Thank You" headline, byline, 3 themed CTAs (primary gradient / secondary outline / tertiary ghost), meta footer with CC BY-NC-SA. Replaces 7 different bespoke ugly closing slides with one consistent beautiful template.

### Fixed
- **Public Finance & Budgeting 101 overflow**: 18 dense slides (11+ list items each) marked with new `.slide.compact` modifier. Reduced font-size, line-height, and padding within compact slides to fit content within the fixed 1280×720 viewport. Same compact treatment applied conservatively (14+ li or 320+ words threshold) to 30 dense slides across the other 6 native decks.
- **Stale 101.impactmojo.in references**: removed from native deck end slide CTAs; replaced with self-hosted `/101-courses/` URL throughout.
- **Slide 100 (thank-you) on Social Margins**: stale link fixed; CTAs swapped from devecon/poa/101.impactmojo.in to gender/poa/decolonize-dev which are thematically aligned with Social Margins; later replaced entirely by the new standardised end-slide template.

### Changed
- Social Margins TOC + agenda updated to reflect 110 slides + new Section 12 (slides 98-107) + renumbered Section 13 (Further Reading, Glossary, Thank You at slides 108-110). Reading-the-deck guide rewritten to describe the new structure.
- HTML balance: 1494 → 1656 open/close divs in social-margins.html (added 10 substantive slides + Section 12 divider + agenda expansion). All 7 native decks balance-checked.

## [10.23.13] - 2026-05-02

### Changed
- **Groups 9-14 audit batch.** Closed all six remaining content-type audits (101-courses, Deep Dives, Blog, Top-level pages, Flagship course pages, NotebookLM registry). 130 files scanned across 6 groups; 86 files patched in a single commit.
- **SEO baseline 100%** across all 130 audited files: 14 canonical links + 38 og:image + 70 og:site_name + 4 full twitter:card blocks added. Default og:image is the ImpactMojo logo at `/assets/images/ImpactMojo Logo.png`. Twitter cards include matching title/description/image. Inserted after the last existing `og:` tag where present, otherwise after meta description.
- **3 native 101 decks (PFB, social-margins, work-labour-livelihoods)** received full SEO + Google Analytics installation: meta description, robots, canonical, og:type/title/description/url/image/site_name, twitter:card block, and the GA G-JRCMEB9TBW snippet. Previously they had only `<title>` + viewport because the Claude-Chat-generated slide-deck template ships with minimal head metadata.
- **54 dingbat replacements** (✓ ✗ ✦ ✧) → inline Sargam-style stroke SVGs across 14 files: `101-courses/mel-basics.html` (10 ✗/✓ marks in pros/cons lists), `blog/learning-by-doing.html` (1), `blog/theory-of-change-pitfalls.html` (5 ✓ Strong labels), `content-marketing-kit.html` (8), and 10 flagship course pages (3 sparkles each in v3-hero decoration). SVGs sized via `width:1em; height:1em` with `vertical-align:-0.15em` to inherit text colour and baseline.
- **NotebookLM registry verified clean**: 11 entries, all with title + URL, JSON valid. No drift between registry and platform claims.

### Known drift (deferred)
- 21 real-emoji chars remain across 7 files (📚📧💬👋♥🌐📩⚠📏🏆🎓🗓): used as functional UI category icons (`accessibility.html`, `forgot-password.html` chatbot menus), friendly greetings (`👋` on `blog.html`, `catalog.html`), and content emphasis (3 in `whats-coming-in-2026.html`). Need bespoke 1:1 SVG mapping per use case rather than bulk substitution. Tracked for a dedicated emoji-to-Sargam pass.

## [10.23.12] - 2026-05-02

### Changed
- **Social Margins 101 — Phase A finish (lightweight cross-vector signposting).** Caste content in sections 02-11 retained as the deepest vector treatment in the deck; each section divider now carries an italic "Parallels" subtitle explicitly connecting the section's analytical frame to other vectors (tribe, religion, gender, sexuality, disability, region, language, class). Examples: section 04 (Colonialism & Census) parallels — Hindu/Muslim binary, Scheduled Tribes vs PVTGs, Hindi/Urdu wedge, criminalised hijra under CTA 1871; section 05 (Constitution) parallels — Schedules V/VI, Articles 25-30, NALSA, RPWD Act; section 11 (Contemporary Debates) parallels — caste census ↔ religion-based reservation, EWS ↔ poverty as vector, AI bias ↔ identity surveillance.
- Agenda note (slide 2) rewritten from "deep treatment of caste anchored by..." to a "Reading the deck" framing that names where each vector is treated and explicitly signposts the parallels mechanism.
- Added `.div-subtitle` CSS rule (italic 15px, 62%-opacity white, max-width 680px) to support cross-vector subtitles on section dividers.
- HTML balance preserved (1494 open / 1494 close divs, 100 slides). Phase A is considered complete for v10.23.x. Net-new vector sections (Tribal/Adivasi, Religion broader, Gender broader, Sexuality, Disability, Region/Language, Class) as their own slide modules are tracked for future releases under the broader Social Margins expansion.

## [10.23.11] - 2026-05-01

### Changed
- **Caste Studies 101 folded into expanded Social Margins 101.** User feedback: separate Caste Studies course was too narrow; Social Margins is the better umbrella name for a course covering all identity vectors (caste, tribe, religion, gender, sexuality, disability, region, language, class). Architectural switchover (`fd3c909`) shipped first; Phase A content expansion ongoing across releases.
- **Foundational course count: 41 → 40** (Caste Studies merged into expanded Social Margins). 4 native HTML decks now: social-margins, public-finance-budgeting, work-labour-livelihoods, plus 36 Gamma-hosted.
- `social-margins.html` (was the Gamma-only Marginalised Identities 101) now lives as a 100-slide native HTML deck:
  - Section 01 (slides 3-8) **fully rewritten** to be foundational across all identities — "What Are Social Margins?", "Vectors of Marginalisation", "Foundational Voices on Identity & Marginalisation" (Ambedkar, Crenshaw, Spivak, Iris Marion Young, Phule, Uma Chakravarti), "Categories That Shape Identity Analysis" (ascribed/achieved, visible/invisible, identity/structure, recognition/redistribution), "Intersectionality — How Identities Compound" (Crenshaw + South Asian translation).
  - Sections 02-11 (slides 9-97) currently retain the existing strong caste content (origins, anti-caste thought, colonialism/census, Article 17/reservations, economy, violence, education, gender×caste, diaspora, contemporary debates). Agenda transparently flags that broader sections (Tribal/Adivasi, Religion, Gender broader, Sexuality, Disability, Region, Language, Class) are "in expansion in upcoming releases".
  - Section 12 lexicon (slide 99) restructured to a 3-column table with **Vector** annotations — added Intersectionality, Subaltern, Recognition vs Redistribution, NALSA judgment, Section 377, Hijra, RPWD Act 2016, Social model of disability, Communalism, Sub-nationalism alongside existing caste terms.
- 301 redirects: `/101-courses/caste-studies` → `/101-courses/social-margins.html`.
- Catalog `c40` (Caste Studies) deleted; `c17` retitled "Marginalised Identities 101" → "Social Margins 101" with broader scope description. Filter chip 41 → 40.
- Homepage modal: Caste Studies item removed; Social Margins item swapped from Gamma fallback to direct native HTML link with new description. Heading "All Courses (53)" → 52. View-All-Courses button 53 → 52. C16 dropdown option label updated.
- `search-index.json`: `COURSE-CASTE-STUDIES` replaced by `COURSE-SOCIAL-MARGINS` with expanded tag set.
- `sitemap.xml`: caste-studies removed; social-margins lastmod 2026-04-05 → 2026-05-01, priority 0.7 → 0.8.
- 13 docs files updated to reflect 53 → 52 / 41 → 40 counts (README, catalog hero, 11 docs/*.md).

### Note
This is a **Phase B (architectural) commit + partial Phase A (content)**. The deck is correctly named, discoverable, and has rewritten foundational framing — but full deep treatment of non-caste identity vectors as their own sections is queued for upcoming releases. User explicitly authorised iterative refinement: "we can always revise A".

## [10.23.10] - 2026-05-01

### Added
- **Public Choice — 12th flagship course** at `/courses/pubchoice/` — *Decisions, Incentives & Institutions*. 13 modules synthesising the Virginia school (rent-seeking), Bloomington school (commons), and New Institutional Economics, with cases from India, Bangladesh, Pakistan, Sri Lanka, and Nepal. 83-term interactive lexicon. 12th NotebookLM AI Study Companion.
- **3 new 101-courses** — native slide-deck (1280×720, 12 sections) format: *Caste Studies 101* (varna/jati, Ambedkarite thought, anti-caste movements), *Public Finance & Budgeting 101* (Union/state budgets, finance commissions, budget transparency), *Work, Labour & Livelihoods 101* (SNA boundary, care economy, sustainable-livelihoods framework, agrarian question, migration, non-farm economy).
- **Deep Dives** — new content type at `/DeepDives/`: 5 curated annotated reading lists by Sukhmeet Bedi + ImpactMojo Editorial team (Indian Political Economy, Impact Measurement, Climate & Just Transitions in South Asia, Caste/Identity/Development, Data/Power/Global South). Mixed media (books, papers, podcasts, datasets), 2–4 sentence annotations per reading.

### Changed
- **Foundational course count: 38 → 41**. *Work, Labour & Livelihoods 101* supersedes both *Decent Work for All 101* and *Livelihoods 101* (deleted with 301 redirects). Net +3.
- **Performance wins on index.html**: extracted 215 KB inline `<style>` to `/css/imx-main.css` (cacheable, parallel-loadable). Index dropped from 645 KB raw / 96 KB brotli → 431 KB / 64 KB. Repeat-visit TTFB improved from ~1.4s to **175 ms** (8× faster) via Netlify edge caching (`max-age=300, must-revalidate`). Auth scripts deferred to bottom of body.
- **Specials nav restructured** into 4 collapsible accordion subgroups (Reference Libraries, Long-form Reading, Practice & Programs, Behind the Scenes) replacing a flat 13-item dropdown.
- **Reference library proxies cleaned up** — eliminated `on-web.link` shortlinks (one was already 404'ing). PolicyDhara, DevDiscourses now served via Netlify Edge Functions proxying directly from the upstream GitHub Pages repos with injected `<base href>` for asset resolution.

### Fixed (content audit batch — Group 1–8)
- **Reference Libraries**: ImpactLex term count drift (claimed 1,200 vs actual 1,055), DevDiscourses count, FieldCases count — all aligned to source-of-truth across catalog, homepage, FAQ.
- **Search-index**: backfilled 27 BookSummary/Reference/Handout entries that were on disk but missing from `data/search-index.json`. 3 catalog descriptions corrected (Hindi-shipping mojini-guide misclaim).
- **Games**: emoji → SVG migration for climate-action and public-health games (Lucide-style, viewBox 0 0 24 24, 1.5px stroke). Stale `101.impactmojo.in` links replaced with self-hosted paths. `im-topbar` injected into all 16 games.
- **Labs**: `toc-lab` Browse button added. 2 mistyped lab catalog entries corrected.
- **Premium tools**: removed duplicate Code Converter Pro entry. Renamed *Qualitative Research Lab Pro* → *Qualitative Insights Lab Pro* (8 occurrences in source file). 4 missing tools backfilled to catalog (TOC Workbench Pro live; DevData Practice / Visualization Cookbook / DevEconomics Toolkit coming soon). Filter chip 7 → 9. Search-index entries added for all live tools.
- **BookSummaries**: 30 of 31 companions verified clean (viewport, meta, OG, GA, Amaranth, im-topbar, no emojis). Replaced **54 emoji instances** in dt-companion.html (Design Thinking) with inline Sargam-style SVGs across 24 unique characters. All 31 catalog titles confirmed to match canonical `<title>` in source files.
- **Flagship modules**: 5 catalog drifts + 3 homepage drifts in module counts. After fixes, all 12 flagships have consistent counts across catalog, homepage cards, and `id="module-N"` anchors. Specifically: Gandhi 12→13 (home), Devecon 12→13 (home), Dataviz 13→12 (catalog), DevAI 13→12 (catalog), MEL 13→14 (both), SEL 12→13 (catalog).
- **Handouts render bug** in `handouts.html`: `TRACK_MAPPING` had 5 of 6 stale folder-name keys (`Data Analysis Track`, `Gender Studies Track`, `Research Methods Track`, etc.) that didn't match disk. Only Policy & Economics rendered with proper colour/order — the other 5 tracks fell into "Other Resources" alphabetical fallback. Fixed all 5 + added 4 missing mappings (Education and Pedagogy, Thematic Areas, Cross Cutting Resources, Quick Reference Cards).
- **Handouts emoji removal**: replaced **1,317 emoji instances** across 63 handout files (144 unique characters) with inline Sargam-style SVGs. Self-contained (no sprite/CDN dependency) so handouts stay print-portable.
- **Typo fix**: `Handouts/Thematic Areas/South Aisa Region/` → `South Asia Region/`.
- **Count corrections**: catalog + README "400+ handouts" was inflated marketing copy → 85 actual.
- **README + 18 docs files**: backfilled all stale counts (11→12 flagships, 38→41 foundational, 48→53 courses, 400+→85 handouts, 11→12 NotebookLM).
- **Mobile**: sitewide ≤768px padding floor on top-level sections so cards stop bleeding into viewport edge.
- **Specials nav**: all 13 items now use absolute URLs (`/#flagship-courses` etc.). `js/router.js` now respects hash fragments before path-based routes.
- **DevEcon CSS shim**: defined missing `--indigo`, `--cyan`, `--orange`, `--success` aliases in all 4 `:root` blocks of `courses/devecon/index.html` (17 components were referencing undefined vars).
- **Catalog accessibility**: `.track-filter.active` failed WCAG AA contrast (sky-500 on sky-500@20%). Fixed to amber-700 light / sky-300 dark.
- **`faq-bank.js` line 167**: stray `""` syntax error was killing the whole file's parsing — fixed.

## [10.20.0] - 2026-04-20

### Added
- **Book Summary: *Beyond Developmentality* — Debal Deb** (Earthscan, 2009). Deb's eco-socialist critique of the doctrine of development: eight neo-classical myths, "developmentality" as Foucauldian epistemic apparatus, inclusive freedom, strong sustainability grounded in the Basudha farm counter-evidence. 9 chapters + 4 learning pathways + 8 key concepts + 6 South Asia lenses. BookSummaries total: 31 → 32 (with interactive archive).
- **Archived interactive companion** at `/BookSummaries/beyond-developmentality-deb-interactive.html` (original React SPA preserved), linked from the new templated page via "Launch interactive companion".
- Landing card, search-index entry, sitemap entry for the new book.

### Changed
- **Brand refresh across all 31 book summaries.** Every BookSummary now passes the 14-item ImpactMojo brand checklist:
  - Floating paper plane SVG (decorative, 30 files gained it)
  - Skip-to-content link for WCAG 2.4.1 (30 files)
  - `translate.js` defer script (30 files)
  - Favicon + apple-touch-icon (28 files)
  - Full `im-topbar` with logo + Premium CTA + 3-mode theme selector (19 files)
  - Single-file fixes: theme selector for `handbook-social-protection.html`

### Fixed
- Book counters in `BookSummaries/index.html`: total 30 → 31, dev-econ filter 6 → 7.

## [10.19.0] - 2026-04-13

### Added
- **3 new Book Summaries** (28 → 31 total):
  - *Principles for Navigating Big Debt Crises* — Ray Dalio (2018)
  - *Handbook for IPCC Authors: Climate Communications* — Corner, Shaw & Clarke (2018)
  - *Storytelling to Accelerate Climate Solutions* — Coren & Wang (Springer, 2024)
- BookSummaries index cards, search index entries, sitemap URLs, docs updates

## [10.18.0] - 2026-04-12

### Fixed
- **Sitemap coverage** — 87 missing URLs added to `sitemap.xml` (2 courses, 35 foundational, 23 BookSummaries, 18 blog posts, 9 public pages). Total: 84 → 171.
- **Stale 101.impactmojo.in links** — ~100 legacy subdomain refs migrated to local paths in `js/faq-bank.js`, `js/bookmarks-compare.js`, `js/learning-tracks.js`, `js/game-agents.js`, and 4 docs files.
- **Search index phantom labs** — 6 duplicate/phantom lab entries removed, 3 missing labs added. Lab count: 17 → 13.
- **Content count drifts** — `docs/content-guide.md` (flagship 9→11, labs 19→11), `premium.html`, `catalog.html` JS comments corrected.
- **21 `.DS_Store` files** removed from git tracking.

## [10.17.0] - 2026-04-12

### Added
- **Netlify Forms migration** — 12 forms migrated from Formspree (`xpwdvgzp`) to Netlify Forms with `data-netlify="true"`, `netlify-honeypot="bot-field"`, and unique `name` attributes. Email notifications configured for all forms via Netlify hooks API.
- **Engagement drip pipeline** — 5-stage email sequence (Day 0/3/7/14/21) in `send-notification` Edge Function with deduplication via `notifications.metadata.drip_stage`. Day 21 pitches Premium for explorer-tier users with one-time support fallback.
- **Streak tracking** — `update_streak()` PL/pgSQL function increments `profiles.streak_days` on daily login, resets on miss. Called from `auth.js:fetchProfile()` as fire-and-forget RPC.
- **Post-certificate upsell** — `issue-certificate` Edge Function now sends branded congratulations email with certificate number, verification link, and subtle Premium mention for explorer-tier users.
- **Monthly newsletter** — `netlify/functions/monthly-newsletter.mjs` scheduled function (15th, 10:00 IST) parses `docs/changelog.md` for recent additions, pulls content counts from `search-index.json`, sends via `monthly-update` endpoint.
- **Premium sales letter** — `/premium-letter.html` (15KB, standalone, dark mode, mobile responsive). Conversational tone with concrete tool examples and honest pricing rationale.
- **Practitioner Starter Kit** — `/starter-kit.html` with 10 curated handouts across M&E, data, policy, and cross-cutting tracks.
- **Branded email template** — `wrapEmail()` rewritten with navy gradient header, stacked logo, blue title bar, amber-to-red accent bar, dark footer with preference management link.
- **Resend integration** — `RESEND_API_KEY` configured in Supabase secrets. Domain `impactmojo.in` verified with DKIM, SPF, DMARC DNS records added via Netlify DNS API.
- **Notifications tables** — `notifications` and `notification_preferences` tables applied to production Supabase (were defined in migration but never run). RLS policies, indexes, `notify_user()` function, auto-preference trigger, backfill for 14 existing users.
- **Daily engagement cron** — `netlify/functions/daily-engagement.mjs` (02:30 UTC / 08:00 IST) runs engagement-drip, streak-reminders, cohort-deadlines in parallel.
- **Netlify env vars** — `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` set for scheduled functions.

### Changed
- **Netlify form detection** — `processing_settings.ignore_html_forms` changed from `true` to `false` via Netlify API.
- **Documentation** — CLAUDE.md, 4 rules files, 2 agent definitions, 3 command files, 2 skill files updated to reference Netlify Forms instead of Formspree.
- **`auth.js`** — added `supabaseClient.rpc('update_streak')` call after successful profile fetch.

### Removed
- **Formspree dependency** — all references to `https://formspree.io/f/xpwdvgzp` removed from production HTML/JS files. Backups retain historical references.

## [10.14.0] - 2026-04-07

### Added
- **Device-mode default theme resolution** on 70 pages — `:root` now carries light tokens, `@media (prefers-color-scheme: dark) { :root {} }` drives dark, and explicit `body.{light,dark}-mode` + `[data-theme="*"]` overrides keep the theme toggle dominant. Applied to blog posts, Labs, course index + lexicon pages, admin pages, book companion tools, premium tools, `transparency`, `testimonials`, `challenges`, `bct-repository`, `dataverse`, `toc-builder`, `toc-workbench`.
- **Link-in-text-block underline rule** (WCAG 2.1 AA §1.4.1) on 74 content pages — inline `<a>` inside `<main> p` / `<main> li` now carries `text-decoration: underline`, scoped to exclude button-styled anchors.
- **CC BY-NC-SA 4.0 attribution** backfilled into 17 handouts — all 84 handout pages now uniform on every brand-default check.
- **Premium topbar link** added to 11 main-site pages whose only Premium button lived inside the removed duplicate `im-topbar`.
- **Language translation widget** (`js/translate.js`) on `climate-trace-india.html` and `transparency.html`.
- **`id="home"` anchor** on `index.html` hero section so `<a href="#home">` nav links resolve (fixes pa11y NoSuchID).
- **Paper plane SVG** on `courses/gender/lexicon.html` and `courses/pubpol/lexicon.html`.
- **`<footer>` landmark** with ImpactMojo attribution on `courses/pubpol/lexicon.html`.
- **PR-comment permissions** — `accessibility.yml` + `ci.yml` now grant `pull-requests: write` (scoped per job) so `marocchino/sticky-pull-request-comment@v3` stops failing.

### Changed
- **WCAG AA muted-text contrast** bumped across 115 files mode-aware: light `--text-muted #94A3B8→#52627A` (2.56:1→6.20:1), dark `--text-muted #64748B→#94A3B8` (3.75:1→6.96:1), dark `--text-secondary #94A3B8→#CBD5E1` (6.96:1→12.02:1).
- **`catalog.html` card colours** — scoped overrides for `.card-rating` (amber `#F59E0B`→`#B45309`/`#FBBF24`) and `.card-track` (sky `#0EA5E9`→`#0369A1`/`#38BDF8`), both now pass WCAG AA.
- **Theme system unified** on `im-theme` localStorage key — `js/cookie-ui.js`, `js/account.js`, `js/game-shell.js` all read canonical first then fall back to legacy keys (`theme`, `impactmojo-theme`, `imx_theme`) for seamless migration; all writes mirrored to legacy keys. Also set `data-theme` on `<html>`.
- **Brand fonts** — `BookSummaries/ultralearning-companion.html` (was Source Serif 4) and `BookSummaries/deep-work-companion.html` (was Merriweather) migrated to Inter / Amaranth / JetBrains Mono.
- **Content counts** aligned to ground truth across 26 files (11 flagship, 38 foundational, 11 Labs, 16 Games): `README.md`, `CLAUDE.md`, catalog, index, premium, upgrade, content-marketing-kit, org-dashboard, verify-certificate, updates, PressKit, blog post, and 13 `docs/*.md` files.
- **39 pictographic emoji → Sargam line icons** across 10 content pages. Typographic symbols (✓ ✔ ✦ ✧ ⚠) left as decorative characters.
- **10 unbuilt course cards** in `catalog.html` + `catalog_data.json` marked `comingSoon: true`, rendered as disabled cards with dashed border and amber "Coming Soon" pill badge: Survey Design 101, Gender Mainstreaming 101, Mixed Methods 101, Impact Evaluation 101, Maternal Health 101, Child Development 101, Feminist Research 101, Economics 101, VaniScribe (×2).

### Fixed
- **Handout 404s** — `getHandoutURL` in `handouts.html` now serves from same-origin `/Handouts/` with URL-encoded path segments (was pointing at a stale `varnasr.github.io/ImpactMojo/` mirror).
- **Duplicate `im-topbar` covering main site nav** on 28 pages — the overlay was hiding the legacy `<header class="header">` main navigation (including all dropdowns). Removed from pages where the legacy header is the real main nav; kept on handouts, blog posts, lexicons, games, and slide decks where it's the only topbar.
- **121 of 131 stale `101.impactmojo.in` links** rewritten to self-hosted equivalents via a Python migration with filesystem existence checks.

### Removed
- **PhD-level rigor marketing language** — reverted to actual tagline.

## [10.13.0] - 2026-04-05

### Added
- **Native 101 slide decks** — Replaced Gamma.app iframe wrappers with self-hosted HTML slide decks for 3 foundational courses: Development Economics 101, MEL 101, Climate Essentials 101
- **Shared deck template** — Reusable CSS (`101-courses/native/shared/deck.css`) and JS engine (`deck.js`) for all native 101 decks: light/dark/system theme, keyboard/touch/swipe nav, fullscreen, Chart.js integration, viewport scaling
- **17 Chart.js visualisations** in Dev Econ 101 (poverty trends, Lorenz curve, convergence trajectories, structural transformation, India GDP growth, rural credit, HCI comparison, UPI growth, global trade, FDI, RCT publications, caste income, urbanisation, SDG progress, jobless growth)

### Changed
- **101 deck CSS** — Proportionally larger fonts, padding, and gaps across all slide components to fill 1280×720 viewport: titles 32px/26px, body 16px, bullets 16px, stat numbers 36px, quotes 20px, charts 230px height
- **Inline style overrides** — Bumped 200+ hardcoded inline font sizes (11→13px, 12→14px, 13→15px) that CSS classes couldn't override
- **Dev Econ CTA** — "Explore the Full Course" → "Explore the Flagship Course"

### Fixed
- **Slide navigation** — Slides 51–100 were outside `slide-viewport` div in all Claude Chat-generated decks, making them unreachable by nav JS
- **JS syntax error** — Literal newlines inside Chart.js label strings broke entire script block
- **`chartsInit` declaration order** — Variable referenced before declaration in Dev Econ deck

## [10.12.0] - 2026-03-31

### Added
- **Self-hosted Docsify documentation** — Replaced GitBook with branded Docsify at `/docs/`, featuring dark/light/system theme, full-text search, code copy, prev/next pagination, Google Translate (14 South Asian languages), ImpactMojo branding (Inter + Amaranth + JetBrains Mono fonts, brand colors)
- **GitHub org profile README** — `.github/profile/README.md` visible at github.com/ImpactMojo

### Changed
- **Repository moved to ImpactMojo org** — All 200+ GitHub URLs updated from `Varnasr/ImpactMojo` to `ImpactMojo/ImpactMojo` across HTML, docs, config, and data files
- **MCP package scope** — `@varnasr/impactmojo-mcp-server` → `@impactmojo/impactmojo-mcp-server`
- **Netlify repo connection** — Updated from `Varnasr/ImpactMojo` to `ImpactMojo/ImpactMojo`
- **GitHub org settings** — Avatar, description, URL, email, location, and 16 repo topics configured
- **Sister repo links** — README and blog references to ImpactLex, PolicyDhara, dev-case-studies, etc. updated to org
- **`_redirects`** — Removed GitBook proxy, added Docsify SPA fallback; updated `varnasr.github.io` → `impactmojo.github.io`

### Removed
- **GitBook dependency** — No longer proxying to `impactmojo.gitbook.io`; all docs self-hosted

## [10.11.0] - 2026-03-28

### Added
- **Blog: Introducing the ImpactMojo MCP Server** — New blog post at `/blog/impactmojo-mcp-server.html` with 2 napkin.ai-generated illustrations, added card to `blog.html`
- **Napkin.ai blog illustrations** — Generated real infographics for the open source blog post (`github-open-dev-ecosystem`) replacing placeholder images, using the Napkin.ai API
- **CMK: 5 new LinkedIn posts** (LI-11 through LI-15) — Climate & Sustainability, Gender & Inclusion, AI in Development, Book Companions, MCP Server Launch. Total assets: 25 → 30
- **Housekeeping: CMK brochure update step** — Added Content Marketing Kit and brochure PDF to the counts/references checklist in `housekeeping/SKILL.md`

### Changed
- **CMK: Broadened scope beyond economics** — Renamed "Economics Games" to "Interactive Learning Games" across IG-04, LI-07, CR-03; updated headlines and hashtags
- **CMK: Corrected content counts** — 48 → 9 courses, 16 → 16 games, 247 → 270 dataverse throughout all captions and visuals
- **CMK: Redesigned brochure thumbnails** — Replaced plain colored boxes with content-preview thumbnails showing actual page content
- **CMK: Updated year** — "Content Kit 2025" → "Content Kit 2026"

## [10.10.0] - 2026-03-27

### Added
- **ImpactMojo MCP Server** — New `/mcp-server/` directory with a standalone TypeScript MCP server exposing the full knowledge base via Model Context Protocol. 11 tools (search_content, lookup_bct, search_bcts, list_bct_categories, browse_dataverse, search_dataverse, list_challenges, get_challenge, list_courses, get_game_info, query_climate_data) and 3 resources (overview, catalog, tracks). Compatible with Claude Desktop, Claude Code, Cursor, and any MCP client.
- **Dataverse entry** — Added `impactmojo-mcp` to Education & Learning category (269→270 items)
- **Search index entry** — Added MCP server to `data/search-index.json`
- **Published to GitHub Packages** — `@varnasr/impactmojo-mcp-server@1.0.0` with auto-publish GitHub Action on `mcp-server/v*` tags

## [10.8.1] - 2026-03-20

### Added
- **BookSummaries landing page** — `/BookSummaries/index.html` so navigation goes to a browsable landing page instead of directly to the Hanna book

### Fixed
- **RQ Premium redirect loop** — Race condition in `resource-launch.js` where clicking Research Question Builder before `premium.js` initializes redirected to login instead of showing the upgrade modal
- **Premium page design consistency** — Updated `premium.html` cards to use main site design standards (3px borders, 20px radius, offset box-shadows)
- **Premium tool fonts** — Updated `code-converter-pro.html` and `qual-insights-lab.html` to use ImpactMojo fonts (Amaranth/Inter/JetBrains Mono) and color palette instead of Segoe UI

## [10.8.0] - 2026-03-20

### Added
- **Cohort-based learning** — Supabase-backed cohorts with start/end dates, member enrollment, progress tracking, and deadline countdown (org dashboard Training tab)
- **Cohort discussion threads** — Real-time discussion within cohorts with post/delete support
- **Notification system** — `send-notification` Edge Function with streak reminders, cohort deadline alerts, and manual notification API
- **Notification preferences** — Per-user email opt-in/out (course updates, streak reminders, cohort deadlines, discussions, assignments, certificates) with digest frequency
- **In-app notification feed** — Recent notifications card on account page with unread badges and mark-as-read
- **Database migration** — `cohorts`, `cohort_members`, `cohort_discussions`, `notifications`, `notification_preferences` tables with full RLS policies, indexes, and triggers

### Changed
- **Auth session recovery** — Faster safety-net (1.5s + 4s fallback), increased SIGNED_OUT debounce to 1000ms, aggressive `_recoverSessionFromStorage()` for stored sessions, window.load recovery
- **API token documentation** — Added Gemini, DeepSeek, Grok, Sarvan.ai, Gamma to CLAUDE.md and .env.example

### Fixed
- **Gender equity game** — SVG viewBox too short, causing Madhubani art heads to be clipped
- **Info asymmetry game** — Pattachitra frame and end-story-art missing `width:100%`, appearing too small on mobile
- **Login persistence** — Session not surviving page navigation due to timing gaps in token refresh cycle

## [10.7.0] - 2026-03-20

### Added
- **BookSummaries** — New content type under Specials: interactive book summaries
- **The Handbook of Social Protection** (Hanna & Olken, MIT Press 2026) — first interactive book companion with chapter navigator, evidence explorer, data playground, programme compare, glossary, South Asia lens, and AI-powered Q&A
- BookSummaries entry added to Specials dropdown nav, catalog, sitemap, and search index
- **Claude Code global skills** — 6 repo-level skills (github-ops, netlify-ops, supabase-ops, gemini-ai, gamma-ops, housekeeping) for Claude Code on the web
- **SessionStart hook** — auto-loads API keys (Gemini, Gamma, DeepSeek, Grok, Sarvan.ai) from gitignored `.claude/.env.keys`
- **API token documentation** — CLAUDE.md updated with all 8 environment tokens

### Changed
- **`.env.example` updated** with Grok, Sarvan.ai, and Gamma API key placeholders
- **`.claude/settings.json`** now registers both SessionStart and Stop hooks
- **`.gitignore`** updated to protect `.claude/.env.keys` from commits

## [10.6.0] - 2026-03-19

### Added
- **Field Notes Pro** — 70 curated development economics field notes deployed as premium tool at `impactmojo-field-notes-pro.netlify.app`
- **Workshop Pro** — 7 interactive workshop templates (ToC, Logframe, Chart Selector, Stakeholder Mapping, Empathy Canvas, Policy Canvas, AI Canvas) deployed at `impactmojo-workshop-pro.netlify.app`
- **Field Notes JSON editor** link added to admin dashboard — edit `data/notes.json` directly from GitHub
- **Server-side auth-gate** on all new premium Netlify resource sites with `RESOURCE_TOKEN_SECRET` env vars configured

### Changed
- **Removed `mobile-index.html`** — `index.html` is now fully responsive, no separate mobile page needed
- **Updated all doc counts** — labs 10→19, games 12→16, Dataverse 215→247 across platform-overview, content-guide, architecture docs
- **Architecture docs updated** — full tier access control matrix with all 16 resource IDs
- **GitBook changelog updated** through v10.5.1
- **Sitemap timestamps refreshed** to 2026-03-19
- **ROADMAP.md updated** with Q1 2026 completions (workshop templates, field notes, auth-gate, mobile removal)
- **CLAUDE.md updated** — removed stale mobile-index.html checklist item
- **GitHub repo description updated** with current counts

## [10.5.1] - 2026-03-19

### Fixed
- **Admin tier reset bug** — admin accounts (varna.sr@gmail.com, varna@pinpointventures.in, vsoni.1986@gmail.com) were intermittently shown as free/explorer tier due to stale localStorage cache when profile fetch timed out
- **Profile fetch timeout** increased from 5s to 8s to reduce cache fallback on slow connections
- **Profile fetch retry** — failed fetches now auto-retry after 5 seconds so stale cached tier doesn't persist

### Added
- **Admin tier protection trigger** (`protect_admin_tier`) — database trigger prevents client-side downgrades of admin role, subscription tier, or subscription status
- **Idempotent profile creation** — `handle_new_user()` trigger now uses `ON CONFLICT DO NOTHING` to prevent overwriting existing profiles on re-authentication

## [10.5.0] - 2026-03-19

### Added
- **RQ Builder Pro** premium card — Practitioner tier, guided research question builder with PICO/SPIDER framing
- **TOC Workbench Pro** premium card — Practitioner tier, advanced Theory of Change building with assumption mapping and PDF/PNG export
- Both new tools added to premium modal, mobile-index.html, and search index

### Changed
- **Premium tool count updated from 7 → 9** across all pages and docs (catalog.html, content-catalog.md, faq.md, architecture.md, premium-tools-guide.md)
- **All 9 premium cards modernized with unique Sargam icons** — replaced generic si_Flare/imx-star badges with contextual icons (si_Search, si_Crosshair_detailed, si_Direction_alt, si_Library_books, si_Bar_chart, si_Database, si_Chat, si_Activity, si_Lightning)
- **Compact premium cards reformatted** to consistent expanded multi-line style matching the rest of the section
- **Tier access matrix updated** in architecture.md to include `toc-workbench-pro`

## [10.4.1] - 2026-03-19

### Changed
- **All 11 labs aligned to ImpactMojo standard design** — 3-button theme selector (System/Light/Dark), floating paper plane SVG decoration, sargamicon header badges
- **Theme persistence** — labs now share the `impactmojo-theme` localStorage key with system-preference awareness

## [10.4.0] - 2026-03-18

### Added
- **7 new self-hosted interactive labs** — Design Thinking, Impact Partnerships, Resource Sustainability, Policy Advocacy, MEL Design, MEL Plan Builder, Gender Analysis (all in `/courses/`)
- **Lab links updated** — all lab links in index.html now point to self-hosted files instead of `101.impactmojo.in`

### Changed
- **Lab count updated** from 12 to 19 across README and platform pages
- **Sitemap updated** with 7 new lab page entries
- **Search index updated** with entries for all new labs

## [10.3.0] - 2026-03-18

### Added
- **3 new games** beyond economics: Climate Action (Warli art), Gender Equity/Care Economy (Madhubani art), Public Health/Epidemic Response (Pattachitra art)
- **Indian folk art story illustrations** across all 12 existing games — intro screens, mid-game interludes, and adaptive ending art in 6 styles (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- **Sample Size Calculator** lab tool — 4 modes (proportion, mean, two-group, cluster sampling) with educational content
- **Budget Template Generator** lab tool — 7 budget categories, 5 smart templates, CSV/clipboard export
- **Admin dashboard panels** — User Management (search, filter, pagination) and Site Settings (feature flags, metadata, integrations, backups)
- **Accessibility improvements** — skip-nav links, ARIA landmarks, focus-visible styles, screen-reader labels on index, mobile-index, about, catalog
- **Claude Code project config** — `.claude/CLAUDE.md`, Stop hook for housekeeping, `/housekeeping` skill

### Changed
- **Renamed "Economics Games" → "Games"** across 14 files (now covers broader topics)
- **Fixed card text contrast** across 8 games — increased badge opacity, darkened text, added text-shadows (WCAG AA)
- **Fixed Dojos nav icon** — was duplicating Flagship Courses icon, now uses Activity icon
- **Fixed PolicyDhara workflow** — commit-msg prefix mismatch causing all scheduled runs to fail

### Removed
- **12 old Netlify game sites** deleted — all games now self-hosted in `/Games/`

## [10.2.0] - 2026-03-17

### Added
- **Self-hosted interactive games** in `/Games/` folder — replacing old Netlify-hosted apps at 101.impactmojo.in
- **MiroFish AI agent engine** (`supabase/functions/game-agent/`) — multi-provider LLM support with automatic fallback chain (DeepSeek → Groq → Gemini → Together → OpenAI)
- **30+ AI agent personas** (`data/game-agents.json`) — South Asian development practitioners with distinct personalities, backstories, and strategic behaviours
- **Game agents client library** (`js/game-agents.js`) — browser-side integration with Edge Function + local fallback engine
- **LLM provider secrets** configured: Groq, Google Gemini, DeepSeek API keys set as Supabase secrets

### Changed
- **Game links in index.html** — all 12 game links updated from `101.impactmojo.in/*` to `/Games/*.html`
- **game-agents.js Supabase URL** — corrected to actual project endpoint

### Games Built
- Public Good Game (free-rider problem, 4 AI agents)
- Prisoners' Dilemma (strategic interdependence, 4 AI agents)
- Commons Crisis (tragedy of the commons, 4 AI agents)
- Cooperation Paradox (Nash vs Pareto, 2 AI agents)
- Opportunity Cost (budget allocation, 2 AI agents)
- Risk & Reward Explorer (prospect theory, 3 AI agents)
- Bidding Wars (auction theory, 3 AI agents)
- Information Asymmetry (lemons problem, 3 AI agents)
- Network Effects (platform adoption, 3 AI agents)
- Externality Game (Pigouvian tax, 3 AI agents)
- The Real Middle (India income inequality)
- Econ Concepts Puzzle (12 brain-teasers)

## [10.1.0] - 2026-03-16

### Added
- **Git best-practice standards** propagated across all 29 ImpactMojo repos: `.gitattributes`, `.editorconfig`, `.githooks/pre-commit`, `.githooks/commit-msg`, `.gitmessage`, `.github/CODEOWNERS`, `.github/SECURITY.md`, `.github/dependabot.yml`, `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/` (bug report, feature request, content issue)
- **Dependabot** configured per-repo (npm, pip, github-actions ecosystems auto-detected)
- **Pre-commit hook** blocks secrets (.env, .pem, .key), debugger statements, merge conflict markers; warns on console.log and files >500KB
- **Commit-msg hook** enforces prefix convention (Add/Fix/Update/Translate/Docs/Refactor/Test/CI/Chore)

### Fixed
- **Broken GitBook sidebar links**: Added `/impactmojo/*` → `/docs/*` Netlify redirects so sidebar navigation on impactmojo.in/docs works correctly

## [10.0.0] - 2026-03-16

### Added
- **What's New section** on mobile homepage — 8 feature cards highlighting new courses, DevData, Case Studies, DevDiscourses
- **Wall of Love section** on mobile homepage — horizontally scrollable testimonial cards in 6 languages (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- **4 new course pages** linked: Politics of Aspiration, Media for Development, Constitution & Law, Social-Emotional Learning
- **Canvas line charts** on admin dashboard and transparency page — smooth Catmull-Rom spline rendering with gradient fills, replacing bar charts
- **Revenue model section** on transparency page — Explorer (free) vs Practitioner/Organisation (paid) tier cards

### Changed
- **Font standardization across 80 files**: Amaranth (body text) + Inter (headings) + JetBrains Mono (code). Removed Poppins, Fraunces, Merriweather, Source Serif 4, Source Sans 3, Cormorant Garamond. All fallback chains standardized
- **Google Fonts loading standardized**: Amaranth:400,700 + Inter:400-800 + JetBrains Mono:400,500. Consistent weight ranges across all pages
- **Transparency page redesigned**: renamed from "Transparency & Analytics", simplified data model (Legacy + GA4 = Totals), added methodology section
- **Admin dashboard redesigned**: removed one-time Supabase setup section, replaced bar charts with canvas line charts, games & tools charts in two-column layout
- **Org dashboard modal polished**: Create Learning Path modal — tighter padding, compact course rows, pill-shaped category buttons, proper light theme checkbox styling
- **Dashboard tabs** now accept profile parameter directly, fixing race condition where tabs showed wrong role/tier

### Fixed
- **Auth gate race condition**: `authStateChanged` event fired before profile fetch completed, causing premature access denial. Both `admin-gate.js` and `auth-gate.js` now await `fetchProfile()` before checking roles
- **Dashboard tabs wrong role**: `DashboardTabs.init()` relied on global `ImpactMojoAuth.profile` which wasn't set yet. Fixed by passing profile from auth callback
- **Mobile hamburger cutting off logo**: hidden desktop-only elements (theme selector, tour toggle, starburst badge, nav buttons) on mobile across `index.html`, `account.html`, `org-dashboard.html`, `mobile-index.html`
- **Mobile logo truncation**: removed `overflow:hidden` + `text-overflow:ellipsis` that was truncating "ImpactMojo" to "Impact..." on mobile-index.html

### Removed
- One-off fonts: Fraunces (dojos), Merriweather (about), Source Serif 4 (lexicons), Source Sans 3 (gandhi), Cormorant Garamond (gandhi)
- Supabase one-time setup section from admin dashboard
- Bar chart rendering code from admin and transparency pages

## [9.5.0] - 2026-03-15

### Added
- Unified dashboard tab navigation across account, org, admin, and analytics pages
- Team training packages for organizations (pre-built training paths, facilitator guides, assessment rubrics, cohort management)

## [9.1.0] - 2026-03-07

### Added
- **PolicyDhara** as 4th free resource (homepage, mobile, nav dropdown) linking to https://on-web.link/PolicyDhara
- Organization Dashboard content: welcome getting-started guide, "What's Included" feature grid, "Coming Soon for Teams" roadmap preview
- New roadmap items: Open Badges & Micro-credentials (#30), Live Case Challenges (#31)
- GitHub Issues for all roadmap features (#25-#31)

### Changed
- Org dashboard loads members and paths in parallel (`Promise.all`) for faster rendering
- Added `preconnect` hints for Supabase and CDN on org dashboard

### Fixed
- Org dashboard auth gate now waits for auth to fully resolve before checking tier access
- Google OAuth sign-in no longer triggers redundant profile fetch/sync on redirect

### Removed
- "Qualitative Data Lab" from roadmap (already live as Qual Insights Lab)
- "AI Learning Assistant" from roadmap (commoditized by general AI agents)

## [9.0.0] - 2026-03-06

### Added
- JWT-based premium access control for all resource sites
- Netlify Edge Functions (auth-gate) on 4 premium tool sites
- Supabase Edge Function for minting resource tokens
- `resource-launch.js` — client-side JWT launcher for premium tools
- `token-gate.js` — client-side token verification
- GitHub Wiki with 7 documentation pages
- GitHub Discussions with 12 seed conversations
- GitHub Actions CI for broken links and accessibility checks
- `.editorconfig` for consistent formatting
- `CHANGELOG.md` (this file)
- JSON-LD structured data for SEO

### Changed
- README rewritten with business models (Workshops, Coaching, Dojos, Premium tiers)
- README Netlify badge fixed (was using wrong site ID format)
- README version bumped to 9.0.0

### Fixed
- Broken Netlify deploy status badge in README
- `RESOURCE_SECRET_TOKEN` typo on premium resource site (renamed to `RESOURCE_TOKEN_SECRET`)

## [8.0.0] - 2026-02-28

### Added
- Performance optimization: extracted 160KB inline JS to deferred external files
- `js/bookmarks-compare.js` — bookmarks and course comparison logic
- `js/cookie-ui.js` — cookie consent banner
- `js/learning-tracks.js` — learning track navigation
- `js/mobile-ui.js` — mobile-specific UI logic
- Service worker upgraded with versioned cache and network-first strategy
- Font subsetting (Latin + Devanagari only)
- Community channels added to premium registration form

### Changed
- Inline JavaScript extracted from `index.html` (reduced from ~200KB to ~40KB)
- Service worker cache version bumped with proper invalidation

## [7.0.0] - 2026-02-15

### Added
- Premium membership tiers (Explorer, Practitioner, Professional, Organization)
- Supabase authentication (Email, Google OAuth, Magic Links)
- User profiles with progress tracking
- Bookmarks, personal notes, and reading lists
- Course comparison feature
- 38 foundational courses across 6 learning tracks
- 12 economics learning games
- 10 interactive labs
- ImpactLex PWA with 500+ terms
- Dev Case Studies library (200 cases, 117 countries)
- DevDiscourses (500+ curated papers and books)
- 400+ downloadable handouts
- Multilingual support (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- Coaching and workshop booking pages
- Dojos skill session page
- Blog (Learning Loops) and podcast (Between the Logframes)

[10.7.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.6.0...v10.7.0
[10.6.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.5.1...v10.6.0
[10.5.1]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.5.0...v10.5.1
[10.5.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.4.1...v10.5.0
[10.4.1]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.4.0...v10.4.1
[10.4.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.3.0...v10.4.0
[10.3.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.2.0...v10.3.0
[10.2.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.1.0...v10.2.0
[10.1.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.0.0...v10.1.0
[10.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.5.0...v10.0.0
[9.5.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.1.0...v9.5.0
[9.1.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.0.0...v9.1.0
[9.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v8.0.0...v9.0.0
[8.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v7.0.0...v8.0.0
[7.0.0]: https://github.com/ImpactMojo/ImpactMojo/releases/tag/v7.0.0

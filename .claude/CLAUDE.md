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
- Ensure no broken links in navigation (desktop and mobile)
- Verify mobile responsiveness for new UI
- Check text contrast/readability (WCAG AA minimum)
- Test all forms submit to correct Formspree endpoint (`xpwdvgzp`)
- No hardcoded secrets or credentials committed

## Code Style

- Games are single self-contained HTML files (HTML + CSS + JS, no build step)
- Use CSS custom properties for theming
- Indian folk art styles for game illustrations (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- All card/badge text must have high contrast — no white text on light backgrounds
- Mobile-first responsive design
- Prefer editing existing files over creating new ones

## API Tokens (available in environment)

- **GitHub**: Use `$GITHUB_PAT` for all GitHub API calls (PRs, merges, issues). Call `https://api.github.com/repos/Varnasr/ImpactMojo/...` with header `Authorization: token $GITHUB_PAT`.
- **Supabase**: Use `$SUPABASE_PAT` for Supabase Management API calls (database queries, migrations). Call `https://api.supabase.com/v1/projects/ddyszmfffyedolkcugld/...` with header `Authorization: Bearer $SUPABASE_PAT`.
- **Netlify**: Use `$NETLIFY_PAT` for Netlify API calls if needed.
- **Gemini**: Use `$GEMINI_API_KEY` for Google Gemini AI API calls. Pass as `?key=$GEMINI_API_KEY` query parameter.
- **Gamma**: Use `$GAMMA_API_KEY` for Gamma presentation API. Header: `Authorization: Bearer $GAMMA_API_KEY`.
- **DeepSeek**: Use `$DEEPSEEK_API_KEY` for DeepSeek LLM API calls.
- **Grok**: Use `$GROK_API_KEY` for xAI Grok API calls.
- **Sarvan.ai**: Use `$SARVAN_API_KEY` for Sarvan.ai Indic language model API calls.
- Always prefer these tokens over `gh` CLI or local git proxy for creating PRs, merging, and managing issues.

## Git Practices

- Write concise commit messages focused on "why" not "what"
- Never force-push to main
- Never commit .env files or secrets
- Stage files explicitly, avoid `git add -A`

## Global Writing Rules for All Output

These rules apply to ALL prose produced in this workspace: comments, docstrings,
commit messages, READMEs, reports, summaries, inline documentation, and any
written communication. Sources: tropes.fyi and Wikipedia: Signs of AI Writing
(WikiProject AI Cleanup).

### Word Choice

Never use these words or their close variants:

- "delve", "certainly", "utilize", "leverage" (as a verb), "robust",
  "streamline", "harness", "foster", "underscore", "enhance", "testament",
  "pivotal", "intricate", "crucial", "transformative", "groundbreaking"
- Magic adverbs that assert significance without proof: "quietly", "deeply",
  "fundamentally", "remarkably", "arguably"
- Grandiose nouns where plain ones work: "tapestry", "landscape" (as a
  domain metaphor), "paradigm", "synergy", "ecosystem" (as a vague catch-all),
  "framework" (as a vague catch-all)
- Pompous copula substitutes: "serves as", "stands as", "marks", "represents"
  where "is" is correct
- Vague cultural praise: "rich cultural heritage", "enduring legacy",
  "scenic", "breathtaking", "clean and modern"
- Invented analytical labels: compound noun phrases using "paradox", "trap",
  "creep", "vacuum", "inversion" that are not established terms in the field

### Sentence Structure

- No negative parallelism: "It's not X, it's Y" / "Not because X, but
  because Y" / "The question isn't X. The question is Y."
- No dramatic countdown: "Not X. Not Y. Just Z."
- No self-answering rhetorical questions for effect: "The result? Devastating."
- No anaphora abuse: repeating the same sentence opener three or more
  times in quick succession
- No compulsive rule-of-three: a single tricolon can work; multiple
  back-to-back tricolons read as a pattern, not a choice
- No empty transition phrases: "It's worth noting", "It bears mentioning",
  "Importantly", "Interestingly", "Notably" when used as filler connectors
- No tacked-on present participle analysis: "...highlighting its importance",
  "...reflecting broader trends", "...underscoring its role"
- No false ranges: "From innovation to cultural transformation." List two
  things as two things; do not dress them up as a spectrum
- No "Not only X, but Y" contrasts manufactured where no real tension exists
- No passive authority: "X has been described as..." without a named source

### Document and Paragraph Structure

- No short punchy fragments as standalone paragraphs for manufactured emphasis
- No disguised lists: do not write "The first... The second... The third..."
  when you mean a list. Use a list or write a real paragraph.
- No fractal summaries: no section previews, no mid-document recaps, no
  conclusions that only restate the body. Say it once, well.
- No dead metaphor repetition: introduce a metaphor, use it, move on
- No historical analogy stacking to fake authority
- No one-point dilution: do not restate a single argument in multiple
  metaphors across thousands of words
- No structural announcements: no "In conclusion", "To sum up", "In summary"
- No "Despite its challenges..." formula

### Tone and Voice

- No false suspense: "Here's the kicker", "Here's the thing", "Here's where
  it gets interesting", "Here's what most people miss", "Here's the deal"
- No patronising teacher mode: "Think of it as...", "It's like a...",
  "Let's break this down", "Let's unpack this", "Let's dive in", "Let's explore"
- No futurist invitation openings: "Imagine a world where..."
- No performed vulnerability as a rhetorical device
- No asserted clarity: "The reality is simple", "History is unambiguous"
- No stakes inflation: scale claims to what the evidence actually supports
- No vague attribution: "Experts argue", "Industry reports suggest",
  "Observers have noted." Name the source or do not cite it
- No inflated importance puffing: do not add sentences explaining why a
  mundane detail is significant for broader themes or legacies

### Formatting

- No em dashes. Use commas, parentheses, or restructure the sentence.
- No bold-first bullets: do not begin every list item with a bolded keyword
- No unicode arrows or decorative special characters in prose
- No formatting as a substitute for argument
- No emojis in READMEs, commit messages, or documentation unless the project
  explicitly requires them

### Code Comments and Documentation Specifically

- Write comments that explain why, not what. The code already says what.
- No comments that restate the function signature in prose
- No docstrings that begin "This function..." followed by a restatement of
  the function name
- Commit messages: imperative mood, specific, no filler. "Fix off-by-one in
  pagination" not "Made some improvements to the codebase."
- READMEs: no grandiose mission statements for routine utilities. State what
  it does and how to use it.

### The Core Principle

Write with specificity. Vague language, inflated stakes, performed structure,
and manufactured drama are not style choices; they are evasions.
Any single pattern used once, deliberately, may be fine.
The problem is frequency, unconscious repetition, and substituting
pattern for thought.

---
name: add-files
description: Add new content files (games, labs, courses, handouts) to ImpactMojo with all required cross-references updated automatically. Use when the user says "add a game", "create a new lab", "add a course", "new handout", or wants to add any content to the platform.
---

# Add Files to ImpactMojo

Guided workflow for adding new content to the platform. Handles file creation and all required cross-reference updates.

## Step 1 — Identify Content Type

Ask the user what they want to add:

| Type | Location | Naming Convention |
|---|---|---|
| **Game** | `/Games/{game-name}.html` | Kebab-case, descriptive name |
| **Lab** | `/Labs/{lab-name}-lab.html` | Kebab-case with `-lab` suffix |
| **Flagship Course** | `/courses/{name}/index.html` | Folder per course |
| **Foundational Course** | Catalog entry (may link externally) | — |
| **Handout** | `/Handouts/{Track}/{name}.html` | Organized by track folder |

## Step 2 — Create the Content File

### For Games
- Create a single self-contained HTML file in `/Games/`
- Must include: inline CSS, inline JS, responsive meta tags
- Use Indian folk art style for illustrations (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- No external dependencies — everything in one file
- Reference existing games for structure: `/Games/prisoners-dilemma-game.html`

### For Labs
- Create HTML file in `/Labs/` with `-lab.html` suffix
- Include guided workflow with step-by-step prompts
- Browser-based, client-side only
- Reference existing labs for structure: `/Labs/mel-design-lab.html`

### For Courses
- **Flagship**: Create folder `/courses/{name}/` with `index.html` and supporting files
- **Foundational**: Add catalog entry; may link to `101.impactmojo.in` or self-hosted page

### For Handouts
- Create HTML file in appropriate `/Handouts/{Track}/` subfolder
- Tracks: MEL, DataTech, Policy, Gender, Health, Philosophy, Governance, Communication, BCT, Games, Labs

## Step 3 — Update Cross-References (ALL required)

After creating the content file, update these locations:

### 3a. index.html
- Add link to the new content in the appropriate section (games grid, labs grid, courses section)
- Update content counts (e.g., "16 Games" → "17 Games") — search for ALL occurrences across nav, hero, feature cards, sidebar
- Counts appear in multiple places — use grep to find all instances

### 3b. data/search-index.json
- Add a new entry with this structure:
```json
{
  "id": "<TYPE><NUMBER>",
  "title": "Content Title",
  "description": "Brief description of the content",
  "type": "game|lab|course|handout",
  "category": "Relevant Category",
  "url": "/path/to/file.html",
  "tags": ["Tag1", "Tag2"]
}
```

### 3c. catalog.html / catalog_data.json
- Add entry to catalog if it's a course or significant content piece
- Include: title, type, track, level, link

### 3d. Documentation (docs/)
- **Games**: Update `docs/games-guide.md` with description, learning objectives, how to use
- **Labs**: Update `docs/labs-guide.md`
- **Courses**: Update `docs/content-guide.md` and `docs/content-catalog.md`
- **Any**: Update `docs/platform-overview.md` if it changes platform scope

### 3e. CHANGELOG.md
- Add entry under current date: `### Added` section
- Format: `- **New {Type}**: {Title} — {brief description}`

### 3f. sitemap.xml
- Add `<url>` entry for the new page

## Step 4 — Backup

- Copy current `index.html` to `Backups/` before making changes:
  ```bash
  cp index.html Backups/index-backup-$(date +%Y%m%d-%H%M).html
  ```

## Step 5 — Verify

Run these checks after adding content:

1. **Count consistency**: Grep for old count numbers across all HTML files to ensure none were missed
2. **Link validity**: Verify the new file path is correct and accessible
3. **Search index**: Validate `data/search-index.json` is valid JSON
4. **No stale refs**: Check new content doesn't link to `101.impactmojo.in` when it should be self-hosted

## Step 6 — GitHub "Alive Docs" Updates

After verifying the content:

1. **GitHub Wiki** — clone `Varnasr/ImpactMojo.wiki.git`, update relevant pages (Content-Guide, Changelog, and type-specific pages like Book-Summaries or 101-Course-Decks), push
2. **GitHub Discussion** — create an Announcements discussion for significant new content (games, courses, book summaries)
3. **GitHub Issues** — close related tracking issues with links to the commit/PR

## Quick Reference — Minimum Updates Per Type

| Update Location | Game | Lab | Course | Handout |
|---|---|---|---|---|
| Create file | Y | Y | Y | Y |
| index.html (link) | Y | Y | Y | — |
| index.html (counts) | Y | Y | Y | — |
| search-index.json | Y | Y | Y | Y |
| catalog.html | — | — | Y | — |
| catalog_data.json | — | — | Y | — |
| docs/games-guide.md | Y | — | — | — |
| docs/labs-guide.md | — | Y | — | — |
| docs/content-guide.md | — | — | Y | — |
| CHANGELOG.md | Y | Y | Y | Y |
| sitemap.xml | Y | Y | Y | — |
| Backup index.html | Y | Y | Y | — |
| GitHub Wiki | Y | — | Y | — |
| GitHub Discussion | Y | — | Y | — |

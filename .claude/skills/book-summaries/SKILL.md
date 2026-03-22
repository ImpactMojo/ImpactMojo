---
name: book-summaries
description: Create interactive book companion pages for BookSummaries/. Use when the user asks to add a book summary, create a book companion, or summarize a development economics text.
---

# Book Summaries Skill

Create interactive book companion pages for key texts in development economics, social protection, and public policy.

## When to Use

- User says "add a book summary", "create a book companion", "summarize this book"
- User wants to create an interactive guide for a development economics text
- User provides a book title or PDF to summarize

## Directory Structure

```
BookSummaries/
├── index.html                        # Listing page for all companions
├── handbook-social-protection.html   # Social protection handbook
├── debraj-ray-companion.html         # Debraj Ray's Development Economics
├── dt-companion.html                 # Development as Freedom (Sen)
└── {new-companion}.html              # New companions go here
```

## Creating a New Book Companion

### 1. File Naming

Use kebab-case: `{author-or-short-title}-companion.html`

Examples:
- `banerjee-duflo-companion.html` (Poor Economics)
- `easterly-companion.html` (The Elusive Quest for Growth)
- `dreze-sen-companion.html` (An Uncertain Glory)

### 2. HTML Template

Follow the existing companion structure:
- Same CSS variables as the main site (see `BookSummaries/index.html` for reference)
- Google Analytics tag (`G-JRCMEB9TBW`)
- Responsive viewport meta
- Dark/light mode support
- Favicon links

### 3. Content Structure

Each companion should include:

```
1. Book Overview
   - Title, author(s), publication year
   - Why this book matters for practitioners
   - Key themes (3-5 bullet points)

2. Chapter-by-Chapter Summaries
   - Chapter title and core argument
   - Key concepts defined
   - Evidence and examples cited
   - Practitioner takeaways

3. Interactive Elements
   - Expandable/collapsible sections per chapter
   - Key term definitions (hover or click)
   - Cross-references to ImpactMojo courses/labs where relevant

4. Quick Reference
   - Key frameworks or models from the book
   - Important data points or statistics
   - Recommended reading order (if non-linear reading is useful)
```

### 4. Cross-Reference Checklist

After creating the companion:

1. **Add card to `BookSummaries/index.html`** — add a companion card following existing pattern
2. **Add to search index** — `data/search-index.json`:
   ```json
   {"id": "BOOK{NNN}", "title": "...", "description": "...", "type": "book-summary", "category": "...", "url": "/BookSummaries/{slug}.html", "tags": [...]}
   ```
3. **Update sitemap.xml** — add `<url>` entry
4. **Update content counts** — grep for book summary counts in `index.html`, `catalog.html`
5. **Update changelog** — `docs/changelog.md`
6. **Link from related courses** — if the book maps to an existing course, add a link in the course page

### 5. GitBook Documentation Updates

7. **Update `docs/book-summaries-guide.md`** — add the new book to the "Available Books" table
8. **Update `docs/content-catalog.md`** — add row to the BookSummaries table, update count in heading
9. **Update `docs/platform-overview.md`** — update BookSummaries entry with new book count and title
10. **Update `docs/content-guide.md`** — update BookSummaries count in the content types table
11. **Update `docs/roadmap.md`** — if this was a roadmap item, mark it complete

### 6. GitHub "Alive Docs" Updates

12. **Create GitHub Discussion** (Announcements category) — announce the new book companion with title, author, chapter count, features, and link. Use GraphQL API:
    ```bash
    curl -s -X POST "https://api.github.com/graphql" \
      -H "Authorization: bearer $GITHUB_PAT" \
      -d '{"query": "mutation { createDiscussion(input: {repositoryId: \"...\", categoryId: \"...\", title: \"...\", body: \"...\"}) { discussion { url } } }"}'
    ```
13. **Update GitHub Issue #272** — check off the new book in the BookSummaries expansion tracking issue
14. **Update GitHub Wiki** — clone `Varnasr/ImpactMojo.wiki.git`, update `Book-Summaries.md` and `Content-Guide.md` with the new entry, push
15. **Comment on related discussions** — if Discussion #276 ("Which books should we summarise next?") listed this book, comment confirming it's now live

## Writing Guidelines

- **Practitioner-first**: explain why each concept matters for fieldwork
- **Evidence-focused**: highlight the empirical evidence, not just theory
- **South Asian lens**: connect to Indian/South Asian development context where possible
- **Accessible language**: avoid jargon; define technical terms inline
- **Length**: aim for comprehensive coverage — companions can be 5,000–15,000 words
- **Attribution**: always cite the original author; these are companions, not replacements

## Quality Checks

- Validate HTML structure matches existing companions
- Ensure dark mode works (test CSS variables)
- Check all expandable/collapsible sections function correctly
- Verify responsive layout on mobile widths
- Run `python3 -m json.tool data/search-index.json > /dev/null` after updating search index

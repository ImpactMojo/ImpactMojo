---
description: "Conduct deep research on development economics topics using multiple AI providers and web sources. Use when the user asks to research a topic, gather evidence for content, find data for a new course/game, or needs substantive background material."
---

# Deep Research Skill

Multi-source research workflow for creating evidence-backed ImpactMojo content.

## When to Use
- Researching a new course topic or game mechanic
- Gathering data for blog posts or Threads content
- Finding recent papers, reports, or case studies
- Cross-validating claims across sources
- Building reading lists or bibliographies

## Research Workflow

### Step 1 — Define the Research Question
Clarify with the user:
- What specific topic or question?
- What type of content will this feed into? (game, course, blog, handout)
- What depth is needed? (quick overview vs. comprehensive review)
- Any specific regions or time periods?

### Step 2 — Multi-Source Search
Use available tools in this priority order:

1. **Web Search** — Current articles, news, recent publications
2. **Grok AI** (`grok-ai` skill) — Cross-validate facts, get alternative perspectives
3. **Gemini AI** (`gemini-ai` skill) — Generate summaries, extract structured data
4. **DeepSeek AI** (`deepseek-ai` skill) — Chain-of-thought reasoning for complex analysis

### Step 3 — Synthesize Findings
Structure research output as:

```markdown
## Research: {Topic}

### Key Findings
- Finding 1 (source)
- Finding 2 (source)

### Data Points
| Metric | Value | Source | Year |
|--------|-------|--------|------|

### Relevant Frameworks
- Framework/theory and how it applies

### South Asian Context
- Region-specific data, case studies, or examples

### Content Opportunities
- How this could become a game mechanic
- Course module suggestions
- Blog post angles

### Sources
1. [Source 1](url) — brief description
2. [Source 2](url) — brief description
```

### Step 4 — Validate
- Cross-check key claims across at least 2 sources
- Flag any conflicting data with both versions
- Note data recency — prefer post-2020 sources
- Identify gaps where more research is needed

## Quality Standards
- Always cite sources with URLs when available
- Distinguish between peer-reviewed research and commentary
- Note sample sizes and methodological limitations
- Prefer World Bank, UNDP, J-PAL, NBER, and regional research institutions
- Flag if data is specific to one country vs. South Asia broadly

## Integration with Other Skills
- Feed findings into `blog-writer` for evidence-backed posts
- Use data points in `threads-writer` for social content
- Inform game design parameters in `add-game`
- Support course outline development

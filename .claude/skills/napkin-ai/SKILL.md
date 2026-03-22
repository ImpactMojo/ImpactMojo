---
name: napkin-ai
description: Napkin.ai API operations — generate visual infographics and diagrams from text using $NAPKIN_API_KEY. Use when the user asks to create visuals, infographics, illustrations for blog posts, or napkin-style diagrams.
---

# Napkin.ai Skill

Use the Napkin.ai API via `$NAPKIN_API_KEY` to generate visual infographics and diagrams from text descriptions.

## Authentication

```
Authorization: Bearer $NAPKIN_API_KEY
```

Base URL: `https://api.napkin.ai/v1`

## Capabilities

### Generate Visual from Text
```bash
curl -s -X POST "https://api.napkin.ai/v1/generate" \
  -H "Authorization: Bearer $NAPKIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Description of the visual you want",
    "style": "infographic"
  }'
```

### Available Styles
- `infographic` — Data-driven visual layouts
- `diagram` — Flowcharts, process diagrams
- `concept` — Concept maps, mind maps
- `comparison` — Side-by-side comparisons
- `timeline` — Chronological visualizations

## ImpactMojo Use Cases
- **Blog illustrations**: Generate 2 napkin.ai visuals per blog post (established pattern)
- **Course diagrams**: Visualize frameworks (Theory of Change, logframes, causal chains)
- **Handout graphics**: Create visual summaries for printable handouts
- **Social media**: Generate shareable infographics for Threads/LinkedIn posts
- **Workshop materials**: Visual aids for facilitation

## Existing Integration

Blog posts use napkin.ai illustrations stored at:
```
blog/images/{post-slug}/napkin-{n}.png
```

Each blog post gets 2 illustrations (established in v10.8.1 — see changelog).

## Best Practices
- Generate 2 visuals per blog post (platform convention)
- Save outputs to `blog/images/{slug}/` directory
- Use `infographic` style for data-heavy content, `diagram` for process flows
- Reference the visual in the blog HTML with proper alt text
- Never commit `$NAPKIN_API_KEY` to the repository

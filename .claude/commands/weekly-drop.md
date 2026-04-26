---
description: "Weekly content drop — research a trending dev-econ topic and produce a full publication brief (blog + threads + visuals + SEO)"
---

# Weekly Drop

Adapted from the "Full Automation via Claude Cowork" playbook (YouTube edition) → ImpactMojo's dev-econ / South Asia education context. Produces one fully-scoped weekly publication brief end-to-end.

`$ARGUMENTS` may optionally specify a topic or sub-niche (e.g. `gender-budgeting`, `climate-finance`, `RWA`). If empty, pick the top trending dev-econ / South Asia policy topic this week.

## Steps

1. **Research the topic** (`deep-research` skill)
   - Identify the top rising development-economics / South Asia / public-policy topic of the past 7 days. Use the topic in `$ARGUMENTS` if provided.
   - Pull the 3 most-cited / most-discussed recent pieces from the past 30 days: papers, working papers, op-eds, policy briefs, major news pieces. Capture authors, dates, source URLs, and 1-line takeaways.
   - Note any ImpactMojo content (course / lab / game / handout / book summary) that already touches the topic — these become cross-link anchors.

2. **Pick a slug + create the drop folder**
   - Slug format: `YYYY-MM-DD-<kebab-topic>` (use today's date)
   - Create `WeeklyDrops/<slug>/` (mkdir -p; folder is gitignored unless promoted — see step 8)

3. **Write `brief.md`** in the drop folder, with these sections:
   - **Topic** + 1-paragraph framing (why it matters for South Asia / dev practitioners now)
   - **Sources** (the 3 pieces, with takeaways)
   - **Angle** (the ImpactMojo POV — what we add that the 3 sources don't)
   - **PAS outline** (Problem → Agitate → Solve), with re-hook beats every ~200 words
   - **Cross-links** (existing ImpactMojo courses / labs / games / handouts / book summaries to anchor)
   - **CTA** (which lab/game/course the reader should try next)

4. **Draft the blog post** (`blog-writer` skill)
   - Save as `blog-draft.html` in the drop folder, following the blog template from `.claude/skills/blog-writer/SKILL.md`
   - PAS structure with re-hooks every ~200 words (the dev-econ analogue of the "every 90 seconds" YouTube rule)
   - Include the napkin illustration `<img>` placeholders inline; actual generation happens in step 6
   - Wire up the cross-links from step 3

5. **Draft the Threads post** (`threads-writer` skill)
   - Save as `threads.md`
   - Long-form, evidence-backed, citing the 3 sources from step 1
   - Replaces the "ElevenLabs narration prompt" slot from the original playbook

6. **Generate napkin.ai illustration prompts** (`napkin-ai` skill)
   - 3–5 prompts mapped scene-by-scene to the blog's section breaks (replaces the "Pexels B-roll list" from the original)
   - Save prompts to `illustrations/prompts.md`
   - Only call the Napkin API if the user confirms — otherwise just leave the prompts ready

7. **SEO + social pack**
   - Save as `seo.md` in the drop folder. Include:
     - SEO `<title>` (≤ 60 chars) + `<meta name="description">` (≤ 155 chars)
     - Open Graph title + description + suggested OG image
     - JSON-LD `Article` schema stub
     - **5 social hook headlines** (replaces the "5 thumbnail concepts" from the original) — for X / LinkedIn / Threads / Bluesky / WhatsApp broadcast

8. **Notify + offer to promote**
   - Print a summary: topic, slug, files written, suggested cross-links, any blockers (missing API key, etc.)
   - Ask the user whether to:
     a. Promote the drop into `Blog/` + update `blog.html` card + search-index (run `housekeeping` after)
     b. Open a GitHub issue tracking the drop for review (use `github-ops` skill)
     c. Leave it in `WeeklyDrops/` for human review

## Scheduling notes (the "Every Monday at 7am" piece)

Claude Code does not natively schedule calendar-based jobs. To run this every Monday at 07:00 local:

```cron
0 7 * * 1 cd ~/ImpactMojo && claude -p "/weekly-drop" >> .claude/logs/weekly-drop.log 2>&1
```

Or invoke manually each Monday. The `loop` skill is interval-based (not calendar-based) and is not the right fit here.

## Guardrails

- Do **not** publish anything to the live site automatically. Everything lands in `WeeklyDrops/` for review.
- Run the `fact-check` skill on the blog draft before promoting.
- Do **not** burn API credits without confirmation: napkin.ai image generation, gamma deck creation, and any paid LLM calls require explicit user approval.
- Backup `index.html` before any promotion step touches it (per `.claude/rules/content-management.md`).

---
description: "Weekly content drop — research a trending dev-econ topic and produce a full publication brief (blog + video + threads + visuals + SEO)"
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

5. **Build the video pack** — full YouTube-ready production brief (the original Cowork video deliverables, retained)
   - Save everything under `video/` in the drop folder.
   - **`video/script.md`** — retention-optimized 8–10 minute script using PAS structure with re-hooks every ~90 seconds. Mark hook beats with `[HOOK]` tags. Add a cold-open under 15 seconds and a single CTA pointing at the matching ImpactMojo lab/game/course.
   - **`video/storyboard.md`** — scene-by-scene breakdown: timecode, on-screen text, visual treatment, and B-roll cue per scene.
   - **`video/narration.md`** — narration prompt(s):
     - **English narration** → ElevenLabs prompt block (voice, stability, similarity, style settings, pacing notes)
     - **Hindi / regional narration** → `sarvam-ai` TTS config (model, speaker, language code, sample rate) for South Asian languages — preferred over ElevenLabs for non-English. Do **not** call Sarvam without user confirmation.
   - **`video/broll.md`** — B-roll list with **Pexels** + **Coverr** search terms per scene (free stock for English/global footage), plus napkin.ai prompts for any custom hand-drawn animation slots that stock footage can't cover.
   - **`video/captions.srt`** — caption stub aligned to the script's section breaks (will need timing pass during edit).
   - **`video/youtube.md`** — YouTube metadata pack:
     - Title (≤ 60 chars, retention-optimized, no clickbait)
     - Description with chapters, source citations, and ImpactMojo cross-links
     - Tags (10–15)
     - Pinned comment draft
     - End-screen CTA spec (which lab / course to link)
   - **`video/thumbnails.md`** — **5 thumbnail concepts** (matches the original Cowork deliverable). Each: composition sketch in words + napkin.ai prompt + headline overlay text (≤ 5 words).
   - **`video/shorts.md`** — 2–3 vertical Shorts/Reels cut-down ideas, 30–60s each, with hook + payoff + CTA.

6. **Draft the Threads post** (`threads-writer` skill)
   - Save as `threads.md`
   - Long-form, evidence-backed, citing the 3 sources from step 1
   - Should reference the video drop where relevant ("full breakdown in the video, link in bio")

7. **Generate napkin.ai illustration prompts** (`napkin-ai` skill)
   - 3–5 prompts mapped scene-by-scene to the blog's section breaks AND the video's storyboard scenes (so blog hero images and video custom slots reuse the same visual language)
   - Save prompts to `illustrations/prompts.md`
   - Only call the Napkin API if the user confirms — otherwise just leave the prompts ready

8. **SEO + social pack**
   - Save as `seo.md` in the drop folder. Include:
     - SEO `<title>` (≤ 60 chars) + `<meta name="description">` (≤ 155 chars)
     - Open Graph title + description + suggested OG image
     - JSON-LD `Article` + `VideoObject` schema stubs (the latter referencing the YouTube upload once published)
     - **5 social hook headlines** for X / LinkedIn / Threads / Bluesky / WhatsApp broadcast — these promote the blog + video as a bundle

9. **Notify + offer to promote**
   - Print a summary: topic, slug, files written, suggested cross-links, any blockers (missing API key, etc.)
   - Ask the user whether to:
     a. Promote the **blog** into `Blog/` + update `blog.html` card + search-index (run `housekeeping` after)
     b. Generate the **video assets** for real (Sarvam/ElevenLabs narration audio, napkin.ai thumbnail PNGs) — paid, requires confirmation
     c. Open a GitHub issue tracking the drop for review (use `github-ops` skill)
     d. Leave everything in `WeeklyDrops/` for human review

## Scheduling notes (the "Every Monday at 7am" piece)

Claude Code does not natively schedule calendar-based jobs. To run this every Monday at 07:00 local:

```cron
0 7 * * 1 cd ~/ImpactMojo && claude -p "/weekly-drop" >> .claude/logs/weekly-drop.log 2>&1
```

Or invoke manually each Monday. The `loop` skill is interval-based (not calendar-based) and is not the right fit here.

## Guardrails

- Do **not** publish anything to the live site or upload anything to YouTube automatically. Everything lands in `WeeklyDrops/` for review.
- Run the `fact-check` skill on **both** the blog draft and the video script before promoting — video is harder to correct after publish.
- Do **not** burn API credits without confirmation: napkin.ai image generation, Sarvam TTS audio, ElevenLabs narration, and gamma deck creation are all paid and require explicit user approval. Default behavior is to leave only prompts/configs ready, not generated assets.
- Prefer `sarvam-ai` over ElevenLabs for Hindi / regional language narration (better South Asian phonetics, project-aligned).
- Backup `index.html` before any promotion step touches it (per `.claude/rules/content-management.md`).
- Video editing happens outside Claude Code. The drop ships a complete brief; final cut is human work in DaVinci / Premiere / CapCut.

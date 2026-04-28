# Napkin.ai illustration prompts — The Heat Floor

5 prompts. Reused across blog hero/inline images AND video custom-animation slots so the visual language stays consistent.

**Style anchors (apply to all):**
- Hand-drawn editorial / napkin style
- ImpactMojo orange (#E87722) + teal (#00857C) accents
- Cream/paper texture background
- No emoji
- No photorealism — all illustrations
- 16:9 for video; 1200×630 for blog hero (square crops for thumbnails)

---

## #1 — Hero: "The Heat Floor"

**Where used:**
- Blog hero image (`/blog/images/2026-04-27/heat-floor-hero.png`)
- Video Scene 22 end card

**Prompt:**

> A hand-drawn editorial illustration. Centre: a factory cross-section with workers at an assembly line, but the roof is a giant glass thermometer with mercury rising into a red zone. Outside the factory: informal labourers under a blazing sun, heat shimmer rising off cracked earth. ImpactMojo orange and teal accents. Cream paper texture background. No people's faces in close detail — silhouettes and gesture only. 16:9 aspect ratio. Editorial newspaper aesthetic, warm but slightly desaturated palette.

---

## #2 — Distribution: "Same temperature. 17× the loss."

**Where used:**
- Blog inline image (after the Nature paper paragraph)
- Video Scene 9

**Prompt:**

> A hand-drawn bar chart, editorial style. Two stacked bars on cream paper texture. Left bar (formal sector) is short, shaded teal, labelled "FORMAL — 1×". Right bar (informal sector) is dramatically taller, shaded gradient red-to-orange, labelled "INFORMAL — 17×". Above the chart, hand-lettered title: "Same temperature. 17× the loss." Below: tiny attribution "Source: Nature, 2025." Subtle thermometer icon in the corner. ImpactMojo brand palette. 16:9.

---

## #3 — Three Redesigns Flowchart

**Where used:**
- Blog inline image (in the SOLVE section)
- Video Scene 15

**Prompt:**

> A hand-drawn editorial flowchart on cream paper. Three connected boxes flowing left to right, each with a hand-drawn icon and a short label. Box 1 (left): an industrial cooling fan icon, label "1. COOLING AS SUBSIDY". Box 2 (centre): a desk-with-laptop icon, label "2. SERVICES TARGETING". Box 3 (right): an umbrella over a worker icon with rupee symbol falling, label "3. HEAT-DAY INSURANCE". Connecting arrows between boxes. ImpactMojo orange for arrows, teal for box outlines. Heading above: "Three redesigns for industrial policy". 16:9.

---

## #4 — Manufacturing Map with Heat Overlay

**Where used:**
- Video Scene 7 (animated version) and Scene 10 (static)

**Prompt:**

> A stylised editorial illustration of the India political map, hand-drawn on cream paper. Landmass in dark teal. Bright orange dots scattered across the map marking manufacturing clusters (concentrated in northern, western, and southern India). A translucent red gradient overlay covering most of the central plains, depicting heat. Subtle hand-lettered annotations: "Manufacturing cluster" with arrow to a dot, "Heat zone" with arrow to red overlay. ImpactMojo brand palette. 16:9. No text titles — let the visual do the work.

---

## #5 — Adaptation is Incomplete

**Where used:**
- Blog inline (after JPE paper paragraph)
- Video Scene 13

**Prompt:**

> A hand-drawn diagnostic chart on cream paper, editorial style. Two vertical bars side-by-side. Bar 1 (left, "WITHOUT COOLING"): tall, fully shaded red, labelled "Heat productivity loss". Bar 2 (right, "WITH FANS + AC"): shorter but still substantial, shaded with red-to-orange gradient — clearly NOT zero. A bold dashed line at the top labelled "Full productivity (unreached)". Hand-lettered caption below: "Adaptation is real. And incomplete." Tiny attribution: "Source: JPE 2021." ImpactMojo orange and teal. 16:9.

---

## Generation queue (when user confirms)

When/if the user approves API generation:

```bash
# Pseudocode — actual call lives in .claude/skills/napkin-ai/SKILL.md
for prompt in 1..5; do
  napkin generate \
    --prompt-file illustrations/prompt-${prompt}.txt \
    --aspect-ratio 16:9 \
    --output illustrations/${prompt}-<slug>.png
done
```

Estimated cost: 5 prompts × ~$0.05 per render = **~$0.25**. Trivial. Still requires explicit user confirmation per `/weekly-drop` guardrails.

## Editor instructions

- These prompts are **first drafts** — refine the napkin output if the first generation misses the brief. Iterate up to 3 times per image; if the 4th attempt still fails, switch to a human illustrator.
- All five images should feel like they're from the same sketchbook. If one feels off-brand vs the others, regenerate the outlier.
- Save final PNGs at:
  - `/blog/images/2026-04-27/<slug>.png` (blog)
  - `/WeeklyDrops/2026-04-27-heat-stressed-industrial-policy/illustrations/<n>-<slug>.png` (drop folder)

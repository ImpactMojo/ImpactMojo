---
name: threads-writer
description: Generate long, evidence-backed Threads posts on development economics topics using Grok. Use when the user asks to write a thread, create Threads content, or draft dev econ posts for social media.
---

# Threads Writer Skill

Generate high-quality, evidence-backed threads on development economics topics for Meta's Threads app, using Grok as the LLM backend.

## When to Use

- User says "write a thread about...", "threads post on...", "draft a thread"
- User wants dev econ content for social media
- User mentions Threads app + any development topic

## Process

### Step 1: Clarify the Topic

Ask the user (if not already clear):
- **Topic**: e.g., "RCTs in development", "cash transfers vs in-kind", "missing women"
- **Angle**: contrarian take, explainer, myth-busting, historical, policy implications
- **Length**: short (5-7 posts), medium (8-12 posts), long (13-20 posts)
- **Tone**: accessible academic, practitioner-friendly, provocative, narrative

Default: medium length, accessible academic tone.

### Step 2: Generate via Grok

Use Grok for its strength in long-form, well-structured reasoning.

```bash
curl -s -X POST "https://api.x.ai/v1/chat/completions" \
  -H "Authorization: Bearer $GROK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-3",
    "messages": [
      {
        "role": "system",
        "content": "You are a development economist writing for Threads (Meta). Write a long, evidence-backed thread on the given topic.\n\nRules:\n- Each post must be under 500 characters (Threads limit)\n- First post must hook the reader — bold claim, surprising stat, or provocative question\n- Every claim must cite a specific study, author, or dataset (e.g., \"Banerjee & Duflo 2011\", \"NFHS-5 data\")\n- Use a mix of: data points, named studies, real-world examples (preferably South Asian), and clear explanations\n- End with a takeaway or call to reflection\n- Number each post (1/, 2/, etc.)\n- No hashtags, no emojis unless specifically requested\n- Write in a voice that is confident, clear, and intellectually honest — acknowledge complexity, don'\''t oversimplify\n- South Asian examples and data preferred where relevant"
      },
      {
        "role": "user",
        "content": "TOPIC_GOES_HERE"
      }
    ],
    "temperature": 0.7,
    "max_tokens": 4096
  }'
```

### Step 3: Format and Review

After generation:
1. **Verify character counts** — each post must be ≤500 characters
2. **Check citations** — flag any vague references ("studies show...") and replace with specific ones
3. **Split long posts** — if any post exceeds 500 chars, break it naturally
4. **Add thread numbering** — `1/`, `2/`, etc.
5. **Present to user** as a numbered list, ready to copy-paste

### Step 4: Output Format

Present the thread as:

```
📋 Thread: [Topic Title]
Posts: [count] | Est. read: [X] min

---

1/
[First post — the hook]

2/
[Second post]

...

[N]/
[Final post — takeaway]

---

Sources cited: [list of papers/datasets referenced]
```

## Thread Styles

| Style | Description | Best for |
|-------|-------------|----------|
| **Explainer** | Break down a concept from first principles | Complex topics (endogeneity, GE effects) |
| **Myth-buster** | Challenge a common belief with evidence | Popular misconceptions (microfinance, aid) |
| **Paper spotlight** | Deep dive into one landmark study | Seminal papers (Kremer 2003, Deaton 2013) |
| **Policy debate** | Present both sides of a live policy question | UBI, conditional transfers, industrial policy |
| **Data story** | Let a dataset tell a story | NFHS, ASER, World Bank indicators |
| **Historical** | Trace how thinking evolved on a topic | From Washington Consensus to SDGs |

## Example Topics

- Why RCTs dominate development research (and why that's a problem)
- Cash transfers: what 20 years of evidence actually says
- The missing women of South Asia — Sen's insight, updated
- Why microcredit didn't end poverty
- NREGA: India's largest employment program, by the numbers
- What the ASER data tells us about India's learning crisis
- Cost-effectiveness in global health: the GiveWell approach
- Industrial policy is back — what changed?

## Best Practices

- **Grok-3 is preferred** over grok-3-mini for thread quality — longer reasoning, better structure
- **Always fact-check citations** — LLMs can hallucinate paper titles and dates
- **South Asian framing** — even global topics should connect to South Asian realities where possible
- **Avoid jargon without explanation** — if you use "endogeneity", explain it in the same post
- **One idea per post** — don't cram two arguments into one post

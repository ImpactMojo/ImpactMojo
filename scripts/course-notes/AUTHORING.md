# Writing the notes for a 101 deck

A 101 notes PDF is the whole deck printed two slides to a page, with notes written for every slide and two
hand-written pages for every section. The notes for one deck live in `content/course-notes/<slug>.json`.
`content/course-notes/brsr-reporting.json` is the model. Read it before you write anything, and match its
depth, voice and shape.

## What the reader is

Someone who paid for notes and expects a good teacher to have sat down with the deck and written beside it.
They can read the slide. They want to know what it means, how to remember it, how to use it, and where
people go wrong. A note that restates the slide has failed. A note should do at least one of these:

- explain why the slide matters, or how to read it
- give a way to remember it (an order, a test, a picture in words)
- warn about a common slip
- tell the reader what to do with it (check this, ask that, work the exercise first)
- connect it to an earlier or later slide

## Sources and facts

The slide text in `build/slides/<slug>.json` is your only source. Do not add a date, number, name, rule, rate,
quotation or citation that is not in that text. You may explain, give an analogy, or work a simple example.
If two slides disagree, or a slide looks wrong, write the note for what the slide says and put the problem in
your final report. Never fix a deck silently and never guess.

Worked examples may use invented numbers, but only formulas, rates and rules that the deck itself gives. Say
"illustrative" in the setup when the figures are invented. Write every calculation in the form
`a × b = c` or `a ÷ b = c` (also `+` and `−`), one calculation per step. The validator recomputes every such
line and fails the file if one is wrong. Round the way the deck rounds.

## File shape

```json
{
  "slug": "brsr-reporting",
  "intro": "25 to 80 words on how to use these notes.",
  "sections": [ { ...one object per section divider, in deck order... } ],
  "notes": { "4": "note text for slide 4", "5": "..." }
}
```

`notes` has one entry for every slide whose `kind` is `content` in the extracted file, and none for `title`,
`section` or `end` slides. Each note is 22 to 62 words (aim for 35 to 50), first or second person, plain
sentences. Wrap one or two key phrases in `**double asterisks**` to get a highlighter mark. That is the only
markup.

One section object per divider slide, in order (`n` runs 1, 2, 3 ...):

```json
{
  "n": 1,
  "title": "the section title as the deck gives it",
  "big_idea": "one sentence, up to 170 characters, with a **highlight**",
  "in_plain_words": ["paragraph of 30 to 110 words", "second paragraph (a third is allowed)"],
  "diagram": { "type": "...", "caption": "optional, up to 90 characters" },
  "key_terms": [ { "term": "up to 28 characters", "meaning": "up to 120 characters" } ],
  "worked_example": { "title": "", "setup": "", "steps": ["3 to 6 steps"], "answer": "" },
  "mistakes": ["3 or 4 mistakes, up to 190 characters each"],
  "recall": [ { "q": "", "a": "" } ]
}
```

`key_terms` has 4 to 6 entries. `recall` has 4 or 5 question and answer pairs, answerable from the deck. The
worked example is required. Where the section has no numbers, work a case: classify, match, order or apply a
test, and show each step.

## Diagrams

Pick the type that shows the section's real structure. Vary the types across a deck. Keep labels short; the
validator enforces the limits.

| type | shape | limits |
|---|---|---|
| `flow` | `nodes: [{label, sub?}]`, drawn left to right, wrapping after 4 | 3 to 6 nodes; label 30, sub 36 characters |
| `cycle` | `nodes: [{label, sub?}]`, `center?` | 3 to 6 nodes; label 26, sub 30 |
| `tree` | `root`, `children: [{label, items?: []}]` | root 40; 2 to 4 children (label 34); up to 4 items (46) |
| `compare` | `left: {title, items}`, `right: {title, items}`, `vs?` | titles 30; 2 to 4 items each (52) |
| `formula` | `parts: [{t, hint?} or {op}]`, `note?` | 3 to 9 parts; t 24, hint 28, note 90 |
| `timeline` | `events: [{when, what}]` | 4 to 7 events; when 24, what 46 |
| `stack` | `levels: [{label, sub?}]`, top first | 3 to 6 levels; label 30, sub 34 |
| `hub` | `center`, `spokes: [{label, sub?}]` | 4 to 6 spokes; label 24, sub 30; center 26 |

Use `formula` for any section built on an equation, `flow` for a procedure, `compare` for two contrasting
ideas, `tree` for a classification, `timeline` for dates, `hub` for one idea with several parts, `cycle`
for a loop, `stack` for levels or layers.

## Voice and the writing rules

Write as a clear, warm teacher speaking to one person ("you"). Concrete beats general. Vary sentence length.
Say a thing once. The owner's rules apply to every string:

- No em dashes, ever. No emoji.
- No negative parallelism in any form: no "not X but Y", "not only", "not just", "X, not Y", "isn't ... it's",
  "less about X than Y", "rather than" as a turn. State the positive claim.
- No filler openers or closers: "it's worth noting", "importantly", "moreover", "in conclusion",
  "ultimately", "at the end of the day", "that said".
- None of these words: delve, utilise, leverage, robust, streamline, harness, foster, underscore, enhance,
  crucial, pivotal, landscape, paradigm, synergy, nuanced, holistic, seamless, multifaceted, notable,
  vibrant, empower, elevate, unlock, resonate, facilitate, genuine, genuinely, honestly, truly, arguably,
  navigate (as metaphor), realm, domain, plethora, myriad, "when it comes to", "shed light on".
- No stacked threes as a habit, no fragments for effect, no slogans, no rhetorical questions that you then
  answer.
- Do not call the reader a learner or student. Do not praise the course.

`python3 scripts/course-notes/lint-notes.py content/course-notes/<slug>.json` checks the banned words and
patterns. A pass is necessary and not enough: read what you wrote.

## Checks to run before you finish

```bash
node scripts/course-notes/validate-notes.mjs <slug>
python3 scripts/course-notes/lint-notes.py content/course-notes/<slug>.json
```

Both must pass. Do not run git, and do not edit any file except your own `content/course-notes/<slug>.json`.

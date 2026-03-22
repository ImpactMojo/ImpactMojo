---
name: dojo-ops
description: Manage dojo practice sessions — add new sessions, update series, modify schedules, and maintain dojos.html. Use when the user asks to add a dojo session, update dojo content, or manage the 56-session practice program.
---

# Dojo Operations Skill

Manage the ImpactMojo Dojos — 56 practice-based skill sessions across 6 series for development practitioners.

## When to Use

- User says "add a dojo session", "update the dojos", "new dojo series"
- User wants to modify session content, schedules, or series structure
- User asks about dojo logistics (pricing, locations, cohort format)

## Dojo Structure

### The 6 Series

| Code | Series | Sessions | Focus |
|------|--------|----------|-------|
| S01 | Thinking Clearly in Development | 8 | Calibrating confidence, cognitive biases, probabilistic thinking |
| S02 | Evidence Reasoning | 9 | Statistical thinking, hypothesis testing, research design, cost-effectiveness |
| S03 | Political Economy & Implementation | 16 | Stakeholder mapping, implementation diagnosis, scaling, adaptive management |
| S04 | Methods That Actually Work | 9 | Field research methodologies, data collection techniques |
| S05 | Epistemic Hygiene | 8 | Intellectual honesty, Fermi estimation, honest writing |
| S06 | Gender, Power & Data | 6 | GESI principles, power analysis, gender-responsive data |

### Session Format
- **Duration**: 90 minutes per session
- **Locations**: Delhi, Bangalore, Online
- **Cost**: ₹1,500 per session, no long-term commitment
- **Cohort size**: Small groups for practice-based learning

## Key File

`dojos.html` — main page listing all 6 series with session details.

## Adding a New Session

1. Open `dojos.html`
2. Find the appropriate series section (e.g., `S01`)
3. Add the session card following the existing HTML pattern in that series
4. Update the session count in the stats bar at the top
5. Update `data/search-index.json` if the session is significant enough to be searchable
6. Update `docs/dojos-guide.md` with the new session details

## Adding a New Series

1. Create a new series section in `dojos.html` following the existing pattern
2. Assign the next series code (e.g., `S07`)
3. Add all sessions within the series
4. Update the stats bar (total sessions count, series count)
5. Update content counts across: `index.html`, `catalog.html`, `docs/platform-overview.md`
6. Add entries to `data/search-index.json`
7. Update `docs/dojos-guide.md`
8. Update `docs/changelog.md`

## Content Guidelines

- Sessions should be **practice-based** — participants do, not just listen
- Each session needs a clear **skill outcome** (what can you do after this?)
- Use South Asian development context for examples and case studies
- Frame around **practitioner challenges**, not academic theory
- Session titles should be action-oriented (e.g., "Calibrating Your Confidence" not "Confidence Calibration Theory")

## Cross-Reference Updates

When modifying dojos, check these files:
- `dojos.html` — main page
- `index.html` — dojo mention in hero/features section
- `docs/dojos-guide.md` — documentation
- `data/search-index.json` — search entries
- `docs/changelog.md` — if user-facing change

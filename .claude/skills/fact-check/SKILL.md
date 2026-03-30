---
name: fact-check
description: Fact-check content across the ImpactMojo platform — blog posts, courses, labs, games, and book summaries. Use when the user says "fact check", "check facts", "verify content", "review for errors", or on a regular content audit schedule.
---

# Fact-Check Content Audit

Systematically review ImpactMojo content for factual accuracy. Run this regularly (monthly recommended) or before major launches.

## Scope

Review content in this priority order:

1. **Blog posts** (`blog/*.html`) — highest risk, public-facing thought leadership
2. **Flagship courses** (`courses/*/index.html`, `courses/*/lexicon.html`) — educational content must be accurate
3. **101 courses** (`101-courses/*.html`) — foundational course decks
4. **Book summaries** (`BookSummaries/*-companion.html`) — attributed claims and citations
5. **Labs** (`Labs/*-lab.html`) — methodology descriptions and worked examples
6. **Games** (`Games/*.html`) — scenario text and factual framing

## Steps

1. **Gather content files**
   ```bash
   echo "=== Content inventory ==="
   echo "Blog posts: $(ls blog/*.html 2>/dev/null | wc -l)"
   echo "Flagship courses: $(ls courses/*/index.html 2>/dev/null | wc -l)"
   echo "Lexicons: $(ls courses/*/lexicon.html courses/*/media-lexicon.html 2>/dev/null | wc -l)"
   echo "101 courses: $(ls 101-courses/*.html 2>/dev/null | wc -l)"
   echo "Book summaries: $(ls BookSummaries/*-companion.html 2>/dev/null | wc -l)"
   echo "Labs: $(ls Labs/*-lab.html 2>/dev/null | wc -l)"
   echo "Games: $(ls Games/*.html 2>/dev/null | wc -l)"
   ```

2. **Check for known recurring errors**
   Run these automated checks first to catch common issues:
   ```bash
   # Research Rundown should be "bimonthly", not "weekly"
   grep -rn "Research Rundown.*weekly\|weekly.*Research Rundown" blog/ courses/ --include="*.html"

   # Logframe origin — should NOT say USAID "developed" or "created" the logframe
   # (USAID formalised it; it originated from defense sector systems analysis)
   grep -rn "developed by USAID\|created by USAID\|USAID developed\|USAID created" blog/ courses/ --include="*.html" | grep -i logframe

   # Psychological safety — should NOT say "coined by" Edmondson
   # (Schein & Bennis originated it 1965; Edmondson popularised it)
   grep -rn "coined by.*Edmondson\|Edmondson.*coined" blog/ courses/ --include="*.html"

   # Benjamin Franklin "Tell me and I forget" — disputed attribution
   grep -rn "Benjamin Franklin" blog/ courses/ --include="*.html"

   # MIT OCW — should not imply thousands of courses were available in 2001
   grep -rn "OpenCourseWare.*2001.*thousands\|2001.*OpenCourseWare.*thousands" blog/ courses/ --include="*.html"
   ```

3. **Review content by category**
   For each content type, use parallel subagents to read article content (skip CSS/JS boilerplate) and flag:

   **Hard errors (must fix):**
   - Wrong dates (treaty signed, policy enacted, organisation founded)
   - Wrong attributions (quote or concept credited to wrong person)
   - Wrong statistics (population figures, percentages, counts)
   - Wrong organisation/policy names
   - Wrong methodology descriptions (formulas, definitions)
   - Outdated facts presented as current (e.g., stale population counts)

   **Soft issues (flag for review):**
   - Unverifiable quotes attributed to specific people
   - Approximate statistics without source caveats
   - Simplifications that could mislead (e.g., "X invented Y" when X popularised Y)
   - Outdated but technically-not-wrong figures ("over 400 million" when real number is 600 million)

4. **Cross-check internal consistency**
   ```bash
   # Check that the same fact isn't stated differently in different places
   # Example: OECD DAC criteria dates
   grep -rn "OECD DAC.*199[0-9]\|DAC criteria.*199[0-9]" blog/ courses/ --include="*.html"

   # Example: Sphere Standards dates
   grep -rn "Sphere.*20[0-9][0-9]\|Sphere Standards.*first" blog/ courses/ --include="*.html"

   # Example: Paris Declaration date
   grep -rn "Paris Declaration.*20[0-9][0-9]" blog/ courses/ --include="*.html"
   ```

5. **Fix errors**
   - Fix all hard errors immediately
   - For soft issues, add appropriate hedging language ("widely attributed to", "approximately", "as of [year]")
   - Document what was changed and why

6. **Cross-link audit**
   While reviewing, also check:
   - Blog posts should have 4-7 in-text cross-links to sibling posts and ImpactMojo labs/tools
   - Course pages should link to relevant blog posts, labs, and games
   - First mention only, relative paths, no self-links

7. **Update known-errors registry**
   After fixing, add new patterns to the automated checks in Step 2 above so they're caught in future runs. Edit this skill file to add new `grep` patterns.

8. **Commit and report**
   ```bash
   git add -A
   git commit -m "Fact-check audit: fix [N] errors across [content types]"
   git push
   ```
   Report to user:
   - Number of hard errors found and fixed
   - Number of soft issues flagged
   - Files modified
   - Any items needing human judgment

## Known Correct Facts (Reference)

Keep this section updated as a quick-reference for frequently checked claims:

| Claim | Correct Fact | Source |
|-------|-------------|--------|
| Logframe origin | Defense sector systems analysis (PPBS); formalised by USAID via Practical Concepts Inc., 1969 | Rosenberg (1969) |
| OECD DAC evaluation criteria | First published 1991; updated 2019 (added coherence) | OECD |
| Sphere Standards | First edition 2000 | Sphere Association |
| Paris Declaration | 2005 | OECD |
| Accra Agenda for Action | 2008 | OECD |
| HAP established | 2003 | HAP International |
| Psychological safety | Schein & Bennis (1965); popularised by Edmondson (1999) | Administrative Science Quarterly |
| "Tell me and I forget..." | Disputed — often misattributed to Franklin/Confucius; cf. Xunzi | Quote Investigator |
| MIT OCW | Announced 2001, pilot launched 2002 (~50 courses), grew to 2,400+ | MIT OCW |
| Research Rundown frequency | Bimonthly (once every two months) | Internal |
| Nepal local governments | 753 local levels per 2015 constitution | Constitution of Nepal |
| India scheduled languages | 22 (Eighth Schedule) | Constitution of India |
| Cohen's d conventions | 0.2 small, 0.5 medium, 0.8 large | Cohen (1988) |
| Belmont Report principles | Respect for persons, beneficence, justice (1979) | HHS |
| UNESCO OER Recommendation | Adopted November 2019 | UNESCO |

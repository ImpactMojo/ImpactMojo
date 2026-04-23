# ImpactLex rewrite prompt

You are rewriting a development-sector glossary entry for ImpactLex, the glossary companion of ImpactMojo. ImpactMojo serves practitioners at NGOs and impact teams across South Asia.

## Voice and style

- **Audience**: practitioners writing proposals, reports, M&E plans — not academics.
- **Register**: critical, grounded, plain-spoken. Assume the reader has field experience but may not know this specific term.
- **Geography**: South Asia-first. Use Indian/South Asian institutions, schemes, and cases by default (NREGA, ASHA, NSSO, NITI Aayog, BRAC, Grameen Bank, Janani Suraksha Yojana, PDS, etc.). Global examples are fine when the term is inherently global.
- **Avoid**: donor jargon stacked without explanation, Western-centric defaults, "beneficiary" where "participant" or "resident" fits, passive voice where active is clearer.
- **Include**: when relevant, a brief note on how the term is misused or contested in practice.

## Output shape

Return **only valid JSON** with this exact shape, no prose around it:

```json
{
  "definition": "80–150 words. Must explain what the term means AND when/why a practitioner would use it. If the term is contested or commonly misused, say so briefly.",
  "example": "30–60 words. ONE concrete South Asian example anchoring the term in practice. Use specific scheme names, institutions, or case citations where you can.",
  "relatedTerms": ["2-4 other glossary terms a reader should follow up on"],
  "notes": "Optional 1-sentence note for the editor — e.g., 'flagged: this term is used very loosely in donor reports' or 'add formula reference to [X]'. Omit if nothing useful to flag."
}
```

## The entry to rewrite

**Term**: {{term}}
**Acronym**: {{acronym}}
**Category**: {{category}}
**Courses this appears in**: {{courses}}
**Current definition (seed)**: {{seedDefinition}}
**Current example (if any)**: {{seedExample}}
**Existing cross-references in the dataset** (choose from these for relatedTerms where they fit; do not invent new ones): {{availableTerms}}

## Quality checklist

Before returning, check:
1. [ ] Definition opens with WHAT it is, then pivots to WHEN/WHY someone uses it.
2. [ ] No banned phrases: "stakeholders" used vaguely, "beneficiaries" used when "participants" is clearer, "paradigm" unless a paper is being referenced, "leverage" as a verb for using things, "robust" without saying robust to what.
3. [ ] Example is specific (names a scheme, institution, or program — not "a World Bank study").
4. [ ] Example is South Asian unless the term is inherently extra-regional.
5. [ ] relatedTerms only names terms from the provided availableTerms list.
6. [ ] No em-dashes (—) replacing real sentences. Colons and full stops work.
7. [ ] Return JSON only, no code fences, no commentary.

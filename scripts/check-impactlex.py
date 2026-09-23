#!/usr/bin/env python3
"""ImpactLex: the glossary says how each entry was written, and the offline
snapshot does not go quietly stale.

Two failures this guards, both invisible on the page before 2026-09-23.

**An entry nobody has reviewed looked exactly like one an editor had.**
`app.js` renders every term that is not `rejected`, which is right — a term
people search for should be findable — but `status` never reached the reader.
159 of 494 entries are still `seed`, 226 were first drafted by a language
model, and 460 carry no citation at all. All three rendered identically to a
reviewed, hand-written, cited entry. For a glossary a practitioner quotes from,
that is the whole ballgame. `provenanceOf()` now states all three on every
term, and the Sources block is never hidden, because an absent citation is
information rather than a reason to omit the heading.

**The snapshot is what every visitor sees first.** `app.js` renders it
immediately and only then swaps in InstantDB, so a stale snapshot is the first
paint for everyone on every load, not merely an offline fallback. It cannot be
regenerated without `INSTANTDB_ADMIN_TOKEN`, which is exactly why its age needs
to be visible rather than remembered.

    python3 scripts/check-impactlex.py
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(ROOT, "impactlex", "data", "seed-snapshot.json")
APP = os.path.join(ROOT, "impactlex", "app.js")
INDEX = os.path.join(ROOT, "impactlex", "index.html")

# The snapshot is regenerated from the live database, which needs a token this
# repository does not hold. Six months is generous; it is here so the drift
# reports itself instead of being discovered by a reader.
MAX_AGE_DAYS = 180

failures = []


def check(name, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


def main():
    with open(SNAP, encoding="utf-8") as f:
        snap = json.load(f)
    terms = snap.get("terms", [])
    app = open(APP, encoding="utf-8").read()
    index = open(INDEX, encoding="utf-8").read()

    check("the snapshot's own count matches the terms in it",
          snap.get("count") == len(terms),
          f"count={snap.get('count')} terms={len(terms)}")

    generated = snap.get("generatedAt")
    age = None
    if generated:
        when = datetime.fromisoformat(generated.replace("Z", "+00:00"))
        age = (datetime.now(timezone.utc) - when).days
    check("the offline snapshot is not stale",
          age is not None and age <= MAX_AGE_DAYS,
          f"generated {generated}, {age} days ago (limit {MAX_AGE_DAYS}); "
          "regenerate with INSTANTDB_ADMIN_TOKEN set"
          if age is not None else "no generatedAt in the snapshot")

    # Provenance has to be read off the record, not inferred, so the fields it
    # reads must still be there. `aiProvider` is deliberately not in this list:
    # it is set only on entries a model drafted, and its absence is the signal
    # that a person wrote the entry. Requiring it on every term would be
    # requiring the record to lie.
    for field in ("status", "sources"):
        present = sum(1 for t in terms if field in t)
        check(f"every term carries `{field}`", present == len(terms),
              f"{present} of {len(terms)}")

    # `provenanceOf()` reads `aiProvider` for truthiness, so a typo in it does
    # not error anywhere: the entry simply changes its account of how it was
    # written. Pin the vocabulary.
    KNOWN_PROVIDERS = {"groq", "gemini"}
    bad = sorted({t["aiProvider"] for t in terms
                  if t.get("aiProvider") and t["aiProvider"] not in KNOWN_PROVIDERS})
    check("`aiProvider`, where set, is a provider we know",
          not bad, ", ".join(bad) if bad else f"{sorted(KNOWN_PROVIDERS)}")

    # An entry drafted by a model but never reviewed is the one combination a
    # reader most needs told, so the filter that surfaces it has to exist.
    check("the unreviewed filter is offered",
          "unreviewed" in app and "'Not yet reviewed'" in app)

    check("the reader is told which entries are reviewed",
          "provenanceOf" in app and "modal-provenance" in app and 'id="modal-provenance"' in index)

    # Both halves matter, and the markup half alone would pass while the page
    # kept hiding the block at runtime. The `hidden` attribute in index.html
    # was only the initial state; app.js set it on every open, to false when a
    # term had sources and true when it did not.
    # Capture the value rather than use a negative lookahead: `\s*` backtracks
    # to zero width, so `=\s*(?!false)` happily matches at the space before
    # `false` and reports a failure on correct code. Caught by running it.
    assigns = re.findall(r"\$\('modal-sources-section'\)\.hidden\s*=\s*([^;]+);", app)
    hides_at_runtime = [a.strip() for a in assigns if a.strip() != "false"]
    check("the Sources block is never hidden",
          "No source recorded for this entry." in app
          and re.search(r'id="modal-sources-section"(?![^>]*\bhidden\b)', index) is not None
          and not hides_at_runtime,
          "an absent citation is information; omitting the heading hides it")

    check("the provenance filter exists and is wired",
          'id="provenance-filters"' in index and "PROVENANCE_FILTERS" in app)

    # Rejected entries must stay invisible. That was true before and is the one
    # status the reader should not be offered.
    check("rejected entries are still filtered out",
          app.count("t.status !== 'rejected'") >= 2,
          "both the snapshot path and the InstantDB path")

    counts = {}
    for t in terms:
        counts[t.get("status")] = counts.get(t.get("status"), 0) + 1
    ai = sum(1 for t in terms if t.get("aiProvider"))
    sourced = sum(1 for t in terms if t.get("sources"))
    print(f"\n  {len(terms)} terms — " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) +
          f"; {ai} model-drafted; {sourced} with a citation")

    print("\nPASS - all checks passed" if not failures
          else f"\nFAIL - {len(failures)} check(s) failed: " + ", ".join(failures))
    sys.exit(1 if failures else 0)


main()

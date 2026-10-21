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

**The snapshot is the glossary, and there is nothing behind it.** Until
2026-10-21 `app.js` rendered the snapshot and then swapped in a copy held in
InstantDB, which was an older import: 385 terms against the snapshot's 494, 75
published against 335, and 154 shorter definitions. Visitors saw the older copy.
InstantDB is shutting down on 2026-08-31 2027, so the live copy is gone from
the code and the snapshot is the only source. This check holds it there: a
second source that nobody compares is how the two came apart.

    python3 scripts/check-impactlex.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(ROOT, "impactlex", "data", "seed-snapshot.json")
APP = os.path.join(ROOT, "impactlex", "app.js")
INDEX = os.path.join(ROOT, "impactlex", "index.html")

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

    # No second source for the glossary. The InstantDB client, its app id and
    # its admin scripts are gone; a copy that is edited somewhere else is the
    # drift this repository had.
    config = open(os.path.join(ROOT, "impactlex", "config.js"), encoding="utf-8").read()
    check("the glossary has one source: the snapshot",
          "instantdb" not in app.lower() and "instantdb" not in config.lower()
          and "esm.sh" not in app,
          "app.js and config.js name no live database")

    # Contributions are the one thing that needs a database. They go to a
    # Supabase table that anyone can insert into and only an admin can read.
    check("contributions go to Supabase",
          "impactlex_contributions" in app and "supabaseUrl" in config)

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
          app.count("t.status !== 'rejected'") >= 1,
          "the snapshot path")

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

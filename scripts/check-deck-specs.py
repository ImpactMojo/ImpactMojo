#!/usr/bin/env python3
"""Fail when a deck spec would overwrite its live deck with something else.

Why this exists
---------------
`scripts/deck-builder/build.py <spec>` writes 101-courses/<slug>.html from a
Python spec, overwriting whatever is there. Many decks were then edited as
HTML -- fact-check corrections, expanded slides, new sources -- and the spec
was never told. On 2026-10-07, 47 of 66 specs built a deck that differed from
the live one on up to 91 slides. Nothing said so: `build.py --check` counts
slides and nothing else, so a well-meant rebuild would have restored every
error the fact-check removed, and the diff would have read as a routine build.

Three of those specs did not even parse (an earlier link rewrite had put
double-quoted attributes inside double-quoted Python strings), which is how the
drift came to light.

So every spec must be in one of two states:

  in sync   the spec builds the live deck byte for byte
  frozen    listed in scripts/deck-builder/frozen.json with a reason; build.py
            then refuses to write it without --force

A frozen spec that has been brought back into sync fails too, so the list
cannot outlive its reason. Run with --list to print each spec's state and the
number of slides that differ.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "scripts" / "deck-builder" / "build.py"
SPECS = ROOT / "scripts" / "deck-builder" / "specs"
FROZEN = ROOT / "scripts" / "deck-builder" / "frozen.json"
# Not a deck: a fixture for the builder itself.
SKIP = {"_smoketest"}


def load_builder():
    spec = importlib.util.spec_from_file_location("deck_build", BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def slides(text):
    body = text.split('<div class="slide-viewport" id="viewport">', 1)[1]
    body = body.split("</div><!-- /slide-viewport -->", 1)[0]
    return re.split(r'(?=<div class="slide[ "])', body)


def main():
    builder = load_builder()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8")) if FROZEN.exists() else {}
    names = sorted(p.stem for p in SPECS.glob("*.py") if p.stem not in SKIP)
    problems, rows = [], []

    for name in names:
        try:
            out, _ = builder.build(name)
            slug = builder.load_spec(name)["slug"]
        except Exception as e:  # a spec that does not run is the worst state
            problems.append(f"{name}: does not build ({type(e).__name__}: {e})")
            continue
        live_path = ROOT / "101-courses" / f"{slug}.html"
        if not live_path.exists():
            problems.append(f"{name}: builds {live_path.name}, which does not exist")
            continue
        live = live_path.read_text(encoding="utf-8")
        a, b = slides(live), slides(out)
        differ = sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b))
        same = live == out
        rows.append((name, slug, "in sync" if same else f"{differ} slides differ"
                     if differ else "head or scripts differ", name in frozen))
        if same and name in frozen:
            problems.append(f"{name}: frozen, but it builds the live deck exactly; "
                            f"remove it from frozen.json")
        elif not same and name not in frozen:
            what = f"{differ} slide(s)" if differ else "the <head> or scripts"
            problems.append(f"{name}: building it would change {what} of "
                            f"101-courses/{slug}.html. Port the live edits into the "
                            f"spec, or freeze it in frozen.json with a reason")

    for name in frozen:
        if name not in names:
            problems.append(f"{name}: frozen, but no such spec")

    if "--list" in sys.argv:
        for name, slug, state, fz in rows:
            print(f"{name:30} {slug:30} {state:24} {'frozen' if fz else ''}")

    if problems:
        print(f"FAIL - {len(problems)} deck spec problem(s):")
        for p in problems:
            print(f"  {p}")
        sys.exit(1)
    synced = sum(1 for r in rows if r[2] == "in sync")
    print(f"PASS - {synced} specs build their live deck exactly; "
          f"{len(frozen)} frozen with a reason")


if __name__ == "__main__":
    main()

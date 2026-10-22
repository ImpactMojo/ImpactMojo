#!/usr/bin/env python3
"""Run the owner's writing rules over every string in an authored notes file.

    python3 scripts/course-notes/lint-notes.py content/course-notes/<slug>.json [...]

The rules are the ones the Evaluator's Desk templates are held to (scripts/evaluator-pack/build.py):
no em dashes, no negative parallelism, none of the banned words and phrases. Exits 1 on a hit.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "evaluator-pack"))
from build import lint  # noqa: E402


def strings(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from strings(v, f"{path}/{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from strings(v, f"{path}/{i}")


def main(files):
    hits = 0
    for f in files:
        doc = json.load(open(f, encoding="utf-8"))
        for path, s in strings(doc):
            if path == "/slug":  # an identifier, not prose
                continue
            for _, rule, ctx in lint(Path(f).name, [s]):
                print(f"{Path(f).name}{path}: {rule} | {ctx}")
                hits += 1
    print(f"{hits} lint hit(s) in {len(files)} file(s)")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

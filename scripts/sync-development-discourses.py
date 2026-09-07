#!/usr/bin/env python3
"""Refresh data/development-discourses.json from the Development Discourses repo.

Why this exists
---------------
The Theories of Development pages link into Development Discourses
(Varnasr/development-discourses), a separate repository holding 645 open-access
resources. A link into another repo is the kind of cross-reference that rots
silently: the target is renamed or dropped, the link 404s, and nothing here
notices because nothing here can see that repo.

So the ids a theory points at are mirrored into a small committed snapshot, and
scripts/build-theories.py refuses to build on an id that is not in it. This
script is what refreshes the snapshot against the real library, and it refuses
to write if an id a theory still references has disappeared, which is the case
worth catching: silently dropping the entry would leave the theory page with one
fewer reading and no error anywhere.

It also keeps titles, authors and years current, since those are rendered here
and edited there.

Usage:
    python3 scripts/sync-development-discourses.py --repo ../development-discourses
    python3 scripts/sync-development-discourses.py --repo ../development-discourses --check
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "data" / "development-discourses.json"
THEORIES = ROOT / "data" / "theories"
FIELDS = ("title", "authors", "year", "topic")


def referenced_ids():
    ids = set()
    for path in sorted(THEORIES.glob("*.json")):
        if path.name == "_meta.json":
            continue
        ids.update(json.loads(path.read_text(encoding="utf-8")).get("discourses", []))
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True,
                    help="path to a checkout of Varnasr/development-discourses")
    ap.add_argument("--check", action="store_true",
                    help="report drift without writing")
    args = ap.parse_args()

    source = Path(args.repo).expanduser().resolve() / "data" / "resources.json"
    if not source.is_file():
        print(f"FAIL - no resources.json at {source}")
        return 1

    library = {r["id"]: r for r in json.loads(source.read_text(encoding="utf-8"))}
    wanted = referenced_ids()

    gone = sorted(i for i in wanted if i not in library)
    if gone:
        print(f"FAIL - {len(gone)} referenced resource(s) are no longer in "
              f"{args.repo}. Point the theory at something that exists, or "
              f"remove the reference; do not let the snapshot quietly drop it:")
        for i in gone:
            for path in sorted(THEORIES.glob("*.json")):
                if path.name != "_meta.json" and i in json.loads(
                        path.read_text(encoding="utf-8")).get("discourses", []):
                    print(f"    {i}  (referenced by {path.name})")
        return 1

    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    snapshot["entries"] = {
        i: {f: library[i][f] for f in FIELDS} for i in sorted(wanted)
    }
    text = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        if SNAPSHOT.read_text(encoding="utf-8") != text:
            print("FAIL - data/development-discourses.json has drifted from the "
                  "source library. Re-run without --check.")
            return 1
        print(f"PASS - {len(wanted)} referenced resource(s) match the source library.")
        return 0

    SNAPSHOT.write_text(text, encoding="utf-8")
    print(f"PASS - snapshot refreshed: {len(wanted)} resource(s) from {args.repo}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

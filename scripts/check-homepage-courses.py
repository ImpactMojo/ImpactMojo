#!/usr/bin/env python3
"""Guard: every flagship course must appear on the homepage.

Why this exists
---------------
Adding a flagship updates `data/counts.json`, `catalog.html`, `courses/index.html`,
`sitemap.xml`, `data/search-index.json`, `js/offline.js`, `service-worker.js`,
`js/course-progress.js` and the Supabase certificate map. Nothing updates
`index.html`, and until this guard nothing checked it.

So on 2026-09-08 three of the twenty-one flagships had **zero** references on the
front page of the site -- `esg` (shipped 2026-08-21), `social-movements` (older),
and `gender-mel` (shipped that morning) -- while every other course had two to
five (#1085). Not a regression anyone introduced: a slow drift that nobody was
positioned to notice, because the homepage is the one file the add-a-course
checklist never names.

Two structures inside index.html carry the course list, and they fail differently.

1. The JSON-LD `ItemList` named "Flagship Courses" is what search engines read.
   It declared `"numberOfItems": 18` while listing 17 items, so it was wrong
   against itself before it was wrong against the library. `check-counts.py`
   cannot see this: it matches prose and stat tiles, and `numberOfItems` is a
   JSON-LD attribute in neither shape.

2. The resume map (slug -> [title, url]) drives the "continue where you left off"
   card. A course missing from it has its progress stored in localStorage and no
   way to surface it: the lookup misses, the card does not render, and nothing
   errors. The feature is simply absent for that course.

What it checks
--------------
* Every directory under `courses/` appears in the JSON-LD ItemList.
* Every directory under `courses/` appears in the resume map.
* `numberOfItems` equals the number of items actually listed.

Deliberate exemptions live in EXEMPT with a written reason, and a stale exemption
fails too -- an exempted course that later gets listed is reported, so the list
cannot rot into a blindfold. Same contract as check-search-coverage.py.

Run: python3 scripts/check-homepage-courses.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = ROOT / "index.html"
COURSES = ROOT / "courses"

# slug -> why it is legitimately absent from the homepage course list
EXEMPT: dict[str, str] = {}


def course_slugs() -> set[str]:
    return {p.name for p in COURSES.iterdir() if p.is_dir()}


def jsonld_block(text: str) -> str:
    i = text.find('"name": "Flagship Courses"')
    if i == -1:
        sys.exit('FAIL - no JSON-LD ItemList named "Flagship Courses" in index.html')
    end = text.find("]\n    }", i)
    return text[i:end]


def resume_block(text: str) -> str:
    # The map opens on the `mel:` entry and closes at the first `};`.
    i = text.find("mel: ['")
    if i == -1:
        sys.exit("FAIL - no resume course map in index.html")
    return text[i:text.find("};", i)]


def main() -> int:
    text = HOME.read_text(encoding="utf-8")
    slugs = course_slugs()

    ld = jsonld_block(text)
    listed = set(re.findall(r"impactmojo\.in/courses/([^/\"]+)", ld))
    declared = re.search(r'"numberOfItems":\s*(\d+)', ld)
    actual = len(re.findall(r'"position":', ld))

    resume = resume_block(text)
    mapped = set(re.findall(r"/courses/([^/']+)", resume))

    problems = []

    if declared and int(declared.group(1)) != actual:
        problems.append(
            f'JSON-LD says "numberOfItems": {declared.group(1)} but lists {actual} items'
        )

    for slug in sorted(slugs - listed - set(EXEMPT)):
        problems.append(f"{slug}: missing from the JSON-LD flagship ItemList")
    for slug in sorted(slugs - mapped - set(EXEMPT)):
        problems.append(f"{slug}: missing from the resume course map")

    for slug, reason in sorted(EXEMPT.items()):
        if slug not in slugs:
            problems.append(f"{slug}: exempted ({reason}) but no such course directory")
        elif slug in listed and slug in mapped:
            problems.append(f"{slug}: exempted ({reason}) but now listed - drop the exemption")

    if problems:
        print("FAIL - the homepage does not list every flagship course:\n")
        for p in problems:
            print(f"  {p}")
        print(
            "\nEvery directory under courses/ must appear in index.html's JSON-LD"
            '\n"Flagship Courses" ItemList and in the resume map that drives the'
            '\n"continue where you left off" card. See #1085.'
        )
        return 1

    print(
        f"PASS - all {len(slugs)} flagship courses appear on the homepage "
        f"({actual} in the ItemList, {len(EXEMPT)} exempted on purpose)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

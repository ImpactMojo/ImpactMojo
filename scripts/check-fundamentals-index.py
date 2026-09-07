#!/usr/bin/env python3
"""Guard: the Fundamentals landing page must count and link what actually ships.

Why this exists
---------------
The landing page said "Four so far" while listing five cards, for as long as the
fifth framework had been live. Nothing caught it: the number is prose on a page
under fundamentals/, and check-counts.py deliberately scans only root-level
pages for platform totals. It was found by a person reading the page.

That is the class of bug worth a guard — a number stated in one place and the
thing it counts maintained in another. This checks three of them:

  * the "N so far" heading matches the number of framework cards listed
  * every fundamentals/*.html page except the index is linked from the index
  * every card links to a file that exists

And one more, added after #1064. The two cards that point at the library from
*outside* it -- on index.html and libraries.html -- had gone on describing four
frameworks and "171 statistics" long after there were eight, and the homepage
card still said "Open the wheel". Neither was covered by anything: this script
deliberately stopped at the library's own directory, and check-counts.py reads
data/counts.json, which has no Fundamentals entry.

The rule those two cards now follow is that they must not state a count at all.
A number in a card is a second place to maintain, and the first thing that goes
stale when a framework is added. So this refuses any digit or number-word used
to count frameworks in those descriptions, and checks each card still links to
the library rather than into one page of it.

Run: python3 scripts/check-fundamentals-index.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "fundamentals" / "index.html"

# Cards elsewhere on the site that point at the library (#1064).
ENTRY_POINTS = ["index.html", "libraries.html"]

# A number immediately in front of one of these nouns is a count of the library,
# which is what must not be hardcoded outside it. "Fundamentals" on its own, or a
# number that belongs to something else in the same card, is left alone.
COUNTED_NOUNS = r"(?:clickable\s+)?(?:maps?|frameworks?|diagrams?|statistics|" \
                r"statutes|judgments|positions)"
NUMBER = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)"

WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}


def check_entry_points():
    """The cards linking in from elsewhere must not carry a count (#1064)."""
    found = []
    for name in ENTRY_POINTS:
        page = ROOT / name
        if not page.exists():
            found.append(f"{name} is missing, so its Fundamentals card cannot be checked")
            continue
        src = page.read_text(encoding="utf-8")
        # The card is the anchor to /fundamentals/ plus the description inside it.
        cards = re.findall(r'<a[^>]+href="/fundamentals/"[^>]*>(.{0,900}?)</a>', src, re.S)
        if not cards:
            found.append(f"{name} has no card linking to /fundamentals/ "
                         f"(a link into one framework page is not the library)")
            continue
        for card in cards:
            text = re.sub(r"<[^>]+>", " ", card)
            text = text.replace("&mdash;", " ").replace("&rsquo;", "'").replace("&amp;", "&")
            hit = re.search(NUMBER + r"\s+" + COUNTED_NOUNS, text, re.I)
            if hit:
                found.append(f'{name}: the Fundamentals card states a count, "{hit.group(0)}". '
                             f"A count outside the library goes stale the next time a framework "
                             f"is added (#1064); describe it without one.")
    return found


def main() -> int:
    if not INDEX.exists():
        print(f"FAIL - {INDEX} is missing.")
        return 1
    src = INDEX.read_text(encoding="utf-8")
    problems = []

    cards = re.findall(r'<div class="credit-card">\s*<h3><a href="(/fundamentals/[^"]+)"', src)
    n_cards = len(cards)

    m = re.search(r"<h2>\s*(\w+)\s+so far\s*</h2>", src, re.I)
    if not m:
        problems.append('no "<N> so far" heading found — has the section been renamed?')
    else:
        word = m.group(1).lower()
        stated = WORDS.get(word, int(word) if word.isdigit() else None)
        if stated is None:
            problems.append(f'heading count "{m.group(1)}" is not a number this check knows')
        elif stated != n_cards:
            problems.append(f'the heading says "{m.group(1)}" ({stated}) '
                            f"but {n_cards} framework cards are listed")

    for href in cards:
        if not (ROOT / href.lstrip("/")).exists():
            problems.append(f"card links to {href}, which does not exist")

    shipped = sorted(p.name for p in (ROOT / "fundamentals").glob("*.html")
                     if p.name != "index.html")
    linked = {Path(h).name for h in cards}
    for name in shipped:
        if name not in linked:
            problems.append(f"fundamentals/{name} ships but the index does not link it")

    problems += check_entry_points()

    if problems:
        print("FAIL - the Fundamentals index does not describe what ships.\n")
        for p in problems:
            print(f"    {p}")
        return 1

    print(f"PASS - the Fundamentals index counts, links and resolves all "
          f"{n_cards} frameworks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

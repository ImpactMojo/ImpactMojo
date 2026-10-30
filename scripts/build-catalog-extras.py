#!/usr/bin/env python3
"""Write the generated part of the catalogue from site search.

catalog.html says it lists everything on the site, and on 2026-10-29 it did
not: no Practice Packs, no case challenges, no Data Notes, no theories, no
Fundamentals pages, no Code School courses, seven reading companions short and
seven Specials short. Each of those had been added to data/search-index.json,
which every new page must reach (check-search-coverage.py), and the hand-kept
list in catalog.html was simply never told.

So the kinds below are read from the search index. The script writes them
between the `catalog:generated` markers inside `allContent`, skipping any
address the hand-written entries already cover, so a hand-written entry with a
better description always wins.

    python3 scripts/build-catalog-extras.py          # rewrite the block
    python3 scripts/build-catalog-extras.py --check  # fail if it is stale
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "catalog.html"
START = "    // catalog:generated:start (scripts/build-catalog-extras.py; do not edit by hand)\n"
END = "    // catalog:generated:end\n"

# search-index type -> catalogue type. A search type may need a filter on the address.
KINDS = [
    ("practice-pack", "practice-pack", lambda u: u.startswith("/practice-packs/") and u != "/practice-packs/"),
    ("challenge", "challenge", lambda u: u.startswith("/challenges.html#")),
    ("data-dive", "data-note", lambda u: u.startswith("/DataNotes/")),
    ("data-note", "data-note", lambda u: u.startswith("/DataNotes/")),
    ("theory", "theory", lambda u: u.startswith("/theories/") and u != "/theories/"),
    ("fundamental", "fundamental", lambda u: u.startswith("/fundamentals/")),
    ("showcase", "fundamental", lambda u: u.startswith("/fundamentals/")),
    ("tool", "code", lambda u: u.startswith("/code/") and u != "/code/"),
    ("special", "special", lambda u: u.startswith(("/specials/", "/the-long-view"))),
    # By the numbers: the page and one row per card, in the Data Room filter but
    # outside its count of explorers (see NO_COUNT).
    ("explorer", "explorer", lambda u: u.startswith("/by-the-numbers/")),
    # A reading companion counts when the Reading Companions page lists it;
    # the older *-interactive pages are kept for old links and are not listed.
    ("book-summary", "book-summary", lambda u: u.startswith("/BookSummaries/") and _listed(u)),
]
# Kinds the catalogue lists without counting them, because their type already
# has a count of its own (the Data Room's explorers).
NO_COUNT = {"explorer"}

# Single pages the catalogue should carry, by address, with the catalogue type.
PAGES = {"/survey-instruments.html": "reference", "/field-radio.html": "tool"}

_BS_INDEX = (ROOT / "BookSummaries/index.html").read_text(encoding="utf-8").lower()


def _listed(url):
    return url.rsplit("/", 1)[-1].lower() in _BS_INDEX


# A kind with one obvious track takes it; the rest are read from the row.
FIXED_TRACK = {"theory": "policy", "data-note": "policy", "code": "data-tech", "fundamental": "mel"}
CHALLENGE_TRACK = {"Policy & Economics": "policy", "Data & Technology": "data-tech",
                   "Monitoring, Evaluation & Learning": "mel", "Philosophy, Law & Governance": "philosophy",
                   "Health, Communication & Wellbeing": "health", "Gender Equity & Inclusion": "gender"}


def track(row, ctype):
    if ctype in FIXED_TRACK:
        return FIXED_TRACK[ctype]
    if ctype == "challenge" and row.get("category") in CHALLENGE_TRACK:
        return CHALLENGE_TRACK[row["category"]]
    t = " ".join([row.get("category", ""), row.get("title", "")]).lower()
    if "theory of change" in t or "logframe" in t:
        return "mel"
    if "long view" in t:
        return "policy"
    for key, words in (("gender", ("gender", "feminis", "women")),
                       ("health", ("health", "nutrition", "wellbeing", "mental")),
                       ("data-tech", ("data", "survey", "statistic", "code", "python", " r ", "sql", "dashboard", "visual", "technology")),
                       ("philosophy", ("philosophy", "law", "governance", "gandhi", "ambedkar", "rights")),
                       ("policy", ("policy", "econom", "budget", "costing", "theor", "growth", "finance", "development"))):
        if any(w in t for w in words):
            return key
    # Reading companions outside those words are mostly politics and theory.
    return "philosophy" if ctype == "book-summary" else "mel"


def js(s):
    return json.dumps(s, ensure_ascii=False)


def norm(u):
    return u.split("?")[0].rstrip("/").lower()


def build(text):
    head, rest = text.split(START, 1) if START in text else (None, None)
    if head is None:
        raise SystemExit("catalog.html has no catalog:generated:start marker")
    body, tail = rest.split(END, 1)
    if head.rstrip().endswith("}"):  # the hand-written list may end without a comma
        head = head.rstrip() + ",\n"
    hand = set(norm(u) for u in re.findall(r"url: *['\"]([^'\"]+)['\"]", head + tail))
    rows = json.loads((ROOT / "data/search-index.json").read_text(encoding="utf-8"))
    out, seen = [], set()
    for stype, ctype, keep in KINDS:
        for r in rows:
            u = r.get("url", "")
            if r.get("type") != stype or not keep(u) or norm(u) in hand or norm(u) in seen:
                continue
            seen.add(norm(u))
            out.append((ctype, r))
    for u, ctype in PAGES.items():
        r = next((x for x in rows if x.get("url") == u), None)
        if r is None:
            raise SystemExit(f"{u} is not in data/search-index.json")
        if norm(u) not in hand and norm(u) not in seen:
            seen.add(norm(u))
            out.append((ctype, r))
    lines = []
    for i, (ctype, r) in enumerate(out, start=1):
        title = re.sub(r"\s*[:|-]\s*Reading Companion\s*$", "", r["title"]).strip()
        lines.append("    { id: %s, type: %s,%s title: %s, description: %s, track: %s, url: %s },\n" % (
            js(f"gen-{ctype}-{i}"), js(ctype), " noCount: true," if ctype in NO_COUNT else "",
            js(title), js(r.get("description", "")), js(track(r, ctype)), js(r["url"])))
    return head + START + "".join(lines) + END + tail, len(out)


def main():
    text = PAGE.read_text(encoding="utf-8")
    new, n = build(text)
    if "--check" in sys.argv:
        if new != text:
            raise SystemExit("FAIL - catalog.html is stale. Run python3 scripts/build-catalog-extras.py")
        print(f"PASS - catalog.html carries {n} generated entries from site search")
        return
    PAGE.write_text(new, encoding="utf-8")
    print(f"wrote {n} generated entries into catalog.html")


if __name__ == "__main__":
    main()

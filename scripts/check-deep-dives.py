#!/usr/bin/env python3
"""Keep the three Deep Dive lists agreeing with each other.

A deep dive exists in three places and nothing compared them:

  * the page itself, ``DeepDives/<slug>.html``
  * ``data/deep-dives.json``, which the index page fetches and renders
  * the JSON-LD ``ItemList`` inside ``DeepDives/index.html``, which is what
    search engines read

On 2026-09-18 the third was missing ``farm-animal-welfare-india`` (#1106).
The page rendered correctly, because it renders from the JSON; the omission
was visible only to a crawler, and ``numberOfItems`` said 22, agreeing with
its own short list and disagreeing with reality. A count that is derived from
the thing it is meant to check cannot catch anything.

This guard also checks ``reading_count``, because that number is a claim about
the page made somewhere other than the page. It counts ``<article
class="dd-item">`` in the file and compares. Deliberate exemptions live in
``EXEMPT`` with a written reason, and a stale exemption fails too, so the list
cannot rot into a blindfold.

    python3 scripts/check-deep-dives.py

Exit 0 + "PASS" when clean; exit 1 with a listing otherwise.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "DeepDives"
DATA = ROOT / "data" / "deep-dives.json"
INDEX = DIR / "index.html"

# Files under DeepDives/ that are not deep dives.
NOT_A_DIVE = {"index.html", "_template.html"}

# slug -> written reason. A slug listed here must be genuinely absent from
# data/deep-dives.json; if it turns up there, this guard fails on the stale
# exemption rather than passing quietly.
EXEMPT: dict[str, str] = {}

ITEM_RE = re.compile(r'<article class="dd-item">')
# Each page also carries an Article JSON-LD block describing itself. Its "url"
# is a self-reference, so a url naming a different page is a canonical signal
# pointing at the wrong document (#1113): two deep dives built by copying
# platform-gig-work-india.html kept its url, description and datePublished,
# because the headline was rewritten and nothing on screen reads the rest.
ARTICLE_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
SELF_URL_RE = re.compile(r'"url":\s*"[^"]*?/DeepDives/([a-z0-9-]+\.html)"')
LD_RE = re.compile(r'"itemListElement":\s*\[(.*?)\]\s*\}\s*\}\s*</script>', re.S)
LD_URL_RE = re.compile(r'"url":\s*"[^"]*?(/DeepDives/[a-z0-9-]+\.html)"')
NUM_RE = re.compile(r'"numberOfItems":\s*(\d+)')
CHIP_RE = re.compile(r'dd-chip-teal">\s*(\d+) readings')


def main() -> int:
    problems: list[str] = []

    on_disk = {p.name for p in DIR.glob("*.html") if p.name not in NOT_A_DIVE}

    data = json.loads(DATA.read_text(encoding="utf-8"))["deep_dives"]
    in_data = {}
    for entry in data:
        name = entry["url"].rsplit("/", 1)[-1]
        if name in in_data:
            problems.append(f"data/deep-dives.json lists {name} twice")
        in_data[name] = entry

    index_src = INDEX.read_text(encoding="utf-8")
    m = LD_RE.search(index_src)
    if not m:
        print("FAIL - no JSON-LD itemListElement found in DeepDives/index.html")
        return 1
    in_ld = LD_URL_RE.findall(m.group(1))
    ld_set = {u.rsplit("/", 1)[-1] for u in in_ld}
    if len(in_ld) != len(ld_set):
        problems.append("the JSON-LD ItemList repeats a deep dive")

    for name in sorted(on_disk - set(in_data)):
        if name.removesuffix(".html") in EXEMPT:
            continue
        problems.append(f"{name} is on disk but missing from data/deep-dives.json")
    for name in sorted(set(in_data) - on_disk):
        problems.append(f"data/deep-dives.json lists {name}, which is not on disk")
    for name in sorted(set(in_data) - ld_set):
        problems.append(f"{name} is missing from the JSON-LD ItemList in DeepDives/index.html")
    for name in sorted(ld_set - set(in_data)):
        problems.append(f"the JSON-LD ItemList has {name}, which is not in data/deep-dives.json")

    num = NUM_RE.search(index_src)
    if not num:
        problems.append('DeepDives/index.html has no "numberOfItems"')
    elif int(num.group(1)) != len(in_data):
        problems.append(
            f'"numberOfItems" is {num.group(1)} but data/deep-dives.json has {len(in_data)}'
        )

    for name, entry in sorted(in_data.items()):
        page = DIR / name
        if not page.exists():
            continue
        actual = len(ITEM_RE.findall(page.read_text(encoding="utf-8")))
        claimed = entry.get("reading_count")
        if claimed is None:
            problems.append(f"{name} has no reading_count in data/deep-dives.json")
        elif claimed != actual:
            problems.append(
                f"{name}: reading_count is {claimed} but the page has {actual} readings"
            )

        src = page.read_text(encoding="utf-8")
        for blk in ARTICLE_RE.findall(src):
            m = SELF_URL_RE.search(blk)
            if m and m.group(1) != name:
                problems.append(
                    f"{name}: its JSON-LD url says {m.group(1)}, which is a different page "
                    f"(check description and datePublished too)"
                )

        chip = CHIP_RE.search(page.read_text(encoding="utf-8"))
        if not chip:
            problems.append(f"{name} has no \"<n> readings\" chip")
        elif int(chip.group(1)) != actual:
            problems.append(
                f"{name}: the page's own chip says {chip.group(1)} readings "
                f"but the page has {actual}"
            )

    for slug, reason in sorted(EXEMPT.items()):
        if f"{slug}.html" in in_data:
            problems.append(
                f"stale exemption: {slug} is in data/deep-dives.json now, so drop it "
                f"from EXEMPT (was exempt because: {reason})"
            )

    if problems:
        print(f"FAIL - {len(problems)} Deep Dive listing problem(s):\n")
        for p in problems:
            print(f"  {p}")
        return 1

    extra = f" ({len(EXEMPT)} exempted on purpose)" if EXEMPT else ""
    print(
        f"PASS - {len(in_data)} deep dives agree on disk, in data/deep-dives.json "
        f"and in the index page's ItemList{extra}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

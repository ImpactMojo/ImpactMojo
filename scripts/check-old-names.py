#!/usr/bin/env python3
"""Retired product names must not come back into reader-facing text.

The site renamed its products in 2026: the Labs became Free Studio, the
foundational slide decks became the 101 Series, the Pro tools became Pro
Studio, and the book companions became Reading Companions. The renames were
done by hand, page by page, and a UX audit on 2026-10-13 still found the old
names on live pages: "Interactive Labs" 21 times in eight files, a
"Foundational 101 Decks" card on 21 flagship course pages, a catalogue search
box offering to "Search courses, labs, games", and "Book companions" in the
site map's stat strip. A reader who meets two names for one thing reasonably
assumes there are two things.

What is checked: the visible text of every HTML page (script and style
bodies, comments and the generated share block are left out) plus the
attributes a reader sees or hears (placeholder, aria-label, alt, title and
the meta description).

What is not a hit:
  * file and folder names. /Labs/ stays /Labs/, and "MEL Lab" or "Qual
    Insights Lab" are the names of single tools, so only the plural product
    name and the phrases below are matched;
  * dated pages, listed in EXEMPT with a reason, and every path under an
    EXEMPT_DIRS prefix (backups, dated blog posts, translated copies);
  * a line carrying the token "old-name-ok", for a quotation or a third-party
    name that happens to match.

A stale exemption fails too, so the list cannot rot into a blindfold.

Usage:
  python3 scripts/check-old-names.py          # PASS, or every hit and exit 1
  python3 scripts/check-old-names.py --list   # also print hits per file count
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATTERNS = [
    (re.compile(r"\binteractive\s+labs?\b", re.I), "Interactive Labs: say Free Studio"),
    (re.compile(r"\bbasic\s+labs\b", re.I), "basic labs: say Free Studio"),
    (re.compile(r"\b(?:foundational\s+)?101\s+decks\b", re.I), "101 decks: say the 101 Series"),
    (re.compile(r"\bsearch\s+courses,\s*labs\b", re.I), "search placeholder: say Free Studio tools"),
    (re.compile(r"\bbook\s+companions\b", re.I), "Book companions: say Reading Companions"),
    (re.compile(r"\bpro\s+tools\s*\(", re.I), "Pro tools (n): say Pro Studio"),
    # The plural product name in a list of products or with a count. A tool
    # called "MEL Lab" is singular and never matches.
    (re.compile(r"\b(?:courses|games|studios),?\s+(?:and\s+)?labs\b", re.I), "labs as a product: say Free Studio"),
    (re.compile(r"\blabs,?\s+(?:and\s+)?(?:games|tools|templates)\b", re.I), "labs as a product: say Free Studio"),
    (re.compile(r"\b\d+\s+(?:interactive\s+)?labs\b", re.I), "a count of labs: say Free Studio tools"),
    (re.compile(r"\ball\s+labs\b", re.I), "All Labs: say Free Studio"),
]

# Directories whose pages are dated records or copies, not current copy.
EXEMPT_DIRS = {
    "Backups/": "dated copies of the site",
    "node_modules/": "third-party code",
    ".claude/": "agent notes, not served",
    "docs/": "GitBook docs, including the changelog, a dated record",
    "tests/": "test fixtures",
    "supabase/": "email templates, checked by check-counts.py",
    "netlify/": "functions, not pages",
    "scripts/": "tooling",
    "blog/": "blog posts are dated articles and keep the names of their date",
    "BookSummaries/": "compiled companion bundles; their wording is the book's",
}

# Single pages exempt, each with a reason. A stale entry fails.
EXEMPT = {
    "updates.html": "dated what's-new cards record the names in use at the time",
    "testimonials.html": "a reader's own words in a testimonial are never edited",
}

ATTR_RE = re.compile(
    r'\b(?:placeholder|aria-label|alt|title)\s*=\s*"([^"]*)"'
    r'|<meta\s+name="description"\s+content="([^"]*)"',
    re.I,
)
STRIP_RE = re.compile(
    r"<!-- share:start -->.*?<!-- share:end -->"
    r"|<script\b[^>]*>.*?</script>"
    r"|<style\b[^>]*>.*?</style>"
    r"|<!--.*?-->",
    re.S | re.I,
)
TAG_RE = re.compile(r"<[^>]+>")
OK_TOKEN = "old-name-ok"


def blank(m):
    # keep line numbers stable
    return "\n" * m.group(0).count("\n")


def reader_text(src):
    """Return per-line reader-facing text, line numbers preserved."""
    body = STRIP_RE.sub(blank, src)
    out = []
    for line in body.split("\n"):
        attrs = " ".join(a or b for a, b in ATTR_RE.findall(line))
        text = TAG_RE.sub(" ", line)
        out.append(text + " " + attrs)
    return out


def pages():
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(d) for d in EXEMPT_DIRS):
            continue
        yield rel, p


def main(argv):
    hits = []
    seen_exempt = set()
    files_hit = {}
    for rel, path in pages():
        try:
            src = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        raw_lines = src.split("\n")
        found = []
        for i, text in enumerate(reader_text(src)):
            if OK_TOKEN in raw_lines[i]:
                continue
            for rx, why in PATTERNS:
                m = rx.search(text)
                if m:
                    found.append((i + 1, m.group(0), why))
                    break
        if rel in EXEMPT:
            if found:
                seen_exempt.add(rel)
            continue
        for ln, frag, why in found:
            hits.append(f"{rel}:{ln}: \"{frag}\" ({why})")
        if found:
            files_hit[rel] = len(found)

    stale = sorted(set(EXEMPT) - seen_exempt)
    if "--list" in argv:
        for rel, n in sorted(files_hit.items(), key=lambda kv: -kv[1]):
            print(f"{n:4d}  {rel}")
    if hits or stale:
        if hits:
            print(f"FAIL — {len(hits)} retired product name(s) in reader-facing text:\n")
            for h in hits:
                print("  " + h)
        for rel in stale:
            print(f"FAIL — stale exemption: {rel} no longer contains an old name; remove it from EXEMPT")
        return 1
    print(f"PASS — no retired product names in reader-facing text")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Every absolute link to impactmojo.in names something that exists.

Relative links break where a reader can see them. Absolute self-links mostly
live where nobody looks: JSON-LD `url` and `image` fields, which a search
engine reads and a visitor never does. On 2026-10-12 five Labs pages declared
themselves at /Studios/<name>.html, a folder that does not exist, three
flagship courses named JSON-LD images that were never drawn, and the homepage
listed Power BI at a folder with no index page. Every one answered 404 and
every page rendered normally.

A path passes if it is a file, a folder holding index.html, or a pretty URL
for an .html file. Comparison ignores case, because Netlify lowercases paths.
Paths served by a redirect or a function are listed in EXEMPT with a reason,
and a stale exemption fails too.

    python3 scripts/check-self-links.py     # must print PASS
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = ("Backups/", "node_modules/", ".git/")
URL = re.compile(r"https://(?:www\.)?impactmojo\.in(/[^\"'\s<>)#?&\\]*)")

# Served by a rule or a function rather than a file; each checked live 2026-10-12.
EXEMPT = {
    "api/v1": "partner API, netlify/functions/partner-api.mjs",
    "api/v1/catalog": "partner API, netlify/functions/partner-api.mjs",
    "api/v1/courses/gandhi": "partner API, netlify/functions/partner-api.mjs",
}
# Generator templates whose URLs carry placeholders.
TEMPLATE = re.compile(r"\[[A-Z_]+\]|\{\{")


def main():
    files = set()
    for f in ROOT.rglob("*"):
        rel = f.relative_to(ROOT).as_posix()
        if f.is_file() and not rel.startswith(SKIP_DIRS):
            files.add(rel.lower())
    seen, bad = set(), []
    for f in sorted(ROOT.rglob("*.html")):
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP_DIRS):
            continue
        for raw in URL.findall(f.read_text(errors="ignore")):
            p = unquote(raw).strip("/").lower()
            if not p or TEMPLATE.search(raw):
                continue
            if p in EXEMPT:
                seen.add(p)
                continue
            if p in files or p + "/index.html" in files or p + ".html" in files:
                continue
            bad.append((rel, raw))
    stale = sorted(set(EXEMPT) - seen)
    for rel, raw in bad:
        print("FAIL %s names https://www.impactmojo.in%s, which is not on disk" % (rel, raw))
    for p in stale:
        print("FAIL stale exemption: no page links to /%s any more" % p)
    if bad or stale:
        sys.exit(1)
    print("PASS: every absolute self-link resolves")


if __name__ == "__main__":
    main()

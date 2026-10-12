#!/usr/bin/env python3
"""Hold the em dashes inside inline JavaScript strings to a ratchet.

Why this exists
---------------
check-no-em-dashes.py reads page text and deliberately skips <script>. But a
great deal of what a reader sees lives inside scripts: the DATA blocks of the
book companions, the lexicons of the flagship courses, game dialogue, the
catalogue's course descriptions, the practice workbooks' prompts. On
2026-10-12 those strings held 3,653 em dashes that the 2026-10-05 sweep had
never reached, and the second pass removed about 3,500 of them.

What is left is deliberate: verbatim quotations (a book's `quotes` array, a
statute, a speech), attributions after a quote, a bare dash meaning "no
value", and the prompts sent to a language model. A regex cannot tell those
from prose, so this is a ratchet rather than a ban. Each page's count of em
dashes inside string literals that contain a space is recorded in
script-em-dash-baseline.json. A page that gains one fails. A page that loses
one also fails until the baseline is lowered (run with --update), so the
number can only go down.

    python3 scripts/check-script-em-dashes.py            # CI
    python3 scripts/check-script-em-dashes.py --update   # after removing some
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / "scripts" / "script-em-dash-baseline.json"
SKIP = ("Backups/", "node_modules/", "i18n/", "tests/", "mcp-server/", "admin/",
        "supabase/", "docs/", ".claude/")
SCRIPT = re.compile(r"<script\b(?![^>]*\bsrc=)(?![^>]*ld\+json)[^>]*>(.*?)</script>", re.S | re.I)
STR = re.compile(r"'(?:[^'\\\n]|\\.){3,}'|\"(?:[^\"\\\n]|\\.){3,}\"|`(?:[^`\\]|\\.){3,}`", re.S)
EM = re.compile(r"—|\\u2014|\\u\{2014\}|&mdash;|&#8212;|&#x2014;", re.I)


def counts():
    out = {}
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(s) for s in SKIP):
            continue
        n = 0
        for sm in SCRIPT.finditer(p.read_text(encoding="utf-8", errors="ignore")):
            for st in STR.finditer(sm.group(1)):
                s = st.group(0)
                if " " in s:
                    n += len(EM.findall(s))
        if n:
            out[rel] = n
    return out


def main():
    now = counts()
    if "--update" in sys.argv[1:]:
        BASELINE.write_text(json.dumps(now, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print("wrote %s: %d em dashes on %d pages" % (BASELINE.name, sum(now.values()), len(now)))
        return
    base = json.loads(BASELINE.read_text(encoding="utf-8")) if BASELINE.exists() else {}
    up = sorted((f, base.get(f, 0), n) for f, n in now.items() if n > base.get(f, 0))
    down = sorted((f, b, now.get(f, 0)) for f, b in base.items() if now.get(f, 0) < b)
    if up or down:
        print("FAIL — em dashes inside inline-script strings")
        for f, b, n in up:
            print("  %s: %d, allowed %d. Rewrite the new ones (comma, full stop, colon)." % (f, n, b))
        for f, b, n in down:
            print("  %s: %d, baseline %d. Lower the baseline: --update." % (f, n, b))
        sys.exit(1)
    print("PASS — %d em dashes inside script strings on %d pages, none above the ratchet "
          "(quotations, attributions, placeholders, model prompts)" % (sum(now.values()), len(now)))


if __name__ == "__main__":
    main()

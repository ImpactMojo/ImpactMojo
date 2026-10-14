#!/usr/bin/env python3
"""Move the paid modules of each Practice Pack out of the public page.

Every pack keeps its first `freeModules` panels in the page. The rest (the
later modules and the capstone builder) are written to
build/practice-packs/<slug>.json, which is uploaded to the private Supabase
`products` bucket at practice-packs/<slug>.json and served only by
netlify/functions/pack-content.mjs to members with access.

The page keeps an empty panel with the same id and data-gated="1", and the
pack's own script is switched to type="text/x-im-pack" so that
js/practice-pack-gate.js can run it once the paid panels are in place.

Usage:
  python3 scripts/practice-packs/split-gated.py          # split, write JSON
  python3 scripts/practice-packs/split-gated.py --check  # PASS if no page
                                                          # carries paid text
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "build" / "practice-packs"
PANEL = re.compile(r'<div class="module-panel(?: active)?" id="module-(\d+)"[^>]*>')
DIV = re.compile(r'<div\b|</div>', re.I)


def panel_end(s, start):
    depth = 0
    for m in DIV.finditer(s, start):
        depth += 1 if m.group(0).lower().startswith('<div') else -1
        if depth == 0:
            return m.end()
    raise ValueError("unbalanced div")


def free_count(s):
    m = re.search(r"freeModules\s*:\s*(\d+)", s)
    return int(m.group(1)) if m else 2


def pack_script(s):
    """The inline script that defines goTab, the pack's own logic."""
    for m in re.finditer(r'<script(\s[^>]*)?>(.*?)</script>', s, re.S):
        if 'function goTab' in m.group(2):
            return m
    return None


def split(path, check=False):
    s = path.read_text(encoding="utf-8")
    slug = path.parent.name
    free = free_count(s)
    gated, out, pos = {}, [], 0
    for m in PANEL.finditer(s):
        idx = int(m.group(1))
        if idx < free:
            continue
        end = panel_end(s, m.start())
        inner = s[m.end():end - len('</div>')]
        if 'data-gated="1"' in m.group(0):
            continue
        if inner.strip():
            gated[str(idx)] = inner
        out.append(s[pos:m.start()])
        tag = m.group(0)[:-1] + ' data-gated="1">'
        out.append(tag + '</div>')
        pos = end
    out.append(s[pos:])
    new = ''.join(out)
    sm = pack_script(new)
    if sm and 'text/x-im-pack' not in (sm.group(1) or ''):
        new = new[:sm.start()] + '<script type="text/x-im-pack" id="im-pack-js">' + sm.group(2) + '</script>' + new[sm.end():]
    if check:
        return slug, bool(gated), new != s
    if gated:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{slug}.json").write_text(json.dumps({"slug": slug, "free": free, "panels": gated}, ensure_ascii=False), encoding="utf-8")
    if new != s:
        path.write_text(new, encoding="utf-8")
    return slug, len(gated), new != s


def main():
    check = "--check" in sys.argv
    pages = sorted((ROOT / "practice-packs").glob("*/index.html"))
    bad = []
    for p in pages:
        slug, gated, changed = split(p, check)
        if check and (gated or changed):
            bad.append(slug)
        elif not check:
            print(f"{slug}: {gated} panels moved" + (" (page rewritten)" if changed else ""))
    if check:
        if bad:
            print("FAIL - paid panels still in the page: " + ", ".join(bad))
            return 1
        print(f"PASS - {len(pages)} Practice Packs carry no paid panels in the page")
    return 0


if __name__ == "__main__":
    sys.exit(main())

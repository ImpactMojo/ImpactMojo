#!/usr/bin/env python3
"""No content card may sit inside an element that site-chrome.js removes.

js/site-chrome.js deletes the legacy page chrome at runtime: every <footer>,
.footer, .foot, .site-footer, .im-footer, the old nav bars, and any <header>
or <nav> that is a direct child of <body>. Whatever is inside goes with it.

On 2026-10-13 that was 19 Reading Companion cards. They had been pasted inside
the legacy <footer> of BookSummaries/index.html, after the social icons, so
with JavaScript off the hub showed 185 cards and with it on 166. Geertz, Asad,
Fanon, Wynter and fifteen others were live, linked from nothing a visitor could
see, and the hub's own count disagreed with data/counts.json. Nothing errored
and every other check passed, because the markup was valid and the page had
its <h1>.

This guard uses the same model of what the chrome removes as
check-h1-survives-chrome.py (it imports it, so the two cannot drift), then
looks inside each removed block for a content card: an element whose class
list carries a token that is `card`, or ends or starts with `card`/`cards`
as a hyphenated part (`book-card`, `card-grid`, `tool-card`). A footer's own
link lists and social icons carry no such class, so the check stays quiet
unless content has landed in the wrong place.

Exemptions live in EXEMPT with a written reason, and a stale one fails.
"""
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    'h1chrome', ROOT / 'scripts' / 'check-h1-survives-chrome.py')
h1chrome = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(h1chrome)

EXEMPT = {
    # "path.html": "reason",
}

CLASS_ATTR = re.compile(r'<([a-z][a-z0-9]*)\b[^>]*\bclass\s*=\s*["\']([^"\']*)["\']', re.I)
CARD_TOKEN = re.compile(r'^(?:cards?|cards?[-_].*|.*[-_]cards?)$', re.I)


def removed_spans(body: str):
    """Outermost (start, end) spans that site-chrome.js removes."""
    spans = []
    for m in h1chrome.OPEN_TAG.finditer(body):
        tag, attrs = m.group(1), m.group(2)
        if not h1chrome._is_killed(tag, attrs):
            continue
        end = h1chrome._element_end(body, tag, m.end())
        if end > 0:
            spans.append((m.start(), end))
    for start, open_end in h1chrome.body_level_headers(body):
        end = h1chrome._element_end(body, 'header', open_end)
        if end > 0:
            spans.append((start, end))
    spans.sort(key=lambda sp: (sp[0], -sp[1]))
    outer, last_end = [], -1
    for a, b in spans:
        if a >= last_end:
            outer.append((a, b))
            last_end = b
    return outer


def strip_scripts(src: str) -> str:
    """Blank out <script> and <style> bodies, keeping offsets, so markup held
    in JavaScript strings is not read as live markup."""
    def blank(m):
        return m.group(1) + ' ' * len(m.group(2)) + m.group(3)
    return re.sub(r'(<(?:script|style)\b[^>]*>)(.*?)(</(?:script|style)>)', blank, src,
                  flags=re.I | re.S)


def main() -> int:
    failures, checked = [], 0
    for path in sorted(ROOT.rglob('*.html')):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(('Backups/', 'node_modules/', 'tests/')) or '/.claude/' in f'/{rel}':
            continue
        try:
            src = path.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        if 'site-chrome.js' not in src or h1chrome.opts_out(src, rel):
            continue
        checked += 1
        if rel in EXEMPT:
            continue
        b = src.find('<body')
        if b < 0:
            continue
        body = strip_scripts(src[b:])
        for a, e in removed_spans(body):
            block = body[a:e]
            hits = []
            for m in CLASS_ATTR.finditer(block):
                toks = [t for t in m.group(2).split() if CARD_TOKEN.match(t)]
                if toks:
                    hits.append(f'<{m.group(1).lower()} class="{" ".join(toks)}">')
            if hits:
                line = src[:b].count('\n') + body[:a].count('\n') + 1
                failures.append(f'{rel}:{line}: {len(hits)} card element(s) inside a block '
                                f'site-chrome removes, first {hits[0]}')

    live = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.html')}
    for rel in sorted(set(EXEMPT) - live):
        failures.append(f'{rel} (stale EXEMPT entry, file no longer exists)')

    if failures:
        print('FAIL - content cards sit inside chrome that js/site-chrome.js deletes at')
        print('       runtime. Visitors with JavaScript on never see them. Move them out')
        print('       of the <footer> / legacy header into the page content.\n')
        for f in failures:
            print(f'  {f}')
        return 1
    print(f'PASS - no content card sits inside removed chrome on {checked} pages that load site-chrome.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

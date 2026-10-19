#!/usr/bin/env python3
"""Give every handout's fixed multi-column grids one column on a phone.

The handouts lay out comparison cards in grids such as
`grid-template-columns: 1fr 1fr` and only drop to one column under
`@media print`. On a 390px phone each column is about 165px, and a `1fr`
track never shrinks below its longest word. That fitted while the body face
was the condensed Amaranth; v10.384.0 (14 October 2026) moved body text to
Inter, which is wider, and nine handouts began scrolling sideways by 6 to 20px
(#1281). The print rule shows the narrow layout the authors meant, so this
gives the same grids one column at 600px and below.

Grids set in a page's stylesheet and in a style attribute are both
covered. Only grids written with two or more fixed tracks are touched (`1fr 1fr`,
`repeat(2, 1fr)`, `2fr 1fr` and so on). `auto-fit` and `auto-fill` grids
already wrap on their own, and the legacy `.im-*` chrome is left alone.
Rules inside `@media print` are ignored, since a
selector that is only a grid on paper needs nothing on a phone.

The rule is written between markers immediately before a `</style>` in the
page head (testing rule 31: never at a computed offset), so a rerun replaces
it and the script is idempotent.

    python3 scripts/handout-phone-grids.py          # write
    python3 scripts/handout-phone-grids.py --check  # fail if any page is stale
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = '/* phone-grids:start */', '/* phone-grids:end */'
BLOCK = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
STYLE = re.compile(r'<style[^>]*>(.*?)</style>', re.S | re.I)


def strip_comments(css):
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


def rules(css):
    """Yield (media, selector, body) for each style rule, one level of @media deep."""
    i, n, media = 0, len(css), [None]
    depth_media = []
    depth = 0
    buf = ''
    while i < n:
        ch = css[i]
        if ch == '{':
            head = buf.strip()
            buf = ''
            if head.startswith('@'):
                depth_media.append(depth)
                media.append(head)
                depth += 1
            else:
                close = css.find('}', i)
                if close == -1:
                    return
                yield media[-1], head, css[i + 1:close]
                i = close
        elif ch == '}':
            buf = ''
            if depth_media and depth_media[-1] == depth - 1:
                depth_media.pop()
                media.pop()
            depth = max(0, depth - 1)
        else:
            buf += ch
        i += 1


def fixed_tracks(value):
    v = value.strip().rstrip(';').replace('!important', '').strip()
    if re.search(r'auto-(fit|fill)', v):
        return 0
    m = re.fullmatch(r'repeat\(\s*(\d+)\s*,\s*([\d.]+fr)\s*\)', v)
    if m:
        return int(m.group(1))
    parts = v.split()
    if len(parts) >= 2 and all(re.fullmatch(r'[\d.]+fr', p) for p in parts):
        return len(parts)
    return 0


def selectors(html):
    head = html.split('</head>', 1)[0]
    css = strip_comments(' '.join(STYLE.findall(BLOCK.sub('', head))))
    found = []
    for media, sel, body in rules(css):
        if media and 'print' in media:
            continue
        for decl in body.split(';'):
            if ':' not in decl:
                continue
            prop, val = decl.split(':', 1)
            if prop.strip() == 'grid-template-columns' and fixed_tracks(val) >= 2:
                for s in sel.split(','):
                    s = ' '.join(s.split())
                    # .im-* is the legacy top bar and footer, which carry their
                    # own phone rules and which js/site-chrome.js removes anyway.
                    if s and s not in found and not s.startswith('.im-'):
                        found.append(s)
    return found


INLINE = re.compile(r'style="[^"]*?grid-template-columns:\s*([^;"]+)', re.I)


def inline_values(html):
    """Fixed multi-column grids written in a style attribute, as written."""
    body = html.split('</head>', 1)[-1]
    out = []
    for m in INLINE.finditer(body):
        v = m.group(1).strip()
        if fixed_tracks(v) >= 2 and v not in out:
            out.append(v)
    return out


def render(sels, inline):
    rules = []
    if sels:
        rules.append('  ' + ',\n  '.join(sels) + '{grid-template-columns:1fr}')
    if inline:
        # A style attribute beats any stylesheet rule unless the rule is
        # !important, so these match the attribute's own text.
        attrs = ',\n  '.join('[style*="grid-template-columns: %s"]' % v for v in inline)
        rules.append('  ' + attrs + '{grid-template-columns:1fr !important}')
    return (f'{START}\n'
            '/* Fixed multi-column grids take one column on a phone; see\n'
            '   scripts/handout-phone-grids.py (#1281). */\n'
            '@media (max-width:600px){\n' + '\n'.join(rules) + '\n}\n'
            f'{END}\n')


def apply(html):
    clean = BLOCK.sub('', html)
    sels = selectors(clean)
    inline = inline_values(clean)
    if not sels and not inline:
        return clean
    head, sep, rest = clean.partition('</head>')
    at = head.rfind('</style>')
    if at == -1:
        return clean
    head = head[:at] + render(sels, inline) + head[at:]
    return head + sep + rest


def main():
    check = '--check' in sys.argv
    stale, changed = [], 0
    for path in sorted((ROOT / 'Handouts').rglob('*.html')):
        text = path.read_text(encoding='utf-8')
        new = apply(text)
        if new != text:
            if check:
                stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(new, encoding='utf-8')
                changed += 1
    if check:
        if stale:
            print('FAIL - phone grid rule missing or stale in %d handout(s):' % len(stale))
            for s in stale:
                print('  ' + s)
            return 1
        print('PASS - every handout grid with fixed columns has its phone rule')
        return 0
    print('wrote the phone grid rule into %d handout(s)' % changed)
    return 0


if __name__ == '__main__':
    sys.exit(main())

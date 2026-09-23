#!/usr/bin/env python3
"""A custom property declared only inside a dark-theme block.

In the default (light) theme every rule referencing it then has no value at
all. `background: var(--gradient-primary)` with no value is not an error and
does not fall back to anything useful: the declaration is invalid at computed
value time, the property takes its initial value, and the element paints
nothing. A button with `color: white` on top of that is white text on the page
background.

Found on 2026-09-23 across 17 pages, including the whole legal set, the auth
pages, about, contact, faq, podcast and workshops. `--gradient-primary` was
declared once, inside `body.dark-mode`, and referenced from nine rules on
blog.html alone. On 404.html it was the primary call to action: measured from
the rendered pixels, white on #F8FAFC, 1.04:1.

Nothing catches this. The page renders, the build has no build, and the
element is simply absent. It is the same class as #1016, where `--im-surface`
and `--im-surface-2` were referenced across the law guides and defined
nowhere.

A `var(--x, fallback)` reference is fine and is not reported: the fallback is
the light value. Only a bare `var(--x)` counts.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'Backups', 'node_modules', '.git', 'docs', 'tests'}

DARK_SEL = re.compile(r'(body\.dark-mode|\[data-theme=["\']?dark["\']?\]|prefers-color-scheme:\s*dark)')
STYLE = re.compile(r'<style[^>]*>(.*?)</style>', re.S)
RULE = re.compile(r'([^{}]+)\{([^{}]*)\}')
DECL = re.compile(r'(--[\w-]+)\s*:')
# A bare var(--x): no comma before the closing paren.
BARE_VAR = re.compile(r'var\(\s*(--[\w-]+)\s*\)')

# path -> {token: reason}. A stale exemption fails too.
EXEMPT = {}


def pages():
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in sorted(files):
            if f.endswith('.html'):
                yield os.path.join(dirpath, f)


def dark_only(path):
    """Tokens this page's own <style> uses bare, but declares only in dark."""
    with open(path, encoding='utf-8', errors='replace') as fh:
        src = fh.read()
    css = ''.join(m.group(1) for m in STYLE.finditer(src))
    if not css:
        return set()
    light, dark = set(), set()
    for m in RULE.finditer(css):
        props = set(DECL.findall(m.group(2)))
        if props:
            (dark if DARK_SEL.search(m.group(1)) else light).update(props)
    used = set(BARE_VAR.findall(css))
    return (used & dark) - light


def main():
    failures = []
    seen_exempt = set()
    n = 0
    for path in pages():
        n += 1
        rel = os.path.relpath(path, ROOT)
        bad = dark_only(path)
        allowed = EXEMPT.get(rel, {})
        for token in sorted(bad):
            if token in allowed:
                seen_exempt.add((rel, token))
                continue
            failures.append('%s: %s is declared only in a dark-theme block, '
                            'so it has no value in the default theme' % (rel, token))
    for rel, tokens in EXEMPT.items():
        for token in tokens:
            if (rel, token) not in seen_exempt:
                failures.append('stale exemption: %s / %s no longer fails; '
                                'remove it from EXEMPT' % (rel, token))
    if failures:
        print('FAIL - %d problem(s) across %d page(s):' % (len(failures), n))
        for f in failures:
            print('  ' + f)
        return 1
    print('PASS - no dark-only custom property is referenced bare, across %d page(s).' % n)
    return 0


if __name__ == '__main__':
    sys.exit(main())

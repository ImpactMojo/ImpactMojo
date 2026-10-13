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


COMMENT = re.compile(r'/\*.*?\*/', re.S)


def blocks(css):
    """Yield (preludes, body) for every innermost declaration block.

    `preludes` is the selector of the block plus every enclosing at-rule
    prelude, outermost first. This is the point of the walk. Until 2026-10-13
    the check matched `selector { body }` with a flat regex, so in

        @media (prefers-color-scheme: dark) { :root { --gradient-primary: ... } }

    the inner rule's selector was read as `:root` alone and the declaration
    was counted as a light one. That is exactly how 44 blog posts and
    blog.html declared `--gradient-primary` only for dark and passed: the
    Substack button painted white on #F8FAFC in the light theme while this
    check printed PASS.
    """
    stack = []
    start = 0
    for i, ch in enumerate(css):
        if ch == '{':
            stack.append(css[start:i].strip())
            start = i + 1
        elif ch == '}':
            body = css[start:i]
            if stack:
                prelude = stack.pop()
                if ':' in body or not body.strip():
                    yield stack + [prelude], body
            start = i + 1


def dark_only(path):
    """Tokens this page's own <style> uses bare, but declares only in dark."""
    with open(path, encoding='utf-8', errors='replace') as fh:
        src = fh.read()
    css = COMMENT.sub('', ''.join(m.group(1) for m in STYLE.finditer(src)))
    if not css:
        return set()
    light, dark = set(), set()
    for preludes, body in blocks(css):
        props = set(DECL.findall(body))
        if props:
            is_dark = any(DARK_SEL.search(p) for p in preludes)
            (dark if is_dark else light).update(props)
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

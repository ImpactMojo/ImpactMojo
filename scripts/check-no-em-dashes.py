#!/usr/bin/env python3
"""Fail when an em dash appears in reader-facing text of a page.

Why this exists
---------------
The site's house style bans the em dash: machine-written prose leans on it, and
readers have started to read it as a tell. On 2026-10-05 about 56,000 of them
were removed from copy, titles, meta tags, JSON-LD and page data. Nothing
stops the next page from bringing them back, so this check does.

What it reads: text nodes and the attributes that reach a reader (title, alt,
aria-label, placeholder, meta content), outside <script>, <style>, <pre>,
<code> and <textarea>. JSON-LD is read too. It deliberately does not read
inline JavaScript, where an em dash in a comment or a quoted source is not a
house-style failure, or the translated pages, which are a separate pass.

A text node that is only an em dash is a table-cell placeholder meaning "no
value" and is allowed. Anything else needs rewriting: a colon for an
explanation, a comma for an aside, a full stop for a new sentence, a pipe in a
title.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'Backups', 'node_modules', '.git', 'i18n', 'tests', 'archive'}
EM = re.compile(r'(?:&mdash;|&#8212;|&#x2014;|—)', re.I)
BLOCK = re.compile(r'<(script|style|pre|code|textarea)\b[^>]*>.*?</\1\s*>', re.S | re.I)
LDJSON = re.compile(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', re.S | re.I)
COMMENT = re.compile(r'<!--.*?-->', re.S)
TAG = re.compile(r'<[^>]+>')
ATTR = re.compile(r'\b(content|alt|aria-label|title|placeholder)=(["\'])(.*?)\2', re.S | re.I)


def findings(html):
    out = []
    for m in LDJSON.finditer(html):
        if EM.search(m.group(1)):
            out.append('JSON-LD')
    h = COMMENT.sub('', html)
    h = BLOCK.sub('<x>', h)
    for tag in TAG.findall(h):
        for m in ATTR.finditer(tag):
            if EM.search(m.group(3)):
                out.append(m.group(1) + '=' + m.group(3)[:50])
    for text in TAG.split(h):
        if EM.search(text) and EM.sub('', text).strip() != '':
            out.append(text.strip()[:60])
    return out


def main():
    bad = {}
    n = 0
    for r, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(r, f)
            n += 1
            try:
                h = open(p, encoding='utf-8').read()
            except UnicodeDecodeError:
                continue
            fs = findings(h)
            if fs:
                bad[os.path.relpath(p, ROOT)] = fs
    if bad:
        print('FAIL - %d page(s) carry an em dash in reader-facing text:' % len(bad))
        for p, fs in sorted(bad.items())[:40]:
            print('  %s (%d): %s' % (p, len(fs), fs[0]))
        print('Use a colon, comma, full stop or pipe. See scripts/check-no-em-dashes.py.')
        return 1
    print('PASS - no em dash in reader-facing text across %d page(s).' % n)
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Fail when a 101 deck is thinner than the standard, or when the backlog rots.

Why this exists
---------------
The flagship courses had a written standard and drifted anyway. The 52
foundational decks had the opposite problem: no standard at all, so nobody
could tell a thin deck from a dense one without opening it, and no drift was
ever reported because there was no bar to drift from.

Measured 2026-08-22, the decks are not on a gradient. Forty sit at 67-81
words per slide; twelve sit at 140-227; nothing is in between. Every deck has
~100 slides and ~102 SVG figures, so the shell is uniform and the content
varies 3.4x. That cliff is what makes a floor defensible -- it is the line the
newer decks already clear, not an aesthetic preference.

See docs/101-deck-standard.md for what the numbers mean.
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECKS = ROOT / '101-courses'

# Counted as real words: entities are decoded and bare symbols (a dash, a
# bullet) are not words. The first version split the raw markup, so each
# "&mdash;" counted as a word and the 140 floor sat on an inflated measure;
# removing the em dashes from the copy moved two decks to 139. On the real
# measure the dense group runs 136-227 and the thin group stays at 81 or
# below, so the floor sits in the same gap, at 130.
MIN_WORDS_PER_SLIDE = 130
# Set at the FLOOR of the dense group, not its ceiling. mel-basics carries 33
# tables and 76 two-column slides; setting the bar there would have failed four
# decks that are demonstrably fine, which is how a guard loses its authority.
MIN_TABLES = 7
MIN_TWO_COL = 28

# Decks below the floor, with their measured density. Empty since 2026-08-23:
# the backlog opened at 41 decks on 2026-08-22 and every one has been rewritten.
# Kept rather than deleted, because the two properties below are what make the
# floor enforceable, and a deck genuinely mid-rewrite can be listed here again.
#
# This list can only SHRINK: a deck here that now clears the floor fails as a
# stale entry, and a deck NOT here that falls below the floor fails outright.
# Without both halves the list would quietly become a permanent exemption.
DECK_BACKLOG = {}

# Interactive courses that live in 101-courses/ but are not slide decks. They have
# modules and code cells, not slides, so a words-per-slide floor means nothing for them.
# A name here that no longer exists fails, so the list cannot go stale.
NOT_DECKS = set()

SLIDE_RE = re.compile(r'class="slide[ "]')
TABLE_RE = re.compile(r'<table', re.I)
TWOCOL_RE = re.compile(r'two-col')


def measure(path):
    src = path.read_text(encoding='utf-8', errors='replace')
    body = re.sub(r'<script.*?</script>', '', src, flags=re.S)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.S)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', body))
    words = len([t for t in text.split() if re.search(r'\w', t)])
    slides = len(SLIDE_RE.findall(src)) or 1
    return {
        'words': words,
        'slides': slides,
        'wps': words / slides,
        'tables': len(TABLE_RE.findall(src)),
        'two_col': len(TWOCOL_RE.findall(src)),
        'svgs': src.count('<svg'),
    }


def main():
    decks = sorted(p for p in DECKS.glob('*.html') if p.name != 'index.html' and p.name not in NOT_DECKS)
    for name in sorted(NOT_DECKS):
        if not (DECKS / name).exists():
            print('FAIL - %s is in NOT_DECKS but does not exist' % name)
            return 1
    if not decks:
        print('FAIL - no decks found in %s' % DECKS)
        return 1

    failures, backlog_seen = [], []
    for p in decks:
        m = measure(p)
        thin = m['wps'] < MIN_WORDS_PER_SLIDE
        listed = p.name in DECK_BACKLOG

        if thin and not listed:
            failures.append('%-32s %3.0f words/slide (floor %d) and not in DECK_BACKLOG'
                            % (p.name, m['wps'], MIN_WORDS_PER_SLIDE))
        elif thin and listed:
            backlog_seen.append((p.name, m['wps']))
        elif not thin and listed:
            failures.append('%-32s now %3.0f words/slide - clears the floor; remove it '
                            'from DECK_BACKLOG' % (p.name, m['wps']))
        else:
            # Above the floor: the structural checks apply.
            if m['tables'] < MIN_TABLES:
                failures.append('%-32s %d table(s), needs %d' % (p.name, m['tables'], MIN_TABLES))
            if m['two_col'] < MIN_TWO_COL:
                failures.append('%-32s %d two-column slide(s), needs %d'
                                % (p.name, m['two_col'], MIN_TWO_COL))

    missing = sorted(set(DECK_BACKLOG) - {p.name for p in decks})
    for name in missing:
        failures.append('%-32s in DECK_BACKLOG but no such deck exists' % name)

    if backlog_seen:
        print('Backlog: %d deck(s) below %d words/slide, queued for rewrite:'
              % (len(backlog_seen), MIN_WORDS_PER_SLIDE))
        for name, wps in sorted(backlog_seen, key=lambda r: r[1]):
            print('    %-32s %3.0f' % (name, wps))
        print()

    if failures:
        print('FAIL')
        for f in failures:
            print('  ' + f)
        print('\nSee docs/101-deck-standard.md.')
        return 1

    print('PASS - %d deck(s) checked, %d above the floor, %d in the backlog.'
          % (len(decks), len(decks) - len(backlog_seen), len(backlog_seen)))
    return 0


if __name__ == '__main__':
    sys.exit(main())

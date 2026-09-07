#!/usr/bin/env python3
"""Guard: every box in a Theories of Development diagram is readable, in both themes.

Why this exists
---------------
The diagrams in js/theories.js paint text onto a coloured box, which is the
exact arrangement that has been got wrong twice in this repo (rules/testing.md
item 12: white on #d97706 at 3.19:1, and every outer-ring label on the
Fundamentals wheel at 2.3 to 3.2:1). Neither audit caught either one, because
axe-core does not evaluate SVG text contrast and pa11y ran one theme.

This renderer avoids the mechanism that caused those failures: it never picks
an ink at render time. Each node kind names a fill token and an ink token, and
css/theories.css defines both per theme. That moves the whole question into the
stylesheet, where it can be read, which is what this script does.

It checks three things, and the third is the one an eye would miss:

  * each fill/ink pair clears 4.5:1, in light and in dark;
  * the edge stroke clears 3:1 against the canvas, the threshold for a
    graphic that carries meaning;
  * the *dimmed* state clears 4.5:1 too. Earlier steps are drawn at reduced
    opacity, so their real contrast is between two composites against the
    canvas rather than between the two tokens, and lowering --th-dim far
    enough would make every completed step of every argument unreadable while
    each token pair still passed on its own.

Run: python3 scripts/check-theories-contrast.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "css" / "theories.css"

KINDS = [("cause", "--th-cause-ink", "--th-cause-bg"),
         ("mechanism", "--th-mech-ink", "--th-mech-bg"),
         ("outcome", "--th-out-ink", "--th-out-bg")]
TEXT_MIN, GRAPHIC_MIN = 4.5, 3.0


def rgb(value):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def luminance(colour):
    out = []
    for channel in rgb(colour):
        c = channel / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def blend(fg, bg, alpha):
    f, b = rgb(fg), rgb(bg)
    return "#%02x%02x%02x" % tuple(round(f[i] * alpha + b[i] * (1 - alpha)) for i in range(3))


def block(src, selector):
    """Return the custom properties declared in one rule."""
    i = src.find(selector)
    if i == -1:
        return {}
    body = src[src.index("{", i) + 1:]
    depth, end = 1, 0
    for pos, ch in enumerate(body):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = pos
                break
    return dict(re.findall(r"(--[a-z0-9-]+)\s*:\s*([^;]+);", body[:end]))


def main():
    src = CSS.read_text(encoding="utf-8")
    base = block(src, ":root {")
    dark = block(src, '[data-theme="dark"] {')
    media = block(src, ':root:not([data-theme="light"])')
    problems = []

    if not base:
        print(f"FAIL - no :root token block found in {CSS}")
        return 1

    # The media-query copy and the [data-theme] copy must agree, or the system
    # default and the explicit toggle render differently.
    for key, value in dark.items():
        if media.get(key, "").strip() != value.strip():
            problems.append(f"token {key} differs between [data-theme=\"dark\"] and the "
                            f"prefers-color-scheme block")

    try:
        dim = float(base["--th-dim"])
    except (KeyError, ValueError):
        problems.append("--th-dim is missing from :root or is not a number")
        dim = 1.0

    for theme, tokens in (("light", base), ("dark", {**base, **dark})):
        canvas = tokens.get("--th-canvas", "").strip()
        for kind, ink_key, bg_key in KINDS:
            ink, bg = tokens.get(ink_key, "").strip(), tokens.get(bg_key, "").strip()
            if not ink or not bg:
                problems.append(f"{theme}: {kind} is missing {ink_key} or {bg_key}")
                continue
            r = ratio(ink, bg)
            if r < TEXT_MIN:
                problems.append(f"{theme}: {kind} label {ink} on {bg} is {r:.2f}:1 "
                                f"(needs {TEXT_MIN})")
            r_dim = ratio(blend(ink, canvas, dim), blend(bg, canvas, dim))
            if r_dim < TEXT_MIN:
                problems.append(f"{theme}: {kind} label at --th-dim {dim} is {r_dim:.2f}:1 "
                                f"against its own box (needs {TEXT_MIN}); raise --th-dim")

        edge = tokens.get("--th-edge", "").strip()
        if edge and canvas:
            r = ratio(edge, canvas)
            if r < GRAPHIC_MIN:
                problems.append(f"{theme}: edge stroke {edge} on {canvas} is {r:.2f}:1 "
                                f"(needs {GRAPHIC_MIN} for a meaningful graphic)")

    if problems:
        print(f"FAIL - {len(problems)} contrast problem(s) in {CSS.name}:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"PASS - diagram text clears {TEXT_MIN}:1 in both themes, dimmed and undimmed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

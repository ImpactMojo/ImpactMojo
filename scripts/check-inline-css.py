#!/usr/bin/env python3
"""Every inline stylesheet closes what it opens.

A browser does not reject a stylesheet with an unclosed rule. It keeps
parsing, folds everything after the break into the broken declaration, and
throws it away, so the page renders with part of its CSS silently missing.
Nothing errors and nothing in the console says so.

On 2026-10-10 that was 79 pages. A contrast pass in August and September
inserted its block of dark-theme corrections at a fixed character offset
rather than at the end of the stylesheet, so on 77 pages it landed in the
middle of a word: `justify-content:cent` + the block + `er;}`. Everything
from the split to the end of the block was lost, including the corrections
themselves. Two Flagship lexicons had a separate, older defect: the
stylesheet stopped at `align-items: cent` and the rest of the shared top-bar
CSS was never there.

This check reads each <style> element, skipping comments and strings, and
fails if a rule is left open, a brace closes nothing, a comment never ends,
or a comment starts on a line whose previous line stops mid-declaration
(the shape the offset insertion left).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = ("Backups/", "node_modules/", "tests/visual/")
# Files whose <style> bodies are templates, not CSS. Path -> reason.
EXEMPT = {}


def scan(css):
    """Return a list of problems in one stylesheet body."""
    problems = []
    depth, i, n = 0, 0, len(css)
    stack, start = [], 0  # prelude of each open block; start of the current prelude
    while i < n:
        c = css[i]
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            if j < 0:
                problems.append("comment never closed (line %d)" % (css.count("\n", 0, i) + 1))
                return problems
            if css[:i].endswith("\n"):
                prev = css[:i].rstrip("\n")
                last = prev[-1:]
                cut = (last not in "{};,>/" if depth > 0 else (last.isalnum() or last in "-_.#(:"))
                if prev and not last.isspace() and cut:
                    problems.append("comment inserted mid-declaration (line %d)" % (css.count("\n", 0, i) + 1))
            i = j + 2
            continue
        if c in "\"'":
            j = i + 1
            while j < n and css[j] != c:
                if css[j] == "\n":
                    # CSS strings cannot span a line; the parser drops the declaration.
                    problems.append("string not closed on its line (line %d)" % (css.count("\n", 0, i) + 1))
                    break
                j += 2 if css[j] == "\\" else 1
            i = j + 1
            continue
        if css.startswith("*/", i):
            problems.append("'*/' outside any comment (line %d)" % (css.count("\n", 0, i) + 1))
            i += 2
            continue
        if c == "{":
            prelude = re.sub(r"/\*.*?\*/", "", css[start:i], flags=re.S).strip()
            if stack and not stack[-1].startswith("@"):
                problems.append("rule nested inside '%s' (line %d)" % (stack[-1][:40], css.count("\n", 0, i) + 1))
            stack.append(prelude)
            start = i + 1
            depth += 1
        elif c == ";" and (not stack or not stack[-1].startswith("@")):
            start = i + 1
        elif c == "}":
            if stack:
                stack.pop()
            start = i + 1
            depth -= 1
            if depth < 0:
                problems.append("'}' closes nothing (line %d)" % (css.count("\n", 0, i) + 1))
                depth = 0
        i += 1
    if depth > 0:
        problems.append("%d rule(s) left open at the end" % depth)
    return problems


def main():
    errors, sheets, seen_exempt = [], 0, set()
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP):
            continue
        if rel in EXEMPT:
            seen_exempt.add(rel)
            continue
        s = p.read_text(encoding="utf-8", errors="ignore")
        # A <style> written inside a script string is JavaScript, not markup.
        s = re.sub(r"<script\b.*?</script>", "", s, flags=re.S | re.I)
        for m in re.finditer(r"<style\b[^>]*>(.*?)</style>", s, re.S | re.I):
            sheets += 1
            for prob in scan(m.group(1)):
                errors.append("%s: %s" % (rel, prob))
    stale = sorted(set(EXEMPT) - seen_exempt)
    if errors or stale:
        print("FAIL — inline stylesheets that do not close")
        for e in errors:
            print("  " + e)
        for s in stale:
            print("  stale EXEMPT entry: " + s)
        sys.exit(1)
    print("PASS — %d inline stylesheets, every rule and comment closed" % sheets)


if __name__ == "__main__":
    main()

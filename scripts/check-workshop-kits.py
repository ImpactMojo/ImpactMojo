#!/usr/bin/env python3
"""Guard: the facilitator kits stay valid Workshopy Markdown.

Why this exists
---------------
`facilitator-kits/*.md` are not documents we render. They are imported into
Workshopy, where the format carries meaning that plain Markdown does not:

  * a top-level `#` heading starts a new **step**
  * `#[quiz]` turns a step into a **graded quiz**
  * inside a quiz, `##` is a question and `- [ ]` / `- [x]` are its options,
    with `[x]` marking the correct one

Verified against workshopy.io's own published example, 2026-09-18.

The failure mode is quiet and lands on a facilitator in front of a room: a quiz
with no correct option marked grades everyone wrong, a `##` outside a quiz step
looks like a question and is not one, and a stray `#` mid-paragraph silently
splits a step in two. None of that is visible in a Markdown preview, which is
where an author would check.

It also enforces the free-tier constraint the kits are written for: sessions up
to 45 minutes, which in practice means a step count a facilitator can actually
get through. A kit that cannot finish in the room is worse than no kit.

Run: python3 scripts/check-workshop-kits.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KITS = ROOT / "facilitator-kits"

MAX_STEPS = 12          # 45 minutes; beyond this the room runs out of time
MIN_STEPS = 4
MIN_QUIZZES = 1


def check(path: pathlib.Path) -> list[str]:
    problems = []
    lines = path.read_text(encoding="utf-8").split("\n")

    steps, quiz_steps = [], []
    current = None
    fenced = False

    for n, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue

        if line.startswith("#[quiz]"):
            current = {"line": n, "quiz": True, "questions": []}
            steps.append(current)
            quiz_steps.append(current)
            if not line[len("#[quiz]"):].strip():
                problems.append(f"line {n}: #[quiz] step has no title")
        elif line.startswith("# "):
            current = {"line": n, "quiz": False, "questions": []}
            steps.append(current)
        elif line.startswith("## "):
            if current is None:
                problems.append(f"line {n}: '##' before any step heading")
            elif not current["quiz"]:
                problems.append(
                    f"line {n}: '##' inside a non-quiz step reads as a question "
                    f"but is not one — use bold text or make the step a #[quiz]"
                )
            else:
                current["questions"].append({"line": n, "options": []})
        elif re.match(r"\s*- \[( |x)\]", line):
            if current is None or not current["quiz"]:
                problems.append(f"line {n}: option checkbox outside a quiz step")
            elif not current["questions"]:
                problems.append(f"line {n}: option before any '##' question")
            else:
                current["questions"][-1]["options"].append(
                    "x" in re.match(r"\s*- \[( |x)\]", line).group(0)
                )
        elif line.startswith("#") and not line.startswith("#!"):
            # `###` and deeper have no meaning in this format and usually mean
            # the author reached for ordinary Markdown structure by habit.
            problems.append(f"line {n}: heading level not used by Workshopy: {line[:40]!r}")

    if not steps:
        problems.append("no steps at all — the file needs top-level '#' headings")
    if len(steps) > MAX_STEPS:
        problems.append(f"{len(steps)} steps; more than {MAX_STEPS} will not fit a 45-minute session")
    if len(steps) < MIN_STEPS:
        problems.append(f"only {len(steps)} steps")
    if len(quiz_steps) < MIN_QUIZZES:
        problems.append(f"{len(quiz_steps)} quiz steps; at least {MIN_QUIZZES} expected")

    for q in quiz_steps:
        if not q["questions"]:
            problems.append(f"line {q['line']}: quiz step with no '##' question")
        for question in q["questions"]:
            opts = question["options"]
            if len(opts) < 2:
                problems.append(f"line {question['line']}: question has {len(opts)} option(s)")
            if not any(opts):
                problems.append(
                    f"line {question['line']}: no option marked '- [x]' — every "
                    f"participant would be graded wrong"
                )
    return problems


def check_labels(files: list[pathlib.Path]) -> list[str]:
    """The landing page prints "N steps · M questions" under each kit.

    Those numbers were first written from the plan for each kit rather than
    counted from the finished file, and three of six were wrong by the time
    the files settled (#1100). A facilitator budgeting a 45-minute slot uses
    exactly these numbers, on a page whose whole argument is that the file is
    the source of truth.
    """
    page = ROOT / "facilitator-kits" / "index.html"
    if not page.is_file():
        return []
    html = page.read_text(encoding="utf-8")
    problems = []

    for path in files:
        lines = path.read_text(encoding="utf-8").split("\n")
        steps = sum(1 for l in lines if l.startswith("# ") or l.startswith("#[quiz]"))
        questions = sum(1 for l in lines if l.startswith("## "))

        m = re.search(
            r'href="/facilitator-kits/' + re.escape(path.name) + r'".*?'
            r'<p class="who-line">(\d+) steps &middot; (\d+) questions',
            html, re.S)
        if not m:
            problems.append(f"{path.name}: no 'N steps · M questions' label on the kits page")
            continue
        said_steps, said_qs = int(m.group(1)), int(m.group(2))
        if said_steps != steps:
            problems.append(f"{path.name}: page says {said_steps} steps, file has {steps}")
        if said_qs != questions:
            problems.append(f"{path.name}: page says {said_qs} questions, file has {questions}")
    return problems


def main() -> int:
    if not KITS.is_dir():
        print("PASS - no facilitator-kits/ directory")
        return 0

    files = sorted(KITS.glob("*.md"))
    if not files:
        print("FAIL - facilitator-kits/ exists but holds no .md kit")
        return 1

    failed = 0
    for path in files:
        problems = check(path)
        if problems:
            failed += 1
            print(f"FAIL - {path.relative_to(ROOT)}")
            for p in problems:
                print(f"    {p}")

    if failed:
        print(f"\n{failed} of {len(files)} kit(s) are not valid Workshopy Markdown.")
        print("Format: '# ' starts a step, '#[quiz] Title' makes it a graded quiz,")
        print("'##' inside a quiz is a question, '- [ ]' / '- [x]' are its options.")
        return 1

    label_problems = check_labels(files)
    if label_problems:
        print("FAIL - the kits page describes files that say something else:\n")
        for lp in label_problems:
            print(f"  {lp}")
        print("\nThe landing page states a step and question count per kit. Derive them")
        print("from the files rather than from the plan the kit was written to. See #1100.")
        return 1

    steps = sum(len([l for l in p.read_text().split("\n")
                     if l.startswith("# ") or l.startswith("#[quiz]")]) for p in files)
    print(f"PASS - {len(files)} facilitator kit(s) valid, {steps} steps total, "
          f"and the kits page agrees with all {len(files)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

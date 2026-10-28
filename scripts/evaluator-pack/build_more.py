#!/usr/bin/env python3
"""Build the fifteen further Evaluator's Desk templates and lint them.

    python3 scripts/evaluator-pack/build_more.py OUT_DIR [module ...]

Each module t_*.py defines PAGE (the listing data) and either SPEC (a Word pack, built by
spec_build) or build(out_dir) (an Excel pack that also writes its zip). Exits 1 on a lint hit.
"""
import importlib
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build import doc_text, lint, xlsx_text  # noqa: E402
from spec_build import build_doc  # noqa: E402

MODULES = [
    "t_clarify", "t_options", "t_charter", "t_status", "t_evidence",
    "t_storyline", "t_workshop", "t_aar", "t_feedback", "t_casestudy",
    "t_invoice", "t_workplan", "t_raid", "t_prioritise", "t_response",
]


def load(names=None):
    out = []
    for n in names or MODULES:
        try:
            out.append(importlib.import_module(n))
        except ModuleNotFoundError as e:
            if e.name != n:
                raise
    return out


def main(out, names):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    problems = []
    built = []
    for m in load(names or None):
        if hasattr(m, "SPEC"):
            p = out / m.SPEC["file"]
            build_doc(m.SPEC, p)
            problems += lint(p.name, doc_text(p))
            built.append(p.name)
        else:
            files = m.build(out)
            for f in files:
                p = out / f
                if f.endswith(".docx"):
                    problems += lint(f, doc_text(p))
                elif f.endswith(".xlsx"):
                    problems += lint(f, xlsx_text(p))
            built.append(m.PAGE["file"])
    for p in problems:
        print("LINT", *p, sep=" | ")
    print(f"built {len(built)} products into {out}; {len(problems)} lint hits")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2:]))

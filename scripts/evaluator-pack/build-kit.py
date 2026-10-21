#!/usr/bin/env python3
"""Build the upgraded Evaluation Essentials Kit zip: the delivered 27-product kit plus the Evaluator's Desk files.

    python3 scripts/evaluator-pack/build-kit.py CURRENT_KIT.zip BUILD_DIR OUT.zip

CURRENT_KIT.zip is the file now in the private `products` bucket (32 files). BUILD_DIR is the
output of build.py. OUT.zip has 35 files for 30 products. Nothing is uploaded here.
Refuses to run while any added file still carries a [LEGAL CHECK] note.
"""
import re
import sys
import zipfile
from pathlib import Path

from docx import Document

ADD = [
    "ImpactMojo-SOW-Change-Request-Template.docx",
    "ImpactMojo-Inception-Report-Template.docx",
    "ImpactMojo-Bid-No-Bid-Scorecard.xlsx",
    "ImpactMojo-Bid-No-Bid-Scorecard-GUIDE.docx",
]


def has_legal_note(path):
    if not path.name.endswith(".docx"):
        return False
    d = Document(str(path))
    texts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for r in t.rows:
            texts += [c.text for c in r.cells]
    return any("[LEGAL CHECK" in x for x in texts)


def main(current, build, out):
    build = Path(build)
    held = [f for f in ADD if has_legal_note(build / f)]
    if held and "--force" not in sys.argv:
        print("REFUSED: these files still carry [LEGAL CHECK] notes:", *held, sep="\n  ")
        return 1
    with zipfile.ZipFile(current) as src, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as dst:
        names = set()
        for i in src.infolist():
            dst.writestr(i, src.read(i.filename))
            names.add(i.filename)
        for f in ADD:
            if f in names:
                raise SystemExit(f"{f} is already in the kit")
            dst.write(build / f, f)
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        print(len(z.namelist()), "files in", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(*[a for a in sys.argv[1:] if not a.startswith("--")]))

#!/usr/bin/env python3
"""Every buy button names a product the order handler can deliver.

A buy page posts the product's title to the `product-order` Netlify form, and
netlify/functions/submission-created.mjs looks that title up in FILES to find
the file to send. On 2026-10-05 the em-dash sweep rewrote the FILES keys
("…Learning, Course Notes") and not the titles the pages send ("…Learning —
Course Notes"), so 41 of 62 buy buttons stopped resolving. The first buyer
after that, on 2026-10-10, paid ₹350 and got nothing but an email to the
owner saying "Unknown product … Deliver manually".

The handler now matches titles with case and punctuation ignored. This check
holds the other half: every product value on a page must resolve to a FILES
entry under that same normalisation, unless it is listed in MANUAL with the
reason it has no file. A stale MANUAL entry fails too.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDLER = ROOT / "netlify" / "functions" / "submission-created.mjs"

# Products sold through the same form that are fulfilled by hand by design,
# or whose file is not yet in the storage bucket. Title (without the price)
# -> reason.
MANUAL = {
    "AI for ME Certificate Track": "an enrolment, fulfilled by hand",
    "Data & Technology Assessed Track": "an enrolment, fulfilled by hand",
    "MEL Assessed Track": "an enrolment, fulfilled by hand",
    "Policy & Economics Assessed Track": "an enrolment, fulfilled by hand",
    "Verified Credential Upgrade": "an enrolment, fulfilled by hand",
    "12A, 12AB & 80G — Tax Exemption for NGOs, Annotated": "no PDF in the products bucket yet (checked 2026-10-10)",
    "Labour Laws for NGOs, Annotated": "no PDF in the products bucket yet (checked 2026-10-10)",
}


def norm(t):
    # The same rule as norm() in the handler: entities dropped, then
    # everything that is not a letter or digit.
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"&(?:amp|#x?[0-9a-f]+|[a-z]+);", "", t.lower()))


def strip_price(t):
    return re.sub(r"\s*\(₹.*$", "", t).strip()


def main():
    src = HANDLER.read_text(encoding="utf-8")
    block = src[src.index("const FILES"):src.index("};", src.index("const FILES"))]
    keys = {norm(k) for k in re.findall(r'^\s*"((?:[^"\\]|\\.)*)":\s*"[^"]+",?\s*$', block, re.M)}
    if "fileFor(title)" not in src:
        print("FAIL — the handler no longer looks titles up through fileFor()")
        sys.exit(1)

    manual = {norm(k): k for k in MANUAL}
    used, errors, seen = set(), [], 0
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("Backups/", "node_modules/")):
            continue
        s = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'name="product"\s+value="([^"]*)"|value="([^"]*)"\s+name="product"', s):
            title = strip_price(next(g for g in m.groups() if g is not None))
            seen += 1
            n = norm(title)
            if n in keys:
                continue
            if n in manual:
                used.add(n)
                continue
            errors.append("%s: \"%s\" matches no file in the order handler" % (rel, title))
    stale = [manual[n] for n in manual if n not in used]
    if errors or stale:
        print("FAIL — buy buttons the order handler cannot deliver")
        for e in errors:
            print("  " + e)
        for t in stale:
            print("  stale MANUAL entry: %s" % t)
        sys.exit(1)
    print("PASS — %d buy buttons, each resolves to a deliverable file or a documented manual product (%d)" % (seen, len(MANUAL)))


if __name__ == "__main__":
    main()

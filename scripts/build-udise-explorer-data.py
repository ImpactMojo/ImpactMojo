#!/usr/bin/env python3
"""Build the inline data block of udise.html.

    python3 scripts/build-udise-explorer-data.py --extract EXISTING.pdf NEP.pdf
        reads the two UDISE+ 2025-26 booklets and writes data/udise-2025-26.json
    python3 scripts/build-udise-explorer-data.py           # writes the page
    python3 scripts/build-udise-explorer-data.py --check   # fails if the page is stale

Sources. The two booklets are published by the Ministry of Education on the
UDISE+ dashboard (https://dashboard.udiseplus.gov.in/report2026/), one in the
older stage structure (primary, upper primary, secondary) and one in the NEP
2020 structure (foundational, preparatory, middle, secondary). The facility
counts (Table 2.5) are the same in both and are read from the first. Pupil
teacher ratios, the secondary GER, dropout and the GPI of GER are read from the
NEP booklet, because the 2024-25 figures this page held before matched the NEP
tables and not the older ones (the 2024-25 All-India PTR of 13, 17 and 21 is
the NEP preparatory, middle and secondary figure; the older primary PTR is 20).

data/udise-base.json holds what the page showed before the 2025-26 update: the
2021-22 and 2024-25 figures for states, districts and All-India, read from the
UDISE+ open-data service. District figures for 2025-26 are served only by the
UDISE+ API (api.udiseplus.gov.in), which could not be reached when this was
built, so the district view stays on 2024-25 and says so.

Checks run on extract, and again on every build:
  * every count column of Table 2.5: the states and UTs add up to the India row;
  * every state and UT in the base file is found exactly once in every table;
  * the All-India facility shares recomputed from the counts.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "udise.html"
BASE = ROOT / "data" / "udise-base.json"
NEW = ROOT / "data" / "udise-2025-26.json"
SLOT = re.compile(r'(<script>\nwindow\.UDISE_DATA=)(\{.*?\})(;?\n</script>)', re.S)

FAC = ["elec", "water", "gtoilet", "handwash", "library", "playground", "ramp", "computer", "internet"]
PTR = ["ptr_pry", "ptr_upry", "ptr_sec"]

# Table 2.5 columns (numbered as printed): the facility each page key reads.
T25 = {"nsch": 2, "library": 3, "playground": 4, "gtoilet": 8, "elec": 11,
       "computer": 15, "internet": 17, "water": 19, "handwash": 20, "ramp": 23}


def norm(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z]+", " ", s)
    s = re.sub(r"\band\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def code_for(name, names):
    k = norm(name)
    if re.search(r"\b(daman|dadra)\b", k):
        k = "dadra nagar haveli daman diu"
    for c, n in names.items():
        if norm(n) == k:
            return c
    return None


def rows_of(text, title, ncols, names):
    """Rows of the first table whose title line contains `title`.

    A row is a state name followed by numbers. A name that wraps onto a line
    of its own before its numbers is joined to them."""
    lines = text.split("\n")
    # the contents page carries the same title with dot leaders and a page number
    start = next(i for i, l in enumerate(lines)
                 if title in l and "....." not in l and not re.search(r"\.\s*\d+\s*$", l))
    out, pending, i = {}, "", start + 1
    while i < len(lines) and len(out) < len(names) + 1:
        l = lines[i]
        i += 1
        if re.match(r"\s*\(1\)", l) or not l.strip():
            continue
        m = re.match(r"\s*([A-Za-z&.,' ()-]*?)\s*(-?\d[\d.]*(?:\s+-?\d[\d.]*)*)\s*$", l)
        if not m:
            pending = (pending + " " + l.strip()).strip()
            continue
        name = m.group(1).strip()
        # a wrapped name: the start on a line of its own, the rest (or nothing) beside the numbers
        if pending and norm(name) != "india" and (not name or code_for(name, names) is None):
            name = (pending + " " + name).strip()
        pending = ""
        nums = [float(x) for x in m.group(2).split()]
        if len(nums) != ncols:
            raise SystemExit("%s: row %r has %d numbers, expected %d" % (title, name, len(nums), ncols))
        c = "IN" if norm(name) == "india" else code_for(name, names)
        if c is None:
            raise SystemExit("%s: unknown row name %r" % (title, name))
        if c in out:
            raise SystemExit("%s: %r appears twice" % (title, name))
        out[c] = nums
    missing = set(names) - set(out)
    if missing or "IN" not in out:
        raise SystemExit("%s: missing rows %s" % (title, sorted(missing)))
    return out


def pdftext(p):
    return subprocess.run(["pdftotext", "-layout", str(p), "-"], check=True, capture_output=True, text=True).stdout


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def extract(existing_pdf, nep_pdf):
    base = json.loads(BASE.read_text())
    names = {c: s["n"] for c, s in base["states"].items()}
    ex, nep = pdftext(existing_pdf), pdftext(nep_pdf)
    a = rows_of(ex, "Table 2.5: State wise highlights of the UDISE+ 2025-26", 12, names)
    b = rows_of(ex, "Table 2.5 (continued): State wise highlights of the UDISE+ 2025-26", 12, names)
    t25 = {c: a[c] + b[c][1:] for c in a}          # columns 2-13, then 15-25 (14 repeats 2)
    for c in t25:
        if a[c][0] != b[c][0]:
            raise SystemExit("Table 2.5: total schools differ between the two halves for %s" % c)
    ptr = rows_of(nep, "Table 4.12: Pupil Teacher Ratio (PTR) by level of school education, 2025-26", 4, names)
    ger = rows_of(nep, "Table 6.1: Gross Enrolment Ratio (GER) by Gender and Level of School Education, 2025-26: All", 12, names)
    gpi = rows_of(nep, "Table 6.7: Gender Parity Index (GPI) of GER by Level of School Education, 2025-26", 4, names)
    drop = rows_of(nep, "Table 6.11: Dropout Rate by level of education and gender, 2025-26", 9, names)

    def col(row, n):  # printed column number n of Table 2.5 (columns 2-13 then 15-25)
        return row[n - 2] if n <= 13 else row[n - 3]

    out = {}
    for c in list(names) + ["IN"]:
        r = t25[c]
        out[c] = {"counts": {k: int(col(r, n)) for k, n in T25.items()},
                  "ptr_pry": ptr[c][1], "ptr_upry": ptr[c][2], "ptr_sec": ptr[c][3],
                  "ger_sec": ger[c][11], "gpi_mid": gpi[c][2],
                  "drop_upry": drop[c][5], "drop_sec": drop[c][8]}
    doc = {
        "source": "UDISE+ 2025-26 booklets, Department of School Education and Literacy, Ministry of Education",
        "files": {
            "existing": {"url": "https://dashboard.udiseplus.gov.in/report2026/static/media/UDISE%2B" + Path(existing_pdf).name,
                         "sha256": sha(existing_pdf), "tables": ["2.5"]},
            "nep": {"url": "https://dashboard.udiseplus.gov.in/report2026/static/media/UDISE%2B" + Path(nep_pdf).name,
                    "sha256": sha(nep_pdf), "tables": ["4.12", "6.1", "6.7", "6.11"]},
        },
        "notes": "ptr_pry, ptr_upry and ptr_sec are the NEP preparatory (3-5), middle (6-8) and secondary (9-12) PTR; "
                 "ger_sec is the NEP secondary (9-12) GER, total; gpi_mid is the GPI of GER at the middle stage (6-8); "
                 "drop_upry and drop_sec are the NEP middle and secondary dropout rates, total.",
        "rows": out,
    }
    check_new(doc, names)
    NEW.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print("wrote", NEW.relative_to(ROOT))


def check_new(doc, names):
    rows = doc["rows"]
    for k in T25:
        tot = sum(rows[c]["counts"][k] for c in names)
        if tot != rows["IN"]["counts"][k]:
            raise SystemExit("Table 2.5 %s: states add to %d, India row is %d" % (k, tot, rows["IN"]["counts"][k]))
    for c in list(names) + ["IN"]:
        cn = rows[c]["counts"]
        for k in FAC:
            if cn[k] > cn["nsch"]:
                raise SystemExit("%s: more schools with %s than schools" % (c, k))


def pct(n, d):
    return round(100.0 * n / d, 1)


def build():
    base = json.loads(BASE.read_text())
    new = json.loads(NEW.read_text())
    names = {c: s["n"] for c, s in base["states"].items()}
    check_new(new, names)

    def cur(r):
        cn = r["counts"]
        d = {k: pct(cn[k], cn["nsch"]) for k in FAC}
        d["nsch"] = cn["nsch"]
        for k in PTR + ["ger_sec", "gpi_mid", "drop_upry", "drop_sec"]:
            d[k] = r[k]
        return d

    def y24(old):  # the 2024-25 state figures the district view is read against
        return {k: old[k] for k in FAC + PTR + ["nsch"] if k in old}

    states = {}
    for c, s in base["states"].items():
        states[c] = {"n": s["n"], "cur": cur(new["rows"][c]), "prev": s["prev"], "d24": y24(s["cur"])}
    nat = {"cur": cur(new["rows"]["IN"]), "prev": base["national"]["prev"], "d24": y24(base["national"]["cur"])}
    meta = {"src": "UDISE+ 2025-26 (and 2021-22; districts 2024-25), Department of School Education & Literacy, Ministry of Education",
            "y0": "2021-22", "y1": "2025-26", "yd": "2024-25", "hist": True}
    return {"meta": meta, "states": states, "districts": base["districts"], "national": nat}


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--extract":
        extract(sys.argv[2], sys.argv[3])
        return
    check = "--check" in sys.argv
    data = build()
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    page = PAGE.read_text()
    m = SLOT.search(page)
    if not m:
        raise SystemExit("udise.html: data slot not found")
    if check:
        if m.group(2) != blob:
            raise SystemExit("FAIL: udise.html data block is stale; run scripts/build-udise-explorer-data.py")
        print("PASS")
        return
    PAGE.write_text(page[:m.start(2)] + blob + page[m.end(2):])
    print("wrote udise.html")


if __name__ == "__main__":
    main()

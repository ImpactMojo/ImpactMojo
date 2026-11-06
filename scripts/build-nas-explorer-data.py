#!/usr/bin/env python3
"""PARAKH Rashtriya Sarvekshan 2024 state averages for the separate section of nas.html.

    python3 scripts/build-nas-explorer-data.py --extract DIR   # DIR holds the 36 state report PDFs
    python3 scripts/build-nas-explorer-data.py                 # writes the PRS block into nas.html
    python3 scripts/build-nas-explorer-data.py --check         # fails if the page is stale

The NAS 2021 data on the page is not touched. PARAKH Rashtriya Sarvekshan 2024
tested Classes 3, 6 and 9 in all school types; NAS 2021 tested Classes 3, 5, 8
and 10 in government and aided schools. The two are kept apart and never joined.

Source: the state and UT reports NCERT published at
https://parakh.ncert.gov.in/prs-reports-2024-statelist/ (files under
/media/public_files/2025-08/). Each report opens every grade with a chart,
"Comparison of State Average with National Average Across Subjects" (UT
reports say "UT Average"), giving the average percentage of questions answered
correctly, as whole numbers, for the state and for India.

Checks, on extract and on every build:
  * all 36 states and UTs are present, each with 2, 3 and 4 subjects at Classes 3, 6 and 9;
  * the national figure printed beside each state is the same in all 36 reports;
  * every gap the report states in words ("the performance gap is 5% in
    Language ...") equals the difference between the two printed averages.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "nas.html"
DATA = ROOT / "data" / "parakh-2024-states.json"
SLOT = re.compile(r'(<script>\nwindow\.PRS_DATA=)(\{.*?\})(;\n</script>)', re.S)
LIST = "https://parakh.ncert.gov.in/prs-reports-2024-statelist/"
BASE_URL = "https://parakh.ncert.gov.in/media/public_files/2025-08/"

SUBJ = {"3": ["lang", "math"], "6": ["lang", "math", "wau"], "9": ["lang", "math", "sci", "ssc"]}
WORD = {"Language": "lang", "Mathematics": "math", "The World Around Us": "wau",
        "Science": "sci", "Social Science": "ssc"}


def parse(pdf):
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True,
                          capture_output=True, text=True).stdout
    m = re.search(r"(?:State|UT) Report:\s*([^\n]+?)\s*$", text, re.M)
    name = m.group(1).strip() if m else None
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines)
           if re.search(r"Comparison of (State|UT) Average with National Average", l)]
    if len(idx) != 3:
        raise SystemExit("%s: found %d comparison charts, expected 3" % (pdf.name, len(idx)))
    out, gaps = {}, {}
    for g, i in zip(("3", "6", "9"), idx):
        vals, j = [], i + 1
        while "National" not in lines[j]:
            vals += [int(x) for x in re.findall(r"(\d+)%", lines[j])]
            j += 1
        subs = SUBJ[g]
        if len(vals) != 2 * len(subs):
            raise SystemExit("%s Class %s: %d figures, expected %d" % (pdf.name, g, len(vals), 2 * len(subs)))
        out[g] = {s: {"state": vals[2 * k], "india": vals[2 * k + 1]} for k, s in enumerate(subs)}
        # the sentence under the chart, up to the page number
        para = " ".join(l.strip() for l in lines[j + 1:j + 40] if not re.fullmatch(r"\s*\d+\s*", l))
        para = para.split("GRADE")[0]
        m = re.search(r"(?:difference|gap) is (.*?)(?:\.|$)", para)
        if m:
            gaps[g] = [(int(n), WORD.get(w)) for n, w in
                       re.findall(r"(\d+)% in (The World Around Us|Social Science|Language|Mathematics|Science)", m.group(1))]
    return name, out, gaps


def check(doc):
    st = doc["states"]
    if len(st) != 36:
        raise SystemExit("expected 36 states and UTs, found %d" % len(st))
    nat = doc["india"]
    for n, s in st.items():
        for g, subs in SUBJ.items():
            for k in subs:
                if s[g][k]["india"] != nat[g][k]:
                    raise SystemExit("%s Class %s %s: national figure %s differs from %s"
                                     % (n, g, k, s[g][k]["india"], nat[g][k]))
        for g, pairs in s.get("gaps", {}).items():
            for gap, k in pairs:
                d = abs(s[g][k]["state"] - s[g][k]["india"])
                if gap != d:
                    raise SystemExit("%s Class %s %s: report says a gap of %d, the chart gives %d" % (n, g, k, gap, d))


def extract(folder):
    states, nat = {}, None
    files = sorted(Path(folder).glob("*.pdf"))
    for f in files:
        name, out, gaps = parse(f)
        if not name:
            raise SystemExit("%s: no state name" % f.name)
        row = {g: out[g] for g in SUBJ}
        row["gaps"] = {g: v for g, v in gaps.items() if v}
        row["file"] = BASE_URL + "PRS%202024%20" + f.name.replace(" ", "%20").replace("&", "%26")
        row["sha256"] = hashlib.sha256(f.read_bytes()).hexdigest()
        states[name] = row
        if nat is None:
            nat = {g: {k: out[g][k]["india"] for k in SUBJ[g]} for g in SUBJ}
    doc = {"source": "PARAKH Rashtriya Sarvekshan 2024, state and UT reports, NCERT (2025)",
           "list": LIST,
           "measure": "Average percentage of questions answered correctly, as printed (whole numbers)",
           "india": nat, "states": states}
    check(doc)
    DATA.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print("wrote", DATA.relative_to(ROOT), len(states), "states and UTs")


def blob():
    doc = json.loads(DATA.read_text())
    check(doc)
    st = {n: {g: {k: v["state"] for k, v in s[g].items()} for g in SUBJ} for n, s in doc["states"].items()}
    return json.dumps({"india": doc["india"], "states": st}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--extract":
        extract(sys.argv[2])
        return
    page = PAGE.read_text()
    m = SLOT.search(page)
    if not m:
        raise SystemExit("nas.html: PRS data slot not found")
    b = blob()
    if "--check" in sys.argv:
        if m.group(2) != b:
            raise SystemExit("FAIL: nas.html PRS block is stale; run scripts/build-nas-explorer-data.py")
        print("PASS")
        return
    PAGE.write_text(page[:m.start(2)] + b + page[m.end(2):])
    print("wrote nas.html")


if __name__ == "__main__":
    main()

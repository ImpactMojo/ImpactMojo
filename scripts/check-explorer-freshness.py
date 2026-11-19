#!/usr/bin/env python3
"""Which data explorers are due for a refresh?

data/explorer-freshness.json lists every data explorer with the date its
figures were last pulled from the source. Each explorer is a hand-built
snapshot, so nothing refreshes it: the only way anyone learns a source has
published something newer is that somebody looks. This script says which
explorers are past their review interval, and which have no retrieval date
recorded at all.

    python3 scripts/check-explorer-freshness.py            # validate the manifest; PASS or FAIL
    python3 scripts/check-explorer-freshness.py --report explorer-freshness
                                                           # also write <name>.md and <name>.json

Validation fails (exit 1) only on a manifest that is wrong: a missing page or
data file, a malformed date, or a retrieved date that disagrees with the date
the data file records for itself. Being overdue is not a failure; it is what
the weekly workflow turns into an issue.
"""
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "explorer-freshness.json"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_KEYS = re.compile(r"(^|_)(fetched|retrieved)$")


def parse(s):
    return dt.date.fromisoformat(s)


def own_dates(node, found=None):
    """Every retrieved or fetched date the data file records for itself."""
    found = [] if found is None else found
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and DATE_KEYS.search(k) and re.match(r"\d{4}-\d{2}-\d{2}", v):
                found.append(v[:10])
            elif isinstance(v, (dict, list)) and k not in ("rows", "records", "facilities", "S", "V", "I", "G"):
                own_dates(v, found)
    elif isinstance(node, list):
        for x in node[:50]:
            own_dates(x, found)
    return found


def load():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["explorers"]


def validate(rows):
    errs = []
    seen = set()
    for e in rows:
        i = e["id"]
        if i in seen:
            errs.append("%s: listed twice" % i)
        seen.add(i)
        for k in ("page", "data_file"):
            if not (ROOT / e[k]).is_file():
                errs.append("%s: %s %s does not exist" % (i, k, e[k]))
        for k in ("retrieved", "as_of_date"):
            if e.get(k) is not None and not DATE.match(e[k]):
                errs.append("%s: %s is not YYYY-MM-DD" % (i, k))
        if e.get("as_of_date") and not e.get("as_of_label"):
            errs.append("%s: as_of_date needs an as_of_label" % i)
        if not isinstance(e.get("review_every_days"), int) or e["review_every_days"] < 7:
            errs.append("%s: review_every_days must be a whole number of days, 7 or more" % i)
        f = ROOT / e["data_file"]
        if f.is_file() and f.suffix == ".json":
            own = own_dates(json.loads(f.read_text(encoding="utf-8")))
            if own and e.get("retrieved") != max(own):
                errs.append("%s: manifest retrieved is %s, the data file's own latest date is %s"
                            % (i, e.get("retrieved"), max(own)))
    return errs


def status(rows, today):
    out = []
    for e in rows:
        if e.get("retrieved") is None:
            out.append((e, "no-date", None, None))
            continue
        age = (today - parse(e["retrieved"])).days
        due = parse(e["retrieved"]) + dt.timedelta(days=e["review_every_days"])
        out.append((e, "overdue" if today > due else "ok", age, due))
    return out


def report(rows, today):
    st = status(rows, today)
    overdue = [s for s in st if s[1] == "overdue"]
    nodate = [s for s in st if s[1] == "no-date"]
    L = ["# Data explorers due for a check", "",
         "As of %s: %d explorers, %d past their review interval, %d with no retrieval date recorded." %
         (today.isoformat(), len(rows), len(overdue), len(nodate)), ""]
    if overdue:
        L += ["## Past their review interval", "", "| Explorer | Retrieved | Age | Was due | What to check |", "|---|---|---|---|---|"]
        for e, _, age, due in sorted(overdue, key=lambda s: -s[2]):
            L.append("| [%s](https://www.impactmojo.in/%s) | %s | %d days | %s | %s |" %
                     (e["id"], e["page"], e["retrieved"], age, due.isoformat(), e["check"]))
        L.append("")
    if nodate:
        L += ["## No retrieval date recorded", "",
              "These cannot be aged. Record the date the figures were pulled in the data file and in `data/explorer-freshness.json`.", ""]
        for e, *_ in nodate:
            L.append("- `%s` (%s): %s" % (e["id"], e["data_file"], e["check"]))
        L.append("")
    L.append("Nothing here is refreshed automatically: an unattended script would publish unchecked figures. Rebuild the explorer from its source, then update its date.")
    return "\n".join(L) + "\n", {"overdue": len(overdue), "no_date": len(nodate), "total": len(rows)}


def main():
    rows = load()
    errs = validate(rows)
    if errs:
        print("FAIL - explorer freshness manifest is wrong:")
        for e in errs:
            print("  " + e)
        return 1
    today = dt.date.today()
    md, tally = report(rows, today)
    if "--report" in sys.argv:
        name = sys.argv[sys.argv.index("--report") + 1]
        pathlib.Path(name + ".md").write_text(md, encoding="utf-8")
        pathlib.Path(name + ".json").write_text(json.dumps({"tally": tally}), encoding="utf-8")
    print("PASS - %d explorers listed; %d past their interval, %d with no date recorded" %
          (tally["total"], tally["overdue"], tally["no_date"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

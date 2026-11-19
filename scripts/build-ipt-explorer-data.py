#!/usr/bin/env python3
"""India Persecution Tracker explorer: the data file and its checks.

    python3 scripts/build-ipt-explorer-data.py --extract DIR   # rewrite data/ipt-india.json
    python3 scripts/build-ipt-explorer-data.py                 # CI: validate the data and the page that loads it

data/ipt-india.json is a navigation and analysis layer over the South Asia
Justice Campaign's India Persecution Tracker (southasiajusticecampaign.org),
four editions: 2025 (annual), 2025 July-September, 2026 January-April and
2026 May-July. It is not a republication. Each record is one source-linked
sentence from an edition, kept to 240 characters, credited, and linked to the
news report SAJC cites and to the edition it came from. The explorer never
claims the records are complete: SAJC says its own are not.

--extract reads a folder holding the four saved editions (ipt2025.html,
ipt2025-3.html, ipt2026-1.html, ipt2026-2.html) and, in maps/, the map files
those editions embed (killings_map_2026-Q1_v5.html, killings_map_2026-Q2_v1.html,
demolitions_map_2026-Q1_v1.html, demolitions_map_2026-Q2_v1.html,
violence_choropleth_2026-Q1_v1.html, IPT_anticonversion-map_v2.html).

Decisions that are easy to undo by accident:

  - The tab titles on SAJC's pages do not line up with the panels beside them
    (the nested State/Non-state tabs shift every index), so each panel is
    assigned its section from what it says, in PANELS below, edition by edition.
  - A record's date is set only when the sentence carries a day and a month
    that fall inside the edition's own window. Anything else is null. A date is
    never guessed from the paragraph around it.
  - States are read from the sentence by name, with a short list of cities for
    the places SAJC writes without a state. A sentence naming several states
    keeps all of them, in order of appearance.
  - A sentence about sexual violence or a minor is kept as a record but its
    excerpt is withheld (EXCERPT_WITHHELD), so the explorer never republishes
    the wording of such an account. The count and the link stay.
  - Counts shown on the page are counted from the records. SAJC's own headline
    figures are quoted as text where the explorer shows them, never recomputed.
"""
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "ipt-india.json"
PAGE = ROOT / "ipt.html"
SLOT = re.compile(r'(<script id="ipt-data" type="application/json">)(.*?)(</script>)', re.S)
BASE = "https://southasiajusticecampaign.org/"

EDITIONS = {
    "ipt2025": dict(id="ipt2025", label="2025 annual", start="2025-01-01", end="2025-12-31"),
    "ipt2025-3": dict(id="ipt2025-3", label="2025 July to September", start="2025-07-01", end="2025-09-30"),
    "ipt2026-1": dict(id="ipt2026-1", label="2026 January to April", start="2026-01-01", end="2026-04-30"),
    "ipt2026-2": dict(id="ipt2026-2", label="2026 May to July", start="2026-05-01", end="2026-07-31"),
}

# (panel index) -> (section, actor). Read off the first paragraph of every panel.
SECTIONS = {
    "life": "Deprivation of life", "arrests": "Arrests and detention", "torture": "Torture and ill-treatment",
    "disenfranchisement": "Disenfranchisement and denationalisation", "expulsions": "Forced expulsions and refoulement",
    "hate": "Advocacy of religious hatred", "freedom": "Religious freedom",
    "discrimination": "Discrimination in economic, social and cultural rights", "civic": "Civic space and democratic backsliding",
    "remedy": "Lack of effective remedy", "overview": "Overview", "mixed": "Rights, civic space and discrimination",
}
PANELS = {
    "ipt2026-2": {0: ("overview", None), 2: ("life", "state"), 3: ("life", "non-state"), 4: ("arrests", None),
                  6: ("torture", "state"), 7: ("torture", "non-state"), 8: ("disenfranchisement", None),
                  9: ("expulsions", None), 10: ("hate", None), 11: ("freedom", None), 12: ("discrimination", None),
                  13: ("civic", None), 14: ("remedy", None)},
    "ipt2026-1": {0: ("overview", None), 2: ("life", "state"), 3: ("life", "non-state"), 4: ("arrests", None),
                  6: ("torture", "state"), 7: ("torture", "non-state"), 8: ("disenfranchisement", None),
                  9: ("expulsions", None), 10: ("hate", None), 11: ("freedom", None), 12: ("discrimination", None),
                  13: ("civic", None), 14: ("remedy", None)},
    "ipt2025-3": {0: ("overview", None), 2: ("life", "state"), 3: ("life", "non-state"), 4: ("arrests", None),
                  6: ("torture", "state"), 7: ("torture", "non-state"), 8: ("expulsions", None), 9: ("hate", None),
                  10: ("freedom", None), 11: ("disenfranchisement", None), 12: ("discrimination", None),
                  13: ("remedy", None), 14: ("civic", None)},
    "ipt2025": {0: ("overview", None), 2: ("life", "state"), 3: ("life", "non-state"), 4: ("arrests", None),
                6: ("torture", "state"), 7: ("torture", "non-state"), 8: ("expulsions", None), 9: ("hate", None),
                10: ("mixed", None), 11: ("remedy", None)},
}

STATES = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
          "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
          "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
          "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi", "Jammu & Kashmir", "Ladakh",
          "Chandigarh", "Puducherry", "Andaman & Nicobar Islands", "Lakshadweep", "Dadra & Nagar Haveli and Daman & Diu"]
ALIASES = {
    "Orissa": "Odisha", "Jammu and Kashmir": "Jammu & Kashmir", "Jammu & Kashmir": "Jammu & Kashmir",
    "Kashmir": "Jammu & Kashmir", "J&K": "Jammu & Kashmir", "NCT of Delhi": "Delhi", "New Delhi": "Delhi",
    "Andaman and Nicobar": "Andaman & Nicobar Islands", "Bengal": "West Bengal",
    "Ghaziabad": "Uttar Pradesh", "Meerut": "Uttar Pradesh", "Aligarh": "Uttar Pradesh", "Lucknow": "Uttar Pradesh",
    "Sambhal": "Uttar Pradesh", "Bareilly": "Uttar Pradesh", "Noida": "Uttar Pradesh", "Muzaffarnagar": "Uttar Pradesh",
    "Kolkata": "West Bengal", "Murshidabad": "West Bengal", "Mumbai": "Maharashtra", "Pune": "Maharashtra",
    "Guwahati": "Assam", "Goalpara": "Assam", "Nagaon": "Assam", "Hyderabad": "Telangana", "Bengaluru": "Karnataka",
    "Mangaluru": "Karnataka", "Ahmedabad": "Gujarat", "Surat": "Gujarat", "Jaipur": "Rajasthan", "Bhopal": "Madhya Pradesh",
    "Indore": "Madhya Pradesh", "Ujjain": "Madhya Pradesh", "Dehradun": "Uttarakhand", "Patna": "Bihar",
    "Srinagar": "Jammu & Kashmir", "Gurugram": "Haryana", "Nuh": "Haryana", "Raipur": "Chhattisgarh", "Ranchi": "Jharkhand",
}
NAME_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(sorted(map(re.escape, list(STATES) + list(ALIASES)), key=len, reverse=True)) + r")(?![A-Za-z])")

MONTHS = {m: i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])}
DATE_RE = re.compile(r"\b(\d{1,2})(?:\s*(?:-|–|and)\s*\d{1,2})?\s+(" + "|".join(MONTHS) + r")(?:\s+(\d{4}))?\b")
URL_MARK = re.compile(r"⟦(https?://[^⟧]+)⟧")
SENSITIVE_WORDS = re.compile(r"\b(rape|raped|gang-?rape|sexual(?:ly)?|molest\w*|minor|minors|girl|girls|schoolgirl|boy|boys|schoolboy|child|children|infant|toddler|teenager|teenagers|teen|juvenile)\b", re.I)
AGE_RE = re.compile(r"\b(\d{1,2})[- ]year[- ]old\b|\b(?:aged|age)\s+(\d{1,2})\b|,\s*(\d{1,2}),", re.I)


def sensitive(text):
    """Sexual violence, or anyone under 18. An adult's age ("a 27-year-old") does not count."""
    if SENSITIVE_WORDS.search(text):
        return True
    for m in AGE_RE.finditer(text):
        a = next((g for g in m.groups() if g), None)
        if a and int(a) < 18:
            return True
    return False
EXCERPT_WITHHELD = "Excerpt withheld: the account involves sexual violence or a child. Read it at the source."
MAX_EXCERPT = 240
# India's outer bounding box, for the map records.
LAT0, LAT1, LON0, LON1 = 6.0, 37.6, 67.5, 98.0


def clean_html(x):
    x = re.sub(r'<a [^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', lambda m: m.group(2) + " ⟦" + html.unescape(m.group(1)) + "⟧", x, flags=re.S)
    x = re.sub(r"<[^>]+>", "", x)
    return html.unescape(re.sub(r"\s+", " ", x)).strip()


def panels_of(text):
    starts = [m.start() for m in re.finditer(r'class="wp-block-kadence-tab kt-tab-inner-content ', text)]
    out = []
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else text.find("</footer>", s)
        seg = text[s:e]
        paras = [clean_html(p) for p in re.findall(r"<(?:p|li)[^>]*>(.*?)</(?:p|li)>", seg, flags=re.S)]
        out.append([p for p in paras if p])
    return out


def sentences(par):
    # A source marker belongs to the sentence it follows, so split after the marker.
    par = re.sub(r"(⟦[^⟧]+⟧)([.,;:]?)", r"\1\2", par)
    par = re.sub(r"(?<=[a-z0-9)’”])\.(?=[A-Z])", ". ", par)
    parts = re.split(r"(?<=[.!?])(?:\s*⟦[^⟧]+⟧)?\s+(?=[A-Z‘“'\"(])", par)
    return [p.strip() for p in parts if p.strip()]


def date_of(sentence, ed):
    m = DATE_RE.search(sentence)
    if not m:
        return None
    day, mon = int(m.group(1)), MONTHS[m.group(2)]
    year = int(m.group(3)) if m.group(3) else int(ed["start"][:4])
    try:
        iso = "%04d-%02d-%02d" % (year, mon, day)
    except Exception:
        return None
    return iso if ed["start"] <= iso <= ed["end"] else None


def states_of(sentence):
    seen = []
    for m in NAME_RE.finditer(sentence):
        s = ALIASES.get(m.group(1), m.group(1))
        if s not in seen:
            seen.append(s)
    return seen


def tidy_dashes(text):
    """House style: no em dash. A spaced or unspaced dash becomes a comma."""
    return re.sub(r"\s*\u2014\s*", ", ", text)


def excerpt_of(sentence):
    plain = re.sub(r"\s*⟦[^⟧]+⟧", "", sentence).strip()
    if sensitive(plain):
        return None, True
    plain = tidy_dashes(plain)
    if len(plain) > MAX_EXCERPT:
        cut = plain[:MAX_EXCERPT].rsplit(" ", 1)[0].rstrip(",;:")
        plain = cut + "…"
    return plain, False


def extract_editions(folder):
    recs, counts = [], {}
    for eid, ed in EDITIONS.items():
        text = (folder / (eid + ".html")).read_text(encoding="utf-8")
        panels = panels_of(text)
        n_panels = 0
        for idx, (sec, actor) in PANELS[eid].items():
            if sec == "overview" or idx >= len(panels):
                continue
            n_panels += 1
            for par in panels[idx]:
                for sent in sentences(par):
                    urls = URL_MARK.findall(sent)
                    if not urls:
                        continue
                    ex, withheld = excerpt_of(sent)
                    recs.append({
                        "edition": eid, "section": sec, "actor": actor,
                        "date": date_of(sent, ed), "states": states_of(sent),
                        "excerpt": ex, "withheld": withheld, "sources": list(dict.fromkeys(urls)),
                    })
        counts[eid] = n_panels
    # one record per (edition, section, first source, excerpt)
    seen, out = set(), []
    for r in recs:
        key = (r["edition"], r["section"], r["sources"][0], (r["excerpt"] or "")[:60])
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    for i, r in enumerate(out, 1):
        r["id"] = i
    return out


def json_after(s, name):
    m = re.search(r"(?:const|var|let)\s+" + name + r"\s*=\s*([\[{])", s)
    if not m:
        raise SystemExit("no %s in map file" % name)
    i = m.start(1)
    opener, closer = s[i], "]" if s[i] == "[" else "}"
    depth = 0
    for j in range(i, len(s)):
        if s[j] == opener:
            depth += 1
        elif s[j] == closer:
            depth -= 1
            if depth == 0:
                return s[i:j + 1]
    raise SystemExit("unterminated %s" % name)


def extract_maps(folder):
    killings, demolitions = [], []
    for q, ed in (("2026-Q1_v5", "ipt2026-1"), ("2026-Q2_v1", "ipt2026-2")):
        s = (folder / "maps" / ("killings_map_%s.html" % q)).read_text(encoding="utf-8")
        for r in json.loads(json_after(s, "incidents")):
            m_, d, y = r["Date"].split("/")
            summ = None if sensitive(r["Details"]) else r["Details"]
            killings.append({"edition": ed, "date": "%s-%s-%s" % (y, m_, d), "place": r["Location"], "state": r["State"],
                             "lat": float(r["LAT"]), "lon": float(r["LON"]), "victims": int(r["Victims"]),
                             "actor": "state" if r["Category"].lower().startswith("state") else "non-state",
                             "summary": summ})
    for q, ed in (("2026-Q1_v1", "ipt2026-1"), ("2026-Q2_v1", "ipt2026-2")):
        s = (folder / "maps" / ("demolitions_map_%s.html" % q)).read_text(encoding="utf-8")
        for r in json.loads(json_after(s, "incidents")):
            iso = r["date"] if re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["date"]) else None
            demolitions.append({"edition": ed, "date": iso, "date_text": None if iso else r["date"], "place": r["loc"], "state": r["state"],
                                "lat": float(r["lat"]), "lon": float(r["lon"]), "type": r["type"], "kind": r["cat"],
                                "summary": None if sensitive(r["summary"]) else r["summary"]})
    s = (folder / "maps" / "IPT_anticonversion-map_v2.html").read_text(encoding="utf-8")
    raw = json_after(s, "stateData")
    laws = []
    for m in re.finditer(r"'([^']+)':\s*\{\s*status:\s*'([^']*)',\s*law:\s*'((?:[^'\\]|\\.)*)',\s*year:\s*(\d+|null)", raw):
        laws.append({"state": m.group(1), "status": m.group(2), "law": m.group(3).replace("\\'", "'"),
                     "year": None if m.group(4) == "null" else int(m.group(4))})
    return killings, demolitions, laws


def extract(folder):
    folder = Path(folder)
    recs = extract_editions(folder)
    k, d, laws = extract_maps(folder)
    data = {
        "meta": {
            "source": "South Asia Justice Campaign, India Persecution Tracker",
            "source_url": BASE,
            "editions": [dict(EDITIONS[e], url="%s%s/" % (BASE, e)) for e in EDITIONS],
            "note": "Each record is one source-linked sentence from an edition, shortened to 240 characters and credited. "
                    "The editions say their own record is not exhaustive. Counts here are counts of these records.",
            "retrieved": "2026-11-19",
        },
        "records": recs, "killings": k, "demolitions": d, "anticonversion": laws,
        "map": json.loads((ROOT / "data" / "datacentres-india.json").read_text(encoding="utf-8"))["map"],
    }
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("wrote %s: %d records, %d killings, %d demolitions, %d anti-conversion rows" % (DATA.name, len(recs), len(k), len(d), len(laws)))


def validate(data):
    errs = []
    eds = {e["id"]: e for e in data["meta"]["editions"]}
    ids = [r["id"] for r in data["records"]]
    if len(ids) != len(set(ids)):
        errs.append("record ids repeat")
    for r in data["records"]:
        e = eds.get(r["edition"])
        if not e:
            errs.append("record %s names an unknown edition" % r["id"]); continue
        if r["section"] not in SECTIONS:
            errs.append("record %s has an unknown section %r" % (r["id"], r["section"]))
        if not r["sources"] or not all(u.startswith("https://") or u.startswith("http://") for u in r["sources"]):
            errs.append("record %s has no usable source address" % r["id"])
        if r["date"] and not (e["start"] <= r["date"] <= e["end"]):
            errs.append("record %s is dated %s, outside its edition" % (r["id"], r["date"]))
        if r["excerpt"] and "\u2014" in r["excerpt"]:
            errs.append("record %s excerpt carries an em dash" % r["id"])
        if r["excerpt"] is not None and len(r["excerpt"]) > MAX_EXCERPT + 1:
            errs.append("record %s excerpt is over the length limit" % r["id"])
        if r["excerpt"] is not None and sensitive(r["excerpt"]):
            errs.append("record %s carries an excerpt that should be withheld" % r["id"])
        if r["withheld"] != (r["excerpt"] is None):
            errs.append("record %s: withheld flag and excerpt disagree" % r["id"])
        for s in r["states"]:
            if s not in STATES:
                errs.append("record %s names %r, not a state or union territory" % (r["id"], s))
    for kind in ("killings", "demolitions"):
        for r in data[kind]:
            if not (LAT0 <= r["lat"] <= LAT1 and LON0 <= r["lon"] <= LON1):
                errs.append("%s record %s/%s sits outside India" % (kind, r["date"] or r.get("date_text"), r["place"]))
            if r["edition"] not in eds:
                errs.append("%s record names an unknown edition" % kind)
            if r["date"] and not (eds[r["edition"]]["start"] <= r["date"] <= eds[r["edition"]]["end"]):
                errs.append("%s record %s is outside its edition" % (kind, r["date"]))
    if any(r["victims"] < 1 for r in data["killings"]):
        errs.append("a killing record has no victims")
    ed_counts = Counter(r["edition"] for r in data["records"])
    for e in eds:
        if ed_counts[e] < 30:
            errs.append("edition %s holds only %d records; the parser has lost a panel" % (e, ed_counts[e]))
    return errs


def render_block(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def main():
    args = sys.argv[1:]
    if args[:1] == ["--extract"]:
        extract(args[1]); return
    data = json.loads(DATA.read_text(encoding="utf-8"))
    errs = validate(data)
    if errs:
        print("FAIL - IPT explorer data")
        for e in errs[:25]:
            print("  " + e)
        sys.exit(1)
    if not PAGE.exists():
        print("PASS - IPT data valid (%d records); ipt.html not written yet" % len(data["records"])); return
    page = PAGE.read_text(encoding="utf-8")
    problems = []
    if "fetch('/data/ipt-india.json')" not in page:
        problems.append("ipt.html does not load data/ipt-india.json")
    title = re.search(r"<title>(.*?)</title>", page, re.S).group(1)
    n = "{:,}".format(len(data["records"]))
    if n not in title:
        problems.append("the page title says a record count other than %s" % n)
    hk, hd = str(len(data["killings"])), str(len(data["demolitions"]))
    if 'id="hK">%s<' % hk not in page or 'id="hD">%s<' % hd not in page:
        problems.append("the static map counts in the header differ from the data (%s killings, %s demolitions)" % (hk, hd))
    if 'id="hN">%s<' % n not in page:
        problems.append("the static record count in the header differs from the data")
    if problems:
        print("FAIL - ipt.html")
        for p_ in problems:
            print("  " + p_)
        sys.exit(1)
    print("PASS - IPT explorer data is current (%d records, %d killings, %d demolitions)" % (len(data["records"]), len(data["killings"]), len(data["demolitions"])))


if __name__ == "__main__":
    main()

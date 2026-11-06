#!/usr/bin/env python3
"""Snapshot the MCA CSR series from data.gov.in into data/csr-india.json.

Why a snapshot and not a live call: data.gov.in caps the shared public key at
10 records per request and rate-limits it hard, so a page calling the API at
render time would be slow, flaky, and dependent on a key we do not control.
Every other explorer on the site ships its data in the repo; this does the same.

Re-run to refresh. Set DATA_GOV_KEY to use your own key (free registration at
data.gov.in) instead of the shared demo key.

Sources, all Ministry of Corporate Affairs via data.gov.in:
  state  - State/UT-wise CSR Expenditure, 2018-19 to 2022-23
  sector - Development Sector-wise CSR Expenditure, 2018-19 to 2022-23

Two later sources, each written into its own series so a refresh of one never
touches another:

  --ls-pdf PATH   Lok Sabha Unstarred Question 161, answered 20 July 2026, by
                  the Ministry of Corporate Affairs. Annexure I is State/UT-wise
                  and Annexure II Development Sector-wise CSR expenditure for
                  2020-21 to 2024-25, from the ministry's Corporate Data
                  Management Cell, "updated data up to March 31, 2026". This is
                  the newest table the ministry has published in a form that can
                  be fetched: data.gov.in stops at 2022-23, and the export on
                  mcacdm.nic.in/csr-data sits behind a CAPTCHA. The PDF's
                  SHA-256 is pinned, and every column is checked against the
                  printed Total row before anything is written.
                    https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU161_1zCBRl.pdf?source=lsapps
  --mospi-nsdp    Per capita NSDP at current prices (MoSPI National Accounts,
                  base 2011-12, indicator 25) for 2023-24 and 2024-25, which
                  data.gov.in does not carry. The host needs
                  OP_LEGACY_SERVER_CONNECT. --mospi-nsdp-json PATH loads rows
                  already pulled from the same API (as a list of
                  {state, year, per_capita_nsdp_current}).

With no flag the script refreshes the data.gov.in series only.
"""
import hashlib
import re
import ssl
import urllib.parse
import urllib.request
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "csr-india.json"
KEY = os.environ.get(
    "DATA_GOV_KEY",
    "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b",  # public demo key
)

RESOURCES = {
    "state": ("80f3abf8-7c91-4966-a37f-8c7b0aae92e9",
              "State/UT-wise Details of CSR Expenditure from 2018-19 to 2022-23"),
    "sector": ("40ca3289-b33c-4f60-b8fe-c5050d8e27fa",
               "Development Sector-wise Details of CSR Expenditure from 2018-19 to 2022-23"),
    # Denominator for the per-person view. Census 2011 is the most recent
    # enumerated population India has -- the 2021 census has not been held --
    # so per-person figures are CSR now over people counted then, and the page
    # says so rather than burying it.
    "population": ("cd3f9ecd-0bc3-406a-bb7d-8562ffb75083",
                   "State/UT-wise Population, Decadal Growth Rate and Density, Census 2011"),
    # The wealth axis. Per-capita NSDP covers 33 states and reaches 2022-23,
    # matching the CSR series; the per-capita GSDP table covers only 28.
    # Carries literal "NA" strings for unpublished cells -- not zero.
    "nsdp": ("c9bfd3c0-b9de-4a5b-8752-f72a4f2932ad",
             "State/UT-wise Per Capita Net State Domestic Product at Current Prices"),
}

PAGE = 10          # the shared key's hard cap
MAX_TRIES = 6


def get(url):
    """One request, with backoff on the rate limiter.

    Shells out to curl deliberately: this environment routes outbound HTTPS
    through an agent proxy that curl is configured for and urllib is not, so
    urllib times out where curl succeeds.
    """
    delay = 5
    for attempt in range(MAX_TRIES):
        try:
            out = subprocess.run(
                ["curl", "-s", "--max-time", "45", url],
                capture_output=True, text=True, check=True,
            ).stdout
            body = json.loads(out)
        except Exception:
            if attempt == MAX_TRIES - 1:
                raise
            time.sleep(delay)
            delay *= 2
            continue
        if isinstance(body, dict) and body.get("error"):
            if attempt == MAX_TRIES - 1:
                raise RuntimeError(body["error"])
            time.sleep(delay)
            delay *= 2
            continue
        return body
    raise RuntimeError("unreachable")


def fetch_all(rid):
    rows, offset, total = [], 0, None
    while True:
        url = (f"https://api.data.gov.in/resource/{rid}"
               f"?api-key={KEY}&format=json&limit={PAGE}&offset={offset}")
        body = get(url)
        total = body.get("total", 0)
        batch = body.get("records", [])
        rows.extend(batch)
        print(f"    {len(rows)}/{total}", flush=True)
        if not batch or len(rows) >= total:
            break
        offset += PAGE
        time.sleep(2)          # stay under the limiter
    if total is not None and len(rows) != total:
        raise RuntimeError(f"expected {total} rows, got {len(rows)}")
    return rows


LS_URL = ("https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/"
          "AU161_1zCBRl.pdf?source=lsapps")
LS_SHA256 = "6d4cac0d50df1bcde29d298cf6e344442b4d8cf3ba2c26cfdbb498601ab53309"
LS_YEARS = ["2020_21", "2021_22", "2022_23", "2023_24", "2024_25"]
NUM = re.compile(r"^(?:-|\d{1,3}(?:,\d{3})*\.\d{2})$")


def ls_value(tok):
    """'-' is how the table prints a cell with nothing in it. It stays null."""
    return None if tok == "-" else float(tok.replace(",", ""))


def ls_table(lines, first_col_numbered):
    """Rows of a pdftotext -layout table: a label followed by five numbers.

    Long sector names wrap: the first line carries the start of the name and
    no numbers, the next carries the rest of the name and the five numbers,
    or the other way round. Text with no numbers is held and joined to the
    next numbered row.
    """
    rows, pending = [], ""
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        toks = line.split()
        tail = []
        while toks and NUM.match(toks[-1]) and len(tail) < 5:
            tail.insert(0, toks.pop())
        label = " ".join(toks)
        label = re.sub(r"^\d+\.?\s+", "", label) if first_col_numbered else label
        if len(tail) == 5:
            name = (pending + " " + label).strip() if label else pending.strip()
            if not label and rows and not pending:
                raise SystemExit(f"FAIL - numbers with no label: {raw!r}")
            rows.append((name, [ls_value(t) for t in tail]))
            pending = ""
        elif tail:
            raise SystemExit(f"FAIL - a row with {len(tail)} numbers, expected 5: {raw!r}")
        else:
            if rows and not pending and not re.match(r"^\d+\.?\s", line) and first_col_numbered is False:
                # continuation of the previous sector name, printed under it
                n, v = rows[-1]
                rows[-1] = (n + " " + label, v)
            else:
                pending = (pending + " " + label).strip()
    return rows


def parse_ls_pdf(path):
    data = Path(path).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != LS_SHA256:
        raise SystemExit(f"FAIL - {path} has SHA-256 {digest}, expected {LS_SHA256}. "
                         "The ministry may have replaced the file; read it before trusting it.")
    text = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                          capture_output=True, text=True, check=True).stdout
    a1 = text.index("State/UT-wise -wise CSR expenditure")
    a2 = text.index("Development Sector-wise CSR expenditure")
    a3 = text.index("Annexure-III", a2)

    def body(chunk, start_marker):
        lines = chunk.splitlines()
        # The column header is the line carrying the first two years.
        i = next(k for k, l in enumerate(lines)
                 if start_marker in l and "2021-22" in l)
        out = []
        for l in lines[i + 1:]:
            if "Updated data up to" in l:
                break
            out.append(l)
        return out

    state_lines = [l for l in body(text[a1:a2], "2020-21") if "Annexure" not in l]
    sector_lines = [l for l in body(text[a2:a3], "2020-21") if "Annexure" not in l]

    def rows_of(lines, label_key):
        out, total = [], None
        for name, vals in ls_table(lines, True):
            name = re.sub(r"\s+", " ", name).strip()
            rec = {label_key: name}
            rec.update({f"csr_expenditure_{y}": v for y, v in zip(LS_YEARS, vals)})
            if name.lower() == "total":
                total = rec
            out.append(rec)
        if total is None:
            raise SystemExit("FAIL - no Total row in the table")
        for y in LS_YEARS:
            col = f"csr_expenditure_{y}"
            parts = sum(r[col] or 0 for r in out if r is not total)
            if abs(parts - total[col]) > 0.5:
                raise SystemExit(f"FAIL - {label_key} {y}: rows add to {parts:.2f}, "
                                 f"the Total row prints {total[col]:.2f}")
        return out

    state = rows_of(state_lines, "state_ut")
    sector = rows_of(sector_lines, "development_sector")
    if len(state) != 41 or len(sector) != 30:
        raise SystemExit(f"FAIL - expected 40 states/rows plus Total and 29 sectors plus Total; "
                         f"got {len(state)} and {len(sector)}")
    for y in LS_YEARS:
        col = f"csr_expenditure_{y}"
        if state[-1][col] != sector[-1][col]:
            raise SystemExit(f"FAIL - {y}: the two annexures print different totals")
    meta = {
        "source": ("Ministry of Corporate Affairs, reply to Lok Sabha Unstarred Question "
                   "No. 161, answered 20 July 2026, Annexures I and II. Corporate Data "
                   "Management Cell, updated data up to 31 March 2026."),
        "url": LS_URL,
        "sha256": digest,
        "retrieved": time.strftime("%Y-%m-%d"),
    }
    return (dict(meta, title="State/UT-wise CSR expenditure, 2020-21 to 2024-25", rows=state),
            dict(meta, title="Development Sector-wise CSR expenditure, 2020-21 to 2024-25",
                 rows=sector))


MOSPI = "https://api.mospi.gov.in/api/nas/getNasData"


def fetch_mospi_nsdp(years=("2023-24", "2024-25")):
    ctx = ssl.create_default_context()
    ctx.options |= 0x4          # OP_LEGACY_SERVER_CONNECT; the host needs it
    rows = []
    for y in years:
        q = dict(base_year="2011-12", series="Current", frequency_code="Annually",
                 indicator_code=25, year=y, page=1, limit=100, Format="JSON",
                 state_code=",".join("%02d" % i for i in range(1, 38)))
        u = MOSPI + "?" + urllib.parse.urlencode(q)
        body = json.load(urllib.request.urlopen(u, context=ctx, timeout=60))
        for r in body.get("data", []):
            rows.append({"state": r["state"], "year": r["year"],
                         "per_capita_nsdp_current": num_or_none(r["current_price"])})
    return rows


def num_or_none(x):
    try:
        return float(str(x).replace(",", ""))
    except ValueError:
        return None


def nsdp_series(rows):
    return {
        "source": ("MoSPI, National Accounts Statistics, state series, Per Capita Net "
                   "State Domestic Product at current prices, base year 2011-12 "
                   "(api.mospi.gov.in, indicator 25)"),
        "retrieved": time.strftime("%Y-%m-%d"),
        "rows": rows,
    }


def main():
    if "--ls-pdf" in sys.argv or "--mospi-nsdp" in sys.argv or "--mospi-nsdp-json" in sys.argv:
        cur = json.loads(OUT.read_text(encoding="utf-8"))
        if "--ls-pdf" in sys.argv:
            st, se = parse_ls_pdf(sys.argv[sys.argv.index("--ls-pdf") + 1])
            cur["series"]["ls_state"], cur["series"]["ls_sector"] = st, se
            print(f"  ls_state {len(st['rows'])} rows, ls_sector {len(se['rows'])} rows")
        if "--mospi-nsdp-json" in sys.argv:
            rows = json.loads(Path(sys.argv[sys.argv.index("--mospi-nsdp-json") + 1])
                              .read_text(encoding="utf-8"))
            cur["series"]["nsdp_mospi"] = nsdp_series(rows)
        elif "--mospi-nsdp" in sys.argv:
            cur["series"]["nsdp_mospi"] = nsdp_series(fetch_mospi_nsdp())
        OUT.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)}")
        return 0
    out = {
        "_source": "Ministry of Corporate Affairs, via data.gov.in (Open Government Data Platform)",
        "_licence": "Government Open Data Licence - India",
        "_note": ("CSR expenditure in rupees crore. Snapshot -- refresh with "
                  "scripts/fetch-csr-data.py. The 2021-22 and 2022-23 columns are the "
                  "most recent the MCA series publishes at State/UT level."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "series": {},
    }
    for name, (rid, title) in RESOURCES.items():
        print(f"  {name}: {title}")
        rows = fetch_all(rid)
        out["series"][name] = {"resource_id": rid, "title": title, "rows": rows}
    # Keep the series that come from other sources.
    if OUT.exists():
        for k, v in json.loads(OUT.read_text(encoding="utf-8"))["series"].items():
            out["series"].setdefault(k, v)

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    for k, v in out["series"].items():
        print(f"  {k:12s} {len(v['rows']):>4} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Is each Dataverse resource still there?

    python3 scripts/check-dataverse-links.py                 # print a summary
    python3 scripts/check-dataverse-links.py --report out    # also write out.json and out.md
    python3 scripts/check-dataverse-links.py --fail-on-broken

data/dataverse.json holds 335 resources and nothing read their addresses until
this script: the daily crawl in link-check.yml reads only *.html and *.md, and
the Dataverse page fetches this JSON in the browser, so its links never appear
in a file the crawl sees.

Each address lands in exactly one bucket:

  ok       the final answer is 2xx (after redirects)
  broken   404 or 410, or the host name does not exist. Only this bucket is
           treated as dead.
  blocked  401, 403, 429, 451, 999: the site refuses an automated client. These
           usually open fine in a browser, and calling them dead would send
           someone to remove a live resource.
  unknown  timeouts, TLS or connection errors, 5xx, and 202 (a bot-challenge
           page that says nothing about the resource). Worth a look when it
           repeats; not evidence of removal.

A non-ok answer is retried once, with a GET if the first try was a HEAD. The
same rule is used by development-discourses' verify_urls.py, which learned it
when 102 of 162 "failures" were 403s that all opened in a browser.

Entries with status "coming-soon" and addresses on this site are skipped. An
address a person types is never trusted: only http(s) is followed.
"""
import argparse
import concurrent.futures as cf
import json
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; ImpactMojoLinkCheck/1.0; +https://www.impactmojo.in/)"
BLOCKED = {401, 403, 429, 451, 999}
DEAD = {404, 410}


def classify_code(code):
    if 200 <= code < 300 and code != 202:
        return "ok"
    if code in DEAD:
        return "broken"
    if code in BLOCKED:
        return "blocked"
    return "unknown"


def one_try(url, method, timeout):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return classify_code(r.status), r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return classify_code(e.code), e.code, url
    except urllib.error.URLError as e:
        reason = e.reason
        if isinstance(reason, socket.gaierror) and reason.errno in (socket.EAI_NONAME, -2):
            return "broken", "dns", url
        if isinstance(reason, (socket.timeout, TimeoutError)):
            return "unknown", "timeout", url
        if isinstance(reason, ssl.SSLError):
            return "unknown", "tls", url
        return "unknown", type(reason).__name__, url
    except (socket.timeout, TimeoutError):
        return "unknown", "timeout", url
    except Exception as e:  # never let one address stop the run
        return "unknown", type(e).__name__, url


def check(url, timeout=20):
    result = one_try(url, "HEAD", timeout)
    if result[0] != "ok":
        result = one_try(url, "GET", timeout)
    if result[0] in ("unknown",):
        time.sleep(1)
        result = one_try(url, "GET", timeout)
    return {"bucket": result[0], "code": result[1], "final_url": result[2]}


def entries():
    dv = json.loads((ROOT / "data" / "dataverse.json").read_text(encoding="utf-8"))
    for c in dv["categories"]:
        for i in c["items"]:
            yield c["name"], i


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", help="write <path>.json and <path>.md")
    ap.add_argument("--fail-on-broken", action="store_true")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--only", help="comma-separated entry ids, for a spot check")
    args = ap.parse_args()

    only = set(args.only.split(",")) if args.only else None
    todo = []
    for cat, i in entries():
        u = i.get("url", "")
        if only and i["id"] not in only:
            continue
        if i.get("status") == "coming-soon":
            continue
        if urllib.parse.urlparse(u).scheme not in ("http", "https"):
            continue
        if urllib.parse.urlparse(u).netloc.endswith("impactmojo.in"):
            continue
        todo.append((cat, i))

    rows = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(check, i["url"], args.timeout): (cat, i) for cat, i in todo}
        for f in cf.as_completed(futs):
            cat, i = futs[f]
            r = f.result()
            rows.append({"id": i["id"], "name": i["name"], "category": cat, "url": i["url"], **r})
    rows.sort(key=lambda r: (r["bucket"], r["id"]))
    tally = {b: sum(1 for r in rows if r["bucket"] == b) for b in ("ok", "broken", "blocked", "unknown")}

    lines = ["# Dataverse link check", "",
             "Checked %d external resources. ok %d, broken %d, blocked %d, unknown %d." % (
                 len(rows), tally["ok"], tally["broken"], tally["blocked"], tally["unknown"]), ""]
    if tally["broken"]:
        lines += ["## Broken (404, 410 or no such host)", ""]
        lines += ["- `%s` %s: %s (%s)" % (r["id"], r["name"], r["url"], r["code"]) for r in rows if r["bucket"] == "broken"]
        lines.append("")
    lines += ["Blocked (%d) and unknown (%d) are not counted as dead: blocked sites refuse automated clients and "
              "usually open in a browser; unknown covers timeouts and certificate errors." % (tally["blocked"], tally["unknown"])]
    unk = [r for r in rows if r["bucket"] == "unknown"]
    if unk:
        lines += ["", "## Unknown, for a second look", ""]
        lines += ["- `%s` %s (%s)" % (r["id"], r["url"], r["code"]) for r in unk]
    md = "\n".join(lines) + "\n"

    print(md if len(rows) <= 40 or tally["broken"] else md.split("\n\n## Unknown")[0])
    if args.report:
        Path(args.report + ".json").write_text(json.dumps({"tally": tally, "rows": rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        Path(args.report + ".md").write_text(md, encoding="utf-8")
    sys.exit(1 if (args.fail_on_broken and tally["broken"]) else 0)


if __name__ == "__main__":
    main()

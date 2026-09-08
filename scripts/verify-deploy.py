#!/usr/bin/env python3
"""Post-merge deploy verifier with build-hook fallback.

Why this exists: on 2026-07-19 the v10.141.0 merge to main never triggered a
Netlify production build — deploy previews built, production silently stayed
on the previous release. Netlify's git webhook can occasionally drop a push
event; nothing errors, the site just doesn't update.

What it does:
  1. Resolves the expected commit (origin/main HEAD by default).
  2. Polls the Netlify API for a production-context deploy of that commit.
  3. If none has even STARTED after --grace seconds, POSTs /builds to trigger
     one manually (the fallback), then keeps polling. If that POST is refused
     it says so, retries a few times, and names the status code in the final
     line -- see "On a refused trigger" below.
  4. Exits 0 once the production deploy for the expected commit is "ready";
     exits 1 on timeout or build error.

On a refused trigger
--------------------
This used to print `build triggered: None` and carry on. Netlify answers a
refused POST with a JSON error body, so `b.get("id")` was None and the line
read like a success with a missing field; the run then ended on the generic
"no ready production deploy within Ns", which is also what a merely slow build
looks like. On 2026-09-07 Netlify's API and its GitHub integration were down
together for ten hours: the merge never built, the fallback POST returned 404
every time, and that was legible nowhere. The run was read as a defect in this
script and a bug was filed against it (#1074).

So a refused trigger is now loud at the moment it happens, retried up to
MAX_TRIGGER_ATTEMPTS times rather than once, and named in the closing line
with its status code, which points at Netlify instead of at us.

Usage (after merging a PR):
    set -a; . .claude/.env.keys 2>/dev/null; set +a
    python3 scripts/verify-deploy.py            # defaults: grace 120s, timeout 600s
    python3 scripts/verify-deploy.py --grace 60 --timeout 900

Requires $NETLIFY_PAT. Uses curl (urllib is blocked by the sandbox proxy).
"""

import argparse
import json
import os
import subprocess
import sys
import time

SITE_ID = "f9e879bf-4792-42aa-96ea-c3a3b396f8b8"
API = f"https://api.netlify.com/api/v1/sites/{SITE_ID}"

# A refused trigger is retried rather than spent on one shot, but not forever:
# if Netlify is refusing three times over 45 seconds it is down, and the run
# should end saying so rather than hammering the API for the whole timeout.
MAX_TRIGGER_ATTEMPTS = 3


def curl_json(url, method="GET", body=None):
    """Returns (http_status, parsed_body_or_None).

    The status is the point: without it a refused request is indistinguishable
    from a successful one that happened to carry no id. The body is parsed
    leniently because Netlify does not always answer in JSON -- a build hook
    refusal is the bare string "Not Found" -- and a json.JSONDecodeError here
    would take down a run whose actual job is to report that something failed.
    """
    cmd = ["curl", "-s", "-w", "\n%{http_code}", "-X", method, url,
           "-H", f"Authorization: Bearer {os.environ['NETLIFY_PAT']}"]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout
    raw, _, code = out.rpartition("\n")
    try:
        status = int(code.strip())
    except ValueError:
        status = 0
    try:
        return status, (json.loads(raw) if raw.strip() else None)
    except json.JSONDecodeError:
        return status, None


def expected_sha():
    subprocess.run(["git", "fetch", "-q", "origin", "main"], check=False)
    return subprocess.run(["git", "rev-parse", "origin/main"],
                          capture_output=True, text=True, check=True).stdout.strip()


def production_deploy_for(sha):
    _, deploys = curl_json(f"{API}/deploys?per_page=15")
    deploys = deploys or []
    for d in deploys:
        if d.get("context") == "production" and (d.get("commit_ref") or "").startswith(sha[:12]):
            return d
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grace", type=int, default=120,
                    help="seconds to wait for Netlify to start the build on its own")
    ap.add_argument("--timeout", type=int, default=600,
                    help="total seconds before giving up")
    ap.add_argument("--sha", help="expected commit (default: origin/main HEAD)")
    args = ap.parse_args()

    if not os.environ.get("NETLIFY_PAT"):
        print("ERROR: NETLIFY_PAT not set (load .claude/.env.keys first)")
        return 1

    sha = args.sha or expected_sha()
    print(f"expecting production deploy of {sha[:12]}")

    start = time.time()
    triggered = False
    trigger_attempts = 0
    last_trigger_status = None
    while time.time() - start < args.timeout:
        d = production_deploy_for(sha)
        if d:
            state = d.get("state")
            if state == "ready":
                print(f"PASS — production deploy ready ({d.get('id')})")
                return 0
            if state == "error":
                print(f"FAIL — production build errored: {d.get('error_message')}")
                return 1
            print(f"  building… ({state})")
        elif not triggered and trigger_attempts < MAX_TRIGGER_ATTEMPTS \
                and time.time() - start >= args.grace:
            # webhook never fired — the fallback this script exists for
            trigger_attempts += 1
            print(f"no production build after {args.grace}s — triggering manually "
                  f"(webhook fallback, attempt {trigger_attempts}/{MAX_TRIGGER_ATTEMPTS})")
            status, b = curl_json(f"{API}/builds", method="POST", body={"clear_cache": False})
            last_trigger_status = status
            if 200 <= status < 300:
                print(f"  build triggered: {(b or {}).get('id')}")
                triggered = True
            else:
                # Not "triggered". Leaving the flag clear means the next poll
                # tries again, which is what you want for a transient refusal.
                msg = (b or {}).get("message") if isinstance(b, dict) else None
                print(f"  TRIGGER REFUSED — HTTP {status}"
                      f"{': ' + str(msg) if msg else ''}. Netlify has not been asked to build.")
        else:
            print("  waiting for Netlify to pick up the merge…")
        time.sleep(15)

    if trigger_attempts and not triggered:
        print(f"FAIL — no deploy of {sha[:12]}, and the manual trigger was refused "
              f"{trigger_attempts}x (last HTTP {last_trigger_status}), so Netlify was "
              f"never asked to build it. This is an API problem, not a slow build: "
              f"check status.netlify.com and the token's site permissions before "
              f"looking for a fault here.")
    else:
        print(f"FAIL — no ready production deploy of {sha[:12]} within {args.timeout}s")
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Copy the Supabase `products` bucket into the Drive mirror folder.

    SUPABASE_URL=... SUPABASE_SERVICE_KEY=... python3 scripts/mirror/mirror-to-drive.py OUT_DIR DRIVE_LISTING.json

Run by .github/workflows/mirror-to-drive.yml, which lists the Drive folder with rclone first.
This script decides what is missing or different, downloads only those objects into OUT_DIR
(same relative paths as the bucket) and writes OUT_DIR/.changed with one path per line.
The workflow then uploads OUT_DIR. Nothing is ever deleted from Drive. Objects under
`_backup-` are old copies kept on purpose and are not mirrored.

An object counts as already mirrored when Drive holds a file at that path with the same size
and, where Supabase gives an md5-shaped etag, the same md5.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BUCKET = "products"
URL = os.environ["SUPABASE_URL"].rstrip("/")
KEY = os.environ["SUPABASE_SERVICE_KEY"]
H = {"Authorization": f"Bearer {KEY}", "apikey": KEY}


def call(path, body=None, raw=False):
    req = urllib.request.Request(URL + path, headers={**H, **({"Content-Type": "application/json"} if body else {})},
                                 data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read() if raw else json.load(r)


def walk(prefix=""):
    """Every object under the prefix. A row with no `id` is a folder."""
    offset = 0
    while True:
        rows = call(f"/storage/v1/object/list/{BUCKET}", {"prefix": prefix, "limit": 100, "offset": offset,
                                                          "sortBy": {"column": "name", "order": "asc"}})
        for r in rows:
            path = f"{prefix}{r['name']}"
            if r.get("id") is None:
                yield from walk(path + "/")
            else:
                yield path, r.get("metadata") or {}
        if len(rows) < 100:
            return
        offset += 100


def main(out, listing):
    drive = {i["Path"]: i for i in json.load(open(listing)) if not i.get("IsDir")}
    out = Path(out)
    changed = []
    seen = 0
    for path, meta in walk():
        if path.startswith("_backup-"):
            continue
        seen += 1
        size = meta.get("size")
        etag = str(meta.get("eTag") or meta.get("etag") or "").strip('"')
        have = drive.get(path)
        if have and have.get("Size") == size:
            md5 = (have.get("Hashes") or {}).get("md5")
            if not (re.fullmatch(r"[0-9a-f]{32}", etag) and md5 and md5 != etag):
                continue
        dest = out / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(call(f"/storage/v1/object/authenticated/{BUCKET}/{urllib.parse.quote(path)}", raw=True))
        changed.append(path)
        print("download", path)
    (out / ".changed").write_text("\n".join(changed))
    print(f"{seen} objects in the bucket, {len(changed)} to upload")


if __name__ == "__main__":
    main(*sys.argv[1:3])

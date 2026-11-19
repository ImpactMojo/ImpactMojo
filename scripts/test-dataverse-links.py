#!/usr/bin/env python3
"""The link checker's bucketing, run against a local server that answers each
way a real site does. A checker that calls a 403 dead would send someone to
delete live resources, so every bucket is asserted, in both directions."""
import importlib.util
import socket
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

spec = importlib.util.spec_from_file_location("cdl", Path(__file__).with_name("check-dataverse-links.py"))
cdl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cdl)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _go(self):
        p = self.path
        if p == "/ok": self.send_response(200)
        elif p == "/gone": self.send_response(410)
        elif p == "/missing": self.send_response(404)
        elif p == "/blocked": self.send_response(403)
        elif p == "/throttled": self.send_response(429)
        elif p == "/oops": self.send_response(500)
        elif p == "/challenge": self.send_response(202)
        elif p == "/redir-ok": self.send_response(302); self.send_header("Location", "/ok")
        elif p == "/redir-dead": self.send_response(301); self.send_header("Location", "/missing")
        elif p == "/head-refused":
            if self.command == "HEAD": self.send_response(405)
            else: self.send_response(200)
        elif p == "/slow": time.sleep(3); self.send_response(200)
        else: self.send_response(404)
        self.send_header("Content-Length", "0"); self.end_headers()
    do_GET = _go
    do_HEAD = _go


srv = HTTPServer(("127.0.0.1", 0), H)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
B = "http://127.0.0.1:%d" % port
want = {
    "/ok": "ok", "/redir-ok": "ok", "/head-refused": "ok",
    "/missing": "broken", "/gone": "broken", "/redir-dead": "broken",
    "/blocked": "blocked", "/throttled": "blocked",
    "/oops": "unknown", "/challenge": "unknown",
}
bad = []
for path, bucket in want.items():
    got = cdl.check(B + path, timeout=5)["bucket"]
    if got != bucket: bad.append("%s: wanted %s, got %s" % (path, bucket, got))
if cdl.check(B + "/slow", timeout=1)["bucket"] != "unknown": bad.append("/slow (timeout) should be unknown")
# a name that cannot resolve is dead; the .invalid TLD is reserved never to resolve
r = cdl.check("http://no-such-host.invalid/", timeout=5)
if r["bucket"] not in ("broken", "unknown"): bad.append("dns failure: got %s" % r["bucket"])
srv.shutdown()
if bad:
    print("FAIL: Dataverse link checker"); [print("  " + b) for b in bad]; sys.exit(1)
print("PASS: Dataverse link checker buckets (%d cases)" % (len(want) + 2))

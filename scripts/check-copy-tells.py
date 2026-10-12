#!/usr/bin/env python3
"""Hold the line on the stock phrases the owner's house style bans.

On 2026-10-10 a sitewide pass rewrote about 220 sentences across 135 pages:
"isn't just X: it's Y", "genuinely", "arguably", "navigating the
complexities", "harnessing the power", "13 Comprehensive Modules" and the
rest. This check covers only phrases with no legitimate technical reading, so
it can fail on sight. Words such as "robust" (robust standard errors),
"transformative" (gender-transformative) and "paradigm" (research paradigms)
are deliberately not here: they are correct in statistics and methods
teaching, and a regex cannot tell those uses from filler.

Text is read from reader-facing HTML with scripts, styles and comments
removed. Quotations, titles of cited works, testimonials and lists of
phrases to avoid are legitimate, and are exempted one by one in EXEMPT with
the reason. A stale exemption fails too.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = ("Backups/", "node_modules/", "i18n/", "tests/", "mcp-server/", "admin/",
        "supabase/", "docs/")

PHRASES = [
    r"\bgenuinely\b",
    r"\barguably\b",
    r"\bisn['’]t just\b",
    r"\bis not just\b",
    r"\bnot just\b[^.;:]{1,80}?\bbut\b",
    r"\bnavigat(?:e|ing) the complexities\b",
    r"\bin today['’]s fast-paced\b",
    r"\bharness(?:ing)? the power\b",
    r"\bunlock(?:ing)? the (?:power|potential)\b",
    r"\ba stark reminder\b",
    r"\bplays? an? (?:vital|key|crucial|pivotal) role\b",
    r"\bComprehensive Modules\b",
    r"\bat the forefront\b",
    r"\bpave[sd]? the way\b",
    r"\bembark(?:s|ed|ing)? on a journey\b",
    # Added 2026-10-12 after the second sitewide pass: words and phrases with no
    # technical reading that now appear nowhere in reader-facing text.
    r"\bhonestly\b",
    r"\btruly\b",
    r"\bdelve[sd]?\b|\bdelving\b",
    r"\btapestry\b",
    r"\btestament\b",
    r"\bgroundbreaking\b",
    r"\bseamless(?:ly)?\b",
    r"\bunparalleled\b",
    r"\binvaluable\b",
    r"\bmeticulous(?:ly)?\b",
    r"\bcommendable\b",
    r"\bnoteworthy\b",
    r"\bnotably\b",
    r"\bvibrant\b",
    r"\bbustling\b",
    r"\bnestled\b",
    r"\bbreathtaking\b",
    r"\bcaptivating\b",
    r"\bplethora\b",
    r"\bmyriad\b",
    r"\bspearhead\w*",
    r"\blet['’]s (?:dive|unpack|break (?:this|it) down)\b",
    r"\bdive in\b",
    r"\bit['’]s worth noting\b|\bit is worth noting\b",
    r"\bneedless to say\b",
    r"\bwhen it comes to\b",
    r"\bat the intersection of\b",
    r"\bin an era of\b",
    r"\bever-evolving\b",
    r"\bshed(?:s|ding)? light on\b",
    r"\bgain valuable insights\b",
    r"\bdeeply rooted\b",
    r"\bwatershed moment\b",
    r"\benduring legacy\b",
    r"\bunleash\w*",
    r"\bgarner(?:s|ed|ing)\b",
    r"\bbolster\w*",
    r"\belucidat\w*",
]
RX = re.compile("|".join(PHRASES), re.I)

# (path, phrase as it appears) -> reason
EXEMPT = {
    ("peer-review.html", "Genuinely"): "an illustrative peer review, quoted as a review",
    ("content-marketing-kit.html", "In today's fast-paced"): "listed as a phrase to avoid",
    ("101-courses/climate-essentials.html", "is not just"): "inside a quotation",
    ("blog/from-learner-to-leader.html", "Not just 'because the donor wants it' but"): "a learner's testimonial",
    ("DeepDives/platform-gig-work-india.html", "Unlocking the Potential"): "title of a cited BCG report",
    ("blog/animal-welfare-and-the-fifty-rupee-fine.html", "arguably"): "quoting the source's own assessment",
    ("Labs/nvc-mediation-lab.html", "honestly"): "Rosenberg's own NVC wording, 'expressing honestly'",
    ("101-courses/qda-software.html", "Delve"): "the name of a qualitative-analysis software product",
    ("101-courses/feminist-research.html", "at the intersection of"): "intersectionality's own phrasing (Crenshaw)",
}


def text_of(path):
    s = path.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))


def main():
    found, used = [], set()
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(s) for s in SKIP):
            continue
        for m in RX.finditer(text_of(p)):
            key = (rel, m.group(0))
            if key in EXEMPT:
                used.add(key)
                continue
            t = text_of(p)
            found.append("%s: \"%s\"  …%s…" % (rel, m.group(0), t[max(0, m.start() - 60):m.end() + 40]))
    stale = sorted(set(EXEMPT) - used)
    if found or stale:
        print("FAIL — stock phrases in reader-facing text")
        for f in found:
            print("  " + f)
        for s in stale:
            print("  stale exemption: %s %r" % s)
        sys.exit(1)
    print("PASS — none of %d banned stock phrases in reader-facing text (%d documented exemptions)" % (len(PHRASES), len(EXEMPT)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Put every Field Radio clip into site search.

Why this is generated rather than hand-written
----------------------------------------------
Until 2026-09-18 the station had exactly one row in ``data/search-index.json``
-- the page itself. Nineteen clips carrying 44,000 characters of transcript
were live, crawlable and unfindable: a visitor searching a phrase they had
heard in a clip got nothing, and a visitor searching "CREAM indicator" got
nothing, because the only indexed text was the station's own blurb.

Two decisions follow, and both are about not copying the text.

The rows here carry **no transcript**. ``data/search-index.json`` is fetched on
every page load -- ``js/search.js`` calls ``initFuse`` on ``DOMContentLoaded``,
not on first keystroke -- so 45,000 characters of transcript in it would be a
bill every visitor pays on every page for a search few of them run. Instead
``js/search.js`` fetches ``data/field-radio.json`` the first time someone
searches, and matches transcripts from there. One copy of the text, loaded by
the people who use it.

Measured, not assumed: adding a ``transcript`` key to the existing Fuse index
finds nothing. With ``distance: 200`` Fuse scores by how near a match sits to
the start of the field, so on a 4,000-character transcript every probe that was
not in the opening line missed. Turning ``ignoreLocation`` on globally fixed
that and changed the top result on 5 of 20 ordinary queries across the other
1,368 entries -- too much collateral for 19 clips, which is why the transcript
search is a separate, small Fuse instance and the sitewide one is untouched.

The titles, speakers and tracks the rows *do* carry are read from
``data/field-radio.json`` rather than retyped, so renaming a clip there renames
it in search.

What is hand-written is ``COPY``: the one-line description a searcher reads in
the results, and the tags. Those are editorial and cannot be derived from a
transcript without inventing something. A clip missing from ``COPY`` fails the
build rather than shipping with a machine-made summary, and a ``COPY`` entry
for a clip that no longer exists fails too, so the table cannot rot.

Ordering
--------
``build-theories.py`` owns the rows whose URL starts ``/theories/`` and
re-appends them at the end of the file on every run. So these rows are inserted
*before* that block, which keeps both scripts' ``--check`` green whichever runs
first. Run this one, then that one.

    python3 scripts/build-field-radio-index.py          # write
    python3 scripts/build-field-radio-index.py --check  # verify, for CI

Exit 0 + "PASS" when clean; exit 1 with a listing otherwise.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLIPS = ROOT / "data" / "field-radio.json"
INDEX = ROOT / "data" / "search-index.json"
STATION = "/field-radio.html"
PREFIX = "FIELD-RADIO-"

# clip id -> (description shown in the search result, extra tags)
#
# The description is what a searcher reads before deciding to click, so it says
# what the clip argues rather than what it is about. Both are drawn from the
# transcript; neither invents a claim the speaker did not make.
COPY: dict[str, tuple[str, list[str]]] = {
    "vs-05": (
        "What monitoring, evaluation and learning each actually do, and why so much of the data "
        "collected across South Asia serves compliance rather than decisions. Worked through a "
        "nutrition programme distributing supplements to children under five.",
        ["mel", "monitoring", "evaluation", "learning", "decisions", "nutrition", "introduction"],
    ),
    "fr-01": (
        "The opening voice note of the community's weekly challenge: design one outcome indicator "
        "for a programme in your own sector, and say what it measures and how you would collect it.",
        ["indicators", "outcome indicator", "weekly challenge", "community", "indicator design"],
    ),
    "fr-02": (
        "Fifteen seconds on the ground rule for the group: the exercise is to learn from each "
        "other, not to evaluate anyone or check their performance.",
        ["community", "learning", "ground rules", "peer learning"],
    ),
    "fr-03": (
        "An open thread for real MEL design problems — indicator choice, evaluation design, or a "
        "budget constraint on MEL — worked through against the course material.",
        ["ask me anything", "mel", "indicators", "evaluation design", "budget", "office hours"],
    ),
    "fr-04": (
        "A livelihoods organisation in Bihar whose theory of change existed on paper but was "
        "treated as a funding document nobody opened between proposal cycles. The fix was not "
        "rewriting it; it was tying each assumption to something the team already collected.",
        ["theory of change", "assumptions", "bihar", "livelihoods", "mis", "adaptive management"],
    ),
    "fr-05": (
        "The bottleneck most MEL systems hit somewhere between 15 and 50 field staff: five "
        "trackers with five separate name lists, and no way to tell afterwards whether you counted "
        "one child five times. Build a master roster with a unique ID before touching a dashboard.",
        ["data quality", "unique id", "master roster", "kobotoolbox", "dashboards",
         "deduplication", "data systems"],
    ),
    "fr-06": (
        "Assumptions are the conditions that have to be true for a programme to work — the "
        "invisible if-statements behind every intervention, written once at proposal stage and "
        "almost never revisited.",
        ["assumptions", "theory of change", "weekly challenge", "programme design"],
    ),
    "fr-07": (
        "Entry routes into the development sector for someone coming from political science: India "
        "Fellow, ISDM's postgraduate programme, the Gandhi Fellowship, Teach for India and the "
        "Young Professionals tracks, and the different hiring logic behind each.",
        ["careers", "fellowships", "india fellow", "isdm", "gandhi fellowship", "teach for india",
         "political science", "jobs"],
    ),
    "fr-08": (
        "Why assumptions are easy to identify and still get left behind: they do not feel like work "
        "next to activities, budgets, indicators and outputs, so they stay a box filled in during "
        "proposal writing and then forgotten.",
        ["assumptions", "theory of change", "programme design", "evidence"],
    ),
    "fr-09": (
        "Write the assumption, name the evidence that would support it, name the evidence that "
        "would challenge it, set how often you check, and decide what you do if it does not hold. "
        "Worked through community health workers conducting home visits.",
        ["assumptions", "evidence plan", "framework", "public health", "community health workers",
         "adaptive management"],
    ),
    "fr-10": (
        "CREAM — clear, relevant, economic, adequate and monitorable — as a second test of "
        "indicator quality after SMART, and the output-or-outcome question that follows from it.",
        ["indicators", "cream", "smart", "indicator quality", "outputs", "outcomes"],
    ),
    "fr-11": (
        "A walkthrough of the free Theory of Change Workbench in seven steps: problem, goal, "
        "outcomes, outputs, assumptions, indicators, and a diagram built for you at the end.",
        ["theory of change", "workbench", "tool", "outcomes", "outputs", "assumptions",
         "indicators", "free tool"],
    ),
    "vs-03": (
        "Forty thousand textbooks distributed is real, measurable, and tells you nothing about "
        "whether a single child read a page. On the gap between what is easy to count and what a "
        "decision-maker actually needs before funding a second print run.",
        ["indicators", "smart", "measurement", "outputs", "outcomes", "education", "textbooks"],
    ),
    "vs-04": (
        "What changes when a team has a learning culture: staff can say they do not know without "
        "fear, data is used for improvement rather than only for reporting, field insight travels "
        "across teams, and failures are examined instead of hidden.",
        ["learning culture", "organisational learning", "mel", "teams", "adaptive management"],
    ),
    "vs-02": (
        "A baseline without a counterfactual is a photograph. Why literacy rising from 40% to 50% "
        "means very little on its own, and why the decisions that determine whether anything "
        "collected later can be interpreted get made in the first two weeks, under time pressure.",
        ["baseline", "counterfactual", "evaluation design", "impact evaluation", "sampling",
         "attribution"],
    ),
    "fr-12": (
        "How a course here actually gets made, from an idea list in a public repo to a finished "
        "deck. The filter is one question: does the sector need to know this, and is there no "
        "playbook for it already?",
        ["course design", "curriculum", "content", "behind the scenes", "impactmojo"],
    ),
    "vs-06": (
        "A working definition worth testing on your own project: learning happened if someone with "
        "the authority to change something changed it because of evidence your system produced. "
        "Name one decision in the last year that went differently because of your MEL data.",
        ["learning", "mel", "evidence", "decisions", "accountability", "adaptive management"],
    ),
    "vs-07": (
        "Three design decisions that shape what a focus group can tell you: whose experience you "
        "need to understand, who else is in the room, and how the conversation is structured. "
        "Adolescent girls asked about mobility in front of their father will not answer as they would alone.",
        ["gender", "fgd", "focus group discussion", "kii", "key informant interview",
         "qualitative research", "sampling", "intersectionality", "power", "gesi"],
    ),
    "vs-08": (
        "Sixty women in a hundred-person training is where the question starts, not where it ends. "
        "Moving from counting participation to asking about access, benefit, voice and control — "
        "and whether a woman who earned an income kept control of it.",
        ["gender", "mel", "sex-disaggregated data", "participation", "access", "control",
         "measurement", "gesi", "women's empowerment"],
    ),
}


def build(clips: list[dict]) -> list[dict]:
    rows = []
    for c in clips:
        desc, tags = COPY[c["id"]]
        kind = "Short video" if c.get("type") == "video" else "Voice note"
        rows.append({
            "id": PREFIX + c["id"],
            "title": c.get("title") or "Untitled",
            "description": desc,
            "type": "field-radio",
            "category": "Field Radio",
            "url": f"{STATION}#{c['id']}",
            "tags": sorted({t.lower() for t in tags} | {
                "field radio", "voice note" if kind == "Voice note" else "short video",
                (c.get("speaker") or "").lower(), (c.get("track") or "").lower(),
            } - {""}),
        })
        # No transcript field here, deliberately. data/search-index.json is
        # fetched on EVERY page load (js/search.js calls initFuse on
        # DOMContentLoaded), so putting 45,000 characters of transcript in it
        # would charge every visitor on every page for a search few of them run.
        # js/search.js instead fetches data/field-radio.json on the first query
        # and searches the transcripts there -- one copy of the text, on the
        # site, loaded by the people who actually search.
    return rows


def main() -> int:
    check = "--check" in sys.argv

    clips = json.loads(CLIPS.read_text(encoding="utf-8"))["clips"]
    ids = [c["id"] for c in clips]

    missing = [i for i in ids if i not in COPY]
    stale = [k for k in COPY if k not in ids]
    if missing or stale:
        print("FAIL - the COPY table in this script disagrees with data/field-radio.json:\n")
        for i in missing:
            print(f"  {i} is a clip with no description — add one to COPY")
        for k in stale:
            print(f"  {k} is in COPY but is no longer a clip — remove it")
        return 1

    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        print(f"FAIL - data/field-radio.json repeats clip id(s): {', '.join(dup)}")
        return 1

    entries = json.loads(INDEX.read_text(encoding="utf-8"))
    kept = [e for e in entries if not str(e.get("id", "")).startswith(PREFIX)]

    # Insert before the theories block, which build-theories.py re-appends last
    # on every run. Appending after it would make that script's --check fail.
    at = next((n for n, e in enumerate(kept)
               if str(e.get("url", "")).startswith("/theories/")), len(kept))
    out = kept[:at] + build(clips) + kept[at:]
    text = json.dumps(out, ensure_ascii=False, indent=2) + "\n"

    if check:
        if text != INDEX.read_text(encoding="utf-8"):
            print("FAIL - data/search-index.json is stale for Field Radio.")
            print("Run: python3 scripts/build-field-radio-index.py")
            print("     python3 scripts/build-theories.py")
            return 1
        print(f"PASS - all {len(ids)} Field Radio clips are in site search.")
        return 0

    INDEX.write_text(text, encoding="utf-8")
    print(f"wrote {len(ids)} Field Radio rows into data/search-index.json. "
          f"Now run build-theories.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

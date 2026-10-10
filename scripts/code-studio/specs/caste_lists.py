# -*- coding: utf-8 -*-
"""Linking caste lists: matching the Mandal Commission's 1980 list for Bihar to today's Central List, in pandas."""

# Every cell is self-contained, so a learner can run any of them first.
HEAD = ('import re\nimport pandas as pd\n'
        'mandal = pd.read_csv("mandal_bihar.csv")\n'
        'obc = pd.read_csv("obc_bihar.csv")\n')
NAMES = ('\ndef names(entry):\n'
         '    """Every name an entry lists, cleaned for comparison."""\n'
         '    extra = []\n'
         '    for inside in re.findall(r"\\((.*?)\\)", entry):\n'
         '        low = inside.lower().strip()\n'
         '        if low == "muslim" or low.startswith(("only", "in ", "this")):\n'
         '            continue  # a religion or a limit on area, not another name\n'
         '        extra.append(inside)\n'
         '    entry = re.sub(r"\\(.*?\\)", " ", entry) + "," + ",".join(extra)\n'
         '    out = []\n'
         '    for part in re.split(r"[,/;\\u2014]| or | and | & ", entry):\n'
         '        part = part.lower().replace("-", " ")\n'
         '        part = re.sub(r"[^a-z ]", "", part)\n'
         '        part = re.sub(r"\\s+", " ", part).strip()\n'
         '        if part:\n'
         '            out.append(part)\n'
         '    return out\n')
EXPLODE = ('\nm = mandal.assign(key=mandal["name"].map(names)).explode("key")\n'
           'o = obc.assign(key=obc["name"].map(names)).explode("key")\n')

C = {}
C["read"] = HEAD + ('print(len(mandal), "entries on the Mandal list for Bihar (1980)")\n'
                    'print(len(obc), "active entries on the Central List for Bihar")\n'
                    'print(mandal.sample(5, random_state=1).to_string(index=False))')
C["names"] = HEAD + NAMES + ('\nfor e in ["Kasab(Kasai) (Muslim)", "Chandrabanshi (Kahar)", "Kewat, Keot",\n'
                             '          "Aguri\\u2014Vaishya, Sudi, Halwai"]:\n'
                             '    print(e, "->", names(e))')
C["exact"] = HEAD + NAMES + EXPLODE + (
    'print(len(m), "Mandal names;", len(o), "Central List names")\n'
    'pairs = m.merge(o, on="key", suffixes=("_m", "_o"))\n'
    'print(pairs["mandal_id"].nunique(), "of", len(mandal), "Mandal entries share at least one exact name")\n'
    'print(pairs[["mandal_id", "obc_id", "key"]].head(6).to_string(index=False))')
C["near"] = HEAD + NAMES + EXPLODE + (
    'from difflib import SequenceMatcher\n'
    'pairs = m.merge(o, on="key")\n'
    'left = m[~m["mandal_id"].isin(pairs["mandal_id"])]\n'
    'print(left["mandal_id"].nunique(), "Mandal entries with no exact name in common")\n'
    'keys = o["key"].unique()\n'
    'rows = []\n'
    'for mid, key in zip(left["mandal_id"], left["key"]):\n'
    '    score, best = max((SequenceMatcher(None, key, k).ratio(), k) for k in keys)\n'
    '    rows.append((mid, key, best, round(score, 2)))\n'
    'cand = pd.DataFrame(rows, columns=["mandal_id", "mandal_name", "obc_name", "score"])\n'
    'cand = cand.sort_values("score", ascending=False)\n'
    'print(cand.head(25).to_string(index=False))')
C["cut"] = HEAD + NAMES + EXPLODE + (
    'from difflib import SequenceMatcher\n'
    'pairs = m.merge(o, on="key")\n'
    'left = m[~m["mandal_id"].isin(pairs["mandal_id"])]\n'
    'keys = o["key"].unique()\n'
    'rows = []\n'
    'for mid, key in zip(left["mandal_id"], left["key"]):\n'
    '    score, best = max((SequenceMatcher(None, key, k).ratio(), k) for k in keys)\n'
    '    rows.append((mid, key, best, round(score, 2)))\n'
    'cand = pd.DataFrame(rows, columns=["mandal_id", "mandal_name", "obc_name", "score"])\n'
    'for cut in (0.95, 0.9, 0.85, 0.8):\n'
    '    print(cut, (cand["score"] >= cut).sum(), "names would be accepted")\n'
    'print(cand[cand["score"] >= 0.85].sort_values("score", ascending=False).to_string(index=False))')
C["both"] = HEAD + NAMES + EXPLODE + (
    'sc = pd.read_csv("sc_bihar.csv")\n'
    's = sc.assign(key=sc["name"].map(names)).explode("key")\n'
    'both = o.merge(s, on="key", suffixes=("_obc", "_sc"))\n'
    'print(both[["name_obc", "name_sc", "key"]].to_string(index=False))')


def py(key):
    return {"t": "code", "lang": "py", "code": C[key], "pkgs": "pandas"}


def p(h):
    return {"t": "p", "html": h}


def ex(h):
    return {"t": "info", "html": "<strong>Try it.</strong> " + h}


IC = lambda s: '<code class="inline">%s</code>' % s

PAGE = {
    "slug": "caste-lists",
    "order": 19,
    "kind": "runnable",
    "title": "Linking Caste Lists",
    "h1": "Linking caste lists",
    "lede": ("Match the Mandal Commission's 1980 list of backward classes in Bihar to today's Central List of "
             "OBCs, name by name, in pandas running in your browser. The method is record linkage, and the lesson "
             "is how much of it a computer cannot decide for you."),
    "description": ("A record-linkage exercise on real government lists: clean caste names, match the Mandal "
                    "Commission's 1980 Bihar list to the Central List of OBCs exactly and by string similarity, "
                    "and find names that sit on both the OBC and Scheduled Caste lists. Python and pandas in your "
                    "browser."),
    "card": "Match the 1980 Mandal list to today's Central List for Bihar: cleaning, exact and near matches.",
    "datasets": ["mandal_bihar", "obc_bihar", "sc_bihar"],
    "engine_note": ("<strong>How the live code works.</strong> Your first Run downloads Pyodide (Python for the "
                    "browser, about 10&nbsp;MB) and pandas, so give it up to a minute on a slow connection. Three "
                    "files are in the working folder: " + IC("mandal_bihar.csv") + " (168 entries), "
                    + IC("obc_bihar.csv") + " (132) and " + IC("sc_bihar.csv") + " (23). <strong>This is real "
                    "data</strong>, taken from Jolad and Kalyani's <a href=\"/dataverse.html#database-of-castes\">"
                    "Database of castes</a> (Harvard Dataverse, doi:10.7910/DVN/WT5VIY, CC0), which digitises the "
                    "Mandal Commission report and the National Commission for Backward Classes' Central List."),
    "modules": [
        {"tab": "The lists", "title": "Two lists, forty years apart", "blocks": [
            p("In 1980 the Second Backward Classes Commission, chaired by B.&nbsp;P. Mandal, listed the backward "
              "classes of each state. The Central List of OBCs that governs central government jobs and "
              "admissions today was built after 1993 and has been amended by resolution ever since. A "
              "researcher who wants to know which communities Mandal named and the Central List kept has to "
              "link the two lists name by name, because neither carries the other's identifiers."),
            p("Linking two files that share no key is called <strong>record linkage</strong>. The same problem "
              "turns up when you match beneficiary lists to a survey, villages across census rounds, or "
              "schools across two years of UDISE. Caste lists make the difficulty unusually visible: one "
              "community is spelt several ways, one entry lists several communities, and two different "
              "communities can have names a letter apart."),
            py("read"),
            p("Bihar has 168 entries on the Mandal list and 132 active entries on the Central List. Look at the "
              "sample: one entry can carry several names (" + IC("Dhunia, Dhumian") + "), and brackets hold "
              "either another spelling (" + IC("Sauta (Sota)") + ") or another name."),
            ex("Print the entries whose name contains a bracket with "
               + IC('obc[obc["name"].str.contains(r"\\(")]') + ". How many are there, and what do the brackets "
               "say?"),
        ]},
        {"tab": "Cleaning", "title": "Cleaning names before you compare them", "blocks": [
            p("Two spellings that a reader sees as the same, " + IC("Kewat") + " and " + IC("kewat ") + ", are "
              "different strings to a computer. So every name is reduced to a <strong>key</strong>: lower "
              "case, letters and spaces only, single spaces, and one key per name the entry lists."),
            p("The brackets need a decision. In the Bihar Central List they hold three kinds of thing: a religion "
              "(" + IC("(Muslim)") + ", on 23 entries), a limit on area (" + IC("(only in the districts of Sivan "
              "&amp; Rohtas)") + ") and another name for the same community (" + IC("Chandrabanshi (Kahar)") +
              "). The function keeps the third and drops the first two."),
            py("names"),
            p(IC("Kasab(Kasai) (Muslim)") + " becomes two keys, " + IC("kasab") + " and " + IC("kasai") + ", and "
              "the religion goes. The Mandal entry for Aguri is one long entry in which a dash separates the "
              "first name from the rest, so the function splits on it too."),
            {"t": "h3", "html": "Exact matches"},
            p(IC(".explode()") + " turns each list of keys into one row per key, and a merge on the key finds "
              "every pair of entries that share a cleaned name."),
            py("exact"),
            p("The 168 Mandal entries carry 272 names and the 132 Central List entries carry 201. "
              "<strong>114 Mandal entries share at least one exact name</strong> with the Central List. Mandal "
              "entry 432 matches Central List entry 325 on seven names at once, because both lists group the "
              "trading castes of the Vaishya cluster into a single entry."),
            ex("In " + IC("names()") + ", delete the line " + IC("extra.append(inside)") + " so that every bracket "
               "is thrown away, and run the exact match again. How many Mandal entries do you lose, and which?"),
        ]},
        {"tab": "Near matches", "title": "Near matches, and why a score cannot decide", "blocks": [
            p("The 54 entries left over may be missing from today's list, or spelt differently. "
              + IC("difflib.SequenceMatcher") + " from Python's standard library scores how alike two strings "
              "are, from 0 to 1. For each unmatched Mandal name the cell finds the most similar Central List name."),
            py("near"),
            p("Read the list from the top. " + IC("churihara") + " and " + IC("churihar") + " differ by a final "
              "vowel, and " + IC("kaghzi") + " and " + IC("kagzi") + " by one letter: these look like one name "
              "written two ways. Further down, " + IC("sunri") + " and " + IC("sunar") + " score 0.80, and so do "
              + IC("lodha") + " and " + IC("lohar") + ". Those are different communities whose names happen to "
              "share most of their letters. The score measures spelling, and caste names are short, so a single "
              "letter is a large share of the string."),
            {"t": "h3", "html": "Choosing a cut-off"},
            py("cut"),
            p("No cut-off separates the true from the false. At 0.95 nothing is accepted. At 0.85 seven names "
              "are accepted, and each needs a reason before you keep it: " + IC("godhi") + " and " + IC("godi")
              + " are plausibly one community, because the Mandal entry also gives " + IC("Chhavo") + " and the "
              "Central List entry " + IC("Chhava") + ", while " + IC("kawar") + " and " + IC("kalwar") + " score "
              "0.91 on spelling alone and need a source, such as the state's own list or an ethnographic "
              "survey, before anyone treats them as the same. Lower the cut-off to 0.80 and 26 names come in, "
              "including the pairs above that are plainly different."),
            {"t": "info", "tone": "warning", "html": "<strong>A score ranks candidates for a person to check. It "
             "does not make the decision.</strong> Record every accepted near match with the reason you accepted "
             "it, so that someone else can disagree with you."},
            ex("Add a column " + IC("decision") + " to " + IC("cand") + " and fill it by hand for the seven "
               "pairs at 0.85 or above, with " + IC('"same"') + ", " + IC('"different"') + " or "
               + IC('"check"') + ". Then count each."),
        ]},
        {"tab": "Two lists", "title": "One name on two lists", "blocks": [
            p("The same cleaning can link the Central List of OBCs to Bihar's list of Scheduled Castes."),
            py("both"),
            p("Six names sit on both lists: Dhobi, Nat, Mehtar, Lalbegi, Halalkhor and Bhangi. They come from "
              "three Central List entries, and each is marked " + IC("(Muslim)") + ", which the cleaning function threw away. That "
              "qualifier is the whole difference. Paragraph 3 of the Constitution (Scheduled Castes) Order, 1950 "
              "allows only a person who professes Hinduism, Sikhism or Buddhism to be a member of a Scheduled "
              "Caste, and the Muslim members of these communities appear on the backward classes list instead."),
            p("The general point: <strong>cleaning decides what a match means</strong>. A rule that is right for "
              "linking Mandal to the Central List, where religion is not the question, is wrong for linking the "
              "OBC and SC lists, where it is the question. Write the rule down next to the result."),
            ex("Change " + IC("names()") + " so that it keeps " + IC("muslim") + " as part of the key, and run "
               "the cell again. What is left?"),
        ]},
        {"tab": "Limits", "title": "What a match can and cannot tell you", "blocks": [
            p("Every match here is a match of spellings. A Mandal entry with no match has not been shown to be "
              "dropped from the Central List: it may be listed under a name neither list prints, or folded into "
              "another entry. A match has not been shown to be the same people either: two communities in "
              "different parts of a state can share a name."),
            {"t": "ul", "items": [
                "Report the count of exact matches and the count of near matches separately, and say how the near "
                "ones were decided.",
                "Keep the original text of both entries in the output, beside the keys you matched on.",
                "Treat the cut-off as a choice you made and report what happens to the result if it moves.",
                "Check a sample of matches and non-matches against a third source before you publish a rate.",
            ]},
            ex("Repeat the exact match for the whole country with the full Database of castes, and compare the "
               "share of Mandal entries matched across states. Which states fall well below Bihar's 114 of 168, "
               "and is that a difference in lists or in spelling?"),
        ]},
    ],
    "next": [
        {"href": "/castes.html", "title": "Caste Lists Explorer",
         "desc": "The 1931 Census, the SC and OBC lists and the Mandal list, charted."},
        {"href": "/101-courses/caste-studies.html", "title": "Caste Studies 101",
         "desc": "The history and politics behind these lists."},
        {"href": "/code/pandas.html", "title": "pandas for Development Data",
         "desc": "The pandas basics this page assumes."},
        {"href": "/dataverse.html#database-of-castes", "title": "Database of castes",
         "desc": "The source data, in the Dataverse."},
    ],
}

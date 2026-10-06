# -*- coding: utf-8 -*-
"""OpenRefine: Cleaning Messy Survey and MIS Data. A guided tool course with Python cells that repeat each
cleaning step on the page.

Facts checked on 6 October 2026 against openrefine.org (download page and user manual). Sources are listed in
the agent report.
"""

DL = '<a href="/code/data/households.csv" download style="color:var(--accent-color)">households.csv</a>'

# Every cell rebuilds the same messy practice copy, so each one runs on its own.
MK = '''import pandas as pd
hh = pd.read_csv("households.csv")
dist = pd.read_csv("districts.csv")

# A messy practice copy: every third household gets a variant spelling of its
# district, and some expenditure cells arrive as text.
variants = {
    "Purnia": ["Purnea", "PURNIA", " Purnia"],
    "Kozhikode": ["Kozhikkode", "Calicut", "kozhikode"],
    "Barmer": ["Badmer", "Barmer "],
    "Wayanad": ["Wayanadu", "Waynad"],
    "Udaipur": ["udaipur", "Udaipur."],
    "Gaya": ["Gaya ", "GAYA"],
    "Betul": ["Baitul", "Betul"],
    "Rewa": ["Reewa", "Rewa"],
    "Indore": ["Indor", "Indore"],
    "Patna": ["Patna  ", "patna"],
}
def messy_district(r):
    if r["hh_id"] % 3:
        return r["district"]
    v = variants[r["district"]]
    return v[(r["hh_id"] // 3) % len(v)]
def messy_exp(r):
    if r["hh_id"] % 40 == 13:
        return "not asked"
    if r["hh_id"] % 20 == 7:
        return f"{r['monthly_pc_exp']:,}"
    return str(r["monthly_pc_exp"])
state = dict(zip(dist["district"], dist["state"]))
raw = pd.DataFrame({
    "hh_id": hh["hh_id"],
    "district": hh.apply(messy_district, axis=1),
    "location": hh["district"] + ", " + hh["district"].map(state),
    "area": hh["area"],
    "caste": hh["caste"],
    "monthly_pc_exp": hh.apply(messy_exp, axis=1),
})
'''

C = {}
C["make"] = MK + '''print(raw.head(8))
print(raw.shape)
print()
print("Copy everything below this line into OpenRefine's Clipboard box")
print(raw.to_csv(index=False))'''

C["textfacet"] = MK + '''# Text facet on district: every distinct value and its count
facet = raw["district"].value_counts().sort_index()
print(facet)
print(len(facet), "distinct values for 10 real districts")'''

C["numfacet"] = MK + '''# Numeric facet: which cells parse as numbers?
num = pd.to_numeric(raw["monthly_pc_exp"], errors="coerce")
print("numeric:", num.notna().sum(), " non-numeric:", num.isna().sum())
print(raw.loc[num.isna(), ["hh_id", "monthly_pc_exp"]].drop_duplicates("monthly_pc_exp", keep="first").head(6))
# The histogram OpenRefine draws, as counts in Rs 500 bands
print(pd.cut(num.dropna(), bins=range(0, 8001, 500)).value_counts().sort_index())'''

C["fingerprint"] = MK + '''import re, unicodedata
def fingerprint(s):
    # The steps OpenRefine's documentation lists for its fingerprint keying function
    s = s.strip().lower()
    s = re.sub(r"[^\\w\\s]", "", s)                     # drop punctuation
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()  # ASCII-fold
    return " ".join(sorted(set(s.split())))

vals = raw["district"].value_counts()
keys = pd.DataFrame({"value": vals.index, "rows": vals.values})
keys["key"] = keys["value"].map(fingerprint)
clusters = keys.groupby("key").filter(lambda g: len(g) > 1).sort_values(["key", "rows"], ascending=[True, False])
print(clusters.to_string(index=False))
print()
print("Not caught by fingerprint:", sorted(set(keys["value"]) - set(clusters["value"]) - set(dist["district"])))'''

C["ngram"] = MK + '''import re
def ngram_fingerprint(s, n=2):
    s = re.sub(r"[^\\w]", "", s.lower())                # lowercase, drop punctuation and spaces
    grams = sorted(set(s[i:i + n] for i in range(len(s) - n + 1)))
    return "".join(grams)

for a, b in [("Purnia", "Purnea"), ("Kozhikode", "Kozhikkode"), ("Wayanad", "Waynad"), ("Barmer", "Badmer")]:
    print(f"{a:10} {ngram_fingerprint(a):22} {b:11} {ngram_fingerprint(b):22} same key: {ngram_fingerprint(a) == ngram_fingerprint(b)}")'''

C["levenshtein"] = MK + '''def lev(a, b):
    # edit distance: insertions, deletions and substitutions
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

radius = 2
official = list(dist["district"])
for v in sorted(raw["district"].unique()):
    if v in official:
        continue
    near = [(o, lev(v, o)) for o in official if lev(v, o) <= radius]
    print(repr(v).ljust(14), "->", near if near else "nothing within radius " + str(radius))'''

C["merge"] = MK + '''# What you decide in the clustering window, written down as a mapping
fix = {"Purnea": "Purnia", "PURNIA": "Purnia", " Purnia": "Purnia",
       "Kozhikkode": "Kozhikode", "kozhikode": "Kozhikode",
       "Badmer": "Barmer", "Barmer ": "Barmer",
       "Wayanadu": "Wayanad", "Waynad": "Wayanad",
       "udaipur": "Udaipur", "Udaipur.": "Udaipur",
       "Gaya ": "Gaya", "GAYA": "Gaya", "Baitul": "Betul",
       "Reewa": "Rewa", "Indor": "Indore", "Patna  ": "Patna", "patna": "Patna"}
clean = raw.copy()
clean["district"] = clean["district"].replace(fix)
left = clean.loc[~clean["district"].isin(dist["district"]), "district"].value_counts()
print("Values still not in districts.csv:")
print(left)
print()
print(clean["district"].value_counts().sort_index())'''

C["grel"] = MK + '''# GREL value.trim().toTitlecase()  ->  pandas .str.strip().str.title()
t = raw["district"].str.strip().str.title()
print(raw["district"].nunique(), "distinct values before,", t.nunique(), "after trim and title case")
print(sorted(t.unique()))
print()
# GREL value.replace(",", "").toNumber()  ->  remove commas, then convert
exp = pd.to_numeric(raw["monthly_pc_exp"].str.replace(",", ""), errors="coerce")
print("non-numeric before:", pd.to_numeric(raw["monthly_pc_exp"], errors="coerce").isna().sum(),
      " after removing commas:", exp.isna().sum())
print(raw.loc[exp.isna(), "monthly_pc_exp"].unique())'''

C["split"] = MK + '''# Edit column > Split into several columns..., separator ", "
parts = raw["location"].str.split(", ", n=1, expand=True)
parts.columns = ["location 1", "location 2"]
print(parts.head(4))
print(parts["location 2"].value_counts())
print()
# Edit column > Join columns..., separator " | "
joined = raw["area"] + " | " + raw["caste"]
print(joined.value_counts().head(6))'''

C["recipe"] = MK + '''# The whole cleaning as one recipe that runs again on next month's export
def clean_households(df, districts):
    out = df.copy()
    out["district"] = out["district"].str.strip().str.title()
    out["district"] = out["district"].str.replace(r"\\.$", "", regex=True)
    lookup = {"Purnea": "Purnia", "Kozhikkode": "Kozhikode", "Calicut": "Kozhikode",
              "Badmer": "Barmer", "Wayanadu": "Wayanad", "Waynad": "Wayanad",
              "Baitul": "Betul", "Reewa": "Rewa", "Indor": "Indore"}
    out["district"] = out["district"].replace(lookup)
    out["monthly_pc_exp"] = pd.to_numeric(out["monthly_pc_exp"].str.replace(",", ""), errors="coerce")
    bad = set(out["district"]) - set(districts["district"])
    assert not bad, f"unknown districts: {bad}"
    return out

clean = clean_households(raw, dist)
print(clean.shape)
print(clean["district"].value_counts().sort_index())
print("missing expenditure:", clean["monthly_pc_exp"].isna().sum())
clean.to_csv("households_clean.csv", index=False)
print(pd.read_csv("households_clean.csv").shape, "read back from households_clean.csv")'''


A = 'style="color:var(--accent-color)"'


def link(href, text):
    return '<a href="%s" rel="noopener" target="_blank" %s>%s</a>' % (href, A, text)


def py(key):
    return {"t": "code", "lang": "py", "pkgs": "pandas", "code": C[key]}


PAGE = {
    "slug": "openrefine",
    "order": 13,
    "kind": "guide",
    "tool": "OpenRefine",
    "title": "OpenRefine: Cleaning Messy Survey and MIS Data",
    "h1": "OpenRefine: cleaning messy survey and MIS data",
    "lede": ("Clean a household file the way most field teams receive it: district names spelt five ways, "
             "numbers stored as text, two facts in one column. OpenRefine is free, runs on your own computer "
             "and records every step, so the cleaning can be repeated on next month's export. Python cells on "
             "this page run each step on the same data, so you can compare."),
    "description": ("A free guided course in OpenRefine for development practitioners in South Asia: install it, "
                    "create a project from a household CSV, use text, numeric and timeline facets, cluster "
                    "district names spelt different ways, transform with GREL, split and join columns, reconcile, "
                    "and save the operation history as JSON to repeat the cleaning."),
    "card": "Facets, clustering for district and village names spelt five ways, GREL, and a cleaning you can replay.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>OpenRefine does not run in a browser tab from this site.</strong> It runs on your own "
                    "computer and opens in your browser at a local address. The grey boxes are GREL expressions "
                    "for you to type into OpenRefine; this page does not show OpenRefine screens or results, "
                    "because it cannot produce them. Each module says what to look for on your screen. The "
                    "Python cells run the same cleaning step here with pandas, so you can check your OpenRefine "
                    "counts against them. The first Python run downloads the engine once (about 10&nbsp;MB)."),
    "modules": [
        {"tab": "Start",
         "title": "Install and start OpenRefine",
         "blocks": [
             {"t": "p", "html": "Monitoring and MIS exports arrive messy. One enumerator types "
                                "<em>Purnea</em>, another <em>Purnia</em>, a third <em>PURNIA</em> with a trailing "
                                "space. A spreadsheet treats those as three districts. OpenRefine is built for "
                                "exactly this: it shows you every distinct value in a column, groups the ones that "
                                "are probably the same, and lets you fix thousands of cells in one action."},
             {"t": "info", "html": "<strong>Version and cost, checked 6 October 2026.</strong> The current "
                                   "release on the " + link("https://openrefine.org/download", "OpenRefine download page")
                                   + " is <strong>OpenRefine 3.10.0</strong>, dated 26 February 2026 (3.9.5 and "
                                   "3.8.7 are listed as older versions). OpenRefine is free software under the "
                                   "BSD 3-clause licence: no price, no account, no licence key."},
             {"t": "h3", "html": "Which file to download"},
             {"t": "ul", "items": [
                 "<strong>Windows:</strong> an installer (EXE) or a ZIP file. Both Windows packages include Java "
                 "(the download page calls this \"embedded Java\"), so you do not need to install Java separately.",
                 "<strong>Mac:</strong> a DMG file. The " + link("https://openrefine.org/docs/manual/installing",
                 "installation manual") + " says the Mac version includes Java. It also mentions "
                 "<code class=\"inline\">brew install --cask openrefine</code> if you use Homebrew.",
                 "<strong>Linux:</strong> a TAR.GZ file. Extract it and run <code class=\"inline\">./refine</code> "
                 "from the extracted folder. If Java is missing, the manual points to Adoptium.net for a Java "
                 "runtime.",
             ]},
             {"t": "h3", "html": "Starting it"},
             {"t": "steps", "items": [
                 "Windows: run <code class=\"inline\">openrefine.exe</code> from the folder where you installed "
                 "it. Mac: open OpenRefine from Applications. Linux: run <code class=\"inline\">./refine</code> in "
                 "a terminal.",
                 "A console window opens and stays open. Leave it running: it is the program.",
                 "Your browser opens at <code class=\"inline\">http://127.0.0.1:3333/</code>. If it does not, type "
                 "that address yourself. The manual describes OpenRefine as \"a small web server on your own "
                 "computer\" that you use through your browser.",
                 "To quit, close the browser tabs, go to the console window and press "
                 "<code class=\"inline\">Ctrl + C</code>. The manual says this is how OpenRefine saves your "
                 "changes on exit; it also autosaves every five minutes.",
             ]},
             {"t": "info", "html": "<strong>Your data stays on your computer.</strong> Projects are stored in a "
                                   "workspace folder on your own machine, and the local address "
                                   "<code class=\"inline\">127.0.0.1</code> is your own computer. That matters for "
                                   "beneficiary lists and survey files with names and phone numbers. Two features "
                                   "do send data out: reconciliation (module 7) sends the column you reconcile to "
                                   "the service you choose, and fetching URLs sends whatever the URLs contain. Use "
                                   "them on columns that hold no personal data."},
             {"t": "h3", "html": "On a modest laptop"},
             {"t": "p", "html": "OpenRefine holds the whole project in memory. A file of a few hundred thousand "
                                "rows is fine on most laptops; for larger ones, the manual explains how to raise "
                                "the memory limit. On Windows, if you start OpenRefine with "
                                "<code class=\"inline\">refine.bat</code>, you can set it in "
                                "<code class=\"inline\">refine.ini</code> on the line "
                                "<code class=\"inline\">REFINE_MEMORY=1024M</code> (that file is not read when you "
                                "start with <code class=\"inline\">openrefine.exe</code>). The manual advises giving "
                                "OpenRefine no more than half of the memory left after your operating system's "
                                "own use."},
         ]},
        {"tab": "Project",
         "title": "Create a project from a CSV",
         "blocks": [
             {"t": "p", "html": "An OpenRefine <strong>project</strong> is a copy of your data plus the history of "
                                "everything you do to it. The original file on disk is never changed."},
             {"t": "h3", "html": "The practice file"},
             {"t": "p", "html": "The course uses " + DL + ": 240 households in ten districts. "
                                "<span class=\"illustrative-tag\">Illustrative data, invented for teaching</span> "
                                "The district names are real places; every number is made up. That file is clean, "
                                "so the cell below makes a messy copy of it, the kind a field team actually sends: "
                                "every third household gets a variant spelling of its district (wrong case, extra "
                                "spaces, a full stop, an older spelling, a transliteration variant, a colonial-era "
                                "name), some expenditure figures arrive as <code class=\"inline\">2,580</code> with "
                                "a comma, and a few say <code class=\"inline\">not asked</code>. A "
                                "<code class=\"inline\">location</code> column holds district and state together."},
             py("make"),
             {"t": "p", "html": "The first block printed is the top eight rows and the size, 240 rows and 6 "
                                "columns. Below the line is the whole file as CSV text."},
             {"t": "h3", "html": "Load it into OpenRefine"},
             {"t": "steps", "items": [
                 "Run the cell above. Select the CSV text below the line \"Copy everything below this line\", "
                 "from <code class=\"inline\">hh_id,district,...</code> to the last row, and copy it.",
                 "In OpenRefine, on the <strong>Create project</strong> screen, choose <strong>Clipboard</strong> "
                 "on the left, paste the text into the box and click <strong>Next &raquo;</strong>.",
                 "You now see the preview. Check that OpenRefine has read it as comma-separated values and that "
                 "the first row became the column names. If a name such as <em>Kozhikode</em> showed odd "
                 "characters, you would change the character encoding here (UTF-8 is the usual choice).",
                 "Type a project name, for example <code class=\"inline\">households messy</code>, and click "
                 "<strong>Create project &raquo;</strong>.",
             ]},
             {"t": "p", "html": "For your own files, choose <strong>This Computer</strong> and click "
                                "<strong>Browse&hellip;</strong> instead of Clipboard. The manual lists CSV, TSV, "
                                "Excel (XLS and XLSX), ODS, JSON and XML among the formats it reads, and it can open "
                                "a ZIP or GZ archive directly."},
             {"t": "info", "html": "<strong>What to look for.</strong> The project opens on a grid that shows the "
                                   "row count at the top: it should say 240 rows. The "
                                   "<code class=\"inline\">monthly_pc_exp</code> column is text for now, because "
                                   "some cells hold commas and words."},
         ]},
        {"tab": "Facets",
         "title": "See the problem: text, numeric and timeline facets",
         "blocks": [
             {"t": "p", "html": "A <strong>facet</strong> summarises one column in the left-hand panel and lets "
                                "you filter rows by clicking a value. It is the fastest way to see what a column "
                                "really contains."},
             {"t": "h3", "html": "Text facet: every distinct spelling"},
             {"t": "steps", "items": [
                 "Click the small triangle at the top of the <code class=\"inline\">district</code> column.",
                 "Choose <strong>Facet &rarr; Text facet</strong>.",
                 "The facet panel lists every value with its count. Use the sort option at the top of the facet "
                 "to sort by count instead of alphabetically. Click a value to show only those rows; click "
                 "<strong>exclude</strong> beside it to show every row except those.",
             ]},
             {"t": "p", "html": "The cell below does the same count with pandas."},
             py("textfacet"),
             {"t": "p", "html": "There are <strong>29 distinct values for 10 districts</strong>. Look closely: "
                                "<em>Barmer</em> appears twice (16 rows and 4 rows) because one of them carries a "
                                "trailing space you cannot see, and the same is true of <em>Gaya</em> and "
                                "<em>Patna</em>. Your OpenRefine facet should list the same 29 choices with the same "
                                "counts. The \"29 choices\" link at the top of the facet copies the list as "
                                "tab-separated text, which is a quick way to paste it into a report."},
             {"t": "h3", "html": "Numeric facet: which cells are not numbers"},
             {"t": "steps", "items": [
                 "OpenRefine imported <code class=\"inline\">monthly_pc_exp</code> as text. Convert it first "
                 "with the data-type transform for numbers under <strong>Edit cells &rarr; Common "
                 "transforms</strong>. A yellow bar at the top tells you how many cells were converted; cells "
                 "that cannot be converted keep their original value. (For your own files, you can instead tick "
                 "\"Attempt to parse cell text into numbers\" in the import preview.)",
                 "Then <strong>Facet &rarr; Numeric facet</strong> on the same column.",
                 "The facet draws a histogram and offers checkboxes for <strong>non-numeric</strong>, "
                 "<strong>blank</strong> and <strong>error</strong> values. Tick only non-numeric to see the cells "
                 "that did not convert.",
             ]},
             py("numfacet"),
             {"t": "p", "html": "Here <strong>222 cells parse as numbers and 18 do not</strong>: twelve written "
                                "with a thousands comma (such as <code class=\"inline\">2,580</code>) and six that "
                                "say <code class=\"inline\">not asked</code>. The banded counts below them are the "
                                "histogram the facet draws; most households sit between Rs&nbsp;1,500 and "
                                "Rs&nbsp;3,500. Module 5 fixes the commas."},
             {"t": "h3", "html": "Timeline facet: dates"},
             {"t": "p", "html": "A <strong>timeline facet</strong> works like a numeric facet for dates, and only "
                                "on cells of the date type. The practice file has no date column, so try it on your "
                                "own data, for example the submission time in a KoboToolbox or ODK export: convert "
                                "the column with the data-type transform for dates under <strong>Edit cells &rarr; "
                                "Common transforms</strong> (or the GREL expression "
                                "<code class=\"inline\">value.toDate()</code>), then choose <strong>Facet &rarr; "
                                "Timeline facet</strong>. The facet also counts blank cells and cells that failed "
                                "to convert, which is how you spot interviews logged on impossible dates."},
             {"t": "info", "html": "<strong>Exercise.</strong> Add a text facet on <code class=\"inline\">caste</code> "
                                   "and click <em>SC</em>. The district facet now counts only SC households. Facets "
                                   "combine, and most operations apply only to the rows currently shown, so clear your "
                                   "selections (<strong>Reset All</strong>) before an edit meant for every row."},
         ]},
        {"tab": "Clustering",
         "title": "Cluster spellings of the same place",
         "blocks": [
             {"t": "p", "html": "Clustering finds values that are probably the same thing written differently and "
                                "offers to merge them. Open it from the column menu: <strong>Edit cells &rarr; "
                                "Cluster and edit&hellip;</strong>, or press <strong>Cluster</strong> in a text facet. "
                                "The window offers two families of methods, and the OpenRefine manual recommends "
                                "using them in the order shown, strictest first."},
             {"t": "ul", "items": [
                 "<strong>Key collision</strong>: each value is turned into a key, and values with the same key "
                 "form a cluster. The keying functions are <em>Fingerprint</em>, <em>N-gram fingerprint</em>, and "
                 "four phonetic ones: <em>Metaphone3</em>, <em>Cologne Phonetic</em>, <em>Daitch-Mokotoff</em> and "
                 "<em>Beider-Morse</em>. Fast, even on millions of cells.",
                 "<strong>Nearest neighbour</strong>: values are compared in pairs and clustered when their "
                 "distance is within a <em>radius</em> you set. The distance functions are <em>Levenshtein</em> "
                 "(edit distance) and <em>PPM</em>. Slower, and looser.",
             ]},
             {"t": "h3", "html": "Fingerprint first"},
             {"t": "p", "html": "The " + link("https://openrefine.org/docs/technical-reference/clustering-in-depth",
                                "clustering documentation") + " lists the fingerprint steps: trim spaces, lowercase, "
                                "remove punctuation, turn accented Western letters into plain ASCII "
                                "(<em>g&ouml;del</em> becomes <em>godel</em>), split into words, sort and "
                                "de-duplicate the words, and join them again. The cell below follows those steps. "
                                "It is our reimplementation, so OpenRefine's own keys may differ in small details."},
             py("fingerprint"),
             {"t": "p", "html": "Fingerprint finds six clusters: Barmer, Gaya, Kozhikode, Patna, Purnia and "
                                "Udaipur, which between them hold the case, space and punctuation variants "
                                "(<em>GAYA</em>, <em>patna</em>, <em>Udaipur.</em>, the trailing spaces). It leaves "
                                "nine values alone: <em>Badmer, Baitul, Calicut, Indor, Kozhikkode, Purnea, Reewa, "
                                "Wayanadu, Waynad</em>. Those differ in their letters, and fingerprint never changes "
                                "letters, which is why it produces so few false matches."},
             {"t": "h3", "html": "Merging in the window"},
             {"t": "steps", "items": [
                 "Each row of the clustering window is one cluster, with its values, their row counts and a "
                 "text box for the new value.",
                 "Pick one of the listed values to apply to every cell in the cluster, or type the official "
                 "spelling into the text box, and mark the cluster for merging. Leave a cluster unmarked if its "
                 "values are different places.",
                 "Click <strong>Merge selected &amp; re-cluster</strong>. OpenRefine applies the merge and runs the "
                 "method again on what is left.",
                 "Change the method and keying function, and repeat. Close the window when nothing sensible is "
                 "left.",
             ]},
             {"t": "h3", "html": "N-gram fingerprint and transliteration variants"},
             {"t": "p", "html": "N-gram fingerprint lowercases the value, strips spaces and punctuation, cuts it into "
                                "overlapping pieces of <em>n</em> characters, and sorts the unique pieces. The cell "
                                "compares four pairs with <em>n</em> = 2."},
             py("ngram"),
             {"t": "p", "html": "All four pairs get <strong>different</strong> keys. <em>Kozhikkode</em> has a "
                                "doubled <em>k</em>, which adds the piece <code class=\"inline\">kk</code>; "
                                "<em>Purnea</em> has <code class=\"inline\">ea</code> where <em>Purnia</em> has "
                                "<code class=\"inline\">ia</code>. Key collision only clusters exact key matches, "
                                "so a single changed letter is enough to escape it."},
             {"t": "h3", "html": "Nearest neighbour for one-letter differences"},
             {"t": "p", "html": "Levenshtein distance counts single-character edits. OpenRefine's manual gives the "
                                "example that <em>New York</em> and <em>newyork</em> are 3 apart, so a change of case "
                                "counts as an edit. The cell compares every messy value against the ten official "
                                "names in <code class=\"inline\">districts.csv</code> with a radius of 2."},
             py("levenshtein"),
             {"t": "p", "html": "Radius 2 matches <em>Purnea, Kozhikkode, Badmer, Wayanadu, Waynad, Reewa, Indor</em> "
                                "and most of the space, case and punctuation variants at distance 1, and "
                                "<em>Baitul</em> to <em>Betul</em> and <em>Patna</em> with two trailing spaces at "
                                "distance 2. It misses <em>GAYA</em> and <em>PURNIA</em>, because four or five "
                                "capital letters are four or five edits; fingerprint had already caught those, which "
                                "is the reason to run fingerprint first. It cannot match <em>Calicut</em> to "
                                "<em>Kozhikode</em> at any sensible radius."},
             {"t": "info", "tone": "warning",
              "html": "<strong>Set the block size for short names.</strong> Before comparing pairs, OpenRefine groups "
                      "values into blocks that share a run of characters, 6 by default, and the manual recommends "
                      "at least 3. Rewa, Gaya and Patna are shorter than six letters, so with the default they may "
                      "never be compared at all. For district, block and village names, set the block size to 3 and "
                      "raise it only if the window fills with nonsense."},
             {"t": "h3", "html": "What clustering can and cannot do with Indian place names"},
             {"t": "ul", "items": [
                 "<strong>Case, spaces and punctuation</strong> (<em>GAYA, Patna&nbsp;&nbsp;, Udaipur.</em>): "
                 "fingerprint handles them safely.",
                 "<strong>One-letter transliteration differences</strong> (<em>Purnea/Purnia, Badmer/Barmer, "
                 "Kozhikkode/Kozhikode, Baitul/Betul</em>): these come from writing the same Hindi, Malayalam or "
                 "Bengali sound in Roman letters in different ways. Levenshtein at radius 1 or 2 finds most of them. "
                 "Check each one: at radius 2, two different villages can also fall together, and the "
                 "manual's own example is <em>M. Makeba</em> matching <em>B. Makeba</em>, another person.",
                 "<strong>Phonetic keys</strong>: the manual describes Metaphone3 as an English-language algorithm "
                 "and Cologne Phonetic as built for German. They may catch some vowel variants, but they were not "
                 "designed for Indian names, so read each cluster before you accept it.",
                 "<strong>Different names for one place</strong> (<em>Calicut/Kozhikode, Gurgaon/Gurugram, "
                 "Allahabad/Prayagraj</em>): no string method links them. Use a lookup table, or better, match on "
                 "the Census or LGD code instead of the name.",
                 "<strong>Names in two scripts</strong> (<em>&#x92a;&#x942;&#x930;&#x94d;&#x923;&#x93f;&#x92f;&#x93e;</em> "
                 "in one row, <em>Purnia</em> in another): the ASCII folding in fingerprint covers accented Western "
                 "letters only, and none of the methods transliterates Devanagari or any other Indian script into "
                 "Roman letters. Split such a column by script and map each against the official list.",
             ]},
             {"t": "p", "html": "The cell below writes down what you would decide in the clustering window as a "
                                "mapping, applies it, and checks the result against the official list."},
             py("merge"),
             {"t": "p", "html": "After the merges, one value remains outside <code class=\"inline\">districts.csv"
                                "</code>: <em>Calicut</em>, 2 rows. That is the colonial-era name for Kozhikode, "
                                "and the cell in module 8 maps it with an explicit lookup."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the Levenshtein cell, change "
                                   "<code class=\"inline\">radius = 2</code> to <code class=\"inline\">radius = 1</code> "
                                   "and run again. Which two matches disappear? Then try <code class=\"inline\">radius = 3"
                                   "</code> and look for a match you would refuse."},
         ]},
        {"tab": "GREL",
         "title": "Transform cells with GREL",
         "blocks": [
             {"t": "p", "html": "GREL (General Refine Expression Language) is OpenRefine's formula language. In an "
                                "expression, <code class=\"inline\">value</code> is the current cell. Open "
                                "<strong>Edit cells &rarr; Transform&hellip;</strong> on a column, type an expression, "
                                "and the window shows a preview of the first rows before you apply it. The "
                                "functions below are from the " + link("https://openrefine.org/docs/manual/grelfunctions",
                                "GREL functions reference") + "."},
             {"t": "syntax", "label": "GREL: tidy a name column",
              "code": 'value.trim()\nvalue.toTitlecase()\nvalue.trim().toTitlecase()'},
             {"t": "p", "html": "<code class=\"inline\">trim()</code> removes leading and trailing spaces and "
                                "<code class=\"inline\">toTitlecase()</code> capitalises the first letter of each "
                                "word. You can chain them. The same two fixes are also on the menu, under "
                                "<strong>Edit cells &rarr; Common transforms</strong> (Trim leading and trailing "
                                "whitespace; Case transforms)."},
             {"t": "syntax", "label": "GREL: numbers stored as text",
              "code": 'value.replace(",", "").toNumber()'},
             {"t": "p", "html": "<code class=\"inline\">replace(find, replacement)</code> removes the thousands "
                                "comma; <code class=\"inline\">toNumber()</code> converts the result to a number. A "
                                "cell that still cannot be converted, such as <em>not asked</em>, stays as it was, "
                                "which the numeric facet will show as non-numeric."},
             py("grel"),
             {"t": "p", "html": "Trim and title case take the district column from <strong>29 distinct values to "
                                "20</strong>. Removing commas takes the non-numeric expenditure cells from "
                                "<strong>18 to 6</strong>, and the six left all say <em>not asked</em>. Those are "
                                "missing values, and they should stay missing: do not type a zero."},
             {"t": "syntax", "label": "GREL: more expressions you will use",
              "code": ('value.fingerprint()\n'
                       'value.split(",")[0]\n'
                       'if(value == null, "missing", value)\n'
                       'cells["district"].value + ", " + cells["area"].value')},
             {"t": "ul", "items": [
                 "<code class=\"inline\">value.fingerprint()</code> in <strong>Edit column &rarr; Add column based "
                 "on this column&hellip;</strong> puts each cell's fingerprint key in a new column, so you can see "
                 "why two values clustered.",
                 "<code class=\"inline\">value.split(\",\")[0]</code> keeps the part before the first comma.",
                 "<code class=\"inline\">if(value == null, \"missing\", value)</code> labels empty cells.",
                 "<code class=\"inline\">cells[\"district\"].value</code> reads another column in the same row, so "
                 "the last line builds a combined label.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> In the Python cell, delete "
                                   "<code class=\"inline\">.str.title()</code> from the second line and run again. "
                                   "How many distinct values are left with only the trim?"},
         ]},
        {"tab": "Columns",
         "title": "Split and join columns",
         "blocks": [
             {"t": "p", "html": "MIS exports often pack two facts into one column (\"Gaya, Bihar\") or spread one "
                                "fact across several. OpenRefine's column menu handles both, as described in the "
                                + link("https://openrefine.org/docs/manual/columnediting", "column editing manual") + "."},
             {"t": "h3", "html": "Split one column into several"},
             {"t": "steps", "items": [
                 "On the <code class=\"inline\">location</code> column, choose <strong>Edit column &rarr; Split into "
                 "several columns&hellip;</strong>",
                 "Choose <strong>by separator</strong> and type a comma followed by a space.",
                 "Choose whether to remove the original column, and click OK.",
             ]},
             {"t": "h3", "html": "Join several columns into one"},
             {"t": "steps", "items": [
                 "Choose <strong>Edit column &rarr; Join columns&hellip;</strong> from any column.",
                 "Tick the columns to join (here <code class=\"inline\">area</code> and "
                 "<code class=\"inline\">caste</code>) and drag them into order.",
                 "Type a separator, for example <code class=\"inline\"> | </code>, and choose whether the result "
                 "goes into the selected column or a new one.",
             ]},
             py("split"),
             {"t": "p", "html": "The split gives a second column holding the state, with 72 rows each for Madhya "
                                "Pradesh and Bihar and 48 each for Rajasthan and Kerala. The joined "
                                "<em>area | caste</em> column is a quick cross-tab: Rural | OBC is the largest "
                                "group with 71 households."},
             {"t": "h3", "html": "Multi-valued cells are a different operation"},
             {"t": "p", "html": "If a cell holds a list, such as the schemes a household receives "
                                "(\"PDS; MGNREGA; PM-KISAN\"), use <strong>Edit cells &rarr; Split multi-valued "
                                "cells&hellip;</strong>. That puts each item on its own row under the same record, "
                                "so you can facet by scheme. <strong>Edit cells &rarr; Join multi-valued "
                                "cells&hellip;</strong> puts them back."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the Python cell, change the join to "
                                   "<code class=\"inline\">raw[\"area\"] + \" | \" + raw[\"caste\"]</code> &rarr; "
                                   "<code class=\"inline\">raw[\"caste\"] + \" | \" + raw[\"area\"]</code> and run. The "
                                   "counts do not change; only the label order does."},
         ]},
        {"tab": "Reconcile",
         "title": "Reconciliation, in outline",
         "blocks": [
             {"t": "p", "html": "Clustering makes a column consistent with itself. <strong>Reconciliation</strong> "
                                "matches it against an outside list and attaches that list's identifier to each "
                                "cell. For a district column, the useful identifier is an official code that does "
                                "not change when the spelling does."},
             {"t": "steps", "items": [
                 "On the column, choose <strong>Reconcile &rarr; Start reconciling&hellip;</strong>",
                 "The window offers <strong>Wikidata</strong> as a built-in service. To use another, click "
                 "<strong>Add Standard Service&hellip;</strong> and paste the service's address.",
                 "Pick a type if the service offers types (for a district column, a type meaning \"district of "
                 "India\" narrows the candidates), and start. Each cell gets a best match, a list of candidates, or "
                 "nothing.",
                 "Facet on the reconciliation results to review the uncertain ones, and match them by hand.",
             ]},
             {"t": "p", "html": "The " + link("https://openrefine.org/docs/manual/reconciling", "reconciling manual")
                                + " also mentions <em>reconcile-csv</em>, a small tool that builds a reconciliation "
                                "service from a CSV file. That suits the usual MIS case: reconcile your messy village "
                                "column against the official list your programme already holds, with its codes. If "
                                "you already have identifiers in a column, <strong>Reconcile &rarr; Use values as "
                                "identifiers</strong> links them directly."},
             {"t": "info", "tone": "warning",
              "html": "<strong>Reconciliation leaves your computer.</strong> The values in the column are sent to the "
                      "service. Reconciling district names against Wikidata is harmless; reconciling a column of "
                      "beneficiary names is not. Under India's Digital Personal Data Protection Act 2023, check what "
                      "your consent notice and data-sharing agreements allow before any personal data goes to an "
                      "outside service."},
             {"t": "p", "html": "Without a service, the same idea is a join on a lookup table. The Python cell in "
                                "the next module maps <em>Calicut</em> to <em>Kozhikode</em> that way and then "
                                "refuses to finish if any district is still unknown."},
         ]},
        {"tab": "History",
         "title": "Undo, replay the cleaning, and export",
         "blocks": [
             {"t": "h3", "html": "Undo / Redo"},
             {"t": "p", "html": "Click the <strong>Undo / Redo</strong> tab in the left panel. It lists every change "
                                "in order, starting with step 0, <em>Create project</em>, which cannot be undone. "
                                "Click any earlier step to go back to it; the later steps stay in the list, greyed out, "
                                "and you can click forward again. If you make a new change while stepped back, the "
                                "greyed steps are erased for good, so step forward again before carrying on."},
             {"t": "h3", "html": "Extract the operation history as JSON"},
             {"t": "steps", "items": [
                 "In the Undo / Redo tab, click <strong>Extract&hellip;</strong>",
                 "A box lists every operation up to the current state. Tick the ones you want; they appear as "
                 "JSON on the right.",
                 "Copy the JSON and save it as a text file next to your data, for example "
                 "<code class=\"inline\">clean_households.json</code>. That file is your cleaning recipe.",
                 "Next month, create a project from the new export, open Undo / Redo, click "
                 "<strong>Apply&hellip;</strong>, paste the JSON, and every step runs again.",
             ]},
             {"t": "p", "html": "The manual notes that not every operation can be extracted: edits to a single cell "
                                "cannot be replayed. Do one-off corrections with a GREL expression or a cluster merge, "
                                "so they go into the recipe. Read the JSON before you rely on it: you should find your "
                                "column names and your GREL expressions written out in it."},
             {"t": "h3", "html": "The same idea in Python"},
             {"t": "p", "html": "A cleaning recipe written as code does the same job and can be checked. This cell "
                                "puts all the steps from this course into one function and stops with an error if a "
                                "district is still unknown."},
             py("recipe"),
             {"t": "p", "html": "The result has 240 rows and 6 columns, exactly 24 households in each of the ten "
                                "districts, and 6 missing expenditure values (the <em>not asked</em> cells), and it "
                                "reads back from the saved file with the same shape."},
             {"t": "info", "html": "<strong>Exercise.</strong> Delete the <code class=\"inline\">\"Calicut\": "
                                   "\"Kozhikode\"</code> entry from the lookup and run again. The "
                                   "<code class=\"inline\">assert</code> line stops the run and names the unknown "
                                   "district. A recipe that fails loudly on a new spelling is better than one that "
                                   "lets it through."},
             {"t": "h3", "html": "Export"},
             {"t": "p", "html": "The <strong>Export</strong> button at the top right offers, among others: "
                                "comma- or tab-separated values, an HTML table, Excel (XLS or XLSX), ODS, a custom "
                                "tabular exporter, an SQL statement exporter and a templating exporter for JSON. "
                                "The " + link("https://openrefine.org/docs/manual/exporting", "exporting manual") + " "
                                "warns that many of these export only the rows in the current view, with your facets "
                                "applied, so clear facets before exporting the full file. "
                                "<strong>Export &rarr; OpenRefine project archive to file</strong> saves the whole project "
                                "with its history as a .tar.gz file that another OpenRefine can import."},
             {"t": "info", "tone": "warning",
              "html": "<strong>A project archive keeps every earlier state.</strong> The exporting manual warns "
                      "that project archives contain the data from previous steps. If you removed names or phone "
                      "numbers in OpenRefine, anyone with the archive can step back to them. Share the exported CSV "
                      "and the extracted JSON recipe, and keep the archive to yourself."},
         ]},
    ],
    "next": [
        {"href": "/code/pandas.html", "title": "pandas for development data",
         "desc": "Write the same cleaning as Python code, then summarise and merge."},
        {"href": "/code/open-data-editor.html", "title": "Open Data Editor",
         "desc": "Check a cleaned file for structural errors before you share it."},
        {"href": "/code/qgis.html", "title": "QGIS: maps for development data",
         "desc": "Clean district names are what make a map join work."},
        {"href": "/101-courses/data-lit.html", "title": "Data Literacy 101",
         "desc": "The ideas behind tidy, trustworthy data."},
        {"href": "/101-courses/data-protection-dpdp.html", "title": "Data Protection and the DPDP Act",
         "desc": "What you may do with personal data in survey and MIS files."},
    ],
}

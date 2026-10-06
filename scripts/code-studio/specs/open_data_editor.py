# -*- coding: utf-8 -*-
"""Open Data Editor: Checking a Dataset Before You Share It. A guided tool course with Python cells that run the
same checks on the page.

Facts checked on 6 October 2026 against the Open Data Editor documentation (opendataeditor.okfn.org), the OKFN
project page, the opendataeditor GitHub repository (README, LICENSE, releases) and the Data Package Table Schema
standard (datapackage.org). Sources are listed in the agent report.
"""

DL = '<a href="/code/data/households.csv" download style="color:var(--accent-color)">households.csv</a>'
DD = '<a href="/code/data/districts.csv" download style="color:var(--accent-color)">districts.csv</a>'
A = 'style="color:var(--accent-color)"'


def link(href, text):
    return '<a href="%s" rel="noopener" target="_blank" %s>%s</a>' % (href, A, text)


CHECK = '''import csv, io

def check_table(text):
    """Report the structural errors Open Data Editor's guide lists, in its own words."""
    rows = list(csv.reader(io.StringIO(text)))
    header, data = rows[0], rows[1:]
    errors = []
    if all(h.strip() == "" for h in header):
        errors.append(("Header missing (Blank Label)", 1, None))
    for c, h in enumerate(header, 1):
        if h.strip() == "":
            errors.append(("Column name missing", 1, c))
        elif [x.strip() for x in header].count(h.strip()) > 1:
            errors.append(("Duplicate column name: " + h, 1, c))
    for r, row in enumerate(data, 2):
        if all(x.strip() == "" for x in row):
            errors.append(("Empty row", r, None))
        elif len(row) < len(header):
            errors.append(("Missing cell", r, len(row) + 1))
        elif len(row) > len(header):
            errors.append(("Extra cell", r, len(header) + 1))
    # Wrong data type: a column that is mostly whole numbers, with a cell that is not
    for c in range(len(header)):
        vals = [(r, row[c]) for r, row in enumerate(data, 2) if c < len(row) and row[c].strip() != ""]
        ints = [v for _, v in vals if v.strip().lstrip("-").isdigit()]
        if vals and len(ints) >= 0.8 * len(vals):
            for r, v in vals:
                if not v.strip().lstrip("-").isdigit():
                    errors.append(("Wrong data type: " + repr(v), r, c + 1))
    return errors
'''

C = {}
C["broken"] = CHECK + '''
BROKEN = """hh_id,district,area,,monthly_pc_exp,area
1,Rewa,Urban,4,3210,Urban
2,Rewa,Rural,6,2230,Rural
,,,,,
3,Rewa,Rural,3,1670
4,Rewa,Rural,5,2100,Rural,yes
5,Rewa,Rural,4,"2,080",Rural
6,Rewa,Rural,7,3140,Rural
"""
for err, row, col in check_table(BROKEN):
    print(f"row {row}", f"col {col}" if col else "     ", err)

print()
with open("households.csv") as f:
    found = check_table(f.read())
print("households.csv:", len(found), "errors")'''

C["schema"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
districts = pd.read_csv("districts.csv")

# Rules of the kind you set in a Table Schema: required, unique, enum, minimum, maximum, foreign key
def check_rules(df):
    out = []
    dup = df["hh_id"][df["hh_id"].duplicated()]
    out += [("Primary key error: hh_id not unique", v) for v in dup]
    bad = df.loc[~df["district"].isin(districts["district"]), "district"]
    out += [("Foreign key error: district not in districts.csv", v) for v in bad]
    bad = df.loc[~df["area"].isin(["Rural", "Urban"]), "area"]
    out += [("Constraint error: area not in [Rural, Urban]", v) for v in bad]
    bad = df.loc[(df["hh_size"] < 1) | (df["hh_size"] > 20), "hh_size"]
    out += [("Constraint error: hh_size outside 1 to 20", v) for v in bad]
    bad = df.loc[df["monthly_pc_exp"].isna(), "hh_id"]
    out += [("Constraint error: monthly_pc_exp is required", f"hh_id {v}") for v in bad]
    return out

print("households.csv:", len(check_rules(hh)), "rule errors")

# A copy with four mistakes typed in by hand
bad = hh.copy()
bad.loc[5, "hh_id"] = 5                  # row 6 reuses hh_id 5
bad.loc[30, "district"] = "Gaya "        # trailing space
bad.loc[31, "area"] = "rural"            # lower case
bad.loc[40, "hh_size"] = 0
bad.loc[41, "monthly_pc_exp"] = None
for rule, value in check_rules(bad):
    print(rule, "->", repr(value))'''

C["descriptor"] = '''import json
import pandas as pd
districts = pd.read_csv("districts.csv")

schema = {
    "fields": [
        {"name": "hh_id", "type": "integer", "constraints": {"required": True, "unique": True}},
        {"name": "district", "type": "string",
         "constraints": {"required": True, "enum": sorted(districts["district"])}},
        {"name": "area", "type": "string", "constraints": {"enum": ["Rural", "Urban"]}},
        {"name": "hh_size", "type": "integer", "constraints": {"minimum": 1, "maximum": 20}},
        {"name": "monthly_pc_exp", "type": "number", "title": "Monthly per capita expenditure (Rs)",
         "constraints": {"required": True, "minimum": 0}},
    ],
    "primaryKey": ["hh_id"],
    "missingValues": [""],
}
text = json.dumps(schema, indent=2)
print(text)
with open("households.schema.json", "w") as f:
    f.write(text)
print(len(schema["fields"]), "fields written to households.schema.json")'''

C["dictionary"] = '''import pandas as pd
hh = pd.read_csv("households.csv")

# A one-line-per-column data dictionary to send with the file
dd = pd.DataFrame({
    "column": hh.columns,
    "type": [str(t) for t in hh.dtypes],
    "missing": hh.isna().sum().values,
    "distinct": hh.nunique().values,
    "example": [hh[c].iloc[0] for c in hh.columns],
})
print(dd.to_string(index=False))
dd.to_csv("households_dictionary.csv", index=False)'''


def py(key):
    return {"t": "code", "lang": "py", "pkgs": "pandas", "code": C[key]}


PAGE = {
    "slug": "open-data-editor",
    "order": 14,
    "kind": "guide",
    "tool": "Open Data Editor",
    "title": "Open Data Editor: Checking a Dataset Before You Share It",
    "h1": "Open Data Editor: checking a dataset before you share it",
    "lede": ("Before a survey file or MIS extract goes to a partner, a portal or a funder, check that its structure "
             "holds: one name per column, the same number of cells in every row, numbers where numbers belong, "
             "and the rules you promised (unique IDs, allowed values). Open Data Editor does these checks without "
             "code, on your own computer. Python cells on this page run the same checks so you can see what each "
             "error means."),
    "description": ("A free guided course in the Open Knowledge Foundation's Open Data Editor for development "
                    "practitioners in South Asia: install it, open a CSV, read its error report, fix errors, add "
                    "metadata and Table Schema rules, export a clean file, and know what it can and cannot do."),
    "card": "A no-code check of a CSV before you share it: error report, fixes, metadata rules and export.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>Open Data Editor is a desktop application.</strong> It does not run on this page. "
                    "The steps tell you what to click and what to look for; this page does not show Open Data "
                    "Editor screens, because it cannot produce them. The Python cells run equivalent checks here "
                    "with pandas and Python's csv module, so you can see each kind of error on a small file. The "
                    "first Python run downloads the engine once (about 10&nbsp;MB)."),
    "modules": [
        {"tab": "What it is",
         "title": "What Open Data Editor is, and its status",
         "blocks": [
             {"t": "p", "html": "Open Data Editor (ODE) is made by the Open Knowledge Foundation (OKFN). Its "
                                "documentation describes it as \"a free, open-source tool designed to help "
                                "nonprofits, data journalists, activists, and public servants detect errors in "
                                "their datasets\", for people who work with tables in Excel, Google Sheets or CSV "
                                "and do not write code. It checks files against the rules of the Frictionless "
                                "framework, an open standard for describing tables, and the OKFN page says the "
                                "Digital Public Goods Alliance has recognised it as a digital public good since "
                                "2025."},
             {"t": "info", "html": "<strong>Version and status, checked 6 October 2026.</strong> The latest "
                                   "release on " + link("https://github.com/okfn/opendataeditor/releases",
                                   "ODE's GitHub releases page") + " is <strong>v1.8.0</strong>, published 17 "
                                   "September 2026; the previous one, v1.7.1, came out on 23 October 2025. The "
                                   "user guide at " + link("https://opendataeditor.okfn.org/", "opendataeditor.okfn.org")
                                   + " is headed \"Open Data Editor 1.5.1 documentation\", so it trails the "
                                   "software by several releases: if a button on your screen differs from these "
                                   "steps, trust your screen. The repository README still titles the project "
                                   "\"Open Data Editor (beta)\". The source code is under the <strong>MIT "
                                   "licence</strong> and the application is free."},
             {"t": "h3", "html": "What it does well"},
             {"t": "ul", "items": [
                 "Finds structural errors as soon as you open a file: missing or duplicate column names, empty "
                 "rows, rows with too few or too many cells, and cells of the wrong type.",
                 "Checks rules you add as metadata: a column must be filled in, unique, one of a list of values, "
                 "within a range, or match a pattern.",
                 "Lets you fix cells in a grid and re-check, then export the file, or an Excel workbook listing every "
                 "error.",
                 "Works locally. Its documentation calls it local-first, and the optional AI assistant uses a model "
                 "downloaded to your computer; the documentation says no data is sent to the cloud.",
             ]},
             {"t": "h3", "html": "What it is not"},
             {"t": "p", "html": "It is not a cleaning tool in the OpenRefine sense: it shows you that "
                                "<em>Purnea</em> and <em>Purnia</em> both appear only if you have told it which "
                                "values are allowed, and it does not cluster or bulk-merge them. Use "
                                "<a href=\"/code/openrefine.html\" " + A + ">OpenRefine</a> to clean, and Open Data "
                                "Editor to check the result before it leaves your hands."},
         ]},
        {"tab": "Install",
         "title": "Download and install",
         "blocks": [
             {"t": "p", "html": "The " + link("https://opendataeditor.okfn.org/user-guide/downloading-ode.html",
                                "download guide") + " offers one file per system, from the "
                                + link("https://okfn.org/en/projects/open-data-editor/", "OKFN project page") +
                                " or from GitHub releases:"},
             {"t": "ul", "items": [
                 "<strong>Windows:</strong> the most recent EXE file.",
                 "<strong>macOS:</strong> the most recent DMG file.",
                 "<strong>Linux:</strong> an AppImage (any distribution) or a DEB file (Ubuntu and Debian).",
             ]},
             {"t": "steps", "items": [
                 "Windows: download the EXE. If the browser warns about the download, choose to keep it "
                 "(the guide shows a \"Continue download\" prompt). Double-click it. If Windows shows a security "
                 "window, click <strong>More info</strong>, then <strong>Run anyway</strong>.",
                 "macOS: open the DMG. If macOS shows a security message, the guide says to click the question mark "
                 "in it, follow the link in the first section, and change the setting that allows the app to "
                 "run.",
                 "Linux AppImage: make the file executable (in a terminal, <code class=\"inline\">chmod +x</code> "
                 "followed by the file name), then double-click it.",
                 "Ubuntu or Debian DEB: double-click it, or install it from a terminal with the command below.",
             ]},
             {"t": "syntax", "label": "Terminal (Debian or Ubuntu), from the ODE install guide",
              "code": "# Replace <version> with the version you downloaded\nsudo dpkg -i opendataeditor-linux-<version>.deb"},
             {"t": "info", "html": "<strong>On a modest laptop.</strong> The checks themselves are light. The "
                                   "optional AI assistant is not: the GitHub README says its default model, "
                                   "Apertus 8B (Apache 2.0 licence), \"requires at least 6GB of video memory\", "
                                   "and the model is a separate download that ODE offers the first time you press "
                                   "the AI button. Skip it on a machine without a graphics card; nothing else "
                                   "depends on it."},
         ]},
        {"tab": "Open a file",
         "title": "Open a CSV",
         "blocks": [
             {"t": "p", "html": "Download the two course files: " + DL + " (240 households) and " + DD + " (10 "
                                "districts). <span class=\"illustrative-tag\">Illustrative data, invented for "
                                "teaching</span> The district names are real places; every number is made up."},
             {"t": "steps", "items": [
                 "Open Open Data Editor and click <strong>Upload your data</strong> (in the centre of the start "
                 "screen, or at the top left of the sidebar).",
                 "Under <strong>From your computer</strong>, choose <strong>Add one or more Excel or csv "
                 "files</strong> and select <code class=\"inline\">households.csv</code>. To check a whole folder "
                 "of files, use <strong>Add one or more folders</strong>.",
                 "The file appears in the sidebar. Click it: ODE validates it and shows it in the grid.",
             ]},
             {"t": "info", "html": "<strong>ODE works on a copy.</strong> The upload guide says ODE does not change "
                                   "your original file: it copies it into the application's own folder. "
                                   "Right-click the file in the sidebar and choose <strong>Open Location</strong> "
                                   "to see where the copy lives. Your edits go to that copy, so export it when you "
                                   "are done (module 7)."},
             {"t": "h3", "html": "Tables published online"},
             {"t": "p", "html": "Under <strong>Add External Data</strong> you can paste the address of a table on "
                                "an open data portal, a Google Sheet or a GitHub repository. For a Google Sheet, the "
                                "guide says the sheet must be published to the web and you should paste its normal "
                                "address, the one ending in <code class=\"inline\">/edit</code>. The guide marks the published "
                                "<code class=\"inline\">pubhtml</code> address as the wrong one to use."},
             {"t": "h3", "html": "Prepare the file before you open it"},
             {"t": "ul", "items": [
                 "One header row of column names, starting in the first row. Remove titles, notes, logos and "
                 "totals above or beside the table; the guide warns that these produce many errors.",
                 "No merged cells.",
                 "Decimals written with a full stop. The guide warns that a comma as decimal separator makes the "
                 "number column read as text.",
             ]},
         ]},
        {"tab": "Errors",
         "title": "The errors it reports",
         "blocks": [
             {"t": "p", "html": "A file with problems gets a <strong>red dot</strong> beside its name in the "
                                "sidebar, and problem cells are shaded red in the grid. Click "
                                "<strong>Errors Report</strong> at the top left of the grid for the full list. The "
                                + link("https://opendataeditor.okfn.org/user-guide/full-list-of-table-errors-detected.html",
                                       "full list of errors") + " names seven it finds without any metadata:"},
             {"t": "ul", "items": [
                 "<strong>Header missing (Blank Label)</strong>: the header row is empty.",
                 "<strong>Column name missing</strong>: one or more columns have no name.",
                 "<strong>Duplicate column name</strong>: two columns share a name.",
                 "<strong>Empty row</strong>: a row with no values.",
                 "<strong>Missing cell</strong>: a row has fewer cells than the header.",
                 "<strong>Extra cell</strong>: a row has more cells than the header.",
                 "<strong>Wrong data type</strong>: a cell does not fit the column's type, such as text in a "
                 "column of numbers. The guide notes ODE can only infer the intended type when enough cells in "
                 "the column already have it.",
             ]},
             {"t": "p", "html": "The cell below builds a small broken file with five of those problems, checks it "
                                "with a short function written for this course (not ODE's own code), and then "
                                "checks the real <code class=\"inline\">households.csv</code>."},
             py("broken"),
             {"t": "p", "html": "The broken file produces seven errors: column 4 has no name, "
                                "<code class=\"inline\">area</code> appears twice (columns 3 and 6), row 4 is empty, "
                                "row 5 is missing a cell, row 6 has an extra one, and in row 7 "
                                "<code class=\"inline\">\"2,080\"</code> is text in a column of whole numbers. "
                                "<code class=\"inline\">households.csv</code> has 0 errors. To see the same file in ODE, "
                                "copy the eight lines between the triple quotes into a text editor, save them as "
                                "<code class=\"inline\">broken.csv</code> and upload it: its Errors Report should "
                                "point to the same rows and columns."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the cell, delete the line "
                                   "<code class=\"inline\">,,,,,</code> and run again. Which error disappears, and "
                                   "which row numbers move?"},
         ]},
        {"tab": "Fix",
         "title": "Fix errors and re-check",
         "blocks": [
             {"t": "p", "html": "For a handful of bad cells, fix them in ODE's grid, following the "
                                + link("https://opendataeditor.okfn.org/user-guide/editing-errors-in-tables.html",
                                       "editing guide") + ":"},
             {"t": "steps", "items": [
                 "Find the red cell (the Errors Report lists its row and column).",
                 "Double-click it and type the corrected value.",
                 "Click elsewhere in the table to accept the change.",
                 "Click <strong>Save changes</strong>, which becomes active when there are unsaved edits. ODE "
                 "re-validates and updates the Errors Report.",
             ]},
             {"t": "h3", "html": "Know when to stop editing by hand"},
             {"t": "ul", "items": [
                 "<strong>Structural errors</strong> (missing or extra cells, a blank or duplicate column name) "
                 "usually come from how the file was exported: a stray comma inside an unquoted text field, a "
                 "notes column, two tables in one sheet. Fix the export and export again; patching rows by "
                 "hand leaves the cause in place for next month.",
                 "<strong>Many wrong-type cells in one column</strong> (\"2,080\", \"NA\", \"not asked\") are a "
                 "cleaning job. Do it in OpenRefine or in code, where the step is recorded and can be repeated.",
                 "<strong>A wrong value that is the right type</strong>, such as a household size of 0, passes "
                 "every check in module 4. Only a rule catches it, which is what module 6 adds.",
             ]},
             {"t": "info", "tone": "warning",
              "html": "<strong>Do not invent a value to clear an error.</strong> If an expenditure cell says "
                      "\"not asked\", the honest fix is an empty cell (missing). Do not type a zero or the column mean. "
                      "A clean report on a file with made-up values is worse than a report with errors."},
         ]},
        {"tab": "Metadata",
         "title": "Metadata and rules",
         "blocks": [
             {"t": "p", "html": "Metadata is the description that travels with the file: a title, what each "
                                "column means, its type, and the rules its values must follow. In ODE, select a "
                                "file and click any cell of the header row to open the <strong>Metadata</strong> "
                                "window; edit, then click <strong>Save changes</strong>, which re-validates the "
                                "file."},
             {"t": "p", "html": "The rules follow the " + link("https://datapackage.org/standard/table-schema/",
                                "Table Schema standard") + ". ODE's error guide says it supports these field "
                                "constraints: <code class=\"inline\">required</code>, "
                                "<code class=\"inline\">enum</code> (a list of allowed values), "
                                "<code class=\"inline\">minimum</code>, <code class=\"inline\">maximum</code>, "
                                "<code class=\"inline\">minLength</code>, <code class=\"inline\">maxLength</code> "
                                "and <code class=\"inline\">pattern</code>, plus <code class=\"inline\">unique</code>, "
                                "a primary key and foreign keys. With them it can report seven more errors: extra, "
                                "missing and incorrect column names against the schema, and primary key, foreign "
                                "key, unique and constraint errors."},
             {"t": "p", "html": "The cell below writes rules of that kind for the household file and applies them, "
                                "first to <code class=\"inline\">households.csv</code> and then to a copy with five "
                                "mistakes typed in."},
             py("schema"),
             {"t": "p", "html": "The real file breaks no rule. The copy breaks all five, and each one is a mistake "
                                "that no structural check sees: a repeated ID, <em>Gaya</em> with a trailing space "
                                "(not in <code class=\"inline\">districts.csv</code>), <em>rural</em> in lower case, "
                                "a household of 0 people, and a blank expenditure."},
             {"t": "h3", "html": "The rules as a Table Schema"},
             {"t": "p", "html": "Written in the standard's JSON form, the same rules look like this. A partner with "
                                "any Frictionless tool can check your file against it."},
             py("descriptor"),
             {"t": "info", "html": "<strong>Exercise.</strong> In the rules cell, change <code class=\"inline\">&gt; 20</code> "
                                   "to <code class=\"inline\">&gt; 6</code> and run. The real file now fails on "
                                   "every household of 7 or 8 people. Those households are real; the rule was "
                                   "wrong. Set limits from what is possible in the population; the largest value "
                                   "in one file is a poor guide."},
         ]},
        {"tab": "Export",
         "title": "Export, share and publish",
         "blocks": [
             {"t": "p", "html": "Click <strong>Export</strong> at the top right of the grid. The "
                                + link("https://opendataeditor.okfn.org/user-guide/exporting-your-data.html",
                                       "export guide") + " lists two options:"},
             {"t": "ul", "items": [
                 "<strong>Download file</strong>: the table as CSV.",
                 "<strong>Download file with errors</strong>: an Excel workbook with three sheets. "
                 "<em>Data</em> is the table with errors painted red, <em>Errors Description</em> lists each error "
                 "with its row and column, and <em>Blank Rows</em> holds the rows that had no values. Send this to "
                 "the person who produced the file: it tells them exactly what to fix.",
             ]},
             {"t": "h3", "html": "Publishing"},
             {"t": "p", "html": "The README describes ODE as an application to \"explore, validate and publish "
                                "data\", but the current user guide (checked 6 October 2026) has no section on "
                                "publishing to a data portal: its last step is export. So publish the exported CSV "
                                "through your portal's own upload page (a CKAN portal, Zenodo, your organisation's "
                                "repository), and attach the data dictionary and the schema. If your installed "
                                "version shows a publish option, check its destination before you use it."},
             py("dictionary"),
             {"t": "p", "html": "The dictionary has one row per column of the household file (13 rows), with each "
                                "column's type, its count of missing values (0 in this file), how many distinct "
                                "values it holds and an example. Save it next to the CSV."},
             {"t": "h3", "html": "A checklist before the file leaves your computer"},
             {"t": "ul", "items": [
                 "The Errors Report is empty, or every remaining error is explained in a note.",
                 "No column holds names, phone numbers, Aadhaar numbers, exact addresses or GPS points unless "
                 "sharing them is allowed. India's Digital Personal Data Protection Act 2023 governs personal data "
                 "in digital form; check your consent notice and data-sharing agreement before you share.",
                 "Small cells are safe: a table of caste by village with 1 or 2 households in a cell can identify "
                 "families even without names.",
                 "The data dictionary and the schema go with the file, along with who collected it, when, and "
                 "the licence you are publishing under.",
             ]},
         ]},
    ],
    "next": [
        {"href": "/code/openrefine.html", "title": "OpenRefine: cleaning messy survey and MIS data",
         "desc": "Clean the file first: facets, clustering and a replayable recipe."},
        {"href": "/code/qgis.html", "title": "QGIS: maps for development data",
         "desc": "Put the checked district file on a map."},
        {"href": "/code/pandas.html", "title": "pandas for development data",
         "desc": "Write checks like these as code you can run on every new export."},
        {"href": "/101-courses/data-protection-dpdp.html", "title": "Data Protection and the DPDP Act",
         "desc": "What you may share, with whom, and on what basis."},
        {"href": "/101-courses/data-lit.html", "title": "Data Literacy 101",
         "desc": "Why a well-described table is worth more than a large one."},
    ],
}

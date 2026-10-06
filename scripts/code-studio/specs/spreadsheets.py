# -*- coding: utf-8 -*-
"""Spreadsheets for M&E: a guided tool course in Excel and Google Sheets formulas, with R and Python cells that
compute the same numbers on households.csv so learners can check their spreadsheet answers.

Facts checked on 6 October 2026 against support.microsoft.com (XLOOKUP, VLOOKUP, SUMIFS, SUMPRODUCT, data
validation, PivotTable, conditional formatting, merge cells, DATEDIF, specifications and limits) and
support.google.com (XLOOKUP, data validation, pivot tables, conditional formatting, version history, Drive file
limits). Sources are listed in the agent report.
"""

A = 'style="color:var(--accent-color)"'


def link(href, text):
    return '<a href="%s" rel="noopener" target="_blank" %s>%s</a>' % (href, A, text)


def IC(s):
    return '<code class="inline">%s</code>' % s


DL = '<a href="/code/data/households.csv" download %s>households.csv</a>' % A
DD = '<a href="/code/data/districts.csv" download %s>districts.csv</a>' % A

R, P = {}, {}

R["shape"] = '''hh <- read.csv("households.csv")
dim(hh)                         # rows, columns
names(hh)
sum(duplicated(hh$hh_id))       # repeated IDs: should be 0
sapply(hh, class)               # what each column holds'''
P["shape"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
print(hh.shape)                         # rows, columns
print(list(hh.columns))
print(hh["hh_id"].duplicated().sum())   # repeated IDs: should be 0
print(hh.dtypes)                        # what each column holds'''

R["lists"] = '''hh <- read.csv("households.csv")
# The values each dropdown (List) validation should allow
for (v in c("district", "area", "caste", "head_gender", "has_toilet")) {
  cat(v, ":", paste(sort(unique(hh[[v]])), collapse = ", "), "\\n")
}
# The ranges for whole-number and decimal rules
sapply(hh[, c("head_edu_years", "hh_size", "monthly_pc_exp", "land_acres")], range)'''
P["lists"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
# The values each dropdown (List) validation should allow
for v in ["district", "area", "caste", "head_gender", "has_toilet"]:
    print(v, ":", ", ".join(sorted(hh[v].unique())))
# The ranges for whole-number and decimal rules
print(hh[["head_edu_years", "hh_size", "monthly_pc_exp", "land_acres"]].agg(["min", "max"]))'''

R["lookup"] = '''hh <- read.csv("households.csv")
d  <- read.csv("districts.csv")
# XLOOKUP / INDEX-MATCH / VLOOKUP(..., FALSE): bring each district's state into the household sheet
hh$state <- d$state[match(hh$district, d$district)]
table(hh$state, useNA = "ifany")

# One district typed differently, as happens in a merged MIS export
hh$district[hh$hh_id == 100] <- "Purnea"
hh$state <- d$state[match(hh$district, d$district)]
sum(is.na(hh$state))                    # rows where an exact lookup finds nothing (#N/A)
hh[is.na(hh$state), c("hh_id", "district")]'''
P["lookup"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
d = pd.read_csv("districts.csv")
# XLOOKUP / INDEX-MATCH / VLOOKUP(..., FALSE): bring each district's state into the household sheet
state = dict(zip(d["district"], d["state"]))
hh["state"] = hh["district"].map(state)
print(hh["state"].value_counts(dropna=False).sort_index())

# One district typed differently, as happens in a merged MIS export
hh.loc[hh["hh_id"] == 100, "district"] = "Purnea"
hh["state"] = hh["district"].map(state)
print(hh["state"].isna().sum())          # rows where an exact lookup finds nothing (#N/A)
print(hh.loc[hh["state"].isna(), ["hh_id", "district"]])'''

R["ifs"] = '''hh <- read.csv("households.csv")
# One row per district: COUNTIFS, AVERAGEIFS and SUMIFS
tab <- do.call(rbind, lapply(sort(unique(hh$district)), function(dn) {
  g <- hh[hh$district == dn, ]
  data.frame(district    = dn,
             households  = nrow(g),                                   # COUNTIFS
             pct_toilet  = round(100 * mean(g$has_toilet == "Yes"), 1),# COUNTIFS / COUNTIFS
             mean_pc_exp = round(mean(g$monthly_pc_exp)),             # AVERAGEIFS
             persons     = sum(g$hh_size))                            # SUMIFS
}))
tab'''
P["ifs"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
# One row per district: COUNTIFS, AVERAGEIFS and SUMIFS
hh["toilet"] = (hh["has_toilet"] == "Yes")
tab = hh.groupby("district").agg(
    households=("hh_id", "size"),          # COUNTIFS
    pct_toilet=("toilet", "mean"),          # COUNTIFS / COUNTIFS
    mean_pc_exp=("monthly_pc_exp", "mean"), # AVERAGEIFS
    persons=("hh_size", "sum"),             # SUMIFS
)
tab["pct_toilet"] = (100 * tab["pct_toilet"]).round(1)
tab["mean_pc_exp"] = tab["mean_pc_exp"].round(0).astype(int)
print(tab)'''

R["pivot"] = '''hh <- read.csv("households.csv")
# Pivot 1: rows district, columns area, values count of hh_id
addmargins(table(hh$district, hh$area))
# Pivot 2: rows caste, columns area, values average of monthly_pc_exp
round(tapply(hh$monthly_pc_exp, list(hh$caste, hh$area), mean))'''
P["pivot"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
# Pivot 1: rows district, columns area, values count of hh_id
print(pd.crosstab(hh["district"], hh["area"], margins=True, margins_name="Total"))
# Pivot 2: rows caste, columns area, values average of monthly_pc_exp
print(hh.pivot_table(index="caste", columns="area", values="monthly_pc_exp", aggfunc="mean").round(0))'''

R["rag"] = '''hh <- read.csv("households.csv")
target <- 90                      # programme target: % of households with a bank account
pct <- round(100 * tapply(hh$has_bank_account == "Yes", hh$district, mean), 1)
status <- ifelse(pct >= target, "green",
          ifelse(pct >= target - 10, "amber", "red"))
out <- data.frame(pct_bank = pct, status = status)
out[order(out$pct_bank), ]
table(status)'''
P["rag"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
target = 90                       # programme target: % of households with a bank account
pct = (100 * (hh["has_bank_account"] == "Yes").groupby(hh["district"]).mean()).round(1)
status = pd.cut(pct, [-1, target - 10, target, 101], right=False, labels=["red", "amber", "green"])
out = pd.DataFrame({"pct_bank": pct, "status": status}).sort_values("pct_bank")
print(out)
print(out["status"].value_counts().sort_index())'''

R["weights"] = '''hh <- read.csv("households.csv")
# AVERAGE(H2:H241) and SUMPRODUCT(G2:G241, H2:H241) / SUM(G2:G241)
c(per_household = mean(hh$monthly_pc_exp),
  per_person    = sum(hh$hh_size * hh$monthly_pc_exp) / sum(hh$hh_size))
# The same two numbers by caste
round(sapply(split(hh, hh$caste), function(g)
  c(per_household = mean(g$monthly_pc_exp),
    per_person    = sum(g$hh_size * g$monthly_pc_exp) / sum(g$hh_size))), 1)'''
P["weights"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
# AVERAGE(H2:H241) and SUMPRODUCT(G2:G241, H2:H241) / SUM(G2:G241)
print("per household:", hh["monthly_pc_exp"].mean())
print("per person:   ", (hh["hh_size"] * hh["monthly_pc_exp"]).sum() / hh["hh_size"].sum())
# The same two numbers by caste
hh["w_exp"] = hh["hh_size"] * hh["monthly_pc_exp"]
g = hh.groupby("caste")
print(pd.DataFrame({"per_household": g["monthly_pc_exp"].mean(),
                    "per_person": g["w_exp"].sum() / g["hh_size"].sum()}).round(1))'''


def dual(key):
    return {"t": "dual", "r": R[key], "py": P[key], "pypkgs": "pandas"}


LAYOUT = """households.csv opened in Excel or Google Sheets (240 data rows, header in row 1)
A hh_id   B district   C area   D caste   E head_gender   F head_edu_years   G hh_size
H monthly_pc_exp   I land_acres   J has_toilet   K has_bank_account   L shg_member   M received_transfer
Data in rows 2 to 241.   districts.csv on a sheet named districts: A district  B state  ...  rows 2 to 11."""

VALID = """Custom rule for G2:G241 (household size), typed as one formula for the first cell:
=AND(ISNUMBER(G2), G2>=1, G2<=30, G2=INT(G2))

Custom rule for H2:H241 (monthly per capita expenditure in rupees):
=AND(ISNUMBER(H2), H2>0)

Custom rule for A2:A241 (hh_id must not repeat):
=COUNTIF($A$2:$A$241, A2)=1"""

LOOKUPS = """In N2, then fill down to N241 (state for each household):

Excel 2021, 2024, Microsoft 365, and Google Sheets
=XLOOKUP(B2, districts!$A$2:$A$11, districts!$B$2:$B$11, "not found")

Any version of Excel, and Google Sheets
=INDEX(districts!$B$2:$B$11, MATCH(B2, districts!$A$2:$A$11, 0))

VLOOKUP: the last argument must be FALSE for an exact match
=VLOOKUP(B2, districts!$A$2:$E$11, 2, FALSE)

Show a message instead of #N/A (Excel and Google Sheets)
=IFNA(INDEX(districts!$B$2:$B$11, MATCH(B2, districts!$A$2:$A$11, 0)), "check spelling")"""

IFS = """District names typed in O2:O11 of an indicator sheet, then fill each formula down:

Households                 =COUNTIFS($B$2:$B$241, $O2)
% with a toilet            =COUNTIFS($B$2:$B$241, $O2, $J$2:$J$241, "Yes") / COUNTIFS($B$2:$B$241, $O2)
Mean per capita spending   =AVERAGEIFS($H$2:$H$241, $B$2:$B$241, $O2)
Persons covered            =SUMIFS($G$2:$G$241, $B$2:$B$241, $O2)

Two conditions: rural SC households in the district
=COUNTIFS($B$2:$B$241, $O2, $C$2:$C$241, "Rural", $D$2:$D$241, "SC")"""

CF = """Conditional formatting, custom formula rules on Q2:Q11 (% with a bank account, as a fraction):
green   =$Q2>=0.9
amber   =AND($Q2>=0.8, $Q2<0.9)
red     =$Q2<0.8

Put the target in a cell (say T1 = 0.9) and refer to it, so a new target changes every rule:
=$Q2>=$T$1"""

WEIGHTS = """Mean per capita spending per household, and per person (weighted by household size):
=AVERAGE(H2:H241)
=SUMPRODUCT(G2:G241, H2:H241) / SUM(G2:G241)

Per person, SC households only:
=SUMPRODUCT(($D$2:$D$241="SC") * $G$2:$G$241 * $H$2:$H$241) / SUMIFS($G$2:$G$241, $D$2:$D$241, "SC")

NFHS household weight in a new column, if your file holds the DHS variable hv005 in column X:
=X2/1000000"""

DATES = """A real date, built from parts:        =DATE(2026, 10, 6)
Days between two interview dates:      =B2-A2
Show a date as text in ISO form:       =TEXT(A2, "yyyy-mm-dd")
Year and month of an interview:        =YEAR(A2)    =MONTH(A2)
Check that a cell holds a date (Excel stores dates as numbers):   =ISNUMBER(A2)"""

PAGE = {
    "slug": "spreadsheets",
    "order": 17,
    "kind": "guide",
    "tool": "Excel and Google Sheets",
    "title": "Spreadsheets for M&E",
    "h1": "Spreadsheets for M&amp;E",
    "lede": ("Most monitoring data passes through a spreadsheet. Set one up so the numbers can be trusted: one row "
             "per household, rules that stop bad entries, lookups that fail loudly, indicator tables built with "
             "COUNTIFS and SUMPRODUCT, and a dashboard that colours itself against targets. Every formula has an "
             "R and Python cell beside it that computes the same figure, so you can check your spreadsheet."),
    "description": ("A free guided course in Excel and Google Sheets for monitoring and evaluation in South Asia: "
                    "tidy layout, data validation, XLOOKUP, INDEX/MATCH and VLOOKUP's pitfalls, COUNTIFS, SUMIFS "
                    "and AVERAGEIFS indicator tables, pivot tables, conditional formatting, weighted averages with "
                    "SUMPRODUCT, dates, version habits, and when to move to R or Python."),
    "card": "Tidy sheets, validation, XLOOKUP, COUNTIFS indicator tables, pivots, weighted means, with R and Python checks.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>Excel and Google Sheets do not run on this page.</strong> The grey boxes are formulas "
                    "for you to type into your own spreadsheet with " + DL + " and " + DD + " open (both are "
                    "illustrative data, invented for teaching: ten real district names with made-up households). "
                    "This page shows no spreadsheet screenshots. Each code cell computes the same figure in R or "
                    "Python on the same file; switch language with the tabs on the cell. The first run downloads "
                    "the engine once (R about 7&nbsp;MB, Python about 10&nbsp;MB)."),
    "modules": [
        {"tab": "Structure",
         "title": "One row per record, one column per variable",
         "blocks": [
             {"t": "p", "html": "A spreadsheet built to be read by people (merged headings, subtotals between rows, "
                                "colour as data) is hard to count from. A sheet built to be counted from follows "
                                "four rules, and every formula in this course depends on them."},
             {"t": "ul", "items": [
                 "<strong>One row per record.</strong> One household, one visit or one beneficiary per row. "
                 "Totals go on a separate sheet.",
                 "<strong>One column per variable, one header row.</strong> Short names with no spaces "
                 "(" + IC("monthly_pc_exp") + "), with the full question and units in a codebook sheet.",
                 "<strong>One value per cell.</strong> \"Purnia, Bihar\" in one cell is two variables. "
                 "\"3 (approx)\" is a number and a note; split them.",
                 "<strong>A unique ID in the first column</strong> that never changes, never repeats and is not a "
                 "name.",
             ]},
             {"t": "info", "tone": "warning",
              "html": "<strong>Avoid merged cells.</strong> Microsoft's " + link(
                  "https://support.microsoft.com/en-us/office/merge-and-unmerge-cells-5cbd15d5-9375-4540-907f-c673a93fcedf",
                  "merge cells guide") + " warns that when you merge cells, only the upper-left cell's contents "
                      "are kept and \"the contents of the other cells that you merge are deleted\". A merged "
                      "district heading over 24 rows also leaves 23 rows with no district, so every COUNTIFS on "
                      "district misses them. Put the district in every row instead."},
             {"t": "syntax", "label": "Layout used in every formula on this page", "code": LAYOUT},
             {"t": "p", "html": "Download " + DL + " and open it. The cell checks the same three things you should "
                                "check by eye: size, column names and duplicate IDs."},
             dual("shape"),
             {"t": "p", "html": "The file has 240 rows and 13 columns, no repeated " + IC("hh_id") + ", numbers in "
                                "the numeric columns and text in the rest. In Excel, select column A and look at "
                                "the status bar: <em>Count</em> should read 241 (240 IDs plus the header)."},
             {"t": "info", "html": "<strong>Exercise.</strong> In your spreadsheet, type 1 over the "
                                   + IC("hh_id") + " in A3, then type " + IC("=COUNTIF($A$2:$A$241, A2)") + " in "
                                   "N2 and fill down. Sort by column N, largest first: the two rows with a count "
                                   "of 2 are your duplicates. Undo the change afterwards."},
         ]},
        {"tab": "Validation",
         "title": "Data validation: stop bad entries at the cell",
         "blocks": [
             {"t": "p", "html": "If people type data into the sheet, validation is your form's constraint column. "
                                "Use dropdowns for categories and ranges for numbers."},
             {"t": "h3", "html": "Excel"},
             {"t": "steps", "items": [
                 "Select the cells, for example C2:C241.",
                 "On the <strong>Data</strong> tab, in the Data Tools group, select <strong>Data "
                 "Validation</strong> (" + link("https://support.microsoft.com/en-us/office/apply-data-validation-to-cells-29fecbcc-d1b9-42c1-9d76-eff3ce5f7249",
                                                "Microsoft guide") + ").",
                 "Under <strong>Allow</strong>, choose <em>List</em> and type " + IC("Rural,Urban") + ", or "
                 "choose <em>Whole Number</em>, <em>Decimal</em>, <em>Date</em>, <em>Text Length</em> or "
                 "<em>Custom</em> (a formula).",
                 "On the <strong>Input Message</strong> tab, tick <em>Show input message when cell is "
                 "selected</em> and write the instruction.",
                 "On the <strong>Error Alert</strong> tab, choose <em>Stop</em> to refuse the entry, or "
                 "<em>Warning</em> to let the user decide.",
             ]},
             {"t": "h3", "html": "Google Sheets"},
             {"t": "steps", "items": [
                 "Select the cells, then <strong>Data &gt; Data validation</strong> (" + link(
                     "https://support.google.com/docs/answer/186103", "Google guide") + ").",
                 "Choose a criterion such as <em>Dropdown</em> or <em>Dropdown (from a range)</em>.",
                 "Under <strong>Advanced options</strong>, choose what happens if the data is invalid: "
                 "<em>Show a warning</em>, or reject the input.",
             ]},
             {"t": "syntax", "label": "Custom validation formulas (Excel and Google Sheets)", "code": VALID},
             {"t": "p", "html": "Build the dropdown lists and number ranges from the data you expect. The cell "
                                "lists every category and the range of each numeric column in " + DL + "."},
             dual("lists"),
             {"t": "p", "html": "The file holds 10 districts, two areas (Rural, Urban), four caste groups "
                                "(General, OBC, SC, ST), and Yes or No for toilets. Household size runs from 1 to "
                                "8, years of schooling of the head from 0 to 17, and monthly per capita "
                                "expenditure from Rs 700 to Rs 20,690."},
             {"t": "info", "html": "<strong>Exercise.</strong> Add the custom rule for household size to G2:G241, "
                                   "then try typing 0, 4.5 and 31 into G2. Each should be refused. Ranges come "
                                   "from what is plausible, wider than what this sample happens to contain: a "
                                   "rule of 1 to 8 would refuse the next household of nine."},
             {"t": "info", "tone": "warning",
              "html": "<strong>Validation checks typing, and nothing else.</strong> Data pasted over a validated "
                      "cell, or already in the sheet before the rule was added, is not rechecked automatically. "
                      "After a paste, check the column again, for example with the COUNTIF in module 1 or the "
                      "R and Python cells here."},
         ]},
        {"tab": "Lookups",
         "title": "XLOOKUP, INDEX/MATCH and VLOOKUP's pitfalls",
         "blocks": [
             {"t": "p", "html": "A lookup copies a value from another table by matching a key: here, each "
                                "household's state from " + DD + " by district name."},
             {"t": "syntax", "label": "Lookup formulas", "code": LOOKUPS},
             {"t": "h3", "html": "Which function your software has"},
             {"t": "ul", "items": [
                 "<strong>XLOOKUP</strong>: Microsoft's " + link(
                     "https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929",
                     "XLOOKUP page") + " says \"XLOOKUP is not available in Excel 2016 and Excel 2019\". It works "
                 "in Excel 2021, Excel 2024 and Microsoft 365. Its exact-match mode is the default, and the "
                 "fourth argument sets what to show when nothing is found. Google Sheets has " + link(
                     "https://support.google.com/docs/answer/12405947", "XLOOKUP") + " with the same argument "
                 "order (it calls the fourth one " + IC("missing_value") + ").",
                 "<strong>INDEX with MATCH</strong> works in every version of Excel and in Google Sheets. The "
                 + IC("0") + " in MATCH asks for an exact match.",
                 "<strong>VLOOKUP</strong> works everywhere, and has three traps.",
             ]},
             {"t": "h3", "html": "VLOOKUP's three traps"},
             {"t": "ul", "items": [
                 "<strong>The default is an approximate match.</strong> Microsoft's " + link(
                     "https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1",
                     "VLOOKUP page") + " says that if you leave out the last argument, VLOOKUP \"assumes the "
                 "first column in the table is sorted\" and \"will then search for the closest value\". On an "
                 "unsorted district list that can return another district's state with no error. Always write "
                 + IC("FALSE") + " at the end.",
                 "<strong>The key must be the first column</strong> of the range, so VLOOKUP cannot look left.",
                 "<strong>The column is a number.</strong> " + IC("2") + " means \"the second column of the "
                 "range\". Insert a column into the districts sheet and every VLOOKUP silently returns the wrong "
                 "column. XLOOKUP and INDEX/MATCH point at the column itself.",
             ]},
             {"t": "p", "html": "The cell does the exact lookup, then misspells one district as a merged MIS "
                                "export might, and counts what fails to match."},
             dual("lookup"),
             {"t": "p", "html": "Every household finds its state: 72 in Bihar, 48 in Kerala, 72 in Madhya "
                                "Pradesh and 48 in Rajasthan. After household 100's district is changed to "
                                "<em>Purnea</em>, exactly one row has no state. In the spreadsheet that row shows "
                                "#N/A, or your " + IC("\"not found\"") + " text. That is the behaviour you want: a "
                                "lookup that fails visibly."},
             {"t": "info", "html": "<strong>Exercise.</strong> After you fill the lookup down, count the failures "
                                   "with " + IC("=COUNTIF(N2:N241, \"not found\")") + " (or "
                                   + IC("=SUMPRODUCT(--ISNA(N2:N241))") + " if you did not use the fourth "
                                   "argument). Make that count part of every update: it should be 0 before any "
                                   "table is built on the column."},
         ]},
        {"tab": "Indicators",
         "title": "Indicator tables with COUNTIFS, SUMIFS and AVERAGEIFS",
         "blocks": [
             {"t": "p", "html": "An indicator table has one row per district (or block, or caste group) and one "
                                "column per indicator. The *IFS functions count, add or average the rows that "
                                "meet every condition you give them."},
             {"t": "syntax", "label": "Indicator formulas (Excel and Google Sheets)", "code": IFS},
             {"t": "info", "tone": "warning",
              "html": "<strong>Argument order differs.</strong> Microsoft's " + link(
                  "https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b",
                  "SUMIFS page") + " points out that the range to add comes first in SUMIFS and third in SUMIF. "
                      "AVERAGEIFS follows SUMIFS. Use the *IFS forms everywhere, even with one condition, so the "
                      "order is always the same."},
             {"t": "p", "html": "The cell computes the same four columns for all ten districts, so you can check "
                                "each cell of your table."},
             dual("ifs"),
             {"t": "p", "html": "Each district has 24 households. The share with a toilet runs from 50.0% in "
                                "Rewa to 83.3% in Indore, Kozhikode and Patna, and mean monthly per capita "
                                "expenditure from Rs 2,395 in Purnia to Rs 6,758 in Kozhikode. If your spreadsheet "
                                "shows 0.958 where the cell shows 95.8, format the column as a percentage."},
             {"t": "info", "html": "<strong>Exercise.</strong> Add a column for the share of households that "
                                   "received a transfer (column M), then change the condition in the R or Python "
                                   "cell to match and compare. In R, add " + IC(
                                       'pct_transfer = round(100 * mean(g$received_transfer == "Yes"), 1),')
                                   + " inside " + IC("data.frame(") + "."},
         ]},
        {"tab": "Pivots",
         "title": "Pivot tables",
         "blocks": [
             {"t": "p", "html": "A pivot table builds a cross-tabulation without formulas. It is the quickest way "
                                "to explore; for a table you will update every month, the formulas in module 4 "
                                "are easier to audit."},
             {"t": "steps", "items": [
                 "Click any cell in the data. In Excel select <strong>Insert &gt; PivotTable</strong> (" + link(
                     "https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576",
                     "Microsoft guide") + "); in Google Sheets, <strong>Insert &gt; Pivot table</strong> (" + link(
                     "https://support.google.com/docs/answer/1272900", "Google guide") + ").",
                 "Put it on a new sheet.",
                 "Pivot 1: drag <em>district</em> to Rows, <em>area</em> to Columns and <em>hh_id</em> to Values. "
                 "Change the value from Sum to <strong>Count</strong>: a sum of IDs is meaningless.",
                 "Pivot 2: <em>caste</em> to Rows, <em>area</em> to Columns, <em>monthly_pc_exp</em> to Values, "
                 "summarised by <strong>Average</strong>.",
             ]},
             dual("pivot"),
             {"t": "p", "html": "Pivot 1 has 164 rural and 76 urban households, 240 in all; Kozhikode (21) and "
                                "Indore (16) have the most urban households and Barmer (2) the fewest. In Pivot "
                                "2, urban means are above rural means in every caste group. Your pivot's grand "
                                "totals and cells should match these exactly."},
             {"t": "info", "tone": "warning",
              "html": "<strong>A pivot does not refresh itself in Excel.</strong> After you add or change rows, "
                      "refresh it (right-click the pivot, Refresh), and check that its source range still covers "
                      "the new rows. Formatting the data as a table first (Insert &gt; Table) makes the range grow "
                      "with the data."},
             {"t": "info", "html": "<strong>Exercise.</strong> In Pivot 2, swap Average for Count. The smallest "
                                   "cell is the number of urban ST households (5 in this file). A mean over very few households is "
                                   "not worth reporting; decide on a minimum cell size (many teams use 25 or 30) "
                                   "and grey out cells below it."},
         ]},
        {"tab": "Dashboard",
         "title": "Conditional formatting against targets",
         "blocks": [
             {"t": "p", "html": "A red-amber-green column next to an indicator tells a reader which districts are "
                                "behind without reading every number. Set the rule against a target cell, so the "
                                "colours follow the target when it changes."},
             {"t": "steps", "items": [
                 "Excel: select the indicator cells, then <strong>Home</strong> tab, Styles group, "
                 "<strong>Conditional Formatting</strong>. For a rule from a formula, choose New Rule and the "
                 "option that uses a formula (" + link(
                     "https://support.microsoft.com/en-us/office/use-conditional-formatting-to-highlight-information-in-excel-fed60dfa-1d3f-4e13-9ecb-f1951ff89d7f",
                     "Microsoft guide") + ").",
                 "Google Sheets: <strong>Format &gt; Conditional formatting</strong>, then under \"Format cells "
                 "if\" choose <em>Custom formula is</em> (" + link("https://support.google.com/docs/answer/78413",
                                                                    "Google guide") + ").",
                 "Add one rule per colour, in the order red, amber, green.",
             ]},
             {"t": "syntax", "label": "Custom formula rules", "code": CF},
             dual("rag"),
             {"t": "p", "html": "Against a 90% target for bank accounts, 4 districts are green, 4 amber and 2 "
                                "red; the lowest is Purnia at 75.0%. Your coloured column should show the same "
                                "split."},
             {"t": "info", "html": "<strong>Colour is not enough on its own.</strong> Some readers cannot tell red "
                                   "from green, and a printout may be black and white. Keep the number visible, "
                                   "and put the status word (or a symbol) in its own column as the cell does."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change " + IC("target") + " to 85 in the cell and "
                                   "the target cell T1 to 0.85 in your sheet (and the amber limits to 75%). The "
                                   "two red districts turn amber and Gaya turns green; check that your sheet "
                                   "agrees."},
         ]},
        {"tab": "Weights and dates",
         "title": "Weighted averages with SUMPRODUCT, and dates",
         "blocks": [
             {"t": "p", "html": "The average of monthly per capita expenditure over households answers \"what does "
                                "a typical household spend per person?\". Weighting by household size answers "
                                "\"what does a typical person live on?\". Large households are often poorer, so "
                                "the two differ, and a report must say which it uses."},
             {"t": "syntax", "label": "Weighted averages (Excel and Google Sheets)", "code": WEIGHTS},
             {"t": "p", "html": "SUMPRODUCT multiplies the two ranges row by row and adds the results (" + link(
                 "https://support.microsoft.com/en-us/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e",
                 "Microsoft guide") + "). Inside it, a condition such as " + IC('($D$2:$D$241="SC")') + " becomes "
                                "1 or 0, which keeps only the rows you want."},
             dual("weights"),
             {"t": "p", "html": "The per-household mean is Rs 3,400.9 and the per-person mean is lower, Rs "
                                "3,335.4, because larger households in this file spend a little less per head. "
                                "By caste the gap is largest for ST households (Rs 2,694.0 against Rs 2,369.9), "
                                "and for SC households it runs the other way (Rs 2,355.8 against Rs 2,377.2). "
                                "Which mean you report changes the comparison between groups."},
             {"t": "info", "html": "<strong>Survey weights work the same way.</strong> For NFHS household data, "
                                   "the DHS weight " + IC("hv005") + " (or " + IC("v005") + " for women) is "
                                   "divided by 1,000,000; put the weight in the first SUMPRODUCT range and in the "
                                   "SUM. A weighted mean in a spreadsheet gives the right point estimate; its "
                                   "standard error needs the survey design (strata and clusters), which is a job "
                                   "for R, Stata or Python."},
             {"t": "h3", "html": "Dates"},
             {"t": "p", "html": "Excel and Google Sheets store a date as a number, which is what lets you subtract "
                                "one from another. A date typed in a format the sheet does not recognise stays "
                                "text, and then sorts and subtracts wrongly. Type dates as yyyy-mm-dd, check "
                                "them with " + IC("ISNUMBER") + ", and say in the codebook which date a column "
                                "holds (interview, enrolment, payment)."},
             {"t": "syntax", "label": "Date formulas", "code": DATES},
             {"t": "info", "tone": "warning",
              "html": "<strong>Be careful with DATEDIF.</strong> Excel still has DATEDIF for whole years or months "
                      "between dates, but its " + link(
                          "https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c",
                          "help page") + " warns that one of its options \"may result in a negative number, a "
                      "zero, or an inaccurate result\". For days, subtract; for age in years, check a few "
                      "results by hand."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the weighting in the cell from "
                                   + IC("hh_size") + " to " + IC("land_acres") + " in both places and run "
                                   "again. You get mean spending per acre owned, a weighting that makes no sense. "
                                   "A weight should be the number of units each row stands for."},
         ]},
        {"tab": "Habits",
         "title": "Version habits, and when to move to R or Python",
         "blocks": [
             {"t": "h3", "html": "Habits that make a spreadsheet auditable"},
             {"t": "ul", "items": [
                 "<strong>Keep the raw data untouched.</strong> Put the export on a sheet named " + IC("raw") +
                 ", protect it, and do all work on other sheets that refer to it.",
                 "<strong>Name files by date.</strong> " + IC("hh_baseline_2026-10-06.xlsx") +
                 " sorts in order; " + IC("final_v2_revised.xlsx") + " does not.",
                 "<strong>Keep a change log sheet</strong>: date, who, what changed, why. One line per change.",
                 "<strong>Use the built-in history.</strong> In Google Sheets, click <em>Last edit</em> at the "
                 "top right to open version history, name a version before a big change, and restore an earlier "
                 "one if needed (" + link("https://support.google.com/docs/answer/190843", "Google guide") + "). "
                 "Excel files saved to OneDrive or SharePoint also keep earlier versions.",
                 "<strong>Put inputs in their own cells.</strong> A target, an exchange rate or a "
                 "poverty line typed into one labelled cell can be changed once and checked by anyone.",
             ]},
             {"t": "h3", "html": "Signs it is time to move to R or Python"},
             {"t": "ul", "items": [
                 "<strong>You repeat the same steps every month.</strong> A script runs them again in seconds, "
                 "identically, and records what it did.",
                 "<strong>You need standard errors or survey weights with design.</strong> NFHS, PLFS and most "
                 "evaluation samples are clustered; spreadsheets cannot compute the right standard errors.",
                 "<strong>You join several files.</strong> A roster, a household file and a village file joined "
                 "by lookups in a spreadsheet are hard to check; a merge in code reports what did not match.",
                 "<strong>The file is large.</strong> Microsoft's " + link(
                     "https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3",
                     "Excel limits page") + " gives 1,048,576 rows per worksheet; Google's " + link(
                     "https://support.google.com/drive/answer/37603", "Drive file limits") + " give up to "
                 "20 million cells for a spreadsheet. A slow, heavy file usually reaches its practical limit long "
                 "before either.",
                 "<strong>The data is personal.</strong> A spreadsheet of names and phone numbers emailed between "
                 "staff is copied everywhere; under the DPDP Act 2023 your organisation must protect it from "
                 "13 May 2027, and should start now. Keep "
                 "identifiers in one controlled file and share the analysis without them.",
             ]},
             {"t": "p", "html": "Every cell on this page did in a few lines what took a column of formulas. The "
                                "courses below teach that way of working from the start."},
         ]},
    ],
    "next": [
        {"href": "/code/r-python.html", "title": "R and Python side by side",
         "desc": "The first steps in both languages, on the same household data."},
        {"href": "/code/tidyverse.html", "title": "The tidyverse",
         "desc": "Indicator tables in R with group_by and summarise."},
        {"href": "/code/pandas.html", "title": "pandas for development data",
         "desc": "The same tables in Python, with merges that report what failed."},
        {"href": "/code/kobo-odk.html", "title": "KoboToolbox and ODK",
         "desc": "Collect the data with checks built into the form."},
        {"href": "/101-courses/mel-basics.html", "title": "MEL Basics 101",
         "desc": "Choosing indicators and targets before you build the table."},
        {"href": "/101-courses/data-viz.html", "title": "Data Visualization 101",
         "desc": "Turning an indicator table into a chart people can read."},
    ],
}

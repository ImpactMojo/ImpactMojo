# -*- coding: utf-8 -*-
"""SPSS Syntax for Development Data: a guided course in SPSS command syntax, with R cells that run the same steps here.

Facts checked on 6 October 2026 against IBM's SPSS Statistics product and pricing pages, IBM documentation
(Syntax Editor, pasting syntax, the IBM SPSS Complex Samples 31 manual), the DHS Program's Guide to DHS
Statistics and the DHS Recode VII manual. Sources are listed in the agent report.
"""

DL = '<a href="/code/data/households.csv" download style="color:var(--accent-color)">households.csv</a>'
DD = '<a href="/code/data/districts.csv" download style="color:var(--accent-color)">districts.csv</a>'

GET_HH = ("GET DATA\n"
          "  /TYPE=TXT\n"
          "  /FILE='C:\\impactmojo\\spss\\households.csv'\n"
          "  /DELIMITERS=\",\"\n"
          "  /QUALIFIER='\"'\n"
          "  /ARRANGEMENT=DELIMITED\n"
          "  /FIRSTCASE=2\n"
          "  /VARIABLES=\n"
          "    hh_id F4.0\n"
          "    district A12\n"
          "    area A5\n"
          "    caste A8\n"
          "    head_gender A6\n"
          "    head_edu_years F2.0\n"
          "    hh_size F2.0\n"
          "    monthly_pc_exp F6.0\n"
          "    land_acres F5.2\n"
          "    has_toilet A3\n"
          "    has_bank_account A3\n"
          "    shg_member A3\n"
          "    received_transfer A3.\n"
          "DATASET NAME households WINDOW=FRONT.\n")

R = {}
R["look"] = ('hh <- read.csv("households.csv")\n'
             '# FREQUENCIES VARIABLES=caste\n'
             'table(hh$caste)\n'
             '# DESCRIPTIVES VARIABLES=monthly_pc_exp hh_size head_edu_years\n'
             'sapply(hh[, c("monthly_pc_exp", "hh_size", "head_edu_years")],\n'
             '       function(x) round(c(N = length(x), Mean = mean(x), SD = sd(x), Min = min(x), Max = max(x)), 2))\n'
             '# CROSSTABS /TABLES=caste BY area /CELLS=COUNT ROW /STATISTICS=CHISQ\n'
             'tab <- table(hh$caste, hh$area)\n'
             'tab\n'
             'round(100 * prop.table(tab, 1), 1)\n'
             'chisq.test(tab, correct = FALSE)')
R["compute"] = ('hh <- read.csv("households.csv")\n'
                "# COMPUTE toilet = (has_toilet = 'Yes').\n"
                'hh$toilet <- as.integer(hh$has_toilet == "Yes")\n'
                '# RECODE head_edu_years (0=0) (1 THRU 5=1) (6 THRU 10=2) (11 THRU HIGHEST=3) INTO edu_cat.\n'
                'hh$edu_cat <- cut(hh$head_edu_years, breaks = c(-Inf, 0, 5, 10, Inf),\n'
                '                  labels = c("None", "Primary (1-5)", "Secondary (6-10)", "Higher (11+)"))\n'
                'table(hh$edu_cat)\n'
                'table(hh$toilet)')
R["aggregate"] = ('hh <- read.csv("households.csv")\n'
                  '# AGGREGATE ... MODE=ADDVARIABLES /BREAK=district /district_mean=MEAN(monthly_pc_exp)\n'
                  'hh$district_mean <- ave(hh$monthly_pc_exp, hh$district)\n'
                  'head(hh[, c("hh_id", "district", "monthly_pc_exp", "district_mean")], 3)\n'
                  '# AGGREGATE /OUTFILE=... /BREAK=district /mean_exp=MEAN(monthly_pc_exp) /n=N\n'
                  'by_d <- aggregate(monthly_pc_exp ~ district, data = hh, FUN = mean)\n'
                  'by_d$n <- as.vector(table(hh$district)[by_d$district])\n'
                  'by_d')
R["match"] = ('hh <- read.csv("households.csv")\n'
              'd  <- read.csv("districts.csv")\n'
              '# MATCH FILES /FILE=* /TABLE=\'districts.sav\' /IN=in_district /BY district.\n'
              'm <- merge(hh, d, by = "district", all.x = TRUE)\n'
              'm$in_district <- as.integer(!is.na(m$state))\n'
              'table(m$in_district)\n'
              'table(m$state, m$programme_phase)')
R["weight"] = ('hh <- read.csv("households.csv")\n'
               '# DESCRIPTIVES with and without WEIGHT BY hh_size\n'
               'c(per_household = mean(hh$monthly_pc_exp),\n'
               '  per_person    = weighted.mean(hh$monthly_pc_exp, hh$hh_size))\n'
               '# WEIGHT BY hh_size also changes the N that SPSS reports\n'
               'c(cases = nrow(hh), weighted_N = sum(hh$hh_size))')
R["regression"] = ('hh <- read.csv("households.csv")\n'
                   '# the dummies SPSS needs you to COMPUTE yourself\n'
                   'hh$obc   <- as.integer(hh$caste == "OBC")\n'
                   'hh$sc    <- as.integer(hh$caste == "SC")\n'
                   'hh$st    <- as.integer(hh$caste == "ST")\n'
                   'hh$urban <- as.integer(hh$area == "Urban")\n'
                   '# REGRESSION /DEPENDENT monthly_pc_exp /METHOD=ENTER obc sc st head_edu_years urban\n'
                   'fit <- lm(monthly_pc_exp ~ obc + sc + st + head_edu_years + urban, data = hh)\n'
                   'round(summary(fit)$coefficients, 2)\n'
                   'round(summary(fit)$r.squared, 3)')

PAGE = {
    "slug": "spss",
    "order": 11,
    "kind": "guide",
    "tool": "SPSS",
    "title": "SPSS Syntax for Development Data",
    "h1": "SPSS syntax for development data",
    "lede": ("Use SPSS through syntax files you can save and re-run: GET DATA, variable and value labels, RECODE, "
             "COMPUTE, FREQUENCIES, DESCRIPTIVES, CROSSTABS, AGGREGATE, MATCH FILES, WEIGHT BY and the Complex "
             "Samples procedures for NFHS, and REGRESSION. Learn to paste syntax from the menus, follow along in "
             "your own SPSS with two small CSV files, and check each step in R on this page."),
    "description": ("A free guided course in IBM SPSS Statistics syntax for development practitioners in South "
                    "Asia: GET DATA, VARIABLE LABELS, VALUE LABELS, RECODE, COMPUTE, FREQUENCIES, CROSSTABS, "
                    "AGGREGATE, MATCH FILES, WEIGHT BY, Complex Samples (CSPLAN) for NFHS, REGRESSION and "
                    "pasting syntax from menus."),
    "card": "Syntax files from GET DATA to Complex Samples and REGRESSION, with every step you can paste from a menu.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>SPSS does not run in a browser.</strong> The grey boxes are SPSS syntax for you to "
                    "type or paste into your own Syntax Editor. This page shows no SPSS output tables, because "
                    "it cannot produce any; each module tells you what to look for in your Output Viewer "
                    "instead. Where the same step can be done in R, an R cell runs it here on the same data, so "
                    "you can check your numbers. The first R run downloads the R engine once (about 7&nbsp;MB)."),
    "modules": [
        {"tab": "Set up",
         "title": "SPSS, the Syntax Editor and why syntax",
         "blocks": [
             {"t": "p", "html": "IBM SPSS Statistics is a paid statistics package used across government "
                                "departments, NGOs, universities and market research firms in South Asia. Most "
                                "people learn it through the menus. This course teaches the syntax underneath "
                                "the menus, because a syntax file is a record of your analysis that you, a "
                                "colleague or a reviewer can run again and get the same tables."},
             {"t": "info", "html": "<strong>Version and cost, checked 6 October 2026.</strong> IBM's "
                                   "<a href=\"https://www.ibm.com/products/spss-statistics\" rel=\"noopener\" "
                                   "target=\"_blank\" style=\"color:var(--accent-color)\">SPSS Statistics page</a> "
                                   "describes <strong>version 32</strong>. IBM's "
                                   "<a href=\"https://www.ibm.com/products/spss-statistics/pricing\" rel=\"noopener\" "
                                   "target=\"_blank\" style=\"color:var(--accent-color)\">pricing page</a> offers "
                                   "monthly, quarterly or annual subscriptions, with the Base subscription "
                                   "\"starting at $99.00 USD\" per authorised user and add-on bundles starting at "
                                   "$79.00 USD each, one of which (\"Complex sampling and testing\") carries "
                                   "Complex Samples. IBM also lists perpetual licences, campus editions for "
                                   "institutions, student licences through authorised vendors, and a free trial. "
                                   "Prices on that page are for purchases on ibm.com and may differ through a "
                                   "local reseller."},
             {"t": "h3", "html": "Open a syntax window"},
             {"t": "steps", "items": [
                 "Make a project folder, for example <code class=\"inline\">C:\\impactmojo\\spss</code>.",
                 "Download the two course files into it: " + DL + " (240 households) and " + DD + " (10 "
                 "districts). <span class=\"illustrative-tag\">Illustrative data, invented for teaching</span> "
                 "The district names are real places; every number is made up.",
                 "In SPSS choose <strong>File &gt; New &gt; Syntax</strong>. The Syntax Editor opens.",
                 "Type or paste a block of syntax, select it, and click the <strong>Run</strong> button "
                 "(the right-pointing triangle) on the Syntax Editor toolbar. The <strong>Run</strong> menu also "
                 "has <strong>All</strong>, <strong>Selection</strong>, <strong>To End</strong> and "
                 "<strong>Step Through</strong>.",
                 "Save the file with <strong>File &gt; Save</strong>; SPSS syntax files end in "
                 "<code class=\"inline\">.sps</code>.",
             ]},
             {"t": "h3", "html": "Rules of SPSS syntax"},
             {"t": "ul", "items": [
                 "Every command ends with a full stop. A missing full stop is the most common reason a block "
                 "does nothing or errors.",
                 "Subcommands start with a slash: <code class=\"inline\">/TABLES=</code>, "
                 "<code class=\"inline\">/STATISTICS=</code>.",
                 "A comment starts with an asterisk at the beginning of a line and ends with a full stop.",
                 "Commands such as <code class=\"inline\">COMPUTE</code> and <code class=\"inline\">RECODE</code> "
                 "wait for the next procedure before they change the data. "
                 "<code class=\"inline\">EXECUTE.</code> makes them run straight away, so you can see the new "
                 "column in the Data Editor.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> Open a new syntax window, type "
                                   "<code class=\"inline\">* My first SPSS syntax file.</code> on the first line, and "
                                   "save it as <code class=\"inline\">01_import.sps</code> in your project folder. "
                                   "You will fill it in the next module."},
         ]},
        {"tab": "Read data",
         "title": "Read a CSV with GET DATA",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">GET DATA /TYPE=TXT</code> reads a delimited text file. You "
                                "tell it the delimiter, which row the data start on (row 2, after the header), "
                                "and the name and format of each column. <code class=\"inline\">F4.0</code> is a "
                                "number four characters wide with no decimals; <code class=\"inline\">A12</code> "
                                "is text up to 12 characters."},
             {"t": "syntax", "label": "SPSS syntax: 01_import.sps", "code":
                 "* 01_import.sps : read the course household file.\n"
                 "* Change the FILE path to your own folder.\n" + GET_HH +
                 "\n"
                 "DISPLAY DICTIONARY.\n"
                 "LIST VARIABLES=hh_id district caste monthly_pc_exp /CASES=FROM 1 TO 5."},
             {"t": "ul", "items": [
                 "The Data Editor should show 240 rows. <code class=\"inline\">DISPLAY DICTIONARY</code> lists "
                 "the 13 variables with their formats.",
                 "If a column is blank or wrong, check its format: text read as <code class=\"inline\">F</code> "
                 "comes out as system-missing, shown as a dot.",
                 "Dialogs that read and change data, and most analysis dialogs, have a <strong>Paste</strong> "
                 "button beside <strong>OK</strong>. The rest of this module explains it.",
             ]},
             {"t": "h3", "html": "Paste syntax from any dialog"},
             {"t": "p", "html": "IBM's documentation describes this as the easiest way to build a syntax file: "
                                "make your selections in a dialog, then click <strong>Paste</strong>. The "
                                "command goes into the syntax window (a new one opens if none is open), where "
                                "you can run it, edit it and save it. Pasting at each step of an analysis builds "
                                "a file that repeats the whole analysis later. Use the menus to find a command, "
                                "and keep the syntax as your record."},
             {"t": "info", "html": "<strong>Exercise.</strong> Choose <strong>Analyze &gt; Descriptive Statistics "
                                   "&gt; Frequencies</strong>, move <code class=\"inline\">caste</code> into the "
                                   "Variable(s) box and click <strong>Paste</strong>. Compare the pasted command "
                                   "with the <code class=\"inline\">FREQUENCIES</code> line in the next module."},
         ]},
        {"tab": "Describe",
         "title": "FREQUENCIES, DESCRIPTIVES and CROSSTABS",
         "blocks": [
             {"t": "syntax", "label": "SPSS syntax: 02_describe.sps", "code":
                 "FREQUENCIES VARIABLES=caste area head_gender.\n"
                 "\n"
                 "DESCRIPTIVES VARIABLES=monthly_pc_exp hh_size head_edu_years\n"
                 "  /STATISTICS=MEAN STDDEV MIN MAX.\n"
                 "\n"
                 "FREQUENCIES VARIABLES=monthly_pc_exp\n"
                 "  /FORMAT=NOTABLE\n"
                 "  /STATISTICS=MEAN MEDIAN\n"
                 "  /PERCENTILES=25 75.\n"
                 "\n"
                 "CROSSTABS\n"
                 "  /TABLES=caste BY area\n"
                 "  /CELLS=COUNT ROW\n"
                 "  /STATISTICS=CHISQ."},
             {"t": "h3", "html": "What to look for"},
             {"t": "ul", "items": [
                 "The caste frequency table should have four rows (General, OBC, SC, ST) and a Total of 240.",
                 "<code class=\"inline\">/FORMAT=NOTABLE</code> stops SPSS printing one row per distinct "
                 "expenditure value and keeps only the statistics.",
                 "In the crosstab, <code class=\"inline\">ROW</code> gives the percentage of each caste group "
                 "living in rural and urban areas. The Chi-Square Tests table follows it; read the Pearson "
                 "Chi-Square row.",
                 "The menu route for the crosstab is <strong>Analyze &gt; Descriptive Statistics &gt; "
                 "Crosstabs</strong>.",
             ]},
             {"t": "p", "html": "The same three summaries in R, on the same file. Your SPSS counts, means and "
                                "Pearson chi-square should match these."},
             {"t": "code", "lang": "r", "code": R["look"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the crosstab to "
                                   "<code class=\"inline\">/TABLES=head_gender BY caste</code> with "
                                   "<code class=\"inline\">/CELLS=COUNT COLUMN</code>. In the R cell, change "
                                   "<code class=\"inline\">tab</code> to "
                                   "<code class=\"inline\">table(hh$head_gender, hh$caste)</code> and "
                                   "<code class=\"inline\">prop.table(tab, 1)</code> to "
                                   "<code class=\"inline\">prop.table(tab, 2)</code>, then run both."},
         ]},
        {"tab": "Recode and label",
         "title": "COMPUTE, RECODE and labels",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">COMPUTE</code> makes or changes a variable from an "
                                "expression. <code class=\"inline\">RECODE ... INTO</code> maps old values to "
                                "new ones in a new variable, which keeps the original intact. Then give both "
                                "variables and values readable labels."},
             {"t": "syntax", "label": "SPSS syntax: 03_recode.sps", "code":
                 "* 0/1 indicators from Yes/No text.\n"
                 "COMPUTE toilet = (has_toilet = 'Yes').\n"
                 "COMPUTE bank = (has_bank_account = 'Yes').\n"
                 "COMPUTE annual_pc_exp = monthly_pc_exp * 12.\n"
                 "\n"
                 "* Education bands in a new variable.\n"
                 "RECODE head_edu_years (0=0) (1 THRU 5=1) (6 THRU 10=2) (11 THRU HIGHEST=3) INTO edu_cat.\n"
                 "\n"
                 "* Text categories to numeric codes.\n"
                 "RECODE caste ('General'=1) ('OBC'=2) ('SC'=3) ('ST'=4) INTO caste_n.\n"
                 "EXECUTE.\n"
                 "\n"
                 "VARIABLE LABELS\n"
                 "  toilet 'Household has a toilet (1 = yes)'\n"
                 "  edu_cat 'Schooling of household head, banded'\n"
                 "  caste_n 'Caste group'\n"
                 "  monthly_pc_exp 'Monthly per capita expenditure (Rs)'.\n"
                 "\n"
                 "VALUE LABELS\n"
                 "  toilet bank 0 'No' 1 'Yes'\n"
                 "  /edu_cat 0 'None' 1 'Primary (1-5)' 2 'Secondary (6-10)' 3 'Higher (11+)'\n"
                 "  /caste_n 1 'General' 2 'OBC' 3 'SC' 4 'ST'.\n"
                 "\n"
                 "FREQUENCIES VARIABLES=toilet edu_cat caste_n.\n"
                 "SAVE OUTFILE='C:\\impactmojo\\spss\\households_clean.sav'."},
             {"t": "ul", "items": [
                 "<code class=\"inline\">(has_toilet = 'Yes')</code> is a logical expression: it is 1 when true "
                 "and 0 when false. String comparisons in SPSS are case-sensitive, so "
                 "<code class=\"inline\">'yes'</code> would match nothing in this file.",
                 "The frequency table for <code class=\"inline\">edu_cat</code> should show the four labels, "
                 "summing to 240, and no missing values.",
                 "A <code class=\"inline\">.sav</code> file keeps your labels, which a CSV cannot.",
             ]},
             {"t": "p", "html": "The R version of the indicator and the bands, to check your frequencies:"},
             {"t": "code", "lang": "r", "code": R["compute"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Add "
                                   "<code class=\"inline\">COMPUTE large_hh = (hh_size &gt;= 6).</code>, give it the "
                                   "No/Yes value labels, and run "
                                   "<code class=\"inline\">CROSSTABS /TABLES=large_hh BY area.</code> In the R "
                                   "cell, add <code class=\"inline\">table(hh$hh_size &gt;= 6, hh$area)</code> and "
                                   "compare."},
         ]},
        {"tab": "Aggregate and merge",
         "title": "AGGREGATE, MATCH FILES and restructuring",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">AGGREGATE</code> summarises by group. With "
                                "<code class=\"inline\">MODE=ADDVARIABLES</code> it adds the group value to every "
                                "case and keeps all 240 households; with an output file it writes one row per "
                                "group."},
             {"t": "syntax", "label": "SPSS syntax: 04_aggregate.sps", "code":
                 "GET FILE='C:\\impactmojo\\spss\\households_clean.sav'.\n"
                 "\n"
                 "* District mean on every household row.\n"
                 "AGGREGATE\n"
                 "  /OUTFILE=* MODE=ADDVARIABLES\n"
                 "  /BREAK=district\n"
                 "  /district_mean=MEAN(monthly_pc_exp).\n"
                 "\n"
                 "* One row per district, in a separate file.\n"
                 "AGGREGATE\n"
                 "  /OUTFILE='C:\\impactmojo\\spss\\district_summary.sav'\n"
                 "  /BREAK=district\n"
                 "  /mean_exp=MEAN(monthly_pc_exp)\n"
                 "  /mean_size=MEAN(hh_size)\n"
                 "  /n=N."},
             {"t": "p", "html": "Open <code class=\"inline\">district_summary.sav</code> afterwards: it should have "
                                "10 rows and the <code class=\"inline\">n</code> column should sum to 240. The R "
                                "cell gives the same district means:"},
             {"t": "code", "lang": "r", "code": R["aggregate"]},
             {"t": "h3", "html": "MATCH FILES: attach district information"},
             {"t": "p", "html": "Each household belongs to one district and each district has many households, "
                                "so the district file is a <em>table lookup</em>: "
                                "<code class=\"inline\">/TABLE</code> in "
                                "<code class=\"inline\">MATCH FILES</code>. Both files must be sorted by the key, "
                                "and you should give a text key the same width in both files, which is why both "
                                "<code class=\"inline\">GET DATA</code> commands give "
                                "<code class=\"inline\">district</code> the format "
                                "<code class=\"inline\">A12</code>."},
             {"t": "syntax", "label": "SPSS syntax: 05_match.sps", "code":
                 "GET DATA\n"
                 "  /TYPE=TXT\n"
                 "  /FILE='C:\\impactmojo\\spss\\districts.csv'\n"
                 "  /DELIMITERS=\",\"\n"
                 "  /QUALIFIER='\"'\n"
                 "  /ARRANGEMENT=DELIMITED\n"
                 "  /FIRSTCASE=2\n"
                 "  /VARIABLES=\n"
                 "    district A12\n"
                 "    state A16\n"
                 "    region A8\n"
                 "    programme_phase F1.0\n"
                 "    field_team A8.\n"
                 "SORT CASES BY district.\n"
                 "SAVE OUTFILE='C:\\impactmojo\\spss\\districts.sav'.\n"
                 "\n"
                 "GET FILE='C:\\impactmojo\\spss\\households_clean.sav'.\n"
                 "SORT CASES BY district.\n"
                 "MATCH FILES\n"
                 "  /FILE=*\n"
                 "  /TABLE='C:\\impactmojo\\spss\\districts.sav'\n"
                 "  /IN=in_district\n"
                 "  /BY district.\n"
                 "EXECUTE.\n"
                 "FREQUENCIES VARIABLES=in_district state."},
             {"t": "ul", "items": [
                 "<code class=\"inline\">/IN=in_district</code> makes a 0/1 flag: 1 when the household found its "
                 "district in the table. Its frequency table should show 240 cases coded 1. In real files, a "
                 "misspelt district (Purnea for Purnia) appears as a 0.",
                 "For two files with one row per household each (a <code class=\"inline\">1:1</code> join, such "
                 "as two modules of the same survey), use two <code class=\"inline\">/FILE</code> subcommands: "
                 "<code class=\"inline\">MATCH FILES /FILE='roster.sav' /FILE='programme.sav' /BY hh_id.</code>",
             ]},
             {"t": "code", "lang": "r", "code": R["match"]},
             {"t": "h3", "html": "Restructure: cases to variables and back"},
             {"t": "syntax", "label": "SPSS syntax: long to wide", "code":
                 "GET FILE='C:\\impactmojo\\spss\\households_clean.sav'.\n"
                 "AGGREGATE /OUTFILE=* /BREAK=district area /monthly_pc_exp=MEAN(monthly_pc_exp).\n"
                 "SORT CASES BY district area.\n"
                 "CASESTOVARS /ID=district /INDEX=area."},
             {"t": "p", "html": "After <code class=\"inline\">CASESTOVARS</code> the active file should have 10 rows "
                                "and one expenditure column per area. "
                                "<code class=\"inline\">VARSTOCASES</code> goes the other way; read the new "
                                "column names in Variable View and list them after "
                                "<code class=\"inline\">/MAKE monthly_pc_exp FROM</code>."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the "
                                   "<code class=\"inline\">/BREAK</code> of the district summary to "
                                   "<code class=\"inline\">caste</code> and add "
                                   "<code class=\"inline\">/toilet_share=MEAN(toilet)</code>. You should get four "
                                   "rows. Change the R cell to group by caste and check the means."},
         ]},
        {"tab": "Weights and Complex Samples",
         "title": "WEIGHT BY, and Complex Samples for NFHS",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">WEIGHT BY</code> makes every following procedure count "
                                "each case as many times as its weight. Our course file has no sampling weight, "
                                "but weighting each household by its size shows what a weight does: the "
                                "per-household average becomes a per-person average."},
             {"t": "syntax", "label": "SPSS syntax: 06_weight.sps", "code":
                 "GET FILE='C:\\impactmojo\\spss\\households_clean.sav'.\n"
                 "DESCRIPTIVES VARIABLES=monthly_pc_exp /STATISTICS=MEAN.\n"
                 "WEIGHT BY hh_size.\n"
                 "DESCRIPTIVES VARIABLES=monthly_pc_exp /STATISTICS=MEAN.\n"
                 "WEIGHT OFF."},
             {"t": "p", "html": "Compare the two means and the two N values. With "
                                "<code class=\"inline\">WEIGHT BY hh_size</code> the N becomes the number of "
                                "people, because SPSS treats each household as hh_size copies of itself. The R "
                                "cell computes both:"},
             {"t": "code", "lang": "r", "code": R["weight"]},
             {"t": "info", "tone": "warning", "html": "<strong>WEIGHT BY gives the right estimate and the wrong "
                                                       "standard error for a survey.</strong> IBM's Complex Samples "
                                                       "manual says that sampling weights \"should not be used with "
                                                       "other analytical procedures via the Weight Cases procedure, "
                                                       "which treats weights as case replications\". For NFHS, "
                                                       "define the design with Complex Samples instead."},
             {"t": "h3", "html": "An NFHS analysis plan"},
             {"t": "p", "html": "NFHS uses the DHS recode variable names. The DHS Recode VII manual defines "
                                "<code class=\"inline\">v005</code> as the sample weight with six implied decimal "
                                "places (divide by 1,000,000), <code class=\"inline\">v021</code> as the primary "
                                "sampling unit and <code class=\"inline\">v022</code> as the \"sample strata for "
                                "sampling errors\". In SPSS you save these in an analysis plan file with "
                                "<code class=\"inline\">CSPLAN</code>, then name the plan in every "
                                "<code class=\"inline\">CS</code> procedure. The pattern below follows the SPSS "
                                "example in the DHS Program's <em>Guide to DHS Statistics</em>."},
             {"t": "syntax", "label": "SPSS syntax: NFHS women's file (not part of the course data)", "code":
                 "* Open the NFHS women's (IR) SPSS file you downloaded from the DHS Program.\n"
                 "GET FILE='C:\\nfhs\\your_nfhs_women_file.sav'.\n"
                 "\n"
                 "COMPUTE wt = v005 / 1000000.\n"
                 "COMPUTE modern_use = (v313 = 3).\n"
                 "EXECUTE.\n"
                 "\n"
                 "CSPLAN ANALYSIS\n"
                 "  /PLAN FILE='C:\\nfhs\\nfhs_ir.csplan'\n"
                 "  /PLANVARS ANALYSISWEIGHT=wt\n"
                 "  /DESIGN STRATA=v022 CLUSTER=v021\n"
                 "  /ESTIMATOR TYPE=WR.\n"
                 "\n"
                 "CSDESCRIPTIVES\n"
                 "  /PLAN FILE='C:\\nfhs\\nfhs_ir.csplan'\n"
                 "  /SUMMARY VARIABLES=modern_use\n"
                 "  /SUBPOP TABLE=v024 DISPLAY=LAYERED\n"
                 "  /MEAN\n"
                 "  /STATISTICS SE CIN\n"
                 "  /MISSING SCOPE=ANALYSIS CLASSMISSING=EXCLUDE."},
             {"t": "ul", "items": [
                 "The menu route to build the plan is <strong>Analyze &gt; Complex Samples &gt; Prepare for "
                 "Analysis</strong>; its wizard can paste the <code class=\"inline\">CSPLAN</code> command. The "
                 "estimates are under <strong>Analyze &gt; Complex Samples &gt; Descriptives</strong>, "
                 "<strong>Frequencies</strong>, <strong>Crosstabs</strong> and <strong>General Linear "
                 "Model</strong>.",
                 "The DHS guide's own example uses <code class=\"inline\">v023</code> as the stratum and notes that "
                 "strata are not defined the same way in every survey; it suggests region by urban/rural "
                 "(<code class=\"inline\">v024</code> by <code class=\"inline\">v025</code>) when that is how the "
                 "sample was drawn. Check Appendix A of the survey report before you choose.",
                 "<code class=\"inline\">/SUBPOP TABLE=v024</code> estimates for each value of "
                 "<code class=\"inline\">v024</code> while keeping the whole design, which is the right way to "
                 "get subgroup estimates. Filtering cases out with "
                 "<code class=\"inline\">SELECT IF</code> first would drop design information.",
                 "IBM's Complex Samples manual (version 31) says these procedures are included in SPSS "
                 "Statistics Premium Edition or the Complex Samples option. Check your licence before you "
                 "plan an NFHS analysis around them.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> In the course file, run "
                                   "<code class=\"inline\">DESCRIPTIVES VARIABLES=toilet</code> with and without "
                                   "<code class=\"inline\">WEIGHT BY hh_size</code>. Write a comment in your syntax "
                                   "file saying which mean is the share of households with a toilet and which is "
                                   "the share of people."},
         ]},
        {"tab": "Regression",
         "title": "REGRESSION and a chart",
         "blocks": [
             {"t": "p", "html": "SPSS <code class=\"inline\">REGRESSION</code> takes numeric predictors only, so a "
                                "categorical variable needs dummy variables, one for each group except the "
                                "reference group (General here). The menu route is <strong>Analyze &gt; "
                                "Regression &gt; Linear</strong>."},
             {"t": "syntax", "label": "SPSS syntax: 07_regression.sps", "code":
                 "GET FILE='C:\\impactmojo\\spss\\households_clean.sav'.\n"
                 "COMPUTE obc = (caste = 'OBC').\n"
                 "COMPUTE sc = (caste = 'SC').\n"
                 "COMPUTE st = (caste = 'ST').\n"
                 "COMPUTE urban = (area = 'Urban').\n"
                 "EXECUTE.\n"
                 "\n"
                 "REGRESSION\n"
                 "  /STATISTICS COEFF OUTS R ANOVA CI(95)\n"
                 "  /DEPENDENT monthly_pc_exp\n"
                 "  /METHOD=ENTER obc sc st head_edu_years urban.\n"
                 "\n"
                 "GRAPH /BAR(SIMPLE)=MEAN(monthly_pc_exp) BY caste."},
             {"t": "p", "html": "In the Coefficients table, read the column labelled B: each caste coefficient is "
                                "the difference from General households with the same schooling and area. The R "
                                "cell fits the same model with the same dummies, so the B column in your output "
                                "should match its Estimate column, and R Square should match too."},
             {"t": "code", "lang": "r", "code": R["regression"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Add <code class=\"inline\">land_acres</code> to "
                                   "<code class=\"inline\">/METHOD=ENTER</code> and run again. In the R cell, add "
                                   "<code class=\"inline\">+ land_acres</code> to the formula and check that both "
                                   "give the same coefficients."},
         ]},
        {"tab": "Reproducible SPSS",
         "title": "A master syntax file and saved output",
         "blocks": [
             {"t": "p", "html": "Keep each step in its own <code class=\"inline\">.sps</code> file and run them "
                                "in order from one master file. <code class=\"inline\">INSERT</code> runs another "
                                "syntax file."},
             {"t": "syntax", "label": "SPSS syntax: 00_master.sps", "code":
                 "* 00_master.sps : the whole analysis, from CSV to tables.\n"
                 "INSERT FILE='C:\\impactmojo\\spss\\01_import.sps'.\n"
                 "INSERT FILE='C:\\impactmojo\\spss\\03_recode.sps'.\n"
                 "INSERT FILE='C:\\impactmojo\\spss\\04_aggregate.sps'.\n"
                 "INSERT FILE='C:\\impactmojo\\spss\\05_match.sps'.\n"
                 "INSERT FILE='C:\\impactmojo\\spss\\07_regression.sps'.\n"
                 "OUTPUT SAVE OUTFILE='C:\\impactmojo\\spss\\analysis_output.spv'."},
             {"t": "ul", "items": [
                 "Never edit the raw CSV, and never fix a value by typing in the Data Editor. Put every change "
                 "in syntax so it can be re-run and checked.",
                 "Comment each block with what it does and why: "
                 "<code class=\"inline\">* Drop test interviews done before 1 March.</code>",
                 "Use full paths, or set one folder at the top and keep every file in it, so the syntax runs "
                 "on a colleague's computer after one edit.",
                 "Save output (<code class=\"inline\">.spv</code>) alongside the syntax that made it, with the "
                 "same date in both file names.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> Build <code class=\"inline\">00_master.sps</code> from "
                                   "the files you wrote, close SPSS, open it again, and run only the master file. "
                                   "If every table comes back, your analysis is reproducible."},
             {"t": "h3", "html": "IBM's own documentation"},
             {"t": "ul", "items": [
                 "<a href=\"https://www.ibm.com/products/spss-statistics\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">IBM SPSS Statistics</a>, with a free trial and links to the "
                 "documentation.",
                 "<a href=\"https://www.ibm.com/docs/en/SSLVMB_31.0.0/statistics_reference_project_ddita/spss/complex_samples/syn_csplan_examples.html\" "
                 "rel=\"noopener\" target=\"_blank\" style=\"color:var(--accent-color)\">CSPLAN examples</a> in the "
                 "Command Syntax Reference.",
                 "<a href=\"https://dhsprogram.com/data/Guide-to-DHS-Statistics/Analyzing_DHS_Data.htm\" "
                 "rel=\"noopener\" target=\"_blank\" style=\"color:var(--accent-color)\">Guide to DHS Statistics: "
                 "analyzing DHS data</a>, with weights and complex designs in SPSS, Stata and R.",
             ]},
         ]},
    ],
    "next": [
        {"href": "/code/jamovi-jasp.html", "title": "jamovi and JASP",
         "desc": "Free point-and-click statistics with an SPSS-like layout, built on R."},
        {"href": "/code/stata.html", "title": "Stata Syntax for Development Data",
         "desc": "The same arc in Stata do-files, including svyset for NFHS."},
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "Run the same steps in free software, live in your browser."},
        {"href": "/101-courses/stats-without-code.html", "title": "Statistics Without Code 101",
         "desc": "The ideas behind the tables, without software."},
        {"href": "/101-courses/survey-design.html", "title": "Survey Design 101",
         "desc": "Why NFHS is stratified and clustered, and what that does to your standard errors."},
    ],
}

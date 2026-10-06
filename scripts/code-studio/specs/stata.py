# -*- coding: utf-8 -*-
"""Stata Syntax for Development Data: a guided course in do-files, with R cells that run the same steps here.

Facts checked on 6 October 2026 against StataCorp's own pages and manuals (stata.com), the DHS Program's
Guide to DHS Statistics and the DHS Recode VII manual. Sources are listed in the agent report.
"""

DL = ('<a href="/code/data/households.csv" download style="color:var(--accent-color)">households.csv</a>')
DD = ('<a href="/code/data/districts.csv" download style="color:var(--accent-color)">districts.csv</a>')

R = {}
R["look"] = ('hh <- read.csv("households.csv")\n'
             'str(hh)\n'
             'summary(hh$monthly_pc_exp)\n'
             'table(hh$caste)\n'
             'table(hh$caste, hh$area)')
R["newvars"] = ('hh <- read.csv("households.csv")\n'
                '# Stata: generate toilet = (has_toilet == "Yes")\n'
                'hh$toilet <- as.integer(hh$has_toilet == "Yes")\n'
                '# Stata: recode head_edu_years (0=0) (1/5=1) (6/10=2) (11/max=3), generate(edu_cat)\n'
                'hh$edu_cat <- cut(hh$head_edu_years, breaks = c(-Inf, 0, 5, 10, Inf),\n'
                '                  labels = c("None", "Primary (1-5)", "Secondary (6-10)", "Higher (11+)"))\n'
                'table(hh$edu_cat)\n'
                'mean(hh$toilet)')
R["egen"] = ('hh <- read.csv("households.csv")\n'
             '# Stata: egen district_mean = mean(monthly_pc_exp), by(district)\n'
             'hh$district_mean <- ave(hh$monthly_pc_exp, hh$district)\n'
             'head(hh[, c("hh_id", "district", "monthly_pc_exp", "district_mean")])\n'
             '# Stata: collapse (mean) monthly_pc_exp hh_size (count) n = hh_id, by(district)\n'
             'by_d <- aggregate(cbind(monthly_pc_exp, hh_size) ~ district, data = hh, FUN = mean)\n'
             'by_d$n <- as.vector(table(hh$district)[by_d$district])\n'
             'by_d')
R["merge"] = ('hh <- read.csv("households.csv")\n'
              'd  <- read.csv("districts.csv")\n'
              '# Stata: merge m:1 district using districts\n'
              'm <- merge(hh, d, by = "district", all.x = TRUE)\n'
              'nrow(m)\n'
              'sum(is.na(m$state))   # households with no district match: Stata\'s _merge == 1\n'
              'table(m$state)')
R["reshape"] = ('hh <- read.csv("households.csv")\n'
                '# Stata: collapse (mean) monthly_pc_exp, by(district area)\n'
                'long <- aggregate(monthly_pc_exp ~ district + area, data = hh, FUN = mean)\n'
                'nrow(long)\n'
                '# Stata: reshape wide monthly_pc_exp, i(district) j(area) string\n'
                'wide <- reshape(long, idvar = "district", timevar = "area", direction = "wide")\n'
                'wide')
R["weights"] = ('hh <- read.csv("households.csv")\n'
                '# Stata: mean monthly_pc_exp   and   mean monthly_pc_exp [pw=hh_size]\n'
                'c(per_household = mean(hh$monthly_pc_exp),\n'
                '  per_person    = weighted.mean(hh$monthly_pc_exp, hh$hh_size))\n'
                '# the same two numbers by caste\n'
                'sapply(split(hh, hh$caste), function(g)\n'
                '  c(per_household = mean(g$monthly_pc_exp),\n'
                '    per_person    = weighted.mean(g$monthly_pc_exp, g$hh_size)))')
R["regress"] = ('hh <- read.csv("households.csv")\n'
                'hh$caste <- factor(hh$caste)   # levels in alphabetical order, as Stata\'s encode does\n'
                'hh$area  <- factor(hh$area)\n'
                '# Stata: regress monthly_pc_exp i.caste_n head_edu_years i.area_n\n'
                'fit <- lm(monthly_pc_exp ~ caste + head_edu_years + area, data = hh)\n'
                'round(summary(fit)$coefficients, 2)\n'
                '# Stata: margins caste_n\n'
                '# set every household to one caste in turn, predict, and average\n'
                'sapply(levels(hh$caste), function(k) {\n'
                '  nd <- hh\n'
                '  nd$caste <- factor(k, levels = levels(hh$caste))\n'
                '  round(mean(predict(fit, nd)), 1)\n'
                '})')
R["graph"] = ('hh <- read.csv("households.csv")\n'
              '# Stata: graph bar (mean) monthly_pc_exp, over(caste_n)\n'
              'm <- tapply(hh$monthly_pc_exp, hh$caste, mean)\n'
              'barplot(m, ylab = "Mean monthly per capita expenditure (Rs)",\n'
              '        main = "Illustrative data, invented for teaching")')

PAGE = {
    "slug": "stata",
    "order": 10,
    "kind": "guide",
    "tool": "Stata",
    "title": "Stata Syntax for Development Data",
    "h1": "Stata syntax for development data",
    "lede": ("Write Stata do-files from your first import to a weighted regression: describe, generate, recode, "
             "labels, egen, collapse, merge, reshape, svyset for NFHS-style surveys, regress and margins, "
             "graphs and logs. Follow along in your own copy of Stata with two small CSV files, and check each "
             "step in R on this page."),
    "description": ("A free guided course in Stata syntax for development practitioners in South Asia: do-files, "
                    "import delimited, describe, tabulate, generate, recode, labels, egen, collapse, merge, "
                    "reshape, svyset with NFHS weights and design variables, regress, margins, graphs and logs."),
    "card": "Do-files from import to svyset and margins, on a household survey you can download and follow along with.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>Stata does not run in a browser.</strong> The grey boxes are do-file lines for you to "
                    "type into your own Stata. This page does not show Stata output, because it cannot produce "
                    "any; each module tells you what to look for on your screen instead. Where the same step can "
                    "be done in R, an R cell runs it here on the same data, so you can check your Stata numbers "
                    "against it. The first R run downloads the R engine once (about 7&nbsp;MB)."),
    "modules": [
        {"tab": "Set up",
         "title": "Stata, the do-file and your project folder",
         "blocks": [
             {"t": "p", "html": "Stata is a paid statistics package from StataCorp, used widely in development "
                                "economics, evaluation teams and survey firms. Most published replication files "
                                "for NFHS, PLFS and IHDS analyses are Stata do-files, so reading Stata is useful "
                                "even if you work in R."},
             {"t": "info", "html": "<strong>Version and cost, checked 6 October 2026.</strong> The current release "
                                   "is <strong>Stata 19</strong> (StataCorp's citation for it reads "
                                   "\"StataCorp. 2025. Stata 19\"). Annual licences also carry "
                                   "<strong>StataNow</strong>, which adds new features during the release. Stata "
                                   "comes in three editions, Stata/BE (basic, mid-sized datasets), Stata/SE "
                                   "(larger datasets) and Stata/MP (multicore, the largest datasets), and all "
                                   "three run on Windows, macOS and Linux. StataCorp's "
                                   "<a href=\"https://www.stata.com/order/\" rel=\"noopener\" target=\"_blank\" "
                                   "style=\"color:var(--accent-color)\">order page</a> asks for your country "
                                   "before it shows a price, and buyers in many countries go through an "
                                   "<a href=\"https://www.stata.com/worldwide/\" rel=\"noopener\" target=\"_blank\" "
                                   "style=\"color:var(--accent-color)\">authorised international reseller</a>. "
                                   "Check with your university or organisation before you buy: many hold a "
                                   "site licence."},
             {"t": "h3", "html": "The five main windows"},
             {"t": "p", "html": "Stata's own <em>Getting Started</em> manual names five main windows: "
                                "<strong>History</strong> (commands you have run), <strong>Results</strong> "
                                "(output), <strong>Command</strong> (where you type one command and press Enter), "
                                "<strong>Variables</strong> (the variables in memory) and "
                                "<strong>Properties</strong> (details of the selected variable). The menus can "
                                "build most commands for you, and the command they build appears in the Results "
                                "window, which is a good way to learn syntax."},
             {"t": "h3", "html": "Work in a do-file from the first day"},
             {"t": "p", "html": "A do-file is a plain text file of commands that Stata runs from top to bottom. "
                                "It is your record of what you did, and anyone with the same data can re-run it "
                                "and get the same numbers. Open the Do-file Editor by clicking its button on the "
                                "toolbar or by typing <code class=\"inline\">doedit</code> in the Command window."},
             {"t": "steps", "items": [
                 "Make a project folder, for example <code class=\"inline\">C:\\impactmojo\\stata</code> on "
                 "Windows or <code class=\"inline\">~/impactmojo/stata</code> on a Mac.",
                 "Download the two course files into it: " + DL + " (240 households) and " + DD + " (10 "
                 "districts). <span class=\"illustrative-tag\">Illustrative data, invented for teaching</span> "
                 "The district names are real places; every number is made up.",
                 "In Stata, type <code class=\"inline\">doedit</code> in the Command window and press Enter.",
                 "Type the lines below into the new do-file and save it in your project folder as "
                 "<code class=\"inline\">01_setup.do</code>.",
                 "Click the <strong>Do</strong> button (Execute (do)) on the Do-file Editor toolbar. If you "
                 "highlight some lines first, the same button runs only those lines.",
             ]},
             {"t": "syntax", "label": "Stata do-file: 01_setup.do", "code":
                 "* 01_setup.do : first do-file for the Code Studio Stata course\n"
                 "version 19            // run as Stata 19, even in a later Stata\n"
                 "clear all             // start with nothing in memory\n"
                 "cd \"C:\\impactmojo\\stata\"   // change to YOUR project folder\n"
                 "pwd                   // print the working folder, to check\n"
                 "dir *.csv             // you should see households.csv and districts.csv"},
             {"t": "p", "html": "Lines starting with <code class=\"inline\">*</code> are comments, and "
                                "<code class=\"inline\">//</code> starts a comment at the end of a line. "
                                "Look in the Results window: <code class=\"inline\">pwd</code> should print your "
                                "folder, and <code class=\"inline\">dir</code> should list both CSV files. If "
                                "<code class=\"inline\">cd</code> fails, the path is wrong; copy it from your "
                                "file manager's address bar."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the <code class=\"inline\">cd</code> line to "
                                   "your own folder, run the do-file, then type "
                                   "<code class=\"inline\">help import delimited</code> in the Command window. "
                                   "Every Stata command has a help file like this, with the syntax at the top and "
                                   "worked examples at the bottom."},
         ]},
        {"tab": "Import and look",
         "title": "Import a CSV and look at it",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">import delimited</code> reads comma-separated and "
                                "tab-separated text files. With the variable names in the first row, as in our "
                                "files, it needs only the file name. Then look before you change anything."},
             {"t": "syntax", "label": "Stata do-file: 02_look.do", "code":
                 "version 19\n"
                 "clear all\n"
                 "cd \"C:\\impactmojo\\stata\"\n"
                 "import delimited using \"households.csv\", clear\n"
                 "\n"
                 "describe                         // variables, types, number of observations\n"
                 "codebook district caste, compact\n"
                 "list in 1/5                      // first five households\n"
                 "summarize monthly_pc_exp hh_size head_edu_years\n"
                 "summarize monthly_pc_exp, detail // adds percentiles and the median\n"
                 "tabulate caste\n"
                 "tabulate caste area              // two-way table\n"
                 "tabulate caste area, row         // row percentages"},
             {"t": "h3", "html": "What to look for"},
             {"t": "ul", "items": [
                 "<code class=\"inline\">describe</code> should report 240 observations and 13 variables. "
                 "Variables holding text (<code class=\"inline\">district</code>, <code class=\"inline\">caste</code>, "
                 "<code class=\"inline\">has_toilet</code> and the other Yes/No columns) show a "
                 "<code class=\"inline\">str</code> storage type. Stata cannot run numeric commands on them until "
                 "you convert them, which is the next module.",
                 "In <code class=\"inline\">tabulate caste</code> the Freq. column should sum to 240, with four "
                 "rows: General, OBC, SC and ST.",
                 "In <code class=\"inline\">summarize, detail</code> compare the mean with the 50% percentile "
                 "(the median). Expenditure is usually skewed to the right, so the mean sits above the median.",
             ]},
             {"t": "p", "html": "The same look in R, on the same file, runs here. Use it to check the counts in "
                                "your Stata tables."},
             {"t": "code", "lang": "r", "code": R["look"]},
             {"t": "info", "html": "<strong>Exercise.</strong> In Stata, run "
                                   "<code class=\"inline\">tabulate district area</code> and find the district with "
                                   "the most urban households. In the R cell, change the last line to "
                                   "<code class=\"inline\">table(hh$district, hh$area)</code>, run it, and check "
                                   "that the two tables agree."},
         ]},
        {"tab": "New variables",
         "title": "generate, replace, recode, encode and labels",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">generate</code> makes a new variable; "
                                "<code class=\"inline\">replace</code> changes values in one that exists. Stata "
                                "refuses to <code class=\"inline\">generate</code> a name already in use, which "
                                "protects you from overwriting a variable by accident."},
             {"t": "syntax", "label": "Stata do-file: 03_newvars.do", "code":
                 "version 19\n"
                 "clear all\n"
                 "cd \"C:\\impactmojo\\stata\"\n"
                 "import delimited using \"households.csv\", clear\n"
                 "\n"
                 "* 0/1 indicators from Yes/No text\n"
                 "generate toilet = (has_toilet == \"Yes\")\n"
                 "generate bank   = (has_bank_account == \"Yes\")\n"
                 "generate annual_pc_exp = monthly_pc_exp * 12\n"
                 "\n"
                 "* replace changes values in an existing variable\n"
                 "generate low_exp = 0\n"
                 "replace  low_exp = 1 if monthly_pc_exp < 2000\n"
                 "\n"
                 "* recode a number into bands, with value labels, into a new variable\n"
                 "recode head_edu_years (0 = 0 \"None\") (1/5 = 1 \"Primary (1-5)\") ///\n"
                 "    (6/10 = 2 \"Secondary (6-10)\") (11/max = 3 \"Higher (11+)\"), generate(edu_cat)\n"
                 "tabulate edu_cat\n"
                 "\n"
                 "* encode turns text into numbers with labels (codes follow alphabetical order)\n"
                 "encode caste, generate(caste_n)\n"
                 "encode area,  generate(area_n)\n"
                 "tabulate caste_n\n"
                 "tabulate caste_n, nolabel        // see the numbers behind the labels"},
             {"t": "h3", "html": "Labels: say what a variable means"},
             {"t": "p", "html": "A variable label describes the variable. A value label names each code. You "
                                "define a value label once with <code class=\"inline\">label define</code>, then "
                                "attach it with <code class=\"inline\">label values</code>."},
             {"t": "syntax", "label": "Stata do-file: add to 03_newvars.do", "code":
                 "label variable toilet \"Household has a toilet (1 = yes)\"\n"
                 "label variable monthly_pc_exp \"Monthly per capita expenditure (Rs)\"\n"
                 "\n"
                 "label define yesno 0 \"No\" 1 \"Yes\"\n"
                 "label values toilet bank low_exp yesno\n"
                 "\n"
                 "describe toilet bank low_exp edu_cat caste_n\n"
                 "tabulate toilet\n"
                 "save households_clean, replace   // Stata's own .dta format, labels included"},
             {"t": "ul", "items": [
                 "After <code class=\"inline\">encode</code>, <code class=\"inline\">tabulate caste_n, nolabel</code> "
                 "should show codes 1 to 4, with 1 for General and 4 for ST, because "
                 "<code class=\"inline\">encode</code> assigns codes in alphabetical order.",
                 "<code class=\"inline\">tabulate toilet</code> should now show the words No and Yes, and the two "
                 "frequencies should sum to 240.",
                 "<code class=\"inline\">///</code> at the end of a line tells a do-file that the command "
                 "continues on the next line.",
             ]},
             {"t": "p", "html": "The R version of the indicator and the education bands:"},
             {"t": "code", "lang": "r", "code": R["newvars"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Make a variable <code class=\"inline\">large_hh</code> "
                                   "equal to 1 when <code class=\"inline\">hh_size</code> is 6 or more, give it the "
                                   "<code class=\"inline\">yesno</code> label, and tabulate it against "
                                   "<code class=\"inline\">area_n</code>. In the R cell, add "
                                   "<code class=\"inline\">table(hh$hh_size &gt;= 6, hh$area)</code> and compare."},
         ]},
        {"tab": "egen and collapse",
         "title": "Group summaries: egen and collapse",
         "blocks": [
             {"t": "p", "html": "Two commands summarise by group, and they differ in what they leave in memory. "
                                "<code class=\"inline\">egen ..., by()</code> adds a column and keeps every "
                                "household. <code class=\"inline\">collapse</code> replaces the data with one row "
                                "per group. Use <code class=\"inline\">egen</code> when you want to compare each "
                                "household with its district; use <code class=\"inline\">collapse</code> when you "
                                "want a district table."},
             {"t": "syntax", "label": "Stata do-file: 04_groups.do", "code":
                 "version 19\n"
                 "clear all\n"
                 "cd \"C:\\impactmojo\\stata\"\n"
                 "use households_clean, clear\n"
                 "\n"
                 "* egen: one new column, all 240 rows kept\n"
                 "egen district_mean = mean(monthly_pc_exp), by(district)\n"
                 "egen district_n    = count(hh_id), by(district)\n"
                 "generate above_district = monthly_pc_exp > district_mean\n"
                 "list hh_id district monthly_pc_exp district_mean in 1/5\n"
                 "\n"
                 "* collapse: one row per district (preserve/restore brings the households back)\n"
                 "preserve\n"
                 "collapse (mean) monthly_pc_exp hh_size toilet (count) n = hh_id, by(district)\n"
                 "list\n"
                 "export delimited using \"district_summary.csv\", replace\n"
                 "restore\n"
                 "describe, short    // back to 240 observations"},
             {"t": "ul", "items": [
                 "After <code class=\"inline\">collapse</code>, <code class=\"inline\">list</code> should show 10 "
                 "rows, one per district, and the <code class=\"inline\">n</code> column should sum to 240.",
                 "<code class=\"inline\">preserve</code> takes a copy of the data and "
                 "<code class=\"inline\">restore</code> puts it back, so one do-file can make a summary table "
                 "and carry on with the household data.",
             ]},
             {"t": "p", "html": "In R, <code class=\"inline\">ave()</code> plays the part of "
                                "<code class=\"inline\">egen, by()</code> and <code class=\"inline\">aggregate()</code> "
                                "the part of <code class=\"inline\">collapse</code>. Check the district means "
                                "against your Stata list."},
             {"t": "code", "lang": "r", "code": R["egen"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the <code class=\"inline\">by()</code> in the "
                                   "Stata <code class=\"inline\">collapse</code> to <code class=\"inline\">by(caste)</code> "
                                   "and run again; you should get four rows. In the R cell, change "
                                   "<code class=\"inline\">~ district</code> to <code class=\"inline\">~ caste</code> "
                                   "and <code class=\"inline\">hh$district</code> to "
                                   "<code class=\"inline\">hh$caste</code> in both places."},
         ]},
        {"tab": "Merge and reshape",
         "title": "merge (1:1 and m:1) and reshape",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">merge</code> adds variables from a second Stata file "
                                "(the <em>using</em> file) to the data in memory (the <em>master</em>), matching "
                                "on key variables. Each household belongs to one district, and each district has "
                                "many households, so attaching the district file is a many-to-one, "
                                "<code class=\"inline\">m:1</code>, merge. The using file must be a "
                                "<code class=\"inline\">.dta</code>, so save the districts first."},
             {"t": "syntax", "label": "Stata do-file: 05_merge.do", "code":
                 "version 19\n"
                 "clear all\n"
                 "cd \"C:\\impactmojo\\stata\"\n"
                 "\n"
                 "* the using file must be a Stata .dta\n"
                 "import delimited using \"districts.csv\", clear\n"
                 "isid district                 // stops with an error if district is not unique\n"
                 "save districts, replace\n"
                 "\n"
                 "use households_clean, clear\n"
                 "merge m:1 district using districts\n"
                 "tabulate _merge\n"
                 "assert _merge == 3            // stop the do-file if any row failed to match\n"
                 "drop _merge"},
             {"t": "h3", "html": "Read _merge every time"},
             {"t": "p", "html": "<code class=\"inline\">merge</code> creates a variable "
                                "<code class=\"inline\">_merge</code>: 1 means the row was only in the master "
                                "(a household whose district is missing from the district file), 2 means only in "
                                "the using file, and 3 means matched. Here <code class=\"inline\">tabulate _merge</code> "
                                "should show 240 matched rows and nothing else. In real files a misspelt district "
                                "(Purnea for Purnia) shows up as a 1 and a 2, which is why the "
                                "<code class=\"inline\">assert</code> line is worth keeping."},
             {"t": "p", "html": "A <code class=\"inline\">1:1</code> merge joins two files with one row per key "
                                "on each side, such as two survey modules for the same households. To practise "
                                "one, split the household file into two and join it back:"},
             {"t": "syntax", "label": "Stata do-file: a 1:1 merge", "code":
                 "use households_clean, clear\n"
                 "preserve\n"
                 "keep hh_id shg_member received_transfer      // the 'programme module'\n"
                 "save hh_programme, replace\n"
                 "restore\n"
                 "drop shg_member received_transfer            // the 'roster module'\n"
                 "merge 1:1 hh_id using hh_programme\n"
                 "tabulate _merge                              // expect 240 matched\n"
                 "assert _merge == 3\n"
                 "drop _merge"},
             {"t": "p", "html": "The same district merge in R, with the R version of the "
                                "<code class=\"inline\">_merge</code> check:"},
             {"t": "code", "lang": "r", "code": R["merge"]},
             {"t": "h3", "html": "reshape: wide and long"},
             {"t": "p", "html": "Long data has one row per unit per category (district by area); wide data has "
                                "one row per unit and one column per category. "
                                "<code class=\"inline\">reshape</code> moves between them. You name the stub "
                                "(the variable that repeats), <code class=\"inline\">i()</code> (the unit) and "
                                "<code class=\"inline\">j()</code> (the category); add "
                                "<code class=\"inline\">string</code> when <code class=\"inline\">j</code> is text."},
             {"t": "syntax", "label": "Stata do-file: reshape", "code":
                 "use households_clean, clear\n"
                 "collapse (mean) monthly_pc_exp, by(district area)\n"
                 "list in 1/4                                        // long: 20 rows\n"
                 "reshape wide monthly_pc_exp, i(district) j(area) string\n"
                 "list                                               // wide: 10 rows\n"
                 "generate urban_rural_ratio = monthly_pc_expUrban / monthly_pc_expRural\n"
                 "reshape long monthly_pc_exp, i(district) j(area) string   // and back"},
             {"t": "p", "html": "After <code class=\"inline\">reshape wide</code> you should have 10 rows and two "
                                "new columns, <code class=\"inline\">monthly_pc_expRural</code> and "
                                "<code class=\"inline\">monthly_pc_expUrban</code>. Every district in this file "
                                "has both rural and urban households, so neither column has missing values. The "
                                "R version runs here:"},
             {"t": "code", "lang": "r", "code": R["reshape"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Repeat the reshape by head of household's gender: "
                                   "<code class=\"inline\">collapse (mean) monthly_pc_exp (count) n = hh_id, by(district head_gender)</code>, "
                                   "then <code class=\"inline\">reshape wide monthly_pc_exp n, i(district) j(head_gender) string</code>. "
                                   "Two stubs reshape together. Look at <code class=\"inline\">nFemale</code>: "
                                   "every district has some female-headed households, but in seven districts the "
                                   "mean rests on three or four of them. Say in a comment why you would not "
                                   "publish those seven means."},

         ]},
        {"tab": "Weights and svyset",
         "title": "Weights, and svyset for NFHS-style surveys",
         "blocks": [
             {"t": "p", "html": "Stata takes weights in square brackets after the variable list. The two you "
                                "will use most are <code class=\"inline\">[pw=...]</code> (probability or "
                                "sampling weights, the kind a survey supplies) and "
                                "<code class=\"inline\">[aw=...]</code> (analytic weights, used for averages of "
                                "group means). Our course file has no sampling weight, but it shows why weights "
                                "matter: each row is a household, and a household of eight people counts for "
                                "more people than a household of one. Weighting by household size turns a "
                                "per-household average into a per-person average."},
             {"t": "syntax", "label": "Stata do-file: 06_weights.do", "code":
                 "use households_clean, clear\n"
                 "mean monthly_pc_exp                    // average household\n"
                 "mean monthly_pc_exp [pw = hh_size]     // average person\n"
                 "mean monthly_pc_exp [pw = hh_size], over(caste_n)"},
             {"t": "p", "html": "The two means differ when large households are poorer or richer than small "
                                "ones. The R cell computes both, overall and by caste, so you can compare with "
                                "your Stata output:"},
             {"t": "code", "lang": "r", "code": R["weights"]},
             {"t": "h3", "html": "Declaring an NFHS design with svyset"},
             {"t": "p", "html": "NFHS is India's Demographic and Health Survey, and its files use the DHS recode "
                                "variable names. The DHS Recode VII manual defines the three you need: "
                                "<code class=\"inline\">v005</code> is the sample weight, \"an 8 digit variable "
                                "with 6 implied decimal places\", to be divided by 1,000,000 before use; "
                                "<code class=\"inline\">v021</code> is the primary sampling unit; and "
                                "<code class=\"inline\">v022</code> is the \"sample strata for sampling errors\", "
                                "the grouping of PSUs used for Taylor series variance estimates, which is the "
                                "method <code class=\"inline\">svy</code> uses by default. "
                                "<code class=\"inline\">svyset</code> declares this once, and every "
                                "<code class=\"inline\">svy:</code> command afterwards uses it."},
             {"t": "syntax", "label": "Stata do-file: NFHS women's file (not part of the course data)", "code":
                 "* Use the NFHS women's (IR) Stata file you downloaded from the DHS Program\n"
                 "use \"your_nfhs_women_file.dta\", clear\n"
                 "\n"
                 "generate wt = v005 / 1000000\n"
                 "svyset v021 [pw = wt], strata(v022)\n"
                 "svyset                                  // prints the design you declared\n"
                 "\n"
                 "* any 0/1 indicator you have built, e.g. currently using a modern method\n"
                 "generate modern_use = (v313 == 3)\n"
                 "svy: mean modern_use\n"
                 "svy: mean modern_use, over(v024)        // v024 is the DHS region variable; codebook v024 shows its labels\n"
                 "\n"
                 "* subpopulations: keep the full design, estimate for a subgroup\n"
                 "codebook v025                           // read the urban/rural codes first\n"
                 "generate rural = (v025 == 2)            // if codebook shows 2 = rural\n"
                 "svy, subpop(rural): mean modern_use"},
             {"t": "ul", "items": [
                 "The DHS Program's <em>Guide to DHS Statistics</em> uses the same "
                 "<code class=\"inline\">v313 == 3</code> definition of modern method use in its own Stata example, "
                 "and notes that strata are not defined the same way in every survey: its example uses "
                 "<code class=\"inline\">v023</code>, and it suggests region by urban/rural "
                 "(<code class=\"inline\">v024</code> by <code class=\"inline\">v025</code>) when that is how "
                 "the sample was drawn. Check Appendix A of the survey report before you choose.",
                 "Use <code class=\"inline\">subpop()</code> for a subgroup. Dropping the other rows with "
                 "<code class=\"inline\">keep if</code> throws away design information, and the standard errors "
                 "come out wrong.",
                 "The output of <code class=\"inline\">svy: mean</code> reports the number of strata, the number "
                 "of PSUs and the design degrees of freedom above the estimates. Read them: a PSU count far below "
                 "what the survey report says means the wrong variable went into "
                 "<code class=\"inline\">svyset</code>.",
             ]},
             {"t": "info", "tone": "warning", "html": "<strong>Weights change estimates; the design changes standard "
                                                       "errors.</strong> <code class=\"inline\">mean x [pw=wt]</code> "
                                                       "gives the right point estimate for NFHS, but only "
                                                       "<code class=\"inline\">svy: mean x</code> after "
                                                       "<code class=\"inline\">svyset</code> gives confidence "
                                                       "intervals that allow for clustering and stratification."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the course file, run "
                                   "<code class=\"inline\">mean toilet</code> and "
                                   "<code class=\"inline\">mean toilet [pw = hh_size]</code>. Write one sentence in "
                                   "a comment saying which is the share of households with a toilet and which is "
                                   "the share of people living in one."},
         ]},
        {"tab": "Regress and graph",
         "title": "regress, margins and graphs",
         "blocks": [
             {"t": "p", "html": "<code class=\"inline\">regress</code> fits a linear regression. The prefix "
                                "<code class=\"inline\">i.</code> tells Stata a variable is categorical, so it "
                                "makes the dummy variables for you and leaves out the lowest code as the base "
                                "(General, code 1, for <code class=\"inline\">caste_n</code>). "
                                "<code class=\"inline\">margins</code> then turns the coefficients into "
                                "predicted values you can explain to a programme manager."},
             {"t": "syntax", "label": "Stata do-file: 07_regress.do", "code":
                 "use households_clean, clear\n"
                 "regress monthly_pc_exp i.caste_n head_edu_years i.area_n\n"
                 "margins caste_n          // average predicted expenditure for each caste group\n"
                 "marginsplot              // graph of the margins with confidence intervals\n"
                 "\n"
                 "* with a 0/1 outcome the same command gives a linear probability model\n"
                 "regress toilet i.caste_n head_edu_years i.area_n"},
             {"t": "p", "html": "By default <code class=\"inline\">margins caste_n</code> sets every household "
                                "to General, predicts and averages, then does the same for OBC, SC and ST, "
                                "keeping each household's own education and area. The R cell below does "
                                "exactly that by hand, so your Stata coefficients and margins should match it to "
                                "the rupee."},
             {"t": "code", "lang": "r", "code": R["regress"]},
             {"t": "h3", "html": "Graphs"},
             {"t": "syntax", "label": "Stata do-file: graphs", "code":
                 "graph bar (mean) monthly_pc_exp, over(caste_n) ///\n"
                 "    ytitle(\"Mean monthly per capita expenditure (Rs)\")\n"
                 "graph export \"exp_by_caste.png\", replace width(1200)\n"
                 "\n"
                 "twoway (scatter monthly_pc_exp head_edu_years) ///\n"
                 "       (lfit monthly_pc_exp head_edu_years),   ///\n"
                 "       ytitle(\"Monthly per capita expenditure (Rs)\") xtitle(\"Years of schooling, head\")\n"
                 "graph export \"exp_by_edu.png\", replace width(1200)"},
             {"t": "p", "html": "The bar chart in R, for comparison with yours:"},
             {"t": "code", "lang": "r", "code": R["graph"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Add <code class=\"inline\">land_acres</code> to the "
                                   "Stata regression and run <code class=\"inline\">margins area_n</code>. In the R "
                                   "cell above, add <code class=\"inline\">+ land_acres</code> to the "
                                   "<code class=\"inline\">lm()</code> formula and check that the coefficients still "
                                   "match Stata's."},
         ]},
        {"tab": "Logs and reproducibility",
         "title": "Logs, a master do-file and reproducible work",
         "blocks": [
             {"t": "p", "html": "A log file records the commands you ran and everything in the Results window. "
                                "Keep one for every analysis you report, so you can show where a number came "
                                "from months later. <code class=\"inline\">log using name, text</code> writes "
                                "plain text that any editor can open."},
             {"t": "syntax", "label": "Stata do-file: 00_master.do", "code":
                 "* 00_master.do : runs the whole analysis from raw CSV to tables and graphs\n"
                 "version 19\n"
                 "clear all\n"
                 "set more off\n"
                 "cd \"C:\\impactmojo\\stata\"\n"
                 "\n"
                 "capture log close\n"
                 "log using \"analysis_log\", text replace\n"
                 "\n"
                 "do 03_newvars.do      // import, clean, label, save households_clean.dta\n"
                 "do 04_groups.do       // district summary\n"
                 "do 05_merge.do        // attach district information\n"
                 "do 07_regress.do      // regression, margins, graphs\n"
                 "\n"
                 "log close"},
             {"t": "ul", "items": [
                 "<code class=\"inline\">version 19</code> at the top makes later releases of Stata interpret "
                 "the do-file as Stata 19 did.",
                 "<code class=\"inline\">capture log close</code> closes a log left open by an earlier run "
                 "without stopping on an error if none is open.",
                 "Never edit the raw CSV. Every change goes in a do-file, so the path from raw data to result "
                 "can be re-run.",
                 "If you draw a random sample or bootstrap, put <code class=\"inline\">set seed 20261006</code> "
                 "(any fixed number) before it, so the same draw comes out every time.",
                 "Use <code class=\"inline\">assert</code> for things that must be true "
                 "(<code class=\"inline\">assert hh_size &gt;= 1</code>, <code class=\"inline\">isid hh_id</code>). "
                 "A do-file that stops loudly is better than one that finishes with wrong numbers.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> Build <code class=\"inline\">00_master.do</code> from "
                                   "the do-files you wrote in this course, run it, then open "
                                   "<code class=\"inline\">analysis_log.log</code> in a text editor and find the "
                                   "<code class=\"inline\">tabulate _merge</code> table in it."},
             {"t": "h3", "html": "Stata's own documentation"},
             {"t": "ul", "items": [
                 "<a href=\"https://www.stata.com/features/documentation/\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">Stata documentation</a>: every manual as a free PDF, "
                 "including <em>Getting Started</em> and the <em>User's Guide</em>.",
                 "<a href=\"https://www.stata.com/manuals/svysvyset.pdf\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">[SVY] svyset</a>, "
                 "<a href=\"https://www.stata.com/manuals/dmerge.pdf\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">[D] merge</a>, "
                 "<a href=\"https://www.stata.com/manuals/dreshape.pdf\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">[D] reshape</a> and "
                 "<a href=\"https://www.stata.com/manuals/rmargins.pdf\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">[R] margins</a>.",
                 "<a href=\"https://www.stata.com/new-in-stata/\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">New in Stata 19</a>.",
             ]},
         ]},
    ],
    "next": [
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "Run the same steps in free software, live in your browser."},
        {"href": "/code/spss.html", "title": "SPSS Syntax for Development Data",
         "desc": "The same arc in SPSS syntax, including Complex Samples for NFHS."},
        {"href": "/101-courses/survey-design.html", "title": "Survey Design 101",
         "desc": "Why surveys are stratified and clustered, and what that does to your standard errors."},
        {"href": "/101-courses/econometrics-101.html", "title": "Econometrics 101",
         "desc": "What a regression coefficient means, and when it does not mean what you hope."},
    ],
}

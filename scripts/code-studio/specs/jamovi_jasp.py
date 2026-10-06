# -*- coding: utf-8 -*-
"""jamovi and JASP: Free Point-and-Click Statistics. A guided course, with R cells that run the same analyses here.

Facts checked on 6 October 2026 against jamovi.org (FAQ, release notes, getting started), docs.jamovi.org (user
manual, analysis guides, jmv reference), jamovi's LICENSE.md on GitHub, and jasp-stats.org (download, getting
started, features, how to use JASP, the R syntax mode post). Sources are listed in the agent report.
"""

DL = '<a href="/code/data/households.csv" download style="color:var(--accent-color)">households.csv</a>'

R = {}
R["desc"] = ('hh <- read.csv("households.csv")\n'
             '# jamovi: Exploration > Descriptives, monthly_pc_exp in Variables, area in Split by\n'
             'stats <- function(x) round(c(N = length(x), Mean = mean(x), Median = median(x),\n'
             '                             SD = sd(x), Minimum = min(x), Maximum = max(x)), 1)\n'
             'sapply(split(hh$monthly_pc_exp, hh$area), stats)')
R["ttest"] = ('hh <- read.csv("households.csv")\n'
              '# jamovi: T-Tests > Independent Samples T-Test (Student\'s t is ticked by default)\n'
              't.test(monthly_pc_exp ~ area, data = hh, var.equal = TRUE)\n'
              '# tick Welch\'s in jamovi for the version that does not assume equal variances\n'
              't.test(monthly_pc_exp ~ area, data = hh)$p.value')
R["anova"] = ('hh <- read.csv("households.csv")\n'
              '# jamovi: ANOVA > One-Way ANOVA, monthly_pc_exp by caste\n'
              'oneway.test(monthly_pc_exp ~ caste, data = hh)                    # Welch\'s (unequal variances)\n'
              'oneway.test(monthly_pc_exp ~ caste, data = hh, var.equal = TRUE)  # Fisher\'s (equal variances)\n'
              'round(tapply(hh$monthly_pc_exp, hh$caste, mean), 1)')
R["chisq"] = ('hh <- read.csv("households.csv")\n'
              '# jamovi: Frequencies > Independent Samples (chi-square test of association)\n'
              'tab <- table(caste = hh$caste, toilet = hh$has_toilet)\n'
              'tab\n'
              'round(100 * prop.table(tab, 1), 1)   # row percentages\n'
              'chisq.test(tab, correct = FALSE)')
R["corr"] = ('hh <- read.csv("households.csv")\n'
             '# jamovi: Regression > Correlation Matrix\n'
             'round(cor(hh[, c("monthly_pc_exp", "head_edu_years", "hh_size", "land_acres")]), 3)\n'
             'cor.test(hh$head_edu_years, hh$monthly_pc_exp)')
R["lm"] = ('hh <- read.csv("households.csv")\n'
           '# jamovi: Regression > Linear Regression\n'
           '#   Dependent Variable: monthly_pc_exp\n'
           '#   Covariates: head_edu_years    Factors: caste, area\n'
           'fit <- lm(monthly_pc_exp ~ head_edu_years + caste + area, data = hh)\n'
           'round(summary(fit)$coefficients, 2)\n'
           'round(c(R = sqrt(summary(fit)$r.squared), R2 = summary(fit)$r.squared), 3)')

PAGE = {
    "slug": "jamovi-jasp",
    "order": 12,
    "kind": "guide",
    "tool": "jamovi and JASP",
    "title": "jamovi and JASP: Free Point-and-Click Statistics",
    "h1": "jamovi and JASP: free point-and-click statistics",
    "lede": ("Two free, open-source statistics programs with an SPSS-style layout, both built on R: install them, "
             "open a CSV, and run descriptives, t-tests, ANOVA, contingency tables, correlation and regression. "
             "Then see the R behind each click with jamovi's syntax mode and Rj, try JASP's Bayesian analyses, "
             "export your results, and learn when it is time to move to R."),
    "description": ("A free guided course in jamovi and JASP for development practitioners in South Asia: "
                    "installing, opening a CSV, descriptives, t-tests, ANOVA, contingency tables, correlation, "
                    "regression, jamovi syntax mode and Rj, JASP Bayesian analyses, exporting results and moving "
                    "to R."),
    "card": "Free, open-source alternatives to SPSS, built on R: from opening a CSV to regression and Bayes factors.",
    "datasets": ["households"],
    "engine_note": ("<strong>jamovi and JASP are desktop programs</strong> (jamovi also runs in a browser on its "
                    "own site). This page cannot run them, so it shows no jamovi or JASP output; each module "
                    "gives the menu path and tells you what to look for. Every analysis also has an R cell that "
                    "runs here on the same data, and since both programs run R underneath, your numbers should "
                    "match. The first R run downloads the R engine once (about 7&nbsp;MB)."),
    "modules": [
        {"tab": "What they are",
         "title": "Two free statistics programs built on R",
         "blocks": [
             {"t": "p", "html": "jamovi and JASP look like SPSS: a spreadsheet of data, menus of analyses, and "
                                "tables of results that update as you tick options. Both are free, both are open "
                                "source, and both run R underneath. For a district team, a small NGO or a "
                                "university department without an SPSS licence, they cover most of the "
                                "statistics a monitoring and evaluation report needs."},
             {"t": "h3", "html": "jamovi"},
             {"t": "ul", "items": [
                 "<strong>Cost and licence.</strong> jamovi's FAQ says it is \"free and open\", with \"nothing to "
                 "pay\", and free to use \"for any purpose, including commercial work\". Its "
                 "<a href=\"https://github.com/jamovi/jamovi/blob/main/LICENSE.md\" rel=\"noopener\" "
                 "target=\"_blank\" style=\"color:var(--accent-color)\">licence file</a> says the source code is "
                 "released under the AGPL3, with some components under the GPL2+.",
                 "<strong>Version.</strong> As of 6 October 2026 the "
                 "<a href=\"https://www.jamovi.org/releases.html\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">release notes</a> list <strong>jamovi 28.7</strong>, "
                 "released 3 October 2026, as the latest release. The older 2.7 series also received an update "
                 "(2.7.39) on 1 October 2026. jamovi ships small, frequent updates, so expect a higher number by "
                 "the time you read this.",
                 "<strong>Two ways to run it.</strong> jamovi Desktop for Windows, macOS and Linux, which works "
                 "offline and keeps your data on your computer; and jamovi Cloud in a web browser, which has a "
                 "free Guest plan and paid subscriptions. The FAQ says Cloud data are processed on jamovi's "
                 "servers during your session and removed afterwards.",
             ]},
             {"t": "h3", "html": "JASP"},
             {"t": "ul", "items": [
                 "<strong>Cost and licence.</strong> JASP's download page says it is \"Entirely for free, no "
                 "strings attached\" and released under a GNU Affero GPL v3 licence. It is an open-source "
                 "project supported by the University of Amsterdam.",
                 "<strong>Version.</strong> As of 6 October 2026 the "
                 "<a href=\"https://jasp-stats.org/download/\" rel=\"noopener\" target=\"_blank\" "
                 "style=\"color:var(--accent-color)\">download page</a> offers <strong>JASP 0.98.1</strong>, "
                 "released 7 July 2026.",
                 "<strong>What sets it apart.</strong> Most of its analyses come in a classical form and a "
                 "Bayesian form, side by side. Module 6 covers the Bayesian ones.",
             ]},
             {"t": "info", "html": "<strong>Which one?</strong> Start with jamovi if you want an SPSS replacement "
                                   "with the R code visible and a browser option for Chromebooks and lab "
                                   "computers. Start with JASP if you want Bayes factors beside your p-values. "
                                   "They read each other's common formats (CSV, SPSS .sav, Stata .dta), so you "
                                   "can use both."},
             {"t": "info", "html": "<strong>Exercise.</strong> Before you install anything, check how much memory "
                                   "your computer has. JASP's download page asks for at least 4&nbsp;GB of RAM, "
                                   "recommends 8&nbsp;GB, and needs about 4&nbsp;GB of free disk space."},
         ]},
        {"tab": "Install and open",
         "title": "Install, open a CSV and set variable types",
         "blocks": [
             {"t": "h3", "html": "Install"},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> download from <a href=\"https://www.jamovi.org/download.html\" "
                 "rel=\"noopener\" target=\"_blank\" style=\"color:var(--accent-color)\">jamovi.org/download</a>. "
                 "On Windows, run the installer; jamovi's installation guide says a <code class=\"inline\">.zip</code> "
                 "version exists for computers where IT policy blocks installers. On macOS, open the "
                 "<code class=\"inline\">.dmg</code> and drag jamovi to Applications. On Linux and Chromebooks it "
                 "comes from Flathub. To skip installing, use jamovi Cloud in a browser.",
                 "<strong>JASP:</strong> download from <a href=\"https://jasp-stats.org/download/\" "
                 "rel=\"noopener\" target=\"_blank\" style=\"color:var(--accent-color)\">jasp-stats.org/download</a>. "
                 "Windows users can choose the Microsoft Store (which updates itself) or an installer; macOS has "
                 "separate downloads for Apple Silicon and Intel; Linux and ChromeOS use Flatpak. No internet "
                 "connection is needed to run JASP once it is installed.",
             ]},
             {"t": "h3", "html": "Open the course file"},
             {"t": "p", "html": "Download " + DL + " (240 households, 13 columns). "
                                "<span class=\"illustrative-tag\">Illustrative data, invented for teaching</span> "
                                "The district names are real places; every number is made up."},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> click the file menu (&#9776;) at the top left, choose "
                 "<strong>Open</strong>, then <strong>This PC</strong>, and pick "
                 "<code class=\"inline\">households.csv</code>. The data appear as a spreadsheet on the left; "
                 "results will appear on the right.",
                 "<strong>JASP:</strong> click the main menu (the three blue stripes), choose "
                 "<strong>File</strong>, then <strong>Open</strong>, and browse to the file. JASP needs a header "
                 "row naming each column, which this file has.",
             ]},
             {"t": "h3", "html": "Check the variable types"},
             {"t": "p", "html": "Both programs guess a type for each column, and a wrong guess changes which "
                                "analyses accept it. JASP's getting-started page lists three types (Nominal, "
                                "Ordinal, Scale) and its rules: a numeric column with 3 to 10 distinct whole "
                                "numbers becomes Ordinal. In our file <code class=\"inline\">hh_size</code> runs "
                                "from 1 to 8, so check whether it arrived as Ordinal and set it to Scale if you "
                                "want its mean. In jamovi, double-click a column header (or press F3) to open the "
                                "variable editor and set the measure type."},
             {"t": "ul", "items": [
                 "<code class=\"inline\">district</code>, <code class=\"inline\">caste</code>, "
                 "<code class=\"inline\">area</code> and the Yes/No columns should be Nominal.",
                 "<code class=\"inline\">monthly_pc_exp</code>, <code class=\"inline\">land_acres</code> and "
                 "<code class=\"inline\">head_edu_years</code> should be continuous (Scale).",
                 "<code class=\"inline\">hh_id</code> is an identifier. Leave it out of analyses.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> In jamovi's variable editor, look at the levels of "
                                   "<code class=\"inline\">caste</code>. You should see General, OBC, SC and ST. "
                                   "Change the order so General is first; jamovi uses the first level as the "
                                   "reference group in regression."},
         ]},
        {"tab": "Descriptives",
         "title": "Descriptives, split by group",
         "blocks": [
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> <strong>Analyses &gt; Exploration &gt; Descriptives</strong>. Drag "
                 "<code class=\"inline\">monthly_pc_exp</code> into <strong>Variables</strong> and "
                 "<code class=\"inline\">area</code> into <strong>Split by</strong>. Open the "
                 "<strong>Statistics</strong> section for more statistics and <strong>Plots</strong> for box "
                 "plots and histograms.",
                 "<strong>JASP:</strong> choose <strong>Descriptives</strong> on the ribbon, move "
                 "<code class=\"inline\">monthly_pc_exp</code> into the variables box and "
                 "<code class=\"inline\">area</code> into the split box.",
             ]},
             {"t": "p", "html": "The table should give N, mean, median, standard deviation, minimum and maximum "
                                "for rural and urban households separately, with the two N values adding to 240. "
                                "The R cell computes the same numbers:"},
             {"t": "code", "lang": "r", "code": R["desc"]},
             {"t": "p", "html": "In both groups the mean is above the median, which is the usual sign of a few "
                                "large values pulling the mean up. A box plot from the Plots section will show "
                                "them as points above the whisker."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the split to <code class=\"inline\">caste</code> "
                                   "in jamovi or JASP. In the R cell, change <code class=\"inline\">hh$area</code> to "
                                   "<code class=\"inline\">hh$caste</code> and run again. Which group has the lowest "
                                   "median?"},
         ]},
        {"tab": "t-tests and ANOVA",
         "title": "Compare means: t-tests and one-way ANOVA",
         "blocks": [
             {"t": "h3", "html": "Independent samples t-test"},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> <strong>Analyses &gt; T-Tests &gt; Independent Samples T-Test</strong>. "
                 "Put <code class=\"inline\">monthly_pc_exp</code> in <strong>Dependent Variables</strong> and "
                 "<code class=\"inline\">area</code> in <strong>Grouping Variable</strong>. The grouping variable "
                 "must have exactly two levels.",
                 "<strong>JASP:</strong> <strong>T-Tests</strong> on the ribbon, then the classical "
                 "<strong>Independent Samples T-Test</strong>, with the same two variables.",
             ]},
             {"t": "p", "html": "Read the t statistic, its degrees of freedom and the p-value. Tick "
                                "<strong>Welch's</strong> as well: it does not assume the two groups have equal "
                                "variances, and urban and rural expenditure rarely do. The R cell runs both:"},
             {"t": "code", "lang": "r", "code": R["ttest"]},
             {"t": "p", "html": "On this file R gives t = &minus;9.84 on 238 degrees of freedom for Student's "
                                "test. jamovi should show the same size of t; its sign depends on which group "
                                "jamovi lists first."},
             {"t": "h3", "html": "One-way ANOVA"},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> <strong>Analyses &gt; ANOVA &gt; One-way ANOVA</strong>. Put "
                 "<code class=\"inline\">monthly_pc_exp</code> in <strong>Dependent Variable</strong> and "
                 "<code class=\"inline\">caste</code> in the grouping box, then choose equal or unequal "
                 "variances. Tick <strong>Equality of variances</strong> for Levene's test.",
                 "<strong>JASP:</strong> <strong>ANOVA</strong> on the ribbon, then the classical "
                 "<strong>ANOVA</strong>.",
             ]},
             {"t": "code", "lang": "r", "code": R["anova"]},
             {"t": "p", "html": "R gives Welch's F = 7.84 (3 and 89.2 degrees of freedom) and Fisher's "
                                "F = 4.63 (3 and 236). Check that jamovi's One-Way ANOVA table matches the "
                                "version you chose."},
             {"t": "p", "html": "The ANOVA asks whether mean expenditure differs across the four caste groups at "
                                "all. It does not say which groups differ; for that, ask for post-hoc tests in "
                                "the same dialog."},
             {"t": "info", "html": "<strong>Exercise.</strong> Run the t-test with "
                                   "<code class=\"inline\">has_toilet</code> as the grouping variable. In the R cell, "
                                   "change <code class=\"inline\">~ area</code> to "
                                   "<code class=\"inline\">~ has_toilet</code> in both lines and compare."},
         ]},
        {"tab": "Tables and regression",
         "title": "Contingency tables, correlation and regression",
         "blocks": [
             {"t": "h3", "html": "Contingency tables"},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> <strong>Analyses &gt; Frequencies &gt; Independent Samples "
                 "(&chi;&sup2; test of association)</strong>. Put <code class=\"inline\">caste</code> in "
                 "<strong>Rows</strong> and <code class=\"inline\">has_toilet</code> in <strong>Columns</strong>. "
                 "Under <strong>Cells</strong>, tick row percentages.",
                 "<strong>JASP:</strong> <strong>Frequencies &gt; Contingency Tables</strong>, with the same rows "
                 "and columns.",
             ]},
             {"t": "code", "lang": "r", "code": R["chisq"]},
             {"t": "h3", "html": "Correlation"},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> <strong>Analyses &gt; Regression &gt; Correlation Matrix</strong>. "
                 "Move <code class=\"inline\">monthly_pc_exp</code>, <code class=\"inline\">head_edu_years</code>, "
                 "<code class=\"inline\">hh_size</code> and <code class=\"inline\">land_acres</code> into the box. "
                 "jamovi shows each coefficient once, below the diagonal, with stars for significance.",
                 "<strong>JASP:</strong> <strong>Regression &gt; Correlation</strong>.",
             ]},
             {"t": "code", "lang": "r", "code": R["corr"]},
             {"t": "h3", "html": "Linear regression"},
             {"t": "steps", "items": [
                 "<strong>jamovi:</strong> <strong>Analyses &gt; Regression &gt; Linear Regression</strong>. "
                 "Put <code class=\"inline\">monthly_pc_exp</code> in <strong>Dependent Variable</strong>, "
                 "<code class=\"inline\">head_edu_years</code> in <strong>Covariates</strong> (continuous) and "
                 "<code class=\"inline\">caste</code> and <code class=\"inline\">area</code> in "
                 "<strong>Factors</strong> (categorical). jamovi makes the dummy variables for you.",
                 "<strong>JASP:</strong> <strong>Regression &gt; Linear Regression</strong>.",
             ]},
             {"t": "p", "html": "In the Model Coefficients table, each caste row is the difference from the "
                                "reference level (General, if you set it first in module 2) for households with "
                                "the same schooling and area. The R cell fits the same model; your estimates "
                                "should match its Estimate column, and R&sup2; should match too."},
             {"t": "code", "lang": "r", "code": R["lm"]},
             {"t": "info", "html": "<strong>Exercise.</strong> Add <code class=\"inline\">land_acres</code> as a second "
                                   "covariate. In the R cell, add <code class=\"inline\">+ land_acres</code> to the "
                                   "formula. Does the schooling coefficient move much once land is in the model?"},
         ]},
        {"tab": "The R underneath",
         "title": "jamovi syntax mode, Rj, and JASP's R button",
         "blocks": [
             {"t": "p", "html": "Both programs run R to produce their tables, and both will show you the R. "
                                "This is the bridge from clicking to coding."},
             {"t": "h3", "html": "jamovi syntax mode"},
             {"t": "steps", "items": [
                 "Click the application menu (&#8942;) at the top right of jamovi and tick <strong>Syntax "
                 "mode</strong>.",
                 "Every analysis now shows the R call that produces it, using the <code class=\"inline\">jmv</code> "
                 "R package. Right-click the syntax to copy it.",
                 "Untick it to leave syntax mode.",
             ]},
             {"t": "p", "html": "The calls look like the lines below, which follow the examples in jamovi's "
                                "<code class=\"inline\">jmv</code> reference. They are code to read, written for "
                                "our households file; the exact options jamovi writes depend on what you ticked."},
             {"t": "syntax", "label": "R (jmv package): what syntax mode writes, in outline", "code":
                 "jmv::descriptives(data = data, vars = vars(monthly_pc_exp), splitBy = \"area\")\n"
                 "jmv::ttestIS(formula = monthly_pc_exp ~ area, data = data)\n"
                 "jmv::anovaOneW(formula = monthly_pc_exp ~ caste, data = data)\n"
                 "jmv::contTables(data = data, rows = \"caste\", cols = \"has_toilet\", pcRow = TRUE)\n"
                 "jmv::corrMatrix(data = data, vars = vars(monthly_pc_exp, head_edu_years, hh_size))\n"
                 "jmv::linReg(data = data, dep = monthly_pc_exp, covs = vars(head_edu_years),\n"
                 "            factors = vars(caste, area),\n"
                 "            blocks = list(list(\"head_edu_years\", \"caste\", \"area\")))"},
             {"t": "p", "html": "The syntax does not include the step that reads the data. In R you would read "
                                "the CSV first, install <code class=\"inline\">jmv</code> with "
                                "<code class=\"inline\">install.packages(\"jmv\")</code>, and the same calls give "
                                "the same tables."},
             {"t": "h3", "html": "Rj: write R inside jamovi"},
             {"t": "steps", "items": [
                 "Click <strong>Modules</strong> at the top right, choose <strong>jamovi library</strong> and "
                 "install <strong>Rj</strong>.",
                 "Choose <strong>Rj Editor</strong> from the new R icon in the Analyses ribbon.",
                 "Your open dataset is available as a data frame called <code class=\"inline\">data</code>. Type "
                 "R code and run it with the green triangle, or Ctrl+Shift+Enter (&#8984;+Shift+Enter on a Mac). "
                 "The results appear in the results panel like any other analysis.",
             ]},
             {"t": "info", "tone": "warning", "html": "jamovi's FAQ notes that analyses written with Rj contain R "
                                                       "code, so when you open a file that has some, jamovi warns "
                                                       "you and will not run it until you allow it. Allow code only "
                                                       "from files you trust."},
             {"t": "h3", "html": "JASP's R button"},
             {"t": "p", "html": "From JASP 0.17, core analyses carry an <strong>R</strong> button. Click it after "
                                "setting your options and JASP shows the R function call behind the analysis, "
                                "with its settings. You can paste that code into another JASP to reproduce the "
                                "analysis, or send it to a colleague so they can see exactly which options you "
                                "used."},
             {"t": "info", "html": "<strong>Exercise.</strong> Switch on jamovi's syntax mode, run the independent "
                                   "samples t-test from module 4, and copy the syntax into a text file. Compare "
                                   "it with the <code class=\"inline\">jmv::ttestIS</code> line above: what did "
                                   "jamovi add?"},
         ]},
        {"tab": "Bayes in JASP",
         "title": "JASP's Bayesian analyses",
         "blocks": [
             {"t": "p", "html": "JASP's features page lists Bayesian versions of the t-tests, ANOVA (including "
                                "repeated measures and ANCOVA), correlation, linear and logistic regression, "
                                "binomial and multinomial tests, contingency tables and log-linear regression. "
                                "In each ribbon menu the Bayesian analyses sit beside the classical ones."},
             {"t": "h3", "html": "What a Bayes factor says"},
             {"t": "p", "html": "A p-value asks how surprising the data would be if there were no difference. A "
                                "Bayes factor compares two hypotheses directly: "
                                "<strong>BF<sub>10</sub></strong> is how many times better the data are "
                                "predicted by the alternative (a difference) than by the null (no difference). "
                                "BF<sub>10</sub> = 5 means the data are five times as likely under the "
                                "alternative; BF<sub>10</sub> = 0.2 means five times as likely under the null. "
                                "That second reading is something a p-value cannot give you: evidence "
                                "<em>for</em> no difference, which matters when a programme report needs to say "
                                "two districts did not differ."},
             {"t": "steps", "items": [
                 "In JASP, open <strong>T-Tests</strong> and choose the Bayesian "
                 "<strong>Independent Samples T-Test</strong>.",
                 "Put <code class=\"inline\">monthly_pc_exp</code> in the variable box and "
                 "<code class=\"inline\">area</code> as the grouping variable.",
                 "Read BF<sub>10</sub> in the results table, and note the prior shown in the options panel; "
                 "the Bayes factor depends on it.",
                 "Repeat with <code class=\"inline\">head_gender</code> as the grouping variable and compare the two "
                 "Bayes factors.",
             ]},
             {"t": "info", "html": "<strong>Report both.</strong> If you run classical and Bayesian "
                                   "tests on the same question, report both, and say which prior JASP used (it is "
                                   "shown in the options panel). Choosing whichever result looks better after the "
                                   "fact is the same problem as hunting for p-values."},
             {"t": "info", "html": "<strong>Exercise.</strong> Run the Bayesian contingency table for "
                                   "<code class=\"inline\">caste</code> by <code class=\"inline\">has_toilet</code>, "
                                   "and the classical one from module 5. Write two sentences for a programme "
                                   "manager: what each result says about caste and toilet access in this "
                                   "(invented) sample."},
         ]},
        {"tab": "Export and next steps",
         "title": "Save, export, and when to move to R",
         "blocks": [
             {"t": "h3", "html": "Save and share"},
             {"t": "ul", "items": [
                 "<strong>jamovi</strong> saves data, analyses and results together in one "
                 "<code class=\"inline\">.omv</code> file that a colleague can reopen. Right-click any table or "
                 "plot to copy it, APA-formatted, into Word or an email. Each analysis has an annotation space for "
                 "your interpretation, so the output can double as a draft write-up. jamovi's release notes record "
                 "export to Excel (.xlsx) in 2.7.12, LibreOffice (.ods) in 2.7.13, LaTeX in 2.7.14, and Word "
                 "(.docx) and .odt in 28.4.",
                 "<strong>JASP</strong> saves a <code class=\"inline\">.jasp</code> file holding the data, the "
                 "analyses and your notes. Its <a href=\"https://jasp-stats.org/how-to-use-jasp/\" "
                 "rel=\"noopener\" target=\"_blank\" style=\"color:var(--accent-color)\">How to use JASP</a> page "
                 "shows how to export results to HTML, copy tables straight into a word processor, and copy "
                 "tables as LaTeX.",
                 "<strong>Templates for routine data.</strong> jamovi can import a new data file into an existing "
                 "<code class=\"inline\">.omv</code> (from the &#9776; menu): the old rows are replaced, columns "
                 "are matched by name, and every filter, computed variable and analysis updates. For a monthly "
                 "monitoring dataset with the same columns each month, that turns your analysis into a reusable "
                 "template.",
             ]},
             {"t": "h3", "html": "When to move to R"},
             {"t": "p", "html": "jamovi and JASP are enough for a lot of evaluation work. Move to R (or Stata) "
                                "when you meet one of these:"},
             {"t": "ul", "items": [
                 "<strong>Joining files.</strong> jamovi's documentation says that \"at present, there is no way "
                 "to combine files horizontally\": you cannot merge a household file with a district file. R does "
                 "it in one line.",
                 "<strong>Survey designs.</strong> NFHS, PLFS and most large household surveys need weights, "
                 "strata and clusters for correct standard errors. R's <code class=\"inline\">survey</code> "
                 "package, Stata's <code class=\"inline\">svy</code> and SPSS Complex Samples handle that.",
                 "<strong>Repeating the same work across many files or rounds</strong>, where a script beats "
                 "clicking.",
                 "<strong>Analyses with no menu</strong>, such as difference-in-differences with fixed effects or "
                 "small-area estimation. Rj can run some of these inside jamovi, but at that point you are "
                 "writing R anyway.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> Save your jamovi analyses as "
                                   "<code class=\"inline\">households.omv</code>, close jamovi, reopen the file and "
                                   "check that every table is still there. Then copy one table into a Word or "
                                   "LibreOffice document."},
         ]},
    ],
    "next": [
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "The next step after jamovi: the same analyses as code, live in your browser."},
        {"href": "/code/spss.html", "title": "SPSS Syntax for Development Data",
         "desc": "If your organisation uses SPSS, the syntax behind its menus."},
        {"href": "/code/stata.html", "title": "Stata Syntax for Development Data",
         "desc": "Do-files, merges and svyset for NFHS-style surveys."},
        {"href": "/101-courses/stats-without-code.html", "title": "Statistics Without Code 101",
         "desc": "The ideas behind t-tests, ANOVA and regression, without software."},
        {"href": "/101-courses/bi-analysis.html", "title": "Bivariate Analysis 101",
         "desc": "Crosstabs, correlation and comparing means, explained."},
    ],
}

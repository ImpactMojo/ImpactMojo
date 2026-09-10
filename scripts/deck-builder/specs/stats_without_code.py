# -*- coding: utf-8 -*-
"""
Statistics Without Code 101 — ImpactMojo 101 Series (native deck spec)
Point-and-click statistics with jamovi and JASP: importing and cleaning data, descriptives,
comparing groups, correlation and regression, categorical outcomes, scales and factor analysis,
the modules for mediation, mixed models, meta-analysis and SEM, Bayesian analysis in JASP,
power, effect sizes, reporting, reproducibility, and when to move to R or Stata. For students,
NGO analysts and teachers in South Asia who need real statistics without writing code.
Build: python3 scripts/deck-builder/build.py stats_without_code
"""

DECK = {
    "slug": "stats-without-code",
    "title": "Statistics Without Code 101",
    "description": ("Statistics Without Code 101 — a free foundational course on jamovi and JASP, "
                    "the free point-and-click statistics tools built on R. Import and clean survey "
                    "data, describe it, compare groups, run regressions, analyse categorical "
                    "outcomes, check scales, use the modules for mediation, mixed models, "
                    "meta-analysis and SEM, try Bayesian analysis in JASP, report effect sizes "
                    "properly, keep the work reproducible, and know when a menu is not enough. "
                    "For students, NGO analysts and teachers in South Asia. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Statistics<br>Without<br>Code 101",
         "sub": "Real Analysis in jamovi and JASP &mdash; from a Survey CSV to a Reported Result, "
                "with Every Click Written Down",
         "tags": ["Data & Technology", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Point-and-Click, and Its Limits"},
             {"name": "Getting Data In and Clean"},
             {"name": "Describing Data"},
             {"name": "Comparing Groups"},
             {"name": "Correlation and Regression"},
             {"name": "Categorical Outcomes"},
             {"name": "Scales and Factor Analysis"},
             {"name": "The Modules: Beyond the Basics"},
             {"name": "Bayesian Analysis in JASP"},
             {"name": "Effect Sizes, Power and Reporting"},
             {"name": "Choosing Tools, Teaching and Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Point-and-Click, and Its Limits"},

        {"type": "content", "label": "The Tools", "title": "jamovi and JASP: free, open, built on R, and menu-driven",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "jamovi", "html":
                         "Free and open source, from a small team that came out of the JASP "
                         "project in 2017. A spreadsheet on the left, results on the right, "
                         "every analysis a form with tick-boxes, and every result an R "
                         "computation underneath. Saves data and analyses together in one "
                         "file. A library of add-on modules covers mediation, mixed models, "
                         "meta-analysis, SEM, item response theory, power and more. Runs on "
                         "Windows, Mac, Linux and in a browser (jamovi Cloud). jamovi.org."},
                        {"t": "panel", "color": "amber", "title": "JASP", "html":
                         "Free and open source, from the University of Amsterdam, led by "
                         "Eric-Jan Wagenmakers, since 2013. The same idea with a stronger "
                         "emphasis on Bayesian analysis alongside the classical tests, APA-"
                         "formatted tables by default, and modules for SEM, meta-analysis, "
                         "network analysis, machine learning and audit. jasp-stats.org."}],
              "right": [{"t": "body", "html": "Both replace SPSS for most of what a "
                        "social-science or NGO analyst does, at no cost, on any machine, "
                        "with output that is correct and formatted for a report. Both show "
                        "the R code behind an analysis if asked, which makes them the "
                        "gentlest route into R there is. Neither is a toy; the numbers are "
                        "R's numbers."},
                        {"t": "bullets", "color": "cyan", "sm": True, "items": [
                            "This course teaches jamovi as the main tool, because its data editor, filters and computed variables make it the better place to clean a survey, and JASP for the Bayesian section, where it leads.",
                            "Menu paths are given for jamovi 2.x; JASP's are close and named where they differ.",
                            "Every analysis is shown as: the click path, the boxes to tick, the output, and the sentence to write."]},
                        {"t": "hbox", "color": "green", "html": "Navarro and Foxcroft, "
                         "<em>Learning Statistics with jamovi</em> (2019), is free online and "
                         "is the textbook this course pairs with."}]},
         ]},

        {"type": "content", "label": "Who", "title": "Who this is for, and what it assumes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Reader", "Situation", "What this course gives"],
              "rows": [
                  ["Master's student in a social-science department", "SPSS licence expired or never existed; a thesis with a survey to analyse", "A complete free toolkit and the analyses a thesis needs, done correctly"],
                  ["NGO monitoring and evaluation officer", "A baseline in Excel, a funder who wants 'significance', no programmer on staff", "The right test for each question, the effect size to report, and the plot for the report"],
                  ["Teacher of research methods", "A classroom with mixed laptops and no budget", "A tool that installs in minutes and runs the same everywhere, plus a teaching sequence"],
                  ["Practitioner moving toward R", "Wants to understand the output before learning to write it", "Syntax mode shows the R behind every click"],
                  ["Field researcher", "Needs to check data quality in a district office with no internet", "Descriptives, filters and plots offline, in an afternoon"]]},
             {"t": "body", "cls": "sm", "html": "Assumed: the statistics in Data Analysis 101 "
              "and Bivariate Analysis 101 at the level of knowing what a mean, a p-value and "
              "a regression coefficient are. Not assumed: any code. Worked examples use two "
              "illustrative datasets, a self-help-group survey of 640 women and a learning "
              "assessment of 1,200 children in 40 schools, described in section 02."},
         ]},

        {"type": "content", "label": "Limits", "title": "What a menu cannot do, so you know before you start",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "red", "items": [
                  "<strong>Complex survey design.</strong> jamovi accepts a case-weight variable, but only integer frequency weights, and neither jamovi nor JASP handles strata and clusters, so standard errors from a menu ignore the design. For NFHS, PLFS, DHS or any weighted survey, R's <em>survey</em> package or Stata's <em>svy</em> is required.",
                  "<strong>Large or repeated pipelines.</strong> Cleaning 40 monthly files the same way is a script's job. A menu does it once.",
                  "<strong>Advanced econometrics.</strong> Instrumental variables, panel fixed effects with clustering, difference-in-differences with staggered adoption, time series: partly available through modules, mostly not.",
                  "<strong>Reproducibility across people.</strong> The saved file records the analyses, but a reviewer cannot re-run a menu sequence the way they re-run a script."]}],
              "right": [{"t": "body", "html": "The honest position: jamovi and JASP cover "
                        "the analyses in a typical master's thesis, an NGO evaluation report "
                        "and an undergraduate methods course, and cover them well. Where a "
                        "question needs survey weights or a scripted pipeline, the course says "
                        "so at that point and names the tool that does it. Knowing the edge "
                        "is part of using the tool competently."},
                        {"t": "hbox", "color": "amber", "html": "The commonest error this "
                         "course can prevent: an NFHS analysis run unweighted in a menu and "
                         "reported as national estimates. Section 02 returns to it."}]},
         ]},

        {"type": "content", "label": "The Interface", "title": "The jamovi window: data, analyses, results, and the three tabs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The left pane is the data: a spreadsheet where "
                        "each column has a name, a measurement type (nominal, ordinal, "
                        "continuous, ID) and a data type (integer, decimal, text), set by "
                        "double-clicking the header. The right pane is the results: every "
                        "analysis you run appends its tables and plots there, and clicking "
                        "one reopens its options. The tabs across the top are "
                        "<strong>Data</strong> (Setup, Compute, Transform, Filters, "
                        "Add/Delete rows and columns), <strong>Analyses</strong> (the menus), "
                        "and <strong>Edit</strong> (annotations)."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The measurement type controls what analyses will accept the variable. A 1/2 gender code set as continuous will be averaged; set it nominal and label it.",
                           "Results update live when the data or an option changes; there is no 'run' button.",
                           "The three-dots menu (top right) holds Syntax mode, the number format, and the plot theme.",
                           "Save as .omv: data, analyses, options and annotations in one file; anyone with jamovi reopens it exactly."]}],
              "right": [{"t": "panel", "color": "amber", "title": "JASP's equivalents", "html":
                         "A data view on the left (editable since version 0.18), analyses "
                         "grouped as Descriptives, T-Tests, ANOVA, Mixed Models, Regression, "
                         "Frequencies and Factor, each with a classical and a Bayesian "
                         "entry; results on the right, APA-formatted; a .jasp file that "
                         "stores everything. A '+' button adds modules. The logic is "
                         "identical; the menus are labelled slightly differently and this "
                         "course notes the difference where it matters."},
                        {"t": "hbox", "color": "green", "html": "Ten minutes of clicking "
                         "through the interface with the bundled Tooth Growth or Big Five "
                         "dataset is worth more than any slide here. Do it before section "
                         "02."}]},
         ]},

        {"type": "content", "label": "Syntax Mode", "title": "Syntax mode: the R behind the click, and the bridge to code",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The three-dots menu's Syntax mode shows, above "
                        "every result, the R command that produced it, using jamovi's own "
                        "<em>jmv</em> package: <code>jmv::ttestIS(data = df, vars = score, "
                        "group = treatment, effectSize = TRUE)</code>. Copy it into R with "
                        "<em>jmv</em> installed and it runs, producing the same tables. The "
                        "<em>Rj</em> module goes the other way: an editor inside jamovi where "
                        "you write R against the loaded data and see the output in the "
                        "results pane."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Use syntax mode to learn what the options do: tick a box, watch the argument appear.",
                           "Use it to document: paste the syntax into the methods appendix. It is the reproducible record of the analysis.",
                           "Use Rj for the one thing the menus lack: a weighted estimate with the <em>survey</em> package, a custom plot, a loop over districts.",
                           "JASP has no syntax mode as such, but its analyses map onto named R packages (<em>BayesFactor</em>, <em>lavaan</em>, <em>metafor</em>) that it documents."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The teaching use", "html":
                         "A student who has run twenty t-tests by menu and seen the syntax "
                         "each time has learned the grammar of an R function without "
                         "noticing. The step to writing <code>t.test(score ~ treatment, "
                         "data = df)</code> is small. That is the argument for jamovi over "
                         "SPSS in a methods course: the same menus, plus the door to code, "
                         "at no cost."},
                        {"t": "hbox", "color": "green", "html": "R for Development 101 in "
                         "this series picks up where syntax mode leaves off."}]},
         ]},

        {"type": "content", "label": "SPSS", "title": "Coming from SPSS: what maps, what differs, what you gain",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["SPSS", "jamovi", "Note"],
              "rows": [
                  ["Variable View: type, label, values, measure", "Double-click the column header: name, description, type, levels", "Levels are labelled in place; no separate value-labels dialog"],
                  ["Analyze &rarr; Descriptive Statistics &rarr; Frequencies / Descriptives / Explore", "Analyses &rarr; Exploration &rarr; Descriptives, with Split by", "One dialog covers all three"],
                  ["Compare Means &rarr; Independent-Samples T Test", "T-Tests &rarr; Independent Samples T-Test", "Effect size and assumption checks are tick-boxes"],
                  ["General Linear Model &rarr; Univariate", "ANOVA &rarr; ANOVA (or ANCOVA)", "Post hoc, estimated marginal means and plots in one form"],
                  ["Regression &rarr; Linear / Binary Logistic", "Regression &rarr; Linear Regression / Logistic Regression (2 Outcomes)", "Model builder with blocks; collinearity and residual plots as options"],
                  ["Crosstabs with chi-square", "Frequencies &rarr; Independent Samples (&chi;&sup2; test of association)", "Row, column and expected counts as tick-boxes"],
                  ["Scale &rarr; Reliability Analysis; Dimension Reduction &rarr; Factor", "Factor &rarr; Reliability Analysis; PCA; Exploratory Factor Analysis; CFA", "&omega; alongside &alpha;; parallel analysis built in; CFA in the core"],
                  ["Syntax window", "Syntax mode; Rj module", "R, not SPSS syntax"],
                  ["Split File, Select Cases", "Split by in each analysis; Data &rarr; Filters", "Filters are live and stack"],
                  [".sav files", "Open directly; also .csv, .xlsx, .dta, .rds", "Value labels are preserved on import"]]},
             {"t": "body", "cls": "sm", "html": "What you lose: nothing a thesis needs. What "
              "you gain: effect sizes and assumption checks in every dialog, omega, CFA and "
              "parallel analysis without add-ons, live results, and a file a co-author can "
              "open without a licence."},
         ]},

        {"type": "content", "label": "This Course", "title": "How the course is arranged",
         "blocks": [
             {"t": "flow", "steps": [
                 "DATA IN: import, types, labels, filters, computed variables, checks (02)",
                 "DESCRIBE: descriptives and plots that answer questions (03)",
                 "COMPARE: two groups, several groups, before and after (04)",
                 "RELATE: correlation and regression, with diagnostics (05)",
                 "CATEGORICAL: proportions, chi-square, logistic regression (06)",
                 "SCALES: reliability, EFA, CFA (07)",
                 "MODULES: mediation, mixed models, meta-analysis, SEM, IRT (08)",
                 "BAYES: the JASP way of answering the same questions (09)",
                 "REPORT: effect sizes, power, reproducibility (10)",
                 "PRACTICE: choosing tools, teaching, a full worked study (11)"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Each analysis slide follows one pattern: the "
                        "question in words; the menu path; the options to tick and why; the "
                        "output table with illustrative numbers; the assumptions and what to "
                        "do when they fail; and the sentence that goes in the report. The "
                        "same pattern makes the course usable as a reference: find the "
                        "question, follow the slide."}],
              "right": [{"t": "hbox", "color": "amber", "html": "The statistics are the "
                        "same as in every other course in this series. What is new is that "
                        "every one of them is reachable without a line of code, and the "
                        "course says exactly where."}]},
         ]},

        # ===================== SECTION 02: GETTING DATA IN AND CLEAN =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Getting Data In and Clean"},

        {"type": "content", "label": "Import", "title": "Importing: CSV, Excel, SPSS, Stata, and what to check on arrival",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Menu &rarr; Open &rarr; browse. jamovi reads "
                        ".csv, .txt, .xlsx, .sav (SPSS), .dta (Stata), .sas7bdat, .rds and "
                        ".RData, and its own .omv. Value labels from SPSS and Stata become "
                        "levels. CSVs arrive with every column typed by inspection: a column "
                        "of 1s and 2s is treated as continuous integer, a column with any "
                        "text as nominal text. The first job after import is to walk the "
                        "columns and set each one's type and levels deliberately."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "KoboToolbox and ODK exports: download as XLS or CSV with labels, not codes, or with both; jamovi will show the labels.",
                           "Excel files with merged headers, notes above the data, or totals rows must be cleaned in Excel first; jamovi wants one header row and one row per case.",
                           "Dates arrive as text; jamovi has no date type. Compute the pieces you need (year, month, days since baseline) in the source or with a computed variable.",
                           "Indian number formats with commas (1,23,456) are text on import; strip them in the source."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The arrival checklist", "html":
                         "Number of rows equals the number of interviews. Number of columns "
                         "equals the questionnaire's variables. Every ID is unique (Data "
                         "&rarr; Descriptives on the ID with Frequency tables shows "
                         "duplicates). Missing values are recognised as missing, not as "
                         "999 or blank strings (set the missing codes in the column setup). "
                         "Every categorical variable has the levels you expect and no "
                         "stray ones ('Female', 'female', 'F'). Ten minutes; it prevents "
                         "every later analysis being wrong."},
                        {"t": "hbox", "color": "green", "html": "Keep the raw file untouched "
                         "and save the jamovi work as a separate .omv. The raw file is the "
                         "audit trail."}]},
         ]},

        {"type": "content", "label": "Datasets", "title": "The two worked datasets used in this course",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["shg_survey.csv (n = 640 women, 32 villages)", "Type", "Levels or range"],
                        "rows": [
                            ["id", "ID", "1&ndash;640"],
                            ["village", "Nominal", "32 codes"],
                            ["treatment", "Nominal", "SHG member / non-member (village-randomised)"],
                            ["age", "Continuous", "18&ndash;60"],
                            ["educ", "Ordinal", "None / Primary / Secondary / Higher"],
                            ["hh_size", "Continuous", "1&ndash;14"],
                            ["income_own", "Nominal", "Yes / No"],
                            ["d1&ndash;d5", "Ordinal", "Decision-making items, 0 / 1 / 2"],
                            ["savings_rs", "Continuous", "Monthly savings, rupees, right-skewed"],
                            ["decide_score", "Continuous", "Sum of d1&ndash;d5, 0&ndash;10"],
                            ["lang", "Nominal", "Hindi / Bangla"]]}],
              "right": [{"t": "table",
                         "head": ["learning.csv (n = 1,200 children, 40 schools)", "Type", "Levels or range"],
                         "rows": [
                             ["child_id, school_id", "ID / Nominal", ""],
                             ["arm", "Nominal", "Remedial / Control (school-randomised)"],
                             ["grade", "Ordinal", "3 / 4 / 5"],
                             ["sex", "Nominal", "Girl / Boy"],
                             ["baseline", "Continuous", "Reading score, 0&ndash;100"],
                             ["endline", "Continuous", "Reading score, 0&ndash;100"],
                             ["attend_pct", "Continuous", "Attendance, 0&ndash;100"],
                             ["reads_para", "Nominal", "Can read a paragraph at endline: Yes / No"]]},
                        {"t": "hbox", "color": "cyan", "html": "Both are illustrative and "
                         "constructed for teaching. Every number in the output tables that "
                         "follow is illustrative too, with magnitudes chosen to be "
                         "realistic."}]},
         ]},

        {"type": "content", "label": "Types and Levels", "title": "Setting measurement types and labelling levels",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Double-click a column header, or Data &rarr; "
                        "Setup. Set the measure type: <strong>Nominal</strong> for categories "
                        "with no order (village, sex), <strong>Ordinal</strong> for ordered "
                        "categories (education, Likert items), <strong>Continuous</strong> for "
                        "numbers with meaningful intervals (age, score, rupees), "
                        "<strong>ID</strong> for identifiers that should never be analysed. "
                        "For nominal and ordinal variables, the Levels box lists the values "
                        "found; type a label beside each code (1 = Female, 2 = Male) and "
                        "drag to reorder ordinal levels."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Likert items: ordinal for descriptives and frequencies; many analyses (means, t-tests, factor analysis) will treat them as continuous when asked, and the course says when that is defensible.",
                           "A binary 0/1 variable can be continuous (its mean is a proportion) or nominal (for chi-square); set it as the analysis needs, or keep two copies.",
                           "Add a description to every variable. It appears in output and saves the codebook lookup."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why this step decides everything", "html":
                         "A t-test dialog will not accept a nominal variable as the outcome; "
                         "a chi-square will not accept a continuous one as a factor; a "
                         "regression will dummy-code a nominal predictor and treat an ordinal "
                         "one as ordered polynomial contrasts unless told otherwise. The "
                         "types are not decoration; they are the analysis's first "
                         "assumption, and they are set here."},
                        {"t": "hbox", "color": "green", "html": "For education (None, Primary, "
                         "Secondary, Higher): ordinal, levels in that order, so every table "
                         "and plot reads left to right."}]},
         ]},

        {"type": "content", "label": "Computed Variables", "title": "Computed and transformed variables: scores, recodes, logs",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Need", "Data &rarr; Compute (new variable) formula", "Note"],
                        "rows": [
                            ["Scale score", "<code>d1 + d2 + d3 + d4 + d5</code> or <code>MEAN(d1, d2, d3, d4, d5)</code>", "MEAN handles missing items; set a minimum with <code>MEAN(..., ignore_missing = 1)</code> and check the count"],
                            ["Log of a skewed variable", "<code>LN(savings_rs + 1)</code>", "The +1 for zeros; say so"],
                            ["Change score", "<code>endline - baseline</code>", "Section 04 discusses when a change score is the wrong analysis"],
                            ["Standardised score", "<code>Z(baseline)</code>", "Mean 0, SD 1 across the sample"],
                            ["Per-capita", "<code>savings_rs / hh_size</code>", "Division by zero if hh_size can be 0; filter first"],
                            ["Condition", "<code>IF(attend_pct >= 75, \"Regular\", \"Irregular\")</code>", "Text result becomes nominal"],
                            ["Age band", "<code>IF(age < 25, \"18-24\", IF(age < 40, \"25-39\", \"40+\"))</code>", "Nested IF; or use Transform for many bands"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "<strong>Transform</strong> (Data "
                        "&rarr; Transform) recodes an existing variable through a saved "
                        "transformation that can be applied to many columns at once: reverse "
                        "a 1&ndash;5 item (<code>6 - $source</code>), collapse categories, "
                        "convert codes to labels. Both computed and transformed variables "
                        "update live if the source data change, and both show their "
                        "formula in the column header, which is the documentation."},
                        {"t": "hbox", "color": "amber", "html": "Every computed variable is a "
                         "decision (which items, how missing was handled, why the log). "
                         "Write the formula into the methods; jamovi shows it, so copy it."}]},
         ]},

        {"type": "content", "label": "Filters", "title": "Filters: analysing a subset without deleting anything",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Data &rarr; Filters adds a filter row: a "
                        "formula that is true for the cases to keep. <code>age &gt;= 18</code>; "
                        "<code>treatment == \"SHG member\"</code>; <code>NOT(village == 17)</code>; "
                        "<code>attend_pct &gt; 0 and baseline != NA</code>. Filtered-out rows "
                        "are greyed, kept in the file, and excluded from every analysis "
                        "while the filter is active. Filters stack; each can be switched "
                        "off; the active set is shown in every result's footnote."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The right way to exclude implausible values (a savings figure of 9,999,999), pilot cases, or a district with a known data problem: filter, note it, keep the rows.",
                           "The wrong way: deleting rows. The raw n and the analysed n must both be reportable.",
                           "Split by (in most analysis dialogs) runs the same analysis per group without filtering; use it for descriptives by arm, filters for exclusions.",
                           "Report every filter in the methods, with the n before and after."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Data quality checks by filter", "html":
                         "A filter is also a query. <code>endline &lt; baseline - 30</code> "
                         "shows children whose score fell by more than 30 points: possible "
                         "ID mismatches. <code>savings_rs &gt; 20000</code> shows outliers "
                         "to verify against the paper form. <code>d1 == NA or d2 == NA</code> "
                         "shows partial refusals of the decision module, which section 05 "
                         "of SEM 101 says are not random. Each is thirty seconds and each "
                         "belongs in the data-quality log."},
                        {"t": "hbox", "color": "green", "html": "Survey Design 101's "
                         "high-frequency checks can all be run in jamovi with filters and "
                         "descriptives, in the field, on the day."}]},
         ]},

        {"type": "content", "label": "Missing Data", "title": "Missing values: recognising them, counting them, handling them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Blank cells and the codes you declare as "
                        "missing (Setup &rarr; Missing values: 999, -99, 'Refused') are "
                        "treated as missing. Descriptives reports N and Missing per variable; "
                        "a frequency table shows missing as a row if asked. Most analyses "
                        "drop cases listwise: a regression with six predictors loses every "
                        "case missing any one of them, and the results footnote gives the "
                        "n used."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Report the missingness per variable in the descriptives table. It is the first thing a careful reader looks for.",
                           "For a scale score, MEAN() with a minimum-items rule is a defensible partial-response treatment; state the rule.",
                           "Multiple imputation is not in the jamovi core. The <em>Rj</em> module with the <em>mice</em> package does it; or move to R for that analysis.",
                           "Do not replace missing with the mean. It is one click in some tools and it is wrong."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Whether it matters", "html":
                         "Descriptives &rarr; split by a 'missing on the outcome' indicator "
                         "(a computed variable: <code>IF(endline == NA, 1, 0)</code>) shows "
                         "whether the children with no endline score differ at baseline from "
                         "those with one. If they were weaker, attrition biases the "
                         "endline mean upward and the report must say so. This is the "
                         "one missing-data analysis every evaluation needs and it takes "
                         "two clicks."},
                        {"t": "hbox", "color": "green", "html": "Attrition by arm is reported "
                         "in every trial. A crosstab of arm by missing-endline, section 06, "
                         "is the table."}]},
         ]},

        {"type": "content", "label": "Weights", "title": "The survey-weights problem, stated plainly",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "NFHS, PLFS, DHS, NSS and most large surveys "
                        "sample some households with higher probability than others and "
                        "supply a weight per case to correct for it, and they sample in "
                        "clusters within strata, which changes every standard error. jamovi "
                        "can weight cases, but only by an integer frequency weight, and it "
                        "has nowhere to enter strata or clusters; fractional design weights "
                        "must be rounded, which the survey's documentation forbids. An NFHS "
                        "analysis run in the menus is an analysis of the sample, not of the "
                        "population, and its confidence intervals are too narrow. JASP has "
                        "no design support either."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "For your own survey with equal-probability sampling and a simple design, the menus are correct and clustering can be acknowledged as a limitation or handled in R.",
                           "For a weighted national survey, use jamovi for exploration and data checks only. Estimate in R (<em>survey</em>, via the Rj module or RStudio) or Stata (<em>svy</em>).",
                           "InsightStack's data starters for DHS and PLFS load the files with the weights and design already set, in R, Stata and Python.",
                           "Say in the report which estimates are weighted and which are not. Never present an unweighted menu estimate as a population figure."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What Rj makes possible", "html":
                         "Install the Rj module (Modules &rarr; jamovi library). In its "
                         "editor: <code>library(survey); des &lt;- svydesign(ids = ~psu, "
                         "strata = ~stratum, weights = ~wt, data = data); "
                         "svymean(~stunted, des)</code>. Four lines, inside jamovi, on "
                         "the loaded data, with correct standard errors. It is code, but "
                         "it is four lines, and Survey Design 101 and the FieldStack notes "
                         "give the design variables for each survey."},
                        {"t": "hbox", "color": "red", "html": "This is the one limit in the "
                         "course that produces wrong published numbers when ignored. The "
                         "rest produce inconvenience."}]},
         ]},

        {"type": "content", "label": "Data Checklist", "title": "Before any analysis: the data checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Check", "How in jamovi", "Done"],
              "rows": [
                  ["Row count matches the interview count", "Bottom of the data pane; Descriptives N on the ID", ""],
                  ["IDs unique", "Descriptives &rarr; Frequency tables on ID; any count above 1", ""],
                  ["Every variable typed and labelled", "Walk the headers; Setup", ""],
                  ["Missing codes declared", "Setup &rarr; Missing values", ""],
                  ["Missingness per variable known", "Descriptives &rarr; N, Missing", ""],
                  ["Ranges plausible", "Descriptives &rarr; Min, Max; box plots", ""],
                  ["Categorical levels clean", "Frequency tables; fix in source or Transform", ""],
                  ["Outliers verified or filtered with a note", "Filters; box plots", ""],
                  ["Scale scores computed with a stated missing rule", "Compute with MEAN()", ""],
                  ["Weights and design understood", "If weighted: not in the menus", ""],
                  ["Raw file preserved; work saved as .omv", "Save As", ""]]},
             {"t": "body", "cls": "sm", "html": "Eleven rows, forty minutes for a survey of "
              "this size. Every one of them has, in some published report, been skipped "
              "and produced a number that was wrong."},
         ]},

        # ===================== SECTION 03: DESCRIBING DATA =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Describing Data"},

        {"type": "content", "label": "Descriptives", "title": "Exploration &rarr; Descriptives: the one dialog to learn first",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Drag variables into the box, optionally a "
                        "grouping variable into Split by, and tick what you want: N, "
                        "missing, mean, median, mode, sum, SD, variance, range, minimum, "
                        "maximum, standard error, confidence interval of the mean, IQR, "
                        "skewness, kurtosis, Shapiro-Wilk, percentiles. Tick Frequency "
                        "tables for nominal and ordinal variables. Under Plots: histogram, "
                        "density, box plot, violin, dot plot, bar plot, Q-Q plot. Everything "
                        "updates as you tick. Transpose the table if there are many "
                        "variables and few statistics."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "For a report's Table 1: N, mean, SD, median, IQR for continuous; frequency tables for categorical; split by arm.",
                           "For a data check: min, max, missing, and a box plot per variable.",
                           "For a distribution decision: histogram with density, skewness, and the Q-Q plot, before choosing a test in section 04."]}],
              "right": [{"t": "panel", "color": "amber", "title": "JASP", "html":
                         "Descriptives &rarr; Descriptive Statistics, the same options plus "
                         "a correlation heat-map, a Pareto plot, and Likert plots for "
                         "ordinal items. JASP's table is APA-formatted by default and can "
                         "be copied as LaTeX or HTML."},
                        {"t": "hbox", "color": "green", "html": "Mean and SD describe a "
                         "symmetric variable; median and IQR describe a skewed one. "
                         "Savings in rupees is skewed: report the median, and the mean only "
                         "alongside it."}]},
         ]},

        {"type": "content", "label": "Table 1", "title": "A worked Table 1: the SHG survey by arm",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["", "SHG member (n = 322)", "Non-member (n = 318)", "Missing"],
                        "rows": [
                            ["Age, mean (SD)", "34.1 (8.2)", "34.6 (8.5)", "0"],
                            ["Education, n (%): None / Primary / Secondary / Higher", "118 (37) / 96 (30) / 84 (26) / 24 (7)", "124 (39) / 92 (29) / 80 (25) / 22 (7)", "0"],
                            ["Household size, median (IQR)", "5 (4&ndash;7)", "5 (4&ndash;7)", "0"],
                            ["Own income, n (%) yes", "141 (44)", "112 (35)", "3"],
                            ["Monthly savings (Rs), median (IQR)", "300 (100&ndash;600)", "150 (0&ndash;400)", "11"],
                            ["Decision-making score (0&ndash;10), mean (SD)", "5.8 (2.1)", "4.9 (2.2)", "8"],
                            ["Language, n (%) Bangla", "162 (50)", "158 (50)", "0"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. Built from one "
                        "Descriptives run split by treatment, with frequency tables ticked, "
                        "and the percentages computed from the counts. The Missing column "
                        "is there because a reader asks."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What it shows", "html":
                         "The arms are balanced on the pre-treatment characteristics (age, "
                         "education, household size, language), as randomisation should "
                         "make them; the outcomes (own income, savings, decision-making) "
                         "differ in the direction the programme intends. Whether the "
                         "difference is more than chance is section 04's question; "
                         "whether it is large enough to matter is section 10's."},
                        {"t": "hbox", "color": "amber", "html": "Do not put p-values on a "
                         "balance table for a randomised design. Differences are chance by "
                         "construction, and one in twenty will be 'significant'."}]},
         ]},

        {"type": "content", "label": "Plots", "title": "Plots that answer questions: which one, when",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Question", "Plot", "Where in jamovi", "Note"],
              "rows": [
                  ["What does this variable look like?", "Histogram with density", "Descriptives &rarr; Plots", "Skew, bimodality, floor and ceiling effects"],
                  ["Are there outliers, and do groups differ?", "Box plot, or violin with box, split by group", "Descriptives &rarr; Plots &rarr; Box plot; Split by", "Tick Data points to see every case"],
                  ["Is it roughly normal?", "Q-Q plot", "Descriptives &rarr; Plots", "Points on the line: yes; a curve: skew"],
                  ["How are categories distributed?", "Bar plot", "Descriptives &rarr; Plots &rarr; Bar plot", "For nominal and ordinal variables"],
                  ["Do two continuous variables relate?", "Scatter plot with fit line", "Regression &rarr; Correlation Matrix &rarr; Plot; or the <em>scatr</em> module", "Add group colour with Split by"],
                  ["Group means with uncertainty", "Descriptives plot: mean with CI", "T-Tests and ANOVA &rarr; Descriptives plots", "The plot for a results section"],
                  ["Before and after, per person", "Paired plot", "<em>Flexplot</em> or <em>esci</em> module", "Shows individual change, not only means"],
                  ["Interaction", "Estimated marginal means plot", "ANOVA &rarr; Estimated Marginal Means &rarr; Plots", "Lines that cross or diverge"]]},
             {"t": "body", "cls": "sm", "html": "Every plot exports as PNG, PDF, SVG or EPS "
              "from its right-click menu, at the resolution a journal needs. The plot "
              "theme (three-dots menu) sets a consistent look; the default is fine and "
              "the greyscale option prints well."},
         ]},

        {"type": "content", "label": "Distributions", "title": "Reading a distribution before choosing a test",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Monthly savings in the SHG survey: histogram "
                        "piled at zero and to the left, a long right tail to Rs 5,000, "
                        "skewness 2.4, Shapiro-Wilk p &lt; .001, Q-Q plot curving away above "
                        "the line. Reading score at endline: a symmetric hump with a small "
                        "floor at zero, skewness 0.1, Shapiro-Wilk p = .08. The first calls "
                        "for a median, a log transform or a non-parametric test; the second "
                        "is fine for means and t-tests."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Shapiro-Wilk rejects normality for almost any large sample; read it with the plot, not instead of it. With n = 640 a p of .001 can accompany a distribution that is fine for a t-test.",
                           "What matters for t-tests and ANOVA is the sampling distribution of the mean, which is close to normal for n above about 30 per group unless the skew is extreme.",
                           "Extreme skew, many zeros, or a bounded 0&ndash;100 score with a floor: consider the median, a transform, a non-parametric test, or a model built for the shape (section 06 and the modules)."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Likert items and scale scores", "html":
                         "A single five-point item is ordinal, and its histogram is five "
                         "bars. A score summing five such items is close enough to "
                         "continuous for means and t-tests in most applied work, and "
                         "Norman (<em>Advances in Health Sciences Education</em> 2010, "
                         "15:625) reviews the evidence that parametric tests are robust "
                         "here. Report the item-level frequencies as well, because a mean "
                         "of 3.2 hides whether the sample is split or clustered in the "
                         "middle."},
                        {"t": "hbox", "color": "green", "html": "Look at every outcome "
                         "variable's histogram once, split by group. It is the cheapest "
                         "insurance in statistics."}]},
         ]},

        {"type": "content", "label": "Ordinal Items", "title": "Describing Likert and ordinal items: frequencies, not only means",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A three-point decision-making item (no say, "
                        "joint, alone) or a five-point agreement item is described by its "
                        "frequency table: the share at each level, split by group. "
                        "Descriptives with Frequency tables ticked gives it; a bar plot "
                        "draws it; JASP's Likert plot (Descriptives &rarr; Plots) stacks the "
                        "levels horizontally for several items at once, which is the "
                        "standard figure for a battery. The mean of the codes (1.32) is a "
                        "summary a reader cannot picture; '41% decide alone, 39% jointly, "
                        "20% have no say' is one they can."},
                       {"t": "table",
                        "head": ["d1: who decides on food purchases", "SHG member", "Non-member"],
                        "rows": [
                            ["No say", "12%", "24%"],
                            ["Jointly", "38%", "44%"],
                            ["Alone", "50%", "32%"],
                            ["n", "320", "316"]]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Illustrative. The shift is from 'no say' and 'jointly' toward 'alone'; the mean of the codes rises from 1.08 to 1.38 and hides the shape.",
                  "For a battery of items, one stacked bar per item, ordered by the share at the top level, is the report figure; the <em>surveymv</em> module and JASP's Likert plot draw it.",
                  "Test the shift with the ordinal logistic model (section 06) or, descriptively, the chi-square on the 3&times;2 table.",
                  "Sum the items into a scale only after section 07 has shown they belong together."]},
                        {"t": "hbox", "color": "amber", "html": "Means of Likert items are "
                         "defensible for a scale score and misleading for a single item. "
                         "Show the distribution."}]},
         ]},

        {"type": "content", "label": "Crosstabs", "title": "Two categorical variables: the contingency table",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Frequencies &rarr; Contingency Tables &rarr; "
                        "Independent Samples. Rows: education; columns: own income. Under "
                        "Cells tick Row percentages (or Column, depending on which variable "
                        "is the 'given'). The table shows counts and percentages; the "
                        "&chi;&sup2; test of association appears above it, with a p-value, "
                        "and section 06 covers reading it. As a descriptive tool this is "
                        "how every 'by' table in a report is made."},
                       {"t": "table",
                        "head": ["Education", "Own income: Yes", "No", "Total"],
                        "rows": [
                            ["None", "62 (26%)", "180 (74%)", "242"],
                            ["Primary", "68 (36%)", "120 (64%)", "188"],
                            ["Secondary", "84 (51%)", "80 (49%)", "164"],
                            ["Higher", "28 (61%)", "18 (39%)", "46"],
                            ["Total", "242 (38%)", "398 (62%)", "640"]]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Row percentages when the row variable is the explanatory one (education) and you want to compare across its levels.",
                  "Layers (a third variable) split the table: education by income within each arm.",
                  "Small cells (below 5 expected) make the &chi;&sup2; unreliable; jamovi offers Fisher's exact test as a tick-box.",
                  "Export the table to Word via copy; it keeps its structure."]},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. The gradient "
                         "is the story: own income rises with education from a quarter to "
                         "three-fifths. The p-value on the &chi;&sup2; (section 06) says "
                         "the gradient is not chance; the percentages say what it is."}]},
         ]},

        {"type": "content", "label": "Describing Change", "title": "Describing before and after: the paired view",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Baseline and endline reading scores for the "
                        "same children. Descriptives on both gives two means; a computed "
                        "change score (endline minus baseline) gives the mean change and "
                        "its distribution, which is what the paired t-test in section 04 "
                        "tests. But the mean change hides who changed: a paired plot (the "
                        "<em>esci</em> module's paired-samples estimation, or Flexplot) "
                        "draws a line per child from baseline to endline, split by arm, and "
                        "shows whether the gain was general or concentrated among those "
                        "who started low."},
                       {"t": "stats", "cols": 3, "cards": [
                           {"num": "41.2", "label": "mean baseline reading score, both arms", "color": "cyan", "source": "Illustrative"},
                           {"num": "+9.8", "label": "mean change in the remedial arm (SD of change 12.4)", "color": "green", "source": "Illustrative"},
                           {"num": "+3.1", "label": "mean change in the control arm (SD 11.9)", "color": "amber", "source": "Illustrative"}]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Report the baseline mean, the endline mean and the change with its SD, per arm. Three numbers per arm; the fourth (the difference in changes) is the effect and section 04 tests it.",
                  "A change score is the right description. It is not always the right analysis: regressing endline on baseline and arm (section 05) is usually more precise, and the course says why there.",
                  "Ceiling: a child at 95 cannot gain 20. Check the baseline distribution for children near the top before interpreting small gains among them.",
                  "Regression to the mean: children selected for remedial classes because they scored low will score higher next time whatever happens. The control arm is the only protection."]}]},
         ]},

        # ===================== SECTION 04: COMPARING GROUPS =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Comparing Groups"},

        {"type": "content", "label": "Which Test", "title": "Choosing the comparison: a decision table",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Question", "Outcome", "Groups", "Test (jamovi menu)", "Non-parametric alternative"],
              "rows": [
                  ["Do two independent groups differ?", "Continuous", "2, different people", "T-Tests &rarr; Independent Samples T-Test (Student or Welch)", "Mann-Whitney U (same dialog)"],
                  ["Did the same people change?", "Continuous", "2, same people", "T-Tests &rarr; Paired Samples T-Test", "Wilcoxon signed-rank (same dialog)"],
                  ["Does a mean differ from a known value?", "Continuous", "1", "T-Tests &rarr; One Sample T-Test", "Wilcoxon (same dialog)"],
                  ["Do three or more groups differ?", "Continuous", "3+, different people", "ANOVA &rarr; One-Way ANOVA (Welch or Fisher), or ANOVA for factorial designs", "ANOVA &rarr; Non-parametric &rarr; Kruskal-Wallis"],
                  ["Do groups differ after adjusting for a covariate?", "Continuous", "2+", "ANOVA &rarr; ANCOVA", "&mdash;"],
                  ["Repeated measures over time?", "Continuous", "3+ occasions, same people", "ANOVA &rarr; Repeated Measures ANOVA", "Non-parametric &rarr; Friedman"],
                  ["Two factors at once (arm &times; sex)?", "Continuous", "Crossed", "ANOVA &rarr; ANOVA with two factors", "&mdash;"],
                  ["Do groups differ on a proportion?", "Binary", "2+", "Section 06: contingency tables, logistic regression", "Fisher's exact"]]},
             {"t": "body", "cls": "sm", "html": "The rows are the questions an evaluation "
              "asks. Note that 'do the arms differ at endline after accounting for baseline' "
              "is ANCOVA (or its regression twin in section 05), and it is usually the "
              "right analysis for a before-after-control design, ahead of the paired t-test "
              "on change scores."},
         ]},

        {"type": "content", "label": "Independent t", "title": "Two groups: the independent-samples t-test, done properly",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Question</strong>: do SHG "
                        "members and non-members differ in decision-making score? "
                        "<strong>Path</strong>: T-Tests &rarr; Independent Samples T-Test; "
                        "decide_score into Dependent Variables, treatment into Grouping "
                        "Variable. <strong>Tick</strong>: Welch's (not Student's, because it "
                        "does not assume equal variances and costs nothing); Mean difference "
                        "with Confidence interval; Effect size (Cohen's d); Descriptives; "
                        "Descriptives plot; Assumption checks: Normality (Shapiro-Wilk), "
                        "Q-Q plot, Homogeneity (Levene's)."},
                       {"t": "table",
                        "head": ["", "Statistic", "df", "p", "Mean difference", "95% CI", "Cohen's d"],
                        "rows": [
                            ["Welch's t", "5.21", "631", "&lt; .001", "0.90", "0.56 to 1.24", "0.42"]]},
                       {"t": "table",
                        "head": ["Group", "N", "Mean", "SD", "SE"],
                        "rows": [
                            ["SHG member", "318", "5.80", "2.10", "0.118"],
                            ["Non-member", "314", "4.90", "2.20", "0.124"]]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'SHG members scored higher on decision-making than non-members "
                         "(5.8 vs 4.9 on a 0&ndash;10 scale; mean difference 0.90, 95% CI "
                         "0.56 to 1.24; Welch's t(631) = 5.21, p &lt; .001; d = 0.42).' The "
                         "difference and its interval carry the finding; the p-value "
                         "confirms it is not chance; d says it is a moderate effect."},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. Note the "
                         "clustering: women in the same village are not independent, and "
                         "the CI is somewhat too narrow. Section 08's mixed models fix it; "
                         "for a report, say it in the limitations."}]},
         ]},

        {"type": "content", "label": "Assumptions", "title": "Assumption checks in the dialog, and what to do when they fail",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Check", "Where", "Reads as", "If it fails"],
              "rows": [
                  ["Normality (Shapiro-Wilk, Q-Q)", "T-Tests and ANOVA &rarr; Assumption Checks", "p &lt; .05 rejects normality; the Q-Q plot shows how", "With n above ~30 per group and moderate skew, proceed; with severe skew or small n, Mann-Whitney or a transform"],
                  ["Equal variances (Levene's)", "Same", "p &lt; .05: variances differ", "Use Welch's t or Welch's ANOVA (both are tick-boxes; use them by default anyway)"],
                  ["Independence", "Not a check; a design fact", "Clustered by village, school, enumerator?", "Mixed model (section 08) or cluster-robust SEs in R; at least say so"],
                  ["Outliers", "Box plot", "Points beyond the whiskers", "Verify the data; report with and without; do not delete silently"],
                  ["Sphericity (repeated measures)", "RM ANOVA &rarr; Assumption Checks (Mauchly)", "p &lt; .05: sphericity violated", "Tick Greenhouse-Geisser correction"],
                  ["Homogeneity of regression slopes (ANCOVA)", "Add the interaction term and test it", "Interaction significant: slopes differ", "Report the interaction; ANCOVA's adjusted means are then misleading"]]},
             {"t": "body", "cls": "sm", "html": "Every check is one tick-box away, which is "
              "why there is no excuse for a report that does not mention them. The "
              "sentence: 'Variances were unequal (Levene's p = .02), so Welch's test was "
              "used; distributions were approximately normal by Q-Q plot.'"},
         ]},

        {"type": "content", "label": "Paired t", "title": "Before and after: the paired t-test, and why it is often not the analysis you want",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "T-Tests &rarr; Paired Samples T-Test; baseline "
                        "and endline as the pair. Tick mean difference with CI, effect size, "
                        "descriptives, the Wilcoxon alternative. Illustrative output for the "
                        "remedial arm: mean change +9.8, 95% CI 8.8 to 10.8, t(599) = 19.4, "
                        "p &lt; .001, d = 0.79. For the control arm: +3.1, CI 2.2 to 4.0. Each "
                        "is a within-group change, and each is 'significant', and neither is "
                        "the programme effect."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The programme effect is the difference between the two changes (9.8 &minus; 3.1 = 6.7 points), which the paired test does not estimate.",
                           "Two ways to get it in jamovi: an independent t-test on the change score by arm (simple; correct for a randomised design), or ANCOVA of endline on arm with baseline as covariate (more precise, section 05).",
                           "A paired test on the treatment arm alone is the single most common wrong analysis in NGO evaluation reports: it attributes secular growth, practice effects and regression to the mean to the programme."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When the paired test is right", "html":
                         "When there is no control group and the question is descriptive: "
                         "'did scores change?' Then report it as change, not as effect. "
                         "When the design is a crossover or a within-person comparison of "
                         "two conditions. When the 'pair' is a matched pair of villages. "
                         "In each case the sentence is about the pair, and the causal claim "
                         "is the design's, not the test's."},
                        {"t": "hbox", "color": "green", "html": "The difference-in-differences "
                         "in a menu: compute change, independent t-test by arm. Illustrative "
                         "result: difference in changes 6.7 points, 95% CI 5.3 to 8.1, "
                         "d = 0.55."}]},
         ]},

        {"type": "content", "label": "ANOVA", "title": "Three or more groups: one-way ANOVA and post hoc comparisons",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Question</strong>: does "
                        "decision-making differ by education level? <strong>Path</strong>: "
                        "ANOVA &rarr; ANOVA; decide_score as Dependent, educ as Fixed Factor. "
                        "<strong>Tick</strong>: Effect size (&omega;&sup2; is less biased than "
                        "&eta;&sup2;); Assumption Checks; Post Hoc Tests with educ, Tukey "
                        "correction, Effect size; Estimated Marginal Means with plot and "
                        "table."},
                       {"t": "table",
                        "head": ["Source", "SS", "df", "MS", "F", "p", "&omega;&sup2;"],
                        "rows": [
                            ["educ", "186.4", "3", "62.1", "13.8", "&lt; .001", "0.057"],
                            ["Residuals", "2,862.0", "636", "4.5", "", "", ""]]},
                       {"t": "table",
                        "head": ["Post hoc (Tukey)", "Mean difference", "SE", "p<sub>tukey</sub>", "d"],
                        "rows": [
                            ["Primary &minus; None", "0.52", "0.21", "0.06", "0.24"],
                            ["Secondary &minus; None", "1.14", "0.22", "&lt; .001", "0.53"],
                            ["Higher &minus; None", "1.61", "0.35", "&lt; .001", "0.75"],
                            ["Secondary &minus; Primary", "0.62", "0.23", "0.03", "0.29"]]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'Decision-making differed by education, F(3, 636) = 13.8, p &lt; "
                         ".001, &omega;&sup2; = 0.06. Tukey-corrected comparisons showed "
                         "higher scores for women with secondary (+1.1, p &lt; .001) and "
                         "higher (+1.6, p &lt; .001) education than for those with none; "
                         "the primary-none difference was small and not significant "
                         "(+0.5, p = .06).' The estimated marginal means plot is the "
                         "figure."},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. The omnibus F "
                         "says something differs; the post hoc table says what. Report "
                         "both, and the effect sizes, not the F alone."}]},
         ]},

        {"type": "content", "label": "Factorial", "title": "Two factors: does the programme work differently for girls and boys?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "ANOVA &rarr; ANOVA; endline as Dependent; arm "
                        "and sex as Fixed Factors; jamovi builds the model with both main "
                        "effects and the interaction. Tick Estimated Marginal Means for "
                        "arm &times; sex with a plot. The interaction term is the question: "
                        "if it is significant, the programme's effect differs by sex, and "
                        "the marginal-means plot shows how (lines not parallel). If not, "
                        "report the main effects."},
                       {"t": "table",
                        "head": ["Source", "F", "df", "p", "&omega;&sup2;"],
                        "rows": [
                            ["arm", "48.2", "1, 1196", "&lt; .001", "0.038"],
                            ["sex", "3.1", "1, 1196", "0.08", "0.002"],
                            ["arm &times; sex", "0.6", "1, 1196", "0.44", "0.000"]]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Illustrative: a clear arm effect, no evidence that it differs by sex (interaction p = .44, &omega;&sup2; near zero). The sentence says so, and does not go on to test the effect 'separately for girls and boys', which invites finding a difference by chance.",
                  "Add baseline as a Covariate in the same dialog and the model becomes ANCOVA with factors, the standard evaluation model.",
                  "Type III sums of squares (the default) are right for unbalanced designs; leave them.",
                  "Simple effects (the effect of arm within each sex) are an option under Estimated Marginal Means; report them only when the interaction is significant."]},
                        {"t": "hbox", "color": "amber", "html": "Testing for heterogeneity by "
                         "sex, caste, grade and district is eight interactions. One will "
                         "be 'significant'. Pre-specify the one that matters."}]},
         ]},

        {"type": "content", "label": "Repeated Measures", "title": "Repeated measures: the same children at three points",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "ANOVA &rarr; Repeated Measures ANOVA. Define "
                        "the within-subjects factor (time: baseline, midline, endline), drag "
                        "the three score columns into its cells, add arm as a "
                        "Between-Subjects Factor. Tick Assumption Checks (Mauchly's "
                        "sphericity) and apply Greenhouse-Geisser if it fails; Estimated "
                        "Marginal Means for time &times; arm with a plot. The time &times; arm "
                        "interaction is the programme effect over time."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Data must be wide: one row per child, one column per occasion. Long data (one row per child-occasion) needs reshaping first, which jamovi cannot do; do it in the source or in Rj.",
                           "Any child missing an occasion is dropped entirely. With attrition, the mixed model (section 08) keeps them and is the better tool.",
                           "The sphericity assumption (equal variances of all pairwise differences) fails routinely; the correction is one tick."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Illustrative reading", "html":
                         "Time &times; arm: F(1.8, 2,100) = 21.4, p &lt; .001 after "
                         "Greenhouse-Geisser (&epsilon; = 0.91). The plot: both arms rise "
                         "from baseline to midline; the remedial arm keeps rising to "
                         "endline while the control flattens. The effect appears in the "
                         "second half of the year. That is a finding the two-wave design "
                         "could not have produced, and it is the reason to collect a "
                         "midline."},
                        {"t": "hbox", "color": "green", "html": "Report the marginal means at "
                         "each occasion by arm with CIs, in a table and a plot. The F "
                         "statistic is the footnote."}]},
         ]},

        {"type": "content", "label": "Non-parametric", "title": "Non-parametric tests: when, and what they actually test",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Test", "Replaces", "Tests", "Effect size"],
                        "rows": [
                            ["Mann-Whitney U", "Independent t", "Whether one group tends to have higher values (stochastic dominance), not the medians unless shapes match", "Rank-biserial correlation (tick-box)"],
                            ["Wilcoxon signed-rank", "Paired t", "Whether differences tend to be positive", "Rank-biserial"],
                            ["Kruskal-Wallis", "One-way ANOVA", "Whether any group tends higher", "&epsilon;&sup2; (tick-box); Dwass-Steel-Critchlow-Fligner pairwise comparisons"],
                            ["Friedman", "Repeated-measures ANOVA", "Whether occasions differ in rank", "Durbin-Conover pairwise"],
                            ["Spearman's &rho;", "Pearson's r", "Monotonic association", "&rho; itself"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Use them when the outcome is "
                        "ordinal with few levels, when the sample is small and the "
                        "distribution clearly non-normal, or when outliers dominate and "
                        "cannot be resolved. Do not use them because Shapiro-Wilk was "
                        "significant in a sample of 600. They lose a little power when the "
                        "t-test would have been valid and they answer a slightly different "
                        "question, which the report should state in words: 'savings tended "
                        "to be higher among members (Mann-Whitney U = 38,240, p &lt; .001; "
                        "rank-biserial r = 0.24)', with the medians and IQRs alongside."},
                        {"t": "hbox", "color": "amber", "html": "For skewed money variables, "
                         "the alternative is often better than either: a t-test on the log "
                         "(a ratio of geometric means), or a median regression in R."}]},
         ]},

        {"type": "content", "label": "Comparison Report", "title": "Reporting a group comparison: the table and the figure",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Outcome", "Remedial, mean (SD), n", "Control, mean (SD), n", "Difference (95% CI)", "Test", "Effect size"],
                        "rows": [
                            ["Endline reading (0&ndash;100)", "51.0 (16.2), 600", "44.3 (16.8), 600", "6.7 (4.8 to 8.6)", "Welch t(1,196) = 7.0, p &lt; .001", "d = 0.41"],
                            ["Change from baseline", "9.8 (12.4), 600", "3.1 (11.9), 600", "6.7 (5.3 to 8.1)", "Welch t(1,196) = 9.5, p &lt; .001", "d = 0.55"],
                            ["Attendance (%)", "82.1 (11.0), 600", "80.9 (11.6), 600", "1.2 (&minus;0.1 to 2.5)", "Welch t(1,196) = 1.8, p = .07", "d = 0.11"],
                            ["Reads a paragraph, n (%)", "372 (62)", "294 (49)", "13 points (7 to 18)", "&chi;&sup2;(1) = 20.4, p &lt; .001", "RR 1.27"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. One row per outcome, "
                        "the same columns for each, the difference and its interval before "
                        "the test, the effect size last. The last row is section 06's."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The figure", "html":
                         "The descriptives plot from the t-test dialog: two means with 95% "
                         "CIs, one per arm, for the primary outcome. Or, better, the "
                         "<em>esci</em> module's estimation plot, which shows the two "
                         "distributions, the means, and the difference with its interval "
                         "on a separate axis. Export as SVG."},
                        {"t": "hbox", "color": "amber", "html": "Clustering by school makes "
                         "every interval here too narrow. Section 08 shows the mixed "
                         "model that corrects it, and the report's limitations must "
                         "mention it if the mixed model was not run."}]},
         ]},

        # ===================== SECTION 05: CORRELATION AND REGRESSION =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Correlation and Regression"},

        {"type": "content", "label": "Correlation", "title": "The correlation matrix: Pearson, Spearman, and the plot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Regression &rarr; Correlation Matrix; drag "
                        "in the continuous variables. Tick Pearson (for linear "
                        "relationships between roughly normal variables), Spearman (for "
                        "monotonic relationships, ordinal variables or outliers), Report "
                        "significance, Confidence intervals, Flag significant, and Plot "
                        "(a scatter matrix with densities and fit lines). Kendall's tau-b "
                        "is there for small samples with many ties."},
                       {"t": "table",
                        "head": ["", "Baseline", "Endline", "Attendance"],
                        "rows": [
                            ["Baseline", "&mdash;", "", ""],
                            ["Endline", "0.71 [0.68, 0.74]", "&mdash;", ""],
                            ["Attendance", "0.18 [0.12, 0.23]", "0.24 [0.19, 0.29]", "&mdash;"]]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Illustrative. Baseline predicts endline strongly (r = 0.71), which is why ANCOVA is precise. Attendance relates weakly to both.",
                  "Report r with its CI; the p-value adds nothing when n = 1,200 and everything is 'significant'. r = 0.18 is a small association whatever its p.",
                  "The scatter plot is not optional. Anscombe's quartet has four datasets with identical r and entirely different shapes.",
                  "Correlation is symmetric and says nothing about direction or cause. Every phrase in the report should be 'associated with'."]},
                        {"t": "hbox", "color": "amber", "html": "A correlation matrix with "
                         "twenty variables and stars on the significant ones is a fishing "
                         "net. Pick the correlations the question needs."}]},
         ]},

        {"type": "content", "label": "Linear Regression", "title": "Linear regression: the dialog, the output, and the sentence",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Question</strong>: what is "
                        "the programme effect on endline reading, adjusting for baseline and "
                        "grade? <strong>Path</strong>: Regression &rarr; Linear Regression; "
                        "endline as Dependent; baseline into Covariates; arm and grade into "
                        "Factors. <strong>Tick</strong>: Model Fit (R&sup2;, adjusted, F); "
                        "Model Coefficients: Confidence interval, Standardized estimate; "
                        "Assumption Checks: Q-Q plot of residuals, Residual plots, "
                        "Collinearity statistics, Durbin-Watson if ordered; Estimated "
                        "Marginal Means for arm."},
                       {"t": "table",
                        "head": ["Predictor", "Estimate", "SE", "95% CI", "t", "p", "Std. &beta;"],
                        "rows": [
                            ["Intercept", "14.6", "1.4", "11.8 to 17.4", "10.3", "&lt; .001", ""],
                            ["baseline", "0.72", "0.02", "0.68 to 0.76", "33.5", "&lt; .001", "0.71"],
                            ["arm: Remedial &minus; Control", "6.6", "0.68", "5.3 to 7.9", "9.7", "&lt; .001", "0.20"],
                            ["grade: 4 &minus; 3", "1.9", "0.83", "0.3 to 3.5", "2.3", "0.02", ""],
                            ["grade: 5 &minus; 3", "3.4", "0.84", "1.8 to 5.1", "4.1", "&lt; .001", ""]]},
                       {"t": "body", "cls": "sm", "html": "R&sup2; = 0.55, adjusted 0.55, "
                        "F(4, 1,195) = 362, p &lt; .001. Illustrative."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'Adjusting for baseline score and grade, children in the remedial "
                         "arm scored 6.6 points higher at endline (95% CI 5.3 to 7.9, "
                         "p &lt; .001), about 0.4 SD of the baseline distribution. Baseline "
                         "score was the strongest predictor (0.72 points per baseline "
                         "point). The model explained 55% of the variance in endline "
                         "scores.'"},
                        {"t": "hbox", "color": "amber", "html": "This is ANCOVA in regression "
                         "form and the standard analysis for a randomised two-wave design. "
                         "Its CI (5.3 to 7.9) is narrower than the change-score t-test's "
                         "(5.3 to 8.1) because baseline is used as a covariate rather than "
                         "subtracted with coefficient 1."}]},
         ]},

        {"type": "content", "label": "Diagnostics", "title": "Regression diagnostics: the plots and what they say",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Check", "Where", "Good", "Bad, and the fix"],
              "rows": [
                  ["Residuals vs fitted", "Assumption Checks &rarr; Residual plots", "A flat band of points", "A curve: non-linearity, add a squared term or transform; a funnel: heteroskedasticity, use robust SEs (Rj: <em>sandwich</em>) or transform the outcome"],
                  ["Q-Q plot of residuals", "Same", "Points on the line", "Heavy tails or skew: check outliers; for large n the estimates are fine, the intervals slightly off"],
                  ["Collinearity (VIF, tolerance)", "Assumption Checks &rarr; Collinearity statistics", "VIF below 5, ideally below 3", "Two predictors measure the same thing; drop one or combine"],
                  ["Influential cases (Cook's distance)", "Assumption Checks &rarr; Cook's distance", "All small", "A few cases drive the fit; verify them, report with and without"],
                  ["Autocorrelation (Durbin-Watson)", "Assumption Checks", "Near 2", "Only for ordered data; for clustered data the fix is a mixed model"],
                  ["Linearity of each covariate", "Scatter plots; add a squared term", "No improvement", "Curvilinear: keep the square, interpret with a plot"]]},
             {"t": "body", "cls": "sm", "html": "Three ticks, thirty seconds. The two most "
              "common problems in evaluation data are a bounded outcome with floor effects "
              "(the residual plot shows it) and clustering (no plot shows it; you know it "
              "from the design). The first argues for a plot of the outcome's distribution "
              "in the report; the second for section 08."},
         ]},

        {"type": "content", "label": "Categorical Predictors", "title": "Factors in regression: dummy coding, reference levels and contrasts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A nominal predictor dragged into Factors is "
                        "dummy-coded automatically: one coefficient per level against a "
                        "reference level, which is the first level in the variable's order. "
                        "Reference Levels in the dialog changes it; for education, 'None' "
                        "is the natural reference and the coefficients read as 'Primary "
                        "versus None', 'Secondary versus None'. For an ordinal factor jamovi "
                        "offers polynomial contrasts (linear, quadratic trends); for most "
                        "reporting the simple (dummy) contrasts are clearer."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The estimated marginal means (tick it) give the adjusted mean outcome at each level, which is what a report table wants, with CIs.",
                           "An ordinal predictor with many levels (age bands) can be entered as a factor or as a numeric covariate; the factor is safer, the covariate is one number.",
                           "Interactions: Model Builder &rarr; select two terms &rarr; add as interaction. Section 04's factorial logic applies, with the marginal-means plot as the reading."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The Model Builder", "html":
                         "Regression &rarr; Linear Regression &rarr; Model Builder lets you "
                         "add predictors in blocks and compares the blocks: R&sup2; change "
                         "and its F-test from adding the programme arm to a model that "
                         "already has baseline and grade. That is the 'what does the "
                         "programme add' question in one table, and it is where "
                         "hierarchical regression in a thesis lives."},
                        {"t": "hbox", "color": "green", "html": "Reference level: choose the "
                         "one the comparison is about, and say which in the table note. "
                         "'Female' as reference means the coefficient is 'Male minus "
                         "Female'."}]},
         ]},

        {"type": "content", "label": "Interpreting", "title": "Reading coefficients: units, standardisation, and what 'controlling for' means",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Unstandardised</strong> (Estimate): the change in the outcome, in its units, per unit of the predictor, other predictors held constant. 6.6 reading points for the programme; 0.72 endline points per baseline point.",
                  "<strong>Standardised</strong> (Std. &beta;): the change in SDs of the outcome per SD of the predictor. Useful to compare predictors within a model; meaningless for a binary predictor's 'SD'.",
                  "<strong>Holding constant</strong> means comparing children with the same baseline and grade. It does not mean the programme effect is causal unless the design made it so; here it did.",
                  "<strong>R&sup2;</strong> is how much variance the model explains; a small R&sup2; with a precise, important coefficient is a good model of an outcome with many causes.",
                  "<strong>Non-significant</strong> is not 'no effect'; the CI says what effects are compatible. Attendance: 1.2 points, CI &minus;0.1 to 2.5. Small effects are not ruled out."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Observational data", "html":
                         "The same regression on the SHG survey, decide_score on "
                         "membership, education, age and own income, gives a membership "
                         "coefficient adjusted for those three. Membership was randomised "
                         "by village, so it is a causal effect. Own income was not, so its "
                         "coefficient is an association: women with income decide more, or "
                         "women who decide more earn income, or both come from something "
                         "unmeasured. The dialog does not know the difference. The "
                         "analyst does, and the report's verbs must show it."},
                        {"t": "hbox", "color": "green", "html": "Econometrics 101 and Impact "
                         "Evaluation 101 in this series are the courses on when a "
                         "coefficient is an effect. This course is on how to get the "
                         "coefficient."}]},
         ]},

        {"type": "content", "label": "Curves and Logs", "title": "Non-linear relationships: logs, squares, and reading them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Savings in rupees on age: the scatter plot "
                        "shows savings rising to the forties and falling after. A straight "
                        "line misses it. Compute age_sq (<code>age^2</code>) and add both as "
                        "covariates; the coefficient on the square is negative and "
                        "significant; the estimated marginal means plot (or the "
                        "<em>Flexplot</em> module) draws the curve. Alternatively compute "
                        "the log of savings as the outcome, in which case coefficients "
                        "read as proportional changes: 0.05 means about 5% more savings "
                        "per year of age."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Log outcome: coefficients are approximately percentage changes for small values; exactly (exp(b) &minus; 1) &times; 100.",
                           "Log predictor: the coefficient is the change in the outcome per 1% change in the predictor, divided by 100.",
                           "Zeros: log(x + 1) is common and changes the interpretation for small x; say so. Half the sample saving zero is a two-part question (do they save; how much), and section 06's logistic model answers the first part.",
                           "A square term's peak is at &minus;b<sub>1</sub>/(2b<sub>2</sub>); compute it and report it in the predictor's units."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The plot decides. If the "
                        "scatter with a smooth line (Correlation Matrix &rarr; Plot, or "
                        "Flexplot) is straight, the linear model is fine; if it bends, "
                        "model the bend; if it does something no polynomial fits, the "
                        "relationship may be a threshold, and a factor with cut points is "
                        "more honest than a curve."}]},
         ]},

        {"type": "content", "label": "Regression Report", "title": "Reporting a regression: the table a thesis examiner expects",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["", "Model 1: baseline only", "Model 2: + arm", "Model 3: + grade, sex, attendance"],
                        "rows": [
                            ["Baseline score", "0.74 (0.71, 0.77)", "0.73 (0.70, 0.76)", "0.72 (0.68, 0.76)"],
                            ["Remedial arm", "", "6.7 (5.4, 8.0)", "6.6 (5.3, 7.9)"],
                            ["Grade 4 (vs 3)", "", "", "1.9 (0.3, 3.5)"],
                            ["Grade 5 (vs 3)", "", "", "3.4 (1.8, 5.1)"],
                            ["Boy (vs girl)", "", "", "&minus;0.8 (&minus;2.1, 0.5)"],
                            ["Attendance (per 10 points)", "", "", "0.9 (0.3, 1.5)"],
                            ["R&sup2;", "0.50", "0.54", "0.55"],
                            ["&Delta;R&sup2; (p)", "", "0.04 (&lt; .001)", "0.01 (&lt; .001)"],
                            ["n", "1,200", "1,200", "1,196"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. Unstandardised "
                        "coefficients with 95% CIs; the three models from the Model Builder "
                        "in three columns; the note states the reference levels, the "
                        "outcome's units and the clustering caveat."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Why three columns", "html":
                         "The arm effect barely moves as covariates are added (6.7 to "
                         "6.6), which is what randomisation predicts and what a reader "
                         "checks. In an observational study, a coefficient that halves "
                         "when a control is added was confounded by it, and the columns "
                         "show that too. The &Delta;R&sup2; row says what each block "
                         "added."},
                        {"t": "hbox", "color": "amber", "html": "Stars are optional; intervals "
                         "are not. A coefficient with a CI is readable without the "
                         "p-value; the reverse is not true."}]},
         ]},

        # ===================== SECTION 06: CATEGORICAL OUTCOMES =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Categorical Outcomes"},

        {"type": "content", "label": "Proportions", "title": "One proportion and a goodness-of-fit: the Frequencies menu",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Frequencies &rarr; Proportion Test (2 "
                        "Outcomes) tests whether a binary variable's proportion differs "
                        "from a value: is the share of children who can read a paragraph "
                        "different from the state's 50% figure? Tick the confidence "
                        "interval. Frequencies &rarr; N Outcomes (&chi;&sup2; Goodness of "
                        "Fit) tests whether the distribution across categories matches "
                        "expected proportions: does the sample's caste distribution match "
                        "the district's census shares? Enter the expected proportions in "
                        "the dialog."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Illustrative: 666 of 1,200 children read a paragraph, 55.5%, 95% CI 52.7 to 58.3; against 50%, p &lt; .001.",
                           "The CI is the result; the test against an arbitrary value rarely is.",
                           "Goodness-of-fit against census shares is a representativeness check for a survey, and belongs in the methods."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Binary variables as continuous", "html":
                         "A 0/1 variable set as continuous has a mean equal to the "
                         "proportion, and Descriptives gives it with a CI, split by group, "
                         "in one step. A t-test on a 0/1 outcome by arm estimates the "
                         "difference in proportions with a CI and is close to the "
                         "two-proportion z-test; it is a defensible shortcut for a "
                         "report, and the contingency table (next slide) is the formal "
                         "version."},
                        {"t": "hbox", "color": "green", "html": "Report proportions with n and "
                         "CI: '55.5% (666 of 1,200; 95% CI 52.7 to 58.3)'. Never a "
                         "percentage without its n."}]},
         ]},

        {"type": "content", "label": "Chi-square", "title": "Two categorical variables: the chi-square test of association",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Question</strong>: does the "
                        "share of children reading a paragraph differ by arm? "
                        "<strong>Path</strong>: Frequencies &rarr; Contingency Tables &rarr; "
                        "Independent Samples; arm in Rows, reads_para in Columns. "
                        "<strong>Tick</strong>: &chi;&sup2;, &chi;&sup2; continuity correction "
                        "(for 2&times;2), Fisher's exact; Comparative Measures: Odds ratio, "
                        "Relative risk, with CIs; Nominal: Phi and Cramer's V; Cells: Row "
                        "percentages, Expected counts."},
                       {"t": "table",
                        "head": ["Arm", "Reads: Yes", "No", "Total", "Row %"],
                        "rows": [
                            ["Remedial", "372", "228", "600", "62.0%"],
                            ["Control", "294", "306", "600", "49.0%"],
                            ["Total", "666", "534", "1,200", "55.5%"]]},
                       {"t": "table",
                        "head": ["Statistic", "Value", "df", "p"],
                        "rows": [
                            ["&chi;&sup2;", "20.6", "1", "&lt; .001"],
                            ["Relative risk (Remedial vs Control)", "1.27", "", "95% CI 1.15 to 1.39"],
                            ["Odds ratio", "1.70", "", "95% CI 1.35 to 2.14"],
                            ["Cramer's V", "0.13", "", ""]]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'Children in the remedial arm were more likely to read a "
                         "paragraph at endline (62% vs 49%; difference 13 percentage "
                         "points; risk ratio 1.27, 95% CI 1.15 to 1.39; &chi;&sup2;(1) = "
                         "20.6, p &lt; .001).' The percentage-point difference and the risk "
                         "ratio are what a programme reader can use; the odds ratio "
                         "overstates the effect when the outcome is common, as here."},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. Cramer's V of "
                         "0.13 is a small association by convention and a 13-point "
                         "difference in reading is not small in policy. Effect-size "
                         "conventions are not the last word."}]},
         ]},

        {"type": "content", "label": "Small Cells", "title": "Small samples, small cells, and paired categorical data",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "The &chi;&sup2; approximation fails when expected counts are small (below 5 in more than 20% of cells is the old rule). Tick Expected counts to see them; use Fisher's exact test (a tick-box) for 2&times;2 tables with small cells, and collapse categories or use Fisher's generalisation for larger tables.",
                  "Larger tables (education &times; income, 4&times;2): the &chi;&sup2; says the variables are associated; the row percentages say how; Cramer's V says how strongly. Post hoc, compare the standardised residuals (available as a tick-box) to see which cells drive it.",
                  "Ordered categories (education &times; a Likert item): the &chi;&sup2; ignores the order; Spearman's correlation or an ordinal regression uses it and has more power.",
                  "Paired categorical data (the same child at baseline and endline, reads or not): Frequencies &rarr; Paired Samples (McNemar test). The question is whether more children moved from No to Yes than from Yes to No."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Layers", "html":
                         "Add a third variable to Layers and the table repeats within each "
                         "level: arm &times; reads within each grade. jamovi reports a "
                         "&chi;&sup2; per layer. This is how a report shows that the "
                         "programme's effect on reading held in every grade, or did not, "
                         "without a logistic model. It is also where Simpson's paradox "
                         "lives: an association in the pooled table that reverses within "
                         "every layer, because the layer variable confounds it."},
                        {"t": "hbox", "color": "green", "html": "Illustrative McNemar: of 600 "
                         "remedial children, 190 moved from not reading to reading and 22 "
                         "the other way; p &lt; .001. The 22 are worth a look."}]},
         ]},

        {"type": "content", "label": "Logistic", "title": "Logistic regression: a binary outcome with several predictors",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Path</strong>: Regression "
                        "&rarr; Logistic Regression &rarr; 2 Outcomes (Binomial); reads_para "
                        "as Dependent; baseline into Covariates; arm, grade, sex into "
                        "Factors. <strong>Tick</strong>: Model Fit (deviance, AIC, McFadden's "
                        "R&sup2;); Model Coefficients: Odds ratio with CI; Estimated Marginal "
                        "Means for arm (these are predicted probabilities, and the useful "
                        "output); Prediction: Classification table, Accuracy, AUC and ROC "
                        "curve; Assumption Checks: Collinearity."},
                       {"t": "table",
                        "head": ["Predictor", "Estimate (log odds)", "SE", "Odds ratio", "95% CI", "p"],
                        "rows": [
                            ["Intercept", "&minus;2.84", "0.23", "", "", "&lt; .001"],
                            ["baseline (per point)", "0.064", "0.005", "1.07", "1.06 to 1.08", "&lt; .001"],
                            ["arm: Remedial", "0.61", "0.13", "1.84", "1.42 to 2.38", "&lt; .001"],
                            ["grade: 4 vs 3", "0.28", "0.16", "1.32", "0.97 to 1.81", "0.08"],
                            ["grade: 5 vs 3", "0.55", "0.16", "1.73", "1.26 to 2.38", "&lt; .001"],
                            ["sex: Boy", "&minus;0.09", "0.13", "0.91", "0.71 to 1.17", "0.47"]]},
                       {"t": "body", "cls": "sm", "html": "Estimated marginal means: predicted "
                        "probability of reading, remedial 0.63 (0.59 to 0.67), control 0.48 "
                        "(0.44 to 0.52), at mean baseline. AUC 0.79. Illustrative."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'Adjusting for baseline score, grade and sex, children in the "
                         "remedial arm had 1.8 times the odds of reading a paragraph "
                         "(95% CI 1.4 to 2.4, p &lt; .001); the predicted probability was "
                         "63% versus 48% at the mean baseline score, a difference of 15 "
                         "percentage points.' Give the probabilities; nobody thinks in "
                         "odds."},
                        {"t": "hbox", "color": "amber", "html": "The odds ratio (1.84) is "
                         "larger than the risk ratio (1.27) because the outcome is common. "
                         "Reporting the odds ratio as if it were a risk ratio ('84% more "
                         "likely') is a routine misreading."}]},
         ]},

        {"type": "content", "label": "Reading Logistic", "title": "Reading logistic output: odds, probabilities, and fit",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "The coefficient is a change in log odds; exponentiated, an odds ratio; neither is a change in probability. The change in probability depends on where you start, which is why the marginal means (predicted probabilities at set values) are the reportable result.",
                  "McFadden's R&sup2; is not variance explained and its values are low (0.2 is good); do not compare it with a linear R&sup2;.",
                  "AUC is the probability that a random reader has a higher predicted probability than a random non-reader; 0.5 is chance, above 0.8 is strong. It measures discrimination, not calibration.",
                  "The classification table at a 0.5 cut-off is often misleading when the outcome is unbalanced; report it, but do not choose the model on it.",
                  "Separation (a predictor that perfectly predicts the outcome) produces enormous coefficients and SEs; the fix is a penalised model in R, or collapsing the predictor."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Three or more categories", "html":
                         "Regression &rarr; Logistic Regression &rarr; N Outcomes "
                         "(Multinomial) for unordered categories (main occupation: farm, "
                         "non-farm, none); Ordinal Outcomes for ordered ones (a five-point "
                         "satisfaction item, or a decision-making item scored 0/1/2). The "
                         "ordinal model (proportional odds) gives one odds ratio per "
                         "predictor for being in a higher category and assumes it is the "
                         "same across the thresholds; that assumption is not tested in "
                         "jamovi's dialog and should be checked in R for a paper."},
                        {"t": "hbox", "color": "green", "html": "The ordinal model is the "
                         "right analysis of a single Likert item as an outcome. A t-test "
                         "on it is the common one."}]},
         ]},

        {"type": "content", "label": "Rates and Counts", "title": "Counts and rates: when the outcome is 'how many'",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Number of clinic visits, number of days "
                        "absent, number of loans: counts, bounded at zero, skewed, often "
                        "with many zeros. A linear regression on a count gives negative "
                        "predictions and wrong intervals. The jamovi core has no Poisson "
                        "dialog; the <em>GAMLj</em> module's Generalized Linear Model does "
                        "Poisson and negative binomial, with an offset for exposure (days "
                        "at risk) and coefficients that exponentiate to rate ratios."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Poisson assumes variance equals the mean; counts almost always have more variance (overdispersion), and negative binomial handles it. GAMLj reports the dispersion.",
                           "Many zeros beyond what the model expects: a zero-inflated or hurdle model, in R. Or split the question: any visits (logistic) and how many among those with any (count).",
                           "A rate ratio of 1.3 reads as '30% more visits per child-year in the treatment arm'."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The bounded-score problem", "html":
                         "A reading score from 0 to 100 with a pile at 0 and a pile at "
                         "100 is neither a count nor a continuous normal variable. Linear "
                         "regression is usually tolerable for the middle and wrong at the "
                         "ends; a beta regression or a Tobit is the formal answer, in R. "
                         "For a report, the linear model with a plot of the distribution "
                         "by arm and a sentence about the floor is honest."},
                        {"t": "hbox", "color": "green", "html": "GAMLj, by Marcello Gallucci, "
                         "is the single most useful module to install. Section 08."}]},
         ]},

        {"type": "content", "label": "Attrition Table", "title": "A worked attrition table: who was lost, by arm",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["", "Remedial", "Control", "Test"],
                        "rows": [
                            ["Enrolled at baseline", "640", "640", ""],
                            ["Endline score available", "600 (93.8%)", "600 (93.8%)", "&chi;&sup2;(1) = 0.0, p = 1.00"],
                            ["Baseline score of those lost, mean (SD)", "34.1 (15.0), n = 40", "36.2 (15.8), n = 40", "Welch t(78) = 0.6, p = .54"],
                            ["Baseline score of those retained", "41.7 (16.0)", "41.5 (16.3)", ""],
                            ["Lost vs retained, pooled", "35.2 vs 41.6", "", "Welch t(94) = 3.5, p &lt; .001"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. Built from one "
                        "contingency table (arm &times; missing-endline indicator) and two "
                        "t-tests using a computed indicator and filters. Attrition is equal "
                        "across arms and lost children were weaker at baseline in both arms "
                        "equally."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'Attrition was 6.2% in both arms. Children lost to follow-up had "
                         "lower baseline scores than those retained (35.2 vs 41.6, "
                         "p &lt; .001) but did not differ by arm (p = .54), so the "
                         "comparison between arms is unlikely to be biased by attrition; "
                         "the endline means overstate the level for the full cohort.' Four "
                         "numbers, one paragraph, and the evaluation's main threat "
                         "addressed."},
                        {"t": "hbox", "color": "amber", "html": "Every evaluation report "
                         "needs this table and most do not have it. It costs three "
                         "dialogs."}]},
         ]},

        {"type": "content", "label": "Categorical Report", "title": "Reporting categorical results: the checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Result", "Report", "Not"],
              "rows": [
                  ["A proportion", "% with n and 95% CI", "% alone"],
                  ["Two proportions", "Both %, the difference in points with CI, the risk ratio with CI, the test", "The odds ratio alone when the outcome is common"],
                  ["A table", "Counts and row or column % (say which), the &chi;&sup2; with df and p, Cramer's V", "Percentages with no counts"],
                  ["A logistic model", "Odds ratios with CIs, predicted probabilities at meaningful values, n, AUC", "'Significant predictors' with stars"],
                  ["Small cells", "Fisher's exact; the cells collapsed and why", "A &chi;&sup2; with expected counts of 2"],
                  ["Attrition", "By arm, with baseline comparison of lost and retained", "'Some children could not be followed up'"],
                  ["Ordinal outcome", "The ordinal model's odds ratio, or the item distribution by group", "A mean of the codes as if continuous, without saying so"]]},
             {"t": "body", "cls": "sm", "html": "The pattern is the same as section 04's: "
              "the estimate and its interval first, the test second, the effect size in "
              "units a reader can use. For categorical outcomes the usable unit is the "
              "percentage point."},
         ]},

        # ===================== SECTION 07: SCALES AND FACTOR ANALYSIS =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Scales and Factor Analysis"},

        {"type": "content", "label": "Reliability", "title": "Reliability analysis: alpha, omega, and the items that hurt",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Path</strong>: Factor &rarr; "
                        "Reliability Analysis; d1 to d5 into Items. <strong>Tick</strong>: "
                        "Cronbach's &alpha;, McDonald's &omega;; Item statistics: "
                        "item-rest correlation, &alpha; if item dropped, &omega; if item "
                        "dropped; Correlation heatmap. Reverse-scaled items go in their "
                        "own box and are flipped automatically."},
                       {"t": "table",
                        "head": ["Item", "Mean", "SD", "Item-rest r", "&alpha; if dropped", "&omega; if dropped"],
                        "rows": [
                            ["d1 food purchases", "1.32", "0.71", "0.58", "0.74", "0.75"],
                            ["d2 large purchases", "1.04", "0.78", "0.64", "0.72", "0.73"],
                            ["d3 visiting family", "1.21", "0.74", "0.60", "0.73", "0.74"],
                            ["d4 own health care", "1.18", "0.76", "0.55", "0.75", "0.76"],
                            ["d5 children's schooling", "1.55", "0.62", "0.31", "0.81", "0.82"],
                            ["Scale", "", "", "", "&alpha; = 0.79", "&omega; = 0.80"]]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading it", "html":
                         "Alpha 0.79 and omega 0.80 are acceptable. Item d5 correlates "
                         "weakly with the rest (0.31) and the scale would be more reliable "
                         "without it (0.81). That is a reason to look at d5, not a reason "
                         "to delete it: SEM 101's discussion of that item applies. Report "
                         "&omega; over &alpha; when they differ, because &alpha; assumes "
                         "equal loadings."},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. Ordinal items "
                         "with three categories: the reliability from the raw scores "
                         "understates the ordinal reliability. jamovi's dialog uses the "
                         "raw scores; say so, or compute the ordinal version in Rj."}]},
         ]},

        {"type": "content", "label": "EFA", "title": "Exploratory factor analysis: how many factors, and which items go together",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Factor &rarr; Exploratory Factor Analysis; the "
                        "twelve empowerment items into Variables. Extraction: minimum "
                        "residuals (default) or maximum likelihood; Rotation: oblimin (the "
                        "factors may correlate); Number of factors: based on parallel "
                        "analysis (the recommended default), or eigenvalue above 1, or a "
                        "fixed number to compare. Tick Assumption Checks (Bartlett's, KMO), "
                        "Factor summary, Factor correlations, Model fit measures, and Hide "
                        "loadings below 0.3 for readability. Scree plot under Additional "
                        "Output."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "KMO above 0.7 and Bartlett's p &lt; .001 say the items correlate enough to factor. KMO below 0.6 says stop.",
                           "Parallel analysis compares the eigenvalues to those from random data of the same size; it is the one factor-count rule that survives scrutiny.",
                           "Principal Component Analysis is a separate dialog (Factor &rarr; PCA) and is not factor analysis; use it for data reduction, not for scale structure."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Illustrative result", "html":
                         "Parallel analysis: three factors. After oblimin rotation, d1 to "
                         "d5 load on factor 1 (0.45 to 0.79, d5 lowest), m1 to m3 on factor "
                         "2 (0.68 to 0.83), a1 to a4 on factor 3 (0.52 to 0.74); one cross-"
                         "loading (a1 on factor 1, 0.32). Factor correlations 0.31 to 0.46. "
                         "The scale has the structure it was designed with; d5 and a1 are "
                         "the items to discuss. Uniqueness above 0.8 on an item means the "
                         "factors explain little of it."},
                        {"t": "hbox", "color": "green", "html": "EFA on the pilot or on half "
                         "the sample; CFA (next slide) on the rest. Both in one dialog "
                         "each."}]},
         ]},

        {"type": "content", "label": "CFA", "title": "Confirmatory factor analysis in the jamovi core",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Factor &rarr; Confirmatory Factor "
                        "Analysis. Create three factors, name them, drag the items into "
                        "each. Estimates: Standardized estimate, Factor covariances; Model "
                        "Fit: Test for exact fit (&chi;&sup2;), CFI, TLI, RMSEA with CI, SRMR; "
                        "Additional Output: Residual covariances, Modification indices, "
                        "Path diagram. The estimator is maximum likelihood; missing data by "
                        "full-information ML (a tick) or exclude cases listwise."},
                       {"t": "table",
                        "head": ["Fit measure", "Value", "Reads as"],
                        "rows": [
                            ["&chi;&sup2; (df), p", "118.6 (51), &lt; .001", "Exact fit rejected, as expected at n = 640"],
                            ["CFI", "0.955", "Above 0.95"],
                            ["TLI", "0.942", "Just under 0.95"],
                            ["RMSEA [90% CI]", "0.046 [0.035, 0.057]", "Good"],
                            ["SRMR", "0.045", "Good"]]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Illustrative. The structure holds by every approximate-fit measure; the residual covariances show where the small misfit is.",
                  "jamovi's core CFA uses ML only, which is not ideal for three-category items; the <em>SEMLj</em> module (section 08) adds the ordinal estimator (WLSMV) and full SEM.",
                  "Modification indices are shown; the reason to look at them and not to act on them is in SEM 101, section 06.",
                  "The path diagram is a report figure; export it as SVG."]},
                        {"t": "hbox", "color": "green", "html": "Reliability, EFA and CFA in "
                         "three core dialogs: jamovi covers scale validation to the level "
                         "a master's thesis needs, without SPSS or AMOS."}]},
         ]},

        {"type": "content", "label": "Scale Scores", "title": "From factor to score: what to compute and use downstream",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Sum or mean of items</strong>: Compute with MEAN(); transparent, comparable across studies, weights every item equally. The right choice for most reports.",
                  "<strong>Factor scores</strong>: EFA and CFA dialogs can save them (a tick under Additional Output writes them to the data as new columns). Weighted by loadings; standardised; not comparable across samples; fine for a regression within this study.",
                  "<strong>Standardised sum</strong>: Z() of the mean score, so effects read in SDs.",
                  "<strong>Categorised</strong> ('high' vs 'low' empowerment at the median): loses information, invites arbitrary cut points, and should be avoided unless a threshold has meaning."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Sub-scales", "html":
                         "Three factors give three scores (decision-making, mobility, "
                         "assets) and a total. Report the programme's effect on each: a "
                         "programme that moves mobility and not decision-making is a "
                         "finding the total hides. Three t-tests or one ANCOVA per "
                         "sub-scale, with a note that three tests were run. The MANOVA "
                         "dialog (ANOVA &rarr; MANCOVA) tests them jointly, and is rarely "
                         "what a reader wants."},
                        {"t": "hbox", "color": "green", "html": "Whatever the score, its "
                         "reliability and its construction go in the methods, with the "
                         "formula. A reviewer will ask."}]},
         ]},

        {"type": "content", "label": "Translation Check", "title": "Comparing languages: the invariance check jamovi can and cannot do",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The survey ran in Hindi and Bangla. Before "
                        "comparing scores across languages, the items should work the same "
                        "way in each. In the jamovi core: run the CFA with Split by "
                        "language and compare the loadings and fit by eye; run reliability "
                        "split by language. That is the configural check and a rough metric "
                        "check. The formal invariance sequence (metric, scalar, with "
                        "&Delta;CFI) is in the <em>SEMLj</em> module's multigroup option, or "
                        "in R with <em>lavaan</em> and <em>semTools</em>."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Illustrative: loadings within 0.1 of each other in both languages for ten items; d3 loads 0.72 in Hindi and 0.51 in Bangla; &alpha; 0.80 and 0.76.",
                           "A loading that differs by 0.2 is an item to take back to the translators and the cognitive-interview notes.",
                           "Report the split CFA in the methods and the formal test if the comparison across languages is a result of the paper."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "SEM 101, section 08, is the "
                        "full treatment. The point here is that the first, informative "
                        "look costs one tick (Split by) and most multilingual surveys "
                        "never take it."}]},
         ]},

        {"type": "content", "label": "IRT", "title": "Item response theory in a module: when items should not be summed",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A reading test where items range from "
                        "letters to paragraphs is not a set of interchangeable questions; "
                        "a child who reads the paragraph has answered the easier items too. "
                        "Item response theory models each item's difficulty and "
                        "discrimination and places children on a common ability scale. The "
                        "<em>snowIRT</em> and <em>psychoPDA</em> modules bring Rasch and "
                        "2PL/graded response models into jamovi: item parameters, item "
                        "characteristic curves, person ability estimates, fit statistics, "
                        "and differential item functioning by group."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Use it for ability and knowledge tests, and for scales where items differ sharply in severity (food insecurity: worrying about food versus going a whole day without).",
                           "The ability estimate is a better outcome than the raw score when items differ in difficulty and when tests differ across waves.",
                           "DIF by language or sex is the IRT version of measurement invariance, item by item."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "Item Response Theory 101 in "
                        "this series is the course; the module is where a jamovi user can "
                        "run its examples without code. Install: Modules &rarr; jamovi "
                        "library &rarr; search 'IRT'."}]},
         ]},

        {"type": "content", "label": "Scale Report", "title": "Reporting a scale: the paragraph and the table",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The paragraph", "html":
                         "'Decision-making was measured with five items (Appendix A) "
                         "scored 0 to 2 and summed (range 0&ndash;10; mean of available "
                         "items used where one item was missing, n = 14). Internal "
                         "consistency was acceptable (McDonald's &omega; = 0.80, Cronbach's "
                         "&alpha; = 0.79). Exploratory factor analysis on the pilot (n = 180) "
                         "and confirmatory factor analysis on the main sample supported a "
                         "three-factor structure across the twelve empowerment items "
                         "(CFI = 0.955, RMSEA = 0.046, SRMR = 0.045); item d5 loaded weakly "
                         "(0.41) and was retained for comparability with the source "
                         "scale. Loadings were similar in the Hindi and Bangla versions "
                         "except for item d3 (0.72 vs 0.51).'"}],
              "right": [{"t": "table",
                         "head": ["Scale", "Items", "Range", "&omega;", "&alpha;", "Mean (SD)", "Missing"],
                         "rows": [
                             ["Decision-making", "5", "0&ndash;10", "0.80", "0.79", "5.4 (2.2)", "8"],
                             ["Mobility", "3", "0&ndash;6", "0.81", "0.80", "3.1 (1.6)", "5"],
                             ["Control over assets", "4", "0&ndash;8", "0.76", "0.75", "3.8 (1.9)", "11"]]},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. The paragraph "
                         "and the table between them answer every question a methods "
                         "reviewer asks about a scale, and every number in them came from "
                         "the three Factor dialogs."}]},
         ]},

        # ===================== SECTION 08: THE MODULES =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "The Modules: Beyond the Basics"},

        {"type": "content", "label": "The Library", "title": "The jamovi library: modules worth installing, and what each adds",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Module", "Adds", "Use it for"],
              "rows": [
                  ["<em>GAMLj</em> (Gallucci)", "General linear model, generalized linear model (logistic, Poisson, negative binomial, ordinal, multinomial), mixed models, generalized mixed models; simple effects, plots, contrasts", "Clustered data (children in schools), counts, and any regression with interactions plotted properly"],
                  ["<em>jAMM</em> (Gallucci)", "Mediation and moderation with bootstrapped indirect effects, conditional effects, path diagrams", "Mechanism questions"],
                  ["<em>SEMLj</em> (Gallucci and Jentschke)", "Full SEM via lavaan: syntax or diagram interface, ordinal estimators, multigroup, invariance, fit", "Everything in SEM 101"],
                  ["<em>MAJOR</em> (Hamilton)", "Meta-analysis via metafor: effect sizes from various inputs, random effects, forest and funnel plots, moderators", "Everything in Systematic Reviews 101, section 07"],
                  ["<em>esci</em> (Cumming and Calin-Jageman)", "Estimation statistics: effect sizes with CIs and the plots that show them", "Reports that lead with the difference, not the p"],
                  ["<em>Flexplot</em> (Fife)", "Graphics-first modelling: scatter, paired, interaction plots with fitted models", "Seeing the model before fitting it"],
                  ["<em>jpower</em>", "Power analysis for t-tests and proportions", "Section 10"],
                  ["<em>snowIRT</em>, <em>psychoPDA</em>", "Item response theory", "Section 07"],
                  ["<em>Rj</em>", "An R editor inside jamovi", "The one thing the menus lack"],
                  ["<em>TOSTER</em>", "Equivalence tests", "Showing two things are the same, not merely not different"],
                  ["<em>walrus</em>", "Robust statistics (trimmed means, bootstrapped tests)", "Outlier-heavy data"],
                  ["<em>Distraction</em>", "Distributions: plots and probabilities", "Teaching"]]},
             {"t": "body", "cls": "sm", "html": "Modules &rarr; jamovi library &rarr; Install. "
              "Each appears as a new menu under Analyses. Module versions matter for "
              "reproducibility; note them in the methods."},
         ]},

        {"type": "content", "label": "Mixed Models", "title": "Clustered data: the mixed model in GAMLj",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "Children in 40 schools; the "
                        "programme was assigned by school; children in one school resemble "
                        "each other. Every t-test and regression so far has treated the "
                        "1,200 children as independent and produced intervals that are too "
                        "narrow. <strong>Path</strong>: Linear Models (GAMLj) &rarr; Mixed "
                        "Model; endline as Dependent; baseline as Covariate; arm and grade "
                        "as Factors; school_id as Cluster variable; in Random Effects, add "
                        "the intercept by school. Tick Fixed effects estimates with CI, "
                        "Random components (variance, ICC), Estimated marginal means."},
                       {"t": "table",
                        "head": ["Effect", "Estimate", "SE", "95% CI", "p", "Compare: OLS CI"],
                        "rows": [
                            ["baseline", "0.72", "0.02", "0.68 to 0.76", "&lt; .001", "0.68 to 0.76"],
                            ["arm: Remedial", "6.5", "1.42", "3.6 to 9.4", "&lt; .001", "5.3 to 7.9"],
                            ["Random intercept SD (school)", "4.1", "", "", "", ""],
                            ["Residual SD", "10.6", "", "", "", ""],
                            ["ICC", "0.13", "", "", "", ""]]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading it", "html":
                         "The programme estimate barely changes (6.6 to 6.5); its "
                         "interval doubles in width (5.3&ndash;7.9 to 3.6&ndash;9.4), because "
                         "with 40 schools the effective sample for a school-level "
                         "treatment is 40, not 1,200. The ICC of 0.13 says 13% of the "
                         "variance in endline scores is between schools. This is the "
                         "analysis the design requires, and the interval it gives is the "
                         "one to report."},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. A cluster-"
                         "randomised trial analysed without accounting for clusters is the "
                         "most common statistical error in education evaluations, and the "
                         "module fixes it in one dialog."}]},
         ]},

        {"type": "content", "label": "Mediation", "title": "Mediation in jAMM: membership, savings, decision-making",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Medmod (core) does a simple mediation with a "
                        "bootstrap; <em>jAMM</em> does the general case. Path: jAMM &rarr; "
                        "GLM Mediation Model; decide_score as Dependent; savings_rs as "
                        "Mediator; treatment as Factor; age, educ as Covariates. Tick "
                        "Bootstrap (percentile, 5,000), confidence intervals, the path "
                        "diagram, and the individual regressions. Output: the a, b, "
                        "c&prime; paths, the indirect effect with its bootstrap CI, the "
                        "total effect."},
                       {"t": "table",
                        "head": ["Effect", "Estimate", "95% CI (bootstrap)"],
                        "rows": [
                            ["a: treatment &rarr; savings", "142 Rs", "98 to 186"],
                            ["b: savings &rarr; decide (per 100 Rs)", "0.21", "0.13 to 0.29"],
                            ["Indirect (a &times; b)", "0.30", "0.18 to 0.44"],
                            ["Direct (c&prime;)", "0.60", "0.25 to 0.95"],
                            ["Total", "0.90", "0.56 to 1.24"]]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Illustrative. A third of the total effect runs through the savings path; two-thirds does not. The sentence: 'the association is consistent with partial mediation through savings; the mediator was not randomised.'",
                  "Moderation in the same module: a moderator variable and its interaction with the predictor, with simple slopes at &plusmn;1 SD and a plot.",
                  "Moderated mediation: both, with the conditional indirect effect at levels of the moderator.",
                  "SEM 101, sections 07 and 10, cover what these estimates assume. The module makes them easy to get; it does not make them causal."]},
                        {"t": "hbox", "color": "amber", "html": "Clustering by village is not "
                         "handled in jAMM's bootstrap. For a paper, the SEM in SEMLj or "
                         "lavaan with clustered errors is the version to report."}]},
         ]},

        {"type": "content", "label": "Meta-analysis", "title": "Meta-analysis in MAJOR: pooling published effects",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A dataset with one row per study: effect "
                        "size and its standard error (or means, SDs and ns per arm, or a "
                        "correlation and n, or a log odds ratio and CI; the module accepts "
                        "each). Path: MAJOR &rarr; the entry matching the input type. Tick "
                        "the model (random effects, REML), heterogeneity statistics (Q, "
                        "I&sup2;, &tau;&sup2;), the forest plot, the funnel plot, and "
                        "publication bias tests (Egger's, trim-and-fill, only with ten or "
                        "more studies). Moderators for a meta-regression."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Illustrative: seven SHG studies, pooled SMD on decision-making 0.18, 95% CI 0.09 to 0.27, I&sup2; = 52%, &tau;&sup2; = 0.01, prediction interval &minus;0.05 to 0.41.",
                           "The forest plot is the result; the prediction interval is the honest one.",
                           "Everything in Systematic Reviews 101 section 07 applies, including what the module does not decide: which studies to include and how to extract them."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The module is the "
                        "<em>metafor</em> package with a form on it. A meta-analysis "
                        "that a master's student can run in an afternoon is the right "
                        "scale of ambition for a thesis chapter; the search and screening "
                        "are the weeks of work."}]},
         ]},

        {"type": "content", "label": "SEM Module", "title": "SEMLj: structural equation models with a form or a syntax box",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "SEMLj offers two entries: a syntax interface "
                        "where you type lavaan model syntax into a box, and an interactive "
                        "interface where you define latent variables and paths by dragging. "
                        "Both run lavaan and return the same tables: loadings, paths, "
                        "fit, modification indices, the path diagram, standardised "
                        "estimates, indirect effects if defined, and multigroup analysis "
                        "with constraints for invariance testing. Estimators include ML, "
                        "MLR and WLSMV for ordinal items; missing data by FIML."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The worked SEM in SEM 101, section 07, runs in the syntax box as written there.",
                           "Invariance: the multigroup panel with 'loadings', 'intercepts' or 'thresholds' constrained, compared by fit in the output.",
                           "Bootstrap for indirect effects is a tick; clustering is not supported in the dialog and needs lavaan in Rj."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "For a student who has done "
                        "sections 02 to 07, this module is the route into SEM without "
                        "AMOS, without a licence, and with better estimators than AMOS "
                        "offers."}]},
         ]},

        {"type": "content", "label": "GLM Plots", "title": "Interactions, simple effects and plots in GAMLj",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "GAMLj's General Linear Model is the core "
                        "regression dialog with better defaults for interpretation: "
                        "centred covariates, simple effects and simple slopes on request, "
                        "estimated marginal means at chosen values, and plots of any "
                        "predictor with any moderator on the horizontal axis and separate "
                        "lines, with CIs or raw data. The question 'does the programme "
                        "work better for children who started lower?' is an arm &times; "
                        "baseline interaction, and the plot of endline against baseline "
                        "with one line per arm is its answer."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Illustrative: interaction coefficient &minus;0.06 (95% CI &minus;0.10 to &minus;0.02): the programme's effect is larger for lower baseline scores; simple effects at baseline &minus;1 SD: 9.1 points; at +1 SD: 4.1 points.",
                           "Covariates are centred by default so main effects read at the mean; the option to change this is there.",
                           "Effect sizes (partial &eta;&sup2;, &omega;&sup2;) per term; contrasts of your choosing."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "If you install one module, "
                        "install GAMLj and use its GLM instead of the core regression for "
                        "anything with an interaction or a cluster. The core dialogs are "
                        "for learning; GAMLj is for reports."}]},
         ]},

        {"type": "content", "label": "Rj", "title": "Rj: the escape hatch, with four lines of R",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Need", "Rj code (data is the loaded dataset)"],
                        "rows": [
                            ["Weighted estimate with survey design", "<code>library(survey); d &lt;- svydesign(ids=~psu, strata=~stratum, weights=~wt, data=data); svymean(~decide_score, d)</code>"],
                            ["Cluster-robust standard errors", "<code>library(sandwich); library(lmtest); m &lt;- lm(endline ~ baseline + arm, data); coeftest(m, vcov = vcovCL(m, cluster = data$school_id))</code>"],
                            ["Multiple imputation", "<code>library(mice); imp &lt;- mice(data, m = 20); pool(with(imp, lm(endline ~ baseline + arm)))</code>"],
                            ["Reshape long to wide", "<code>library(tidyr); pivot_wider(data, names_from = wave, values_from = score)</code>"],
                            ["A custom plot", "<code>library(ggplot2); ggplot(data, aes(baseline, endline, colour = arm)) + geom_point(alpha = .3) + geom_smooth(method = \"lm\")</code>"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Each snippet runs inside jamovi on "
                        "the data already loaded, with the output in the results pane "
                        "beside the menu analyses. Packages must be installed in the R that "
                        "jamovi uses (the module's documentation says how). This is not a "
                        "way to avoid learning R; it is a way to learn it four lines at a "
                        "time, for exactly the thing the menu cannot do."},
                        {"t": "hbox", "color": "amber", "html": "The first snippet is the "
                         "answer to section 02's weights problem. It is short. It is still "
                         "code, and it is still required."}]},
         ]},

        # ===================== SECTION 09: BAYESIAN ANALYSIS IN JASP =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Bayesian Analysis in JASP"},

        {"type": "content", "label": "Why Bayes", "title": "The same questions, a different kind of answer",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A p-value is the probability of data at "
                        "least this extreme if there were no effect. It cannot say how "
                        "likely the effect is, cannot support the null, and does not "
                        "accumulate as data arrive. A Bayesian analysis starts from a prior "
                        "distribution over the effect, updates it with the data, and reports "
                        "the posterior: the range of effects now credible, and the Bayes "
                        "factor, which says how much more the data support one hypothesis "
                        "than another. JASP was built to make this as easy as a t-test, and "
                        "in JASP every classical dialog has a Bayesian twin."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "A 95% credible interval means what most people think a confidence interval means: 95% probability the effect lies in it, given the data and the prior.",
                           "A Bayes factor of 8 for the alternative means the data are 8 times more likely under an effect than under none. A Bayes factor of 8 for the null is evidence for no effect, which a p-value can never give.",
                           "Evidence accumulates: analyse as data arrive without the multiple-testing problem of repeated p-values.",
                           "The price: a prior must be chosen and stated, and the result depends on it, usually mildly."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When it earns its place in development work", "html":
                         "Small pilots where 'not significant' would be read as 'does not "
                         "work': the Bayes factor says whether the data favour no effect or "
                         "are simply uninformative. Sequential monitoring of a programme's "
                         "outcomes. Combining a new study with a prior estimate from the "
                         "literature. Reporting to a decision-maker who wants 'how likely "
                         "is it that the effect is at least 5 points', which the posterior "
                         "answers directly and the p-value cannot."},
                        {"t": "hbox", "color": "green", "html": "Van Doorn and colleagues, "
                         "'The JASP guidelines for conducting and reporting a Bayesian "
                         "analysis' (<em>Psychonomic Bulletin &amp; Review</em> 2021, 28:813), "
                         "is the ten-page guide to read first."}]},
         ]},

        {"type": "content", "label": "Bayesian t-test", "title": "The Bayesian independent-samples t-test in JASP",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "cls": "sm", "html": "<strong>Path</strong>: T-Tests &rarr; "
                        "Bayesian Independent Samples T-Test; decide_score as Dependent, "
                        "treatment as Grouping. <strong>Tick</strong>: Bayes factor BF<sub>10</sub>; "
                        "Descriptives; Plots: Prior and posterior with additional info, "
                        "Bayes factor robustness check, Sequential analysis. Prior: the "
                        "default Cauchy with scale 0.707 on the standardised effect size "
                        "(Rouder and colleagues 2009), or a narrower one if you have "
                        "reason to expect a small effect."},
                       {"t": "table",
                        "head": ["", "BF<sub>10</sub>", "Error %", "Median &delta;", "95% credible interval"],
                        "rows": [
                            ["SHG member vs non-member", "4.8 &times; 10<sup>4</sup>", "&lt; 0.001", "0.41", "0.25 to 0.57"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, matching section "
                        "04's classical result (d = 0.42). The data are tens of thousands of "
                        "times more likely under an effect than under none; the effect is "
                        "credibly between a quarter and a half of a standard deviation."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading the plots", "html":
                         "The prior-and-posterior plot shows the prior (wide, centred on "
                         "zero) and the posterior (narrow, centred on 0.41); the two dots "
                         "at zero are the Savage-Dickey ratio that is the Bayes factor. The "
                         "robustness plot shows BF<sub>10</sub> across prior widths: if it "
                         "stays large from a narrow to a wide prior, the conclusion does "
                         "not depend on the prior. The sequential plot shows the Bayes "
                         "factor as cases accumulate; here it crosses 100 by about n = "
                         "200."},
                        {"t": "hbox", "color": "amber", "html": "The sentence: 'The data "
                         "provided extreme evidence for a difference (BF<sub>10</sub> = "
                         "4.8 &times; 10<sup>4</sup>); the posterior median effect size was "
                         "0.41 (95% CI 0.25 to 0.57), robust across prior widths.'"}]},
         ]},

        {"type": "content", "label": "Bayes Factors", "title": "Reading Bayes factors: the scale, the direction, and the null",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["BF<sub>10</sub>", "Evidence for H<sub>1</sub> (an effect)", "BF<sub>01</sub> = 1/BF<sub>10</sub>", "Evidence for H<sub>0</sub> (no effect)"],
                        "rows": [
                            ["1", "None; the data do not distinguish", "1", "None"],
                            ["1 to 3", "Anecdotal", "1 to 3", "Anecdotal"],
                            ["3 to 10", "Moderate", "3 to 10", "Moderate"],
                            ["10 to 30", "Strong", "10 to 30", "Strong"],
                            ["30 to 100", "Very strong", "30 to 100", "Very strong"],
                            ["Above 100", "Extreme", "Above 100", "Extreme"]]},
                       {"t": "body", "cls": "sm", "html": "The Lee and Wagenmakers (2013) "
                        "adaptation of Jeffreys's labels. They are conventions for "
                        "description, not thresholds for decision; a BF of 2.9 and one of "
                        "3.1 are the same evidence."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "BF<sub>10</sub> is H<sub>1</sub> over H<sub>0</sub>; BF<sub>01</sub> the reverse. JASP lets you choose which to display; state which you report.",
                  "The Bayes factor compares two specific hypotheses under specific priors. A BF for 'an effect of any size' differs from one for 'a positive effect' (one-sided, a tick-box) and from one under a narrow prior.",
                  "Evidence for the null is the distinctive gift: illustrative, attendance by arm, BF<sub>01</sub> = 4.2, moderate evidence that attendance did not differ. A p of .07 could not have said that.",
                  "Bayes factors and credible intervals answer different questions (is there an effect; how big is it) and both should be reported."]},
                        {"t": "hbox", "color": "amber", "html": "'BF<sub>10</sub> = 1.4' means "
                         "the study was too small to tell. Say that, rather than 'no "
                         "significant effect'."}]},
         ]},

        {"type": "content", "label": "Bayesian Models", "title": "Bayesian ANOVA, regression and correlation in JASP",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "ANOVA &rarr; Bayesian ANOVA compares all "
                        "models built from the factors (null, arm, sex, arm + sex, arm + sex "
                        "+ interaction) and reports each model's Bayes factor against the "
                        "null and the inclusion Bayes factor for each effect, averaging over "
                        "models. Regression &rarr; Bayesian Linear Regression does the same "
                        "over all subsets of predictors and gives posterior inclusion "
                        "probabilities and model-averaged coefficients with credible "
                        "intervals. Regression &rarr; Bayesian Correlation Matrix gives "
                        "Bayes factors and posteriors for each correlation."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Illustrative Bayesian ANOVA: inclusion BF for arm above 10<sup>6</sup>; for sex 0.6; for the interaction 0.2. The data favour leaving the interaction out, which is more informative than 'p = .44'.",
                           "Bayesian regression's model averaging is a principled answer to 'which predictors matter' that stepwise regression pretends to give.",
                           "Frequencies &rarr; Bayesian Contingency Tables gives a Bayes factor for association and a posterior for the odds ratio."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What is not in the menus", "html":
                         "Custom priors from a previous study (informed priors) are "
                         "possible in the t-test and regression dialogs but limited; "
                         "hierarchical models with random effects for schools are in the "
                         "Bayesian Mixed Models entry in recent versions and need long "
                         "sampling; anything beyond that is <em>brms</em> in R. The "
                         "menus cover the standard analyses in Bayesian form and that is "
                         "most of what a thesis needs."},
                        {"t": "hbox", "color": "green", "html": "Run the classical and "
                         "Bayesian versions side by side for the primary outcome. When "
                         "they agree, say so; when they differ, the Bayes factor is usually "
                         "telling you the evidence was weaker than the p-value implied."}]},
         ]},

        {"type": "content", "label": "Priors", "title": "Priors: what the defaults are, and when to change them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "JASP's default priors are designed to be "
                        "reasonable for psychology's effect sizes: a Cauchy on the "
                        "standardised effect with scale 0.707 for t-tests, a multivariate "
                        "Cauchy for ANOVA fixed effects, a JZS prior for regression. They "
                        "put substantial weight on medium and large effects. Field "
                        "programmes' effects are typically small (0.1 to 0.3 SD), and a "
                        "default prior that expects larger effects can produce a Bayes "
                        "factor mildly favouring the null when the true effect is small "
                        "and the sample modest."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "State the prior in the methods every time: 'Cauchy prior on effect size, scale 0.707 (JASP default)'.",
                           "For a field evaluation, consider scale 0.5 or a one-sided prior if only a positive effect is plausible, and report the robustness plot.",
                           "An informed prior from a meta-analysis (a normal centred on the pooled SMD with its SD) is legitimate and powerful, and must be stated and justified.",
                           "Never choose the prior after seeing which one gives the answer you want. The robustness check exists to show that you did not."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Estimation without Bayes factors", "html":
                         "If the question is 'how big', not 'whether', the posterior "
                         "distribution and its credible interval are the answer and the "
                         "Bayes factor can be left aside. With a wide prior and a decent "
                         "sample, the credible interval is nearly the confidence interval "
                         "with the interpretation people wanted all along. That is the "
                         "gentlest use of Bayesian methods and often the most useful."},
                        {"t": "hbox", "color": "green", "html": "Kruschke's <em>Doing Bayesian "
                         "Data Analysis</em> (2nd ed., Academic Press, 2015) is the "
                         "estimation-first text; JASP's Learn Bayes module teaches the "
                         "ideas interactively."}]},
         ]},

        {"type": "content", "label": "Bayes Report", "title": "Reporting a Bayesian analysis: the van Doorn checklist, condensed",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Element", "Report"],
              "rows": [
                  ["Hypotheses", "What H<sub>0</sub> and H<sub>1</sub> are, and whether one- or two-sided"],
                  ["Prior", "The distribution and its parameters for every tested effect, and why (default, informed from a source, or chosen for the expected effect size)"],
                  ["Software", "JASP version and the R package underneath (<em>BayesFactor</em>)"],
                  ["Bayes factor", "BF<sub>10</sub> or BF<sub>01</sub>, stated; the numerical error percentage if sampling was used"],
                  ["Posterior", "Median or mean of the effect size, the 95% credible interval, and the plot"],
                  ["Robustness", "The Bayes factor across prior widths (the plot or its range)"],
                  ["Sequential", "If data were analysed as they arrived, the sequential plot"],
                  ["Interpretation", "Evidence described with the conventional labels, without treating them as thresholds; the null supported where the BF supports it"],
                  ["Classical companion", "The frequentist result alongside, where readers expect it"]]},
             {"t": "body", "cls": "sm", "html": "Van Doorn and colleagues (2021) give the "
              "full list and worked examples. A Bayesian analysis reported without its "
              "prior is unreviewable; with it, it is more transparent than the classical "
              "version, because the assumption is on the page."},
         ]},

        {"type": "content", "label": "jamovi's Bayes", "title": "The same analyses in jamovi: the jsq module",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The <em>jsq</em> module ports JASP's Bayesian "
                        "t-tests, ANOVA, regression, correlation and contingency tables into "
                        "jamovi, with the same priors, Bayes factors, posterior plots and "
                        "robustness checks. Install it from the library and the Bayesian "
                        "entries appear beside the classical ones. The results are the same "
                        "<em>BayesFactor</em> package's; the interface is jamovi's, so the "
                        "data-cleaning tools of section 02 and the modules of section 08 "
                        "are in the same window."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Use JASP when the Bayesian analysis is the main event and you want the fuller dialogs, the Learn Bayes module and the newest methods.",
                           "Use jamovi with jsq when the Bayesian result is a companion to a classical workflow already in jamovi.",
                           "Either way, the reporting checklist is the same."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "A student who can run a "
                        "t-test, read a Bayes factor and a credible interval, and state a "
                        "prior has more statistical literacy than most published applied "
                        "papers show. It takes an afternoon in JASP."}]},
         ]},

        # ===================== SECTION 10: EFFECT SIZES, POWER AND REPORTING =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Effect Sizes, Power and Reporting"},

        {"type": "content", "label": "Effect Sizes", "title": "Effect sizes: which one, and what it means in your units",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Analysis", "Effect size (tick-box)", "Reads as", "Convention, and its limits"],
              "rows": [
                  ["Independent t", "Cohen's d (also Hedges' g, Glass's &Delta;)", "Difference in SD units", "0.2 / 0.5 / 0.8 small / medium / large (Cohen 1988); in education Kraft (2020) argues 0.05 / 0.20 as the meaningful boundaries"],
                  ["Paired t", "Cohen's d (paired)", "Mean change over the SD of changes", "Not comparable to the independent d; say which"],
                  ["ANOVA", "&omega;&sup2; (preferred), &eta;&sup2;, partial &eta;&sup2;", "Share of variance explained by the factor", "0.01 / 0.06 / 0.14; partial &eta;&sup2; is inflated in multi-factor designs"],
                  ["Correlation", "r", "Strength of linear association", "0.1 / 0.3 / 0.5"],
                  ["Regression", "Unstandardised B in outcome units; standardised &beta;; R&sup2;, &Delta;R&sup2;", "B is the one a reader can use", "&beta; for comparison within a model only"],
                  ["Contingency table", "Percentage-point difference; risk ratio; odds ratio; Cramer's V", "Points for policy; RR for comparison; V for strength", "V: 0.1 / 0.3 / 0.5; OR overstates RR when outcomes are common"],
                  ["Non-parametric", "Rank-biserial r; &epsilon;&sup2;", "Probability-based difference", "As for r"],
                  ["Logistic", "Odds ratio; predicted probability difference", "Points, again", "Give the probabilities"]]},
             {"t": "body", "cls": "sm", "html": "Every dialog in this course has an effect "
              "size tick-box and every result in a report should carry one. The unit that "
              "matters is the outcome's own: 6.6 reading points, 13 percentage points, "
              "Rs 150 a month. The standardised version is for comparison across studies "
              "and goes second."},
         ]},

        {"type": "content", "label": "Interpreting Size", "title": "How big is big? Benchmarks against the setting, not Cohen",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Cohen's benchmarks came from psychology "
                        "experiments in the 1960s and 1970s and he warned against using "
                        "them outside that context. In education, Kraft (<em>Educational "
                        "Researcher</em> 2020, 49:241) reviewed hundreds of interventions "
                        "and found the median effect on achievement was about 0.1 SD; a "
                        "0.2 SD effect from a cheap, scalable programme is large. In "
                        "development economics, cash-transfer effects on school enrolment of "
                        "a few percentage points are policy-relevant. The benchmark is what "
                        "comparable programmes achieve, at what cost, for whom."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Translate the SD effect into the outcome's units and into something concrete: 0.4 SD on reading is 6.6 points, about a third of a year's typical growth in this sample.",
                           "Compare with the literature's effects for similar programmes; Systematic Reviews 101 is how to find them.",
                           "Divide by cost where cost is known: points per Rs 1,000 per child.",
                           "Report the CI's lower bound as the conservative reading: 'at least 5 points'."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "'A medium effect (d = 0.42)' "
                        "tells a programme officer nothing. '0.9 points on a 10-point "
                        "decision-making scale, about a fifth of the gap between women "
                        "with no schooling and those with secondary schooling' tells "
                        "them something."}]},
         ]},

        {"type": "content", "label": "Power", "title": "Power analysis before the study: jpower and the cluster problem",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The <em>jpower</em> module (or G*Power, free, "
                        "Faul and colleagues, <em>Behavior Research Methods</em> 2007, "
                        "39:175) answers: how many respondents to detect an effect of size d "
                        "with 80% power at &alpha; = 0.05? For an independent t-test with "
                        "d = 0.3, about 176 per group; d = 0.2, about 394 per group; "
                        "d = 0.5, 64 per group. Enter the smallest effect that would "
                        "matter, not the effect you hope for. jpower also gives the power "
                        "curve and the effect detectable with the sample you can afford."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "For proportions: jpower's two-proportion entry; a 10-point difference from 50% needs about 390 per group.",
                           "For regression and ANOVA: G*Power's f&sup2; and f entries; Impact Evaluation 101 covers the formulas.",
                           "After the study, do not compute 'observed power'; it is a function of the p-value and adds nothing. Report the CI."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Clustered designs", "html":
                         "When schools or villages are the unit of assignment, the "
                         "effective sample is far smaller than the number of children. The "
                         "design effect is 1 + (m &minus; 1) &times; ICC: with 30 children per "
                         "school and ICC 0.13, it is 4.8, so 1,200 children carry the "
                         "information of 250. Neither jpower nor G*Power handles this in "
                         "its basic dialogs; multiply the required n by the design effect, "
                         "or use a cluster-RCT calculator (the <em>PowerUpR</em> package, "
                         "or Optimal Design). Forty schools of thirty is a modest trial "
                         "for an effect of 0.2 SD."},
                        {"t": "hbox", "color": "green", "html": "Power is decided before "
                         "data collection. The number to put in the proposal is the one "
                         "that comes out of this slide."}]},
         ]},

        {"type": "content", "label": "Intervals", "title": "Confidence intervals: reading them, drawing them, leading with them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A 95% confidence interval is the range of "
                        "effects compatible with the data at the conventional level; across "
                        "many studies, 95% of such intervals contain the true value. Its "
                        "width is the precision; its position is the estimate; whether it "
                        "crosses zero is the significance test, read at a glance. It "
                        "answers 'how big, and how sure' where the p-value answers only "
                        "'whether'. Every dialog in jamovi and JASP offers it as a tick-box "
                        "and every reported estimate should carry it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "'6.5 points (95% CI 3.6 to 9.4)': the effect is very probably between a modest and a large one; the study cannot pin it closer.",
                           "'1.2 points (95% CI &minus;0.1 to 2.5)': a small positive effect is plausible and so is none; the study was not large enough to decide.",
                           "Two intervals that overlap can still differ significantly; test the difference, do not eyeball the overlap.",
                           "A wide interval is a finding about the study's size, and the report says so."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Drawing them", "html":
                         "The descriptives plot in the t-test and ANOVA dialogs draws group "
                         "means with CIs; the estimated marginal means plot draws adjusted "
                         "means with CIs; the <em>esci</em> module draws the difference "
                         "itself with its interval on a separate axis, which is the figure "
                         "Cumming and Calin-Jageman recommend. A forest-style plot of all "
                         "secondary outcomes' effects with CIs, one row each, is the single "
                         "most informative figure an evaluation report can contain, and "
                         "<em>esci</em> or the MAJOR module's forest plot will draw it from "
                         "a small table of estimates."},
                        {"t": "hbox", "color": "green", "html": "Lead with the interval. The "
                         "p-value is derivable from it; the reverse is not true."}]},
         ]},

        {"type": "content", "label": "Multiple Testing", "title": "Many outcomes, many subgroups: keeping the false-positive rate honest",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Twenty tests at &alpha; = 0.05 on outcomes "
                        "with no true effect produce one significant result on average. An "
                        "evaluation with eight outcomes and five subgroups has forty tests. "
                        "The fixes: declare a primary outcome and treat the rest as "
                        "secondary; correct the p-values within a family (Bonferroni is "
                        "conservative, Holm is better and equally simple, Benjamini-"
                        "Hochberg controls the false discovery rate); or pre-register the "
                        "tests so a reader can count them."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "jamovi's post hoc dialogs offer Tukey, Scheff&eacute;, Bonferroni and Holm corrections as tick-boxes; use Holm.",
                           "For a set of outcomes, compute the Holm-adjusted p-values by hand (rank the p-values, multiply the smallest by k, the next by k &minus; 1, ...) or in Rj with <code>p.adjust</code>.",
                           "Subgroup findings not pre-specified are exploratory; say so in the sentence that reports them.",
                           "A 'significant' effect in one subgroup and not another is not evidence of a difference between them; test the interaction."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The honest evaluation "
                        "report has one primary result with an interval, a table of "
                        "secondary results with adjusted p-values or an explicit count, "
                        "and an exploratory section labelled as such. The dishonest one "
                        "has twelve bullet points, each significant, and no count."}]},
         ]},

        {"type": "content", "label": "Misreadings", "title": "The five misreadings that a menu makes easy",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Misreading", "Why it happens", "The correction"],
              "rows": [
                  ["p &lt; .001 means a big effect", "The dialog shows p first and largest", "p depends on n; the effect size is separate and must be reported"],
                  ["p = .07 means no effect", "'Not significant' reads as 'nothing'", "The CI shows what effects remain plausible; a Bayes factor may say the data were uninformative"],
                  ["Significant in the treatment arm, not in control, so the programme worked", "Two paired tests instead of one comparison", "Test the difference between arms; section 04"],
                  ["Controlled for it, so it is not confounding", "Regression dialogs make adjustment feel like proof", "Adjustment handles measured confounders in the form entered; unmeasured ones remain; causal claims need a design"],
                  ["The model fits (R&sup2; = 0.55), so the coefficients are causal", "Fit and causation look alike in a table", "R&sup2; is prediction; the arm coefficient is causal only because arm was randomised"]]},
             {"t": "body", "cls": "sm", "html": "None of these is a software problem, and "
              "all of them are more common in menu-driven work because the menu removes "
              "the moment of choice where a person writing code would have to think. The "
              "cure is the sentence: write the result in words before reading the p-value."},
         ]},

        {"type": "content", "label": "Reproducibility", "title": "Making menu work reproducible: the .omv file, annotations and syntax",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The .omv file holds the data, every "
                        "analysis, every option and every result, and reopens identically on "
                        "any machine with jamovi. Add annotations (Edit tab, or click above "
                        "any result) saying what each analysis is for and what you concluded. "
                        "Turn on syntax mode and the R call sits above each result. Together "
                        "these make a menu analysis as reproducible as a script, provided "
                        "the file is shared."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Keep one .omv per project, analyses in the order of the report, annotated. Delete exploratory dead ends or move them to a second file.",
                           "Record the jamovi version and every module's version in the first annotation; module updates change defaults.",
                           "Export the syntax of every reported analysis to a text file as an appendix.",
                           "Deposit the .omv with the data on OSF or Zenodo when the report is published; a reader with jamovi can check every table."]}],
              "right": [{"t": "panel", "color": "amber", "title": "JASP", "html":
                         "The .jasp file does the same; annotations are added by clicking "
                         "the result titles; the file can be exported as HTML or PDF with "
                         "all tables and plots; and the JASP team's own guidelines ask for "
                         "the .jasp file to be shared with a paper. The Open Science "
                         "Framework has a JASP integration that stores it directly."},
                        {"t": "hbox", "color": "green", "html": "A reviewer who can open your "
                         "file and see the analysis is a reviewer who trusts the table. "
                         "That is the whole case for saving and sharing it."}]},
         ]},

        {"type": "content", "label": "Export", "title": "Getting results out: tables, plots and the report",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Output", "How", "Note"],
              "rows": [
                  ["A table to Word", "Right-click the table &rarr; Copy; paste into Word", "Pastes as a real table; the number format (three-dots menu) is applied"],
                  ["A table to LaTeX", "Right-click &rarr; Export &rarr; LaTeX (JASP); copy as HTML and convert (jamovi)", "JASP's is cleaner"],
                  ["A plot", "Right-click the plot &rarr; Export &rarr; PDF, SVG, EPS or PNG", "SVG or PDF for print; PNG at 300 dpi for Word"],
                  ["All results", "Menu &rarr; Export &rarr; HTML or PDF", "The whole results pane as a document; useful for an appendix or a supervisor"],
                  ["The data with computed variables", "Menu &rarr; Export &rarr; CSV", "For use in R or Stata; filters are applied if 'filtered rows' is chosen"],
                  ["The syntax", "Syntax mode on; select and copy", "Into the methods appendix"],
                  ["APA formatting", "JASP tables are APA by default; jamovi's are close", "Round to two decimals in the report; p to three, or '&lt; .001'"]]},
             {"t": "body", "cls": "sm", "html": "The report is written in a word processor; "
              "the numbers come from the software by copy, never by retyping. Retyped "
              "numbers are the source of the mismatches between tables and text that "
              "referees find."},
         ]},

        {"type": "content", "label": "Report Structure", "title": "The results section of an evaluation report, from jamovi output",
         "blocks": [
             {"t": "flow", "steps": [
                 "SAMPLE: Table 1 by arm (Descriptives); attrition table (Contingency, t-tests)",
                 "PRIMARY OUTCOME: ANCOVA or mixed model estimate with CI and effect size; the descriptives plot",
                 "SECONDARY OUTCOMES: one table, same columns, adjusted p-values or a count",
                 "MECHANISM AND HETEROGENEITY: pre-specified interaction or mediation, labelled; exploratory ones labelled",
                 "SCALES: reliability and structure, in the methods or an appendix",
                 "ROBUSTNESS: with and without outliers; non-parametric companion; clustered version",
                 "LIMITATIONS: clustering if not modelled; attrition; measurement; the verbs used"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Every step maps to a dialog in this course, "
                        "and the whole sequence for an evaluation of this size takes a "
                        "competent analyst two days in jamovi, of which the first is data "
                        "checking. Academic Writing 101 covers the prose around it."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Lead with the primary outcome's "
                        "estimate and interval, in units. Everything else supports that "
                        "sentence."}]},
         ]},

        {"type": "content", "label": "Worked Report", "title": "A worked results paragraph, assembled from the course's outputs",
         "blocks": [
             {"t": "panel", "color": "cyan", "title": "Illustrative", "html":
              "'Of 1,280 children enrolled at baseline in 40 schools, 1,200 (93.8%) were "
              "assessed at endline, with equal attrition by arm; children lost to follow-up "
              "had lower baseline scores in both arms (Table 2). Arms were balanced at "
              "baseline (Table 1). Adjusting for baseline score and grade, and accounting "
              "for clustering by school, children in the remedial arm scored 6.5 points "
              "higher on the 100-point reading assessment at endline (95% CI 3.6 to 9.4, "
              "p &lt; .001; ICC = 0.13), about 0.4 SD of the baseline distribution and a third "
              "of the typical annual gain in this sample. The share reading a full paragraph "
              "rose from 49% to 62% (difference 13 points, 95% CI 7 to 18). The effect was "
              "larger for children with lower baseline scores (interaction p = .004; 9.1 "
              "points at one SD below the baseline mean, 4.1 at one SD above) and did not "
              "differ by sex (interaction p = .44). Attendance did not differ by arm "
              "(1.2 points, 95% CI &minus;0.1 to 2.5; Bayesian BF<sub>01</sub> = 4.2, moderate "
              "evidence of no difference). Results were similar in the unadjusted analysis "
              "and with the ten influential cases removed (Appendix Table A3). All analyses "
              "were conducted in jamovi 2.6 with the GAMLj module; the analysis file is "
              "deposited at [repository].'"},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Every number came from a dialog "
                        "in sections 02 to 09. The paragraph reports the estimate before the "
                        "test, the unit before the SD, the cluster-adjusted interval, the "
                        "pre-specified interaction and its plot, the null finding as a "
                        "finding, and the file location."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Read it against the "
                        "misreadings slide. None of the five is in it."}]},
         ]},

        {"type": "content", "label": "Reporting Checklist", "title": "Before you submit: the statistics checklist",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Every result", "Done"],
                        "rows": [
                            ["Estimate in the outcome's units, with a 95% CI", ""],
                            ["The test statistic, df and exact p (or '&lt; .001')", ""],
                            ["An effect size, named", ""],
                            ["n for that analysis (after missing and filters)", ""],
                            ["Assumption checks mentioned, and the choice they led to", ""],
                            ["Direction and magnitude in words a non-statistician can use", ""]]}],
              "right": [{"t": "table",
                         "head": ["The report", "Done"],
                         "rows": [
                             ["Primary outcome declared; secondary outcomes counted or adjusted", ""],
                             ["Clustering handled or acknowledged", ""],
                             ["Attrition table by arm", ""],
                             ["Scales' reliability and structure reported", ""],
                             ["Exploratory analyses labelled", ""],
                             ["Causal verbs only where the design supports them", ""],
                             ["Software and module versions; the .omv or .jasp file deposited", ""],
                             ["Numbers copied, never retyped; text matches tables", ""]]},
                        {"t": "hbox", "color": "cyan", "html": "Fourteen lines, and the "
                         "difference between an NGO report a funder can act on and one "
                         "they cannot."}]},
         ]},

        # ===================== SECTION 11: CHOOSING TOOLS, TEACHING AND PRACTICE =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Choosing Tools, Teaching and Practice"},

        {"type": "content", "label": "The Tools", "title": "The point-and-click field: what each tool is for",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Best at", "Weak at"],
              "rows": [
                  ["jamovi", "Free, open", "Data cleaning in place, the standard analyses with effect sizes, modules for mixed models, SEM, meta-analysis, IRT; syntax mode", "Survey weights; long-to-wide reshaping; dates"],
                  ["JASP", "Free, open", "Bayesian analyses, APA tables, the Learn Bayes module, SEM and meta-analysis modules, a plot builder and an AI assistant in recent versions", "Data editing (improving); survey weights"],
                  ["gretl", "Free, open", "Econometrics: time series, panels, instrumental variables, with menus", "Psychometrics; plots are dated"],
                  ["PSPP", "Free, open", "An SPSS clone for those who must match SPSS output", "Few effect sizes; little development"],
                  ["BlueSky Statistics; R Commander", "Free (BlueSky has a paid tier)", "R with menus; BlueSky is broad and generates R code", "Smaller communities"],
                  ["Excel and Google Sheets", "Free or licensed", "Descriptives, pivot tables, quick plots, the Analysis ToolPak's t-tests and regression", "Everything else; no assumption checks; errors travel silently"],
                  ["SPSS", "Licence, expensive", "The institutional default; broad; good documentation", "Cost; no omega, CFA or parallel analysis without add-ons; syntax is its own language"],
                  ["Stata", "Licence", "Survey weights, panels, econometrics; menus plus a command line worth learning", "Cost; weaker psychometrics and plots than R"],
                  ["R with RStudio", "Free, open", "Everything, reproducibly", "Not point-and-click; the learning curve is the cost"]]},
             {"t": "body", "cls": "sm", "html": "For a department: jamovi as the teaching tool "
              "and R as the destination. For an NGO: jamovi for evaluation analysis, with "
              "Rj or a colleague in R for weighted surveys. For an econometrics course: "
              "gretl beside jamovi. SPSS is not needed for anything in this course."},
         ]},

        {"type": "content", "label": "When to Move On", "title": "When the menu is not enough: the signs, and the next tool",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Sign", "Why the menu fails", "Next tool"],
              "rows": [
                  ["The survey has weights, strata and clusters", "No design support", "R <em>survey</em> (via Rj or RStudio); Stata <em>svy</em>"],
                  ["The same cleaning must be done to twenty files", "Menus do it once", "R or Python scripts; Data Analysis 101"],
                  ["Panel data with fixed effects and clustered errors", "GAMLj can approximate; the standard tools are elsewhere", "Stata <em>xtreg</em>; R <em>fixest</em>; gretl"],
                  ["Difference-in-differences with staggered adoption", "Not in any module", "R <em>did</em>, <em>fixest</em>; Impact Evaluation 101"],
                  ["Time series", "Not in jamovi or JASP", "gretl; R <em>forecast</em>; Time Series 101"],
                  ["Multiple imputation", "Rj only", "R <em>mice</em>"],
                  ["Custom or publication-quality figures", "Fixed plot options", "R <em>ggplot2</em>; Data Visualization 101"],
                  ["A reviewer asks for the code", "A menu sequence is not code", "Syntax mode exported; or redo in R"],
                  ["Text, images, networks", "No dialogs", "R or Python"]]},
             {"t": "body", "cls": "sm", "html": "None of these is a reason not to start in "
              "jamovi. Each is a reason the next course exists. The syntax mode is the "
              "bridge, and the analyst who has run every analysis in this course and read "
              "the R behind it has done the first month of an R course already."},
         ]},

        {"type": "content", "label": "Teaching", "title": "Teaching with jamovi: a twelve-week sequence for a methods course",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Week", "Topic", "jamovi", "Assessment"],
              "rows": [
                  ["1", "Data: types, levels, cleaning, the checklist", "Setup, Compute, Filters", "A cleaned file with a data log"],
                  ["2", "Describing: distributions and plots", "Descriptives, all plots", "Table 1 and three plots from a supplied survey"],
                  ["3", "Comparing two groups; effect sizes", "Independent and paired t-tests", "A comparison with CI, d and a sentence"],
                  ["4", "Several groups; assumptions", "One-way ANOVA, post hoc, non-parametric", "An ANOVA with post hoc and a plot"],
                  ["5", "Factorial designs and interactions", "ANOVA with two factors; marginal means", "An interaction plot and its reading"],
                  ["6", "Correlation and simple regression", "Correlation matrix, linear regression", "A regression table with diagnostics"],
                  ["7", "Multiple regression and ANCOVA", "Model builder, factors, marginal means", "The three-column regression table"],
                  ["8", "Categorical outcomes", "Contingency tables, logistic regression", "A crosstab and a logistic model with probabilities"],
                  ["9", "Scales", "Reliability, EFA, CFA", "A scale validation paragraph"],
                  ["10", "Clustered data and mediation", "GAMLj mixed model; jAMM", "A mixed model with ICC"],
                  ["11", "Bayesian inference", "JASP t-test and ANOVA", "A Bayes factor with prior stated"],
                  ["12", "Reporting, reproducibility, and the edge", "Annotations, syntax, export, Rj", "A full results section from a supplied dataset, with the .omv file"]]},
             {"t": "body", "cls": "sm", "html": "Every week's assessment is a piece of a "
              "report; week 12's is the report. The sequence matches Navarro and "
              "Foxcroft's chapters and the sections of this course, and it installs on a "
              "classroom of mixed laptops in the first ten minutes of week 1."},
         ]},

        {"type": "content", "label": "Institutions", "title": "Adopting jamovi in a department or an organisation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Install</strong>: one download per machine, no licence server, no activation, works offline. The 'solid' release for teaching; 'current' for new features.",
                  "<strong>Lab machines</strong>: install once; modules install per user profile from the library, which needs internet the first time. Pre-install the five modules used in the course.",
                  "<strong>jamovi Cloud</strong>: a browser version for students without laptops; check the current free tier and data-privacy terms before putting participant data on it.",
                  "<strong>Data protection</strong>: files stay on the machine; nothing is uploaded unless the cloud version is used. For sensitive survey data this is the argument for the desktop version.",
                  "<strong>Version control</strong>: fix the version for a course or a project and note it; a mid-semester update that changes a default confuses everyone."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The SPSS conversation", "html":
                         "An institution paying for SPSS licences it uses for t-tests and "
                         "regressions is paying for nothing this course does not provide. "
                         "The transition costs are the teaching materials (Navarro and "
                         "Foxcroft is free and complete) and the habit. The gains are the "
                         "licence, the effect sizes and assumption checks that SPSS hides "
                         "behind extra dialogs, omega and CFA and parallel analysis without "
                         "add-ons, and students who leave with a tool they can keep."},
                        {"t": "hbox", "color": "green", "html": "The strongest argument is "
                         "the last one. A graduate who learned SPSS at a university that "
                         "paid for it loses the tool on graduation. One who learned jamovi "
                         "does not."}]},
         ]},

        {"type": "content", "label": "Worked Study", "title": "A worked study, dialog by dialog: the SHG evaluation from CSV to report",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "Dialog", "Output", "Section"],
                        "rows": [
                            ["Import and set up", "Open; Setup for 15 variables; missing codes 999", "Typed, labelled data", "02"],
                            ["Check", "Descriptives with min/max/missing; Filters for implausible savings; frequency tables", "Data log; 6 cases filtered with reasons", "02"],
                            ["Scores", "Compute: decide_score = MEAN(d1..d5); log_savings", "Two new variables with formulas", "02"],
                            ["Scale", "Reliability; CFA split by language", "&omega; = 0.80; structure holds; d3 differs by language", "07"],
                            ["Table 1", "Descriptives split by treatment; frequency tables", "Balance table", "03"],
                            ["Primary outcome", "GAMLj mixed model: decide_score ~ treatment + age + educ + (1 | village)", "Effect 0.85, 95% CI 0.42 to 1.28; ICC 0.09", "08"],
                            ["Secondary", "Mixed model on log_savings; logistic on income_own", "Two more rows, same columns", "05, 06, 08"],
                            ["Mechanism", "jAMM mediation through savings", "Indirect 0.30, CI 0.18 to 0.44, labelled consistent-with", "08"],
                            ["Heterogeneity", "GAMLj interaction treatment &times; income_own, pre-specified", "Interaction p = .21; no evidence", "08"],
                            ["Bayesian companion", "JASP Bayesian t-test", "BF<sub>10</sub> extreme; posterior d 0.41", "09"],
                            ["Report", "Copy tables; export plots; annotate; syntax to appendix; deposit .omv", "Results section and file", "10"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative numbers. Eleven "
                        "steps, no code except the optional weighted check in Rj, and every "
                        "output a reviewer can reopen. The cluster-adjusted primary estimate "
                        "(0.85, CI 0.42 to 1.28) is smaller and less precise than the naive "
                        "t-test's (0.90, CI 0.56 to 1.24), and it is the honest one."},
                        {"t": "hbox", "color": "amber", "html": "Two days for an analyst who "
                         "knows the course; a week for one learning it. Both produce a "
                         "report that a funder's methods reviewer will accept."}]},
         ]},

        {"type": "content", "label": "Pitfalls", "title": "The dozen errors that menu analyses make easy",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Error", "Section", "Fix in one line"],
              "rows": [
                  ["Analysing a weighted survey unweighted", "02", "R <em>survey</em> via Rj; say what is unweighted"],
                  ["Wrong variable types (a code averaged, a number as text)", "02", "Set every type on import"],
                  ["Deleting rows instead of filtering", "02", "Filters, with notes"],
                  ["Paired t-test on one arm as the programme effect", "04", "Compare arms: change-score t or ANCOVA"],
                  ["p-values on a balance table", "03", "Descriptives only"],
                  ["Ignoring clustering", "04, 08", "GAMLj mixed model"],
                  ["Odds ratio reported as relative risk", "06", "Give probabilities and the RR"],
                  ["Item deletion by 'alpha if dropped'", "07", "Look at the item; keep it unless there is a reason"],
                  ["Twelve outcomes, no correction, no primary", "10", "Declare a primary; Holm; count the tests"],
                  ["Non-significant read as no effect", "10", "The CI; a Bayes factor"],
                  ["Retyped numbers", "10", "Copy tables"],
                  ["No file shared", "10", "Deposit the .omv"]]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "What it covers", "Notes"],
              "rows": [
                  ["Navarro and Foxcroft, <em>Learning Statistics with jamovi</em> (2019)", "The whole of sections 02 to 07, as a textbook with the dialogs", "Free at learnstatswithjamovi.com; the companion to this course"],
                  ["jamovi user guide and the module documentation (jamovi.org)", "Every dialog; GAMLj, jAMM and SEMLj have their own sites with worked examples", "Free"],
                  ["Van Doorn et al., <em>Psychon Bull Rev</em> 2021, 28:813", "Conducting and reporting a Bayesian analysis in JASP", "Section 09; ten pages"],
                  ["Cumming and Calin-Jageman, <em>Introduction to the New Statistics</em> (2nd ed., Routledge, 2024)", "Estimation, effect sizes and CIs, with the esci module", "Sections 04 and 10"],
                  ["Lakens, <em>Improving Your Statistical Inferences</em> (free online course and book)", "p-values, power, effect sizes, equivalence tests, pre-registration", "The clearest treatment of section 10's material"],
                  ["Kraft, <em>Educational Researcher</em> 2020, 49:241", "Interpreting effect sizes in education", "Section 10"],
                  ["Kruschke, <em>Doing Bayesian Data Analysis</em> (2nd ed., Academic Press, 2015)", "Bayesian estimation from first principles", "For those who want more than section 09"],
                  ["Datalab.cc's jamovi video series (Barton Poulson)", "Screen-by-screen walkthroughs", "Free; good for a first week"],
                  ["ImpactMojo: Data Analysis 101, Bivariate Analysis 101, Multivariate Analysis 101, Econometrics 101, Impact Evaluation 101, SEM 101", "The statistics behind each dialog, and the designs that make coefficients causal", "impactmojo.in/101-courses/"]]},
         ]},

        {"type": "content", "label": "Summary", "title": "What to remember",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "jamovi and JASP are free, open, correct, and enough for a thesis or an evaluation report. SPSS is not required.",
                  "Set every variable's type and labels on import; filter, never delete; compute scores with a stated missing rule.",
                  "Plot every outcome before testing it. The plot chooses the test.",
                  "The estimate and its interval come first, in the outcome's units; the p-value second; the effect size named.",
                  "Compare arms, not before-and-after within one arm."]}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "Children in schools and women in villages are clustered; the GAMLj mixed model is one dialog and it is the honest analysis.",
                  "Reliability, EFA and CFA are three core dialogs; use them before summing a scale.",
                  "Weighted surveys are the one thing the menus cannot do. Four lines in Rj can.",
                  "A Bayes factor can support the null; a p-value cannot. Report the prior.",
                  "Annotate, keep the syntax, deposit the file. A menu analysis is reproducible if the file is shared."]},
                        {"t": "hbox", "color": "amber", "html": "The menu removes the moment "
                         "where a coder has to think. Put it back by writing the sentence "
                         "before reading the p-value."}]},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Statistics Without Code 101 &middot; Complete",
         "headline": "Now go run it,<br>and write the sentence first.",
         "byline": "Every analysis a thesis or an evaluation needs, in a free tool, with the "
                   "estimate before the p-value and the file shared afterwards. Explore the rest "
                   "of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

# -*- coding: utf-8 -*-
"""
Quantitative Methods 101 - ImpactMojo 101 Series (native deck spec)
The quantitative toolkit a development practitioner needs to read and commission analysis:
measurement, description, distributions, sampling, survey weights and design effects,
confidence intervals and tests, correlation and regression, effect sizes and power,
reading a results table and the common errors in published Indian statistics.
Build: python3 scripts/deck-builder/build.py quant_methods

Sources opened for this deck (October 2026):
- DHS Program, "Using Datasets for Analysis" (v005/1,000,000):
  https://dhsprogram.com/data/Using-DataSets-for-Analysis.cfm
- MoSPI, PLFS unit-level data README (MLTS rules):
  https://mospi.gov.in/sites/default/files/README.pdf
- NFHS-5 India Fact Sheet (IIPS / MoHFW):
  https://dhsprogram.com/pubs/pdf/OF43/India_National_Fact_Sheet.pdf
- NFHS-6 (2023-24) India Fact Sheet, provisional (IIPS / MoHFW), mirror read October 2026:
  https://data.opencity.in/dataset/nfhs-6-2023-24
- DHS Program API (indicator CN_NUTS_C_HA2, surveys BD2022DHS, IA2006DHS, IA2015DHS,
  IA2020DHS, NP2022DHS, PK2017DHS): https://api.dhsprogram.com
- MoSPI eSankhyiki API, PLFS annual (calendar year) UR and LFPR; HCES 2023-24 MPCE by
  fractile class and Gini: https://esankhyiki.mospi.gov.in
- ASA statement on p-values, press release 7 March 2016:
  https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
- Duflo, Glennerster & Kremer (2006), NBER Technical Working Paper 0333:
  https://www.nber.org/papers/t0333
- Banerjee, Cole, Duflo & Linden (2005), NBER Working Paper 11904:
  https://www.nber.org/papers/w11904
- Bickel, Hammel & O'Connell (1975), Science 187(4175): 398-404 (Crossref record)
- Cohen (1988) conventions, as summarised at https://effectsizefaq.com
- Census 2011 sex ratio 943: Andaman & Nicobar Basic Statistics, Census of India 2011 PCA table:
  https://ecostat.andamannicobar.gov.in/basicstatPDF2024_25/33.populationcensus.pdf
- CES 2017-18 withheld, 15 November 2019: Business Today report of the MoSPI statement:
  https://www.businesstoday.in/latest/economy-politics/story/govt-withholds-consumer-spending-report-for-2017-18-on-grounds-of-data-quality-238853-2019-11-15
"""

DECK = {
    "slug": "quant-methods",
    "title": "Quantitative Methods 101",
    "description": ("Quantitative Methods 101, a free foundational course for development "
                    "practitioners in South Asia. Read and commission quantitative analysis: "
                    "levels of measurement, descriptive statistics, distributions, sampling error, "
                    "survey weights and design effects in NFHS and PLFS, confidence intervals, "
                    "p-values, correlation and regression, effect sizes, power, and the common "
                    "errors in published Indian statistics. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Quantitative<br>Methods<br>101",
         "sub": "Reading and commissioning numbers in development work: measurement, sampling, "
                "survey weights, intervals, tests, regression and power, worked through with "
                "NFHS, PLFS and HCES data",
         "tags": ["Quantitative Methods", "South Asia Focus", "100 Slides", "Free Forever"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Why quantitative methods"},
             {"name": "Variables and measurement"},
             {"name": "Describing data"},
             {"name": "Distributions"},
             {"name": "Sampling and sampling error"},
             {"name": "Survey weights and design effects"},
             {"name": "Intervals, tests and p-values"},
             {"name": "Correlation, causation, regression"},
             {"name": "Effect sizes and power"},
             {"name": "Reading and commissioning analysis"},
             {"name": "Errors in published statistics"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why quantitative methods"},

        {"type": "content", "label": "Purpose", "title": "What this course is for",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Most development practitioners will never run a regression "
                   "themselves. Almost all of them will read one, approve one, fund one or defend a "
                   "budget on the strength of one. A district officer quotes NFHS stunting figures, a "
                   "programme manager reads an evaluation report, a foundation officer signs off a "
                   "baseline survey of 2,400 households. Each of those moments asks for the same "
                   "skill: knowing what a number can and cannot carry."},
                  {"t": "body", "cls": "sm", "html": "This deck teaches that skill at the level of "
                   "intuition and arithmetic. Every worked example shows its sums, so you can redo "
                   "them on paper and check the next report you read."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "By the end you should be able to", "blocks": [
                      {"t": "bullets", "sm": True, "items": [
                          "Say what kind of variable an indicator is and which summaries suit it",
                          "Apply NFHS and PLFS weights correctly and explain why they exist",
                          "Compute a standard error and a 95% confidence interval for a proportion",
                          "Read a p-value and a regression table without overclaiming",
                          "Ask for a power calculation and judge whether it is credible",
                          "Spot the common errors in published Indian statistics"]}]}]},
         ]},

        {"type": "content", "label": "Numbers in use", "title": "Three numbers that already shape policy",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "29.3%", "label": "children under 5 stunted, India", "color": "amber",
                  "source": "NFHS-6 (2023&ndash;24) India Fact Sheet, IIPS/MoHFW"},
                 {"num": "40.3%", "label": "female labour force participation, age 15+, usual status", "color": "indigo",
                  "source": "MoSPI, PLFS annual estimate, calendar year 2024"},
                 {"num": "&#8377;4,122", "label": "average monthly per capita consumption, rural India", "color": "green",
                  "source": "MoSPI, HCES 2023&ndash;24, without imputation"}]},
             {"t": "body", "html": "Each of these figures drives budgets: Poshan Abhiyaan targets, "
              "labour policy debates, poverty line arguments. Each is also an <strong>estimate</strong>. "
              "It rests on a definition (stunting is height-for-age below &minus;2 standard deviations of "
              "the WHO growth standard), a sample (679,238 households in NFHS-6), a reference period "
              "(the 365 days before the PLFS interview for usual status) and a margin of error. A reader "
              "who knows those four things can use the number well. A reader who does not will "
              "eventually compare two figures that were never measuring the same thing."},
             {"t": "hbox", "color": "cyan", "html": "Quantitative literacy here means asking of every "
              "figure: defined how, counted among whom, when, and how precisely."},
         ]},

        {"type": "content", "label": "A habit", "title": "Four questions to ask of any number",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Question", "What you are checking", "Example of the trap"],
              "rows": [
                  ["What exactly was counted?", "The definition, the indicator formula, the reference period",
                   "PLFS reports unemployment on usual status and on current weekly status; the two differ by almost 2 points"],
                  ["Who was asked, and who was left out?", "The population, the sampling frame, non-response",
                   "NFHS covers households; people in hostels, barracks and prisons are outside the frame"],
                  ["How precise is it?", "Sample size, standard error, design effect, confidence interval",
                   "A district estimate from 300 children carries an interval of roughly &plusmn;5 to &plusmn;8 points"],
                  ["Compared with what?", "Baseline, other places, other rounds, a counterfactual",
                   "A fall between two survey rounds can come from a changed questionnaire"]]},
             {"t": "body", "cls": "sm", "html": "These four questions organise the whole deck. Sections 2 "
              "to 4 deal with what was counted and how to summarise it. Sections 5 to 7 deal with who "
              "was asked and how precise the answer is. Sections 8 and 9 deal with comparisons, causes "
              "and the size of effects. Sections 10 and 11 turn the questions into a checklist you can "
              "use on a report this week."},
         ]},

        {"type": "content", "label": "The pipeline", "title": "From a question to a defensible number",
         "blocks": [
             {"t": "flow", "steps": [
                 "QUESTION: what do we need to know?",
                 "MEASURE: define and operationalise",
                 "SAMPLE: select who is asked",
                 "ESTIMATE: weight and summarise",
                 "QUANTIFY ERROR: SE, CI, design effect",
                 "INTERPRET: compare, explain, decide"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Errors enter at every stage, and later "
                        "stages cannot repair earlier ones. A brilliant regression on a badly worded "
                        "question is still an answer to the wrong question. A large sample drawn from "
                        "an incomplete frame is a precise estimate of the wrong population. Most "
                        "arguments about a published figure turn out to be about the first three "
                        "boxes, which is why this deck spends as long on measurement and sampling as "
                        "on testing."}],
              "right": [{"t": "panel", "color": "amber", "title": "Where reviewers look first", "html":
                         "When you review a quantitative report, start at the left of this chain. Read the "
                         "questionnaire item before the result table. Read the sampling section before "
                         "the conclusions. Ask how the weights were built before you ask whether the "
                         "coefficient is significant. It is quicker, and it catches more."}]},
         ]},

        {"type": "content", "label": "Definitions matter", "title": "One survey, two unemployment rates",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "qmUrChart",
                        "title": "Unemployment rate, age 15+, India (%), by reference period",
                        "source": "MoSPI, PLFS annual estimates (calendar years), via eSankhyiki API",
                        "type": "bar",
                        "data": {"labels": ["2023", "2024", "2025"],
                                 "datasets": [
                                     {"label": "Usual status (PS+SS)", "data": [3.1, 3.2, 3.1], "backgroundColor": "#0369A1"},
                                     {"label": "Current weekly status (CWS)", "data": [5.0, 4.9, 5.3], "backgroundColor": "#F59E0B"}]},
                        "options": {"__js__": "{ scales:{ y:{ beginAtZero:true, title:{display:true,text:'per cent of labour force'} } } }"}}],
              "right": [
                  {"t": "body", "cls": "sm", "html": "The same PLFS interviews yield two unemployment "
                   "rates. <strong>Usual status</strong> (principal plus subsidiary, PS+SS) classifies a "
                   "person by their activity over the 365 days before the survey; anyone who worked for "
                   "30 days or more in a subsidiary capacity counts as employed. <strong>Current weekly "
                   "status</strong> looks only at the seven days before the interview."},
                  {"t": "body", "cls": "sm", "html": "For calendar year 2024 the first gives 3.2% and the "
                   "second 4.9%. Neither is wrong. They answer different questions: chronic joblessness "
                   "versus joblessness last week, which catches seasonal gaps in farm work."},
                  {"t": "hbox", "color": "red", "html": "Quote the status with the number, every time."}]},
         ]},

        {"type": "content", "label": "Three roles", "title": "Reader, commissioner, analyst",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "cyan", "title": "Reader", "html":
                   "Reads published statistics and evaluation reports. Needs to know what an indicator "
                   "means, how precise it is, and whether a claimed difference is real. This is most "
                   "practitioners, most of the time."},
                  {"t": "panel", "color": "indigo", "title": "Commissioner", "html":
                   "Writes terms of reference, approves sample sizes, accepts deliverables. Needs to ask "
                   "for a power calculation, a weighting note and the code, and to judge the answers."}],
              "right": [
                  {"t": "panel", "color": "green", "title": "Analyst", "html":
                   "Runs the numbers. Needs software skills on top of everything here; the linked decks "
                   "on Econometrics, Exploratory Data Analysis and Multivariate Analysis go further."},
                  {"t": "hbox", "color": "amber", "html": "Anyone holding unit-level data about people "
                   "is a data fiduciary under the Digital Personal Data Protection Act 2023, whose duties "
                   "apply, with the 2025 Rules, from 13 May 2027. From that date section 17(2)(b) exempts processing for research, archiving or "
                   "statistical purposes only where its conditions are met, including that the data is "
                   "not used for decisions about a specific person."}]},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Variables and measurement"},

        {"type": "content", "label": "Building blocks", "title": "Cases, variables and the unit of analysis",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Case and variable",
                   "def": "A case is one row of a dataset: a household, a person, a child, a village. A "
                   "variable is one column: a characteristic recorded for every case, such as age, caste "
                   "category or monthly consumption."},
                  {"t": "body", "cls": "sm", "html": "The <strong>unit of analysis</strong> is the kind of "
                   "case your question is about. It decides which file you open and which weight you use. "
                   "A question about how many households have piped water is answered on the household "
                   "file; a question about how many people live in such households is answered on the "
                   "person file, or by weighting households by their size."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "How Indian surveys are organised", "html":
                   "NFHS data, like all DHS data, comes as separate recode files: household (HR), "
                   "household member (PR), women (IR), men (MR) and children (KR, BR). PLFS ships a "
                   "household-level file and a person-level file linked by a common key of quarter, "
                   "visit, FSU serial number, hamlet group, second-stage stratum and household number. "
                   "Merging them wrongly, or analysing children from the women's file without "
                   "understanding that each row is a birth, is one of the most frequent errors in "
                   "student and consultant work alike."},
                  {"t": "hbox", "color": "cyan", "html": "Write the unit of analysis into the first line "
                   "of every analysis plan."}]},
         ]},

        {"type": "content", "label": "Levels of measurement", "title": "Nominal, ordinal, interval, ratio",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "What the values tell you", "South Asian example", "Sensible summaries"],
              "rows": [
                  ["Nominal", "Categories with no order", "Religion; state; social group (SC, ST, OBC, others); type of cooking fuel",
                   "Counts, percentages, mode"],
                  ["Ordinal", "Ordered categories, unequal or unknown gaps", "Wealth quintile; education level completed; a five-point agreement scale",
                   "Median, percentiles, percentages by category"],
                  ["Interval", "Equal gaps, arbitrary zero", "Temperature in &deg;C; a test score on a scaled metric; a height-for-age z-score",
                   "Mean, SD, differences"],
                  ["Ratio", "Equal gaps and a true zero", "Monthly consumption in &#8377;; land owned in acres; number of children; days worked",
                   "Everything above, plus ratios and percentage change"]]},
             {"t": "body", "cls": "sm", "html": "The level limits the arithmetic. Saying one household spends "
              "twice as much as another makes sense for consumption (ratio) and makes no sense for wealth "
              "quintile (ordinal): the richest quintile is not &quot;five times&quot; the poorest. The "
              "classification was set out by the psychologist S.S. Stevens in 1946; in practice, the "
              "useful question is simply which operations the numbers will bear."},
         ]},

        {"type": "content", "label": "Categories", "title": "Codes are labels, and averaging them is meaningless",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Survey files store categories as numbers. In a typical layout "
                   "social group might be coded 1 for ST, 2 for SC, 3 for OBC and 9 for others. Software "
                   "will happily compute the mean of that column and report 2.7. The number describes "
                   "nothing: change the coding order and it changes, while the households stay the same."},
                  {"t": "body", "cls": "sm", "html": "For nominal variables report the share of cases in "
                   "each category. For ordinal variables report the distribution across categories or "
                   "the median category. A cross-tabulation, covered in Section 3, is usually the right "
                   "first table."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Ordinal scales in programme surveys", "html":
                   "Satisfaction and attitude items (&quot;strongly agree&quot; to &quot;strongly "
                   "disagree&quot;) are ordinal. Averaging them as if the gaps were equal is common and "
                   "sometimes defensible when many items are summed into a scale, but a single item "
                   "should be reported as a distribution. A mean of 3.4 hides whether half the "
                   "respondents strongly disagreed."},
                  {"t": "panel", "color": "red", "title": "Watch the special codes", "html":
                   "Codes like 98 (&quot;don't know&quot;) and 99 (&quot;missing&quot;) sit inside "
                   "numeric columns. Leave them in and a mean age or a mean landholding can jump. DHS "
                   "files flag implausible anthropometric values with special high codes in the "
                   "z-score variables; the recode manual lists them, and they must be dropped first."}]},
         ]},

        {"type": "content", "label": "Numeric scales", "title": "Interval and ratio variables in practice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Interval scale",
                   "def": "Equal distances mean equal differences, but zero is a convention. A z-score of "
                   "0 means &quot;at the reference median&quot;; it does not mean &quot;no height&quot;. You can say a "
                   "child moved from &minus;2.4 to &minus;1.9, a gain of 0.5 SD; you cannot say one child "
                   "is twice as stunted as another."},
                  {"t": "term", "word": "Ratio scale",
                   "def": "Zero means none of the quantity. Consumption, income, hours worked, acres owned "
                   "and number of antenatal visits are ratio variables, so percentage changes and ratios "
                   "between groups are meaningful."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "Why this matters for reporting", "html":
                   "HCES 2023&ndash;24 reports average monthly per capita consumption of &#8377;6,996 in "
                   "urban India and &#8377;4,122 in rural India (MoSPI). Because consumption is a ratio "
                   "variable you can say urban spending per head is about 1.7 times rural "
                   "(6,996 &divide; 4,122 = 1.70). Learning-assessment scale scores are closer to "
                   "interval: a gap of 20 points is meaningful, a statement that one district scores "
                   "&quot;10% higher&quot; usually is not, because the zero of the scale was set by "
                   "the test designer."},
                  {"t": "hbox", "color": "indigo", "html": "Before computing a percentage change, check the "
                   "variable has a true zero."}]},
         ]},

        {"type": "content", "label": "Type and zero", "title": "Discrete, continuous, zero and missing",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "<strong>Discrete</strong> variables take whole values: children "
                   "ever born, rooms in a dwelling, days of MGNREGA work in a year (the Act was repealed "
                   "from 1 July 2026 and replaced by the Viksit Bharat G RAM G Act 2025, which provides "
                   "for 125 days, so series that span both need care). <strong>Continuous</strong> "
                   "variables can take any value in a range: height, weight, consumption. Counts with "
                   "many zeros, such as days of hired labour, need their own summaries; a mean of 4 "
                   "days may be most households at zero and a few at 40."},
                  {"t": "body", "cls": "sm", "html": "Report the share with a zero next to the mean "
                   "whenever zeros are common."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Zero and missing are different facts", "html":
                   "&quot;Earned nothing last month&quot; is information. &quot;Did not answer&quot; is "
                   "an absence of information. A dataset that stores both as 0 will understate "
                   "average earnings and overstate the share with no income. A dataset that stores "
                   "both as blank will do the reverse once the software drops blanks. Check the "
                   "codebook for how each was recorded, then decide and document."},
                  {"t": "hbox", "color": "amber", "html": "A missing value is never silently a zero."}]},
         ]},

        {"type": "content", "label": "Indicators", "title": "Most indicators are built, and the build is the definition",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Indicator", "Built from", "Formula", "Source"],
              "rows": [
                  ["Stunting", "Child height, age, sex", "Share of children under 5 with height-for-age z-score below &minus;2 (WHO Child Growth Standards)", "NFHS / DHS"],
                  ["Labour force participation rate", "Activity status of each person", "(employed + unemployed) &divide; population of that age, &times; 100", "PLFS"],
                  ["Unemployment rate", "Activity status", "unemployed &divide; labour force, &times; 100", "PLFS"],
                  ["MPCE", "Household consumption, household size", "household monthly consumption &divide; household size", "HCES"],
                  ["Sex ratio", "Counts by sex", "females per 1,000 males", "Census, NFHS"]]},
             {"t": "body", "cls": "sm", "html": "Two notes on this table. The unemployment rate divides by "
              "the <strong>labour force</strong>, while the worker population ratio divides by the "
              "<strong>whole population</strong>, so a fall in unemployment can coexist with a fall in "
              "the share of people working if many leave the labour force. And MPCE assigns each member "
              "the household average, which hides inequality inside the household, between men and "
              "women in particular."},
         ]},

        {"type": "content", "label": "Operationalisation", "title": "From a concept to a column",
         "blocks": [
             {"t": "flow", "steps": [
                 "CONCEPT: women's work",
                 "DEFINITION: economic activity in a reference period",
                 "QUESTION: activity codes asked of each member",
                 "VARIABLE: usual principal and subsidiary status",
                 "INDICATOR: female LFPR"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Each arrow is a decision that someone made, and "
                        "each can be argued with. Unpaid work producing goods for the household's own use, "
                        "such as fetching water or tending poultry, sits on a contested boundary between "
                        "economic and domestic activity. Moving that boundary changes measured female "
                        "participation by many points without any woman doing anything different."}],
              "right": [{"t": "panel", "color": "indigo", "title": "The practitioner's check", "html":
                         "When a report states a figure for a concept (women's agency, food security, "
                         "learning), find the operational definition in its annex. If there is no annex, "
                         "ask for one. The Time Use Survey, run by NSO in 2019 and again in 2024 (report released "
                         "25 February 2025), exists "
                         "precisely because a labour force survey's activity codes cannot see most "
                         "unpaid work."}]},
         ]},

        {"type": "content", "label": "Quality", "title": "Validity and reliability",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Validity",
                   "def": "Does the variable measure the concept it claims to? A household asset index is a "
                   "reasonable proxy for long-run wealth; it is a poor measure of last month's income shock."},
                  {"t": "term", "word": "Reliability",
                   "def": "Would the same person, asked again under the same conditions, give the same answer? "
                   "Recall of small, frequent food purchases fades over a month, which is one reason "
                   "consumption surveys use shorter recall periods for frequently bought items."},
                  {"t": "body", "cls": "sm", "html": "A measure can be reliable and invalid: a scale that "
                   "always reads 2 kg light is consistent and wrong."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Signs of trouble in the data itself", "html":
                   "Age heaping, where reported ages pile up on numbers ending in 0 and 5, shows that "
                   "people are estimating. Heights recorded mostly to the whole centimetre show "
                   "measurer shortcuts. A sudden change in an indicator between two survey phases that "
                   "used different field agencies is worth checking before it is believed. These "
                   "patterns are visible in a frequency table, and they are why analysts look at raw "
                   "distributions before summarising."},
                  {"t": "hbox", "color": "cyan", "html": "Validity is argued; reliability can be tested "
                   "with repeat measurement and back-checks."}]},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Describing data"},

        {"type": "content", "label": "The centre", "title": "Mean, median and mode",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Measure", "How it is computed", "Strength", "Weakness"],
              "rows": [
                  ["Mean", "Sum of values &divide; number of values", "Uses every observation; adds up (mean &times; n = total)",
                   "Pulled hard by extreme values"],
                  ["Median", "Middle value once sorted (average of the two middle values if n is even)",
                   "Unmoved by a few very large or small values", "Ignores how far the tails stretch; cannot be summed across groups"],
                  ["Mode", "Most frequent value or category", "The only centre for nominal data",
                   "Can be unstable; there may be several"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Choose by the question. A state finance department "
                        "estimating total spending needs the mean, because only the mean multiplies back to a "
                        "total. A report on what a typical household experiences should lead with the median, "
                        "because in skewed data most households sit below the mean."}],
              "right": [{"t": "hbox", "color": "cyan", "html": "When mean and median are far apart, report "
                         "both. The gap itself tells the reader the distribution is lopsided, and which "
                         "way it leans."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "One rich household moves the mean",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Illustrative (hypothetical figures): monthly per capita consumption (&#8377;) for ten "
                   "households in a hamlet, sorted:"},
                  {"t": "raw", "html": "<div style='font-family:monospace;font-size:1rem;margin:0.4rem 0;'>"
                   "2,000 &middot; 2,200 &middot; 2,400 &middot; 2,600 &middot; 2,800 &middot; 3,000 &middot; 3,200 &middot; 3,400 &middot; 3,800 &middot; 30,000</div>"},
                  {"t": "body", "cls": "sm", "html": "<strong>Mean</strong> = 55,400 &divide; 10 = "
                   "&#8377;5,540.<br><strong>Median</strong> = (2,800 + 3,000) &divide; 2 = &#8377;2,900.<br>"
                   "Drop the landowner's household and the mean of the other nine is 25,400 &divide; 9 = "
                   "&#8377;2,822, while the median of nine becomes the fifth value, &#8377;2,800."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "What the reader would conclude", "html":
                   "A report that says &quot;average consumption in the hamlet is &#8377;5,540&quot; is "
                   "arithmetically right and describes nobody: nine of ten households consume less than "
                   "&#8377;3,900. The median of &#8377;2,900 is a far better description of the typical "
                   "household. One observation changed the mean by &#8377;2,718 and the median by "
                   "&#8377;100."},
                  {"t": "hbox", "color": "indigo", "html": "Illustrative figures. The same arithmetic "
                   "applies to land, income and loan sizes in real surveys, which are almost always "
                   "skewed to the right."}]},
         ]},

        {"type": "content", "label": "Real data", "title": "Consumption in India is skewed to the right",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "qmHcesChart",
                        "title": "Average MPCE (&#8377;) by fractile class, rural India, 2023&ndash;24",
                        "source": "MoSPI, HCES 2023&ndash;24, without imputation, via eSankhyiki API",
                        "type": "bar",
                        "data": {"labels": ["0&ndash;5", "5&ndash;10", "10&ndash;20", "20&ndash;30", "30&ndash;40", "40&ndash;50",
                                            "50&ndash;60", "60&ndash;70", "70&ndash;80", "80&ndash;90", "90&ndash;95", "95&ndash;100"],
                                 "datasets": [{"label": "Average MPCE (Rs)",
                                               "data": [1677, 2126, 2473, 2833, 3162, 3498, 3866, 4304, 4885, 5763, 6929, 10137],
                                               "backgroundColor": "#0369A1"}]},
                        "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Rs per person per month'} }, x:{ title:{display:true,text:'percentile class of population'} } } }"}}],
              "right": [
                  {"t": "body", "cls": "sm", "html": "The rural mean is &#8377;4,122. The class containing "
                   "the median person, the 40th to 60th percentiles, averages &#8377;3,498 and &#8377;3,866, "
                   "so the median lies somewhere between them and below the mean. The mean sits up at "
                   "roughly the 60th percentile because the top classes pull it upward: the richest 5% "
                   "average &#8377;10,137."},
                  {"t": "hbox", "color": "cyan", "html": "Urban India shows the same pattern more sharply: "
                   "a mean of &#8377;6,996 against &#8377;5,622 and &#8377;6,334 in the 40th&ndash;60th "
                   "percentile classes, and &#8377;20,310 in the top 5%."}]},
         ]},

        {"type": "content", "label": "Spread", "title": "Range, interquartile range and standard deviation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "A centre without a spread is half a description. Two districts "
                   "with the same mean test score can differ completely: one with every child near the "
                   "mean, another with a cluster of high scorers and a cluster who cannot read."},
                  {"t": "bullets", "sm": True, "items": [
                      "<strong>Range</strong>: maximum minus minimum. Simple, and decided by the two most extreme cases.",
                      "<strong>Interquartile range</strong>: 75th percentile minus 25th. The spread of the middle half, resistant to outliers; pairs with the median.",
                      "<strong>Variance</strong>: the average squared deviation from the mean.",
                      "<strong>Standard deviation (SD)</strong>: the square root of the variance, in the original units; pairs with the mean."]}],
              "right": [
                  {"t": "panel", "color": "green", "title": "Worked: SD of five scores", "html":
                   "Scores 4, 6, 8, 10, 12. Mean = 40 &divide; 5 = 8.<br>"
                   "Deviations: &minus;4, &minus;2, 0, 2, 4.<br>"
                   "Squared: 16, 4, 0, 4, 16; sum = 40.<br>"
                   "Sample variance = 40 &divide; (5 &minus; 1) = 10.<br>"
                   "SD = &radic;10 = <strong>3.16</strong>.<br><br>"
                   "We divide by n &minus; 1 for a sample because deviations measured from the sample's "
                   "own mean are slightly too small on average; the correction removes that bias."}]},
         ]},

        {"type": "content", "label": "Inequality summaries", "title": "Spread between groups: ratios and the Gini",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "stats", "cols": 2, "cards": [
                      {"num": "6.0&times;", "label": "rural: top 5% average MPCE &divide; bottom 5% (10,137 &divide; 1,677)", "color": "amber",
                       "source": "MoSPI, HCES 2023&ndash;24"},
                      {"num": "8.5&times;", "label": "urban: top 5% &divide; bottom 5% (20,310 &divide; 2,376)", "color": "red",
                       "source": "MoSPI, HCES 2023&ndash;24"}]},
                  {"t": "body", "cls": "sm", "html": "Ratios between percentile groups are easy to explain "
                   "to a non-specialist and say exactly which comparison is being made."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "The Gini coefficient", "html":
                   "The Gini runs from 0 (everyone consumes the same) to 1 (one person consumes "
                   "everything). MoSPI reports a consumption Gini of 0.237 for rural and 0.284 for urban "
                   "India in 2023&ndash;24, against 0.266 and 0.314 in 2022&ndash;23. A single summary "
                   "number for a whole distribution is convenient and lossy: very different "
                   "distributions can share a Gini."},
                  {"t": "hbox", "color": "red", "html": "Consumption Ginis run lower than income or wealth "
                   "Ginis because households smooth consumption, and survey consumption under-records the "
                   "richest. Never compare a consumption Gini for India with an income Gini elsewhere."}]},
         ]},

        {"type": "content", "label": "Language of change", "title": "Percentages and percentage points",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Stunting among children under five in India was 38.4% in NFHS-4 "
                   "(2015&ndash;16) and 35.5% in NFHS-5 (2019&ndash;21), according to the NFHS-5 India Fact "
                   "Sheet. That change can be described two ways, and both are correct:"},
                  {"t": "bullets", "sm": True, "items": [
                      "<strong>Absolute</strong>: 38.4 &minus; 35.5 = a fall of <strong>2.9 percentage points</strong>.",
                      "<strong>Relative</strong>: 2.9 &divide; 38.4 = 0.0755, a fall of <strong>7.6 per cent</strong>."]},
                  {"t": "body", "cls": "sm", "html": "Writing &quot;stunting fell by 2.9%&quot; is wrong on "
                   "both readings. Press releases and reports make this slip often, and advocates on each "
                   "side of a debate pick whichever version suits them."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Rules for writing about change", "html":
                   "Use &quot;percentage points&quot; for the difference between two percentages. Use "
                   "&quot;per cent&quot; only for a relative change, and say what it is relative to. Report "
                   "the two levels as well, so readers can do either calculation. Relative changes in "
                   "small numbers look dramatic: a rise from 0.5% to 1.0% is &quot;doubling&quot; and "
                   "half a percentage point."},
                  {"t": "hbox", "color": "cyan", "html": "Levels first, then the absolute change, then the "
                   "relative change if it helps."}]},
         ]},

        {"type": "content", "label": "Denominators", "title": "A ratio is only as good as its denominator",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "stats", "cols": 2, "cards": [
                      {"num": "943", "label": "females per 1,000 males, total population", "color": "indigo",
                       "source": "Census of India 2011, Primary Census Abstract"},
                      {"num": "1,020", "label": "females per 1,000 males, de jure household population", "color": "amber",
                       "source": "NFHS-5 (2019&ndash;21) India Fact Sheet"}]},
                  {"t": "body", "cls": "sm", "html": "The NFHS-5 figure circulated widely as evidence that "
                   "India had &quot;more women than men&quot;. The two numbers do not measure the same "
                   "population."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Why they differ", "html":
                   "The Census counts everyone, including people in institutions and the houseless. NFHS "
                   "counts usual members of sampled households only. Men who live away for work in "
                   "hostels, dormitories, worksites or other states are more likely to fall outside a "
                   "household roster, which raises the female share among those who remain. The same "
                   "fact sheet gives a sex ratio at birth of 929 for children born in the five years "
                   "before the survey, which points the other way."},
                  {"t": "hbox", "color": "cyan", "html": "Before comparing two ratios, write down the "
                   "numerator and denominator of each."}]},
         ]},

        {"type": "content", "label": "Two variables", "title": "Cross-tabulations and which way to percentage",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "table",
                   "head": ["Illustrative", "Toilet used", "Not used", "Total"],
                   "rows": [
                       ["Received IEC visit", "240", "60", "300"],
                       ["No visit", "350", "350", "700"],
                       ["Total", "590", "410", "1,000"]]},
                  {"t": "body", "cls": "sm", "html": "Row percentages: 240 &divide; 300 = 80% of visited "
                   "households use the toilet, against 350 &divide; 700 = 50% of the rest.<br>Column "
                   "percentages: 240 &divide; 590 = 41% of users had a visit."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Percentage across the cause", "html":
                   "The rule of thumb: compute percentages within categories of the variable you treat as "
                   "the explanation (here, the visit), and compare across them. The row percentages "
                   "answer &quot;do visited households behave differently?&quot;. The column percentages "
                   "answer a different question, about the make-up of users. Both are legitimate; mixing "
                   "them up produces sentences that sound like findings and mean nothing."},
                  {"t": "hbox", "color": "amber", "html": "A 30-point gap is an association. Whether "
                   "the visit caused it is a separate question, taken up in Section 8."}]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Distributions"},

        {"type": "content", "label": "Shape", "title": "What a distribution is, and the four things to read in it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Distribution",
                   "def": "The pattern of how often each value, or range of values, occurs. A histogram "
                   "draws it for a continuous variable; a bar chart of category shares draws it for a "
                   "categorical one."},
                  {"t": "body", "cls": "sm", "html": "Plot a variable before summarising it. Summaries "
                   "assume a shape, and the plot shows whether the assumption holds. The Exploratory Data "
                   "Analysis 101 deck spends a whole course on this habit."}],
              "right": [
                  {"t": "table",
                   "head": ["Read", "Question", "Example"],
                   "rows": [
                       ["Centre", "Where is the bulk?", "Median MPCE"],
                       ["Spread", "How wide?", "IQR of test scores"],
                       ["Shape", "Symmetric or skewed? One peak or two?", "Landholding: long right tail"],
                       ["Outliers", "Values far from the rest, real or errors?", "A height of 210 cm for a two-year-old"]]},
                  {"t": "hbox", "color": "cyan", "html": "Two peaks usually mean two populations mixed "
                   "together, such as rural and urban, that should be analysed apart."}]},
         ]},

        {"type": "content", "label": "The normal curve", "title": "The normal distribution and the 68&ndash;95&ndash;99.7 rule",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "qmNormalChart",
                        "title": "Standard normal density (mean 0, SD 1)",
                        "source": "Computed from the normal density formula",
                        "type": "line",
                        "data": {"labels": ["&minus;3", "&minus;2.5", "&minus;2", "&minus;1.5", "&minus;1", "&minus;0.5", "0", "0.5", "1", "1.5", "2", "2.5", "3"],
                                 "datasets": [{"label": "density", "data": [0.004, 0.018, 0.054, 0.130, 0.242, 0.352, 0.399, 0.352, 0.242, 0.130, 0.054, 0.018, 0.004],
                                               "borderColor": "#0369A1", "backgroundColor": "rgba(3,105,161,0.12)", "fill": True, "tension": 0.4, "pointRadius": 0}]},
                        "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'standard deviations from the mean'} }, y:{ title:{display:true,text:'density'} } } }"}}],
              "right": [
                  {"t": "body", "cls": "sm", "html": "Many measured quantities, such as adult heights within "
                   "one sex, and above all the averages of repeated samples, follow a bell-shaped curve. "
                   "In a normal distribution about <strong>68%</strong> of values lie within 1 SD of the "
                   "mean, about <strong>95%</strong> within 2 SD (1.96 exactly) and about "
                   "<strong>99.7%</strong> within 3 SD."},
                  {"t": "body", "cls": "sm", "html": "The 1.96 is the number behind every 95% confidence "
                   "interval in Section 7."},
                  {"t": "hbox", "color": "amber", "html": "Income, consumption, land and loan sizes are "
                   "not normal. Applying normal-based rules to the raw values misleads."}]},
         ]},

        {"type": "content", "label": "Standardising", "title": "z-scores, and how stunting is measured",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.4rem 0;'>"
                   "z&nbsp;=&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>value &minus; reference median</span>"
                   "&nbsp;/&nbsp;reference SD</div>"},
                  {"t": "body", "cls": "sm", "html": "A z-score says how many standard deviations a value "
                   "sits from a reference. It puts measurements on a common scale, so a two-year-old and a "
                   "four-year-old can be compared even though their heights differ."},
                  {"t": "panel", "color": "green", "title": "Worked (illustrative reference values)", "html":
                   "A child measures 82.0 cm. Suppose the reference median for her age and sex is "
                   "87.1 cm with an SD of 3.2 cm.<br>z = (82.0 &minus; 87.1) &divide; 3.2 = "
                   "&minus;5.1 &divide; 3.2 = <strong>&minus;1.59</strong>. She is short for her age and "
                   "above the &minus;2 stunting cut-off."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "How NFHS uses it", "html":
                   "NFHS and every DHS compute height-for-age z-scores against the WHO Child Growth "
                   "Standards. A child below &minus;2 is counted as stunted, below &minus;3 as severely "
                   "stunted. The 29.3% stunting figure for India in NFHS-6 (2023&ndash;24), like 35.5% in "
                   "NFHS-5 (2019&ndash;21), is therefore a share of children whose z-score fell below a "
                   "fixed line."},
                  {"t": "hbox", "color": "amber", "html": "Because stunting is a cut-off on a continuous "
                   "measure, a whole population can grow taller without the share below &minus;2 moving "
                   "much. Report the mean z-score alongside the prevalence when you can."}]},
         ]},

        {"type": "content", "label": "Skew", "title": "Skewed variables and the log scale",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Consumption, earnings, loan sizes, farm output and firm size are "
                   "skewed to the right: many small values and a long tail of large ones. For such "
                   "variables the median and percentile ratios describe better than the mean and SD."},
                  {"t": "body", "cls": "sm", "html": "Analysts often take the natural logarithm. Equal "
                   "<em>ratios</em> become equal <em>distances</em>: &#8377;2,000 to &#8377;4,000 and "
                   "&#8377;10,000 to &#8377;20,000 are the same step on a log scale (ln 2 = 0.693 each "
                   "time). The log of a right-skewed variable is often close to symmetric, which suits "
                   "regression."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "What this means for reading results", "html":
                   "When a report models log consumption, its coefficients describe proportional changes. "
                   "A coefficient of 0.08 on a programme dummy means consumption about 8% higher "
                   "(exactly e<sup>0.08</sup> &minus; 1 = 8.3%). Section 8 returns to this."},
                  {"t": "panel", "color": "amber", "title": "Zeros break logs", "html":
                   "The log of zero is undefined. Earnings or harvest values with many zeros cannot be "
                   "logged directly; adding 1 before logging is common and changes the result depending "
                   "on the units. Ask how zeros were handled."}]},
         ]},

        {"type": "content", "label": "Yes or no", "title": "Binary outcomes and counts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Many development indicators are <strong>binary</strong>: stunted or "
                   "not, enrolled or not, institutional delivery or not. Coded 1 and 0, the mean of a "
                   "binary variable is the proportion with the characteristic. Its variance is "
                   "p(1 &minus; p)."},
                  {"t": "table",
                   "head": ["p", "p(1 &minus; p)", "SD"],
                   "rows": [["0.05", "0.0475", "0.22"], ["0.20", "0.16", "0.40"], ["0.355", "0.229", "0.48"], ["0.50", "0.25", "0.50"]]},
                  {"t": "body", "cls": "sm", "html": "Variance peaks at p = 0.5. A survey designed to measure "
                   "a 50% indicator needs the largest sample; this is why sample size calculations "
                   "often assume p = 0.5 when nothing better is known."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Counts", "html":
                   "Counts such as antenatal visits, children ever born or days ill last month are whole "
                   "numbers starting at zero and usually right-skewed. Their mean is meaningful; their SD "
                   "often exceeds what a symmetric distribution would give. Specialised models (Poisson, "
                   "negative binomial) exist for them, covered in the Econometrics 101 deck."},
                  {"t": "hbox", "color": "cyan", "html": "For a binary outcome, the mean is the "
                   "prevalence. Read a &quot;mean of 0.36&quot; as 36%."}]},
         ]},

        {"type": "content", "label": "Data fingerprints", "title": "Heaping, digit preference and impossible values",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Distributions carry fingerprints of how the data were collected. "
                   "Where people do not know their exact age, reported ages pile up on numbers ending in "
                   "0 and 5. Where enumerators round, heights cluster on whole centimetres. Where a "
                   "questionnaire skip is mis-programmed, a whole category goes missing for one "
                   "field team."},
                  {"t": "body", "cls": "sm", "html": "None of these show in a table of means. All of them "
                   "show in a frequency table or histogram, which is why reviewers ask to see one."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Why age heaping matters downstream", "html":
                   "Stunting depends on height <em>for age</em>. If a child's age is wrong by six months, "
                   "the z-score is wrong, and heaping on whole years shifts children across age bands. "
                   "Child age in DHS surveys comes from birth dates recorded in the birth history, which "
                   "is more accurate than asking age directly; small local surveys that ask age in years "
                   "produce noisier z-scores."},
                  {"t": "panel", "color": "amber", "title": "Impossible values", "html":
                   "A 2-year-old at 130 cm, a household of 31, 400 days worked last year: check them "
                   "against the questionnaire and the field notes, then correct, flag or exclude, and "
                   "record which."}]},
         ]},

        {"type": "content", "label": "The bridge", "title": "The sampling distribution: why averages behave",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Sampling distribution",
                   "def": "The distribution an estimate would have if you drew the sample again and again "
                   "from the same population. Its SD has a special name: the <strong>standard error</strong>."},
                  {"t": "body", "cls": "sm", "html": "The <strong>central limit theorem</strong> says that "
                   "for reasonably large samples, the sampling distribution of a mean or a proportion is "
                   "close to normal, even when the variable itself is skewed. Consumption is lopsided; the "
                   "average consumption of many repeated samples of 1,000 households is bell-shaped."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "Why this is the hinge of the whole deck", "html":
                   "We only ever see one sample. The central limit theorem tells us how far a single "
                   "sample estimate is likely to sit from the true value, using the normal curve and "
                   "the standard error. Confidence intervals, p-values and power calculations in "
                   "Sections 7 and 9 all rest on this one result."},
                  {"t": "hbox", "color": "amber", "html": "Two different SDs: the SD of the variable "
                   "describes people; the standard error describes the estimate. Reports confuse them "
                   "often."}]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Sampling and sampling error"},

        {"type": "content", "label": "The idea", "title": "How a sample can describe a country",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "stats", "cols": 3, "cards": [
                      {"num": "679,238", "label": "households", "color": "cyan", "source": "NFHS-6 India Fact Sheet"},
                      {"num": "716,397", "label": "women", "color": "indigo", "source": "NFHS-6 India Fact Sheet"},
                      {"num": "100,977", "label": "men", "color": "green", "source": "NFHS-6 India Fact Sheet"}]},
                  {"t": "body", "cls": "sm", "html": "NFHS-6 interviewed these households in two phases, "
                   "28 May 2023 to 26 February 2024 and 7 February 2024 to 31 December 2024, through 27 "
                   "field agencies. That is well under 1% of India's households, and it supports estimates "
                   "for every state. NFHS-5 (2019&ndash;21), with 636,699 households, also published a "
                   "fact sheet for every district."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "Why it works", "html":
                   "Precision depends mainly on the <strong>size of the sample</strong> and very little on the share "
                   "of the population sampled. A well-drawn random sample of 1,000 households measures a "
                   "proportion about as precisely in a district of 2 lakh households as in a state of 2 "
                   "crore. What makes this work is <strong>probability selection</strong>: every unit in "
                   "the population has a known, non-zero chance of selection, so the sample can be "
                   "weighted back to the population and its error quantified."},
                  {"t": "hbox", "color": "amber", "html": "A convenience sample (whoever came to the "
                   "meeting, whoever answered the phone) has no known selection probabilities, so its "
                   "error cannot be computed at all."}]},
         ]},

        {"type": "content", "label": "Designs", "title": "Probability sampling designs used in South Asian surveys",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "How units are chosen", "Why used", "Cost to precision"],
              "rows": [
                  ["Simple random", "Every unit equally likely, drawn from a full list", "Benchmark for all formulas",
                   "None, but a full list of households rarely exists"],
                  ["Systematic", "Every k-th unit from a list after a random start", "Easy in the field from a household listing",
                   "Usually close to simple random"],
                  ["Stratified", "Population split into groups (state, rural/urban); sample drawn in each", "Guarantees coverage; separate estimates per stratum",
                   "Usually <em>improves</em> precision"],
                  ["Cluster", "Groups (villages, urban blocks) selected, then units within them", "Cuts travel and listing cost",
                   "Usually <em>worsens</em> precision"],
                  ["Multistage", "Clusters first, then households within selected clusters", "The standard for NFHS, PLFS and HCES",
                   "Combines both effects"]]},
             {"t": "body", "cls": "sm", "html": "NFHS and other DHS surveys select villages and urban census "
              "enumeration blocks as primary sampling units, list the households in each, and then select "
              "a fixed number of households. PLFS calls its first-stage units FSUs and stratifies within "
              "them; its README refers to second-stage strata (SSS), and the weights are calculated at that "
              "level. A survey's sampling chapter tells you which units are clusters and which are strata, "
              "and you need both facts to compute correct standard errors."},
         ]},

        {"type": "content", "label": "Two kinds of error", "title": "Sampling error and non-sampling error",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "cyan", "title": "Sampling error", "html":
                   "The chance difference between a sample estimate and the population value, arising "
                   "because only some units were observed. It is random in direction, shrinks as the "
                   "sample grows, and can be estimated from the data: the standard error is its measure. "
                   "Every confidence interval in a report describes this error and only this error."},
                  {"t": "body", "cls": "sm", "html": "A report that gives a margin of error has addressed "
                   "sampling error. It has said nothing yet about the other kind."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Non-sampling error", "html":
                   "Everything else: an incomplete frame, refusals, households not found at home, "
                   "questions misunderstood, interviewer effects, recall error, data entry slips, "
                   "processing mistakes. It can be systematic, so it does not average out. It does "
                   "<strong>not</strong> shrink with a larger sample; a larger survey may even have more "
                   "of it if field supervision thins out."},
                  {"t": "hbox", "color": "amber", "html": "In large national surveys non-sampling error "
                   "often exceeds sampling error. A national interval of &plusmn;0.3 points can sit on "
                   "top of a measurement problem several times that size."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "The standard error of a proportion",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.4rem 0;'>"
                   "SE(p)&nbsp;=&nbsp;&radic;[&nbsp;p(1&nbsp;&minus;&nbsp;p)&nbsp;/&nbsp;n&nbsp;]</div>"},
                  {"t": "body", "cls": "sm", "html": "This is the simple random sampling formula. Section 6 "
                   "shows how clustering inflates it."},
                  {"t": "panel", "color": "green", "title": "Nepal DHS 2022, stunting", "html":
                   "p = 24.8% = 0.248; children measured (unweighted) n = 2,687.<br>"
                   "p(1 &minus; p) = 0.248 &times; 0.752 = 0.1865.<br>"
                   "0.1865 &divide; 2,687 = 0.0000694.<br>"
                   "&radic;0.0000694 = 0.00833, so SE &asymp; <strong>0.83 percentage points</strong>.<br>"
                   "95% interval: 24.8 &plusmn; 1.96 &times; 0.83 = 24.8 &plusmn; 1.63, "
                   "i.e. <strong>23.2% to 26.4%</strong> (before any design effect)."}],
              "right": [
                  {"t": "body", "html": "Source for p and n: The DHS Program API, indicator CN_NUTS_C_HA2, "
                   "survey NP2022DHS. The published DHS report gives its own standard errors computed "
                   "with the full design; they are larger than this simple version, for reasons "
                   "Section 6 explains."},
                  {"t": "hbox", "color": "cyan", "html": "Three habits from this slide: square-root of "
                   "p(1&minus;p)/n; multiply by 1.96 for 95%; and treat the result as a floor until "
                   "the design effect is applied."}]},
         ]},

        {"type": "content", "label": "Comparing countries", "title": "Stunting across South Asia, with the sample behind each figure",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "qmSaChart",
                        "title": "Children under 5 stunted (%), most recent survey in the DHS Program API",
                        "source": "The DHS Program API, indicator CN_NUTS_C_HA2; Pakistan DHS 2017&ndash;18, NFHS-5 2019&ndash;21, Bangladesh DHS 2022, Nepal DHS 2022",
                        "type": "bar",
                        "data": {"labels": ["Pakistan 2017-18", "India 2019-21", "Nepal 2022", "Bangladesh 2022"],
                                 "datasets": [{"label": "% stunted", "data": [37.6, 35.5, 24.8, 23.6],
                                               "backgroundColor": ["#B45309", "#B45309", "#0369A1", "#0369A1"]}]},
                        "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ beginAtZero:true, title:{display:true,text:'per cent of children under 5'} } } }"}}],
              "right": [
                  {"t": "table",
                   "head": ["Survey", "n (unweighted)", "SRS SE"],
                   "rows": [["Pakistan 2017&ndash;18", "3,492", "0.82"], ["India 2019&ndash;21", "206,407", "0.11"],
                            ["Nepal 2022", "2,687", "0.83"], ["Bangladesh 2022", "4,260", "0.65"]]},
                  {"t": "body", "cls": "sm", "html": "India's sample of children is about 48 times "
                   "Bangladesh's, because NFHS-5 was designed for district estimates. The surveys are "
                   "also four to five years apart, so the bars are not a single moment in time. India's "
                   "NFHS-6 (2023&ndash;24) puts stunting at 29.3%; it is not yet in the DHS API, so its "
                   "sample size is not available here and this deck's worked standard errors use NFHS-5."}]},
         ]},

        {"type": "content", "label": "Small areas", "title": "Precision collapses below the state",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "green", "title": "National: India, NFHS-5", "html":
                   "p = 0.355, n = 206,407.<br>SE = &radic;(0.355 &times; 0.645 &divide; 206,407) = "
                   "&radic;0.00000111 = 0.00105, about <strong>0.11 points</strong>.<br>95% interval "
                   "&plusmn;0.21 points: 35.3% to 35.7%."},
                  {"t": "panel", "color": "red", "title": "District: 300 measured children (illustrative)", "html":
                   "Same p = 0.355, n = 300.<br>SE = &radic;(0.229 &divide; 300) = &radic;0.000763 = "
                   "0.0276, about <strong>2.8 points</strong>.<br>95% interval &plusmn;5.4 points. With a "
                   "design effect of 1.95, multiply by &radic;1.95 = 1.40: &plusmn;7.6 points, roughly "
                   "28% to 43%."}],
              "right": [
                  {"t": "body", "html": "District fact sheets are among the most quoted products of NFHS-5, "
                   "and they rest on samples of a few hundred children per district. Two districts that "
                   "differ by 6 points, or one district that &quot;improved&quot; by 6 points between "
                   "rounds, may show nothing more than sampling noise."},
                  {"t": "hbox", "color": "amber", "html": "Rankings of districts are especially fragile: a "
                   "district can move ten places on noise alone. Ask for the interval before acting on "
                   "a district rank, and prefer groupings (top third, bottom third) to exact positions."}]},
         ]},

        {"type": "content", "label": "The square-root law", "title": "To halve the error, quadruple the sample",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "table",
                   "head": ["n", "SE of p = 0.35 (points)", "95% margin (points)"],
                   "rows": [["100", "4.77", "&plusmn;9.3"], ["400", "2.38", "&plusmn;4.7"],
                            ["1,600", "1.19", "&plusmn;2.3"], ["6,400", "0.60", "&plusmn;1.2"]]},
                  {"t": "body", "cls": "sm", "html": "Computed as &radic;(0.35 &times; 0.65 &divide; n) "
                   "&times; 100, then &times; 1.96, simple random sampling. Each fourfold increase in n "
                   "halves the error."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "What this means for budgets", "html":
                   "Precision is expensive at the margin. Going from &plusmn;4.7 to &plusmn;2.3 points "
                   "costs 1,200 extra interviews; going from &plusmn;2.3 to &plusmn;1.2 costs 4,800 more. "
                   "A commissioner should decide in advance what precision the decision needs. If the "
                   "programme would act the same way whether coverage is 60% or 66%, there is no point "
                   "paying for a survey that can tell them apart."},
                  {"t": "hbox", "color": "cyan", "html": "The question to ask a survey firm: what margin "
                   "of error will each reported subgroup have, after the design effect?"}]},
         ]},

        {"type": "content", "label": "Coverage", "title": "Who is outside the frame, and who did not answer",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "amber", "title": "Frame gaps", "html":
                   "Household surveys sample from lists of households. People living in institutions "
                   "(hostels, barracks, prisons, care homes), the houseless, many seasonal migrants at "
                   "worksites and residents of unlisted settlements are under-covered or excluded by "
                   "design. For some topics, such as migrant labour, disability or homelessness, the "
                   "excluded groups are exactly the ones the question is about."},
                  {"t": "hbox", "color": "cyan", "html": "Read the survey's definition of its population "
                   "before generalising from it."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Non-response bias, illustrated", "html":
                   "Illustrative (hypothetical figures): a phone survey reaches 70% of sampled households. If the 30% not "
                   "reached are poorer, the estimate of poverty is biased downward, and interviewing "
                   "more of the reachable households only gives a more precise estimate of the wrong "
                   "number. Weighting adjustments help only to the extent that the variables used to "
                   "adjust (say, district and household size) predict both response and the outcome."},
                  {"t": "body", "cls": "sm", "html": "Ask for response rates by stratum and by key "
                   "characteristics, and for a comparison of respondents with a known benchmark such "
                   "as the Census."}]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Survey weights and design effects"},

        {"type": "content", "label": "Why weights", "title": "Why survey records carry weights",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Design weight",
                   "def": "The inverse of a unit's probability of selection. A household selected with "
                   "probability 1 in 500 stands for 500 households; its weight is 500."},
                  {"t": "body", "cls": "sm", "html": "National surveys deliberately sample some groups at "
                   "higher rates than others: small states and union territories, urban areas, or "
                   "districts, so that each gets a usable sample. That makes the raw sample "
                   "unrepresentative of the country by construction. Weights undo it. Most survey "
                   "weights then add adjustments for non-response and for agreement with known "
                   "population totals."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "What happens without them", "html":
                   "If Goa, Sikkim and Delhi each receive a sample big enough for a state estimate, an "
                   "unweighted all-India figure gives each of them far more influence than their "
                   "population warrants. Means, proportions and totals all come out wrong, and the "
                   "error has a direction: toward whatever the over-sampled groups look like."},
                  {"t": "hbox", "color": "amber", "html": "Weighted estimates are the default for any "
                   "population figure from NFHS, PLFS or HCES. An unweighted figure needs a reason."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "A weight changes the answer",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "table",
                   "head": ["Illustrative", "Urban stratum", "Rural stratum"],
                   "rows": [["Households sampled", "400", "400"], ["Selection probability", "1 in 500", "1 in 2,000"],
                            ["Weight", "500", "2,000"], ["Mean MPCE in sample", "&#8377;7,000", "&#8377;4,000"]]},
                  {"t": "body", "cls": "sm", "html": "<strong>Unweighted mean</strong> = (400 &times; 7,000 "
                   "+ 400 &times; 4,000) &divide; 800 = &#8377;5,500.<br><strong>Weighted mean</strong> = "
                   "(400 &times; 500 &times; 7,000 + 400 &times; 2,000 &times; 4,000) &divide; "
                   "(400 &times; 500 + 400 &times; 2,000) = 4,600,000,000 &divide; 1,000,000 = "
                   "<strong>&#8377;4,600</strong>."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Reading the arithmetic", "html":
                   "The sample has equal numbers of urban and rural households, but the population has "
                   "four rural households for every urban one (2,000 &divide; 500 = 4). The weights "
                   "restore that balance. The unweighted mean overstates consumption by &#8377;900, "
                   "about 20%, purely because cheaper-to-reach urban households were over-represented "
                   "in the sample."},
                  {"t": "hbox", "color": "cyan", "html": "The sum of the weights, 1,000,000, is the "
                   "estimated number of households in the population. Totals need weights that sum to "
                   "the population; NFHS weights do not, as the next slide shows."}]},
         ]},

        {"type": "content", "label": "NFHS and DHS", "title": "NFHS weights: divide v005 by 1,000,000",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "The DHS Program's guide <em>Using Datasets for Analysis</em> is "
                   "explicit: decimal points are not stored in the weight variables, and &quot;analysts "
                   "need to divide the sampling weight they are using by 1,000,000&quot;."},
                  {"t": "table",
                   "head": ["Unit of analysis", "Weight variable"],
                   "rows": [["Households, household members", "hv005"], ["Women, children", "v005"],
                            ["Men", "mv005"], ["Domestic violence module", "d005"]]},
                  {"t": "raw", "html": "<div style='font-family:monospace;font-size:0.95rem;margin:0.3rem 0;'>"
                   "generate wgt = v005/1000000<br>tab stunted [iweight=wgt]</div>"}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "These are relative weights", "html":
                   "DHS weights are scaled so that the weighted sample size stays close to the unweighted "
                   "one. For NFHS-5 stunting the DHS API reports 206,407 children measured and a weighted "
                   "count of 201,276. Such weights give correct proportions and means; they cannot give "
                   "a population total. To estimate how many million children are stunted, multiply the "
                   "weighted proportion by a population figure from another source."},
                  {"t": "panel", "color": "red", "title": "The quiet error", "html":
                   "Forgetting to divide by 1,000,000 leaves weighted means and proportions unchanged, "
                   "because the constant cancels. It multiplies every weighted count by a million, and "
                   "in some software it shrinks standard errors toward zero. The figure looks fine; the "
                   "significance stars do not."}]},
         ]},

        {"type": "content", "label": "PLFS", "title": "PLFS weights: the MLTS rules from the README",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "cls": "sm", "html": "MoSPI's PLFS unit-level README defines MLTS as the "
                   "&quot;weight or multiplier (in two places of decimal) calculated at the level of Second "
                   "Stage Stratum&quot;, and gives three rules:"},
                  {"t": "table",
                   "head": ["Estimate wanted", "Final weight"],
                   "rows": [["One sub-sample only", "MLTS &divide; 100"],
                            ["Both sub-samples combined, where NSS = NSC", "MLTS &divide; 100"],
                            ["Both sub-samples combined, where NSS &ne; NSC", "MLTS &divide; 200"],
                            ["Annual, from all quarters", "the above, divided by the number of quarters"]]},
                  {"t": "body", "cls": "sm", "html": "NSS is the number of FSUs surveyed within a quarter "
                   "&times; visit &times; sector &times; state &times; stratum &times; sub-stratum for the "
                   "sub-sample; NSC is the same count for the combined sub-samples."}],
              "right": [
                  {"t": "panel", "color": "green", "title": "Worked (illustrative MLTS)", "html":
                   "A record carries MLTS = 2,450,000.<br>Sub-sample estimate: 2,450,000 &divide; 100 = "
                   "24,500.<br>Combined, NSS &ne; NSC: 2,450,000 &divide; 200 = 12,250.<br>Annual combined "
                   "from four quarters: 12,250 &divide; 4 = 3,062.5.<br><br>Apply the rule record by "
                   "record: within one dataset some strata have NSS = NSC and others do not."},
                  {"t": "hbox", "color": "red", "html": "Using MLTS/100 everywhere roughly doubles "
                   "weighted totals in the strata where NSS &ne; NSC. Rates barely move, so the error "
                   "survives casual checking."}]},
         ]},

        {"type": "content", "label": "Weighting errors", "title": "Common weighting mistakes and how they show",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Mistake", "What goes wrong", "How to catch it"],
              "rows": [
                  ["No weights at all", "Over-sampled states, sectors or groups dominate", "Compare unweighted and weighted shares of states with the published report"],
                  ["NFHS weight not divided by 1,000,000", "Counts inflated a million-fold; SEs can be wrong", "Weighted N should be close to unweighted N"],
                  ["PLFS: MLTS/100 for a combined estimate everywhere", "Totals inflated where NSS &ne; NSC", "Weighted population should match the PLFS report's estimate"],
                  ["PLFS: quarters pooled without dividing", "Annual totals four times too large", "Same check against the report"],
                  ["Women's weight used for men", "Wrong population represented", "Match weight to file: v005 women, mv005 men"],
                  ["Dropping rows to get a subgroup", "SEs too small (see the slide on software)", "Use subpopulation options"]]},
             {"t": "body", "cls": "sm", "html": "The fastest single check on any weighted analysis is to "
              "reproduce one headline number from the official report, to the decimal, before computing "
              "anything new. NFHS fact sheets and PLFS annual reports publish dozens of such numbers. If "
              "your code cannot reproduce them, it is wrong somewhere, and the fault is usually in the "
              "weights, the filters or the merge."},
         ]},

        {"type": "content", "label": "Clustering", "title": "The design effect: why clustered samples are less precise",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Households in the same village share water sources, health "
                   "workers, prices and weather, so they resemble each other. Twenty households from one "
                   "village carry less independent information than twenty households from twenty villages."},
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.3rem;margin:0.4rem 0;'>"
                   "deff&nbsp;&asymp;&nbsp;1&nbsp;+&nbsp;(m&nbsp;&minus;&nbsp;1)&nbsp;&rho;</div>"},
                  {"t": "body", "cls": "sm", "html": "m is the number of interviews per cluster and &rho; "
                   "(rho) the intra-cluster correlation, the share of variation that lies between "
                   "clusters. This is Kish's approximation for equal-sized clusters."}],
              "right": [
                  {"t": "panel", "color": "green", "title": "Worked (illustrative)", "html":
                   "m = 20 children per village, &rho; = 0.05.<br>deff = 1 + 19 &times; 0.05 = "
                   "<strong>1.95</strong>.<br>Effective sample size = 2,000 &divide; 1.95 = "
                   "<strong>1,026</strong>.<br>Standard errors grow by &radic;1.95 = 1.40."},
                  {"t": "hbox", "color": "amber", "html": "Even a small &rho; matters when clusters are "
                   "large. With m = 40 and the same &rho;, deff = 2.95: almost two-thirds of the "
                   "interviews add no independent information about that indicator. Outcomes tied to "
                   "place, such as water source or electrification, have high &rho; and larger design "
                   "effects."}]},
         ]},

        {"type": "content", "label": "Stratification", "title": "Stratification usually helps, clustering usually hurts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "green", "title": "Stratification", "html":
                   "Sampling separately within states, or within rural and urban sectors, removes the "
                   "chance that the sample happens to contain too many of one kind. Where the outcome "
                   "differs between strata, as consumption differs between rural and urban India, "
                   "stratification reduces the standard error. Its design effect is usually below 1."},
                  {"t": "body", "cls": "sm", "html": "Unequal weights, by contrast, add variance: a sample "
                   "where a few households carry very large weights is less precise than one with "
                   "similar weights. Kish's rule of thumb is a factor of 1 + CV&sup2;, where CV is the "
                   "coefficient of variation of the weights."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Clustering", "html":
                   "Selecting villages and then households within them saves listing and travel costs, "
                   "which is why every national household survey in South Asia does it. The price is "
                   "the design effect on the previous slide."},
                  {"t": "hbox", "color": "indigo", "html": "A survey report that gives one overall "
                   "design effect is giving an average. Design effects differ by indicator: they are "
                   "small for individual traits like age and large for community traits like water "
                   "source. Look for the sampling-errors appendix, which NFHS reports carry for "
                   "selected indicators."}]},
         ]},

        {"type": "content", "label": "Software", "title": "Tell the software about the design",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Weights alone fix the point estimate. Correct standard errors "
                   "also need the <strong>strata</strong> and the <strong>primary sampling units</strong>. "
                   "Stata's <code>svyset</code> and R's <code>survey</code> package take all three and "
                   "compute standard errors by Taylor linearisation."},
                  {"t": "raw", "html": "<div style='font-family:monospace;font-size:0.9rem;margin:0.3rem 0;line-height:1.5'>"
                   "* Stata, NFHS women's file<br>gen wgt = v005/1000000<br>"
                   "svyset v021 [pweight=wgt], strata(v022)<br>svy: mean anaemic</div>"},
                  {"t": "body", "cls": "sm", "html": "In DHS files v021 is the PSU and v022 the sampling "
                   "stratum; check the recode manual for the survey you use."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Subgroups: keep the whole sample", "html":
                   "To estimate for Dalit women or for one state, do not delete the other rows first. "
                   "Use <code>svy, subpop()</code> in Stata or <code>subset()</code> on the design object "
                   "in R. Dropping rows discards the PSUs that contain no members of the subgroup, and "
                   "the software then understates the standard error."},
                  {"t": "hbox", "color": "cyan", "html": "Ask any analyst: which variable did you use as "
                   "PSU, which as strata, and how did you handle subgroups? Three short answers tell you "
                   "whether the standard errors can be trusted."}]},
         ]},

        {"type": "content", "label": "Checklist", "title": "A weighting and design checklist",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "bullets", "color": "green", "items": [
                      "Right file for the unit of analysis (household, person, woman, child)",
                      "Right weight for that file, scaled as the documentation says",
                      "PSU and strata declared before any standard error is computed",
                      "Subgroups estimated with subpopulation options, never by deleting rows",
                      "One published headline figure reproduced exactly before new analysis"]}],
              "right": [
                  {"t": "bullets", "color": "amber", "items": [
                      "Report weighted estimates and unweighted sample sizes together",
                      "State the design effect for key indicators, or the design-based SEs",
                      "Flag small denominators: DHS tables put figures from 25&ndash;49 unweighted cases in parentheses and suppress those under 25",
                      "Do not add weights from two different surveys or rounds",
                      "Keep the weighting code in the deliverable"]},
                  {"t": "hbox", "color": "indigo", "html": "Most weighting mistakes leave percentages "
                   "almost right and standard errors or totals badly wrong, so the check must cover "
                   "all three."}]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Intervals, tests and p-values"},

        {"type": "content", "label": "Confidence intervals", "title": "What a 95% confidence interval says",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.4rem 0;'>"
                   "estimate&nbsp;&plusmn;&nbsp;1.96&nbsp;&times;&nbsp;SE</div>"},
                  {"t": "body", "html": "The interval is a statement about the <strong>procedure</strong>. "
                   "If the survey were repeated many times and an interval built the same way each time, "
                   "about 95% of those intervals would contain the true population value. Any single "
                   "interval either contains it or does not; we cannot know which."},
                  {"t": "body", "cls": "sm", "html": "For 90% intervals use 1.645; for 99% use 2.576. Wider "
                   "intervals buy more confidence with less precision."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "How to say it in a report", "html":
                   "&quot;Stunting is estimated at 37.6% (95% CI 35.3% to 39.9%).&quot; A reader can see "
                   "at once that 36% and 39% are both consistent with the data, and that 30% is not. "
                   "That is far more useful than a lone point estimate given to one decimal place, which "
                   "suggests a precision the survey does not have."},
                  {"t": "panel", "color": "amber", "title": "What the interval leaves out", "html":
                   "It covers sampling error under the assumed design. It does not cover frame gaps, "
                   "non-response or measurement error. A narrow interval around a biased estimate is "
                   "precisely wrong."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "A confidence interval with the design effect",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "green", "title": "Pakistan DHS 2017&ndash;18, stunting", "html":
                   "p = 0.376, n = 3,492 (DHS API, CN_NUTS_C_HA2).<br>"
                   "Simple random SE = &radic;(0.376 &times; 0.624 &divide; 3,492) = &radic;(0.2346 &divide; 3,492) "
                   "= &radic;0.0000672 = 0.0082, i.e. 0.82 points.<br>"
                   "SRS interval: 37.6 &plusmn; 1.96 &times; 0.82 = 37.6 &plusmn; 1.6 &rarr; 36.0% to 39.2%."},
                  {"t": "panel", "color": "amber", "title": "Now allow for clustering (illustrative deff = 2)", "html":
                   "SE &times; &radic;2 = 0.82 &times; 1.414 = 1.16 points.<br>"
                   "Interval: 37.6 &plusmn; 1.96 &times; 1.16 = 37.6 &plusmn; 2.27 &rarr; "
                   "<strong>35.3% to 39.9%</strong>."}],
              "right": [
                  {"t": "body", "html": "The interval widened by about 40%, from &plusmn;1.6 to &plusmn;2.3 "
                   "points, once clustering was allowed for. A design effect of 2 is an assumption made "
                   "for teaching; the Pakistan DHS final report publishes design-based standard errors "
                   "for its key indicators, and those should be used in real work."},
                  {"t": "hbox", "color": "cyan", "html": "When a report gives a confidence interval, check "
                   "whether it says &quot;design-based&quot;, &quot;accounting for clustering&quot; or "
                   "&quot;svy&quot;. If it says nothing, assume it is too narrow."}]},
         ]},

        {"type": "content", "label": "Comparing two estimates", "title": "Is Nepal different from Bangladesh?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "cls": "sm", "html": "Bangladesh DHS 2022: 23.6% stunted, SE 0.65 (n = 4,260). "
                   "Nepal DHS 2022: 24.8%, SE 0.83 (n = 2,687). Simple random SEs computed from the DHS API "
                   "denominators."},
                  {"t": "panel", "color": "green", "title": "Test the difference directly", "html":
                   "Difference = 24.8 &minus; 23.6 = 1.2 points.<br>"
                   "SE of the difference for two independent samples = &radic;(0.65&sup2; + 0.83&sup2;) = "
                   "&radic;(0.42 + 0.69) = &radic;1.11 = 1.05.<br>"
                   "z = 1.2 &divide; 1.05 = <strong>1.14</strong>, below 1.96. Even before any design "
                   "effect, the data cannot distinguish the two countries."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "The overlap shortcut and its trap", "html":
                   "If two 95% intervals do not overlap, the difference is significant. The reverse does "
                   "not hold: two intervals can overlap a little while the difference is still "
                   "significant, because the SE of a difference is smaller than the sum of the two SEs. "
                   "Compute the difference and its own SE whenever the comparison matters."},
                  {"t": "hbox", "color": "cyan", "html": "For two rounds of the same panel, or two groups "
                   "in the same clusters, the samples are not independent and this formula needs a "
                   "covariance term. Ask the analyst."}]},
         ]},

        {"type": "content", "label": "The logic", "title": "How a hypothesis test reasons",
         "blocks": [
             {"t": "flow", "steps": [
                 "NULL: assume no difference",
                 "STATISTIC: how far is the data from the null, in SEs?",
                 "REFERENCE: how often would that happen by chance?",
                 "P-VALUE: that probability",
                 "JUDGEMENT: with effect size and context"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "A test asks a narrow question: if there were in fact "
                        "no difference in the population, how surprising would a sample difference this "
                        "large be? The <strong>test statistic</strong> (z or t) measures the observed "
                        "difference in units of its standard error. A value beyond about &plusmn;2 would "
                        "occur by chance less than 5% of the time if the null were true."}],
              "right": [{"t": "panel", "color": "indigo", "title": "Two-sided by default", "html":
                         "Most programme questions allow an effect in either direction: a scheme might "
                         "raise or lower enrolment. A two-sided test counts surprises at both ends. "
                         "One-sided tests halve the p-value and should be chosen before seeing the data, "
                         "with a stated reason, or not at all."}]},
         ]},

        {"type": "content", "label": "P-values", "title": "Six principles from the American Statistical Association",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [
                  {"t": "bullets", "sm": True, "items": [
                      "P-values can indicate how incompatible the data are with a specified statistical model.",
                      "P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone.",
                      "Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold.",
                      "Proper inference requires full reporting and transparency.",
                      "A p-value, or statistical significance, does not measure the size of an effect or the importance of a result.",
                      "By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis."]},
                  {"t": "body", "cls": "sm", "html": "American Statistical Association, Statement on "
                   "Statistical Significance and P-Values, released 7 March 2016 (Wasserstein and Lazar, "
                   "<em>The American Statistician</em> 70(2))."}],
              "right": [
                  {"t": "quote", "text": "The p-value was never intended to be a substitute for scientific reasoning.",
                   "attr": "Ron Wasserstein, ASA executive director, press release of 7 March 2016"},
                  {"t": "hbox", "color": "amber", "html": "Principle 5 is the one most violated in "
                   "development reporting: a tiny, unimportant effect in a huge sample can have p &lt; "
                   "0.001."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "A two-group comparison, step by step",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "green", "title": "Illustrative: reading scores (hypothetical figures)", "html":
                   "100 children in tutored schools average 52 marks; 100 in comparison schools average "
                   "47. SD in both groups = 20 marks.<br>"
                   "Difference = 5 marks.<br>"
                   "SE of difference = 20 &times; &radic;(1/100 + 1/100) = 20 &times; 0.1414 = 2.83.<br>"
                   "t = 5 &divide; 2.83 = <strong>1.77</strong>; two-sided p &asymp; <strong>0.08</strong>.<br>"
                   "95% CI for the difference: 5 &plusmn; 1.96 &times; 2.83 = 5 &plusmn; 5.5 &rarr; "
                   "&minus;0.5 to 10.5 marks."}],
              "right": [
                  {"t": "body", "html": "The conventional verdict is &quot;not significant at 5%&quot;. "
                   "The better reading is that the data are consistent with anything from no effect to "
                   "a gain of about 10 marks, which is half a standard deviation. The study was too small "
                   "to settle the question; it did not show the tutoring failed."},
                  {"t": "hbox", "color": "cyan", "html": "Report the difference, its interval and the "
                   "p-value together. The interval carries most of the information; p = 0.08 versus "
                   "p = 0.04 is a small difference in evidence, and the 0.05 line is a convention."}]},
         ]},

        {"type": "content", "label": "A real comparison", "title": "Did stunting in India fall between NFHS rounds?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "qmNfhsChart",
                        "title": "Children under 5 stunted, India (%)",
                        "source": "The DHS Program API (CN_NUTS_C_HA2): NFHS-3 2005&ndash;06, NFHS-4 2015&ndash;16, NFHS-5 2019&ndash;21; NFHS-6 2023&ndash;24 India Fact Sheet (provisional)",
                        "type": "bar",
                        "data": {"labels": ["NFHS-3 2005-06", "NFHS-4 2015-16", "NFHS-5 2019-21", "NFHS-6 2023-24"],
                                 "datasets": [{"label": "% stunted", "data": [48.0, 38.4, 35.5, 29.3], "backgroundColor": "#0369A1"}]},
                        "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, max:60, title:{display:true,text:'per cent'} } } }"}}],
              "right": [
                  {"t": "panel", "color": "green", "title": "Testing NFHS-4 against NFHS-5", "html":
                   "SE (NFHS-4) = &radic;(0.384 &times; 0.616 &divide; 232,440) = 0.10 points.<br>"
                   "SE (NFHS-5) = &radic;(0.355 &times; 0.645 &divide; 206,407) = 0.11 points.<br>"
                   "SE of the difference = &radic;(0.10&sup2; + 0.11&sup2;) = 0.15.<br>"
                   "z = 2.9 &divide; 0.15 &asymp; <strong>20</strong>; with a design effect of 2, about 14. "
                   "The fall is far beyond sampling noise."},
                  {"t": "body", "cls": "sm", "html": "Statistical significance settles only chance. Whether "
                   "2.9 points over about four years is a large change for policy, and what caused it, are "
                   "separate questions. The bigger fall, 9.6 points, came between NFHS-3 and NFHS-4, a "
                   "gap of ten years. NFHS-6 (2023&ndash;24) reports a further fall to 29.3%, 6.2 points "
                   "below NFHS-5; its sample size is not yet in the DHS API, so the test is shown on "
                   "the earlier pair."}]},
         ]},

        {"type": "content", "label": "Two kinds of mistake", "title": "Type I and type II errors",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "In truth: no effect", "In truth: a real effect"],
              "rows": [
                  ["Test says: significant", "<strong>Type I error</strong> (false positive). Probability &alpha;, usually 5%.", "Correct detection. Probability = power, usually designed at 80%."],
                  ["Test says: not significant", "Correct. Probability 1 &minus; &alpha;.", "<strong>Type II error</strong> (false negative). Probability &beta; = 1 &minus; power."]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "The two errors trade off. Demanding stronger "
                        "evidence (&alpha; = 1%) lowers false positives and raises false negatives unless "
                        "the sample grows. A programme evaluation with 50% power will miss a real effect "
                        "half the time, and its &quot;no significant impact&quot; headline will be "
                        "read as failure."}],
              "right": [{"t": "panel", "color": "amber", "title": "Which error costs more?", "html":
                         "Scaling up an ineffective programme wastes money (type I). Abandoning an effective "
                         "one wastes the benefit (type II). The balance is a policy judgement, and the "
                         "conventional 5% and 80% are defaults, open to change with a stated reason."}]},
         ]},

        {"type": "content", "label": "Many tests", "title": "Multiple comparisons and the garden of forking paths",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "green", "title": "Worked: twenty outcomes, no true effects", "html":
                   "Each test has a 5% chance of a false positive.<br>"
                   "Chance that none of 20 independent tests is significant = 0.95<sup>20</sup> = 0.358.<br>"
                   "Chance of at least one false positive = 1 &minus; 0.358 = <strong>64%</strong>.<br>"
                   "Expected number of false positives = 20 &times; 0.05 = 1."},
                  {"t": "body", "cls": "sm", "html": "An evaluation that tests twenty outcomes across four "
                   "subgroups and reports the three significant ones has told you very little."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Defences a commissioner can require", "html":
                   "A <strong>pre-analysis plan</strong> registered before data arrive (the AEA RCT Registry "
                   "and 3ie's RIDIE are used for development studies) naming primary outcomes. "
                   "<strong>Indices</strong> that combine related outcomes into one. "
                   "<strong>Adjusted p-values</strong> (Bonferroni divides &alpha; by the number of tests; "
                   "false discovery rate methods are less conservative). Full reporting of every outcome "
                   "tested, significant or not."},
                  {"t": "hbox", "color": "red", "html": "Trying specifications until one crosses 0.05 is "
                   "p-hacking, the practice the ASA statement names."}]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Correlation, causation, regression"},

        {"type": "content", "label": "Association", "title": "The correlation coefficient",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Pearson's r",
                   "def": "A number from &minus;1 to +1 measuring how closely two numeric variables follow a "
                   "straight line. +1 is a perfect rising line, &minus;1 a perfect falling line, 0 no "
                   "linear pattern."},
                  {"t": "body", "cls": "sm", "html": "r&sup2; is the share of the variation in one variable "
                   "that a straight line in the other accounts for. An r of 0.5 sounds large and gives "
                   "r&sup2; = 0.25: three-quarters of the variation lies elsewhere. An r of 0.3 gives "
                   "0.09."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "What r cannot see", "html":
                   "r measures <em>linear</em> association only. A U-shaped relation, such as the one "
                   "often found between age and many health outcomes, can have r near 0 while the two "
                   "variables are tightly linked. r is also sensitive to outliers: one extreme district "
                   "can create or destroy a correlation among thirty. And r has no units, so it says "
                   "nothing about how much y changes when x changes. For that you need the regression "
                   "slope."},
                  {"t": "hbox", "color": "cyan", "html": "Always look at the scatter plot before "
                   "reporting r. The Bivariate Analysis 101 deck works through rank correlations and "
                   "other alternatives."}]},
         ]},

        {"type": "content", "label": "See it", "title": "Reading a scatter plot",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "qmScatterChart",
                        "title": "Illustrative: female literacy and institutional births, 14 districts",
                        "source": "Illustrative data for teaching; not survey estimates",
                        "type": "scatter",
                        "data": {"datasets": [{"label": "district",
                                               "data": [{"x": 48, "y": 61}, {"x": 52, "y": 70}, {"x": 55, "y": 66}, {"x": 58, "y": 74},
                                                        {"x": 60, "y": 79}, {"x": 63, "y": 76}, {"x": 66, "y": 84}, {"x": 68, "y": 81},
                                                        {"x": 71, "y": 88}, {"x": 74, "y": 86}, {"x": 77, "y": 92}, {"x": 80, "y": 90},
                                                        {"x": 84, "y": 96}, {"x": 62, "y": 95}],
                                               "backgroundColor": "rgba(3,105,161,0.75)", "pointRadius": 5}]},
                        "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'women literate (%)'} }, y:{ title:{display:true,text:'institutional births (%)'} } } }"}}],
              "right": [
                  {"t": "body", "cls": "sm", "html": "Thirteen districts lie close to a rising line; one "
                   "(62% literacy, 95% institutional births) sits well above it. Read a scatter in this "
                   "order: direction (rising), form (roughly straight), strength (tight), exceptions (one "
                   "outlier worth a field visit)."},
                  {"t": "body", "cls": "sm", "html": "The outlier may be a district with a strong "
                   "conditional cash transfer, a large private hospital sector, or a data error. The "
                   "plot cannot say which; it says where to look."},
                  {"t": "hbox", "color": "amber", "html": "The pattern does not show that literacy causes "
                   "institutional delivery. Richer districts tend to have both."}]},
         ]},

        {"type": "content", "label": "Causation", "title": "Three reasons an association can mislead",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "red", "title": "Confounding", "html":
                   "A third factor drives both. Households with more schooling also tend to have more "
                   "land, better roads and more connections; any of these may explain their higher "
                   "earnings. Comparing educated and uneducated households compares all of these at once."},
                  {"t": "panel", "color": "amber", "title": "Reverse causation", "html":
                   "The outcome drives the &quot;cause&quot;. Villages with more self-help groups may "
                   "have higher incomes because better-off villages form more groups, as well as, or "
                   "instead of, the reverse."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Selection", "html":
                   "Who receives the programme is not random. If NGOs choose villages that are easier "
                   "to work in, programme villages will look better whether or not the programme did "
                   "anything. If the neediest are targeted, programme villages may look worse even "
                   "when it works."},
                  {"t": "hbox", "color": "cyan", "html": "Each of these produces a real, reproducible, "
                   "statistically significant association. Significance cannot tell you which story "
                   "is true; the design of the comparison can. The Causal Inference and Impact "
                   "Evaluation decks take this further."}]},
         ]},

        {"type": "content", "label": "A paradox", "title": "Simpson's paradox: the aggregate can reverse the parts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "table",
                   "head": ["Illustrative", "Scheme users", "Non-users"],
                   "rows": [["Urban: institutional births", "90 of 100 = 90%", "160 of 200 = 80%"],
                            ["Rural: institutional births", "120 of 400 = 30%", "25 of 100 = 25%"],
                            ["All areas", "210 of 500 = <strong>42%</strong>", "185 of 300 = <strong>62%</strong>"]]},
                  {"t": "body", "cls": "sm", "html": "Users do better in urban areas (90% against 80%) and "
                   "in rural areas (30% against 25%), yet worse overall (42% against 62%). The scheme "
                   "enrolled mostly rural women, where institutional births are low for everyone."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "The classic case", "html":
                   "Bickel, Hammel and O'Connell (1975, <em>Science</em> 187: 398&ndash;404) examined "
                   "graduate admissions at Berkeley. Aggregated, women appeared to be admitted at a lower "
                   "rate; department by department the bias largely disappeared, because women applied "
                   "more often to departments that admitted few applicants of either sex."},
                  {"t": "hbox", "color": "amber", "html": "Whenever a comparison mixes groups with very "
                   "different baselines (rural and urban, states, castes), look at the comparison "
                   "within groups before trusting the total."}]},
         ]},

        {"type": "content", "label": "Regression", "title": "Regression as the best-fitting line",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.4rem 0;'>"
                   "y&nbsp;=&nbsp;a&nbsp;+&nbsp;b&nbsp;x&nbsp;+&nbsp;error</div>"},
                  {"t": "body", "cls": "sm", "html": "Ordinary least squares picks the intercept a and slope "
                   "b that make the squared vertical distances from the points to the line as small as "
                   "possible. The slope b answers the question r cannot: by how much does y change, on "
                   "average, when x is one unit higher?"},
                  {"t": "panel", "color": "green", "title": "Worked (illustrative)", "html":
                   "Monthly earnings (&#8377;) = 4,200 + 812 &times; years of schooling.<br>"
                   "Predicted for 10 years: 4,200 + 8,120 = &#8377;12,320.<br>"
                   "Predicted for 12 years: 4,200 + 9,744 = &#8377;13,944. The difference, "
                   "&#8377;1,624, is 2 &times; 812."}],
              "right": [
                  {"t": "panel", "color": "cyan", "title": "How to read the slope", "html":
                   "&quot;Among these workers, each additional year of schooling is associated with "
                   "&#8377;812 higher monthly earnings on average.&quot; Associated: the slope describes "
                   "the data, and becomes a causal effect only under the conditions on the next slides."},
                  {"t": "hbox", "color": "amber", "html": "The intercept is the prediction at x = 0, here "
                   "a worker with no schooling. It is often outside the data or meaningless (a household "
                   "of size zero) and rarely worth interpreting."}]},
         ]},

        {"type": "content", "label": "Controls", "title": "Multiple regression and omitted variable bias",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Adding variables lets each coefficient be read as the association "
                   "<strong>holding the others constant</strong>. In an earnings regression with "
                   "schooling, age, sex and urban residence, the schooling coefficient compares workers "
                   "of the same age, sex and location who differ in schooling."},
                  {"t": "body", "cls": "sm", "html": "This is statistical control, comparing within groups "
                   "the way the Simpson's paradox table did, done for many variables at once."}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Omitted variable bias", "html":
                   "If a variable that affects earnings and is correlated with schooling is left out "
                   "(family wealth, ability, social networks), the schooling coefficient absorbs part "
                   "of its effect. The bias has a predictable sign: a left-out factor that raises "
                   "earnings and goes with more schooling pushes the schooling coefficient up."},
                  {"t": "panel", "color": "amber", "title": "Controls can also hurt", "html":
                   "Controlling for a variable the treatment itself changes (occupation, in a schooling "
                   "regression) removes part of the effect you want to measure. Choose controls that "
                   "were fixed before the cause, and say why each is there."}]},
         ]},

        {"type": "content", "label": "Coefficients", "title": "Reading coefficients: units, dummies and logs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Model", "Coefficient", "Plain-language reading"],
              "rows": [
                  ["y in &#8377;, x in years", "b = 812", "Each extra year: &#8377;812 more per month on average"],
                  ["y in &#8377;, x a 0/1 dummy (female)", "b = &minus;2,950", "Women earn &#8377;2,950 less than otherwise similar men"],
                  ["ln(y), x in years", "b = 0.08", "Each extra year: about 8% more (exactly e<sup>0.08</sup> &minus; 1 = 8.3%)"],
                  ["ln(y), ln(x)", "b = 0.5", "A 1% rise in x goes with a 0.5% rise in y (an elasticity)"],
                  ["y binary (0/1), linear probability model", "b = 0.06", "6 percentage points higher probability"],
                  ["Interaction female &times; urban", "b = 1,100", "The urban gap differs for women by &#8377;1,100"]]},
             {"t": "body", "cls": "sm", "html": "All coefficients are illustrative. Two habits: always find the "
              "units of y and x before reading b, and for a dummy variable always find the omitted "
              "category, because the coefficient is a comparison with it. A &quot;Scheduled Caste&quot; "
              "dummy compared with &quot;all others&quot; and one compared with &quot;Others (general)&quot; "
              "answer different questions. For log approximations, the simple reading works well "
              "below about 0.1; above it, compute e<sup>b</sup> &minus; 1."},
         ]},

        {"type": "content", "label": "Causal designs", "title": "When can a coefficient be read as an effect?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "Source of comparison", "Key assumption", "Indian example of use"],
              "rows": [
                  ["Randomised trial", "Lottery decides who is treated", "Randomisation done and kept", "Remedial education in Mumbai and Vadodara (Banerjee et al., NBER WP 11904)"],
                  ["Difference-in-differences", "Change over time, treated against untreated", "Parallel trends without the programme", "Phased roll-out of a state scheme"],
                  ["Regression discontinuity", "Units just either side of a cut-off", "No sorting around the cut-off", "Eligibility by a score or population threshold"],
                  ["Instrumental variables", "A factor shifting treatment only", "Instrument affects outcome only through treatment", "Distance to a facility (often disputed)"],
                  ["Regression with controls", "Similar units, measured traits", "No unmeasured confounders", "The weakest; state it plainly"]]},
             {"t": "body", "cls": "sm", "html": "The design, decided before the data, is what makes the "
              "causal claim; regression is the arithmetic that estimates it. Duflo, Glennerster and "
              "Kremer's toolkit (NBER Technical Working Paper 0333, December 2006) remains the standard "
              "practical guide to randomised designs in development. Econometrics 101 and Impact "
              "Evaluation 101 cover these designs in depth."},
         ]},

        {"type": "content", "label": "Levels", "title": "The ecological fallacy: district patterns are not individual facts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Many quick analyses correlate district or state averages because "
                   "those are what fact sheets publish. A correlation across districts between female "
                   "literacy and institutional births describes districts. It does not show that literate "
                   "women are more likely to deliver in hospitals, though that may also be true."},
                  {"t": "body", "cls": "sm", "html": "Associations at the group level are often much "
                   "stronger than at the individual level, because averaging removes individual noise. "
                   "They can even have the opposite sign."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Practical rules", "html":
                   "State the unit in every sentence about a correlation (&quot;districts with higher "
                   "female literacy have more institutional births&quot;). Use unit-level data from "
                   "NFHS or PLFS when the question is about people. Weight districts by population if "
                   "the question is about the population, since an unweighted district analysis gives "
                   "Lakshadweep and Thane equal votes."},
                  {"t": "hbox", "color": "cyan", "html": "Multivariate Analysis 101 covers multilevel "
                   "models, which handle people within districts properly."}]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Effect sizes and power"},

        {"type": "content", "label": "How big", "title": "Effect size: the answer to how much",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "A p-value says whether an effect is distinguishable from zero. An "
                   "<strong>effect size</strong> says how large it is. Policy decisions turn on the "
                   "second: a nutrition programme that lowers stunting by 0.5 points with p &lt; 0.001 "
                   "and one that lowers it by 5 points with p = 0.08 call for different conversations."},
                  {"t": "bullets", "sm": True, "items": [
                      "<strong>Raw effects</strong> keep the units: percentage points, rupees, days, marks. They are the clearest for policy.",
                      "<strong>Standardised effects</strong> divide by a standard deviation, so outcomes on different scales can be compared or pooled.",
                      "<strong>Relative effects</strong> (risk ratios, odds ratios, percentage changes) compare against a baseline."]}],
              "right": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.35rem;margin:0.4rem 0;'>"
                   "d&nbsp;=&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>mean<sub>T</sub> &minus; mean<sub>C</sub></span>"
                   "&nbsp;/&nbsp;SD</div>"},
                  {"t": "panel", "color": "cyan", "title": "From the worked test in Section 7", "html":
                   "A 5-mark difference with an SD of 20 marks gives d = 5 &divide; 20 = 0.25. That "
                   "study's interval ran from &minus;0.5 to 10.5 marks, or about &minus;0.03 to 0.53 SD."},
                  {"t": "hbox", "color": "amber", "html": "Every result should come with its effect size in "
                   "natural units first, standardised second."}]},
         ]},

        {"type": "content", "label": "Benchmarks", "title": "Cohen's conventions, and why to use them cautiously",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "stats", "cols": 3, "cards": [
                      {"num": "0.2", "label": "small", "color": "cyan", "source": "Cohen (1988)"},
                      {"num": "0.5", "label": "medium", "color": "indigo", "source": "Cohen (1988)"},
                      {"num": "0.8", "label": "large", "color": "green", "source": "Cohen (1988)"}]},
                  {"t": "body", "cls": "sm", "html": "Jacob Cohen's <em>Statistical Power Analysis for the "
                   "Behavioral Sciences</em> (2nd edition, 1988) proposed these thresholds for d, with "
                   "0.1, 0.3 and 0.5 for a correlation r. He offered them as rough guides for "
                   "psychology where nothing better was known."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Context beats convention", "html":
                   "In school-based programmes in South Asia an effect of 0.2 SD on learning is "
                   "substantial, and many well-run programmes achieve less. Calling it &quot;small&quot; "
                   "because of Cohen's labels misleads a funder. A cheap programme with d = 0.1 that "
                   "reaches millions of children can matter more than an expensive one with d = 0.5 "
                   "that reaches a few hundred."},
                  {"t": "hbox", "color": "cyan", "html": "Judge an effect against effects of other "
                   "programmes on the same outcome, against its cost (Cost Effectiveness 101), and "
                   "against what would change a decision."}]},
         ]},

        {"type": "content", "label": "An Indian benchmark", "title": "Effect sizes from two Indian experiments",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "stats", "cols": 2, "cards": [
                      {"num": "0.14 &rarr; 0.28 SD", "label": "remedial teaching by young women from the community, all children in treatment schools, year 1 and year 2", "color": "green",
                       "source": "Banerjee, Cole, Duflo &amp; Linden, NBER WP 11904 (2005)"},
                      {"num": "0.35 &rarr; 0.47 SD", "label": "computer-assisted learning, mathematics, year 1 and year 2", "color": "cyan",
                       "source": "Banerjee, Cole, Duflo &amp; Linden, NBER WP 11904 (2005)"}]},
                  {"t": "body", "cls": "sm", "html": "Both experiments ran in Mumbai and Vadodara. The "
                   "authors report that the gains persisted for at least one year after children left "
                   "the programmes."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Turning SD into marks (illustrative)", "html":
                   "If the test's SD were 20 marks, 0.28 SD would be 0.28 &times; 20 = 5.6 marks, and "
                   "0.47 SD would be 9.4 marks. Translating back to the test's own units, or to "
                   "&quot;share of children who can read a paragraph&quot;, makes a result legible to "
                   "a district education officer in a way that &quot;0.28 SD&quot; is not."},
                  {"t": "hbox", "color": "amber", "html": "Standardised effects depend on the SD used. An "
                   "effect divided by the SD of a narrow, homogeneous sample looks larger than the same "
                   "effect divided by a national SD. Check which SD a paper used before comparing."}]},
         ]},

        {"type": "content", "label": "Power", "title": "Statistical power and its four ingredients",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "term", "word": "Power",
                   "def": "The probability that a study detects an effect of a given size, if that effect "
                   "really exists. Conventionally designed at 80%, at a 5% significance level."},
                  {"t": "body", "cls": "sm", "html": "Power is calculated before data collection, to choose "
                   "a sample size, or to state the smallest effect a fixed budget can detect. A power "
                   "calculation done after a null result to explain it away is of little use."}],
              "right": [
                  {"t": "table",
                   "head": ["Ingredient", "Raise it and power"],
                   "rows": [["Sample size (and number of clusters)", "rises"],
                            ["True effect size", "rises"],
                            ["Variance of the outcome", "falls"],
                            ["Intra-cluster correlation", "falls"],
                            ["Strictness of &alpha; (5% to 1%)", "falls"]]},
                  {"t": "hbox", "color": "cyan", "html": "In clustered designs the number of clusters "
                   "matters more than the number of households per cluster. Adding a 21st household "
                   "to each of 40 villages buys little; adding villages buys a lot."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "The minimum detectable effect",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.15rem;margin:0.4rem 0;'>"
                   "MDE&nbsp;=&nbsp;(z<sub>1&minus;&alpha;/2</sub>&nbsp;+&nbsp;z<sub>power</sub>)&nbsp;&times;&nbsp;"
                   "&radic;[1&nbsp;/&nbsp;(P(1&minus;P))]&nbsp;&times;&nbsp;&radic;(&sigma;&sup2;/N)</div>"},
                  {"t": "body", "cls": "sm", "html": "The form used in Duflo, Glennerster and Kremer "
                   "(2006) for individual randomisation. P is the share treated, N the total sample, "
                   "&sigma; the outcome SD. In SD units, set &sigma; = 1."},
                  {"t": "panel", "color": "green", "title": "N = 1,000, half treated, 5% two-sided, 80% power", "html":
                   "z values: 1.96 + 0.84 = 2.80.<br>&radic;[1 &divide; (0.5 &times; 0.5)] = &radic;4 = 2.<br>"
                   "&radic;(1 &divide; 1,000) = 0.0316.<br>"
                   "MDE = 2.80 &times; 2 &times; 0.0316 = <strong>0.177 SD</strong>."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Now cluster it (illustrative)", "html":
                   "Randomise 50 villages of 20 households instead, with &rho; = 0.05: deff = 1.95.<br>"
                   "MDE &times; &radic;1.95 = 0.177 &times; 1.40 = <strong>0.247 SD</strong>.<br>"
                   "The same 1,000 households can now detect only effects about 40% larger."},
                  {"t": "body", "cls": "sm", "html": "Read backwards: if the programme can plausibly move "
                   "the outcome by 0.15 SD, neither design is big enough, and the options are a "
                   "larger sample, a less noisy outcome, baseline covariates that cut variance, or not "
                   "running the evaluation."}]},
         ]},

        {"type": "content", "label": "Worked example", "title": "Sample size to detect a fall in stunting",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "raw", "html": "<div style='text-align:center;font-size:1.2rem;margin:0.4rem 0;'>"
                   "n per arm&nbsp;=&nbsp;(z<sub>&alpha;/2</sub>&nbsp;+&nbsp;z<sub>&beta;</sub>)&sup2;&nbsp;&times;&nbsp;"
                   "[p<sub>1</sub>(1&minus;p<sub>1</sub>)&nbsp;+&nbsp;p<sub>2</sub>(1&minus;p<sub>2</sub>)]&nbsp;/&nbsp;(p<sub>1</sub>&minus;p<sub>2</sub>)&sup2;</div>"},
                  {"t": "panel", "color": "green", "title": "From 35% to 30%, 5% two-sided, 80% power", "html":
                   "(1.960 + 0.842)&sup2; = 2.802&sup2; = 7.85.<br>"
                   "0.35 &times; 0.65 + 0.30 &times; 0.70 = 0.2275 + 0.2100 = 0.4375.<br>"
                   "(0.35 &minus; 0.30)&sup2; = 0.0025.<br>"
                   "n = 7.85 &times; 0.4375 &divide; 0.0025 = <strong>1,374 children per arm</strong>."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "With clustering (deff 1.95, illustrative)", "html":
                   "1,374 &times; 1.95 = <strong>2,679 children per arm</strong>, about 5,360 in all. "
                   "A baseline of 35% is close to India's NFHS-5 (2019&ndash;21) figure of 35.5%; "
                   "NFHS-6 (2023&ndash;24) reports 29.3% nationally."},
                  {"t": "body", "cls": "sm", "html": "A 5-point fall over a programme cycle is ambitious; "
                   "the national fall was 2.9 points between NFHS-4 and NFHS-5 and 6.2 points between "
                   "NFHS-5 and NFHS-6, each over about four years. "
                   "Halving the target effect to 2.5 points roughly quadruples the sample, to about 10,900 "
                   "children per arm with the same design effect. Most programme evaluations cannot "
                   "afford that, which is why many choose a more sensitive outcome such as mean "
                   "height-for-age z-score."}]},
         ]},

        {"type": "content", "label": "Small studies", "title": "Underpowered studies mislead twice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "red", "title": "First: false reassurance", "html":
                   "A study with 30% power usually finds nothing even when the programme works. Its "
                   "&quot;no significant effect&quot; becomes, in a ministry note, &quot;the programme "
                   "did not work&quot;. Absence of evidence from a small study is weak evidence of "
                   "absence. Report the confidence interval, which will show that large benefits were "
                   "not ruled out."},
                  {"t": "body", "cls": "sm", "html": "Check the reported minimum detectable effect against "
                   "what the programme could plausibly achieve."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Second: exaggerated discoveries", "html":
                   "When a low-powered study does cross p &lt; 0.05, the estimate that got it there is "
                   "usually much larger than the true effect, because only the lucky draws clear the "
                   "bar. Gelman and Carlin (2014, <em>Perspectives on Psychological Science</em> 9(6)) "
                   "call this a type M (magnitude) error, and also describe type S errors, where the "
                   "sign is wrong. Scale-ups planned on such estimates disappoint."},
                  {"t": "hbox", "color": "cyan", "html": "Distrust a striking effect from a small pilot "
                   "until a larger study repeats it."}]},
         ]},

        {"type": "content", "label": "Commissioning", "title": "Power in a commissioning conversation",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Ask the evaluator", "A good answer includes", "A warning sign"],
              "rows": [
                  ["What is the primary outcome?", "One named indicator, measured the same way in both arms", "&quot;Several outcomes&quot; with no ranking"],
                  ["What effect can the design detect?", "An MDE in natural units and SD units, with the formula", "&quot;The sample is large&quot;"],
                  ["Where do the variance and &rho; come from?", "A named prior survey, such as NFHS district data or a baseline", "Defaults with no source"],
                  ["How many clusters?", "A number, with the design effect it implies", "Only a household count"],
                  ["What if take-up is 60%?", "MDE adjusted for partial compliance (it grows by 1 &divide; 0.6)", "No mention of take-up"],
                  ["Is there a pre-analysis plan?", "Registered before endline data", "Analysis decided after seeing results"]]},
             {"t": "body", "cls": "sm", "html": "Partial take-up matters more than it looks: if only 60% of "
              "the treatment group participates, the intention-to-treat effect is diluted to 60% of the "
              "effect on participants, and the sample needed rises by a factor of 1 &divide; 0.6&sup2; = "
              "2.8."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Reading and commissioning analysis"},

        {"type": "content", "label": "Anatomy", "title": "A results table, as it appears in a report",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [
                  {"t": "table",
                   "head": ["Dependent variable: monthly earnings (&#8377;)", "Coef.", "SE", "t", "p"],
                   "rows": [["Years of schooling", "812", "140", "5.80", "&lt;0.001"],
                            ["Female (ref: male)", "&minus;2,950", "610", "&minus;4.84", "&lt;0.001"],
                            ["Age (years)", "95", "30", "3.17", "0.002"],
                            ["Urban (ref: rural)", "1,840", "520", "3.54", "&lt;0.001"],
                            ["Constant", "4,200", "900", "4.67", "&lt;0.001"],
                            ["N = 4,812; R&sup2; = 0.21", "", "", "", ""]]},
                  {"t": "body", "cls": "sm", "html": "Illustrative table. Notes: OLS; standard errors "
                   "clustered at village level; survey weights applied."}],
              "right": [
                  {"t": "body", "cls": "sm", "html": "Read a table in this order. First the title and the "
                   "dependent variable, with its units. Then N, and whether it matches the sample "
                   "described in the methods. Then the notes: weights, clustering, the estimator. Only "
                   "then the coefficients, each with its unit and its reference category."},
                  {"t": "hbox", "color": "cyan", "html": "The t-statistic is the coefficient divided by "
                   "its standard error: 812 &divide; 140 = 5.80. Check one or two rows yourself; "
                   "errors in transcription are common."}]},
         ]},

        {"type": "content", "label": "Row by row", "title": "Reading the table: intervals and meaning",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "green", "title": "95% intervals from coef &plusmn; 1.96 &times; SE", "html":
                   "Schooling: 812 &plusmn; 274.4 &rarr; &#8377;538 to &#8377;1,086 per year.<br>"
                   "Female: &minus;2,950 &plusmn; 1,195.6 &rarr; &minus;&#8377;4,146 to &minus;&#8377;1,754.<br>"
                   "Age: 95 &plusmn; 58.8 &rarr; &#8377;36 to &#8377;154 per year.<br>"
                   "Urban: 1,840 &plusmn; 1,019.2 &rarr; &#8377;821 to &#8377;2,859."},
                  {"t": "body", "cls": "sm", "html": "Every interval excludes zero, consistent with every "
                   "p-value being below 0.05. The intervals are wide: the schooling return could be two-thirds "
                   "or one-and-a-third of the point estimate."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "What the table supports", "html":
                   "&quot;Among these workers, women earn about &#8377;2,950 a month less than men of "
                   "the same schooling, age and location (95% CI &#8377;1,754 to &#8377;4,146).&quot; "
                   "This is a conditional gap. It does not identify discrimination as the cause, since "
                   "occupation, hours and sector are not in the model, and it is silent on the women "
                   "who are not in paid work at all, a large group given a female LFPR of 40.3% in "
                   "PLFS 2024."},
                  {"t": "hbox", "color": "amber", "html": "R&sup2; = 0.21 means the model accounts for a "
                   "fifth of the variation in earnings. A low R&sup2; does not make the coefficients "
                   "wrong; it means much else matters too."}]},
         ]},

        {"type": "content", "label": "Fine print", "title": "The notes under the table decide whether to trust it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "bullets", "sm": True, "items": [
                      "<strong>Clustered standard errors</strong>: required when observations share villages, schools or clinics. Unclustered SEs from clustered data are too small.",
                      "<strong>Heteroskedasticity-consistent SEs</strong> (the &quot;sandwich&quot; option in most software): allow the error variance to differ across observations.",
                      "<strong>Weights</strong>: say which weight and why.",
                      "<strong>Fixed effects</strong>: &quot;district fixed effects&quot; means comparisons are made within districts only.",
                      "<strong>Stars</strong>: *, **, *** usually mark p below 0.10, 0.05 and 0.01; check the legend, as conventions vary."]}],
              "right": [
                  {"t": "panel", "color": "red", "title": "Signs to stop and ask", "html":
                   "N changes from column to column with no explanation (rows silently dropped for "
                   "missing values). Coefficients reported without standard errors. Only starred "
                   "results discussed. A control list that includes variables the treatment could have "
                   "changed. A sample described in the methods that does not match the N in the table."},
                  {"t": "hbox", "color": "cyan", "html": "Ask for the code and a log file with any "
                   "commissioned analysis. Reproducibility is a deliverable, and the DPDP Act's "
                   "research exemption still requires that personal data be handled with safeguards."}]},
         ]},

        {"type": "content", "label": "Worked brief", "title": "Commissioning a district baseline: a worked example",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "cls": "sm", "html": "Illustrative brief (hypothetical figures): a state nutrition mission wants a "
                   "baseline for anaemia among women aged 15&ndash;49 in one district, precise enough to "
                   "detect later change, and separate figures for SC and ST women."},
                  {"t": "panel", "color": "green", "title": "Sizing it", "html":
                   "Assume prevalence near 57% (NFHS-5, 2019&ndash;21, all women 15&ndash;49: 57.0%; NFHS-6 "
                   "anaemia figures were not yet released as of October 2026).<br>"
                   "Target margin &plusmn;4 points at 95%: n = 1.96&sup2; &times; 0.57 &times; 0.43 "
                   "&divide; 0.04&sup2; = 3.842 &times; 0.2451 &divide; 0.0016 = 589 women.<br>"
                   "Design effect 1.95: 589 &times; 1.95 = 1,148.6, round up to 1,149.<br>"
                   "Allow 10% non-response: 1,149 &divide; 0.9 = 1,276.7, so <strong>1,277 women</strong>."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "The subgroup problem", "html":
                   "If SC women are 20% of the district's women, the 1,149 completed interviews include "
                   "about 230 of them, and their estimate carries a margin of about &plusmn;8.9 points after "
                   "the design effect. To report SC and ST figures at &plusmn;4 points, each group needs its own "
                   "1,149 completed interviews, which means oversampling and weights."},
                  {"t": "hbox", "color": "cyan", "html": "Decide the subgroups that must be reported "
                   "before the sample is drawn. Adding them afterwards cannot be fixed by analysis."}]},
         ]},

        {"type": "content", "label": "Decision table", "title": "Which tool for which question",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Your question", "Summary or method", "Report with"],
              "rows": [
                  ["What share of households have X?", "Weighted proportion", "95% CI, unweighted n"],
                  ["What does a typical household spend?", "Weighted median (and mean)", "Percentiles or IQR"],
                  ["How unequal is it?", "Percentile ratios, Gini", "Definition of the welfare measure"],
                  ["Do two groups differ?", "Difference with its own SE; t or z test", "Difference, CI, p-value"],
                  ["Did it change between rounds?", "Difference across rounds, checked for comparable methods", "Both levels, change in points, CI"],
                  ["Are X and Y related?", "Scatter, correlation, simple regression", "Slope with units, plot"],
                  ["Is X related to Y, other things equal?", "Multiple regression", "Coefficients, SEs, controls listed"],
                  ["Did the programme cause the change?", "A causal design (RCT, DiD, RD, IV)", "Effect size, CI, design assumptions"],
                  ["How big a sample do we need?", "Power or precision calculation", "MDE or margin, deff, assumptions"]]},
             {"t": "body", "cls": "sm", "html": "Most disputes about analysis are disputes about which row of this "
              "table a question belongs in. Settle that in the terms of reference."},
         ]},

        {"type": "content", "label": "Before quoting", "title": "A checklist before you quote a number",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "cyan", "title": "About the number", "blocks": [
                      {"t": "bullets", "sm": True, "items": [
                          "Source named: survey, round, table, year of fieldwork",
                          "Definition stated: usual status or CWS, with or without imputation, age range",
                          "Population stated: all India, rural, women 15&ndash;49, children under 5",
                          "Precision known: CI or SE, or at least the unweighted n",
                          "Weighted, and the right weight"]}]}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "About the comparison", "blocks": [
                      {"t": "bullets", "sm": True, "items": [
                          "Same definition and method in both figures",
                          "Change given in percentage points and levels",
                          "Difference tested, with its own standard error",
                          "Causal language only with a causal design",
                          "Effect size in natural units, beside any p-value"]}]},
                  {"t": "hbox", "color": "green", "html": "If an item cannot be ticked, the number may "
                   "still be quoted, with the gap stated."}]},
         ]},

        {"type": "content", "label": "Terms of reference", "title": "The quantitative clauses worth writing into a ToR",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "A sampling plan with frame, stages, strata, clusters and selection probabilities",
                      "A power or precision calculation with sourced assumptions",
                      "A weighting note: design weights, non-response adjustment, final scaling",
                      "Questionnaires and codebook, with skip logic, in every field language"]}],
              "right": [
                  {"t": "bullets", "color": "indigo", "items": [
                      "A pre-analysis plan for any impact claim",
                      "Design-based standard errors for all reported estimates",
                      "De-identified data, code and log files as deliverables",
                      "A data protection plan consistent with the DPDP Act 2023 and the 2025 Rules, and with the consent given"]},
                  {"t": "hbox", "color": "amber", "html": "Each clause costs little at the start and is "
                   "nearly impossible to obtain after the final payment."}]},
         ]},

        {"type": "content", "label": "Using public microdata", "title": "Working with NFHS, PLFS and HCES unit-level data",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Unit-level PLFS and HCES data are published by MoSPI through its "
                   "microdata portal (microdata.gov.in), with README files and layouts; NFHS data are "
                   "distributed through the DHS Program after registration. Both come with documentation "
                   "that answers most weighting and design questions, and both ask users to accept "
                   "terms of use."},
                  {"t": "body", "cls": "sm", "html": "MoSPI's eSankhyiki portal also serves published "
                   "aggregates through an API; the PLFS and HCES figures in this deck were retrieved "
                   "that way in October 2026."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Order of work", "html":
                   "Read the README and the questionnaire. Reproduce one published table exactly. Only "
                   "then compute new estimates, using the design variables. Keep a log of every filter "
                   "and recode. When an estimate surprises you, suspect your code first: the published "
                   "figure has been checked by many people."},
                  {"t": "hbox", "color": "amber", "html": "Public microdata are de-identified, but linking "
                   "them to other sources can re-identify people in small districts. Do not attempt it, "
                   "and do not publish cells built from a handful of respondents."}]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Errors in published statistics"},

        {"type": "content", "label": "Comparability", "title": "Comparing across survey rounds",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "html": "Changes in questionnaire, recall period, sample design or "
                   "processing can move an indicator as much as real change does. Consumption surveys are "
                   "the clearest Indian case. On 15 November 2019 MoSPI announced that the results of the "
                   "2017&ndash;18 Consumer Expenditure Survey would not be released, citing &quot;data "
                   "quality issues&quot;, after a leaked draft had reported a fall in real spending "
                   "(Business Today, 15 November 2019)."},
                  {"t": "body", "cls": "sm", "html": "The next surveys, HCES 2022&ndash;23 and "
                   "2023&ndash;24, changed the design, so comparisons with 2011&ndash;12 need care "
                   "and the survey reports' own notes on comparability."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Questions before comparing rounds", "html":
                   "Was the questionnaire the same? The recall periods? The age range or the reference "
                   "standard (growth references changed in 2006)? The sample frame and the season of "
                   "fieldwork? Was any part of fieldwork interrupted, as NFHS-5's was split across "
                   "2019&ndash;21? If any answer is no, report the change with that caveat beside it."},
                  {"t": "hbox", "color": "red", "html": "A trend line drawn through non-comparable points "
                   "is the most common error in published development charts."}]},
         ]},

        {"type": "content", "label": "Composition", "title": "Averages hide the groups inside them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "stats", "cols": 3, "cards": [
                      {"num": "63.7%", "label": "ST women", "color": "green", "source": "MoSPI, PLFS 2024, LFPR 15+, usual status"},
                      {"num": "40.3%", "label": "all women", "color": "cyan", "source": "MoSPI, PLFS 2024"},
                      {"num": "31.3%", "label": "women of &quot;others&quot; social group", "color": "indigo", "source": "MoSPI, PLFS 2024"}]},
                  {"t": "body", "cls": "sm", "html": "Female labour force participation varies by more than "
                   "30 points across social groups. A national change can come from changes within "
                   "groups or from changes in which groups make up the population, or the sample."}],
              "right": [
                  {"t": "panel", "color": "indigo", "title": "Reading group differences carefully", "html":
                   "Higher participation among Adivasi women reflects, among other things, more "
                   "agricultural self-employment and wage work out of economic necessity; lower "
                   "participation among women in better-off groups reflects income effects and social "
                   "norms. A single national figure averages these together. Policy reading needs the "
                   "breakdown, and the breakdown needs the standard error, because ST samples are "
                   "small in many states."},
                  {"t": "hbox", "color": "amber", "html": "Before attributing a national trend to a "
                   "policy, check whether it holds within groups."}]},
         ]},

        {"type": "content", "label": "Review checklist", "title": "Ten errors a reviewer should catch",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Error", "Typical form", "The fix"],
              "rows": [
                  ["Points read as per cent", "&quot;Stunting fell 2.9%&quot;", "2.9 percentage points (7.6% relative)"],
                  ["Status unstated", "Unemployment &quot;3.2%&quot; set against &quot;4.9%&quot;", "Name usual status or CWS"],
                  ["Unweighted national figure", "Raw sample shares reported", "Apply the survey weight"],
                  ["NFHS weight unscaled", "Counts in the hundreds of billions", "Divide v005 by 1,000,000"],
                  ["PLFS combined weight", "MLTS/100 used where NSS &ne; NSC", "MLTS/200 there; divide by quarters for annual"],
                  ["SRS errors on cluster data", "Intervals too narrow", "Declare PSU and strata"],
                  ["District ranks as fact", "&quot;District X ranks 3rd&quot;", "Show intervals; use bands"],
                  ["Mismatched denominators", "Census and NFHS sex ratios compared", "Name both populations"],
                  ["Non-comparable rounds", "Trend across a method change", "Caveat or drop the point"],
                  ["Causal verbs on correlations", "&quot;Literacy drives institutional births&quot;", "&quot;Is associated with&quot;, or a causal design"]]},
             {"t": "body", "cls": "sm", "html": "Every example in this table appears earlier in the deck with "
              "its sources and arithmetic."},
         ]},

        {"type": "content", "label": "Coming data", "title": "New data to watch, as of October 2026",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "panel", "color": "cyan", "title": "Census 2027", "html":
                   "The reference date for the next Census is 1 March 2027, and it includes caste "
                   "enumeration. It will refresh the sampling frames and population totals that every "
                   "household survey uses for weights, sixteen years after the 2011 Census. Expect "
                   "survey estimates of totals, and some ratios, to be revised once the new frame is in "
                   "use."},
                  {"t": "panel", "color": "indigo", "title": "Monthly labour data", "html":
                   "MoSPI now publishes PLFS labour force indicators monthly from 2025, alongside "
                   "quarterly bulletins and annual reports. Monthly estimates carry wider margins than "
                   "annual ones; a 0.2-point monthly move is usually noise."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Rules that change measurement", "html":
                   "The four Labour Codes came into force on 21 November 2025, and MGNREGA was replaced "
                   "from 1 July 2026 by the Viksit Bharat G RAM G Act 2025, with 125 days of work. Where "
                   "administrative series track entitlements under these laws, check the date of any "
                   "break before reading a trend. The Income-tax Act 2025, in force from 1 April 2026, "
                   "may affect tax-based income series in the same way."},
                  {"t": "hbox", "color": "cyan", "html": "Every time-sensitive statement in this deck is "
                   "as of October 2026."}]},
         ]},

        {"type": "content", "label": "Summary", "title": "Ten ideas to keep",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "bullets", "color": "green", "sm": True, "items": [
                      "Every number is a definition, a population, a period and a margin of error",
                      "The level of measurement limits the arithmetic",
                      "Lead with the median in skewed data; report both when they differ",
                      "Use percentage points for differences between percentages",
                      "Precision depends on sample size, and it collapses in small areas"]}],
              "right": [
                  {"t": "bullets", "color": "cyan", "sm": True, "items": [
                      "Weight every population estimate: v005/1,000,000 in NFHS, the MLTS rules in PLFS",
                      "Clustering inflates standard errors; declare PSU and strata",
                      "A p-value measures surprise under the null, never the size or importance of an effect",
                      "Association becomes causation only through design",
                      "Size a study by its minimum detectable effect before collecting data"]},
                  {"t": "hbox", "color": "indigo", "html": "All ten fit in one sentence: know what was "
                   "measured, among whom, how precisely, and against what."}]},
         ]},

        {"type": "content", "label": "Where next", "title": "Where next in the 101 series",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [
                  {"t": "body", "cls": "sm", "html": "This deck covered the reading and commissioning "
                   "toolkit. Each of these decks goes deeper into one part of it:"},
                  {"t": "bullets", "sm": True, "items": [
                      "<a href=\"/101-courses/stats-without-code.html\">Statistics Without Code 101</a>: the same ideas worked through in spreadsheets and point-and-click tools",
                      "<a href=\"/101-courses/bi-analysis.html\">Bivariate Analysis 101</a>: cross-tabs, chi-square, correlation and simple regression in depth",
                      "<a href=\"/101-courses/multivariate-basics.html\">Multivariate Analysis 101</a>: many variables at once, including multilevel models",
                      "<a href=\"/101-courses/econometrics-101.html\">Econometrics 101</a>: regression, panel data and identification"]}],
              "right": [
                  {"t": "bullets", "sm": True, "items": [
                      "<a href=\"/101-courses/eda-hhs.html\">Exploratory Data Analysis 101</a>: looking at household survey data before modelling it",
                      "<a href=\"/101-courses/survey-design.html\">Survey Design 101</a>: questionnaires, sampling and fieldwork",
                      "<a href=\"/101-courses/impact-eval.html\">Impact Evaluation 101</a>: randomised and quasi-experimental designs",
                      "<a href=\"/101-courses/cost-effectiveness.html\">Cost Effectiveness 101</a>: putting effect sizes next to costs",
                      "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the DPDP Act 101</a>: handling personal data lawfully"]},
                  {"t": "hbox", "color": "cyan", "html": "Suggested order for a practitioner: Survey "
                   "Design, then Exploratory Data Analysis, then Bivariate Analysis and Impact "
                   "Evaluation."}]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Quantitative Methods 101 &middot; Complete",
         "headline": "Know what was measured,<br>among whom, how precisely",
         "byline": "Read every figure with its definition, its sample and its margin of error, weight it "
                   "correctly, and size every study before it starts. Explore the rest of the ImpactMojo "
                   "101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

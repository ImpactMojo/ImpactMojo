# -*- coding: utf-8 -*-
"""
Systematic Reviews & Evidence Synthesis 101 — ImpactMojo 101 Series (native deck spec)
Finding, appraising and combining what is already known, for development researchers and
practitioners in South Asia. Covers systematic, scoping, rapid and realist reviews,
meta-analysis, GRADE, PRISMA 2020 and bibliometric analysis.
Build: python3 scripts/deck-builder/build.py systematic_reviews
"""

DECK = {
    "slug": "systematic-reviews",
    "title": "Systematic Reviews & Evidence Synthesis 101",
    "description": ("Systematic Reviews & Evidence Synthesis 101 — a free foundational course for "
                    "development researchers and practitioners in South Asia. How to frame a review "
                    "question, search and screen the literature, appraise risk of bias, run or read a "
                    "meta-analysis, grade the certainty of evidence, report to PRISMA 2020, and use "
                    "bibliometric analysis to map a field. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Systematic<br>Reviews &amp;<br>Evidence<br>Synthesis 101",
         "sub": "Finding, Appraising &amp; Combining What Is Already Known &mdash; from the "
                "Review Question to PRISMA, Meta-Analysis, GRADE and Bibliometrics",
         "tags": ["Research Methods", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Synthesis, and What Kind"},
             {"name": "The Question and the Protocol"},
             {"name": "Searching"},
             {"name": "Screening and Selection"},
             {"name": "Data Extraction"},
             {"name": "Risk of Bias and Study Quality"},
             {"name": "Meta-Analysis"},
             {"name": "Synthesis Without Meta-Analysis"},
             {"name": "GRADE and Reporting"},
             {"name": "Bibliometric Analysis"},
             {"name": "Practice, Tools and Pitfalls"},
         ]},

        # ===================== SECTION 01: WHY SYNTHESIS =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Synthesis, and What Kind"},

        {"type": "content", "label": "Definition", "title": "A review is a study of studies",
         "blocks": [
             {"t": "body", "html": "A <strong>systematic review</strong> answers a defined question by "
              "finding every study that bears on it, judging each one by stated criteria, and combining "
              "what survives. The unit of observation is the study, not the person. That is the whole "
              "difference from an ordinary literature review: a systematic review is itself a piece of "
              "research, with a method that another team could repeat and get the same set of studies."},
             {"t": "term", "word": "Systematic review",
              "def": "A review that uses explicit, pre-specified and reproducible methods to identify, "
              "select, appraise and synthesise all research relevant to a particular question, so "
              "that the conclusion depends on the evidence rather than on which papers the author "
              "happened to have read."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "A literature review", "html":
                        "Written from what the author knows and can find. Selection is invisible. Two "
                        "authors on the same topic produce two different reading lists and two "
                        "different conclusions, and neither can say why."}],
              "right": [{"t": "panel", "color": "green", "title": "A systematic review", "html":
                         "Written from a search that is recorded, criteria that are stated in advance, "
                         "and an appraisal applied to every study the same way. A reader can check the "
                         "search, re-run it, and see exactly where each study went."}]},
         ]},

        {"type": "content", "label": "The Problem It Solves", "title": "Nobody can read everything",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "75", "label": "randomised trials published per day, health alone", "color": "cyan",
                  "source": "Bastian, Glasziou &amp; Chalmers, PLoS Medicine 2010"},
                 {"num": "11", "label": "systematic reviews published per day, same estimate", "color": "green",
                  "source": "Bastian, Glasziou &amp; Chalmers, PLoS Medicine 2010"},
                 {"num": "3rd", "label": "India's rank among countries by volume of research articles", "color": "amber",
                  "source": "NSF Science &amp; Engineering Indicators 2022"}]},
             {"t": "body", "html": "Those figures are from 2010 and have only grown. A programme officer "
              "deciding whether a cash transfer should be conditional, a state official weighing a "
              "mid-day meal reform, or a doctoral student framing a thesis cannot read the primary "
              "literature on the question. Somebody has to read it for them, in a way that can be "
              "trusted. That is what a systematic review is for, and why the funders who commission "
              "evaluations (3ie, the World Bank, FCDO, the Gates Foundation) also commission reviews."},
             {"t": "hbox", "color": "amber", "html": "The alternative to a systematic review is not "
              "\"no review\". It is an unsystematic one, whose selection of studies nobody can see."},
         ]},

        {"type": "content", "label": "Two Cautionary Tales", "title": "When the pile of studies said something different",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Deworming", "html":
                        "Miguel and Kremer's 2004 Kenyan trial (<em>Econometrica</em> 72(1)) reported large "
                        "effects of school-based deworming on attendance and became the basis of mass "
                        "programmes. The Cochrane review by Taylor-Robinson and colleagues (2015) pooled "
                        "the trials and found little or no effect of mass deworming on weight, haemoglobin "
                        "or attendance. A 2015 reanalysis of the Kenyan data by Aiken, Davey and others "
                        "opened a dispute that is still cited as the \"worm wars\". The point is not who "
                        "was right. It is that one trial and the body of trials disagreed, and only a "
                        "review could show it."}],
              "right": [{"t": "panel", "color": "amber", "title": "Microfinance", "html":
                         "Through the 2000s microfinance was described as a proven route out of poverty "
                         "on the strength of case studies and early evaluations. Duvendack and colleagues' "
                         "2011 systematic review for the EPPI-Centre and DFID concluded that the evidence "
                         "base was weak, that the strongest-looking studies had the weakest designs, and "
                         "that no robust effect on poverty could be shown. Randomised trials published "
                         "after 2011 (the six studies collected in the <em>American Economic Journal: "
                         "Applied Economics</em> 2015 symposium) found modest effects at best."}]},
             {"t": "hbox", "color": "cyan", "html": "In both cases the field's belief rested on the "
              "studies people had read. The review changed the belief by changing the denominator."},
         ]},

        {"type": "content", "label": "The Family of Reviews", "title": "Systematic is one kind; choose the right one",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "Question it answers", "Time", "Typical use"],
              "rows": [
                  ["Systematic review", "Does X work, for whom, by how much?", "9&ndash;18 months", "Policy decisions, guidelines, funding"],
                  ["Meta-analysis", "What is the pooled effect across studies?", "Within a systematic review", "When studies are similar enough to combine"],
                  ["Scoping review", "What has been studied, how, and where are the gaps?", "3&ndash;9 months", "New or diffuse fields; before a full review"],
                  ["Rapid review", "What does the evidence say, by next month?", "4&ndash;12 weeks", "A decision with a deadline"],
                  ["Realist synthesis", "What works for whom, in what circumstances, and why?", "6&ndash;18 months", "Complex programmes with mechanisms"],
                  ["Qualitative evidence synthesis", "How do people experience or explain X?", "6&ndash;12 months", "Acceptability, implementation, meaning"],
                  ["Evidence gap map", "Where is the evidence dense and where absent?", "3&ndash;6 months", "Setting a research agenda"],
                  ["Umbrella review", "What do the existing reviews say?", "3&ndash;6 months", "Mature fields with many reviews"],
                  ["Bibliometric analysis", "Who publishes what, where, citing whom?", "2&ndash;8 weeks", "Mapping a field, not judging its findings"]]},
             {"t": "body", "cls": "sm", "html": "The durations are the ranges reported in methods literature and "
              "reviewers' own accounts; Borah and colleagues (<em>BMJ Open</em> 2017, 7:e012545) measured a "
              "median of 67 weeks from PROSPERO registration to publication across 195 reviews."},
         ]},

        {"type": "content", "label": "Matching Question to Method", "title": "Which review, decided by the question",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "green", "items": [
                  "<strong>\"Does conditional cash transfer raise secondary enrolment?\"</strong> An effect question with a comparison: systematic review, with meta-analysis if the trials are similar.",
                  "<strong>\"What is known about self-help groups and women's political participation?\"</strong> A mapping question: scoping review or evidence gap map.",
                  "<strong>\"Why did community health worker schemes work in Chhattisgarh and stall elsewhere?\"</strong> A mechanism-and-context question: realist synthesis.",
                  "<strong>\"How do adolescent girls experience menstrual health programmes?\"</strong> An experience question: qualitative evidence synthesis."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The test", "html":
                         "Write the question down. If it contains a verb like <em>works</em>, "
                         "<em>reduces</em>, <em>increases</em>, it is an effect question and the "
                         "systematic review machinery applies in full. If it contains <em>what is "
                         "known</em> or <em>how has this been studied</em>, you are scoping. If it "
                         "contains <em>why</em> or <em>under what conditions</em>, no pooled number "
                         "will answer it, and pretending otherwise produces a meta-analysis of "
                         "things that are not the same."}]},
             {"t": "hbox", "color": "amber", "html": "The most common error in commissioned reviews is "
              "asking a scoping question and paying for a systematic-review timeline, or the reverse."},
         ]},

        {"type": "content", "label": "Reviews in Development", "title": "Who does this work, and where it lives",
         "blocks": [
             {"t": "table",
              "head": ["Body", "Founded", "What it holds"],
              "rows": [
                  ["Cochrane", "1993", "Health reviews; the <em>Handbook</em> is the method reference for every field"],
                  ["Campbell Collaboration", "2000", "Education, crime, social welfare and, with 3ie, international development"],
                  ["3ie (International Initiative for Impact Evaluation)", "2008", "Development Evidence Portal: impact evaluations, reviews and gap maps"],
                  ["EPPI-Centre, UCL", "1993", "Methods and reviews across social policy; the microfinance review above"],
                  ["JBI (Joanna Briggs Institute)", "1996", "Scoping-review guidance and appraisal tools"],
                  ["PROSPERO, University of York", "2011", "Prospective register of review protocols"]]},
             {"t": "body", "html": "For an Indian or South Asian question, start at the 3ie portal and Campbell's "
              "international development group, then Cochrane for anything with a health outcome. Most "
              "reviews that touch India are not Indian reviews; the search and the framing will be "
              "yours to add."},
         ]},

        {"type": "content", "label": "What This Course Does", "title": "Ten sections, one workflow",
         "blocks": [
             {"t": "flow", "steps": ["Question", "Protocol", "Search", "Screen", "Extract", "Appraise", "Synthesise", "Grade", "Report"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Sections 2 to 9 walk the workflow above, in the order a real review runs.",
                  "Section 10 covers bibliometric analysis, which answers a different question with a different toolkit and is often confused with a review.",
                  "Section 11 is the practical close: a 12-week plan, free tools, and the errors reviewers make."]}],
              "right": [{"t": "panel", "color": "green", "title": "Who this is for", "html":
                         "Practitioners asked to \"pull together the evidence\" before a proposal; "
                         "doctoral students whose thesis needs a literature chapter that would survive "
                         "examination; evaluators reading someone else's review and needing to know "
                         "whether to trust it. Nothing here needs a licence: every tool named is free or "
                         "has a free equivalent."}]},
         ]},

        # ===================== SECTION 02: QUESTION AND PROTOCOL =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Question and the Protocol"},

        {"type": "content", "label": "Framing", "title": "PICO: the question has four parts",
         "blocks": [
             {"t": "table",
              "head": ["Element", "Asks", "Example: cash transfers and schooling"],
              "rows": [
                  ["<strong>P</strong>opulation", "Whose outcomes?", "Children aged 6&ndash;18 in households below a poverty threshold, low- and middle-income countries"],
                  ["<strong>I</strong>ntervention", "What is being done?", "Cash transfer to the household, conditional on school attendance"],
                  ["<strong>C</strong>omparison", "Compared with what?", "No transfer, or an unconditional transfer of the same value"],
                  ["<strong>O</strong>utcome", "Measured how?", "Enrolment, attendance, completion, learning (test scores)"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Adding <strong>S</strong> (study design) gives PICOS, which is "
                        "where you decide whether only randomised trials count or whether matched and "
                        "difference-in-differences designs are in. That choice shapes everything after it."}],
              "right": [{"t": "body", "cls": "sm", "html": "Variants exist for other question types. "
                         "<strong>PEO</strong> (population, exposure, outcome) suits observational "
                         "questions; <strong>SPIDER</strong> (sample, phenomenon of interest, design, "
                         "evaluation, research type) was written for qualitative synthesis."}]},
         ]},

        {"type": "content", "label": "Scope", "title": "Too broad drowns you; too narrow finds nothing",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Too broad", "html":
                        "\"What is the effect of social protection on wellbeing in Asia?\" Pulls in "
                        "pensions, insurance, transfers, public works and school meals, across "
                        "forty countries and every outcome. Screening runs to tens of thousands of "
                        "records and the synthesis compares things that share only a label."}],
              "right": [{"t": "panel", "color": "red", "title": "Too narrow", "html":
                         "\"What is the effect of PM-KISAN on fertiliser use in Bihar?\" One scheme, "
                         "one state, one outcome, launched in 2019. There may be two studies. A "
                         "review of two studies is a reading, not a synthesis, and the time would be "
                         "better spent on a primary study."}]},
             {"t": "body", "html": "The workable middle is a question where you expect between roughly ten "
              "and a few hundred eligible studies. A quick scoping search in one database, with a "
              "day's reading of what it returns, tells you which side of that range you are on before "
              "the protocol is written. Adjust the population, the time window or the outcome set until "
              "the question is answerable."},
             {"t": "hbox", "color": "cyan", "html": "Write the eligibility criteria as sentences a "
              "screener could apply without asking you. \"Studies of women's empowerment\" is not a "
              "criterion. \"Studies reporting at least one of: decision-making index, mobility, "
              "control over earnings, for women aged 15&ndash;49\" is."},
         ]},

        {"type": "content", "label": "Eligibility Criteria", "title": "Inclusion and exclusion, written before searching",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Dimension", "Include", "Exclude", "Why it matters"],
              "rows": [
                  ["Population", "Households in LMICs; children 6&ndash;18", "High-income countries; adult learners", "Transferability of the answer"],
                  ["Intervention", "Cash conditional on attendance", "In-kind transfers, scholarships", "Different mechanism, different question"],
                  ["Comparison", "No transfer; unconditional transfer", "Before&ndash;after with no comparison group", "Cannot separate effect from trend"],
                  ["Outcomes", "Enrolment, attendance, completion, test scores", "Self-reported \"benefit\"", "Comparable measures"],
                  ["Design", "RCT, RDD, DiD, matched", "Cross-sectional correlations", "Ability to support a causal claim"],
                  ["Time", "2000 onward", "Earlier", "Programme era; data quality"],
                  ["Language", "Any, with translation budget", "None excluded", "English-only excludes Indian-language evaluations"],
                  ["Publication", "Peer-reviewed and grey", "Opinion pieces, news", "Grey literature holds most development evaluations"]]},
             {"t": "body", "cls": "sm", "html": "The criteria are a contract with the reader. Once the "
              "search is run, changing them to admit a study you like or drop one you do not is the "
              "review equivalent of moving the goalposts, and the protocol exists so that it shows."},
         ]},

        {"type": "content", "label": "The Protocol", "title": "What goes in a protocol",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Background and rationale: why this review, why now, what exists already",
                  "The question in PICO(S) form and the eligibility criteria as sentences",
                  "Information sources: every database, register, website and person you will search",
                  "The full search strategy for at least one database, with dates",
                  "Screening procedure: how many screeners, how disagreements are resolved",
                  "Data extraction items and the form",
                  "Risk-of-bias tool, named",
                  "Synthesis plan: meta-analysis or not, model, subgroup analyses named in advance",
                  "Certainty assessment (GRADE) and reporting standard (PRISMA 2020)"]}],
              "right": [{"t": "panel", "color": "green", "title": "Why pre-specify subgroups", "html":
                         "If you decide after seeing the results that the effect is \"driven by South "
                         "Asian studies\", a reader cannot tell whether you found a pattern or went "
                         "looking for one. Naming the subgroups in the protocol (by region, by income "
                         "level, by design, by conditionality) turns the same analysis from a fishing "
                         "trip into a test. PRISMA-P (Moher and colleagues, <em>Systematic Reviews</em> "
                         "2015, 4:1) is the checklist for protocols, with 17 items."}]},
         ]},

        {"type": "content", "label": "Registration", "title": "Register the protocol before you search",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "PROSPERO", "html":
                        "The University of York's Centre for Reviews and Dissemination has run "
                        "PROSPERO since 2011. It accepts reviews with a health-related outcome, "
                        "broadly read: nutrition, WASH, maternal health, mental health, violence. "
                        "Registration is free, public and time-stamped. Reviewers then cite the "
                        "registration number in the paper."}],
              "right": [{"t": "panel", "color": "cyan", "title": "OSF Registries", "html":
                         "For reviews outside health (education, livelihoods, governance), the Open "
                         "Science Framework accepts a protocol as a registration, free, with the same "
                         "time stamp. Campbell reviews register with Campbell itself; 3ie registers "
                         "the reviews it funds. The register matters less than the date."}]},
             {"t": "body", "html": "Registration does two things. It stops duplication: a search of "
              "PROSPERO before you start will show whether a team in Dhaka registered your question "
              "last year. And it stops drift: the registered version is what your published methods "
              "will be compared against, so departures have to be explained rather than hidden."},
             {"t": "hbox", "color": "amber", "html": "A review that changes its outcome list after "
              "seeing the studies, and does not say so, is the review-level version of selective "
              "reporting. Registration is the cheapest protection there is."},
         ]},

        {"type": "content", "label": "Team", "title": "Who a review needs",
         "blocks": [
             {"t": "table",
              "head": ["Role", "Does", "Minimum"],
              "rows": [
                  ["Lead reviewer", "Owns the question, protocol and write-up", "One, with time"],
                  ["Second screener and extractor", "Independent screening and extraction of every record", "One; dual screening is not optional"],
                  ["Information specialist", "Builds and translates the search across databases", "A librarian, even for a day"],
                  ["Statistician or methodologist", "Meta-analysis, heterogeneity, bias assessment", "For any pooled analysis"],
                  ["Subject expert", "Knows the programmes, the grey literature and the people to email", "Advisory"],
                  ["Language readers", "Screen and extract studies in Hindi, Bangla, Tamil and so on", "As the question demands"]]},
             {"t": "body", "html": "The two-person minimum is a method requirement, not a staffing nicety. "
              "Every reporting standard asks whether screening and extraction were done in duplicate, "
              "and a single-reviewer review is downgraded by readers and by AMSTAR 2, the tool used to "
              "appraise reviews. A doctoral student can meet it with a supervisor or a fellow student "
              "screening a sample and the disagreement rate reported."},
         ]},

        {"type": "content", "label": "Time", "title": "A review takes longer than you think",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "67", "label": "median weeks from registration to publication, 195 reviews", "color": "amber",
                  "source": "Borah et al., BMJ Open 2017"},
                 {"num": "1,781", "label": "median records screened per review in the same sample", "color": "cyan",
                  "source": "Borah et al., BMJ Open 2017"},
                 {"num": "5", "label": "median number of authors", "color": "green",
                  "source": "Borah et al., BMJ Open 2017"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Most of the time goes into screening and "
                        "extraction, which scale with the number of records, and into chasing full "
                        "texts and unreported statistics from authors, which scales with how much "
                        "of the literature is grey. A development review leans on grey literature "
                        "and so runs at the slow end."}],
              "right": [{"t": "body", "cls": "sm", "html": "A rapid review buys time by restricting "
                        "databases, dates and languages, screening titles once, and extracting a "
                        "shorter form. Cochrane's rapid review guidance (Garritty and colleagues, "
                        "<em>Journal of Clinical Epidemiology</em> 2021, 130:13) lists which "
                        "shortcuts cost least. The restrictions must be reported as limitations."}]},
         ]},

        {"type": "content", "label": "Worked Example", "title": "A protocol in one slide: self-help groups and empowerment",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Item", "Decision"],
                        "rows": [
                            ["Question", "Do economic self-help group programmes improve women's economic, social and political empowerment?"],
                            ["Population", "Adult women in LMICs; group-based savings or credit programmes"],
                            ["Comparison", "No programme, or waitlist"],
                            ["Outcomes", "Economic (income, assets, savings), social (mobility, decision-making), political (participation)"],
                            ["Designs", "RCT, quasi-experimental with comparison group"],
                            ["Search", "Nine databases plus 3ie, J-PAL, IPA, NGO sites; no language limit"],
                            ["Synthesis", "Random-effects meta-analysis by outcome domain; narrative for the rest"]]}],
              "right": [{"t": "panel", "color": "green", "title": "The real one", "html":
                         "This is the shape of Brody and colleagues' Campbell review (<em>Campbell "
                         "Systematic Reviews</em> 2015, 11:19), which found 23 quantitative studies "
                         "and reported small positive effects on economic, social and political "
                         "empowerment, with an accompanying qualitative synthesis on the mechanisms. "
                         "Its protocol was published two years before the review. Read it beside the "
                         "review to see how the plan and the product relate."}]},
         ]},

        # ===================== SECTION 03: SEARCHING =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Searching"},

        {"type": "content", "label": "Where the Studies Are", "title": "Databases: what each covers",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "Covers", "Access", "Use for"],
              "rows": [
                  ["PubMed / MEDLINE", "Biomedicine, public health; MeSH vocabulary", "Free", "Any health outcome"],
                  ["Scopus", "Multidisciplinary, 1970s onward; strong on Indian journals", "Subscription", "Broad coverage, citation data"],
                  ["Web of Science", "Multidisciplinary core journals", "Subscription", "Citation chasing, bibliometrics"],
                  ["EconLit", "Economics journals and working papers", "Subscription", "Development economics"],
                  ["ERIC", "Education", "Free", "Schooling outcomes"],
                  ["OpenAlex", "Everything with a DOI, plus much without", "Free, API", "Free multidisciplinary search; bibliometrics"],
                  ["Google Scholar", "Widest net, opaque ranking", "Free", "Grey literature, citation chasing; not as a sole source"],
                  ["3ie Development Evidence Portal", "Impact evaluations and reviews in development", "Free", "Every development review"],
                  ["IDEAS/RePEc, SSRN, NBER", "Working papers", "Free", "Economics before it is published"],
                  ["Shodhganga (INFLIBNET)", "Indian doctoral theses, full text", "Free", "Indian evidence nobody else indexes"]]},
             {"t": "body", "cls": "sm", "html": "Bramer and colleagues (<em>Systematic Reviews</em> 2017, 6:245) "
              "tested database combinations against 58 published reviews and found that no single database "
              "recalled all included studies; MEDLINE, Embase, Web of Science and Google Scholar together "
              "reached 98 per cent. Plan on at least three, plus the field-specific ones."},
         ]},

        {"type": "content", "label": "Building the String", "title": "Boolean logic, one concept at a time",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Write one block per PICO concept. Inside a block, join synonyms with <strong>OR</strong>: (\"cash transfer*\" OR \"conditional cash\" OR CCT OR \"social pension\").",
                  "Join the blocks with <strong>AND</strong>: population AND intervention AND outcome. Comparison is rarely searched; it is applied at screening.",
                  "Truncation (<strong>*</strong>) catches plurals and variants: <em>school*</em> finds school, schools, schooling.",
                  "Phrase quotes keep words together: \"self-help group\" rather than self AND help AND group.",
                  "Field tags limit where the term must appear: [tiab] in PubMed searches title and abstract; TITLE-ABS-KEY() does the same in Scopus."]}],
              "right": [{"t": "panel", "color": "green", "title": "Do not search the outcome too tightly", "html":
                         "A study of cash transfers that reports enrolment as a secondary outcome may "
                         "never mention it in the abstract. Searching population AND intervention, and "
                         "leaving outcome to screening, recalls more at the price of more records. In "
                         "development, where outcomes are named inconsistently, that trade is usually "
                         "worth making."}]},
             {"t": "hbox", "color": "amber", "html": "Test the string against five studies you already know "
              "should be found. If it misses one, the string is wrong, not the study."},
         ]},

        {"type": "content", "label": "Controlled Vocabulary", "title": "MeSH and thesaurus terms catch what free text misses",
         "blocks": [
             {"t": "body", "html": "Indexers at MEDLINE tag every record with terms from the Medical Subject "
              "Headings (MeSH) tree, so a paper that says \"undernourished\" in its abstract is still "
              "tagged <em>Malnutrition</em>. A search that combines the MeSH term with free-text "
              "synonyms recalls both the indexed and the not-yet-indexed. Scopus and EconLit have their "
              "own thesauri; ERIC has descriptors. Google Scholar has none, which is one reason it "
              "cannot be the only source."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "PubMed example", "html":
                        "(\"Malnutrition\"[Mesh] OR malnutrition[tiab] OR undernutrition[tiab] OR "
                        "stunting[tiab] OR wasting[tiab]) AND (\"Child, Preschool\"[Mesh] OR "
                        "\"under five\"[tiab] OR \"under-five\"[tiab]) AND (India[tiab] OR "
                        "\"India\"[Mesh])"}],
              "right": [{"t": "panel", "color": "cyan", "title": "Translating between databases", "html":
                         "The same concept needs a different string in each database: different field "
                         "tags, different truncation symbols, different thesauri. The Polyglot Search "
                         "Translator (Bond University, free) converts a PubMed string into Scopus, "
                         "Web of Science and others as a first draft, which a person then corrects."}]},
         ]},

        {"type": "content", "label": "Grey Literature", "title": "Most development evaluations are not in journals",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "An evaluation commissioned by a donor is a PDF on the donor's site, "
                        "or on the implementing NGO's, or nowhere public at all. A review that searches "
                        "only journals will find the academic subset, which is not a random sample: "
                        "it overrepresents randomised trials, positive results and English. Grey "
                        "literature searching is where a development review differs most from a "
                        "clinical one."},
                       {"t": "bullets", "sm": True, "color": "green", "items": [
                           "3ie Development Evidence Portal, J-PAL and IPA evaluation databases",
                           "World Bank Open Knowledge Repository; ADB, UNICEF, UNDP, WFP evaluation libraries",
                           "FCDO (DevTracker), USAID (DEC), GIZ, Gates Foundation research",
                           "NITI Aayog, NCAER, state evaluation organisations, IDR's archive",
                           "OpenGrey, ProQuest theses, Shodhganga"]}],
              "right": [{"t": "panel", "color": "amber", "title": "Record it like a database search", "html":
                         "Grey searches are the ones reviewers forget to document, and PRISMA-S "
                         "(Rethlefsen and colleagues, <em>Systematic Reviews</em> 2021, 10:39) asks "
                         "for each website, the date, the terms used and the number of records. Keep a "
                         "log as you go; reconstructing it later is guesswork."}]},
         ]},

        {"type": "content", "label": "South Asian Sources", "title": "Where Indian and regional evidence hides",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "What it holds", "Note"],
              "rows": [
                  ["Shodhganga", "Full-text doctoral theses from Indian universities, via INFLIBNET", "Theses hold primary data on programmes nobody published on"],
                  ["Economic and Political Weekly archive", "Fifty-plus years of applied Indian social science", "Indexed unevenly by Scopus; search directly"],
                  ["IndMED / IndMedica", "Indian biomedical journals not in MEDLINE", "Public-health and nutrition evaluations"],
                  ["National Digital Library of India", "Aggregated theses, reports, books", "Coverage varies; useful for older material"],
                  ["NCAER, IGIDR, CDS, ISEC, IEG working papers", "Institute series", "Search each site; few are indexed"],
                  ["Ministry and state evaluation reports", "Programme evaluations by DMEO, NITI Aayog, state bodies", "PDFs, often undated; record the retrieval date"],
                  ["icddr,b (Bangladesh), NIPS and PIDE (Pakistan), CBS Nepal, IPS Sri Lanka", "National institutes' evaluations and surveys", "Regional coverage that global databases miss"]]},
             {"t": "body", "cls": "sm", "html": "A regional review that skips these sources will conclude, "
              "wrongly, that the evidence from South Asia is thin. It is thinly indexed, which is different."},
         ]},

        {"type": "content", "label": "Google Scholar", "title": "Use it; do not rely on it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "What it is good for", "html":
                        "Citation chasing: the \"cited by\" link finds later studies that built on a "
                        "known one, which databases do badly. Grey literature: it indexes PDFs on "
                        "institutional sites. Full text: it often links to a free copy. Recall: in "
                        "Bramer's tests it added studies no database had."}],
              "right": [{"t": "panel", "color": "red", "title": "What it cannot do", "html":
                         "It shows at most 1,000 results per query and ranks them by an undisclosed "
                         "relevance formula, so the same search returns different results on different "
                         "days and to different users. It has no controlled vocabulary, limited "
                         "Boolean support, and no export of a full result set. A search that cannot be "
                         "reproduced cannot be the backbone of a systematic review."}]},
             {"t": "body", "html": "The convention is to run the main string in the databases, then run a "
              "simplified version in Google Scholar and screen the first 200 to 300 results, reporting "
              "that cut-off. Haddaway and colleagues (<em>PLoS ONE</em> 2015, 10:e0138237) found that "
              "this captured most of the additional grey literature Scholar contributes."},
         ]},

        {"type": "content", "label": "Beyond the Databases", "title": "Hand-searching, citation chasing and asking people",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Backward citation chasing</strong>: read the reference lists of every included study and of prior reviews.",
                  "<strong>Forward citation chasing</strong>: find everything that cites an included study (Scopus, Web of Science, OpenAlex, Scholar).",
                  "<strong>Hand-searching</strong>: read the tables of contents of the three or four journals that publish most in the field, for the review period.",
                  "<strong>Conference proceedings</strong>: the Indian Statistical Institute, NEUDC, PacDev and CSAE programmes hold papers years before publication.",
                  "<strong>Ask</strong>: email the twenty people who work on the question. Unpublished and in-progress studies exist only in their inboxes."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why this is not optional", "html":
                         "Horsley, Dingwall and Sampson's Cochrane methodology review (2011) found that "
                         "checking reference lists identified additional eligible studies in every review "
                         "that tested it. In development, where working papers circulate for years, "
                         "citation chasing routinely finds a fifth or more of the final included set. "
                         "Report the number found by each route."}]},
         ]},

        {"type": "content", "label": "Managing References", "title": "Zotero, deduplication and the search log",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Export every database result set in full (RIS or BibTeX), "
                        "date-stamped, into a reference manager. Zotero is free and handles tens of "
                        "thousands of records; EndNote and Mendeley are the paid and semi-free "
                        "alternatives. Deduplicate before screening: the same paper arrives from "
                        "three databases with three slightly different titles, and screening it three "
                        "times wastes the second screener's day."},
                       {"t": "body", "cls": "sm", "html": "Deduplication tools: Zotero's built-in merge, "
                        "the free <em>Deduklick</em> and <em>SRA Deduplicator</em>, or Rayyan's "
                        "detection on import. Record how many duplicates were removed; PRISMA asks."}],
              "right": [{"t": "table",
                         "head": ["Log entry", "Example"],
                         "rows": [
                             ["Database", "Scopus"],
                             ["Date", "2026-09-10"],
                             ["String", "TITLE-ABS-KEY((\"self-help group*\" OR SHG) AND (women OR female) AND (empower* OR \"decision-making\"))"],
                             ["Limits", "2000&ndash;2026; no language limit"],
                             ["Records", "1,412"],
                             ["Exported as", "scopus_shg_20260910.ris"]]}]},
         ]},

        # ===================== SECTION 04: SCREENING =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Screening and Selection"},

        {"type": "content", "label": "Two Stages", "title": "Titles and abstracts first, full texts second",
         "blocks": [
             {"t": "flow", "steps": ["Records after dedup", "Title/abstract screen", "Full texts sought", "Full-text screen", "Included studies"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Stage one", "html":
                        "Every record is read by two people against the eligibility criteria, "
                        "quickly, and marked include, exclude or unsure. The rule is <em>when in "
                        "doubt, keep</em>: a wrongly excluded study is lost for good, a wrongly "
                        "included one costs a full-text read. At this stage a reviewer manages "
                        "one to two hundred records an hour."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Stage two", "html":
                         "The full text of every surviving record is obtained and read against the "
                         "criteria in full. Each exclusion is given a reason from a fixed list "
                         "(wrong population, wrong design, no comparison group, outcome not "
                         "reported), and the reasons are counted. A study excluded here for "
                         "\"wrong design\" should be listed by name in an appendix; readers will ask "
                         "why a study they know is missing."}]},
         ]},

        {"type": "content", "label": "Dual Screening", "title": "Two screeners, and how much they disagree",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Independent screening by two people, with disagreements settled by "
                        "discussion or a third reviewer, is the standard in every guidance document. "
                        "Single screening misses studies: Waffenschmidt and colleagues' methods study "
                        "(<em>BMC Medical Research Methodology</em> 2019, 19:132) found single screeners "
                        "missed a median of 13 per cent of eligible records. Report the agreement, "
                        "usually as Cohen's kappa, and the number of conflicts."},
                       {"t": "term", "word": "Cohen's kappa",
                        "def": "Agreement between two raters corrected for the agreement expected by "
                        "chance. Values above 0.6 are conventionally read as substantial; below 0.4 "
                        "the criteria are probably ambiguous and need rewording before screening continues."}],
              "right": [{"t": "panel", "color": "green", "title": "The pilot", "html":
                         "Before screening in earnest, both screeners take the same 100 records, "
                         "compare, and argue about every disagreement. Most disagreements turn out to "
                         "be criteria that were not as clear as they seemed. Fix the wording, record "
                         "the change as a protocol amendment, and then start. Kappa on the pilot is "
                         "the number to report."}]},
         ]},

        {"type": "content", "label": "Tools", "title": "Rayyan, Covidence and the spreadsheet",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Does", "Limit"],
              "rows": [
                  ["Rayyan", "Free tier", "Blinded dual screening, conflict resolution, deduplication, keyword highlighting", "Full-text management is basic"],
                  ["Covidence", "Paid; free for Cochrane authors", "Screening, extraction forms, risk of bias, PRISMA numbers", "Cost for a student team"],
                  ["EPPI-Reviewer", "Paid; some free access", "Coding, screening, machine-learning priority screening", "Learning curve"],
                  ["ASReview", "Free, open source", "Active-learning screening: ranks records by predicted relevance", "A stopping rule must be chosen and reported"],
                  ["Zotero + a spreadsheet", "Free", "Everything, by hand", "Blinding and conflicts are manual"]]},
             {"t": "body", "html": "Rayyan (Ouzzani and colleagues, <em>Systematic Reviews</em> 2016, 5:210) "
              "is the default for a team without a budget: import the RIS files, invite the second "
              "screener, switch on blind mode so neither sees the other's votes, and resolve conflicts "
              "at the end. It counts everything PRISMA asks for."},
         ]},

        {"type": "content", "label": "Machine Assistance", "title": "Prioritised screening: what it can and cannot replace",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Active-learning tools such as ASReview and the classifier in "
                        "EPPI-Reviewer learn from your first decisions and re-order the remaining "
                        "records so the likely includes come first. On large sets they let a team "
                        "find most eligible studies after screening a fraction of the pile. They do "
                        "not decide; a person still reads each record that is shown."},
                       {"t": "body", "cls": "sm", "html": "Large language models are now used the same way, "
                        "and the evidence on their recall is mixed and moving. Until a standard "
                        "exists, treat an LLM as a third screener whose decisions are checked, never "
                        "as a replacement for the second human."}],
              "right": [{"t": "panel", "color": "amber", "title": "The stopping rule", "html":
                         "The unsolved problem is when to stop. Screening until 50 consecutive "
                         "records are irrelevant, or until a statistical estimate of remaining "
                         "includes falls below one, are the usual rules, and each must be stated "
                         "in the methods. A review that says \"we used ASReview\" and nothing more "
                         "has not described its screening."}]},
         ]},

        {"type": "content", "label": "The Flow Diagram", "title": "PRISMA's flow diagram: every record accounted for",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Stage", "Count", "Where it goes"],
                        "rows": [
                            ["Records identified from databases", "4,212", "Box 1, by database"],
                            ["Records from other sources", "318", "Registers, websites, citation chasing, separately"],
                            ["Duplicates removed", "1,140", "Before screening"],
                            ["Records screened (title/abstract)", "3,390", ""],
                            ["Records excluded", "3,102", ""],
                            ["Reports sought for retrieval", "288", ""],
                            ["Reports not retrieved", "9", "Named in appendix"],
                            ["Reports assessed for eligibility", "279", ""],
                            ["Reports excluded, with reasons", "241", "Counts per reason"],
                            ["Studies included", "38 (in 41 reports)", "Studies, not papers"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative counts. The 2020 diagram (Page and "
                        "colleagues, <em>BMJ</em> 2021, 372:n71) separates database records from "
                        "other-source records and distinguishes <em>studies</em> from <em>reports</em>: "
                        "one trial may produce three papers and one paper may report two trials. Count "
                        "studies for the synthesis, reports for retrieval."},
                        {"t": "hbox", "color": "cyan", "html": "The diagram is the first thing a "
                         "methodologist reads. If the arithmetic does not add up, nothing after it is "
                         "trusted."}]},
         ]},

        {"type": "content", "label": "Full Texts", "title": "Getting the papers, and what to do when you cannot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Institutional library access, then the free routes: Unpaywall (browser extension), Europe PMC, author manuscripts on RePEc, SSRN and institutional repositories.",
                  "Email the corresponding author. Response rates are low but non-zero, and the email is the same one you will send for missing statistics later.",
                  "Interlibrary loan through INFLIBNET's N-LIST or a university library, which reaches most Indian institutions.",
                  "Report the number not retrieved and list them. A reader may have access you lack."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Reports in other languages", "html":
                         "A study in Bangla, Tamil or Nepali is eligible if it meets the criteria. "
                         "Exclusion by language is a decision to be justified, not a default, and "
                         "reviews that impose it should say what they lost. Machine translation is "
                         "now adequate for screening; extraction should be checked by a reader of "
                         "the language."}]},
         ]},

        {"type": "content", "label": "Scale", "title": "What 5,000 records actually means",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "5,000", "label": "records after deduplication", "color": "cyan", "source": "Illustrative"},
                 {"num": "50&ndash;80 h", "label": "of title/abstract screening, per screener", "color": "amber", "source": "At 60&ndash;100 records an hour"},
                 {"num": "300", "label": "full texts to obtain and read, at 30&ndash;60 minutes each", "color": "green", "source": "Illustrative"}]},
             {"t": "body", "html": "So a modest development review costs two people roughly three working "
              "weeks of screening before extraction begins. The way to cut it is upstream: a tighter "
              "search string, a narrower date window, or exclusion of designs that cannot answer the "
              "question. The way not to cut it is to skip the second screener, which trades weeks of "
              "labour for a review whose completeness cannot be defended."},
             {"t": "hbox", "color": "cyan", "html": "Budget the screening in hours before agreeing "
              "the timeline. Commissioners who want a review in eight weeks are usually asking for a "
              "rapid review, and should be told so."},
         ]},

        # ===================== SECTION 05: DATA EXTRACTION =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Data Extraction"},

        {"type": "content", "label": "The Form", "title": "Design the extraction form before you open a paper",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Extraction is the step where 40 papers become one "
                        "table. The form decides what that table can answer, so it is written from "
                        "the protocol, not from the first paper you happen to read. A field that is "
                        "missing from the form is missing from the review, and adding it after 20 "
                        "papers means going back through 20 papers."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "One row per study, one column per item, coded where possible (country as ISO code, design as a fixed list) so the table can be sorted and counted.",
                           "Free-text fields for anything that will be quoted: the intervention description, the outcome definition, the authors' own caveats.",
                           "A 'page and table' column for every number, so a second extractor or a reader can find it in seconds.",
                           "A 'notes and doubts' column. Half the value of extraction is the queries it raises."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Pilot it on five studies", "html":
                         "Two extractors take the same five papers, fill the form independently and "
                         "compare. Every disagreement is either a form problem (the field was "
                         "ambiguous) or a paper problem (the study reports it two ways). Fix the "
                         "form, write the decision into a guidance note, then extract the rest. "
                         "Cochrane's Handbook (chapter 5) asks for exactly this pilot and for the "
                         "form to be included with the protocol."},
                        {"t": "hbox", "color": "cyan", "html": "Keep the raw extraction and the "
                         "analysis table separate. The first records what the paper says; the "
                         "second records what you did with it."}]},
         ]},

        {"type": "content", "label": "What to Extract", "title": "The items every review needs, and the ones people forget",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Group", "Items", "Why it matters later"],
              "rows": [
                  ["Identification", "Study ID, all reports of it, year, country, funder, registration number", "Linking reports to studies; funding as a bias signal"],
                  ["Setting", "Rural/urban, state or district, baseline poverty or prevalence, delivery agency", "Applicability to your context; subgroup analysis"],
                  ["Population", "Eligibility, age, sex, numbers randomised and analysed per arm", "Attrition; denominators for effect sizes"],
                  ["Intervention", "Components, intensity, duration, who delivered, cost if reported, comparator in the same detail", "The comparator explains half of all heterogeneity"],
                  ["Design", "RCT/cluster/quasi-experimental method, unit of assignment, clustering handled?", "Cluster trials analysed as individual data have false precision"],
                  ["Outcomes", "Every outcome and timepoint pre-specified in the protocol, with definition, instrument and who measured it", "Selective reporting; measurement bias"],
                  ["Results", "Means and SDs, or counts and denominators, or coefficients with SEs, per arm and timepoint", "Effect sizes; never extract only the p-value"],
                  ["Analysis", "Adjusted vs unadjusted, covariates, intention-to-treat vs per-protocol", "Which estimate to pool"],
                  ["Authors' claims", "Their stated conclusion, verbatim", "For the discrepancy check between claim and data"]]},
             {"t": "body", "cls": "sm", "html": "The rows people forget are the comparator, the "
              "unit of assignment and the timepoints. A microfinance review that records 'access to "
              "credit' as the intervention and nothing about what the control group could borrow "
              "is pooling different contrasts under one name."},
         ]},

        {"type": "content", "label": "From Paper to Number", "title": "Getting an effect size out of what was reported",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Paper reports", "You need", "Conversion"],
                        "rows": [
                            ["Mean, SE, n per arm", "SD", "SD = SE &times; &radic;n"],
                            ["Mean and 95% CI", "SD", "SD = &radic;n &times; (upper &minus; lower) / 3.92"],
                            ["Median and IQR", "Mean and SD", "Approximate (Wan et al. 2014, <em>BMC Med Res Methodol</em> 14:135); note the approximation"],
                            ["Regression coefficient and SE", "Mean difference", "Use directly if unadjusted comparison; adjusted estimates pooled separately"],
                            ["t-statistic and n", "SMD", "d = t &times; &radic;(1/n<sub>1</sub> + 1/n<sub>2</sub>)"],
                            ["Percentages and n per arm", "Risk ratio, odds ratio", "Rebuild the 2&times;2 table; take logs before pooling"],
                            ["'Significant at 5%' only", "Nothing usable", "Email the authors; otherwise record as not extractable"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "The Cochrane Handbook chapter 6 gives "
                        "every formula, and the Campbell Collaboration's online effect-size "
                        "calculator (David Wilson's) implements them. Record the route taken for "
                        "each number in the extraction form. Two reviews that pool the same "
                        "studies can disagree because one converted from CIs and the other from "
                        "t-statistics."},
                        {"t": "hbox", "color": "amber", "html": "Economics papers report "
                         "coefficients from many specifications. Extract the one the protocol "
                         "named (usually the authors' preferred, fully-specified estimate) and "
                         "record the others in notes."}]},
         ]},

        {"type": "content", "label": "Dual Extraction", "title": "Two extractors, because one makes errors nobody catches",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "+21.7%", "label": "more errors with single extraction than double (relative difference, P = 0.019)", "color": "red", "source": "Buscemi et al. 2006, <em>J Clin Epidemiol</em> 59:697"},
                 {"num": "&minus;36.1%", "label": "less time for single extraction: the saving that buys those errors", "color": "amber", "source": "Same trial, reviewers randomised to roles"},
                 {"num": "2", "label": "extractors per outcome, the Cochrane minimum for numerical data", "color": "green", "source": "Cochrane Handbook, ch. 5"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Buscemi and colleagues randomised reviewers to "
                        "extract or verify, blind to the hypothesis, and counted errors against "
                        "the source papers. Single extraction produced a fifth more errors, at a "
                        "third less time. Effect estimates barely moved in that pilot, but the "
                        "errors were in numbers that feed a meta-analysis, and in a smaller review "
                        "one wrong SD can move the pooled result. The cost of double extraction "
                        "is 20&ndash;30 hours on a 40-study review."}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "Where the team is small, use one extractor and a second who verifies every number against the paper. That is cheaper than two full extractions and catches most errors.",
                  "Resolve disagreements by going back to the paper, not by averaging.",
                  "Report the method: 'Data were extracted by one reviewer and checked by a second' is honest and acceptable in most journals."]}]},
         ]},

        {"type": "content", "label": "Complications", "title": "Multiple arms, multiple reports, clustered designs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "One study, three arms", "html":
                         "A trial comparing cash, cash plus training and control gives two "
                         "comparisons sharing one control group. Pooling both as if independent "
                         "double-counts the control. Options: combine the two treatment arms into "
                         "one (Cochrane Handbook, chapter 23), split the control group between them, or "
                         "pick the arm that matches the review question and record the choice."},
                        {"t": "panel", "color": "amber", "title": "One study, three papers", "html":
                         "A working paper, a journal article and a follow-up. Link them under one "
                         "study ID, extract from the most complete report, and note where numbers "
                         "differ between versions. The published version is not always the most "
                         "complete: journals cut tables that working papers keep."}],
              "right": [{"t": "panel", "color": "green", "title": "Cluster-randomised trials", "html":
                         "Most development trials randomise villages or schools. If the paper "
                         "analysed at the individual level without accounting for clustering, its "
                         "standard errors are too small. Inflate them by the design effect, "
                         "1 + (m &minus; 1)&rho;, where m is the average cluster size and &rho; the "
                         "intra-cluster correlation, using an ICC from the paper or from a similar "
                         "study, and say which."},
                        {"t": "hbox", "color": "cyan", "html": "Every one of these decisions goes in "
                         "the methods section. A reader who cannot reproduce your effect size from "
                         "the paper and your stated rules cannot check the review."}]},
         ]},

        {"type": "content", "label": "Missing Data", "title": "What the paper does not say, and asking for it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Many trials in any health review report no usable standard "
                        "deviation for at least one outcome, and the share is higher in "
                        "economics, where results arrive as regression tables. There are three "
                        "responses, in order of preference."},
                       {"t": "flow", "steps": [
                           "ASK: one email to the corresponding author with a precise request and a deadline",
                           "DERIVE: from CIs, SEs, t-statistics, or related outcomes in the same paper",
                           "IMPUTE: borrow an SD from similar studies, and test whether the result changes"]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Ask for the specific number, not 'the data'. 'The standard deviation of household consumption at endline in the treatment and control arms, Table 4' gets answered; 'your dataset' does not.",
                  "Set a deadline of three weeks and log every request and reply in the review record.",
                  "If you impute, run the meta-analysis with and without the imputed studies and report both. If the conclusion depends on the imputation, say so in the abstract.",
                  "Never treat 'not reported' as 'no effect'. A missing outcome is a risk-of-bias signal and is recorded as one."]},
                        {"t": "hbox", "color": "green", "html": "Selective reporting is common enough "
                         "that RoB 2 has a whole domain for it. Missing numbers are evidence, not "
                         "just an inconvenience."}]},
         ]},

        # ===================== SECTION 06: RISK OF BIAS =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Risk of Bias and Study Quality"},

        {"type": "content", "label": "Why Appraise", "title": "A pooled estimate is only as good as its worst well-weighted study",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Risk of bias is the likelihood that a study's design "
                        "or conduct led it to over- or under-estimate the true effect. It is about "
                        "internal validity, not about whether the study was well written, large, "
                        "or published in a good journal. A large trial with broken randomisation "
                        "is at high risk; a small one with concealed allocation and complete "
                        "follow-up is at low risk."},
                       {"t": "term", "word": "Risk of bias",
                        "def": "A judgement, per study and per outcome, about whether specific "
                        "features of design or conduct could have produced a systematic error in "
                        "the estimated effect. Assessed by domain, never by a summed score."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Assess per outcome, not per study. Blinding matters for a self-reported outcome and hardly at all for mortality.",
                  "Two assessors, independently, with disagreements resolved by discussion. Report the agreement.",
                  "The judgement feeds three later steps: sensitivity analysis (drop high-risk studies), GRADE (downgrade for risk of bias), and the discussion.",
                  "Do not sum points. Scales such as Jadad weight items arbitrarily; Cochrane advises against any scale that produces a total score (Handbook, chapter 7)."]}]},
         ]},

        {"type": "content", "label": "RoB 2", "title": "Cochrane RoB 2 for randomised trials: five domains",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Domain", "Question it asks", "A development example"],
              "rows": [
                  ["1. Randomisation process", "Was the sequence random and allocation concealed? Do baselines suggest a problem?", "Lottery in public with sealed lists: low. NGO staff choosing 'eligible' villages after the list: high"],
                  ["2. Deviations from intended interventions", "Did participants or staff know the assignment, and did that change what they did? Was the analysis appropriate?", "Control villages receiving a similar scheme from another donor mid-trial"],
                  ["3. Missing outcome data", "How much attrition, and was it related to the outcome?", "30% attrition in a migration-prone district, higher in the control arm"],
                  ["4. Measurement of the outcome", "Was the assessor blind? Could knowing the assignment change the measurement?", "Enumerators from the implementing NGO measuring self-reported income"],
                  ["5. Selection of the reported result", "Was there a pre-analysis plan, and does the paper report what it planned?", "Twelve outcomes measured, three reported, no registration"]]},
             {"t": "body", "cls": "sm", "html": "Sterne and colleagues, <em>BMJ</em> 2019, "
              "366:l4898. Each domain gets one of three judgements: low risk, some concerns, "
              "high risk, reached through signalling questions with a written algorithm. The "
              "overall judgement is the worst domain. Assess per outcome. The tool and its "
              "guidance are free at riskofbias.info."},
         ]},

        {"type": "content", "label": "ROBINS-I", "title": "ROBINS-I for non-randomised studies: the confounding domain comes first",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Domain", "Judgement hinges on"],
                        "rows": [
                            ["Confounding", "Were the important confounders (listed in advance by the review team) measured and controlled? Time-varying confounding?"],
                            ["Selection of participants", "Did entry into the study depend on characteristics observed after the intervention started?"],
                            ["Classification of interventions", "Was exposure status defined clearly and recorded without knowledge of outcome?"],
                            ["Deviations from intended interventions", "Co-interventions, contamination, switching"],
                            ["Missing data", "Attrition, and whether it differs by arm and outcome"],
                            ["Measurement of outcomes", "Assessor knowledge of exposure; comparable methods across groups"],
                            ["Selection of the reported result", "Multiple analyses, subgroups, outcomes, with no plan"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Sterne and colleagues, <em>BMJ</em> "
                        "2016, 355:i4919. Judgements run low, moderate, serious, critical, or no "
                        "information. 'Low' means comparable to a well-conducted trial, which a "
                        "matching study rarely reaches; 'critical' means the study is too "
                        "problematic to inform the synthesis and is dropped from it."},
                        {"t": "hbox", "color": "amber", "html": "The confounding domain requires "
                         "the review team to write down, in the protocol, which confounders a "
                         "credible study must handle. For a cash-transfer review that is baseline "
                         "income, household size, and programme targeting rules."}]},
         ]},

        {"type": "content", "label": "Quasi-Experiments", "title": "Appraising DiD, matching, IV and RDD studies",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Development evidence is mostly quasi-experimental, "
                        "and generic tools written for cohort studies miss the questions an "
                        "economist would ask. 3ie and the Campbell Collaboration's International "
                        "Development Coordinating Group developed a risk-of-bias tool for these "
                        "designs (Waddington and colleagues, <em>J Clin Epidemiol</em> 2017, "
                        "89:43, paper 6 of the quasi-experimental series), organised around the identifying assumption of each method."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Difference-in-differences: is there evidence for parallel pre-trends, and are there enough pre-periods to see them?",
                           "Matching: was there common support, and were the matched covariates measured before treatment?",
                           "Instrumental variables: is the exclusion restriction argued rather than asserted, and is the first stage strong (F above 10, or the newer Lee et al. 2022 thresholds)?",
                           "Regression discontinuity: is the running variable manipulable? Is there a density test at the cut-off?"]}],
              "right": [{"t": "panel", "color": "green", "title": "Two further checks for any design", "html":
                         "Was the estimate pre-registered, or does the paper read like the specification "
                         "was found after the fact? And is the reported outcome the one the "
                         "programme aimed at, or a proxy chosen because it moved? Brodeur, Cook "
                         "and Heyes (<em>American Economic Review</em> 2020, 110:3634) find "
                         "bunching of test statistics just above conventional thresholds in IV "
                         "and DiD papers, and much less in RCTs and RDD."},
                        {"t": "hbox", "color": "amber", "html": "Record the identifying assumption "
                         "and the evidence for it in the extraction form. It is the single item "
                         "that most determines the weight a study should get."}]},
         ]},

        {"type": "content", "label": "Observational and Qualitative", "title": "Tools for the other designs you will meet",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "Tool", "Notes"],
              "rows": [
                  ["Cohort, case-control", "Newcastle-Ottawa Scale; ROBINS-I", "NOS is widely used and has poor inter-rater reliability (Hartling et al. 2013, <em>J Clin Epidemiol</em> 66:982); prefer ROBINS-I where the question is causal"],
                  ["Cross-sectional prevalence", "JBI critical appraisal checklist; Hoy et al. 2012 tool", "Sampling frame, response rate and case definition are the items that matter"],
                  ["Diagnostic accuracy", "QUADAS-2", "Four domains: patient selection, index test, reference standard, flow and timing"],
                  ["Qualitative", "CASP qualitative checklist; JBI qualitative tool", "Appraises credibility and reflexivity, not bias; feeds GRADE-CERQual"],
                  ["Mixed methods", "MMAT (Hong et al. 2018)", "One tool across designs, five items each, no summed score"],
                  ["Economic evaluations", "CHEERS 2022 (reporting); Drummond checklist", "Costing perspective and discount rate are the usual gaps"],
                  ["Modelling and simulation", "No standard tool", "Judge against ISPOR good-practice guidance; say that no validated tool exists"]]},
             {"t": "body", "cls": "sm", "html": "Whichever tool you use, present the results per "
              "study in a table or a traffic-light figure (the <em>robvis</em> R package and web "
              "app draw these from a spreadsheet), and use them. An appraisal that is reported and "
              "then ignored in the synthesis is decoration."},
         ]},

        {"type": "content", "label": "Publication Bias", "title": "The studies you did not find are not a random sample",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Studies with significant, positive results are more "
                        "likely to be written up, submitted, accepted and cited. A review that "
                        "pools only what is published therefore starts biased upward. Franco, "
                        "Malhotra and Simonovits (<em>Science</em> 2014, 345:1502) traced 221 "
                        "social-science experiments run through one funded programme (TESS), so "
                        "the file drawer could be seen: about two-thirds of the null results were "
                        "never written up at all, and strong results were 60 percentage points "
                        "more likely to be written up and 40 points more likely to be published."},
                       {"t": "stats", "cols": 2, "cards": [
                           {"num": "10 of 48", "label": "null-result studies published", "color": "red", "source": "Franco et al. 2014, TESS studies"},
                           {"num": "56 of 91", "label": "strong-result studies published", "color": "green", "source": "Same sample"}]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Prevention beats detection: search registries, working-paper series, evaluation repositories and theses so unpublished work is in the review.",
                  "Detection: a funnel plot of effect against precision, and Egger's regression test for asymmetry (Egger et al. 1997, <em>BMJ</em> 315:629). Neither is meaningful with fewer than ten studies (Cochrane Handbook, chapter 13).",
                  "Asymmetry has other causes, including true heterogeneity where small studies target populations with larger effects. Say which explanation you favour and why.",
                  "In economics, the FAT-PET framework (Stanley and Doucouliagos 2012) regresses effect on standard error; the intercept is the bias-corrected estimate. Andrews and Kasy (<em>AER</em> 2019, 109:2766) offer a selection-model correction."]}]},
         ]},

        {"type": "content", "label": "Funnel Plots", "title": "Reading a funnel plot, and what it cannot tell you",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Each study is a point: effect size on the horizontal "
                        "axis, standard error (inverted, so precise studies sit at the top) on the "
                        "vertical. Without bias the points form a symmetrical funnel around the "
                        "pooled estimate, because small studies scatter more. With publication "
                        "bias the bottom-left corner, small studies with small or negative effects, "
                        "is empty."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Trim-and-fill (Duval and Tweedie 2000, <em>Biometrics</em> 56:455) imputes the missing mirror-image studies and re-pools. Treat it as a sensitivity analysis, not a corrected estimate.",
                           "Contour-enhanced funnel plots shade the regions of significance, which helps separate publication bias from other asymmetry.",
                           "Do not draw one for a review of eight studies. It will look asymmetric or symmetric by chance, and readers will over-read it."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Where the asymmetry comes from in development", "html":
                         "Small pilot studies run by the implementing organisation in a favourable site; "
                         "larger, independent replications at scale with smaller effects. Vivalt "
                         "(<em>Journal of the European Economic Association</em> 2020, 18:3045) "
                         "finds across 20 intervention types that government-implemented "
                         "programmes report smaller effects than NGO- or researcher-implemented "
                         "ones, and that effect sizes are hard to predict from one setting to the "
                         "next. That is heterogeneity, not only bias, and the review should "
                         "model it rather than 'correct' it away."},
                        {"t": "hbox", "color": "cyan", "html": "Report the plot, the test, and your "
                         "reading of it. The reader is entitled to disagree."}]},
         ]},

        {"type": "content", "label": "Using the Appraisal", "title": "Three places the risk-of-bias judgement must show up",
         "blocks": [
             {"t": "flow", "steps": [
                 "TABLE: per-study, per-domain judgements with the reason for each, in the report or appendix",
                 "SYNTHESIS: sensitivity analysis restricted to low-risk studies; subgroup by risk if enough studies",
                 "CERTAINTY: GRADE downgrade for risk of bias when high-risk studies drive the estimate",
                 "DISCUSSION: what the bias would do to the direction of the result, stated plainly"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The most common failure in published development "
                        "reviews is a careful appraisal table followed by a synthesis that treats "
                        "every study alike. If the pooled estimate falls by half when high-risk "
                        "studies are removed, that is the finding, and it belongs in the abstract."}],
              "right": [{"t": "hbox", "color": "green", "html": "Write the sentence now: 'Restricting "
                        "to studies at low risk of bias (k = 6) gave a pooled effect of X, compared "
                        "with Y for all studies.' If you cannot write it, the appraisal was not "
                        "used."}]},
         ]},

        # ===================== SECTION 07: META-ANALYSIS =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Meta-Analysis"},

        {"type": "content", "label": "The Idea", "title": "A weighted average, where precision sets the weight",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Meta-analysis",
                        "def": "The statistical combination of effect estimates from two or more "
                        "studies into one pooled estimate with a confidence interval, each study "
                        "weighted by the inverse of its variance, so that precise studies count "
                        "for more."},
                       {"t": "body", "html": "The arithmetic is short. What takes judgement is "
                        "deciding whether the studies are similar enough to combine, which effect "
                        "measure to combine, whether to assume one true effect or a distribution "
                        "of them, and how to describe the disagreement between studies. A pooled "
                        "number with no account of those choices is a number nobody should use."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Pool only when the protocol said you would, and only studies that ask the same question of comparable populations with a comparable comparator.",
                  "Two studies can be meta-analysed. The result will be fragile and the heterogeneity estimate near useless, and both should be said.",
                  "The pooled estimate is not the truth. It is the best summary of these studies, subject to their biases and to what was not found.",
                  "Never pool across effect measures. Convert everything to one metric first, and record the conversions."]},
                        {"t": "hbox", "color": "amber", "html": "Apples and oranges can be combined "
                         "if the question is about fruit. The protocol defines the fruit."}]},
         ]},

        {"type": "content", "label": "Effect Measures", "title": "Choosing what to pool",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Outcome type", "Measure", "When to use it", "Watch for"],
              "rows": [
                  ["Continuous, same scale", "Mean difference (MD)", "All studies report the outcome in the same units: rupees per month, cm, test score on one instrument", "Units and scaling (monthly vs annual) must match exactly"],
                  ["Continuous, different scales", "Standardised mean difference (Hedges' g)", "Studies use different tests or indices for the same construct", "Sensitive to the SD used; heterogeneous populations widen SDs and shrink g"],
                  ["Binary", "Risk ratio (RR)", "Most interpretable for events such as enrolment, immunisation, default", "Cannot be used when the control event rate is zero"],
                  ["Binary", "Odds ratio (OR)", "Case-control designs; logistic regressions", "Overstates RR when events are common; often misread as RR"],
                  ["Binary", "Risk difference (RD)", "Absolute effect for policy: percentage points of coverage gained", "Varies with baseline rate, so usually more heterogeneous than RR"],
                  ["Rate", "Rate ratio, hazard ratio", "Events per person-time; survival", "Hazard ratios need the estimate and CI from the paper; rarely derivable"],
                  ["Regression coefficient", "Partial correlation, elasticity, or MD from coefficient", "Economics literatures where every study is a regression", "Comparability across specifications; see Stanley and Doucouliagos 2012"]]},
             {"t": "body", "cls": "sm", "html": "Ratios are pooled on the log scale and "
              "back-transformed. Hedges' g corrects Cohen's d for small samples by "
              "J = 1 &minus; 3 / (4df &minus; 1); at 20 participants per arm the correction is "
              "about 2%. Kraft (<em>Educational Researcher</em> 2020, 49:241) argues that in "
              "education 0.05 SD is small, 0.05&ndash;0.20 medium and above 0.20 large, against "
              "Cohen's 0.2/0.5/0.8, which came from psychology and are far too demanding for "
              "field programmes."},
         ]},

        {"type": "content", "label": "Worked Example", "title": "Three studies, fixed-effect: the arithmetic in full",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Study", "Effect (SMD)", "SE", "Weight w = 1/SE&sup2;", "Share", "w &times; effect"],
                        "rows": [
                            ["A", "0.20", "0.10", "100", "19.0%", "20.00"],
                            ["B", "0.35", "0.20", "25", "4.8%", "8.75"],
                            ["C", "0.05", "0.05", "400", "76.2%", "20.00"],
                            ["Sum", "", "", "525", "100%", "48.75"]]},
                       {"t": "body", "cls": "sm", "html": "Pooled effect = 48.75 / 525 = "
                        "<strong>0.093</strong>. SE of the pooled effect = &radic;(1/525) = 0.044. "
                        "95% CI = 0.093 &plusmn; 1.96 &times; 0.044 = "
                        "<strong>0.007 to 0.178</strong>. Illustrative numbers."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the table shows", "html":
                         "Study C, the most precise, carries three-quarters of the weight and "
                         "pulls the pooled estimate toward its own 0.05. Study B, with the largest "
                         "effect, barely registers. Precision, not effect size and not sample "
                         "size directly, is what decides influence. A study's weight in a forest "
                         "plot is drawn as the size of its square for this reason."},
                        {"t": "hbox", "color": "amber", "html": "This is the fixed-effect model: it "
                         "assumes A, B and C estimate the same true effect and differ only by "
                         "sampling error. The next slide tests that assumption."}]},
         ]},

        {"type": "content", "label": "Heterogeneity", "title": "Q, I&sup2; and &tau;&sup2;: measuring how much the studies disagree",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Statistic", "Formula", "Our example", "Reads as"],
                        "rows": [
                            ["Cochran's Q", "&Sigma; w<sub>i</sub>(&theta;<sub>i</sub> &minus; &theta;&#770;)&sup2;", "3.54 on 2 df (p = 0.17)", "A test with low power when k is small; do not rely on its p-value"],
                            ["I&sup2;", "(Q &minus; df) / Q", "43%", "Share of observed variation beyond chance; a proportion, not an amount"],
                            ["&tau;&sup2;", "(Q &minus; df) / C, C = &Sigma;w &minus; &Sigma;w&sup2;/&Sigma;w", "0.0077 (&tau; = 0.088)", "Between-study variance in effect-size units; the amount"],
                            ["Prediction interval", "&theta;&#770; &plusmn; t<sub>k&minus;2</sub> &radic;(&tau;&sup2; + SE&sup2;)", "Wide, with k = 3", "Where a new study's effect would likely fall"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Higgins and Thompson (<em>Statistics "
                        "in Medicine</em> 2002, 21:1539) introduced I&sup2;; the Cochrane Handbook "
                        "reads 0&ndash;40% as possibly unimportant, 30&ndash;60% moderate, "
                        "50&ndash;90% substantial, 75&ndash;100% considerable, with the overlaps "
                        "deliberate. I&sup2; rises with study precision even when &tau;&sup2; does "
                        "not, so large trials produce high I&sup2; for small disagreements."},
                        {"t": "hbox", "color": "green", "html": "Report all three, and the "
                         "prediction interval. IntHout and colleagues (<em>BMJ Open</em> 2016, "
                         "6:e010247) found that in a fifth of Cochrane reviews with a significant "
                         "pooled effect the prediction interval included harm."}]},
         ]},

        {"type": "content", "label": "Random Effects", "title": "The same three studies under a random-effects model",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Study", "Effect", "SE&sup2; + &tau;&sup2;", "Weight w*", "Share", "Fixed share"],
                        "rows": [
                            ["A", "0.20", "0.0100 + 0.0077", "56.6", "32.2%", "19.0%"],
                            ["B", "0.35", "0.0400 + 0.0077", "21.0", "11.9%", "4.8%"],
                            ["C", "0.05", "0.0025 + 0.0077", "98.2", "55.9%", "76.2%"],
                            ["Pooled", "<strong>0.134</strong>", "SE 0.075", "175.8", "", "FE: 0.093"]]},
                       {"t": "body", "cls": "sm", "html": "95% CI: <strong>&minus;0.014 to "
                        "0.282</strong>, against 0.007 to 0.178 under fixed effect. Adding "
                        "&tau;&sup2; to every study's variance flattens the weights: the small "
                        "study gains, the large one loses, and the interval widens to reflect "
                        "the disagreement. The conclusion changed from 'significant' to 'not'. "
                        "Illustrative numbers."}],
              "right": [{"t": "panel", "color": "amber", "title": "Which model, and which estimator", "html":
                         "Fixed effect answers 'what is the one common effect?'; random effects "
                         "answers 'what is the average of a distribution of effects?'. Development "
                         "programmes differ by site, implementer and comparator, so random effects "
                         "is the default and the protocol should say so before the data are seen. "
                         "DerSimonian and Laird (1986) is the classic &tau;&sup2; estimator and is "
                         "still the default in RevMan; REML is better with few studies, and the "
                         "Hartung-Knapp adjustment to the interval is recommended when k is small "
                         "(IntHout, Ioannidis and Borm, <em>BMC Med Res Methodol</em> 2014, 14:25)."},
                        {"t": "hbox", "color": "cyan", "html": "Random effects is not a fix for "
                         "heterogeneity. It describes it. Explaining it is the next slide."}]},
         ]},

        {"type": "content", "label": "Forest Plots", "title": "Reading a forest plot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "One row per study: the point estimate as a square whose area is the weight, the confidence interval as a horizontal line.",
                  "The vertical line of no effect at 0 (differences) or 1 (ratios). A study's line crossing it means that study alone cannot rule out no effect.",
                  "The diamond at the bottom is the pooled estimate; its width is the confidence interval. Some plots add a bar for the prediction interval, which is the honest one.",
                  "Below the diamond: k, Q, I&sup2;, &tau;&sup2;, and the test for overall effect.",
                  "Order the rows by something meaningful (year, risk of bias, effect size), never alphabetically. Sorted by effect, a plot shows heterogeneity at a glance."]}],
              "right": [{"t": "panel", "color": "green", "title": "Five questions to ask of any forest plot", "html":
                         "Do the intervals overlap, or are there two clusters? Is one study "
                         "carrying most of the weight, and is it at low risk of bias? Do the small "
                         "studies sit systematically to one side? Does the diamond's interval "
                         "exclude no effect, and does the prediction interval? Would a "
                         "policymaker reading only the diamond be misled by what the rows show?"},
                        {"t": "hbox", "color": "amber", "html": "A diamond that excludes zero above "
                         "rows that mostly cross it is a common and legitimate result. A diamond "
                         "that excludes zero above two clusters of rows on opposite sides of it is "
                         "a result that should not have been pooled."}]},
         ]},

        {"type": "content", "label": "Explaining Heterogeneity", "title": "Subgroups and meta-regression",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "When studies disagree, the interesting question is "
                        "why. Subgroup analysis splits the studies by a characteristic named in the "
                        "protocol (implementer, region, intensity, risk of bias) and tests whether "
                        "the pooled effects differ. Meta-regression does the same with a "
                        "continuous moderator, or several at once, by regressing effect size on "
                        "study characteristics with weights."},
                       {"t": "bullets", "color": "amber", "items": [
                           "Pre-specify the subgroups and keep them few. Ten post-hoc subgroups will produce one 'significant' difference by chance.",
                           "Cochrane's rule of thumb: at least ten studies per moderator in a meta-regression. With 15 studies, one moderator.",
                           "Test the difference between subgroups, not whether each subgroup's effect is significant on its own.",
                           "Study-level moderators are ecological. 'Effects are larger in studies with more women' is not 'effects are larger for women'."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Two economics examples", "html":
                         "Card, Kluve and Weber (<em>Journal of the European Economic "
                         "Association</em> 2018, 16:894) meta-analyse over 200 active labour "
                         "market evaluations and find that programme type and time horizon "
                         "explain much of the variation: training shows small short-run effects "
                         "and larger ones after two years. Meager (<em>AEJ: Applied</em> 2019, "
                         "11:57) uses a Bayesian hierarchical model on seven microcredit RCTs and "
                         "finds that most of the sites' effects are consistent with a common small "
                         "average, with the heterogeneity concentrated in the upper tail of "
                         "business outcomes."},
                        {"t": "hbox", "color": "green", "html": "Heterogeneity is often the "
                         "finding. Reporting that a programme works in NGO pilots and not at "
                         "government scale is more useful than one averaged number."}]},
         ]},

        {"type": "content", "label": "Dependence", "title": "Many effect sizes from one study",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "An economics paper reports six outcomes at two "
                        "follow-ups from one sample. Treating the twelve estimates as twelve "
                        "independent studies gives that paper twelve votes and shrinks the "
                        "confidence interval falsely. Ignoring all but one throws away evidence. "
                        "Neither is acceptable in a review that will be read by methodologists."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Pick one effect per study per outcome domain by a rule written in the protocol (the primary outcome, the longest follow-up), and report the rule.",
                           "Or average the effects within a study, with a variance that accounts for their correlation (Borenstein et al. 2009, chapter 24).",
                           "Or use robust variance estimation, which allows every effect in and corrects the standard errors for clustering within studies (Hedges, Tipton and Johnson, <em>Research Synthesis Methods</em> 2010, 1:39). Implemented in <em>robumeta</em> and <em>clubSandwich</em> in R."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The economics convention", "html":
                         "Meta-regression studies in economics routinely take every estimate from "
                         "every paper, hundreds or thousands of them, and cluster standard errors "
                         "by study. That is a form of robust variance estimation and is fine when "
                         "the point is to model what drives estimates. It is not fine when the "
                         "point is one pooled effect and half the estimates come from three "
                         "papers. Say which purpose the analysis serves."},
                        {"t": "hbox", "color": "cyan", "html": "Whatever the choice, state the "
                         "number of studies and the number of effect sizes separately, everywhere "
                         "a k appears."}]},
         ]},

        {"type": "content", "label": "Sensitivity", "title": "Sensitivity analyses: showing the result is not an artefact of one decision",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Decision", "Alternative to test", "Report as"],
              "rows": [
                  ["Random vs fixed effect", "The other model", "Both estimates, one sentence on the difference"],
                  ["Inclusion of high-risk studies", "Restrict to low risk", "Pooled effect with and without; the difference is a finding"],
                  ["Imputed SDs or ICCs", "Exclude imputed studies; halve and double the ICC", "Range of pooled estimates"],
                  ["One influential study", "Leave-one-out: re-run k times dropping each study", "Plot of k estimates; name any study whose removal changes the conclusion"],
                  ["Effect measure", "RR instead of OR; MD instead of SMD where possible", "Direction and significance under each"],
                  ["Outliers", "Exclude studies whose CI does not overlap the pooled CI", "With and without, plus a reason the outlier differs"],
                  ["Publication bias", "Trim-and-fill; PET-PEESE; selection model", "Adjusted estimate labelled as a sensitivity result"]]},
             {"t": "body", "cls": "sm", "html": "Pre-specify the list and run all of it, "
              "including the ones that turn out inconvenient. A sensitivity analysis that is "
              "only reported when it supports the main result is the selective reporting the "
              "review exists to detect in others."},
         ]},

        {"type": "content", "label": "Software", "title": "Tools for meta-analysis, free ones first",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Best for", "Limits"],
              "rows": [
                  ["R: <em>metafor</em>", "Free", "Everything: all models, meta-regression, RVE, plots; the reference implementation (Viechtbauer, <em>J Stat Softw</em> 2010, 36(3))", "Code, not menus; a learning curve of a few days"],
                  ["R: <em>meta</em>", "Free", "Quick pooled analyses and publication-quality forest plots with one function call", "Fewer model options than metafor"],
                  ["RevMan Web", "Free", "Cochrane-format reviews, risk-of-bias tables, summary-of-findings tables", "Limited models; no meta-regression"],
                  ["Jamovi with the MAJOR module", "Free", "Point-and-click meta-analysis for a first course; metafor underneath", "Fewer diagnostics; export is limited"],
                  ["JASP", "Free", "Classical and Bayesian meta-analysis with menus", "Newer, fewer worked examples online"],
                  ["Stata <em>meta</em> suite", "Licence", "Economists already in Stata; meta-regression, funnel tests, forest plots", "Cost; RVE needs the user-written <em>robumeta</em>"],
                  ["Comprehensive Meta-Analysis", "Licence", "Effect-size conversion from almost any reported statistic", "Cost; closed"]]},
             {"t": "body", "cls": "sm", "html": "For a South Asian team the choice is R or "
              "Jamovi. Both run on an old laptop offline, both are free, and a Jamovi analysis can "
              "be reproduced in R when a reviewer asks. Keep the extraction sheet and the script "
              "in a public repository so the review is reproducible by anyone."},
         ]},

        # ===================== SECTION 08: SYNTHESIS WITHOUT META-ANALYSIS =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Synthesis Without Meta-Analysis"},

        {"type": "content", "label": "When Not to Pool", "title": "Most development reviews cannot meta-analyse everything, and should not try",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Outcomes measured on incompatible scales, designs "
                        "too different to weight against each other, statistics that cannot be "
                        "turned into effect sizes, or three studies where one is a different "
                        "programme under the same name: any of these means the evidence has to be "
                        "synthesised in words and structured tables. That is a method, with its "
                        "own reporting standard, not a fallback for reviews that failed."},
                       {"t": "term", "word": "SWiM",
                        "def": "Synthesis Without Meta-analysis: a nine-item reporting guideline "
                        "(Campbell and colleagues, <em>BMJ</em> 2020, 368:l6890) covering how "
                        "studies were grouped, the standardised metric used, the synthesis "
                        "method, how heterogeneity was investigated, how certainty was assessed, "
                        "and how the data were presented."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Group studies by a logic stated in advance: intervention type, outcome domain, population. Tables per group.",
                  "Where effect sizes exist but cannot be pooled, still standardise them and tabulate with confidence intervals, so a reader can see the direction and size.",
                  "Where they do not exist, record direction of effect and whether the study's own test was significant, separately.",
                  "Never write 'most studies found a positive effect' without saying how many, out of how many, and at what risk of bias."]},
                        {"t": "hbox", "color": "amber", "html": "The failure mode is the narrative "
                         "review in disguise: a paragraph per study, then a conclusion the "
                         "paragraphs do not support."}]},
         ]},

        {"type": "content", "label": "Vote Counting", "title": "Counting directions, not p-values",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Counting how many studies were 'significant' is the "
                        "wrong count. A programme with a true small effect tested in ten "
                        "underpowered studies will produce two significant results and eight "
                        "'no effect' findings, and the count will say it does not work. Counting "
                        "the <em>direction</em> of effect, regardless of significance, is a "
                        "legitimate method (Cochrane Handbook chapter 12) and comes with a sign "
                        "test: under no effect, directions split 50:50."},
                       {"t": "stats", "cols": 2, "cards": [
                           {"num": "9 of 10", "label": "studies with a positive direction: sign test p = 0.02", "color": "green", "source": "Binomial, two-sided"},
                           {"num": "6 of 10", "label": "positive: p = 0.75, consistent with no effect", "color": "amber", "source": "Same test"}]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Ways to show it", "html":
                         "<strong>Harvest plot</strong> (Ogilvie and colleagues, <em>BMC Med Res "
                         "Methodol</em> 2008, 8:8): one bar per study, placed by direction, bar "
                         "height by quality, shading by design. <strong>Effect direction plot</strong>: "
                         "a table of arrows per outcome per study, sized by sample. "
                         "<strong>Albatross plot</strong>: p-values against sample size, with "
                         "contours for effect sizes, useful when only p and n are reported. All "
                         "three are drawable in R or by hand in a spreadsheet."},
                        {"t": "hbox", "color": "green", "html": "Direction counting tells you "
                         "whether there is an effect. It says nothing about how big. Say that "
                         "in the results."}]},
         ]},

        {"type": "content", "label": "Qualitative Synthesis", "title": "Synthesising qualitative evidence",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "What it does", "Source", "Use when"],
              "rows": [
                  ["Thematic synthesis", "Codes findings line by line, builds descriptive themes, then analytical themes that go beyond the studies", "Thomas and Harden 2008, <em>BMC Med Res Methodol</em> 8:45", "The question is about experience, acceptability, barriers"],
                  ["Framework synthesis", "Starts from an a priori framework (a theory of change, a policy's own logic) and codes into it, adding themes that do not fit", "Carroll et al. 2011; Booth and Carroll 2015", "A commissioner has a framework and wants evidence mapped to it"],
                  ["Meta-ethnography", "Translates concepts across studies (reciprocal, refutational), then a line of argument", "Noblit and Hare 1988; eMERGe reporting guidance 2019", "Interpretive depth on a small set of rich studies"],
                  ["Realist synthesis", "Asks what works for whom in what circumstances; builds context-mechanism-outcome configurations", "Pawson et al. 2005; RAMESES standards, Wong et al. 2013, <em>BMC Medicine</em> 11:21", "Complex interventions whose effect depends on how people respond"],
                  ["Meta-aggregation", "Pools findings into categories and synthesised statements with recommendations", "JBI", "Practice guidance in health"]]},
             {"t": "body", "cls": "sm", "html": "Report to ENTREQ (Tong and colleagues, <em>BMC Med "
              "Res Methodol</em> 2012, 12:181) and assess confidence in each finding with "
              "GRADE-CERQual (Lewin and colleagues, <em>PLoS Medicine</em> 2015, 12:e1001895), "
              "which asks about methodological limitations, coherence, adequacy of data and "
              "relevance. A finding supported by two thin studies from one district is 'low "
              "confidence' however vivid the quotes."},
         ]},

        {"type": "content", "label": "Realist Reviews", "title": "Context, mechanism, outcome: the realist question",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A cash transfer conditional on school attendance "
                        "raises enrolment in one state and not in another. A conventional review "
                        "averages the two. A realist review asks what the money did in each place: "
                        "in one, it covered the cost of a uniform the school required; in the "
                        "other, the school was 8 km away and no transfer changes that. The "
                        "mechanism (relieving a cash constraint) fires only in a context where "
                        "cash was the constraint."},
                       {"t": "flow", "steps": [
                           "Elicit candidate programme theories from documents and stakeholders",
                           "Search purposively, including grey literature and process evaluations, for evidence on each theory",
                           "Extract context-mechanism-outcome configurations, not effect sizes",
                           "Refine the theory; report what works for whom, where, and why"]}],
              "right": [{"t": "panel", "color": "amber", "title": "What a realist review is not", "html":
                         "It is not an excuse to skip systematic searching or appraisal; RAMESES "
                         "(Wong and colleagues 2013) sets 19 reporting items. It does not produce "
                         "an effect size and should not be commissioned by someone who wants one. "
                         "It is also easy to do badly: 'mechanism' gets used for any intermediate "
                         "step, and the configurations become a list of things that happened. A "
                         "mechanism is a change in the reasoning or resources of the people the "
                         "programme reaches."},
                        {"t": "hbox", "color": "cyan", "html": "Realist and statistical synthesis "
                         "are complementary. The meta-analysis says the average is 0.1 SD with "
                         "high heterogeneity; the realist review says where the 0.3 came from."}]},
         ]},

        {"type": "content", "label": "Mixed Methods", "title": "Combining quantitative and qualitative streams",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Segregated</strong>: run a quantitative synthesis and a qualitative one separately, then bring them together in a matrix. Simplest and most common.",
                  "<strong>Sequential</strong>: the qualitative synthesis generates hypotheses (which components matter, which barriers) that the quantitative synthesis then tests as subgroups. The EPPI-Centre's approach.",
                  "<strong>Integrated</strong>: convert findings to one form (usually qualitative) and synthesise together. Rare, and hard to do transparently.",
                  "Whatever the design, keep the two appraisals separate: risk of bias for effect studies, CASP or similar for qualitative ones."]}],
              "right": [{"t": "panel", "color": "green", "title": "The matrix", "html":
                         "Rows are the intervention components or barriers found in the "
                         "qualitative stream; columns are the trials. A cell records whether "
                         "the trial's intervention had that component and what effect it found. "
                         "Reading across, you see whether trials that addressed the barriers "
                         "people named did better. It is descriptive, it is honest about being "
                         "descriptive, and it is often the most useful table in the review."},
                        {"t": "hbox", "color": "amber", "html": "Mixed-methods reviews take longer "
                         "than either stream alone and need two skill sets on the team. Budget "
                         "both."}]},
         ]},

        {"type": "content", "label": "Scoping and Mapping", "title": "Scoping reviews and evidence gap maps",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A scoping review asks what evidence exists, of what "
                        "kind, on what, and where the gaps are. It does not appraise risk of bias "
                        "and does not synthesise effects. Arksey and O'Malley (<em>International "
                        "Journal of Social Research Methodology</em> 2005, 8:19) set the "
                        "framework; PRISMA-ScR (Tricco and colleagues, <em>Annals of Internal "
                        "Medicine</em> 2018, 169:467) is the reporting standard. Use one before a "
                        "systematic review, to decide whether one is feasible, or instead of one "
                        "when the question is about the shape of a literature."},
                       {"t": "bullets", "color": "amber", "items": [
                           "A scoping review is not a quick systematic review. The search is as rigorous; what is dropped is appraisal and synthesis.",
                           "Charting replaces extraction: a table of study characteristics, not results.",
                           "The output is a map and a gap list, and both should be specific enough to commission from."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Evidence gap maps", "html":
                         "3ie's format (Snilstveit and colleagues, <em>J Clin Epidemiol</em> "
                         "2016, 79:120): a grid with interventions as rows and outcomes as "
                         "columns, each cell holding the studies and reviews found, coloured by "
                         "confidence. Blank cells are the map's point. 3ie's maps on social "
                         "protection, WASH and agriculture are open at developmentevidence.3ieimpact.org "
                         "and are the first place to look before proposing a review on any of "
                         "those topics."},
                        {"t": "hbox", "color": "green", "html": "A gap map takes weeks, not months, "
                         "and a funder can read it in ten minutes. It is the most cost-effective "
                         "synthesis product for a South Asian research team to offer."}]},
         ]},

        {"type": "content", "label": "Divergent Reviews", "title": "When six reviews of the same question disagree",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Evans and Popova (<em>World Bank Research "
                        "Observer</em> 2016, 31:242) compared six systematic reviews of what "
                        "improves learning in developing countries. The reviews reached different "
                        "conclusions, and the reason was not the analysis: of 227 studies "
                        "across the six, only three appeared in all six reviews. Different "
                        "inclusion rules, different classifications of interventions and "
                        "different dates produced different evidence bases under one question."},
                       {"t": "stats", "cols": 2, "cards": [
                           {"num": "227", "label": "distinct studies across six reviews of learning outcomes", "color": "cyan", "source": "Evans and Popova 2016"},
                           {"num": "3", "label": "studies included in all six", "color": "red", "source": "Same paper"}]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Before starting, read the existing reviews on your question and tabulate their inclusion criteria against yours. If yours will differ, say why and what that changes.",
                  "Classify interventions by a published taxonomy where one exists, so your categories can be compared with others'.",
                  "An overview of reviews (an umbrella review) is a recognised design for exactly this situation: appraise the reviews with AMSTAR 2 (Shea et al. 2017, <em>BMJ</em> 358:j4008) and explain the divergence.",
                  "Evans and Popova found that once categories were harmonised, the reviews agreed on more than they appeared to: pedagogy-focused interventions and individualised instruction came out consistently."]}]},
         ]},

        # ===================== SECTION 09: GRADE AND REPORTING =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "GRADE and Reporting"},

        {"type": "content", "label": "Certainty", "title": "GRADE: how sure are we, outcome by outcome",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A pooled estimate is a number; GRADE is the "
                        "judgement about how much to trust it. The Grading of Recommendations "
                        "Assessment, Development and Evaluation approach (Guyatt and colleagues, "
                        "<em>BMJ</em> 2008, 336:924) rates the certainty of evidence for each "
                        "outcome as high, moderate, low or very low. It is now the standard in "
                        "Cochrane, Campbell, WHO guidelines and 3ie reviews, and journals "
                        "increasingly expect it."},
                       {"t": "term", "word": "Certainty of evidence",
                        "def": "The extent to which we are confident that the estimate of effect "
                        "is close to the true effect, for a specific outcome. It is a property of "
                        "the body of evidence, not of any one study, and it can differ between "
                        "outcomes in the same review."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Randomised trials start at high; observational and quasi-experimental studies start at low.",
                  "Downgrade one or two levels for each of five reasons: risk of bias, inconsistency, indirectness, imprecision, publication bias.",
                  "Upgrade observational evidence for a large effect, a dose-response gradient, or when plausible confounding would reduce the observed effect.",
                  "The result is a sentence a minister can read: 'Cash transfers probably increase school enrolment (moderate certainty).'"]},
                        {"t": "hbox", "color": "amber", "html": "Two assessors, a written reason for "
                         "every downgrade, and the same rules applied to outcomes you like and "
                         "outcomes you do not."}]},
         ]},

        {"type": "content", "label": "The Five Domains", "title": "Deciding when to downgrade",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Domain", "Downgrade when", "A development example"],
              "rows": [
                  ["Risk of bias", "Most of the weight comes from studies at high risk or with some concerns, and a sensitivity analysis moves the estimate", "Three of five trials unregistered with outcomes chosen after the fact"],
                  ["Inconsistency", "Effects point in different directions, intervals barely overlap, I&sup2; is high and subgroups do not explain it", "Enrolment effects of 0.02 and 0.25 across states with no moderator found"],
                  ["Indirectness", "The studies' population, intervention, comparator or outcome differ from the review question", "Question is about Bangladesh; evidence is from Mexico and Brazil; outcome is attendance, not learning"],
                  ["Imprecision", "The confidence interval includes both a worthwhile benefit and no effect (or harm); total sample below the optimal information size", "Pooled RR 1.15 (0.92 to 1.44) from 600 households"],
                  ["Publication bias", "Small-study effects, or many registered trials with no results, or a field where nulls are known not to be published", "Funnel asymmetry across 14 microenterprise studies; 6 registered trials unreported"]]},
             {"t": "body", "cls": "sm", "html": "Each domain can cost one level (serious) or two "
              "(very serious). Randomised evidence with two serious problems is 'low'; "
              "observational evidence with one is 'very low'. Balshem and colleagues (<em>J "
              "Clin Epidemiol</em> 2011, 64:401) give the definitions; GRADEpro GDT, free for "
              "non-commercial use, walks through the judgements and produces the table."},
         ]},

        {"type": "content", "label": "Summary of Findings", "title": "The summary-of-findings table: one page that carries the review",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Outcome", "Studies (participants)", "Relative effect (95% CI)", "Absolute effect", "Certainty", "Comment"],
                        "rows": [
                            ["School enrolment, 1 year", "7 RCTs (41,200 children)", "RR 1.08 (1.04 to 1.12)", "6 more per 100 enrolled (3 to 9 more), from 75 per 100", "Moderate", "Downgraded for inconsistency"],
                            ["Test scores, 2 years", "4 RCTs (18,500)", "SMD 0.04 (&minus;0.03 to 0.11)", "Roughly 1 percentile point", "Low", "Downgraded for imprecision and indirectness"],
                            ["Child labour", "3 RCTs, 2 quasi (9,800)", "RR 0.91 (0.80 to 1.03)", "4 fewer per 100 (9 fewer to 1 more)", "Low", "Downgraded for risk of bias, imprecision"],
                            ["Household consumption", "9 studies (52,000)", "MD +7% (4 to 10)", "About Rs 420 per month at the baseline mean", "High", "Consistent, precise, direct"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative table for a cash-transfer "
                        "review. Absolute effects are computed at a stated baseline risk, because "
                        "'RR 1.08' means something different at 20% enrolment and at 95%."}],
              "right": [{"t": "panel", "color": "green", "title": "Why it comes first", "html":
                         "Most readers of a review read the abstract and this table. It should "
                         "hold the seven or so outcomes that matter to a decision, stated in "
                         "absolute terms, with the certainty rating beside each. Cochrane puts it "
                         "before the introduction. Campbell and 3ie reviews carry it in the "
                         "plain-language summary."},
                        {"t": "hbox", "color": "cyan", "html": "If your review has no summary-of-findings "
                         "table, a policymaker has to build one from your results section. They "
                         "will not."}]},
         ]},

        {"type": "content", "label": "PRISMA 2020", "title": "Reporting to PRISMA 2020: the 27 items",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Section", "Items", "What reviewers check"],
                        "rows": [
                            ["Title, abstract", "1&ndash;2", "'Systematic review' in the title; the 12-item abstract checklist"],
                            ["Introduction", "3&ndash;4", "Rationale and explicit objectives"],
                            ["Methods", "5&ndash;15", "Eligibility, sources, full search strategy, selection and extraction processes, risk of bias, effect measures, synthesis methods, certainty"],
                            ["Results", "16&ndash;22", "Flow diagram, study characteristics, risk of bias per study, individual and synthesised results, certainty"],
                            ["Discussion", "23", "Interpretation, limitations of evidence and of the review, implications"],
                            ["Other", "24&ndash;27", "Registration and protocol, support, competing interests, availability of data and code"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Page and colleagues, <em>BMJ</em> 2021, "
                        "372:n71, with the explanation and elaboration paper at 372:n160. The "
                        "checklist is a table of where each item appears in your manuscript; "
                        "most journals require it as a supplement. Filling it in honestly is the "
                        "quickest audit of a draft: an item with no page number is a gap."},
                        {"t": "bullets", "color": "amber", "sm": True, "items": [
                            "Item 7 wants the full search strategy for every database, verbatim, as run. An appendix, not a paraphrase.",
                            "Item 27 asks where the extraction sheet and analysis code live. A public repository answers it.",
                            "Extensions: PRISMA-S for searches, PRISMA-ScR for scoping reviews, PRISMA-P for protocols; MOOSE (Stroup et al. 2000, <em>JAMA</em> 283:2008) for observational syntheses."]}]},
         ]},

        {"type": "content", "label": "Writing the Discussion", "title": "The discussion: what the evidence supports, and for whom",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "MAIN FINDINGS: each primary outcome, effect and certainty, in one paragraph",
                  "EVIDENCE LIMITS: bias, inconsistency, gaps, what was not studied",
                  "REVIEW LIMITS: what your search, criteria and resources could not do",
                  "APPLICABILITY: to your setting, with the reasons an effect might transfer or not",
                  "IMPLICATIONS: for policy, hedged to the certainty; for research, specific enough to fund"]},
                       {"t": "body", "html": "Keep the two kinds of limitation apart. 'The trials "
                        "were short' is a limit of the evidence; 'we searched only English-language "
                        "databases' is a limit of the review. Conflating them lets the review's "
                        "shortcuts hide behind the literature's."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Applicability to South Asia", "html":
                         "Most systematic reviews in development pool evidence from three "
                         "continents. A review written for a Bihar or Sindh audience should say "
                         "which studies came from comparable settings, whether the effect differed "
                         "there, and what in the implementation context (front-line worker "
                         "density, banking access, school distance) would change the mechanism. "
                         "Vivalt's 2020 finding that effects are hard to predict across sites is "
                         "the reason this paragraph exists."},
                        {"t": "hbox", "color": "amber", "html": "'More research is needed' is not an "
                         "implication. 'A trial of X in a government delivery system with a "
                         "two-year follow-up on learning outcomes' is."}]},
         ]},

        {"type": "content", "label": "Publishing", "title": "Where reviews are published, and what each outlet expects",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Outlet", "Scope", "Expectations"],
              "rows": [
                  ["Campbell Systematic Reviews", "Social welfare, education, crime, international development, methods; open access, no fee", "Registered title and protocol first; full Campbell and GRADE standards; editorial and methods review before acceptance"],
                  ["Cochrane Database of Systematic Reviews", "Health, including nutrition, WASH, maternal and child health", "Cochrane review group registration; RevMan format; MECIR conduct and reporting standards"],
                  ["3ie systematic review series", "Development effectiveness; commissioned and open access", "3ie protocol approval; quasi-experimental risk-of-bias tool; evidence gap map alongside"],
                  ["Journal of Development Effectiveness", "Impact evaluation and synthesis in development", "PRISMA; interest in methods and policy relevance"],
                  ["World Development, Journal of Development Economics", "General development; reviews accepted selectively", "Contribution beyond summary; meta-regression rather than description"],
                  ["Systematic Reviews (BMC), Research Synthesis Methods", "Protocols, methods, reviews across fields", "Open access with article fee; waivers for low- and middle-income authors"],
                  ["Indian outlets: EPW, Indian Journal of Medical Research, IJCM", "Policy audiences and health; systematic reviews accepted", "Shorter formats; PRISMA still expected; check the journal's indexing before submission"]]},
             {"t": "body", "cls": "sm", "html": "Publish the protocol first, wherever the review "
              "is going. A registered protocol is what separates a systematic review from a "
              "literature review with a flow diagram."},
         ]},

        {"type": "content", "label": "Updating", "title": "Reviews go stale: updating and living reviews",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Shojania and colleagues (<em>Annals of Internal "
                        "Medicine</em> 2007, 147:224) estimated that the median systematic review "
                        "needs updating within about five and a half years, and a quarter within "
                        "two. Development literatures move faster where a topic is fashionable "
                        "with funders. A review should state its search date on the first page "
                        "and say when it plans to be updated."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Keep the search strategy, extraction sheet and code so an update re-runs the search from the last date rather than starting again.",
                           "An update is a new review with the old studies pre-extracted: same protocol, same appraisal, new records screened.",
                           "Say what changed. 'Two new trials, both at low risk, moved the estimate from 0.08 to 0.11' is the finding of an update."]}],
              "right": [{"t": "panel", "color": "green", "title": "Living systematic reviews", "html":
                         "A living review (Elliott and colleagues, <em>J Clin Epidemiol</em> 2017, "
                         "91:23) re-runs the search monthly or quarterly and incorporates new "
                         "studies as they appear, with the current version always published. It "
                         "needs saved searches with alerts, a screening team on retainer and a "
                         "publication format that can be versioned. Cochrane ran several during "
                         "COVID-19; in development, 3ie's gap maps are updated on a schedule and "
                         "are the closest equivalent."},
                        {"t": "hbox", "color": "amber", "html": "Do not promise a living review "
                         "without a budget line for it. An unfunded living review is a stale one "
                         "with a misleading label."}]},
         ]},

        # ===================== SECTION 10: BIBLIOMETRIC ANALYSIS =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Bibliometric Analysis"},

        {"type": "content", "label": "A Different Question", "title": "Bibliometrics asks what a field has done, not what the evidence says",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Bibliometric analysis",
                        "def": "The quantitative study of publications and their citation and "
                        "authorship links: how much a field publishes, who publishes it, which "
                        "works and journals it builds on, how its topics cluster and move over "
                        "time."},
                       {"t": "body", "html": "A systematic review reads 40 studies closely. A "
                        "bibliometric analysis counts 4,000 and reads none of them; it maps "
                        "structure, not findings. The two answer different questions and are "
                        "often confused in South Asian journals, where 'bibliometric review' can "
                        "mean a citation count dressed as a literature review. Donthu and "
                        "colleagues (<em>Journal of Business Research</em> 2021, 133:285) set out "
                        "when each is appropriate."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Use it when the literature is too large to read, when the question is about the field itself (who, where, what topics, what trends), or to scope a systematic review's boundaries.",
                  "Do not use it to claim a programme works. Citation counts measure attention, and attention is not evidence.",
                  "Its inputs are database exports; its outputs are tables of counts and network maps. Everything depends on the database's coverage, which is the first limitation to state."]},
                        {"t": "hbox", "color": "amber", "html": "'The most cited paper on X' is a "
                         "fact about citation, and a useful one. It is not a fact about X."}]},
         ]},

        {"type": "content", "label": "Techniques", "title": "The two families: performance analysis and science mapping",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Technique", "Unit", "Question", "Output"],
              "rows": [
                  ["Publication and citation counts", "Authors, institutions, countries, journals, years", "Who produces the field, and where is it published?", "Ranked tables; annual output curve"],
                  ["Citation analysis", "Documents", "Which works are the field's foundations?", "Most-cited list, citation half-life"],
                  ["Co-citation", "Pairs of documents cited together", "What is the intellectual structure? Documents co-cited often belong to one school", "Clusters of foundational works (Small 1973)"],
                  ["Bibliographic coupling", "Pairs of documents sharing references", "What is the current research front? Papers citing the same sources work on the same problem", "Clusters of recent papers (Kessler 1963)"],
                  ["Co-authorship", "Authors, institutions, countries", "Who collaborates with whom; where are the isolated groups?", "Collaboration network"],
                  ["Co-word (keyword co-occurrence)", "Keywords or title terms", "What are the topics and how do they connect and shift over time?", "Thematic map; overlay by year"]]},
             {"t": "body", "cls": "sm", "html": "The first two are performance analysis: counting. "
              "The last four are science mapping: networks. A competent bibliometric paper "
              "does at least one of each, states the database and date, and interprets the "
              "clusters by reading the papers at their centres. A map with unlabelled clusters "
              "is a picture."},
         ]},

        {"type": "content", "label": "Data Sources", "title": "Where the records come from, and who each source leaves out",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "Access", "Coverage", "Export"],
              "rows": [
                  ["Scopus (Elsevier)", "Subscription; many Indian universities via consortia", "Over 27,000 active titles; curated; weaker on regional and non-English journals", "CSV, RIS, BibTeX with references; 2,000 records at a time"],
                  ["Web of Science (Clarivate)", "Subscription", "Narrower and older; the source of the Journal Impact Factor", "Tab-delimited with cited references; 500 or 1,000 at a time"],
                  ["OpenAlex", "Free, open API and web interface; launched 2022 as the successor to Microsoft Academic Graph", "Broadest: over 250 million works, but with noisier metadata", "CSV, JSON via API; no limit in practice"],
                  ["Dimensions", "Free basic search; paid for full", "Wide, includes grants and policy documents", "Limited in the free tier"],
                  ["Lens.org", "Free for individuals", "Scholarly works plus patents; good for applied fields", "CSV, RIS"],
                  ["Google Scholar", "Free", "Widest, including theses and reports; no quality control", "No export; Publish or Perish scrapes it in small batches"],
                  ["Shodhganga (INFLIBNET)", "Free", "Indian theses in full text", "No structured export; useful as a source, not a dataset"]]},
             {"t": "body", "cls": "sm", "html": "Mongeon and Paul-Hus (<em>Scientometrics</em> "
              "2016, 106:213) show that Scopus and Web of Science under-represent the social "
              "sciences, humanities and non-English publishing. A bibliometric study of "
              "development research in South Asia run on Web of Science alone will "
              "systematically miss Indian, Bangladeshi and Nepali journals, and should say so."},
         ]},

        {"type": "content", "label": "Workflow", "title": "From query to map: the steps, and where time goes",
         "blocks": [
             {"t": "flow", "steps": [
                 "DEFINE: field boundaries as a search string, with the same rigour as a review search",
                 "EXPORT: full records with references and keywords from one or more databases",
                 "CLEAN: merge duplicates, disambiguate author names, harmonise keywords and institutions",
                 "ANALYSE: counts, trends, top lists; then networks",
                 "MAP: clusters, overlays by year, density",
                 "INTERPRET: read the central papers of each cluster and name what it is about"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Cleaning takes half the time. 'A. Banerjee', "
                        "'Banerjee, Abhijit' and 'Banerjee AV' are one author; 'Jawaharlal Nehru "
                        "University' appears under a dozen spellings; 'cash transfer', 'cash "
                        "transfers' and 'CCT' are one keyword. Every count and every map depends "
                        "on those merges, and none of the tools does them well automatically. "
                        "Keep a thesaurus file and cite it."}],
              "right": [{"t": "hbox", "color": "cyan", "html": "Report the query, the database, the "
                        "date, the record count at each cleaning step, and the thesaurus. A "
                        "bibliometric analysis that cannot be re-run is an opinion with a "
                        "network diagram."}]},
         ]},

        {"type": "content", "label": "Tools", "title": "Software: VOSviewer, Bibliometrix, and the rest",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Strength", "Limit"],
              "rows": [
                  ["VOSviewer", "Free (Leiden); van Eck and Waltman, <em>Scientometrics</em> 2010, 84:523", "Network maps: co-authorship, co-citation, coupling, co-word; overlay and density views; reads Scopus, WoS, OpenAlex, Lens", "Maps only; counts and trends need another tool; thesaurus by text file"],
                  ["Bibliometrix and biblioshiny (R)", "Free; Aria and Cuccurullo, <em>Journal of Informetrics</em> 2017, 11:959", "Full workflow in one package: import, descriptives, laws, networks, thematic maps, a point-and-click interface", "R installation; large networks are slow in the browser interface"],
                  ["CiteSpace", "Free for academic use; Chen, <em>JASIST</em> 2006, 57:359", "Bursts and turning points over time; timeline views", "Java, dated interface; WoS-centred"],
                  ["Publish or Perish (Harzing)", "Free", "Author and journal metrics from Google Scholar, Scopus, OpenAlex, Crossref", "Small batches; no networks"],
                  ["Gephi", "Free", "Any network, with full layout and statistics control", "You build the network file yourself"],
                  ["Python: pyalex, pybibx", "Free", "Scripted pulls from OpenAlex; reproducible pipelines", "Code required"]]},
             {"t": "body", "cls": "sm", "html": "For a first project: export from Scopus or OpenAlex, "
              "run descriptives in biblioshiny, draw the maps in VOSviewer. Both run offline on "
              "a modest laptop. Save the VOSviewer map and network files alongside the export so "
              "a reader can reopen exactly the figure in the paper."},
         ]},

        {"type": "content", "label": "Reading a Map", "title": "Reading a VOSviewer map without over-reading it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Node size</strong> is the item's weight: number of documents, or citations, as you chose. <strong>Distance</strong> approximates relatedness; two nodes close together are linked often. <strong>Colour</strong> is the cluster the algorithm assigned.",
                  "<strong>Overlay view</strong> colours nodes by average publication year, which shows where the field has moved: blue for older topics, yellow for recent.",
                  "<strong>Density view</strong> shows where the mass of the field sits; sparse regions are either gaps or artefacts of the query.",
                  "The <strong>resolution</strong> parameter sets how many clusters appear. Change it and the picture changes. Report the value."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What the picture does not show", "html":
                         "Clusters are statistical, not conceptual, until you name them by reading "
                         "their central papers. Distances in a two-dimensional layout are "
                         "approximations of a high-dimensional network and can mislead at the "
                         "edges. A node's size records citations, so an older paper is always "
                         "bigger than a better recent one. And nothing on the map tells you "
                         "whether any of the papers is sound."},
                        {"t": "hbox", "color": "green", "html": "Label the clusters in the caption "
                         "with two or three of their central works, and say how you decided the "
                         "label. That is the analysis; the map is the evidence for it."}]},
         ]},

        {"type": "content", "label": "Indicators", "title": "Citation indicators and their misuse",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Indicator", "Definition", "Use", "Misuse"],
              "rows": [
                  ["h-index", "h papers with at least h citations each (Hirsch, <em>PNAS</em> 2005, 102:16569)", "A rough summary of an author's output and uptake", "Comparing across fields or career stages; it only rises, and it rewards volume"],
                  ["Journal Impact Factor", "Citations in year t to items from t&minus;1 and t&minus;2, divided by citable items", "Comparing journals within one field", "Judging an article or an author by its journal; skewed by a few highly cited papers"],
                  ["CiteScore (Scopus)", "Four-year window, all document types", "As above, wider coverage", "As above"],
                  ["Field-weighted citation impact", "Citations relative to the world average for the same field, year and document type", "Cross-field comparison at institutional scale", "Small numbers; a single paper's FWCI is noise"],
                  ["Altmetrics", "Mentions in policy documents, news, social media", "Tracing policy uptake of development research", "Treating attention as quality"]]},
             {"t": "body", "cls": "sm", "html": "The Leiden Manifesto (Hicks and colleagues, "
              "<em>Nature</em> 2015, 520:429) gives ten principles, the first of which is that "
              "quantitative evaluation should support, not replace, expert judgement, and DORA "
              "(2012) asks institutions to stop using journal metrics to assess individuals. "
              "Both matter in India, where promotion rules have at times scored publications by "
              "journal lists and impact factors, and where that scoring fed the market for "
              "predatory journals."},
         ]},

        {"type": "content", "label": "Laws and Curves", "title": "The regularities every bibliometric paper reports",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Lotka's law</strong>: the number of authors producing n papers falls roughly as 1/n&sup2;. Most authors in any field publish once; a few publish most of it.",
                  "<strong>Bradford's law</strong>: a core of a few journals holds a third of the papers on a topic, a second larger zone holds another third, and a long tail holds the rest.",
                  "<strong>Price's law</strong> and exponential growth: literatures tend to double over fixed periods until they saturate. The annual output curve is the first figure in most papers.",
                  "<strong>Citation ageing</strong>: the half-life of citations, which varies by field; economics cites older work than computer science."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What they are for", "html":
                         "Bradford's core journals tell a systematic reviewer where to hand-search. "
                         "Lotka's distribution tells a funder that a field with 400 authors has "
                         "perhaps 20 sustained researchers. The growth curve tells everyone "
                         "whether a topic is emerging, mature or declining. Reporting the laws "
                         "without saying what follows from them is a common way to fill a "
                         "bibliometric paper with numbers that change nothing."},
                        {"t": "hbox", "color": "cyan", "html": "Biblioshiny computes all of them in "
                         "one click. The judgement is in the sentence after the number."}]},
         ]},

        {"type": "content", "label": "Worked Example", "title": "A bibliometric study of cash-transfer research, step by step",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "Decision", "Illustrative result"],
                        "rows": [
                            ["Query", "TITLE-ABS-KEY(\"cash transfer*\" AND (poverty OR welfare OR \"social protection\")), 2000&ndash;2025, articles and reviews", "3,140 Scopus records"],
                            ["Clean", "Merge 212 author variants, 96 institution variants, keyword thesaurus of 140 lines", "3,088 records after de-duplication"],
                            ["Output", "Annual curve", "Under 20 a year to 2005; about 300 a year by 2022"],
                            ["Producers", "Countries by corresponding author", "USA, UK, then Brazil, Mexico, South Africa; India seventh, Bangladesh and Pakistan in the top twenty"],
                            ["Journals", "Bradford core", "<em>World Development</em>, <em>Journal of Development Effectiveness</em>, <em>Social Science &amp; Medicine</em>, <em>Journal of Development Economics</em>"],
                            ["Co-citation", "Documents, minimum 20 citations", "Clusters around Progresa evaluations, unconditional-transfer trials, and health and nutrition outcomes"],
                            ["Co-word overlay", "Author keywords, minimum 10 occurrences", "Recent yellow: 'COVID-19', 'digital payments', 'universal basic income'; older blue: 'conditionality', 'Progresa'"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Counts here are illustrative, "
                        "constructed for teaching. The point is the shape of the writing: each "
                        "step has a decision, each decision has a number, and the interpretation "
                        "sits beside both. Note what the study cannot say: whether cash transfers "
                        "work, whether the India-based papers are good, or anything about the "
                        "hundreds of evaluations published as reports outside Scopus."},
                        {"t": "hbox", "color": "amber", "html": "Combine it with a gap map or a "
                         "systematic review and the two become useful to each other: the map "
                         "shows the field's shape, the review shows what its centre found."}]},
         ]},

        {"type": "content", "label": "South Asia", "title": "Bibliometrics of and for South Asian research",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "India is among the largest producers of science and "
                        "engineering articles by count (NSF Science &amp; Engineering Indicators "
                        "2022, as section 01 noted). A count says nothing about where the work "
                        "is published or whether anyone reads it, so a bibliometric study of the "
                        "region has to report uptake alongside output and say which database "
                        "each number came from."},
                       {"t": "bullets", "color": "amber", "items": [
                           "A bibliometric study of the region should use OpenAlex or Dimensions alongside Scopus, and say what the difference in coverage was.",
                           "Distinguish output from uptake: papers, and then citations per paper normalised by field.",
                           "Co-authorship maps show a pattern worth reporting: South Asian authors linked to North American and European institutions far more than to each other."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Predatory publishing", "html":
                         "Journal lists used in promotion rules created a market for journals "
                         "that accept anything for a fee, and bibliometric databases index some "
                         "of them. Before counting a journal, check it against DOAJ, the Scopus "
                         "source list, COPE membership and the Think Check Submit criteria; Beall's "
                         "list, though closed in 2017, remains archived and Cabells maintains a "
                         "paid successor. A bibliometric analysis that counts predatory output as "
                         "research output reports the problem as achievement."},
                        {"t": "hbox", "color": "green", "html": "The region's evaluation reports, "
                         "working papers and theses are mostly outside every index. A field map "
                         "built on Scopus alone is a map of the part that faces outward."}]},
         ]},

        {"type": "content", "label": "Writing It Up", "title": "Structure of a bibliometric paper that reviewers accept",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "QUESTION: a question about the field, stated as one that counts and maps can answer",
                  "DATA: source, query, date, cleaning, counts at each step",
                  "PERFORMANCE: output, producers, outlets, with the laws where they add something",
                  "STRUCTURE: at least one network, with clusters named from reading",
                  "SO WHAT: what the field is missing, and what a researcher or funder should do"]},
                       {"t": "body", "html": "Reviewers at <em>Scientometrics</em>, <em>Journal "
                        "of Informetrics</em> and the applied journals reject the same paper "
                        "repeatedly: a Scopus export, the default biblioshiny figures, one "
                        "paragraph per figure describing what it shows, and a conclusion that the "
                        "field is growing. The difference is the question and the reading."}],
              "right": [{"t": "panel", "color": "green", "title": "Pair it with something", "html":
                         "The most useful bibliometric work in development is a component of "
                         "something else: the scoping stage of a systematic review, the "
                         "baseline of a research-capacity evaluation, or the map behind a "
                         "funding call. Donthu and colleagues (2021) give the standalone "
                         "template; the pairing is what makes the numbers matter to anyone "
                         "outside informetrics."},
                        {"t": "hbox", "color": "amber", "html": "Do not call it a systematic "
                         "review. Do not report PRISMA for it. Do not draw conclusions about what "
                         "works from it. Reviewers check all three."}]},
         ]},

        # ===================== SECTION 11: PRACTICE, TOOLS AND PITFALLS =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice, Tools and Pitfalls"},

        {"type": "content", "label": "The Free Stack", "title": "A complete toolkit at no cost, running offline",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Stage", "Tool", "Notes"],
              "rows": [
                  ["Protocol", "PROSPERO or OSF Registries; PRISMA-P checklist", "OSF accepts any discipline; PROSPERO is health-focused and slow to register"],
                  ["Search", "PubMed, Google Scholar, OpenAlex, RePEc/IDEAS, 3ie repository, Campbell library; Scopus where the institution has it", "Save every strategy as run, with date and count"],
                  ["Reference management", "Zotero, with the Better BibTeX plugin", "Free, open; de-duplication and full-text retrieval built in"],
                  ["Screening", "Rayyan (free tier); or a shared Zotero library with tags", "Rayyan blinds screeners to each other and logs conflicts"],
                  ["Extraction", "Google Sheets or LibreOffice Calc from a piloted template; SRDR+ (AHRQ, free)", "One row per study; a 'source page' column for every number"],
                  ["Risk of bias", "RoB 2 and ROBINS-I Excel tools from riskofbias.info; robvis for figures", "Two assessors; keep the signalling-question answers"],
                  ["Analysis", "R with metafor and meta; Jamovi with MAJOR for menus", "Script and data in a public repository"],
                  ["Certainty", "GRADEpro GDT (free for non-commercial use)", "Produces the summary-of-findings table"],
                  ["Bibliometrics", "OpenAlex export, biblioshiny, VOSviewer", "All offline after export"],
                  ["Reporting", "PRISMA 2020 checklist and flow diagram generator (Haddaway et al. 2022, R package and web app)", "Fill the checklist against your own draft before submission"]]},
         ]},

        {"type": "content", "label": "Team and Timeline", "title": "Who does what, and how long it takes",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Phase", "Weeks (typical)", "People", "Output"],
                        "rows": [
                            ["Question, scoping searches, protocol", "4&ndash;8", "Lead, methodologist, subject expert, librarian", "Registered protocol"],
                            ["Search and de-duplication", "2&ndash;3", "Librarian or trained searcher", "Search log; record set"],
                            ["Title and abstract screening", "3&ndash;6", "Two screeners", "Calibrated screening; conflict log"],
                            ["Full-text screening", "3&ndash;5", "Two screeners", "Excluded-with-reasons list"],
                            ["Extraction and appraisal", "6&ndash;10", "Two extractors, two assessors", "Extraction sheet; risk-of-bias table"],
                            ["Synthesis and GRADE", "4&ndash;8", "Statistician or methodologist, lead", "Analyses; summary-of-findings table"],
                            ["Writing, PRISMA, submission", "4&ndash;6", "Lead, all authors", "Manuscript with checklist and appendices"],
                            ["Total", "26&ndash;46", "Four to six people, part time", "Consistent with Borah et al.'s median of 67 weeks elapsed"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "The roles that get skipped are the "
                        "librarian and the second screener, and those are the two that cannot be "
                        "recovered later. A subject expert who does not do methods work is still "
                        "essential at three points: the question, the interpretation of "
                        "heterogeneity, and the applicability paragraph."},
                        {"t": "hbox", "color": "amber", "html": "A rapid review compresses this to "
                         "8&ndash;12 weeks by single screening, limiting databases and dates, and "
                         "skipping meta-regression, and says so in the title and the "
                         "limitations (Garritty et al. 2021)."}]},
         ]},

        {"type": "content", "label": "AI Tools", "title": "Using AI tools in a review without disqualifying it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Language-model tools now offer to write search "
                        "strings, screen abstracts, extract data and summarise papers. Some of "
                        "that is useful. None of it removes the requirement that a named person "
                        "made each decision and that the method is reported in enough detail to "
                        "be reproduced. Treat an AI tool as a third screener whose accuracy you "
                        "have measured, never as the second screener."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Search: useful for drafting synonyms and translating a strategy between database syntaxes. Check every line; models invent field tags.",
                           "Screening: run the model on a sample the humans have already screened and report its sensitivity. Below about 95% sensitivity it is not fit to exclude anything.",
                           "Extraction: acceptable as a first pass verified against the paper, number by number; it fabricates numbers with confidence.",
                           "Writing: never for the results. A model summarising your own extraction table will smooth over the disagreements that are the point."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Discovery tools", "html":
                         "Elicit, Consensus, Semantic Scholar and similar search a corpus built "
                         "largely from open metadata, not from Scopus or Web of Science, and rank "
                         "by relevance models you cannot audit. They are good for scoping a "
                         "question and finding a seed set for citation chasing, and they are not "
                         "a database search. A review whose only search was an AI tool fails "
                         "PRISMA item 7 on its face."},
                        {"t": "hbox", "color": "green", "html": "Report it: the tool, version, "
                         "date, prompt, what it was used for, and how its output was checked. "
                         "Most publishers' policies now require that disclosure in the "
                         "methods."}]},
         ]},

        {"type": "content", "label": "Pitfalls", "title": "The twelve ways development reviews go wrong",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "What it looks like", "Prevention"],
              "rows": [
                  ["No protocol", "Criteria change as papers arrive", "Register before searching"],
                  ["One database", "'We searched Google Scholar'", "Three or more, plus grey literature, plus citation chasing"],
                  ["Single screener", "'Studies were selected by the first author'", "Two, with a conflict log"],
                  ["Pooling different comparators", "Cash vs nothing pooled with cash vs in-kind", "Comparator as an eligibility criterion and a subgroup"],
                  ["Appraisal ignored", "A traffic-light figure and then equal weights", "Sensitivity analysis by risk of bias, in the abstract"],
                  ["Counting p-values", "'Seven of ten studies found significant effects'", "Direction counts or effect sizes"],
                  ["I&sup2; as a verdict", "'Heterogeneity was high (I&sup2; = 82%), so results should be interpreted with caution'", "&tau;&sup2;, a prediction interval, and pre-specified moderators"],
                  ["Twelve estimates from one paper", "k = 60 from 14 studies with no adjustment", "One per study, or RVE"],
                  ["Funnel plot with six studies", "'No evidence of publication bias'", "Do not test below ten; search the file drawer instead"],
                  ["No certainty rating", "Results reported as if all equally reliable", "GRADE per outcome"],
                  ["Applicability unaddressed", "Evidence from Latin America applied to Nepal without comment", "A named paragraph on transfer"],
                  ["Bibliometrics as evidence", "'The most-cited interventions are&hellip;'", "Keep the two products apart"]]},
         ]},

        {"type": "content", "label": "Reading a Review", "title": "How to read someone else's review in twenty minutes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "REGISTRATION: is there a protocol, and does the paper match it?",
                  "SEARCH: which databases, what date, is the strategy in an appendix?",
                  "FLOW: do the numbers add up, and are exclusions listed with reasons?",
                  "APPRAISAL: which tool, by how many people, and was it used in the synthesis?",
                  "SYNTHESIS: pooled or narrative, which model, heterogeneity reported how?",
                  "CERTAINTY: GRADE, and does the abstract's language match it?"]},
                       {"t": "body", "html": "AMSTAR 2 (Shea and colleagues 2017) formalises this "
                        "with 16 items, seven of them critical; a review failing more than one "
                        "critical item is rated critically low. Most reviews published in general "
                        "development journals fail at least one, usually the protocol or the "
                        "appraisal."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading for a decision", "html":
                         "A programme officer does not need to reproduce the review. They need to "
                         "know three things: the effect on the outcomes they care about in "
                         "absolute terms, how certain it is, and whether the evidence came from "
                         "settings like theirs. The summary-of-findings table and the "
                         "applicability paragraph answer all three. If the review does not have "
                         "them, its conclusions are the authors' opinion of their own work."},
                        {"t": "hbox", "color": "amber", "html": "The abstract of a review with "
                         "low-certainty evidence should say 'may'. 'Cash transfers improve "
                         "learning' above a low rating is a mismatch a reader should catch."}]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "What it is", "Access"],
              "rows": [
                  ["Cochrane Handbook for Systematic Reviews of Interventions, version 6.4 (2023)", "The reference for every step, from question to GRADE; chapters 5, 6, 8, 10 and 13 are the core", "Free online at training.cochrane.org/handbook"],
                  ["Gough, Oliver and Thomas, <em>An Introduction to Systematic Reviews</em>, 2nd ed. (Sage, 2017)", "The social-science and mixed-methods treatment, from the EPPI-Centre", "Book"],
                  ["Petticrew and Roberts, <em>Systematic Reviews in the Social Sciences</em> (Blackwell, 2006)", "Still the clearest account of why the method transfers beyond medicine", "Book"],
                  ["Borenstein, Hedges, Higgins and Rothstein, <em>Introduction to Meta-Analysis</em>, 2nd ed. (Wiley, 2021)", "Meta-analysis from first principles with worked arithmetic", "Book"],
                  ["Stanley and Doucouliagos, <em>Meta-Regression Analysis in Economics and Business</em> (Routledge, 2012)", "The economics approach: FAT-PET, publication bias, meta-regression", "Book"],
                  ["Campbell Collaboration and 3ie methods guides", "Standards and templates for development reviews; the quasi-experimental risk-of-bias tool", "Free at campbellcollaboration.org and 3ieimpact.org"],
                  ["Donthu et al. 2021, <em>Journal of Business Research</em> 133:285", "Guidelines for a bibliometric analysis", "Journal article"],
                  ["Cochrane Interactive Learning; Campbell's online course", "Structured courses with exercises", "Cochrane's is paid, with free access in some low- and middle-income countries; Campbell's is free"],
                  ["ImpactMojo", "Survey Design 101, Impact Evaluation 101 and Research Methods 101 in this series cover the primary studies these reviews synthesise", "impactmojo.in/101-courses/"]]},
         ]},

        {"type": "content", "label": "Summary", "title": "What to remember",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "A systematic review is a study, with a protocol, a sample and a method, and it is judged as one.",
                  "The search decides the evidence base. Three databases, grey literature, citation chasing, and a strategy saved verbatim.",
                  "Two people at every judgement: screening, extraction, appraisal, GRADE.",
                  "Risk of bias is assessed per outcome and used in the synthesis, or it was decoration.",
                  "Pool when the protocol said to and the studies allow it; report Q, I&sup2;, &tau;&sup2; and a prediction interval, and explain heterogeneity rather than lament it."]}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "Where you cannot pool, synthesise to SWiM: directions, standardised tables, structured argument.",
                  "Rate certainty with GRADE and let the abstract's verbs match it.",
                  "Report to PRISMA 2020 and put the search, the extraction sheet and the code where anyone can find them.",
                  "Bibliometrics maps the field; it does not weigh the evidence. Keep the two products apart and pair them when it helps.",
                  "Write the applicability paragraph. A review for South Asia that does not say what transfers has not finished."]},
                        {"t": "hbox", "color": "amber", "html": "Every one of these is a decision "
                         "you can defend in writing. That is the whole method."}]},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Systematic Reviews &amp; Evidence Synthesis 101 &middot; Complete",
         "headline": "Now go find out<br>what is already known.",
         "byline": "A review is a study of studies, with a protocol, a sample and a method, and "
                   "every decision in it can be written down and defended. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

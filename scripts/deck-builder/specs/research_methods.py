# -*- coding: utf-8 -*-
"""
Research Methods 101: ImpactMojo 101 Series (native deck spec)
The research process for development practitioners in South Asia, from question to write-up.
Build: python3 scripts/deck-builder/build.py research_methods

Sources opened while writing (October 2026):
- ICMR National Ethical Guidelines for Biomedical and Health Research Involving Human
  Participants 2017: https://ethics.ncdirindia.org/asset/pdf/ICMR_National_Ethical_Guidelines.pdf
- DPDP Act 2023 (No. 22 of 2023), Gazette text: https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- Collection of Statistics Act 2008 (No. 7 of 2009), Gazette text:
  https://megpolice.gov.in/sites/default/files/collection-of-statistics_act_2008.pdf
- NFHS-5 India Report (IIPS & ICF 2021): https://dhsprogram.com/pubs/pdf/FR375/FR375.pdf
- MoSPI press note on PLFS changes, 14 May 2025:
  https://mospi.gov.in/sites/default/files/press_release/Press_note_changes_sample_design_Final.pdf
- MoSPI HCES 2022-23 fact sheet: https://mospi.gov.in/sites/default/files/publication_reports/Factsheet_HCES_2022-23.pdf
- PIB, 15 Nov 2019, CES 2017-18: https://pib.gov.in/PressReleasePage.aspx?PRID=1591792
- ASER 2024 national presentation: https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-All-India-ppt-Jan-27-11am.pdf
- DHS Program survey API (BD2022DHS, NP2022DHS): https://api.dhsprogram.com/rest/dhs/surveys
- Nepal NLSS-IV catalogue: https://microdata.nsonepal.gov.np/index.php/catalog/149
- BBS, HIES 2022 Final Report (14 Dec 2023), sample of 14,400 households:
  https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-bbs/2024/12/22b6e770f6a84cd9a48ff636ae506818.pdf
- IIPS, NFHS-6 (2023-24) Fact Sheets, May 2026:
  https://www.nfhsiips.in/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-2024%20Fact%20Sheets.pdf
- Open Science Collaboration 2015 abstract (PubMed 26315443)
- Deaton & Kozel 2005 abstract: https://openknowledge.worldbank.org/entities/publication/2349d43d-0adb-5d44-b613-5f4e7cd1931b
- Guest, Bunce & Johnson 2006 abstract (doi 10.1177/1525822x05279903)
- AEA RCT Registry about page: https://www.socialscienceregistry.org/site/about
- RIDIE: https://ridie.3ieimpact.org/
- WMA Declaration of Helsinki: https://www.wma.net/policies-post/wma-declaration-of-helsinki/
- Puttaswamy (2017): https://www.scobserver.in/court-case/fundamental-right-to-privacy
"""


def S(label, title, blocks, **kw):
    d = {"type": "content", "label": label, "title": title, "blocks": blocks}
    d.update(kw)
    return d


def B(html, sm=False):
    d = {"t": "body", "html": html}
    if sm:
        d["cls"] = "sm"
    return d


def H(color, html):
    return {"t": "hbox", "color": color, "html": html}


def P(color, title, html):
    return {"t": "panel", "color": color, "title": title, "blocks": [B(html, sm=True)]}


def TC(left, right, ratio="half"):
    return {"t": "twocol", "ratio": ratio, "left": left, "right": right}


def T(head, rows):
    return {"t": "table", "head": head, "rows": rows}


def BL(items, color="", sm=True):
    d = {"t": "bullets", "items": items, "sm": sm}
    if color:
        d["color"] = color
    return d


def TERM(word, d):
    return {"t": "term", "word": word, "def": d}


def FL(steps):
    return {"t": "flow", "steps": steps}


def ST(cards, cols=None):
    d = {"t": "stats", "cards": cards}
    if cols:
        d["cols"] = cols
    return d


def C(num, label, color="cyan", source=None):
    d = {"num": num, "label": label, "color": color}
    if source:
        d["source"] = source
    return d


def DIV(num, word, title):
    return {"type": "divider", "num": num, "label": "Section " + word, "title": title}


def L(file, name):
    return '<a href="/101-courses/%s">%s 101</a>' % (file, name)


ICMR = "ICMR, National Ethical Guidelines for Biomedical and Health Research Involving Human Participants, 2017"

SLIDES = [
    # ===================== TITLE / TOC =====================
    {"type": "title",
     "main": "Research<br>Methods<br>101",
     "sub": "From question to write-up: how development practitioners in South Asia frame "
            "answerable questions, choose designs, sample, measure, handle data ethically "
            "and report what they found",
     "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Question to Write-up"]},

    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Why method matters"},
         {"name": "Framing answerable questions"},
         {"name": "Ways of knowing"},
         {"name": "Choosing a design"},
         {"name": "Sampling logic"},
         {"name": "Measurement: validity and reliability"},
         {"name": "Qualitative, quantitative and mixed"},
         {"name": "Secondary data in South Asia"},
         {"name": "Ethics, consent and the law"},
         {"name": "Analysis plans and pre-registration"},
         {"name": "Putting it to work"},
         {"name": "Writing, dissemination and where next"},
     ]},

    # ===================== SECTION 01 =====================
    DIV("01", "One", "Why method matters"),

    S("Starting point", "Research is a disciplined way of being less wrong", [
        B("Every programme officer already makes claims about the world: that a block has more "
          "out-of-school girls than its neighbour, that a cash transfer reached the poorest, that "
          "a training changed how nurses counsel mothers. <strong>Research</strong> is the set of "
          "habits that lets someone else check such a claim and reach the same answer from the "
          "same evidence. Method is the record of the choices you made on the way."),
        TC([P("amber", "Everyday knowing",
              "Built from what we happened to see, who we happened to ask and what we already "
              "believed. Fast and often right, but impossible to audit. Two experienced officers "
              "can hold opposite views about the same district and neither can show why.")],
           [P("green", "Research knowing",
              "Built from a stated question, a design chosen in advance, a sample drawn by a rule, "
              "measures that were tested and an analysis anyone can repeat. Slower, and every "
              "step is open to challenge, which is exactly what makes the answer usable.")]),
        H("cyan", "The test of a method is simple: could a careful sceptic, given your notes and "
          "your data, follow every step and arrive where you did?"),
    ]),

    S("The chain", "The research process is a chain of decisions", [
        B("Research runs as a sequence. Each link depends on the one before it, and a weak link "
          "early on cannot be repaired by sophistication later. A brilliant regression on a badly "
          "drawn sample answers a question about the wrong people."),
        FL(["QUESTION: what exactly do we need to know?",
            "DESIGN: what comparison or description answers it?",
            "SAMPLE: whom, where and how many?",
            "MEASURES: how will each concept become data?",
            "ANALYSIS: what will we compute, decided in advance?",
            "WRITE-UP: who needs the answer, in what form?"]),
        TC([B("<strong>Where mistakes are cheap:</strong> at the question and design stage, "
              "when a change costs an afternoon of discussion and a revised protocol.", sm=True)],
           [B("<strong>Where mistakes are expensive:</strong> after fieldwork, when a missing "
              "variable or a biased frame can only be described, never fixed.", sm=True)]),
    ]),

    S("When it goes wrong", "India's 1990s poverty numbers and the questionnaire", [
        B("Method is rarely a technical footnote. Official estimates for India showed poverty "
          "falling from 36 per cent of the population in 1993-94 to 26 per cent in 1999-2000. "
          "Deaton and Kozel reviewed the long argument that followed. They found no full "
          "consensus on what happened, and good evidence that the official estimates of poverty "
          "reduction were too optimistic, particularly for rural India."),
        ST([C("36% to 26%", "Official poverty headcount, India, 1993-94 to 1999-2000", "amber",
              "Deaton &amp; Kozel, <em>World Bank Research Observer</em>, 2005"),
            C("Too optimistic", "Their reading of the official decline, especially rural", "red",
              "Deaton &amp; Kozel, 2005")], cols=2),
        H("indigo", "The issues they list are the subject of this deck: questionnaire design, "
          "reporting periods, survey non-response, repair of imperfect data, the choice of poverty "
          "lines, and the way statistics and politics interact. A design choice in a survey "
          "schedule became a national political argument."),
    ]),

    S("When it goes wrong", "A survey the government chose not to publish", [
        TC([B("The National Statistical Office ran an all-India consumption survey in the 75th "
              "round, July 2017 to June 2018. On 15 November 2019 the Ministry of Statistics and "
              "Programme Implementation announced that, in view of data quality issues, it had "
              "decided not to release the results, and would examine running the next survey "
              "after refining the process.", sm=True),
            B("The next published round was the Household Consumption Expenditure Survey of "
              "2022-23, which ran from August 2022 to July 2023. The previous published round "
              "was 2011-12. India went eleven years without a published national consumption "
              "distribution.", sm=True)],
           [ST([C("15 Nov 2019", "MoSPI decision not to release CES 2017-18", "red",
                  "PIB, Ministry of Statistics, 15 Nov 2019"),
                C("2011-12 to 2022-23", "Gap between published consumption rounds", "amber",
                  "MoSPI, HCES 2022-23 Fact Sheet, 2024")], cols=1)], ratio="a32"),
        H("cyan", "Whatever view one takes of that decision, the practitioner's lesson holds: "
          "credibility is part of method. A dataset nobody trusts, or nobody can see, cannot "
          "inform a decision."),
    ]),

    S("Scope", "What this deck covers, and where the depth lives", [
        B("This is the map. It walks the whole research process once, at the level a programme "
          "manager, evaluator or early researcher needs to commission, design or critique a "
          "study. Each method family has its own deck in the series with far more depth."),
        T(["If you need depth on", "Go to", "What it adds"],
          [["Interviews, observation, coding", L("qual-methods.html", "Qualitative Methods"),
            "Sampling to saturation, interviewing, thematic analysis"],
           ["Questionnaires and fieldwork", L("survey-design.html", "Survey Design"),
            "Question wording, translation, pretesting, field quality"],
           ["Combining strands", L("mixed-methods.html", "Mixed Methods"),
            "Integration, joint displays, sequencing"],
           ["Did the programme cause the change?", L("impact-eval.html", "Impact Evaluation"),
            "RCTs, quasi-experiments, attribution"],
           ["Identification logic", L("causal-inference.html", "Causal Inference"),
            "Counterfactuals, confounding, instruments, discontinuities"],
           ["Statistics with numbers", L("quant-methods.html", "Quantitative Methods"),
            "Estimation, inference, regression"]]),
    ], compact=True),

    S("Three habits", "Three habits that separate research from reporting", [
        B("Programme reports and research studies often use the same data. What differs is a "
          "set of habits that make the work checkable and proportionate. These recur in every "
          "section that follows."),
        TC([P("cyan", "1. Write it down first",
              "State the question, the comparison and the analysis before you see the outcome "
              "data. A plan written afterwards can always be made to fit."),
            P("green", "2. Look for what would prove you wrong",
              "Name in advance the result that would count against your expectation, and go "
              "looking for it. A study that could only ever confirm is a brochure.")],
           [P("amber", "3. Claim in proportion",
              "A survey of 400 households in one district describes that district. Say so, "
              "and resist the pull to generalise to the state or the country."),
            P("indigo", "Who holds you to it",
              "Ethics committees, registries, peer reviewers, funders and communities. Each "
              "checks a different habit, and Sections 09 and 10 cover how.")]),
    ]),

    # ===================== SECTION 02 =====================
    DIV("02", "Two", "Framing answerable questions"),

    S("Problem to question", "A problem has to be narrowed into a research question", [
        B("Practitioners usually arrive with a <strong>problem</strong>: girls in a block stop "
          "attending school after class 8. A <strong>topic</strong> is the broad area: "
          "adolescent girls' education. A <strong>research question</strong> is narrow enough "
          "that some specific body of evidence would answer it, and you can say in advance what "
          "that evidence would look like."),
        FL(["PROBLEM: girls stop attending after class 8",
            "TOPIC: transition to secondary school",
            "QUESTION: what share of girls who finish class 8 in 2025 enrol in class 9, and how "
            "does it vary with distance to the nearest secondary school?",
            "EVIDENCE: enrolment records plus a household survey with distance measured"]),
        TC([B("A good question names the <strong>population</strong>, the <strong>place</strong>, "
              "the <strong>time</strong> and the <strong>quantity or process</strong> of "
              "interest.", sm=True)],
           [B("If two people could read your question and plan different studies, it is still a "
              "topic. Keep narrowing until they would plan the same one.", sm=True)]),
    ]),

    S("Question types", "Three kinds of question, three kinds of study", [
        B("Most development research questions fall into three families. Naming the family early "
          "saves months, because each family needs a different design, a different sample and a "
          "different standard of proof."),
        T(["Family", "Asks", "South Asian example (illustrative)", "Typical design"],
          [["Descriptive", "How many, how much, where, who?",
            "What share of Std III children in rural Odisha can read a Std II text?",
            "Probability sample survey, census, administrative data"],
           ["Explanatory", "Why, how, through what process?",
            "Why do women in garment work in Dhaka leave factory jobs after marriage?",
            "Case studies, comparative designs, interviews, panel data"],
           ["Evaluative", "Did it work, for whom, at what cost?",
            "Did a community health worker visit schedule in Nepal change antenatal check-ups?",
            "Randomised or quasi-experimental comparison, process evaluation"]]),
        H("amber", "Watch for evaluative questions dressed as descriptive ones. 'How many women "
          "were trained?' is monitoring. 'Did training change practice?' needs a comparison."),
    ], compact=True),

    S("FINER", "Is the question worth answering? The FINER test", [
        TERM("FINER", "A checklist from clinical research (Hulley and colleagues, <em>Designing "
             "Clinical Research</em>): a good question is Feasible, Interesting, Novel, Ethical "
             "and Relevant. It travels well to development work."),
        TC([BL(["<strong>Feasible:</strong> enough people, money, time, access and skill to "
                "answer it this year",
                "<strong>Interesting:</strong> to the people who will use it, which is a "
                "ministry, a funder or a community, and only sometimes a journal",
                "<strong>Novel:</strong> it adds something; check NFHS, PLFS, ASER and 3ie's "
                "evidence portal before collecting new data"])],
           [BL(["<strong>Ethical:</strong> the burden on respondents is justified by the value "
                "of the answer (Section 09)",
                "<strong>Relevant:</strong> some decision would change depending on the "
                "answer",
                "If no decision would change, the question may be interesting and still not "
                "worth a field budget"], "green")]),
        H("cyan", "Run every draft question through FINER with a colleague who will be honest "
          "about the F. Feasibility kills more studies than any other letter."),
    ]),

    S("PICO", "Structuring an evaluative question: PICO plus setting and time", [
        B("For questions about whether an intervention changed something, the PICO structure "
          "from health research forces precision. Development studies usually need two extra "
          "elements, because context changes effects."),
        T(["Element", "Ask", "Illustrative example"],
          [["Population", "Who exactly?", "Households with a child under 2 in 40 villages of "
            "one Bihar district"],
           ["Intervention", "What, delivered how and how often?", "Fortnightly home visits by "
            "a trained frontline worker for 12 months"],
           ["Comparison", "Compared with what?", "Villages receiving the standard schedule"],
           ["Outcome", "Measured how, when?", "Exclusive breastfeeding under 6 months, "
            "mother's report at endline"],
           ["Setting", "Where and through which system?", "Government ICDS platform"],
           ["Time", "Over what period?", "Baseline 2026, endline 2027"]]),
        H("indigo", "If you cannot fill the Comparison row, you do not yet have an evaluative "
          "question. You have a descriptive one about people who received a programme. See "
          + L("impact-eval.html", "Impact Evaluation") + "."),
    ], compact=True),

    S("Narrowing", "From a slogan to something you can measure", [
        B("Programme language is full of goals that cannot be measured as written: 'improve "
          "nutrition', 'strengthen governance', 'raise women's status'. Research needs each to become "
          "a question about observable things. Compare drafts of the same question."),
        TC([P("red", "Too broad",
              "Does the programme improve women's position in Pakistan? (Which programme? "
              "Which women? Position measured how? Compared with whom? Over what "
              "period?)"),
            P("red", "Too vague",
              "What do people think about the new ration system? (Which people? Think "
              "about which part of it? For what decision?)")],
           [P("green", "Answerable",
              "Among women aged 18&ndash;49 in programme villages of two Sindh districts, did "
              "participation in savings groups change the share who report a say in large "
              "household purchases, compared with matched non-programme villages, after "
              "two years?"),
            P("green", "Answerable",
              "Which steps in collecting monthly rations do card-holders in three Jharkhand "
              "blocks report as most costly in time and travel?")]),
    ]),

    S("Concepts and indicators", "Concepts become indicators through an operational definition", [
        TERM("Operational definition", "The exact procedure that turns an abstract concept "
             "into a recorded value: which question, asked of whom, coded how, over what "
             "reference period."),
        TC([B("Take <strong>'women's work'</strong>. One definition counts any economic "
              "activity in the last 365 days. Another counts only activity in the last seven "
              "days. A third includes unpaid care and household production. Each yields a "
              "different number for the same women, and each is defensible for a different "
              "purpose.", sm=True),
            B("India's PLFS itself reports two frameworks: usual status, with a reference "
              "period of the last 365 days, and current weekly status, with the last seven "
              "days (MoSPI, PLFS press note, 14 May 2025).", sm=True)],
           [H("amber", "Write the operational definition into your protocol before fieldwork. "
              "If you borrow an indicator from NFHS or PLFS, copy its definition exactly, or "
              "your comparison with the official figure is meaningless."),
            B("More on turning concepts into measures in Section 06, and in "
              + L("data-lit.html", "Data Literacy") + ".", sm=True)]),
    ]),

    S("Hypotheses", "A hypothesis is a prediction that could fail", [
        B("A hypothesis states what you expect to find and why, in a form the data could "
          "contradict. It comes from a theory of change: a reasoned account of how an "
          "intervention or a social process leads to an outcome. Writing it down keeps the "
          "analysis honest, because the test is fixed before the data arrive."),
        TC([TERM("Research hypothesis", "Girls living more than 3 km from a secondary school "
                 "are less likely to enrol in class 9 than girls living within 1 km, holding "
                 "household income constant."),
            TERM("Null hypothesis", "No difference in class 9 enrolment by distance band, "
                 "once income is accounted for. Statistical tests ask how surprising the data "
                 "would be if this were true.")],
           [BL(["State the <strong>direction</strong> you expect, and why",
                "Name the <strong>mechanism</strong> (travel time, safety, cost) so you can "
                "look for evidence on it too",
                "Say what result would count <strong>against</strong> you",
                "Qualitative studies use working propositions in the same spirit, revised as "
                "evidence accumulates"], "cyan")]),
        H("green", "Building the theory of change first makes hypotheses easier to write. See "
          + L("toc-workbench.html", "Theory of Change") + "."),
    ]),

    S("Whose question", "Who asked the question shapes what gets found", [
        B("Research questions in development are often set far from the people they concern: in "
          "a funder's results framework, a ministry's monitoring needs or a university "
          "department. That can be legitimate, and it still decides what is counted and what "
          "is left invisible."),
        TC([P("amber", "Questions from above",
              "Tend to ask about coverage, cost and targets. Useful for budgets. They can miss "
              "what participants consider the main problem, such as harassment on the route to "
              "school when the framework asks about fees."),
            BL(["Run scoping conversations with intended participants before fixing the "
                "question",
                "Include frontline workers, who often know where the data will be wrong"],
               "amber")],
           [P("green", "Questions from below",
              "Participatory framing brings in priorities the commissioner did not anticipate. "
              "Robert Chambers made this argument in <em>Rural Development: Putting the Last "
              "First</em> (Longman, 1983)."),
            B("Approaches and tools: " + L("participatory-methods.html", "Participatory Methods")
              + " and " + L("feminist-research.html", "Feminist Research") + ".", sm=True)]),
    ]),

    # ===================== SECTION 03 =====================
    DIV("03", "Three", "Ways of knowing"),

    S("Plain words", "Ontology and epistemology without the jargon", [
        B("Two philosophical questions sit underneath every study, whether or not the authors "
          "name them. You do not need to resolve them, but you need to know which answers your "
          "design quietly assumes, because they decide what counts as evidence."),
        TC([TERM("Ontology", "What is there to know? Is 'poverty' a fact about households that "
                 "exists whether or not we measure it, or a category people construct and "
                 "contest?")],
           [TERM("Epistemology", "How can we know it, and what makes a claim credible? "
                 "Repeated measurement by a standard instrument? The considered account of the "
                 "people living it? Both?")]),
        H("cyan", "In practice these show up as choices: a fixed questionnaire or an open "
          "interview, a sample chosen to represent or to illuminate, a researcher who stays "
          "neutral or one who acknowledges a position. The traditions on the next slide bundle "
          "those choices."),
        B("These traditions are working labels. Many researchers move between them across a "
          "career, and sometimes within a single study.", sm=True),
    ]),

    S("Four traditions", "Four research traditions you will meet", [
        T(["Tradition", "Assumes", "Credible evidence is", "Common methods"],
          [["Positivist and post-positivist", "A reality exists that can be measured, imperfectly",
            "Replicable measurement, controlled comparison, quantified uncertainty",
            "Surveys, experiments, secondary data analysis"],
           ["Interpretivist or constructivist", "Social reality is made through meaning",
            "Rich accounts of how people understand and act", "In-depth interviews, ethnography, "
            "case studies"],
           ["Critical", "Knowledge is shaped by power", "Evidence that "
            "exposes and challenges inequality, produced with those affected",
            "Participatory action research, feminist and caste-conscious inquiry"],
           ["Pragmatist", "Use what answers the question", "Whatever combination best serves "
            "the decision", "Mixed methods"]]),
        H("amber", "Most large South Asian statistical systems (NSS, Census, NFHS) work in the "
          "post-positivist tradition. Much of what we know about how caste, gender and "
          "disability are lived comes from the other three."),
    ], compact=True),

    S("Post-positivism in practice", "Measuring a reality you admit you measure imperfectly", [
        TC([B("Post-positivism accepts that every measurement carries error and every finding is "
              "provisional. Its answer is procedure: standard instruments, trained enumerators, "
              "probability samples, documented weights and stated margins of error.", sm=True),
            B("India's statistical surveys show the tradition at work. The HCES 2022-23 fact "
              "sheet documents its sample, its multistage stratified design, its questionnaires "
              "and its estimation procedure in appendices, so another analyst can reproduce the "
              "estimates from the unit-level data.", sm=True)],
           [P("green", "Strengths",
              "Comparable across places and over time. Large samples allow small-area and "
              "subgroup estimates. Errors can be quantified."),
            P("red", "Limits",
              "Can only find what the questionnaire asks about. Categories fixed at the design "
              "stage, such as a household head or a main occupation, may not fit how people "
              "live.")]),
        H("cyan", "The tradition's own discipline is to report error openly: confidence "
          "intervals, non-response, design effects. Section 05 shows how."),
    ]),

    S("Interpretivism in practice", "Understanding what an experience means to the people in it", [
        TC([B("Interpretive research starts from the view that people act on the meanings things "
              "have for them. To explain behaviour you must understand those meanings, in the "
              "participants' own terms, in context.", sm=True),
            B("Illustrative: a survey records that a woman in rural Rajasthan did 'no work' last "
              "week. An interview reveals she grazed goats, carried water and helped at a family "
              "shop, and that she and her family do not call any of it work. The survey number "
              "is accurate to its definition. The interview explains why the definition misses "
              "her.", sm=True)],
           [P("green", "Strengths",
              "Finds categories researchers did not anticipate. Explains mechanisms. Gives "
              "voice to people standard instruments flatten."),
            P("red", "Limits",
              "Small, purposive samples do not estimate prevalence. Findings depend on the "
              "researcher's skill and position, which must be made visible.")]),
        H("indigo", "Depth on interviews, observation and analysis: "
          + L("qual-methods.html", "Qualitative Methods") + " and "
          + L("visual-eth.html", "Visual Ethnography") + "."),
    ]),

    S("Critical traditions", "Asking who benefits from the way knowledge is produced", [
        B("Critical, feminist and decolonial traditions treat research as part of the social "
          "world it studies. They ask who sets questions, whose categories are used, who is "
          "paid and credited, and whether findings return to the people who gave them. In South "
          "Asia these questions are sharp around caste, gender, religion, Adivasi communities "
          "and disability."),
        TC([BL(["Who is missing from the sampling frame, such as people without a fixed "
                "address or a ration card?",
                "Whose language is the questionnaire in, and who translated it?",
                "Who was in the room for a group discussion, and who could not speak freely?"],
               "amber")],
           [BL(["Who owns the data after the study?",
                "Are local researchers authors, or only field staff?",
                "Do participants see the results, in a form they can use?"], "green")]),
        H("cyan", "These questions improve any study, including a large survey. Go further with "
          + L("feminist-research.html", "Feminist Research") + ", "
          + L("decolonize-dev.html", "Decolonial Development") + " and "
          + L("data-feminism.html", "Data Feminism") + "."),
    ]),

    S("Pragmatism and position", "Why practitioners end up pragmatists, and why position matters", [
        TC([P("cyan", "Pragmatism",
              "Starts from the question and the decision, and picks whatever mix of methods "
              "answers them. It is the usual home of mixed methods research and of most "
              "programme evaluation. Its risk is shallowness: two weak strands do not make a "
              "strong study."),
            B("Pragmatism still owes an account of why each method was chosen and how the "
              "strands were combined. 'We used what was convenient' gives a reviewer nothing to assess.", sm=True)],
           [P("amber", "Reflexivity and positionality",
              "Whatever the tradition, the researcher affects the research. An upper-caste male "
              "interviewer and a Dalit woman respondent may produce a different conversation "
              "from two women from the same community. Reflexivity means noticing and recording "
              "that effect."),
            BL(["Write a short positionality note in the protocol",
                "Keep a field diary of moments when your presence changed the answer",
                "Report both in the methods section"], "amber")]),
    ]),

    # ===================== SECTION 04 =====================
    DIV("04", "Four", "Choosing a design"),

    S("Design follows question", "The question chooses the design", [
        B("A design is the plan for producing the comparison or description your question needs. "
          "Teams often start from a method they like, or one a funder favours, and fit a "
          "question to it. Start instead from the question family in Section 02."),
        T(["Question", "Design family", "Typical data", "Main threat"],
          [["How many girls are out of school, by district?", "Descriptive, cross-sectional",
            "Probability sample survey or census", "Frame coverage, non-response"],
           ["How has it changed since 2018?", "Descriptive, repeated cross-section or panel",
            "Same survey with a stable method", "Changes in method or definitions"],
           ["Why do they leave?", "Explanatory", "Interviews, case studies, panel data",
            "Selective sampling, researcher bias"],
           ["Did a bicycle scheme keep them in school?", "Evaluative", "Comparison of "
            "exposed and unexposed groups", "Confounding, selection"],
           ["How was the scheme delivered?", "Process evaluation", "Records, observation, "
            "interviews", "Relying on implementers' accounts"]]),
        H("cyan", "Name the main threat for your design in the protocol and say how you will "
          "reduce it. Reviewers look for exactly that paragraph."),
    ], compact=True),

    S("Descriptive designs", "Description done well is valuable on its own", [
        B("Description is the foundation of most policy: where to open a school, which "
          "districts to prioritise, how large a budget to request. ASER, run by the ASER Centre, has used district "
          "partners since 2005 to describe schooling and basic learning in rural India, with "
          "one-on-one tasks and a sampling method it reports as consistent over time."),
        ST([C("605", "Rural districts covered, ASER 2024", "cyan",
              "ASER Centre, ASER 2024 national release, Jan 2025"),
            C("352,028", "Households surveyed", "green", "ASER Centre, 2025"),
            C("649,491", "Children aged 3&ndash;16 surveyed", "indigo", "ASER Centre, 2025")],
           cols=3),
        H("amber", "ASER's credibility rests on consistency: the same tasks and the same "
          "sampling approach each round, so a change in the number is more likely to be a change "
          "in children's learning than a change in the method. That is a design decision."),
    ]),

    S("Time in the design", "Cross-section, repeated cross-section or panel", [
        TC([T(["Design", "Who is observed", "Answers"],
              [["Cross-section", "One sample, once", "What is the situation now?"],
               ["Repeated cross-section", "New sample each round", "How has the population "
                "changed?"],
               ["Panel", "Same units, repeatedly", "How do individuals change, and who moves "
                "in and out of a state?"]])],
           [B("<strong>Example:</strong> since January 2025 the PLFS uses a rotational panel in "
              "both rural and urban areas: each selected household is visited four times in "
              "four consecutive months (MoSPI press note, 14 May 2025). That design is what "
              "allows monthly estimates.", sm=True),
            B("Panels are powerful and fragile. Households move, split and refuse, and those who "
              "leave the panel differ from those who stay. Attrition must be tracked and "
              "reported.", sm=True)], ratio="a32"),
        H("indigo", "A repeated cross-section can show that poverty fell. Only a panel can show "
          "whether the same households escaped, or whether some escaped while others fell in."),
    ]),

    S("Explanatory designs", "Designs for asking why and how", [
        TC([P("cyan", "Comparative case studies",
              "Select cases that differ on the factor you think matters and are similar "
              "otherwise: two blocks with different dropout rates but similar income. Trace what "
              "differs."),
            P("cyan", "Process tracing",
              "Follow a causal chain step by step in one case, testing whether each link left "
              "the evidence it should have. Useful for policy change and advocacy outcomes.")],
           [P("green", "Correlational analysis",
              "Use survey data to see which household characteristics travel together with an "
              "outcome. Good for generating hypotheses. Weak for proving causes, for the "
              "reason on the next slide."),
            P("green", "Longitudinal qualitative",
              "Return to the same people over months or years to see how decisions unfold, for "
              "example as a young woman moves from school to marriage to work.")]),
        H("amber", "Explanatory designs live or die on case selection. Choose cases by a stated "
          "rule tied to the question, and record why others were not chosen."),
    ]),

    S("Confounding", "Correlation is a clue, and causation needs a comparison", [
        B("Illustrative: in survey data, children in households with a toilet are taller for "
          "their age. It is tempting to conclude toilets cause growth. But households with "
          "toilets also tend to be richer, better educated and closer to health services, and "
          "each of those could explain the difference."),
        TC([TERM("Confounder", "A factor that influences both the exposure (toilet) and the "
                 "outcome (child height), creating an association that is partly or wholly not "
                 "causal."),
            TERM("Selection", "When the people who receive a programme differ systematically "
                 "from those who do not, often because they chose to join or were chosen.")],
           [BL(["Control for measured confounders, and admit unmeasured ones remain",
                "Use a design where exposure is assigned by chance or by a rule",
                "Compare changes over time as well as levels",
                "Look for a dose-response pattern and a plausible mechanism"], "cyan")]),
        H("indigo", "The logic of counterfactuals is the subject of "
          + L("causal-inference.html", "Causal Inference") + "."),
    ]),

    S("Evaluative designs", "The evaluative toolkit at a glance", [
        T(["Design", "How the comparison is built", "Indian example"],
          [["Randomised controlled trial", "Chance decides who gets the programme",
            "Banerjee, Cole, Duflo and Linden, two randomised experiments on remedial education "
            "in India, <em>QJE</em> 2007"],
           ["Randomised incentive design", "Chance decides which schools get a pay scheme",
            "Muralidharan and Sundararaman, teacher performance pay in India, <em>JPE</em> "
            "2011"],
           ["Difference-in-differences", "Change in exposed group minus change in comparison "
            "group", "Programmes rolled out district by district"],
           ["Regression discontinuity", "Compare units just above and below an eligibility "
            "cut-off", "Schemes with a score or population threshold"],
           ["Theory-based evaluation", "Test each link of the theory of change with mixed "
            "evidence", "Complex governance or advocacy programmes"]]),
        H("cyan", "Each design rests on an assumption that cannot be fully tested. Choosing "
          "among them, and checking those assumptions, is covered in "
          + L("impact-eval.html", "Impact Evaluation") + "."),
    ], compact=True),

    S("Validity", "Four questions about any finding", [
        B("Shadish, Cook and Campbell (<em>Experimental and Quasi-Experimental Designs for "
          "Generalized Causal Inference</em>, 2002) organise threats to a study's conclusions "
          "into four types. Each is a question a reviewer will ask about your design."),
        T(["Validity type", "Question", "Typical threat"],
          [["Statistical conclusion", "Is the association real, or noise?",
            "Sample too small, many tests, unreliable measures"],
           ["Internal", "Did the exposure cause the outcome?",
            "Confounding, selection, attrition"],
           ["Construct", "Do the measures capture the concepts?",
            "An indicator that tracks something else (Section 06)"],
           ["External", "Would it hold elsewhere?", "One district, one season, one "
            "implementing partner"]]),
        H("amber", "Strengthening one type often costs another. A tightly controlled pilot has "
          "high internal validity and may say little about a state-wide scale-up run by the "
          "government."),
    ], compact=True),

    S("Constraints", "Choosing under budget, time, ethics and politics", [
        TC([T(["Constraint", "What it usually rules out", "Workable alternative"],
              [["Programme already rolled out", "Randomisation", "Difference-in-differences, "
                "matched comparison"],
               ["Budget under a lakh", "New large survey", "Secondary data plus targeted "
                "interviews"],
               ["Three months", "Panel, long follow-up", "Cross-section plus records"],
               ["Sensitive topic", "Group discussions", "Private interviews, self-completion"],
               ["Partner resists a control group", "Pure control", "Phased roll-out, "
                "encouragement design"]])],
           [B("Constraints are design inputs. State them in the protocol and explain how the "
              "chosen design answers the question within them. Reviewers respect a modest "
              "design matched candidly to its limits.", sm=True),
            H("red", "The dangerous move is keeping an ambitious question and quietly using a "
              "design that cannot answer it. Shrink the question instead.")], ratio="a32"),
        B("Illustrative figures. Costs vary widely by state, sample and partner.", sm=True),
    ]),

    # ===================== SECTION 05 =====================
    DIV("05", "Five", "Sampling logic"),

    S("Vocabulary", "Population, frame, sample and unit", [
        TC([TERM("Target population", "Everyone the question is about: all girls aged "
                 "14&ndash;16 in rural Uttar Pradesh."),
            TERM("Sampling frame", "The list you actually draw from: villages in the Census "
                 "2011 directory, enrolment registers, voter rolls.")],
           [TERM("Sampling unit", "What you select at each stage: villages, then households, "
                 "then a person."),
            TERM("Coverage error", "The gap between population and frame. Anyone missing from "
                 "the list can never be sampled.")]),
        B("Frames age. Both the PLFS sample design and ASER report drawing on the <strong>Census "
          "2011</strong> frame of villages (MoSPI, 14 May 2025; ASER Centre, 2025). As of October "
          "2026 that frame is fifteen years old, and the next Census, with reference date "
          "1 March 2027, will replace it. New settlements and growing peri-urban areas are the "
          "places an old frame tends to miss."),
        H("amber", "Before sampling, ask who is not on the list: migrants, people in "
          "unrecognised settlements, the homeless. Describe them in the limitations even if you "
          "cannot reach them."),
    ]),

    S("Two logics", "Probability and non-probability sampling answer different questions", [
        TC([P("cyan", "Probability sampling",
              "Every unit in the frame has a known, non-zero chance of selection. This lets you "
              "estimate population values and their margin of error. Needed for any claim like "
              "'34 per cent of households in the district'."),
            BL(["Simple random", "Systematic (every k-th on a list)", "Stratified",
                "Cluster and multistage"], "cyan")],
           [P("green", "Non-probability sampling",
              "Units are chosen by judgement, convenience or referral. Cannot estimate "
              "prevalence, but is the right tool for finding information-rich cases, "
              "reaching hidden groups or exploring a process."),
            BL(["Purposive (chosen for a reason you state)", "Snowball (referral)",
                "Quota", "Convenience (avoid if you can)"], "green")]),
        H("red", "The common error is reporting percentages from a convenience sample as if they "
          "described a population. Twenty interviews at a health centre say nothing about the "
          "share of women in the block who use it."),
    ]),

    S("Multistage designs", "Stratify for precision, cluster for cost", [
        B("National surveys almost never draw households directly. They select <strong>first "
          "stage units</strong> such as villages or urban blocks, within strata, and then "
          "households within those. The HCES 2022-23 is a clear example."),
        TC([ST([C("8,723", "Villages surveyed", "cyan", "MoSPI, HCES 2022-23 Fact Sheet"),
                C("6,115", "Urban blocks surveyed", "cyan", "MoSPI, HCES 2022-23"),
                C("2,61,746", "Households (1,55,014 rural, 1,06,732 urban)", "green",
                  "MoSPI, HCES 2022-23")], cols=1)],
           [B("Within each selected village or block, households were grouped into three "
              "categories (by land possessed in rural areas, by car ownership in urban areas), "
              "and 18 households were selected with proportional representation from the "
              "three, by simple random sampling without replacement (MoSPI fact sheet).", sm=True),
            H("indigo", "Stratification makes sure every group is represented and usually "
              "improves precision. Clustering saves travel cost but makes each extra household "
              "worth less, because neighbours resemble each other.")], ratio="a23"),
    ]),

    S("A simple design", "ASER's sample: 30 villages, 20 households, every child", [
        TC([FL(["DISTRICT: every rural district is a stratum",
                "VILLAGES: 30 randomly selected per district from the Census 2011 frame",
                "HOUSEHOLDS: 20 randomly selected per village",
                "CHILDREN: all aged 3&ndash;16 surveyed, all aged 5&ndash;16 assessed"])],
           [B("This is the design ASER Centre describes in its 2024 national release. Its "
              "simplicity is deliberate. District partners, including colleges, NGOs and "
              "District Institutes of Education and Training, can run it, and the same procedure every round makes trends comparable.", sm=True),
            B("Notice the trade-off: 600 households per district is enough for district "
              "estimates of headline indicators, and too few for reliable estimates for small "
              "subgroups within a district.", sm=True)], ratio="a23"),
        H("cyan", "When you design your own sample, write it out as plainly as this. If you "
          "cannot describe it in four steps, enumerators will not follow it in the field."),
    ]),

    S("How many", "Sample size: the arithmetic and the judgement", [
        TC([B("For a proportion from a simple random sample, a standard formula is "
              "<strong>n = z&sup2; p(1&minus;p) / e&sup2;</strong>, where z is 1.96 for 95 per "
              "cent confidence, p is your best guess of the proportion and e is the margin of "
              "error you can accept. With p = 0.5 and e = 0.05, n = 385.", sm=True),
            B("Clustering inflates this. Multiply by the <strong>design effect</strong>, which you "
              "estimate from a similar earlier survey (the table uses 2 for illustration), and "
              "then divide by the expected response rate.", sm=True)],
           [T(["Margin of error", "n (simple random)", "n with design effect 2"],
              [["&plusmn;10 points", "97", "194"],
               ["&plusmn;5 points", "385", "770"],
               ["&plusmn;3 points", "1,068", "2,136"]]),
            B("Illustrative calculation, p = 0.5, 95% confidence.", sm=True)]),
        H("amber", "Every subgroup you want to report separately needs its own adequate sample. "
          "Four districts, two sexes and three caste groups multiply quickly. Evaluations "
          "also need power calculations; see " + L("impact-eval.html", "Impact Evaluation") + "."),
    ]),

    S("A redesign", "PLFS 2025: a bigger sample and a new design", [
        TC([{"t": "chart", "canvas": "plfsChart", "type": "bar",
             "title": "PLFS sample households per year, before and after the January 2025 redesign",
             "source": "MoSPI, Press Note on PLFS Changes in 2025, 14 May 2025",
             "data": {"labels": ["Up to Dec 2024", "From Jan 2025"],
                      "datasets": [{"label": "Households", "data": [102400, 272304],
                                    "backgroundColor": ["#94A3B8", "#0EA5E9"]}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, title:{display:true,text:'Households'} } } }"}}],
           [B("From January 2025 the PLFS moved from 12,800 to 22,692 first stage units, from "
              "8 to 12 households per unit, and to around 2,72,304 households, about 2.65 times "
              "the earlier sample. The district became the basic stratum for most of the "
              "country.", sm=True),
            H("red", "MoSPI's own note tells users to consider these changes when comparing "
              "post-January 2025 results with earlier PLFS publications. A change in design is "
              "a break in the series, however good the new design is.")]),
        B("The note scheduled the first monthly bulletin, for April 2025, for release in May "
          "2025, and the first rural and urban quarterly bulletin for August 2025.", sm=True),
    ]),

    S("Non-response and weights", "Who did not answer, and how weights correct for design", [
        TC([{"t": "chart", "canvas": "nfhsChart", "type": "bar",
             "title": "NFHS-5 response rates (%)",
             "source": "IIPS &amp; ICF, NFHS-5 India Report, 2021",
             "data": {"labels": ["Households", "Women 15&ndash;49", "Men 15&ndash;54"],
                      "datasets": [{"label": "Response rate", "data": [98, 97, 92],
                                    "backgroundColor": ["#0EA5E9", "#10B981", "#6366F1"]}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:80, max:100 } } }"}}],
           [B("NFHS-5 selected 664,972 households, found 653,144 occupied and interviewed "
              "636,699. It completed 724,115 interviews with eligible women and 101,839 with "
              "eligible men. High rates overall, and the report notes that men responded less "
              "often than women in every state and union territory.", sm=True),
            B("<strong>Sampling weights</strong> correct for unequal chances of selection built "
              "into the design. Non-response adjustments correct, partly, for who refused or "
              "was absent. Unweighted analysis of a stratified national survey gives wrong "
              "national figures.", sm=True)]),
        H("amber", "Always report your response rate, and compare responders with non-responders "
          "on anything you know about both."),
    ]),

    S("Qualitative samples", "Purposive samples and saturation", [
        TC([B("Qualitative studies choose participants for what they can teach about the "
              "question: typical cases, extreme cases, cases that vary on a key factor. The "
              "usual stopping rule is <strong>saturation</strong>, the point where new "
              "interviews stop producing new themes.", sm=True),
            ST([C("12", "Interviews by which saturation occurred, out of 60 analysed", "green",
                  "Guest, Bunce &amp; Johnson, <em>Field Methods</em>, 2006")], cols=1)],
           [B("Guest, Bunce and Johnson analysed sixty in-depth interviews with women in two "
              "West African countries and found that saturation occurred within the first "
              "twelve interviews, with basic elements of the main themes present after six.",
              sm=True),
            H("red", "Their interviews were with one group of women answering one set of "
              "questions. A study comparing Dalit and Savarna women across three states needs saturation within "
              "each group you compare, which means many more interviews."),
            B("Plan a range, monitor new codes as you go, and report how you judged "
              "saturation. More in " + L("qual-methods.html", "Qualitative Methods") + ".",
              sm=True)]),
    ]),

    # ===================== SECTION 06 =====================
    DIV("06", "Six", "Measurement: validity and reliability"),

    S("Concept to number", "Every measure is a chain from idea to data", [
        FL(["CONCEPT: food insecurity",
            "DIMENSION: anxiety, reduced quality, reduced quantity",
            "INDICATOR: share of households reporting skipped meals",
            "ITEM: 'In the last 30 days, did anyone in the household skip a meal because there "
            "was not enough food?'",
            "VALUE: yes / no, per household"]),
        TC([B("Each link can break. The concept may have dimensions the indicator ignores. The "
              "item may be understood differently in Odia and in English. The reference period "
              "may fall in a lean or a harvest month. The respondent may not know about other "
              "members' meals.", sm=True)],
           [B("Measurement quality is assessed with two ideas. <strong>Reliability</strong> "
              "asks whether the measure gives consistent results. <strong>Validity</strong> "
              "asks whether it measures the concept you intend. They are separate properties, "
              "and both are needed.", sm=True)]),
        H("cyan", "Use an established, tested instrument wherever one exists for your concept. "
          "It saves pretesting effort and makes your results comparable with others'."),
    ]),

    S("Two properties", "Reliability and validity: the dartboard picture", [
        TC([P("amber", "Reliable but invalid",
              "Darts land tightly together, away from the bullseye. A weighing scale that always "
              "reads 2 kg heavy. Consistent and wrong. More data will not help."),
            P("red", "Neither",
              "Darts scattered and off-centre. A question so ambiguous that answers vary with "
              "the enumerator's mood and also miss the concept.")],
           [P("indigo", "Valid on average but unreliable",
              "Darts scattered around the bullseye. Unbiased but noisy: individual readings "
              "are unreliable, averages over many respondents can still be useful."),
            P("green", "Reliable and valid",
              "Darts tightly clustered on the bullseye. The goal, achieved by careful design, "
              "testing and training.")]),
        H("cyan", "A measure cannot be more valid than it is reliable. If a child's reading level "
          "changes depending on which enumerator tests her, the score cannot track her true "
          "reading ability well. Fix reliability first, through clear protocols and training."),
    ]),

    S("Kinds of validity", "Four ways to check that a measure measures the right thing", [
        T(["Type", "Question", "How to check", "Example"],
          [["Face", "Does it look right to users and respondents?", "Review with field staff and "
            "community members", "Women confirm the decision-making items cover real decisions"],
           ["Content", "Does it cover all parts of the concept?", "Expert review against a "
            "definition", "A wealth index that leaves out land in a farming area fails"],
           ["Criterion", "Does it agree with a trusted benchmark?", "Compare with a gold "
            "standard, now or later", "Self-reported vaccination against health cards"],
           ["Construct", "Does it behave as theory predicts?", "Check expected correlations "
            "and differences", "A depression scale relates to functioning as expected"]]),
        H("amber", "Validity belongs to a measure used for a purpose in a population. A scale "
          "validated in urban Delhi needs fresh checking among Santali speakers in Jharkhand. "
          "Translation alone does not carry validity across."),
        B("Item Response Theory and factor analysis give formal tools for construct validity: "
          + L("irt-basics.html", "Item Response Theory") + ", "
          + L("sem.html", "Structural Equation Modelling") + ".", sm=True),
    ], compact=True),

    S("Kinds of reliability", "Three ways to check consistency", [
        TC([TERM("Test-retest", "Ask the same respondents again after a short gap. Answers that "
                 "change a lot, when nothing real changed, signal an unreliable item."),
            TERM("Inter-rater", "Two coders or enumerators score the same case independently. "
                 "Agreement, often summarised with Cohen's kappa, shows whether the protocol is "
                 "clear enough."),
            TERM("Internal consistency", "Items meant to tap one concept should move together. "
                 "Cronbach's coefficient alpha (<em>Psychometrika</em>, 1951) summarises this.")],
           [B("<strong>In the field:</strong> back-checks, where a supervisor re-asks a few "
              "questions of a random subset of households, are a practical test-retest and "
              "catch fabricated interviews.", sm=True),
            B("<strong>In qualitative coding:</strong> double-coding a sample of transcripts and "
              "discussing disagreements sharpens the codebook. The aim is a shared "
              "understanding of each code, and the agreement score is one sign of it.", sm=True),
            H("red", "A very high alpha can mean redundant items asking the same thing five "
              "ways. Treat it as one piece of evidence.")]),
    ]),

    S("Reference periods", "The recall period is part of the measure", [
        TC([{"t": "chart", "canvas": "mpceChart", "type": "line",
             "title": "Average MPCE, India, nominal rupees",
             "source": "MoSPI, HCES 2022-23 Fact Sheet, Statement 2 (NSS 55th, 61st, 66th, 68th "
                       "rounds and HCES 2022-23)",
             "data": {"labels": ["1999-00", "2004-05", "2009-10", "2011-12", "2022-23"],
                      "datasets": [
                          {"label": "Rural", "data": [486, 579, 1054, 1430, 3773],
                           "borderColor": "#10B981", "backgroundColor": "rgba(16,185,129,0.1)",
                           "tension": 0.2},
                          {"label": "Urban", "data": [855, 1105, 1984, 2630, 6459],
                           "borderColor": "#0EA5E9", "backgroundColor": "rgba(14,165,233,0.1)",
                           "tension": 0.2}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ title:{display:true,text:'\\u20B9 per person per month'} } } }"}}],
           [B("The fact sheet notes that 1999-00 and 2004-05 use the Mixed Reference Period, "
              "while 2009-10, 2011-12 and 2022-23 use the Modified Mixed Reference Period. "
              "Different recall periods for different items produce different totals from the "
              "same households.", sm=True),
            H("red", "These are nominal values and the method changes along the series. The "
              "line cannot be read as real growth in living standards without adjusting for "
              "prices and for the change in reference period.")]),
    ]),

    S("Design against bias", "HCES 2022-23: designing out order and fatigue effects", [
        B("Questionnaire design can move results. The 2022-23 consumption survey made two "
          "design changes worth studying, both documented in the MoSPI fact sheet."),
        TC([P("cyan", "Three questionnaires, all six orders",
              "Items were split into three questionnaires (food, consumables and services, "
              "durable goods). All six possible orderings of the three were used across "
              "households, to eliminate bias from any particular sequence."),
            P("cyan", "Multiple visits",
              "The three questionnaires were canvassed in three separate monthly visits in a "
              "quarter, departing from the usual practice of a single visit.")],
           [B("Why it matters: respondents tire. Items asked late in a long interview get "
              "shorter, less careful answers. If food always came first, any fatigue effect "
              "would fall entirely on durables. Rotating the order spreads it evenly and makes "
              "it measurable.", sm=True),
            H("amber", "The same changes are one reason 2022-23 estimates need care when "
              "compared with 2011-12. Better design and a clean series can pull in opposite "
              "directions.")]),
    ]),

    S("Response errors", "What respondents and interviewers add to the data", [
        TC([BL(["<strong>Recall error:</strong> people forget, and they pull events into or out "
                "of the reference period ('telescoping')",
                "<strong>Social desirability:</strong> under-reporting of domestic violence, "
                "over-reporting of handwashing or voting",
                "<strong>Acquiescence:</strong> a tendency to agree, stronger where the "
                "interviewer has higher status",
                "<strong>Proxy reporting:</strong> one member answering for others, often a man "
                "for women's work"], "amber")],
           [BL(["Use short, concrete reference periods for frequent events",
                "Ask sensitive items privately, or by self-completion on a tablet",
                "Match interviewer and respondent sex for sensitive topics",
                "Interview each person directly where the concept is individual",
                "Pretest with cognitive interviews: ask respondents what they understood"],
               "green")]),
        H("cyan", "Interviewer effects are measurable: randomise interviewer assignment where "
          "you can, record interviewer IDs, and check whether answers cluster by interviewer. "
          "More in " + L("survey-design.html", "Survey Design") + "."),
    ]),

    S("Qualitative rigour", "Trustworthiness: quality criteria for qualitative work", [
        B("Qualitative research is judged by parallel criteria. Lincoln and Guba (<em>Naturalistic "
          "Inquiry</em>, 1985) proposed four, still widely used to plan and review studies."),
        T(["Criterion", "Parallel to", "Practices that support it"],
          [["Credibility", "Internal validity", "Prolonged engagement, triangulation, checking "
            "interpretations with participants"],
           ["Transferability", "External validity", "Thick description of setting and "
            "participants so readers can judge fit"],
           ["Dependability", "Reliability", "An audit trail of decisions, a stable and "
            "documented coding process"],
           ["Confirmability", "Objectivity", "Reflexive notes, showing how quotes support "
            "themes"]]),
        H("green", "Write these practices into the protocol at the start. They are hard to "
          "reconstruct afterwards. The COREQ checklist (Tong, Sainsbury and Craig, 2007) lists "
          "32 items reviewers use to check interview and focus group reports."),
    ], compact=True),

    # ===================== SECTION 07 =====================
    DIV("07", "Seven", "Qualitative, quantitative and mixed"),

    S("Strengths", "What each approach does best", [
        T(["", "Qualitative", "Quantitative"],
          [["Best at", "Meanings, processes, unexpected factors", "Prevalence, magnitude, "
            "comparison, change over time"],
           ["Typical sample", "Small, purposive, information-rich", "Large, probability-based"],
           ["Data", "Words, observations, images", "Numbers from structured instruments"],
           ["Analysis", "Coding, themes, interpretation", "Estimation, tests, models"],
           ["Generalises to", "Theory and similar contexts, by argument", "A defined population, "
            "by statistics"],
           ["Weak at", "Saying how common something is", "Explaining why, finding what was not "
            "asked"]]),
        H("cyan", "Choose by the question, using the table as a guide. Many questions need both, "
          "which is the case for mixed methods later in this section."),
        B("The labels describe data and logic more than people. Good quantitative researchers "
          "do fieldwork and read transcripts, and good qualitative researchers count when "
          "counting helps.", sm=True),
    ], compact=True),

    S("Qualitative designs", "Qualitative designs at a glance", [
        TC([P("cyan", "Ethnography",
              "Extended immersion in a setting, through observation and conversation. Good for "
              "how a ration shop or a panchayat meeting actually works."),
            P("cyan", "Case study",
              "Intensive study of one or a few bounded cases, often with mixed sources. Good "
              "for complex programmes and policy processes."),
            P("cyan", "Grounded theory",
              "Builds theory from data through constant comparison and theoretical sampling.")],
           [P("green", "Phenomenology",
              "Describes the lived experience of a phenomenon, such as stigma after a TB "
              "diagnosis, from those who live it."),
            P("green", "Narrative and life history",
              "Follows individual stories through time, revealing turning points such as "
              "migration or marriage."),
            B("Methods of data collection (interviews, focus groups, observation, visual and "
              "participatory tools) cut across these designs. Depth: "
              + L("qual-methods.html", "Qualitative Methods") + ", "
              + L("visual-eth.html", "Visual Ethnography") + ", "
              + L("qda-software.html", "Qualitative Analysis Software") + ".", sm=True)]),
    ]),

    S("Quantitative designs", "Quantitative designs at a glance", [
        TC([P("indigo", "Sample surveys",
              "Structured questionnaires to a probability sample. The workhorse of description; "
              "NFHS, PLFS, HCES and ASER are all surveys."),
            P("indigo", "Experiments",
              "Assignment by chance to compare outcomes. Lab, field and survey experiments "
              "(for example, randomising question wording) all count."),
            P("indigo", "Secondary analysis",
              "Analysing data someone else collected. Cheapest per observation and often the "
              "most representative. Section 08.")],
           [P("amber", "Administrative data",
              "Records kept for running programmes: school enrolment, scheme payments, health "
              "management information. Large and timely, but shaped by what officials need to "
              "report."),
            P("amber", "Modelling and simulation",
              "Using estimated relationships to project scenarios, such as the cost of "
              "expanding a scheme."),
            B("Depth: " + L("quant-methods.html", "Quantitative Methods") + ", "
              + L("survey-design.html", "Survey Design") + ", "
              + L("econometrics-101.html", "Econometrics") + ", "
              + L("stats-without-code.html", "Statistics Without Code") + ".", sm=True)]),
    ]),

    S("Mixed designs", "Three core mixed methods designs", [
        B("Mixed methods research combines qualitative and quantitative strands and integrates "
          "them, which is where its value lies. Creswell and Plano Clark describe three core designs, "
          "distinguished by timing and purpose."),
        T(["Design", "Sequence", "Purpose", "Illustrative use"],
          [["Convergent", "Both strands at the same time, merged at analysis", "Compare and "
            "corroborate", "Household survey on school costs alongside interviews with "
            "parents"],
           ["Explanatory sequential", "Quantitative first, then qualitative", "Explain "
            "surprising numbers", "Survey finds one block with low dropout; interviews "
            "find out why"],
           ["Exploratory sequential", "Qualitative first, then quantitative", "Build or adapt "
            "an instrument", "Interviews identify local forms of women's work, then survey "
            "items are written"]]),
        H("indigo", "Decide the design and the integration point at the protocol stage. More in "
          + L("mixed-methods.html", "Mixed Methods") + "."),
    ], compact=True),

    S("Integration", "Integration is where mixed methods earns its cost", [
        TC([B("Running a survey and some focus groups and reporting them in separate chapters is "
              "two studies under one cover. Integration means each strand changes what you "
              "conclude from the other.", sm=True),
            BL(["<strong>Building:</strong> qualitative findings shape the survey instrument",
                "<strong>Explaining:</strong> interviews interpret a statistical pattern",
                "<strong>Merging:</strong> results compared side by side in a joint display",
                "<strong>Embedding:</strong> a qualitative strand inside a trial explains "
                "how the programme was received"], "cyan")],
           [P("green", "A joint display (illustrative)",
              "Rows are themes or indicators. Columns show the survey estimate, what interviews "
              "said and whether they agree, extend or contradict. Contradictions are findings: "
              "if 80 per cent report attending meetings and interviews say women sit silently "
              "at the back, both are true and the gap is the result."),
            H("amber", "Budget time for integration. It is usually the step squeezed out when "
              "fieldwork overruns.")]),
    ]),

    S("Participatory approaches", "Participatory and community-based research", [
        TC([B("Participatory approaches share control of the research with the people it "
              "concerns: framing questions, collecting data, interpreting results and deciding "
              "what to do with them. Their South Asian roots run through participatory rural "
              "appraisal, social audits and community monitoring of public services.", sm=True),
            BL(["Social and resource mapping", "Seasonal calendars and timelines",
                "Wealth ranking by community members", "Community scorecards for services"],
               "green")],
           [P("amber", "Strengths and cautions",
              "Brings in local knowledge and builds ownership of findings. But participation "
              "can be captured by the powerful: a village map drawn in front of the sarpanch "
              "may leave out a Dalit hamlet. Facilitation, who is in the room and how "
              "disagreement is recorded all matter."),
            B("Depth: " + L("participatory-methods.html", "Participatory Methods") + " and "
              + L("community-dev.html", "Community Development") + ".", sm=True)]),
        H("cyan", "Participatory tools can feed into rigorous designs. Community wealth rankings "
          "have been used to build sampling frames where no list of the poor exists."),
    ]),

    S("Choosing the mix", "A decision table for choosing the approach", [
        T(["If you need to", "Lead with", "Add", "Watch for"],
          [["Estimate how common something is", "Probability survey", "Qualitative pretesting",
            "Coverage of the frame"],
           ["Understand why a pattern exists", "Qualitative interviews or case studies",
            "Survey data to locate cases", "Choosing cases that confirm your view"],
           ["Build a measure for a new concept", "Exploratory qualitative work",
            "Survey to test the measure", "Skipping validation"],
           ["Judge whether a programme worked", "Comparison design (Section 04)",
            "Process evaluation, interviews", "Treating monitoring data as impact"],
           ["Give communities a voice in priorities", "Participatory methods",
            "Survey to check representativeness", "Elite capture of the process"]]),
        H("green", "When in doubt, ask which strand the decision-maker will read first, and make "
          "sure that strand can carry the main answer on its own."),
    ], compact=True),

    # ===================== SECTION 08 =====================
    DIV("08", "Eight", "Secondary data in South Asia"),

    S("Start here", "Check existing data before collecting your own", [
        TC([B("South Asia has some of the largest household surveys in the world, many free to "
              "download for research. Analysing them before a new survey saves money, reduces "
              "the burden on respondents and gives you a benchmark for your own figures.", sm=True),
            BL(["Can the question be answered from NFHS, PLFS, HCES, Census, ASER, DHS or "
                "administrative data?",
                "If partly, which piece is missing, and can a small new study fill only that?",
                "Is the official figure available for your district, or only the state?",
                "Is it recent enough for the decision at hand?"], "cyan")],
           [P("green", "Uses",
              "Context and baseline figures; choosing study sites; sample size inputs such as "
              "prevalence and design effects; benchmarking your own survey; and many complete "
              "studies built entirely on secondary data."),
            P("amber", "Limits",
              "Someone else chose the questions, the definitions and the timing. You inherit "
              "their decisions and must read their documentation in full.")]),
        H("indigo", "The ICMR 2017 guidelines list research on publicly available data among "
          "examples of less than minimal risk. Your ethics committee still decides the review "
          "type (Section 09)."),
    ]),

    S("India's core sources", "India's main household data sources", [
        T(["Source", "Run by", "Covers", "Latest round, as of Oct 2026"],
          [["NFHS", "IIPS for the Ministry of Health and Family Welfare", "Population, health, "
            "nutrition, women's status", "NFHS-6, 2023-24; fact sheets released May 2026"],
           ["PLFS", "National Statistics Office, MoSPI", "Employment, unemployment, wages",
            "Redesigned Jan 2025; monthly, quarterly and calendar-year annual results"],
           ["HCES", "National Statistics Office, MoSPI", "Consumption, inequality, CPI weights",
            "Back-to-back rounds, 2022-23 and 2023-24"],
           ["Census", "Registrar General and Census Commissioner", "Full count of population "
            "and housing", "2011; next has reference date 1 March 2027 and includes caste"],
           ["ASER", "ASER Centre (Pratham)", "Rural children's schooling and basic learning",
            "ASER 2024, released January 2025"]]),
        H("cyan", "MoSPI publishes unit-level survey data through its microdata portal "
          "(microdata.gov.in). NFHS data are distributed through The DHS Program as India's "
          "DHS round, after free registration."),
    ], compact=True),

    S("NFHS-5", "NFHS-5 in numbers", [
        ST([C("636,699", "Households interviewed", "cyan", "IIPS &amp; ICF, NFHS-5 India Report, 2021"),
            C("724,115", "Women aged 15&ndash;49 interviewed", "green", "NFHS-5 India Report"),
            C("101,839", "Men aged 15&ndash;54 interviewed", "indigo", "NFHS-5 India Report"),
            C("707", "Districts, as on March 2017", "amber", "NFHS-5 India Report")], cols=4),
        TC([B("Fieldwork ran in two phases: 17 June 2019 to 30 January 2020, and 2 January 2020 "
              "to 30 April 2021, using 1,061 field teams from 17 field agencies. The second "
              "phase was interrupted by the COVID-19 pandemic.", sm=True)],
           [H("amber", "Two practical consequences. States were surveyed at different times, "
              "some before and some during the pandemic, which matters when comparing them. And "
              "districts are those of March 2017, so districts created since need mapping back "
              "to their parent district.")]),
        B("Use the sampling weights and the design variables (strata and clusters) in every NFHS "
          "estimate. The India report describes the sample design in an appendix. NFHS-5 is "
          "shown here because its full India report documents the design; the NFHS-6 (2023-24) "
          "fact sheets followed in May 2026 (IIPS, 2026).", sm=True),
    ]),

    S("PLFS", "Using PLFS: frameworks, periods and breaks", [
        TC([TERM("Usual status (ps+ss)", "Activity status based on the last 365 days, combining "
                 "principal and subsidiary activity."),
            TERM("Current weekly status (CWS)", "Activity status based on the last seven days "
                 "before the survey."),
            B("Both definitions from MoSPI's press note of 14 May 2025.", sm=True)],
           [BL(["PLFS was launched in 2017. Seven annual reports covered July 2017 to June 2024",
                "Twenty-five quarterly bulletins covered urban areas for quarters ending "
                "December 2018 to December 2024",
                "From 2025, annual results follow the calendar year, January to December",
                "From the April&ndash;June 2025 quarter, quarterly results cover rural and "
                "urban areas"], "cyan"),
            H("red", "If you build a time series across 2024 and 2025, mark the break, "
              "and avoid reading the step between the two designs as a labour market change.")]),
        H("indigo", "Concepts of work and how women's work is undercounted: "
          + L("work-labour-livelihoods.html", "Work, Labour &amp; Livelihoods") + "."),
    ]),

    S("The region", "Comparable sources across South Asia", [
        T(["Country", "Survey", "Year", "Households", "Source"],
          [["Bangladesh", "Demographic and Health Survey (NIPORT)", "2022", "30,018",
            "The DHS Program survey listing"],
           ["Bangladesh", "Household Income and Expenditure Survey (BBS)", "2022",
            "14,400", "BBS, HIES 2022 Final Report"],
           ["Nepal", "Demographic and Health Survey (New ERA)", "2022", "13,786",
            "The DHS Program survey listing"],
           ["Nepal", "Living Standards Survey IV (NSO)", "2022-23", "9,600",
            "NSO Nepal microdata catalogue"],
           ["India", "NFHS-5 (IIPS)", "2019-21", "636,699", "NFHS-5 India Report"]]),
        TC([B("DHS surveys share a core questionnaire across countries, which makes cross-country "
              "comparison of health and nutrition indicators possible with care.", sm=True)],
           [B("Nepal's NLSS-IV ran July 2022 to June 2023 to capture seasonal variation, was "
              "drawn from the 2021 census frame, and had World Bank technical support.", sm=True)]),
    ], compact=True),

    S("Getting the data", "How to obtain and read microdata properly", [
        TC([FL(["FIND: the catalogue entry and the survey report",
                "REGISTER: DHS, MoSPI and NSO Nepal need a short account and a project "
                "description",
                "READ: the questionnaire, interviewer manual and sampling appendix before any "
                "analysis",
                "REPRODUCE: one published table exactly before computing anything new"])],
           [P("cyan", "The reproduction test",
              "If you cannot reproduce the official estimate of, say, the state unemployment "
              "rate from the unit-level file, something is wrong in your weights, filters or "
              "definitions. Find it before you report a new number."),
            P("green", "LSMS-type surveys",
              "The World Bank's Living Standards Measurement Study supports multi-topic "
              "household surveys such as Nepal's NLSS, with documentation and data in its "
              "microdata library.")], ratio="a23"),
        H("amber", "Keep a log of every download: file name, version, date and source page. "
          "Survey files are revised, and a reviewer will ask which version you used."),
    ]),

    S("Pitfalls", "Seven common errors with secondary data", [
        TC([BL(["<strong>Ignoring weights:</strong> unweighted national estimates are wrong "
                "estimates",
                "<strong>Ignoring the design:</strong> standard errors without strata and "
                "clusters are too small",
                "<strong>Mixing definitions:</strong> usual status in one year, CWS in "
                "another",
                "<strong>Crossing a methodological break</strong> as if it were a trend"],
               "red")],
           [BL(["<strong>Boundary changes:</strong> new districts and states need a "
                "consistent geography across rounds",
                "<strong>Subgroups too small:</strong> a district-level figure for a small "
                "caste group may rest on a handful of cases",
                "<strong>Treating survey years as calendar years:</strong> 2019-21 is a "
                "fieldwork span"], "red")]),
        H("cyan", "Report the unweighted sample size behind every estimate you publish, and "
          "suppress or flag estimates resting on very few cases. Most statistical offices do "
          "both for exactly this reason."),
        B("Exploring a dataset systematically: "
          + L("eda-hhs.html", "Exploratory Data Analysis") + ".", sm=True),
    ]),

    S("Law and secondary data", "What Indian law says about statistical data", [
        TC([P("indigo", "Collection of Statistics Act, 2008 (No. 7 of 2009)",
              "Section 9 restricts who may see information schedules and bars publishing "
              "answers without suppressing the identity of informants. Section 9(4) requires "
              "published statistics to be arranged so no informant can be identified, "
              "<em>even through the process of elimination</em>, unless the informant consented "
              "or the identification could not reasonably have been foreseen."),
            P("indigo", "Section 11 of the same Act",
              "Allows the appropriate Government to disclose individual schedules for bona "
              "fide research or statistical purposes, if names and addresses are deleted, "
              "users declare the research purpose and the Government is satisfied the "
              "schedules will stay secure.")],
           [P("green", "DPDP Act, 2023, section 17(2)(b)",
              "The Act does not apply to processing of personal data necessary for research, "
              "archiving or statistical purposes, if the data is not used to take any decision "
              "specific to a Data Principal and the processing follows prescribed standards. "
              "Section 17 and Rule 16 of the DPDP Rules 2025, which sets those standards, apply from "
              "13 May 2027 (G.S.R. 843(E); Rule 1(4))."),
            H("amber", "The exemption has conditions. Collecting your own personal data for a "
              "project that also delivers services to named people may fall outside it.")]),
        B("Detail: " + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act") + ".",
          sm=True),
    ]),

    # ===================== SECTION 09 =====================
    DIV("09", "Nine", "Ethics, consent and the law"),

    S("Why ethics is method", "Ethics is part of research design", [
        TC([B("Ethical review is often treated as a form to clear before fieldwork. The "
              "principles behind it are design principles. They decide whom you may sample, "
              "what you may ask, how you record answers and what you owe participants "
              "afterwards.", sm=True),
            P("cyan", "Belmont Report, 1979 (United States)",
              "Set out three basic principles for research with human subjects: respect for "
              "persons, beneficence and justice. ICMR's 2017 guidelines cite it in their "
              "history of research ethics.")],
           [P("green", "ICMR 2017: four basic principles",
              "Respect for persons (autonomy), beneficence, non-maleficence and justice, "
              "expanded into 12 general principles that apply to all biomedical, social and "
              "behavioural science research for health involving human participants, their "
              "biological material and data."),
            P("amber", "Declaration of Helsinki",
              "The World Medical Association's statement for medical research. Its latest "
              "revision was adopted at the 75th General Assembly in Helsinki, Finland, in "
              "October 2024.")]),
        B("Source: " + ICMR + ", Section 1; WMA website.", sm=True),
    ]),

    S("ICMR 2017", "India's reference guidelines for research ethics", [
        ST([C("2017", "Current edition, issued by ICMR", "cyan", ICMR),
            C("12", "Sections in the guidelines", "green",
              "ICMR 2017, message from the chairperson of the advisory group"),
            C("12", "General principles in Section 1", "indigo", "ICMR 2017, Section 1.1")],
           cols=3),
        TC([B("The guidelines have a history. ICMR issued a policy statement in 1980, guidelines "
              "for biomedical research in 2000, a revision in 2006, and the present edition in "
              "2017, which added sections on responsible conduct, vulnerability, public health "
              "research, social and behavioural sciences research for health, and research in "
              "humanitarian emergencies.", sm=True)],
           [H("amber", "The stated scope is research for health. Development research outside "
              "health often goes to an institutional ethics committee that uses these "
              "guidelines as its reference. Check your own committee's terms of reference, "
              "and any funder or university rules that apply.")]),
        B("Section 9, on social and behavioural sciences research, is the part most "
          "development researchers should read in full.", sm=True),
    ]),

    S("Twelve principles", "The 12 general principles, in one line each", [
        T(["Principle", "In practice", "Principle", "In practice"],
          [["Essentiality", "Using human participants is necessary for the question",
            "Professional competence", "Qualified, trained people design and run it"],
           ["Voluntariness", "Free choice to join and to withdraw at any time",
            "Maximisation of benefit", "Designed to benefit participants or society"],
           ["Non-exploitation", "Fair selection; safeguards for vulnerable groups",
            "Institutional arrangements", "Institutions provide governance and support"],
           ["Social responsibility", "Avoid deepening social and historic divisions",
            "Transparency and accountability", "Plans and results made public; conflicts "
            "declared"],
           ["Privacy and confidentiality", "Identity and records protected",
            "Totality of responsibility", "Every stakeholder answers for their part"],
           ["Risk minimisation", "Risks reduced; care and compensation if harm occurs",
            "Environmental protection", "Protect the environment at all stages"]]),
        B("Paraphrased from " + ICMR + ", Section 1.1.1&ndash;1.1.12.", sm=True),
    ], compact=True),

    S("Risk and review", "Risk categories decide the type of review", [
        T(["Risk category (Table 2.1)", "Example from the guidelines", "Likely review (Table 4.2)"],
          [["Less than minimal", "Anonymous or non-identified data; publicly available data; "
            "meta-analysis", "Exemption from review"],
           ["Minimal", "Routine questioning or history taking, observation", "Expedited review"],
           ["Minor increase over minimal (low)", "Routine research on children and "
            "adolescents; persons unable to consent; use of personal identifiable data; "
            "social and psychological risks", "Usually full committee"],
           ["More than minimal (high)", "Interventional studies with drugs, devices or invasive "
            "procedures", "Full committee"]]),
        H("red", "Section 4.8.3: a researcher cannot decide that her or his own proposal is "
          "exempt or expedited. All proposals go to the ethics committee, which decides the "
          "review type case by case."),
        B("Box 9.1 warns that risks in social and behavioural research are hard to measure and "
          "change over time, so they can be mistaken for no or minimal risk.", sm=True),
    ], compact=True),

    S("Consent in the field", "Consent in social research: what ICMR asks for", [
        TC([P("cyan", "Gatekeepers do not replace individuals",
              "Permission from a community head or institution comes first, and individual "
              "consent is still required. Community traditions do not substitute for individual "
              "consent unless a waiver has been granted (Box 9.4)."),
            P("cyan", "Read refusal",
              "Power differences in India can make an explicit 'no' hard to say. Researchers "
              "should watch for body language, silence, monosyllabic replies or restlessness, "
              "and must not persist when they see them (Box 9.4).")],
           [P("green", "Relational autonomy",
              "Identity is shaped by caste, class, ethnicity and gender, so autonomy is "
              "understood in relation to social support and equality of opportunity. The "
              "committee may take account of a woman consulting her husband or family before "
              "consenting (Box 9.4)."),
            P("green", "Consent as a process",
              "In qualitative research consent is often dynamic and negotiable. When written "
              "consent is not possible, other means may be used and documented (9.2.12).")]),
        B("Source: " + ICMR + ", Section 9.", sm=True),
    ]),

    S("Waivers and deception", "When consent can be waived, and when deception is allowed", [
        TC([P("amber", "Waiver of consent (5.7, Box 5.2)",
              "The researcher may apply for a waiver if the research involves less than minimal "
              "risk and the waiver will not adversely affect participants' rights and welfare. "
              "Situations include research on anonymised data, retrospective de-identified "
              "studies, data available publicly, and certain public health studies and "
              "programme evaluations."),
            B("In social and behavioural research, the committee may also waive individual "
              "consent for research of important social value posing no more than minimal risk "
              "that would not be feasible otherwise, such as research on harmful practices "
              "(Box 9.4).", sm=True)],
           [P("red", "Deception (9.2.9)",
              "Any research using deception should undergo full committee review. It must pose "
              "no more than minimal risk, avoid harm to participants' welfare and safety, be "
              "impossible to conduct otherwise, and include a plan for debriefing where "
              "appropriate."),
            B("Mystery-client studies of clinics or offices, and audit studies sending matched "
              "applications, involve deception. Plan the review time.", sm=True)]),
        B("Source: " + ICMR + ".", sm=True),
    ]),

    S("Privacy law", "Privacy, data protection and the researcher", [
        T(["Instrument", "What it says", "What it means for a study"],
          [["<em>Justice K.S. Puttaswamy (Retd.) v Union of India</em> (2017)", "A nine-judge "
            "bench of the Supreme Court unanimously recognised a fundamental right to privacy, "
            "decided 24 August 2017", "Privacy is a constitutional interest. Collect only what "
            "the question needs"],
           ["DPDP Act 2023, s17(2)(b), with the DPDP Rules 2025, from 13 May 2027", "Research, archiving or "
            "statistical processing exempt if no decision specific to a person and prescribed "
            "standards met", "Keep research data separate from any service delivery records"],
           ["Collection of Statistics Act 2008, s9(4)", "No identification of informants, "
            "even by elimination", "Suppress small cells; remove indirect identifiers"],
           ["ICMR 2017, 1.1.5 and 9.2.7", "Privacy and confidentiality protected, with "
            "context-specific safeguards", "Plan storage, access, anonymisation and "
            "retention"]]),
        H("amber", "Indirect identifiers re-identify people in small villages: caste, "
          "occupation and household size together may point to one family. Anonymisation means "
          "removing revealing combinations of variables as well as names."),
    ], compact=True),

    S("Duty and safety", "Disclosure, support and the safety of field teams", [
        TC([P("red", "Duty to disclose (9.2.8)",
              "Researchers may learn facts dangerous to a participant or others, such as "
              "suicidal ideation. They have a responsibility to disclose to relevant persons or "
              "authorities to save life or prevent harm. If sensitive findings are likely, the "
              "protocol should say how they will be handled."),
            P("amber", "Participant support (9.2.10)",
              "Research on mental health, gender-based violence, social exclusion and "
              "discrimination needs support systems in place, such as counselling, "
              "rehabilitation services or police protection.")],
           [P("cyan", "Team safety (9.2.11)",
              "The safety of research teams is the responsibility of the institution, sponsors "
              "and local authorities, including training and insurance. Community advisory "
              "boards can help."),
            B("Safeguarding obligations towards children and vulnerable adults run alongside "
              "research ethics: " + L("safeguarding-psea.html", "Safeguarding &amp; PSEA") + ". "
              "Full treatment of ethics: " + L("research-ethics.html", "Research Ethics") + ".",
              sm=True),
            B("Source: " + ICMR + ", Section 9.2.", sm=True)]),
    ]),

    # ===================== SECTION 10 =====================
    DIV("10", "Ten", "Analysis plans and pre-registration"),

    S("Analysis plan", "Decide the analysis before you see the outcomes", [
        B("An analysis plan sets out, before outcome data are examined, how you will turn data "
          "into answers. It protects you from the temptation to try analyses until one looks "
          "interesting, and it tells readers which results were planned."),
        T(["Section of the plan", "Contents"],
          [["Questions and hypotheses", "Exactly as in the protocol, with expected direction"],
           ["Outcomes", "Primary and secondary outcomes, each with its operational definition"],
           ["Sample and data", "Inclusion rules, how missing data and outliers are handled"],
           ["Estimation", "Models, controls, weights, clustering of standard errors"],
           ["Subgroups", "Which subgroups, chosen in advance, and why"],
           ["Multiple outcomes", "How you will adjust for testing many outcomes"],
           ["Qualitative strand", "Coding approach, how themes link to the questions"]]),
        H("cyan", "A dated plan shared with a colleague or a registry is far better than a "
          "perfect plan written after the data arrive."),
    ], compact=True),

    S("Why it matters", "Evidence that many published findings do not replicate", [
        ST([C("97%", "Original psychology studies with significant results", "amber",
              "Open Science Collaboration, <em>Science</em>, 2015"),
            C("36%", "Replications with significant results", "red",
              "Open Science Collaboration, 2015"),
            C("100", "Studies replicated with high-powered designs", "indigo",
              "Open Science Collaboration, 2015")], cols=3),
        TC([B("The Open Science Collaboration replicated 100 experimental and correlational "
              "studies from three psychology journals. Replication effects were about half the "
              "size of the originals.", sm=True)],
           [B("Ioannidis set out one explanation in 2005 in <em>PLoS Medicine</em>, in an "
              "essay titled 'Why most published research findings are false': small studies, "
              "small effects, flexible designs and many tested relationships all lower the "
              "chance that a significant finding is true.", sm=True)]),
        H("amber", "Development economics has its own versions of the problem, which is why its "
          "registries appeared. Pre-registration is a cheap protection."),
    ]),

    S("Registries", "Where to register a study", [
        T(["Registry", "Who runs it", "Used for"],
          [["AEA RCT Registry", "American Economic Association; the AEA executive committee "
            "decided to establish it in April 2012", "Randomised trials in economics and social "
            "sciences"],
           ["RIDIE", "International Initiative for Impact Evaluation (3ie)", "Impact "
            "evaluations in low and middle income countries, experimental or not"],
           ["Clinical Trials Registry-India (CTRI)", "ICMR; launched 20 July 2007; "
            "registration made mandatory by CDSCO on 15 June 2009 for regulated trials",
            "Clinical and health trials in India"],
           ["Open Science Framework", "Center for Open Science", "Any study design, "
            "including qualitative and observational"]]),
        H("indigo", "ICMR's principle of transparency and accountability (1.1.10) asks that "
          "research plans and outcomes be made public through registries, "
          "reports and publications, while protecting participants' privacy."),
        B("Sources: AEA RCT Registry about page; RIDIE; " + ICMR + ", Section 3.7.", sm=True),
    ], compact=True),

    S("Promises and perils", "Pre-analysis plans: what they buy and what they cost", [
        B("Olken's 'Promises and Perils of Pre-Analysis Plans' (<em>Journal of Economic "
          "Perspectives</em>, 2015) is the standard short guide for development economists. Its "
          "framing is a trade-off."),
        TC([P("green", "Promises",
              "Credibility: readers can see which tests were planned. Discipline: fewer "
              "fishing expeditions across outcomes and subgroups. Clarity: the team agrees on "
              "definitions before data arrive, which also speeds the analysis."),
            BL(["Specify primary outcomes", "Fix the main specification",
                "State how you will handle multiple outcomes"], "green")],
           [P("amber", "Perils",
              "Plans cannot anticipate everything. Very detailed plans can lock in poor "
              "choices or make sensible adaptations look suspicious. Writing them takes time, "
              "and exploratory analysis still has value when labelled as such."),
            BL(["Report deviations openly", "Label exploratory results",
                "Keep the plan proportionate to the study"], "amber")]),
        H("cyan", "The working rule: pre-specify what matters most for credibility, and be "
          "transparent about everything else."),
    ]),

    S("Qualitative plans", "Planning a qualitative analysis without killing discovery", [
        TC([B("Qualitative research is meant to find what was not expected, so a rigid plan "
              "defeats its purpose. But a plan for the <em>process</em> of analysis adds "
              "credibility without fixing the findings.", sm=True),
            BL(["How transcripts will be prepared and translated",
                "Whether coding starts from a framework, from the data, or both",
                "Who codes, how disagreements are resolved",
                "How themes will be linked back to the research questions",
                "How negative cases will be sought and reported"], "cyan")],
           [P("green", "Illustrative plan entry",
              "'Two researchers fluent in Bhojpuri will code the first eight transcripts "
              "independently using a starting framework from the theory of change, meet to "
              "reconcile, then extend the codebook inductively. Memos recording each change to "
              "the codebook will be kept and summarised in the appendix.'"),
            B("Software can help organise this. See "
              + L("qda-software.html", "Qualitative Analysis Software") + ".", sm=True)]),
        H("amber", "Open Science Framework accepts qualitative pre-registrations, and some "
          "journals now publish registered reports for qualitative designs."),
    ]),

    S("Deviations", "Changing the plan transparently", [
        T(["Situation", "Acceptable response", "What to report"],
          [["Fieldwork disrupted (strike, flood, election)", "Revise sample or timing",
            "Original plan, change, date and reason"],
           ["An outcome measure failed in the field", "Drop or replace it", "Why it failed, "
            "and the replacement's definition"],
           ["A new question emerged from the data", "Analyse it as exploratory",
            "Clear label separating it from planned tests"],
           ["Planned model did not converge", "Use a simpler specification", "Both, with "
            "the reason"],
           ["Result disappointing", "Report it as planned", "Everything; null results are "
            "findings"]]),
        H("red", "Never revise the plan after seeing results and present the revision as the "
          "original. Registries keep timestamps for this reason."),
        B("A short 'deviations from the plan' table in the appendix is now common practice in "
          "development economics journals and evaluation reports.", sm=True),
    ], compact=True),

    # ===================== SECTION 11 =====================
    DIV("11", "Eleven", "Putting it to work"),

    S("Worked example 1", "Worked example: from a district problem to a question", [
        H("amber", "Illustrative case (hypothetical figures). A district education officer and an NGO partner want to "
          "understand why girls in three blocks do not move from class 8 to class 9."),
        TC([P("cyan", "Step 1: check existing data",
              "UDISE+ enrolment by school and grade gives transition rates by block. ASER "
              "district figures give learning levels. NFHS district fact sheets give context on age at "
              "marriage. Together they confirm the drop and locate it, but cannot explain it."),
            P("cyan", "Step 2: split the question",
              "Descriptive: what share of girls completing class 8 in 2025 enrolled in class 9, "
              "by block and distance band? Explanatory: how do girls and parents describe the "
              "decision?")],
           [P("green", "Step 3: choose a design",
              "Explanatory sequential mixed methods. First, a household survey of girls who "
              "completed class 8, sampled from school registers. Then interviews with girls "
              "and parents chosen from the survey to contrast those who continued and those who "
              "did not, within the same villages."),
            B("The design follows the decision: the officer can act on distance with transport "
              "or a new section, and on safety or marriage pressure with different tools.",
              sm=True)]),
    ]),

    S("Worked example 2", "Worked example: sample and measures", [
        TC([P("cyan", "Sample",
              "Frame: class 8 registers of all government and aided schools in the three "
              "blocks, which captures girls who reached class 8 and misses those who left "
              "earlier (state this). Stratify by block. Draw girls at random within schools. "
              "Target precision of &plusmn;5 points per block with a design effect of 2 gives "
              "about 770 per block before non-response."),
            P("cyan", "Interviews",
              "Purposive: about 12 to 15 girls who continued and 12 to 15 who did not, plus "
              "parents, across a mix of near and far villages. Monitor new themes and continue "
              "until saturation within each group.")],
           [P("green", "Measures",
              "Enrolment checked against the class 9 register as well as reported. Distance "
              "measured by GPS to the nearest secondary school. Household income through a "
              "short asset index validated against HCES-type items. Marriage expectations "
              "asked privately, by a female interviewer."),
            H("amber", "Each measure names its validity risk: reported enrolment is inflated by "
              "social desirability, so the register is the primary source.")]),
        B("All figures illustrative.", sm=True),
    ]),

    S("Worked example 3", "Worked example: ethics, data and analysis plan", [
        TC([P("indigo", "Ethics",
              "Minors are involved, so under ICMR Table 2.1 this is at least a minor increase "
              "over minimal risk. Submit to an institutional ethics committee. Parental "
              "consent plus the girl's own assent, given privately. Protocol for disclosures of "
              "child marriage plans or abuse, with named referral contacts."),
            P("indigo", "Data protection",
              "Collect names only for linkage to registers, store them separately from "
              "answers, and delete them after linkage. Publish block-level tables only, "
              "suppressing small cells.")],
           [P("green", "Analysis plan, registered before endline",
              "Primary outcome: class 9 enrolment from registers. Main comparison: distance "
              "bands, adjusting for income and caste group, standard errors clustered by "
              "village. Subgroups fixed in advance: block, caste group. Qualitative: framework "
              "coding from the theory of change, then inductive codes."),
            B("Registration on the Open Science Framework, with a dated plan, costs nothing and "
              "takes an afternoon.", sm=True)]),
        H("cyan", "Notice that every choice traces back to the question on the first slide of "
          "the example. That traceability is the mark of a sound protocol."),
    ]),

    S("Decision table", "A one-page design decision table", [
        T(["Your situation", "Design to consider", "Sample", "Ethics flag"],
          [["Need district prevalence; good recent survey exists", "Secondary analysis",
            "The survey's own, with weights", "Usually less than minimal risk"],
           ["Need prevalence; nothing exists", "New cross-sectional survey", "Multistage "
            "probability sample", "Minimal; more for sensitive topics"],
           ["Programme not yet rolled out; partner willing", "Randomised or phased "
            "roll-out", "Power calculation", "Fairness of allocation, consent"],
           ["Programme already running everywhere", "Theory-based or qualitative process "
            "evaluation", "Purposive cases", "Staff and beneficiaries may fear "
            "consequences"],
           ["Want to understand a new phenomenon", "Exploratory qualitative, then survey",
            "Purposive, then probability", "Unanticipated sensitive findings"],
           ["Community wants evidence for its own advocacy", "Participatory action research",
            "Defined with the community", "Ownership and use of data"]]),
        H("green", "Use the table to start a conversation, then work the choice through the "
          "question, the threats in Section 04 and the constraints you face."),
    ], compact=True),

    S("Protocol checklist", "What a complete research protocol contains", [
        TC([BL(["Title, investigators, institutions, funding and conflicts of interest",
                "Background and existing evidence, including secondary data checked",
                "Questions, hypotheses and the theory of change",
                "Design and the main threat to validity, with mitigation",
                "Population, frame, sampling method and sample size calculation",
                "Instruments, operational definitions, translation and pretesting plan"],
               "cyan")],
           [BL(["Fieldwork plan, training, supervision and back-checks",
                "Data management: storage, access, anonymisation, retention",
                "Analysis plan, with registration details",
                "Ethics: risk category, consent and assent procedures, disclosure protocol, "
                "support services",
                "Dissemination plan, including return of findings to participants",
                "Timeline, budget and limitations"], "green")]),
        H("amber", "Ethics committees, funders and journals each ask for most of this list. "
          "Writing it once, well, saves rewriting it three times."),
        B("A protocol is a living document. Version and date every change, and keep the "
          "approved version with your ethics correspondence.", sm=True),
    ]),

    S("Time and money", "Realistic timelines for a modest study", [
        TC([T(["Stage", "Typical time (illustrative)"],
              [["Question, scoping, secondary data", "3&ndash;6 weeks"],
               ["Protocol and instruments", "4&ndash;6 weeks"],
               ["Ethics review", "4&ndash;12 weeks, longer for full committee"],
               ["Translation, pretest, revision", "3&ndash;5 weeks"],
               ["Training and fieldwork", "6&ndash;12 weeks"],
               ["Cleaning and analysis", "6&ndash;10 weeks"],
               ["Writing and dissemination", "6&ndash;10 weeks"]])],
           [B("Teams most often underestimate three stages: ethics review, translation with "
              "pretesting, and data cleaning. Each is invisible in a project plan until it "
              "delays everything after it.", sm=True),
            H("red", "If the decision the research serves will be taken in four months, a "
              "nine-month study cannot inform it. Either shrink the study or agree an interim "
              "product, such as a secondary-data brief."),
            B("Costing methods for programmes and studies: "
              + L("cost-effectiveness.html", "Cost Effectiveness") + ".", sm=True)], ratio="a32"),
    ]),

    # ===================== SECTION 12 =====================
    DIV("12", "Twelve", "Writing, dissemination and where next"),

    S("Structure", "The research report and the policy brief", [
        TC([P("cyan", "Research report (IMRaD)",
              "Introduction: the question and why it matters. Methods: design, sample, "
              "measures, analysis, ethics, in enough detail to repeat. Results: what you found, "
              "planned analyses first. Discussion: what it means, limitations, implications."),
            B("Methods sections are where credibility is won. Reviewers read them first. Include "
              "response rates, deviations from the plan and how saturation was judged.", sm=True)],
           [P("green", "Policy brief",
              "Two to four pages. Lead with the finding and the recommendation. Then the "
              "evidence, a chart or two, and what the evidence cannot tell you. Name the "
              "decision-maker and the action."),
            B("Writing for journals, from structure to responding to reviewers, is in "
              + L("academic-writing.html", "Academic Writing &amp; Publishing") + ". Charts "
              "that tell the truth: " + L("data-viz.html", "Data Visualization") + ".", sm=True)]),
        H("amber", "Same study, different readers. Write the report first, then build the brief "
          "from it, so the numbers agree."),
    ]),

    S("Audiences", "One study, several audiences", [
        T(["Audience", "Wants", "Format", "Watch for"],
          [["Ministry or department", "What to do, what it costs, how sure you are",
            "Brief, presentation, short note", "Overclaiming certainty"],
           ["Implementing partner", "What to change in delivery", "Workshop, practical memo",
            "Defensiveness when findings are critical"],
           ["Participants and community", "What you found about them and what happens next",
            "Meeting in local language, visual summary", "Exposing individuals in small "
            "groups"],
           ["Funder", "Results against objectives, lessons", "Report, dashboard",
            "Pressure to frame null results as success"],
           ["Researchers", "Methods, data, replicability", "Journal article, working paper, "
            "shared data", "Long delays before anyone can use it"]]),
        H("cyan", "Plan each output in the protocol. Dissemination that is unbudgeted usually "
          "does not happen."),
        B("Advocacy with evidence: " + L("advocacy-basics.html", "Advocacy Basics") + ".", sm=True),
    ], compact=True),

    S("Honest reporting", "Limitations, null results and reporting standards", [
        TC([B("Every study has limitations. Stating them precisely is a strength: it tells the "
              "reader how far the findings travel. 'Small sample' is vague. 'Twenty interviews in "
              "two villages of one block, all conducted in Hindi, so Santali-speaking households "
              "are not represented' is useful.", sm=True),
            B("Null results deserve the same care as positive ones. A well-powered study "
              "showing a programme had no effect saves money and redirects effort.", sm=True)],
           [P("green", "Reporting guidelines",
              "Checklists help reviewers and readers find what they need: CONSORT for "
              "randomised trials, STROBE for observational studies, COREQ for interviews and "
              "focus groups, PRISMA for systematic reviews. Many journals require one."),
            B("Syntheses of many studies, and how reviewers judge risk of bias: "
              + L("systematic-reviews.html", "Systematic Reviews &amp; Evidence Synthesis") + ".",
              sm=True)]),
        H("amber", "Report your study in a way that would let someone include it fairly in a "
          "systematic review: clear design, sample sizes, effect sizes with uncertainty."),
    ]),

    S("Returning findings", "Returning findings and sharing data", [
        TC([P("cyan", "Back to participants",
              "ICMR's principle of transparency (1.1.10) asks that research plans and outcomes "
              "be made public while protecting privacy. In practice, plan a "
              "return visit: a village meeting, a pictorial summary, a session with frontline "
              "workers. People who gave their time should hear what it produced."),
            B("Check how findings could harm a group before presenting them locally. A chart "
              "showing one hamlet's low enrolment can stigmatise the families in it.", sm=True)],
           [P("green", "Sharing data",
              "Anonymised data and code let others check and build on your work. Remove direct "
              "and indirect identifiers, follow the Collection of Statistics Act standard of no "
              "identification even by elimination, and document variables fully."),
            BL(["Deposit with a data repository where your funder allows",
                "Share code with comments", "State access conditions clearly"], "green")]),
        H("indigo", "Data ethics beyond research: " + L("digital-ethics.html", "Digital Ethics")
          + " and " + L("data-feminism.html", "Data Feminism") + "."),
    ]),

    S("Takeaways", "Ten things to carry from this deck", [
        TC([BL(["<strong>The question decides everything:</strong> family, population, place, "
                "period, definitions",
                "<strong>Check secondary data first:</strong> NFHS, PLFS, HCES, Census, ASER, "
                "DHS, LSMS",
                "<strong>Match design to question</strong> and name its main threat",
                "<strong>Probability samples for prevalence,</strong> purposive samples for "
                "understanding",
                "<strong>Reliability and validity</strong> are separate, and both are "
                "needed"], "cyan")],
           [BL(["<strong>Reference periods and question order</strong> change the numbers",
                "<strong>Mixed methods earn their cost</strong> only through integration",
                "<strong>Ethics is design:</strong> ICMR 2017, consent, privacy law",
                "<strong>Write the analysis plan before the data,</strong> and register it",
                "<strong>Report candidly</strong> to every audience, including the people "
                "studied"], "green")]),
        H("amber", "Method is how others come to trust your answer. Every section of this deck "
          "is one more way of making the steps visible."),
    ]),

    S("Where next", "Where next in the ImpactMojo 101 series", [
        B("This deck walked the whole research process once. Each of these goes deeper into one "
          "part of it."),
        TC([BL(["Methods: " + L("qual-methods.html", "Qualitative Methods") + ", "
                + L("quant-methods.html", "Quantitative Methods") + ", "
                + L("mixed-methods.html", "Mixed Methods") + ", "
                + L("participatory-methods.html", "Participatory Methods"),
                "Surveys and measurement: " + L("survey-design.html", "Survey Design") + ", "
                + L("irt-basics.html", "Item Response Theory") + ", "
                + L("data-lit.html", "Data Literacy"),
                "Causes and impact: " + L("causal-inference.html", "Causal Inference") + ", "
                + L("impact-eval.html", "Impact Evaluation") + ", "
                + L("econometrics-101.html", "Econometrics")], "cyan")],
           [BL(["Ethics and data: " + L("research-ethics.html", "Research Ethics") + ", "
                + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act") + ", "
                + L("safeguarding-psea.html", "Safeguarding &amp; PSEA"),
                "Perspectives: " + L("feminist-research.html", "Feminist Research") + ", "
                + L("decolonize-dev.html", "Decolonial Development"),
                "Writing and synthesis: " + L("academic-writing.html",
                                                "Academic Writing &amp; Publishing") + ", "
                + L("systematic-reviews.html", "Systematic Reviews &amp; Evidence Synthesis")
                + ", " + L("mel-basics.html", "MEL Basics")], "green")]),
        H("indigo", "A suggested path for a new evaluator: Theory of Change, then Survey Design, "
          "then Qualitative Methods, then Impact Evaluation, then Research Ethics."),
    ]),

    # ===================== END =====================
    {"type": "end",
     "eyebrow": "Research Methods 101 &middot; Complete",
     "headline": "Ask clearly.<br>Show your working.",
     "byline": "A good study is one a careful sceptic can follow from question to conclusion. "
               "Explore the rest of the ImpactMojo 101 Series, free forever.",
     "ctas": [
         {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
         {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
         {"label": "Handouts", "href": "https://www.impactmojo.in"}],
     "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
]

DECK = {
    "slug": "research-methods",
    "title": "Research Methods 101",
    "description": ("Research Methods 101: a free foundational course for development "
                    "practitioners in South Asia. The research process from question to "
                    "write-up: framing answerable questions, ways of knowing, choosing "
                    "descriptive, explanatory and evaluative designs, sampling, validity and "
                    "reliability, qualitative, quantitative and mixed designs, secondary data "
                    "(NFHS, PLFS, HCES, Census, DHS, LSMS), ethics under the ICMR 2017 "
                    "guidelines, analysis plans, pre-registration and dissemination. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": SLIDES,
}

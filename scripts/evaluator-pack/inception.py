"""Inception Report & Evaluation Matrix Template (Word pack, house format)."""
from lib import Pack

FILE = "ImpactMojo-Inception-Report-Template.docx"


def build(path):
    k = Pack()
    k.cover(
        "Inception Report & Evaluation Matrix",
        "The complete pack: annotated inception report, evaluation matrix guide, sample-size method, client sign-off checklist and a worked example",
        "Template · DOCX · ₹199",
    )
    k.version("Version 1.0   ·   October 2026   ·   Part of the Evaluation Essentials Kit")
    k.box("WHAT IS INSIDE THIS PACK", [
        "**Part A.** What an inception report must settle before any data is collected.",
        "**Part B.** The annotated inception report, thirteen sections, each with guidance, what good looks like and the mistakes to avoid, plus space to write.",
        "**Part C.** Reference assets: how to fill the evaluation matrix row by row, a sample-size method with a lookup table, an evidence-strength scale, a checklist your client can use to approve the report, a glossary and sources.",
        "**Part D.** A worked example: selected sections of the inception report for the maternal and newborn health programme, the same case used across the ImpactMojo kit.",
    ])
    k.guide("Replace every [bracketed prompt] and write on the ruled lines. Keep the grey guidance while drafting and delete it before you send the report. An inception report is a contract between you and the client about how the evaluation will run, so write each section as a commitment you can be held to. Blue boxes headed 'Law as checked' state the rule as read on 21 October 2026, with its source. Laws change, so check the date before you rely on one.")

    # ---------------- PART A ----------------
    k.part("PART A", "What the inception report settles")
    k.body("An inception report turns a bid into a plan. You write it after you have read the programme documents and spoken with the people who run the programme, and before any data is collected. It confirms the evaluation questions, shows how each will be answered, and gives the client a chance to correct a misunderstanding while the correction costs a conversation. After fieldwork the same correction costs a second round of surveys.")
    k.body("Approval of the report is usually a payment milestone and always the point after which the design is fixed. Write it for two readers: the client team who approve it, and the field team who follow it.")
    k.body("Five habits make an inception report useful:")
    k.bullets([
        "Rebuild the theory of change from documents and conversations, and mark the assumptions the evaluation will test.",
        "Reduce the ToR's questions to a short final list, and say what was merged, reworded or dropped.",
        "Build the evaluation matrix first and write the design from it.",
        "Show the sample-size arithmetic so the client can check every step.",
        "State what the evaluation can and cannot tell the client.",
    ])

    # ---------------- PART B ----------------
    k.part("PART B", "The annotated inception report")

    k.h("1.  Purpose, use and what has changed since the bid")
    k.purpose("Say why the evaluation is happening, who will use it, and what you now know that you did not know when you bid.")
    k.guide("Open with the decision the evaluation serves and its date. Then list every change from the proposal, so the client does not discover them later. A change you disclose is a finding about the ToR. A change you hide is a dispute.")
    k.table(["Item", "At proposal", "Now", "Reason"], [
        ["[Comparison group]", "[ ]", "[ ]", "[ ]"],
        ["[Sample or timeline]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]"],
    ], [3.4, 4.0, 4.0, 4.5])
    k.good("A client who has not read the proposal for a month can see in one table what moved and why.")
    k.mistakes("Repeating the proposal word for word. The inception phase exists because you learned something, so the report must show it.")

    k.h("2.  Programme and theory of change")
    k.purpose("Describe what the programme does and how it expects change to happen, in a form the evaluation can test.")
    k.guide("Reconstruct the theory of change from the programme documents and your conversations, then ask the programme team to correct it. Draw it on one page and annex the diagram. Mark each assumption the evaluation will test, because those assumptions become evaluation questions.")
    k.table(["Level", "Statement", "Assumption to test"], [
        ["Activities", "[ ]", "[ ]"],
        ["Outputs", "[ ]", "[ ]"],
        ["Outcomes", "[ ]", "[ ]"],
        ["Impact", "[ ]", "[ ]"],
    ], [2.6, 7.0, 6.3])
    k.good("The programme team has read the diagram and agrees it describes what they do. Every assumption is either tested or listed as outside scope.")
    k.mistakes("Copying the logframe as if it were a theory. A logframe lists results. A theory of change explains why one should lead to the next.")

    k.h("3.  Evaluation questions")
    k.purpose("Fix the final list of questions, and show how each ToR question was treated.")
    k.guide("Group questions under the criteria that matter for the decision. Six to ten questions is a workable limit. Each should be specific about the change, the population and the period, and you should be able to name the data that answers it.")
    k.table(["ToR question", "Final question", "Action", "Reason"], [
        ["[ ]", "[ ]", "[kept / merged / reworded / dropped]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]"],
    ], [3.8, 5.0, 3.1, 4.0])
    k.good("Every ToR question appears in the table, and every final question can be traced to a decision.")
    k.mistakes("Keeping twenty questions to avoid a difficult conversation. A long list produces a thin answer to each.")

    k.h("4.  Evaluation matrix")
    k.purpose("Link every question to its criterion, indicators, data sources, methods and analysis, so that nothing is collected without a question and no question lacks data.")
    k.guide("This is the working core of the report. Part C1 shows how to fill each column and what a weak row looks like. Complete the matrix before you write sections 5 to 8, and let the design follow from it.")
    k.table(["Question", "Criterion", "Indicators or sub-questions", "Data source", "Method", "Analysis", "Limitation"], [
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ], [2.4, 1.9, 2.5, 2.2, 2.2, 2.4, 2.3], size=8)
    k.good("Each question has at least two data sources, and every column of every row is filled.")
    k.mistakes("A matrix of questions and methods with no indicators, which leaves the field team to decide what to measure.")

    k.h("5.  Design and standard of evidence")
    k.purpose("State the evaluation design and the kind of claim it can support.")
    k.guide("Say whether the design supports a claim of attribution, with a comparison group and a baseline, or a claim of contribution, built from a reasoned case. Explain why you chose it and what the client can say with it. List the claims that lie outside its reach, so the report is not asked later to carry weight the design cannot bear.")
    k.lines(4)
    k.good("The client can read one sentence that says what the evaluation can establish and one that says what it cannot.")
    k.mistakes("Promising impact and attribution with no comparison group, no baseline and a short timeline.")

    k.h("6.  Sampling and sample size")
    k.purpose("Show who will be sampled, how many, and how you arrived at the number.")
    k.guide("Write the sampling frame, the stages, the strata and the replacement rule. Show the sample-size arithmetic in steps, with each assumption stated and sourced. Part C2 gives the method and a lookup table. Add a sentence on what the sample can and cannot detect.")
    k.table(["Assumption", "Value", "Source or reason"], [
        ["Main outcome", "[ ]", "[ ]"],
        ["Expected level in comparison group", "[ ]", "[ ]"],
        ["Smallest difference worth detecting", "[ ]", "[ ]"],
        ["Significance level and power", "[5% and 80%]", "[ ]"],
        ["Design effect", "[ ]", "[ ]"],
        ["Expected non-response", "[ ]", "[ ]"],
        ["Final sample", "[ ]", "[ ]"],
    ], [5.6, 3.0, 7.3])
    k.good("Another statistician could reproduce the number from the table.")
    k.mistakes("Giving a sample size with no assumptions. Nobody can tell whether it is large enough to see the change the client cares about.")

    k.h("7.  Instruments and fieldwork plan")
    k.purpose("List the instruments, how they will be tested, and how fieldwork will be run and checked.")
    k.guide("Cover each instrument and its language, the pilot, enumerator training in days, supervision, spot checks and back-checks, the data-collection platform, the field schedule by block, and what happens when a respondent cannot be found. The ImpactMojo Survey Instrument Template and FGD Facilitator's Guide carry the tools themselves.")
    k.table(["Instrument", "Respondents", "Language(s)", "Pilot", "Quality checks"], [
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ], [3.6, 3.3, 2.7, 2.6, 3.7])
    k.good("The field team can start work from this section without a further briefing.")
    k.mistakes("Planning quality checks as a promise ('we will supervise closely') instead of as numbers: how many interviews are back-checked, and by whom.")

    k.h("8.  Analysis plan")
    k.purpose("Say, before data arrives, how each question will be answered.")
    k.guide("Name the main outcomes and comparisons, the disaggregation you will report, how you will handle missing data, how qualitative data will be coded, and how sources will be triangulated. State how findings will be rated for strength of evidence using the scale in Part C3.")
    k.lines(4)
    k.good("A reviewer can tell which table or chart will answer each question before any data exists.")
    k.mistakes("Deciding the analysis after seeing the data, which makes every positive result suspect.")

    k.h("9.  Ethics, safeguarding and data management")
    k.purpose("State the protections for participants and for their data, as conditions of the work.")
    k.guide("Cover informed consent and the right to withdraw, assent and guardian consent for anyone under 18, a referral route if a respondent discloses harm, who sees identifiable data, where it is stored, how long it is kept and when it is deleted, whether an ethics review applies, and how AI tools will and will not be used. The ImpactMojo Data Management & Consent Pack and the Ethics & DPDP Consent Checklist carry the forms and the plan.")
    k.lines(4)
    k.legal("The Digital Personal Data Protection Act, 2023 defines a child as anyone under 18 (section 2(f)), and section 9 requires verifiable consent from a parent or lawful guardian before a data fiduciary processes a child's data. The DPDP Rules, 2025 were notified in November 2025. The rules on notice, consent and children (Rules 3 and 5 to 16) start 18 months later, on 13 May 2027, so an evaluation that runs across that date should be designed to the stricter regime from the start. Section 17(2)(b) exempts processing necessary for research or statistical purposes only where the data is not used to take a decision specific to the person and the processing follows the standards the Rules prescribe. A follow-up of named programme participants will often fall outside that exemption. In practice the client that decides why and how data is collected acts as the data fiduciary and the evaluator as its processor under a written contract (section 8(2)). An evaluator who designs the instrument and holds the dataset may be a fiduciary too, so write the role down. If the study involves human participants in health research, check whether an institutional ethics committee must review it under the ICMR National Ethical Guidelines for Biomedical and Health Research Involving Human Participants (2017).")
    k.good("Consent, referral, storage and deletion each have a named person and a date.")
    k.mistakes("A line saying 'data will be kept confidential', with no storage, access or deletion plan behind it.")

    k.h("10.  Workplan, deliverables and client roles")
    k.purpose("Show the weeks, the deliverables, and what the client must do for the dates to hold.")
    k.guide("Group the plan by phase. Mark each client review period and each approval gate. Put the client's tasks in the plan next to yours, because access and review cause most delays in evaluation.")
    k.table(["Weeks", "Phase and activity", "Deliverable or gate", "Client task"], [
        ["[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]"],
    ], [2.2, 5.6, 4.0, 4.1])
    k.good("Every phase has a gate, a deliverable and a client task, and the review periods are written into the calendar.")
    k.mistakes("A workplan that shows only your activities, with no time for the client to review or approve.")

    k.h("11.  Team, quality assurance and risks")
    k.purpose("Name who does the work, who checks it, and what could go wrong.")
    k.guide("List each role, the named person and the days. Name a quality reviewer who is not on the field team. Keep the risk table short, with an owner and a next action for every row, and review it each week.")
    k.table(["Role", "Name", "Days", "Responsibility"], [
        ["[Team leader]", "[ ]", "[ ]", "[ ]"],
        ["[Senior researcher]", "[ ]", "[ ]", "[ ]"],
        ["[Quality reviewer]", "[ ]", "[ ]", "[ ]"],
    ], [3.6, 3.6, 1.8, 6.9])
    k.table(["Type", "Entry", "Owner", "Next action", "By when"], [
        ["[Risk]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[Assumption]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[Dependency]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ], [2.4, 5.4, 2.4, 3.9, 1.8])
    k.good("Each risk has an owner and a next action, and each assumption has a planned check.")
    k.mistakes("A senior name on the cover who does no hands-on work and has no days in the staffing table.")

    k.h("12.  Limitations")
    k.purpose("Tell the client now what the evaluation will be unable to say.")
    k.guide("List three to five limitations plainly: a missing baseline, a comparison that is only approximate, recall error, a sample too small to compare subgroups. For each, say how you will limit the damage and how the report will word the finding.")
    k.lines(3)
    k.good("No limitation will surprise the client when it appears in the final report.")
    k.mistakes("Placing limitations in an annex at the end of the final report instead of agreeing them at inception.")

    k.h("13.  Outline of the final report")
    k.purpose("Draft the headlines of the final report before collecting data, so that every instrument question feeds a headline.")
    k.guide("Write each section title as a full sentence that states the finding you expect, then name the chart or table and the data source. Treat each headline as a guess to test. Rewrite or delete it when the data disagrees.")
    k.table(["Section", "Expected headline (to test)", "Chart or evidence", "Data source"], [
        ["[1]", "[ ]", "[ ]", "[ ]"],
        ["[2]", "[ ]", "[ ]", "[ ]"],
        ["[3]", "[ ]", "[ ]", "[ ]"],
    ], [1.8, 6.6, 3.9, 3.6])
    k.good("Every question in your instruments feeds at least one headline, and the team agrees the headlines will change if the data says so.")
    k.mistakes("Treating the draft headlines as conclusions, and collecting only the evidence that supports them.")
    k.body("**Annexes.** Theory of change diagram. Evaluation matrix. Sampling plan and calculations. Draft instruments. Stakeholder list. Documents reviewed. Ethics and consent forms. Data management plan.")

    # ---------------- PART C ----------------
    k.part("PART C", "Reference assets")

    k.h("C1.  Filling the evaluation matrix, column by column")
    k.table(["Column", "What to write", "A weak entry", "A stronger entry"], [
        ["Question", "One answerable question, specific about change, people and period.", "What was the impact?", "How much did antenatal-care completion change in the programme blocks since 2024, and for which groups?"],
        ["Criterion", "The OECD-DAC criterion it serves: relevance, coherence, effectiveness, efficiency, impact or sustainability.", "Programme", "Effectiveness"],
        ["Indicators or sub-questions", "A defined measure, countable the same way by two people.", "Better health", "Share of women with a recent birth who had four or more antenatal visits."],
        ["Data source", "Where the data comes from. Use at least two for each question.", "Survey", "Household survey and monitoring-system extract"],
        ["Method", "The collection or analysis method, with the comparison if one is used.", "Analysis", "Comparison of programme and comparison blocks, with a pre-2024 trend check"],
        ["Analysis", "How the data will be turned into an answer, and the disaggregation.", "Descriptive statistics", "Difference between groups, reported by social group and wealth quintile"],
        ["Limitation", "What this row cannot tell the client.", "None", "Recall error in the survey; no baseline survey, so the monitoring data carries the trend"],
    ], [2.3, 5.0, 3.2, 5.4], size=8.5)

    k.h("C2.  Sample size for comparing two proportions")
    k.body("This method gives a planning figure for comparing a proportion between two groups, such as programme and comparison blocks. It is a planning approximation. Take the final design to a statistician, particularly when clustering is strong, when there is baseline data, or when you need subgroup comparisons.")
    k.numbered([
        "Choose the outcome and its expected level in the comparison group (p1) and the smallest difference worth detecting, which gives p2.",
        "Take a 5% two-sided significance level (z = 1.96) and 80% power (z = 0.8416).",
        "Compute the sample per group: n = [1.96 × √(2 × p̄ × (1 − p̄)) + 0.8416 × √(p1 × (1 − p1) + p2 × (1 − p2))]² ÷ (p1 − p2)², where p̄ is the mean of p1 and p2.",
        "Multiply by the design effect for clustering (1.5 is a planning figure for household surveys with moderate clustering. Replace it with a figure from your own survey or a similar one).",
        "Divide by (1 − expected non-response), for example 0.90 when you expect 10% non-response.",
        "Round up, and double for the two groups.",
    ])
    k.body("Lookup table for p1 = 60%, a design effect of 1.5 and 10% non-response. Detectable difference is the gap between the two groups.")
    k.table(["Detectable difference", "p2", "Raw sample per group", "With design effect", "With non-response", "Total, both groups"], [
        ["5 percentage points", "65%", "1,471", "2,206", "2,451", "4,902"],
        ["10 percentage points", "70%", "356", "534", "594", "1,188"],
        ["15 percentage points", "75%", "152", "228", "254", "508"],
    ], [3.5, 1.5, 2.9, 2.7, 2.7, 2.6])
    k.body("Halving the difference you want to detect roughly quadruples the sample. Say so to the client when they ask for a small difference on a small budget.")

    k.h("C3.  Evidence-strength scale")
    k.table(["Rating", "Rule", "Wording in the report"], [
        ["Strong", "Two or more independent sources and methods agree, the design supports the type of claim made, and no significant threat is left unaddressed.", "The evidence shows that..."],
        ["Moderate", "Sources agree, but the design cannot rule out another explanation, or only one source is strong.", "The evidence suggests that..."],
        ["Limited", "One source, a small sample, or sources that disagree.", "There are indications that..."],
    ], [2.5, 8.8, 4.6])
    k.body("Rate claims of change and claims of cause separately. 'Antenatal-care completion rose' can be strong while 'the programme caused the rise' is moderate.")

    k.h("C4.  Checklist for the client approving the inception report")
    k.guide("Send this list with the report. It helps the client review well and shortens the approval period.")
    k.numbered([
        "Does the theory of change describe what the programme actually does?",
        "Do the final questions answer the decision named in the ToR?",
        "Is every ToR question accounted for as kept, merged, reworded or dropped?",
        "Does each question have at least two data sources in the matrix?",
        "Do you understand what the design can and cannot establish?",
        "Is the sample size reproducible from the assumptions listed?",
        "Are the field schedule and the client tasks realistic for your team?",
        "Are consent, child protection and data handling stated clearly?",
        "Are the limitations ones you can accept?",
        "Do the draft headlines match what you expect to need for your decision?",
    ])

    k.h("C5.  Glossary")
    k.table(["Term", "Meaning"], [
        ["Evaluation matrix", "A table linking each evaluation question to indicators, data sources, methods and analysis."],
        ["Theory of change", "The explicit, testable logic from activities to the intended change, with its assumptions."],
        ["Attribution", "The share of an observed change that can be causally assigned to the programme. It needs a counterfactual."],
        ["Contribution", "A reasoned account of how the programme added to a change alongside other factors."],
        ["Design effect", "How much clustering reduces the precision of a sample compared with a simple random sample of the same size."],
        ["Back-check", "A short repeat visit or call to a sample of respondents to confirm that the interview took place and key answers match."],
        ["Triangulation", "Using more than one source or method to confirm a finding."],
        ["Disaggregation", "Reporting results separately by group, such as sex, social group, wealth and location."],
    ], [3.8, 12.1])

    k.h("C6.  Standards and sources")
    k.body("Check each source for the current version before you rely on it.")
    k.bullets([
        "OECD/DAC (2019). Better Criteria for Better Evaluation: Revised Evaluation Criteria Definitions and Principles for Use. Paris: OECD Development Assistance Committee.",
        "UNEG (2016). Norms and Standards for Evaluation. New York: United Nations Evaluation Group.",
        "BetterEvaluation (betterevaluation.org). The Rainbow Framework for planning and managing an evaluation.",
        "3ie, International Initiative for Impact Evaluation (3ieimpact.org). Principles and standards for rigorous impact evaluation.",
        "Government of India (2023). The Digital Personal Data Protection Act, 2023. New Delhi: Ministry of Electronics and Information Technology.",
    ], 10)

    # ---------------- PART D ----------------
    k.part("PART D", "Worked example: selected sections of an inception report")
    k.box("ABOUT THIS EXAMPLE", [
        "This is the evaluator's inception report for the Surakshit Maa case used in the ImpactMojo Terms of Reference pack: a programme in three blocks since 2024, eight upgraded labour rooms, about 9,200 pregnant women a year, a funding decision in March 2027 and a 13-week window. Names and figures are illustrative.",
    ])
    k.h("1.  What has changed since the bid")
    k.table(["Item", "At proposal", "Now", "Reason"], [
        ["Comparison blocks", "Two blocks chosen by the evaluator from district averages.", "Two blocks chosen jointly after reviewing monitoring trends.", "One proposed block gained a new district hospital in 2025, which would distort the comparison."],
        ["Questions", "Three questions from the ToR.", "Three questions, with the second reworded.", "'Attribution' cannot be answered by a survey taken once. The question now asks for contribution against the district trend."],
        ["Fieldwork order", "All blocks together.", "The hill block first.", "Monsoon access to the hill block closes after week 8."],
    ], [2.8, 4.1, 4.4, 4.6], size=8.5)
    k.h("3.  Evaluation questions")
    k.table(["ToR question", "Final question", "Action"], [
        ["Effectiveness: to what extent did four or more antenatal visits and skilled birth attendance increase, and did gains hold across Scheduled Caste and poorest-quintile women?", "Same, reported by social group and wealth quintile.", "Kept"],
        ["Impact: what share of the change in skilled birth attendance can be credited to the programme, against the district trend?", "How much of the change in skilled birth attendance since 2024 is consistent with the programme's contribution, once the district trend is accounted for?", "Reworded"],
        ["Sustainability: are the state health budget and staffing likely to sustain the labour-room upgrades and ASHA incentives after the grant?", "Same.", "Kept"],
    ], [6.4, 6.4, 3.1], size=8.5)
    k.h("4.  Evaluation matrix (extract)")
    k.table(["Question", "Criterion", "Indicators", "Data source", "Method", "Analysis", "Limitation"], [
        ["Effectiveness: change in antenatal care and skilled birth attendance by social group and wealth", "Effectiveness", "Women with 4+ antenatal visits; births attended by skilled staff", "Household survey; monitoring-system extract", "Survey of women with a birth in the last 12 months, programme and comparison blocks", "Difference between groups; by social group and wealth quintile", "Recall error. No baseline survey, so monitoring data carries the pre-2024 trend."],
        ["Contribution to the change in skilled birth attendance", "Impact", "Monthly institutional births per block, 2022 to 2026", "Monitoring-system extract; interviews with ASHAs and facility staff", "Difference-in-differences on monthly facility data with a pre-2024 trend check; contribution analysis from interviews", "Compare the change in programme and comparison blocks; test the parallel-trend assumption on pre-2024 months", "The comparison blocks were matched without random assignment. Other changes in the district cannot be ruled out."],
        ["Likelihood that upgrades and incentives continue after the grant", "Sustainability", "State budget line for labour rooms; posts filled; incentive payments on time", "State budget documents; interviews with district and state officers", "Document review; key-informant interviews", "Thematic analysis against an agreed set of sustainability conditions", "Budget intent can differ from release. Officers may change after the evaluation."],
    ], [2.5, 1.7, 2.5, 2.4, 2.8, 2.4, 1.6], size=7.5)
    k.h("5.  Design and standard of evidence")
    k.body("The design is mixed methods. A difference-in-differences comparison of monthly facility data in three programme blocks and two comparison blocks, from 2022 to 2026, shows whether the change since 2024 was larger in the programme blocks. A household survey of women with a recent birth gives the levels and the equity breakdown. Interviews explain what the numbers show. The pre-2024 months test whether the blocks were moving together before the programme.")
    k.body("The design supports a claim that the programme contributed to the change, with a stated strength of evidence. A claim of exact attribution would need a baseline household survey and randomly assigned or closely matched comparison blocks, and neither exists here.")
    k.h("6.  Sampling and sample size")
    k.table(["Assumption", "Value", "Source or reason"], [
        ["Main outcome", "Women with 4+ antenatal visits", "ToR question 1"],
        ["Expected level in comparison blocks", "60%", "District monitoring data for the comparison blocks"],
        ["Smallest difference worth detecting", "10 percentage points (70% in programme blocks)", "The change the funder's board said would justify a second phase"],
        ["Significance level and power", "5% and 80%", "Convention"],
        ["Design effect", "1.5", "Planning figure for villages as clusters with about 12 interviews each"],
        ["Expected non-response", "10%", "Experience of recent-birth surveys in the district"],
        ["Raw sample per group", "356", "Formula in Part C2"],
        ["After design effect", "534", "356 × 1.5, rounded up"],
        ["After non-response", "594", "534 ÷ 0.90, rounded up"],
        ["Final sample", "1,188, rounded to 1,200", "594 per group, two groups"],
    ], [5.2, 5.0, 5.7])
    k.body("The sample can detect a 10-point difference overall. It cannot detect differences of that size inside small subgroups, so subgroup results are reported as descriptive and rated moderate or limited.")
    k.h("11.  Risks (extract)")
    k.table(["Type", "Entry", "Owner", "Next action", "By when"], [
        ["Risk", "Monsoon cuts road access to the hill block after week 8.", "Field coordinator", "Run hill-block fieldwork first, in weeks 5 and 6.", "Week 4"],
        ["Assumption", "Monitoring data for 2022 to 2026 is complete.", "Senior researcher", "Check a 5% sample of facility records against registers.", "Week 2"],
        ["Risk", "Enumerators leave during fieldwork.", "Field coordinator", "Train 20 for 14 posts and hold six in reserve.", "Week 4"],
        ["Risk", "Women from comparison blocks use programme facilities, which blurs the comparison.", "Team leader", "Record the facility used for each birth and test the result with and without those cases.", "Week 9"],
        ["Dependency", "District access letters for field visits.", "Client programme director", "Issue letters for all five blocks.", "Week 3"],
    ], [2.2, 5.2, 2.6, 4.1, 1.8], size=8.5)
    k.h("13.  Outline of the final report (extract, headlines to test)")
    k.table(["Section", "Expected headline (to test)", "Chart or evidence", "Data source"], [
        ["1", "Antenatal-care completion rose faster in the programme blocks than in the comparison blocks.", "Line chart of monthly facility data, 2022 to 2026, with the 2024 start marked", "Monitoring-system extract"],
        ["2", "Gains were smaller for Scheduled Caste and poorest-quintile women.", "Bar chart by social group and wealth quintile", "Household survey"],
        ["3", "ASHA home visits explain most of the rise in antenatal visits.", "Interview themes linked to the rise by block", "Interviews and focus groups"],
        ["4", "The labour-room upgrades depend on state posts that are not yet funded.", "Table of budget lines and filled posts", "State budget documents; interviews"],
    ], [1.8, 6.6, 4.1, 3.4], size=8.5)
    k.figures("The design effect, non-response rate, comparison level and the hospital opened in 2025 are illustrative planning values chosen to show the arithmetic. They come from no real programme. In your own report, take each from programme data or a cited source.")
    k.save(path)


if __name__ == "__main__":
    import sys
    build(sys.argv[1])

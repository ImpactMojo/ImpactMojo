"""Statement of Work & Change Request Template (Word pack, house format)."""
from lib import Pack

FILE = "ImpactMojo-SOW-Change-Request-Template.docx"


def build(path):
    k = Pack()
    k.cover(
        "Statement of Work & Change Request",
        "The complete pack: annotated statement of work, change request form, clause bank and a worked example",
        "Template · DOCX · ₹199",
    )
    k.version("Version 1.0   ·   October 2026   ·   Part of the Evaluation Essentials Kit")
    k.box("WHAT IS INSIDE THIS PACK", [
        "**Part A.** Why scope disputes start before the work does, and what a statement of work settles.",
        "**Part B.** The annotated statement of work, thirteen sections, each with guidance, what good looks like and the mistakes to avoid, plus space to write. A one-page change request form follows.",
        "**Part C.** Reference assets: a clause bank in plain language, a payment-milestone chooser, questions to ask when the client sends its own contract, a glossary and sources.",
        "**Part D.** A worked example: the evaluator's statement of work and one change request for the maternal and newborn health programme, the same case used across the ImpactMojo kit.",
    ])
    k.guide("Replace every [bracketed prompt] and write on the ruled lines. Keep the grey guidance while drafting and delete it before you send the document. A statement of work is written by the person who does the work for the person who pays for it, so write it in the plain language both can read. This pack is a drafting aid, so have a lawyer read the final contract. Blue boxes headed 'Law as checked' state the rule as read on 21 October 2026, with its source. Laws change, so check the date before you rely on one.")

    # ---------------- PART A ----------------
    k.part("PART A", "Why the contract is where scope is won or lost")
    k.body("Most disputes in an evaluation assignment are about one of four things: what was included, how many rounds of comments there would be, when the money was due, and who had the last word on the findings. Each of the four can be settled in an afternoon before signing. After signing, each takes weeks and costs goodwill that the next assignment depends on.")
    k.body("A terms of reference says what the client wants. A statement of work says what you will deliver, to what standard, by when, for what fee, and what happens when the client asks for something else. It is a schedule to the contract or the contract's operative page. If the client has a fixed contract you cannot change, use Part B as a list of questions to raise before you sign.")
    k.body("Four habits keep a statement of work honest:")
    k.bullets([
        "Describe every deliverable with a length, a format and a number of review rounds.",
        "Write the exclusions as carefully as the inclusions.",
        "Tie each payment to something you control, such as submission, with a fixed period for the client to respond.",
        "Agree before signing how a change is requested, priced and approved.",
    ])

    # ---------------- PART B ----------------
    k.part("PART B", "The annotated statement of work")

    k.h("1.  Parties and assignment title")
    k.purpose("Say who is contracting, and give the assignment one short name that every later document uses.")
    k.guide("Use legal names and registered addresses. Name one contract manager on each side. The invoice, the tax deduction certificate and any dispute follow the legal entity that signed.")
    k.table(["Field", "Entry"], [
        ["Client (legal name and address)", "[ ]"],
        ["Evaluator (legal name, registration, address)", "[ ]"],
        ["Assignment title", "[ ]"],
        ["Contract or purchase order number", "[ ]"],
        ["Client contract manager", "[ ]"],
        ["Evaluator lead", "[ ]"],
        ["Start date / end date", "[ ] / [ ]"],
    ], [6.2, 9.7])
    k.good("Legal names match the registration documents, and each side has one named person for day-to-day questions.")
    k.mistakes("A programme's brand name in place of the entity that signs, so the invoice goes to an organisation that never agreed to pay it.")

    k.h("2.  Purpose and the decision served")
    k.purpose("Restate in one paragraph why the evaluation is happening and which decision it informs, in the client's own words.")
    k.guide("Copy the decision and its date from the ToR. If the ToR names none, write the decision as you understand it and ask the client to confirm it in writing. Every later question about whether the work is complete is answered against this paragraph.")
    k.lines(3)
    k.good("Names the decision, the person who makes it and the date.")
    k.mistakes("Copying 'to assess the programme' from the ToR. Nobody can say when that task is finished.")

    k.h("3.  Scope: what is in and what is out")
    k.purpose("Draw the boundary of the work, and write down what sits outside it.")
    k.guide("Cover four dimensions and then add one standing line about other tasks. Naming what is out of scope prevents the most common contract dispute.")
    k.table(["Dimension", "In scope", "Out of scope"], [
        ["Geographic", "[districts / blocks / states]", "[areas excluded]"],
        ["Temporal", "[period covered]", "[periods excluded]"],
        ["Thematic", "[components and outcomes covered]", "[components excluded]"],
        ["Population", "[groups covered]", "[groups excluded]"],
        ["Other tasks", "None unless agreed through section 10.", "Any task not listed in section 4."],
    ], [3.4, 6.2, 6.3])
    k.good("A reader who was not in the negotiation can tell whether a new request is inside the work or outside it.")
    k.mistakes("Accepting a ToR line such as 'the consultant will also undertake any other tasks assigned by the programme team'. It turns a fixed fee into an open commitment.")

    k.h("4.  Deliverables and schedule")
    k.purpose("List every deliverable with its format, length, review rounds and due date, counted from the start date.")
    k.guide("State page limits, the language of each deliverable, whether translation is included, and whether the cleaned dataset, codebook and scripts are deliverables. Give the comment period in working days. If the ToR timeline leaves no room for the comment period you need, say so here and state that each extra day of review moves the next date by a day.")
    k.table(["Deliverable", "Format and length", "Review rounds", "Client comment period", "Due (week)"], [
        ["[Inception report]", "[Word or PDF, up to 25 pages]", "[1]", "[5 working days]", "[3]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ], [3.6, 4.6, 2.2, 3.4, 2.1])
    k.good("Every deliverable has a length, a format, a number of review rounds and a date. Nothing is described only as 'high quality'.")
    k.mistakes("A deliverable called 'evaluation report' with no page limit and no limit on rounds of comments. The report is never finished because it is never defined.")

    k.h("5.  Client responsibilities and dependencies")
    k.purpose("List what the client must provide for your dates to hold, with a date and an owner for each item.")
    k.guide("Typical items are programme documents and the theory of change, extracts from the monitoring system, introductions to district officials, field access letters, ethics approval where it is needed, named reviewers and prompt comments. State what happens when an item is late.")
    k.table(["Dependency", "Client owner", "Needed by"], [
        ["[Programme documents and monitoring data extract]", "[name]", "[date]"],
        ["[Introductions and access letters for field visits]", "[name]", "[date]"],
        ["[Named reviewers and comment turnaround]", "[name]", "[date]"],
        ["[ ]", "[ ]", "[ ]"],
    ], [8.5, 3.7, 3.7])
    k.body("Late inputs: [If an item above is more than 5 working days late, the schedule moves by the same number of days and the change process in section 10 applies to any added cost.]")
    k.good("Each dependency has a date and a named owner, and a late item has a stated effect on the schedule.")
    k.mistakes("'The evaluator will obtain all necessary data.' You cannot obtain what the client holds, and the sentence makes every delay yours.")

    k.h("6.  Acceptance and review")
    k.purpose("Define how a deliverable is accepted, and what happens if nobody replies.")
    k.guide("Fix the comment period, ask for one consolidated set of comments, limit the rounds, and say when silence counts as acceptance. Acceptance means the deliverable matches its description in section 4. The client's agreement with the findings is a separate matter, covered in section 7.")
    k.lines(3)
    k.legal("Parties may agree how acceptance is shown, so a clause that treats a deliverable as accepted when the client sends no comments inside the stated period binds both sides (Indian Contract Act, 1872, section 7 lets the proposal prescribe the manner of acceptance). Silence alone binds nobody, so the clause must be in the signed contract. If the client's own template says its terms override yours, theirs prevail, so read it before you sign. For a micro or small enterprise the Micro, Small and Medium Enterprises Development Act, 2006 fixes its own deemed acceptance: when the buyer makes no written objection within 15 days of delivery, acceptance is the day of delivery (section 15, Explanation). The payment clock runs from there.")
    k.good("One comment period, one consolidated set of comments, a fixed number of rounds and a stated result when the period lapses.")
    k.mistakes("Open-ended review, with several people at the client sending separate comments weeks apart.")

    k.h("7.  Independence and findings")
    k.purpose("Protect the credibility of the evaluation by separating factual corrections from changes to findings.")
    k.guide("The client may correct facts and ask for clarity. The evaluator decides the findings, conclusions and recommendations, and records any comment not taken up with the reason. Add a conflict-of-interest declaration, so that any link between the evaluator and the programme is on the record.")
    k.lines(3)
    k.good("The client can see its comments and the evaluator's reasons in one table, and nobody can say the findings were negotiated.")
    k.mistakes("'Findings will be finalised after approval by the programme team.' This clause makes the programme the judge of its own evaluation.")

    k.h("8.  Fees and payment milestones")
    k.purpose("State the total fee, what it includes and each payment with its trigger.")
    k.guide("Say whether the fee is fixed or on daily rates, whether expenses are included or billed at actuals, and whether taxes are inside the figure. Tie each payment to a submission that you control. Part C2 helps you choose a pattern.")
    k.table(["Milestone", "Trigger", "Share of fee", "Amount", "Payable within"], [
        ["[On signing]", "[Signed contract]", "[ ]%", "[ ]", "[ ] days"],
        ["[Inception]", "[Submission of inception report]", "[ ]%", "[ ]", "[ ] days"],
        ["[Draft]", "[Submission of draft report]", "[ ]%", "[ ]", "[ ] days"],
        ["[Final]", "[Submission of final report and dataset]", "[ ]%", "[ ]", "[ ] days"],
    ], [2.6, 5.4, 2.4, 2.6, 2.9])
    k.good("At least three payments, one of them early, and no more than 40% held back until the last deliverable.")
    k.mistakes("'100% of the fee on approval of the final report.' You carry every fieldwork cost until a person you do not control signs off.")

    k.h("9.  Taxes and deductions")
    k.purpose("State which taxes the fee includes, and note the deductions the client may make before paying you.")
    k.guide("Write one sentence for each of three points: whether the fee includes or excludes GST, whether you are registered for GST, and that the client may deduct tax at source from the professional fee and must give you a certificate. Ask when and how the certificate arrives, because you claim credit for the deduction in your own return.")
    k.lines(2)
    k.legal("GST: evaluation and research services carry 18 per cent. Use SAC 9983 (other professional, technical and business services, 998399 where nothing closer fits) or 9981 (research and experimental development; 99812 covers social sciences and humanities), and match the code to the work you invoice. Between two parties in India the place of supply of a service is the location of the recipient (section 12(2), IGST Act), which decides whether you charge CGST and SGST or IGST. A client outside India that pays in convertible foreign exchange makes this an export of services, zero rated under section 16 of the IGST Act if the conditions in section 2(6) are met. Reverse charge applies only to the services listed in Notification 13/2017-Central Tax (Rate); professional and research services supplied to a government body are not on it, so you charge GST. Government departments must deduct GST at source at 2 per cent under section 51 of the CGST Act where a contract's taxable value exceeds ₹2.5 lakh. Income tax: under the Income-tax Act, 2025 (in force from 1 April 2026) tax on fees is deducted under section 393(1), table serial 6(iii), formerly section 194J. The rate is 10 per cent on fees for professional services and 2 per cent on fees for technical services that are not professional services, with a threshold of ₹50,000 a year. Evaluation and research advice is normally treated as professional services, so ask the client's accounts team how they classify it. When GST is shown separately on the invoice, tax is deducted on the fee without the GST (CBDT Circular 23/2017).")
    k.good("The tax treatment of the fee fits in three sentences and matches the invoice you will send.")
    k.mistakes("A fee quoted as 'inclusive of taxes' when you meant to add GST on top. The client pays the figure and the tax comes out of your fee.")

    k.h("10.  Change control")
    k.purpose("Agree how a new request is raised, priced and approved, so that scope changes are decisions and not habits.")
    k.guide("Any request that changes scope, deliverables, schedule or fee goes on the change request form that follows section 13. You answer within a fixed number of working days with the effect on days, fee and schedule. Work on the change starts when both sides have signed. Small clarifications inside the existing scope do not need a form.")
    k.lines(3)
    k.good("There is a form, a response time and a signature step, and both sides have read them before the first request arrives.")
    k.mistakes("Doing an extra piece of work 'to keep the relationship' and never recording it. The next request then has a precedent.")

    k.h("11.  Intellectual property, data and confidentiality")
    k.purpose("Say who owns the report, the dataset and the instruments, and who is responsible for personal data.")
    k.guide("A common position is that the client owns the final report and the cleaned dataset, and the evaluator keeps its own tools and methods with a licence to the client. Anonymised learning may be reused only with written permission. Under the Digital Personal Data Protection Act, 2023 the client is usually the data fiduciary and the evaluator a data processor, which calls for a written term on how data is handled. The ImpactMojo Data Management & Consent Pack carries the plan, the consent forms and the checklist.")
    k.lines(3)
    k.legal("The Digital Personal Data Protection Act, 2023 requires a data fiduciary to engage a processor only under a valid contract (section 8(2)). The client that decides why and how personal data is collected is usually the fiduciary and the evaluator its processor, although an evaluator who designs the instrument and holds the dataset can be a fiduciary as well, so state the roles. Section 9 requires verifiable parental or guardian consent for anyone under 18. The DPDP Rules, 2025 were notified in November 2025 and the main obligations, including consent and children's data, start on 13 May 2027. Section 16 allows transfer of personal data outside India except to countries the government restricts by notification, and a sector law or funder rule may restrict more, so list every tool and server that sits abroad. Have a lawyer confirm the current text before you rely on it.")
    k.good("Ownership of each output is stated, and the data handling term points to a dated data management plan.")
    k.mistakes("Silence on who owns the dataset, followed by a dispute when the client wants to share it with another evaluator.")

    k.h("12.  Use of AI tools")
    k.purpose("State whether AI tools will be used, for what, and under what data rule.")
    k.guide("List the permitted uses, such as drafting, translation and code. Set a data rule: no respondent data goes into a tool the client has not approved, and any data that does is de-identified first. Promise disclosure in the methodology note, and name the person who checks every output.")
    k.lines(2)
    k.good("The client knows which tools touch which data before fieldwork starts.")
    k.mistakes("Saying nothing, and then using a tool that the client's data policy forbids.")

    k.h("13.  Term, termination and disputes")
    k.purpose("Say how the contract ends and what is paid if it ends early.")
    k.guide("State the notice period, payment for work completed to the date of notice plus costs already committed that cannot be cancelled, what you hand over on early termination, the governing law and where disputes are heard.")
    k.lines(3)
    k.legal("A contract between two Indian parties is governed by the Indian Contract Act, 1872. Section 28 voids a term that absolutely restrains legal proceedings or shortens the limitation period, but an arbitration clause is allowed. Where more than one court has jurisdiction, parties may agree on one of them, and a clause that names a court which has none is void (A.B.C. Laminart v A.P. Agencies, (1989) 2 SCC 163). Under the Arbitration and Conciliation Act, 1996 the seat of arbitration decides which court supervises it (BALCO v Kaiser Aluminium, (2012) 9 SCC 552). Section 74 of the Contract Act lets a court award reasonable compensation up to the sum named for breach, so a liability cap is enforceable between businesses when it is reasonable. An unstamped agreement is not void but cannot be used as evidence until the stamp duty and penalty are paid, and the rates differ by state. The pack gives you the clause topics; a lawyer should confirm the current text of each section and case cited here and settle the final wording for a high-value contract.")
    k.good("A cancelled assignment leaves nobody unpaid for work already done.")
    k.mistakes("No early termination term, so a cancellation after fieldwork leaves the enumerator costs with the evaluator.")

    k.sub("Signatures")
    k.table(["", "Client", "Evaluator"], [
        ["Name and title", "[ ]", "[ ]"],
        ["Signature", "", ""],
        ["Date", "[ ]", "[ ]"],
    ], [4.0, 5.95, 5.95])

    k.page_break()
    k.sub("Change request form")
    k.guide("One page per change. Number the forms in order (CR-01, CR-02) and attach each signed form to the contract.")
    k.table(["Field", "Entry"], [
        ["Change request number and date", "[CR-    ]  [date]"],
        ["Raised by", "[client / evaluator]"],
        ["Description of the change", "[ ]"],
        ["Why it is needed", "[ ]"],
        ["Effect on scope (added or removed)", "[ ]"],
        ["Effect on deliverables", "[ ]"],
        ["Effect on days", "[team leader __ , senior researcher __ , analyst __ , field team __ ]"],
        ["Effect on fee (state whether taxes are included)", "[ ]"],
        ["Effect on schedule (which date moves, by how many days)", "[ ]"],
        ["Effect on risk", "[ ]"],
        ["Options", "[accept as priced / modify / decline / defer]"],
        ["Decision and date", "[ ]"],
        ["Signatures", "Client: ______________    Evaluator: ______________"],
    ], [6.0, 9.9])

    # ---------------- PART C ----------------
    k.part("PART C", "Reference assets")

    k.h("C1.  Clause bank in plain language")
    k.guide("Adapt the wording, keep the brackets for numbers you must fill, and have a lawyer read the result. A clause marked 'lawyer' depends on a statute or on the rest of the contract.")
    k.table(["Clause", "Wording to adapt", "Lawyer"], [
        ["Change control", "Any request that changes the scope, deliverables, schedule or fee is made in writing on the change request form. The evaluator will respond within [3] working days with the effect on days, fee and schedule. Work on the change begins when both parties have signed the form.", "No"],
        ["Acceptance", "Each deliverable is reviewed once. The client sends one consolidated set of comments within [5] working days of submission, and the evaluator revises within [5] working days. If no comments arrive within the period, the deliverable is treated as accepted.", "Yes"],
        ["Independence", "The client may comment on factual accuracy and clarity. The evaluator decides the findings, conclusions and recommendations, and records each comment not taken up with the reason.", "No"],
        ["Late client inputs", "If an input listed in section 5 is more than [5] working days late, the schedule moves by the same period and the evaluator may submit a change request for any added cost.", "No"],
        ["Late payment", "Each invoice is payable within [30] days of receipt. Interest on late payment is [ ]% per month.", "Yes"],
        ["Early termination", "If the client ends the assignment early, it pays for work completed to the date of notice and for costs already committed that cannot be cancelled, and the evaluator hands over the work completed to that date.", "Yes"],
        ["Data handling", "The evaluator processes personal data only on the client's documented instructions, applies the safeguards in the data management plan, and deletes or returns the data on the date stated in that plan.", "Yes"],
        ["Use of AI tools", "The evaluator may use AI tools for [drafting, translation and code]. No respondent data is entered into a tool the client has not approved, and any data that is entered is de-identified first. The methodology note states which tools were used and who checked the outputs.", "No"],
        ["Portfolio use", "The evaluator may describe the assignment in its portfolio only in the anonymised form approved in writing by the client.", "No"],
    ], [2.9, 11.4, 1.6])
    k.legal("If you are a micro or small enterprise registered on Udyam, sections 15 and 16 of the Micro, Small and Medium Enterprises Development Act, 2006 apply whatever the contract says. The buyer must pay by the agreed date, and an agreed period may not exceed 45 days from the day of acceptance or deemed acceptance. With no written agreement the limit is 15 days. After that the buyer owes compound interest with monthly rests at three times the bank rate notified by the Reserve Bank of India. A payment dispute goes to the Micro and Small Enterprises Facilitation Council under section 18, and the Supreme Court held on 31 October 2022 that an arbitration clause does not displace it (Gujarat State Civil Supplies Corporation v Mahakali Foods). The same decision held that an enterprise that was not registered on the date it entered the contract cannot claim for that contract. A buyer that pays a micro or small supplier late also loses its tax deduction for the amount (section 43B(h) of the 1961 Act). Medium enterprises and unregistered suppliers are outside the Act.")

    k.h("C2.  Payment milestone chooser")
    k.table(["Pattern", "Suits", "Risk to you"], [
        ["30 / 40 / 30 on signing, inception and final submission", "Assignments with fieldwork and a fixed scope.", "Low. The first payment covers early costs."],
        ["25 / 30 / 25 / 20 on signing, inception, draft and final, all on submission", "Assignments with several deliverables over 12 weeks or more.", "Low. Money follows the work."],
        ["20 / 40 / 40 on acceptance of inception, draft and final", "Common in a commissioner's template.", "High. You carry fieldwork cost until a client signs off, and acceptance is not in your hands."],
        ["Monthly retainer", "Open-ended advice with no single deliverable.", "Scope grows silently. Write a monthly day cap."],
        ["Single payment on delivery", "Assignments under 10 days.", "Acceptable only when the cost to you is small."],
    ], [5.6, 5.0, 5.3])
    k.body("**Cash test.** Add up what you will have spent by the end of fieldwork. Add up what you will have received by then. If the first number is larger, move a payment earlier or ask for field costs in advance.")

    k.h("C3.  Questions to ask when the client sends its own contract")
    k.numbered([
        "Which document wins if the ToR, the contract and my proposal disagree?",
        "How many rounds of comments are allowed on each deliverable, and within what period?",
        "Is payment tied to submission or to approval, and who approves?",
        "What happens if the client does not reply within the comment period?",
        "Who owns the report, the dataset and my instruments?",
        "Can the client change the findings, or only correct facts?",
        "What does the clause on 'any other tasks' allow, and how is extra work priced?",
        "Does the fee include taxes, and who issues the tax deduction certificate?",
        "What happens to payment if the client cancels midway?",
        "Is there an earnest money, performance security or penalty clause, and what are the amounts?",
    ])

    k.h("C4.  Glossary")
    k.table(["Term", "Meaning"], [
        ["Statement of work (SOW)", "The part of the contract that says what the evaluator will deliver, to what standard, by when, and for what fee."],
        ["Change request", "A written request to alter scope, deliverables, schedule or fee, with the effect on days, fee and schedule."],
        ["Deliverable", "Something handed over under the contract, such as a report, a dataset or a presentation."],
        ["Milestone payment", "A payment tied to a named submission or event."],
        ["Deemed acceptance", "A clause that treats a deliverable as accepted if the client does not respond within a fixed period."],
        ["Data fiduciary and data processor", "Terms from the Digital Personal Data Protection Act, 2023. The fiduciary decides why and how personal data is processed. The processor handles it on the fiduciary's behalf."],
        ["Tax deducted at source (TDS)", "Tax the client withholds from a payment and deposits with the tax authority. The payee claims credit for it."],
    ], [4.6, 11.3])

    k.h("C5.  Standards and sources")
    k.body("Check each source for the current version before you rely on it.")
    k.bullets([
        "Government of India (2023). The Digital Personal Data Protection Act, 2023. New Delhi: Ministry of Electronics and Information Technology.",
        "Government of India (2006). The Micro, Small and Medium Enterprises Development Act, 2006.",
        "Government of India (2017). The Central Goods and Services Tax Act, 2017, and the rules made under it.",
        "Government of India (2025). The Income-tax Act, 2025. Confirm the section numbers that replaced those of the 1961 Act.",
        "UNEG (2016). Norms and Standards for Evaluation. New York: United Nations Evaluation Group.",
    ], 10)

    # ---------------- PART D ----------------
    k.part("PART D", "Worked example: a statement of work and one change request")
    k.box("ABOUT THIS EXAMPLE", [
        "This is the evaluator's side of the Surakshit Maa case used in the ImpactMojo Terms of Reference pack: a programme working in three blocks since 2024, with a funding decision in March 2027 and a 13-week evaluation window. Names and figures are illustrative.",
        "The commissioner's pack suggests paying 20%, 40% and 40% on accepted deliverables. Here the evaluator proposes four payments on submission, with a short comment period, and the client accepts. Read the two packs side by side to see both positions.",
    ])
    k.h("1.  Parties and title")
    k.body("Client: the funding foundation. Evaluator: the evaluation team. Title: Outcome evaluation of the Surakshit Maa programme. Contract manager at the client: the programme director. Evaluator lead: the team leader. Start: week 1. End: week 13.")
    k.h("2.  Purpose and the decision served")
    k.body("To inform the foundation's board decision in March 2027 on whether to fund and scale a second phase across the wider district, by assessing whether antenatal-care completion and skilled birth attendance improved in the three programme blocks since 2024, for whom, and how much of the change can be credited to the programme.")
    k.h("3.  Scope")
    k.table(["Dimension", "In scope", "Out of scope"], [
        ["Geographic", "The three programme blocks and two matched comparison blocks.", "Other blocks and districts."],
        ["Temporal", "2024 to the date of the household survey.", "Any period after fieldwork ends."],
        ["Thematic", "Antenatal care, skilled birth attendance, the effect of the labour-room upgrades, and sustainability of the state support.", "Clinical quality audit of the eight facilities, cost-effectiveness analysis, and the design of a second phase."],
        ["Population", "Women who delivered in the 12 months before the survey, ASHAs and facility staff.", "Men's health, and children beyond the newborn period."],
        ["Other tasks", "None unless agreed through section 10.", "Any task not listed in section 4."],
    ], [3.0, 6.7, 6.2])
    k.h("4.  Deliverables and schedule")
    k.table(["Deliverable", "Format and length", "Review", "Comment period", "Due (week)"], [
        ["Inception report with evaluation matrix", "Word, up to 25 pages", "1 round", "5 working days", "3"],
        ["Fieldwork completion note", "2 pages", "None", "None", "8"],
        ["Draft report", "Word, up to 40 pages plus annexes", "1 round", "5 working days", "11"],
        ["Validation workshop", "Half day, with slides", "None", "None", "11 to 12"],
        ["Final report and two-page brief", "Word and PDF", "None", "None", "12"],
        ["Cleaned dataset, codebook and scripts", "CSV, PDF and code files", "None", "None", "13"],
    ], [4.6, 4.2, 2.0, 2.9, 2.2])
    k.body("Note on the calendar: the 13-week window leaves five working days between the draft and the final report. The comment period is therefore five working days. Each day the client takes beyond that moves the final date by one day.")
    k.h("8.  Fees and payment milestones")
    k.body("Total fee: ₹39,60,000, inclusive of field costs and all taxes, on a daily-rate basis with the staffing table in the proposal.")
    k.table(["Milestone", "Trigger", "Share", "Amount (₹)", "Payable within"], [
        ["On signing", "Signed contract", "25%", "9,90,000", "15 days"],
        ["Inception", "Submission of inception report", "30%", "11,88,000", "15 days"],
        ["Draft", "Submission of draft report", "25%", "9,90,000", "15 days"],
        ["Final", "Submission of final report and dataset", "20%", "7,92,000", "15 days"],
        ["Total", "", "100%", "39,60,000", ""],
    ], [2.5, 6.0, 1.9, 2.8, 2.7])
    k.body("Cash test for the example: by the end of fieldwork in week 8 the evaluator has received 55% of the fee (signing plus inception), which covers enumerator and travel costs. Under the 20 / 40 / 40 pattern on acceptance it would have received 20%.")
    k.h("A change request in use")
    k.body("After the inception report is approved, the client asks for a separate analysis of Scheduled Tribe households in all three blocks. The evaluator fills in the form below. The client signs within a week.")
    k.table(["Field", "Entry"], [
        ["Change request number and date", "CR-01, week 4"],
        ["Raised by", "Client"],
        ["Description", "Add an oversample of 150 Scheduled Tribe households and a separate analysis of their antenatal-care and delivery outcomes."],
        ["Why it is needed", "The funder's board wants to know whether the gains reached tribal households in the hill block."],
        ["Effect on scope", "Added: oversample and subgroup analysis. Nothing removed."],
        ["Effect on deliverables", "One additional chapter in the draft and final reports."],
        ["Effect on days", "Team leader 1, senior researcher 2, analyst 4. Field team: 150 additional completed surveys."],
        ["Effect on fee", "₹1,20,000 on the same inclusive basis as the main fee: 150 surveys at ₹300 = ₹45,000; analyst 4 days at ₹5,500 = ₹22,000; senior researcher 2 days at ₹14,000 = ₹28,000; team leader 1 day at ₹25,000 = ₹25,000."],
        ["Effect on schedule", "None. The oversample runs inside the fieldwork weeks 5 to 8."],
        ["Effect on risk", "Fieldwork in the hill block is slightly longer. Logged in the risk table."],
        ["Decision", "Accepted as priced, week 5."],
    ], [4.6, 11.3])
    k.figures("The day rates and the survey cost in this example are round numbers that sit inside the indicative ranges in the ImpactMojo Terms of Reference pack. Those ranges give orders of magnitude and are no basis for a quote. Replace each with your own.")
    k.save(path)


if __name__ == "__main__":
    import sys
    build(sys.argv[1])

# -*- coding: utf-8 -*-
"""
BRSR & Sustainability Reporting 101: ImpactMojo 101 Series (native deck spec)
India's Business Responsibility and Sustainability Report, for people who prepare one and people who read one.
Build: python3 scripts/deck-builder/build.py brsr_reporting

Facts as of 9 October 2026. Sources opened while writing:
- SEBI (LODR) Regulations 2015, as last amended 14 July 2026, Reg 3(2), Reg 34(2)(f) and footnotes 380-383:
  https://www.sebi.gov.in/legal/regulations/jul-2026/securities-and-exchange-board-of-india-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-july-14-2026-_102974.html
- SEBI circular SEBI/HO/CFD/CMD-2/P/CIR/2021/562, 10 May 2021, paras 1-7:
  https://www.sebi.gov.in/legal/circulars/may-2021/business-responsibility-and-sustainability-reporting-by-listed-entities_50096.html
- SEBI circular CIR/CFD/DIL/8/2012, 13 August 2012 (NSE copy): https://nsearchives.nseindia.com/content/equities/SEBI_Circ_13082012_3.pdf
- SEBI circular SEBI/HO/CFD/CFD-SEC-2/P/CIR/2023/122, 12 July 2023, BRSR Core (annexures read from the full
  52-page copy; the same format is Annexure 17A of the LODR Master Circular)
- SEBI circular SEBI/HO/CFD/CFD-PoD-1/P/CIR/2024/177, 20 December 2024, industry standards on BRSR Core,
  and the Industry Standards Note (BSE notice 20241220-67), Part A and Annexure I
- SEBI circular SEBI/HO/CFD/CFD-PoD-1/P/CIR/2025/42, 28 March 2025 (assessment or assurance, value chain,
  green credits):
  https://www.sebi.gov.in/legal/circulars/mar-2025/measures-to-facilitate-ease-of-doing-business-with-respect-to-framework-for-assurance-or-assessment-esg-disclosures-for-value-chain-and-introduction-of-voluntary-disclosure-on-green-credits_93102.html
- SEBI LODR Master Circular, updated 30 January 2026, Section IV-B and Annexures 16, 17 and 17A (BRSR format,
  guidance note and BRSR Core)
- Central Electricity Authority, CO2 Baseline Database for the Indian Power Sector, User Guide Version 21.0,
  November 2025, Table S and Annexure I
- GHG Protocol Corporate Standard (revised edition), ch. 4; Scope 2 Guidance (2015); Scope 3 Standard (2011);
  IPCC Global Warming Potential Values v2.0 (7 August 2024); blog of 1 August 2025 on revisions
- IPCC AR5 WG1 Table 8.7 and AR6 WG1 Table 7.15; IPCC 2006 Guidelines Vol. 2, Tables 1.2 and 2.2
- Regulation (EU) 2023/956 (CBAM) and Regulation (EU) 2025/2083
- IFRS S1 and S2 (ifrs.org); GRI Universal Standards 2021 (globalreporting.org)
- Delegated Regulation (EU) 2023/2772, ESRS 1 paras 37, 43, 49
- Companies Act 2013, s135(1) and (5)
All figures for "Company X" are invented for teaching and labelled as such on the slides.
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


def Q(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def DIV(num, word, title):
    return {"type": "divider", "num": num, "label": "Section " + word, "title": title}


def L(path, name):
    return '<a href="/101-courses/' + path + '">' + name + '</a>'


def EX(question, working, answer):
    """A calculation exercise: the question, the working and the answer."""
    return TC([P("amber", "Exercise", question)],
              [P("green", "Working", working), H("cyan", answer)])


ILL = '<span class="tag" style="font-size:0.7rem">Illustrative figures</span> '
MC = "SEBI LODR Master Circular, updated 30 January 2026"
C2021 = "SEBI circular of 10 May 2021"
C2023 = "SEBI circular of 12 July 2023 (BRSR Core)"
C2025 = "SEBI circular of 28 March 2025"
ISF = "Industry Standards Note on BRSR Core, December 2024"
CEA = "CEA CO2 Baseline Database, Version 21.0, November 2025"

DECK = {
    "slug": "brsr-reporting",
    "title": "BRSR &amp; Sustainability Reporting 101",
    "description": ("BRSR & Sustainability Reporting 101: a free foundational course on India's Business "
                    "Responsibility and Sustainability Report, for people who prepare one and people who read "
                    "one. Who must file, Sections A, B and C, the nine NGRBC principles, BRSR Core and the 2025 "
                    "move to assessment or assurance, greenhouse gas accounting with the CEA grid factor and "
                    "PPP-adjusted intensity, energy, water, waste, people metrics, value chain and green credits, "
                    "materiality, GRI, ISSB and CBAM, with worked calculation exercises. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "BRSR &amp;<br>Sustainability<br>Reporting 101",
         "sub": "How India's listed companies report on environment, people and governance, how to calculate "
                "the numbers, and how to read them critically",
         "tags": ["100 Slides", "Calculation Exercises", "SEBI Rules to October 2026", "Free Forever"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "What the BRSR is and why it exists"},
             {"name": "Who must file, and from when"},
             {"name": "Sections A, B and C and the nine principles"},
             {"name": "BRSR Core and assessment or assurance"},
             {"name": "Greenhouse gas accounting"},
             {"name": "Energy, water and waste"},
             {"name": "Employees, communities and customers"},
             {"name": "Value chain and green credits"},
             {"name": "Materiality and the global frameworks"},
             {"name": "Reading a BRSR critically"},
             {"name": "A full worked case and where next"},
         ]},

        # ===================== SECTION 01 =====================
        DIV("01", "One", "What the BRSR is and why it exists"),

        S("Starting point", "Why a company reports on more than its accounts", [
            B("A company's annual accounts say how much it earned and what it owns. They say little about "
              "how much water its plants draw from a stressed aquifer, how many workers were injured last "
              "year, or how much of its electricity came from coal. Investors, lenders, buyers, regulators "
              "and the communities near a factory all have reasons to want those numbers, and before 2012 "
              "Indian listed companies had no obligation to publish them in a common format."),
            Q("Reporting of company's performance on sustainability related factors has become as vital as "
              "reporting on financial and operational performance.",
              "SEBI, circular introducing the BRSR, 10 May 2021, para 1"),
            H("cyan", "The Business Responsibility and Sustainability Report (BRSR) is SEBI's answer: one "
              "format, with numbers that can be compared across companies, sectors and years."),
        ]),

        S("Who uses it", "Two kinds of people use a BRSR, and this course is for both", [
            TC([P("indigo", "People who prepare it",
                  "Sustainability and finance teams in listed companies, the consultants who help them, and "
                  "the providers who assess or assure the figures. They need to know what each question asks "
                  "for, which method to use, and how to calculate it correctly.")],
               [P("green", "People who read it",
                  "Investors and lenders, NGOs approaching a company for CSR partnerships, researchers, "
                  "journalists, employees and suppliers. They need to know where to look, what a figure "
                  "means, and when a number should be questioned.")]),
            B("SEBI's own statement of purpose names investors first: the disclosures are meant to help them "
              "\"make better investment decisions\" and to let companies \"engage more meaningfully with their "
              "stakeholders\" (circular of 10 May 2021, para 5)."),
            H("amber", "Each section ends with a calculation or a reading exercise. Work it before you look at "
              "the answer column."),
        ]),

        S("History", "From voluntary guidelines to a mandatory report", [
            T(["Date", "What happened", "Source"],
              [["July 2011", "Ministry of Corporate Affairs issues the National Voluntary Guidelines (NVGs) on "
                "social, environmental and economic responsibilities of business", "SEBI circular of 13 Aug 2012"],
               ["13 August 2012", "Business Responsibility Report (BRR) made mandatory for the top 100 listed "
                "companies, through Clause 55 of the Listing Agreement", "SEBI circular CIR/CFD/DIL/8/2012"],
               ["4 November 2015", "SEBI prescribes the BRR format under the LODR Regulations",
                "SEBI circular CIR/CFD/CMD/10/2015"],
               ["March 2019", "National Guidelines on Responsible Business Conduct (NGRBC) revise the NVGs",
                "Ministry of Corporate Affairs"],
               ["5 and 10 May 2021", "LODR amended; BRSR format issued; voluntary for FY 2021-22, mandatory "
                "for the top 1,000 from FY 2022-23", C2021],
               ["12 July 2023", "BRSR Core introduced, with a timetable for independent checking", C2023],
               ["28 March 2025", "\"Assessment or assurance\"; value chain made voluntary; green credits added",
                C2025]]),
            H("cyan", "The BRSR replaced the BRR from FY 2022-23 for the companies it covers."),
        ], compact=True),

        S("Definition", "What the BRSR is, in the words of the regulation", [
            TERM("Business Responsibility and Sustainability Report",
                 "\"A Business Responsibility and Sustainability Report on the environmental, social and "
                 "governance disclosures, in the format as may be specified by the Board from time to time\", "
                 "which the top one thousand listed entities include in their annual report. SEBI (LODR) "
                 "Regulations 2015, Regulation 34(2)(f)."),
            B("Three points follow from the text. The BRSR is part of the <strong>annual report</strong>, so it "
              "is published once a year with the accounts. The <strong>format is set by SEBI</strong> through "
              "circulars, which is why changes arrive by circular. And it covers <strong>environmental, social "
              "and governance</strong> matters together, using the nine principles of the NGRBC as its "
              "skeleton."),
            H("indigo", "When this course quotes the format, it quotes Annexure 16 of the LODR Master Circular "
              "(updated 30 January 2026), which holds the current version."),
        ]),

        S("Three terms", "BRSR, CSR and ESG are different things", [
            T(["Term", "What it is", "Legal basis", "Who it applies to"],
              [["CSR", "An obligation to spend at least 2% of average net profits of the previous three years "
                "on listed activities", "Companies Act 2013, s135",
                "Companies with net worth of Rs 500 crore or more, turnover of Rs 1,000 crore or more, or net "
                "profit of Rs 5 crore or more in the previous year, listed or not"],
               ["BRSR", "A disclosure in a set format on environmental, social and governance performance",
                "SEBI LODR Reg 34(2)(f)", "The top 1,000 listed companies; others may file voluntarily"],
               ["ESG", "A general label used by investors for environmental, social and governance factors",
                "No single legal definition", "Used loosely; read what each user means by it"]]),
            B("The two obligations overlap without coinciding. An unlisted company can owe CSR and file no BRSR; "
              "a listed company in the top 1,000 files a BRSR whatever its CSR spending. The BRSR does ask about "
              "CSR, in Section A, Part VI.", sm=True),
            H("green", "For the CSR side in detail, see " + L("csr-esg.html", "CSR &amp; ESG 101") + "."),
        ]),

        S("Limits", "What a BRSR can tell you, and what it cannot", [
            TC([P("green", "What it can tell you",
                  "What the company says it did, in a standard format, for two years side by side. Where to "
                  "find the policy behind each principle. Whether the BRSR Core figures were independently "
                  "assessed or assured, and by whom (Section A, points 14 and 15).")],
               [P("red", "What it cannot tell you",
                  "Whether the figures outside BRSR Core were checked by anyone. Whether a community near the "
                  "plant agrees with the company's account of it. Whether the company's targets are adequate. "
                  "Leadership indicators are voluntary, so a blank tells you only that the company chose not "
                  "to answer.")]),
            H("amber", "Treat a BRSR as the company's own statement, made in a regulated format. Its value rises "
              "with independent checking and with comparison against other sources."),
        ]),

        S("How to use this course", "Method, sources and one illustrative company", [
            BL(["Every rule is stated as it stood on <strong>9 October 2026</strong>, with the SEBI circular or "
                "regulation it comes from. SEBI changes the format by circular, so check for later ones.",
                "Calculation exercises use <strong>Company X</strong>, an invented listed manufacturer. Its "
                "figures are illustrative and are labelled so on every slide where they appear.",
                "Emission factors and conversion values are real and sourced: the CEA grid factor, IPCC "
                "default factors and the IPCC global warming potentials.",
                "Short names for the nine principles in this course are paraphrases. The NGRBC itself gives only "
                "the full statements, which Section 03 quotes."]),
            ST([C("Rs 5,000 cr", "Company X revenue from operations (illustrative)", "amber"),
                C("Top 1,000", "listed companies that must file a BRSR", "cyan", "SEBI LODR Reg 34(2)(f)"),
                C("9", "NGRBC principles that structure Section C", "indigo", MC)], cols=3),
        ]),

        # ===================== SECTION 02 =====================
        DIV("02", "Two", "Who must file, and from when"),

        S("The rule", "Regulation 34(2)(f) as it reads in 2026", [
            Q("for the top one thousand listed entities based on market capitalization, a Business "
              "Responsibility and Sustainability Report on the environmental, social and governance disclosures, "
              "in the format as may be specified by the Board from time to time",
              "SEBI (LODR) Regulations 2015, Reg 34(2)(f), as last amended 14 July 2026"),
            BL(["<strong>First proviso:</strong> \"the assessment or assurance of the specified parameters as per "
                "the Business Responsibility and Sustainability Report Core shall be obtained, with effect from and "
                "in the manner as may be specified by the Board\".",
                "<strong>Second proviso:</strong> extends the same approach to disclosures about the value chain.",
                "<strong>Third proviso:</strong> the remaining listed entities, including those on SME exchanges, "
                "\"may voluntarily disclose\"."]),
            H("cyan", "The words \"assessment or assurance\" replaced \"assurance\" with effect from 28 March 2025."),
        ]),

        S("Ranking", "How the top 1,000 is counted now", [
            B("Until the end of 2024, market capitalisation for this purpose was taken as on 31 March. That "
              "explanation was omitted with effect from 31 December 2024. Under Regulation 3(2), the stock "
              "exchanges now rank listed entities \"on the basis of their average market capitalisation from 1st "
              "July to 31st December\" of each year, and the first such list was drawn up as on 31 December 2024."),
            TC([P("indigo", "Why the change matters",
                  "An average over six months is harder to move with a few days of share-price swings, so fewer "
                  "companies slip in and out of the list by chance.")],
               [P("amber", "A company that enters the list",
                  "Under the LODR, a newly covered entity is given time to put systems in place: it must comply "
                  "from 1 April or the start of the next financial year, whichever is later.")]),
            H("green", "To check whether a company is covered, use the list each exchange publishes, and note "
              "the date it was drawn up."),
        ]),

        S("Timeline", "When the BRSR became compulsory", [
            ST([C("FY 2021-22", "BRSR voluntary for the top 1,000", "cyan", C2021 + ", para 7"),
                C("FY 2022-23", "BRSR mandatory for the top 1,000; replaces the BRR", "green", C2021 + ", para 7"),
                C("FY 2023-24", "BRSR Core assessment or assurance begins with the top 150", "indigo",
                  C2023)], cols=3),
            Q("with effect from the financial year 2022-2023, filing of BRSR shall be mandatory for the top 1000 "
              "listed companies (by market capitalization) and shall replace the existing BRR. Filing of BRSR is "
              "voluntary for the financial year 2021-22.",
              "SEBI circular SEBI/HO/CFD/CMD-2/P/CIR/2021/562, 10 May 2021, para 7"),
        ]),

        S("Indicators", "Essential indicators are compulsory; leadership indicators are voluntary", [
            Q("The essential indicators are required to be reported on a mandatory basis while the reporting of "
              "leadership indicators is on a voluntary basis. Listed entities should endeavor to report the "
              "leadership indictors also.",
              "SEBI circular of 10 May 2021, para 4 (spelling as in the original)"),
            TC([P("green", "Essential indicators",
                  "Energy, water, Scope 1 and 2 emissions, waste, safety incidents, wages, complaints, CSR "
                  "details and similar. Every covered company must answer.")],
               [P("amber", "Leadership indicators",
                  "Scope 3 emissions, facilities in areas of water stress, life-cycle assessments, green "
                  "credits and similar. A company may leave them blank.")]),
            H("indigo", "When you compare companies, compare essential indicators first. A leadership indicator "
              "answered by one company and skipped by another cannot be compared."),
        ]),

        S("Other frameworks", "A BRSR can point to a report made under another framework", [
            Q("The listed entities already preparing and disclosing sustainability reports based on "
              "internationally accepted reporting frameworks (such as GRI, SASB, TCFD or Integrated Reporting) "
              "may cross-reference the disclosures made under such framework to the disclosures sought under the "
              "BRSR.", "SEBI circular of 10 May 2021, para 6"),
            B("Cross-referencing saves duplicated work. It also means a reader sometimes has to open a second "
              "document to find a figure. If a BRSR cell says \"refer to the sustainability report, page 54\", "
              "go there and check that the figure covers the same boundary and the same year."),
            H("cyan", "Section 09 covers GRI and the ISSB standards in more detail."),
        ]),

        S("Voluntary filers", "Who else may file a BRSR", [
            BL(["<strong>Listed entities outside the top 1,000</strong>, including those on SME exchanges, may file "
                "voluntarily under the third proviso to Reg 34(2)(f).",
                "<strong>High value debt listed entities</strong>, which have listed debt securities above a "
                "threshold set in the LODR, \"may provide in the annual report, a Business Responsibility and "
                "Sustainability Report\" under Regulation 62Q(3).",
                "<strong>Unlisted companies</strong> have no BRSR obligation under SEBI's rules. Some publish "
                "sustainability reports under GRI or other frameworks because buyers or lenders ask for them."]),
            H("amber", "A voluntary BRSR is still a BRSR, with the same format. Read it with the same care, and "
              "check whether any figure was independently checked."),
        ]),

        S("What changed", "The three big changes since 2021, on one slide", [
            T(["Year", "Change", "What it means for preparers", "What it means for readers"],
              [["2023", "BRSR Core: 9 attributes with defined KPIs and a timetable for independent checking",
                "Some figures must be checked by an outside provider", "These figures are more reliable than the rest"],
               ["2025", "\"Assurance\" became \"assessment or assurance\"; the word \"reasonable\" dropped",
                "Choice of provider widens beyond one profession", "Look at Section A, point 15 to see which was obtained"],
               ["2025", "Value chain disclosures made voluntary and the threshold changed; green credits added as "
                "a voluntary leadership indicator", "Less compulsory work on suppliers",
                "Many companies will not report the value chain; check the coverage stated"]]),
            H("cyan", "Sources: " + C2023 + "; " + C2025 + "."),
        ], compact=True),

        S("Exercise", "Does this company have to file, and must its Core figures be checked?", [
            B(ILL + "Use the rules on the previous slides. The BRSR Core timetable is in Section 04: top 150 from "
              "FY 2023-24, top 250 from FY 2024-25, top 500 from FY 2025-26, top 1,000 from FY 2026-27."),
            T(["Company", "Facts", "Answer"],
              [["A", "Listed; ranked 640 on average market capitalisation",
                "Must file a BRSR. BRSR Core assessment or assurance applies from FY 2026-27, when the top 1,000 "
                "are covered."],
               ["B", "Unlisted; turnover Rs 2,000 crore",
                "No BRSR obligation under SEBI's rules. It owes CSR under s135, because its turnover exceeds "
                "Rs 1,000 crore."],
               ["C", "Listed on an SME exchange", "May file voluntarily; not obliged."],
               ["D", "Listed; ranked 180", "Must file. Core assessment or assurance from FY 2024-25, when the "
                "top 250 are covered."]]),
        ]),

        # ===================== SECTION 03 =====================
        DIV("03", "Three", "Sections A, B and C and the nine principles"),

        S("Structure", "Every BRSR has three sections", [
            T(["Section", "Title in the format", "What it holds"],
              [["A", "General disclosures", "Who the company is: listing details, products, operations, "
                "employees, subsidiaries, CSR, and complaints and material issues"],
               ["B", "Management and process disclosures", "Policies against each of the nine principles, who "
                "approved them, and who oversees them"],
               ["C", "Principle wise performance disclosure", "The numbers and answers, principle by principle, "
                "split into essential and leadership indicators"]]),
            Q("the essential indicators are expected to be disclosed by every entity that is mandated to file this "
              "report, the leadership indicators may be voluntarily disclosed",
              "BRSR format, preamble to Section C (" + MC + ", Annexure 16)"),
        ]),

        S("Section A", "The seven parts of Section A", [
            T(["Part", "Heading in the format", "Useful for"],
              [["I", "Details of the listed entity", "Name, CIN, contact, reporting boundary (point 13), "
                "assessment or assurance provider (points 14 and 15)"],
               ["II", "Products/services", "What the company makes and where it sells"],
               ["III", "Operations", "Number of plants and offices, markets served"],
               ["IV", "Employees", "Headcount by gender, permanent and other, differently abled, turnover rate"],
               ["V", "Holding, Subsidiary and Associate Companies", "Which group entities take part in the "
                "company's business responsibility initiatives"],
               ["VI", "CSR Details", "Whether s135 applies, turnover and net worth"],
               ["VII", "Transparency and Disclosures Compliances", "Complaints from stakeholder groups and the "
                "material issues (question 26)"]]),
            H("amber", "Read point 13 first. It says whether the report covers the company alone (standalone) or "
              "the whole group (consolidated), and every figure that follows depends on it."),
        ], compact=True),

        S("Section A, question 26", "The question that asks what the company considers material", [
            Q("Please indicate material responsible business conduct and sustainability issues pertaining to "
              "environmental and social matters that present a risk or an opportunity to your business, rationale "
              "for identifying the same, approach to adapt or mitigate the risk along-with its financial "
              "implications",
              "BRSR format, Section A, question 26 (" + MC + ", Annexure 16)"),
            B("The table under the question asks, for each issue, whether it is a risk or an opportunity (R/O), "
              "the reason it was identified, the company's approach, and its financial implications, positive or "
              "negative. The format does not say whether the company should judge materiality by its effect on "
              "the business, its effect on people and the environment, or both. Section 09 returns to this."),
            H("indigo", "For a reader, question 26 is the company's own list of what matters. Compare it with what "
              "you know of the sector, and note what is missing."),
        ]),

        S("Section B", "Section B asks about policies and who oversees them", [
            B("Section B is a grid with one column for each of the nine principles. Its first group of questions, "
              "\"Policy and management processes\", asks whether the company's policies cover each principle and "
              "its core elements, whether the Board approved them, whether the policies extend to the value chain, "
              "which national and international standards the company follows, and what specific commitments, "
              "goals and targets it has set."),
            TC([P("cyan", "Governance questions",
                  "A statement from the director responsible for the report; the highest authority responsible "
                  "for the business responsibility policies; whether a Board committee oversees sustainability.")],
               [P("amber", "What to look for",
                  "Targets with a baseline year, a number and a deadline. The format's guidance on questions 5 "
                  "and 6 asks for baseline, coverage, expected result and timeline for each goal.")]),
            H("green", "A policy that exists and a policy that changes behaviour are different. Section B shows "
              "the first; Section C shows whether there are results."),
        ]),

        S("Section C", "Section C is where the numbers are", [
            B("Section C takes each principle in turn and asks a set of essential indicators followed by "
              "leadership indicators. Most of the figures that analysts, journalists and rating agencies quote "
              "come from here: energy and emissions under Principle 6, safety and wages under Principles 3 and 5, "
              "sourcing from small producers under Principle 8, customer complaints and data breaches under "
              "Principle 9, and payment days and related-party concentration under Principle 1."),
            FL(["Principle statement", "Essential indicators (compulsory)", "Leadership indicators (voluntary)",
                "Notes on independent assessment"]),
            H("cyan", "Each table in Section C asks for the current and the previous financial year. Always read "
              "both columns."),
        ]),

        S("The principles", "Principles 1 to 5, as printed in the BRSR", [
            T(["", "Principle statement"],
              [["P1", "Businesses should conduct and govern themselves with integrity, and in a manner that is "
                "Ethical, Transparent and Accountable"],
               ["P2", "Businesses should provide goods and services in a manner that is sustainable and safe"],
               ["P3", "Businesses should respect and promote the well-being of all employees, including those in "
                "their value chains"],
               ["P4", "Businesses should respect the interests of and be responsive to all its stakeholders"],
               ["P5", "Businesses should respect and promote human rights"]]),
            H("indigo", "Source: BRSR format, " + MC + ", Annexure 16, taking the principles from the National "
              "Guidelines on Responsible Business Conduct (Ministry of Corporate Affairs, March 2019)."),
        ]),

        S("The principles", "Principles 6 to 9, as printed in the BRSR", [
            T(["", "Principle statement"],
              [["P6", "Businesses should respect and make efforts to protect and restore the environment"],
               ["P7", "Businesses, when engaging in influencing public and regulatory policy, should do so in a "
                "manner that is responsible and transparent"],
               ["P8", "Businesses should promote inclusive growth and equitable development"],
               ["P9", "Businesses should engage with and provide value to their consumers in a responsible "
                "manner"]]),
            B("This course uses short labels such as \"P6, environment\" for convenience. They are paraphrases; the "
              "NGRBC itself gives only the full statements above.", sm=True),
            B("Principle 7 is often answered in a few lines. Its essential indicators ask for the number of trade and industry associations the company belongs to, the ten largest of them, and any corrective action on anti-competitive conduct ordered by a regulator. Its leadership indicator asks for the public policy positions the company advocated, and by what method. The list of associations is a starting point for asking what positions those bodies took.", sm=True),
        ]),

        S("Where the numbers sit", "Which principle holds which figure", [
            T(["Figure", "Principle", "Type"],
              [["Energy, water, Scope 1 and 2 emissions, waste", "P6", "Essential"],
               ["Scope 3 emissions; facilities in water-stressed areas; green credits", "P6", "Leadership"],
               ["Wellbeing spending; lost-time injury frequency rate; retirement benefits", "P3", "Essential"],
               ["Gross wages paid to women; complaints under the POSH Act", "P5", "Essential"],
               ["Inputs sourced from MSMEs and small producers; social impact assessments", "P8", "Essential"],
               ["Days of accounts payable; concentration of purchases and sales", "P1", "Essential"],
               ["Consumer complaints; data breaches", "P9", "Essential"]]),
            H("amber", "POSH means the Sexual Harassment of Women at Workplace (Prevention, Prohibition and "
              "Redressal) Act 2013, under which the format asks for complaints filed and resolved."),
        ], compact=True),

        S("Exercise", "Match the item to its principle", [
            EX("Without looking back, name the principle under which a BRSR reports each item: "
               "(1) groundwater withdrawn by a plant; (2) complaints under the POSH Act; (3) the share of inputs "
               "bought from MSMEs; (4) the number of days the company takes to pay its suppliers; (5) customer data "
               "breaches; (6) the lost-time injury frequency rate.",
               "Use the table on the previous slide. Water and other environmental figures sit with P6; employee "
               "safety with P3; human rights, including gender pay and harassment, with P5; small producers and "
               "communities with P8; ethics and fair dealing with suppliers with P1; consumers with P9.",
               "Answers: (1) P6, (2) P5, (3) P8, (4) P1, (5) P9, (6) P3."),
        ]),

        # ===================== SECTION 04 =====================
        DIV("04", "Four", "BRSR Core and assessment or assurance"),

        S("What it is", "BRSR Core: a smaller set of figures that must be checked", [
            Q("a set of Key Performance Indicators (KPIs) / metrics under 9 ESG attributes",
              "SEBI circular of 12 July 2023, para 3.1, describing BRSR Core"),
            B("BRSR Core is a subset of the BRSR. It picks the figures SEBI considers most important, defines how "
              "each is to be measured, and requires an outside provider to assess or assure them on a timetable. "
              "The same circular added new indicators, among them \"job creation in small towns, open-ness of "
              "business, gross wages paid to women\", and introduced intensity ratios \"based on revenue adjusted "
              "for Purchasing Power Parity (PPP)\" for better global comparability."),
            H("cyan", "For a reader, BRSR Core figures are the ones with an outside check behind them, once the "
              "company is inside the timetable."),
        ]),

        S("Nine attributes", "The nine attributes of BRSR Core", [
            T(["#", "Attribute, as named in Annexure I of the 2023 circular"],
              [["1", "Green-house gas (GHG) footprint"],
               ["2", "Water footprint"],
               ["3", "Energy footprint"],
               ["4", "Embracing circularity: details related to waste management by the entity"],
               ["5", "Enhancing Employee Wellbeing and Safety"],
               ["6", "Enabling Gender Diversity in Business"],
               ["7", "Enabling Inclusive Development"],
               ["8", "Fairness in Engaging with Customers and Suppliers"],
               ["9", "Open-ness of business"]]),
            H("indigo", "Attribute 1 notes that emissions may be measured under the GHG Protocol Corporate "
              "Accounting and Reporting Standard. Scope 3 is not part of BRSR Core."),
        ], compact=True),

        S("The KPIs", "What each attribute measures: attributes 1 to 5", [
            T(["Attribute", "Key figures"],
              [["1. GHG footprint", "Total Scope 1; total Scope 2; Scope 1 and 2 intensity per rupee of revenue "
                "adjusted for PPP, and per unit of output"],
               ["2. Water footprint", "Water consumption and its intensity; water discharge by destination and "
                "level of treatment"],
               ["3. Energy footprint", "Total energy consumed; share from renewable sources; energy intensity"],
               ["4. Circularity", "Waste generated by category and its intensity; waste recovered; waste disposed"],
               ["5. Wellbeing and safety", "Spending on employee and worker wellbeing as a share of revenue; "
                "safety incidents, including the lost-time injury frequency rate and fatalities"]]),
            H("cyan", "Source: " + C2023 + ", Annexure I; now Annexure 17A of the " + MC + "."),
        ], compact=True),

        S("The KPIs", "What each attribute measures: attributes 6 to 9", [
            T(["Attribute", "Key figures"],
              [["6. Gender diversity", "Gross wages paid to women as a share of total wages; complaints under "
                "the POSH Act"],
               ["7. Inclusive development", "Inputs sourced from MSMEs and small producers and from within India; "
                "wages paid to people employed in smaller towns as a share of total wage cost"],
               ["8. Fairness with customers and suppliers", "Customer data breaches as a share of all data breaches "
                "or cyber security events; number of days of accounts payable"],
               ["9. Open-ness of business", "Concentration of purchases and sales with trading houses, dealers and "
                "related parties; loans, advances and investments with related parties"]]),
            H("amber", "Attributes 8 and 9 surprise people who think of ESG as environment only. Paying small "
              "suppliers late and routing sales through related parties are governance questions SEBI chose to "
              "check."),
        ], compact=True),

        S("Timetable", "Who needs BRSR Core assessment or assurance, and from when", [
            T(["Financial year", "Listed entities covered (by market capitalisation)"],
              [["2023-24", "Top 150"], ["2024-25", "Top 250"], ["2025-26", "Top 500"], ["2026-27", "Top 1,000"]]),
            B("The 28 March 2025 circular left this table unchanged; it is the same in the LODR Master Circular "
              "updated on 30 January 2026. What changed was the obligation's wording, from \"mandatorily "
              "undertake reasonable assurance of the BRSR Core\" (2023, para 3.4.2) to \"mandatorily undertake "
              "assessment or assurance of the BRSR Core\" (2025, para 2.4.2)."),
            H("green", "FY 2026-27 is the first year in which every company that must file a BRSR must also have "
              "its Core figures independently checked."),
        ]),

        S("Assessment or assurance", "What \"assessment\" means, and why it was added", [
            Q("'assessment' refers to third-party assessment undertaken as per the standards developed by the "
              "Industry Standards Forum (ISF) in consultation with SEBI.",
              "SEBI circular of 28 March 2025"),
            BL(["The stated aim was to \"make the process profession agnostic\": before 2025, \"assurance\" was "
                "associated with chartered accountants' assurance standards.",
                "The Industry Standards Forum comprises representatives of three industry associations, ASSOCHAM, "
                "CII and FICCI, \"under the aegis of the Stock Exchanges\" (circular of 20 December 2024).",
                "Since FY 2024-25, listed entities must follow the ISF's industry standards when reporting BRSR "
                "Core (circular of 20 December 2024)."]),
            H("cyan", "Section A, point 15 now reads \"Type of assessment or assurance obtained\". Look there to "
              "see which route the company took."),
        ]),

        S("Independence", "Who may assess or assure, and the conflict rule", [
            B("The 2025 circular names no single profession. It places the burden on the Board, which \"shall "
              "ensure that the assessment or assurance provider of the BRSR Core has the necessary expertise\". "
              "It also sets an independence rule: the provider and its associates must not \"sell its products or "
              "provide any non-audit / non-assessment / non-assurance related service including consulting "
              "services, to the listed entity or its group entities\"."),
            TC([P("amber", "For preparers",
                  "The consultant who helped prepare your BRSR cannot also assess or assure its Core figures. "
                  "Plan the two roles separately.")],
               [P("green", "For readers",
                  "Section A, point 14 names the provider. A reader can check whether the same firm appears as "
                  "an adviser elsewhere in the annual report.")]),
        ]),

        S("Exercise", "From which year must each company's Core figures be checked?", [
            EX(ILL + "Four listed companies, ranked on average market capitalisation: E is 120th, F is 240th, "
               "G is 470th, H is 910th. For each, give the first financial year in which BRSR Core assessment or "
               "assurance is compulsory.",
               "Find the first row of the timetable whose coverage includes the company's rank: top 150 from "
               "FY 2023-24, top 250 from FY 2024-25, top 500 from FY 2025-26, top 1,000 from FY 2026-27. A rank "
               "can change from year to year, so in practice check the list for each year.",
               "E: FY 2023-24. F: FY 2024-25. G: FY 2025-26. H: FY 2026-27."),
        ]),

        # ===================== SECTION 05 =====================
        DIV("05", "Five", "Greenhouse gas accounting"),

        S("Why first", "Emissions are the figure most often quoted and most often miscalculated", [
            B("BRSR Principle 6 asks every covered company for total Scope 1 and Scope 2 emissions in tonnes of "
              "CO2 equivalent, and their intensity per rupee of turnover, per rupee adjusted for PPP, and "
              "optionally per unit of output. Scope 3 emissions and their intensity are a leadership indicator. "
              "Scope 1 and 2 are also BRSR Core attribute 1, so they must be independently checked on the "
              "timetable."),
            FL(["Activity data (litres, tonnes, MWh)", "Emission factor (kg CO2 per unit)",
                "Global warming potential (for non-CO2 gases)", "Tonnes of CO2 equivalent"]),
            H("cyan", "The arithmetic is multiplication. The errors are in the inputs: wrong units, wrong factor, "
              "wrong year, missing sites."),
        ]),

        S("Definitions", "Scope 1, Scope 2 and Scope 3 in the GHG Protocol", [
            T(["Scope", "Definition in the GHG Protocol Corporate Standard (ch. 4)", "Example for a factory"],
              [["1", "\"Direct GHG emissions occur from sources that are owned or controlled by the company\"",
                "Diesel burnt in its own generators and boilers; LPG in its canteen"],
               ["2", "\"Emissions from the generation of purchased electricity consumed by the company\"",
                "Grid electricity bought from the distribution company"],
               ["3", "\"All other indirect emissions\", from \"sources not owned or controlled by the company\"",
                "Making the steel it buys; trucking its products; employees' commuting"]]),
            B("The BRSR guidance note defines Scope 2 more widely, as \"purchased or acquired electricity, "
              "heating, cooling, and steam\" (" + MC + ", Annexure 17).", sm=True),
        ]),

        S("Scope 3", "The fifteen categories of Scope 3", [
            TC([T(["Upstream", ""],
                  [["1", "Purchased goods and services"], ["2", "Capital goods"],
                   ["3", "Fuel- and energy-related activities not in Scope 1 or 2"],
                   ["4", "Upstream transportation and distribution"], ["5", "Waste generated in operations"],
                   ["6", "Business travel"], ["7", "Employee commuting"], ["8", "Upstream leased assets"]])],
               [T(["Downstream", ""],
                  [["9", "Downstream transportation and distribution"], ["10", "Processing of sold products"],
                   ["11", "Use of sold products"], ["12", "End-of-life treatment of sold products"],
                   ["13", "Downstream leased assets"], ["14", "Franchises"], ["15", "Investments"]])]),
            H("amber", "Source: GHG Protocol Scope 3 Standard (2011). A company that reports \"Scope 3\" should say "
              "which categories it counted. Most report a few."),
        ], compact=True),

        S("Global warming potential", "Converting other gases to CO2 equivalent", [
            T(["Gas", "IPCC AR5 GWP100", "IPCC AR6 GWP100"],
              [["Carbon dioxide (CO2)", "1", "1"],
               ["Methane (CH4)", "28 (fossil 30)", "27.0 non-fossil; 29.8 fossil"],
               ["Nitrous oxide (N2O)", "265", "273"]]),
            B("Sources: IPCC AR5 WG1 Table 8.7; AR6 WG1 Table 7.15. The GHG Protocol's guidance of 7 August 2024 "
              "recommends the latest (AR6) values, with the fossil methane value for fugitive emissions and "
              "industrial processes and the non-fossil value for other sources, including fuel combustion. The "
              "BRSR prescribes no edition; its guidance note asks companies to disclose the sources of the GWP "
              "values and emission factors they used.", sm=True),
            H("cyan", "Exercise: 2 tonnes of methane from on-site wastewater treatment is 2 x 27.0 = 54 t CO2e "
              "under AR6, and 2 x 28 = 56 t CO2e under AR5. State which one you used."),
        ]),

        S("Exercise", "Scope 1: diesel and LPG burnt on site", [
            EX(ILL + "Company X burnt 210 tonnes of diesel in its generators and 40 tonnes of LPG in its "
               "canteens and furnaces in the year. Using IPCC 2006 default values, calculate the CO2 emitted.",
               "Diesel: net calorific value 43.0 TJ per Gg; CO2 factor 74,100 kg per TJ. 210 t = 0.21 Gg. "
               "0.21 x 43.0 = 9.03 TJ. 9.03 x 74,100 = 669,123 kg.<br>LPG: 47.3 TJ per Gg; 63,100 kg per TJ. "
               "40 t = 0.04 Gg. 0.04 x 47.3 = 1.892 TJ. 1.892 x 63,100 = 119,385 kg.",
               "Scope 1 from combustion = 669.1 + 119.4 = <strong>788.5 t CO2</strong>. (Methane and nitrous "
               "oxide from combustion are left out here for simplicity; a full inventory includes them.)"),
            B("Sources: IPCC 2006 Guidelines, Vol. 2, Table 1.2 (net calorific values) and Table 2.2 (CO2 "
              "factors). The ISF note lists 2.68 kg CO2e per litre of diesel and 2.98 per kg of LPG for its "
              "provisional proxy method; 47.3 x 63.1 gives the same 2.98 kg per kg.", sm=True),
        ]),

        S("Grid factor", "Scope 2 in India starts from the CEA's grid emission factor", [
            ST([C("0.710", "t CO2 per MWh, Indian grid, FY 2024-25 (weighted average)", "cyan", CEA),
                C("0.727", "t CO2 per MWh, FY 2023-24", "indigo", CEA + ", Annexure I"),
                C("V21.0", "latest version, published November 2025", "green", CEA)], cols=3),
            B("The weighted average divides \"the absolute CO2 emissions of all power stations by the total net "
              "generation\", including renewable generation and grid-connected captive plants. The ISF note tells "
              "companies to \"use the latest applicable CEA-published grid emission factor\". Version 21 also "
              "revised some earlier years after adding actual captive-plant data, so use the current table for "
              "past years too."),
            H("amber", "A company using a factor from an old version of the database, or the factor for the wrong "
              "year, will misstate Scope 2 with no error visible on the page."),
        ]),

        S("Exercise", "Scope 2: grid electricity", [
            EX(ILL + "Company X bought 18,000 MWh of electricity from the grid in FY 2024-25. It also used "
               "2,000 MWh from rooftop solar panels it owns. Calculate location-based Scope 2. Then calculate the "
               "error if the team had used the FY 2023-24 factor by mistake.",
               "Only purchased grid electricity counts in Scope 2. Own rooftop solar has no combustion emissions. "
               "18,000 MWh x 0.710 t per MWh = 12,780 t CO2.<br>With 0.727: 18,000 x 0.727 = 13,086 t CO2.",
               "Scope 2 = <strong>12,780 t CO2</strong>. The wrong factor overstates it by 306 t, about 2.4%."),
            B("Own rooftop solar still appears in the energy table, as renewable electricity in line A. It carries no Scope 2 emissions because nothing was bought from the grid for it. Units exported to the grid under net metering need care, and the company should state how it treated them.", sm=True),
        ]),

        S("Market-based Scope 2", "Location-based and market-based figures", [
            Q("A location-based method reflects the average emissions intensity of grids on which energy "
              "consumption occurs ... A market-based method reflects emissions from electricity that companies "
              "have purposefully chosen (or their lack of choice).",
              "GHG Protocol, Scope 2 Guidance (2015)"),
            B("Where a company operates in markets that offer contractual instruments for electricity, the "
              "Guidance says it \"shall report scope 2 emissions in two ways\": location-based and market-based. "
              "The market-based figure can fall sharply when a company buys renewable power through contracts, "
              "while the location-based figure stays tied to the grid's average."),
            H("indigo", "The GHG Protocol is revising its Scope 2 rules. Its post of 1 August 2025 expected final "
              "text on the key requirements by mid-2026 and the full revised standard by the end of 2027. Check "
              "the current position before you rely on the 2015 Guidance."),
        ]),

        S("Exercise", "Intensity per rupee, and per rupee adjusted for PPP", [
            EX(ILL + "Company X's revenue from operations is Rs 5,000 crore. Its Scope 1 is 788.5 t and Scope 2 "
               "is 12,780 t. Calculate (a) Scope 1 and 2 intensity per crore of revenue and (b) per million "
               "international dollars of PPP-adjusted revenue, using the ISF note's example rate of 22.4 rupees "
               "per international dollar.",
               "Scope 1 + 2 = 13,568.5 t.<br>(a) 13,568.5 / 5,000 = 2.71 t per crore.<br>(b) Revenue = Rs "
               "50,000,000,000. PPP-adjusted revenue = 50,000,000,000 / 22.4 = 2,232,142,857 international "
               "dollars = 2,232.1 million. 13,568.5 / 2,232.1 = 6.08.",
               "(a) <strong>2.71 t CO2e per Rs crore</strong>; (b) <strong>6.08 t per million PPP dollars</strong>."),
            B("The ISF note's formula is \"PPP Adjusted Revenue in USD = Revenue in INR/IMF PPP Conversion "
              "Factor\". It gives 22.4 as the rate \"as of April 2024\" and tells companies to use the latest IMF "
              "rate and disclose it. Use the current rate in a real filing.", sm=True),
        ]),

        S("Common errors", "Where emission figures go wrong", [
            TC([BL(["<strong>Units:</strong> kWh entered as MWh multiplies Scope 2 by a thousand.",
                    "<strong>Factor year:</strong> the CEA factor for a different year, or from an old version.",
                    "<strong>Boundary:</strong> a subsidiary's plant left out of a consolidated report, or included "
                    "in a standalone one."], color="red")],
               [BL(["<strong>Missing sources:</strong> diesel generators at sites that run on the grid most of "
                    "the time.",
                    "<strong>Undisclosed method:</strong> no statement of the GWP values or emission factors used.",
                    "<strong>Partial Scope 3:</strong> a Scope 3 total with no list of the categories counted."],
                   color="red")]),
            H("amber", "A reader cannot recalculate a company's emissions from the BRSR alone. A reader can check "
              "that the totals move sensibly with the energy figures, which Section 06 shows how to do."),
        ]),

        # ===================== SECTION 06 =====================
        DIV("06", "Six", "Energy, water and waste"),

        S("Energy table", "How the energy table is built", [
            T(["Line", "Renewable sources", "Non-renewable sources"],
              [["Electricity consumption", "A", "D"], ["Fuel consumption", "B", "E"],
               ["Other sources", "C", "F"]]),
            B("Total energy consumed is A+B+C+D+E+F. The format asks for energy intensity per rupee of turnover, "
              "per rupee adjusted for PPP, and optionally per unit of output. The guidance note says the data "
              "\"shall be reported in terms of Joules or multiples such as Giga Joules\", and that conversion "
              "factors must be applied consistently and disclosed."),
            H("cyan", "Useful conversion: 1 MWh = 3.6 GJ. For fuels, multiply the mass by its net calorific value."),
            B("Fuel burnt in a company's own captive power plant is reported once, as fuel in line E. The electricity that plant generates should not be added again as electricity consumed, or the same energy is counted twice. The same logic applies to steam raised in the company's own boilers.", sm=True),
        ]),

        S("Exercise", "Total energy and the renewable share", [
            EX(ILL + "Using Company X's figures, calculate total energy consumed in GJ and the share from "
               "renewable sources: grid electricity 18,000 MWh; own rooftop solar 2,000 MWh; diesel 210 t; LPG 40 t.",
               "Grid: 18,000 x 3.6 = 64,800 GJ (D). Solar: 2,000 x 3.6 = 7,200 GJ (A). Diesel: 9.03 TJ = 9,030 GJ "
               "(E). LPG: 1.892 TJ = 1,892 GJ (E).<br>Total = 64,800 + 7,200 + 9,030 + 1,892 = 82,922 GJ. "
               "Renewable share = 7,200 / 82,922.",
               "Total energy = <strong>82,922 GJ</strong>; renewable share = <strong>8.7%</strong>; intensity = "
               "82,922 / 5,000 = <strong>16.6 GJ per Rs crore</strong>."),
            B("The grid itself carries renewable power, but the format's renewable lines are for electricity the "
              "company sources as renewable. Grid purchases go in D unless the company holds a contract or "
              "instrument for renewable supply.", sm=True),
        ]),

        S("Exercise", "Energy intensity per PPP revenue and per unit of output", [
            EX(ILL + "Company X consumed 82,922 GJ. Its PPP-adjusted revenue is 2,232.1 million international "
               "dollars (Section 05, at 22.4 rupees per dollar), and it produced 400,000 t of product. Calculate "
               "energy intensity per million PPP dollars and per tonne of product.",
               "Per PPP revenue: 82,922 / 2,232.1 = 37.15 GJ per million PPP dollars.<br>Per unit of output: "
               "82,922 / 400,000 = 0.207 GJ per tonne.",
               "<strong>37.2 GJ per million PPP $</strong>; <strong>0.21 GJ per tonne of product</strong>."),
            B("Output-based intensity is optional in the format, but it is the better figure for comparing two "
              "plants in the same industry, because it does not move with prices.", sm=True),
        ]),

        S("PAT scheme", "Energy efficiency obligations under the PAT scheme", [
            B("Principle 6, essential indicator 2 asks whether any of the company's sites are \"designated "
              "consumers\" under the Perform, Achieve and Trade (PAT) scheme of the Bureau of Energy Efficiency, and "
              "if so, whether their targets were met and what was done if they were not. PAT sets specific energy "
              "consumption targets for energy-intensive plants under the National Mission for Enhanced Energy "
              "Efficiency."),
            TC([P("green", "Why readers should look",
                  "A missed PAT target is a regulatory fact recorded outside the company's own narrative.")],
               [P("amber", "What it does not show",
                  "PAT targets are per unit of output. A plant can meet its target while total energy use rises "
                  "with production.")]),
        ]),

        S("Water", "How water is reported", [
            T(["Item in the format", "Unit"],
              [["Withdrawal by source: surface water, groundwater, third-party water, seawater or desalinated "
                "water, others", "kilolitres"],
               ["Total withdrawal and total consumption", "kilolitres"],
               ["Water intensity per rupee of turnover, and adjusted for PPP", "kilolitres per rupee"],
               ["Discharge by destination and level of treatment", "kilolitres"]]),
            B("The guidance note defines consumption as water \"no longer available for use by the ecosystem or "
              "local community\". If it cannot be measured directly, \"Total water consumption = Total water "
              "withdrawal &ndash; total water discharge\"."),
            H("amber", "Leadership indicator 1 of Principle 6 asks for withdrawal, consumption and discharge for "
              "each facility in an area of water stress. A national total can hide a plant drawing on a depleted "
              "aquifer."),
        ], compact=True),

        S("Exercise", "Water withdrawal, consumption and intensity", [
            EX(ILL + "Company X withdrew 300,000 kL of groundwater and bought 120,000 kL from the municipal supply. "
               "It discharged 80,000 kL of treated effluent to a common treatment plant. Consumption is not "
               "metered. Calculate withdrawal, consumption and intensity per crore of revenue.",
               "Withdrawal = 300,000 + 120,000 = 420,000 kL (groundwater plus third-party water).<br>Consumption = "
               "withdrawal &ndash; discharge = 420,000 &ndash; 80,000 = 340,000 kL.<br>Intensity = 340,000 / 5,000.",
               "Withdrawal <strong>420,000 kL</strong>; consumption <strong>340,000 kL</strong>; intensity "
               "<strong>68 kL per Rs crore</strong>."),
            B("Groundwater is 71% of withdrawal here. A reader would next ask where the plant is and whether the "
              "company reports it under the water-stress leadership indicator.", sm=True),
        ]),

        S("Waste", "The eight categories of waste in the format", [
            T(["Code", "Category", "Code", "Category"],
              [["A", "Plastic waste", "E", "Battery waste"],
               ["B", "E-waste", "F", "Radioactive waste"],
               ["C", "Bio-medical waste", "G", "Other hazardous waste"],
               ["D", "Construction and demolition waste", "H", "Other non-hazardous waste"]]),
            B("Waste is reported in metric tonnes, with intensity per rupee and per rupee adjusted for PPP. The "
              "format then asks, for each category, how much was <strong>recovered</strong> (recycled, re-used or "
              "other recovery operations) and how much was <strong>disposed</strong> (incineration, landfilling or "
              "other disposal operations)."),
            H("cyan", "Each category has its own rules under India's waste management rules; the BRSR asks only "
              "for the quantities."),
        ], compact=True),

        S("Exercise", "Waste recovered and disposed", [
            EX(ILL + "Company X generated 1,200 t of waste. It recycled 700 t, re-used 100 t, incinerated 150 t and "
               "sent 250 t to landfill. Calculate waste recovered, waste disposed and the share recovered.",
               "Recovered = recycled + re-used + other recovery = 700 + 100 = 800 t.<br>Disposed = incineration + "
               "landfill + other disposal = 150 + 250 = 400 t.<br>Check: 800 + 400 = 1,200 t generated.",
               "Recovered <strong>800 t (66.7%)</strong>; disposed <strong>400 t (33.3%)</strong>."),
            B("If recovered and disposed do not add up to generated, the difference is waste stored on site or a "
              "reporting error. Either way, ask.", sm=True),
            B("Hazardous waste in India is governed by the Hazardous and Other Wastes (Management and Transboundary Movement) Rules 2016, and plastics, e-waste, batteries, bio-medical and construction waste each have their own rules. The quantities in a BRSR should agree with the annual returns the company files with its State Pollution Control Board under those rules, which gives a reader a second source to check against.", sm=True),
        ]),

        S("Reading the environment figures", "Four checks a reader can run in five minutes", [
            BL(["<strong>Energy against emissions:</strong> if energy use rose and Scope 1 and 2 fell, look for a "
                "change in renewable sourcing, a new grid factor or a change in boundary.",
                "<strong>Two years side by side:</strong> every table shows the previous year. Large jumps without "
                "explanation are worth a question.",
                "<strong>Intensity and totals together:</strong> intensity can fall while the total rises, if "
                "revenue grew faster (Section 10 works an example).",
                "<strong>Assessment notes:</strong> each environment table ends with a note asking whether an "
                "external agency assessed or assured it, and which."]),
            H("green", "These checks need no technical training, only the habit of reading two columns and one "
              "footnote."),
        ]),

        # ===================== SECTION 07 =====================
        DIV("07", "Seven", "Employees, communities and customers"),

        S("Who counts", "Employees and workers, permanent and other", [
            B("Section A, Part IV counts people in four groups: permanent employees, other-than-permanent "
              "employees, permanent workers and other-than-permanent workers, each split by gender, with separate "
              "counts for differently abled people. Many safety and wage figures in Section C are reported for "
              "\"employees\" and \"workers\" separately."),
            TC([P("indigo", "Why the split matters",
                  "In many Indian manufacturing companies, contract workers outnumber permanent staff and face "
                  "higher risks. A safety record for permanent employees alone can look far better than the "
                  "record for everyone on site.")],
               [P("amber", "What to check",
                  "Whether figures cover other-than-permanent workers, and whether the headcounts in Part IV "
                  "match the groups used in the safety tables.")]),
        ]),

        S("Exercise", "Spending on wellbeing as a share of revenue", [
            EX(ILL + "Company X spent Rs 40 crore on wellbeing measures for employees and workers, including health "
               "insurance, accident insurance, maternity and paternity benefits and day care. Its revenue from "
               "operations is Rs 5,000 crore. Calculate the BRSR Core figure.",
               "The format asks for \"Cost incurred on well-being measures as a % of total revenue of the "
               "company\" (Principle 3, essential indicator 1(c)). 40 / 5,000 x 100.",
               "<strong>0.8% of revenue</strong>."),
            B("A percentage of revenue rises and falls with sales. Read it beside the number of people covered, "
              "which the same indicator reports for each benefit.", sm=True),
            B("The indicator covers health insurance, accident insurance, maternity and paternity benefits and day care facilities, for permanent and other employees and workers, with the number covered in each group. A company whose contract workers receive none of these can still report a respectable share of revenue that reaches only part of its workforce.", sm=True),
        ]),

        S("Exercise", "The lost-time injury frequency rate", [
            EX(ILL + "Company X's employees and workers worked 12 million hours in the year. There were 6 lost-time "
               "injuries. Calculate the LTIFR as the BRSR defines it.",
               "The guidance note: \"(No. of lost time injuries in FY x 1,000,000) / (Total hours worked by all "
               "staff in same FY)\". (6 x 1,000,000) / 12,000,000.",
               "<strong>LTIFR = 0.50 per million person-hours worked</strong>."),
            B("Some international reports use 200,000 hours as the base, following the US Occupational Safety and "
              "Health Administration. A rate on that base is one-fifth of the BRSR rate for the same injuries, so "
              "check the base before comparing.", sm=True),
            B("The guidance note describes lost time as \"the loss of productivity for an organization as a result of a work-related injury or ill-health\". The format reports total recordable injuries, high-consequence injuries and fatalities on separate lines, for employees and for workers. A rate can fall in a year in which someone died, so read the fatalities line first.", sm=True),
        ]),

        S("Exercise", "Safety for employees and for workers, separately", [
            EX(ILL + "Of Company X's 12 million hours, permanent employees worked 5 million and other workers, "
               "mostly on contract, worked 7 million. Employees had 2 lost-time injuries and workers had 4. "
               "Calculate the LTIFR for each group and for everyone.",
               "Employees: 2 x 1,000,000 / 5,000,000 = 0.40.<br>Workers: 4 x 1,000,000 / 7,000,000 = 0.57.<br>"
               "Everyone: 6 x 1,000,000 / 12,000,000 = 0.50.",
               "Employees <strong>0.40</strong>; workers <strong>0.57</strong>; combined <strong>0.50</strong>. "
               "The format asks for employees and workers separately; a report that gives only the first hides "
               "the higher rate."),
            B("Workers engaged through contractors often have their hours recorded by the contractor, not by the company. A company that cannot count those hours cannot calculate their rate. Saying so in the report is more useful to a reader than a combined figure that quietly leaves them out.", sm=True),
        ]),

        S("Exercise", "Gross wages paid to women", [
            EX(ILL + "Company X paid total gross wages of Rs 300 crore, of which Rs 42 crore went to women. Women are "
               "25% of its employees and workers. Calculate the BRSR Core figure and say what a reader should ask.",
               "\"Gross wages paid to females as % of total wages paid by the entity\" (Principle 5, essential "
               "indicator 3(b)). 42 / 300 x 100.",
               "<strong>14.0%</strong>. Women are a quarter of the workforce and receive about a seventh of the "
               "wages. Ask whether women are concentrated in lower-paid roles, and look at the median "
               "remuneration table in the same indicator."),
            B("Median remuneration by gender, reported in the same indicator, helps separate two explanations: fewer women in senior roles, or women paid less in the same roles. The BRSR alone cannot settle which applies. It tells you which question to ask the company next.", sm=True),
        ]),

        S("Human rights", "POSH complaints and other human rights indicators", [
            B("Principle 5 asks, among other things, for complaints filed and resolved under the POSH Act, the "
              "share of employees paid at least the minimum wage, median remuneration by gender, and training on "
              "human rights. BRSR Core attribute 6 includes the POSH complaints figure."),
            TC([P("amber", "Reading a zero",
                  "Zero POSH complaints in a large workforce can mean a safe workplace. It can also mean an "
                  "Internal Committee nobody trusts. The figure alone cannot tell you which.")],
               [P("green", "What helps",
                  "The format asks for complaints as a share of female employees and workers, and for the "
                  "previous year. A sudden rise after a training programme can be a sign that people now "
                  "report.")]),
        ]),

        S("Exercise", "Sourcing from MSMEs and small producers", [
            EX(ILL + "Company X bought inputs worth Rs 2,500 crore. Rs 600 crore came directly from MSMEs and small "
               "producers, and Rs 2,100 crore from suppliers within India. Calculate the two shares Principle 8 asks "
               "for.",
               "Principle 8, essential indicator 4 asks for input material sourced \"directly\" from MSMEs/small "
               "producers and from within India, as a share of total inputs by value. 600 / 2,500 and 2,100 / "
               "2,500.",
               "<strong>24% from MSMEs and small producers</strong>; <strong>84% from within India</strong>."),
            B("BRSR Core attribute 7 also asks for wages paid to people in smaller towns as a share of total wage "
              "cost, using the place-of-employment classes in the format.", sm=True),
        ]),

        S("Exercise", "Days of accounts payable", [
            EX(ILL + "Company X's accounts payable at year end were Rs 350 crore. The cost of goods and services it "
               "procured in the year was Rs 2,500 crore. Calculate the days of accounts payable.",
               "The format's formula (Principle 1, essential indicator 8): \"(Accounts payable *365) / Cost of "
               "goods/services procured\". (350 x 365) / 2,500.",
               "<strong>51.1 days</strong>."),
            B("For a small supplier, payment days decide whether it can pay its own workers. A figure that rises "
              "year on year, or far exceeds the 45-day limit that applies to payments owed to MSMEs under the MSMED "
              "Act 2006, deserves a question.", sm=True),
        ]),

        S("CSR and communities", "Where CSR and community impact appear", [
            BL(["<strong>Section A, Part VI:</strong> whether CSR applies under s135, with turnover and net worth.",
                "<strong>Principle 8, essential indicator 1:</strong> social impact assessments of projects "
                "undertaken under applicable laws, with whether results were made public.",
                "<strong>Principle 8, essential indicators 2 and 3:</strong> rehabilitation and resettlement, and "
                "mechanisms to receive grievances from the community.",
                "<strong>Principle 8, leadership indicators:</strong> CSR projects in aspirational districts, "
                "beneficiaries of CSR projects, and preferential procurement from marginalised groups."]),
            H("green", "For an NGO approaching a company, Principle 8 and Part VI together show where the company "
              "already works and what it says about the communities near its plants."),
        ]),

        # ===================== SECTION 08 =====================
        DIV("08", "Eight", "Value chain and green credits"),

        S("Value chain", "What changed in March 2025", [
            T(["", "2023 framework", "Since 28 March 2025"],
              [["Who is a value chain partner", "Top upstream and downstream partners making up 75% of purchases "
                "or sales by value, together", "Partners \"individually comprising 2% or more\" of purchases or "
                "sales by value"],
               ["Limit", "None beyond the 75%", "The company \"may limit disclosure ... to cover 75%\" of purchases "
                "and sales"],
               ["Disclosure", "Comply or explain, top 250, from FY 2024-25", "Voluntary, top 250, from FY 2025-26"],
               ["Checking", "Limited assurance, comply or explain, from FY 2025-26", "Assessment or assurance, "
                "voluntary, from FY 2026-27"]]),
            H("cyan", "Source: " + C2025 + ". The company must also disclose the share of purchases and sales its "
              "value chain disclosures cover."),
        ], compact=True),

        S("Why it matters", "Why suppliers and buyers should care about value chain disclosures", [
            B("A company's suppliers produce much of its Scope 3 emissions and employ many of the workers whose "
              "safety a buyer may be asked about. Value chain disclosures are the BRSR's way of reaching past the "
              "company's own gate. They are now voluntary, so many companies will not make them, and those that "
              "do may cover only their largest partners."),
            TC([P("indigo", "For an MSME supplier",
                  "Expect data requests from large buyers even where the rule is voluntary: energy use, emissions, "
                  "safety, wages. Keeping these records now costs less than reconstructing them later.")],
               [P("amber", "For a reader",
                  "Check the coverage share the company discloses. Figures for 40% of purchases say little about "
                  "the other 60%.")]),
        ]),

        S("Exercise", "Which suppliers are value chain partners?", [
            EX(ILL + "Company X's suppliers, by share of purchases: S1 30%, S2 18%, S3 12%, S4 6%, S5 3%, S6 1.5%, "
               "and many others each below 1%, together 29.5%. Which are value chain partners under the 2025 rule, "
               "and what share of purchases do they cover?",
               "Partners are those \"individually comprising 2% or more\": S1 to S5. S6 is below 2%. Coverage = 30 "
               "+ 18 + 12 + 6 + 3 = 69%. That is below 75%, so the option to stop at 75% does not arise.",
               "<strong>S1 to S5</strong>, covering <strong>69%</strong> of purchases. Disclose the 69% figure."),
            B("Second case: shares of 40%, 25%, 15%, 8% and 4%. All five pass the 2% test and cover 92%. Under the "
              "75% limit the company may stop once coverage reaches 75%: S1 to S3 already cover 80%. This reading "
              "of the limit is ours; check it against the ISF standards before relying on it.", sm=True),
        ]),

        S("Green credits", "Green credits as a voluntary disclosure", [
            Q("How many Green Credits have been generated or procured: a. By the listed entity b. By the top ten (in "
              "terms of value of purchases and sales, respectively) value chain partners",
              "BRSR, Principle 6, leadership indicator 8, added by the " + C2025),
            BL(["It applies \"for BRSR disclosures for FY 2024-25 and onwards\".",
                "It is a leadership indicator, so it is voluntary; the circular's own title calls it a \"voluntary "
                "disclosure on green credits\". Some commentary describes it as mandatory, which is wrong.",
                "Green credits are issued under India's Green Credit Programme, run by the Ministry of Environment, "
                "Forest and Climate Change under the Green Credit Rules 2023."]),
            H("amber", "A green credit and a reduction in the company's own emissions are separate things. A reader "
              "should look for both and not let one stand in for the other."),
        ]),

        S("Reading value chain figures", "Questions to ask of a value chain disclosure", [
            BL(["What share of purchases and sales does it cover, and is that share stated?",
                "Are the figures measured by the partners or estimated by the company from spending?",
                "Has any of it been assessed or assured? From FY 2026-27 this is possible on a voluntary basis.",
                "Does the Scope 3 figure under Principle 6 sit consistently with the value chain section, or do they "
                "tell different stories?"]),
            H("cyan", "Estimates from spending are a legitimate start. The ISF note's proxy method for small "
              "partners is described as provisional and to be phased out."),
            B("Value chain figures are only as good as the partner's own records. A small supplier may have no meter on its diesel generator and no register of hours worked. A company reporting on such partners should say how each figure was obtained: from the partner's records, from an audit, or estimated from spending.", sm=True),
        ]),

        S("Exercise", "Scope 3 from purchased goods, using spend data", [
            EX(ILL + "Company X wants a first estimate of Scope 3, category 1 (purchased goods and services). It "
               "bought Rs 900 crore of steel and Rs 300 crore of packaging. Use spend-based factors of 400 t CO2e "
               "per Rs crore for steel and 150 t per Rs crore for packaging. Both factors are invented for this "
               "exercise.",
               "Steel: 900 x 400 = 360,000 t. Packaging: 300 x 150 = 45,000 t. Total = 405,000 t CO2e. Compare "
               "with Scope 1 and 2: 405,000 / 13,568.5 = 29.8.",
               "Category 1 estimate = <strong>405,000 t CO2e</strong>, about <strong>30 times</strong> Company X's "
               "own Scope 1 and 2."),
            B("A spend-based estimate multiplies money by an average factor, so it moves with prices as well as "
              "with emissions. It is a starting point; supplier-specific data replaces it over time. In a real "
              "estimate, name the source of every factor.", sm=True),
        ]),

        # ===================== SECTION 09 =====================
        DIV("09", "Nine", "Materiality and the global frameworks"),

        S("Materiality", "Two ways of deciding what is material", [
            TC([P("indigo", "Financial materiality (IFRS S1)",
                  "Information is material if omitting, misstating or obscuring it \"could reasonably be expected "
                  "to influence decisions that primary users of general purpose financial reports make on the "
                  "basis of those reports\". The test looks outward-in: what affects the company and its "
                  "investors.")],
               [P("green", "Double materiality (ESRS 1, EU)",
                  "\"Double materiality has two dimensions, namely: impact materiality and financial "
                  "materiality\" (para 37). A matter is material from the impact side when it concerns the "
                  "company's \"actual or potential, positive or negative impacts on people or the environment\" "
                  "(para 43).")]),
            H("amber", "The BRSR's question 26 asks for issues that present \"a risk or an opportunity to your "
              "business\" and their financial implications. It does not say which test to use. Any statement that "
              "the BRSR requires double materiality is unsupported."),
        ]),

        S("Exercise", "Classify the issue", [
            EX(ILL + "Classify each issue for a cement company as financially material, impact material, or both: "
               "(1) groundwater depletion around a plant in a water-stressed district; (2) a coming carbon price on "
               "cement exports to the EU; (3) dust affecting the health of a nearby village; (4) a change in "
               "accounting for leases.",
               "Ask two questions of each: could it change the company's cash flows or cost of capital? Does the "
               "company's activity cause harm or benefit to people or the environment?",
               "(1) Both: the community loses water and the plant risks supply. (2) Financial. (3) Impact, and "
               "financial if it leads to closure orders or litigation. (4) Financial only, and outside the "
               "BRSR's scope."),
        ]),

        S("GRI", "The GRI Standards", [
            B("The Global Reporting Initiative publishes the most widely used sustainability reporting standards. "
              "Its Universal Standards 2021 (GRI 1 Foundation, GRI 2 General Disclosures and GRI 3 Material Topics) "
              "are \"in effect for reporting from 1 January 2023\". GRI is built around a company's impacts on the "
              "economy, environment and people."),
            TC([P("cyan", "Relation to the BRSR",
                  "SEBI allows a BRSR to cross-reference a GRI report (circular of 10 May 2021, para 6). Many large "
                  "Indian companies publish both.")],
               [P("amber", "For a reader",
                  "A GRI report's content index lists where each disclosure sits. Use it to find figures the BRSR "
                  "cross-refers to.")]),
            B("GRI 3 sets out how an organisation determines its material topics, starting from its impacts. GRI also publishes topic standards, among them GRI 303 on water and effluents and GRI 403 on occupational health and safety, and sector standards for industries with high impacts. A BRSR preparer who already reports under these will find most of the BRSR's environmental and safety questions familiar.", sm=True),
        ]),

        S("ISSB", "The ISSB standards: IFRS S1 and S2", [
            B("The International Sustainability Standards Board (ISSB), part of the IFRS Foundation, issued IFRS S1 "
              "(general requirements) and IFRS S2 (climate-related disclosures) in June 2023, effective for annual "
              "reporting periods beginning on or after 1 January 2024, where a jurisdiction adopts them. "
              "Amendments to IFRS S2 on greenhouse gas emissions were issued in December 2025."),
            H("indigo", "India's position: we found no announcement by SEBI, the Ministry of Corporate Affairs or "
              "the ICAI adopting IFRS S1 or S2 as of October 2026. The ICAI's Sustainability Reporting Standards "
              "Board has issued SSA 5000, a standard for sustainability assurance engagements, which is an "
              "assurance standard. Check for later announcements."),
            B("Foreign investors may still ask an Indian company for ISSB-style information, because their own "
              "regulators require it.", sm=True),
        ]),

        S("CBAM", "The EU's Carbon Border Adjustment Mechanism", [
            T(["Item", "Position in October 2026", "Source"],
              [["Law", "Regulation (EU) 2023/956", "EUR-Lex"],
               ["Sectors", "Cement, iron and steel, aluminium, fertilisers, electricity, hydrogen", "Annex I"],
               ["Transitional period", "1 October 2023 to 31 December 2025: reporting only", "Reg 2023/956"],
               ["Definitive period", "From 1 January 2026", "Reg 2023/956"],
               ["Small importers", "Exempt up to 50 tonnes net mass a year per importer", "Reg (EU) 2025/2083"],
               ["Certificates", "Sold from 1 February 2027; first declaration and surrender by 30 September 2027 "
                "for 2026 imports", "Reg 2023/956 as amended"]]),
            H("amber", "CBAM is paid by the EU importer, who needs the embedded emissions of the goods from the "
              "Indian producer. Exporters of steel, aluminium and cement are asked for plant-level emission data "
              "in the EU's method, which differs from the BRSR's company-level totals."),
        ], compact=True),

        S("Exercise", "Embedded emissions for a CBAM declaration", [
            EX(ILL + "An Indian mill exports 1,000 t of steel products to an EU importer. Its verified embedded "
               "emissions are 2.1 t CO2 per tonne of product. How many tonnes of embedded emissions does the "
               "importer declare, and what reduces the number of certificates it must surrender?",
               "Embedded emissions = 1,000 x 2.1 = 2,100 t CO2. Under Regulation 2023/956 the importer may claim a "
               "reduction for a carbon price effectively paid in the country of origin, and the obligation is "
               "adjusted for the free allocation still given to EU producers of the same goods.",
               "<strong>2,100 t declared</strong>. The certificates surrendered are lower by the two adjustments. "
               "The 2.1 figure is invented; real values come from the plant's own monitoring."),
        ]),

        S("How they fit", "How the frameworks fit together for an Indian company", [
            T(["Framework", "Who sets it", "Who must use it", "Main audience"],
              [["BRSR", "SEBI", "Top 1,000 Indian listed companies", "Investors and other stakeholders"],
               ["GRI", "Global Reporting Initiative", "Voluntary", "Anyone affected by the company"],
               ["IFRS S1 and S2", "ISSB", "Where a jurisdiction adopts them", "Investors"],
               ["ESRS", "European Union", "Companies within the EU rules", "Investors and stakeholders"],
               ["CBAM data", "European Union", "Importers into the EU of covered goods", "EU customs authorities"]]),
            H("cyan", "One set of good underlying records (meters, invoices, payroll, waste manifests) can feed all "
              "of them. Most of the work is in the records, whatever the format."),
        ], compact=True),

        # ===================== SECTION 10 =====================
        DIV("10", "Ten", "Reading a BRSR critically"),

        S("Five questions", "Five questions to ask of any BRSR", [
            FL(["1. Standalone or consolidated? (Section A, point 13)",
                "2. Were Core figures assessed or assured, and by whom? (points 14, 15)",
                "3. How did each figure move from last year, and why?",
                "4. Are units and methods stated?",
                "5. Which leadership indicators were left blank?"]),
            B("These five questions take a few minutes and catch most of the problems a non-specialist can catch. "
              "They do not require recalculating anything."),
            H("green", "Write the answers down before you read the company's narrative sections. It keeps you from "
              "adopting the company's framing."),
            B("The order matters. Boundary comes first, because the standalone company and the group are different populations. Checking comes second, because it tells you how far to trust what follows. Movement from last year comes third, because most errors show up as an implausible jump between the two columns.", sm=True),
        ]),

        S("Exercise", "When intensity falls and the total rises", [
            EX(ILL + "Next year, Company X's Scope 1 and 2 rise from 13,568.5 t to 14,900 t, and its revenue from "
               "Rs 5,000 crore to Rs 6,000 crore. The company's press release says: \"Emission intensity cut by "
               "more than 8%\". Check the claim and state what it leaves out.",
               "Old intensity = 13,568.5 / 5,000 = 2.71 t per crore. New = 14,900 / 6,000 = 2.48. Change = "
               "2.48 / 2.71 &ndash; 1 = &ndash;8.5%. Total change = 14,900 / 13,568.5 &ndash; 1 = +9.8%.",
               "The claim is arithmetically true. Absolute emissions <strong>rose 9.8%</strong>. Both facts belong "
               "in a fair summary."),
            B("Intensity targets are common because they let a growing company show progress. A target stated only as intensity can be met while total emissions keep rising. Where a company states an intensity target, look for an absolute figure or an absolute target beside it, and report both.", sm=True),
        ]),

        S("Warning signs", "Signs that a disclosure needs a closer look", [
            TC([BL(["Targets with no baseline year or deadline (Section B asks for both).",
                    "\"Carbon neutral\" claims resting on credits or offsets, with no fall in Scope 1 and 2.",
                    "A renewable share with no statement of how renewable supply was established."], color="red")],
               [BL(["Large changes from last year with no explanation.",
                    "Methods, factors and GWP values not disclosed.",
                    "Narrative sections much longer than the tables they introduce."], color="red")]),
            H("amber", "None of these proves wrongdoing. Each is a reason to ask the company, or to look for "
              "another source."),
            B("A useful habit: before reading the narrative, write down the three figures you would expect to matter most for the sector. For cement, energy and the Scope 1 emissions from kilns; for a software firm, electricity and employee figures; for a food company, water and packaging waste. Then see whether the report leads with them or buries them.", sm=True),
        ]),

        S("Comparing companies", "How to compare two companies fairly", [
            BL(["Compare companies in the same sector. A cement plant and a software firm have nothing to learn "
                "from each other's emission intensity.",
                "Check that both reports use the same boundary, standalone or consolidated.",
                "Prefer intensity per unit of output (per tonne of cement, per MWh generated) where both report it. "
                "Revenue-based intensity moves with prices.",
                "PPP adjustment is for comparing across countries. Between two Indian companies reporting in rupees "
                "it changes both figures by the same factor and adds nothing."]),
            H("cyan", "When one company reports a leadership indicator and the other does not, the comparison stops "
              "there."),
        ]),

        S("For NGOs", "What an NGO should read before approaching a company", [
            BL(["<strong>Section A, Part VI</strong>: whether CSR applies, and the company's size.",
                "<strong>Section A, question 26</strong>: the issues the company itself calls material. A proposal "
                "that addresses one of them speaks the company's language.",
                "<strong>Principle 8</strong>: where its CSR projects and social impact assessments already are, "
                "and whether it works in aspirational districts.",
                "<strong>Principle 6</strong>: water and waste figures near the plants, if your work is "
                "environmental."]),
            H("green", "Read the BRSR with the CSR report the company files under the Companies Act. Together they "
              "show what it spends and what it says matters."),
            B("A proposal that cites the company's own disclosures shows it has read them. Quote the figure, give the year and the page, and explain how your work relates to it. Do not promise that a project will improve a BRSR figure unless you can measure the link between the two.", sm=True),
        ]),

        S("Where to find them", "Finding BRSRs and the data around them", [
            BL(["A company's BRSR is part of its annual report, published on its own website and filed with the stock "
                "exchanges where it is listed (BSE and NSE).",
                "The exchanges also publish the lists of the top 1,000 companies by average market capitalisation.",
                "SEBI's website carries every circular cited in this course, and the LODR Master Circular with the "
                "current BRSR format in Annexure 16.",
                "The CEA's CO2 Baseline Database gives the grid emission factor for each year."]),
            H("indigo", "Always record the date you downloaded a report and the version of the format it follows. "
              "Formats changed in 2021, 2023 and 2025."),
        ]),

        S("Exercise", "Find the problems in this disclosure", [
            B(ILL + "A company's BRSR contains these five statements. For each, name the problem."),
            T(["#", "Statement", "Problem"],
              [["1", "Scope 2 calculated with the CEA factor from a version published several years ago",
                "The ISF note requires the latest applicable CEA factor"],
               ["2", "Energy table with grid electricity in kWh and fuels in GJ, added together",
                "Units must be consistent; the format asks for Joules or multiples"],
               ["3", "LTIFR of 0.10, \"per 200,000 hours worked\"", "The BRSR base is one million hours; on that "
                "base the rate is 0.50"],
               ["4", "Gross wages to women: 14%, with the previous-year column blank",
                "Both years are required for essential indicators"],
               ["5", "\"Carbon neutral since 2024\", with Scope 1 and 2 unchanged and offsets bought",
                "A claim resting on offsets, without a reduction; disclose both separately"]]),
        ], compact=True),

        # ===================== SECTION 11 =====================
        DIV("11", "Eleven", "A full worked case and where next"),

        S("Worked case", "Company X: the data sheet", [
            B(ILL + "All figures for Company X are invented for teaching. They are used consistently across the "
              "exercises in this deck."),
            T(["Item", "Value", "Item", "Value"],
              [["Revenue from operations", "Rs 5,000 crore", "Groundwater withdrawn", "300,000 kL"],
               ["Grid electricity", "18,000 MWh", "Municipal water bought", "120,000 kL"],
               ["Own rooftop solar", "2,000 MWh", "Water discharged", "80,000 kL"],
               ["Diesel burnt", "210 t", "Waste generated", "1,200 t"],
               ["LPG burnt", "40 t", "Hours worked", "12 million"],
               ["Total gross wages", "Rs 300 crore", "Lost-time injuries", "6"],
               ["Wages paid to women", "Rs 42 crore", "Wellbeing spending", "Rs 40 crore"]]),
        ], compact=True),

        S("Worked case", "Company X: the environment figures", [
            T(["Indicator", "Calculation", "Result"],
              [["Scope 1 (combustion CO2)", "669.1 (diesel) + 119.4 (LPG)", "788.5 t"],
               ["Scope 2 (location-based)", "18,000 MWh x 0.710", "12,780 t"],
               ["Scope 1 + 2 intensity", "13,568.5 / 5,000", "2.71 t per Rs crore"],
               ["Scope 1 + 2 per PPP revenue", "13,568.5 / 2,232.1 (at 22.4)", "6.08 t per million PPP $"],
               ["Total energy", "64,800 + 7,200 + 9,030 + 1,892", "82,922 GJ"],
               ["Renewable share", "7,200 / 82,922", "8.7%"],
               ["Water consumption", "420,000 &ndash; 80,000", "340,000 kL"],
               ["Waste recovered", "(700 + 100) / 1,200", "66.7%"]]),
            H("amber", "Scope 2 is 94% of Company X's Scope 1 and 2. For a company like this, electricity sourcing "
              "matters far more than its own fuel use."),
        ], compact=True),

        S("Worked case", "Company X: the people and governance figures", [
            T(["Indicator", "Calculation", "Result"],
              [["Wellbeing spending", "40 / 5,000", "0.8% of revenue"],
               ["LTIFR", "6 x 1,000,000 / 12,000,000", "0.50"],
               ["Wages paid to women", "42 / 300", "14.0%"],
               ["Inputs from MSMEs and small producers", "600 / 2,500", "24%"],
               ["Days of accounts payable", "350 x 365 / 2,500", "51.1 days"]]),
            B("Read together, the figures raise three questions a reader would put to Company X: why women, who are "
              "a quarter of the workforce, receive 14% of wages; whether the safety rate covers contract workers; "
              "and how many of its MSME suppliers wait longer than 45 days to be paid."),
            B("None of these figures shows wrongdoing. Each is a reason for a conversation with the company. Where it has already answered such a question, in an earlier report or on an investor call, use that answer and cite it beside the figure in anything you publish.", sm=True),
        ]),

        S("Worked case", "What a reader would write about Company X", [
            Q("Company X's emissions come mostly from grid electricity, so its renewable share of 8.7% is the "
              "figure to watch. Its water comes 71% from groundwater; it should say whether any plant sits in a "
              "water-stressed area. Women receive 14% of wages against a quarter of the workforce. Its Core figures "
              "should be checked from FY 2026-27 if it is in the top 1,000.",
              "A model summary, written from the BRSR figures alone"),
            H("cyan", "The summary uses only the numbers, the two-year comparison and the gaps. It makes no claim "
              "the figures cannot support."),
            B("A good summary keeps three things apart: what the report states, what follows from the arithmetic, and what remains unknown. Readers can then disagree with your interpretation without having to doubt your numbers, and the company can answer each point separately.", sm=True),
        ]),

        S("Reference sheet", "Dates, numbers and sources to keep at hand", [
            T(["Item", "Value", "Source"],
              [["BRSR mandatory", "From FY 2022-23, top 1,000", C2021],
               ["Ranking", "Average market cap, 1 July to 31 December", "LODR Reg 3(2)"],
               ["Core checking", "Top 150 (FY 2023-24) to top 1,000 (FY 2026-27)", C2023],
               ["Wording since 28 March 2025", "\"Assessment or assurance\"", C2025],
               ["Value chain partner", "2% or more individually; voluntary from FY 2025-26", C2025],
               ["Grid factor", "0.710 t CO2/MWh (FY 2024-25)", CEA],
               ["LTIFR base", "Per one million hours worked", MC + ", Annexure 16"],
               ["GWP (AR6)", "CH4 27.0 non-fossil, 29.8 fossil; N2O 273", "IPCC AR6 WG1 Table 7.15"]]),
            H("indigo", "Facts as of 9 October 2026."),
        ], compact=True),

        S("Where next", "Where next: related courses and tools", [
            TC([BL(["Spending obligations and impact: " + L("csr-esg.html", "CSR &amp; ESG 101"),
                    "The science behind the numbers: " + L("climate-essentials.html", "Climate Essentials 101"),
                    "Who answers to whom: " + L("governance-accountability.html", "Governance &amp; Accountability 101"),
                    "Workers and wages: " + L("work-labour-livelihoods.html", "Work, Labour &amp; Livelihoods 101")])],
               [BL(["The flagship: <a href=\"/courses/esg/\">Sustainability, ESG &amp; Corporate Responsibility</a>",
                    "Calculating in a spreadsheet: <a href=\"/code/spreadsheets.html\">Spreadsheets for M&amp;E</a>",
                    "Building a dashboard of the figures: <a href=\"/code/powerbi.html\">Power BI for M&amp;E "
                    "Dashboards</a>",
                    "The data behind the climate figures: <a href=\"/dataverse.html\">Dataverse</a>"])]),
            H("green", "All courses are free."),
        ]),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "BRSR &amp; Sustainability Reporting 101 &middot; Complete",
         "headline": "Read both columns,<br>check the footnote",
         "byline": "A BRSR is the company's own account in a regulated format. Calculate with the right factor "
                   "and the right units if you prepare one; compare years, boundaries and checks if you read one. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "ESG Flagship", "href": "https://www.impactmojo.in/courses/esg/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

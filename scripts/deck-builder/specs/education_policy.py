# -*- coding: utf-8 -*-
"""
Education Policy 101: ImpactMojo 101 Series (native deck spec)
How school and higher education policy is made, paid for and judged, for development practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py education_policy

Sources opened while writing (October 2026):
- Psacharopoulos and Patrinos (2018), Education Economics 26(5): 445-458:
  https://ideas.repec.org/a/taf/edecon/v26y2018i5p445-458.html
- World Bank, World Development Report 2018, Learning to Realize Education's Promise, Overview (PDF via
  Open Knowledge Repository, handle 10986/28340): https://www.worldbank.org/en/publication/wdr2018
- National Education Policy 2020 (NCERT copy): https://ncert.nic.in/pdf/nep/NEP_2020.pdf
- Constitution: Wikipedia, Eighty-sixth Amendment (Arts 21A, 45, 51A(k)):
  https://en.wikipedia.org/wiki/Eighty-sixth_Amendment_of_the_Constitution_of_India
  and Concurrent List (entry 25, 42nd Amendment): https://en.wikipedia.org/wiki/Concurrent_List
- RTE Act 2009 text: https://en.wikisource.org/wiki/Right_of_Children_to_Free_and_Compulsory_Education_Act,_2009
  and https://en.wikipedia.org/wiki/Right_of_Children_to_Free_and_Compulsory_Education_Act,_2009
- RTE (Amendment) Act 2019 (No. 1 of 2019), Gazette 11 January 2019 (PRS copy):
  https://prsindia.org/files/bills_acts/bills_parliament/2017/Right%20of%20Children%20to%20Free%20and%20Compulsory%20Education%20(Amendment)%20Act,%202019.pdf
- Careers360, 23 December 2024, Centre notifies RTE rules amendment:
  https://news.careers360.com/centre-notifies-right-to-education-rte-act-rules-2024-amendment-no-detention-policy-fail-class-5-school-exams/amp
- CLPR, Society for Unaided Private Schools of Rajasthan v Union of India (12 April 2012):
  https://clpr.org.in/litigation/society-for-un-aided-private-schools-of-rajasthan-v-union-of-india-and-anr/
- LiveLaw, 1 September 2025, Anjuman Ishaat-e-Taleem Trust v State of Maharashtra referral:
  https://www.livelaw.in/amp/top-stories/supreme-court-doubts-correctness-of-judgment-excluding-minority-schools-from-rte-act-refers-to-cji-302557
- Supreme Court Observer, Dinesh Biwaji Ashtikar v State of Maharashtra (13 January 2026):
  https://www.scobserver.in/journal/the-implementation-mandate-of-the-right-to-education-act/
- Wikipedia: Kothari Commission https://en.wikipedia.org/wiki/Kothari_Commission ; National Policy on Education
  https://en.wikipedia.org/wiki/National_Policy_on_Education ; Sarva Shiksha Abhiyan
  https://en.wikipedia.org/wiki/Sarva_Shiksha_Abhiyan
- ASER Centre, ASER 2024 National findings: https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-National-findings.pdf
- Pratham, ASER 2026 page (no later report released): https://pratham.org/aser-2026/
- PARAKH, PRS 2024 reports page: https://parakh.ncert.gov.in/prs-reports-2024 ; blog:
  https://parakh.ncert.gov.in/blog/parakh-rashtriya-sarvekshan-2024 ; Careers360, 8 July 2025:
  https://news.careers360.com/parakh-rashtriya-sarvekshan-result-2024-state-govt-schools-sc-st-far-behind-class-3-6-9-maths-science-language-evs-exam-survey
- PIB, UDISE+ 2024-25, 28 August 2025 (copy):
  https://educationforallinindia.com/wp-content/uploads/2025/08/PIB-UDISEPlus-2024-25-Press-Release-August-28-2025.pdf
- PIB release 2282141 on UDISE+ 2025-26 (copy): https://educationforallinindia.com/?p=24774
- A.C. Mehta, UDISE+ 2025-26 preliminary analysis (tables from the UDISE+ 2025-26 report, released 7 July 2026):
  https://educationforallinindia.com/wp-content/uploads/2026/07/Analysis-of-UDISE-2025-26-Data-by-aruncmehta-educationforallinindia.pdf
- PRS Legislative Research, Demand for Grants 2026-27 Analysis: Education, 17 February 2026:
  https://prsindia.org/files/budget/budget_parliament/2026/DfG_Analysis_2026-27-Education.pdf
- World Bank WDI API (SE.XPD.TOTL.GD.ZS, SE.XPD.TOTL.GB.ZS, SE.ADT.LITR.ZS, SE.PRM.CMPT.ZS, SE.TER.ENRR,
  SE.LPV.PRIM), accessed 6 October 2026: https://api.worldbank.org/v2/country/IND/indicator/SE.XPD.TOTL.GD.ZS
- Kremer, Chaudhury, Rogers, Muralidharan and Hammer (2005), JEEA 3(2-3): 658-667:
  https://ideas.repec.org/a/tpr/jeurec/v3y2005i2-3p658-667.html
- Muralidharan, Das, Holla and Mohpal (2017), JPubE 145: 116-135:
  https://ideas.repec.org/a/eee/pubeco/v145y2017icp116-135.html
- Duflo, Hanna and Ryan (2012), AER 102(4): 1241-78: https://ideas.repec.org/a/aea/aecrev/v102y2012i4p1241-78.html
  and NBER w11880: https://www.nber.org/papers/w11880
- Muralidharan and Sundararaman (2011), JPE 119(1): 39-77 (NBER w15323): https://www.nber.org/papers/w15323
- Muralidharan and Sundararaman (2015), QJE 130(3): 1011-1066 (NBER w19441): https://www.nber.org/papers/w19441
- Muralidharan, Singh and Ganimian (2019), AER 109(4): 1426-60: https://ideas.repec.org/a/aea/aecrev/v109y2019i4p1426-60.html
- Banerjee, Cole, Duflo and Linden (2007), QJE 122(3): 1235-1264:
  https://ideas.repec.org/a/oup/qjecon/v122y2007i3p1235-1264..html
- Banerjee et al. (2017), JEP 31(4): 73-102: https://ideas.repec.org/a/aea/jecper/v31y2017i4p73-102.html
- Andrabi, Das and Khwaja (2017), AER 107(6): 1535-63: https://ideas.repec.org/a/aea/aecrev/v107y2017i6p1535-63.html
- Muralidharan and Singh, NBER w28129: https://www.nber.org/papers/w28129
- GEEAP, 2023 Cost-Effective Approaches to Improve Global Learning (World Bank document) and press release 9 May 2023:
  https://documents1.worldbank.org/curated/en/099008110232520373/pdf/IDU-9401bfdd-f4ff-486b-84b4-570be4f65543.pdf
  https://www.worldbank.org/en/news/press-release/2023/05/09/education-smart-buys-cost-effectively-supporting-teachers-and-parents-can-lead-to-significant-learning-improvements
- Pakistan Constitution Art 25A: https://www.pakistani.org/pakistan/constitution/part2.ch1.html
- Geo News, 21 January 2024, PIE Pakistan Education Statistics 2021-22:
  https://www.geo.tv/latest/527871-pakistan-grapples-with-out-of-school-children-crisis-26-million-affected
- Wikipedia, Education in Bangladesh: https://en.wikipedia.org/wiki/Education_in_Bangladesh
- ADB Development Asia policy brief on FSSAP: https://development.asia/policy-brief/maximizing-female-education-subsidy-program-bangladesh
- Constitution of Nepal 2015, Art 31 (Constitute Project): https://www.constituteproject.org/constitution/Nepal_2016
- Wikipedia, C. W. W. Kannangara: https://en.wikipedia.org/wiki/C._W._W._Kannangara
- PRS (as above) on the VBSA Bill; ThePrint, 19 July 2026:
  https://theprint.in/politics/discussed-clause-by-clause-now-put-on-backburner-house-panel-defers-viksit-bharat-shiksha-bill-meet/2990601/
  Careers360, 6 August 2026: https://news.careers360.com/vbsa-bill-parliamentary-committee-seeks-more-time-finalise-draft-report-ugc-aicte-ncte-framework-monsoon-session-lok-sabha
- Fact-check (6 October 2026), primary texts opened: Constitution of India (Legislative Department
  consolidated text: Arts 21A, 37, 45, 51A(k); List III entry 25 and footnotes);
  RTE Act 2009, India Code text (ss 3, 12, 13, 16, 17, 21, 24, Schedule); RTE (Amendment) Act 2019, Gazette;
  Indian Kanoon: Mohini Jain v State of Karnataka (30 July 1992) https://indiankanoon.org/doc/40715/ ;
  Unni Krishnan J.P. v State of Andhra Pradesh (4 February 1993) https://indiankanoon.org/doc/1775396/ ;
  Society for Unaided Private Schools of Rajasthan (12 April 2012); Pramati (6 May 2014)
  https://indiankanoon.org/doc/32468867/ ; Anjuman Ishaat-e-Taleem Trust (1 September 2025 and order of
  30 September 2026) https://indiankanoon.org/doc/49960334/ ; Dinesh Biwaji Ashtikar (13 January 2026,
  orders of 1 and 29 September 2026) https://indiankanoon.org/doc/120977455/ https://indiankanoon.org/doc/45845525/ ;
  UDISE+ 2025-26 and 2024-25 reports (Ministry of Education, Table 1, Table 2.2, Table 6.4);
  PARAKH Rashtriya Sarvekshan 2024 National Report (NCERT, 2025), pp. 2, 5, 8, 10:
  https://parakh.ncert.gov.in/sites/default/files/2025-07/REPORT_India_IND.pdf ;
  Budget Speech 2026-27, 1 February 2026 (indiabudget.gov.in); UGC Act 1956 (No. 3 of 1956), s22 (UGC copy);
  PRS bill page and JPC page for the VBSA Bill 2025 (accessed 6 October 2026):
  https://prsindia.org/billtrack/the-viksit-bharat-shiksha-adhishthan-bill-2025
  https://prsindia.org/parliamentary-committees/joint-committee-on-viksit-bharat-shiksha-adhishthan-bill-2025
- Digital Personal Data Protection Act 2023, ss 2(f), 9, 17(2)(b):
  https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
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


WDR = "World Bank, World Development Report 2018, Overview"
NEP = "National Education Policy 2020, Ministry of Education"
ASER = "ASER Centre, ASER 2024 National findings (rural India), released January 2025"
PRS = "PRS Legislative Research, Demand for Grants 2026-27 Analysis: Education, 17 February 2026"
UD26 = "UDISE+ 2025-26, Ministry of Education, released 7 July 2026"
UD26M = UD26 + " and UDISE+ 2024-25 reports, Ministry of Education"
MEHTA = "A.C. Mehta, analysis of UDISE+ 2025-26 (July 2026)"
PRK = "PARAKH Rashtriya Sarvekshan 2024, National Report (NCERT, 2025)"
WDI = "World Bank, World Development Indicators (UNESCO UIS data), accessed 6 October 2026"
GEEAP = "Global Education Evidence Advisory Panel, 2023 Cost-Effective Approaches to Improve Global Learning"
RTE = "Right of Children to Free and Compulsory Education Act 2009 (No. 35 of 2009)"

DECK = {
    "slug": "education-policy",
    "title": "Education Policy 101",
    "description": ("Education Policy 101: a free foundational course for development practitioners "
                    "in South Asia. Returns to schooling and the learning crisis, Articles 21A, 45 and "
                    "51A(k), the RTE Act 2009 and section 12(1)(c), Kothari to NEP 2020, ASER 2024, "
                    "PARAKH Rashtriya Sarvekshan 2024 and UDISE+ 2025-26, the 2026-27 education budget, "
                    "teachers, private schools, assessment reform, the evidence on what works, "
                    "Bangladesh, Pakistan, Nepal and Sri Lanka, higher education regulation and a "
                    "practitioner toolkit. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Education<br>Policy<br>101",
         "sub": "From enrolment to learning: how South Asian states decide who learns what, who "
                "teaches, who pays and how anyone knows whether it worked",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "RTE to NEP 2020"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Why education policy matters"},
             {"name": "The constitution and the RTE Act"},
             {"name": "From Kothari to NEP 2020"},
             {"name": "Access versus learning: the data"},
             {"name": "Paying for school"},
             {"name": "Teachers"},
             {"name": "Private schools and section 12(1)(c)"},
             {"name": "Accountability and assessment"},
             {"name": "What works: the evidence"},
             {"name": "Neighbours and higher education"},
             {"name": "A practitioner's toolkit"},
             {"name": "Open debates and where next"},
         ]},

        # ===================== SECTION 01 =====================
        DIV("01", "One", "Why education policy matters"),

        S("Starting point", "What education policy actually decides", [
            B("Education policy is the set of public choices that decide who goes to school, for how "
              "long, what they are taught, who teaches them, who pays and how results are checked. "
              "In India those choices are made by Parliament and 36 state and union territory "
              "governments, by courts interpreting the constitution, by district officials who post "
              "teachers, and by head teachers who decide what happens on a Monday morning."),
            TC([P("cyan", "Rules and rights",
                  "The constitution, the Right of Children to Free and Compulsory Education Act "
                  "2009, state rules, board regulations and court orders. They set entitlements: "
                  "a seat in a neighbourhood school, a free midday meal, a qualified teacher.")],
               [P("green", "Money and people",
                  "Budgets, centrally sponsored schemes, teacher recruitment and training, "
                  "textbooks and assessment systems. They decide whether the entitlement turns "
                  "into a classroom where a child learns to read.")]),
            H("indigo", "This course follows both halves: what the law promises and what the data "
              "show is delivered, with South Asian evidence first."),
        ]),

        S("Returns to schooling", "Each year of school pays, and the evidence is global", [
            B("Psacharopoulos and Patrinos (2018) pooled 1,120 estimates of the return to "
              "education from 139 countries between 1950 and 2014. A private return is the extra "
              "earnings a person gains from one more year of schooling, net of what it cost them. "
              "Their headline: the average private return is about 9% a year. Social returns, which count public spending as a cost, "
              "remain high, and women see higher average returns than men."),
            ST([C("9%", "average private return to one more year of schooling, worldwide", "green",
                  "Psacharopoulos and Patrinos (2018), Education Economics 26(5)"),
                C("1,120", "estimates pooled, from 139 countries, 1950-2014", "cyan",
                  "Psacharopoulos and Patrinos (2018)"),
                C("Women", "have higher average returns to schooling than men", "indigo",
                  "Psacharopoulos and Patrinos (2018)")], cols=3),
            H("amber", "Returns are an average across years of schooling. They say little about "
              "whether a particular year taught anything, which is the next slide's problem."),
        ]),

        S("The learning crisis", "Schooling is not the same as learning", [
            B("The World Bank's World Development Report 2018 was the first in the series devoted "
              "entirely to education. Its central message is printed in one line: schooling is not "
              "the same as learning. Enrolment had risen fast in low and middle income countries, "
              "while what children could do after years in class had not kept pace."),
            Q("In rural India in 2016, only half of grade 5 students could fluently read text at the "
              "level of the grade 2 curriculum.", WDR + ", citing ASER Centre (2017)"),
            TC([B("The same report notes that in rural India just under three-quarters of grade 3 "
                  "students could not solve a two-digit subtraction such as 46 minus 17, and by "
                  "grade 5 half still could not.", sm=True)],
               [B("It calls the learning crisis a moral crisis, and shows that it worsens "
                  "inequality: it hobbles the disadvantaged youth who most need what a good "
                  "education can offer.", sm=True)]),
        ]),

        S("Flat learning profiles", "Gaps that start early grow wider every year", [
            TERM("Learning profile",
                 "The relationship between the grade a child is enrolled in and what the child can "
                 "actually do. A flat profile means each extra year in school adds little skill."),
            B("WDR 2018 gives two Indian examples. In Andhra Pradesh in 2010, low-performing "
              "grade 5 students were no more likely to answer a grade 1 question correctly than "
              "grade 2 students. In New Delhi in 2015, the average grade 6 student performed at a "
              "grade 3 level in mathematics, and even by grade 9 had reached less than a grade 5 "
              "level, with the gap between stronger and weaker students growing over time."),
            TC([P("red", "Why it happens",
                  "Curricula move at the pace of the textbook. A child who falls behind in grade 2 "
                  "faces grade 3 material she cannot follow, and the teacher has no time to go "
                  "back.")],
               [P("green", "Why it matters for policy",
                  "Adding years of school without fixing the profile adds cost and little learning. "
                  "Section 9 shows the interventions that bend the profile upward.")]),
        ]),

        S("The case for the state", "Why families and markets alone under-provide education", [
            B("Economists give several reasons why governments fund and regulate schooling instead "
              "of leaving it to private choice. None of them requires the state to run every school, "
              "but each explains why public money and public rules are involved."),
            T(["Reason", "What it means", "South Asian example"],
              [["Credit constraints", "Poor families cannot borrow against a child's future earnings",
                "Children leave school to earn; PLFS 2023-24 data cited by PRS show 44% of "
                "out-of-school 14-18 year olds left to supplement household income"],
               ["Information gaps", "Parents cannot easily see what a school teaches",
                "Report cards in Pakistan changed fees and test scores (Section 8)"],
               ["Spillovers", "An educated neighbour, voter or mother benefits others",
                "Bangladesh's girls' stipend delayed marriage (Section 9)"],
               ["Equity and rights", "Education as a constitutional right, owed to every child",
                "Article 21A in India, 25A in Pakistan, 31 in Nepal"]]),
            H("cyan", "Each reason points to a different tool: money for credit constraints, data for "
              "information gaps, subsidies for spillovers, law for rights."),
        ], compact=True),

        S("Course map", "Four questions this course keeps asking", [
            B("Every section returns to the same four questions. They are a useful checklist for "
              "reading any education scheme, budget line or evaluation you meet in the field."),
            FL(["ACCESS: is every child enrolled and attending?",
                "LEARNING: can they read, write and calculate at grade level?",
                "EQUITY: who is left behind, by gender, caste, place or disability?",
                "MONEY: what does it cost and is the money spent?"]),
            TC([B("India has largely answered the first question for children aged 6 to 14: ASER "
                  "2024 finds 98.1% of rural children in that age group enrolled.", sm=True)],
               [B("The second, third and fourth are open, and this course spends most of its time "
                  "on them: what children learn, who is left behind and what it costs.", sm=True)]),
        ]),

        # ===================== SECTION 02 =====================
        DIV("02", "Two", "The constitution and the RTE Act"),

        S("From directive to right", "How education moved from a promise to an enforceable right", [
            B("When the Constitution came into force in 1950, free and compulsory education for "
              "children sat in Part IV, the Directive Principles of State Policy. Article 37 says "
              "those principles are fundamental in governance but cannot be enforced by any court. "
              "For four decades there was no enforceable right to schooling."),
            TC([P("amber", "Before 2002",
                  "Education was a directive under Article 45. In Mohini Jain (1992) the Supreme "
                  "Court read a right to education into Article 21; in Unni Krishnan (1993) five "
                  "judges confined it to free education until a child completes 14.")],
               [P("green", "After 2002 and 2010",
                  "The Constitution (Eighty-sixth Amendment) Act 2002 inserted Article 21A as a "
                  "fundamental right. It came into force on 1 April 2010, together with the RTE "
                  "Act that gives it content.")]),
            H("indigo", "The 2002 amendment wrote the judge-made right into the text of Part III and "
              "handed its content to Parliament. A parent, a school management committee or a "
              "public interest litigant can go to court on the child's behalf."),
        ]),

        S("The 86th Amendment", "Three articles, three different duties", [
            B("The Constitution (Eighty-sixth Amendment) Act 2002, which received assent on "
              "12 December 2002, changed three articles at once. Read together they split the duty "
              "between the state, for different age groups, and parents."),
            T(["Article", "Text as amended", "Who carries the duty"],
              [["21A (Part III)", "\"The State shall provide free and compulsory education to all "
                "children of the age of six to fourteen years in such manner as the State may, by "
                "law, determine.\"", "The State, enforceable in court"],
               ["45 (Part IV)", "\"The State shall endeavour to provide early childhood care and "
                "education for all children until they complete the age of six years.\"",
                "The State, as a directive"],
               ["51A(k) (Part IVA)", "Parents or guardians to \"provide opportunities for education "
                "to his child or, as the case may be, ward between the age of six and fourteen "
                "years\"", "Parents, as a fundamental duty"]]),
            H("amber", "Early childhood stayed a directive. That is why NEP 2020's push on pre-school "
              "rests on policy and schemes, without a justiciable right behind it."),
        ], compact=True),

        S("Who legislates", "Education is on the Concurrent List", [
            B("Entry 25 of List III (the Concurrent List) reads: \"Education, including technical "
              "education, medical education and universities, subject to the provisions of Entries "
              "63, 64, 65 and 66 of List I; vocational and technical training of labour.\" It was "
              "substituted by the Constitution (Forty-second Amendment) Act 1976, effective "
              "3 January 1977, and State List entry 11 was omitted at the same time."),
            TC([P("cyan", "What the Centre holds",
                  "Entry 25 is expressly subject to Union List entries 63 to 66, which keep some "
                  "subjects with Parliament alone. PRS notes that the Centre is responsible for "
                  "determining the standards of higher education institutions.")],
               [P("green", "What the states hold",
                  "Both can legislate on education generally, but states run most schools, employ "
                  "most teachers and spend most of the money. PRS describes school education as "
                  "a shared responsibility, with states responsible for its development.")]),
            H("indigo", "Source: " + PRS + ". Concurrent status explains why a national policy "
              "such as NEP 2020 needs each state to adopt it in rules, budgets and recruitment."),
        ]),

        S("RTE Act 2009", "The core provisions of the RTE Act", [
            B("The " + RTE + " gives Article 21A its content. It came into force on 1 April 2010. "
              "Its provisions fall into three groups: the child's entitlement, duties of schools and "
              "teachers, and the standards a school must meet."),
            T(["Section", "What it says"],
              [["s3(1)", "Every child aged six to fourteen has a right to free and compulsory "
                "education in a neighbourhood school till completion of elementary education"],
               ["s12(1)(c)", "Unaided and specified schools admit at least 25% of the class I "
                "(or entry) strength from weaker sections and disadvantaged groups"],
               ["s13(1)", "No capitation fee and no screening procedure for the child or parents"],
               ["s17(1)", "\"No child shall be subjected to physical punishment or mental "
                "harassment\""],
               ["s21", "Every school except a private unaided one constitutes a School Management "
                "Committee of local authority representatives, parents or guardians and teachers"],
               ["s24(1)", "Teachers maintain regularity and punctuality and complete the curriculum"],
               ["s25 and Schedule", "Pupil-teacher ratios and minimum norms for every school"]]),
        ], compact=True),

        S("Rights in practice", "What a family can ask for under the RTE Act", [
            B("Statutes are easier to use when they are turned into plain claims. The list below "
              "restates the RTE Act from the point of view of a parent of a child aged six to "
              "fourteen. Each claim points to the section that supports it, which is what a "
              "complaint, a right to information request or a petition will need to cite."),
            TC([BL(["A free place in a neighbourhood school until elementary education is "
                    "complete (s3(1))",
                    "Admission without a capitation fee, an entrance test or a parent interview "
                    "(s13(1))",
                    "A school where the child is not beaten or harassed (s17(1))",
                    "No expulsion before elementary education is complete (s16(4), as amended "
                    "in 2019)"], color="green")],
               [BL(["A seat in a private unaided school under the 25% entry quota, if the family "
                    "falls in a notified group (s12(1)(c))",
                    "A say in a government or aided school through its School Management Committee (s21)",
                    "Teachers who attend regularly and complete the curriculum (s24(1))",
                    "Remedial teaching and a re-examination before any child is held back in "
                    "class 5 or 8 (s16(2))"], color="cyan")]),
            H("amber", "Article 51A(k) also places a duty on the parent to provide opportunities "
              "for education. Rights and duties sit side by side in the constitution, and "
              "officials sometimes cite the second to deflect the first."),
        ]),

        S("Input norms", "The RTE Schedule sets inputs, and says little about outcomes", [
            B("The Schedule to the RTE Act lists what every school must have. Most entries are "
              "inputs that an inspector can count: teachers, classrooms, toilets, working days. "
              "None of them measures what a child has learned."),
            TC([T(["Norm", "Classes I-V", "Classes VI-VIII"],
                  [["Teachers", "Two for up to 60 children; ratio not above 40:1 beyond 200",
                    "At least one per class; subject teachers for science and maths, social "
                    "studies and languages"],
                   ["Working days a year", "200", "220"],
                   ["Instructional hours a year", "800", "1,000"]])],
               [B("Input norms were a reasonable first step in 2009, when many schools lacked "
                  "classrooms, toilets and teachers. They are easy to verify and easy to fund.",
                  sm=True),
                B("The risk is that a school meeting every norm can still leave children unable to "
                  "read. Sections 4 and 8 look at how India has tried to add learning to the "
                  "checklist.", sm=True)], ratio="a32"),
            H("amber", "Source: " + RTE + ", Schedule, India Code text."),
        ]),

        S("No-detention", "Automatic promotion, its repeal and what replaced it", [
            B("The original section 16 of the RTE Act said no child admitted to a school would be "
              "held back in any class or expelled until completing elementary education. Critics "
              "blamed it for weak effort; supporters said holding a child back without extra "
              "teaching only pushes her out of school."),
            TC([P("amber", "RTE (Amendment) Act 2019",
                  "Act No. 1 of 2019, assent 10 January 2019, substituted section 16. There is now "
                  "a regular examination in class 5 and class 8. A child who fails gets additional "
                  "instruction and a re-examination within two months. The appropriate government "
                  "may allow schools to hold her back, or may decide not to.")],
               [P("cyan", "What stays",
                  "New section 16(4): \"No child shall be expelled from a school till the "
                  "completion of elementary education.\" In December 2024 the Centre amended its "
                  "own RTE rules to use the power for schools under it (Careers360, 23 December "
                  "2024).")]),
            H("indigo", "Detention is now a state choice. A practitioner should check the state's "
              "rules before assuming either regime applies."),
        ]),

        S("The courts", "Six judgments that shape the right to education", [
            B("The Supreme Court found a right to education before Parliament wrote one, and has "
              "since decided who the RTE Act binds and how hard the state must work to implement "
              "it. Each case below is still cited."),
            T(["Case", "Date", "What it decided"],
              [["Mohini Jain v State of Karnataka", "30 July 1992", "Two judges: the right to "
                "education flows from the right to life in Article 21; capitation fees violate "
                "Article 14"],
               ["Unni Krishnan J.P. v State of Andhra Pradesh", "4 February 1993", "Five judges: "
                "every child has a right to free education until 14; beyond that the right "
                "depends on the state's economic capacity"],
               ["Society for Unaided Private Schools of Rajasthan v Union of India",
                "12 April 2012", "Three judges, 2-1, upheld s12(1)(c) as a reasonable restriction "
                "under Article 19(6); unaided minority schools exempted"],
               ["Pramati Educational and Cultural Trust v Union of India", "2014",
                "Five judges exempted all minority schools, aided and unaided, from the RTE Act"],
               ["Anjuman Ishaat-e-Taleem Trust v State of Maharashtra", "1 September 2025",
                "Two judges doubted Pramati and referred it to the Chief Justice for a larger bench"],
               ["Dinesh Biwaji Ashtikar v State of Maharashtra", "13 January 2026",
                "Directed governments to frame rules under s38 for s12(1)(c) admissions and the "
                "NCPCR to file an affidavit on them; next listed 27 October 2026"]]),
            H("cyan", "Sources: the judgments and orders on Indian Kanoon. On 30 September 2026 a "
              "three-judge bench sent the Pramati question to the Chief Justice, because Pramati "
              "was decided by five judges. It was pending as of October 2026."),
        ], compact=True),

        # ===================== SECTION 03 =====================
        DIV("03", "Three", "From Kothari to NEP 2020"),

        S("Kothari Commission", "The Education Commission, 1964-66", [
            B("The National Education Commission, chaired by D. S. Kothari, was formed on 14 July "
              "1964 and submitted its report on 29 June 1966. It remains the most cited document in "
              "Indian education policy, and both later national policies borrow its targets."),
            TC([BL(["A uniform <strong>10+2+3</strong> structure of schooling and higher education",
                    "A <strong>common school system</strong> of public education, vocationalised in "
                    "general and special streams",
                    "Work experience and social or national service as part of education",
                    "Raising education spending from 2.9% of GDP to <strong>6%</strong> by "
                    "1985-86"])],
               [P("indigo", "Why it still matters",
                  "The 6% figure reappears in 1968, 1986, 1992 and 2020. The common school idea is "
                  "invoked by the Supreme Court in RTE cases, most recently in 2026.")],
               ratio="a32"),
            H("amber", "Source: Wikipedia, Kothari Commission, summarising the 1966 report; the "
              "Supreme Court's judgment in Dinesh Biwaji Ashtikar (13 January 2026) cites the "
              "commission's common school system."),
        ]),

        S("NPE 1968", "The first National Policy on Education", [
            B("The 1968 National Policy on Education, adopted under Prime Minister Indira Gandhi, "
              "turned many of the Kothari recommendations into national policy. It was a statement "
              "of intent: education was then a state subject and there was no statutory right."),
            T(["Commitment", "What it meant in practice"],
              [["Compulsory education to age 14", "A goal, later carried into Article 45 debates "
                "and finally into Article 21A in 2002"],
               ["Three-language formula", "Hindi, English and the regional language; still "
                "contested in several states"],
               ["Equal educational opportunity", "Called for radical restructuring of the system"],
               ["6% of national income", "Kothari's spending target, adopted as policy"]]),
            H("cyan", "Source: Wikipedia, National Policy on Education. NEP 2020 (para 26.1) states "
              "that the 6% target was \"envisaged by the 1968 Policy, reiterated in the Policy of "
              "1986, and ... further reaffirmed in the 1992 review\"."),
        ]),

        S("NPE 1986 and 1992", "Equity, Operation Blackboard and the Programme of Action", [
            B("The 1986 policy, under Rajiv Gandhi, put special emphasis on removing disparities "
              "for women, Scheduled Castes and Scheduled Tribes. It introduced Operation "
              "Blackboard to equip primary schools, a child-centred approach in primary education, "
              "and an expanded open university system through IGNOU. In 1992 the government under "
              "P. V. Narasimha Rao revised it through a Programme of Action."),
            TC([P("green", "What 1986 added",
                  "A focus on disadvantaged groups, minimum facilities in every primary school, "
                  "and distance education for adults and higher education.")],
               [P("amber", "What it left open",
                  "Like 1968 it was a policy without a statutory right behind it. NEP 2020 calls "
                  "its unfinished agenda \"NPE 1986/92\" and says it \"is appropriately dealt "
                  "with in this Policy\".")]),
            H("indigo", "Three decades separate the 1986 policy and NEP 2020. In between, most "
              "change came through schemes and new law."),
        ]),

        S("Schemes", "DPEP, Sarva Shiksha Abhiyan and Samagra Shiksha", [
            B("Policy statements set direction; centrally sponsored schemes moved the money. The "
              "District Primary Education Programme (DPEP) was funded 85% by the Centre and 15% by "
              "states. Sarva Shiksha Abhiyan (SSA), launched in 2001, aimed to universalise "
              "elementary education, open schools in habitations without one and pull working "
              "children into class."),
            FL(["DPEP: district plans, 85:15 funding",
                "SSA 2001: universal elementary education",
                "RMSA: secondary schooling",
                "Samagra Shiksha 2018: one integrated scheme"]),
            TC([B("In 2018 SSA, Rashtriya Madhyamik Shiksha Abhiyan and teacher education schemes "
                  "were merged into Samagra Shiksha, which now funds school education from "
                  "pre-school to class 12.", sm=True)],
               [B("PRS reports that the Centre and states share Samagra Shiksha funds 60:40 in most "
                  "states and 90:10 in Himalayan and north-eastern states. Its 2026-27 allocation "
                  "is Rs 42,100 crore.", sm=True)]),
            H("amber", "Sources: Wikipedia, Sarva Shiksha Abhiyan; " + PRS + "."),
        ]),

        S("Timeline", "Sixty years of Indian education policy on one page", [
            B("The table puts the main policy, legal and measurement milestones in order. Notice "
              "the shift in the last decade from documents about access to instruments that measure "
              "learning."),
            T(["Year", "Milestone"],
              [["1964-66", "Kothari Commission; report submitted 29 June 1966"],
               ["1968", "First National Policy on Education"],
               ["1976", "42nd Amendment moves education to the Concurrent List (in force 3 January 1977)"],
               ["1986 / 1992", "Second NPE; Programme of Action revision"],
               ["2001", "Sarva Shiksha Abhiyan launched"],
               ["2002", "86th Amendment inserts Article 21A"],
               ["2009 / 2010", "RTE Act passed; Article 21A and the Act in force 1 April 2010"],
               ["2018", "Samagra Shiksha merges SSA and RMSA"],
               ["2019", "RTE amendment replaces automatic promotion"],
               ["2020", "NEP 2020 approved by the Union Cabinet on 29 July 2020"],
               ["2021", "NIPUN Bharat foundational learning mission launched"],
               ["2024", "PARAKH Rashtriya Sarvekshan, the renamed National Achievement Survey"],
               ["2025", "VBSA Bill to replace UGC, AICTE and NCTE introduced, 15 December"]]),
        ], compact=True),

        S("NEP 2020 structure", "NEP 2020 replaces 10+2 with 5+3+3+4", [
            B("NEP 2020 states that \"the extant 10+2 structure in school education will be "
              "modified with a new pedagogical and curricular restructuring of 5+3+3+4 covering "
              "ages 3-18\". The change brings three years of pre-school or anganwadi into the "
              "school system for the first time."),
            T(["Stage", "Years", "Grades", "Ages"],
              [["Foundational", "5", "3 years pre-school or anganwadi + Grades 1-2", "3-8"],
               ["Preparatory", "3", "Grades 3-5", "8-11"],
               ["Middle", "3", "Grades 6-8", "11-14"],
               ["Secondary", "4", "Grades 9-12, in two phases", "14-18"]]),
            TC([B("The foundational stage is meant to be \"flexible, multilevel, play/activity-"
                  "based\". Light textbooks start only in the preparatory stage.", sm=True)],
               [B("The medium of instruction until at least Grade 5, but preferably till Grade 8 "
                  "and beyond, should be the home language or mother tongue \"wherever "
                  "possible\".", sm=True)]),
            H("cyan", "Source: " + NEP + ", paras 4.1-4.2 and 4.11."),
        ], compact=True),

        S("NEP 2020 targets", "The numbers NEP 2020 committed to", [
            B("NEP 2020 is unusually specific about targets. Some have dates that have now passed, "
              "which makes them useful benchmarks for judging delivery."),
            ST([C("5 crore+", "elementary students estimated not to have foundational literacy "
                  "and numeracy (NEP para 2.1)", "red", NEP),
                C("3.22 crore", "out-of-school children aged 6-17, NSS 75th round, 2017-18 "
                  "(NEP para 3.1)", "amber", NEP),
                C("100% GER", "target from pre-school to secondary by 2030", "cyan", NEP),
                C("50% by 2035", "target higher education GER, up from 26.3% in 2018", "indigo",
                  NEP)], cols=4),
            TC([B("Universal foundational literacy and numeracy in primary school was the "
                  "\"highest priority\", to be achieved by 2025. The NIPUN Bharat mission later "
                  "set the target as 2026-27 (PRS, February 2026).", sm=True)],
               [B("Public spending on education was to reach 6% of GDP \"at the earliest\", from "
                  "\"around 4.43%\" in 2017-18 budget estimates (NEP para 26.1).", sm=True)]),
        ]),

        S("Policy versus law", "NEP 2020 is a policy, so it binds only through other instruments", [
            B("NEP 2020 was approved by the Union Cabinet. It is not an Act of Parliament and does "
              "not amend the RTE Act. Each element has to travel through some other instrument "
              "before it binds anyone: a statute, a set of rules, a scheme guideline, a board "
              "regulation or a state government order."),
            TC([P("cyan", "Where NEP has legal teeth",
                  "Where the RTE Act or rules were amended (for example the class 5 and 8 "
                  "examinations), where a scheme makes funds conditional, or where a regulator "
                  "such as a school board changes its own rules.")],
               [P("amber", "Where it does not",
                  "The age-3 start, mother-tongue instruction and the three-language formula "
                  "depend on each state. States can and do adopt parts of NEP and decline "
                  "others, because education is on the Concurrent List.")]),
            H("indigo", "When someone says \"NEP requires\", ask which document turns that "
              "requirement into a rule, and whether the state you work in has adopted it."),
        ]),

        # ===================== SECTION 04 =====================
        DIV("04", "Four", "Access versus learning: the data"),

        S("Enrolment", "Almost every child aged 6 to 14 is enrolled", [
            B("ASER is a household survey run by Pratham and local partners. ASER 2024 reached "
              "649,491 children in 17,997 villages across 605 rural districts. It finds that "
              "enrolment for children aged 6 to 14 has been above 95% for close to 20 years. The "
              "access problem that dominated the 1990s is now largely solved for this age group."),
            ST([C("98.1%", "of rural children aged 6-14 enrolled in school, 2024", "green", ASER),
                C("66.8%", "of rural 6-14 year olds in government schools, 2024 (72.9% in 2022)",
                  "cyan", ASER),
                C("77.4%", "of 3-year-olds in some pre-primary institution, up from 68.1% in 2018",
                  "indigo", ASER),
                C("7.9%", "of 15-16 year olds not enrolled, 2024 (13.1% in 2018)", "amber", ASER)],
              cols=4),
            H("amber", "The 2022 jump in government enrolment came during the pandemic and has "
              "partly reversed. Watch the 15-16 age group: girls not enrolled exceed 10% in Madhya "
              "Pradesh (16.1%), Uttar Pradesh (15%) and Rajasthan (12.7%)."),
        ]),

        S("UDISE+", "The school system in numbers, 2025-26", [
            B("UDISE+ is the Ministry of Education's census of schools. Since 2022-23 it collects "
              "individual student records uploaded by schools, so figures from 2022-23 onward are "
              "not comparable with earlier years. The 2025-26 report was released on 7 July 2026."),
            T(["Indicator", "2024-25", "2025-26"],
              [["Total schools", "14,71,473", "14,66,682"],
               ["Government schools", "10,13,322", "10,05,245"],
               ["Private unaided schools", "3,39,583", "3,41,689"],
               ["Enrolment, Grades I-XII", "23,28,85,600", "23,23,06,857"],
               ["Teachers", "1,01,22,420", "1,02,73,020"],
               ["Single-teacher schools", "1,04,125", "1,00,843"],
               ["Zero-enrolment schools", "7,993", "5,663"]]),
            H("cyan", "Source: " + UD26M + ", Table 1 and Table 2.2. Including pre-primary, 2025-26 "
              "enrolment was 24.72 crore."),
        ], compact=True),

        S("Enrolment ratios", "Primary enrolment is falling and secondary is rising", [
            B("Gross enrolment ratio (GER) divides everyone enrolled at a level by the population "
              "of the official age for that level, so it can exceed 100. Net enrolment ratio (NER) "
              "counts only children of the right age."),
            TC([T(["Level", "GER 24-25", "GER 25-26", "NER 25-26"],
                  [["Primary", "90.9", "89.4", "77.1"],
                   ["Upper primary", "90.3", "89.6", "68.4"],
                   ["Secondary", "78.7", "81.5", "50.8"],
                   ["Higher secondary", "58.4", "61.7", "39.0"]])],
               [B("Primary enrolment (Grades I-V) fell 2.36% in one year, to 10.19 crore. "
                  "Secondary and higher secondary rose 3.0% and 4.4%.", sm=True),
                B("A.C. Mehta (July 2026) reads the primary fall as consistent with falling births and a smaller "
                  "primary-age population, which means fewer children per school and more small "
                  "schools.", sm=True)], ratio="a32"),
            H("amber", "Source: " + UD26M + " (NER from Table 6.4). The higher secondary GER of 61.7 is far "
              "below NEP's 100% target for 2030."),
        ]),

        S("Dropout", "Who leaves school, and why", [
            TC([ST([C("1.8%", "preparatory stage dropout rate, 2025-26", "green", UD26),
                    C("3.6%", "middle stage dropout rate, 2025-26 (3.5% in 2024-25)", "amber", UD26),
                    C("7.0%", "secondary stage dropout rate, 2025-26", "red", UD26),
                    C("51.9%", "secondary retention rate, up from 47.2%", "cyan", UD26)], cols=2)],
               [T(["Reason for not attending (age 14-18)", "Share"],
                  [["Supplement household income", "44%"],
                   ["Domestic chores", "28%"],
                   ["Education not necessary", "8%"],
                   ["School too far", "1%"],
                   ["Other", "19%"]]),
                B("Source: unit-level PLFS 2023-24, Economic Survey 2025-26, as reported by PRS "
                  "(February 2026).", sm=True)]),
            B("Distance is rarely the reason given now. Work and household duties are, which "
              "points to cash transfers, flexible schooling and skilling at secondary level more "
              "than new buildings. PRS notes the Economic Survey 2025-26 recommended integrating "
              "skilling into secondary schools.", sm=True),
        ], compact=True),

        S("ASER reading", "Reading has recovered past its pre-pandemic level", [
            B("ASER tests every sampled child aged 5 to 16 one-on-one at home, using the same "
              "method since 2006. The key indicator is whether a child can read a story at "
              "Standard II level of difficulty."),
            {"t": "chart", "canvas": "aserRead",
             "title": "Government school children who can read a Std II level text (%), rural India",
             "source": ASER,
             "type": "bar",
             "data": {"labels": ["2018", "2022", "2024"],
                      "datasets": [{"label": "Std III", "data": [20.9, 16.3, 23.4],
                                    "backgroundColor": "#0369A1"},
                                   {"label": "Std V", "data": [44.2, 38.5, 44.8],
                                    "backgroundColor": "#047857"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:60, title:{display:true,text:'% of children'} } } }"}},
            H("amber", "The recovery is real, and so is the level: in 2024 more than three in four "
              "government school children in Std III still could not read a Std II text. In "
              "private schools 59.3% of Std V children could, against 44.8% in government schools."),
        ]),

        S("ASER arithmetic", "Arithmetic is at its highest in a decade, from a low base", [
            B("ASER's arithmetic tasks check whether a child can recognise numbers, do a two-digit "
              "subtraction with borrowing, and divide a three-digit number by a one-digit number. "
              "ASER 2024 reports that basic arithmetic reached its highest level in over a decade "
              "in both government and private schools."),
            ST([C("33.7%", "of Std III children can at least do subtraction, all schools (28.2% in "
                  "2018)", "cyan", ASER),
                C("27.6%", "the same for Std III in government schools (20.2% in 2022)", "indigo",
                  ASER),
                C("30.7%", "of Std V children can do division (27.9% in 2018)", "amber", ASER),
                C("45.8%", "of Std VIII children can do division (44.1% in 2018)", "red", ASER)],
              cols=4),
            TC([B("Gains are concentrated in the early grades, where the foundational learning "
                  "mission has focused since 2021.", sm=True)],
               [B("Std VIII barely moved. More than half of children about to finish elementary "
                  "school cannot divide a three-digit number by a one-digit number.", sm=True)]),
        ]),

        S("PARAKH 2024", "The government's own survey shows scores falling with each stage", [
            B("PARAKH Rashtriya Sarvekshan 2024, the successor to the National Achievement Survey, "
              "tested 21,15,022 students in Grades 3, 6 and 9 on 4 December 2024, in over 74,000 "
              "government, aided, private and central schools in 781 districts."),
            {"t": "chart", "canvas": "parakhChart",
             "title": "Average score (out of 100) by grade, PARAKH Rashtriya Sarvekshan 2024",
             "source": PRK,
             "type": "bar",
             "data": {"labels": ["Grade 3", "Grade 6", "Grade 9"],
                      "datasets": [{"label": "Language", "data": [64, 57, 54],
                                    "backgroundColor": "#0369A1"},
                                   {"label": "Mathematics", "data": [60, 46, 37],
                                    "backgroundColor": "#B45309"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'Average score'} } } }"}},
            H("indigo", "The same report gives Grade 9 state government school averages of 48 in "
              "language and 33 in mathematics, against 69 and 48 in central government schools."),
        ]),

        S("Reading two surveys", "ASER and PARAKH measure different things on purpose", [
            B("Practitioners often see ASER and PARAKH numbers quoted side by side as if they "
              "measure the same thing. They do not use the same sample, method or bar, so a "
              "difference between them is not by itself a sign that one is wrong."),
            T(["Feature", "ASER 2024", "PARAKH Rashtriya Sarvekshan 2024"],
              [["Run by", "Pratham and local partners", "PARAKH at NCERT, Ministry of Education"],
               ["Where", "Households, rural districts only", "Schools, all 36 states and UTs"],
               ["Who", "Children aged 3-16, in or out of school", "Students in Grades 3, 6 and 9"],
               ["Test", "One-on-one, basic reading and arithmetic", "Written, competency-based "
                "test booklets"],
               ["Reports", "Share of children at each level", "Average percentage score"],
               ["Scale", "649,491 children", "21,15,022 students"]]),
            H("cyan", "Use ASER for foundational skills and out-of-school children; use PARAKH for "
              "curriculum-linked competencies and comparisons across school types and states."),
        ], compact=True),

        # ===================== SECTION 05 =====================
        DIV("05", "Five", "Paying for school"),

        S("The 6% target", "Sixty years of a spending target that has not been met", [
            B("Every Indian education policy since 1966 has named the same target: public spending "
              "on education of 6% of GDP. Kothari recorded a starting point of 2.9%. NEP 2020 put "
              "the level at around 4.43% in 2017-18. The PRS analysis of the 2026-27 budget "
              "estimates combined Centre and state spending at 4.1% of GDP in 2022-23."),
            ST([C("2.9%", "of GDP when the Kothari Commission reported, 1966", "red",
                  "Wikipedia, Kothari Commission"),
                C("4.43%", "Centre plus states, 2017-18 budget estimates", "amber", NEP),
                C("4.1%", "Centre plus states, 2022-23", "cyan", PRS),
                C("6%", "target in 1966, 1968, 1986, 1992 and 2020", "green", NEP)], cols=4),
            TC([B("PRS compares India's 4.1% (2022) with Germany 5.2% (2022), and the US 5.4% and the "
                  "UK 5.9% (2021), from World Bank data. China is 4.0% (2023).", sm=True)],
               [B("A percentage of GDP is a blunt measure. A rising GDP and a falling child "
                  "population both change what a given share buys per pupil.", sm=True)]),
        ]),

        S("Union budget 2026-27", "The Ministry of Education's budget for 2026-27", [
            B("The Union Budget 2026-27, presented on 1 February 2026, allocated Rs 1,39,289 crore "
              "to the Ministry of Education, 14% more than the 2025-26 revised estimate. School "
              "education took 60% and higher education 40%."),
            T(["Head", "2024-25 actual", "2025-26 RE", "2026-27 BE"],
              [["School education", "65,159", "70,567", "83,562"],
               ["of which Samagra Shiksha", "36,502", "38,000", "42,100"],
               ["of which PM POSHAN (midday meals)", "9,903", "10,600", "12,750"],
               ["of which PM SHRI schools", "3,504", "4,500", "7,500"],
               ["Higher education", "45,577", "51,382", "55,727"],
               ["of which central universities", "16,042", "17,085", "17,440"],
               ["of which IITs", "10,309", "11,525", "12,123"],
               ["Total, Ministry of Education", "1,10,736", "1,21,949", "1,39,289"]]),
            H("cyan", "Rs crore. Source: " + PRS + ", from Demands No. 25 and 26, Expenditure "
              "Budget 2026-27."),
        ], compact=True),

        S("Where the money goes", "Samagra Shiksha and higher education dominate", [
            B("The Union budget is only part of public education spending, because states pay most "
              "teacher salaries. Within the Union's share, three lines stand out: Samagra Shiksha, "
              "the midday meal and the central institutions of higher education."),
            {"t": "chart", "canvas": "moeChart",
             "title": "Ministry of Education allocation 2026-27 (Rs crore)",
             "source": PRS,
             "type": "doughnut",
             "data": {"labels": ["Samagra Shiksha", "PM POSHAN", "PM SHRI",
                                 "KVs, JNVs, NCERT and other autonomous bodies",
                                 "Other school education", "Higher education"],
                      "datasets": [{"data": [42100, 12750, 7500, 16867, 4345, 55727],
                                    "backgroundColor": ["#0369A1", "#047857", "#B45309",
                                                        "#4F46E5", "#64748B", "#B91C1C"]}]},
             "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
            H("amber", "PRS estimates education at around 2.4% to 2.6% of the overall Union budget "
              "between 2024-25 and 2026-27. Across all levels of government, WDI puts education at "
              "14.2% of government expenditure in India in 2022."),
        ]),

        S("Fiscal federalism", "Who pays for a government school", [
            B("A government school in Bihar or Tamil Nadu is funded by several streams at once. "
              "Most of the cost is teacher salaries paid from the state budget. The Centre adds "
              "money through centrally sponsored schemes that the state must match."),
            TC([FL(["State budget: salaries, most recurrent cost",
                    "Samagra Shiksha: 60:40 (90:10 in Himalayan and north-eastern states)",
                    "PM POSHAN: midday meal, pre-primary to Grade 8",
                    "PM SHRI: about 14,500 model schools, 2022-23 to 2027-28"])],
               [B("PM POSHAN, launched in 2021-22, subsumed the midday meal scheme and covers "
                  "nearly 11.2 crore children in government and aided schools.", sm=True),
                B("PM SHRI's central share for 2022-23 to 2027-28 is Rs 18,128 crore and the state "
                  "share Rs 9,232 crore; 13,070 schools had been upgraded by January 2026.",
                  sm=True)]),
            H("indigo", "Source: " + PRS + ". Matching grants mean a state that cannot find its "
              "40% leaves central money unspent."),
        ]),

        S("Spending the money", "Allocations are only half the story", [
            B("A budget line shows intent. Whether the money reaches schools depends on release, "
              "spending and timing. The PRS analysis records several gaps that matter to anyone "
              "monitoring a scheme."),
            T(["Finding", "Detail"],
              [["Late spending", "By February 2025 the school education department had spent about "
                "59% of its allocation, leaving the rest for the last two months"],
               ["Committee advice", "Standing Committee (2025): last-quarter spending at most 33% "
                "of the allocation, and at most 15% in the final month"],
               ["NIPUN Bharat", "Rs 7,178 crore approved for 2021-22 to 2023-24; Rs 5,007 crore "
                "(70%) spent"],
               ["PM USHA (higher education)", "On average 16% of allocated funds spent between "
                "2022-23 and 2024-25"],
               ["Teacher training", "Ministry spending fell from Rs 599 crore (2019-20) to Rs 96 "
                "crore (2022-23)"]]),
            H("cyan", "Source: " + PRS + ". A March rush of spending usually buys goods and "
              "events. It rarely buys the year-round teaching support a learning programme needs."),
        ], compact=True),

        S("Household spending", "Families pay even in free government schools", [
            B("The National Statistics Office ran a Comprehensive Modular Survey on Education from "
              "April to June 2025. PRS summarises what households told it about the cost of "
              "school, which matters because the RTE Act promises free education to age 14."),
            ST([C("10x", "cost of a private school relative to a government school, 2025", "red",
                  PRS + ", citing NSO CMS: Education 2025"),
                C("27%", "of government school students report paying course fees at some level",
                  "amber", PRS + ", citing NSO CMS: Education 2025"),
                C("Rs 2,863", "average annual cost per student in a government school (fees and "
                  "transport)", "cyan", PRS + ", citing NSO CMS: Education 2025"),
                C("9.6 crore", "children in private schools, 2024-25", "indigo",
                  PRS + ", citing UDISE+ 2024-25")], cols=4),
            TC([B("About 8% of government school students in Grades 1 to 8 pay an average course "
                  "fee of Rs 229 a year, inside the RTE age band.", sm=True)],
               [B("Private enrolment kept rising despite the tenfold cost gap, which tells you "
                  "parents are paying for something they value. Section 7 asks what.", sm=True)]),
        ]),

        S("Money and learning", "More inputs alone rarely raise learning", [
            B("The 2023 report of the Global Education Evidence Advisory Panel (GEEAP) lists "
              "\"funding additional inputs alone, when other issues are not addressed\" as a bad "
              "buy. Its examples are textbooks, additional teachers to reduce class size, "
              "buildings, grants, salary and libraries."),
            TC([P("red", "The fiscal cost of absence",
                  "Muralidharan, Das, Holla and Mohpal (2017) found 23.6% of teachers absent in "
                  "unannounced visits to 1,297 villages and put the salary cost of unauthorised "
                  "absence at $1.5 billion a year.")],
               [P("green", "Where money works",
                  "The same study estimates better monitoring could be over ten times more cost "
                  "effective at raising the effective pupil-teacher ratio than hiring more "
                  "teachers.")]),
            H("indigo", "The argument is about the next rupee. Inputs matter where they are "
              "missing; where they exist, how they are used decides learning. Sources: " + GEEAP
              + "; Journal of Public Economics 145 (2017)."),
        ]),

        # ===================== SECTION 06 =====================
        DIV("06", "Six", "Teachers"),

        S("The workforce", "India now has more than one crore school teachers", [
            B("UDISE+ 2024-25 recorded, for the first time, more than one crore teachers. By "
              "2025-26 the count was 1,02,73,020. Teachers are the largest item in every state "
              "education budget, so how they are recruited, posted and supported is the biggest "
              "spending decision in education policy."),
            ST([C("1.03 crore", "school teachers, 2025-26", "cyan", UD26),
                C("54.9%", "of teachers are women, 2025-26", "green", UD26),
                C("10 : 1", "pupil-teacher ratio, foundational stage", "indigo", UD26),
                C("21 : 1", "pupil-teacher ratio, secondary stage", "amber", UD26)], cols=4),
            TC([B("National averages look comfortable against the RTE Schedule's ceiling of 40 "
                  "pupils per teacher at primary level. The problem lies in distribution.", sm=True)],
               [B("PRS reports higher secondary ratios of 47:1 in Jharkhand, 37:1 in Maharashtra "
                  "and Odisha, and 35:1 in Uttar Pradesh in 2024-25.", sm=True)]),
        ]),

        S("Vacancies", "Ten lakh posts vacant", [
            B("NEP 2020 says teacher vacancies \"will be filled at the earliest, in a time-bound "
              "manner\", especially in disadvantaged areas. Six years later, PRS reports that "
              "nearly 10 lakh teaching posts were vacant in 2024-25, citing the Rajya Sabha "
              "Standing Committee on Education's 368th report (August 2025)."),
            TC([BL(["Lack of regular recruitment",
                    "Posts not sanctioned",
                    "Shortage of subject-specialist teachers",
                    "Small schools that make distribution hard"], color="red")],
               [P("amber", "Contract teachers",
                  "The Standing Committee noted that contractual recruitment in central "
                  "government schools such as Kendriya Vidyalayas nearly doubled between "
                  "2023-24 and 2024-25, and recommended filling vacancies through regular "
                  "appointment.")]),
            H("indigo", "Reasons as listed by " + PRS + ". Vacancy counts depend on sanctioned "
              "posts, which states set themselves, so compare states with care."),
        ]),

        S("Small schools", "One lakh schools still have a single teacher", [
            B("A single-teacher school asks one adult to teach several grades at once, keep "
              "records, run the midday meal and attend training. When that teacher is absent the "
              "school is closed. UDISE+ shows the number falling steadily, partly through "
              "consolidation."),
            TC([T(["Year", "Single-teacher schools", "Zero-enrolment schools"],
                  [["2022-23", "1,18,190", "10,294"],
                   ["2023-24", "1,10,971", "12,954"],
                   ["2024-25", "1,04,125", "7,993"],
                   ["2025-26", "1,00,843", "5,663"]])],
               [B("Falling primary enrolment means more schools with few children. Merging them "
                  "can free teachers but lengthens journeys for the youngest children.", sm=True),
                B("Government schools fell by 8,077 in 2025-26 while private unaided schools rose "
                  "by 2,106.", sm=True)], ratio="a32"),
            H("amber", "Sources: PIB release on UDISE+ 2024-25, 28 August 2025 (2022-23 and "
              "2023-24); " + UD26M + "."),
        ]),

        S("Absence in 2003", "One in four teachers absent on any given day", [
            B("Kremer, Chaudhury, Rogers, Muralidharan and Hammer (2005) made surprise visits to "
              "government primary schools across India. Their snapshot, published in the "
              "Journal of the European Economic Association, became the reference figure for "
              "teacher absence in South Asia."),
            ST([C("25%", "of teachers absent from school during unannounced visits", "red",
                  "Kremer et al. (2005), JEEA 3(2-3)"),
                C("15%", "absence in Maharashtra, the lowest state", "green", "Kremer et al. (2005)"),
                C("42%", "absence in Jharkhand, the highest state", "amber",
                  "Kremer et al. (2005)")], cols=3),
            TC([P("green", "Lower absence where",
                  "Schools had been inspected recently, had better infrastructure and were closer "
                  "to a paved road.")],
               [P("red", "No difference where",
                  "Teachers were paid more, were locally recruited, or the school had a parent "
                  "association.")]),
        ]),

        S("Absence a decade on", "Absence fell only slightly, and the cost is large", [
            B("Muralidharan, Das, Holla and Mohpal (2017) revisited a nationally representative "
              "panel of 1,297 villages. Absence had fallen only a little, to 23.6%, while "
              "pupil-teacher ratios had improved. Their paper links the two: hiring more teachers "
              "and reducing pupil-teacher ratios was associated with higher absence."),
            TC([ST([C("23.6%", "teachers absent in unannounced visits", "red",
                      "Muralidharan et al. (2017), JPubE 145"),
                    C("$1.5 bn", "annual salary cost of unauthorised absence", "amber",
                      "Muralidharan et al. (2017)")], cols=1)],
               [B("More frequent monitoring was strongly associated with lower absence.", sm=True),
                B("The authors estimate that better monitoring could be over ten times more cost "
                  "effective at raising the effective pupil-teacher ratio than hiring additional "
                  "teachers.", sm=True),
                B("This is correlational evidence from a panel. The next slide turns to "
                  "experiments.", sm=True)], ratio="a23"),
            H("indigo", "Absence is a management failure more than a moral one: it falls where "
              "someone checks."),
        ]),

        S("Incentives", "Two experiments on teacher incentives", [
            B("Two randomised experiments in India tested whether changing teachers' incentives "
              "changes what children learn. Both found that it does, at modest cost."),
            T(["Study", "Setting and design", "Result"],
              [["Duflo, Hanna and Ryan (2012), AER 102(4)", "60 informal one-teacher schools in "
                "rural India; a child photographed the teacher and students at the start and end "
                "of each day with a tamper-proof camera; pay tied to attendance",
                "Absence fell from 42% in comparison schools to 22%; test scores 0.17 standard "
                "deviations higher after one year"],
               ["Muralidharan and Sundararaman (2011), JPE 119(1)", "Government rural primary "
                "schools in Andhra Pradesh; bonus tied to students' test score gains, mean bonus "
                "3% of annual pay", "After two years, 0.28 SD in maths and 0.16 SD in language; "
                "gains also in subjects without incentives"]]),
            H("amber", "Effects are in standard deviations (SD) of the test score distribution, so "
              "they can be compared across tests. The performance pay schools also beat schools "
              "given extra inputs of similar value."),
        ], compact=True),

        S("Qualifications and training", "Many teachers lack professional qualifications", [
            B("Section 23 of the RTE Act requires teachers to hold the minimum qualifications set "
              "by an academic authority; the National Council for Teacher Education sets them. "
              "UDISE+ 2024-25, as reported by PRS, shows the gap by level."),
            TC([T(["Level", "Professionally unqualified"],
                  [["Pre-primary", "52%"],
                   ["Grades 1-5", "12%"],
                   ["Grades 6-8", "12%"],
                   ["Grades 9-10", "10%"],
                   ["Grades 11-12", "11%"]])],
               [B("Qualification is not the same as competence, but an untrained teacher of "
                  "four-year-olds is a direct risk to NEP's foundational stage.", sm=True),
                B("NISHTHA, the in-service training programme launched in 2019 under Samagra "
                  "Shiksha, had trained 43% of targeted teachers and 49% of targeted school "
                  "heads by January 2026 (PRS).", sm=True),
                B("In <em>Anjuman Ishaat-e-Taleem Trust</em> (1 September 2025) the Supreme Court "
                  "held the TET binding on teachers recruited before the RTE Act: those with more than five years "
                  "to retire must pass it within two years or leave service; those with less may "
                  "stay without it but cannot be promoted (paras 216-217).", sm=True)]),
            H("amber", "Source: " + PRS + ". Ministry spending on teacher training fell from "
              "Rs 599 crore in 2019-20 to Rs 96 crore in 2022-23."),
        ]),

        S("Community teachers", "Local tutors can teach the basics well", [
            B("Banerjee, Cole, Duflo and Linden (2007) evaluated Pratham's Balsakhi programme, "
              "which hired young women from the community to teach basic literacy and numeracy to "
              "children who had fallen behind. These tutors had far less training than regular "
              "teachers."),
            TC([ST([C("0.28 SD", "rise in average test scores of all children in treatment schools",
                      "green", "Banerjee et al. (2007), QJE 122(3)"),
                    C("0.10 SD", "gain remaining for targeted children a year after the programme "
                      "ended", "amber", "Banerjee et al. (2007)")], cols=1)],
               [B("The gains were largest for the weakest students, which is the group a flat "
                  "learning profile leaves behind.", sm=True),
                B("GEEAP (2023) rates \"augmenting teaching teams with community-hired staff\" as "
                  "promising but with limited evidence on cost-effectiveness at scale.", sm=True),
                B("For policy the lesson is targeted: a tutor teaching at the child's level can "
                  "work, but it is a complement to regular teachers.", sm=True)], ratio="a23"),
        ]),

        # ===================== SECTION 07 =====================
        DIV("07", "Seven", "Private schools and section 12(1)(c)"),

        S("The private shift", "Private unaided schools now teach 38% of students", [
            B("UDISE+ 2025-26 shows government schools' share of Grades I-XII enrolment slipping "
              "below half, while private unaided schools gained about 25 lakh students in a year in "
              "which total enrolment fell."),
            {"t": "chart", "canvas": "mgmtChart",
             "title": "Share of Grades I-XII enrolment by school management, 2025-26 (%)",
             "source": MEHTA + ", from UDISE+ 2025-26",
             "type": "doughnut",
             "data": {"labels": ["Government", "Government aided", "Private unaided", "Others"],
                      "datasets": [{"data": [49.66, 10.45, 37.97, 1.92],
                                    "backgroundColor": ["#0369A1", "#047857", "#B45309", "#64748B"]}]},
             "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
            H("amber", "In 2024-25 the government share was 50.83% and private unaided 36.80%. "
              "Rural figures differ: ASER 2024 finds 66.8% of rural children aged 6-14 in "
              "government schools."),
        ]),

        S("Why parents choose", "What parents say they pay for", [
            B("The NSSO survey of household social consumption on education (2017-18) asked "
              "students in private institutions why they chose them. PRS reproduces the "
              "answers. Quality and proximity dominate, with English medium a strong third."),
            TC([T(["Reason given", "Share of respondents"],
                  [["Quality of public institution not satisfactory", "34%"],
                   ["Private institution located nearby", "27%"],
                   ["Uses English as medium of instruction", "17%"],
                   ["Facilities such as transport and hostels", "14%"]])],
               [B("Perceived quality and English are both signals that a parent can see. Learning "
                  "levels are much harder for a parent to observe.", sm=True),
                B("That information gap is why report cards and published assessment results "
                  "(Section 8) can change school markets.", sm=True)]),
            H("cyan", "Source: " + PRS + ", citing NSSO, Household Social Consumption on "
              "Education in India, 2017-18."),
        ]),

        S("Private versus public", "Raw gaps overstate what private schools add", [
            B("ASER 2024 finds 59.3% of Std V children in rural private schools can read a Std II "
              "text, against 44.8% in government schools. That gap mixes two things: what the "
              "school adds, and which families choose private schools in the first place."),
            TC([P("amber", "Selection",
                  "Families who pay fees tend to be better off and more educated, with more "
                  "books and help at home. Their children would score higher in any school.")],
               [P("cyan", "Value added",
                  "To isolate the school's contribution you need a design that compares similar "
                  "children, such as a lottery. The next slide describes one from Andhra "
                  "Pradesh.")]),
            TERM("Selection bias",
                 "A difference between groups caused by who chooses to join each group, mistaken "
                 "for the effect of the group itself. See " + L("causal-inference.html",
                                                                 "Causal Inference 101") + "."),
        ]),

        S("A school voucher experiment", "Evidence from a school voucher lottery in Andhra Pradesh", [
            B("Muralidharan and Sundararaman (2015, QJE 130(3)) studied a programme in Andhra "
              "Pradesh that gave students vouchers to attend a private school of their choice. A "
              "two-stage lottery, first across villages and then across applicants, let them "
              "measure both the effect on winners and spillovers on everyone else."),
            ST([C("No gap", "in Telugu and maths test scores between lottery winners and losers "
                  "after two and four years", "amber", "Muralidharan and Sundararaman (2015)"),
                C("Under 1/3", "the cost per student in private schools, relative to public "
                  "schools in the sample", "green", "Muralidharan and Sundararaman (2015)"),
                C("No spillover", "harm to public school students or to private school students",
                  "cyan", "Muralidharan and Sundararaman (2015)")], cols=3),
            H("indigo", "The authors conclude private schools in this setting delivered slightly "
              "better test score gains than public ones at much lower cost per student. Test scores are "
              "one outcome; the study does not settle questions of equity or segregation."),
        ]),

        S("How 12(1)(c) works", "A quarter of entry seats in private schools for disadvantaged children", [
            B("Section 12(1)(c) of the RTE Act requires unaided schools to admit, in class I (or "
              "the entry class), \"to the extent of at least twenty-five per cent. of the strength "
              "of that class\", children from weaker sections and disadvantaged groups in the "
              "neighbourhood, and to provide free education till elementary completion."),
            FL(["STATE notifies weaker sections and disadvantaged groups",
                "SCHOOL declares entry seats",
                "LOTTERY or portal allots seats",
                "STATE reimburses the school under s12(2)"]),
            TC([B("Under s12(2) the state reimburses the lower of its own per-child expenditure "
                  "and the school's actual fee.", sm=True)],
               [B("Section 13(1) bars capitation fees and screening, so a school cannot test a "
                  "child or interview parents to fill these seats.", sm=True)]),
            H("cyan", "Source: " + RTE + ", ss 12-13. In 2012 the Supreme Court upheld the "
              "provision as a reasonable restriction on the freedom to run a business."),
        ]),

        S("Implementation gaps", "Sixteen years on, the Supreme Court is still asking for compliance", [
            B("In Dinesh Biwaji Ashtikar v State of Maharashtra (13 January 2026) the Supreme "
              "Court held that without enforceable rules \"the object of Article 21A and the "
              "statutory policy under Section 12(1)(c) would be a dead letter\". It identified "
              "practical barriers that a practitioner will recognise."),
            TC([BL(["Online application portals that assume digital literacy",
                    "Forms and notices in languages parents do not read",
                    "No public list of how many seats each school has",
                    "Refusals without written reasons"], color="red")],
               [BL(["Rules under s38 framed with NCPCR and state commissions (a direction)",
                    "NCPCR to collate the rules and file an affidavit by 31 March 2026",
                    "Seats published before applications open (guideline)",
                    "Denials recorded with reasons and reviewed by the Block Education Officer "
                    "within 72 hours (guideline)",
                    "Help-desks and a window to correct defective forms (guideline)"],
                   color="green")]),
            H("amber", "Source: the judgment, paras 13-16. On 29 September 2026 the Court asked "
              "the NCPCR chairperson to appear and listed the case on 27 October 2026; check the "
              "latest order before relying on it."),
        ]),

        S("Regulating private schools", "Four levers a state can pull", [
            B("Once private schools educate four in ten children, regulating them well becomes "
              "education policy. States have used four broad levers, and each has a cost."),
            T(["Lever", "What it does", "Risk"],
              [["Recognition norms", "Minimum land, buildings and teacher norms before a school can "
                "operate", "Low-fee schools close or operate unrecognised"],
               ["Fee regulation", "Caps or approvals for fee increases", "Schools cut spending or "
                "add hidden charges"],
               ["Seat mandates", "s12(1)(c) admissions with reimbursement", "Late or low "
                "reimbursement turns schools against the scheme"],
               ["Information", "Publishing learning results for every school", "Teaching to the "
                "test if the measure is narrow"]]),
            H("cyan", "Information has the clearest evidence. Andrabi, Das and Khwaja (2017, AER "
              "107(6)) gave report cards to parents in Pakistani villages: test scores rose 0.11 "
              "SD, private fees fell 17% and primary enrolment rose 4.5%."),
        ], compact=True),

        # ===================== SECTION 08 =====================
        DIV("08", "Eight", "Accountability and assessment"),

        S("Accountability", "Three ingredients of accountability in a school system", [
            B("WDR 2018 asks systems to \"assess learning\" and \"act on evidence\". Making a "
              "school system answer for learning needs three things that are often missing at the "
              "same time: someone has to know how children are doing, someone has to care, and "
              "someone has to be able to change what happens."),
            FL(["INFORMATION: credible data on learning",
                "INCENTIVES: consequences or recognition tied to it",
                "CAPACITY: skills and time to respond",
                "FEEDBACK: the next measurement shows whether it worked"]),
            TC([P("amber", "Information without capacity",
                  "A head teacher told her school is weak, with no support or authority to change "
                  "anything, can only file the report.")],
               [P("amber", "Incentives without information",
                  "Rewards tied to enrolment or attendance registers push schools to improve the "
                  "register, which is easier than improving the learning.")]),
        ]),

        S("National assessment", "From NAS to PARAKH Rashtriya Sarvekshan", [
            B("NEP 2020 (para 4.41) proposed a national assessment centre, PARAKH, as a "
              "standard-setting body that would also run the National Achievement Survey and "
              "guide State Achievement Surveys. PARAKH sits within NCERT. Its 2024 survey is "
              "described as the large-scale assessment of India, also known as NAS."),
            T(["Grade", "Language 2017", "Language 2021", "Maths 2017", "Maths 2021"],
              [["3", "67", "62", "63", "57"],
               ["5", "58", "55", "53", "44"],
               ["8", "56", "53", "42", "36"],
               ["10", "36", "43", "34", "32"]]),
            H("amber", "Average scores out of 100, National Achievement Survey 2017 and 2021, as "
              "reported by " + PRS + ". Scores fell between 2017 and 2021 in grades 3, 5 and 8 in "
              "both subjects, spanning the pandemic school closures."),
        ], compact=True),

        S("School management committees", "Parents on the committee do not guarantee a voice", [
            B("Section 21 of the RTE Act requires every government and aided school to form a "
              "School Management Committee with local authority representatives, parents or "
              "guardians and teachers. The idea is the short route of accountability: parents "
              "watch the school directly instead of waiting for the state to act."),
            TC([P("amber", "What the evidence says",
                  "Kremer et al. (2005) found that schools with parent associations had no lower "
                  "teacher absence. GEEAP (2023) lists \"involving communities in school "
                  "management\" as promising but with limited evidence.")],
               [P("green", "What helps a committee work",
                  "Information parents can use (a simple reading test of their own children), "
                  "authority over some money, and a clear channel to escalate complaints.")]),
            H("cyan", "A committee that exists on paper satisfies s21. Whether it changes "
              "anything depends on what it knows and what it controls."),
        ]),

        S("Information as a tool", "Telling parents and teachers what children know", [
            B("GEEAP (2023) rates \"providing information on the benefits, costs, and quality of "
              "education\" as a great buy, its highest category. The logic is simple: families "
              "decide how long a child stays in school and which school to pick, so better "
              "information changes decisions at very low cost."),
            TC([ST([C("+0.11 SD", "test scores in villages that received school report cards",
                      "green", "Andrabi, Das and Khwaja (2017), AER 107(6)"),
                    C("-17%", "private school fees in those villages", "cyan",
                      "Andrabi, Das and Khwaja (2017)")], cols=1)],
               [B("The Pakistan experiment randomly assigned half the sample villages to receive "
                  "report cards showing schools' test results.",
                  sm=True),
                B("Weaker private schools improved or cut fees, and enrolment rose 4.5%.",
                  sm=True),
                B("ASER's citizen-led testing in India rests on the same idea at national scale: "
                  "a number that anyone can understand.", sm=True)], ratio="a23"),
        ]),

        S("When reform becomes paperwork", "A management reform that changed nothing", [
            B("Muralidharan and Singh (NBER Working Paper 28129) evaluated a large school "
              "management programme in India: comprehensive school assessments, detailed school "
              "ratings and customised improvement plans in 1,774 schools. It did not change "
              "incentives or accountability."),
            ST([C("1,774", "schools in the experiment", "cyan", "Muralidharan and Singh, NBER w28129"),
                C("No impact", "on school functioning or student outcomes", "red",
                  "Muralidharan and Singh, NBER w28129"),
                C("600,000+", "schools in the national scale-up; in the state studied it still did not "
                  "raise learning", "amber", "Muralidharan and Singh, NBER w28129")], cols=3),
            H("indigo", "Interviews with officials found the main effect on the ground was more "
              "reporting and paperwork. Assessments were completed and the ratings were "
              "informative, so the programme looked successful on compliance measures."),
        ]),

        S("Board exams", "Lowering the stakes of board examinations", [
            B("NEP 2020 (para 4.36) says board and entrance examinations force students to "
              "concentrate on a few subjects and reward coaching. It keeps Grade 10 and 12 boards "
              "but asks for them to test core capacities and to lower the stakes."),
            TC([P("cyan", "What NEP proposes",
                  "Students may take board exams on up to two occasions in a school year, one "
                  "main and one for improvement. Boards may move to annual, semester or modular "
                  "exams. School examinations in Grades 3, 5 and 8 track progress.")],
               [P("amber", "Trade-offs",
                  "Two attempts reduce the cost of one bad day but add administrative load. "
                  "Exams in Grades 5 and 8 can now lead to detention (Section 2), so the same "
                  "test carries higher stakes for younger children.")]),
            H("indigo", "Source: " + NEP + ", paras 4.36-4.40. Implementation varies by board; "
              "check the board's current scheme before advising students."),
        ]),

        S("Data quality", "Know the limits of the numbers you cite", [
            B("Education policy in India runs on administrative data. UDISE+ figures are uploaded "
              "by schools holding active codes, and the Ministry disclaims responsibility for errors "
              "in that self-reported data. Since 2022-23 the data are individual student records, "
              "so they cannot be compared with 2021-22 and earlier."),
            TC([BL(["Registers count enrolment; attendance can be far lower",
                    "Dropout rates are derived from year-to-year records",
                    "GER depends on population projections, which age as the Census ages",
                    "Learning surveys differ in sample and method"], color="amber")],
               [P("green", "Practical rules",
                  "Cite the year and source of every number. Do not join series across a method "
                  "break. Prefer household surveys for out-of-school children. Triangulate a "
                  "surprising figure against a second source.")]),
            H("cyan", "The Census with reference date 1 March 2027 will reset the population "
              "denominators behind GER and NER. Source for UDISE+ caveats: " + UD26M + "."),
        ]),

        # ===================== SECTION 09 =====================
        DIV("09", "Nine", "What works: the evidence"),

        S("Smart buys", "The GEEAP ranking of education interventions", [
            B("The Global Education Evidence Advisory Panel, convened by the UK FCDO, UNICEF, "
              "USAID and the World Bank, reviewed more than 550 evaluations for its "
              "2023 report and sorted interventions by cost-effectiveness and evidence of working "
              "at scale. Its members include Rukmini Banerji of Pratham, Karthik Muralidharan and "
              "Tahir Andrabi."),
            T(["Category", "Examples"],
              [["Great buys", "Information on benefits, costs and quality of education; structured "
                "pedagogy; teaching by learning level instead of grade"],
               ["Good buys", "Parent-directed early stimulation (0-36 months); quality pre-primary "
                "(3-5); reducing travel time; merit scholarships for disadvantaged children; "
                "school-based deworming where worm load is high"],
               ["Promising, limited evidence", "Adaptive learning software where hardware exists; "
                "community-hired staff; mobile phones; safeguarding; socio-emotional skills; "
                "community school management; targeting girls"],
               ["Effective but relatively expensive", "Cash transfers (as a tool for learning); "
                "feeding in primary schools"],
               ["Bad buys", "Hardware alone; additional inputs alone, such as textbooks, more "
                "teachers, buildings, grants, salary and libraries"]]),
        ], compact=True),

        S("Teaching at the Right Level", "Grouping children by what they can do", [
            TERM("Teaching at the Right Level (TaRL)",
                 "Pratham's approach: assess each child with a simple reading and arithmetic test, "
                 "group children by level for part of the day regardless of grade, teach with "
                 "level-appropriate activities, and reassess regularly."),
            FL(["ASSESS: one-on-one basic test",
                "GROUP: by level, for part of the day",
                "TEACH: activities for that level",
                "REASSESS: move children up as they learn"]),
            B("Banerjee and colleagues (2017, Journal of Economic Perspectives 31(4)) describe a "
              "series of randomised trials in Indian schools that took the approach from a "
              "proof of concept to government scale. Some designs failed inside the regular "
              "school system, and those failures shaped the later versions; two versions "
              "eventually raised learning in government schools at scale.", sm=True),
            H("green", "GEEAP lists targeting instruction by learning level as a great buy, in or "
              "out of school."),
        ]),

        S("Remedial and computer-assisted learning", "Balsakhi: a tutor and a computer", [
            B("Banerjee, Cole, Duflo and Linden (2007, QJE 122(3)) ran two randomised experiments "
              "in urban Indian schools. One hired community tutors (balsakhis) to teach children "
              "who were behind; the other gave children time on mathematics software."),
            ST([C("0.28 SD", "remedial tutoring: rise in average test scores in treatment schools",
                  "green", "Banerjee, Cole, Duflo and Linden (2007)"),
                C("0.47 SD", "computer-assisted mathematics: rise in maths scores", "cyan",
                  "Banerjee, Cole, Duflo and Linden (2007)"),
                C("0.10 SD", "what remained for targeted children a year after the programmes "
                  "ended", "amber", "Banerjee, Cole, Duflo and Linden (2007)")], cols=3),
            TC([B("Both worked while running, and both benefited the weakest children most.",
                  sm=True)],
               [B("Fade-out is common. Programmes need to continue, or to change the regular "
                  "classroom, if the gains are to last.", sm=True)]),
        ]),

        S("Mindspark", "Adaptive software in urban India", [
            B("Muralidharan, Singh and Ganimian (2019, AER 109(4)) studied Mindspark, a "
              "personalised, technology-aided after-school programme in urban India. Middle-school "
              "students were offered free access by lottery. The software adapts each question to "
              "the level the child has actually reached, which may be several grades below the "
              "one she is enrolled in."),
            TC([ST([C("0.37 SD", "maths gain for lottery winners in 4.5 months", "green",
                      "Muralidharan, Singh and Ganimian (2019)"),
                    C("0.23 SD", "Hindi gain in the same period", "cyan",
                      "Muralidharan, Singh and Ganimian (2019)")], cols=1)],
               [B("With full attendance of 90 days the authors project gains of 0.6 SD in maths "
                  "and 0.39 SD in Hindi.", sm=True),
                B("Absolute gains were similar for all students, so relative gains were much "
                  "larger for academically weaker students.", sm=True),
                B("GEEAP rates adaptive software as promising where hardware already exists, and "
                  "hardware alone as a bad buy.", sm=True)], ratio="a23"),
        ]),

        S("Structured pedagogy", "Lesson plans, materials and coaching together", [
            B("GEEAP defines structured pedagogy as \"a package that includes structured lesson "
              "plans, learning materials, and ongoing teacher support\" and rates it a great buy. "
              "Each element alone does less: a textbook without a plan, or training without "
              "follow-up, rarely changes daily teaching."),
            TC([P("cyan", "NIPUN Bharat",
                  "India's National Mission on Foundational Literacy and Numeracy, launched in "
                  "2021, aimed for every child to read and do basic arithmetic by Grade 3, with "
                  "2026-27 as the target year; Ministry replies since December 2025 say the end "
                  "of Grade 2. It sets learning targets, designs materials and "
                  "funds teacher training.")],
               [P("green", "Vidya Pravesh",
                  "A three-month school preparation module proposed in NEP 2020 and launched in "
                  "2021. PRS reports 8.9 lakh schools implementing it as of December 2025 and 4.2 "
                  "crore children covered in 2024-25.")]),
            H("indigo", "Source: " + PRS + ". ASER 2024's rise in Std III reading and arithmetic "
              "is consistent with this focus, though a survey cannot attribute it to one "
              "programme."),
        ]),

        S("Early years", "Learning gaps open before school starts", [
            B("Article 45 now asks the state to provide early childhood care and education until "
              "age six. NEP 2020 brings ages 3 to 5 into the foundational stage. GEEAP rates "
              "parent-directed stimulation for children aged 0 to 36 months and quality pre-primary "
              "education for ages 3 to 5 as good buys."),
            TC([ST([C("83.4%", "of 4-year-olds in a pre-primary institution, 2024", "green", ASER),
                    C("16.7%", "of Std I children underage (5 or below), lowest ever", "cyan", ASER)],
                   cols=1)],
               [B("Anganwadi centres, run under the women and child development ministry, enrol "
                  "more than half of all 3 and 4 year olds (ASER 2024).", sm=True),
                B("PRS reports 52% of pre-primary teachers professionally unqualified in "
                  "2024-25. Expanding pre-school without trained teachers risks pushing formal "
                  "lessons onto four-year-olds.", sm=True),
                B("See " + L("child-development.html", "Child Development 101") + " for the "
                  "developmental science.", sm=True)], ratio="a23"),
        ]),

        S("Girls' education", "Bangladesh's stipend for girls in secondary school", [
            B("Bangladesh introduced the Female Secondary Stipend and Assistance Program (FSSAP) in "
              "1994. Girls in rural secondary schools received a stipend and tuition subsidy if "
              "they attended 75% of school days, scored at least 45% in class tests and stayed "
              "unmarried until completing secondary school."),
            ST([C("13% a year", "growth in girls' secondary enrolment after 1994, against 2.5% "
                  "for boys", "green", "ADB Development Asia policy brief on FSSAP"),
                C("+1 year", "rise in women's age at first marriage since the programme began",
                  "cyan", "ADB Development Asia policy brief on FSSAP"),
                C("3.14", "estimated benefit-cost ratio", "indigo",
                  "ADB Development Asia policy brief on FSSAP")], cols=3),
            H("amber", "Bangladesh now reports gender parity in primary and secondary education "
              "(Wikipedia, Education in Bangladesh). GEEAP lists targeting interventions towards "
              "girls as promising and merit scholarships for disadvantaged children as a good buy."),
        ]),

        S("From pilot to policy", "Questions to ask before scaling an intervention", [
            B("Most of the evidence in this section began as a pilot run by an NGO or researchers. "
              "Banerjee et al. (2017) show that results from small proof-of-concept studies may "
              "not hold when a government runs the programme. Muralidharan and Singh show a "
              "reform can be delivered on paper and change nothing."),
            T(["Question", "Why it matters"],
              [["Who delivered the pilot?", "NGO staff are selected and supervised differently "
                "from government teachers"],
               ["What did it cost per child per SD gained?", "Compare with the next best use of the "
                "same money"],
               ["Does it change incentives or only add tasks?", "Tasks without incentives become "
                "paperwork"],
               ["Did gains last after it stopped?", "Balsakhi gains fell from 0.28 to about 0.10 SD"],
               ["Has it worked in more than one place?", "GEEAP's great buys have"]]),
            H("cyan", "See " + L("cost-effectiveness.html", "Cost Effectiveness 101") + " and "
              + L("impact-eval.html", "Impact Evaluation 101") + " for the methods."),
        ], compact=True),

        # ===================== SECTION 10 =====================
        DIV("10", "Ten", "Neighbours and higher education"),

        S("Spending in South Asia", "India spends the most of its GDP among its large neighbours", [
            B("Government expenditure on education as a share of GDP from the World Bank's World "
              "Development Indicators, which draws on UNESCO Institute for Statistics data. The "
              "latest available year differs by country, so read small differences with care."),
            {"t": "chart", "canvas": "saSpend",
             "title": "Government expenditure on education, % of GDP (latest year)",
             "source": WDI,
             "type": "bar",
             "data": {"labels": ["India (2022)", "Nepal (2024)", "Bangladesh (2024)",
                                 "Pakistan (2023)", "Sri Lanka (2023)"],
                      "datasets": [{"label": "% of GDP", "data": [4.10, 3.69, 2.03, 1.95, 1.83],
                                    "backgroundColor": ["#0369A1", "#047857", "#B45309",
                                                        "#B91C1C", "#4F46E5"]}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:6, title:{display:true,text:'% of GDP'} } } }"}},
            H("amber", "Sri Lanka's share fell to 1.2% in 2022 during its economic crisis. Nepal's "
              "has fallen from 4.43% in 2021. Only India is above 4%, and none reaches the 6% "
              "that Indian policy has targeted since 1966."),
        ]),

        S("Comparison table", "Five South Asian systems on the same indicators", [
            B("The table uses one source for every cell so the definitions match. Years are the "
              "latest available in WDI as of October 2026. Learning poverty is the World Bank's "
              "measure combining children out of school with those in school who cannot read an "
              "age-appropriate text by age 10."),
            T(["Indicator", "India", "Bangladesh", "Pakistan", "Nepal", "Sri Lanka"],
              [["Education spend, % of govt expenditure", "14.2 (2022)", "11.9 (2025)",
                "9.8 (2023)", "10.8 (2025)", "7.2 (2024)"],
               ["Adult literacy, %", "78.2 (2024)", "79.0 (2022)", "58.9 (2021)", "68.7 (2019)",
                "92.7 (2024)"],
               ["Primary completion rate, %", "90.3 (2025)", "94.3 (2024)", "74.1 (2024)",
                "109.4 (2025)", "94.5 (2023)"],
               ["Tertiary GER, %", "34.4 (2025)", "23.7 (2024)", "10.9 (2024)", "21.3 (2024)",
                "20.7 (2023)"],
               ["Learning poverty, %", "56.1 (2017)", "51.2 (2022)", "79.5 (2019)", "n/a",
                "14.8 (2015)"]]),
            H("cyan", "Source: " + WDI + ". Primary completion above 100 reflects over-age "
              "completers. Learning poverty years differ widely; use it for orders of magnitude only."),
        ], compact=True),

        S("Pakistan", "A constitutional right and 26 million children out of school", [
            B("The Constitution (Eighteenth Amendment) Act 2010 inserted Article 25A into "
              "Pakistan's constitution: \"The State shall provide free and compulsory education to "
              "all children of the age of five to sixteen years in such manner as may be "
              "determined by law.\" The amendment received presidential assent on 19 April 2010, "
              "eighteen days after India's Article 21A came into force."),
            ST([C("26.2 million", "children out of school, 2021-22", "red",
                  "Pakistan Institute of Education, Pakistan Education Statistics 2021-22, via Geo "
                  "News, 21 January 2024"),
                C("39%", "of school-age children out of school (44% in 2016-17)", "amber",
                  "Pakistan Institute of Education, via Geo News"),
                C("65%", "of children out of school in Balochistan", "red",
                  "Pakistan Institute of Education, via Geo News"),
                C("1.95%", "of GDP on education, 2023", "indigo", WDI)], cols=4),
            H("cyan", "Pakistan's age band (5-16) is wider than India's (6-14), so its right "
              "covers secondary school. The share out of school fell while the number rose, "
              "because the school-age population grew faster."),
        ]),

        S("Bangladesh", "Gender parity on a small budget", [
            B("Article 17 of the Constitution of Bangladesh commits the state to free and "
              "compulsory education for all children. Bangladesh is the region's standard example "
              "of reaching girls: the 1994 secondary stipend described in Section 9 coincided with "
              "rapid gains in girls' enrolment, and the country now reports gender parity in "
              "primary and secondary education."),
            TC([ST([C("2.03%", "of GDP on education, 2024", "amber", WDI),
                    C("79.0%", "adult literacy, 2022", "cyan", WDI)], cols=1)],
               [B("Spending has stayed close to 2% of GDP. Since 2011 WDI records a low of 1.1% "
                  "(2019) and a high of 2.2% (2012).", sm=True),
                B("Bangladesh shows that targeted demand-side incentives can move enrolment "
                  "quickly even with a low budget. Learning is a separate question: WDI's "
                  "learning poverty estimate is 51.2% for 2022.", sm=True)], ratio="a23"),
            H("indigo", "Compare with Pakistan: similar spending as a share of GDP (1.95% in 2023), "
              "but primary completion of 74.1% against Bangladesh's 94.3% (WDI, 2024). The size of "
              "the budget does not settle results on its own."),
        ]),

        S("Nepal", "A federal constitution with education rights to secondary level", [
            B("Article 31 of the Constitution of Nepal 2015 goes further than India's Article 21A. "
              "Clause (2) gives every citizen \"the right to compulsory and free basic education, "
              "and free education up to the secondary level\". Clause (5) gives every Nepali "
              "community the right to education in its mother tongue up to the secondary level."),
            TC([P("cyan", "Mother tongue as a right",
                  "Clause (5) makes mother-tongue education to secondary level a community "
                  "right, with a right to open and run schools as provided by law. In India the "
                  "same idea sits in NEP 2020 as a policy preference \"wherever possible\".")],
               [P("amber", "The money",
                  "WDI shows education spending of 3.69% of GDP in 2024, down from 4.43% in 2021, "
                  "and 10.8% of government expenditure in 2025.")]),
            H("indigo", "Compare Nepal's secondary-level guarantee with NEP 2020's 100% GER target "
              "for secondary by 2030: Nepal wrote it as a right, India as a goal."),
        ]),

        S("Sri Lanka", "Free education since 1945, and a fiscal squeeze", [
            B("Sri Lanka introduced free education under C. W. W. Kannangara, the State Council's "
              "first Minister of Education. The reforms came into operation on 1 October 1945. Kannangara also built central schools in rural areas, "
              "from three in 1941 to 35 by 1945 and 50 by 1950. Undergraduate education at state "
              "universities remains tuition-free."),
            ST([C("92.7%", "adult literacy, 2024, the highest of the five countries here", "green", WDI),
                C("14.8%", "learning poverty, 2015", "cyan", WDI),
                C("1.83%", "of GDP on education, 2023 (1.2% in 2022)", "red", WDI)], cols=3),
            H("amber", "Sri Lanka shows that early universal provision can produce lasting gains "
              "in literacy. It also shows how a fiscal crisis squeezes education: 7.2% of "
              "government expenditure in 2024 (WDI). History: Wikipedia, C. W. W. Kannangara "
              "and Education in Sri Lanka."),
        ]),

        S("Higher education in India", "Four crore students, uneven across states", [
            B("Higher education in India is provided through institutions of national importance, "
              "central, state, private and deemed-to-be universities and their colleges. PRS "
              "reports 1,395 universities as of January 2026 and around four crore students "
              "enrolled."),
            ST([C("1,395", "universities, January 2026", "cyan", PRS + ", citing AISHE dashboard"),
                C("28%", "higher education GER, 2021-22", "amber", PRS + ", citing AISHE 2021-22"),
                C("50% by 2035", "NEP 2020 target GER", "green", NEP),
                C("Rs 55,727 cr", "Department of Higher Education, 2026-27 BE", "indigo", PRS)],
              cols=4),
            TC([B("State gaps are wide: GER of 47% in Tamil Nadu and 41% in Kerala against 17% in "
                  "Bihar, 19% in Jharkhand and 24% in Uttar Pradesh (AISHE 2021-22, via PRS).",
                  sm=True)],
               [B("WDI's tertiary GER for India is 34.4% for 2025, on UNESCO's definition, which "
                  "differs from AISHE's. Do not mix the two series.", sm=True)]),
        ]),

        S("One regulator", "From HECI to the Viksit Bharat Shiksha Adhishthan Bill", [
            B("NEP 2020 proposed a single Higher Education Commission of India (HECI) with four "
              "verticals: a regulatory council (NHERC), an accreditation council (NAC), a grants "
              "council (HEGC) and a General Education Council (GEC). The bill that followed took "
              "a different name and a slightly different shape."),
            TC([P("cyan", "The VBSA Bill 2025",
                  "Introduced in the Lok Sabha on 15 December 2025, it would create the Viksit "
                  "Bharat Shiksha Adhishthan as a single regulator for higher education, "
                  "replacing the UGC (set up under the UGC Act 1956), AICTE and NCTE, with "
                  "regulatory, standards and accreditation councils. Section 22 of the UGC Act "
                  "reserves degrees to universities set up by law, deemed universities and bodies "
                  "empowered by an Act of Parliament; the Bill would "
                  "let the Regulatory Council authorise others, with the Centre's approval. It "
                  "went to a Joint Parliamentary Committee on 16 December 2025.")],
               [P("amber", "Status, as of October 2026",
                  "The committee listed its draft report for adoption on 17 July 2026; ThePrint "
                  "(19 July 2026) reported that sitting called off. It was hearing experts again "
                  "on 25 August and 11 September 2026, and PRS records no report presented. The "
                  "Bill has not been passed.")]),
            H("indigo", "Sources: " + PRS + "; PRS bill and committee pages, accessed 6 October "
              "2026; UGC Act 1956, s22. Check for a later report or vote before citing the status."),
        ]),

        # ===================== SECTION 11 =====================
        DIV("11", "Eleven", "A practitioner's toolkit"),

        S("Diagnostic checklist", "Ten questions before you design an education programme", [
            B("Use these questions at the start of any programme design, district plan or funding "
              "proposal. Each one maps to a section of this course and to a data source you can "
              "open yourself."),
            TC([BL(["Are children enrolled? (UDISE+, ASER)",
                    "Are they attending on a typical day? (your own spot checks)",
                    "Can Grade 3 children read a Grade 2 text? (ASER-style test)",
                    "Which children are furthest behind, and who are they?",
                    "Are teachers present and teaching? (unannounced visits)"], color="cyan")],
               [BL(["How many posts are vacant, and in which schools?",
                    "Which scheme funds the activity, and is money released on time?",
                    "Does the school management committee meet and know the results?",
                    "Which state rules apply (detention, 12(1)(c), language)?",
                    "What will the programme cost per child, and per SD of learning?"],
                   color="green")]),
            H("amber", "If you can answer only the first question, you are designing an access "
              "programme. Most South Asian systems now need learning programmes."),
        ]),

        S("Decision table", "Match the problem to the evidence", [
            B("The table links common field diagnoses to responses with the strongest evidence in "
              "this course, and to the trap that most often undoes them."),
            T(["Diagnosis", "Response with evidence", "Watch out for"],
              [["Many children in Grades 3-5 cannot read", "Teaching at the Right Level; "
                "structured pedagogy", "Running it as a one-off camp with no follow-up"],
               ["High teacher absence", "Regular monitoring with consequences",
                "Monitoring that adds forms without anyone acting on them"],
               ["Parents cannot judge schools", "Simple learning report cards",
                "Narrow tests that invite teaching to the test"],
               ["Girls leave after Grade 8", "Conditional stipends; reducing travel time",
                "Conditions that exclude the poorest girls"],
               ["Low pre-school quality", "Trained staff and play-based materials",
                "Formal lessons pushed down to age four"],
               ["Unused 12(1)(c) seats", "Seat publication, help with forms, prompt "
                "reimbursement", "Online-only portals"]]),
        ], compact=True),

        S("Worked example", "Illustrative: planning a reading programme for one block", [
            B("Illustrative case (hypothetical figures). A block education officer has 120 government primary schools and "
              "about 6,000 children in Grades 3 to 5. A quick one-on-one test in a sample of "
              "schools suggests that roughly two-thirds cannot read a Grade 2 text. The officer "
              "has a modest budget from the state's foundational learning allocation."),
            FL(["TEST: every child in Grades 3-5, one-on-one",
                "GROUP: by level for one hour a day",
                "TRAIN: teachers in level-based activities",
                "RETEST: at 50 days and at year end"]),
            TC([P("cyan", "What to measure",
                  "Share of children reading a Grade 2 text, by school and by group, at baseline "
                  "and after each cycle. Teacher presence on unannounced visits.")],
               [P("amber", "What to cost",
                  "Training days, materials and supervision per child. Divide by the change in "
                  "the share reading to get a cost per additional reader.")]),
            H("indigo", "All numbers on this slide are illustrative. The design follows the TaRL "
              "evidence in Section 9."),
        ]),

        S("Choosing a data source", "Which dataset answers which question", [
            B("Practitioners lose time arguing over numbers that come from instruments built for "
              "different purposes. This table pairs common questions with the source designed to "
              "answer them."),
            T(["Question", "Best source", "Level available"],
              [["How many schools, teachers and students?", "UDISE+ (annual)",
                "School, block, district, state"],
               ["Can children read and do arithmetic?", "ASER (household, rural)",
                "District and state"],
               ["How do Grade 3, 6, 9 students score on the curriculum?",
                "PARAKH Rashtriya Sarvekshan", "District and state"],
               ["Why are adolescents out of school?", "PLFS and NSO education surveys",
                "State"],
               ["What does the Union spend, and is it used?", "Union budget, PRS analysis",
                "Scheme"],
               ["Higher education enrolment and institutions?", "AISHE", "State, institution"]]),
            H("cyan", "When sources disagree, check sample, year and method first. See "
              + L("data-lit.html", "Data Literacy 101") + " and " + L("survey-design.html",
                                                                     "Survey Design 101") + "."),
        ], compact=True),

        S("Working with government", "Where an NGO or researcher can plug in", [
            B("Most children are in government schools, so most lasting change runs through the "
              "state's own systems. Partnerships work best when they fit the calendar and the "
              "legal hooks the system already has."),
            TC([P("cyan", "System entry points",
                  "State annual work plans under Samagra Shiksha; district and block training "
                  "calendars; state assessment cells and SCERTs; school management committees "
                  "under RTE s21.")],
               [P("green", "Legal hooks",
                  "s12(1)(c) admissions and their portals; s17 on corporal punishment; s24 "
                  "teacher duties; the state's rules on examinations in classes 5 and 8.")]),
            B("Practical habits: share findings with the officials who supplied the data before "
              "publishing; present results by school and block, which is where decisions are "
              "made; and keep the intervention cheap enough that the state could run it without "
              "you.", sm=True),
            H("indigo", "See " + L("governance-accountability.html", "Governance &amp; "
              "Accountability 101") + " for the wider accountability tools."),
        ]),

        S("Children's data", "Collecting learning data lawfully under the DPDP Act", [
            B("Learning assessments collect personal data about children. The Digital Personal "
              "Data Protection Act 2023 and its 2025 Rules apply to it from 13 May 2027, when the duties, "
              "including section 9, commence (G.S.R. 843(E)). Section 2(f) defines a "
              "child as anyone who has not completed eighteen years."),
            TC([P("amber", "Section 9",
                  "Before processing a child's personal data, a data fiduciary must obtain "
                  "\"verifiable consent of the parent\" (s9(1)), and must not process data in a "
                  "way \"likely to cause any detrimental effect on the well-being of a child\" "
                  "(s9(2)).")],
               [P("green", "Section 17(2)(b)",
                  "The Act's provisions do not apply to processing \"necessary for research, "
                  "archiving or statistical purposes\" where the data are not used to take a "
                  "decision about an individual and processing follows prescribed standards. It applies "
                  "from 13 May 2027, with sections 9 and 11 to 17.")]),
            H("cyan", "A test used to place a child in a learning group is a decision about that "
              "child, so do not assume the research exemption covers programme data. See "
              + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101") + " and "
              + L("research-ethics.html", "Research Ethics 101") + "."),
        ]),

        # ===================== SECTION 12 =====================
        DIV("12", "Twelve", "Open debates and where next"),

        S("Open debates", "Six questions Indian education policy has not settled", [
            B("Each of these has evidence on more than one side, and each is decided state by state "
              "as much as nationally. A practitioner should know the arguments before taking a "
              "position."),
            T(["Debate", "One side", "The other side"],
              [["Detention in classes 5 and 8", "Exams restore effort and accountability",
                "Holding back without remediation pushes children out"],
               ["Mother-tongue instruction", "Children learn to read faster in a language they "
                "speak", "Parents want English for jobs and mobility"],
               ["School consolidation", "Larger schools get subject teachers",
                "Longer journeys keep the youngest and girls at home"],
               ["Private school growth", "Lower cost per child, similar results",
                "Stratification and weaker public school constituencies"],
               ["A single higher education regulator", "Less duplication, clearer rules",
                "Central power over state and autonomous institutions"],
               ["Contract teachers", "Faster hiring, local accountability",
                "Lower pay, weaker careers, legal challenges"]]),
        ], compact=True),

        S("What to watch", "Dates and decisions to watch after October 2026", [
            B("Education policy changes through survey releases, budgets, court orders and "
              "bills. These are the scheduled or pending events, as of October 2026, that are "
              "most likely to change the numbers and rules in this deck."),
            TC([BL(["<strong>ASER 2026</strong>: Pratham is preparing the next survey; ASER "
                    "2024 remains the latest report",
                    "<strong>UDISE+ 2026-27</strong>: the next annual school census",
                    "<strong>NIPUN Bharat</strong>: 2026-27 is the mission's target year for "
                    "foundational learning",
                    "<strong>Census 2027</strong>: reference date 1 March 2027, including caste "
                    "enumeration, will reset enrolment denominators"], color="cyan")],
               [BL(["<strong>Pramati reference</strong>: a larger bench on whether the RTE Act "
                    "applies to minority schools",
                    "<strong>Dinesh Biwaji Ashtikar</strong>: hearing on 27 October 2026 on 12(1)(c) rules",
                    "<strong>VBSA Bill</strong>: JPC report and any vote in Parliament",
                    "<strong>Union Budget 2027-28</strong>: the next test of the 6% target"],
                   color="amber")]),
            H("indigo", "Re-check each item before you cite it. Dates move, and court matters are "
              "often adjourned."),
        ]),

        S("Summary", "Eight ideas to take away", [
            TC([BL(["Enrolment is near universal for ages 6-14; learning is the binding constraint",
                    "Article 21A and the RTE Act made elementary education a justiciable right "
                    "from 1 April 2010",
                    "Education is on the Concurrent List, so states decide much of what NEP 2020 "
                    "becomes",
                    "The 6% of GDP target dates from 1966; spending was 4.1% in 2022-23"],
                   color="cyan")],
               [BL(["Teacher absence and vacancies cost more than most new schemes add",
                    "Private schools now teach 38% of students; selection explains much of their "
                    "raw advantage",
                    "Great buys: information, structured pedagogy, teaching at the right level",
                    "Pilots need to survive government delivery before they count as policy"],
                   color="green")]),
            Q("These severe shortfalls constitute a learning crisis.", WDR),
            B("The figures behind each idea, with sources, are in Sections 1 to 10. When you "
              "quote one, quote its year with it, because most of them will change within two "
              "years.", sm=True),
        ]),

        S("Where next", "Related ImpactMojo 101 decks", [
            B("Education policy connects to almost every other part of development practice. These "
              "decks go deeper on the methods, rights and systems this course touched."),
            TC([BL(["Learning in classrooms: " + L("fln.html", "Foundational Literacy &amp; "
                    "Numeracy 101") + ", " + L("edu-pedagogy.html", "Education &amp; Pedagogy 101"),
                    "Who gets left out: " + L("inclusive-education.html", "Inclusive Education 101")
                    + ", " + L("child-rights.html", "Child Rights 101") + ", "
                    + L("disability-inclusion.html", "Disability Inclusion 101"),
                    "Early years: " + L("child-development.html", "Child Development 101") + ", "
                    + L("sel-basics.html", "SEL Basics 101"),
                    "The state: " + L("public-policy-101.html", "Public Policy 101") + ", "
                    + L("public-finance-budgeting.html", "Public Finance &amp; Budgeting 101")
                    + ", " + L("ind-constitution.html", "Indian Constitution 101")])],
               [BL(["Evidence: " + L("impact-eval.html", "Impact Evaluation 101") + ", "
                    + L("causal-inference.html", "Causal Inference 101") + ", "
                    + L("cost-effectiveness.html", "Cost Effectiveness 101"),
                    "Measurement: " + L("irt-basics.html", "Item Response Theory 101") + ", "
                    + L("survey-design.html", "Survey Design 101") + ", "
                    + L("data-lit.html", "Data Literacy 101"),
                    "Equity: " + L("gender-dev.html", "Gender &amp; Development 101") + ", "
                    + L("caste-studies.html", "Caste Studies 101") + ", "
                    + L("inequality-basics.html", "Inequality Basics 101"),
                    "Systems: " + L("governance-accountability.html", "Governance &amp; "
                    "Accountability 101") + ", " + L("dev-economics.html",
                                                     "Development Economics 101")])]),
            H("cyan", "Item Response Theory 101 explains how assessments such as PARAKH put "
              "different test booklets on one scale."),
        ]),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Education Policy 101 &middot; Complete",
         "headline": "Count the children,<br>then count what they learn",
         "byline": "Enrolment was the twentieth-century problem. Learning, teachers and money spent "
                   "well are this century's. Read the law, open the data, test before you scale, "
                   "and keep asking which child is furthest behind. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

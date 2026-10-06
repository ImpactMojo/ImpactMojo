# -*- coding: utf-8 -*-
"""
Aid & Philanthropy 101: ImpactMojo 101 Series (native deck spec)
Official aid, the 2025 cuts, aid to and from South Asia, and Indian philanthropy law,
for development practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py aid_philanthropy

Sources opened while writing (October 2026):
- OECD, press release, International aid fell sharply in 2025, 9 April 2026:
  https://www.oecd.org/en/about/news/press-releases/2026/04/international-aid-fell-sharply-in-2025-says-oecd.html
- OECD, ODA trends and statistics (LDCs, sub-Saharan Africa, humanitarian, gender finance):
  https://www.oecd.org/en/topics/sub-issues/oda-trends-and-statistics.html
- OECD, Glossary of statistical terms and concepts of development finance (ODA, tied aid):
  https://www.oecd.org/en/topics/sub-issues/oda-standards/glossary-of-statistical-terms-and-concepts-of-development-finance.html
- Wikipedia, Official development assistance (1969 adoption; UNGA 2626 (XXV), 24 October 1970;
  grant equivalent agreed 2014 and implemented 2019; OOF; SDG 17.2): https://en.wikipedia.org/wiki/Official_development_assistance
- World Bank, World Development Indicators API, DT.ODA.ODAT.CD, DT.ODA.ODAT.GN.ZS, DT.ODA.ODAT.PC.ZS
  (last updated 13 July 2026): https://api.worldbank.org/v2/country/IND;BGD;NPL;PAK;LKA;AFG/indicator/DT.ODA.ODAT.CD
- Wikipedia, high level forums on aid effectiveness (Rome, Paris, Accra, Busan):
  https://en.wikipedia.org/wiki/Paris_Declaration_on_Aid_Effectiveness
- OECD, Aid Effectiveness 2011: Progress in Implementing the Paris Declaration (2012), Figure 1.2 and Table 1.1:
  https://www.oecd.org/content/dam/oecd/en/publications/reports/2012/03/aid-effectiveness-2011_g1g1530a/9789264125780-en.pdf
- OECD, 2026 Development Co-operation Profiles, methodological notes (loan grant-element thresholds since 2018):
  https://www.oecd.org/content/dam/oecd/en/topics/policy-issues/development-co-operation/development-co-operation-profiles/development-co-operation-profiles-methodology.pdf
- State Department, On Delivering an America First Foreign Assistance Program, 28 March 2025:
  https://www.state.gov/on-delivering-an-america-first-foreign-assistance-program
- IASC, About the Grand Bargain: https://interagencystandingcommittee.org/about-the-grand-bargain
- Grand Bargain document, May 2016 (commitment 2.4):
  https://interagencystandingcommittee.org/system/files/grand_bargain_final_22_may_final-2_0.pdf
- COSV, The Paris Declaration on Aid Effectiveness and the Accra Agenda for Action: https://www.cosv.org/?p=1407
- European Commission (capacity4dev), The Busan Commitments: An Analysis of EU Progress and Performance:
  https://capacity4dev.europa.eu/media/22792/download/66e8d5fc-bae3-4a75-a319-026012e9b403_en
- Wikipedia, The End of Poverty (Sachs 2005): https://en.wikipedia.org/wiki/The_End_of_Poverty
- Wikipedia, The White Man's Burden (Easterly 2006): https://en.wikipedia.org/wiki/The_White_Man%27s_Burden_(book)
- Wikipedia, Dambisa Moyo (Dead Aid 2009): https://en.wikipedia.org/wiki/Dambisa_Moyo
- Burnside and Dollar (2000), AER 90(4): 847-868: https://ideas.repec.org/a/aea/aecrev/v90y2000i4p847-868.html
- Easterly, Levine and Roodman (2004), AER 94(3): 774-780: https://ideas.repec.org/a/aea/aecrev/v94y2004i3p774-780.html
- Rajan and Subramanian (2008), REStat 90(4): 643-665: https://ideas.repec.org/a/tpr/restat/v90y2008i4p643-665.html
- Wikipedia, Famine, Affluence, and Morality (Singer 1972): https://en.wikipedia.org/wiki/Famine,_Affluence,_and_Morality
- Executive Order 14169, Reevaluating and Realigning United States Foreign Aid, signed 20 January 2025, s3(a):
  https://www.govinfo.gov/content/pkg/FR-2025-01-30/html/2025-02091.htm
- Wikipedia, United States Agency for International Development (83% of programmes, 5,200 contracts, 10 March 2025;
  notice to Congress 28 March 2025; operations ceased 1 July 2025): https://en.wikipedia.org/wiki/United_States_Agency_for_International_Development
- Anadolu Agency, 1 July 2025: https://aa.com.tr/en/americas/us-ends-usaid-aid-to-be-distributed-via-state-department-marco-rubio/3618849
- Civil Service World, 25 February 2025 (UK ODA from 0.5% to 0.3% of GNI):
  https://www.civilserviceworld.com/news/article/government-to-slash-aid-to-fund-defence-boost
- Full Fact, government tracker on 2.5% defence spending: https://fullfact.org/government-tracker/defence-spending-2-5-percent-2027/
- Cavalcanti et al. (2025), The Lancet 406(10500): 283-294 (PubMed 40609560): https://pubmed.ncbi.nlm.nih.gov/40609560/
- Wikipedia, Indian Technical and Economic Cooperation Programme: https://en.wikipedia.org/wiki/Indian_Technical_and_Economic_Cooperation_Programme
- MEA, Lines of Credit for Development Projects (as on August 2024): https://www.mea.gov.in/Lines-of-Credit-for-Development-Projects.htm
- Exim Bank of India, Lines of Credit (IDEAS): https://www.eximbankindia.in/lines-of-credit
- Companies Act 2013, s135 and CSR Policy Rules 2014 (ca2013.com): https://ca2013.com/135-corporate-social-responsibility/
- Companies Act 2013, Schedule VII: https://ca2013.com/schedule/schedule7-3/
- Ministry of Corporate Affairs CSR expenditure by State/UT and by sector, 2018-19 to 2022-23, via data.gov.in
  (resources 80f3abf8-7c91-4966-a37f-8c7b0aae92e9 and 40ca3289-b33c-4f60-b8fe-c5050d8e27fa; snapshot in data/csr-india.json)
- PRS, FCRA Amendment Bill 2020 summary: https://prsindia.org/billtrack/the-foreign-contribution-regulation-amendment-bill-2020
- FCRA Amendment Act 2020 (No. 33 of 2020), Gazette of 28 September 2020:
  https://prsindia.org/files/bills_acts/acts_parliament/2020/Foreign%20Contribution%20(Regulation)%20Amendment%20Act,%202020.pdf
- SCC Times, 23 September 2020 (objects and reasons: 19,000+ registrations cancelled 2011-2019):
  https://www.scconline.com/blog/?p=236145
- Supreme Court Observer, Noel Harper v Union of India, WP (C) 566/2021, judgment 8 April 2022:
  https://www.scobserver.in/cases/noel-harper-union-of-india-fcra-amendment-foreign-contribution-regulation-case-background/
- Income Tax Department, Income-tax Act 2025, section 133: https://www.incometaxindia.gov.in/w/section-133-94
- Bain & Company and Dasra, India Philanthropy Report 2025 (27 February 2025) and 2026 (26 February 2026):
  https://www.bain.com/insights/india-philanthropy-report-2025/ and https://www.bain.com/insights/india-philanthropy-report-2026/
- Wikipedia, Effective altruism: https://en.wikipedia.org/wiki/Effective_altruism
- Wikipedia, GiveWell: https://en.wikipedia.org/wiki/GiveWell
- GiveWell, Our Top Charities (last updated September 2025): https://www.givewell.org/charities/top-charities
- Trust-Based Philanthropy Project, Six practices: https://www.trustbasedphilanthropy.org/practices
- Wikipedia, Trust-based philanthropy: https://en.wikipedia.org/wiki/Trust-based_philanthropy
- Wikipedia, Grand Bargain (humanitarian reform): https://en.wikipedia.org/wiki/Grand_Bargain_(humanitarian_reform)
- Development Initiatives, Global Humanitarian Assistance Report 2026, chapter 3, via ALNAP:
  https://alnap.org/help-library/resources/global-humanitarian-assistance-gha-report-2026/humanitarian-reform-and-delivery/
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


def BAR(canvas, title, source, labels, label, data, color="#0EA5E9", horizontal=False, ytitle=""):
    opts = "{ plugins:{legend:{display:false}}"
    if horizontal:
        opts += ", indexAxis:'y'"
    if ytitle:
        axis = "x" if horizontal else "y"
        opts += ", scales:{ " + axis + ":{ title:{display:true,text:'" + ytitle + "'} } }"
    opts += " }"
    return {"t": "chart", "canvas": canvas, "title": title, "source": source, "type": "bar",
            "data": {"labels": labels,
                     "datasets": [{"label": label, "data": data, "backgroundColor": color}]},
            "options": {"__js__": opts}}


OECD = "OECD, preliminary 2025 ODA data, press release of 9 April 2026"
OECDT = "OECD, ODA trends and statistics page, accessed October 2026"
WDI = "World Bank, World Development Indicators (net ODA received), updated 13 July 2026"
MCA = "Ministry of Corporate Affairs CSR data via data.gov.in, 2018-19 to 2022-23"
IPR25 = "Bain &amp; Company and Dasra, India Philanthropy Report 2025"
IPR26 = "Bain &amp; Company and Dasra, India Philanthropy Report 2026"
GW = "GiveWell, Our Top Charities, last updated September 2025"
GHA = "Development Initiatives, Global Humanitarian Assistance Report 2026"
MEA = "Ministry of External Affairs, Lines of Credit for Development Projects, as on August 2024"
FCRA = "Foreign Contribution (Regulation) Act 2010"
FCRA20 = "FCRA (Amendment) Act 2020 (No. 33 of 2020)"
CA = "Companies Act 2013"
ITA = "Income-tax Act 2025"

SEC1 = [
    DIV("01", "One", "What counts as aid"),

    S("Starting point", "Why a practitioner needs to understand where the money comes from", [
        B("Most development work in South Asia runs on someone else's money. A district nutrition "
          "project may be paid for by a state budget, a World Bank loan, a European bilateral grant, "
          "a company's CSR obligation and a family foundation, all at once. Each source arrives with "
          "its own rules, timelines, reporting formats and ideas about what success looks like. The "
          "people who design and run the work spend a large share of their time translating between "
          "these rules."),
        TC([P("cyan", "Official aid",
              "Money from governments and the bodies they own, such as the World Bank, UNICEF and "
              "bilateral agencies. Counted and reported to the OECD when it meets the definition of "
              "official development assistance (ODA).")],
           [P("green", "Private philanthropy",
              "Money from individuals, families, foundations and companies. In India this includes "
              "corporate social responsibility (CSR) spending required by the Companies Act 2013, and "
              "foreign donations regulated by the FCRA 2010.")]),
        H("indigo", "This course follows both streams: how they are defined, how they changed in "
          "2025, what the law in India says about each, and how to judge a funding offer."),
    ]),

    S("Definition", "Official development assistance: the OECD definition", [
        B("The OECD's Development Assistance Committee (DAC) adopted the concept of official "
          "development assistance in 1969, and it remains the standard measure of aid. The OECD "
          "glossary sets out three tests. A flow to a country on the DAC List of ODA Recipients, or to "
          "a multilateral agency, counts as ODA only if all three hold."),
        TERM("Official development assistance (ODA)",
             "Government aid that promotes and specifically targets the economic development and "
             "welfare of developing countries (OECD glossary). The flow must be undertaken by the "
             "official sector, have the promotion of economic development and welfare as its main "
             "objective, and be on concessional financial terms."),
        TC([BL(["<strong>Official:</strong> from governments or their agencies, so a private "
                "foundation grant is excluded however large.",
                "<strong>Developmental:</strong> economic development and welfare must be the main "
                "objective."])],
           [BL(["<strong>Concessional:</strong> cheaper than a market loan, or a grant.",
                "<strong>To eligible recipients:</strong> countries on the DAC list, or multilateral "
                "agencies working for them."])]),
        H("cyan", "Source: OECD, Glossary of statistical terms and concepts of development finance, "
          "accessed October 2026."),
    ]),

    S("Boundaries", "What counts as ODA, and what is counted elsewhere", [
        B("The boundary matters because governments are judged by their ODA totals. Anything inside "
          "the line raises a donor's score, so donors argue about where the line sits. Two flows sit "
          "just outside it. Military assistance is classified as other official flows (OOF) because "
          "its main aim is not development. Official loans that are not concessional enough are also "
          "OOF: since 2018 flows, a loan counts as ODA only with a grant element of at least 45 per "
          "cent for least developed and other low-income countries, 15 per cent for lower "
          "middle-income and 10 per cent for upper middle-income countries (a single 25 per cent "
          "threshold applied until 2017)."),
        T(["Flow", "Counted as ODA?", "Why"],
          [["Grant to a ministry of health in Nepal", "Yes", "Official, developmental, concessional"],
           ["Concessional loan to Bangladesh for a power line", "Yes, at its grant equivalent", "Concessional terms"],
           ["Core contribution to UNICEF or IDA", "Yes", "Multilateral agency on the DAC list"],
           ["Costs of hosting refugees in the donor country", "Yes, within DAC limits", "Counted, and contested"],
           ["Military equipment or training", "No, classed as OOF", "Main aim is not development"],
           ["Near-market loan, below the grant-element threshold", "No, classed as OOF", "Not concessional enough"],
           ["Grant from a family foundation", "No", "Not official"]]),
        H("amber", "Sources: OECD glossary; OECD, 2026 Development Co-operation Profiles, methodological "
          "notes (loan thresholds); Wikipedia, Official development assistance (OOF definition "
          "and treatment of military aid). Refugee costs within donor countries appear in OECD's own "
          "ODA statistics, which is why critics call the total inflated."),
    ], compact=True),

    S("Measurement", "The grant-equivalent measure: counting a loan by its generosity", [
        B("Until 2018, a loan was counted in full in the year it was disbursed, and repayments were "
          "subtracted as negative aid when they came back. A donor lending at near-market rates could "
          "report the same ODA as one giving a grant. In 2014 the DAC agreed to count only the "
          "<strong>grant equivalent</strong> of a loan, an estimate of how much cheaper it is than a "
          "market loan, recorded when the loan is agreed. It was first applied to headline reporting "
          "in 2019."),
        TC([TERM("Grant equivalent",
                 "The value of a loan's concessionality: the face value minus the present value of the "
                 "repayments, discounted at a reference rate. A grant's grant equivalent is its full value.")],
           [BL(["<strong>Illustrative:</strong> a US$100 million grant counts as US$100 million.",
                "<strong>Illustrative:</strong> a US$100 million loan with a 40 per cent grant element "
                "counts as US$40 million in the year it is signed.",
                "Repayments no longer reduce ODA in later years."])]),
        H("indigo", "Source: Wikipedia, Official development assistance, which records the 2014 "
          "decision and its implementation in 2019. Debt relief rules were settled only in 2020."),
    ]),

    S("The target", "The 0.7 per cent target: a promise made in 1970", [
        B("On 24 October 1970 the UN General Assembly adopted resolution 2626 (XXV), the strategy for "
          "the Second Development Decade. It asked each economically advanced country to reach a "
          "minimum net amount of 0.7 per cent of its gross national product as ODA by the middle of "
          "the decade. Sweden and the Netherlands became the first to meet it, in 1974. Most donors "
          "have never met it in any year."),
        TC([ST([C("1970", "UN General Assembly adopts the 0.7% goal (A/RES/2626 (XXV))", "cyan",
                  "Wikipedia, Official development assistance"),
                C("1974", "First year any donor met it: Sweden and the Netherlands", "green",
                  "Wikipedia, Official development assistance")], cols=2)],
           [BL(["The measure is now ODA as a share of gross national income (GNI).",
                "SDG target 17.2 restates 0.7 per cent and adds 0.15 to 0.20 per cent of GNI for the "
                "least developed countries.",
                "The figure was a political compromise; it carries no estimate of need."])]),
        H("amber", "When a government announces a cut \"to 0.5 per cent\" or \"to 0.3 per cent\", "
          "it is measuring itself against this 1970 benchmark."),
    ]),

    S("Who meets it", "Only four donors met 0.7 per cent in 2025", [
        B("The OECD's preliminary data for 2025 show that four of the 34 DAC members exceeded the UN "
          "target. All four are small, rich Northern European countries with long cross-party "
          "agreement on aid. The DAC as a whole gave 0.26 per cent of combined GNI, down from 0.34 "
          "per cent in 2024, which is little more than a third of the target."),
        TC([BAR("apGni25", "ODA as % of GNI, 2025 (preliminary)", OECD,
                ["Norway", "Luxembourg", "Sweden", "Denmark", "All DAC"], "% of GNI",
                [1.03, 0.99, 0.85, 0.72, 0.26], "#10B981", ytitle="% of GNI")],
           [B("A share of GNI measures effort relative to a country's income. It rewards small "
              "economies that give generously and penalises large ones that give large sums in "
              "absolute terms but little relative to income.", sm=True),
            H("cyan", "Norway 1.03%, Luxembourg 0.99%, Sweden 0.85%, Denmark 0.72%. Source: "
              "OECD, 9 April 2026.")], ratio="a32"),
    ]),

    S("Who gives most", "The five largest providers in 2025, by volume", [
        B("Volume tells a different story from effort. In 2025 Germany became the largest provider of "
          "ODA for the first time, just ahead of the United States, whose ODA fell by 56.9 per cent. "
          "All five of the largest providers reduced their aid, which had never happened before, and "
          "together they accounted for 95.7 per cent of the total decline. Eight of the 34 DAC "
          "members held or increased their ODA."),
        TC([T(["Provider", "ODA 2025 (US$ bn)"],
              [["Germany", "29.1"], ["United States", "29.0"], ["United Kingdom", "17.2"],
               ["Japan", "16.2"], ["France", "14.5"], ["All DAC members and associates", "174.3"]])],
           [ST([C("US$174.3 bn", "total DAC ODA in 2025, 0.26% of GNI", "red", OECD),
                C("US$215.1 bn", "total DAC ODA in 2024, 0.34% of GNI", "cyan", OECD)], cols=1)]),
        H("indigo", "Figures are preliminary. The OECD publishes final 2025 data in December 2026."),
    ]),

    S("Reading aid numbers", "Four questions to ask of any aid statistic", [
        B("Aid figures are easy to quote and easy to misread. A headline about \"record aid\" or "
          "\"historic cuts\" can rest on a change of definition, a single large recipient or a "
          "currency movement. Before you use a number in a proposal or a policy brief, check four "
          "things."),
        TC([BL(["<strong>Gross or net?</strong> Net ODA received subtracts loan repayments, so it "
                "can fall even when new lending rises.",
                "<strong>Current or constant prices?</strong> The OECD reports the 23.1 per cent fall "
                "in real terms, after inflation and exchange rates."])],
           [BL(["<strong>Flows or grant equivalent?</strong> Donor totals since 2018 use grant "
                "equivalents; recipient data in the World Bank tables are net flows.",
                "<strong>Preliminary or final?</strong> Preliminary figures are revised, sometimes "
                "by billions."])]),
        H("green", "Write the definition next to the number. \"Net ODA received, current US$, World "
          "Bank WDI 2023\" is a citation. \"Aid to India\" is not."),
    ]),
]

SEC2 = [
    DIV("02", "Two", "How aid moves"),

    S("Channels", "Bilateral and multilateral aid", [
        B("A donor government can spend its aid budget directly or pass it through an international "
          "organisation. The choice changes who decides where the money goes. In April 2026 the OECD "
          "noted that in recent years members have increasingly relied on the multilateral system to support the least "
          "developed countries and offset cuts to bilateral aid."),
        TC([P("cyan", "Bilateral",
              "Government to government, or donor agency to NGO. The donor chooses country, sector "
              "and partner. Examples: Germany's GIZ and KfW, Japan's JICA, the UK's Foreign, "
              "Commonwealth and Development Office (FCDO). Bilateral aid often follows trade, "
              "security and historical ties.")],
           [P("indigo", "Multilateral",
              "Core contributions to bodies such as the World Bank's IDA, the Asian Development "
              "Bank, UNICEF or the Global Fund. The board of the organisation decides allocation, "
              "usually by formula and need. Donors give up control and gain scale.")]),
        H("green", "In practice many donors also give \"multi-bi\" aid: money passed through a UN "
          "agency but earmarked for a country or theme, which keeps bilateral control inside a "
          "multilateral channel."),
    ]),

    S("Two purposes", "Development aid and humanitarian aid", [
        B("Humanitarian aid responds to emergencies: floods, earthquakes, conflict and displacement. "
          "It aims to save lives within weeks and months. Development aid aims at change over years: "
          "schools, health systems, roads, institutions. The two run on different rules, staff and "
          "budgets, and the gap between them is a familiar problem after a disaster ends."),
        TC([P("red", "Humanitarian",
              "Short cycles, speed over process, often delivered by UN agencies and international "
              "NGOs. Humanitarian ODA fell by 35.8 per cent in 2025, its second year of decline "
              "(OECD, 9 April 2026).")],
           [P("green", "Development",
              "Longer cycles, aligned in principle with national plans, more often through "
              "governments and multilateral banks. Bilateral ODA for core development programming "
              "fell by 26.3 per cent in 2025, the largest drop on record (OECD).")]),
        H("indigo", "The humanitarian-development nexus is the attempt to join the two, so that relief "
          "builds toward recovery. Section 10 returns to humanitarian funding and the Grand Bargain."),
    ]),

    S("Instruments", "The forms aid takes", [
        B("The same rupee of aid can arrive in very different shapes. The form decides who controls "
          "the money, what reporting follows it and how easily it can be withdrawn. Practitioners in "
          "national NGOs mostly meet project grants; ministry officials more often meet loans, "
          "budget support and technical assistance."),
        T(["Form", "What it is", "Who controls spending"],
          [["Project aid", "Funds a defined project with its own budget and log frame", "Donor and implementer"],
           ["Budget support", "Money paid into the recipient government's budget", "Recipient government"],
           ["Technical cooperation", "Experts, training and studies, often paid to donor-country firms", "Donor"],
           ["Concessional loan", "Below-market loan, repaid over decades", "Recipient, within loan terms"],
           ["Debt relief", "Cancelling or rescheduling official debt", "Recipient, indirectly"],
           ["Humanitarian assistance", "Food, shelter, cash and health care in emergencies", "Agencies on the ground"],
           ["In-kind aid", "Goods such as food or medicines", "Donor, through supply chains"]]),
        H("cyan", "Budget support gives most control to the recipient and the least visibility to the "
          "donor's taxpayers. That trade-off explains why donors often prefer project aid."),
    ], compact=True),

    S("Tied aid", "Tied aid: when the grant must be spent at home", [
        B("Tied aid is a grant or loan that must be spent on goods or services from the donor country, "
          "or from a small group of countries. It turns part of an aid budget into an export subsidy. "
          "The recipient pays more for the same equipment or consultancy and has less choice. Untying "
          "aid was one of the Paris Declaration commitments in 2005."),
        TC([TERM("Tied aid (OECD glossary)",
                 "Official grants or loans where procurement of the goods or services involved is "
                 "limited to the donor country or to a group of countries which does not include "
                 "substantially all aid recipient countries.")],
           [BL(["Raises costs: the recipient cannot buy from the cheapest supplier.",
                "Shifts benefits: part of the aid returns as donor-country orders and fees.",
                "Shapes design: projects tilt toward what the donor sells.",
                "Persists: the Paris target was more than 89 per cent untied; the share fell from 89 "
                "per cent in 2005 to 86 per cent in 2009 (OECD 2011 survey)."])]),
        H("amber", "Ask of any offer: must we buy from your suppliers or hire your consultants? The "
          "answer changes the real value of the grant."),
    ]),

    S("The aid chain", "Every layer between donor and community takes a share", [
        B("Aid rarely travels straight from a donor to the people it is meant for. It passes through "
          "agencies, pooled funds, international NGOs and national partners. Each layer adds "
          "management, compliance and overhead, and each one holds some power over the next. The "
          "Global Humanitarian Assistance Report 2026 found that two thirds of humanitarian funding, "
          "US$17.4 billion, could not be tracked beyond the first recipient."),
        FL(["DONOR TREASURY: budget vote",
            "DONOR AGENCY: country strategy",
            "UN AGENCY OR INGO: first-tier recipient",
            "NATIONAL NGO: second tier",
            "COMMUNITY GROUP: delivery"]),
        TC([B("<strong>Why it matters:</strong> a community organisation in Sylhet or Satkhira may "
              "receive a small fraction of the original grant, on the shortest contract, with the "
              "heaviest reporting.", sm=True)],
           [B("<strong>Transparency gap:</strong> when funds cannot be traced past the first tier, "
              "no one can show how much reaches local actors. Source: " + GHA + ".", sm=True)]),
    ]),

    S("Beyond ODA", "ODA is one flow among several", [
        B("For most South Asian economies, ODA is now a small share of external finance. Remittances "
          "from workers abroad, foreign direct investment, commercial borrowing and loans from "
          "non-DAC lenders are each larger in many years. Private philanthropy is separate again. "
          "The categories have different owners and different rules, so they cannot simply be added "
          "together as \"aid\"."),
        T(["Flow", "Official?", "Concessional?", "Counted as ODA?"],
          [["ODA grants and soft loans", "Yes", "Yes", "Yes"],
           ["Other official flows (OOF)", "Yes", "No, or below the threshold", "No"],
           ["Loans from non-DAC lenders", "Yes", "Varies", "Only if reported and eligible"],
           ["South-South cooperation (for example India's ITEC)", "Yes", "Often", "No, India is not a DAC member"],
           ["Remittances", "No", "Not applicable", "No"],
           ["Foreign direct investment", "No", "No", "No"],
           ["Private philanthropy and CSR", "No", "Grants", "No"]]),
        H("indigo", "Section 7 looks at India as a provider of South-South cooperation, which sits "
          "outside the ODA statistics."),
    ], compact=True),

    S("Allocation", "Aid follows donor priorities: the case of Ukraine in 2025", [
        B("Where aid goes is a political decision. In 2025, ODA to Ukraine including outflows from "
          "European Union institutions rose 18.7 per cent to US$44.9 billion, the largest volume of "
          "ODA ever provided to a single country. The OECD noted that this exceeded total bilateral "
          "ODA from DAC members to all least developed countries, or to all of sub-Saharan Africa, "
          "combined."),
        TC([ST([C("US$44.9 bn", "ODA to Ukraine in 2025, including EU institutions", "indigo", OECD),
                C("&minus;25.8%", "change in DAC ODA to least developed countries, 2025", "red", OECDT)],
               cols=1)],
           [BL(["Security and proximity shape allocation as much as poverty does.",
                "Bilateral ODA to Ukraine alone fell 38.2 per cent to US$10.3 billion; EU institutions "
                "made up the difference.",
                "In-donor refugee costs fell 22.1 per cent, another sign of shifting priorities.",
                "For South Asia, competing priorities mean less room in shrinking budgets."])]),
        H("amber", "When you read a donor's country strategy, ask what else is competing for the "
          "same budget line this year."),
    ]),
]

SEC3 = [
    DIV("03", "Three", "The great aid debate"),

    S("Three questions", "Does aid work: three different questions", [
        B("The argument over aid is often confused because people answer different questions. One "
          "economist asks whether aid raises national growth rates. Another asks whether a bed net "
          "programme saves lives. A political scientist asks whether aid changes how governments "
          "behave toward their citizens. A programme can succeed on the second question while the "
          "first remains unanswered."),
        TC([BL(["<strong>Macro:</strong> does aid raise growth across countries? Studied with "
                "cross-country regressions.",
                "<strong>Micro:</strong> does this intervention change outcomes? Studied with "
                "evaluations, including randomised trials."])],
           [BL(["<strong>Political economy:</strong> does aid strengthen or weaken accountability "
                "between a state and its citizens?",
                "<strong>Ethical:</strong> do rich people and rich states have a duty to give, "
                "whatever the growth effect?"])]),
        H("cyan", "Keep the four apart when you read Sachs, Easterly and Moyo below. Each moves "
          "between them."),
    ]),

    S("The big push", "Jeffrey Sachs, The End of Poverty (2005)", [
        B("Jeffrey Sachs argued that extreme poverty, then defined by the World Bank as income below "
          "one dollar a day, could be eliminated by 2025 through carefully planned aid. Very poor "
          "countries are stuck below the \"bottom rung\" of the development ladder; a large, "
          "coordinated injection of investment would let them climb. He called for global aid to rise "
          "from US$65 billion in 2002 to between US$135 and US$195 billion a year by 2015, and "
          "endorsed the 0.7 per cent target as enough to do it."),
        TC([P("green", "Clinical economics",
              "Sachs compared countries to patients: each needs a differential diagnosis of its "
              "particular constraints, from disease to geography to debt, before a prescription.")],
           [P("cyan", "South Asia in the book",
              "The book discusses India and Bangladesh as examples of different stages of "
              "development, beside Malawi and China. Sachs headed the UN Millennium Project from "
              "2002 to 2005.")]),
        H("indigo", "Source: Wikipedia, The End of Poverty, summarising Sachs (2005), Penguin Press."),
    ]),

    S("Planners and searchers", "William Easterly, The White Man's Burden (2006)", [
        B("William Easterly, a former World Bank research economist, wrote partly in reply to Sachs. "
          "He described a second tragedy beside poverty itself: after roughly fifty years and about "
          "US$2.3 trillion in Western aid, there was comparatively little to show, even as cheap "
          "medicines and bed nets failed to reach people. His central device is a contrast between "
          "two kinds of actor."),
        T(["", "Planners", "Searchers"],
          [["Goals", "Large, set from outside (end world poverty)", "Small, found by asking what is in demand"],
           ["Knowledge", "Assume the answer is known", "Test, learn and adapt"],
           ["Feedback", "Little from the intended beneficiaries", "Constant, from users"],
           ["Accountability", "Diffuse; no one answers for failure", "Clear; failure is punished"]]),
        H("amber", "Easterly accepted that some aid works, citing vaccination and other targeted "
          "health programmes with measurable results as successes. Source: Wikipedia, The White "
          "Man's Burden (book)."),
    ]),

    S("Dead aid", "Dambisa Moyo, Dead Aid (2009)", [
        B("Dambisa Moyo, a Zambian-born economist, argued that government-to-government aid had harmed "
          "Africa and should be phased out. She separated humanitarian relief from official "
          "development assistance, which she said perpetuated the cycle of poverty and held back "
          "growth. In its place she offered proposals for African governments to finance development "
          "without relying on aid."),
        TC([P("red", "The argument",
              "Aid that flows to governments regardless of performance reduces their need to tax and "
              "answer to citizens. It encourages corruption and dependency, and crowds out other "
              "sources of finance.")],
           [P("amber", "The criticism",
              "Reviewers, including in the IMF's Finance &amp; Development and in Prospect, faulted its "
              "use of evidence and its oversimplification, and noted that Peter Bauer and William "
              "Easterly had made similar points earlier, with more nuance.")]),
        H("indigo", "Source: Wikipedia, Dambisa Moyo, which summarises the book and its reviews."),
    ]),

    S("Side by side", "Three authors, three diagnoses", [
        B("The three books are often taught as a set. They agree that poverty is urgent and that much "
          "aid has been wasted. They disagree about why, and so about what to do. The table sets their "
          "positions next to each other so you can see where the real disagreement lies."),
        T(["", "Sachs (2005)", "Easterly (2006)", "Moyo (2009)"],
          [["Binding constraint", "Too little capital to escape a poverty trap", "Bad incentives and no feedback", "Aid dependence and weak accountability"],
           ["Prescription", "Scale up aid, a coordinated big push", "Small, tested, accountable interventions", "Phase out government aid; find other finance"],
           ["View of 0.7%", "Endorses it", "Sceptical of big targets", "Rejects the premise"],
           ["Strongest evidence used", "Health and agriculture cost estimates", "Record of failed plans", "Africa's growth record"],
           ["Common criticism", "Overconfident planning", "Too sweeping against planning (Sen)", "Weak use of evidence"]]),
        H("green", "None of the three is about South Asia first. Read them as arguments to test "
          "against cases you know, such as polio eradication in India or microfinance in Bangladesh."),
    ], compact=True),

    S("The evidence", "What the cross-country evidence says about aid and growth", [
        B("Economists have tried for decades to measure whether aid raises growth across countries. "
          "The results swing with the method. The main problem is reverse causation: donors send more "
          "aid to countries in trouble, so a simple correlation can make aid look harmful."),
        T(["Study", "Finding"],
          [["Burnside and Dollar (2000), American Economic Review 90(4)",
            "Aid raises growth in countries with good fiscal, monetary and trade policies, and has "
            "little effect under poor policies"],
           ["Easterly, Levine and Roodman (2004), AER 94(3), comment",
            "Updating the data to 1970&ndash;97 and filling gaps, the good-policy result no longer holds"],
           ["Rajan and Subramanian (2008), Review of Economics and Statistics 90(4)",
            "After correcting for the bias that poor growth may attract aid, little evidence of a "
            "positive or negative effect; no sign aid works better under better policy"]]),
        TC([B("<strong>Policy message:</strong> Burnside and Dollar concluded that aid would work better if it "
              "were more systematically conditioned on good policy.", sm=True)],
           [B("<strong>Lesson:</strong> macro results are fragile. Judge programmes by their own "
              "evaluated results. See " + L("impact-eval.html", "Impact Evaluation 101") + ".", sm=True)]),
    ]),

    S("The ethical case", "Peter Singer and the refugees of 1971", [
        B("In 1971, as refugees from the Bangladesh Liberation War faced starvation in camps in India, "
          "the philosopher Peter Singer wrote \"Famine, Affluence, and Morality\", published in "
          "Philosophy &amp; Public Affairs in 1972. He argued that if we can prevent something very bad "
          "without sacrificing anything of comparable moral importance, we ought to do it. Distance "
          "makes no moral difference."),
        Q("It makes no moral difference whether the person I can help is a neighbor's child ten yards "
          "from me or a Bengali whose name I shall never know, ten thousand miles away.",
          "Peter Singer, Famine, Affluence, and Morality, Philosophy &amp; Public Affairs, 1972"),
        TC([B("<strong>The drowning child:</strong> walking past a child drowning in a shallow pond to "
              "keep your clothes clean is plainly wrong. Singer asks why distance changes that.", sm=True)],
           [B("<strong>Why it matters here:</strong> the essay shaped the ethics behind effective "
              "altruism (Section 9), and it began with South Asia.", sm=True)]),
    ]),

    S("For practitioners", "What the debate means for your work", [
        B("You do not need to settle the macro debate to do good work, but it should change how you "
          "design and defend programmes. Each side of the argument offers a test you can apply to a "
          "proposal before a funder applies it for you."),
        TC([P("green", "Take from Sachs",
              "Some problems need scale and coordination: immunisation, disease control, "
              "infrastructure. Under-funding a proven programme has a cost in lives.")],
           [P("amber", "Take from Easterly and Moyo",
              "Build feedback from the people served. Ask who is accountable when the plan fails. "
              "Watch for programmes that weaken a government's accountability to its own citizens.")]),
        BL(["Separate the evidence for the intervention from the evidence for aid in general.",
            "Amartya Sen, reviewing Easterly in Foreign Affairs, praised his attention to incentives "
            "but called his rejection of planning too sweeping. Hold both views at once.",
            "Write down which question your programme answers: growth, lives, or accountability."]),
    ]),
]

SEC4 = [
    DIV("04", "Four", "The aid effectiveness agenda"),

    S("The forums", "From Monterrey to Busan, 2002&ndash;2011", [
        B("After the Millennium Development Goals were adopted, donors and recipients met repeatedly "
          "to agree how aid should be delivered, as well as how much. The UN conference on financing "
          "for development at Monterrey in 2002 urged more aid and better aid. Four OECD-coordinated "
          "high level forums followed."),
        T(["Year", "Meeting", "Main product"],
          [["2002", "Monterrey, Mexico (UN)", "Monterrey Consensus: more aid, owned by developing countries"],
           ["2003", "Rome, Italy", "Rome Declaration on Harmonisation"],
           ["2005", "Paris, France", "Paris Declaration: five principles and 12 indicators"],
           ["2008", "Accra, Ghana", "Accra Agenda for Action, 4 September 2008"],
           ["2011", "Busan, Republic of Korea", "Busan Partnership; Global Partnership for Effective Development Co-operation"]]),
        H("cyan", "Source: Wikipedia, high level forums on aid effectiveness; COSV summary of the "
          "Paris Declaration and Accra Agenda."),
    ]),

    S("Paris 2005", "The Paris Declaration's five principles", [
        B("The Paris Declaration of 2005 is the best known product of the forums. It set out five "
          "principles and a set of measurable targets for 2010, with a monitoring survey to check "
          "progress. Each principle answers a complaint recipient governments had made for years: too "
          "many donors, each with its own systems, plans and missions."),
        FL(["OWNERSHIP: countries set their own strategies",
            "ALIGNMENT: donors use those strategies and country systems",
            "HARMONISATION: donors coordinate and simplify",
            "RESULTS: manage toward measurable goals",
            "MUTUAL ACCOUNTABILITY: both sides answer for results"]),
        TC([B("<strong>Ownership</strong> means national development strategies agreed with "
              "parliaments and citizens, and governments leading on aid coordination.", sm=True)],
           [B("<strong>Harmonisation</strong> means joint missions, shared analysis and fewer parallel "
              "project units that bypass ministries.", sm=True)]),
    ]),

    S("Did Paris deliver?", "The 2010 monitoring results", [
        B("The OECD's 2011 survey compared each indicator with its 2005 baseline and 2010 target. "
          "Progress was real but slow, and most targets were missed. The pattern is telling: targets "
          "that depended on recipients improved more than those that depended on donors changing "
          "their own procedures."),
        T(["Indicator", "2005 baseline", "Target", "2010 outcome"],
          [["Countries with operational development strategies", "19%", "75%", "52%"],
           ["Aid for government sector reported on budget", "44%", "85%", "46%"],
           ["Aid using country public financial management systems", "40%", "55%", "48%"],
           ["Aid disbursed within the scheduled year", "42%", "71%", "43%"],
           ["Aid fully untied", "89%", "More than 89%", "86% (2009)"],
           ["Parallel project implementation units", "1,696", "565", "1,158"],
           ["Countries with mutual assessment reviews", "44%", "100%", "50%"]]),
        H("amber", "Source: OECD, Aid Effectiveness 2011: Progress in Implementing the Paris Declaration "
          "(2012), Figure 1.2 (the 32 countries in both the 2006 and 2011 surveys) and, for untied "
          "aid, Table 1.1 and chapter 3. Of all the 2010 targets, only coordinated technical "
          "cooperation (target 50 per cent, outcome 57 per cent) was met."),
    ], compact=True),

    S("Accra 2008", "The Accra Agenda for Action", [
        B("Ministers from donor and developing countries endorsed the Accra Agenda for Action in Accra, "
          "Ghana, on 4 September 2008. It took stock of slow progress on Paris and set out three areas "
          "for faster change. The most visible shift was the recognition that civil society and "
          "parliaments, as well as governments, should shape development policy."),
        TC([BL(["<strong>Ownership:</strong> wider participation in policy, stronger government "
                "leadership of aid coordination and more use of country systems.",
                "<strong>Inclusive partnerships:</strong> DAC donors, developing countries, other "
                "donors, foundations and civil society all participate fully."])],
           [BL(["<strong>Delivering results:</strong> aid focused on real and measurable impact.",
                "Accra also asked for more predictable aid, so that governments could plan budgets "
                "beyond a single year."])]),
        H("cyan", "Source: COSV summary of the Paris Declaration and Accra Agenda for Action, "
          "reproducing OECD text."),
    ]),

    S("Busan 2011", "Busan: from aid effectiveness to development effectiveness", [
        B("The fourth and final forum, at Busan from 29 November to 1 December 2011, widened the frame beyond traditional "
          "donors and governments to the private sector, civil society organisations, parliamentarians "
          "and local authorities. The outcome document set four shared principles and created the Global Partnership "
          "for Effective Development Co-operation (GPEDC), which replaced the forum process."),
        T(["Busan principle", "Meaning"],
          [["Ownership of development priorities by developing countries", "Partnerships succeed only if led by developing countries"],
           ["Focus on results", "Lasting impact on poverty, inequality and national capacity"],
           ["Inclusive development partnerships", "Openness, trust and mutual learning among all actors"],
           ["Transparency and accountability to each other", "To each other, to beneficiaries and to citizens"]]),
        H("indigo", "Source: European Commission, The Busan Commitments: An Analysis of EU Progress and "
          "Performance, quoting the Busan Partnership document."),
    ]),

    S("Ownership in practice", "What ownership looks like from a ministry", [
        B("Ownership sounds simple until a ministry has many donors, each with its own priorities, "
          "reporting cycle and preferred indicators. The example below is Illustrative, built from the "
          "pattern the Paris indicators were designed to measure: parallel units, off-budget aid and "
          "separate missions."),
        TC([P("red", "Low ownership (Illustrative)",
              "A health ministry hosts six donor-funded project units, each with its own staff on "
              "higher salaries. Two thirds of aid does not appear in the national budget. Officials "
              "spend weeks each year hosting separate review missions.")],
           [P("green", "Higher ownership (Illustrative)",
              "Donors fund one sector plan through a pooled fund, use the government's procurement "
              "and audit systems, and hold one joint annual review. Aid appears on budget and "
              "parliament can see it.")]),
        H("amber", "Ownership can also be claimed by a government that does not answer to its own "
          "citizens. Accra's addition of parliaments and civil society was meant to address this."),
    ]),

    S("Why it stalled", "Why the effectiveness agenda lost momentum", [
        B("By the late 2010s the effectiveness agenda had faded from donor speeches. Several forces "
          "pulled against it. Donors faced domestic pressure to show visible, attributable results, "
          "which favours separate projects with donor flags. Security concerns and migration drew "
          "budgets toward donor interests. New lenders did not sign up to DAC norms. Then the cuts of "
          "2025 reduced the money itself."),
        TC([BL(["Visibility: a pooled fund cannot carry a single donor's logo.",
                "Risk: using country systems means sharing fiduciary risk.",
                "Attribution: results frameworks reward what one donor can claim."])],
           [BL(["Politics: aid budgets tied to trade, security and migration aims.",
                "Fragmentation: more funders, including foundations and new states.",
                "Volume: less money in 2025 means less influence over reform."])]),
        H("green", "For a South Asian NGO, the principles remain useful as a checklist. A funder who "
          "aligns with your plan, accepts your systems and reports jointly is following Paris, "
          "whether or not it says so."),
    ]),
]

SEC5 = [
    DIV("05", "Five", "The 2025 aid cuts"),

    S("The scale", "2025: the largest fall in aid on record", [
        B("The OECD's preliminary data, published on 9 April 2026, show that ODA from DAC members and "
          "associates fell by 23.1 per cent in real terms in 2025, the largest annual drop in the "
          "history of ODA and the second year of decline. It brings aid back to levels last seen in "
          "2015, the year the Sustainable Development Goals were adopted."),
        ST([C("&minus;23.1%", "real change in DAC ODA, 2025", "red", OECD),
            C("US$174.3 bn", "DAC ODA in 2025, down from US$215.1 bn", "amber", OECD),
            C("0.26%", "of combined GNI, down from 0.34%", "indigo", OECD),
            C("&minus;5.8%", "further decline projected for 2026", "red", OECD)], cols=4),
        TC([B("<strong>Concentrated:</strong> the United States alone cut its ODA by 56.9 per cent, "
              "and the five largest providers made up 95.7 per cent of the fall.", sm=True)],
           [B("<strong>Broad:</strong> 26 members cut aid; only eight held or increased it. Cuts "
              "reached core programmes, humanitarian aid and refugee costs alike.", sm=True)]),
    ]),

    S("The United States", "How USAID was dismantled in 2025", [
        B("USAID was founded in 1961 and was, until 2025, the largest foreign aid agency in the world. "
          "Within six months of the new administration taking office, its programmes were mostly "
          "cancelled and its remaining functions moved to the State Department. Because Congress "
          "reorganised USAID as an independent agency in 1998, it can be formally abolished only by "
          "an act of Congress."),
        T(["Date", "Event"],
          [["20 January 2025", "Executive Order 14169 orders a 90-day pause in US foreign development assistance"],
           ["Late January 2025", "Secretary of State Marco Rubio issues a waiver for humanitarian aid; delivery stays uncertain"],
           ["10 March 2025", "Rubio announces 83 per cent of USAID programmes cancelled, about 5,200 contracts"],
           ["28 March 2025", "State and USAID notify Congress of a plan to move some USAID functions to State by 1 July and end the rest"],
           ["1 July 2025", "USAID ceases to implement foreign assistance; State Department takes over"]]),
        H("red", "Sources: EO 14169 (Federal Register, 30 January 2025); State Department, 28 March 2025; Anadolu Agency, 1 July 2025; "
          "Wikipedia, United States Agency for International Development."),
    ]),

    S("The order", "What Executive Order 14169 said", [
        B("The order was signed on 20 January 2025 and published in the Federal Register on 30 January "
          "under the title \"Reevaluating and Realigning United States Foreign Aid\". Its operative "
          "section froze new obligations and disbursements of development assistance while each "
          "programme was reviewed against foreign policy goals. A programme could resume early only "
          "if the Secretary of State decided to continue it."),
        Q("90-day pause in United States foreign development assistance for assessment of programmatic "
          "efficiencies and consistency with United States foreign policy.",
          "Executive Order 14169, section 3(a), 20 January 2025"),
        TC([B("<strong>For implementers:</strong> a pause in disbursement stops salaries, supply "
              "chains and services within weeks, even if a programme is later restored.", sm=True)],
           [B("<strong>For the law:</strong> several lawsuits argued that the administration lacked the "
              "power to do this without congressional authorisation.", sm=True)]),
    ]),

    S("The United Kingdom", "The UK: from 0.7 to 0.5 to 0.3 per cent of GNI", [
        B("The UK wrote the 0.7 per cent target into law in the International Development (Official "
          "Development Assistance Target) Act 2015, s1, and reported 0.70 per cent in 2019. In 2021 "
          "the government cut ODA to 0.5 per cent of GNI. On 25 February 2025 Prime Minister Keir "
          "Starmer told the House of Commons that defence spending would rise to 2.5 per cent of GDP "
          "by 2027, paid for by cutting ODA from 0.5 to 0.3 per cent of GNI over the same period."),
        TC([ST([C("0.5% &rarr; 0.3%", "UK ODA target, announced 25 February 2025, for 2027",
                  "red", "Civil Service World, 25 February 2025"),
                C("&pound;13.4 bn", "extra defence spending a year from 2027",
                  "indigo", "Civil Service World, 25 February 2025")], cols=1)],
           [BL(["The UK was still the third largest provider in 2025, at US$17.2 billion (OECD).",
                "ODA had risen to 0.58 per cent under the previous government (Civil Service World).",
                "The cut follows a pattern across donors: aid budgets moved to defence and security."])]),
        H("amber", "If your organisation holds FCDO funding, directly or through a partner, check the "
          "current country allocation before assuming a programme continues."),
    ]),

    S("Who cut", "The five largest providers all cut aid in 2025", [
        B("For the first time on record, every one of the five largest providers reduced its ODA in "
          "the same year. Germany became the largest provider, ahead of the United States, mainly "
          "because US aid fell so far. The chart shows 2025 volumes; the OECD release gives the US "
          "fall as 56.9 per cent and attributes 95.7 per cent of the total decline to these five."),
        TC([BAR("apTop25", "ODA by provider, 2025 (US$ billion, preliminary)", OECD,
                ["Germany", "United States", "United Kingdom", "Japan", "France"], "US$ bn",
                [29.1, 29.0, 17.2, 16.2, 14.5], "#6366F1", ytitle="US$ billion")],
           [B("Germany, the UK, Japan and France all cut alongside the United States, and smaller "
              "donors faced budget, security and political pressure, in the words of the DAC Chair, "
              "Carsten Staur.", sm=True),
            H("cyan", "Only four donors exceeded 0.7 per cent: Norway, Luxembourg, Sweden and "
              "Denmark.")], ratio="a32"),
    ]),

    S("The human cost", "Estimating what the US cuts may cost in lives", [
        B("A study in The Lancet, published online on 30 June 2025, used panel data from 133 countries "
          "to estimate the effect of USAID funding on mortality between 2001 and 2021, and then "
          "forecast the effect of the cuts. It is an observational study with wide uncertainty "
          "intervals, so quote its ranges."),
        ST([C("91.8 million", "deaths estimated prevented by USAID funding, 2001&ndash;2021", "green",
              "Cavalcanti et al., The Lancet 406(10500), 2025"),
            C("14.05 million", "additional deaths forecast by 2030 if cuts are not reversed (range 8.5&ndash;19.7 million)",
              "red", "Cavalcanti et al., The Lancet, 2025"),
            C("4.54 million", "of those forecast deaths among children under five", "amber",
              "Cavalcanti et al., The Lancet, 2025")], cols=3),
        TC([B("<strong>Method:</strong> fixed-effects Poisson models linking funding levels to "
              "mortality, combined with microsimulation forecasts.", sm=True)],
           [B("<strong>Caution:</strong> these are observational associations from panel data, with no randomised comparison. "
              "Use the ranges, and say so when you cite the figure.", sm=True)]),
    ]),

    S("Who is hit", "The cuts fall hardest on the poorest countries", [
        B("Aid cuts are not spread evenly. Donors protect some priorities and let others fall. The "
          "OECD's 2025 data show the steepest falls in the places and sectors with fewest alternative "
          "sources of finance. Gender-related aid had already started falling before 2025."),
        T(["Category", "Change", "Period"],
          [["DAC ODA to least developed countries", "&minus;25.8%", "2025"],
           ["DAC ODA to sub-Saharan Africa", "&minus;26.3%", "2025"],
           ["Bilateral ODA for core development programming", "&minus;26.3%", "2025"],
           ["Humanitarian ODA", "&minus;35.8%", "2025"],
           ["In-donor refugee costs", "&minus;22.1%", "2025"],
           ["Bilateral allocable ODA with gender equality objectives", "&minus;13%", "2023 to 2024"]]),
        H("red", "Sources: " + OECD + "; " + OECDT + ". Final 2025 data are due in December 2026."),
    ], compact=True),

    S("South Asian organisations", "What the cuts mean for organisations in South Asia", [
        B("Many South Asian NGOs never held a USAID contract directly. They were sub-grantees of an "
          "international NGO or a consulting firm, so the cut arrived as a stop-work notice from a "
          "partner. Indian organisations face an extra constraint: since 2020 a FCRA-registered "
          "organisation may not pass foreign contributions on to another (Section 8 of this course), so they cannot "
          "easily be rescued by a larger Indian partner's foreign funds."),
        TC([P("red", "Immediate effects",
              "Staff contracts ended, health and nutrition services paused, data collection stopped "
              "mid-survey, and organisations with one large funder faced closure.")],
           [P("green", "Strategic responses",
              "Diversify funders, build domestic donor and CSR income, keep three to six months of "
              "reserves, write exit clauses into sub-grants, and document assets bought with "
              "foreign funds.")]),
        H("amber", "GiveWell ran a rapid response fund in 2025 and disbursed US$39 million to "
          "programmes that lost US funding (Wikipedia, GiveWell). Private money moved fast, but it "
          "replaced a small fraction."),
    ]),
]

SEC6 = [
    DIV("06", "Six", "Aid to South Asia"),

    S("The numbers", "Net ODA received by South Asian countries, 2023", [
        B("The World Bank's World Development Indicators report net ODA received by each country, "
          "using OECD data. Net means disbursements minus repayments of principal on earlier aid "
          "loans. The latest year with complete data is 2023. Three measures tell three different "
          "stories: the total, the share of national income and the amount per person."),
        T(["Country", "Net ODA received (US$ million)", "% of GNI", "Per person (US$)"],
          [["Bangladesh", "5,684", "1.25", "33.15"],
           ["Pakistan", "3,964", "1.20", "16.01"],
           ["Afghanistan", "3,060", "17.76", "73.82"],
           ["India", "2,377", "0.07", "1.65"],
           ["Nepal", "1,173", "2.82", "39.51"],
           ["Sri Lanka", "827", "1.01", "37.54"]]),
        H("cyan", "Source: " + WDI + ", indicators DT.ODA.ODAT.CD, DT.ODA.ODAT.GN.ZS and "
          "DT.ODA.ODAT.PC.ZS. Current US dollars. Data for 2024 were not yet published."),
    ], compact=True),

    S("Trends", "Net ODA received, 2012&ndash;2023", [
        B("Over a decade the totals move a great deal from year to year, because large loans are "
          "disbursed in lumps and repayments come back in others. Bangladesh shows the clearest rise, "
          "from US$2.15 billion in 2012 to US$5.68 billion in 2023. India's total has stayed between "
          "about US$1.7 billion and US$3.2 billion throughout."),
        {"t": "chart", "canvas": "apSaTrend", "title": "Net ODA received, US$ million (current prices)",
         "source": WDI, "type": "line",
         "data": {"labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"],
                  "datasets": [
                      {"label": "Bangladesh", "data": [2154, 2634, 2423, 2593, 2533, 3782, 3045, 4383, 5376, 5091, 5205, 5684],
                       "borderColor": "#10B981", "backgroundColor": "#10B981", "tension": 0.2},
                      {"label": "Pakistan", "data": [2017, 2194, 3616, 3764, 2961, 2364, 1387, 2010, 2593, 2924, 1734, 3964],
                       "borderColor": "#6366F1", "backgroundColor": "#6366F1", "tension": 0.2},
                      {"label": "India", "data": [1682, 2456, 2992, 3174, 2679, 3198, 2462, 2551, 1796, 3137, 2818, 2377],
                       "borderColor": "#F59E0B", "backgroundColor": "#F59E0B", "tension": 0.2},
                      {"label": "Nepal", "data": [770, 873, 884, 1224, 1064, 1270, 1452, 1334, 1760, 1600, 1199, 1173],
                       "borderColor": "#0EA5E9", "backgroundColor": "#0EA5E9", "tension": 0.2},
                      {"label": "Sri Lanka", "data": [491, 403, 492, 445, 373, 316, -247, 193, 219, 155, 12, 827],
                       "borderColor": "#EF4444", "backgroundColor": "#EF4444", "tension": 0.2}]},
         "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'US$ million'} } } }"}},
        H("indigo", "Afghanistan is left off the chart so that the scale stays readable; it received "
          "US$6.67 billion in 2012 and US$3.06 billion in 2023."),
    ]),

    S("Size and dependence", "India receives a lot of aid and depends on it very little", [
        B("India is a large recipient in absolute terms. Relative to its economy, though, aid is close "
          "to zero: 0.07 per cent of GNI in 2023. For Nepal the share was 2.82 per cent, forty times "
          "larger. The difference matters for bargaining power. A ministry that relies on donors for "
          "a large part of its development budget has less room to say no to their conditions."),
        TC([ST([C("0.07%", "net ODA received as share of GNI, India, 2023", "amber", WDI),
                C("2.82%", "net ODA received as share of GNI, Nepal, 2023", "cyan", WDI),
                C("1.25%", "net ODA received as share of GNI, Bangladesh, 2023", "green", WDI)], cols=1)],
           [B("<strong>For India:</strong> aid matters most where it brings technical knowledge, "
              "pilots or loans for specific infrastructure, and through NGOs that depend on it.", sm=True),
            B("<strong>For Nepal:</strong> aid is a visible part of public finance, so donor "
              "coordination and alignment with national plans matter more.", sm=True),
            H("indigo", "Per person, India received US$1.65 in 2023, against US$39.51 in Nepal.")]),
    ]),

    S("Per person", "Per person, the ranking reverses", [
        B("Ranking by aid per person turns the table upside down. The smaller countries receive far "
          "more per head, and India, with the largest population, receives the least. This is one "
          "reason donors describe India as a partner for technical cooperation and lending, and "
          "describe Nepal and Afghanistan as aid-dependent."),
        TC([BAR("apPerCap", "Net ODA received per person, 2023 (US$)", WDI,
                ["Afghanistan", "Nepal", "Sri Lanka", "Bangladesh", "Pakistan", "India"], "US$ per person",
                [73.82, 39.51, 37.54, 33.15, 16.01, 1.65], "#0EA5E9", horizontal=True, ytitle="US$ per person")],
           [B("Per-person figures depend on population estimates as well as aid flows. Sri Lanka's "
              "figure was US$0.55 in 2022 and US$37.54 in 2023, which shows how a single year can "
              "mislead.", sm=True),
            H("amber", "Always show more than one year before drawing a conclusion about a country.")],
           ratio="a32"),
    ]),

    S("Net flows", "Reading a negative number: Sri Lanka in 2018", [
        B("In 2018 Sri Lanka's net ODA received was negative: minus US$247 million, or minus 0.27 per "
          "cent of GNI. The negative sign records that its repayments of principal on "
          "earlier concessional loans were larger than the new aid it received that year. A negative "
          "figure tells you about the timing of loans and repayments, and nothing about donors' "
          "goodwill."),
        TC([TERM("Net ODA received",
                 "Gross disbursements of grants and concessional loans, minus repayments of principal "
                 "on earlier ODA loans, in a given year. It can be negative.")],
           [T(["Year", "Sri Lanka net ODA (US$ m)"],
              [["2017", "316"], ["2018", "&minus;247"], ["2019", "193"], ["2022", "12"], ["2023", "827"]])]),
        H("cyan", "Source: " + WDI + ". When you cite aid to a country that borrows heavily, say "
          "whether the figure is gross or net."),
    ]),

    S("Nepal", "Nepal: aid in a small economy", [
        B("Nepal shows what aid dependence looks like. Net ODA received rose from US$770 million in "
          "2012 to a peak of US$1.76 billion in 2020, when it reached 5.2 per cent of GNI. By 2023 it "
          "had fallen to US$1.17 billion, or 2.82 per cent of GNI. In the years when aid is a large "
          "share of public investment, the timing of donor disbursements shapes what the state can "
          "build."),
        TC([ST([C("5.2%", "net ODA as share of GNI, Nepal, 2020 (decade peak)", "red", WDI),
                C("US$39.51", "net ODA received per person, Nepal, 2023", "cyan", WDI)], cols=1)],
           [BL(["Aid coordination is a daily task for Nepal's ministries, so Paris-style "
                "alignment has real stakes.",
                "Federalism under the 2015 Constitution added provincial and local governments as "
                "partners for donors.",
                "Falls in donor budgets in 2025 reach Nepal through both bilateral and multilateral "
                "channels."])]),
        H("indigo", "Practitioners in Nepal should track donors' multi-year commitments as closely as "
          "the national budget."),
    ]),

    S("Afghanistan", "Afghanistan: the extreme case of dependence", [
        B("Afghanistan is the region's outlier. In 2012 net ODA received equalled 33.4 per cent of "
          "GNI, and in 2021 it was still 32.7 per cent. By 2023 it was 17.76 per cent, US$3.06 "
          "billion. When aid supplies a third of national income, aid decisions are economic policy, "
          "and a donor exit becomes an economic shock."),
        TC([BAR("apAfg", "Net ODA received as % of GNI, Afghanistan", WDI,
                ["2012", "2015", "2018", "2021", "2023"], "% of GNI",
                [33.4, 22.2, 20.73, 32.7, 17.76], "#EF4444", ytitle="% of GNI")],
           [B("Very high dependence brings a known set of risks: parallel systems outside the state, "
              "salaries set by donors, and services that stop when funding stops.", sm=True),
            H("amber", "These ratios rely on GNI estimates that are themselves uncertain in crisis "
              "years. Treat the level as indicative and the direction as the finding.")], ratio="a32"),
    ]),

    S("Loans and growth", "Bangladesh and Pakistan: rising totals and the role of loans", [
        B("Bangladesh's net ODA received more than doubled between 2012 and 2023, and per person it "
          "rose from US$13.89 to US$33.15. Pakistan's moved between US$1.4 billion and US$4.0 billion. "
          "Net ODA includes concessional loans, so rising totals can mean more borrowing as well as "
          "more grants. As incomes rise, countries lose access to the softest terms and the mix moves "
          "toward loans."),
        TC([P("green", "Bangladesh",
              "2,154 (2012) to 5,684 (2023), US$ million. Per person, 13.89 to 33.15 US$. Share of "
              "GNI stayed between about 0.9 and 1.6 per cent, because the economy grew alongside aid.")],
           [P("indigo", "Pakistan",
              "2,017 (2012), a low of 1,387 (2018) and 3,964 (2023), US$ million. Swings follow "
              "large disbursements in some years and repayments in others.")]),
        H("cyan", "Source: " + WDI + ". For a loan-heavy country, read the debt data beside the aid "
          "data. See " + L("development-finance.html", "Development Finance 101") + "."),
    ]),
]

SEC7 = [
    DIV("07", "Seven", "India as a development partner"),

    S("Both sides", "India: recipient and provider at the same time", [
        B("India still receives aid: net ODA of US$2.38 billion in 2023, including concessional loans "
          "and grants. It also provides development finance and training to other "
          "countries, through programmes run by the Ministry of External Affairs. India is not a "
          "member of the OECD's Development Assistance Committee, so its outgoing assistance does not "
          "appear in DAC ODA totals and follows its own rules."),
        TC([P("cyan", "India as recipient",
              "World Bank and Asian Development Bank loans, bilateral loans from countries such as "
              "Japan, and grants to NGOs registered under the FCRA. Small relative to the economy: "
              "0.07 per cent of GNI in 2023 (World Bank WDI).")],
           [P("green", "India as provider",
              "Training under ITEC since 1964, concessional lines of credit under the IDEAS scheme, "
              "and grants for projects in neighbouring countries, managed since 2012 by the "
              "Development Partnership Administration in the MEA.")]),
        H("indigo", "India describes this as development partnership and South-South cooperation, "
          "a framing that avoids the donor-recipient hierarchy of DAC aid."),
    ]),

    S("ITEC", "The Indian Technical and Economic Cooperation programme", [
        B("ITEC was launched on 15 September 1964 by the Ministry of External Affairs. For decades it "
          "remained small, because India was itself a major aid recipient. It grew from the 2000s as "
          "the economy grew. It is described as demand-driven: partner countries request the "
          "training or support they want."),
        TC([BL(["Training for civil and defence personnel in Indian institutions, with airfare, "
                "boarding and tuition paid by India.",
                "Projects and project-related activities, including consultancy and feasibility "
                "studies.",
                "Study tours and donation of equipment."])],
           [BL(["Deputation of Indian experts to partner countries.",
                "Aid for disaster relief.",
                "Coverage of about 158 countries with its companion programme for Africa, according "
                "to MEA material summarised by Wikipedia."])]),
        H("cyan", "Source: Wikipedia, Indian Technical and Economic Cooperation Programme, citing the "
          "Ministry of External Affairs. Check itecgoi.in for current course lists."),
    ]),

    S("Institutions", "The Development Partnership Administration, 2012", [
        B("In 2012 the Ministry of External Affairs set up a Development Partnership Administration "
          "(DPA) within its Economic Relations Division to bring outgoing assistance under one roof "
          "and simplify its administration. Earlier finance ministers had floated a separate agency, "
          "under names such as an India International Development Cooperation Agency, but India kept "
          "development partnership inside the foreign ministry."),
        TC([P("green", "Why inside the MEA",
              "Development partnership is treated as part of foreign policy, closely tied to the "
              "Neighbourhood First policy and to relations with Africa. Decisions sit with diplomats.")],
           [P("amber", "What it means for partners",
              "Projects are negotiated government to government. Indian NGOs and researchers have few "
              "formal routes into the programme, unlike DAC donors' open calls for proposals.")]),
        H("indigo", "Source: Wikipedia, Indian Technical and Economic Cooperation Programme (section "
          "on an Indian aid agency)."),
    ]),

    S("Lines of credit", "Lines of credit under the IDEAS scheme", [
        B("In 2003-04 the Government of India set up what is now the Indian Development and Economic "
          "Assistance Scheme (IDEAS). Under it, concessional lines of credit backed by the government "
          "are routed through the Export-Import Bank of India to partner governments and institutions. "
          "The loans pay for goods and services, including consultancy, supplied from India (Exim "
          "Bank of India)."),
        ST([C("300+", "lines of credit extended", "cyan", MEA),
            C("US$32 bn", "total value of lines of credit", "green", MEA),
            C("68", "partner countries", "indigo", MEA),
            C("~600", "projects covered", "amber", MEA)], cols=4),
        TC([B("<strong>Sectors:</strong> railways, roads, agriculture, industry, airports, ports, "
              "hospitals, power transmission, hydroelectricity and information technology (MEA).", sm=True)],
           [B("<strong>Mechanism (Exim Bank):</strong> credits let buyers in partner countries import "
              "projects, equipment, goods and services from India on deferred credit terms.", sm=True)]),
    ]),

    S("Where the credit goes", "Lines of credit by partner, as on August 2024", [
        B("The MEA states that the neighbourhood gets priority under its Neighbourhood First policy. "
          "Bangladesh alone accounts for about a quarter of the total. Africa, taken together, "
          "received 196 lines of credit worth US$12 billion across 42 countries."),
        TC([BAR("apLoc", "Indian lines of credit, US$ billion (as on August 2024)", MEA,
                ["Africa (42 countries)", "Bangladesh", "Sri Lanka", "CIS", "Nepal", "Maldives", "Latin America", "Myanmar"],
                "US$ bn", [12.0, 7.862, 2.0, 1.84, 1.65, 1.43, 0.811, 0.745], "#10B981",
                horizontal=True, ytitle="US$ billion")],
           [B("Sri Lanka is shown at US$2 billion; the MEA says \"more than US$2 billion\". Oceania "
              "received US$155 million.", sm=True),
            H("cyan", "Examples named by the MEA include railway projects in Bangladesh and Sri Lanka "
              "and Hanimaadhoo International Airport in the Maldives.")], ratio="a32"),
    ]),

    S("Assessing the model", "Strengths and criticisms of India's approach", [
        B("India presents its development partnership as demand-driven and free of the policy "
          "conditions attached to much DAC aid. Lines of credit, though, are designed to buy Indian "
          "goods and services, which is close to the OECD's definition of tied aid. Both things can "
          "be true at once, and partner governments weigh them differently."),
        TC([P("green", "Strengths claimed",
              "Requests come from partner governments. Few policy conditions. Training builds "
              "networks across the Global South. Infrastructure is visible and long-lived.")],
           [P("red", "Common criticisms",
              "Procurement tied to Indian suppliers. Credits must be repaid, adding to partners' debt. "
              "Limited public data on disbursement and results compared with DAC reporting, which "
              "makes outside assessment hard.")]),
        H("amber", "The Exim Bank has itself invited proposals for socio-economic impact assessments "
          "of projects funded under these lines of credit, a sign that evidence on results is still "
          "being built."),
    ]),

    S("Comparing providers", "DAC donors and India compared", [
        B("Comparing India with DAC donors helps explain why the same partner country may prefer "
          "different providers for different jobs. The table summarises the formal differences. It "
          "describes rules and channels, and says nothing on its own about which model delivers more "
          "development."),
        T(["Feature", "DAC donors", "India"],
          [["Reports to OECD as ODA", "Yes, required", "No; not a DAC member"],
           ["Main instruments", "Grants, concessional loans, multilateral contributions", "Lines of credit, grants, training"],
           ["Policy conditions", "Often, especially on budget support", "Few, by stated policy"],
           ["Procurement", "Mostly untied (86% fully untied in 2009)", "Lines of credit buy from India"],
           ["Who implements", "Governments, UN agencies, NGOs, firms", "Indian companies and public bodies"],
           ["Managing body", "Development agencies or ministries", "MEA Development Partnership Administration"]]),
        H("indigo", "Sources: OECD; MEA; Exim Bank of India; Paris monitoring as tabulated in "
          "Wikipedia. See " + L("dev-architecture.html", "Global Development Governance 101") + "."),
    ], compact=True),
]

SEC8 = [
    DIV("08", "Eight", "Philanthropy in India: money and law"),

    S("The scale", "India's social sector funding, and the gap", [
        B("The India Philanthropy Report 2026, from Bain &amp; Company and Dasra, estimates that total "
          "social sector funding grew at 13 per cent a year between FY20 and FY25 to about "
          "&#8377;27 lakh crore. Public spending is about 95 per cent of it. Private philanthropy, at "
          "a projected &#8377;1.43 lakh crore in FY25, is small by comparison, and the report "
          "estimates a funding gap near &#8377;16 lakh crore against NITI Aayog norms."),
        ST([C("&#8377;27 lakh cr", "total social sector funding, FY25 (about US$310 bn)", "cyan", IPR26),
            C("~95%", "share from public spending", "indigo", IPR26),
            C("&#8377;1.43 lakh cr", "private philanthropy, FY25 projection", "green", IPR26),
            C("&#8377;16 lakh cr", "estimated funding gap, FY25", "red", IPR26)], cols=4),
        TC([B("<strong>Lesson:</strong> philanthropy cannot replace the state. Its value lies in "
              "risk-taking, innovation, advocacy and filling gaps the state does not reach.", sm=True)],
           [B("<strong>Caution:</strong> these are consultancy estimates with stated methods. Quote "
              "them as estimates and name the report and year.", sm=True)]),
    ]),

    S("Who gives", "Families, companies and the rise of family offices", [
        B("Families are at the centre of private giving in India. The 2026 report estimates that they "
          "contribute about 42 per cent of private giving, through personal philanthropy and through "
          "the CSR of family-owned or family-run businesses. The 2025 report found that such "
          "businesses provide 65 to 70 per cent of private-sector CSR, about &#8377;18,000 crore a "
          "year."),
        TC([ST([C("~42%", "of private giving from families (personal and family-business CSR)", "green", IPR26),
                C("45 &rarr; 300", "family offices in India, 2018 to 2024", "cyan", IPR25)], cols=1)],
           [BL(["About 65 per cent of families had dedicated staff to manage their philanthropy "
                "(2025 report).",
                "41 per cent preferred grant-making as their main approach; 23 per cent combined grants "
                "with running programmes.",
                "Causes are widening to gender, equity, climate, livelihoods, arts and animal welfare."])]),
        H("indigo", "Sources: " + IPR25 + " (27 February 2025); " + IPR26 + " (26 February 2026)."),
    ]),

    S("CSR: who must spend", "Section 135 of the Companies Act 2013: who is covered", [
        B("India is one of the few countries where companies are required by law to spend on social "
          "causes. Section 135 of the Companies Act 2013 took effect on 1 April 2014. It applies to "
          "any company that, in the immediately preceding financial year, met any one of three "
          "thresholds."),
        T(["Threshold under s135(1)", "Amount"],
          [["Net worth", "&#8377;500 crore or more"],
           ["Turnover", "&#8377;1,000 crore or more"],
           ["Net profit", "&#8377;5 crore or more"]]),
        TC([BL(["The company must form a CSR committee of three or more directors, at least one "
                "independent (s135(1)).",
                "The committee drafts the CSR policy, recommends spending and monitors it (s135(3))."])],
           [BL(["The Board approves the policy and places it on the company's website (s135(4)).",
                "If the required spend is &#8377;50 lakh or less, the Board itself does the committee's "
                "work (s135(9))."])]),
    ], compact=True),

    S("The 2% rule", "Spending 2 per cent, and what happens to unspent money", [
        B("Section 135(5) requires the Board to ensure the company spends at least 2 per cent of its "
          "average net profits from the three immediately preceding financial years, giving "
          "preference to local areas where it operates. Amendments in 2019 and 2020 turned a "
          "comply-or-explain rule into a spending duty with money penalties."),
        FL(["CALCULATE: 2% of average net profit, last three years",
            "SPEND: in the financial year, under the CSR policy",
            "ONGOING PROJECT UNSPENT: move to Unspent CSR Account within 30 days; spend within 3 years",
            "OTHER UNSPENT: transfer to a Schedule VII fund (s135(5) proviso, s135(6))"]),
        TC([B("<strong>Penalty (s135(7)):</strong> the company pays twice the amount it should have "
              "transferred or &#8377;1 crore, whichever is less; each officer in default one tenth or "
              "&#8377;2 lakh, whichever is less.", sm=True)],
           [B("<strong>Impact assessment (CSR Rules, rule 8(3)):</strong> companies with an average "
              "obligation of &#8377;10 crore or more must commission independent assessment of "
              "projects of &#8377;1 crore or more.", sm=True)]),
    ]),

    S("Schedule VII", "Schedule VII: what counts as CSR", [
        B("CSR spending counts only if it falls within the activities listed in Schedule VII to the "
          "Companies Act 2013. The list has been amended several times, including in 2019 and 2020. "
          "Under the CSR Rules, activities that benefit the company's own employees do not count, "
          "and activities outside India count only for training Indian sports personnel."),
        T(["Item", "Activity (summarised)"],
          [["(i)", "Hunger, poverty and malnutrition; health care, sanitation and safe drinking water"],
           ["(ii)", "Education, including special education and vocational skills; livelihood projects"],
           ["(iii)", "Gender equality; homes and hostels for women and orphans; care for older people; reducing inequalities"],
           ["(iv)", "Environmental sustainability, animal welfare, conservation; Clean Ganga Fund"],
           ["(v)", "National heritage, art and culture; public libraries; traditional crafts"],
           ["(vi)&ndash;(vii)", "Armed forces veterans and war widows; training for sports"],
           ["(viii)", "Prime Minister's National Relief Fund and specified welfare funds"],
           ["(ix)&ndash;(xii)", "Technology incubators and research; rural development; slum area development; disaster management"]]),
        H("cyan", "Source: Companies Act 2013, Schedule VII, as amended (ca2013.com)."),
    ], compact=True),

    S("CSR spending", "CSR spending, 2018-19 to 2022-23", [
        B("The Ministry of Corporate Affairs publishes CSR spending reported by companies. Total "
          "spending rose from &#8377;20,218 crore in 2018-19 to &#8377;29,988 crore in 2022-23. For "
          "scale, the same India Philanthropy Report estimates total private philanthropy at well over "
          "a lakh crore, so mandatory CSR is a large but minority share of private giving."),
        TC([BAR("apCsr", "Total CSR expenditure, &#8377; crore", MCA,
                ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23"], "&#8377; crore",
                [20218, 24966, 26211, 26616, 29988], "#F59E0B", ytitle="Rupees crore")],
           [B("Reported spending rose in every year of this series, including the pandemic year "
              "2020-21. Growth was slowest between 2020-21 and 2021-22.", sm=True),
            H("amber", "These are reported figures. The MCA's state-level series ends in 2022-23, "
              "the latest year it publishes at that level.")], ratio="a32"),
    ]),

    S("Concentration", "CSR money follows company headquarters", [
        B("Section 135(5) asks companies to prefer local areas where they operate. Most large "
          "companies are headquartered in a few industrial states, so CSR spending concentrates "
          "there. In 2022-23 Maharashtra received &#8377;5,497 crore, while Bihar received "
          "&#8377;235 crore and Meghalaya &#8377;22 crore. A further &#8377;6,061 crore was reported "
          "as \"PAN India\", with no state named."),
        TC([T(["Sector, 2022-23", "&#8377; crore"],
              [["Education", "10,086"], ["Health care", "6,831"], ["Rural development", "2,005"],
               ["Environmental sustainability", "1,960"], ["Livelihood projects", "1,654"],
               ["Hunger, poverty, malnutrition", "1,233"], ["All sectors", "29,988"]])],
           [T(["State or category, 2022-23", "&#8377; crore"],
              [["Maharashtra", "5,497"], ["Gujarat", "2,008"], ["Karnataka", "1,986"],
               ["Uttar Pradesh", "1,153"], ["Bihar", "235"], ["Meghalaya", "22"],
               ["PAN India (no state)", "6,061"]])]),
        H("red", "Education and health took more than half of all CSR in 2022-23. Source: " + MCA +
          ". See " + L("csr-esg.html", "CSR &amp; ESG 101") + "."),
    ], compact=True),

    S("FCRA", "The Foreign Contribution (Regulation) Act 2010", [
        B("Foreign money for Indian civil society is regulated by the " + FCRA + ". An association "
          "may accept a foreign contribution only if it is registered with the central government or "
          "has prior permission for a specific contribution (s11). Certain people may not accept "
          "foreign contributions at all, including election candidates, editors and publishers of "
          "newspapers, judges, government servants, legislators and political parties (s3)."),
        TC([TERM("Foreign contribution",
                 "A donation or transfer of currency, security or article, beyond a specified value, "
                 "from a foreign source (PRS summary of the Act). The Act governs both acceptance and "
                 "use.")],
           [BL(["Registration must be renewed before it expires (s16).",
                "Foreign funds must be used for the purpose for which they were received (s8).",
                "The government may suspend (s13) or cancel registration.",
                "More than 19,000 registrations were cancelled between 2011 and 2019, according to "
                "the 2020 Bill's statement of objects and reasons (SCC Times, 23 September 2020)."])]),
        H("amber", "FCRA status is the first thing a foreign funder will ask an Indian partner about."),
    ]),

    S("FCRA 2020", "The 2020 amendment, section by section", [
        B("Parliament passed the Foreign Contribution (Regulation) Amendment Bill in September 2020 "
          "and it received assent on 28 September 2020 as Act No. 33 of 2020. It tightened almost "
          "every stage of the money's journey. The Supreme Court upheld the main amendments in "
          "<em>Noel Harper v Union of India</em>, judgment of 8 April 2022, holding that the right to "
          "association does not include a right to unregulated foreign funds."),
        T(["Section of the 2010 Act", "Change made in 2020"],
          [["s3", "Public servants, and employees of government-owned corporations, barred from accepting"],
           ["s7", "No transfer of foreign contribution to any other person, even if registered"],
           ["s8(1)", "Administrative expenses capped at 20 per cent (was 50 per cent)"],
           ["s12(1A), s17", "Receipt only in an \"FCRA Account\" at the notified State Bank of India branch, New Delhi"],
           ["s12A", "Aadhaar of office bearers, directors or key functionaries required"],
           ["s13", "Suspension may be extended by a further 180 days"],
           ["s14A", "New route to surrender a registration certificate"]]),
        H("red", "Sources: " + FCRA20 + ", Gazette of 28 September 2020; PRS bill summary; Supreme "
          "Court Observer, WP (C) 566/2021."),
    ], compact=True),

    S("Tax and giving", "Donations under the Income-tax Act 2025, section 133", [
        B("The " + ITA + " applies from 1 April 2026 and replaces the Income-tax Act 1961. Section 133 "
          "now governs deductions for donations, the role section 80G played under the old Act. "
          "For a gift to a charity to earn the 50 per cent deduction, the charity must be a registered "
          "non-profit organisation, or a listed institution or fund, approved under section 354."),
        TC([BL(["<strong>100 per cent deduction (s133(1)(a)):</strong> listed funds such as the "
                "Prime Minister's National Relief Fund, PM CARES, the National Children's Fund and "
                "Swachh Bharat Kosh.",
                "<strong>50 per cent deduction (s133(1)(b)):</strong> donations to an approved "
                "registered non-profit organisation established in India for a charitable purpose."])],
           [BL(["<strong>Cap (s133(2)):</strong> certain donations count only up to 10 per cent of "
                "adjusted gross total income.",
                "<strong>Cash (s133(5)):</strong> no deduction for cash donations over &#8377;2,000.",
                "<strong>Verification (s133(6)):</strong> claims are checked against the information "
                "the organisation files with the tax department."])]),
        H("cyan", "Source: Income Tax Department, Income-tax Act 2025, section 133. CSR sums spent "
          "under s135(5) and paid into Swachh Bharat Kosh or the Clean Ganga Fund do not qualify "
          "(s133(1)(a)(xx) and (xxi))."),
    ]),
]

SEC9 = [
    DIV("09", "Nine", "Effective altruism and its critics"),

    S("The argument", "From Singer's essay to a movement", [
        B("Singer's 1972 essay set out a simple chain of reasoning. Effective altruism, a name coined "
          "in 2011, added a second question: if you are going to give, how do you do the most good "
          "with each rupee or dollar? The philosophers most associated with it are Peter Singer, "
          "Toby Ord and William MacAskill. Giving What We Can and 80,000 Hours came together under "
          "the Centre for Effective Altruism in 2011."),
        FL(["PREMISE: suffering from lack of food, shelter and care is bad",
            "PREMISE: if we can prevent it at little moral cost, we ought to",
            "STEP: distance does not change the duty",
            "EA ADDS: compare options and fund the most cost-effective"]),
        TC([B("<strong>What EA measures:</strong> outcomes per dollar, such as deaths averted or "
              "years of healthy life gained.", sm=True)],
           [B("<strong>What EA asks of donors:</strong> give a meaningful share of income, and choose "
              "where it goes by evidence.", sm=True)]),
        H("indigo", "Sources: Wikipedia, Famine, Affluence, and Morality; Wikipedia, Effective altruism."),
    ]),

    S("GiveWell", "GiveWell: rating charities by cost per life saved", [
        B("GiveWell was founded in 2007 by Holden Karnofsky and Elie Hassenfeld, who had worked at a "
          "hedge fund and found that the data they wanted on charities often did not exist. Where "
          "many evaluators looked at overhead ratios, GiveWell estimates how much good a donation "
          "does, using published evidence and its own cost-effectiveness models. It argued early on "
          "that charities should spend more on overhead if that paid for tracking results."),
        TC([ST([C("2007", "GiveWell founded", "cyan", "Wikipedia, GiveWell"),
                C("US$39 m", "rapid response grants in 2025 after USAID cuts", "green",
                  "Wikipedia, GiveWell")], cols=1)],
           [BL(["Recommends a small number of top charities working in low-income countries.",
                "Publishes its models and reasoning so others can check them.",
                "Leif Wenar, a philosopher, has criticised it for not taking enough account of harms "
                "caused by recommended charities.",
                "Overhead is treated as a cost like any other, judged by what it buys."])]),
        H("amber", "Compare this with " + L("cost-effectiveness.html", "Cost Effectiveness 101") +
          ", which teaches the same arithmetic for programme choices."),
    ]),

    S("Top charities", "GiveWell's top charities, September 2025", [
        B("GiveWell lists four top charities. For each it gives a unit cost and an estimated average "
          "cost per life saved for the funding it directed in 2022&ndash;2024. These are model "
          "estimates with wide uncertainty. All four programmes work in sub-Saharan Africa or similar "
          "settings, where child mortality from malaria and vaccine-preventable disease is high."),
        T(["Charity and programme", "Unit cost", "Estimated cost per life saved"],
          [["Malaria Consortium: seasonal malaria chemoprevention", "About US$7 per child protected", "US$4,000"],
           ["Against Malaria Foundation: insecticide-treated nets", "About US$6 per net", "US$5,500"],
           ["Helen Keller Intl: vitamin A supplements", "About US$2 per child per year", "US$3,500"],
           ["New Incentives: cash for routine childhood vaccines (Nigeria)", "About US$146 per infant vaccinated", "US$4,500"]]),
        H("cyan", "Source: " + GW + ". Figures are averages for funding directed 2022&ndash;2024."),
    ], compact=True),

    S("Reading the numbers", "What \"cost per life saved\" does and does not tell you", [
        B("A figure such as US$4,000 per life saved is the output of a model. It combines the effect "
          "size from trials, local disease burden, coverage, costs and adjustments for what would "
          "have happened anyway. Change any input and the figure moves. Its value lies in comparing "
          "options on the same method, and its main danger is false precision."),
        TC([P("green", "What it tells you",
              "Which of several health programmes, assessed the same way, is likely to avert more "
              "deaths per dollar in a particular setting.")],
           [P("red", "What it leaves out",
              "Outcomes that are hard to count, such as rights, dignity, voice or institutional "
              "change. Long-run effects on the state. Benefits outside health.")]),
        BL(["Ask which inputs drive the result most (a sensitivity analysis).",
            "Ask whether the estimate travels: a malaria figure from the Sahel tells you little about "
            "a district in Odisha without local data.",
            "Ask who chose the outcome being counted."]),
    ]),

    S("Critiques", "Five criticisms of effective altruism", [
        B("Effective altruism attracted strong criticism as it grew, and more after the collapse of "
          "the FTX cryptocurrency exchange, whose founder Sam Bankman-Fried had been a major funder of "
          "the movement. The criticisms below are drawn from the published debate summarised in "
          "Wikipedia's articles on effective altruism and on GiveWell."),
        TC([BL(["<strong>Incrementalism:</strong> it favours fixable, measurable interventions over "
                "systemic or political change.",
                "<strong>Elitism:</strong> Ken Berger and Robert Penna of Charity Navigator called the "
                "ranking of causes \"elitist\".",
                "<strong>Uncounted harms:</strong> Leif Wenar argues GiveWell does not take enough "
                "account of harms caused by the charities it recommends."])],
           [BL(["<strong>Concentration:</strong> a few very large donors, such as Dustin Moskovitz, "
                "provide much of the movement's money.",
                "<strong>Longtermism:</strong> later books, such as Toby Ord's The Precipice (2020), "
                "turned toward risks to future generations, which raises the question of how much "
                "attention stays on present poverty."])]),
        H("amber", "Cost-effectiveness remains a useful tool. These criticisms are reasons to use it "
          "beside participation and judgement."),
    ]),

    S("In South Asia", "Using effective-giving ideas in South Asia", [
        B("Effective-giving thinking has a role in India, but it needs local inputs. Unit costs, "
          "disease burden and existing public provision differ sharply from the settings GiveWell "
          "models. A programme that is cost-effective in a country with weak public health systems "
          "may duplicate a functioning state scheme in another."),
        TC([P("cyan", "Useful habits",
              "Compare at least two ways of reaching the same goal. Price them with local costs. "
              "Count the counterfactual: what the state or the market would have done anyway. "
              "Publish the reasoning.")],
           [P("amber", "Local cautions",
              "Check overlap with public schemes such as the National Health Mission or nutrition "
              "programmes. Ask whether the funding builds or bypasses public systems. Include "
              "outcomes that matter to the community, even when they are hard to measure.")]),
        H("indigo", "Illustrative: a funder comparing two adolescent anaemia projects in Jharkhand "
          "should cost both with Jharkhand prices and current public supplementation coverage, "
          "before borrowing any global figure."),
    ]),

    S("Two cultures", "Effective altruism and trust-based philanthropy compared", [
        B("Two approaches dominate current debate among funders. Effective altruism asks the funder "
          "to decide carefully where money does most good. Trust-based philanthropy asks the funder to "
          "hand more decisions to the people doing the work. They answer different questions, and a "
          "thoughtful funder can borrow from both."),
        T(["", "Effective altruism", "Trust-based philanthropy"],
          [["Starting question", "Where does a dollar do the most good?", "How can funders share power with grantees?"],
           ["Who decides", "Funder, using evidence", "Grantee, with funder support"],
           ["Funding type", "Often restricted to a specific programme", "Multi-year, unrestricted"],
           ["Evidence", "Trials and cost-effectiveness models", "Grantee knowledge and feedback"],
           ["Main risk", "Ignores what cannot be counted", "Weak accountability for results"]]),
        H("green", "Section 10 turns to trust-based philanthropy and the wider question of power in "
          "funding."),
    ], compact=True),
]

SEC10 = [
    DIV("10", "Ten", "Power, trust and localisation"),

    S("Power in a grant", "Who holds power in a funding relationship", [
        B("Every grant is a relationship between unequal parties. The funder decides whether to fund, "
          "for how long, on what terms and with what reporting. The grantee holds knowledge of the "
          "community and the work, but can be replaced. That imbalance shapes behaviour on both sides: "
          "grantees tell funders what they want to hear, and funders mistake compliance for results."),
        TC([P("indigo", "Funder holds",
              "Money, timing, renewal, the choice of indicators, the reporting template and the power "
              "to walk away. Often also the public story about the work.")],
           [P("green", "Grantee holds",
              "Relationships with communities, local knowledge, staff who stay, and the practical "
              "judgement of what will work in a particular block or ward.")]),
        H("amber", "A useful test: who can end the relationship at short notice without cost to "
          "themselves? In most grants it is the funder alone."),
    ]),

    S("Trust-based philanthropy", "Trust-based philanthropy: the idea", [
        B("Trust-based philanthropy was first set out in 2014 by the Whitman Institute in San "
          "Francisco, which had argued for years that grantees should hold more decision-making "
          "power. The approach aims to shift the imbalance between funders and nonprofit leaders "
          "toward trust, shared power and mutual accountability. It spread quickly during the "
          "COVID-19 pandemic, when many funders relaxed reporting and converted restricted grants to "
          "general support."),
        TC([TERM("Trust-based philanthropy",
                 "An approach that treats grantees as partners pursuing their own goals, reduces the "
                 "burdens funders impose, and gives grantees more say over how money is used "
                 "(Wikipedia, Trust-based philanthropy).")],
           [BL(["More than 800 organisations signed a pledge to adopt trust-based practices.",
                "Critics include the Philanthropy Roundtable, which rejects the focus on power.",
                "The hardest problem is keeping meaningful measurement while cutting reporting."])]),
        H("cyan", "Sources: Wikipedia, Trust-based philanthropy; Trust-Based Philanthropy Project."),
    ]),

    S("Six practices", "The six practices of trust-based grantmaking", [
        B("The Trust-Based Philanthropy Project turns the idea into six practical steps for funders. "
          "Each one moves a burden from the grantee to the funder. Read them as a checklist you can "
          "hold up to any funder, including an Indian CSR team or a family foundation."),
        T(["Practice", "What it asks of the funder"],
          [["Give multi-year, unrestricted funding", "Let grantees decide where money is most needed"],
           ["Do the homework", "Get to know prospective grantees before asking for proposals"],
           ["Simplify paperwork", "Shorter applications and reports focused on dialogue"],
           ["Be transparent and responsive", "Open, honest communication about decisions"],
           ["Solicit and act on feedback", "Ask grantees and communities what to change, and change it"],
           ["Offer support beyond the cheque", "Leadership, networks and organisational support"]]),
        H("green", "Source: Trust-Based Philanthropy Project, Six Practices of Trust-Based "
          "Grantmaking, accessed October 2026."),
    ], compact=True),

    S("Restricted and unrestricted", "Restricted and unrestricted money", [
        B("Restricted grants pay only for named activities. Unrestricted grants pay for whatever the "
          "organisation judges most needed, including salaries, systems, reserves and new ideas. Most "
          "Indian NGOs live on restricted project money, with overheads squeezed by funders and, for "
          "foreign funds, by the 20 per cent cap on administrative expenses in s8 of the FCRA."),
        TC([P("red", "When money is all restricted",
              "No reserves, so one late payment stops work. Finance and monitoring staff are "
              "underpaid. Staff move between projects as grants end. Organisations cannot invest "
              "in learning.")],
           [P("green", "When some money is unrestricted",
              "Reserves bridge gaps. Systems for data and finance improve. Organisations can respond "
              "to a flood or a policy change without waiting for a new grant.")]),
        H("amber", "Illustrative: an NGO with a &#8377;2 crore budget and no unrestricted income "
          "cannot cover a three-month funding delay from any source. A reserve of &#8377;50 lakh "
          "would cover it."),
    ]),

    S("Grand Bargain", "The Grand Bargain of 2016", [
        B("At the World Humanitarian Summit in Istanbul in May 2016, some of the largest donors and "
          "humanitarian organisations agreed the Grand Bargain, a set of 51 commitments to get more "
          "means into the hands of people in need and make humanitarian action more efficient. First "
          "conceived as a deal between the five biggest donors and the six largest UN agencies, it "
          "now has 71 signatories. One commitment became the centre of the localisation debate."),
        TERM("The localisation target",
             "Signatories committed to achieve by 2020 a global, aggregated target of at least 25 per "
             "cent of humanitarian funding to local and national responders as directly as possible "
             "(Grand Bargain, May 2016, commitment 2.4)."),
        TC([BL(["A review in 2021 led to Grand Bargain 2.0.",
                "In June 2023 the signatories endorsed a further iteration."])],
           [BL(["Its focus: quality funding, localisation and participation of affected people.",
                "Signatories also committed to multi-year investment in the capacities of local "
                "and national responders."])]),
        H("cyan", "Sources: IASC, About the Grand Bargain, accessed October 2026; Grand Bargain "
          "document, May 2016."),
    ]),

    S("Target and reality", "Localisation: the 25 per cent target and the 5 per cent reality", [
        B("Nine years after the Grand Bargain, the target remains far away. The Global Humanitarian "
          "Assistance Report 2026 found that local and national actors received only 5 per cent of "
          "humanitarian funding as first-tier recipients in 2025, US$1.2 billion. Localised funding "
          "fell in volume by 27 per cent, faster than funding overall. Counting money passed on "
          "through intermediaries as well, 8.7 per cent reached local and national actors, down "
          "from 9.5 per cent in 2024."),
        TC([BAR("apLocal", "Direct funding to local and national actors, % of humanitarian funding", GHA,
                ["Grand Bargain target (2020)", "Reported, 2025"], "%", [25, 5], ["#10B981", "#EF4444"],
                ytitle="% of funding")],
           [B("Indirect funding passed on through intermediaries added US$1.3 billion, much of it "
              "from UNHCR and UNICEF.", sm=True),
            H("red", "The gap is partly a counting problem: money passed down through several layers "
              "is hard to trace. It is also a power problem: intermediaries keep control.")], ratio="a32"),
    ]),

    S("India's constraint", "Localisation in India and the FCRA", [
        B("Localisation asks international organisations to pass money and decisions to local ones. "
          "In India, since 2020, s7 of the FCRA forbids a registered organisation from transferring "
          "foreign contributions to any other person. An international NGO's Indian office with "
          "foreign funds cannot sub-grant them to a district-level partner, even one with its own "
          "FCRA registration."),
        TC([P("amber", "Consequences",
              "Foreign funders must contract each Indian organisation directly, which favours larger "
              "NGOs able to hold FCRA registration, manage an SBI New Delhi account and meet "
              "compliance. Small community groups are cut off from foreign money.")],
           [P("green", "Responses",
              "Direct grants from foreign funders to more partners; Indian intermediaries using "
              "domestic money for sub-grants; more domestic philanthropy and CSR. In <em>Noel "
              "Harper</em> (2022) the Supreme Court suggested NGOs look to domestic donors.")]),
        H("indigo", "Domestic philanthropy and CSR therefore matter for localisation in India. They are "
          "the funds that can still flow to small local organisations."),
    ]),

    S("Decolonising aid", "Who sets the agenda?", [
        B("The localisation debate is part of a wider critique. Writers on decolonising development "
          "argue that aid often keeps decisions, knowledge and money in the Global North and in "
          "capital cities, while the risks of failure sit with communities. The questions apply to "
          "Indian funders working in other states as much as to foreign donors."),
        TC([BL(["Whose definition of the problem is used in the proposal?",
                "Who owns the data collected from communities?",
                "Who is named as the author of the report?"])],
           [BL(["What share of the budget is spent in the place the work happens?",
                "Who decides when the programme ends?",
                "Are local staff paid on the same scale as staff from elsewhere?"])]),
        H("cyan", "Go further with " + L("decolonize-dev.html", "Decolonial Development 101") + " and " +
          L("participatory-methods.html", "Participatory Methods 101") + "."),
    ]),
]

SEC11 = [
    DIV("11", "Eleven", "Putting it to work"),

    S("Reading a funder", "Six questions to ask about any funder", [
        B("Before you apply, or before you accept, read the funder as carefully as it will read you. "
          "The questions below work for a bilateral agency, a foundation, a company's CSR team or a "
          "wealthy family. Most answers are in public documents if you look."),
        T(["Question", "Where to look", "Warning sign"],
          [["Where does its money come from?", "Annual report, CSR policy, government budget", "Source is unstable or contested"],
           ["What does it fund, and for how long?", "Grants list, past annual reports", "Mostly one-year grants"],
           ["Who decides?", "Board, committee, programme staff", "Decisions sit far from the work"],
           ["What does it ask in return?", "Grant agreement template", "Heavy reporting for small sums"],
           ["How did it behave in 2020 and 2025?", "News, peers, its own statements", "Abrupt exits without notice"],
           ["Does it fund overhead?", "Budget guidelines", "Overhead capped far below real cost"]]),
        H("green", "Ask two current grantees what working with the funder is like. Their answer is "
          "worth more than the website."),
    ], compact=True),

    S("Sources", "Where to find information on Indian and foreign funders", [
        B("Indian law and global reporting standards make a good deal of funder information public. "
          "A few hours with these sources can tell you a funder's size, priorities and stability "
          "before your first meeting."),
        TC([BL(["<strong>CSR:</strong> the company's CSR policy on its website (s135(4)) and its "
                "annual report on CSR, which must explain any unspent amount.",
                "<strong>MCA data:</strong> CSR spending by state and sector on data.gov.in.",
                "<strong>Foreign funders:</strong> OECD aid data and the funder's country strategy."])],
           [BL(["<strong>Foundations:</strong> annual reports and grants lists; for US foundations, "
                "public tax filings.",
                "<strong>Philanthropy research:</strong> the India Philanthropy Report (Bain and "
                "Dasra), published each year.",
                "<strong>Your own records:</strong> how the funder paid, reported and communicated in "
                "past grants."])]),
        H("indigo", "Keep a one-page funder profile for each, updated yearly. It saves weeks when a "
          "call for proposals opens."),
    ]),

    S("Assessing an offer", "A decision table for a grant offer", [
        B("When an offer arrives, read the terms before the amount. Seven terms decide whether a grant "
          "strengthens or drains an organisation. The table gives a simple green, amber and red test "
          "for each, which you can use in a board discussion."),
        T(["Term", "Green", "Amber", "Red"],
          [["Duration", "3 years or more", "2 years", "Under 1 year, renewable"],
           ["Restriction", "Unrestricted or broad", "Programme budget with flexibility", "Line items, no changes"],
           ["Overhead", "Real cost covered", "Fixed rate below cost", "None allowed"],
           ["Reporting", "Annual, narrative plus key data", "Quarterly", "Monthly, custom indicators"],
           ["Data and IP", "Shared ownership", "Funder use with consent", "Funder owns all data"],
           ["Exit", "Notice and transition support", "Notice only", "Termination at will"],
           ["Payment", "In advance", "Quarterly in advance", "In arrears"]]),
        H("amber", "Two or more reds is a reason to negotiate. Under-priced overhead and payment in "
          "arrears together can turn a large grant into a loss."),
    ], compact=True),

    S("Worked example", "Worked example: a CSR grant (Illustrative)", [
        B("<strong>Illustrative.</strong> A manufacturing company had average net profits of "
          "&#8377;300 crore over the last three financial years, so its CSR obligation is &#8377;6 "
          "crore (2 per cent, s135(5)). It offers your NGO &#8377;1.2 crore over two years for "
          "girls' secondary education in two districts near its plant."),
        TC([BL(["<strong>Eligibility:</strong> education falls under Schedule VII item (ii).",
                "<strong>Local preference:</strong> districts near the plant meet the proviso to "
                "s135(5).",
                "<strong>Implementing agency:</strong> your organisation must be registered with the "
                "MCA for CSR and have a track record of at least three years (CSR Rules, rule 4)."])],
           [BL(["<strong>Two years:</strong> this is an ongoing project. Unspent money at year-end "
                "goes to the company's Unspent CSR Account within 30 days (s135(6)).",
                "<strong>Impact assessment:</strong> not mandatory, because the company's average "
                "obligation is below &#8377;10 crore (rule 8(3)).",
                "<strong>Negotiate:</strong> overhead, a payment schedule in advance, and data "
                "ownership."])]),
        H("green", "Ask the company for its approved CSR policy and annual action plan. A grant outside "
          "the plan may be delayed while the Board revises it."),
    ]),

    S("Worked example", "Worked example: a foreign grant under the FCRA (Illustrative)", [
        B("<strong>Illustrative.</strong> A European foundation offers your FCRA-registered NGO "
          "&#8377;1 crore over one year for a livelihoods programme run with three community-based "
          "organisations in Assam. Plan the budget against the FCRA before you sign."),
        FL(["RECEIVE: only in the FCRA Account at the notified SBI branch, New Delhi (s17)",
            "BUDGET: administrative expenses at most &#8377;20 lakh, 20 per cent (s8(1))",
            "PARTNERS: no transfer of foreign funds to the three CBOs (s7)",
            "REDESIGN: pay CBO members' costs directly, or fund CBOs from domestic money"]),
        TC([B("<strong>Option A:</strong> your staff deliver directly, paying vendors and participants "
              "from your FCRA accounts. The CBOs advise but receive no foreign funds.", sm=True)],
           [B("<strong>Option B:</strong> the foundation funds each CBO directly, if they have their "
              "own FCRA registration; or a domestic donor funds the CBOs' share.", sm=True)]),
        H("red", "Check how the FCRA Rules define administrative expenses before you set salaries, "
          "and record the reasoning in your budget notes."),
    ]),

    S("Checklist", "Ten checks before you sign", [
        B("Run through this list with your finance lead and a board member before signing any grant "
          "agreement. Each item has caused real problems for organisations that skipped it."),
        TC([BL(["Is the activity eligible under the funder's rules: Schedule VII for CSR, the "
                "purpose of your FCRA registration for foreign funds?",
                "Does the money arrive in the right account?",
                "Is overhead priced at real cost, and within the 20 per cent FCRA cap if foreign?",
                "Are payments in advance, and what happens if they are late?",
                "Who owns the data, and does consent cover the funder's use under the DPDP Act 2023?"])],
           [BL(["Can you change budget lines without fresh approval?",
                "What notice does either side give to end the grant?",
                "Are reporting demands proportional to the amount?",
                "Does the grant depend on sub-granting that the FCRA forbids?",
                "Does accepting it make one funder more than half your income?"])]),
        H("indigo", "Keep the completed checklist with the signed agreement. It is your record of "
          "what you knew when you said yes. See " +
          L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101") + "."),
    ]),

    S("Summary", "Ten points to take away", [
        B("Each point connects to a decision you will make when you design, fund or run development "
          "work. Facts are stated as of October 2026; check for later amendments and new data."),
        BL(["ODA is official, developmental and concessional, measured since 2019 by grant equivalent.",
            "Only four DAC donors exceeded 0.7 per cent of GNI in 2025; the DAC gave 0.26 per cent.",
            "Aid fell 23.1 per cent in 2025, the largest drop on record, led by the US (&minus;56.9 per cent).",
            "Sachs, Easterly and Moyo disagree about why aid fails; the macro evidence is fragile.",
            "India receives aid worth 0.07 per cent of GNI and has extended US$32 billion in lines of credit.",
            "CSR under s135: 2 per cent of average net profit, Schedule VII activities, unspent rules.",
            "FCRA 2020: no transfer (s7), 20 per cent admin cap (s8), SBI New Delhi account (s17).",
            "Income-tax Act 2025, s133, governs donation deductions from 1 April 2026.",
            "Cost per life saved is a model; use it with local data and judgement.",
            "Localisation lags: 5 per cent direct to local actors in 2025 against a 25 per cent target."]),
        H("cyan", "Re-check the OECD figures when final 2025 data are released in December 2026."),
    ]),

    S("Where next", "Where next: related courses", [
        B("Aid and philanthropy connect to most other courses in the ImpactMojo 101 Series. These are "
          "the most direct next steps, chosen to deepen the finance, law, evidence and power "
          "questions raised in this deck."),
        TC([BL(["Money for development at scale: " + L("development-finance.html", "Development Finance 101"),
                "Company giving and reporting: " + L("csr-esg.html", "CSR &amp; ESG 101"),
                "Raising money for your organisation: " + L("fundraising-basics.html", "Fundraising Basics 101"),
                "Comparing options per rupee: " + L("cost-effectiveness.html", "Cost Effectiveness 101"),
                "Global institutions and rules: " + L("dev-architecture.html", "Global Development Governance 101")])],
           [BL(["Testing what works: " + L("impact-eval.html", "Impact Evaluation 101"),
                "Who sets the agenda: " + L("decolonize-dev.html", "Decolonial Development 101"),
                "Interests behind aid decisions: " + L("pol-economy.html", "Political Economy 101"),
                "Designing fundable programmes: " + L("programme-design.html", "Programme Design 101"),
                "Monitoring for funders and for learning: " + L("mel-basics.html", "MEL Basics 101")])]),
        H("green", "All courses are free. Start with Development Finance 101 for the money, or "
          "Fundraising Basics 101 if you are writing a proposal this month."),
    ]),
]

DECK = {
    "slug": "aid-philanthropy",
    "title": "Aid &amp; Philanthropy 101",
    "description": ("Aid & Philanthropy 101: a free foundational course for development practitioners "
                    "in South Asia. The OECD definition of ODA and the grant-equivalent measure, the "
                    "0.7% target and who meets it, the Sachs, Easterly and Moyo debate, the Paris, "
                    "Accra and Busan agenda, the 2025 aid cuts, aid to South Asia, India as a "
                    "development partner, CSR under section 135, the FCRA 2010 and its 2020 amendment, "
                    "section 133 of the Income-tax Act 2025, effective altruism and GiveWell, "
                    "trust-based philanthropy, the Grand Bargain and a practitioner's toolkit for "
                    "reading funders and grants. ImpactMojo, CC BY-NC-ND."),
    "slides": [
        {"type": "title",
         "main": "Aid<br>&amp; Philanthropy<br>101",
         "sub": "Who pays for development, on what terms, and what changed in 2025: a foundational "
                "course on official aid, Indian philanthropy and funding law for practitioners in "
                "South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "ODA to CSR"]},

        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "What counts as aid"},
             {"name": "How aid moves"},
             {"name": "The great aid debate"},
             {"name": "The aid effectiveness agenda"},
             {"name": "The 2025 aid cuts"},
             {"name": "Aid to South Asia"},
             {"name": "India as a development partner"},
             {"name": "Philanthropy in India: money and law"},
             {"name": "Effective altruism and its critics"},
             {"name": "Power, trust and localisation"},
             {"name": "Putting it to work"},
         ]},
    ] + SEC1 + SEC2 + SEC3 + SEC4 + SEC5 + SEC6 + SEC7 + SEC8 + SEC9 + SEC10 + SEC11 + [
        {"type": "end",
         "eyebrow": "Aid &amp; Philanthropy 101 &middot; Complete",
         "headline": "Read the terms,<br>then follow the money",
         "byline": "Aid budgets fell sharply in 2025 and Indian philanthropy is growing under tight "
                   "law. Know where each rupee comes from, what it allows, and who decides. Explore "
                   "the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

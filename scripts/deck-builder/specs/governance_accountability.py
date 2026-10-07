# -*- coding: utf-8 -*-
"""
Governance & Accountability 101: ImpactMojo 101 Series (native deck spec)
How power is checked and services are delivered, for development practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py governance_accountability

Sources opened while writing (October 2026):
- World Bank, Worldwide Governance Indicators (2026 release), home and documentation pages:
  https://www.worldbank.org/en/publication/worldwide-governance-indicators
  https://www.worldbank.org/en/publication/worldwide-governance-indicators/documentation
- O'Donnell, Horizontal Accountability in New Democracies, Journal of Democracy 9(3), July 1998, 112-26:
  https://www.journalofdemocracy.org/articles/horizontal-accountability-in-new-democracies/
  text: https://www.democraziapura.it/wp-content/uploads/2015/10/1998-ODonnell.pdf
- Smulovitz and Peruzzotti, Societal Accountability in Latin America, Journal of Democracy 11(4), 2000:
  https://www.journalofdemocracy.org/articles/societal-accountability-in-latin-america/
- World Bank, World Development Report 2004, Making Services Work for Poor People (full text):
  https://documents.worldbank.org/curated/en/832891468338681960/text/268950WDR00PUB0ces0work0poor0people.txt
- Chaudhury, Hammer, Kremer, Muralidharan and Rogers (2006), JEP 20(1): 91-116:
  https://ideas.repec.org/a/aea/jecper/v20y2006i1p91-116.html
- Muralidharan, Das, Holla and Mohpal (2017), JPubE 145: 116-135:
  https://ideas.repec.org/a/eee/pubeco/v145y2017icp116-135.html
- Muralidharan, Niehaus and Sukhtankar (2016), AER 106(10): 2895-2929:
  https://ideas.repec.org/a/aea/aecrev/v106y2016i10p2895-2929.html
- Banerjee, Duflo, Imbert, Mathew and Pande (2020), AEJ Applied 12(4): 39-72:
  https://ideas.repec.org/a/aea/aejapp/v12y2020i4p39-72.html
- Muralidharan, Niehaus and Sukhtankar, NBER WP 26744 (2020): https://ideas.repec.org/p/nbr/nberwo/26744.html
  and https://www.nber.org/papers/w26744
- Muralidharan, Niehaus, Sukhtankar and Weaver (2021), AEJ Applied 13(2): 52-82:
  https://ideas.repec.org/a/aea/aejapp/v13y2021i2p52-82.html
- Bjorkman and Svensson (2009), QJE 124(2): 735-769: https://ideas.repec.org/a/oup/qjecon/v124y2009i2p735-769..html
- Banerjee, Banerji, Duflo, Glennerster and Khemani (2010), AEJ Policy 2(1): 1-30:
  https://ideas.repec.org/a/aea/aejpol/v2y2010i1p1-30.html
- Olken (2007), JPE 115(2): 200-249: https://ideas.repec.org/a/ucp/jpolec/v115y2007p200-249.html
- Ferraz and Finan (2008), QJE 123(2): 703-745: https://ideas.repec.org/a/oup/qjecon/v123y2008i2p703-745..html
- Chattopadhyay and Duflo (2004), Econometrica 72(5): 1409-1443:
  https://ideas.repec.org/a/ecm/emetrp/v72y2004i5p1409-1443.html
- Kapur (2020), JEP 34(1): 31-54: https://ideas.repec.org/a/aea/jecper/v34y2020i1p31-54.html
- Pritchett (2009), Is India a Flailing State?, HKS RWP09-013: https://ideas.repec.org/p/ecl/harjfk/rwp09-013.html
- Pritchett, Woolcock and Andrews (2010), Capability Traps?, CGD WP 234: https://ideas.repec.org/p/cgd/wpaper/234.html
- Andrews, Pritchett and Woolcock (2013), World Development 51: 234-244:
  https://ideas.repec.org/a/eee/wdevel/v51y2013icp234-244.html
- Muralidharan, Accelerating India's Development (India Viking, February 2024), publisher's description:
  https://www.penguin.co.in/book/accelerating-indias-development/
- Transparency International CPI 2025 country pages: https://www.transparency.org/en/countries/india (and
  bangladesh, pakistan, nepal, sri-lanka, bhutan)
- Global Corruption Barometer Asia 2020, as summarised by Asia Pacific Foundation of Canada:
  https://www.asiapacific.ca/asia-watch/corruption-rise-asia-survey and TI media advisory:
  https://www.transparency.org/en/press/media-advisory-asia-corruption-survey-to-be-released-on-24-november
- Right to Information Act 2005, CIC copy: https://cic.gov.in/sites/default/files/RTI-Act_English.pdf
- PRS, RTI (Amendment) Bill 2019: https://prsindia.org/billtrack/the-right-to-information-amendment-bill-2019
- SCC Online, RTI term of office rules, notification of 24 October 2019:
  https://www.scconline.com/blog/post/2019/10/25/right-to-information-term-of-office-salaries-allowances-and-other-terms-and-conditions-of-service-of-chief-information-commissioner-information-commissioners-in-the-central-information-commission/
- Digital Personal Data Protection Act 2023 (No. 22 of 2023), Gazette of 11 August 2023, s44(3):
  https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- MeitY, G.S.R. 843(E), 13 November 2025 (commencement of the DPDP Act in stages; s44(3) from publication,
  ss 3-17 after eighteen months): https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf
- DPDP Rules 2025, G.S.R. 846(E), 13 November 2025, rule 1 (phased commencement)
- RTI Online FAQ (BPL fee exemption, RTI Rules 2012): https://rtionline.gov.in/faq.php
- Satark Nagrik Sangathan, Report Card of Information Commissions, press release October 2025:
  https://www.snsindia.org/wp-content/uploads/2025/10/Press-Release-2025.pdf
- Global Freedom of Expression, CPIO Supreme Court v Subhash Chandra Agarwal (2019):
  https://globalfreedomofexpression.columbia.edu/cases/central-public-information-officer-supreme-court-of-india-v-subhash-chandra-agarwal
- Supreme Court Observer, ADR v Union of India (electoral bonds), 2024 INSC 113:
  https://www.scobserver.in/cases/association-for-democratic-reforms-electoral-bonds-case-background/
- Centre for Law and Democracy, RTI Rating country pages: https://www.rti-rating.org/country-data/
- VB-G RAM G Act 2025 (Act No. 36 of 2025), ss 19, 20, 24, 25, 33, 37:
  https://www.indiacode.nic.in/bitstream/123456789/22478/1/a2025-36.pdf
- Wikipedia, Social audit (SSAAT, May 2009): https://en.wikipedia.org/wiki/Social_audit
- Singh and Vutukuru, Enhancing Accountability in Public Service Delivery through Social Audits: A case study
  of Andhra Pradesh (HKS policy analysis), quoting NREGA s17 and dating the 2006 pilot and mass audit:
  http://www.copasah.org/uploads/1/2/6/4/12642634/enhancing_accountability_in_public_service_delivery_through_social_audits-a_case_study_of_andhra_pradesh_india.pdf
- Constitution of India, Articles 243D, 243G, 243I, 243J, 243W, 243Y (advocatekhoj bare act pages) and
  Articles 148-151 (constitutionofindia.net); Wikipedia, Panchayati raj in India; Municipal governance in India
- RBI, Finances of Panchayati Raj Institutions, 24 January 2024: https://rbi.org.in/ScriptS/PublicationsView.aspx?id=22404
  press release https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=57182 and Chapter II, Table II.4
- Down To Earth, 1 February 2021, Fifteenth Finance Commission grants to local governments:
  https://www.downtoearth.org.in/governance/fifteenth-finance-commission-over-rs-4-36-lakh-crore-for-local-governments-75296
- DMEO / Planning Commission, Decentralized Planning Experience in Kerala:
  https://dmeo.gov.in/sites/default/files/2019-10/Decentralized%20Planning%20Experience%20in%20Kerala.pdf
- Nepal, Ministry of Federal Affairs and General Administration, list of local levels (753 entries):
  https://mofaga.gov.np/local-contact?visible=753
- Constitution of Pakistan, Article 140A: https://www.pakistani.org/pakistan/constitution/part4.ch3.html
- Lokpal and Lokayuktas Act 2013, ss 3, 14, 63: https://www.legalauthority.in/bare-act/lokpal-and-lokayuktas-act-2013
- PIB, President's Secretariat, 23 March 2019 (oath to Justice P.C. Ghose): https://www.pib.gov.in/PressReleasePage.aspx?PRID=1569295
- PIB, President's Secretariat, 10 March 2024 (oath to Justice A.M. Khanwilkar): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2013271
- PIB, 12 December 2024, Lok Sabha answer on the Whistle Blowers Protection Act 2014:
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=2083815
- Press reports (Tribune, NDTV, 27 February 2024) on the acting arrangement after 27 May 2022
- Wikipedia, Prevention of Corruption Act 1988 (2018 amendment, bribe giving, s9): https://en.wikipedia.org/wiki/Prevention_of_Corruption_Act,_1988
- Wikipedia, Public Accounts Committee (India): https://en.wikipedia.org/wiki/Public_Accounts_Committee_(India)
- PRS, Prevention of Corruption (Amendment) Bill 2013: https://prsindia.org/billtrack/the-prevention-of-corruption-amendment-bill-2013
- Supreme Court of India, CPIL v Union of India, WP(C) 1373 of 2018, 2026 INSC 55, 13 January 2026 (judgment text,
  including at para 109 of Nagarathna J the Lokpal Act's assent on 1 January 2014):
  https://api.sci.gov.in/supremecourt/2018/40618/40618_2018_4_1501_67544_Judgement_13-Jan-2026.pdf
- PIB backgrounder on CPGRAMS, 9 August 2026:
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc2026821966201.pdf
- PIB, DBT assessment, 21 April 2025: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/apr/doc2025421543301.pdf
- Wikipedia, Right to Public Services legislation: https://en.wikipedia.org/wiki/Right_to_Public_Services_legislation
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


RTI = "Right to Information Act 2005"
WDR = "World Bank, World Development Report 2004"
SNS = "Satark Nagrik Sangathan, Report Card of Information Commissions, October 2025"
CPI = "Transparency International, Corruption Perceptions Index 2025"

DECK = {
    "slug": "governance-accountability",
    "title": "Governance &amp; Accountability 101",
    "description": ("Governance & Accountability 101: a free foundational course for development "
                    "practitioners in South Asia. What governance means and how the World Bank "
                    "measures it, vertical and horizontal accountability, the long and short routes "
                    "of the World Development Report 2004, principal-agent problems, corruption and "
                    "its measurement, the 73rd and 74th Amendments, the RTI Act 2005 and its 2019 and "
                    "2023 amendments, social audit under the VB-G RAM G Act 2025, CPGRAMS, the Lokpal, "
                    "the CAG, DBT, state capacity and the evidence on what improves services. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Governance<br>&amp; Accountability<br>101",
         "sub": "Who answers to whom, and how citizens can make them answer: a foundational "
                "course on governance, transparency and service delivery for development "
                "practitioners in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "RTI to Lokpal"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "What governance means"},
             {"name": "The accountability relationship"},
             {"name": "Principals, agents and absent providers"},
             {"name": "Corruption and how to measure it"},
             {"name": "Decentralisation: funds, functions, functionaries"},
             {"name": "Transparency and the RTI Act"},
             {"name": "Social audit and citizen monitoring"},
             {"name": "Grievances, charters and the Lokpal"},
             {"name": "Audit institutions, e-governance and DBT"},
             {"name": "Putting it to work: a practitioner's toolkit"},
             {"name": "State capacity, evidence and where next"},
         ]},

        # ===================== SECTION 01 =====================
        DIV("01", "One", "What governance means"),

        S("Starting point", "Why a development practitioner needs to think about governance", [
            B("A school with a building, a salaried teacher and a free midday meal can still teach "
              "little if the teacher does not turn up. A ration shop stocked by the state can still "
              "turn away an eligible family if the dealer is never checked. Most failures that "
              "practitioners see in the field are failures of governance: the rules exist and the "
              "money is spent, but the people paid to deliver are not answerable to the people "
              "they serve."),
            TC([P("amber", "Inputs view",
                  "Counts buildings, budgets, staff posts and scheme coverage. Assumes that once "
                  "inputs are in place, services follow. Struggles to explain why two districts "
                  "with the same budget produce very different results.")],
               [P("green", "Governance view",
                  "Asks who decides, who delivers, who checks and what happens when delivery "
                  "fails. Looks at information, incentives and sanctions along the chain from "
                  "citizen to minister to frontline worker.")]),
            H("cyan", "This course takes the governance view and gives you the law, the "
              "frameworks and the evidence to use it in programme design and evaluation."),
        ]),

        S("Definition", "Governance: a working definition from the World Bank", [
            B("The World Bank's Worldwide Governance Indicators (WGI) define governance as "
              "\"the traditions and institutions by which authority in a country is exercised\". "
              "The definition is broad on purpose. It covers how governments are chosen and "
              "replaced, whether they can make and carry out sound policy, and whether citizens "
              "and the state respect the institutions that govern their interactions."),
            TERM("Governance",
                 "The traditions and institutions by which authority is exercised (World Bank, "
                 "WGI). In practice: the rules, organisations and habits that decide who holds "
                 "power, how it is used, and how its holders are checked."),
            TC([B("<strong>Government</strong> is the set of organisations: ministries, "
                  "departments, panchayats, courts.", sm=True)],
               [B("<strong>Governance</strong> is how those organisations, plus citizens, "
                  "parties, media and markets, actually behave together.", sm=True)]),
            H("indigo", "Keep the distinction in mind. A country can have a large government "
              "and weak governance, or a small one that works well."),
        ]),

        S("Measurement", "The six dimensions of the Worldwide Governance Indicators", [
            B("The WGI summarise governance in six composite indicators, published annually for "
              "more than 200 economies from 1996 to 2025 in the 2026 release. Each dimension "
              "combines many underlying survey and expert questions. The descriptions below are "
              "short summaries of what each dimension tries to capture."),
            T(["Dimension", "What it tries to capture", "Illustrative kind of question that feeds it"],
              [["Voice and Accountability", "Whether citizens can choose and criticise their government",
                "Freedom of the press, fairness of elections"],
               ["Political Stability", "Likelihood of violent or unconstitutional disruption",
                "Expert risk ratings of unrest"],
               ["Government Effectiveness", "Quality of public services and the civil service",
                "Firm and household views of service quality"],
               ["Regulatory Quality", "Ability to make and apply sound rules for markets",
                "Firm surveys on the regulatory environment"],
               ["Rule of Law", "Confidence in courts, police, contracts and property",
                "Expert ratings of judicial independence"],
               ["Control of Corruption", "Use of public power for private gain",
                "Survey questions on bribery and capture"]]),
            H("cyan", "Source: World Bank, Worldwide Governance Indicators, 2026 release, project "
              "pages and documentation."),
        ]),

        S("How it is built", "What the WGI numbers are, and what they are not", [
            B("The 2026 WGI draw on perception data from 35 cross-country sources: household "
              "surveys, firm surveys and expert assessments. More than 400 underlying questions "
              "are mapped to the six dimensions, rescaled from 0 to 1, and combined. The release "
              "reports estimates in a standard statistical unit and as scores on a 0&ndash;100 "
              "scale."),
            ST([C("35", "cross-country data sources behind the 2026 WGI", "cyan",
                  "World Bank, WGI documentation, 2026 release"),
                C("400+", "underlying indicators mapped to six dimensions", "indigo",
                  "World Bank, WGI documentation, 2026 release"),
                C("1996&ndash;2025", "years covered, recalculated for consistency", "green",
                  "World Bank, WGI home page, 2026 release")], cols=3),
            H("amber", "The World Bank's own usage advisory says the scores are estimates based on "
              "perceptions, may lag behind reforms, and should not be used as definitive ratings "
              "of government performance."),
        ]),

        S("Using indices critically", "Four reasons to be careful with governance scores", [
            B("Governance indicators are useful for comparing broad patterns across countries and "
              "over long periods. They are a poor guide to what is happening in a particular "
              "district, department or scheme, which is where most practitioners work. Treat them "
              "as a starting question, then go and look."),
            TC([BL(["<strong>Perception:</strong> they record what respondents and experts believe, "
                    "which may reflect news coverage more than conduct.",
                    "<strong>Lag:</strong> the World Bank warns that perceptions may trail actual "
                    "reforms by years."]),],
               [BL(["<strong>Aggregation:</strong> a national score hides wide gaps between states, "
                    "and between districts within a state.",
                    "<strong>Margins of error:</strong> small changes in rank are often inside the "
                    "uncertainty band and mean little."])]),
            H("red", "Never use a national governance score to justify a decision about a single "
              "programme site. Use administrative data, audits and field checks instead."),
        ]),

        S("Debate", "Good governance as an agenda, and its critics", [
            B("From the 1990s, donors began to attach governance conditions to aid: civil service "
              "reform, anti-corruption commissions, transparency laws. Critics argued that the "
              "list of desirable reforms grew longer than any poor country could manage, and that "
              "copying the institutions of rich countries rarely produced their results. Lant "
              "Pritchett, Michael Woolcock and Matt Andrews later called this "
              "<strong>isomorphic mimicry</strong>: adopting the forms of functional states while "
              "the function stays absent (Section 11)."),
            TC([P("green", "What the agenda got right",
                  "Institutions matter for outcomes. Information, checks and sanctions change "
                  "behaviour. Citizens have a stake in how public money is spent.")],
               [P("amber", "What it got wrong",
                  "Long reform lists, transplanted designs and scores treated as targets. Laws "
                  "were passed and agencies created with little attention to whether they could "
                  "work.")]),
            H("indigo", "The lesson for practitioners: judge an institution by what it does in "
              "your district. Its existence on paper proves little."),
        ]),

        S("South Asia stakes", "Why governance questions are sharp in South Asia", [
            B("South Asian states have expanded rights-based entitlements faster than their "
              "capacity to deliver them. India legislated a right to information in 2005 and "
              "guaranteed rural employment, now under the VB-G RAM G Act 2025 with 125 days a year. Nepal rebuilt its whole system of local government under the "
              "2015 Constitution. The gap between what the law promises and what a citizen "
              "receives is where governance lives."),
            T(["Country", "A governance reform to know", "Year"],
              [["India", "Right to Information Act", "2005"],
               ["Bangladesh", "Right to Information Act", "2009"],
               ["Nepal", "Right to Information Act; 753 local levels under the new Constitution", "2007; 2015"],
               ["Sri Lanka", "Right to Information Act, No. 12", "2016"],
               ["Pakistan", "Right of Access to Information Act (federal)", "2017"]]),
            H("cyan", "Sources: Centre for Law and Democracy, RTI Rating country pages; Nepal, Ministry "
              "of Federal Affairs and General Administration, list of local levels. Each of these laws is discussed later in the course."),
        ]),

        # ===================== SECTION 02 =====================
        DIV("02", "Two", "The accountability relationship"),

        S("Core idea", "Accountability has two parts: answerability and enforcement", [
            B("Accountability is a relationship between two parties. One holds power or "
              "resources on behalf of the other. The first must explain and justify what it "
              "did, and the second must be able to impose a consequence if the explanation is "
              "not good enough. Remove either part and what remains is weaker: explanation "
              "without sanction is public relations, sanction without explanation is arbitrary."),
            TERM("Accountability",
                 "A relationship in which one actor must inform and justify its conduct to "
                 "another (answerability), and can face sanctions or rewards for it "
                 "(enforcement)."),
            TC([P("cyan", "Answerability",
                  "Information and justification: annual reports, RTI replies, social audit "
                  "hearings, questions in the legislature, audit reports.")],
               [P("green", "Enforcement",
                  "Consequences: losing an election, a penalty under s20 of the RTI Act, "
                  "disciplinary action, prosecution, recovery of misused funds.")]),
            H("amber", "When you assess an accountability tool, ask both questions: does it produce "
              "information, and can anyone act on it?"),
        ]),

        S("O'Donnell", "Vertical and horizontal accountability", [
            B("The political scientist Guillermo O'Donnell drew a widely used distinction in 1998. "
              "Vertical accountability runs from citizens to rulers, mainly through elections "
              "and a free press. Horizontal accountability runs between state agencies: courts, "
              "auditors, ombudsmen and legislatures checking the executive."),
            Q("[State agencies able] to take actions ranging from routine oversight to criminal "
              "sanctions or impeachment in relation to possibly unlawful actions or omissions by "
              "other agents or agencies of the state.",
              "Guillermo O'Donnell, Horizontal Accountability in New Democracies, Journal of "
              "Democracy 9(3), 1998"),
            TC([B("<strong>Vertical:</strong> elections, a free press, freedom of association. "
                  "Periodic and blunt: a vote judges a whole government once in five years.", sm=True)],
               [B("<strong>Horizontal:</strong> CAG, courts, Lokpal, information commissions, "
                  "legislative committees. Continuous, but only as strong as the agencies' "
                  "independence.", sm=True)]),
            H("indigo", "O'Donnell's own conclusion: horizontal checks depend heavily on vertical "
              "ones, because public opinion is what pushes agencies to act."),
        ]),

        S("A third direction", "Societal or diagonal accountability", [
            B("Catalina Smulovitz and Enrique Peruzzotti (Journal of Democracy, 2000) added "
              "societal accountability: citizens' associations, movements and media that expose "
              "wrongdoing and push horizontal agencies into action between elections. In South "
              "Asia the standard example is the Mazdoor Kisan Shakti Sangathan, which used public "
              "hearings (jan sunwais) against corruption in Rajasthan's public works in the 1990s."),
            T(["Direction", "Who holds whom to account", "South Asian example"],
              [["Vertical", "Voters and citizens hold elected leaders", "Panchayat and assembly elections"],
               ["Horizontal", "State agencies check other state agencies", "CAG reports to Parliament; High Court review"],
               ["Societal / diagonal", "Organised citizens and media trigger or join state checks",
                "MKSS public hearings; social audits under rural employment law"]]),
            H("green", "Most development programmes work in the third direction. Knowing the "
              "first two tells you which levers your community work can pull."),
        ]),

        S("WDR 2004", "The World Development Report 2004 triangle", [
            B("The World Bank's World Development Report 2004, <em>Making Services Work for Poor "
              "People</em>, mapped service delivery as a triangle of citizens or clients, "
              "politicians and policymakers, and providers. It defined four relationships of "
              "accountability, and its vocabulary is still used in most donor governance work."),
            T(["Relationship", "Connects", "Example in an Indian primary health centre"],
              [["Voice", "Citizens to politicians and policymakers", "Voters pressing an MLA about a closed PHC"],
               ["Compact", "Policymakers to provider organisations", "State health department's rules and budget for PHCs"],
               ["Management", "Provider organisations to frontline staff", "District medical officer supervising doctors"],
               ["Client power", "Clients directly to providers", "Patients complaining to, or choosing, a facility"]]),
            H("cyan", "Source: " + WDR + ", glossary and overview."),
        ]),

        S("Two routes", "The long route and the short route", [
            B("In a market, the customer pays the seller and can walk away, so accountability is "
              "direct. For health, education and water, the report notes, society has chosen to "
              "provide the service through government. Citizens must then work through the "
              "<strong>long route</strong>: voice to politicians, who use the compact to steer "
              "providers. The <strong>short route</strong> is client power over providers directly."),
            TC([P("indigo", "Long route",
                  "Citizen &rarr; politician &rarr; department &rarr; provider. Works when "
                  "elections reward service quality and departments can monitor staff. Breaks "
                  "when votes turn on caste, patronage or handouts.")],
               [P("green", "Short route",
                  "Citizen &rarr; provider. Vouchers, school committees, user groups, social "
                  "audits. The report cites Bangladesh's Female Secondary School Assistance "
                  "Program, which paid schools according to the girls they enrolled.")]),
            H("amber", "WDR 2004: when the long route breaks down, \"service delivery fails "
              "(absentee teachers, leaking water pipes)\". Source: " + WDR + ", overview."),
        ]),

        S("A number from the report", "When the long route fails: Bangladesh's absent doctors", [
            B("The report illustrates the failure with a survey of primary health care facilities "
              "in Bangladesh, which found the absentee rate among doctors to be 74 percent. Doctors "
              "posted to remote areas are rarely monitored, so the penalty for absence is low. "
              "The figure is old and should not be read as current; it is useful as a reminder of "
              "how large the gap between posts filled and services delivered can be."),
            ST([C("74%", "absentee rate among doctors in a survey of primary health facilities in "
                  "Bangladesh, cited in the report", "red", WDR + ", chapter 1"),
                C("4", "relationships of accountability in the report's framework", "cyan",
                  WDR + ", glossary")], cols=2),
            TC([B("<strong>What absence tells you:</strong> the compact and management "
                  "relationships are not working, whatever the budget says.", sm=True)],
               [B("<strong>What it does not tell you:</strong> whether better pay, closer "
                  "supervision or community pressure is the right fix. That needs local "
                  "diagnosis.", sm=True)]),
        ]),

        S("Using the framework", "Mapping a failure onto the triangle", [
            B("The triangle is most useful as a diagnostic. Take one service failure and ask "
              "which relationship broke. The answer changes the remedy. A worked example, "
              "labelled Illustrative, follows the chain for a village where the anganwadi centre "
              "is open only two days a week."),
            T(["Question", "Finding (Illustrative)", "Remedy it points to"],
              [["Voice: do residents raise it with elected members?", "Rarely; the ward member is from the dominant hamlet",
                "Gram sabha agenda item; women's group petition"],
               ["Compact: does the department set and fund clear standards?", "Standards exist; supplementary nutrition funds arrive late",
                "Raise release delays with the district programme officer"],
               ["Management: is the worker supervised?", "Supervisor post vacant for a year",
                "Push to fill the post; use the grievance portal"],
               ["Client power: can mothers act directly?", "No forum; workers answer to the block office only",
                "Monthly community meeting with attendance records read aloud"]]),
            H("green", "One failure, four possible breaks. Fixing the wrong one wastes the "
              "programme's effort."),
        ]),

        # ===================== SECTION 03 =====================
        DIV("03", "Three", "Principals, agents and absent providers"),

        S("The model", "The principal-agent problem in one slide", [
            B("Economists describe accountability failures as principal-agent problems. A "
              "principal wants a task done and hires an agent to do it. The agent knows more about "
              "its own effort than the principal does, and may have different goals. Unless the "
              "principal can observe effort or results and reward or sanction them, the agent "
              "can shirk, divert resources or serve someone else."),
            TERM("Principal-agent problem",
                 "A situation where one party (the agent) acts on behalf of another (the "
                 "principal), has private information about its own actions, and has interests "
                 "that differ from the principal's."),
            TC([P("cyan", "Hidden action",
                  "The principal cannot see effort. A health worker reports home visits that "
                  "never happened.")],
               [P("indigo", "Hidden information",
                  "The agent knows something the principal does not. A contractor knows the real "
                  "cost of a road and inflates the estimate.")]),
            H("amber", "Monitoring, incentives and selection of honest agents are the three "
              "standard responses. Each has costs."),
        ]),

        S("A chain of principals", "In government, every agent is also a principal", [
            B("Public service delivery is a chain of principal-agent relationships. Citizens are "
              "principals for legislators, legislators for ministers, ministers for departments, "
              "departments for district officers, and so on down to the teacher or nurse. "
              "Information is lost at every link, and each agent can blame the next one down."),
            FL(["CITIZENS elect legislators",
                "LEGISLATURE passes law and budget",
                "MINISTRY designs schemes",
                "DISTRICT allocates staff and funds",
                "FRONTLINE teacher, nurse, ration dealer"]),
            TC([B("<strong>Long chains dilute accountability.</strong> By the time a complaint about "
                  "a ration shop reaches the state food secretary, it is one line in a monthly "
                  "report.", sm=True)],
               [B("<strong>Short chains help.</strong> Decentralisation and the WDR's short route "
                  "both try to shorten the distance between the citizen and the person who can "
                  "fix the problem.", sm=True)]),
        ]),

        S("Complications", "Why public agents are harder to manage than private ones", [
            B("Textbook principal-agent fixes assume one principal with one clear goal. Public "
              "agencies face several principals with conflicting goals, and tasks that are hard "
              "to measure. These features explain why simple performance pay often disappoints "
              "in government."),
            T(["Feature", "What it means", "Example"],
              [["Multiple principals", "Agents answer to several masters who want different things",
                "A block officer pulled between the collector, the MLA and the department"],
               ["Multitasking", "Rewarding measured tasks draws effort away from unmeasured ones",
                "Teachers paid on test scores may neglect non-tested skills"],
               ["Hard-to-measure output", "Quality of care or teaching is difficult to verify",
                "Immunisations are easy to count; the quality of counselling is hard to verify"],
               ["Weak exit", "Citizens cannot easily switch to another public provider",
                "One ration shop per village"]]),
            H("indigo", "Design accountability around what can be observed, and check that the "
              "measured task is the one that matters."),
        ]),

        S("Evidence", "Missing in action: absence across six countries", [
            B("The clearest evidence of agency problems in service delivery comes from "
              "unannounced visits. Nazmul Chaudhury, Jeffrey Hammer, Michael Kremer, Karthik "
              "Muralidharan and Halsey Rogers sent enumerators to primary schools and health "
              "clinics in Bangladesh, Ecuador, India, Indonesia, Peru and Uganda and recorded "
              "who was present."),
            ST([C("19%", "of teachers absent, averaged across six countries", "amber",
                  "Chaudhury et al., Journal of Economic Perspectives, 2006"),
                C("35%", "of health workers absent, averaged across six countries", "red",
                  "Chaudhury et al., Journal of Economic Perspectives, 2006"),
                C("~1 in 2", "Indian government primary teachers actually teaching when "
                  "enumerators arrived", "indigo",
                  "Chaudhury et al., Journal of Economic Perspectives, 2006")], cols=3),
            H("amber", "In India, one quarter of government primary teachers were absent, and only "
              "about half were teaching. Presence is only the floor; effort needs its own measure."),
        ]),

        S("The cost", "What teacher absence costs India", [
            B("A decade later, Karthik Muralidharan, Jishnu Das, Alaka Holla and Aakash Mohpal "
              "revisited schools in 1,297 villages across India. Inputs had improved a great "
              "deal: buildings, toilets, teacher numbers. Absence had fallen only modestly. "
              "They estimated the salary cost of unauthorised absence and compared two ways of "
              "getting more teaching time."),
            ST([C("23.6%", "of teachers absent during unannounced visits", "red",
                  "Muralidharan, Das, Holla and Mohpal, Journal of Public Economics, 2017"),
                C("$1.5bn", "estimated yearly salary cost of unauthorised teacher absence", "amber",
                  "Muralidharan, Das, Holla and Mohpal, Journal of Public Economics, 2017"),
                C("10&times;+", "more cost-effective, by their estimate: more frequent monitoring versus "
                  "hiring teachers, to raise the effective pupil-teacher ratio", "green",
                  "Muralidharan, Das, Holla and Mohpal, Journal of Public Economics, 2017")], cols=3),
            H("cyan", "The policy point: in a system with weak management, spending on inputs "
              "buys less than spending on accountability."),
        ]),

        S("Responses", "Three ways to close the agency gap", [
            B("Every accountability instrument in this course is a version of one of three "
              "responses to the principal-agent problem. Knowing which one you are using helps "
              "you predict where it will fail."),
            TC([P("cyan", "Monitoring",
                  "Make effort or results visible: inspections, biometric attendance, audits, "
                  "social audits, phone calls to beneficiaries. Fails when the monitor colludes "
                  "or the data are gamed."),
                P("green", "Incentives",
                  "Reward or sanction what is observed: performance pay, transfers, penalties "
                  "under the RTI Act. Fails when the measured task is the wrong one.")],
               [P("indigo", "Selection and motivation",
                  "Recruit and keep people who care about the mission, and protect their "
                  "professional norms. Fails when appointments are sold or politically managed."),
                P("amber", "Voice and exit",
                  "Let citizens complain or switch provider. Fails when the poor lack time, "
                  "literacy or a safe channel to complain.")]),
            H("red", "No single response works everywhere. Most effective systems combine "
              "monitoring with consequences that someone actually applies."),
        ]),

        S("Field caution", "Reading agent behaviour fairly", [
            B("Absence data invite a story of lazy workers. Field researchers find more varied "
              "causes: official duties such as election work and surveys, long travel to remote "
              "postings, unpaid salaries, unfilled posts covered by one person, and rules that "
              "reward paperwork over service. A practitioner who blames frontline staff for a "
              "system failure loses their cooperation and misses the fix."),
            TC([P("red", "Blame the agent",
                  "Shame lists, punitive inspections and public naming. Can raise attendance in "
                  "the short run; often breeds collusion and false records.")],
               [P("green", "Diagnose the system",
                  "Map duties, travel, pay delays and supervision before deciding on sanctions. "
                  "Pair new demands with support such as housing near remote postings or fewer "
                  "non-teaching duties.")]),
            H("cyan", "Talk to frontline workers early in any accountability programme. They know "
              "where the chain breaks above them."),
        ]),

        # ===================== SECTION 04 =====================
        DIV("04", "Four", "Corruption and how to measure it"),

        S("Definitions", "What we mean by corruption", [
            B("A common working definition is the abuse of public office or entrusted power for "
              "private gain. Indian law is narrower and more specific: the Prevention of "
              "Corruption Act 1988 defines specific offences, among them a public servant taking "
              "an undue advantage, criminal misconduct and habitual offending. Development "
              "work meets corruption in several forms, and each calls for a different response."),
            T(["Form", "What it looks like", "Who loses"],
              [["Petty or bureaucratic", "A bribe for a caste certificate, ration card or land record",
                "Poor households, who pay a larger share of income"],
               ["Grand", "Kickbacks on large contracts or allocation of natural resources",
                "Taxpayers and future users of poor infrastructure"],
               ["Leakage", "Fake names on muster rolls, diverted grain, ghost pensioners",
                "Intended beneficiaries who receive less"],
               ["Capture", "Rules written or bent for the benefit of a few firms or families",
                "Competitors and citizens who pay higher prices"]]),
            H("amber", "Coercive bribes (pay or be refused a right) and collusive bribes (pay to "
              "break a rule) need different remedies. Treating both as one problem confuses design."),
        ]),

        S("Indian law", "The Prevention of Corruption Act and the 2018 amendment", [
            B("Under the 1988 Act as first enacted, PRS Legislative Research notes, a bribe giver "
              "was charged with abetment. The Prevention of Corruption (Amendment) Act 2018 (No. 16 "
              "of 2018) treats bribe giving as an offence in its own right and, in section 9, "
              "makes commercial organisations liable for bribes given on their behalf. It also "
              "inserted section 17A, which bars police from inquiring into an offence "
              "relatable to a public servant's official decision or recommendation without "
              "prior approval."),
            TC([P("indigo", "Section 17A",
                  "Prior approval of the competent authority before any inquiry or "
                  "investigation into decisions taken in official functions, with an exception "
                  "for arrest on the spot while accepting an undue advantage.")],
               [P("amber", "Split verdict, January 2026",
                  "In Centre for Public Interest Litigation v Union of India (2026 INSC 55, "
                  "13 January 2026), Justice Nagarathna held s17A unconstitutional; Justice "
                  "Viswanathan upheld it if approval follows a Lokpal or Lokayukta "
                  "recommendation. The Court directed that the matter be placed before the Chief "
                  "Justice to constitute an appropriate Bench to hear it afresh.")]),
            H("red", "Check the current position before relying on s17A in any case: as of October "
              "2026 no decision of the new Bench had been traced."),
        ]),

        S("Perception indices", "The Corruption Perceptions Index in South Asia, 2025", [
            B("Transparency International's Corruption Perceptions Index (CPI) scores countries "
              "from 0 (highly corrupt) to 100 (very clean) on perceived public sector corruption, "
              "combining expert and business surveys. It is the most quoted corruption number in "
              "the world. Here are the 2025 scores for South Asia, out of 182 countries ranked."),
            {"t": "chart", "canvas": "cpiChart",
             "title": "CPI 2025 score, South Asian countries (0 = highly corrupt, 100 = very clean)",
             "source": CPI + ", country pages",
             "type": "bar",
             "data": {"labels": ["Bhutan", "India", "Sri Lanka", "Nepal", "Pakistan", "Bangladesh"],
                      "datasets": [{"label": "CPI 2025 score",
                                    "data": [71, 39, 35, 34, 28, 24],
                                    "backgroundColor": ["#047857", "#0369A1", "#0369A1", "#0369A1",
                                                        "#B45309", "#B91C1C"]}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:100, title:{display:true,text:'CPI 2025 score'} } } }"}},
            H("cyan", "Ranks out of 182: Bhutan 18, India 91, Sri Lanka 107, Nepal 109, Pakistan "
              "136, Bangladesh 150. Source: " + CPI + "."),
        ]),

        S("Experience surveys", "Asking people what they paid", [
            B("Perception indices ask experts what they think. Experience surveys ask citizens "
              "what happened to them. Transparency International's Global Corruption Barometer "
              "Asia 2020 surveyed nearly 20,000 people in 17 countries, mostly by telephone "
              "because of COVID-19, between March 2019 and September 2020."),
            ST([C("39%", "of public service users in India reported paying a bribe in the previous "
                  "12 months, the highest in the survey", "red",
                  "Transparency International, Global Corruption Barometer Asia 2020"),
                C("89%", "of Indian respondents thought government corruption a big problem", "amber",
                  "Transparency International, Global Corruption Barometer Asia 2020"),
                C("23%", "region-wide bribe rate for contact with the police, the highest of any "
                  "service", "indigo",
                  "Transparency International, Global Corruption Barometer Asia 2020")], cols=3),
            H("green", "Experience data are closer to what a programme can act on: they name the "
              "service, the frequency and who paid."),
        ]),

        S("Limits", "What perception indices cannot tell you", [
            B("Perception scores are slow to move, sensitive to scandals and media coverage, and "
              "silent about where in the system the problem sits. They can also be gamed: "
              "governments that want a better score may manage the appearance of reform. The "
              "Centre for Law and Democracy's RTI Rating shows a related problem from the other "
              "side: it rates the text of laws, and Afghanistan's 2014 law tops its table."),
            TC([P("red", "Perception index",
                  "Experts and business people rate the whole public sector. Good for "
                  "long-run cross-country patterns. Cannot locate leakage or test a reform.")],
               [P("green", "Direct measurement",
                  "Compare records with reality: engineers' cost estimates, beneficiary surveys, "
                  "unannounced visits, audit findings. Locates leakage and can show whether a "
                  "reform reduced it.")]),
            H("amber", "A law that scores well on paper and an agency that scores well in "
              "perception surveys can both coexist with poor delivery. Measure delivery."),
        ]),

        S("Direct measures", "Measuring corruption by comparing records with reality", [
            B("The strongest corruption research measures the gap between what was recorded and "
              "what happened. Each method below has been used in published studies cited in this "
              "course, and each can be adapted to programme monitoring at modest cost."),
            T(["Method", "How it works", "Study"],
              [["Engineering audit", "Independent engineers estimate materials in a finished road and compare with reported spending",
                "Olken (2007), 600+ Indonesian village roads"],
               ["Random public audits", "Audit findings released to voters before elections",
                "Ferraz and Finan (2008), Brazilian municipalities"],
               ["Beneficiary verification", "Survey listed beneficiaries to see who exists and what they received",
                "Muralidharan, Niehaus and Sukhtankar (2016), Andhra Pradesh"],
               ["Unannounced visits", "Count staff present and working",
                "Chaudhury et al. (2006); Muralidharan et al. (2017)"],
               ["Phone checks", "Call beneficiaries to confirm receipt of transfers",
                "Muralidharan, Niehaus, Sukhtankar and Weaver (2021)"]]),
            H("green", "Any MEL team can run a small version of these. Section 10 shows how."),
        ]),

        S("Strategy", "Prevent, detect, sanction: a map of anti-corruption tools", [
            B("Anti-corruption work in India uses many instruments that are often discussed one "
              "at a time. Grouping them by what they do shows where a system is thin. A district "
              "with strong detection and no sanction produces audit paragraphs and no change; a "
              "district with harsh sanctions and no detection punishes only the unlucky."),
            T(["Function", "Indian instruments covered in this course", "Typical weakness"],
              [["Prevent", "Proactive disclosure (RTI s4), DBT and payment reforms, e-tendering, right to service laws",
                "Rules that exist on paper and are not checked"],
               ["Detect", "RTI requests, social audits, CAG audits, phone monitoring, grievance data",
                "Findings that no one with authority reads"],
               ["Sanction", "Prevention of Corruption Act prosecutions, RTI s20 penalties, Lokpal and Lokayuktas, disciplinary rules",
                "Approval requirements, delay and rare use of penalties"],
               ["Protect", "Whistleblower law, confidential channels, anonymised complaints",
                "Whistle Blowers Protection Act 2014 not operational (see Section 8)"]]),
            TC([B("<strong>For a programme:</strong> map which of the four functions exist for the "
                  "service you work on before adding another detection tool.", sm=True)],
               [B("<strong>For research:</strong> ask which function an intervention changes; it "
                  "tells you which outcome to measure.", sm=True)]),
        ]),

        # ===================== SECTION 05 =====================
        DIV("05", "Five", "Decentralisation: funds, functions, functionaries"),

        S("Why decentralise", "The case for and against moving power down", [
            B("Decentralisation moves decisions closer to citizens. The argument for it is "
              "informational and political: local governments know local needs, and local voters "
              "can see and judge results. The argument against is about capacity and capture: "
              "local bodies may lack skilled staff, and local elites may control them more "
              "easily than they could control a distant state."),
            TC([P("green", "Arguments for",
                  "Better information about needs. Shorter accountability chain. Room for local "
                  "experiment. Political voice for groups who are a minority nationally but a "
                  "majority locally.")],
               [P("red", "Arguments against",
                  "Thin administrative capacity. Elite capture. Unequal tax bases between rich "
                  "and poor areas. Blurred responsibility when three tiers share a function.")]),
            H("indigo", "Evidence from South Asia suggests both sets of arguments are right in "
              "different places. Design and finance decide which one wins."),
        ]),

        S("The amendments", "The 73rd and 74th Amendments", [
            B("India gave constitutional status to rural and urban local government through the "
              "Constitution (Seventy-third Amendment) Act 1992, which inserted Part IX on "
              "panchayats, and the Seventy-fourth Amendment Act 1992, which inserted Part IXA on "
              "municipalities. The 73rd Amendment came into force on 24 April 1993."),
            T(["Feature", "Panchayats (Part IX)", "Municipalities (Part IXA)"],
              [["Powers and functions", "Article 243G", "Article 243W"],
               ["Illustrative list of matters", "Eleventh Schedule, 29 subjects", "Twelfth Schedule, 18 functions"],
               ["Finance Commission", "Article 243I, every fifth year", "Article 243Y, same commission"],
               ["Reservation", "Article 243D: SCs, STs, at least one-third women", "Article 243T, parallel provisions"],
               ["Audit of accounts", "Article 243J, by state law", "Article 243Z, by state law"]]),
            H("cyan", "Sources: Constitution of India, Articles 243D, 243G, 243I, 243J, 243W, 243Y; "
              "Wikipedia, Panchayati raj in India and Municipal governance in India."),
        ]),

        S("The key word", "\"May\": why devolution depends on each state", [
            B("Article 243G says the Legislature of a State <em>may</em>, by law, endow panchayats "
              "with the powers and authority needed to function as institutions of "
              "self-government, including the preparation and implementation of plans for "
              "economic development and social justice, and schemes on the Eleventh Schedule "
              "matters. Article 243W says the same for municipalities and the Twelfth Schedule."),
            TC([P("indigo", "What the Constitution guarantees",
                  "Five-year terms with elections before a term ends (Article 243E), reserved "
                  "seats (243D), a five-yearly State Finance Commission (243I) and a State "
                  "Election Commission (243K).")],
               [P("amber", "What it leaves to states",
                  "Which of the 29 subjects to devolve, how much money, which staff, and how "
                  "much control the state bureaucracy keeps. That is why devolution varies so "
                  "widely across India.")]),
            H("red", "When a programme assumes a gram panchayat controls a function, check the "
              "state's Panchayati Raj Act and its devolution orders first."),
        ]),

        S("Reservation", "Seats for women, SCs and STs, and what changed", [
            B("Article 243D reserves seats for Scheduled Castes and Scheduled Tribes in proportion "
              "to their population in the panchayat area, and not less than one-third of all "
              "directly elected seats for women, including within the SC and ST quotas. Offices "
              "of chairpersons are also reserved as state law provides, often by rotation."),
            Q("Leaders invest more in infrastructure that is directly relevant to the needs of "
              "their own genders.",
              "Raghabendra Chattopadhyay and Esther Duflo, Women as Policy Makers, Econometrica "
              "72(5), 2004, on 265 village councils in West Bengal and Rajasthan"),
            TC([B("<strong>Why the study is strong:</strong> since the mid-1990s one third of "
                  "council head posts had been randomly reserved for women, so reserved and "
                  "unreserved councils could be compared fairly.", sm=True)],
               [B("<strong>What to watch:</strong> proxy rule by male relatives is widely "
                  "reported. A programme can support elected women with training and by "
                  "dealing with them directly.", sm=True)]),
        ]),

        S("The three Fs", "Funds, functions and functionaries", [
            B("Devolution is often assessed on three dimensions. A local government with "
              "functions but no money cannot act; with money but no staff it cannot spend well; "
              "with staff who answer to a state department it cannot direct them. Practitioners "
              "who work with panchayats should check all three before assigning them a role in a "
              "programme."),
            T(["Dimension", "Question to ask", "Warning sign"],
              [["Functions", "Which Eleventh Schedule subjects has the state devolved by order?",
                "Subjects devolved on paper while the line department still runs every scheme"],
               ["Funds", "How much untied money does the panchayat control each year?",
                "Almost all funds are scheme-tied grants with fixed guidelines"],
               ["Functionaries", "Who appoints, transfers and disciplines the staff?",
                "Staff report to block or district officers and ignore the elected body"]]),
            H("amber", "A panchayat that scores well on one F and badly on the others is still "
              "a weak partner for accountability work."),
        ]),

        S("Finance", "Panchayats depend on grants: the RBI's numbers", [
            B("The Reserve Bank of India's study <em>Finances of Panchayati Raj Institutions</em>, "
              "released on 24 January 2024, used data for 2020&ndash;21 to 2022&ndash;23. It "
              "found that revenue receipts are dominated by grants-in-aid from the Centre and the "
              "states, and that panchayats raise very little from local taxes, fees and charges."),
            ST([C("95%+", "of panchayat revenue receipts are grants-in-aid", "indigo",
                  "RBI, Finances of Panchayati Raj Institutions, 24 January 2024"),
                C("1.1%", "of total revenue receipts from panchayats' own taxes in 2020&ndash;21 and "
                  "2021&ndash;22 (1.0% in 2022&ndash;23)", "red",
                  "RBI, Finances of Panchayati Raj Institutions, 24 January 2024, Table II.4"),
                C("~80%", "of revenue receipts from Central Government grants alone in "
                  "2021&ndash;23 (79.6% and 79.8%)", "amber",
                  "RBI, Finances of Panchayati Raj Institutions, 24 January 2024, Table II.4")], cols=3),
            H("cyan", "Grant dependence weakens the local tax-for-services link that "
              "decentralisation theory relies on: voters who pay little locally may demand "
              "little locally."),
        ]),

        S("Finance Commissions", "Central and State Finance Commissions", [
            B("Article 243I requires the Governor to constitute a State Finance Commission every "
              "fifth year to recommend how state taxes are shared with panchayats, which taxes "
              "they may levy, and what grants they receive. Article 243Y extends the same "
              "commission to municipalities. The Union Finance Commission also recommends grants "
              "to local bodies."),
            {"t": "chart", "canvas": "fcChart",
             "title": "Fifteenth Finance Commission grants to local governments, 2021&ndash;26 (Rs crore)",
             "source": "Down To Earth, 1 February 2021, reporting the Fifteenth Finance Commission",
             "type": "doughnut",
             "data": {"labels": ["Rural local bodies", "Urban local bodies", "Health grants via local bodies",
                                 "Other (balance of total)"],
                      "datasets": [{"data": [236805, 121055, 70051, 8450],
                                    "backgroundColor": ["#047857", "#0369A1", "#B45309", "#64748B"]}]},
             "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
            H("amber", "Total Rs 4,36,361 crore for 2021&ndash;26. The \"Other\" slice is the "
              "arithmetic balance of the reported total, shown so the parts add up."),
        ]),

        S("Kerala", "Kerala's People's Plan Campaign, 1996", [
            B("Kerala is the best-known Indian case of deep devolution. An evaluation published by "
              "the Planning Commission (now hosted by DMEO) records that the state announced in "
              "July 1996 a decision to devolve 35 to 40% of plan funds to local governments, and "
              "launched the People's Plan Campaign in August 1996 with mass mobilisation through "
              "organisations including the Kerala Sasthra Sahitya Parishad."),
            TC([P("green", "Design features",
                  "Ward-level grama sabhas with a quorum of ten per cent of voters. Conditions on "
                  "the devolved funds: at least 30% for productive sectors, no more than 30% for "
                  "infrastructure, at least 10% for women's programmes.")],
               [P("amber", "Finance Commission link",
                  "Kerala's First State Finance Commission reported in February 1996. The same "
                  "evaluation notes that the formula used to share plan funds among local bodies "
                  "was evolved by a State Planning Board working group in 1997, separately from "
                  "the commission's recommendations.")]),
            H("cyan", "Source: Planning Commission evaluation, Decentralized Planning Experience in "
              "Kerala (DMEO website)."),
        ]),

        S("South Asia", "Local government elsewhere in South Asia", [
            B("India's neighbours have taken different routes. Nepal's 2015 Constitution created "
              "a three-tier federal system with 753 local levels, each with its own executive. "
              "Pakistan's Constitution, in Article 140A, requires each province by law to "
              "establish a local government system and devolve political, administrative and "
              "financial responsibility to elected local representatives, with elections held by "
              "the Election Commission of Pakistan."),
            T(["Country", "Constitutional basis", "Practitioner note"],
              [["India", "Parts IX and IXA (73rd and 74th Amendments, 1992)",
                "Devolution varies by state; check the state Act"],
               ["Nepal", "Constitution of Nepal 2015", "753 local levels: 6 metropolitan cities, 11 sub-metropolitan, 276 municipalities, 460 rural municipalities"],
               ["Pakistan", "Article 140A", "Provinces design their own systems; elections run by the ECP"]]),
            H("indigo", "Sources: Nepal, Ministry of Federal Affairs and General Administration, list "
              "of 753 local levels; Constitution of Pakistan, Article 140A (pakistani.org)."),
        ]),

        S("Elite capture", "When decentralisation hands power to the powerful", [
            B("Moving decisions to the village can move them into the hands of the village's "
              "dominant caste, landlords or contractors. Gram sabhas may be held on paper, "
              "beneficiary lists may favour the sarpanch's network, and reserved office holders "
              "may be pressured. Decentralisation increases accountability only where those "
              "left out have voice, information and some protection."),
            TC([P("red", "Signs of capture",
                  "Gram sabha minutes with identical signatures. Works concentrated in one "
                  "hamlet. Beneficiary lists that track one family's network. Reserved members "
                  "silent in meetings.")],
               [P("green", "Counterweights",
                  "Ward-level sabhas, women's sabhas, public reading of beneficiary lists, "
                  "social audit by outsiders, and support for SC, ST and women members.")]),
            H("amber", "Read " + L("pol-economy.html", "Political Economy 101") + " for the "
              "theory of capture, and " + L("participatory-methods.html", "Participatory Methods 101")
              + " for running inclusive village meetings."),
        ]),

        # ===================== SECTION 06 =====================
        DIV("06", "Six", "Transparency and the RTI Act"),

        S("The Act", "The Right to Information Act 2005 in brief", [
            B("India's RTI Act gives every citizen the right to request information from any "
              "public authority and requires authorities to publish a defined set of information "
              "without being asked. It overrides the Official Secrets Act 1923 and other laws to "
              "the extent of inconsistency (section 22). Public authorities include bodies owned, "
              "controlled or substantially financed by government, and NGOs substantially "
              "financed directly or indirectly by government funds (section 2(h))."),
            TC([P("cyan", "Demand side",
                  "Any citizen can file a request (s6). No reason need be given (s6(2)). Applicants "
                  "below the poverty line pay no fee under the RTI Rules 2012.")],
               [P("green", "Supply side",
                  "Every authority must maintain and catalogue records and publish its functions, "
                  "budgets, norms and decision-making processes on its own initiative "
                  "(section 4(1)(b)).")]),
            H("amber", "If your NGO receives substantial government funding, it may itself be a "
              "public authority under s2(h). Take legal advice before assuming otherwise."),
        ]),

        S("Sections to know", "Ten sections every practitioner should know", [
            B("You do not need to memorise the Act, but these provisions come up in almost every "
              "RTI request, appeal and training session. Section numbers refer to the Right to "
              "Information Act 2005."),
            T(["Section", "What it does"],
              [["s2(h)", "Defines public authority, including substantially financed NGOs"],
               ["s4(1)(b)", "Proactive disclosure of functions, norms, budgets and decisions"],
               ["s6", "How to make a request; s6(2): no reasons required"],
               ["s7(1)", "Reply within 30 days; 48 hours if life or liberty is involved"],
               ["s7(2)", "No decision within time counts as deemed refusal"],
               ["s8(1)", "Exemptions, including clause (j) on personal information"],
               ["s8(2)", "Public interest override, notwithstanding the Official Secrets Act"],
               ["s11", "Procedure for third-party information"],
               ["s19", "First appeal within 30 days; second appeal to the commission within 90 days"],
               ["s20", "Penalty of Rs 250 a day on the PIO, up to Rs 25,000"]]),
            H("cyan", "Source: " + RTI + ", CIC copy of the Act."),
        ]),

        S("The process", "From request to second appeal", [
            B("The RTI process has a fixed sequence with time limits at every step. Missing a "
              "deadline can end a case, so record dates carefully. Section 24 exempts the "
              "intelligence and security organisations listed in the Second Schedule, except for "
              "information on allegations of corruption and human rights violations."),
            FL(["REQUEST to the PIO under s6",
                "REPLY within 30 days (s7(1))",
                "FIRST APPEAL within 30 days to the appellate officer (s19(1))",
                "SECOND APPEAL within 90 days to the CIC or SIC (s19(3))",
                "PENALTY on the PIO where the commission finds fault (s20)"]),
            TC([B("<strong>Deemed refusal:</strong> silence after 30 days is a refusal under "
                  "s7(2), and you can appeal at once.", sm=True)],
               [B("<strong>Life or liberty:</strong> where information concerns a person's life "
                  "or liberty, the PIO must reply within 48 hours (proviso to s7(1)).", sm=True)]),
        ]),

        S("Exemptions", "Section 8: what can be withheld, and the override", [
            B("Section 8(1) lists the grounds on which information may be refused, among them "
              "national security and sovereignty, information forbidden by a court, legislative "
              "privilege, commercial confidence, fiduciary relationships, information that would "
              "impede an investigation, and personal information under clause (j). Section 8(3) "
              "makes most records more than twenty years old disclosable."),
            TC([P("indigo", "Section 8(2): the general override",
                  "A public authority may allow access even to exempt information \"if public "
                  "interest in disclosure outweighs the harm to the protected interests\", "
                  "notwithstanding the Official Secrets Act 1923.")],
               [P("amber", "How PIOs use exemptions",
                  "Many refusals cite s8 without reasons. A refusal must name the section and "
                  "explain why it applies. A bare citation is itself a ground for first appeal.")]),
            H("cyan", "Section 8(2) was not touched by the 2023 amendment discussed two slides "
              "on. It remains your main argument when personal information is refused."),
        ]),

        S("2019 amendment", "The RTI (Amendment) Act 2019: commissioners' tenure", [
            B("The 2005 Act fixed the term of Chief Information Commissioners and Information "
              "Commissioners at five years (or age 65) and tied the central commissioners' salaries "
              "to those of the Election Commission. PRS Legislative Research's summary of the 2019 Bill records "
              "that it removed the fixed term and let the central government notify the term, "
              "salaries and conditions of service for both central and state commissioners."),
            TC([P("red", "Before 2019",
                  "Five-year term fixed in the Act. Central Chief Information Commissioner paid "
                  "like the Chief Election Commissioner. Conditions could not be changed to a "
                  "commissioner's disadvantage by executive order.")],
               [P("amber", "After 2019",
                  "Rules notified on 24 October 2019 set a three-year term for central and state "
                  "commissioners. Term and pay are now set by the central government, the same "
                  "body whose information commissions rule on.")]),
            H("indigo", "Why it matters: horizontal accountability depends on independence. "
              "Shorter, executive-set terms change the incentives of those who decide appeals."),
        ]),

        S("2023 amendment", "How the DPDP Act 2023 rewrote section 8(1)(j)", [
            B("Section 44(3) of the Digital Personal Data Protection Act 2023 (No. 22 of 2023, "
              "assented to on 11 August 2023) substituted a new clause (j) in section 8(1) of the "
              "RTI Act. MeitY's notification G.S.R. 843(E) of 13 November 2025 brought s44(3) into "
              "force on its publication in the Gazette that day; most of the DPDP Act itself "
              "commences only on 13 May 2027."),
            TC([P("indigo", "Clause (j) as enacted in 2005",
                  "Exempts personal information \"the disclosure of which has no relationship to "
                  "any public activity or interest, or which would cause unwarranted invasion of "
                  "the privacy of the individual unless\" the PIO or appellate authority \"is "
                  "satisfied that the larger public interest justifies the disclosure\".")],
               [P("red", "Clause (j) as substituted by s44(3)",
                  "\"(j) information which relates to personal information;\" Nothing more. The "
                  "public activity test and the public interest test written into the clause are "
                  "gone.")]),
            H("cyan", "Sources: DPDP Act 2023, s44(3), Gazette of India, 11 August 2023; G.S.R. "
              "843(E), Gazette of India, 13 November 2025; " + RTI + "."),
        ]),

        S("What it means", "Working with the new section 8(1)(j)", [
            B("Information about officials' conduct, beneficiary lists, muster rolls and "
              "contractor payments all relate to identifiable people. Under the substituted "
              "clause a PIO can now refuse such requests by citing s8(1)(j) alone. Two arguments "
              "remain open to requesters, and both will be tested in the commissions and courts."),
            T(["Argument", "Basis", "Status as of October 2026"],
              [["General public interest override", "Section 8(2), which the 2023 Act did not amend",
                "Available; requester must show public interest outweighs harm"],
               ["Information that cannot be denied to Parliament cannot be denied to any person",
                "Proviso that followed clause (j) in the 2005 text",
                "Contested: commentators differ on whether the proviso survives the substitution"],
               ["Proactive disclosure duties", "Section 4 and scheme-specific laws (for example s24(d) of the VB-G RAM G Act)",
                "Unaffected; ask for disclosures the law already requires"]]),
            H("amber", "Practical step: frame requests around public functions and aggregate data "
              "where you can, and cite s8(2) and the relevant disclosure duty where you cannot."),
        ]),

        S("Commissions", "The information commissions are the bottleneck", [
            B("A right is only as good as the body that enforces it. Satark Nagrik Sangathan's "
              "annual report card assessed all 29 information commissions for July 2024 to June "
              "2025. Its findings show that delay and vacancy, more than the text of the law, now "
              "decide whether an RTI request succeeds."),
            ST([C("4,13,972", "appeals and complaints pending on 30 June 2025 in 29 commissions", "red", SNS),
                C("18 of 29", "commissions with an estimated wait of more than a year", "amber", SNS),
                C("98%", "of cases where a penalty was potentially imposable saw none imposed", "indigo", SNS),
                C("6", "commissions defunct for some part of July 2024 to October 2025", "red", SNS)], cols=4),
            H("cyan", "The same report found the Central Information Commission returned 38% of the "
              "appeals and complaints it received, and that 20 of 29 commissions had not published "
              "their 2023&ndash;24 annual reports."),
        ]),

        S("Case law", "Two Supreme Court decisions that extended transparency", [
            B("Courts have used both the RTI Act and Article 19(1)(a) to widen access to "
              "information about public power. Two Constitution Bench decisions are worth "
              "knowing because they concern institutions at the top of the system."),
            TC([P("indigo", "CPIO, Supreme Court v Subhash Chandra Agarwal (2019)",
                  "On 13 November 2019 a Constitution Bench held that the office of the Chief "
                  "Justice of India is a public authority under s2(h) of the RTI Act. It applied a "
                  "proportionality test to balance judges' privacy against public interest in "
                  "disclosure of information such as judges' asset declarations.")],
               [P("green", "Association for Democratic Reforms v Union of India (2024)",
                  "On 15 February 2024 a Constitution Bench unanimously struck down the 2018 "
                  "Electoral Bond Scheme, holding that it violated voters' right to information "
                  "under Article 19(1)(a) about the funding of political parties (2024 INSC 113).")]),
            H("cyan", "Sources: Global Freedom of Expression, Columbia University, on Subhash "
              "Chandra Agarwal; Supreme Court Observer, on ADR v Union of India."),
        ]),

        S("Region", "Right to information laws across South Asia", [
            B("Afghanistan, Bangladesh, India, the Maldives, Nepal, Pakistan and Sri Lanka all "
              "have right to information laws. The Centre for "
              "Law and Democracy's RTI Rating scores the legal text out of 150 on seven "
              "categories, from scope to appeals and sanctions. It rates the law as written and "
              "does not assess how commissions work in practice, and its India entry is based on the 2005 Act "
              "without the 2019 and 2023 amendments."),
            T(["Country", "Law assessed", "RTI Rating score (of 150)"],
              [["Afghanistan", "Law of 2014 (as rated)", "139"],
               ["Sri Lanka", "Right to Information Act, No. 12 of 2016", "131"],
               ["India", "Right to Information Act, 2005", "126"],
               ["Maldives", "Law of 2014", "114"],
               ["Nepal", "Right to Information Act, 2007 (2064 BS)", "112"],
               ["Bangladesh", "Right to Information Act, 2009", "109"],
               ["Pakistan", "Right of Access to Information Act, 2017", "108"]]),
            H("amber", "Source: Centre for Law and Democracy, RTI Rating country data, read October "
              "2026. A strong law and a slow commission can coexist; check both."),
        ]),

        # ===================== SECTION 07 =====================
        DIV("07", "Seven", "Social audit and citizen monitoring"),

        S("Definition", "What a social audit is", [
            B("A social audit is a public verification of a programme's records by the people it "
              "is meant to serve. Muster rolls, bills, vouchers and measurement books are "
              "collected, checked against what workers and residents report, and read out at a "
              "public meeting where officials must answer. It combines the answerability of an "
              "audit with the public pressure of a hearing."),
            FL(["RECORDS obtained from the panchayat and block",
                "VERIFICATION door to door and at work sites",
                "PUBLIC HEARING in the gram sabha",
                "ACTION TAKEN report and follow-up"]),
            TC([B("<strong>What it adds to a financial audit:</strong> the people named in the "
                  "records confirm or deny them, so ghost workers and inflated measurements "
                  "surface.", sm=True)],
               [B("<strong>What it needs:</strong> complete records, trained resource persons "
                  "independent of the implementing agency, and officials obliged to act on "
                  "findings.", sm=True)]),
        ]),

        S("Origins", "From Rajasthan's public hearings to a statutory duty", [
            B("Social audit in India grew from the Mazdoor Kisan Shakti Sangathan's public "
              "hearings (jan sunwais) in Rajasthan in the 1990s, where villagers read out "
              "official spending records and compared them with what was built. Section 17 of the "
              "Mahatma Gandhi National Rural Employment Guarantee Act 2005 required the Gram Sabha "
              "to conduct regular social audits of all projects under the scheme. Andhra Pradesh "
              "built the first large-scale system: a pilot in February 2006, a mass social audit "
              "across 600 villages of Anantapur district in September 2006 and, from May 2009, an "
              "autonomous Society for Social Audit, Accountability and Transparency (SSAAT)."),
            TC([P("green", "What Andhra Pradesh showed",
                  "Commitment matters: the state set up a dedicated social audit office, gave its "
                  "director a clear mandate, and recruited a key MKSS member to signal intent.")],
               [P("amber", "What it also showed",
                  "Audits uncover irregularities faster than departments act on them. Without "
                  "follow-up, findings pile up and villagers stop attending.")]),
            H("cyan", "Sources: Singh and Vutukuru, case study of social audits in Andhra Pradesh "
              "(Harvard Kennedy School policy analysis, hosted by COPASAH); Wikipedia, Social audit, "
              "for the SSAAT date."),
        ]),

        S("The new law", "Social audit after MGNREGA's repeal", [
            B("Section 37 of the Viksit Bharat Guarantee for Rozgar and Ajeevika Mission "
              "(Gramin) Act 2025 (VB-G RAM G Act, No. 36 of 2025) repeals MGNREGA from the "
              "appointed date, which was 1 July 2026. The new Act guarantees 125 days of wage "
              "employment and keeps social audit, but places it in different provisions."),
            T(["Provision of the VB-G RAM G Act 2025", "What it says"],
              [["s20(1)", "The Gram Sabha shall monitor and review execution of all works in the Gram Panchayat"],
               ["s20(2)", "The Gram Sabha shall conduct regular social audits of all works, in such manner as the Central Government prescribes"],
               ["s20(3)", "The Gram Panchayat must make available muster rolls, bills, vouchers, measurement books, sanction orders, digital records and geo-tagged photographs"],
               ["s18(5)(d)", "The Programme Officer must ensure regular social audits by the Gram Sabha and timely action on findings"],
               ["s24(d)&ndash;(e)", "Weekly public disclosure of muster rolls, payments and grievances; strengthening of the social audit mechanism as prescribed"],
               ["s33(2)(g), (n)", "Central Government rules on the manner of social audit and the mechanism"]]),
            H("amber", "Check the rules notified under s33 before designing audit work. Much of the "
              "detail now sits in central rules made under the Act."),
        ]),

        S("Then and now", "What changed for social audit, MGNREGA to VB-G RAM G", [
            B("Practitioners trained under MGNREGA will find familiar elements in the new Act and "
              "some important shifts. The Act places the audit duty on the Gram Sabha itself and "
              "pairs it with technology-based monitoring. Whether audits stay independent of the "
              "implementing agency will depend on the rules and on how states use their existing "
              "Social Audit Units."),
            TC([P("indigo", "MGNREGA 2005 (repealed from 1 July 2026)",
                  "Section 17 required the Gram Sabha to conduct regular social audits of all "
                  "projects under the scheme. States set up social audit bodies to run them, such as SSAAT in Andhra Pradesh "
                  "from May 2009.")],
               [P("green", "VB-G RAM G Act 2025",
                  "Section 20 keeps Gram Sabha social audit and lists the records to be "
                  "provided. Section 24 adds biometric authentication, geospatial planning, "
                  "dashboards and weekly disclosure. Rules come from the Centre under s33.")]),
            H("cyan", "Source: VB-G RAM G Act 2025 (India Code, Act No. 36 of 2025), ss 20, 24, "
              "33 and 37."),
        ]),

        S("Evidence", "Does community monitoring work? Three experiments", [
            B("Randomised trials of community monitoring have produced mixed results, and the "
              "differences between them are instructive. The three below are among the most "
              "cited; each is summarised from its published abstract."),
            T(["Study", "What was tested", "Result"],
              [["Bjorkman and Svensson (2009), Uganda, QJE",
                "NGO-run village meetings to monitor primary health providers",
                "More community monitoring, more effort by health workers, higher utilisation, lower child mortality and higher child weight"],
               ["Banerjee, Banerji, Duflo, Glennerster and Khemani (2010), Uttar Pradesh, AEJ Policy",
                "Information on village education committees; training in a reading test; volunteer reading camps",
                "No effect of the first two on involvement, teacher effort or learning; children in the volunteer camps improved reading"],
               ["Olken (2007), Indonesia, JPE",
                "More grassroots participation in monitoring road projects, versus raising government audits from 4% to 100%",
                "Audits cut missing expenditure by eight percentage points; participation had little average effect"]]),
            H("amber", "Information alone rarely moves providers. Citizens act when they have a "
              "forum, a clear standard and a route to consequences."),
        ]),

        S("Tools", "A family of citizen monitoring tools", [
            B("Social audit is one member of a larger family. The right tool depends on whether "
              "you want to measure satisfaction, check records, or negotiate improvements with "
              "providers. Each tool below has been used across South Asia by government "
              "departments, NGOs and research groups."),
            T(["Tool", "What it does", "Best used for"],
              [["Citizen report card", "Survey of users rating a service across providers or areas",
                "Comparing performance and starting a public conversation"],
               ["Community scorecard", "Users and providers score a facility together, then agree actions",
                "Joint problem solving at one facility"],
               ["Social audit", "Public verification of records against reality",
                "Detecting leakage in works and transfer programmes"],
               ["Public expenditure tracking", "Follows funds from budget to facility",
                "Finding where money leaks or is delayed"],
               ["Public hearing (jan sunwai)", "Open meeting where testimony is heard and officials respond",
                "Building pressure for action on specific cases"]]),
            H("green", "See " + L("participatory-methods.html", "Participatory Methods 101") +
              " for facilitation, and " + L("advocacy-basics.html", "Advocacy Basics 101") +
              " for turning findings into change."),
        ]),

        S("Conditions", "When social accountability works, and when it does not", [
            B("Reviewing the experiments and the Indian experience together suggests a set of "
              "conditions. None is sufficient alone. Use them as a checklist before you invest "
              "in a social accountability component."),
            TC([BL(["Records exist, are complete, and are released on time",
                    "Citizens know the standard they are entitled to (wage rate, days, quantity)",
                    "The audit team is independent of the implementing agency",
                    "There is a forum where officials must attend and answer"], color="green")],
               [BL(["Someone with authority acts on findings within a fixed time",
                    "Complainants are protected from retaliation",
                    "Findings are published and tracked across rounds",
                    "Marginalised groups can speak alongside the village elite"], color="amber")]),
            H("red", "If the last link is missing, social audit becomes a ritual that produces "
              "reports and disillusion. Plan for follow-up before you plan the hearing."),
        ]),

        S("Risks", "Protecting people who speak up", [
            B("Social audits and RTI requests expose people who benefit from leakage, and those "
              "people may retaliate. RTI users and social audit resource persons in India have "
              "faced threats and violence. A programme that encourages citizens to challenge "
              "officials has a duty to reduce the risks it creates."),
            TC([P("red", "Risks to anticipate",
                  "Threats to complainants and their families. Loss of work or benefits. False "
                  "counter-complaints. Pressure on reserved-seat members and frontline staff who "
                  "testify.")],
               [P("green", "Protective practice",
                  "File requests through organisations to shield exposed individuals. Aggregate "
                  "testimony. Share findings with district officials before the hearing. Keep "
                  "a referral route to legal aid and the police.")]),
            H("amber", "See " + L("safeguarding-psea.html", "Safeguarding &amp; PSEA 101") +
              " for risk assessment, and " + L("research-ethics.html", "Research Ethics 101") +
              " for consent when you collect testimony."),
        ]),

        # ===================== SECTION 08 =====================
        DIV("08", "Eight", "Grievances, charters and the Lokpal"),

        S("Charters", "Citizen charters and right to service laws", [
            B("A citizen charter states what service a department promises, to what standard and "
              "in what time. On its own it has no legal force. Several Indian states went further "
              "and passed right to service laws, which make delivery within a notified time a "
              "legal duty and allow penalties on officials who miss it. Madhya Pradesh was the "
              "first state to enact such a law, on 18 August 2010, and Bihar followed in 2011."),
            TC([P("amber", "Citizen charter",
                  "Promise of standards and timelines. Useful for awareness. No remedy if the "
                  "promise is broken. A national Citizen's Charter and Grievance Redressal Bill "
                  "was proposed in 2011.")],
               [P("green", "Right to service law",
                  "Notified services, time limits, designated officers, appeals and fines. Works "
                  "where appeals are heard quickly and fines are actually imposed.")]),
            H("cyan", "Source: Wikipedia, Right to Public Services legislation (with state Act "
              "references). Check your state's notified service list before advising citizens."),
        ]),

        S("CPGRAMS", "The central grievance portal", [
            B("The Centralised Public Grievance Redress and Monitoring System (CPGRAMS) links all "
              "central ministries and departments, states and union territories on one portal, "
              "pgportal.gov.in. Citizens can file online, through a mobile app, or at Common "
              "Service Centres. A PIB backgrounder of 9 August 2026 sets out the government's "
              "figures."),
            ST([C("27 lakh", "grievances handled in 2024, against about 3.01 lakh in 2014", "cyan",
                  "PIB backgrounder on CPGRAMS, 9 August 2026"),
                C("15 days", "average disposal time in central ministries in 2025, against 157 in 2014", "green",
                  "PIB backgrounder on CPGRAMS, 9 August 2026"),
                C("1.11 lakh+", "grievance redressal officers by 2025, against 10,232 in 2014", "indigo",
                  "PIB backgrounder on CPGRAMS, 9 August 2026")], cols=3),
            H("amber", "These are official figures. \"Disposed\" means closed by the department, "
              "which is different from resolved to the citizen's satisfaction."),
        ]),

        S("Grievance or accountability?", "What a grievance system can and cannot do", [
            B("Grievance redress fixes individual cases: a pension not credited, a certificate "
              "delayed. Accountability changes the behaviour that produces such cases. A "
              "grievance system becomes an accountability tool when complaints are analysed for "
              "patterns, published, and used to sanction or retrain the units that generate them."),
            TC([P("cyan", "Grievance redress",
                  "One complaint, one fix. Measured by disposal time. Can close cases by "
                  "forwarding them or by replying without action.")],
               [P("green", "Accountability use",
                  "Complaints grouped by office, scheme and cause. Repeat failures trigger "
                  "inspection. Citizens can rate the reply and reopen it.")]),
            H("indigo", "For programmes: help users file, but also collect copies of complaints "
              "and replies. Your own record is the evidence for advocacy later."),
        ]),

        S("Lokpal", "The Lokpal and Lokayuktas Act 2013", [
            B("The Lokpal is an anti-corruption ombudsman for the Union. The Act's preamble links "
              "it to India's ratification of the UN Convention Against Corruption. The President "
              "gave assent on 1 January 2014. The Lokpal can inquire into complaints of "
              "corruption against a wide range of public functionaries."),
            T(["Section", "Provision"],
              [["s3(2)", "A Chairperson (a present or former Chief Justice or Supreme Court judge, or an eminent person) and up to eight Members"],
               ["s3(2)(b)", "Half the Members must be judicial; at least half the Members must be from SCs, STs, OBCs, minorities and women"],
               ["s14", "Jurisdiction includes the Prime Minister (with exclusions such as international relations and security), Ministers, MPs and Group A to D central officials"],
               ["s63", "Every State to establish a Lokayukta by state law within one year of commencement, if not already established"]]),
            H("cyan", "Sources: Lokpal and Lokayuktas Act 2013 (bare Act text); Supreme Court, CPIL "
              "v Union of India, 2026 INSC 55, for the date of assent."),
        ]),

        S("In practice", "A slow start: from Act to institution", [
            B("Passing the Act was the end of a long public campaign, but appointing the "
              "institution took more than five years. The first Lokpal, retired Supreme Court "
              "judge Pinaki Chandra Ghose, took office on 23 March 2019. After his term ended in "
              "May 2022 a member held additional charge until Justice A.M. Khanwilkar was "
              "appointed Chairperson from 10 March 2024."),
            FL(["1 JAN 2014: Presidential assent",
                "2014&ndash;2019: no Lokpal appointed",
                "23 MAR 2019: first Lokpal, P.C. Ghose",
                "2022&ndash;2024: acting arrangement",
                "10 MAR 2024: A.M. Khanwilkar"]),
            TC([B("<strong>Lesson:</strong> creating an accountability agency in law does not "
                  "create it in fact. Appointments, staff and an investigation wing all take "
                  "political will.", sm=True)],
               [B("<strong>For states:</strong> Lokayukta laws differ widely in powers and "
                  "independence. Read the state Act itself before relying on the national model.", sm=True)]),
        ]),

        S("Whistleblowers", "Protecting insiders who report corruption", [
            B("Outsiders see symptoms; insiders see how corruption works. The Whistle Blowers "
              "Protection Act 2014 was meant to protect public servants and others who disclose "
              "corruption. It was published as Act No. 17 of 2014 on 12 May 2014, but the government "
              "has never notified a date for it to come into force. A Lok Sabha answer of 12 December "
              "2024 says the Act first needs amendments against disclosures affecting sovereignty "
              "and security; the 2015 amendment Bill, passed by the Lok Sabha, lapsed when the "
              "Sixteenth Lok Sabha was dissolved in 2019."),
            TC([P("red", "The gap",
                  "Without an operational law, insiders who report rely on general service "
                  "rules, court orders in individual cases and the goodwill of their superiors.")],
               [P("green", "What programmes can do",
                  "Run confidential reporting channels inside your own organisation and "
                  "partners. Separate the person who reports from the person who investigates. "
                  "Record and act on every report.")]),
            H("amber", "Meanwhile the Central Vigilance Commission receives disclosures under the "
              "PIDPI Resolution 2004 (PIB, 12 December 2024). Confirm the Act's status from the "
              "Gazette before advising anyone who plans to make a disclosure."),
        ]),

        S("Choosing a channel", "Which grievance or complaint route fits which problem", [
            B("Citizens and programmes often send every problem to the same office. Matching the "
              "problem to the right channel saves months. The table summarises the main routes "
              "discussed in this course."),
            T(["Problem", "First channel", "If that fails"],
              [["Service not delivered on time", "State right to service Act, where notified; CPGRAMS",
                "Appeal under the state Act; complaint to district collector"],
               ["Information refused or ignored", "First appeal under s19(1) RTI Act",
                "Second appeal to the information commission under s19(3)"],
               ["Irregularities in rural works", "Gram Sabha social audit (s20 VB-G RAM G Act)",
                "Grievance mechanism under s25 of that Act; district vigilance"],
               ["Bribe demanded by a public servant", "State anti-corruption bureau or police",
                "Lokayukta or Lokpal, depending on the official"],
               ["Pattern of misuse of funds", "CAG and state audit, via legislators",
                "Public interest litigation in the High Court"]]),
            H("cyan", "Keep copies and dates of everything. Each later channel will ask what you "
              "did first."),
        ]),

        # ===================== SECTION 09 =====================
        DIV("09", "Nine", "Audit institutions, e-governance and DBT"),

        S("CAG", "The Comptroller and Auditor-General: Articles 148&ndash;151", [
            B("The CAG is India's supreme audit institution and a central horizontal "
              "accountability agency. The Constitution protects its independence by tying its "
              "removal to the process for a Supreme Court judge and by routing its reports to "
              "the legislature, away from the executive that it audits."),
            T(["Article", "What it provides"],
              [["148", "CAG appointed by the President by warrant under hand and seal; removable only like a Supreme Court judge"],
               ["149", "CAG performs duties and exercises powers over the accounts of the Union, the States and other bodies as Parliament prescribes by law"],
               ["150", "Accounts of the Union and States kept in the form the President prescribes on the CAG's advice"],
               ["151", "Reports on Union accounts go to the President, who lays them before each House; reports on State accounts go to the Governor, who lays them before the Legislature"]]),
            H("cyan", "Sources: Constitution of India, Articles 148&ndash;151, from "
              "constitutionofindia.net and the advocatekhoj bare Act text."),
        ]),

        S("How audit becomes accountability", "From audit report to consequence", [
            B("An audit report changes nothing until someone acts on it. In India the main link "
              "is the legislature's Public Accounts Committee, which examines CAG reports and "
              "asks departments to explain. Media coverage of major reports adds pressure. Local "
              "body accounts are audited under state law, as Article 243J provides."),
            FL(["AUDIT by CAG field offices",
                "REPORT to President or Governor (Art 151)",
                "TABLED in Parliament or the Legislature",
                "EXAMINED by the Public Accounts Committee",
                "ACTION TAKEN notes from the department"]),
            TC([B("<strong>Compliance audit</strong> checks whether money was spent according to "
                  "rules. <strong>Performance audit</strong> asks whether a programme achieved "
                  "what it set out to do.", sm=True)],
               [B("<strong>For practitioners:</strong> CAG performance audits of schemes you work "
                  "on are free, rigorous evaluations. Read them before you design a baseline.", sm=True)]),
        ]),

        S("Audit evidence", "What experiments say about audits", [
            B("Two well-known studies show that audits can reduce corruption, and that publishing "
              "them can change elections. Both come from outside South Asia, but their designs "
              "have shaped Indian research and practice."),
            TC([P("indigo", "Olken (2007), Indonesia",
                  "Raising the probability of a government audit of village road projects from "
                  "4% to 100% reduced missing expenditure, measured against independent "
                  "engineers' estimates, by eight percentage points. Grassroots monitoring had "
                  "little average effect.")],
               [P("green", "Ferraz and Finan (2008), Brazil",
                  "Brazil's federal government audited municipalities chosen at random and "
                  "published the findings. Releasing audit results before the 2004 elections "
                  "had a significant effect on incumbents' electoral performance, larger where "
                  "local radio spread the news.")]),
            H("amber", "The two together: top-down audit works, and it works better when citizens "
              "get to see the results."),
        ]),

        S("DBT", "Direct Benefit Transfer: the government's case", [
            B("Direct Benefit Transfer (DBT) pays subsidies and benefits straight into "
              "beneficiaries' bank accounts, usually with Aadhaar-based identification, instead "
              "of routing cash or goods through intermediaries. A PIB release of 21 April 2025 "
              "reported an assessment by the BlueKraft Digital Foundation of DBT's effects from "
              "2009 to 2024."),
            ST([C("Rs 3.48 lakh cr", "cumulative savings attributed to DBT in the assessment", "green",
                  "PIB, 21 April 2025, reporting BlueKraft Digital Foundation"),
                C("16% &rarr; 9%", "subsidies as a share of total expenditure, before DBT and in 2023&ndash;24", "cyan",
                  "PIB, 21 April 2025, reporting BlueKraft Digital Foundation"),
                C("11 cr &rarr; 176 cr", "beneficiaries covered before and after DBT", "indigo",
                  "PIB, 21 April 2025, reporting BlueKraft Digital Foundation")], cols=3),
            H("amber", "Read \"savings\" carefully: removing duplicate and fake beneficiaries saves "
              "money, but so does wrongly removing eligible ones. The next slides show both."),
        ]),

        S("Evidence on payments", "Biometric smartcards and e-invoicing: two Indian experiments", [
            B("Two large randomised evaluations show that payment reforms can cut leakage in "
              "Indian welfare programmes. Both were run with state governments at scale, which "
              "makes them unusually relevant to policy."),
            TC([P("green", "Smartcards, Andhra Pradesh",
                  "Muralidharan, Niehaus and Sukhtankar (AER 2016) randomised biometric "
                  "Smartcard payments for NREGS and social security pensions across 157 "
                  "subdistricts and 19 million people. Payments became faster, more predictable "
                  "and less corrupt, with less leakage, and access did not fall. Beneficiaries "
                  "preferred the new system.")],
               [P("cyan", "Just-in-time payments, India's workfare programme",
                  "Banerjee, Duflo, Imbert, Mathew and Pande (AEJ Applied 2020) replaced advance "
                  "fund releases with payments triggered by e-invoicing. Programme spending fell "
                  "24% with employment slightly up, officials' personal wealth fell 10%, but "
                  "payment delays rose. The national scale-up cut spending 19%.")]),
            H("amber", "Both studies report a trade-off to watch: technology can tighten control "
              "while adding delay or friction for workers."),
        ]),

        S("Exclusion", "When stricter verification shuts out eligible people", [
            B("Muralidharan, Niehaus and Sukhtankar also evaluated reforms that added stricter "
              "biometric identity checks to India's largest social protection programme (NBER "
              "Working Paper 26744, 2020). Corruption fell, but at a substantial cost to "
              "legitimate beneficiaries."),
            ST([C("1.5&ndash;2 million", "legitimate beneficiaries who lost access at some point "
                  "during the reforms", "red",
                  "Muralidharan, Niehaus and Sukhtankar, NBER WP 26744, 2020")], cols=1),
            TC([B("<strong>The authors' reading:</strong> the harm came mainly from how the "
                  "transition was managed, which shows how much the protocols around a new "
                  "technology matter.", sm=True)],
               [B("<strong>For programmes:</strong> track exclusion as carefully as leakage. "
                  "Count who was removed and check a sample at the door.", sm=True)]),
        ]),

        S("Last mile", "Phone calls as monitoring", [
            B("Monitoring does not always need inspectors. Muralidharan, Niehaus, Sukhtankar and "
              "Weaver (AEJ Applied 2021) tested phone-based monitoring of a programme that "
              "transferred nearly a billion dollars to 5.7 million Indian farmers. In randomly "
              "chosen areas, officials were told that implementation would be measured through "
              "calls to beneficiaries."),
            ST([C("7.8%", "reduction in farmers who did not receive their transfers", "green",
                  "Muralidharan, Niehaus, Sukhtankar and Weaver, AEJ Applied, 2021"),
                C("3.6 cents", "cost per additional dollar delivered", "cyan",
                  "Muralidharan, Niehaus, Sukhtankar and Weaver, AEJ Applied, 2021")], cols=2),
            TC([B("<strong>Why it worked:</strong> officials knew their performance would be "
                  "measured by beneficiaries, which changed the incentive along the chain.", sm=True)],
               [B("<strong>Adapting it:</strong> a programme can call a random sample of "
                  "beneficiaries monthly and share results with district officials.", sm=True)]),
        ]),

        S("Dashboards and portals", "Technology for transparency: what to expect", [
            B("New laws increasingly write technology into accountability. Section 24 of the "
              "VB-G RAM G Act 2025 lists biometric authentication of workers and transactions, "
              "geospatial planning with satellite imagery, mobile and dashboard monitoring of "
              "demand, works and payments, and weekly digital and physical disclosure of muster "
              "rolls, payments, sanctions, inspections and grievances."),
            TC([P("green", "What technology does well",
                  "Records become harder to alter after the fact. Data reach supervisors "
                  "quickly. Public dashboards let anyone compare areas. Geo-tagged photographs "
                  "make a missing asset easier to spot.")],
               [P("amber", "What it cannot do alone",
                  "Verify that a recorded worker was the real worker, or that a photographed "
                  "pond holds water. Help a citizen who cannot read a dashboard. Fix an error "
                  "that excludes someone when no human reviews it.")]),
            H("cyan", "Use dashboards as a starting point for field checks and social audits, and "
              "print the key figures for the gram sabha. Source: VB-G RAM G Act 2025, s24."),
        ]),

        # ===================== SECTION 10 =====================
        DIV("10", "Ten", "Putting it to work: a practitioner's toolkit"),

        S("Diagnostic", "An accountability diagnostic in ten questions", [
            B("Before designing any governance component, run this diagnostic for the service you "
              "care about. It takes a few days of document review and interviews, and it prevents "
              "the common mistake of applying a favourite tool to the wrong problem."),
            TC([BL(["What is the entitlement, in law or scheme guidelines, and does the user know it?",
                    "Who is the frontline provider, and who supervises them?",
                    "Which tier controls funds, functions and functionaries?",
                    "What records exist, and are they public under s4 or scheme rules?",
                    "Which relationship in the WDR triangle is weakest?"])],
               [BL(["Which horizontal agencies have looked at this service (CAG, commissions)?",
                    "What grievance channels exist, and how fast do they act?",
                    "Who benefits from the current failure?",
                    "Who is excluded from voice: women, SC and ST households, migrants?",
                    "What would a frontline worker say is the real constraint?"])]),
            H("green", "Write the answers on one page. Share it with officials and community "
              "partners before choosing tools."),
        ]),

        S("Decision table", "Matching the tool to the problem", [
            B("Once the diagnostic identifies the weak link, the choice of tool is easier. This "
              "table is a starting point drawn from the evidence in Sections 3 to 9; adapt it to "
              "your context."),
            T(["Diagnosis", "Tool to try first", "Evidence to read"],
              [["Providers absent or not working", "Unannounced visits with results shared with supervisors",
                "Chaudhury et al. 2006; Muralidharan et al. 2017"],
               ["Funds leak between treasury and beneficiary", "Payment reform, beneficiary phone checks",
                "Muralidharan et al. 2016, 2021; Banerjee et al. 2020"],
               ["Records falsified at local level", "Social audit with independent team",
                "VB-G RAM G Act s20; Andhra Pradesh SSAAT"],
               ["Citizens unaware of entitlements", "Information plus a forum and follow-up",
                "Banerjee et al. 2010; Bjorkman and Svensson 2009"],
               ["Officials refuse information", "RTI requests and appeals, s8(2) arguments",
                "RTI Act ss 6, 7, 8, 19"],
               ["Eligible people removed from lists", "Exclusion audit of deleted names",
                "Muralidharan, Niehaus and Sukhtankar 2020"]]),
            H("amber", "The table suggests where to start. A pilot with measurement tells you "
              "whether it works in your district."),
        ]),

        S("Worked example", "Illustrative: a ration shop that runs short", [
            B("Illustrative example (hypothetical figures). Families in a block report that their ration shop opens "
              "irregularly and gives less grain than entitled. A district NGO runs the "
              "diagnostic and finds: the dealer is related to the sarpanch, stock registers are "
              "not displayed, and complaints to the block supply officer go unanswered."),
            FL(["RTI for stock and distribution registers (s6)",
                "Compare with household survey of 100 cardholders",
                "Present findings at gram sabha with officials invited",
                "File grievances and track replies",
                "Share pattern with district supply officer"]),
            TC([P("green", "What success looks like",
                  "Registers displayed, shop hours posted and kept, verified receipt rising "
                  "between survey rounds, and a dealer replaced if irregularities continue.")],
               [P("amber", "What to watch",
                  "Retaliation against families who testified. Dealers shifting losses to "
                  "families least able to complain. Officials closing grievances without action.")]),
        ]),

        S("RTI drafting", "Writing an RTI request that gets an answer", [
            B("Many requests fail because they ask questions instead of asking for records, or "
              "because they ask for so much that the PIO can refuse as disproportionate. A good "
              "request is short, specific and tied to documents the authority already holds."),
            TC([P("red", "Weak request",
                  "\"Why has the road in our village not been built and who is responsible for "
                  "the corruption?\" This asks for opinions and conclusions, which the Act does "
                  "not oblige a PIO to create.")],
               [P("green", "Strong request",
                  "\"Please provide certified copies of the sanction order, measurement book "
                  "entries and payment vouchers for the road work in ward 4, gram panchayat X, "
                  "for 2025&ndash;26.\" Records, a place and a period.")]),
            BL(["Address the request to the right PIO and keep proof of filing and payment",
                "Ask for aggregate data where personal details are not needed, given the new s8(1)(j)",
                "Diarise day 30 for the reply and day 60 for the first appeal deadline",
                "Cite s4(1)(b) where the record should already be public"], color="cyan"),
        ]),

        S("Programme design", "Building accountability into a programme from the start", [
            B("Accountability works best when it is designed in from the start, before problems "
              "appear. Whether you run a government scheme or an NGO project, the same four "
              "commitments make your own delivery answerable to the people you serve."),
            T(["Commitment", "What to do", "How to check it is working"],
              [["Publish entitlements", "Post who is eligible, what they get and when, in local languages",
                "Spot checks that notices are up and readable"],
               ["Open records", "Share beneficiary lists (with privacy safeguards) and spending summaries",
                "Number of records requested and supplied"],
               ["Two-way channel", "Phone line, visits and meetings where complaints are logged",
                "Share of complaints resolved within a set time"],
               ["Independent check", "Periodic social audit or third-party verification",
                "Findings acted on within the next round"]]),
            H("indigo", "Apply the same standards to your own organisation that you ask of "
              "government. It builds trust and it is good practice."),
        ]),

        S("Measuring governance", "Governance indicators for your MEL framework", [
            B("Governance outcomes can be measured at programme level without relying on national "
              "indices. The indicators below are concrete, observable and can be collected by a "
              "monitoring team. Pick a few that match your theory of change."),
            T(["Level", "Indicator", "Data source"],
              [["Provider", "Share of unannounced visits where the provider is present and working", "Spot-check visits"],
               ["Delivery", "Share of listed beneficiaries confirming receipt of full entitlement", "Phone or household survey"],
               ["Transparency", "Share of required s4 or scheme disclosures actually displayed", "Site observation"],
               ["Voice", "Women and SC/ST attendance and speaking share at gram sabhas", "Meeting observation"],
               ["Responsiveness", "Median days to resolve logged grievances", "Programme grievance log"],
               ["Enforcement", "Share of social audit findings with recorded action", "Action-taken reports"]]),
            H("green", "See " + L("mel-basics.html", "MEL Basics 101") + " and " +
              L("toc-workbench.html", "Theory of Change 101") + " to fit these into a results "
              "framework."),
        ]),

        S("Data protection", "Handling personal data in accountability work", [
            B("Accountability work collects sensitive information: names on beneficiary lists, "
              "testimony about officials, caste and income details. The Digital Personal Data "
              "Protection Act 2023 commences in stages (G.S.R. 843(E), 13 November 2025): its core "
              "duties in ss 3&ndash;17 apply from 13 May 2027. Section 17(2)(b) will then exempt "
              "processing necessary for research, archiving or statistical purposes, but only if "
              "the data are not used to take a decision specific to an individual and follow "
              "prescribed standards. Monitoring that acts on named cases falls outside it."),
            TC([P("cyan", "Before collecting",
                  "Decide the minimum data needed. Seek informed consent. Explain who will see "
                  "testimony and how complainants will be protected.")],
               [P("green", "Before publishing",
                  "Aggregate by village or ward. Remove names unless the person agrees and the "
                  "public interest is clear. Store records securely and delete when no longer "
                  "needed.")]),
            H("amber", "Read " + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101")
              + " for the Act's duties and the s17(2)(b) conditions."),
        ]),

        S("Working with government", "Partnering with officials without losing independence", [
            B("Most practitioners need officials' cooperation to get records, run hearings and "
              "fix problems. Accountability work can sour that relationship if it feels like an "
              "ambush. It can also be co-opted if the organisation depends on the department it "
              "monitors. Both risks can be managed."),
            TC([P("green", "Build cooperation",
                  "Share the plan with district officials early. Present findings to them before "
                  "going public. Give credit when problems are fixed. Recognise officials who "
                  "respond well.")],
               [P("amber", "Protect independence",
                  "Do not accept funding from the department you audit for the same activity. "
                  "Publish methods and findings. Keep a written record of commitments made at "
                  "hearings and report back on them.")]),
            H("indigo", "See " + L("advocacy-basics.html", "Advocacy Basics 101") + " for "
              "building relationships with decision makers."),
        ]),

        # ===================== SECTION 11 =====================
        DIV("11", "Eleven", "State capacity, evidence and where next"),

        S("Flailing state", "Pritchett: is India a flailing state?", [
            B("In a 2009 Harvard Kennedy School working paper, Lant Pritchett argued that India's "
              "state is \"flailing\": its capable head, in the central ministries and elite "
              "services, is no longer reliably connected to the arms and legs of implementation. "
              "Using examples from health, education and routine tasks such as issuing driving "
              "licences, he showed agents of the state routinely failing to carry out assigned "
              "tasks, causing a large gap between de jure and de facto reality."),
            TC([P("indigo", "The image",
                  "Strong policy design and elite administration at the top; weak, poorly "
                  "monitored delivery at the bottom. The gap explains why good laws produce poor "
                  "services.")],
               [P("amber", "The implication",
                  "More schemes and more money do not fix a flailing state. Capacity to "
                  "implement must be built, measured and protected.")]),
            H("cyan", "Source: Pritchett, Is India a Flailing State?, Harvard Kennedy School "
              "Working Paper RWP09-013, 2009."),
        ]),

        S("Capability traps", "Isomorphic mimicry and premature load bearing", [
            B("Pritchett, Woolcock and Andrews (Center for Global Development Working Paper 234, "
              "2010) argued that many countries are in state capability traps: implementation "
              "capability is severely limited and improves, if at all, only very slowly. They "
              "named two techniques of failure. Andrews, Pritchett and Woolcock (World "
              "Development, 2013) proposed Problem-Driven Iterative Adaptation (PDIA) as a way out."),
            T(["Concept", "Meaning", "What to do instead"],
              [["Isomorphic mimicry", "Adopting the forms of functional states and organisations, which hides a lack of function",
                "Judge institutions by what they do"],
               ["Premature load bearing", "Placing demands on systems faster than their capability can grow, so capability weakens",
                "Sequence reforms; add load as capacity proves itself"],
               ["PDIA", "Solve locally named problems, encourage experiment, build fast feedback, involve many agents",
                "Start from a specific delivery problem, try and adapt"]]),
            H("amber", "Ask of any new commission, portal or law: who will run it, with what staff, "
              "and what happens when the load arrives?"),
        ]),

        S("Kapur", "Why does the Indian state both fail and succeed?", [
            B("Devesh Kapur (Journal of Economic Perspectives, 2020) observed that the Indian "
              "state's performance runs from woefully inadequate to surprisingly impressive. It "
              "does better on macroeconomic than microeconomic outcomes, on episodic tasks with a "
              "built-in end (elections, the Kumbh Mela, vaccination drives) than on daily "
              "delivery, and where social hierarchy matters less."),
            TC([P("indigo", "Three reasons Kapur gives",
                  "Under-resourced local governments. The long-term effects of India's "
                  "\"precocious\" democracy, which arrived before a capable state. The "
                  "persistence of social cleavage.")],
               [P("green", "Two myths he questions",
                  "Kapur finds weak basis for claims that India's state is bloated in size or "
                  "submerged in patronage. He also notes state capacity improving at the micro "
                  "level even as macro performance grew more worrying.")]),
            H("cyan", "Source: Kapur, Why Does the Indian State Both Fail and Succeed?, JEP 34(1), "
              "2020, 31&ndash;54. (The examples in brackets are illustrations of episodic tasks.)"),
        ]),

        S("Muralidharan", "Accelerating India's Development (2024)", [
            B("Karthik Muralidharan's book <em>Accelerating India's Development: A State-Led "
              "Roadmap for Effective Governance</em> (India Viking, February 2024) analyses "
              "India's governance problems, especially in delivering essential public services, "
              "and sets out evidence-based reforms with an emphasis on state governments. He is "
              "co-founder of the Centre for Effective Governance of Indian States (CEGIS)."),
            Q("Building a more effective state is the great unfinished task of Indian democracy.",
              "Publisher's description of the book's argument, Penguin India (India Viking), 2024"),
            TC([B("<strong>Core claim:</strong> quality public services translate the political "
                  "equality of one person, one vote into greater equality of opportunity.", sm=True)],
               [B("<strong>For practitioners:</strong> the book draws on many of the studies in "
                  "this course, including the teacher absence and payment experiments.", sm=True)]),
        ]),

        S("What works", "Summary of the evidence in this course", [
            B("The studies cited in this course point to a cautious summary. These are patterns "
              "across specific settings. None is a universal law, and each depends on implementation "
              "quality. Use them to form hypotheses for your own context, then test."),
            T(["Finding", "Supported by", "Caveat"],
              [["Monitoring with consequences reduces absence and leakage",
                "Muralidharan et al. 2017; Olken 2007; Muralidharan et al. 2021", "Monitor must be independent"],
               ["Payment technology can cut leakage at scale",
                "Muralidharan et al. 2016; Banerjee et al. 2020", "Watch delays and exclusion"],
               ["Information alone rarely changes providers",
                "Banerjee et al. 2010; Olken 2007", "Information plus a forum can work"],
               ["Organised community monitoring can improve services",
                "Bjorkman and Svensson 2009", "Context and how meetings are run matter"],
               ["Publishing audits changes elections",
                "Ferraz and Finan 2008", "Needs media reach"],
               ["Reserved leadership changes priorities",
                "Chattopadhyay and Duflo 2004", "Proxy rule remains a risk"]]),
            H("green", "Read " + L("impact-eval.html", "Impact Evaluation 101") + " before "
              "designing your own test of a governance intervention."),
        ]),

        S("Summary", "Ten points to take away", [
            B("Each point connects to a design choice, a legal duty or a measurement decision in "
              "programme work. Return to them when you review a programme's governance component."),
            BL(["Governance is how power is exercised; judge it by delivery on the ground.",
                "Accountability needs both answerability and enforcement.",
                "Use O'Donnell's vertical and horizontal, and the WDR's long and short routes, to diagnose.",
                "Absence and leakage are agency problems; monitoring with consequences helps.",
                "Measure corruption directly; perception indices cannot locate it.",
                "Decentralisation needs funds, functions and functionaries, and guards against capture.",
                "RTI: ss 4, 6, 7, 8, 19, 20; s8(1)(j) was rewritten by DPDP s44(3) from 13 November 2025.",
                "Social audit now rests on s20 of the VB-G RAM G Act 2025 and its rules.",
                "Agencies on paper (Lokpal, commissions) need appointments and staff to work.",
                "Technology can tighten control; track exclusion as closely as leakage."]),
            H("cyan", "Facts are stated as of October 2026. Check for later amendments and judgments."),
        ]),

        S("Where next", "Where next: related courses", [
            B("Governance connects to most other courses in the ImpactMojo 101 Series. These are "
              "the most direct next steps, chosen to deepen the constitutional law, the policy "
              "process, the politics and the money behind the topics in this deck."),
            TC([BL(["Articles, rights and remedies: " + L("ind-constitution.html", "Indian Constitution 101"),
                    "How policy is made and changed: " + L("public-policy-101.html", "Public Policy 101"),
                    "Interests, elites and capture: " + L("pol-economy.html", "Political Economy 101"),
                    "Budgets, grants and fiscal federalism: " + L("public-finance-budgeting.html", "Public Finance &amp; Budgeting 101"),
                    "Turning findings into change: " + L("advocacy-basics.html", "Advocacy Basics 101")])],
               [BL(["Running inclusive community processes: " + L("participatory-methods.html", "Participatory Methods 101"),
                    "Personal data and RTI: " + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101"),
                    "Rights frameworks: " + L("human-rights.html", "Human Rights 101"),
                    "Testing what works: " + L("impact-eval.html", "Impact Evaluation 101"),
                    "Global institutions: " + L("dev-architecture.html", "Global Development Governance 101")])]),
            H("green", "All courses are free. Start with Indian Constitution 101 if you need the "
              "legal foundations, or Political Economy 101 for the incentives behind them."),
        ]),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Governance &amp; Accountability 101 &middot; Complete",
         "headline": "Find the broken link,<br>then make someone answer",
         "byline": "Good laws and full budgets are not enough. Diagnose which accountability "
                   "relationship has failed, choose the tool that fits, measure delivery "
                   "directly, and protect the people who speak up. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

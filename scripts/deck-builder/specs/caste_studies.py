# -*- coding: utf-8 -*-
"""
Caste Studies 101: ImpactMojo 101 Series (native deck spec)
Caste as a structure of inequality, for development practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py caste_studies

Sources opened while writing (October 2026):
- Census of India 2011, SC and ST data highlights (ORGI, 30 April 2013):
  https://www.indiaspend.com/wp-content/uploads/2020/09/INDIA_CENSUS_ABSTRACT-2011-Data_on_SC-STs.pdf
- PIB backgrounder on Census 2027 (April 2026):
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/apr/doc2026425856601.pdf
- All India Radio, Bihar caste survey findings, 2 October 2023:
  https://newsonair.gov.in/bihar-govt-releases-findings-of-its-caste-based-survey-obcs-and-ebcs-comprise-more-than-63-of-states-population
- Supreme Court record of proceedings, State of Punjab v Davinder Singh, 1 August 2024:
  https://api.sci.gov.in/supremecourt/2010/25536/25536_2010_1_1501_54462_Order_01-Aug-2024.pdf
- Verdictum on the creamy layer opinions in Davinder Singh:
  https://www.verdictum.in/court-updates/supreme-court/2024-insc-562-state-of-punjab-v-davinder-singh-creamy-layer-scheduled-caste-tribe-1546270
- The Tribune, Union Cabinet on creamy layer, 9 August 2024:
  https://www.tribuneindia.com/news/india/union-cabinet-says-no-to-creamy-layer-for-scs-and-sts
- Constitution text, Articles 15, 16, 46, 330, 332, 334, 338, 338A, 341:
  https://www.constitutionofindia.net/articles/article-15/ (and sibling pages)
- Ministry report under s15A(4) PCR Act for 2013 (Article 17 text, PCR history and sections):
  https://socialjustice.gov.in/writereaddata/UploadFile/arpcr13.pdf
- SC/ST (Prevention of Atrocities) Amendment Act 2015, as enacted (sections 4, 8, 11):
  https://www.advocatekhoj.com/library/bareacts/scheduledcastesandtribes2015/index.php
- MSJE notification bringing the 2015 amendment into force on 26 January 2016:
  https://socialjustice.gov.in/writereaddata/UploadFile/Notification-PoA%20Amendment%20Act%202015636010028571445794.pdf
- SC/ST (Prevention of Atrocities) Amendment Act 2018 (No. 27 of 2018, 17 August 2018), text:
  https://bnblegal.com/bareact/sc-st-prevention-of-atrocities-amendment-act-2018/
- Constitution of India as on 1 May 2024 (Legislative Department): Articles 15, 16, 17, 46, 243D, 334, 338A, 338B, 341, 342A
  https://lddashboard.legislative.gov.in/sites/default/files/coi/COI_2024.pdf
- Indra Sawhney v Union of India, 16 November 1992 (full text, incl. Mandal figures 3,743 and 52%):
  https://indiankanoon.org/doc/1363234/
- Mandal Commission report, Vols I-II (scan): https://archive.org/details/PARI.report-of-the-backward-classes-commission-volumes-i-and-ii
- Gazette, Prohibition of Employment as Manual Scavengers Act 2013 (No. 25 of 2013, assent 18 September 2013):
  https://www.mahapolice.gov.in/uploads/protection_civil_rights/pcr5.pdf
- Gazette S.O. 4505(E), 14 August 2026, Census 2027 Household Schedule questions (item 10 caste):
  (Gazette No. CG-DL-E-14082026-275454; read in full from the copy at https://images.assettype.com/deccanherald/2026-08-14/e3cvxla0/e_gazette.pdf)
- PIB text of Lok Sabha reply on sewer deaths 2021 to June 2026 (via India Education Diary, July 2026):
  https://indiaeducationdiary.in/332-sanitation-worker-deaths-reported-in-18-states-uts-due-to-hazardous-sewer-and-septic-tank-cleaning-between-january-2021-and-june-2026/
- DPDP Act 2023 text (s17(2)(b)); commencement in phases under G.S.R. 843(E), 13 November 2025
- Kumar Cheda Singh Varma, Kshatriyas and Would-be Kshatriyas (Allahabad, 1904), scan:
  https://archive.org/details/kshatriyaswouldbekshatriyaskumarchedasinghvarma1904_202003_664_a
- Constitution of Nepal 2015, Articles 24 and 40 (Constitute Project translation)
- The Hindu via Catholic Connect, June 2026, Balakrishnan Commission report ready:
  https://catholicconnect.in/news/report-on-sc-status-for-dalit-christians-and-muslims-ready-for-submission
- Supreme Court Observer, Prathvi Raj Chauhan v Union of India:
  https://www.scobserver.in/cases/prithvi-raj-chauhan-union-of-india-legality-of-sc-st-act-amendment-case-background/
- gconnect.in, DoPT compendium on reservation percentages:
  https://www.gconnect.in/orders-in-brief/reservation/provisions-scs-sts-obcs-compendium-instructions-reservation.html
- LiveLaw, Balram Singh v Union of India, 20 October 2023:
  https://www.livelaw.in/amp/supreme-court/completely-eradicate-manual-scavenging-supreme-court-directs-union-states-increases-compensation-for-sewer-deaths-to-rs-30-lakh-240650
- Business Standard, 5 August 2026, Lok Sabha reply on sewer deaths:
  https://www.business-standard.com/india-news/sanitation-workers-sewer-septic-tank-cleaning-deaths-since-2019-126080500881_1.html
- Ambedkar, Castes in India (1916), text: https://franpritchett.com/00ambedkar/txt_ambedkar_castes.html
- Ambedkar, Annihilation of Caste (1936), text:
  https://sa.theanarchistlibrary.org/library/ambedkar-annihilation-of-caste
- Princeton University Press, Dirks, Castes of Mind: https://press.princeton.edu/books/paperback/9780691088952/castes-of-mind
- Britannica, Jyotirao Phule: https://www.britannica.com/biography/Jyotirao-Phule
- Anderson (2011) AEJ Applied 3(1): 239-263, UBC copy:
  https://econ.cms.arts.ubc.ca/wp-content/uploads/sites/38/2013/05/pdf_paper_siwan-anderson-caste-impediment-trade.pdf
- Hoff and Pandey, World Bank WPS 3351 abstract: https://ideas.repec.org/p/wbk/wbrwps/3351.html
- Pande (2003) AER abstract: https://ideas.repec.org/a/aea/aecrev/v93y2003i4p1132-1151.html
- Iyer, Khanna and Varshney, Ideas for India: https://www.ideasforindia.in/topics/social-identity/caste-and-entrepreneurship-in-india.html
- GSDRC summary of Thorat, Attewell and Rizvi: https://gsdrc.org/document-library/urban-labour-market-discrimination/
- Thread quoting Thorat and Attewell's sample: https://threadreaderapp.com/thread/1224607460918427649
- IHDS-II untouchability findings: https://homegrown.co.in/homegrown-explore/untouchability-is-still-widely-practised-in-india-says-recent-caste-survey-findings
- Morung Express on the Centre's SECC affidavit (September 2021):
  https://morungexpress.com/secc-2011-caste-data-unreliable-several-entries-had-numbers-symbols-centre-told-sc
- TaxTMI, SECC rural release 3 July 2015: https://www.taxtmi.com/news?id=14663
- Gazette, Constitution (Scheduled Castes) Orders (Amendment) Act 1990:
  https://socialjustice.gov.in/public/ckeditor/upload/48021673325306.pdf
- Verdictum, Balakrishnan Commission: https://www.verdictum.in/news/kg-balakrishnan-inquiry-commission-scheduled-caste-converts-1442284
- Supreme Court Observer, Ghazi Saaduddin: https://www.scobserver.in/cases/ghazi-saaduddin-v-state-of-maharashtra-constitutionality-of-the-constitution-scheduled-caste-order/
- DanChurchAid on Nepal Census 2021 Dalit report: https://www.danchurchaid.org/data-for-evidence-based-advocacy-dalit-lives-matter
- Kathmandu Post, 9 January 2025: https://kathmandupost.com/opinion/2025/01/09/constitutionand-the-status-of-dalits
- Bipin Adhikari on Nepal's 2011 Act: https://bipinadhikari.com.np/2011/05/03/caste-based-discrimination-and-untouchability-offence
- Dawn, 19 May 2021, Pakistan Census 2017 religion data: https://www.dawn.com/news/amp/1624375
- Financial Express (Dhaka), Anti-Discrimination Bill 2022:
  https://old.thefinancialexpress.com.bd/national/anti-discrimination-bill-placed-in-parliament-1649160244?amp=true
- Sri Lanka Prevention of Social Disabilities Act (Cap. 33): https://lankalaw.net/wp-content/uploads/2024/03/posd33370.pdf
- Not reopened against a primary source (standard reference facts, listed as weakly sourced in the
  fact-check report): Delimitation Order 2008 seat counts; Mahad 1927; Nagpur 1956; Dalit Panthers 1972;
  BSP 1984; PESA 1996; Forest Rights Act dates; Rohith Vemula 2016
- Drishti IAS, Santhal Hul of 1855
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


DECK = {
    "slug": "caste-studies",
    "title": "Caste Studies 101",
    "description": ("Caste Studies 101: a free foundational course for development practitioners "
                    "and researchers in South Asia. Caste as a structure of inequality: varna and "
                    "jati, the colonial census, Phule and Ambedkar, Article 17 and the atrocities "
                    "law, reservations from Indra Sawhney to Davinder Singh, caste in land and "
                    "labour markets, the SECC, the Bihar survey and Census 2027, caste in Nepal, "
                    "Pakistan, Bangladesh and Sri Lanka, and how to work on caste ethically. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Caste<br>Studies<br>101",
         "sub": "Caste as a structure of inequality: history, law, economics and data, a "
                "foundational course for development practitioners and researchers in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Law &amp; Evidence"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Why caste belongs in development practice"},
             {"name": "Varna, jati and how caste works"},
             {"name": "Histories: census, colony and scholarship"},
             {"name": "Phule, Ambedkar and the anti-caste tradition"},
             {"name": "Untouchability and the criminal law"},
             {"name": "The Constitution and reservations"},
             {"name": "Caste in the economy"},
             {"name": "Counting caste: data and its limits"},
             {"name": "Beyond Hindu India and beyond India"},
             {"name": "Working on caste in programmes and research"},
             {"name": "Movements, open questions and where next"},
         ]},

        # ===================== SECTION 01 =====================
        DIV("01", "One", "Why caste belongs in development practice"),

        S("Starting point", "Caste is a structure, and structures shape outcomes", [
            B("Most development programmes in South Asia measure poverty by income, consumption, "
              "land or schooling. Each of those is shaped by caste. Who owns irrigated land in a "
              "village, who gets called for a job interview in a city, who cleans a septic tank "
              "and who sits on the panchayat are questions with caste answers. A practitioner who "
              "treats caste as background culture will misread the evidence in front of them."),
            TC([P("amber", "Caste as culture",
                  "Treated as custom, ritual or personal belief. The programme stays neutral and "
                  "assumes the benefit reaches everyone equally. Differences in uptake are put "
                  "down to awareness or attitude, and nobody asks who controls the access point.")],
               [P("green", "Caste as structure",
                  "Treated as a durable system that allocates land, occupations, marriage, "
                  "residence and respect by birth. The programme asks who is excluded, by whom, "
                  "through which institution, and designs delivery and measurement around that.")]),
            H("cyan", "This course takes the second view. It is the view of the Constitution of "
              "India, of Ambedkar, and of most of the empirical economics reviewed later."),
        ]),

        S("Scale", "How many people are we talking about?", [
            B("The Census of India counts two groups defined by the Constitution: Scheduled Castes "
              "(SCs) and Scheduled Tribes (STs). In 2011 they made up a quarter of the population. "
              "These are counts of people in notified lists, which is why later sections treat "
              "them as legal categories as much as social ones."),
            ST([C("201.4 million", "Scheduled Castes in 2011, 16.6% of India's population", "cyan",
                  "Census of India 2011, SC/ST data highlights, ORGI, 30 April 2013"),
                C("104.3 million", "Scheduled Tribes in 2011, 8.6% of the population", "green",
                  "Census of India 2011, SC/ST data highlights, ORGI, 30 April 2013"),
                C("1,241", "distinct groups notified as Scheduled Castes across 31 states and UTs", "amber",
                  "Census of India 2011, SC/ST data highlights, ORGI, 30 April 2013"),
                C("705", "groups notified as Scheduled Tribes across 30 states and UTs", "indigo",
                  "Census of India 2011, SC/ST data highlights, ORGI, 30 April 2013")], cols=4),
            H("amber", "Other Backward Classes (OBCs) have no Census count since 1931. That gap is "
              "why the 2023 Bihar survey and the 2027 Census matter so much (Section 8)."),
        ]),

        S("Three questions", "Three questions to bring to any programme", [
            B("You do not need to be a sociologist to work responsibly on caste. You need three "
              "questions and the habit of asking them at design, delivery and evaluation. Each one "
              "turns an abstract concern into something a programme team can check in the field "
              "and record in its monitoring data."),
            T(["Question", "What it reveals", "Example from the field"],
              [["Who is in the data and who is missing?", "Coverage and sampling gaps by caste",
                "A household survey lists hamlets from the panchayat office and misses the Dalit "
                "basti on the edge of the village"],
               ["Who controls the access point?", "Gatekeeping by dominant groups",
                "A self-help group meets in an upper-caste courtyard that some members will not enter"],
               ["Who benefits, measured separately?", "Whether averages hide caste gaps",
                "Average yields rise while SC tenants see no change because they buy water from "
                "upper-caste pump owners"]]),
            H("green", "The rest of this course gives you the history, law and evidence to answer "
              "these questions with confidence."),
        ]),

        S("A common mistake", "Caste is about more than the poorest", [
            B("Programmes often reach caste only through poverty targeting: if the poorest are "
              "served, caste will take care of itself. The evidence reviewed in Section 7 shows "
              "why that fails. Dalit graduates with the same qualifications as upper-caste "
              "graduates receive fewer interview calls. SC and ST entrepreneurs own far fewer "
              "enterprises than their population share. Caste affects people at every income level."),
            TC([P("red", "Poverty-only lens",
                  "Misses discrimination against educated, urban or salaried Dalits and Adivasis. "
                  "Cannot explain why an SC household with the same income has less land, fewer "
                  "networks and less credit than an upper-caste neighbour.")],
               [P("green", "Caste-aware lens",
                  "Asks about assets, networks, occupational segregation, violence and dignity "
                  "alongside income. Disaggregates every outcome by caste category, and treats "
                  "social exclusion as a cause of poverty in its own right.")]),
            H("indigo", "Inequality frameworks that separate group inequality from individual "
              "inequality are covered in " + L("inequality-basics.html", "Inequality Basics 101") + "."),
        ]),

        S("Terms", "Words you will meet, and how to use them", [
            B("Language about caste carries history. Several words in common use are slurs, and "
              "official categories differ from the names communities choose for themselves. Use "
              "the legal category when you mean the legal category, and the self-chosen name when "
              "you are describing people and movements."),
            T(["Term", "Meaning", "Usage note"],
              [["Scheduled Castes (SCs)", "Castes notified by the President under Article 341",
                "A legal category; membership is decided by a notified list"],
               ["Dalit", "Self-chosen political name meaning 'broken' or 'oppressed'",
                "Taken up as a political name by the Dalit Panthers (founded 1972); widely preferred today"],
               ["Scheduled Tribes (STs)", "Communities notified under Article 342",
                "Legal category; many prefer Adivasi, meaning original inhabitants"],
               ["OBCs", "Socially and educationally backward classes",
                "Central and state lists differ; a caste can be OBC in one state only"],
               ["Savarna", "Castes inside the four varnas", "Used in scholarship to name dominant groups"]]),
            H("red", "Never use caste names as insults or in jokes, and never write a person's caste "
              "into a report unless they have consented and it is needed for the analysis."),
        ]),

        S("Roadmap", "How this course is built", [
            TC([P("cyan", "Ideas and history",
                  "Section 2 sets out varna and jati. Section 3 follows colonial classification "
                  "and the scholarship of Srinivas and Dirks. Section 4 reads Phule and Ambedkar, "
                  "whose analysis of caste is still the most useful starting point for practice.")],
               [P("green", "Law, economics and data",
                  "Sections 5 and 6 cover untouchability law and the constitutional framework, "
                  "including reservations and the case law to 2024. Section 7 reviews the economic "
                  "evidence. Section 8 explains what the Census, the SECC and the Bihar survey can "
                  "and cannot tell you.")]),
            TC([P("amber", "Region",
                  "Section 9 looks at caste among Christians, Muslims and Sikhs in India, and in "
                  "Nepal, Pakistan, Bangladesh and Sri Lanka, each with its own law and politics.")],
               [P("indigo", "Practice",
                  "Section 10 turns all of this into checklists, a decision table and a worked "
                  "example for programme and research teams. Section 11 closes with movements, "
                  "open debates and further courses.")]),
            H("cyan", "Dates and legal positions are stated as of October 2026. Law in this area "
              "changes often, so check for later judgments before relying on any slide in court."),
        ]),

        # ===================== SECTION 02 =====================
        DIV("02", "Two", "Varna, jati and how caste works"),

        S("Two words", "Varna and jati are different things", [
            B("Discussions of caste often slide between two Sanskrit terms. Keeping them apart "
              "removes a great deal of confusion, because most of the inequality a practitioner "
              "meets operates through jati, while most popular explanations of caste talk about varna."),
            TC([TERM("Varna", "A fourfold scheme found in Brahmanical texts: Brahmin, Kshatriya, "
                     "Vaishya and Shudra, with groups outside the scheme treated as untouchable. "
                     "It is a theory of ranked social order, written down by priests.")],
               [TERM("Jati", "The endogamous birth group people actually belong to, numbering in "
                     "the thousands and specific to a region. Jatis marry within themselves, often "
                     "carry an occupational name, and rank themselves against neighbours.")]),
            H("cyan", "The 2011 Census lists 1,241 groups notified as Scheduled Castes alone. No "
              "four-part scheme can describe that, which is why researchers work with jati, and "
              "why data on varna alone is of little use for programme design."),
        ]),

        S("Mechanism", "Endogamy is the core of the system", [
            B("In 1916, as a doctoral student at Columbia University, B. R. Ambedkar argued that "
              "the defining feature of caste is endogamy: marriage only within the group. "
              "Occupation, ritual rank and food rules all vary across regions. The rule that a "
              "person marries inside the jati is what reproduces the group, generation after "
              "generation, and keeps its boundaries closed."),
            Q("Thus the superposition of endogamy on exogamy means the creation of caste.",
              "B. R. Ambedkar, Castes in India: Their Mechanism, Genesis and Development, paper read "
              "at Columbia University, 9 May 1916; printed in Indian Antiquary, May 1917"),
            H("amber", "For practice this matters because endogamy keeps assets, networks and "
              "status inside the group. Inter-caste marriage remains rare: about 5% of marriages "
              "were inter-caste in the India Human Development Survey (IHDS-II, 2011-12), as "
              "reported in 2014 and republished by NCAER."),
        ]),

        S("Five features", "What a jati system does in everyday life", [
            B("Sociologists describe caste through a set of linked features. Not every region shows "
              "all of them with equal force, and each has weakened or changed form in cities. "
              "Together they explain why caste outlasts changes in law and income."),
            T(["Feature", "How it works", "Where a programme meets it"],
              [["Endogamy", "Marriage within the jati", "Women's mobility, dowry, honour violence"],
               ["Hierarchy", "Groups rank themselves above and below others",
                "Who will eat with whom at a training lunch"],
               ["Hereditary occupation", "Some work is assigned by birth",
                "Sanitation, leather and funeral work concentrated among Dalit castes"],
               ["Purity and pollution", "Touch, food and water treated as polluting",
                "Separate seating, cups or water points at a health centre"],
               ["Spatial segregation", "Separate hamlets or streets",
                "A road, tap or anganwadi placed in the main village only"]]),
            H("green", "Ask which of these features is active in the place you work. The answer "
              "differs between a Bihar village, a Chennai slum and a Nepali hill district."),
        ]),

        S("Untouchability", "Untouchability is the extreme form, and it persists", [
            B("Untouchability is the practice of treating some castes as ritually polluting, so "
              "that their touch, shadow, food or water is avoided. It shows up as refused entry to "
              "temples and homes, separate vessels in tea shops and exclusion from common wells. "
              "The India Human Development Survey asked whether anyone in the family practised "
              "it and, if not, whether an SC person could enter the kitchen or use the family's "
              "utensils. A household counts as practising if it said yes to the first question or no "
              "to the second."),
            ST([C("27%", "of households across India reported practising untouchability on that two-question test", "red",
                  "IHDS-II 2011-12 (NCAER and University of Maryland), over 42,000 households; "
                  "as reported by The Indian Express, November 2014, and republished by NCAER"),
                C("52%", "of Brahmin respondents, the highest of any caste group", "amber",
                  "IHDS-II 2011-12, as reported by The Indian Express, November 2014"),
                C("33%", "of OBC respondents", "indigo",
                  "IHDS-II 2011-12, as reported by The Indian Express, November 2014")], cols=3),
            H("cyan", "Self-reports probably understate practice, because the question asks people "
              "to admit conduct that is an offence under the Protection of Civil Rights Act 1955."),
        ]),

        S("Regional variation", "The same question gives very different answers by state", [
            B("Averages hide a wide spread. In the IHDS-II data, admitted practice of "
              "untouchability was highest in the Hindi-speaking north and centre and lowest in "
              "West Bengal and Kerala. Practice was also reported within groups that are themselves "
              "discriminated against: 15% of SC and 22% of ST respondents admitted to it, which "
              "shows how deeply graded hierarchy runs."),
            {"t": "chart", "canvas": "ihdsStateChart",
             "title": "Households admitting to practising untouchability, selected states (%)",
             "source": "IHDS-II 2011-12 (NCAER and University of Maryland), as reported by The Indian Express, November 2014, and republished by NCAER",
             "type": "bar",
             "data": {"labels": ["Madhya Pradesh", "Himachal Pradesh", "Chhattisgarh", "Rajasthan",
                                 "Bihar", "Uttar Pradesh", "Andhra Pradesh", "Maharashtra", "Kerala",
                                 "West Bengal"],
                      "datasets": [{"label": "% of households", "data": [53, 50, 48, 47, 47, 43, 10, 4, 2, 1],
                                    "backgroundColor": "#0EA5E9"}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'% of households'} } } }"}},
        ]),

        S("Graded inequality", "Every group has someone below it", [
            B("Ambedkar described caste as a system of graded inequality: each group is "
              "subordinated to those above it and placed above others below it. This gives almost "
              "every group a stake in the order, which is one reason caste is hard to dismantle "
              "and why solidarity across oppressed castes has been difficult to build."),
            Q("The Caste System is not merely a division of labourers which is quite different "
              "from division of labour ... it is a hierarchy in which the divisions of labourers are "
              "graded one above the other.",
              "B. R. Ambedkar, Annihilation of Caste, 1936, section 4"),
            TC([P("amber", "For programme design",
                  "A Dalit beneficiary group is rarely homogeneous. Some SC jatis have gained more "
                  "from education and reservation than others, a fact at the centre of the 2024 "
                  "sub-classification judgment (Section 6).")],
               [P("indigo", "For research",
                  "Report results by jati where samples allow, or at least by SC, ST, OBC and "
                  "others. A single 'SC' average may hide one group doing well and another not.")]),
        ]),

        S("Change and continuity", "Caste changes form without disappearing", [
            B("Urbanisation, schooling, migration and the market have loosened many caste rules. "
              "Few people now enforce occupational rules strictly, and inter-dining is common in "
              "cities. Yet the features that matter most for inequality, endogamy, unequal "
              "land ownership and network-based hiring, have proved durable. Caste also became a "
              "basis for political mobilisation and for claims on the state after 1950."),
            T(["What weakened", "What persisted", "What grew"],
              [["Hereditary occupation for most castes", "Endogamy", "Caste associations and parties"],
               ["Ritual rules on food in cities", "Land concentration in dominant castes", "Caste-based claims for reservation"],
               ["Open legal disabilities", "Segregated residence in villages", "Dalit and Adivasi middle classes"],
               ["Some temple exclusion", "Sanitation work by Dalit castes", "Online caste networks and matrimonial sites"]]),
            H("cyan", "When someone says caste is disappearing, ask which feature they mean."),
        ]),

        # ===================== SECTION 03 =====================
        DIV("03", "Three", "Histories: census, colony and scholarship"),

        S("Why history", "How caste came to be counted shapes the data we use", [
            B("Every caste category in current data has a history. The lists of Scheduled Castes "
              "descend from colonial lists of 'depressed classes'. The idea that caste can be "
              "ranked on a single national ladder was pushed hard by the colonial census. Knowing "
              "this history makes you a more careful user of caste data, and helps explain why "
              "communities contest their classification so fiercely."),
            FL(["Pre-colonial: many local hierarchies, varied by region and kingdom",
                "1871 onward: colonial censuses record caste for every household",
                "1901: census attempts a national ranking of castes",
                "1950: Constitution creates SC and ST lists for protection",
                "2027: caste enumeration returns to the Census"]),
            H("amber", "Section 8 returns to the 2027 Census. Here the question is how the "
              "colonial state turned caste into an administrative category."),
        ]),

        S("Risley and 1901", "The 1901 Census tried to rank every caste", [
            B("As Census Commissioner for 1901, Herbert Hope Risley directed that a scheme be "
              "drawn up classifying Hindu castes under the four varnas and assigning each a place "
              "by social precedence. Risley also used anthropometry, including the nasal index, to "
              "argue that caste was based on race. Modern historians treat that racial theory as "
              "pseudo-science."),
            Q("The members of certain castes which have, hitherto, in an undefined sort of way, "
              "been striving to rise in the social scale eagerly seized the opportunity thus "
              "afforded them of having their pretensions to a higher status placed on record.",
              "Kumar Cheda Singh Varma, Kshatriyas and Would-be Kshatriyas (Allahabad: Pioneer "
              "Press, 1904), introduction, on the 1901 Census"),
            H("cyan", "The effect was to make the census a site of caste politics. Groups petitioned "
              "to be recorded under higher names. The lesson for today: a category in an official "
              "form invites people to organise around it."),
        ]),

        S("Dirks", "Castes of Mind: colonial rule remade caste", [
            B("Nicholas Dirks, in <em>Castes of Mind: Colonialism and the Making of Modern India</em> "
              "(Princeton University Press, 2001), argues that caste as a single, all-India system "
              "is a modern product of the encounter with British rule. Dirks accepts that caste "
              "existed before British rule. He argues that census-taking, ethnography and law made "
              "caste the master category for describing and governing Indian society."),
            TC([P("cyan", "What Dirks contributes",
                  "Attention to how classification creates the thing it claims to describe. "
                  "Colonial administrators used caste lists to recruit soldiers, define 'criminal "
                  "tribes' and settle land, which gave caste identities legal weight.")],
               [P("amber", "The main criticism",
                  "Critics, including scholars in the Ambedkarite tradition, argue that stressing "
                  "colonial construction can underplay the long history of untouchability in "
                  "Brahmanical texts and village practice, well before the British arrived.")]),
            H("green", "Hold both points: caste predates colonial rule, and colonial rule changed "
              "how caste was recorded, ranked and used by the state."),
        ]),

        S("Srinivas", "Sanskritisation: mobility within the system", [
            B("M. N. Srinivas, working on Coorg in Karnataka, introduced the term sanskritisation "
              "in <em>Religion and Society among the Coorgs of South India</em> (1952). In <em>Social "
              "Change in Modern India</em> (1966) he defined it as the process by which a low caste, "
              "a tribe or another group changes its customs, ritual, ideology and way of life in the "
              "direction of a high, frequently twice-born caste, usually followed by a claim to a "
              "higher position."),
            TERM("Sanskritisation", "The process by which a lower-ranked group adopts the "
                 "practices of higher castes, such as vegetarianism, Sanskritic rituals or "
                 "restrictions on women's work, to claim higher status. It changes a group's "
                 "position without changing the hierarchy itself."),
            H("amber", "For gender programmes this is directly relevant: sanskritisation has often "
              "meant withdrawing women from paid work outside the home as a marker of status, "
              "which shows up in labour force data. See " + L("wee-studies.html", "Women's Economic Empowerment 101") + "."),
        ]),

        S("Dominant caste", "Dominance comes from land and numbers", [
            B("Srinivas also coined the idea of the <strong>dominant caste</strong> from his "
              "fieldwork in Rampura, a village near Mysore. A dominant caste is one that is "
              "numerically strong in a locality and holds preponderant economic and political "
              "power, above all through land. Srinivas first defined the term in 1955 and set it "
              "out fully in 'The Dominant Caste in Rampura', <em>American Anthropologist</em> 61(1), 1959."),
            TC([P("green", "Examples practitioners meet",
                  "Jats in parts of Haryana and western Uttar Pradesh, Marathas in Maharashtra, "
                  "Vokkaligas and Lingayats in Karnataka, and Yadavs in parts of Bihar hold local "
                  "dominance in many villages despite middle ritual rank.")],
               [P("red", "Why it matters for delivery",
                  "Panchayat leaders, input dealers, water sellers and moneylenders often come from "
                  "the dominant caste. A programme that routes benefits through local elites "
                  "routes them through the dominant caste.")]),
            H("cyan", "Siwan Anderson's 2011 study of villages in a poor region of rural India, "
              "reviewed in Section 7, defines dominance by majority land ownership, the definition "
              "later stressed by Dumont."),
        ]),

        S("Other lenses", "Four ways scholars have read caste", [
            B("No single theory explains caste. Each lens below draws attention to something real "
              "and misses something else. Practitioners can use them as a checklist of mechanisms "
              "to look for, without having to settle the debates."),
            T(["Lens", "Core claim", "Associated work", "What it misses"],
              [["Purity and hierarchy", "Caste is a religious ranking by purity",
                "Louis Dumont, Homo Hierarchicus (English edition 1970)", "Power, land and resistance"],
               ["Power and land", "Caste is sustained by control of land and labour",
                "Srinivas on dominant caste", "Ritual and identity in cities"],
               ["Colonial construction", "Modern caste was shaped by colonial rule",
                "Dirks, Castes of Mind (2001)", "Pre-colonial untouchability"],
               ["Anti-caste critique", "Caste is graded inequality sustained by endogamy and scripture",
                "Phule (1873), Ambedkar (1916, 1936)", "Little; it is the most practice-oriented"]]),
            H("amber", "Dumont's purity-centred reading is contested. Anderson (2011) notes that "
              "Dumont also held that local dominance arises from economic power, through control of land."),
        ]),

        S("From colony to Constitution", "Depressed classes, separate electorates and the Poona Pact", [
            B("In August 1932 the British government's Communal Award offered the 'depressed "
              "classes' separate electorates. Gandhi began a fast unto death against it. On 24 "
              "September 1932 the Poona Pact, signed by Ambedkar, Gandhi's associates and other "
              "Hindu leaders, replaced separate electorates with seats reserved for the depressed "
              "classes within a joint electorate."),
            TC([P("cyan", "Separate electorate",
                  "Only voters from the group elect the group's representative. Ambedkar argued "
                  "this was the only way to produce representatives answerable to Dalits rather "
                  "than to upper-caste voters.")],
               [P("amber", "Reserved seat, joint electorate",
                  "Only a member of the group may stand, but everyone in the constituency votes. "
                  "This is the system Articles 330 and 332 adopted in 1950 and that operates today.")]),
            H("indigo", "The trade-off between representation and accountability returns in "
              "Section 6, with Rohini Pande's evidence on what reserved seats deliver."),
        ]),

        S("Lessons", "What history teaches the practitioner", [
            B("History is a working tool here. The categories in a 2026 baseline survey come from "
              "1901 enumeration methods, 1950 presidential orders and decades of litigation. "
              "Knowing this changes how you design questions, how you code answers and how you "
              "interpret change over time."),
            BL(["<strong>Categories are made</strong>: SC, ST and OBC lists are legal artefacts that "
                "change by order and by Act of Parliament; record the list version you used.",
                "<strong>Classification is political</strong>: communities seek inclusion or "
                "reclassification because categories carry rights; expect contested answers.",
                "<strong>Local rank varies</strong>: a jati can be dominant in one district and "
                "marginal in another; avoid national rankings.",
                "<strong>Counting changes behaviour</strong>: the 1901 petitions are the classic case; "
                "your survey can also signal which identities matter.",
                "<strong>Self-identification beats imputation</strong>: inferring caste from surnames "
                "is error-prone and can be harmful."]),
            H("green", "Keep these five in mind when you reach the data section."),
        ]),

        # ===================== SECTION 04 =====================
        DIV("04", "Four", "Phule, Ambedkar and the anti-caste tradition"),

        S("Phule", "Jotirao Phule: education and the critique of Brahmanism", [
            B("Jotirao Phule (1827-1890), born into a Mali farming family in Maharashtra, built the first "
              "sustained modern movement against caste. In 1848 he and Savitribai Phule began a "
              "school for girls from lower castes, with Savitribai teaching. In 1873 he published "
              "<em>Gulamgiri</em> (Slavery), which compared the condition of lower castes to "
              "slavery in America, and founded the Satyashodhak Samaj (Society of Truth Seekers)."),
            ST([C("1848", "school for lower-caste girls opened by Jotirao and Savitribai Phule", "cyan", "Encyclopaedia Britannica, Jyotirao Phule"),
                C("1873", "Gulamgiri published and Satyashodhak Samaj founded", "green", "Encyclopaedia Britannica, Jyotirao Phule"),
                C("Mali", "Phule's own caste, a farming community", "amber", "Encyclopaedia Britannica, Jyotirao Phule")], cols=3),
            H("cyan", "Phule linked caste, gender and education decades before these became policy "
              "categories. His opening of his own well to all castes was a direct challenge to "
              "untouchability."),
        ]),

        S("Savitribai", "Savitribai Phule and the gender of caste", [
            B("Savitribai Phule taught in the 1848 school and in the schools the couple went on "
              "to open, facing fierce resistance from orthodox Brahmins. The Phules also "
              "supported widow remarriage and opened a refuge for widows and their children. "
              "Their work shows that caste and gender cannot be separated: control over women's "
              "marriage and sexuality is how endogamy is enforced."),
            TC([P("indigo", "The link Ambedkar later drew",
                  "In 1916 Ambedkar argued that endogamy required controlling women: practices "
                  "such as child marriage and enforced widowhood kept surplus women and men inside "
                  "the group. Caste is therefore a gender system as much as an economic one.")],
               [P("green", "Practice today",
                  "Programmes on early marriage, women's mobility and violence against women meet "
                  "caste directly, through honour norms and violence against inter-caste couples. "
                  "Dalit women face caste and gender at once.")]),
            H("amber", "See " + L("gender-mainstreaming.html", "Gender Mainstreaming 101") + " and "
              + L("feminist-research.html", "Feminist Research 101") + " for intersectional methods."),
        ]),

        S("Ambedkar", "B. R. Ambedkar: economist, lawyer, constitution-maker", [
            B("Bhimrao Ramji Ambedkar trained as an economist at Columbia University and the "
              "London School of Economics and as a barrister. He chaired the Drafting Committee of "
              "the Constituent Assembly. His writing on caste combines anthropology, economics and "
              "law, and it remains the most practical theory of caste for anyone designing "
              "policy, because it names mechanisms that can be changed."),
            T(["Year", "Work or act", "Why it matters for practice"],
              [["1916", "Castes in India (Columbia seminar paper)", "Endogamy as the mechanism of caste"],
               ["1927", "Mahad Satyagraha, 20 March", "Claiming access to public water as a right"],
               ["1932", "Poona Pact, 24 September", "Origins of reserved seats in legislatures"],
               ["1936", "Annihilation of Caste", "Caste as division of labourers; scriptural authority as the root"],
               ["1956", "Conversion to Buddhism, Nagpur, 14 October", "Exit from caste through religion"]]),
            H("cyan", "Each date on this table is checked against sources listed in the spec notes."),
        ]),

        S("Annihilation of Caste", "The speech that was never delivered", [
            B("In 1935 the Jat-Pat-Todak Mandal of Lahore, a caste Hindu reform group, invited "
              "Ambedkar to preside over its 1936 annual conference. When the organisers read his "
              "printed address they asked him to cut it, and he refused. The conference was "
              "cancelled, and Ambedkar published the speech himself in 1936 as <em>Annihilation of "
              "Caste</em>. The first edition of 1,500 copies sold out within two months."),
            Q("I am convinced that the real remedy is inter-marriage. Fusion of blood can alone "
              "create the feeling of being kith and kin.",
              "B. R. Ambedkar, Annihilation of Caste, 1936"),
            H("amber", "Ambedkar went further than inter-marriage: he argued that the real remedy "
              "was to destroy belief in the sanctity of the Shastras, because people observe caste "
              "out of religious conviction."),
        ]),

        S("Division of labourers", "Why caste is bad economics as well as bad ethics", [
            B("Defenders of caste called it a division of labour. Ambedkar's reply is a piece of "
              "labour economics. A division of labour is efficient when people choose occupations "
              "by aptitude and can move when conditions change. Caste fixes occupation by birth, "
              "so labour cannot move to where it is most productive and talent is wasted."),
            TC([P("green", "Market division of labour",
                  "Voluntary, based on skill, responsive to wages and technology. People can "
                  "retrain and move when an industry declines.")],
               [P("red", "Caste division of labourers",
                  "Assigned by birth, graded in rank, enforced by social sanction. People are kept "
                  "in degrading work such as manual scavenging even when other work exists.")]),
            H("cyan", "Modern evidence backs the argument: Munshi and Rosenzweig (AER, 2006) found "
              "caste networks in Mumbai kept lower-caste boys in local-language schooling tied to "
              "traditional jobs as returns to English education rose (Section 7)."),
        ]),

        S("Liberty, equality, fraternity", "Ambedkar's positive ideal", [
            B("Ambedkar set out what should replace caste. His ideal was a society based on "
              "liberty, equality and fraternity, and he gave fraternity a precise meaning: "
              "many shared interests, free contact between groups and a habit of respect. He "
              "called this democracy as a way of living together, wider than a form of government."),
            Q("Democracy is not merely a form of government. It is primarily a mode of associated "
              "living, of conjoint communicated experience.",
              "B. R. Ambedkar, Annihilation of Caste, 1936, section 14"),
            TC([P("indigo", "Fraternity in a programme",
                  "Mixed-caste groups that meet on neutral ground, shared meals in trainings, and "
                  "leadership roles rotated across castes are small, practical forms of "
                  "'associated living'.")],
               [P("amber", "The caution",
                  "Forcing contact without protection can expose Dalit participants to backlash. "
                  "Design for safety first and track who speaks and who leads.")]),
        ]),

        S("Beyond Ambedkar", "The wider anti-caste tradition", [
            B("Phule and Ambedkar belong to a larger tradition. In the south, Narayana Guru in "
              "Kerala and E. V. Ramasamy (Periyar) in Tamil Nadu led movements against Brahmin "
              "dominance and untouchability. Ambedkar also weighed the bhakti saints and judged "
              "them ineffective: in his 1937 reply to Gandhi, printed with the second edition of "
              "<em>Annihilation of Caste</em>, he wrote that none of the saints ever attacked the Caste System."),
            T(["Figure or movement", "Region", "Focus"],
              [["Jotirao and Savitribai Phule", "Maharashtra", "Education, critique of Brahmanism"],
               ["Narayana Guru", "Kerala", "Temple access and social reform among Ezhavas"],
               ["Periyar and the Self-Respect Movement", "Tamil Nadu", "Rationalism, anti-Brahminism, women's rights"],
               ["B. R. Ambedkar", "Maharashtra and national", "Law, rights, representation, conversion"],
               ["Kanshi Ram and the BSP (1984)", "Uttar Pradesh and national", "Political power for Bahujans"]]),
            H("green", "These dates and roles are well documented; for any quotation from these "
              "figures, go to a published edition of their writing."),
        ]),

        S("Why it matters now", "Ambedkar's framework as a programme tool", [
            B("Ambedkar's analysis gives a practitioner four mechanisms to look for, each of which "
              "can be observed and each of which a programme can affect. That makes it more useful "
              "for design than theories built around purity alone."),
            T(["Mechanism", "Observable sign", "Programme response"],
              [["Endogamy", "Inter-caste couples face violence; women's mobility restricted",
                "Safe-space services, legal aid, support for couples"],
               ["Occupational assignment", "Dalit castes over-represented in sanitation and leather",
                "Skills and capital for exit, mechanisation, dignity at work"],
               ["Graded inequality", "Benefits captured by better-off sub-groups",
                "Disaggregate and target within SC and ST categories"],
               ["Religious sanction", "Exclusion justified by custom", "Rights awareness grounded in Article 17"]]),
            H("cyan", "Section 10 turns these into a checklist for programme teams."),
        ]),

        # ===================== SECTION 05 =====================
        DIV("05", "Five", "Untouchability and the criminal law"),

        S("Article 17", "The Constitution abolishes untouchability", [
            B("Article 17 is one of the few provisions of the Constitution that speaks directly "
              "to private conduct. It abolishes untouchability, forbids its practice in any form, "
              "and makes enforcing any disability arising from it an offence. Parliament gave it "
              "effect through two statutes, examined in the next slides."),
            Q("\"Untouchability\" is abolished and its practice in any form is forbidden. The "
              "enforcement of any disability arising out of \"Untouchability\" shall be an offence "
              "punishable in accordance with law.",
              "Constitution of India, Article 17"),
            TC([P("cyan", "Article 15(2)",
                  "No citizen may be denied access to shops, restaurants, hotels or places of "
                  "public entertainment, or the use of wells, tanks, bathing ghats and roads, on "
                  "grounds of caste among others.")],
               [P("green", "Article 46",
                  "Directs the State to promote with special care the educational and economic "
                  "interests of the weaker sections, in particular SCs and STs, and to protect them "
                  "from social injustice and all forms of exploitation.")]),
        ]),

        S("PCR Act 1955", "The Protection of Civil Rights Act 1955", [
            B("Parliament first enacted the Untouchability (Offences) Act 1955 (Act 22 of 1955), "
              "notified on 8 May 1955. It was amended and renamed in 1976 as the Protection of "
              "Civil Rights Act 1955. The Act extends to the whole of India and is implemented by "
              "state governments. Offences under it are cognisable and tried summarily (Section 15)."),
            T(["Section", "Offence or duty"],
              [["3", "Preventing entry to public places of worship or use of sacred water sources"],
               ["4", "Denying access to shops, restaurants, hotels, cremation grounds and similar places"],
               ["5", "Refusing admission to hospitals, dispensaries or educational institutions"],
               ["6", "Refusing to sell goods or render services"],
               ["7A", "Compelling a person, on the ground of untouchability, to scavenge or remove carcasses"],
               ["15A", "Duty of the State to ensure rights are available: legal aid, special courts, committees"]]),
            H("amber", "Source: annual report under Section 15A(4) of the PCR Act for 2013, social "
              "justice ministry, Government of India."),
        ]),

        S("PoA Act 1989", "The Atrocities Act: why a second law was needed", [
            B("By the 1980s it was clear that the PCR Act did not reach the violence used to "
              "enforce caste. Parliament enacted the Scheduled Castes and the Scheduled Tribes "
              "(Prevention of Atrocities) Act 1989 on 11 September 1989; it came into force on 30 "
              "January 1990, with Rules in 1995. It defines specific atrocities committed by a "
              "person outside the SC and ST communities against SC or ST persons."),
            TC([P("red", "What it covers",
                  "Humiliation, forced labour, dispossession of land, sexual violence, social and "
                  "economic boycott, and caste abuse in public view, among a long list in Section 3. "
                  "Penalties are higher than for the same acts under the general criminal law.")],
               [P("green", "How it is meant to work",
                  "Special courts and special public prosecutors, relief and rehabilitation for "
                  "victims, identification of atrocity-prone areas, and duties on officials. "
                  "Wilful neglect of duty by a public servant is itself punishable.")]),
            H("cyan", "The Act applies where the victim is SC or ST and the accused is not. Read it "
              "with the 2015 and 2018 amendments in the next two slides."),
        ]),

        S("2015 amendment", "The 2015 amendment widened the law", [
            B("The SC and ST (Prevention of Atrocities) Amendment Act 2015 (Act 1 of 2016) came "
              "into force on 26 January 2016. It responded to evidence from Dalit and Adivasi "
              "organisations that many common forms of humiliation and exclusion fell outside the "
              "1989 list, and that trials took years."),
            T(["Change", "Detail"],
              [["New offences", "Tonsuring, garlanding with footwear, denying access to irrigation, "
                "forcing manual scavenging, dedicating women as devadasis, social or economic boycott"],
               ["Exclusive Special Courts", "Dedicated courts and Special Public Prosecutors for atrocity cases"],
               ["Rights of victims and witnesses", "New Chapter IVA, Section 15A"],
               ["Speed", "Trial to be completed, as far as possible, within two months of the charge sheet"],
               ["Knowledge presumed", "If the accused knew the victim, knowledge of caste is presumed"]]),
            H("amber", "For programme staff, the victim and witness rights in Section 15A are the "
              "most useful: the right to be informed, to be heard and to protection."),
        ]),

        S("2018", "Mahajan, the backlash and Section 18A", [
            B("On 20 March 2018, in <em>Subhash Kashinath Mahajan v State of Maharashtra</em>, the "
              "Supreme Court required a preliminary inquiry before registering an FIR under the Act "
              "and approval before arrest, and allowed anticipatory bail. Dalit organisations "
              "protested across the country. Parliament responded with the SC and ST (Prevention "
              "of Atrocities) Amendment Act 2018, which inserted Section 18A."),
            FL(["20 March 2018: Mahajan adds safeguards for the accused",
                "17 August 2018: assent to the amendment inserting Section 18A (in force 20 August 2018)",
                "1 October 2019: Supreme Court recalls the Mahajan directions on review",
                "10 February 2020: Prathvi Raj Chauhan v Union of India upholds the 2018 amendment"]),
            H("cyan", "Section 18A removes the preliminary inquiry and the approval for arrest, and bars "
              "anticipatory bail, reversing all three Mahajan safeguards. Sources: Act No. 27 of 2018; "
              "Supreme Court Observer for the case dates."),
        ]),

        S("Manual scavenging", "Manual scavenging: caste as occupation, written into law", [
            B("Manual scavenging, the cleaning of human excreta by hand, is the clearest surviving "
              "case of caste-assigned work. The Prohibition of Employment as Manual Scavengers and "
              "their Rehabilitation Act 2013 (No. 25 of 2013, assent 18 September 2013, in force 6 "
              "December 2013) replaced a 1993 Act. It widened the definition to cover open drains, "
              "pits and railway tracks, banned hazardous manual cleaning of sewers and septic tanks, "
              "and required surveys and rehabilitation."),
            ST([C("58,098", "manual scavengers identified in national surveys of 2013 and 2018", "amber",
                  "Lok Sabha reply, as reported by Business Standard, 5 August 2026"),
                C("32,473", "of them in Uttar Pradesh, more than half the total", "red",
                  "Lok Sabha reply, as reported by Business Standard, 5 August 2026"),
                C("Rs 30 lakh", "compensation for a sewer death, raised from Rs 10 lakh", "green",
                  "Balram Singh v Union of India, Supreme Court, 20 October 2023")], cols=3),
            H("amber", "The 2013 Act exempts workers given protective gear, which critics call an "
              "escape clause. In the same 2026 reply the government said every district declared itself manual-scavenger-free after a 2024-25 survey."),
        ]),

        S("Sewer deaths", "Deaths in sewers and septic tanks continue", [
            B("The government distinguishes manual scavenging (handling excreta from insanitary "
              "latrines) from hazardous cleaning (entering sewers and septic tanks without safety "
              "gear). By that distinction it reports no deaths from manual scavenging. It does "
              "report deaths during sewer and septic tank cleaning, drawn from the National "
              "Commission for Safai Karamcharis."),
            {"t": "chart", "canvas": "sewerDeathsChart",
             "title": "Deaths while cleaning sewers and septic tanks, India (2026 = January to June)",
             "source": "NCSK data in a Lok Sabha written reply, reported by Business Standard, 5 August 2026",
             "type": "bar",
             "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026 H1"],
                      "datasets": [{"label": "Deaths", "data": [132, 34, 62, 88, 65, 54, 47, 16],
                                    "backgroundColor": "#EF4444"}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Deaths'} } } }"}},
            H("red", "498 deaths from 1 January 2019 to 30 June 2026; a separate July 2026 reply put "
              "2021 to June 2026 at 332, matching the chart. The 2013 Act's own preamble ties manual "
              "scavenging to 'a highly iniquitous caste system'."),
        ]),

        S("Enforcement gap", "Why the law on paper and the law in practice differ", [
            B("Strong statutes do not enforce themselves. Studies by Dalit rights groups and the "
              "statutory commissions repeatedly identify the same weak points between an incident "
              "and a conviction. Each is a place where a programme or a legal aid partner can help."),
            FL(["Incident: victim fears reprisal and economic boycott",
                "Police: delay or refusal to register an FIR under the right sections",
                "Investigation: weak evidence, hostile witnesses",
                "Trial: long delays despite special courts",
                "Outcome: acquittal or compromise under pressure"]),
            TC([P("green", "What helps",
                  "Paralegals trained in the PoA Act, prompt support to file complaints, "
                  "documentation, witness protection under Section 15A, and links to the State "
                  "and National Commissions for SCs and STs.")],
               [P("amber", "What to record",
                  "Date of complaint and of FIR, sections applied, compensation paid, time to "
                  "charge sheet. These are the indicators that show whether the law works.")]),
        ]),

        S("Commissions", "The constitutional commissions", [
            B("The Constitution creates two commissions to watch over these safeguards. Article "
              "338 establishes the National Commission for Scheduled Castes. Article 338A, "
              "inserted by the Constitution (Eighty-ninth Amendment) Act 2003, establishes a "
              "separate National Commission for Scheduled Tribes. Each has a chairperson, a "
              "vice-chairperson and three members appointed by the President."),
            T(["Body", "Basis", "Main duties"],
              [["National Commission for Scheduled Castes", "Article 338",
                "Investigate and monitor safeguards; inquire into complaints; report to the President"],
               ["National Commission for Scheduled Tribes", "Article 338A (2003)",
                "Same duties for STs, including forest and land issues"],
               ["National Commission for Backward Classes", "Article 338B (102nd Amendment, 2018)",
                "Constitutional status for the OBC commission"]]),
            H("cyan", "A complaint to a commission can move a stalled police case. Keep copies of "
              "every submission."),
        ]),

        # ===================== SECTION 06 =====================
        DIV("06", "Six", "The Constitution and reservations"),

        S("Equality clauses", "Formal equality and substantive equality", [
            B("Article 15(1) bars the State from discriminating on grounds of caste, and Article "
              "16(2) bars discrimination in public employment. The same articles then permit "
              "special provisions. This is the constitutional basis for reservation: equal "
              "treatment of unequally placed groups would preserve inequality."),
            T(["Clause", "What it permits"],
              [["Article 15(4)", "Special provisions for socially and educationally backward classes or SCs and STs"],
               ["Article 15(5)", "Reservation in admissions, including private institutions aided or unaided, other than minority institutions"],
               ["Article 15(6)", "Special provisions for economically weaker sections (EWS) other than those in 15(4) and 15(5)"],
               ["Article 16(4)", "Reservation in posts for any backward class not adequately represented"],
               ["Article 16(4A)", "Reservation in promotion, with consequential seniority, for SCs and STs"],
               ["Article 16(6)", "EWS reservation in posts, up to a maximum of 10%"]]),
            H("cyan", "Text checked against the current Constitution as reproduced by "
              "constitutionofindia.net. For the wider framework see " + L("ind-constitution.html", "Indian Constitution 101") + "."),
        ]),

        S("Lists", "Who is a Scheduled Caste is decided by notification", [
            B("Under Article 341 the President, after consulting the Governor, notifies the castes "
              "deemed to be Scheduled Castes in each state or union territory. Only Parliament, by "
              "law, can add or remove a group afterwards. Article 342 does the same for Scheduled "
              "Tribes. Lists are therefore state-specific: a caste can be SC in one state and not "
              "in its neighbour."),
            TC([P("cyan", "The Constitution (Scheduled Castes) Order 1950",
                  "Lists SCs state by state. Paragraph 3 restricts SC status to persons professing "
                  "Hinduism, Sikhism or Buddhism. Buddhists were added by the Constitution "
                  "(Scheduled Castes) Orders (Amendment) Act 1990 (No. 15 of 1990).")],
               [P("amber", "What this means for data",
                  "A Dalit who converts to Christianity or Islam loses SC status in law, though "
                  "not caste in social life. Surveys that ask 'Are you SC?' therefore undercount "
                  "Dalits of those faiths (Section 9).")]),
            H("green", "Always record which state list applies to a respondent, and the date of the list."),
        ]),

        S("Current shares", "Reservation in central government jobs", [
            B("For direct recruitment to central government posts by all-India open competition, "
              "the Department of Personnel and Training reserves 15% for SCs, 7.5% for STs and "
              "27% for OBCs. A further 10% is reserved for economically weaker sections who are not "
              "covered by SC, ST or OBC reservation. States set their own percentages for state "
              "posts, reflecting their populations."),
            {"t": "chart", "canvas": "reservationChart",
             "title": "Central reservation in direct recruitment by open competition (%)",
             "source": "DoPT instructions, as compiled by gconnect.in; EWS under Article 16(6)",
             "type": "doughnut",
             "data": {"labels": ["SC 15", "ST 7.5", "OBC 27", "EWS 10", "Unreserved 40.5"],
                      "datasets": [{"data": [15, 7.5, 27, 10, 40.5],
                                    "backgroundColor": ["#0EA5E9", "#10B981", "#6366F1", "#F59E0B", "#94A3B8"]}]},
             "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
        ]),

        S("Mandal", "The Mandal Commission and OBC reservation", [
            B("The Second Backward Classes Commission, chaired by B. P. Mandal, was set up in 1979. "
              "Its 1980 report identified 3,743 castes and communities as backward and estimated "
              "that they made up 52% of the population, excluding SCs and STs. It recommended "
              "reserving 27% of central government posts for OBCs, which kept total reservation "
              "below half. The report was shelved until the V. P. Singh government announced its "
              "implementation in August 1990."),
            ST([C("3,743", "castes and communities identified as backward", "cyan", "Mandal Commission report, 1980"),
                C("52%", "Commission's estimate of the OBC share of population", "amber",
                  "Mandal Commission report, 1980, based on 1931 Census data"),
                C("27%", "reservation recommended for OBCs in central posts", "green", "Mandal Commission report, 1980")], cols=3),
            H("amber", "The 52% figure rested on projections from the 1931 Census, the last to count "
              "all castes. That is a central reason for the demand for fresh caste data."),
        ]),

        S("Indra Sawhney", "Indra Sawhney v Union of India (1992)", [
            B("On 16 November 1992 a nine-judge bench of the Supreme Court decided the challenge to "
              "the Mandal orders by six votes to three. The judgment set the rules that still "
              "frame reservation law, and later amendments and cases are best read as responses to it."),
            T(["Holding", "Effect"],
              [["27% OBC reservation upheld", "Caste is an acceptable indicator of social backwardness"],
               ["Creamy layer excluded", "Advanced members of OBCs, above an income and status test, are excluded"],
               ["50% ceiling", "Reservation should not exceed half of posts, save in extraordinary situations"],
               ["No reservation in promotion", "Article 16(4) covers initial appointment only"],
               ["Backwardness is social and educational", "Economic criteria alone do not define a backward class under 16(4)"]]),
            H("cyan", "Parliament reversed the promotion holding for SCs and STs by inserting Article "
              "16(4A). The EWS amendment of 2019 later relied on a separate clause, Article 16(6)."),
        ]),

        S("EWS", "The EWS amendment and Janhit Abhiyan (2022)", [
            B("The Constitution (One Hundred and Third Amendment) Act 2019 added Articles 15(6) "
              "and 16(6), permitting reservation of up to 10% for economically weaker sections who "
              "are not SC, ST or OBC. On 7 November 2022, in <em>Janhit Abhiyan v Union of India</em>, "
              "a five-judge bench upheld the amendment by three votes to two."),
            TC([P("green", "Majority (Maheshwari, Trivedi, Pardiwala JJ)",
                  "Economic criteria are a valid basis for special provisions. Excluding SCs, STs "
                  "and OBCs from EWS is permissible because they already have their own reservation. "
                  "The amendment does not violate the basic structure.")],
               [P("red", "Dissent (Lalit CJI, Bhat J)",
                  "Excluding the groups that face the deepest disadvantage from a scheme for the "
                  "economically weak violates the equality code and the basic structure.")]),
            H("amber", "With EWS, central reservation in direct recruitment reaches 59.5%: the 49.5% "
              "for SCs, STs and OBCs plus 10% for EWS."),
        ]),

        S("Sub-classification", "State of Punjab v Davinder Singh (2024)", [
            B("On 1 August 2024 a seven-judge bench held, by six to one, that states may "
              "sub-classify the Scheduled Castes for the purpose of reservation, for example by "
              "setting aside part of the SC quota for the most under-represented SC groups. The "
              "judgment overruled <em>E. V. Chinnaiah v State of Andhra Pradesh</em> (2005), which "
              "had treated SCs as one homogeneous class."),
            T(["Point", "What the Court decided"],
              [["Operative order", "Chinnaiah overruled; sub-classification of SCs for reservation is permissible"],
               ["Judges", "Chandrachud CJI with Misra J; concurring Gavai, Mithal, Nath and S. C. Sharma JJ; Trivedi J dissenting"],
               ["Conditions", "A state must justify sub-classification with quantifiable and empirical "
                "data on a sub-group's relative backwardness and inadequate representation"],
               ["Scope", "The order speaks to SCs; separate opinions discuss STs as well"],
               ["Earlier law", "Chinnaiah, (2005) 1 SCC 394, had barred states from dividing the SC list"]]),
            H("cyan", "Source: Supreme Court record of proceedings, Civil Appeal 2317/2011, 1 August "
              "2024, and published summaries of the opinions."),
        ]),

        S("Creamy layer", "Creamy layer for SCs and STs: what was and was not decided", [
            B("Four of the seven judges in Davinder Singh, B. R. Gavai, Vikram Nath, Pankaj Mithal "
              "and S. C. Sharma, wrote that the State should evolve a policy to identify a creamy "
              "layer among SCs and STs and exclude it from reservation. That view appears in their "
              "separate opinions. It is not part of the operative order, which deals with "
              "sub-classification."),
            TC([P("amber", "The four opinions",
                  "Gavai J: the State must evolve a policy for identifying the creamy layer even "
                  "from SCs and STs. Nath J: the criteria could differ from those used for OBCs. "
                  "Sharma J: identification should become a constitutional imperative.")],
               [P("indigo", "The Union government's position",
                  "On 9 August 2024 the Union Cabinet said SC and ST reservation would continue as "
                  "the Constitution provides, and that the Constitution makes no provision for a "
                  "creamy layer among SCs and STs (The Tribune, 9 August 2024).")]),
            H("red", "Report this precisely: sub-classification is the holding; a creamy layer for "
              "SCs and STs is a view of four judges that the Union has rejected, as of October 2026."),
        ]),

        S("Promotions", "Reservation in promotion after Indra Sawhney", [
            B("Article 16(4A) allows reservation in promotion for SCs and STs where they are not "
              "adequately represented, with consequential seniority. The Supreme Court has upheld "
              "the clause while attaching conditions. The result is a body of case law that "
              "governments must follow when they design promotion rosters."),
            T(["Case", "Year", "Holding in brief"],
              [["Indra Sawhney v Union of India", "1992", "No reservation in promotion under Article 16(4)"],
               ["M. Nagaraj v Union of India", "2006", "Required states to collect quantifiable data "
                "showing SC and ST backwardness; applied the creamy layer principle"],
               ["Jarnail Singh v Lachhmi Narain Gupta", "26 Sept 2018", "Struck down the "
                "backwardness-data requirement as contrary to Indra Sawhney; kept the creamy layer "
                "principle; declined to send Nagaraj to a larger bench"]]),
            H("amber", "These holdings are summarised from standard case reports. Before advising "
              "on a specific roster, read the latest judgment for the cadre concerned."),
        ]),

        S("Political reservation", "Reserved seats and what they deliver", [
            B("Articles 330 and 332 reserve seats for SCs and STs in the Lok Sabha and state "
              "assemblies in proportion to their population. Article 334, as amended, ends this "
              "reservation eighty years from the commencement of the Constitution, that is in "
              "January 2030, unless Parliament amends it again. Since the 2008 delimitation, 84 of "
              "543 Lok Sabha seats are reserved for SCs and 47 for STs."),
            TC([ST([C("84", "Lok Sabha seats reserved for SCs", "cyan", "Delimitation Order 2008"),
                    C("47", "Lok Sabha seats reserved for STs", "green", "Delimitation Order 2008")], cols=2)],
               [B("Rohini Pande (<em>American Economic Review</em>, 2003) exploited the "
                  "institutional features of political reservation in Indian states and found that "
                  "it increased transfers to the groups that benefit from the mandate. Reserved "
                  "seats therefore change policy as well as the composition of the legislature.", sm=True)]),
            H("indigo", "Article 243D reserves panchayat seats and chair posts for SCs and STs as "
              "well, which matters for every village-level programme."),
        ]),

        S("OBC lists", "The 102nd and 105th Amendments", [
            B("The Constitution (One Hundred and Second Amendment) Act 2018 gave the National "
              "Commission for Backward Classes constitutional status in Article 338B and added "
              "Article 342A on lists of socially and educationally backward classes. In May 2021, "
              "in the Maratha reservation case (<em>Jaishri Laxmanrao Patil</em>), the Supreme Court "
              "read it as leaving only the Centre able to notify those lists. Parliament responded "
              "with the One Hundred and Fifth Amendment in August 2021, restoring the states' "
              "power to keep their own OBC lists."),
            FL(["2018: 102nd Amendment, Article 338B",
                "May 2021: Maratha case reads Centre-only power",
                "August 2021: 105th Amendment restores state lists"]),
            H("cyan", "For programme data this explains why OBC status must be recorded against a "
              "specific list: central or state."),
        ]),

        S("The debate", "Arguments about reservation, stated fairly", [
            B("Reservation is the most argued-over policy in this deck. A practitioner should be "
              "able to state each side accurately, and to know which claims have evidence behind "
              "them. The table pairs the common arguments with the evidence covered in this course."),
            T(["Claim", "Evidence to weigh"],
              [["Reservation reduces efficiency", "Little direct evidence; the claim is often asserted, rarely measured"],
               ["Benefits go to a few better-off groups", "Supported for some SC sub-groups; the basis of Davinder Singh"],
               ["Caste no longer matters for urban jobs", "Contradicted by correspondence studies (Thorat and Attewell, 2007)"],
               ["Political reservation changes policy", "Supported by Pande (2003) for transfers to SCs and STs"],
               ["Reservation should rest on economic criteria alone", "Economic criteria permitted alongside caste since 2019 (EWS)"]]),
            H("green", "For deeper treatment of how interest groups shape these choices, see "
              + L("pol-economy.html", "Political Economy 101") + "."),
        ]),

        # ===================== SECTION 07 =====================
        DIV("07", "Seven", "Caste in the economy"),

        S("Land", "Land is the oldest caste asset", [
            B("In rural South Asia, land brings income, credit, status and political power. Caste "
              "shaped who received land under colonial settlements and who was excluded from land "
              "reform afterwards. The SECC 2011 rural data found that close to three in ten rural "
              "households were landless and earned most of their income from manual casual labour."),
            ST([C("29.97%", "of rural households landless and dependent mainly on manual casual labour", "amber",
                  "SECC 2011 rural data, Ministry of Rural Development, released 3 July 2015"),
                C("18.5%", "SC share of India's rural population", "cyan",
                  "Census of India 2011, SC/ST data highlights, ORGI 2013"),
                C("11.3%", "ST share of rural population", "green",
                  "Census of India 2011, SC/ST data highlights, ORGI 2013")], cols=3),
            H("cyan", "When you see a land programme, ask who held the land before and who will "
              "hold the title after. Women's names on titles are a separate, equally important question."),
        ]),

        S("Anderson 2011", "Caste as an impediment to trade", [
            B("Siwan Anderson (<em>American Economic Journal: Applied Economics</em> 3, January "
              "2011, 239-263) compared villages in rural India dominated, by majority land "
              "ownership, either by an upper caste or by a lower backward agricultural caste. "
              "Low-caste households earned substantially more in villages dominated by a low caste. "
              "The mechanism was a breakdown of trade in irrigation water across caste lines."),
            ST([C("45%", "higher yields for lower-caste water buyers when sellers share their caste", "green",
                  "Anderson (2011), AEJ: Applied Economics 3(1)")], cols=1),
            TC([P("cyan", "What it shows",
                  "Caste affects markets that look purely economic. Water buyers and sellers who "
                  "do not trust or deal fairly with each other produce less.")],
               [P("amber", "Programme implication",
                  "Irrigation, input or credit schemes that assume an open local market may fail "
                  "low-caste farmers in villages dominated by another caste.")]),
        ]),

        S("Hiring", "Thorat and Attewell: discrimination at the first step", [
            B("Sukhadeo Thorat and Paul Attewell ran a correspondence study of hiring in India's "
              "urban private sector, published in the <em>Economic and Political Weekly</em> "
              "(October 2007). Matched applications that differed only in the applicant's name, "
              "signalling a high-caste Hindu, a Dalit or a Muslim, were sent to real job "
              "advertisements. Employers called back fewer Dalit and Muslim applicants with the "
              "same qualifications."),
            ST([C("4,808", "applications sent to 548 job advertisements over 66 weeks", "cyan",
                  "Thorat and Attewell (2007), EPW 42(41), as quoted from the paper"),
                C("About 2/3", "Dalit applicant's odds of an interview call relative to a high-caste Hindu", "amber",
                  "Thorat and Attewell, as summarised by GSDRC"),
                C("About 1/3", "Muslim applicant's odds relative to a high-caste Hindu", "red",
                  "Thorat and Attewell, as summarised by GSDRC")], cols=3),
            H("green", "The applicants were college-educated. This is discrimination in the modern "
              "formal sector, the place where caste is often said to have stopped mattering."),
        ]),

        S("Method note", "Why correspondence studies are persuasive", [
            B("Surveys show that Dalits earn less, but they cannot separate discrimination from "
              "differences in schooling or skills. A correspondence study holds everything on the "
              "application constant except the signal of caste or religion, so any gap in "
              "callbacks is the employer's response to that signal."),
            TC([P("green", "Strengths",
                  "Clean comparison, real employers, real jobs. The result does not rely on "
                  "self-reports of discrimination, which victims may under-report and employers "
                  "will deny.")],
               [P("amber", "Limits",
                  "Measures only the first stage of hiring; interviews, wages and promotion are outside it. "
                  "Names must signal caste reliably. Ethically, employers do not consent, which "
                  "research ethics boards weigh against the public value of the evidence.")]),
            H("indigo", "Design details and ethics of field experiments are covered in "
              + L("impact-eval.html", "Impact Evaluation 101") + " and "
              + L("research-ethics.html", "Research Ethics 101") + "."),
        ]),

        S("Entrepreneurship", "Who owns India's enterprises?", [
            B("Lakshmi Iyer, Tarun Khanna and Ashutosh Varshney used the Economic Censuses of "
              "1990, 1998 and 2005, covering 19 large states, to measure enterprise ownership by "
              "caste (<em>Economic and Political Weekly</em>, 2013). SCs and STs owned far fewer "
              "enterprises than their population share. OBCs owned about their share."),
            {"t": "chart", "canvas": "entChart",
             "title": "Share of population and of non-farm enterprises owned, 2005 (%)",
             "source": "Iyer, Khanna and Varshney (2013), Economic Census 2005, 19 states; via Ideas for India",
             "type": "bar",
             "data": {"labels": ["Scheduled Castes", "Scheduled Tribes", "OBCs"],
                      "datasets": [{"label": "Population share", "data": [16.4, 7.7, 43],
                                    "backgroundColor": "#94A3B8"},
                                   {"label": "Enterprise ownership share", "data": [9.8, 3.7, 43.5],
                                    "backgroundColor": "#0EA5E9"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ title:{display:true,text:'%'} } } }"}},
            H("amber", "The SC share of enterprises in 2005 was the same as in 1990."),
        ]),

        S("Why the gap", "Why Dalit enterprise stays small", [
            B("Iyer, Khanna and Varshney found the ownership gap was not significantly associated "
              "with literacy, secondary schooling or reliance on farming across states and districts. Other studies point to mechanisms that "
              "programmes can address directly, though the weight of each varies by region and "
              "sector."),
            T(["Barrier", "How it works", "Programme lever"],
              [["Networks", "Suppliers, buyers and lenders deal within caste", "Market linkages, buyer agreements"],
               ["Credit", "Collateral and guarantors come from land and kin", "Credit guarantees, group lending"],
               ["Customers", "Some customers avoid Dalit-run food or service businesses", "Branding, institutional buyers"],
               ["Social sanction", "Success can provoke backlash in the village", "Urban clusters, legal support"],
               ["Starting capital", "Lower inherited wealth", "Grants, matched savings"]]),
            H("cyan", "Illustrative pairing of barrier and lever; test which barrier binds in your "
              "context before choosing a response."),
        ]),

        S("Networks", "Caste networks help and trap at once", [
            B("Caste networks are a form of social capital: they find jobs, lend money and settle "
              "disputes. Kaivan Munshi and Mark Rosenzweig (<em>American Economic Review</em>, "
              "2006) studied schooling in Mumbai. Lower-caste male networks kept channelling boys "
              "into local-language schools that led to traditional working-class jobs, even after "
              "returns to English-medium education rose in the 1990s. Lower-caste girls, outside "
              "those male job networks, switched rapidly to English schools."),
            TC([P("green", "Network as help",
                  "Insurance against shocks, referrals into jobs, migration support. Programmes "
                  "that ignore networks miss how people actually find work.")],
               [P("red", "Network as trap",
                  "Steering into the group's traditional occupation; costly exit for individuals "
                  "when the economy changes. Benefits flow mainly to those already connected.")]),
            H("amber", "Labour market programmes should map these networks before choosing "
              "placement partners. See " + L("work-labour-livelihoods.html", "Work, Labour &amp; Livelihoods 101") + "."),
        ]),

        S("Stereotype threat", "Caste salience changes performance", [
            B("Karla Hoff and Priyanka Pandey ran experiments with 321 high-caste and 321 low-caste "
              "junior high school boys in rural India (World Bank Policy Research Working "
              "Paper 3351, 2004; <em>AER</em> Papers and Proceedings, 2006). Boys solved mazes for "
              "money. When caste was not revealed there was no caste gap in performance. When "
              "caste was announced publicly, a large gap appeared."),
            FL(["Caste hidden: no gap in maze scores",
                "Caste announced: low-caste performance falls",
                "Reward made random: gap disappears",
                "Interpretation: expected prejudice lowers effort"]),
            H("indigo", "The authors conclude that low-caste boys expected to be judged "
              "prejudicially when there was scope for discretion. Classroom and training practice "
              "that publicly marks caste can lower performance."),
        ]),

        S("Discrimination framework", "Where discrimination enters a life", [
            B("Evidence on caste in the economy can be organised by market and by stage. The table "
              "below gathers the studies used in this section and notes what remains less studied, "
              "which is useful when you commission new research."),
            T(["Market", "Stage", "Evidence in this course", "Gap"],
              [["Labour", "Hiring callbacks", "Thorat and Attewell (2007)", "Wages and promotion inside firms"],
               ["Land and water", "Trade between castes", "Anderson (2011)", "Tenancy contracts today"],
               ["Enterprise", "Ownership", "Iyer, Khanna and Varshney (2013)", "Survival and growth of firms"],
               ["Schooling", "Choice and performance", "Munshi and Rosenzweig (2006); Hoff and Pandey (2006)", "Teacher behaviour"],
               ["Politics", "Representation", "Pande (2003)", "Panchayat-level delivery"]]),
            H("green", "Ashwini Deshpande's <em>The Grammar of Caste</em> (Oxford University Press, "
              "2011) is a book-length survey of the economics of caste using national data."),
        ]),

        # ===================== SECTION 08 =====================
        DIV("08", "Eight", "Counting caste: data and its limits"),

        S("What exists", "The main sources of caste data", [
            B("A practitioner needs to know which source records which categories, at what level "
              "and with what known problems. Few sources record individual jatis; most record only "
              "SC, ST, OBC and 'others'. Choosing the wrong source is a common reason why "
              "caste analysis in programme reports is thin."),
            T(["Source", "Caste categories", "Level", "Main limitation"],
              [["Census 2011", "SC and ST, with notified group names", "Village and ward", "No OBC or other caste data"],
               ["SECC 2011", "Caste names recorded", "Household", "Caste data never released; unusable per the Centre"],
               ["NFHS, PLFS, HCES", "SC, ST, OBC, others", "District or state", "Self-reported; no jati detail"],
               ["IHDS", "SC, ST, OBC, Brahmin, others; practice questions", "Household panel", "Older rounds (2004-05, 2011-12)"],
               ["Bihar survey 2023", "All castes", "State", "One state only"],
               ["Census 2027", "SC, ST and caste (item 10 of the schedule notified 14 August 2026)", "Expected to be fine-grained", "Data not yet released as of October 2026"]]),
            H("cyan", "Survey design for caste questions is covered in " + L("survey-design.html", "Survey Design 101") + "."),
        ]),

        S("Census 2011", "What the 2011 Census shows about SCs and STs", [
            B("The Census Primary Census Abstract for SCs and STs is the backbone of most "
              "targeting in India. Between 2001 and 2011 the SC population grew 20.8% and the ST "
              "population 23.7%, faster than the population as a whole. The notified lists also changed between the two "
              "censuses, so part of the growth reflects additions."),
            {"t": "chart", "canvas": "scstChart",
             "title": "SC and ST population, India, 2001 and 2011 (millions)",
             "source": "Census of India 2011, SC/ST data highlights, ORGI, 30 April 2013",
             "type": "bar",
             "data": {"labels": ["2001", "2011"],
                      "datasets": [{"label": "Scheduled Castes", "data": [166.6, 201.4], "backgroundColor": "#0EA5E9"},
                                   {"label": "Scheduled Tribes", "data": [84.3, 104.3], "backgroundColor": "#10B981"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ title:{display:true,text:'Millions'} } } }"}},
            H("amber", "Highest SC share: Punjab, 31.9%. Highest ST shares: Lakshadweep, 94.8%, and "
              "Mizoram, 94.4%. Same source."),
        ]),

        S("SECC", "The SECC 2011: a caste count that was never published", [
            B("The Socio Economic and Caste Census 2011 collected caste names for every household. "
              "Its rural socio-economic data was released on 3 July 2015. The caste data was "
              "never released. In a "
              "September 2021 affidavit to the Supreme Court, the Union government said the "
              "exercise had produced more than 46 lakh different caste names nationally."),
            TC([P("red", "What went wrong, per the Centre",
                  "Open-ended answers with no prepared register of castes; numbers or symbols "
                  "entered in the caste column; 4,28,677 castes recorded in Maharashtra alone, "
                  "against 494 entries in official lists.")],
               [P("green", "The lesson for survey design",
                  "Caste cannot be collected well as free text without a tested code list, "
                  "probes for spelling variants, and a plan for coding synonyms. Pilot the "
                  "question in each language before going to scale.")]),
            H("amber", "Source: Union government affidavit, September 2021, as reported by the "
              "Morung Express."),
        ]),

        S("Bihar 2023", "The Bihar caste survey", [
            B("Bihar conducted its own caste-based survey and released the findings on 2 October "
              "2023. It counted a population of over 13 crore. It was a rare full count of every "
              "caste in a large state, and it showed Other Backward Classes, split "
              "into Backward Classes and Extremely Backward Classes, as more than 63% of the "
              "population."),
            {"t": "chart", "canvas": "biharChart",
             "title": "Bihar caste-based survey 2023: population by category (%)",
             "source": "Government of Bihar, released 2 October 2023, as reported by All India Radio",
             "type": "doughnut",
             "data": {"labels": ["Extremely Backward Classes 36.01", "Backward Classes 27.12",
                                 "Scheduled Castes 19.65", "General 15.52", "Scheduled Tribes 1.68"],
                      "datasets": [{"data": [36.01, 27.12, 19.65, 15.52, 1.68],
                                    "backgroundColor": ["#6366F1", "#0EA5E9", "#F59E0B", "#94A3B8", "#10B981"]}]},
             "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
            H("cyan", "Yadavs, at 14.26%, were the largest single group. The survey was a state "
              "government exercise, separate from the decennial Census of India."),
        ]),

        S("Census 2027", "Caste returns to the Census", [
            B("On 30 April 2025 the Cabinet Committee on Political Affairs decided to include caste "
              "enumeration in the next Census. The intent to conduct the Census was notified in the "
              "Gazette of India on 16 June 2025. Until 2011 the Census enumerated only SCs and STs. "
              "Census 2027 is also India's first digital Census, with an optional self-enumeration "
              "portal."),
            T(["Step", "Date or detail"],
              [["Reference date", "00:00 hours, 1 March 2027"],
               ["Snow-bound areas (Ladakh, parts of J&amp;K, HP, Uttarakhand)", "00:00 hours, 1 October 2026"],
               ["Phase I: houselisting", "April to September 2026, 30 days in each state"],
               ["Phase II: population enumeration with caste", "February 2027 (September 2026 in the snow-bound areas)"],
               ["Questions notified", "14 August 2026, S.O. 4505(E): 40 items; item 10 is 'Scheduled Caste (SC)/ Scheduled Tribe (ST)/Caste'"],
               ["Approved outlay", "Rs 11,718.24 crore"]]),
            H("amber", "Sources: PIB backgrounder on Census 2027, April 2026; Gazette of India S.O. "
              "4505(E), 14 August 2026. As of October 2026 no caste data from Census 2027 has been "
              "released, and the coding scheme for caste answers has not been published."),
        ]),

        S("Using categories", "Coding caste in your own data", [
            B("Most programme and research teams will use broad categories. The way you ask and "
              "code caste decides whether your results can be compared with national data and "
              "whether respondents trust you. A simple protocol avoids the most common errors."),
            FL(["Ask religion first",
                "Ask category: SC, ST, OBC (state or central list), none",
                "Optionally ask jati, with consent and a code list",
                "Record the state whose list applies",
                "Allow 'prefer not to say'"]),
            TC([P("green", "Do",
                  "Use the same category wording as NFHS or PLFS so you can benchmark. Let "
                  "respondents self-identify. Pilot local terms. Keep jati in a separate, "
                  "protected field.")],
               [P("red", "Do not",
                  "Infer caste from surnames or appearance. Ask caste in front of neighbours. "
                  "Print caste on beneficiary lists posted in public places.")]),
        ]),

        S("Disaggregation", "Averages hide caste gaps", [
            B("A programme that reports only an overall average can show success while the "
              "groups it most needed to reach see no change. Disaggregating by caste category is "
              "the minimum. Where samples allow, disaggregate by caste and sex together, because "
              "Dalit and Adivasi women often face the largest gaps."),
            T(["Indicator (Illustrative)", "All", "SC", "ST", "Others"],
              [["Enrolled in the scheme (%)", "62", "48", "41", "71"],
               ["Received full benefit (%)", "55", "39", "33", "64"],
               ["Reported being turned away (%)", "8", "17", "21", "4"]]),
            H("amber", "Illustrative figures. The pattern is typical: an overall 62% hides a "
              "30-point gap between STs and others. Plan sample sizes so subgroup estimates are "
              "precise enough to report, as covered in " + L("data-lit.html", "Data Literacy 101") + "."),
        ]),

        S("Data limits", "What caste data cannot tell you", [
            B("Caste categories are blunt. SC, ST and OBC each contain hundreds of groups with very "
              "different histories and outcomes. Official data also misses those whose caste the "
              "law does not recognise, such as Dalit Christians and Muslims. Treat every caste "
              "statistic as a lower bound on what you do not know."),
            BL(["<strong>Aggregation</strong>: 'OBC' can combine landed dominant castes and very "
                "poor artisan castes in a single figure.",
                "<strong>Legal definitions</strong>: SC status depends on religion under the 1950 "
                "Order, so SC counts exclude many Dalits.",
                "<strong>Reporting</strong>: crime data depends on complaints registered by "
                "police; low counts can mean low reporting.",
                "<strong>Change over time</strong>: lists change, so trends can reflect additions "
                "as well as real change.",
                "<strong>Missing jati</strong>: most surveys cannot show which sub-groups are left behind."]),
            H("cyan", "Mixed methods help: pair the numbers with qualitative work. See "
              + L("mixed-methods.html", "Mixed Methods 101") + "."),
        ]),

        # ===================== SECTION 09 =====================
        DIV("09", "Nine", "Beyond Hindu India and beyond India"),

        S("Other religions", "Caste among Christians, Muslims and Sikhs", [
            B("Caste does not stop at the boundary of Hinduism. Dalits who became Christians, "
              "Muslims, Sikhs or Buddhists carried caste with them, because neighbours, employers "
              "and marriage markets kept recognising it. The law recognises this only in part: "
              "Sikh and Buddhist Dalits can hold SC status, while Christian and Muslim Dalits "
              "cannot. Two national commissions have examined whether that line is justified."),
            TC([P("cyan", "Legal position",
                  "Paragraph 3 of the Constitution (Scheduled Castes) Order 1950 limits SC status "
                  "to Hindus, Sikhs and Buddhists. A challenge, <em>Ghazi Saaduddin v State of "
                  "Maharashtra</em>, has been pending in the Supreme Court since 2004.")],
               [P("amber", "Commissions",
                  "The Ranganath Misra Commission (constituted 29 October 2004, reported 2007) "
                  "recommended extending SC status to Dalit converts; the government did not "
                  "accept it. On 6 October 2022 a commission chaired by former CJI K. G. "
                  "Balakrishnan was appointed to examine the question.")]),
            H("red", "The Hindu reported in June 2026 that the Balakrishnan Commission's report was "
              "ready, with its deadline at 10 June 2026. The report had not been made public in the "
              "sources checked as of October 2026."),
        ]),

        S("Nepal", "Nepal: a caste code, then a ban", [
            B("Nepal's Muluki Ain (National Code) of 1854 placed every group in a legal caste "
              "hierarchy, with rules on food, marriage and punishment by caste (Hofer, 1979, is "
              "the standard study). Today the "
              "Constitution of Nepal 2015 guarantees a right against untouchability and "
              "discrimination (Article 24) and rights of Dalits, including proportional inclusion "
              "in state bodies (Article 40)."),
            ST([C("13.4%", "Dalit share of Nepal's population: 3,898,990 of 29,164,578 people", "cyan",
                  "Census 2021, NSO and FEDO Dalit report, as summarised by DanChurchAid"),
                C("8.6%", "Hill Dalits as a share of the population", "green",
                  "Census 2021, NSO and FEDO Dalit report, as summarised by DanChurchAid"),
                C("4.8%", "Madheshi Dalits as a share of the population", "amber",
                  "Census 2021, NSO and FEDO Dalit report, as summarised by DanChurchAid")], cols=3),
            H("indigo", "The Caste-based Discrimination and Untouchability (Offence and "
              "Punishment) Act 2011 makes caste-based discrimination and untouchability offences "
              "punishable with imprisonment and fines, and provides compensation for victims. "
              "Article 24 of the 2015 Constitution covers 'any private or public place'."),
        ]),

        S("Nepal in practice", "Law and reality in Nepal", [
            B("Nepal's legal framework is among the strongest in the region on paper, yet "
              "commentary in Nepal describes the 2011 Act as ineffective in practice. A Kathmandu "
              "Post column of 9 January 2025 noted that caste-based violence continues, with Dalits "
              "killed in such violence, despite the constitutional guarantees. Hill and Madheshi "
              "Dalits also live in different regions and face different local power structures."),
            T(["Instrument", "Year", "What it does"],
              [["Muluki Ain", "1854", "Codified caste hierarchy in law"],
               ["Caste-based Discrimination and Untouchability (Offence and Punishment) Act", "2011",
                "Criminal penalties for caste-based discrimination and untouchability"],
               ["Constitution of Nepal, Articles 24 and 40", "2015", "Right against untouchability; Dalit rights to inclusion"]]),
            H("cyan", "Programmes in Nepal should disaggregate Hill and Madheshi Dalits separately; "
              "the 2021 Census report makes that possible for the first time."),
        ]),

        S("Pakistan", "Pakistan: Scheduled Castes as a census religion", [
            B("Pakistan inherited the colonial category of Scheduled Castes. In its 2017 Census, "
              "Scheduled Castes were reported separately from Hindus in the religion data, as a "
              "category of their own. A Dalit who identified as Hindu on the form was counted as "
              "Hindu, so the two figures together are the closest official guide to the size of "
              "Pakistan's Dalit population."),
            ST([C("1.73%", "Hindus as a share of Pakistan's population", "cyan",
                  "Pakistan Census 2017, final results, as reported by Dawn, 19 May 2021"),
                C("0.41%", "Scheduled Castes as a share of the population", "amber",
                  "Pakistan Census 2017, final results, as reported by Dawn, 19 May 2021")], cols=2),
            H("red", "Treat 0.41% as a lower bound for Dalits: anyone who chose 'Hindu' is outside "
              "it. Read the census form before using the figure."),
        ]),

        S("Bangladesh", "Bangladesh: Dalit and Harijan communities", [
            B("Bangladesh has Dalit and Harijan communities, and caste-based exclusion is "
              "recognised in national law-making: the government's own anti-discrimination bill "
              "lists caste among the prohibited grounds, alongside religion, race, language, age, "
              "gender and disability. That bill is the most important "
              "recent legal step found in the sources checked for this course."),
            TC([P("cyan", "Anti-Discrimination Bill 2022",
                  "Placed in Parliament on 5 April 2022 by Law Minister Anisul Huq, it would bar "
                  "discrimination on grounds including religion, caste, race, language, age, "
                  "gender and disability, and referred to a standing committee for scrutiny.")],
               [P("amber", "Status",
                  "The bill had not been passed when Parliament was dissolved on 6 August 2024. "
                  "No later enactment was found in the sources checked as of October 2026, so do "
                  "not cite it as law.")]),
            H("green", "For NGOs in Bangladesh, start by mapping which occupational communities in "
              "your area face exclusion, with community organisations as partners."),
        ]),

        S("Sri Lanka", "Sri Lanka: caste without the word in the census", [
            B("Sri Lanka has its own caste hierarchies, and Parliament legislated against caste "
              "exclusion soon after independence. The Prevention of Social Disabilities Act, "
              "No. 21 of 1957 (in force 13 April 1957, amended by Act 18 of 1971), makes it an "
              "offence to impose a social disability on anyone by reason of caste, punishable by up "
              "to three years' imprisonment and a fine."),
            T(["Section 3 lists disabilities, including preventing a person from", "Example"],
              [["Being admitted as a student or employed as a teacher", "Schools"],
               ["Entering or buying at a shop, market or fair", "Commerce"],
               ["Being served at a hotel, eating house or restaurant", "Public food"],
               ["Using water from a public well or other public supply", "Water"],
               ["Entering a public cemetery or taking part in a burial or cremation", "Death rites"]]),
            H("cyan", "Under Section 2(4), the court presumes the disability was imposed because of "
              "caste, and the accused must prove otherwise."),
        ]),

        S("Regional comparison", "Five countries, five legal approaches", [
            B("Every country in the region has caste, and each has responded through different "
              "legal tools. Comparing them helps practitioners working across borders, and shows "
              "that strong law is a starting point for change, with enforcement still to follow."),
            T(["Country", "Main legal instrument", "Official caste data", "Distinctive feature"],
              [["India", "Article 17; PCR Act 1955; PoA Act 1989", "SC and ST in Census; caste in 2027", "Reservation in jobs, education, legislatures"],
               ["Nepal", "Act of 2011; Constitution 2015", "Dalit report from Census 2021", "Proportional inclusion right"],
               ["Pakistan", "General equality guarantees", "SC as a census religion option (2017)", "SC and Hindu counted separately"],
               ["Bangladesh", "Anti-Discrimination Bill 2022 (not enacted)", "None", "Dalits among Hindus and Muslims"],
               ["Sri Lanka", "Prevention of Social Disabilities Act 1957", "None", "Reverse burden of proof on caste motive"]]),
            H("amber", "For rights frameworks beyond caste, see " + L("social-margins.html", "Social Margins 101") + "."),
        ]),

        # ===================== SECTION 10 =====================
        DIV("10", "Ten", "Working on caste in programmes and research"),

        S("Design checklist", "A caste checklist for programme design", [
            B("Use this checklist at the design stage of any programme in South Asia, whatever "
              "its sector. It turns the history, law and evidence in this course into questions a "
              "team can answer in a workshop. Record the answers in the design document so they "
              "can be checked at review."),
            T(["Stage", "Question", "Evidence to collect"],
              [["Context", "Which castes live here, where, and who is dominant?", "Hamlet map, land ownership"],
               ["Access", "Where are services located and who controls them?", "Location of taps, centres, meeting places"],
               ["Targeting", "Do lists rely on officials from the dominant caste?", "Who prepares and verifies lists"],
               ["Staffing", "Do frontline staff come from the communities served?", "Staff caste and gender profile, by consent"],
               ["Risk", "Could participation expose people to backlash?", "Past incidents, local power relations"],
               ["Measurement", "Can every outcome be disaggregated by caste category?", "Sample design, data fields"]]),
            H("cyan", "Theory of change work on who is excluded and why is covered in "
              + L("toc-workbench.html", "Theory of Change 101") + "."),
        ]),

        S("Decision table", "Choosing a targeting approach", [
            B("Teams often ask whether to target by caste category, by economic need, or both. The "
              "answer depends on the problem and the context. This decision table sets out common "
              "situations and the approach the evidence in this course supports."),
            T(["Situation", "Recommended approach", "Reason"],
              [["Exclusion is driven by untouchability (water, temples, services)", "Target SC hamlets and households directly",
                "Poverty targeting will not reach a discriminatory barrier"],
               ["Benefit captured by better-off sub-groups", "Target within SC or ST by sub-group or need",
                "Graded inequality; the reasoning of Davinder Singh"],
               ["Universal service with uneven uptake", "Universal design plus caste-disaggregated monitoring",
                "Avoids stigma while checking for gaps"],
               ["Livelihood programme in a dominant-caste village", "Separate groups, outside market linkages",
                "Anderson (2011): trade breaks down across caste"],
               ["Hiring or placement programme", "Name-blind screening with partner employers", "Thorat and Attewell (2007)"]]),
            H("amber", "Whatever approach you choose, explain it to the community in plain terms, "
              "since visible caste targeting can provoke resentment if unexplained."),
        ]),

        S("Worked example", "Worked example: a water programme in a mixed-caste village", [
            B("<strong>Illustrative.</strong> An NGO plans handpumps in a village of 400 households "
              "in eastern Uttar Pradesh: 260 households of a dominant OBC caste in the main "
              "settlement, 110 SC households in a separate tola 600 metres away, and 30 others. "
              "The panchayat proposes all four pumps in the main settlement, near the temple."),
            TC([P("red", "Without a caste lens",
                  "Pumps placed where the panchayat asks. Coverage looks complete on a map. SC "
                  "women walk 600 metres and may be refused or made to wait. The baseline-endline "
                  "survey reports average distance to water, which hides the SC tola.")],
               [P("green", "With a caste lens",
                  "Hamlet map drawn with SC residents. At least one pump in the SC tola, with a "
                  "women's committee including SC members. Monitoring records who draws water at "
                  "each pump and any refusal, a potential offence under the PCR Act.")]),
            H("cyan", "Illustrative. The design choice costs the same and changes who benefits."),
        ]),

        S("Research ethics", "Collecting caste data ethically", [
            B("Caste data is sensitive. A list of Dalit households with names and locations could "
              "be used to target them. Ethical research protects respondents through consent, "
              "minimum collection, secure storage and careful publication. The Digital Personal Data "
              "Protection Act 2023 and its 2025 Rules commence in stages: the core duties and rights "
              "in sections 3 to 17 apply from 13 May 2027 (G.S.R. 843(E), 13 November 2025)."),
            BL(["<strong>Consent</strong>: explain why caste is asked and that answering is optional.",
                "<strong>Minimise</strong>: collect category only, unless jati is needed for a stated analysis.",
                "<strong>Separate</strong>: store caste fields apart from names and contact details.",
                "<strong>Protect</strong>: do not publish small-area tables that identify households.",
                "<strong>Research exemption</strong>: from 13 May 2027, Section 17(2)(b) of the DPDP "
                "Act exempts processing for research, archiving or statistical purposes where personal "
                "data is not used to take decisions about the individual and the prescribed standards are met.",
                "<strong>Return results</strong>: share findings with the communities who provided the data."]),
            H("indigo", "See " + L("research-ethics.html", "Research Ethics 101") + " and "
              + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101") + "."),
        ]),

        S("Fieldwork", "Who asks the question shapes the answer", [
            B("The caste of enumerators and facilitators affects what respondents say and who "
              "agrees to take part. A Dalit respondent may hesitate to report discrimination to an "
              "upper-caste interviewer from a nearby village; an upper-caste respondent may "
              "answer an untouchability question differently to a Dalit interviewer. Plan teams "
              "and protocols with this in mind."),
            TC([P("green", "Good practice",
                  "Mixed-caste teams, with matching where sensitive questions are asked. Interviews "
                  "in private. Training on caste-sensitive conduct, including where to sit and "
                  "accepting water. Field supervisors who can handle complaints.")],
               [P("amber", "Watch for",
                  "Enumerators skipping the Dalit tola because it is far or 'unsafe'. Respondents "
                  "being interviewed with a landlord present. Staff refusing food or water from "
                  "Dalit households, which damages trust and may be an offence.")]),
            H("cyan", "Qualitative techniques for sensitive topics are in "
              + L("qual-methods.html", "Qualitative Methods 101") + "."),
        ]),

        S("Inside organisations", "Caste inside your own organisation", [
            B("Development organisations reproduce the caste patterns of the society around them. "
              "Senior staff in Indian NGOs, research institutes and foundations are often drawn "
              "from a narrow set of castes, while drivers, cleaners and field staff come from "
              "others. Rohith Vemula, a Dalit PhD scholar at the University of Hyderabad, died by "
              "suicide on 17 January 2016; his death prompted national debate about caste "
              "discrimination in institutions that see themselves as progressive."),
            T(["Practice", "What to do"],
              [["Recruitment", "Advertise widely, use structured interviews, review shortlists by category"],
               ["Pay and roles", "Check whether sanitation and support roles are filled by one caste"],
               ["Grievances", "Name caste discrimination in the anti-harassment policy, with a safe channel"],
               ["Leadership", "Track representation in management and the board, by consent"],
               ["Partners", "Ask partner organisations the same questions"]]),
            H("amber", "Safeguarding systems should cover caste harm. See "
              + L("safeguarding-psea.html", "Safeguarding &amp; PSEA 101") + "."),
        ]),

        S("Writing and reporting", "How to write about caste", [
            B("The way a report describes caste affects how readers understand the people in it. "
              "Precise, sourced and non-sensational writing protects participants and makes the "
              "evidence more credible to policymakers. These rules apply to donor reports, "
              "academic papers and social media alike."),
            T(["Instead of", "Write"],
              [["'Lower castes are backward'", "'SC households in the sample had lower enrolment (source, year)'"],
               ["A caste name as a descriptor of behaviour", "The behaviour, with no caste label"],
               ["'Caste violence broke out'", "'Members of [group] attacked [group] on [date] (source)'"],
               ["'Upliftment of Dalits'", "'Access to [service] for SC households rose from X% to Y%'"],
               ["Photographs of identifiable victims", "Consent-based images, or none"]]),
            H("cyan", "Ethical use of images is discussed in " + L("visual-eth.html", "Visual Ethnography 101") + "."),
        ]),

        # ===================== SECTION 11 =====================
        DIV("11", "Eleven", "Movements, open questions and where next"),

        S("Dalit movements", "Dalit movements: from Mahad to the ballot box", [
            B("Dalit politics has moved through several forms. On 20 March 1927 Ambedkar led the "
              "Mahad Satyagraha to drink from the public Chavdar tank. On 14 October 1956 at Nagpur "
              "he and several hundred thousand followers converted to Buddhism. The Dalit Panthers formed in "
              "Bombay in 1972, led by young writers including Namdeo Dhasal, J. V. Pawar and Raja "
              "Dhale. Kanshi Ram founded the Bahujan Samaj Party on 14 April 1984."),
            T(["Phase", "Example", "Strategy"],
              [["Civic rights", "Mahad Satyagraha, 1927", "Claiming public resources"],
               ["Religious exit", "Conversion at Nagpur, 1956", "Leaving the caste order"],
               ["Cultural assertion", "Dalit Panthers, 1972", "Literature, protest, self-naming"],
               ["Electoral power", "Bahujan Samaj Party, 1984", "Winning office for Bahujan voters"],
               ["Legal and digital campaigns", "Protests after Mahajan, 2018", "Defending the PoA Act"]]),
            H("cyan", "Programmes that work with these movements, as partners, gain legitimacy and "
              "local knowledge."),
        ]),

        S("Adivasi movements", "Adivasi movements: land, forest and self-rule", [
            B("Adivasi resistance long predates independence. The Santhal Hul began on 30 June "
              "1855 under Sidho and Kanho Murmu and their siblings. Later tenancy laws, such as the "
              "Santhal Pargana Tenancy Act, restrict the transfer of Adivasi land in that region. "
              "After 1950, Adivasi movements focused on displacement by dams and mines, forest "
              "rights and self-governance in Fifth Schedule areas."),
            T(["Law", "Date", "What it does"],
              [["Panchayats (Extension to the Scheduled Areas) Act (PESA)", "24 December 1996",
                "Extends Part IX to Scheduled Areas; gram sabha powers over minor forest produce, land alienation"],
               ["Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act",
                "Assent 29 December 2006; in force 31 December 2007",
                "Recognises individual and community forest rights through the gram sabha"]]),
            H("amber", "STs are a constitutional category distinct from caste, but they share "
              "exclusion from land and services. See " + L("env-justice.html", "Environmental Justice 101") + "."),
        ]),

        S("Open questions", "Debates practitioners should follow", [
            B("Several questions in this field remain open as of October 2026, and the answers will "
              "affect programmes and data for years. Each is worth watching through primary "
              "sources: Gazette notifications, judgments and Census releases."),
            T(["Question", "Why it matters", "What to watch"],
              [["How will Census 2027 code caste?", "Defines categories for decades of research",
                "Enumerator instructions, code lists and the first caste tables"],
               ["Will states sub-classify SC quotas?", "Changes who benefits within SC reservation",
                "State laws citing Davinder Singh; data used to justify them"],
               ["Will SC status extend to Dalit Christians and Muslims?", "Affects millions excluded from SC benefits",
                "Release of the Balakrishnan Commission report; Ghazi Saaduddin"],
               ["What follows Article 334 in 2030?", "Political reservation ends unless extended",
                "Constitutional amendment before January 2030"],
               ["Does the 50% ceiling survive new caste data?", "States may seek higher OBC shares",
                "Litigation after Census 2027"]]),
            H("green", "Read " + L("advocacy-basics.html", "Advocacy Basics 101")
              + " for turning these questions into evidence-based campaigns."),
        ]),

        S("Summary", "Ten points to take away", [
            B("If you remember nothing else from this course, remember these. Each one connects "
              "to a design decision, a data choice or a legal duty in programme work."),
            BL(["Caste is a structure that allocates land, work, marriage and respect; treat it as such.",
                "Jati is the unit that matters in the field; varna is a textual scheme.",
                "Endogamy reproduces caste; gender control enforces endogamy.",
                "Article 17 abolishes untouchability; the PCR Act 1955 and PoA Act 1989 enforce it.",
                "Reservation rests on Articles 15, 16, 330, 332 and 341, and on Indra Sawhney (1992).",
                "Davinder Singh (2024) permits SC sub-classification; creamy layer for SCs and STs was not decided.",
                "Discrimination persists in formal hiring, markets and enterprise ownership.",
                "Caste data is thin; Census 2027 (reference date 1 March 2027) will change that.",
                "Caste exists across religions and across South Asia, with different laws.",
                "Collect caste data with consent, minimum detail and strong protection."]),
            H("cyan", "Return to the three questions from Section 1 whenever you review a programme."),
        ]),

        S("Where next", "Where next: related courses", [
            B("Caste connects to almost every other course in the ImpactMojo 101 Series. These are "
              "the most direct next steps, chosen to deepen the law, the economics and the "
              "methods used in this deck."),
            TC([BL(["Marginalised groups and rights: " + L("social-margins.html", "Social Margins 101"),
                    "Articles, rights and remedies: " + L("ind-constitution.html", "Indian Constitution 101"),
                    "Measuring group and individual gaps: " + L("inequality-basics.html", "Inequality Basics 101"),
                    "Interests, elites and policy: " + L("pol-economy.html", "Political Economy 101"),
                    "Labour markets and informality: " + L("work-labour-livelihoods.html", "Work, Labour &amp; Livelihoods 101")])],
               [BL(["Consent, risk and sensitive data: " + L("research-ethics.html", "Research Ethics 101"),
                    "Rights frameworks: " + L("human-rights.html", "Human Rights 101"),
                    "Gender and intersectionality: " + L("gender-dev.html", "Gender &amp; Development 101"),
                    "Asking caste in surveys: " + L("survey-design.html", "Survey Design 101"),
                    "Identifying discrimination effects: " + L("causal-inference.html", "Causal Inference 101")])]),
            H("green", "All courses are free. Start with Social Margins 101 if you work directly "
              "with Dalit and Adivasi communities."),
        ]),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Caste Studies 101 &middot; Complete",
         "headline": "See the structure,<br>then change the design",
         "byline": "Caste shapes who owns land, who gets hired and who is counted. Bring the three "
                   "questions, the law and the evidence from this course to every programme you "
                   "design, and collect caste data with care. Explore the rest of the ImpactMojo "
                   "101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

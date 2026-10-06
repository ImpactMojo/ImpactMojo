# -*- coding: utf-8 -*-
"""
Public Policy 101: ImpactMojo 101 Series (native deck spec)
How public policy is made, chosen, carried out and tested, for development practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py public_policy

Sources opened while writing (October 2026):
- VB-G RAM G Act 2025 (Act No. 36 of 2025, 20 December 2025), ss 3, 4, 5, 6, 22, 37:
  https://www.indiacode.nic.in/bitstream/123456789/22478/1/a2025-36.pdf
- India Code text of the Act as on 1 July 2026, footnote: in force 1 July 2026 by S.O. 2382(E), 11 May 2026
- SCC Online blog, 12 May 2026, Act in force and MGNREGA repealed from 1 July 2026 (MoRD notification of 11 May 2026):
  https://www.scconline.com/blog/post/2026/05/12/vbgramg-act-implemented-from-1-july-2026/
- National Rural Employment Guarantee Act 2005 (No. 42 of 2005), ss 3 and 22 (PRS copy):
  https://prsindia.org/files/bills_acts/acts_parliament/2005/the-national-rural-employment-guarantee-act-2005.pdf
- PRS, Parliament as a Law Making Body, 2 December 2014 (pre-legislative consultation policy, 30 days; 15th LS ~70% referral):
  https://prsindia.org/files/parliament/discussion_papers/1417684398--Parliament%20as%20a%20Law%20Making%20Body_0.pdf
- PRS, Vital Stats: Functioning of the 17th Lok Sabha (bill referral 60/71/28/16 per cent; ~1,700 committee meetings):
  https://prsindia.org/files/parliament/vital_stats/Functioning-17th_Lok_Sabha.pdf
- PIB, Cabinet press note and resolution constituting NITI Aayog, 1 January 2015:
  https://pib.gov.in/newsite/PrintRelease.aspx?relid=114268
- DMEO OOMF page (outlays mapped to outputs and outcomes): https://dmeo.gov.in/hi/output-outcome-framework
- DMEO, DGQI 1.0 Methodology Toolkit (data preparedness; six themes):
  https://dmeo.gov.in/sites/default/files/2021-08/DGQI-1.0_Methodology_Toolkit.pdf
- DMEO home page (constituted September 2015, merger of PEO and IEO; OOMF, DGQI): https://dmeo.gov.in/
- DMEO, Evaluation of Centrally Sponsored Schemes: Women & Child Development Sector, March 2021 (IPE Global):
  https://dmeo.gov.in/sites/default/files/2021-04/P2_Women_and_Child_Sector_Best_Practices_Compendium_2021.pdf
- Government of India (Transaction of Business) Rules 1961, as amended to 13 January 2025, rules 4, 6, 7, Second Schedule:
  https://cabsec.gov.in/writereaddata/transactionofbusinessrulescomplete/completeaobrules/english/1_Upload_3983.pdf
- Constitution of India, Article 74(1): https://www.constitutionofindia.net/articles/article-74-council-of-ministers-to-aid-and-advise-president/
- Constitution of India (Legislative Department, as on 1 May 2024), Seventh Schedule, List II entries 2, 6, 14;
  List III entries 23, 25 (entry 25 substituted by the 42nd Amendment Act 1976, s57):
  https://legislative.gov.in/constitution-of-india/
- Indian Kanoon: S.P. Gupta v President of India, 30 December 1981 (AIR 1982 SC 149), https://indiankanoon.org/doc/1294854/ ;
  Hussainara Khatoon v Home Secretary, State of Bihar, orders of February to May 1979, https://indiankanoon.org/doc/1007347/
- Wikipedia, Public interest litigation in India: https://en.wikipedia.org/wiki/Public_interest_litigation_in_India
- iPleaders, S.P. Gupta v Union of India, AIR 1982 SC 149: https://blog.ipleaders.in/s-p-gupta-v-union-of-india-case-analysis/
- Supreme Court interim order of 2 May 2003 in PUCL v Union of India, WP(C) 196 of 2001 (recites order of 28 November 2001),
  Right to Food Campaign copy (archived): http://web.archive.org/web/20120110211740/http://www.righttofoodindia.org:80/orders/may203.html
- Justice K.S. Puttaswamy (Retd.) v Union of India, 26 September 2018 (Aadhaar): https://indiankanoon.org/doc/127517806/
- Wikipedia, Public policy (Dye 1972; Lasswell 1956): https://en.wikipedia.org/wiki/Public_policy
- Conflict Research Consortium, summary of Lasswell, The Decision Process (1956): https://www.beyondintractability.org/bksum/lasswell-decision
- Crossref, Lindblom (1959) PAR 19(2): 79; Kapur (2020) JEP 34(1): 31-54; Dasgupta and Kapur (2020) APSR 114(4): 1316-1334
  (https://api.crossref.org/works/10.2307/973677 and siblings); Texas Politics, Theory and Reality in Public Policy Formation:
  https://texaspolitics.utexas.edu/archive/html/bur/features/0303_02/muddling.html
- Wikipedia, Multiple streams framework: https://en.wikipedia.org/wiki/Multiple_streams_framework
- Open Library records: Kingdon 1984 (Little, Brown); Baumgartner and Jones 1993 (University of Chicago Press);
  Lipsky 1980 (Russell Sage); Pressman and Wildavsky 1973 (University of California Press); Hood 1983; Thaler and Sunstein 2008
  (https://openlibrary.org/search.json)
- Cairney, Understanding Public Policy, chapter 9, Punctuated Equilibrium (Stirling repository):
  https://storre.stir.ac.uk/bitstream/1893/16029/1/Paul%20Cairney%20Understanding%20Public%20Policy%20chapter%209%20STORRE.pdf
- IPPA teaching resource on Hood (1983): https://www.ippapublicpolicy.org/teaching-ressource/the-policy-instrument-approaches/4
- Gilson (2015), Lipsky's Street Level Bureaucracy, Oxford Handbook of Classics of Public Policy (quotes Lipsky 1980, p.xiii):
  https://researchonline.lshtm.ac.uk/id/eprint/2305355/1/Gilson%20-%20Lipsky%27s%20Street%20Level%20Bureaucracy.pdf
- Pritchett (2009), Is India a Flailing State?, HKS RWP09-013: https://ideas.repec.org/p/ecl/harjfk/rwp09-013.html
- Kapur (2020) abstract: https://www.aeaweb.org/articles?id=10.1257/jep.34.1.31
- Dasgupta and Kapur (2020) abstract: https://api.crossref.org/works/10.1017/S0003055420000477
- Chaudhury et al. (2006) JEP 20(1): 91-116: https://ideas.repec.org/a/aea/jecper/v20y2006i1p91-116.html
- Muralidharan, Das, Holla and Mohpal (2017) JPubE 145: 116-135: https://ideas.repec.org/a/eee/pubeco/v145y2017icp116-135.html
- Muralidharan, Niehaus and Sukhtankar (2016) AER 106(10): 2895-2929: https://ideas.repec.org/a/aea/aecrev/v106y2016i10p2895-2929.html
- Banerjee, Duflo, Imbert, Mathew and Pande (2020) AEJ Applied 12(4): 39-72: https://ideas.repec.org/a/aea/aejapp/v12y2020i4p39-72.html
- Muralidharan, Niehaus and Sukhtankar, NBER WP 26744 (2020, rev. 2021), and full text (Jharkhand PDS):
  https://www.nber.org/papers/w26744 ; https://www.nber.org/system/files/working_papers/w26744/w26744.pdf
- PIB / Ministry of Finance, India's DBT: Boosting Welfare Efficiency, 21 April 2025:
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/apr/doc2025421543301.pdf
- Economic Survey 2014-15, Vol I, chapter 3, JAM Number Trinity (Table 3.1):
  https://www.indiabudget.gov.in/budget2015-2016/es2014-15/echapvol1-03.pdf
- Economic Survey 2018-19, Vol I, chapter 2, Policy for Homo Sapiens (nudge; Figure 2):
  https://www.indiabudget.gov.in/budget2019-20/economicsurvey/doc/vol1chapter/echap02_vol1.pdf
- PIB, Give UP Campaign of LPG Subsidy, Lok Sabha reply, 3 August 2015: https://pib.gov.in/newsite/PrintRelease.aspx?relid=124158
- MoPNG, Give it Up (1.13 crore as on 1 April 2023): https://mopng.gov.in/en/marketing/give-it-up
- PIB backgrounder on the single-use plastic ban, 1 July 2022:
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2022/jul/doc20227169001.pdf
- Digital Personal Data Protection Act 2023, Gazette of India, 11 August 2023, s17(2)(b)
- Khan and Qutub, The Benazir Income Support Programme and the Zakat Programme, ODI, November 2010:
  https://cdn.odi.org/media/documents/7247.pdf
- BISP programme pages (Kafaalat UCT; Taleemi Wazaif CCT; Nashonuma CCT): https://bisp.gov.pk/
- Pakistan Economic Survey 2024-25, chapter 16, Social Protection, Table 16.4:
  https://www.finance.gov.pk/survey/chapter_25/16_Social_Protection.pdf
- Wikipedia, Eighteenth Amendment to the Constitution of Pakistan
- Kotagama, A Rapid Appraisal of the Aswesuma Social Benefit Scheme, CEPA, 27 June 2023: https://cepa.lk/?p=6432
- Budget speech 1991-92, Manmohan Singh, 24 July 1991, paras 2, 5, 11: https://www.indiabudget.gov.in/doc/bspeech/bs199192.pdf
- RBI publication on the 1991 crisis (gold pledged with the Bank of England): https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=13843
- GSDRC, Problem-driven tools (Fritz, Kaiser and Levy 2009): https://gsdrc.org/topic-guides/political-economy-analysis/tools/problem-driven-tools/
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


VBG = "VB-G RAM G Act 2025 (Act No. 36 of 2025)"
NREGA = "National Rural Employment Guarantee Act 2005 (No. 42 of 2005)"
TOB = "Government of India (Transaction of Business) Rules 1961, as amended to 13 January 2025"
PRS14 = "PRS Legislative Research, Parliament as a Law Making Body, 2 December 2014"
PRS17 = "PRS Legislative Research, Vital Stats: Functioning of the 17th Lok Sabha"
ES15 = "Economic Survey 2014-15, Vol I, chapter 3, Table 3.1"
ES19 = "Economic Survey 2018-19, Vol I, chapter 2"

DECK = {
    "slug": "public-policy-101",
    "title": "Public Policy 101",
    "description": ("Public Policy 101: a free foundational course for development practitioners in "
                    "South Asia. What public policy is, the policy cycle and its critics (Lindblom, "
                    "Kingdon, punctuated equilibrium), policy instruments from regulation to nudges, "
                    "how policy is made in India (Cabinet, ministries, NITI Aayog, Parliament and its "
                    "committees, the 2014 pre-legislative consultation policy, the Seventh Schedule, "
                    "courts and PILs), implementation and street-level bureaucracy, evidence and DMEO, "
                    "and cases from MGNREGA to the VB-G RAM G Act 2025, Aadhaar-linked DBT, Pakistan's "
                    "BISP and Sri Lanka's Aswesuma. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Public<br>Policy<br>101",
         "sub": "How governments decide what to do, choose their tools, carry decisions out and "
                "learn whether they worked: a foundational course for development practitioners "
                "in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Cabinet to Panchayat"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "What public policy is"},
             {"name": "The policy cycle"},
             {"name": "Theories that complicate the cycle"},
             {"name": "Policy instruments"},
             {"name": "How policy is made in India"},
             {"name": "Implementation and state capacity"},
             {"name": "Evidence in policy"},
             {"name": "South Asian cases"},
             {"name": "Stakeholders and political economy"},
             {"name": "A practitioner's toolkit"},
             {"name": "Writing a policy brief, and where next"},
         ]},

        # ===================== SECTION 01 =====================
        DIV("01", "One", "What public policy is"),

        S("Starting point", "Public policy is what reaches a household, or fails to", [
            B("A woman in a village in Jharkhand collects rice at a ration shop after her thumbprint "
              "is checked against a national database. A child in Tamil Nadu eats a cooked meal at "
              "school. A shopkeeper in Delhi stops handing out thin plastic carry bags. Each of these "
              "moments is the end of a long chain of public decisions: a law, a set of rules, a "
              "budget line, a court order, an officer's instruction. Public policy is the name for "
              "that chain, and this course follows it from the Cabinet room to the ration shop."),
            TC([P("cyan", "What this course covers",
                  "How issues reach government, how options are chosen, which tools governments "
                  "use, how decisions are carried out by real officials, and how anyone can tell "
                  "whether a policy worked.")],
               [P("amber", "Why practitioners need it",
                  "Almost every programme an NGO or funder runs sits inside a policy it did not "
                  "write. Knowing how that policy is made and changed is how a pilot becomes a "
                  "scheme, and how a scheme gets fixed.")]),
            H("indigo", "Facts in this deck are stated as of October 2026. Laws, schemes and "
              "numbers change, so check the latest text before you rely on any of them."),
        ]),

        S("Definition", "Whatever governments choose to do or not to do", [
            B("The most quoted definition comes from the American political scientist Thomas Dye: "
              "public policy is \"whatever governments choose to do or not to do\" (Dye, "
              "<em>Understanding Public Policy</em>, 1972, p. 2). It is short on purpose. It "
              "includes laws and spending, and it also includes decisions to leave a problem alone. "
              "Critics call it too broad to be useful, because almost anything a government does "
              "then counts as policy."),
            TERM("Public policy (working definition for this course)",
                 "A course of action, or a deliberate inaction, adopted by a public authority to "
                 "deal with a problem, expressed through law, rules, budgets, programmes, orders "
                 "or official statements, and carried out by public officials."),
            TC([B("<strong>Choice:</strong> policy involves a decision among options, even when "
                  "the decision is to wait.", sm=True)],
               [B("<strong>Authority:</strong> it is backed by the state's power to command, "
                  "spend, inform or organise, which private action lacks.", sm=True)]),
            H("cyan", "Source: Dye's definition as cited in Wikipedia, Public policy (Dye 1972: 2)."),
        ]),

        S("Forms of policy", "One policy, many legal forms", [
            B("In South Asia a single policy usually lives in several documents at once, each with "
              "a different legal force. Practitioners who read only the scheme guidelines often "
              "miss the Act that creates the entitlement, or the court order that set the minimum "
              "standard. The table below shows the main forms with Indian examples checked for "
              "this course."),
            T(["Form", "What it does", "Indian example"],
              [["Act of Parliament", "Creates rights, duties and institutions; binding",
                "VB-G RAM G Act 2025, s5: 125 days of guaranteed work a year"],
               ["Rules under an Act", "Detail made by the executive under a power in the Act",
                "Plastic Waste Management Amendment Rules 2021 (notified 12 August 2021)"],
               ["Scheme", "A plan of spending and delivery, often made under an Act",
                "Each State must notify a Scheme within six months (VB-G RAM G Act, s3)"],
               ["Executive resolution", "Creates bodies or policies without a statute",
                "Cabinet resolution constituting NITI Aayog, 1 January 2015"],
               ["Court order", "Directs the state to act on a right",
                "Supreme Court order of 28 November 2001 on cooked midday meals"]]),
            H("amber", "Always ask: which document creates the right, and which only describes "
              "how it will be delivered? The answer decides what a citizen can enforce."),
        ]),

        S("Why government acts", "The classic reasons for public action", [
            B("Economists and political scientists give several reasons why a problem becomes a "
              "public responsibility. These are reasons to consider public action. None of them "
              "proves that a particular government programme will work better than doing nothing, "
              "which is a separate question this course returns to in Sections 6 and 7."),
            TC([BL(["<strong>Public goods:</strong> things like flood protection or disease "
                    "surveillance that markets underprovide because people cannot be excluded.",
                    "<strong>Externalities:</strong> costs or benefits that fall on others, such "
                    "as littered plastic or a child's vaccination protecting neighbours."])],
               [BL(["<strong>Information gaps:</strong> buyers cannot judge food safety or "
                    "medicine quality on their own.",
                    "<strong>Equity and rights:</strong> a society may decide that no one should "
                    "go without food or basic schooling, whatever the market does."])]),
            H("indigo", "In practice the reason a government gives shapes the tool it picks: a "
              "rights argument points to an entitlement law, an externality argument to a tax or a "
              "ban."),
        ]),

        S("Inaction", "Deciding not to act is also a policy", [
            B("The second half of Dye's definition matters in practice. When a government keeps an "
              "issue off its agenda, leaves a law without rules, or lets a scheme run without "
              "evaluation, that is a choice with consequences. Political scientists call issues "
              "that never reach a formal decision <strong>non-decisions</strong>. They are hard to "
              "study because nothing is written down."),
            TC([P("amber", "Visible inaction",
                  "A law passed with no rules notified, so its rights cannot be claimed. A bill "
                  "introduced and allowed to lapse. A committee report that receives no action "
                  "taken reply.")],
               [P("red", "Invisible inaction",
                  "A problem that affects people with little political voice is never discussed "
                  "at all. No file is opened, so no record exists to show the choice was "
                  "made.")]),
            H("cyan", "Practical habit: when you study a policy problem, list what the government "
              "has <em>not</em> done as carefully as what it has done. Gaps are often where "
              "advocacy and research can add most."),
        ]),

        S("Actors", "Who makes policy in South Asia", [
            B("Policy is made by many actors with different powers. Formal authority sits with the "
              "executive, the legislature and the courts. Real influence also comes from the "
              "bureaucracy, state and local governments, parties, donors, business, civil society "
              "and the media. Section 9 shows how to map them for a specific issue."),
            T(["Actor", "Main lever", "Example in this course"],
              [["Union Cabinet and ministries", "Drafts laws, rules, schemes and budgets",
                "Transaction of Business Rules 1961, rule 4 consultations"],
               ["Parliament and its committees", "Passes laws, scrutinises bills and budgets",
                "16% of bills referred to committees in the 17th Lok Sabha"],
               ["State governments", "Legislate on State List subjects; implement most schemes",
                "States notify the VB-G RAM G Scheme and pay 40% (60:40 States)"],
               ["Courts", "Interpret rights; issue directions in PILs",
                "PUCL v Union of India, cooked midday meals (2001)"],
               ["Frontline officials", "Exercise discretion in delivery", "Lipsky's street-level bureaucrats"]]),
            H("amber", "The same pattern holds across the region: Pakistan's provinces gained "
              "education, health and social welfare functions under the Eighteenth Amendment of "
              "2010."),
        ]),

        S("Values in conflict", "Every policy trades off values", [
            B("Policy choices rarely pit good against bad. They pit good against good: speed "
              "against care, efficiency against equity, a tight target against wide coverage. "
              "The same word can also mean different things to different sides: fairness to a "
              "taxpayer may mean paying only for the needy, while fairness to a farm worker may "
              "mean a benefit nobody has to prove they deserve."),
            TC([BL(["<strong>Efficiency:</strong> the most outcome per rupee.",
                    "<strong>Equity:</strong> who gains and who bears the cost.",
                    "<strong>Liberty:</strong> how far the state restricts choice."])],
               [BL(["<strong>Security:</strong> protection from shocks and risk.",
                    "<strong>Accountability:</strong> whether someone can be made to answer.",
                    "<strong>Feasibility:</strong> whether the state can actually deliver it."])]),
            H("indigo", "Example from this course: biometric authentication in the ration system "
              "trades leakage control (efficiency) against the risk of turning away eligible "
              "families (equity). Section 8 shows the evidence on both sides."),
        ]),

        # ===================== SECTION 02 =====================
        DIV("02", "Two", "The policy cycle"),

        S("Origins", "From Lasswell's seven functions to the five-stage cycle", [
            B("In 1956 the political scientist Harold Lasswell divided the decision process into "
              "seven functions: intelligence, recommendation, prescription, invocation, "
              "application, appraisal and termination. Later textbooks condensed his list into the "
              "familiar policy cycle. The stages give a common vocabulary for asking where a "
              "policy is, and what kind of work it needs next."),
            FL(["Agenda setting: a problem gets official attention",
                "Formulation: options are designed and compared",
                "Adoption: an authority decides",
                "Implementation: officials carry it out",
                "Evaluation: results are judged and fed back"]),
            TC([B("<strong>Strength:</strong> a simple map that fits how ministries, donors and "
                  "evaluators already organise work.", sm=True)],
               [B("<strong>Weakness:</strong> real policy rarely moves in order. Section 3 "
                  "covers the theories built to correct it.", sm=True)]),
            H("cyan", "Sources: Conflict Research Consortium summary of Lasswell, <em>The Decision "
              "Process</em> (1956); Wikipedia, Public policy."),
        ]),

        S("Stage 1", "Agenda setting: how a problem gets attention", [
            B("Thousands of problems compete for a government's attention and only a few get it. "
              "Scholars distinguish the broad public agenda, the issues people talk about, from the "
              "institutional agenda, the issues a Cabinet, legislature or court is actually "
              "considering. Moving an issue from the first to the second is the purpose of most "
              "advocacy."),
            TC([BL(["<strong>Crises:</strong> a drought, an epidemic or a financial shock.",
                    "<strong>Elections and manifestos:</strong> promises that a new government "
                    "must be seen to keep.",
                    "<strong>Data:</strong> a survey round or audit report that shows a problem "
                    "is worse than assumed."])],
               [BL(["<strong>Courts:</strong> a PIL can force an issue onto every state's "
                    "agenda at once.",
                    "<strong>Media and movements:</strong> sustained coverage or protest.",
                    "<strong>Donors and global targets:</strong> commitments made abroad that "
                    "need domestic action."])]),
            H("amber", "Example: the Supreme Court's order of 28 November 2001 in PUCL v Union "
              "of India put cooked midday meals on the agenda of every state government, including "
              "those that had not planned them."),
        ]),

        S("Stage 2", "Formulation: designing options inside government", [
            B("Formulation turns a problem into a proposal. In India the formal route runs through "
              "the ministry that owns the subject, which must consult other departments before a "
              "proposal goes further. Rule 4 of the " + TOB + " sets out the main consultations, "
              "and they explain why a draft often changes before anyone outside government sees "
              "it."),
            T(["Who must be consulted", "On what (rule 4)", "Why it matters for design"],
              [["Any department affected", "Cases that concern more than one department (4(1))",
                "Overlapping mandates must be settled first"],
               ["Ministry of Finance", "Orders with a financial bearing, new spending, posts (4(2))",
                "Cost and fiscal space shape what survives"],
               ["Ministry of Law", "Proposals for legislation; general rules and orders (4(3))",
                "Legal form and constitutional fit"],
               ["Department of Personnel and Training", "Recruitment and service conditions (4(4))",
                "Staffing rules for new bodies"],
               ["Ministry of External Affairs", "Matters affecting external relations (4(5))",
                "Treaty and foreign aid implications"]]),
            H("cyan", "Source: " + TOB + ", rule 4."),
        ]),

        S("Stage 3", "Adoption: who has the power to decide", [
            B("A proposal becomes policy only when an authority with legal power adopts it. Under "
              "Article 74(1) of the Constitution the Council of Ministers, headed by the Prime "
              "Minister, aids and advises the President, who acts on that advice. The Second "
              "Schedule to the Transaction of Business Rules lists the cases that must go to the "
              "full Cabinet, starting with \"cases involving legislation including the issue of "
              "Ordinances\"."),
            FL(["Ministry drafts and consults",
                "Cabinet approves the bill or decision",
                "Parliament passes the bill",
                "President assents; the Act is notified",
                "Rules, schemes and guidelines follow"]),
            TC([P("green", "Executive decisions",
                  "Schemes, resolutions and many rules are adopted by the executive alone, within "
                  "powers already given by law or the Constitution.")],
               [P("indigo", "Legislative decisions",
                  "New rights and duties need an Act. Parliament can amend, delay or refer the "
                  "bill to a committee before passing it.")]),
        ]),

        S("Stage 4", "Implementation: where most policies succeed or fail", [
            B("Adoption fixes what should happen. Implementation is what does happen. In India most "
              "social policy is delivered by state governments and local bodies even when the "
              "Union designs and funds it. The VB-G RAM G Act 2025 shows the division of labour "
              "written into law: the Union sets the framework and the normative allocation, each "
              "State must notify its own Scheme within six months of commencement (s3), and Gram "
              "Panchayats prepare Viksit Gram Panchayat Plans from which works originate (s4)."),
            TC([BL(["Union: framework, funds, rules, monitoring",
                    "State: Scheme, staff, wage payment, unemployment allowance",
                    "Panchayat: registration, planning, execution of works"])],
               [BL(["Frontline staff: deciding whose work demand is recorded and when",
                    "Banks and payment systems: whether money arrives on time",
                    "Citizens: whether they know the entitlement and claim it"])]),
            H("amber", "Section 6 is about what goes wrong at this stage, and why designing for "
              "implementation from the first draft is cheaper than fixing it later."),
        ]),

        S("Stage 5", "Evaluation: learning whether the policy worked", [
            B("Evaluation asks whether a policy did what it promised, at what cost, and for whom. "
              "India's main government evaluation body is the Development Monitoring and "
              "Evaluation Office (DMEO), an attached office of NITI Aayog constituted in September "
              "2015 by merging the Programme Evaluation Office and the Independent Evaluation "
              "Office. To inform the Fifteenth Finance Commission's deliberations, the Ministry of Finance "
              "entrusted DMEO with evaluations of Centrally Sponsored Schemes, reported sector by "
              "sector; the Women and Child Development report is dated March 2021."),
            ST([C("Sept 2015", "DMEO constituted (PEO and IEO merged)", "cyan", "DMEO website"),
                C("March 2021", "CSS evaluation, Women &amp; Child Development sector", "indigo",
                  "DMEO, analysis by IPE Global"),
                C("12", "States and UTs covered by that report's fieldwork", "green",
                  "DMEO, CSS evaluation, WCD sector, 2021")], cols=3),
            H("cyan", "Evaluation is useful only if it reaches the next decision. Linking scheme "
              "renewal to evaluation, as in the Finance Commission cycle, is one way to make "
              "that happen."),
        ]),

        S("Worked mapping", "The cycle applied: from MGNREGA to VB-G RAM G", [
            B("The replacement of India's rural employment guarantee shows every stage of the "
              "cycle. The table maps the steps that can be checked in public documents. It does "
              "not try to explain why the change happened, which needs the theories in Section 3 "
              "and the political economy tools in Section 9."),
            T(["Stage", "What happened", "Source"],
              [["Earlier policy", "NREGA 2005 guaranteed at least 100 days a year (s3)", NREGA],
               ["Adoption", "VB-G RAM G Act enacted, Act No. 36 of 2025, dated 20 December 2025", VBG],
               ["Commencement", "Ministry of Rural Development notification S.O. 2382(E) of 11 May 2026: in force from 1 July 2026",
                VBG + ", India Code footnote"],
               ["Repeal", "MGNREGA repealed from the appointed date, with savings for past acts (s37)", VBG],
               ["Implementation", "States to notify Schemes within six months (s3)", VBG],
               ["Evaluation", "Too early for evidence on outcomes as of October 2026", "None yet"]]),
            H("amber", "Treat any claim about the new Act's effects with care until data from at "
              "least one full financial year are published."),
        ]),

        S("Uses and limits", "What the cycle is good for, and where it misleads", [
            B("The stage model is a teaching device, and it is useful for organising a policy "
              "analysis or a monitoring plan. It misleads when it is read as a description of how "
              "policy really moves. Stages overlap, decisions are revisited, and implementation "
              "often reshapes the policy so much that the officials who carry it out are, in "
              "effect, still formulating it."),
            TC([P("green", "Use it to",
                  "Locate where a policy is; plan who to engage at each stage; design an "
                  "evaluation that tests the policy's own logic; structure a policy brief.")],
               [P("red", "Do not use it to",
                  "Assume problems are solved in order; predict when change will come; ignore "
                  "power, chance and timing; treat the official decision as the end of "
                  "politics.")]),
            H("indigo", "Section 3 introduces three theories that each correct one weakness of "
              "the cycle: Lindblom on small steps, Kingdon on timing, and Baumgartner and Jones on "
              "sudden change."),
        ]),

        # ===================== SECTION 03 =====================
        DIV("03", "Three", "Theories that complicate the cycle"),

        S("Starting point", "The rational model and its limits", [
            B("The policy cycle carries a hidden assumption: that decision makers define a goal, "
              "list every option, estimate the consequences of each, and choose the best. This is "
              "the <strong>rational-comprehensive</strong> model. It is a useful benchmark for an "
              "analyst. As a description of how governments decide, it fails, because no ministry "
              "has the time, information or agreement on goals that the model needs."),
            TC([P("indigo", "What the rational model assumes",
                  "Clear and agreed objectives; a full list of alternatives; reliable predictions "
                  "of each option's effects; one decision maker who chooses.")],
               [P("amber", "What governments actually face",
                  "Contested goals across departments and parties; limited time; patchy data; "
                  "many actors, each with a veto at some point; pressure to act before analysis "
                  "is complete.")]),
            H("cyan", "Three theories take that gap seriously. Each gives a practitioner a "
              "different question to ask about a policy problem."),
        ]),

        S("Incrementalism", "Lindblom: the science of muddling through", [
            B("Charles Lindblom's article \"The Science of 'Muddling Through'\" (Public "
              "Administration Review 19(2), 1959) contrasted the rational-comprehensive, or "
              "<strong>root</strong>, method with the method of <strong>successive limited "
              "comparisons</strong>, the <strong>branch</strong> method. Administrators, he argued, "
              "look mainly at options that differ only slightly from current policy, and judge a "
              "policy partly by whether the people involved can agree on it."),
            TC([B("<strong>Why small steps:</strong> few options to analyse, mistakes are small and "
                  "reversible, and agreement is easier to reach than agreement on ultimate goals.",
                  sm=True)],
               [B("<strong>The critique:</strong> small steps favour the status quo and those it "
                  "already serves. When a problem needs a large change, incrementalism can "
                  "delay it.", sm=True)]),
            Q("Administrators usually look only at policies that differ in relatively small "
              "degree from the policies currently in effect.",
              "Summary of Lindblom (1959), Texas Politics, University of Texas at Austin"),
        ]),

        S("Incrementalism in practice", "Last year's budget is the best predictor of this year's", [
            B("Incremental thinking is easy to see in public budgets. Departments usually start "
              "from the previous year's allocation and argue over the change, because rebuilding "
              "every line from zero each year is beyond any finance ministry. The example below is "
              "invented for teaching; it shows the logic, and its numbers come from no real "
              "budget."),
            T(["Budget line (Illustrative)", "Last year (Rs crore)", "This year (Rs crore)", "Change"],
              [["Scheme A, established", "1,000", "1,060", "+6%"],
               ["Scheme B, established", "400", "420", "+5%"],
               ["Scheme C, new pilot", "0", "25", "new"],
               ["Scheme D, under review", "300", "300", "0%"]]),
            TC([B("<strong>Implication for practitioners:</strong> a pilot that asks for a small "
                  "new line has better odds than a proposal that requires cutting an "
                  "established scheme.", sm=True)],
               [B("<strong>Implication for evaluators:</strong> because cuts are rare, evidence "
                  "that a scheme fails often changes its design more than its budget.", sm=True)]),
        ]),

        S("Multiple streams", "Kingdon: problems, policies and politics", [
            B("John Kingdon's <em>Agendas, Alternatives, and Public Policies</em> (first published "
              "1984) asked why some issues reach the agenda and others do not. His answer is that "
              "three largely separate streams flow through government. Change becomes possible "
              "when they meet in a <strong>policy window</strong>, and someone is ready to join "
              "them."),
            TC([BL(["<strong>Problem stream:</strong> conditions come to be seen as problems "
                    "needing action, often through data, a crisis or feedback from programmes.",
                    "<strong>Policy stream:</strong> experts, officials and advocates develop and "
                    "refine possible solutions, many of which wait years for use."])],
               [BL(["<strong>Politics stream:</strong> public mood, elections, changes of "
                    "government and pressure from organised interests.",
                    "<strong>Policy entrepreneurs:</strong> people who couple a ready solution "
                    "to a recognised problem when the politics allow."])]),
            H("indigo", "Kingdon's practical lesson: have a worked-out solution ready before the "
              "window opens, because windows close quickly. Source: Wikipedia, Multiple streams "
              "framework; Open Library record for Kingdon (1984)."),
        ]),

        S("Streams applied", "A reading of India's 1991 reforms through three streams", [
            B("The 1991 reforms are often used to illustrate a policy window. The facts below are "
              "documented; the mapping onto Kingdon's streams is an interpretation offered for "
              "teaching, and other readings are possible. The point is the method: separate the "
              "problem, the available ideas and the politics, then ask what joined them."),
            T(["Stream", "1991 (documented facts)", "How it fits the framework"],
              [["Problem", "Reserves of about Rs 2,500 crore would finance imports for a mere fortnight "
                "(Budget speech, 24 July 1991); the RBI pledged gold with the Bank of England to raise loans",
                "A visible crisis made the problem impossible to ignore"],
               ["Policy", "Proposals to dismantle industrial licensing and open sectors to foreign "
                "investment", "Ideas debated for years were ready to use"],
               ["Politics", "A government barely a month in office; exchange rate adjustments on 1 and 3 "
                "July 1991 were the first steps", "A short window in which major change was acceptable"]]),
            H("amber", "Sources for the facts: Budget speech 1991-92 (24 July 1991); RBI. Ask the same "
              "three questions of any reform you study, and look for who coupled the streams."),
        ]),

        S("Punctuated equilibrium", "Baumgartner and Jones: long calm, sudden change", [
            B("Frank Baumgartner and Bryan Jones, in <em>Agendas and Instability in American "
              "Politics</em> (1993), noticed that most policies stay almost unchanged for long "
              "periods and then shift sharply. Their explanation combines limited attention with "
              "power. A small policy community keeps an issue quiet by defining it as technical or "
              "settled. Change comes when the issue's <strong>policy image</strong> is redefined "
              "and it moves to a new <strong>venue</strong> where different people decide."),
            TC([TERM("Policy image", "How an issue is portrayed and understood: as a technical "
                     "matter, a question of rights, a scandal, a fiscal burden.")],
               [TERM("Venue", "The institution where the issue is decided: a ministry, a "
                     "parliamentary committee, a court, a state government.")]),
            H("cyan", "Source: Paul Cairney, <em>Understanding Public Policy</em>, chapter 9, "
              "summarising Baumgartner and Jones (1993). Excluded groups who lose in one venue "
              "have an incentive to go \"venue shopping\" in another."),
        ]),

        S("Venue shift", "The right to food moves into the Supreme Court", [
            B("A clear South Asian example of venue shift is the right to food case. In 2001 the "
              "People's Union for Civil Liberties filed a writ petition (WP(C) 196 of 2001). On 28 "
              "November 2001 the Supreme Court directed governments to provide every child in "
              "government and government-assisted primary schools a prepared midday meal with at "
              "least 300 calories and 8&ndash;12 grams of protein, for at least 200 days a year. "
              "States serving dry rations were told to switch to cooked meals in phases."),
            TC([P("indigo", "What changed",
                  "The issue's image moved from a welfare scheme to a constitutional right, and "
                  "its venue moved from state food and education departments to the Supreme "
                  "Court, which kept monitoring compliance.")],
               [P("amber", "What it did not settle",
                  "Its interim order of 2 May 2003 recorded that Bihar, Jharkhand and Uttar "
                  "Pradesh had not begun, and directed them to start in the poorest districts. A "
                  "new venue changes the decision; delivery still depends on states.")]),
            H("cyan", "Source: Supreme Court interim order of 2 May 2003 in PUCL v Union of India, "
              "reciting the order of 28 November 2001."),
        ]),

        S("Comparison", "Four ways to explain policy change", [
            B("None of these theories is right on its own. Each draws attention to a different "
              "force, and a good analysis uses more than one. The table summarises what each "
              "explains well and what it misses, with the question it suggests for your own "
              "work."),
            T(["Theory", "Explains well", "Misses", "Question for practitioners"],
              [["Policy cycle", "The sequence of official tasks", "Power, timing, overlap",
                "Which stage is this policy at?"],
               ["Incrementalism (Lindblom 1959)", "Stability and small adjustments", "Large, rapid change",
                "What small change could gain agreement?"],
               ["Multiple streams (Kingdon 1984)", "Why issues suddenly reach the agenda",
                "Implementation; non-individual actors", "Is a solution ready for the next window?"],
               ["Punctuated equilibrium (1993)", "Long stability broken by bursts", "Exact timing",
                "Who controls the issue's image and venue?"]]),
            H("indigo", "Political economy analysis (Section 9) adds the missing question in all "
              "four: who gains and who loses, and what will they do about it?"),
        ]),

        # ===================== SECTION 04 =====================
        DIV("04", "Four", "Policy instruments"),

        S("Toolkit", "Hood's four resources of government", [
            B("Once a government decides to act, it must choose a tool. Christopher Hood's <em>The "
              "Tools of Government</em> (1983) grouped the tools by the resource each one uses. "
              "The scheme is often remembered as <strong>NATO</strong>: nodality, authority, "
              "treasure and organisation. Every instrument in this section draws on at least one "
              "of the four."),
            T(["Resource", "Hood's meaning", "South Asian example"],
              [["Nodality", "Being at the centre of information networks",
                "Public campaigns such as Give It Up for the LPG subsidy"],
               ["Authority", "Legitimate power to command or prohibit",
                "Ban on identified single-use plastic items from 1 July 2022"],
               ["Treasure", "Money or exchangeable assets",
                "Direct benefit transfers; BISP cash transfers in Pakistan"],
               ["Organisation", "People, buildings, equipment the state controls",
                "Ration shops, anganwadi centres, public schools"]]),
            H("cyan", "Source: IPPA teaching resource on Hood (1983). The quickest diagnostic for "
              "any scheme: which resource does it rely on, and does the state have enough of it?"),
        ]),

        S("A spectrum", "From laissez faire to mandate", [
            B("India's Economic Survey 2018-19 placed policies on a spectrum by how strongly they "
              "push behaviour: laissez faire, nudge, incentivise and mandate. Its Figure 2 draws "
              "each policy as a bar running from laissez faire to the furthest level it reaches. "
              "The table follows those bars; whether each placement is right is a good discussion "
              "question."),
            T(["Furthest level reached", "Indian examples in the Survey's Figure 2", "What the state does"],
              [["Laissez faire", "Give It Up", "Leaves the choice to the person, with an appeal"],
               ["Nudge", "Aadhaar and Jan Dhan Yojana (part way); Beti Bachao, Beti Padhao; Swachh "
                "Bharat Mission", "Changes how a choice is presented or what is seen as normal"],
               ["Incentivise", "Taxes on tobacco (part way)",
                "Changes the price or payoff of a choice"],
               ["Mandate", "Compulsory voting in panchayat elections in some states (part way); "
                "alcohol bans in some states", "Requires or forbids the behaviour"]]),
            H("amber", "Source: " + ES19 + ", Figure 2, Policies spanning the influence spectrum "
              "in India. Stronger tools are not better tools; they cost more to enforce and "
              "restrict more choice."),
        ]),

        S("Regulation", "Regulation: rules backed by penalties", [
            B("Regulation sets rules and punishes breaches. It looks cheap, because the "
              "government pays little directly. Its real cost sits in inspection and "
              "enforcement. India's ban on identified single-use plastic items is a good example. "
              "The Ministry of Environment, Forest and Climate Change notified the Plastic Waste "
              "Management Amendment Rules 2021 on 12 August 2021, prohibiting identified items "
              "from 1 July 2022."),
            TC([P("green", "What makes it work",
                  "A clear list of banned items; a start date announced about ten months ahead; pollution control "
                  "boards given powers to act; alternatives available at similar cost.")],
               [P("red", "Where it weakens",
                  "Thousands of small sellers to inspect; enforcement left to bodies with few "
                  "staff; demand that does not fall when supply is pushed underground.")]),
            H("cyan", "Source: PIB backgrounder, 1 July 2022, which also notes enforcement powers "
              "under section 5 of the Environment (Protection) Act 1986 and state special task "
              "forces."),
        ]),

        S("Subsidies", "Subsidies: who actually benefits", [
            B("Price subsidies are popular because they look universal. Their benefits often go "
              "to people who consume more, or leak before reaching anyone. The Economic Survey "
              "2014-15 put numbers on this using the NSS 68th round (2011-12) and its own "
              "estimates. The chart shows the share of the public distribution system (PDS) "
              "allocation estimated as lost to leakage, by commodity."),
            {"t": "chart", "canvas": "leakChart",
             "title": "Share of PDS allocation lost as leakage, by commodity (%)",
             "source": ES15,
             "type": "bar",
             "data": {"labels": ["Wheat", "Sugar", "Kerosene", "Rice"],
                      "datasets": [{"label": "Lost as leakage (%)",
                                    "data": [54, 48, 41, 15],
                                    "backgroundColor": ["#B91C1C", "#B45309", "#B45309", "#0369A1"]}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:60, title:{display:true,text:'% of allocation lost'} } } }"}},
            H("amber", "The same table found that the bottom half of households consumed only 25 "
              "per cent of LPG, and the bottom quintile captured 10 per cent of electricity "
              "subsidies against 37 per cent for the top quintile."),
        ]),

        S("Transfers", "Cash and in-kind transfers", [
            B("Transfers give households resources directly. In-kind transfers, such as grain "
              "through ration shops, guarantee a specific good but need a physical supply chain. "
              "Cash transfers are cheaper to deliver and let households choose, but their value "
              "falls with inflation and they need bank access. India's Economic Survey 2014-15 "
              "argued that the <strong>JAM trinity</strong>, Jan Dhan accounts, Aadhaar and "
              "mobile phones, could make direct cash transfers possible at scale."),
            TC([P("cyan", "In kind",
                  "Protects against price spikes; shows clearly what the state provides; can "
                  "target nutrition. Risks: leakage in storage and transport, poor quality, "
                  "ration shop discretion.")],
               [P("green", "Cash",
                  "Lower delivery cost; recipient choice; faster to scale. Risks: exclusion if "
                  "accounts or authentication fail, erosion by inflation, last-mile access to "
                  "cash.")]),
            H("indigo", "Section 8 looks at the evidence on India's move toward direct benefit "
              "transfer, which is more mixed than either side of the debate usually admits."),
        ]),

        S("Conditionality", "Conditional and unconditional transfers", [
            B("A conditional transfer pays only if the household does something, such as keeping "
              "a child in school or attending health check-ups. An unconditional transfer pays "
              "regardless. Pakistan's Benazir Income Support Programme (BISP) runs both kinds: "
              "the Benazir Kafaalat programme makes unconditional payments, while Benazir Taleemi "
              "Wazaif (education stipends) and the Nashonuma programme (maternal and child "
              "health) attach conditions."),
            TC([BL(["<strong>For conditions:</strong> they target a specific behaviour, can build "
                    "political support among taxpayers, and link cash to services.",
                    "<strong>Cost:</strong> someone has to verify compliance, which needs staff "
                    "and data."])],
               [BL(["<strong>Against conditions:</strong> the poorest may be least able to "
                    "comply, often because the school or clinic is far or poor.",
                    "<strong>Design rule:</strong> never condition a payment on a service the "
                    "state cannot supply."])]),
            H("cyan", "Source for BISP components: BISP programme pages (bisp.gov.pk), October 2026."),
        ]),

        S("Information", "Information and persuasion: the Give It Up campaign", [
            B("Governments also act by informing and persuading. India's Give It Up campaign, "
              "launched by the Prime Minister, asked LPG consumers who could afford the market price "
              "to surrender their cooking gas subsidy voluntarily. Each consumer who gave it up was "
              "linked to a BPL household that received an LPG connection in turn. By 28 July 2015, "
              "13.9 lakh consumers had given it up; by 1 April 2023 the Ministry of Petroleum and "
              "Natural Gas put the total at nearly 1.13 crore."),
            TC([P("green", "Why it could work",
                  "Low cost; appeals to social norms and public spirit; uses the state's "
                  "position at the centre of information (Hood's nodality).")],
               [P("amber", "Its limits",
                  "Relies on opt-in, so inertia keeps most eligible-but-better-off households "
                  "in the scheme. The Economic Survey 2018-19 suggested making the default "
                  "opt-out instead.")]),
            H("cyan", "Sources: PIB, Lok Sabha reply of 3 August 2015; Ministry of Petroleum and Natural "
              "Gas, Give it Up page; " + ES19 + "."),
        ]),

        S("Nudges", "Nudges: changing the choice, keeping the freedom", [
            B("Richard Thaler and Cass Sunstein's <em>Nudge</em> (2008) argued that the way a "
              "choice is presented changes what people choose, and that governments can design "
              "choices to help people without forbidding anything. India's Economic Survey "
              "2018-19 drew three principles from this literature: social norms shape behaviour, "
              "people stick with defaults, and repeated reminders sustain good habits."),
            TC([TERM("Default", "The option that applies if a person does nothing. Switching a "
                     "default from opt-in to opt-out often moves behaviour more than any "
                     "subsidy."),
                ],
               [TERM("Choice design", "How options are presented: their "
                     "order, wording, timing and what is pre-selected.")]),
            H("red", "Cautions: nudges work at the margin and rarely fix a missing service. A "
              "default that enrols people automatically can also exclude or burden them if the "
              "system behind it fails, so check who the default leaves out."),
        ]),

        S("Choosing", "Matching the instrument to the problem", [
            B("Instrument choice should follow from a diagnosis of why the problem exists. The "
              "table is a starting point for discussion; real choices also depend on law, "
              "politics and capacity. Use it to check that a proposed tool addresses the cause "
              "you have identified, and to name the main risk before it arrives."),
            T(["If the cause is mainly...", "Consider", "Main risk to plan for"],
              [["Lack of money in poor households", "Cash or in-kind transfers", "Exclusion errors in targeting"],
               ["Harm imposed on others", "Regulation, taxes", "Weak enforcement; evasion"],
               ["People lack information", "Information, labelling, campaigns", "Message ignored or distrusted"],
               ["Inertia or forgetting", "Defaults, reminders (nudges)", "Small effects; silent exclusion"],
               ["No provider exists", "Public provision or contracting (organisation)",
                "Staffing and absence (Section 6)"],
               ["Providers do not perform", "Monitoring, incentives, accountability",
                "Gaming of the measured indicator"]]),
            H("indigo", "Instruments are often combined. VB-G RAM G mixes treasure (wages), "
              "authority (a legal guarantee) and organisation (panchayat-run works)."),
        ]),

        # ===================== SECTION 05 =====================
        DIV("05", "Five", "How policy is made in India"),

        S("Constitutional frame", "The executive: who holds the power to decide", [
            B("India follows a parliamentary system. Article 74(1) of the Constitution provides for "
              "\"a Council of Ministers with the Prime Minister at the head to aid and advise the "
              "President who shall, in the exercise of his functions, act in accordance with such "
              "advice\". Executive action is taken in the President's name, but the decisions are "
              "the government's. Article 77(3) lets the President make rules for the convenient "
              "transaction of business, and the Transaction of Business Rules 1961 are made under "
              "that power."),
            TC([P("cyan", "Allocation of Business Rules 1961",
                  "List the ministries and departments and allot every subject of government to "
                  "one of them. The owning department leads on any policy in its subject.")],
               [P("indigo", "Transaction of Business Rules 1961",
                  "Set how business is done: who must be consulted, which cases go to the "
                  "Cabinet or its committees, and which the minister may decide alone.")]),
            H("amber", "Reading these two sets of rules tells you which officer actually holds "
              "the file on your issue, which is where any serious engagement with government "
              "begins."),
        ]),

        S("Ministries", "The ministry that owns the file", [
            B("Most policy starts as a note in the owning department. Under rule 3 of the "
              "Transaction of Business Rules, business allotted to a department is disposed of by "
              "or under the direction of its minister, subject to the consultation rules. Rule "
              "4(2) requires the previous concurrence of the Ministry of Finance for any order "
              "with a financial bearing, and rule 4(3) requires consultation with the Ministry of "
              "Law on proposals for legislation and on rules of a general character."),
            TC([BL(["Subject ministry drafts the proposal",
                    "Other affected departments comment (rule 4(1))",
                    "Finance examines cost; Law examines legal form"])],
               [BL(["Revised note goes to the minister",
                    "Cabinet or a Cabinet committee decides where the rules require it",
                    "Decision is communicated and the department acts"])]),
            H("cyan", "Source: " + TOB + ". In practice the Finance Ministry's concurrence is "
              "where many ambitious proposals are scaled down, so a cost estimate prepared early "
              "makes a proposal more likely to survive."),
        ]),

        S("Cabinet", "The Cabinet and its committees", [
            B("Rule 6 of the Transaction of Business Rules provides for Standing Committees of the "
              "Cabinet, with members chosen by the Prime Minister, and allows ad hoc committees "
              "including Groups of Ministers to investigate and, if authorised, decide. Any "
              "decision of a committee may be reviewed by the Cabinet. The Second Schedule lists "
              "cases that must go before the full Cabinet."),
            T(["Selected Second Schedule cases (must go to Cabinet)", "Why it matters for policy"],
              [["Cases involving legislation, including Ordinances", "Every government bill is a Cabinet decision first"],
               ["Proposals to appoint public commissions or committees of inquiry, and their reports",
                "Commissions are a common way to defer or prepare reform"],
               ["Negotiations with other countries on treaties and important agreements",
                "International commitments that later need domestic law"],
               ["Proclamations of emergency under Articles 352 to 360", "Exceptional powers"]]),
            H("indigo", "Rule 6(7): no case that concerns more than one department goes to a "
              "Cabinet committee until all the departments concerned have been consulted."),
        ]),

        S("NITI Aayog", "From the Planning Commission to NITI Aayog", [
            B("On 1 January 2015 the Union Cabinet replaced the Planning Commission, set up by a "
              "Cabinet resolution on 15 March 1950, with the National Institution for "
              "Transforming India (NITI Aayog). The government's press note described it as a "
              "\"think tank\" of the government that would give the Union and the states "
              "strategic and technical advice. The Prime Minister chairs it, and its Governing "
              "Council includes the Chief Ministers of all states."),
            TC([P("amber", "Planning Commission, 1950&ndash;2014",
                  "Drew up Five-Year Plans for the economy. It was created by an executive "
                  "resolution of 15 March 1950, with no statute behind it.")],
               [P("green", "NITI Aayog, from 2015",
                  "An advisory body, also created by Cabinet resolution. Works through indices, "
                  "strategy papers and state engagement. Houses DMEO as an attached office.")]),
            H("cyan", "Source: PIB, Cabinet press note and resolution, 1 January 2015 (the resolution "
              "names a Governing Council of the Chief Ministers of all states and Lieutenant "
              "Governors of union territories). Because both bodies rest on resolutions, a later government can change "
              "them without amending any law."),
        ]),

        S("Consultation", "The Pre-Legislative Consultation Policy, 2014", [
            B("In 2014 the Union government adopted a policy on consultation before legislation. "
              "According to PRS Legislative Research, it applies to every ministry before a "
              "legislative proposal, including subordinate legislation, goes to the Cabinet. A "
              "draft bill is to be published for public comment for 30 days, with a justification, "
              "its financial implications, an estimated impact assessment and an explanatory "
              "note. A summary of comments is to be published on the ministry's website."),
            ST([C("30 days", "public comment window for draft bills under the policy", "cyan", PRS14),
                C("10 days", "given for comments on draft amendments to the MTP Act 1971 (2014)", "red", PRS14)],
               cols=2),
            TC([B("<strong>What it allows:</strong> any organisation can comment on a draft before "
                  "the Cabinet approves it, when change is cheapest.", sm=True)],
               [B("<strong>Its weakness:</strong> it is an executive policy with no statute behind "
                  "it, and PRS found it had not been applied uniformly.", sm=True)]),
        ]),

        S("Parliament", "How a bill becomes law in Parliament", [
            B("After Cabinet approval a bill is introduced in either House, except Money Bills and "
              "other financial bills, which start in the Lok Sabha. It can be referred to a "
              "Department-related Standing Committee for detailed examination, though referral is "
              "not mandatory. It is then debated and voted clause by clause, passed by both "
              "Houses, and sent for the President's assent."),
            FL(["Introduction (first reading)",
                "Committee examination, if referred",
                "Consideration and clause-by-clause voting",
                "Passage in the other House",
                "Presidential assent"]),
            TC([B("<strong>Where to engage:</strong> committees invite written submissions and "
                  "sometimes oral evidence from experts and organisations.", sm=True)],
               [B("<strong>Watch the time:</strong> in the 15th Lok Sabha, 35% of bills passed "
                  "were debated for an hour or less (PRS, 2014).", sm=True)]),
            H("cyan", "Source: " + PRS14 + "."),
        ]),

        S("Committees", "Fewer bills now go to committees", [
            B("Committees are where most detailed scrutiny of bills happens. The share of bills "
              "referred to them has fallen sharply. PRS Legislative Research reports that 16% of "
              "bills in the 17th Lok Sabha (2019&ndash;2024) were referred, lower than in each of "
              "the three previous Lok Sabhas."),
            {"t": "chart", "canvas": "drscChart",
             "title": "Share of bills referred to parliamentary committees, by Lok Sabha (%)",
             "source": PRS17,
             "type": "bar",
             "data": {"labels": ["14th (2004&ndash;09)", "15th (2009&ndash;14)", "16th (2014&ndash;19)", "17th (2019&ndash;24)"],
                      "datasets": [{"label": "% of bills referred",
                                    "data": [60, 71, 28, 16],
                                    "backgroundColor": ["#0369A1", "#0369A1", "#B45309", "#B91C1C"]}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% referred'} } } }"}},
            H("amber", "Committees still meet often: about 1,700 meetings in the 17th Lok Sabha, "
              "and the Joint Committee on the Personal Data Protection Bill 2019 met 78 times "
              "(PRS). Unreferred bills miss that scrutiny."),
        ]),

        S("States", "The Seventh Schedule: who may legislate on what", [
            B("Article 246 and the Seventh Schedule divide legislative power between the Union and "
              "the states into three lists. Much of social policy sits with the states or in the "
              "Concurrent List, which is why national schemes depend on state governments. The "
              "42nd Amendment of 1976 moved education from the State List to the Concurrent List."),
            T(["Subject", "List and entry", "What it means in practice"],
              [["Police", "State List, entry 2", "Law and order is a state responsibility"],
               ["Public health and sanitation; hospitals", "State List, entry 6",
                "States run most public health services"],
               ["Agriculture", "State List, entry 14", "Farm policy needs state action"],
               ["Education", "Concurrent List, entry 25 (since 1976)", "Both Union and states legislate"],
               ["Social security and social insurance; employment and unemployment",
                "Concurrent List, entry 23", "Basis for shared employment and welfare law"]]),
            H("cyan", "Source: Constitution of India, Seventh Schedule (Legislative Department text as "
              "on 1 May 2024); entry 25 of List III was substituted by the Constitution (Forty-second "
              "Amendment) Act 1976, with effect from 3 January 1977."),
        ]),

        S("Fiscal federalism", "Centrally sponsored schemes and who pays", [
            B("Many national programmes are <strong>Centrally Sponsored Schemes</strong>: the Union "
              "designs and part-funds them, and states implement and share the cost. The funding "
              "formula is a policy choice with large effects. Under the VB-G RAM G Act 2025, s22, "
              "the sharing pattern is 90:10 for the North Eastern States, the Himalayan States and "
              "Jammu and Kashmir, 60:40 for all other states and union territories with a "
              "legislature, and fully Union-funded for union territories without one."),
            ST([C("60:40", "Union : State share, most states (s22(2))", "cyan", VBG),
                C("90:10", "North Eastern and Himalayan States, J&amp;K (s22(2))", "green", VBG),
                C("100%", "Union share for UTs without a legislature (s22(3))", "indigo", VBG)],
               cols=3),
            TC([B("<strong>Normative allocation:</strong> the Union fixes each state's allocation "
                  "on objective parameters it prescribes (s4(5), s22(4)).", sm=True)],
               [B("<strong>Above the allocation:</strong> any spending in excess is borne by the "
                  "state (s4(6), s22(5)).", sm=True)]),
        ]),

        S("Courts", "Courts and public interest litigation", [
            B("Indian courts are policy actors. Article 32 lets a person approach the Supreme Court "
              "for enforcement of fundamental rights, and Article 226 gives High Courts similar "
              "writ powers. After the Emergency, judges including P.N. Bhagwati and V.R. Krishna "
              "Iyer relaxed the rule that only an injured person may sue. In <em>Hussainara Khatoon "
              "v State of Bihar</em> (1979) the Court took up the cases of undertrial prisoners, and "
              "<em>S.P. Gupta v Union of India</em> (AIR 1982 SC 149) widened standing for public "
              "interest petitions."),
            TC([P("green", "What PILs have done",
                  "Forced action on undertrial detention, cooked school meals and food rights; "
                  "created continuing oversight through commissioners and repeated orders.")],
               [P("amber", "The criticism",
                  "Courts lack budgets, staff and field knowledge; orders can be hard to enforce "
                  "(the 2003 midday meal order); critics call some directions judicial "
                  "overreach.")]),
            H("indigo", "Courts also review policy. In <em>Justice K.S. Puttaswamy (Retd.) v Union of "
              "India</em> (26 September 2018) the Supreme Court upheld section 7 of the Aadhaar Act "
              "2016 and struck down the part of section 57 that let companies and individuals seek "
              "authentication."),
        ]),

        # ===================== SECTION 06 =====================
        DIV("06", "Six", "Implementation and state capacity"),

        S("The gap", "Pressman and Wildavsky: the implementation gap", [
            B("Jeffrey Pressman and Aaron Wildavsky's <em>Implementation</em> (1973) carried the "
              "subtitle <em>How Great Expectations in Washington Are Dashed in Oakland</em>: a "
              "federal promise made in the capital and disappointed in one city, as "
              "the title itself announces. One way to see the problem is arithmetic: a programme that needs many separate agencies and decisions to agree has "
              "many chances to stall, even when each step is likely to go well."),
            TC([P("indigo", "Top-down view",
                  "Start from the law's objectives and ask why officials departed from them. "
                  "Remedies: clearer goals, fewer veto points, more control and monitoring.")],
               [P("green", "Bottom-up view",
                  "Start from the frontline and ask how officials and citizens actually behave. "
                  "Remedies: discretion, local adaptation, feedback from those who deliver.")]),
            H("amber", "Illustrative arithmetic: if a scheme needs ten separate clearances and each "
              "has a 90% chance of coming through on time, the chance all ten do is about 35%."),
        ]),

        S("Street level", "Lipsky: frontline workers make policy", [
            B("Michael Lipsky's <em>Street-Level Bureaucracy</em> (1980) studied teachers, police "
              "officers, social workers and others who deal directly with citizens and have "
              "discretion over them. They work with too few resources, rising demand, vague goals "
              "and clients who cannot go elsewhere. They cope by building routines, rationing "
              "their time and simplifying how they see their clients."),
            Q("The decisions of street-level bureaucrats, the routines they establish, and the "
              "devices they invent to cope with uncertainties and work pressures, effectively "
              "become the public policies they carry out.",
              "Michael Lipsky, Street-Level Bureaucracy (1980), p. xiii, as quoted in Gilson (2015)"),
            TC([B("<strong>South Asian frontline:</strong> anganwadi workers, ASHAs, school "
                  "teachers, panchayat secretaries, ration dealers, police constables.", sm=True)],
               [B("<strong>Implication:</strong> to know what a policy is, watch what these "
                  "officials do, as well as what the law says.", sm=True)]),
        ]),

        S("Coping", "How coping reshapes a policy", [
            B("Lucy Gilson's review of Lipsky (Oxford Handbook of Classics of Public Policy, 2015) "
              "notes that coping routines can control clients, ration services by imposing time or "
              "money costs, and sort clients into more and less deserving. Lipsky himself said "
              "coping may \"widen the gap between policy as written and policy as performed\". "
              "The examples below are invented to show the mechanisms; they describe no real "
              "office."),
            T(["Coping routine (Illustrative)", "How it looks on the ground", "Effect on the policy"],
              [["Rationing by queue", "Applications accepted only one morning a week",
                "Workers with daily wages cannot apply"],
               ["Creaming", "Easiest cases processed first to meet a monthly target",
                "Hardest-to-reach families wait longest"],
               ["Referral", "Difficult cases sent to the block office", "Citizen must travel and may give up"],
               ["Paperwork as gatekeeping", "Extra documents requested beyond the rules",
                "Entitlement turns into a privilege"]]),
            H("cyan", "Design response: reduce the discretion that harms, resource the discretion "
              "that helps, and measure who is turned away as well as who is served."),
        ]),

        S("Flailing state", "Pritchett: is India a flailing state?", [
            B("In a 2009 Harvard Kennedy School working paper, Lant Pritchett argued that India's "
              "capable central institutions were poorly connected to delivery on the ground. He "
              "pointed to examples from health, education and routine tasks such as issuing "
              "driving licences, where state agents routinely did not do the tasks assigned to "
              "them, creating a gap between rules on paper and practice."),
            Q("The India state is \"flailing\": its very capable head is not longer reliably "
              "connected to the arms and legs of implementation.",
              "Lant Pritchett, Is India a Flailing State?, HKS Working Paper RWP09-013, 2009 (abstract, verbatim)"),
            TC([B("<strong>De jure:</strong> what the rules say should happen, in the Act, the "
                  "guidelines and the office order.", sm=True)],
               [B("<strong>De facto:</strong> what actually happens in the clinic, the school and "
                  "the licence office.", sm=True)]),
            H("amber", "A practitioner's version of the test: for any scheme, collect one rule and "
              "one observation of practice, and compare them."),
        ]),

        S("Fail and succeed", "Kapur: why the Indian state both fails and succeeds", [
            B("Devesh Kapur's article in the <em>Journal of Economic Perspectives</em> (2020, 34(1): "
              "31&ndash;54) offers a more mixed picture. The Indian state, he argues, performs well "
              "on complex tasks run on a massive scale and on macroeconomic outcomes, and badly "
              "on everyday local services. He also disputes the claim that the state is bloated."),
            T(["Delivers better when...", "Delivers worse when..."],
              [["Outcomes are macroeconomic", "Outcomes are microeconomic"],
               ["Delivery is episodic, with an in-built exit", "Delivery and accountability are daily"],
               ["Little depends on local state capacity", "Local capacity carries the load"],
               ["Social hierarchy and status matter less", "Norms of hierarchy remain strong"]]),
            H("indigo", "Kapur's three reasons: under-resourced local governments, the long-term "
              "effects of India's early (\"precocious\") democracy, and persistent social "
              "cleavage. He also finds state capacity improving at the micro level. Source: "
              "article abstract, AEA."),
        ]),

        S("Overload", "Bureaucratic overload in rural development", [
            B("Aditya Dasgupta and Devesh Kapur (<em>American Political Science Review</em> "
              "114(4), 2020) surveyed local rural development officials across India, including "
              "time-use diaries. They describe <strong>bureaucratic overload</strong>: local "
              "bureaucrats are often heavily under-resourced relative to their responsibilities. "
              "Officials with fewer resources were worse at implementing rural development "
              "programmes, plausibly because they had too little time for managerial tasks."),
            TC([P("red", "The usual explanation",
                  "Poor implementation is blamed on rent-seeking and capture, so the remedy is "
                  "more control and vigilance.")],
               [P("green", "The overload explanation",
                  "Officials are spread too thin, so the remedy includes more staff, less "
                  "paperwork and clearer priorities.")]),
            H("amber", "They also find fewer resources go to administrative units where political "
              "responsibility for implementation is less clear, which links capacity to "
              "electoral incentives."),
        ]),

        S("Absence", "Measuring the gap: teacher and health worker absence", [
            B("Unannounced visits are a direct way to measure implementation. Chaudhury, Hammer, "
              "Kremer, Muralidharan and Rogers (<em>Journal of Economic Perspectives</em>, 2006) "
              "visited schools and clinics in six countries including Bangladesh and India. A "
              "later nationally representative Indian panel by Muralidharan, Das, Holla and "
              "Mohpal (<em>Journal of Public Economics</em>, 2017) covered schools in 1,297 "
              "villages."),
            ST([C("25%", "government primary teachers absent in India; about half teaching when visited",
                  "red", "Chaudhury et al., JEP 2006"),
                C("23.6%", "teachers absent during unannounced visits in the later Indian panel",
                  "amber", "Muralidharan et al., JPubE 2017"),
                C("$1.5 bn", "estimated annual salary cost of unauthorised teacher absence",
                  "indigo", "Muralidharan et al., JPubE 2017")], cols=3),
            H("green", "The 2017 paper estimates that more frequent monitoring could be over ten "
              "times more cost-effective at raising the effective student-teacher ratio than "
              "hiring more teachers."),
        ]),

        S("Design for delivery", "Designing a policy that can be implemented", [
            B("The lesson of this section is to treat implementation as part of design. A "
              "policy that assumes perfect officials, perfect data and perfect payment systems "
              "will fail in predictable ways. The checklist below can be applied to any draft "
              "scheme before it is adopted."),
            TC([BL(["Count the steps and approvals between the money and the citizen.",
                    "Name the frontline worker who delivers it, and check their workload.",
                    "State what discretion they have, and how it is supervised.",
                    "Budget for staff and training as well as benefits."])],
               [BL(["Plan the grievance route, with a time limit for a reply.",
                    "Pilot in a hard district before scaling.",
                    "Measure exclusion as well as leakage.",
                    "Publish the data that would show the scheme failing."])]),
            H("cyan", "Read " + L("governance-accountability.html", "Governance &amp; "
              "Accountability 101") + " for the accountability tools, such as social audit and "
              "RTI, that support delivery."),
        ]),

        # ===================== SECTION 07 =====================
        DIV("07", "Seven", "Evidence in policy"),

        S("What counts", "What counts as evidence for policy", [
            B("Evidence-based policy means using the best available information about what a "
              "policy will do. In practice policy makers draw on several kinds of evidence, each "
              "answering a different question. A randomised trial can say whether a programme "
              "changed an outcome in one place; administrative data can say how many people it "
              "reached; qualitative work can say why it failed for some of them."),
            T(["Kind of evidence", "Answers best", "Watch for"],
              [["Randomised and quasi-experimental evaluations", "Did the policy cause the change?",
                "Whether results travel to other places and scales"],
               ["Administrative data (MIS, payment records)", "Who was reached, when, at what cost?",
                "Records that reward reporting over reality"],
               ["Surveys (NSS, NFHS, PLFS)", "How common is the problem, and for whom?",
                "Timing; survey changes between rounds"],
               ["Qualitative and participatory research", "Why and how did it work or fail?",
                "Generalising from a few sites"],
               ["Audits and social audits", "Was money spent as claimed?", "Follow-up on findings"]]),
            H("indigo", "The best evidence for a decision is the one that answers the decision's "
              "question. See " + L("impact-eval.html", "Impact Evaluation 101") + "."),
        ]),

        S("Trials at scale", "Biometric smartcards in Andhra Pradesh", [
            B("Muralidharan, Niehaus and Sukhtankar (<em>American Economic Review</em> 106(10), "
              "2016) evaluated biometrically authenticated payments (\"Smartcards\") for the "
              "employment guarantee and social security pensions in Andhra Pradesh. The rollout "
              "was randomised across 157 subdistricts covering 19 million people, so the "
              "experiment was built into the order of an actual government rollout."),
            TC([BL(["NREGS payments became faster, more predictable and less corrupt.",
                    "Programme access did not fall.",
                    "Leakage fell in both NREGS and pensions."])],
               [BL(["Time saved by beneficiaries alone matched the cost of the intervention.",
                    "Beneficiaries strongly preferred the new system.",
                    "Implementation was incomplete, and still worked."])]),
            H("green", "Lesson for policy: a large experiment can be run inside a real government "
              "rollout by randomising the order in which areas receive a reform."),
        ]),

        S("Financial reform", "Just-in-time funds for the workfare programme", [
            B("Banerjee, Duflo, Imbert, Mathew and Pande (<em>AEJ: Applied Economics</em> 12(4), "
              "2020) studied a reform to how funds flowed in India's workfare programme. Advance "
              "payments to local officials were replaced by \"just-in-time\" payments triggered by "
              "e-invoicing, which made misreporting easier to detect. The study used a large "
              "field experiment and then followed the nationwide scale-up."),
            ST([C("&minus;24%", "programme expenditure in the experiment, with employment slightly up",
                  "green", "Banerjee et al., AEJ Applied 2020"),
                C("&minus;10%", "personal wealth of programme officials", "indigo",
                  "Banerjee et al., AEJ Applied 2020"),
                C("&minus;19%", "persistent fall in expenditure after nationwide scale-up", "cyan",
                  "Banerjee et al., AEJ Applied 2020")], cols=3),
            H("amber", "The same study found that payment delays increased. Good evaluations "
              "report the costs of a reform alongside its gains."),
        ]),

        S("A caution", "When a reform excludes eligible people", [
            B("Evidence can also show harm. Muralidharan, Niehaus and Sukhtankar (NBER Working "
              "Paper 26744, 2020, revised 2021) evaluated the introduction of Aadhaar-based "
              "biometric authentication to collect benefits in the Public Distribution System in "
              "Jharkhand, using randomised and natural experiments. Corruption fell, but with "
              "substantial costs to legitimate beneficiaries."),
            ST([C("1.5&ndash;2 million", "legitimate beneficiaries lost access at some point during the reforms",
                  "red", "Muralidharan, Niehaus and Sukhtankar, NBER WP 26744")], cols=1),
            TC([B("<strong>The authors' reading:</strong> adverse effects appear to have been driven "
                  "mainly by how the transition was managed.", sm=True)],
               [B("<strong>The policy lesson:</strong> the impact of a new technology depends on "
                  "the protocols governing its use, and rapid reforms carry risk.", sm=True)]),
            H("indigo", "Put this next to the Andhra Pradesh result: the same broad technology "
              "helped in one design and harmed in another."),
        ]),

        S("Administrative data", "Reading official claims about savings", [
            B("Governments often report results from their own administrative data. On 21 April "
              "2025 the Press Information Bureau (Ministry of Finance) publicised an assessment by "
              "the BlueKraft Digital Foundation reporting cumulative savings of Rs 3.48 lakh crore "
              "from direct benefit transfer (DBT), with subsidies falling from 16% to 9% of total "
              "expenditure."),
            T(["Claim in the PIB note", "Question an analyst should ask"],
              [["Rs 3.48 lakh crore cumulative savings", "How is a \"saving\" defined, and against what counterfactual?"],
               ["Rs 1.85 lakh crore of it from food subsidies (PDS)",
                "Were deleted ration cards ineligible, duplicate, or eligible people excluded?"],
               ["Rs 22,106 crore saved by deleting 2.1 crore PM-KISAN beneficiaries",
                "Were deletions verified, and could people appeal?"],
               ["Beneficiary coverage up from 11 crore to 176 crore", "Are these people, accounts or transactions?"]]),
            H("amber", "Source: PIB, India's DBT: Boosting Welfare Efficiency, 21 April 2025. Read "
              "it alongside the Jharkhand evidence on the previous slide."),
        ]),

        S("DMEO", "DMEO and government evaluation in India", [
            B("DMEO describes its mandate as monitoring and evaluating the implementation of "
              "schemes, programmes and initiatives of the Government of India, to strengthen "
              "delivery, and building the monitoring and evaluation system in the country. Its "
              "website lists an Output-Outcome Monitoring Framework (OOMF) and a Data Governance "
              "Quality Index (DGQI) among its tools, and it commissions sector evaluations through "
              "open tenders."),
            TC([P("cyan", "Output-Outcome Monitoring Framework",
                  "Documents prepared before the Union Budget that \"map financial outlays of "
                  "schemes to intended outputs and outcome targets\" for central schemes.")],
               [P("indigo", "Data Governance Quality Index",
                  "Reviews the \"data preparedness\" of ministries' data and MIS systems on six "
                  "themes, from data generation and quality to data security and staff capacity.")]),
            H("amber", "Practical use: before designing an evaluation of a central scheme, check "
              "whether DMEO has already evaluated it, and use its indicators so your findings can "
              "be compared. Sources: DMEO website and its OOMF and DGQI pages, October 2026."),
        ]),

        S("Data and law", "Using personal data for policy research", [
            B("Policy research increasingly uses administrative records that contain personal "
              "data. In India the Digital Personal Data Protection Act 2023 and its 2025 Rules "
              "impose their duties from 13 May 2027. From that date section 17(2)(b) exempts processing \"necessary for research, archiving "
              "or statistical purposes\" if the data is not used to take a decision specific to a "
              "Data Principal and the processing follows prescribed standards."),
            TC([BL(["Confirm your purpose fits research or statistics.",
                    "Do not use the data to decide about any individual.",
                    "Follow the prescribed standards for such processing."])],
               [BL(["Minimise: collect only the fields you need.",
                    "Separate identifiers from analysis files.",
                    "Keep ethics approval and consent records where they apply."])]),
            H("cyan", "Source: DPDP Act 2023, s17(2)(b), Gazette of India, 11 August 2023; commencement "
              "under G.S.R. 843(E), 13 November 2025. See "
              + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101") + "."),
        ]),

        S("From evidence to decision", "Why good evidence often does not change policy", [
            B("A strong evaluation is one input into a political decision. It competes with "
              "budgets, promises, interests and timing. Kingdon's framework helps here: evidence "
              "sits in the policy stream, and it waits for a problem to be recognised and the "
              "politics to allow action. Researchers who want their work used plan for that "
              "wait."),
            FL(["Ask a question the decision maker already has",
                "Agree in advance on what result would change the decision",
                "Share early findings privately with implementers",
                "Publish a short brief at the moment of decision",
                "Stay available as the policy is revised"]),
            TC([B("<strong>Common failure:</strong> the report arrives after the budget is set, "
                  "answering a question nobody is asking any more.", sm=True)],
               [B("<strong>Common fix:</strong> tie evaluation to a fixed decision point, as with "
                  "evaluations before a scheme's renewal.", sm=True)]),
        ]),

        # ===================== SECTION 08 =====================
        DIV("08", "Eight", "South Asian cases"),

        S("Case 1a", "The rural employment guarantee as enacted in 2005", [
            B("The " + NREGA + " made rural work a legal entitlement. Section 3 required each state to provide every rural household whose adult "
              "members volunteered for unskilled manual work \"not less than one hundred days of "
              "such work in a financial year\". Wages were to be paid weekly, or no later than a "
              "fortnight after the work was done. An applicant not given work within fifteen days "
              "was entitled to an unemployment allowance (s7)."),
            TC([P("cyan", "Who paid (s22)",
                  "The Union met the full cost of wages for unskilled manual work and up to "
                  "three-fourths of the material cost, including skilled and semi-skilled "
                  "wages. States paid the unemployment allowance and one-fourth of material "
                  "cost.")],
               [P("indigo", "Why the design mattered",
                  "Because the Union paid all unskilled wages, the guarantee was demand-driven "
                  "in law: the more work people demanded, the more the Union was obliged to "
                  "fund.")]),
            H("amber", "Later renamed the Mahatma Gandhi NREGA, the Act was repealed from 1 "
              "July 2026. Sources: NREGA 2005 (PRS copy), ss 3, 7, 22."),
        ]),

        S("Case 1b", "The VB-G RAM G Act 2025: what the new law says", [
            B("The Viksit Bharat Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, Act No. 36 "
              "of 2025, dated 20 December 2025, replaced it. The Ministry of Rural Development "
              "notified on 11 May 2026 that the Act would come into force on 1 July 2026, with "
              "MGNREGA repealed from the same date under section 37. The core guarantee rises to "
              "\"not less than one hundred and twenty-five days\" a year (s5)."),
            TC([BL(["<strong>s4:</strong> works must originate in Viksit Gram Panchayat Plans, "
                    "integrated with the PM Gati Shakti National Master Plan.",
                    "<strong>s4(2):</strong> four focus areas: water security, core rural "
                    "infrastructure, livelihood infrastructure, extreme-weather mitigation."])],
               [BL(["<strong>s6:</strong> states notify in advance a period aggregating to sixty days "
                    "a year, covering peak sowing and harvest seasons, when no works run.",
                    "<strong>s22:</strong> a Centrally Sponsored Scheme with a 60:40 or 90:10 "
                    "funding split and a Union-set normative allocation."])]),
            H("cyan", "Sources: " + VBG + " (India Code, with S.O. 2382(E) of 11 May 2026); SCC Online, "
              "12 May 2026. As of October 2026 the Act has been in force for three months."),
        ]),

        S("Case 1c", "Old and new guarantees side by side", [
            B("Comparing the two Acts section by section shows that the change is about more than "
              "the number of days. The funding rules, the planning rules and the seasonal pause "
              "change who decides how much work is available, and when. The table uses only the "
              "text of the two statutes."),
            T(["Feature", "NREGA 2005", "VB-G RAM G Act 2025"],
              [["Days guaranteed per household per year", "At least 100 (s3)", "At least 125 (s5)"],
               ["Unskilled wage cost", "Union pays in full (s22(1)(a))",
                "Shared 60:40 or 90:10 within a normative allocation (s22)"],
               ["Spending above allocation", "No state allocation cap in the Act",
                "Borne by the state (s4(6), s22(5))"],
               ["Planning of works", "Gram Panchayat works under the Scheme",
                "Viksit Gram Panchayat Plans linked to PM Gati Shakti (s4)"],
               ["Seasonal pause", "None in the Act", "60 days a year in aggregate, notified by states (s6)"],
               ["Unemployment allowance", "If no work within 15 days; paid by state (s7, s22(2))",
                "If no work within 15 days; borne by state (s11, s22(8))"]]),
            H("amber", "Read the statutes themselves before relying on any summary, including this "
              "one; rules and the state Schemes will add detail."),
        ]),

        S("Case 1d", "Reading the shift with this course's frameworks", [
            B("The frameworks from earlier sections suggest what to watch as the new Act is "
              "implemented. These are questions for monitoring, and none of them is a finding: as "
              "of October 2026 there is no published outcome data for a full year under the new "
              "law."),
            TC([P("indigo", "Fiscal federalism (Section 5)",
                  "With a state share of wages and a normative allocation, does work offered "
                  "track demand, or the allocation? Do poorer states with a 40% share open fewer "
                  "works?")],
               [P("amber", "Implementation (Section 6)",
                  "Do the six-month Scheme deadline, panchayat planning and the seasonal pause "
                  "change when and where work is available? Who records demand for work?")]),
            TC([P("green", "Evidence (Section 7)",
                  "Which administrative indicators will be published, and can independent "
                  "researchers access them under the DPDP Act's research exemption?")],
               [P("red", "Stakeholders (Section 9)",
                  "Workers, panchayats, state finance departments and contractors each gain or "
                  "lose differently from the change.")]),
        ]),

        S("Case 2a", "Aadhaar and direct benefit transfer: the legal basis", [
            B("India's move to direct benefit transfer rests on the Aadhaar (Targeted Delivery of "
              "Financial and Other Subsidies, Benefits and Services) Act 2016, Act 18 of 2016, "
              "which received the President's assent on 25 March 2016. Section 7 lets the Union or "
              "a state require proof of an Aadhaar number, or authentication, as a condition for "
              "a subsidy, benefit or service paid for from the Consolidated Fund."),
            TC([P("green", "Upheld",
                  "In Puttaswamy (26 September 2018) the Supreme Court upheld section 7. The lead "
                  "judgment described welfare delivery to the marginalised as an aspect of social "
                  "justice, an obligation of the State under Part IV.")],
               [P("red", "Struck down",
                  "The portion of section 57 that let a body corporate or an individual seek "
                  "Aadhaar authentication was held unconstitutional. The Court also struck down "
                  "section 33(2) in its form at the time.")]),
            H("amber", "The majority held the Act was rightly passed as a Money Bill; Justice "
              "Chandrachud's dissent called its passage as one \"a fraud on the Constitution\". Source: Justice K.S. Puttaswamy (Retd.) v Union of "
              "India, judgment of 26 September 2018 (Indian Kanoon text)."),
        ]),

        S("Case 2b", "DBT: what the evidence shows so far", [
            B("The evidence on biometric and digital delivery in India points in more than one "
              "direction. The pattern across studies is that the technology's effect depends on "
              "how the reform is designed and rolled out, and on what happens to people for whom "
              "the system fails."),
            T(["Study or claim", "Setting", "Finding"],
              [["Muralidharan, Niehaus and Sukhtankar (AER 2016)", "Andhra Pradesh, NREGS and pensions",
                "Faster, less corrupt payments; access did not fall"],
               ["Banerjee et al. (AEJ Applied 2020)", "Workfare fund flows, national scale-up",
                "Expenditure down 19&ndash;24%; payment delays up"],
               ["Muralidharan, Niehaus and Sukhtankar (NBER WP 26744)", "Jharkhand PDS",
                "Corruption fell; 1.5&ndash;2 million eligible people lost access at some point"],
               ["PIB / BlueKraft assessment (April 2025)", "All DBT schemes",
                "Rs 3.48 lakh crore cumulative savings claimed"]]),
            H("indigo", "Practitioner rule: track exclusion errors with the same care as leakage. "
              "A saving from removing ineligible people and a saving from excluding eligible "
              "people look identical in a budget."),
        ]),

        S("Case 3", "Pakistan's BISP: from legislators' forms to a poverty scorecard", [
            B("The Benazir Income Support Programme was launched in late 2008 to cushion poor "
              "households against the food, fuel and financial crisis, with food inflation close "
              "to 25%. An ODI study by Shanza Khan and Sara Qutub (November 2010) records that a "
              "plan to identify beneficiaries from the national identity database was dropped "
              "during design. Instead, 8,000 forms were given to each member of the federal "
              "legislature to distribute to families they considered eligible. A poverty "
              "scorecard based on a proxy means test then replaced selection by legislators."),
            TC([P("amber", "Why targeting changed",
                  "Only families who received a legislator's form could apply, and the design "
                  "raised concerns over targeting and leakage. The government sought World Bank "
                  "help, and the Bank proposed the scorecard. Payments go to women in eligible "
                  "households.")],
               [P("green", "Scale today",
                  "Pakistan's Economic Survey 2024-25 (Table 16.4) puts BISP disbursements at "
                  "Rs 385.64 billion to about 9.87 million beneficiaries in July 2024 to 31 March "
                  "2025.")]),
            H("cyan", "The case shows targeting as a political choice: who identifies the poor "
              "decides who controls the programme."),
        ]),

        S("Case 4", "Sri Lanka's Aswesuma: retargeting in a crisis", [
            B("In 2023 Sri Lanka replaced its long-running Samurdhi benefit with the Aswesuma "
              "welfare benefit scheme. The Centre for Poverty Analysis (CEPA) published a rapid "
              "appraisal by Hemesiri Kotagama on 27 June 2023. It notes that the replacement was "
              "a condition in the government's 2023 loan agreement with the International "
              "Monetary Fund, and that households are scored on six dimensions: education, health, "
              "economic level, assets, housing condition and family demography."),
            ST([C("27% &rarr; 12%", "share of families receiving benefits in Rookwood Estate, Nuwara Eliya District, Samurdhi to Aswesuma",
                  "red", "Kotagama, CEPA, 27 June 2023")], cols=1),
            TC([B("<strong>Transparency:</strong> the appraisal says the dimension weights and the "
                  "cut-off score were not public, so households could not check their own "
                  "eligibility.", sm=True)],
               [B("<strong>Lesson:</strong> a formula can be more objective than discretion and "
                  "still exclude, if it is opaque and the appeal route is weak.", sm=True)]),
        ]),

        S("Across the cases", "Four cases, five lessons", [
            B("Set side by side, the four cases show recurring patterns in South Asian social "
              "policy. Each lesson below draws on evidence or documents cited earlier in this "
              "section, and each points to a design question you can ask of any new scheme."),
            T(["Lesson", "Seen in", "Design question"],
              [["Who pays shapes who provides", "NREGA 2005 and VB-G RAM G 2025 funding rules",
                "Does the funding rule reward meeting demand?"],
               ["Targeting is political", "BISP's move from legislators' forms to a scorecard",
                "Who identifies beneficiaries, and who checks them?"],
               ["Technology helps or harms by design", "Andhra Pradesh smartcards; Jharkhand PDS",
                "What happens when authentication fails?"],
               ["Opaque formulas exclude quietly", "Aswesuma appraisal", "Can a household see and appeal its score?"],
               ["Courts can set floors, states deliver", "Midday meal orders, 2001 and 2003",
                "Who has the budget and staff to comply?"]]),
            H("indigo", "Use these questions in Section 10's checklist when you appraise a policy "
              "proposal."),
        ]),

        # ===================== SECTION 09 =====================
        DIV("09", "Nine", "Stakeholders and political economy"),

        S("Why politics", "Why technically sound policies fail", [
            B("Many well-designed policies are never adopted, or are adopted and then hollowed out. "
              "The usual reason is political: the people who would lose from the change are "
              "organised and attentive, while those who would gain are scattered or unaware. "
              "Political economy analysis looks at interests, institutions and incentives to "
              "explain why a policy problem persists and what might shift it."),
            TC([P("indigo", "Technical question",
                  "What policy would produce the best outcome, judged by evidence on costs and "
                  "effects?")],
               [P("amber", "Political economy question",
                  "Who decides, who gains, who loses, what can each of them do about it, and "
                  "under what conditions would the decision change?")]),
            H("cyan", "BISP shows both questions at work: a scorecard was the technical answer to "
              "poor targeting, and replacing legislators' forms with it was a political choice "
              "about who controls benefits. See " + L("pol-economy.html", "Political Economy 101") + "."),
        ]),

        S("A framework", "Problem-driven political economy analysis", [
            B("The World Bank's good practice framework by Verena Fritz, Kai Kaiser and Brian Levy "
              "(2009) starts from a specific problem and works down in three steps. Its value for practitioners is focus: "
              "the analysis stops when it explains the problem you need to solve."),
            FL(["Define the problem, opportunity or vulnerability",
                "Examine the governance and institutional arrangements behind it",
                "Examine the political economy drivers: interests, incentives, power"]),
            TC([B("<strong>Example question at step 2:</strong> which rule, budget line or "
                  "office creates the bottleneck?", sm=True)],
               [B("<strong>Example question at step 3:</strong> who benefits from the bottleneck "
                  "staying in place?", sm=True)]),
            H("cyan", "Source: GSDRC topic guide on problem-driven political economy tools, "
              "summarising Fritz, Kaiser and Levy (2009)."),
        ]),

        S("Mapping", "Stakeholder mapping: power and interest", [
            B("A stakeholder map lists everyone who can affect or is affected by a policy, then "
              "places them by how much power they hold and how strongly the issue affects them. "
              "The grid tells you whom to keep closely engaged and whom to keep informed. The "
              "placements below are an invented example for a plastic ban, used to show the "
              "method."),
            TC([P("red", "High power, high interest (Illustrative)",
                  "Plastic manufacturers' associations; State Pollution Control Boards; "
                  "municipal commissioners. Engage closely and early.")],
               [P("amber", "High power, low interest (Illustrative)",
                  "State finance departments; the Union Ministry of MSME. Keep satisfied; show "
                  "how the policy affects their goals.")]),
            TC([P("green", "Low power, high interest (Illustrative)",
                  "Small vendors; waste pickers; residents near dumpsites. Organise and consult; "
                  "their knowledge of practice is valuable.")],
               [P("cyan", "Low power, low interest (Illustrative)",
                  "Most consumers. Inform; their behaviour still decides whether the ban "
                  "works.")]),
        ]),

        S("Winners and losers", "Concentrated costs, diffuse benefits", [
            B("A useful rule of thumb in political economy: when a policy's costs fall on a small, "
              "organised group and its benefits are spread thinly across many people, the small "
              "group usually wins. The Economic Survey 2014-15 found that the bottom half of "
              "households consumed only 25% of subsidised LPG, which helps explain why untargeted "
              "price subsidies persist: their better-off beneficiaries notice and resist any cut."),
            T(["Policy change (Illustrative)", "Concentrated side", "Diffuse side", "Likely politics"],
              [["Removing an untargeted fuel subsidy", "Current users who lose a visible benefit",
                "Taxpayers who save a little each", "Hard; often phased or paired with a transfer"],
               ["Banning a polluting product", "Manufacturers and their workers",
                "Residents with cleaner surroundings", "Needs time, alternatives and enforcement"],
               ["Biometric checks at ration shops", "Dealers who lose diversion income",
                "Taxpayers and eligible households", "Dealers resist; exclusion risk falls on the poor"]]),
            H("amber", "Designing a reform includes designing the coalition that will defend it."),
        ]),

        S("Federal politics", "Centre, states and the politics of shared schemes", [
            B("In a federation, a single policy has two sets of politicians with different "
              "incentives. Under a 60:40 funding split, a state government pays two rupees for "
              "every three the Union pays, and the political credit may go to whichever level "
              "voters notice. Dasgupta and Kapur (2020) found fewer resources go to administrative "
              "units where political responsibility for implementation is less clear."),
            TC([BL(["Union interests: national branding, fiscal control, uniform standards.",
                    "State interests: flexibility, local credit, protection from unfunded "
                    "mandates.",
                    "Local bodies: funds, staff and discretion over works."])],
               [BL(["Watch for: states slowing spending they must co-fund.",
                    "Watch for: allocation formulas that favour some states.",
                    "Watch for: blame-shifting when delivery fails."])]),
            H("indigo", "A cross-border comparison: after Pakistan's Eighteenth Amendment (2010) "
              "devolved education, health and social welfare functions, provinces took over "
              "policy in those fields while federal cash transfers such as BISP continued."),
        ]),

        S("Feasibility", "Four tests of feasibility", [
            B("Before recommending a policy, test it against four kinds of feasibility. A proposal "
              "that passes on evidence but fails one of these will need redesign or a longer "
              "plan. Write down your judgement for each test and the evidence for it, so others "
              "can challenge it."),
            T(["Test", "Question", "Evidence to gather"],
              [["Technical", "Will it work if implemented as designed?", "Evaluations, pilots, theory of change"],
               ["Political", "Can it be adopted and survive a change of government?",
                "Stakeholder map; positions of parties and states"],
               ["Administrative", "Can the existing state machinery deliver it?",
                "Staff numbers, workload, IT systems, absence data"],
               ["Financial", "Can it be paid for, now and in five years?",
                "Cost estimates; Finance Ministry view; fiscal rules"]]),
            H("cyan", "Administrative feasibility is the test most often skipped and the one "
              "Sections 6 and 8 show failing most often."),
        ]),

        S("Political timing", "Reading the window: when to push and when to prepare", [
            B("Kingdon's windows and Baumgartner and Jones's punctuations both say that timing "
              "matters as much as content. A practitioner cannot open a window, but can be ready "
              "when one opens. Preparation means having evidence, a costed proposal, a draft text "
              "and allies in place before the moment arrives."),
            TC([P("green", "Signals that a window may open",
                  "A new government or minister; a budget or Finance Commission cycle; a "
                  "court hearing; a crisis or scandal in the sector; a new survey round "
                  "showing a problem has worsened.")],
               [P("amber", "Work to do while waiting",
                  "Pilot and evaluate; build relations with the officers who hold the file; "
                  "brief committee members; prepare comments ready for a 30-day consultation "
                  "window.")]),
            H("indigo", "The 2014 consultation policy's 30-day window is short. Organisations that "
              "already know the issue can respond in time; others cannot."),
        ]),

        # ===================== SECTION 10 =====================
        DIV("10", "Ten", "A practitioner's toolkit"),

        S("Method", "Six steps of a policy analysis", [
            B("Policy analysis is the work of advising a decision maker on what to do. The six "
              "steps below are a common teaching sequence used in many forms by policy schools. "
              "They work for a one-page note to a district collector as well as a long report "
              "for a ministry; only the depth changes."),
            FL(["Define the problem with evidence of its size",
                "Set the criteria for judging options",
                "Build three or four realistic options",
                "Project each option's outcomes and costs",
                "Compare trade-offs openly",
                "Recommend, and say what would change your mind"]),
            TC([B("<strong>Include the status quo:</strong> always analyse \"no change\" as one "
                  "option, with its own costs.", sm=True)],
               [B("<strong>State criteria first:</strong> choosing criteria after seeing results "
                  "invites bias toward a favoured option.", sm=True)]),
        ]),

        S("Reading a policy", "Checklist: reading a policy before you act on it", [
            B("Most mistakes practitioners make about policy come from reading only one document. "
              "Before designing a programme around a scheme, or commenting on a draft, assemble "
              "the full set of documents and check each of these points."),
            TC([BL(["Find the parent Act and the section that creates the right or power.",
                    "Find the rules, the notified Scheme and the current guidelines.",
                    "Check commencement dates and any repeal or savings clause.",
                    "Read the budget line and the funding pattern."])],
               [BL(["Look for court orders or pending cases on the subject.",
                    "Check the parliamentary committee report, if the bill was referred.",
                    "Find the latest evaluation (DMEO, CAG, independent studies).",
                    "Talk to one frontline official about how it works in practice."])]),
            H("amber", "Worked check: for rural employment in October 2026 the parent Act is the "
              "VB-G RAM G Act 2025, MGNREGA is repealed with savings under s37, and each state's "
              "Scheme is due within six months of 1 July 2026 under s3."),
        ]),

        S("Worked example", "Options appraisal: exclusion at ration shops (Illustrative)", [
            B("A district team finds that some eligible families are turned away when fingerprint "
              "authentication fails at ration shops. The options and scores below are invented to "
              "show the method; real scores need local data. Scores run from 1 (poor) to 3 "
              "(good) on each criterion."),
            T(["Option (Illustrative)", "Reduces exclusion", "Controls leakage", "Cost", "Feasible now"],
              [["Status quo", "1", "3", "3", "3"],
               ["One-time password to registered mobile as fallback", "2", "2", "3", "2"],
               ["Nominated family member can authenticate", "2", "2", "3", "3"],
               ["Manual override logged by dealer, audited monthly", "3", "1", "2", "3"],
               ["Combine nominee and audited override", "3", "2", "2", "2"]]),
            H("indigo", "Adding the scores is not the decision. Make the weights explicit: a team "
              "that weights exclusion highest, given the Jharkhand evidence in Section 7, would "
              "favour the last option and plan the audit carefully."),
        ]),

        S("Engaging", "Where and how to engage the Indian policy process", [
            B("Different stages offer different openings, and each has its own form and timing. "
              "The table lists formal routes; informal relationships with the officers who hold "
              "the file matter at every stage."),
            T(["Stage", "Formal route", "What to submit"],
              [["Agenda setting", "Petitions, representations, media, research reports",
                "Evidence of the problem's size and who it hurts"],
               ["Formulation", "Comments on drafts under the 2014 consultation policy (30 days)",
                "Clause-specific comments with reasons and alternatives"],
               ["Legislative scrutiny", "Submissions to the parliamentary committee examining a bill",
                "Short memo; offer to give oral evidence"],
               ["Implementation", "RTI requests; grievance systems; social audits",
                "Specific facts and records"],
               ["Review", "Evaluation studies; PILs where rights are breached", "Evidence of outcomes"]]),
            H("cyan", "Information on schemes and records can be sought under the Right to "
              "Information Act 2005. See " + L("governance-accountability.html", "Governance &amp; "
              "Accountability 101") + " for the RTI process."),
        ]),

        S("Decision table", "Choosing what to monitor once a policy is adopted", [
            B("Adoption is where many organisations stop paying attention, and implementation is "
              "where most policies change shape. A short monitoring plan, agreed before rollout, "
              "keeps attention on the points where Sections 6 to 8 show failures usually happen. "
              "Pick the rows that match the policy's main risk."),
            T(["If the main risk is...", "Monitor", "Source of data", "Early warning sign"],
              [["Exclusion of eligible people", "Rejections, failed authentications, appeals",
                "MIS, grievance logs, household survey", "Rising rejections in one block"],
               ["Leakage or ghost beneficiaries", "Payments against verified beneficiaries",
                "Payment records, audit samples", "Payments to unverified accounts"],
               ["Delayed payments", "Days from work or claim to credit", "Payment system data",
                "Median delay above the legal limit"],
               ["Frontline overload", "Cases per official; vacancies", "Staffing records, time-use",
                "Vacancy rate rising with caseload"],
               ["Allocation below demand", "Work or benefit demanded against provided",
                "MIS demand registers, field checks", "Unrecorded demand reported in the field"]]),
            H("indigo", "Under the VB-G RAM G Act, wages are due within a fortnight (s5(3)), and "
              "work is due within fifteen days of an application, failing which the allowance "
              "under s11 applies. Those legal deadlines are natural indicators."),
        ]),

        S("Pitfalls", "Common mistakes in policy work", [
            B("These mistakes recur in policy proposals from NGOs, researchers and governments "
              "alike. Each has appeared in this course in some form. Use the list as a final "
              "check before a recommendation leaves your desk."),
            TC([P("red", "In analysis",
                  "Treating a scheme guideline as the law. Ignoring the status quo option. "
                  "Counting leakage savings without counting exclusion. Quoting a figure with no "
                  "year or source. Assuming a pilot's results will hold at scale.")],
               [P("amber", "In engagement",
                  "Arriving after the decision is made. Writing to the minister when the file "
                  "sits with a joint secretary. Ignoring state governments in a state subject. "
                  "Asking for everything at once. Treating officials only as opponents.")]),
            H("green", "The habit that prevents most of them: write down the specific decision, the "
              "person who will make it, and the date, before you start the analysis."),
        ]),

        # ===================== SECTION 11 =====================
        DIV("11", "Eleven", "Writing a policy brief, and where next"),

        S("The brief", "What a policy brief is for", [
            B("A policy brief is a short document, usually two to four pages, written for a "
              "decision maker who has little time and a decision to make. It differs from a "
              "research paper in purpose. The paper shows how the authors know something; the "
              "brief tells a reader what to do about it, with just enough evidence to be "
              "trusted."),
            TC([P("cyan", "Research paper",
                  "Written for peers; question, method, results, discussion; long; hedged; "
                  "judged on rigour.")],
               [P("green", "Policy brief",
                  "Written for a named decision maker; finding first; short; clear "
                  "recommendation; judged on whether it is used.")]),
            H("amber", "Before writing, answer three questions in one sentence each: who will read "
              "it, what decision they face, and what you want them to do."),
        ]),

        S("Structure", "A standard structure for a policy brief", [
            B("The structure below puts the conclusion first, because many readers stop after the "
              "first paragraph. Every later section supports that opening. Keep the evidence "
              "section to the two or three findings that matter for the decision, each with its "
              "source."),
            FL(["Title that states the finding",
                "Summary: problem, finding, recommendation in 100 words",
                "The problem, with numbers and sources",
                "Options, including the status quo",
                "Recommendation and next steps",
                "Sources and contact"]),
            TC([B("<strong>Title example (Illustrative):</strong> \"Fingerprint failures are "
                  "excluding eligible families; a nominee rule would fix most cases\".", sm=True)],
               [B("<strong>Weak title:</strong> \"An analysis of authentication in the public "
                  "distribution system\". It names a topic and gives no finding.", sm=True)]),
        ]),

        S("Writing", "Writing rules for briefs", [
            B("Officials read briefs quickly, often on a phone. Plain words, short sentences and "
              "numbers with sources make a brief easier to act on and harder to dismiss. The "
              "before-and-after example is invented to show the difference."),
            TC([P("red", "Before (Illustrative)",
                  "\"It may be observed that a significant number of beneficiaries may be "
                  "experiencing challenges with regard to accessing entitlements.\"")],
               [P("green", "After (Illustrative)",
                  "\"In our survey of 600 households in two blocks, one in eight eligible "
                  "families was refused rations at least once in the last three months.\"")]),
            BL(["Lead each paragraph with its point.",
                "Give every number its source and year.",
                "Use the active voice and name who must act.",
                "State uncertainty once, plainly, with its reason."]),
        ]),

        S("Evidence in a brief", "Presenting evidence and its limits", [
            B("A brief earns trust by being exact about what is known. Give the source and year of "
              "every number, say what kind of study produced it, and state the main limit in one "
              "plain sentence. Readers forgive uncertainty that is explained; they stop trusting "
              "a brief that overstates."),
            TC([P("cyan", "Say where a number comes from",
                  "\"A randomised evaluation across 157 subdistricts of Andhra Pradesh found "
                  "faster payments (Muralidharan, Niehaus and Sukhtankar, AER 2016).\"")],
               [P("amber", "Say what it cannot tell you",
                  "\"A later study in Jharkhand's ration system found 1.5 to 2 million eligible "
                  "people lost access at some point, so results depend on how a reform is run.\"")]),
            BL(["Prefer one strong study you can describe to five you cannot.",
                "Show a range when estimates differ, and say why they differ.",
                "Label any example you invented as illustrative.",
                "Date every claim that can change, such as a law's status or a budget figure."]),
        ]),

        S("Summary", "Ten points to take away", [
            B("Each point links to a section of this course and to a decision a practitioner "
              "makes. Return to them when you review a scheme, comment on a draft or plan an "
              "evaluation."),
            BL(["Policy is what governments choose to do or not to do; inaction is a choice too.",
                "One policy lives in an Act, rules, a scheme, a budget and sometimes a court order.",
                "The cycle maps stages; Lindblom, Kingdon and Baumgartner and Jones explain change.",
                "Pick the instrument from the cause of the problem: authority, treasure, nodality, organisation.",
                "In India, consultations under the Transaction of Business Rules shape drafts before anyone sees them.",
                "Only 16% of bills went to committees in the 17th Lok Sabha; engage early.",
                "Frontline officials make policy in practice; design for their workload.",
                "Count exclusion as carefully as leakage.",
                "The VB-G RAM G Act 2025 changes days, funding and planning; watch the data.",
                "A brief states the finding first and names who must act."]),
            H("cyan", "Facts are stated as of October 2026. Check later amendments, rules and "
              "judgments before relying on them."),
        ]),

        S("Where next", "Where next: related courses", [
            B("Public policy connects to most courses in the ImpactMojo 101 Series. These are the "
              "most direct next steps, chosen to deepen the law, the politics, the money and the "
              "evidence behind the topics in this deck."),
            TC([BL(["Accountability, RTI and service delivery: " + L("governance-accountability.html", "Governance &amp; Accountability 101"),
                    "Articles, rights and remedies: " + L("ind-constitution.html", "Indian Constitution 101"),
                    "Interests, elites and capture: " + L("pol-economy.html", "Political Economy 101"),
                    "Budgets and fiscal federalism: " + L("public-finance-budgeting.html", "Public Finance &amp; Budgeting 101"),
                    "Turning analysis into change: " + L("advocacy-basics.html", "Advocacy Basics 101")])],
               [BL(["Testing what works: " + L("impact-eval.html", "Impact Evaluation 101"),
                    "Designing for causal claims: " + L("causal-inference.html", "Causal Inference 101"),
                    "Comparing options by cost: " + L("cost-effectiveness.html", "Cost Effectiveness 101"),
                    "From idea to scheme design: " + L("programme-design.html", "Programme Design 101"),
                    "Data, consent and the law: " + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101")])]),
            H("green", "All courses are free. Start with Governance &amp; Accountability 101 if "
              "implementation is your main concern, or Political Economy 101 for the incentives "
              "behind policy choices."),
        ]),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Public Policy 101 &middot; Complete",
         "headline": "Read the law, watch the frontline,<br>count who is left out",
         "byline": "Policy is made in Cabinet notes, committee rooms and courtrooms, and remade "
                   "every day at the ration shop and the school gate. Diagnose the cause, choose "
                   "the tool that fits, design for the officials who deliver it, and test it "
                   "in the open. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

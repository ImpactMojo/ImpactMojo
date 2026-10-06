# -*- coding: utf-8 -*-
"""
Child Rights 101 -- ImpactMojo 101 Series (native deck spec)
Children's rights for development practitioners in South Asia: the UN Convention on the Rights
of the Child and its protocols, India's constitutional and statutory framework, institutions and
schemes, neighbours' laws, participation, and children in data and research.
Build: python3 scripts/deck-builder/build.py child_rights

House style: no em dashes, sentence-case headings, every statistic sourced on the slide,
every law cited by act, year and section, made-up teaching examples labelled Illustrative.
Facts were checked against the sources listed in the build report (October 2026).
"""


# ---------------------------------------------------------------------------
# Small helpers so the spec stays readable
# ---------------------------------------------------------------------------
def C(label, title, *blocks, **kw):
    d = {"type": "content", "label": label, "title": title, "blocks": list(blocks)}
    d.update(kw)
    return d


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


def B(html, sm=False):
    b = {"t": "body", "html": html}
    if sm:
        b["cls"] = "sm"
    return b


def H(color, html):
    return {"t": "hbox", "color": color, "html": html}


def P(color, title, html):
    return {"t": "panel", "color": color, "title": title, "blocks": [B(html, sm=True)]}


def TW(left, right, ratio="half"):
    return {"t": "twocol", "ratio": ratio, "left": left, "right": right}


def T(head, rows):
    return {"t": "table", "head": head, "rows": rows}


def BL(items, color="", sm=True):
    b = {"t": "bullets", "items": items}
    if color:
        b["color"] = color
    if sm:
        b["sm"] = True
    return b


def TERM(word, d):
    return {"t": "term", "word": word, "def": d}


def ST(cards, cols=None):
    return {"t": "stats", "cols": cols or len(cards), "cards": cards}


def CARD(num, label, color="cyan", source=None):
    c = {"num": num, "label": label, "color": color}
    if source:
        c["source"] = source
    return c


def FLOW(*steps):
    return {"t": "flow", "steps": list(steps)}


def Q(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


UNTC = "UN Treaty Collection, status as at 6 October 2026"
DHS = "NFHS-5 (2019-21), tabulated by the DHS Program API, indicator MA_MBAY_W_B18"

SLIDES = []

# ===================== S1 TITLE, S2 TOC =====================
SLIDES += [
    {"type": "title",
     "main": "Child<br>Rights<br>101",
     "sub": "The UN Convention on the Rights of the Child, India's Constitution and child laws, "
            "the institutions that enforce them, neighbours' frameworks, participation, and "
            "children in data and research, for development practitioners in South Asia",
     "tags": ["100 Slides", "South Asia Focus", "Free Forever", "CRC, JJ Act and POCSO"]},

    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Why child rights"},
         {"name": "The Convention and its four principles"},
         {"name": "Protocols, the Committee and reporting"},
         {"name": "India's constitutional framework"},
         {"name": "Juvenile justice: the JJ Act 2015"},
         {"name": "Sexual offences: the POCSO Act 2012"},
         {"name": "Education and child labour"},
         {"name": "Child marriage"},
         {"name": "Institutions and schemes"},
         {"name": "Neighbours' frameworks"},
         {"name": "Putting it to work"},
         {"name": "Participation, research and data"},
     ]},
]

# ===================== SECTION 01 =====================
SLIDES += [
    D("01", "Section One", "Why child rights"),

    C("The idea", "Children hold rights of their own, here and now",
      TERM("Child rights",
           "Entitlements that every person below eighteen holds as a person, set out in the UN "
           "Convention on the Rights of the Child (1989) and in national law. They cover survival, "
           "development, protection and participation, and they bind the state, which must respect "
           "them, protect children from others who would breach them, and provide what is needed "
           "to realise them."),
      TW([P("amber", "The welfare view",
            "Children are objects of care. Adults decide what is good for them, and services are a "
            "matter of charity or policy choice. A child who is not helped has no complaint, only "
            "bad luck. Programmes in this frame count beneficiaries and rarely ask children "
            "anything.")],
         [P("green", "The rights view",
            "Children are holders of claims. The state owes them specific things, can be asked to "
            "account, and must take their views into account as they grow. A child who is not "
            "helped has been wronged, and someone has a duty to put it right.")]),
      H("cyan", "Most South Asian child policy still mixes the two. Practitioners need to read "
        "which frame a scheme, a court order or a donor log-frame is using, because it changes "
        "what counts as success.")),

    C("Why it matters for practice", "Rights change four questions a programme has to answer",
      B("A development project that touches children (a school meal, a vaccination drive, a "
        "survey, a livelihood grant to a mother) already affects their rights. The rights frame "
        "adds four questions that a needs assessment on its own tends to skip."),
      T(["Question", "What it asks", "Where it comes from"],
        [["Who is left out?", "Which children are excluded by caste, disability, gender, migration "
          "or lack of documents, and why", "CRC Article 2, non-discrimination"],
         ["Whose interest decides?", "Whether the child's best interests were weighed, or the "
          "convenience of the institution, the family or the donor", "CRC Article 3(1)"],
         ["Is the child safe?", "Whether the activity creates risks of abuse, exploitation or "
          "exposure, and who responds if harm happens", "CRC Articles 19 and 34; POCSO 2012"],
         ["Was the child heard?", "Whether children had a say in decisions affecting them, in a "
          "form suited to their age", "CRC Article 12"]]),
      H("green", "None of these needs a lawyer. Each needs someone in the team whose job is to ask "
        "it before the design is fixed."), compact=True),

    C("Scale", "Three numbers that frame child rights in India",
      ST([CARD("472 million", "children up to 18 in India, almost 39 per cent of the population",
               "cyan", "PIB explainer on Mission Vatsalya, 11 August 2023"),
          CARD("35.5%", "children under five stunted in India", "amber",
               "NFHS-5 (2019-21), DHS Program API, CN_NUTS_C_HA2"),
          CARD("1,87,702", "crimes against children registered in India in 2024, up from "
               "1,77,335 in 2023; 42.3 per lakh children", "red",
               "NCRB, Crime in India 2024, Vol. I, Tables 4A.1 and 4A.2")]),
      TW([B("These three numbers point at three families of rights. The first is a reminder that "
            "child policy in India is population policy. The second is a survival and "
            "development right: stunting is measured damage to growth that is hard to reverse "
            "after the first years. The third is a protection right, and it counts only what was "
            "reported to the police.", sm=True)],
         [H("amber", "Read the crime figure carefully. A rise in registered cases can mean more "
            "abuse, more reporting, or both. The National Crime Records Bureau counts First "
            "Information Reports, so better access to police and mandatory reporting under "
            "POCSO both push the number up.")])),

    C("Four families", "One way to group the rights: survive, develop, be protected, take part",
      TW([P("cyan", "Survival and development",
            "Life, health, nutrition, birth registration and an adequate standard of living "
            "(CRC Articles 6, 7, 24, 27). Education and early childhood care (Articles 28 and 29). "
            "Play and rest (Article 31). In India these run through ICDS, the school system and "
            "health missions."),
          P("green", "Protection",
            "Freedom from violence, abuse and neglect (Article 19), economic exploitation "
            "(Article 32) and sexual exploitation (Article 34), and fair treatment in the justice "
            "system (Articles 37 and 40). In India: the JJ Act, POCSO, the child labour and child "
            "marriage laws.")],
         [P("indigo", "Participation",
            "Expressing views and having them weighed (Article 12), freedom of expression, "
            "thought and association (Articles 13 to 15), access to information (Article 17). "
            "The least implemented family almost everywhere."),
          P("amber", "Cross-cutting duties",
            "Non-discrimination (Article 2) and best interests (Article 3) apply to all the "
            "others. For economic, social and cultural rights the state must act to the maximum "
            "extent of available resources (Article 4), and must make the Convention known to adults and children (Article 42).")]),
      H("cyan", "The grouping is a teaching device. The Convention itself treats rights as "
        "indivisible: a child out of school is more exposed to labour and early marriage.")),

    C("Duty bearers", "Who owes what to whom",
      B("Rights only mean something if you can name the person or body that owes the duty. In "
        "child rights work there are several layers, and practitioners often sit in more than one."),
      T(["Duty bearer", "Typical duties", "Indian example"],
        [["State (Union and states)", "Make laws, fund services, set up courts and commissions, "
          "report to the UN Committee", "Ministry of Women and Child Development; state "
          "departments; NCPCR and SCPCRs"],
         ["Statutory bodies", "Decide individual cases about children", "Child Welfare "
          "Committees and Juvenile Justice Boards under the JJ Act 2015 (ss. 27 and 4)"],
         ["Institutions", "Run schools, homes and hospitals safely; report abuse", "A school's "
          "duty to report under POCSO s. 19, and the penalty for an institution's head under s. 21(2)"],
         ["Parents and guardians", "Care, guidance, education", "Constitution Article 51A(k): "
          "parents to provide opportunities for education from six to fourteen"],
         ["Everyone", "Report sexual offences against children", "POCSO s. 19(1) applies to "
          "\"any person\""]]),
      H("amber", "Once an NGO runs a home, a school or a helpline, it carries statutory duties "
        "of its own.")),

    C("A caution", "Rights talk can be used against the children it names",
      TW([P("red", "Three misuses to watch for",
            "<strong>Protection as control:</strong> confining adolescent girls \"for their "
            "safety\". <strong>Rescue without consent:</strong> raids that remove working children "
            "and return them to the same poverty with no follow-up. <strong>Criminalising "
            "adolescents:</strong> using a sexual offences law against two sixteen-year-olds in a "
            "relationship, the problem the Law Commission's 283rd Report (2023) took up.")],
         [P("green", "What the Convention says instead",
            "Measures must serve the child's best interests (Article 3), respect the child's "
            "evolving capacities (Article 5), and give due weight to the child's views (Article 12). "
            "Detention is a measure of last resort and for the shortest time (Article 37(b)).")]),
      H("cyan", "The test for any intervention: would the child, once old enough to judge, agree "
        "that it was done for them? If the honest answer is no, re-examine the design."),
      B("This deck returns to these tensions in the sections on juvenile justice, POCSO and child "
        "marriage, where the law's protective intent and its effects on adolescents can diverge.",
        sm=True)),
]

# ===================== SECTION 02 =====================
SLIDES += [
    D("02", "Section Two", "The Convention and its four principles"),

    C("The treaty", "The UN Convention on the Rights of the Child, 1989",
      ST([CARD("20 Nov 1989", "adopted by the UN General Assembly, resolution 44/25", "cyan",
               "OHCHR, text of the Convention"),
          CARD("2 Sep 1990", "entry into force, under Article 49", "indigo",
               "OHCHR; UN Treaty Collection"),
          CARD("196", "States parties; 140 states signed first", "green", UNTC)]),
      TW([B("The Convention has 54 articles in three parts. Part I (Articles 1 to 41) sets out "
            "rights, Part II (Articles 42 to 45) deals with monitoring, and Part III with "
            "signature and entry into force. Article 1 "
            "defines a child as every human being below eighteen, unless majority is attained "
            "earlier under the law applicable to the child.", sm=True)],
         [H("amber", "The United States signed on 16 February 1995 and has not ratified (UN "
            "Treaty Collection). Under the Vienna Convention on the Law of Treaties 1969, Article "
            "18(a), a signatory must refrain from acts that would defeat the treaty's \"object and "
            "purpose\" until it makes clear it will not become a party; the treaty's obligations "
            "bind a state only once it ratifies or accedes.")]),
      H("green", "Near-universal ratification means the Convention is the shared vocabulary of "
        "child rights. When a government, a donor and an NGO disagree, it is usually the "
        "common text they can all be held to.")),

    C("South Asia's dates", "Every South Asian state is a party",
      T(["State", "Signed", "Ratified or acceded", "Note"],
        [["Bangladesh", "26 Jan 1990", "3 Aug 1990", "Reservation to Art. 14(1); Art. 21 subject to existing law"],
         ["Bhutan", "4 Jun 1990", "1 Aug 1990", ""],
         ["Nepal", "26 Jan 1990", "14 Sep 1990", ""],
         ["Pakistan", "20 Sep 1990", "12 Nov 1990", ""],
         ["Maldives", "21 Aug 1990", "11 Feb 1991", "Reservations including on adoption"],
         ["Sri Lanka", "26 Jan 1990", "12 Jul 1991", ""],
         ["India", "not signed", "11 Dec 1992 (accession)", "Declaration on Art. 32, child labour"],
         ["Afghanistan", "27 Sep 1990", "28 Mar 1994", ""]]),
      B("Source: " + UNTC + ", Chapter IV.11. India acceded without signing first, which has "
        "the same legal effect as ratification. The Commissions for Protection of Child Rights "
        "Act 2005, s. 2(b), describes the Convention as \"ratified by the Government of India on "
        "the 11th December, 1992\".", sm=True), compact=True),

    C("India's declaration", "India accepted Article 32 with a stated plan to phase it in",
      Q("the Government of India undertakes to take measures to progressively implement the "
        "provisions of article 32, particularly paragraph 2 (a), in accordance with its national "
        "legislation and relevant international instruments to which it is a State Party.",
        "Declaration of India on accession, 11 December 1992 (UN Treaty Collection)"),
      TW([B("Article 32 protects children from economic exploitation and harmful work, and "
            "paragraph 2(a) asks states to set a minimum age for admission to employment. "
            "India's declaration noted that \"children of different ages do work in India\" and "
            "that it was \"not practical immediately\" to set minimum ages for every area of "
            "employment.", sm=True)],
         [H("cyan", "Read the 2016 amendment to the child labour law (Section 07) as the "
            "follow-through: it banned all employment below fourteen, with exceptions, and "
            "hazardous work below eighteen. A declaration is a promise with a timetable left "
            "open, and civil society can hold the state to it.")]),
      B("Bangladesh and the Maldives entered reservations; Pakistan's original reservation is not "
        "covered here. Check the current text on the UN Treaty Collection before quoting any "
        "state's reservations.", sm=True)),

    C("Principle 1", "Non-discrimination: Article 2",
      Q("States Parties shall respect and ensure the rights set forth in the present Convention "
        "to each child within their jurisdiction without discrimination of any kind, irrespective "
        "of the child's or his or her parent's or legal guardian's race, colour, sex, language, "
        "religion, political or other opinion, national, ethnic or social origin, property, "
        "disability, birth or other status.", "CRC Article 2(1)"),
      TW([P("cyan", "Two features worth noticing",
            "It covers every child \"within their jurisdiction\", so refugee, stateless and "
            "migrant children are included. And it bars discrimination based on the "
            "<em>parent's</em> status, so a child cannot be penalised for a father's caste, a "
            "mother's religion or a parent's lack of papers.")],
         [P("green", "In South Asian practice",
            "\"Social origin\" and \"birth or other status\" are the grounds that reach caste "
            "and descent. Disability is named expressly in Article 2, and Article 23 adds a "
            "specific right for children with disabilities to a full and decent life with "
            "dignity and active participation in the community.")]),
      H("amber", "Equal treatment can still produce unequal results. Article 2(2) adds a duty to "
        "protect the child against discrimination, which supports targeted measures for the "
        "children most likely to be left out.")),

    C("Principle 2", "Best interests: Article 3(1)",
      Q("In all actions concerning children, whether undertaken by public or private social "
        "welfare institutions, courts of law, administrative authorities or legislative bodies, "
        "the best interests of the child shall be a primary consideration.",
        "CRC Article 3(1)"),
      TW([P("indigo", "What the words do",
            "\"All actions\" covers budgets and laws as well as court cases. \"Private social "
            "welfare institutions\" brings NGOs inside the rule. \"<em>A</em> primary "
            "consideration\" means best interests must be weighed heavily, though other "
            "interests can count too. For adoption, Article 21 makes it \"the paramount "
            "consideration\".")],
         [P("green", "How the Committee reads it",
            "General comment No. 14 (2013) treats best interests as a right, a principle for "
            "interpreting law, and a rule of procedure: decisions should show how the child's "
            "interests were assessed and weighed (Committee on the Rights of the Child).")]),
      H("cyan", "India's JJ Act 2015, s. 3(iv), writes it into domestic law as the \"principle "
        "of best interest\": all decisions about a child are to be based on the child's best "
        "interest and help the child develop full potential.")),

    C("Principle 3", "Life, survival and development: Article 6",
      Q("1. States Parties recognize that every child has the inherent right to life. 2. States "
        "Parties shall ensure to the maximum extent possible the survival and development of "
        "the child.", "CRC Article 6"),
      TW([B("The first paragraph is a negative duty: do not take a child's life. The second is a "
            "positive duty with a resource clause, \"to the maximum extent possible\". Development "
            "in the Convention is broad: physical, mental, spiritual, moral and social, as Article "
            "27 later spells out for the standard of living.", sm=True)],
         [B("This is the principle behind nutrition, immunisation, early childhood care and "
            "safe water. It is also behind Article 7, registration immediately after birth, "
            "because a child who is not recorded is invisible to every scheme that follows.",
            sm=True)]),
      ST([CARD("35.5%", "stunted under-fives, India", "amber", "NFHS-5 (2019-21), DHS Program API"),
          CARD("24.8%", "stunted under-fives, Nepal", "cyan", "Nepal DHS 2022, DHS Program API"),
          CARD("23.6%", "stunted under-fives, Bangladesh", "green", "Bangladesh DHS 2022, DHS Program API")]),
      compact=True),

    C("Principle 4", "Respect for the child's views: Article 12",
      Q("States Parties shall assure to the child who is capable of forming his or her own views "
        "the right to express those views freely in all matters affecting the child, the views "
        "of the child being given due weight in accordance with the age and maturity of the "
        "child.", "CRC Article 12(1)"),
      TW([P("cyan", "Article 12 carries two duties",
            "Children must be able to express views, and those views must be given "
            "<strong>due weight</strong>. Hearing a child and then ignoring what they said "
            "satisfies the first half only. The weight given grows with the child's age and "
            "maturity.")],
         [P("green", "Article 12(2)",
            "The child must have the opportunity to be heard in any judicial and administrative "
            "proceeding affecting the child, directly or through a representative. Custody, "
            "adoption, a Child Welfare Committee inquiry and a school expulsion are all covered.")]),
      H("amber", "Section 12 of this deck returns to participation: models for doing it, and the "
        "ethics of asking children to speak.")),

    C("Together", "The four principles read as a set",
      B("UNICEF describes the four as the core principles of the Convention: non-discrimination, "
        "devotion to the best interests of the child, the right to life, survival and "
        "development, and respect for the views of the child (UNICEF Armenia, \"Four principles "
        "of the Convention\", 24 June 2019). They are meant to be applied to every other right."),
      T(["Right in question", "Non-discrimination asks", "Best interests asks", "Survival and development asks", "Views asks"],
        [["School admission", "Are Dalit, disabled and migrant children admitted on the same terms?",
          "Is the nearest school the best option for this child?", "Does the child learn, or only enrol?",
          "Were children consulted on safety and timing?"],
         ["Placement in care", "Are girls placed more often than boys?", "Is the family option "
          "exhausted first?", "Does the home meet health and education needs?", "Did the child "
          "say where they want to live?"],
         ["A survey", "Are hard-to-reach children sampled?", "Does the interview risk harm?",
          "Does the data lead to services?", "Did the child assent?"]]),
      H("cyan", "Use this grid as a design check. A blank cell is a question nobody on the team "
        "has answered."), compact=True),

]

# ===================== SECTION 03 =====================
SLIDES += [
    D("03", "Section Three", "Protocols, the Committee and reporting"),

    C("Three protocols", "Three optional protocols extend the Convention",
      B("An optional protocol is a separate treaty that a state chooses to join. The first two "
        "add protection against involvement in armed conflict and against sale, prostitution "
        "and pornography; the third lets children, or people acting for them, bring complaints "
        "to the Committee."),
      T(["Protocol", "Adopted", "In force", "Parties", "Core duty"],
        [["Involvement of children in armed conflict (OPAC)", "25 May 2000, A/RES/54/263",
          "12 Feb 2002", "173", "No compulsory recruitment under 18; feasible measures so that "
          "under-18 members do not take a direct part in hostilities"],
         ["Sale of children, child prostitution and child pornography (OPSC)", "25 May 2000, "
          "A/RES/54/263", "18 Jan 2002", "178", "Criminalise the listed offences; cooperate "
          "across borders"],
         ["Communications procedure (OPIC)", "19 Dec 2011, A/RES/66/138", "14 Apr 2014", "54",
          "Children or their representatives can complain to the Committee after domestic "
          "remedies"]]),
      B("Source: " + UNTC + ", Chapter IV.11b, 11c and 11d; UNICEF, \"Optional Protocols\".",
        sm=True), compact=True),

    C("Who has joined", "South Asia and the protocols",
      T(["State", "OPAC ratified", "OPSC ratified", "OPIC (complaints)"],
        [["Bangladesh", "6 Sep 2000", "6 Sep 2000", "Not a party"],
         ["Sri Lanka", "8 Sep 2000", "22 Sep 2006", "Not a party"],
         ["Maldives", "29 Dec 2004", "10 May 2002", "Ratified 27 Sep 2019"],
         ["India", "30 Nov 2005", "16 Aug 2005", "Not a party"],
         ["Nepal", "3 Jan 2007", "20 Jan 2006", "Not a party"],
         ["Bhutan", "9 Dec 2009", "26 Oct 2009", "Not a party"],
         ["Pakistan", "17 Nov 2016", "5 Jul 2011", "Not a party"],
         ["Afghanistan", "24 Sep 2003 (accession)", "19 Sep 2002 (accession)", "Not a party"]]),
      TW([B("Source: " + UNTC + ". The pattern is consistent: every state has accepted the "
            "substantive protocols, and only the Maldives has accepted the complaints "
            "procedure.", sm=True)],
         [H("amber", "For an Indian child, this means there is no route to the UN Committee for "
            "an individual complaint. Remedies run through Indian courts, the NCPCR and "
            "state commissions.")])),

    C("Recruitment ages", "What South Asian states declared under OPAC",
      B("OPAC Article 3(2) requires each state to declare the minimum age at which it permits "
        "voluntary recruitment. The declarations below are quoted or summarised from the UN "
        "Treaty Collection."),
      TW([P("cyan", "India",
            "\"The minimum age for recruitment of prospective recruits into Armed Forces of India "
            "(Army, Air Force and Navy) is 16 years. After enrollment and requisite training "
            "period, the attested Armed Forces personnel is sent to the operational area only "
            "after he attains 18 years of age.\" Recruitment is stated to be voluntary."),
          P("indigo", "Bangladesh",
            "Sixteen for non-commissioned soldiers and seventeen for commissioned officers, with "
            "informed consent of a parent or legal guardian.")],
         [P("green", "Nepal",
            "\"The minimum age for recruitment in the Nepal Army and the Armed Police Force shall "
            "be 18 years.\""),
          P("amber", "Sri Lanka",
            "No compulsory recruitment; recruitment voluntary; \"the minimum age for voluntary "
            "recruitment into national armed forces is 18 years.\"")]),
      H("cyan", "The protocol permits voluntary recruitment below eighteen with safeguards, "
        "which is why the declared ages differ. The rule against direct participation in "
        "hostilities under eighteen applies to all."), compact=True),

    C("The Committee", "The Committee on the Rights of the Child",
      ST([CARD("18", "independent experts, elected by States parties", "cyan",
               "CRC Article 43(2), as amended"),
          CARD("2 years", "first report due after the Convention enters into force for a state",
               "indigo", "CRC Article 44(1)(a)"),
          CARD("5 years", "periodic reports thereafter", "green", "CRC Article 44(1)(b)")]),
      TW([B("Members serve in their personal capacity, with attention to equitable geographical "
            "distribution and the principal legal systems. The Committee started with ten "
            "members. General Assembly resolution 50/155 of 21 December 1995 replaced \"ten\" "
            "with \"eighteen\", and the amendment entered into force on 18 November 2002 (UNICEF "
            "text of the Convention, note to Article 43).", sm=True)],
         [B("The Committee does not issue binding judgments under the Convention itself. It "
            "reviews reports, adopts concluding observations with recommendations, and writes "
            "general comments that interpret the Convention. Under OPIC it can also decide "
            "individual complaints against states that accepted the protocol.", sm=True)]),
      H("amber", "Concluding observations carry weight because they are specific, public and "
        "revisited at the next review. They give NGOs and commissions a public, dated "
        "benchmark to measure the government against.")),

    C("The cycle", "How a periodic review works",
      FLOW("STATE REPORT: the government reports on measures and difficulties (Art. 44)",
           "ALTERNATIVE REPORTS: NGOs, children's groups and national institutions submit their own",
           "LIST OF ISSUES: the Committee asks follow-up questions",
           "DIALOGUE: the delegation answers in Geneva",
           "CONCLUDING OBSERVATIONS: published recommendations",
           "FOLLOW-UP: civil society tracks implementation until the next cycle"),
      TW([B("Under the simplified reporting procedure the order changes: the Committee sends a "
            "list of issues <em>before</em> the report, and the state's replies become the "
            "report. This shortens the paperwork and lets the Committee focus questions.",
            sm=True)],
         [H("green", "Practitioners enter at step two. An alternative report built from "
            "programme data, case files and children's own accounts is often the most concrete "
            "evidence the Committee sees.")])),

    C("India's record", "India's reviews before the Committee",
      T(["Item", "Detail", "Source"],
        [["Combined third and fourth report", "Due 10 July 2008; submitted 26 August 2011",
          "OHCHR treaty body database, India"],
         ["Concluding observations", "CRC/C/IND/CO/3-4, adopted 13 June 2014 (66th session)",
          "OHCHR treaty body database"],
         ["OPAC and OPSC reviews", "CRC/C/OPAC/IND/CO/1 and CRC/C/OPSC/IND/CO/1, both 13 June 2014",
          "OHCHR treaty body database"],
         ["Civil society input", "Alternative reports from groups including the India Alliance "
          "for Child Rights", "OHCHR treaty body database"],
         ["Next cycle (fifth and sixth)", "Listed under the simplified reporting procedure; the "
          "list of issues prior to reporting had not been adopted as at October 2026",
          "OHCHR treaty body database, viewed 6 October 2026"]]),
      H("amber", "More than twelve years have passed since India's last full review. That gap is "
        "itself a finding worth stating in an alternative report: the Convention's reporting "
        "rhythm is five years (Article 44(1)(b))."), compact=True),

    C("General comments", "General comments: the Committee's reading of the text",
      TW([B("A general comment is the Committee's authoritative interpretation of an article or a "
            "theme. It is not a treaty, but courts, governments and donors rely on it to fill "
            "gaps in the text. Five that practitioners in South Asia use often:", sm=True),
          BL(["<strong>No. 14 (2013):</strong> best interests as a primary consideration, Art. 3(1)",
              "<strong>No. 19 (2016):</strong> public budgeting for children's rights, Art. 4",
              "<strong>No. 20 (2016):</strong> rights during adolescence",
              "<strong>No. 24 (2019):</strong> children's rights in the child justice system",
              "<strong>No. 26 (2023):</strong> children's rights and the environment, with a "
              "focus on climate change"], color="cyan")],
         [P("indigo", "How to use one",
            "General comment No. 14 describes best interests as a \"threefold concept\": a "
            "substantive right, an interpretive legal principle, and a rule of procedure. The "
            "procedural part is the useful one for an NGO: \"the decision-making process must "
            "include an evaluation of the possible impact (positive or negative) of the decision "
            "on the child\". Ask to see that evaluation.")]),
      H("green", "Titles and years are from the OHCHR treaty body database; GC 14 wording from "
        "CRC/C/GC/14, paragraph 6.")),
]

# ===================== SECTION 04 =====================
SLIDES += [
    D("04", "Section Four", "India's constitutional framework"),

    C("The text", "Five articles that speak about children",
      T(["Article", "Part", "What it says"],
        [["15(3)", "III, fundamental right", "Nothing in Article 15 prevents the State from "
          "making \"any special provision for women and children\""],
         ["21A", "III, fundamental right", "\"The State shall provide free and compulsory "
          "education to all children of the age of six to fourteen years in such manner as the "
          "State may, by law, determine.\""],
         ["24", "III, fundamental right", "\"No child below the age of fourteen years shall be "
          "employed to work in any factory or mine or engaged in any other hazardous employment.\""],
         ["39(e) and (f)", "IV, directive principle", "The tender age of children is not to be "
          "abused; children are to be given \"opportunities and facilities to develop in a "
          "healthy manner and in conditions of freedom and dignity\""],
         ["45", "IV, directive principle", "\"The State shall endeavour to provide early "
          "childhood care and education for all children until they complete the age of six years.\""]]),
      B("Text as it stands today, from constitutionofindia.net. Article 51A(k), a fundamental "
        "duty, adds that a parent or guardian is to provide opportunities for education to a "
        "child between six and fourteen.", sm=True), compact=True),

    C("Two tiers", "Enforceable rights and guiding principles",
      TW([P("cyan", "Part III: fundamental rights",
            "Articles 15(3), 21A and 24 are justiciable. A person can go to a High Court under "
            "Article 226 or the Supreme Court under Article 32 to enforce them. Article 24 is "
            "worded as a flat prohibition, \"No child below the age of fourteen years shall be "
            "employed\", without naming who employs, which is why petitions about factories "
            "and private workplaces have relied on it."),
          P("green", "Article 15(3) in practice",
            "It is the constitutional basis for laws and schemes that treat children "
            "differently from adults: special courts under POCSO, reserved admission under the "
            "RTE Act, separate procedures under the JJ Act. Without it, such provisions could "
            "be attacked as unequal treatment.")],
         [P("indigo", "Part IV: directive principles",
            "Articles 39(e), 39(f) and 45 are \"not enforceable by any court\" (Article 37), but "
            "are \"fundamental in the governance of the country\". Courts read them alongside "
            "fundamental rights, especially Article 21 (life and personal liberty), to give "
            "content to rights that the text leaves open."),
          P("amber", "Why the tiers matter",
            "Early childhood care (Article 45) remains a directive principle. Education from six "
            "to fourteen became a fundamental right only in 2002. A child of four has a weaker "
            "constitutional claim than a child of six.")]),
      H("cyan", "The Indian Constitution 101 deck explains Parts III and IV and the writ "
        "jurisdiction in detail.")),

    C("The 2002 amendment", "How education became a fundamental right",
      FLOW("1950: Article 45 directs the State to provide free and compulsory education until 14 within ten years",
           "1960 deadline passes without universal schooling",
           "12 Dec 2002: Constitution (Eighty-sixth Amendment) Act inserts Article 21A",
           "Same Act rewrites Article 45 for children under six and adds Article 51A(k)",
           "2009: Right of Children to Free and Compulsory Education Act gives 21A its content",
           "1 April 2010: Article 21A and the RTE Act come into effect"),
      TW([B("The original Article 45 read: \"The State shall endeavour to provide, within a "
            "period of ten years from the commencement of this Constitution, for free and "
            "compulsory education for all children until they complete the age of fourteen "
            "years.\" The ten-year target was missed by decades.", sm=True)],
         [H("amber", "Article 21A says education will be provided \"in such manner as the State "
            "may, by law, determine\". The right exists only as the RTE Act shapes it, which is "
            "why changes to that Act (such as the 2019 amendment on holding children back) "
            "matter constitutionally.")]),
      B("Sources: constitutionofindia.net (original Article 45); text of the Eighty-sixth Amendment "
        "Act, dated 12 December 2002; Accountability Initiative brief reproducing the Ministry of "
        "Education's RTE note (\"Article 21-A and the RTE Act came into effect on 1 April 2010\").",
        sm=True)),

    C("Article 24", "Article 24 and the courts: the Sivakasi case",
      TW([B("In <strong>M.C. Mehta v. State of Tamil Nadu</strong> (Supreme Court, 10 December "
            "1996), a public interest petition under Article 32 concerned children in Sivakasi's "
            "match and fireworks factories. The Court chose to treat child labour as a "
            "national problem.", sm=True),
          P("green", "What the Court ordered",
            "Employers illegally employing children were to pay Rs 20,000 per child into a Child "
            "Labour Rehabilitation-cum-Welfare Fund, used only for that child. The government "
            "was to give an adult family member a job or contribute Rs 5,000 per child. "
            "Families offered jobs had a duty to send the child to school.")],
         [P("indigo", "Why it still matters",
            "The order tied a constitutional prohibition to money and to schooling. The 2016 "
            "amendment to the child labour law later created a Child and Adolescent Labour "
            "Rehabilitation Fund for every district (s. 14B): employers' fines go into it, the "
            "government adds Rs 15,000 for each child, and the money is paid to the child. It "
            "follows the same logic.")]),
      B("Source: CRIN Legal Library summary of M.C. Mehta v. State of Tamil Nadu (1996); Child "
        "Labour (Prohibition and Regulation) Amendment Act 2016 (No. 35 of 2016), s. 19, "
        "inserting s. 14B.", sm=True)),

    C("Reading rights together", "Courts build child rights out of Article 21",
      TW([B("The Supreme Court has repeatedly read Article 21 (the right to life and personal "
            "liberty) together with the directive principles and the CRC. Two recent examples "
            "show the method:", sm=True),
          P("cyan", "Independent Thought v. Union of India (2017)",
            "Decided 11 October 2017 by Justices Madan B. Lokur and Deepak Gupta. The Court held "
            "that sexual intercourse with a girl below eighteen is rape \"regardless of whether "
            "she is married or not\", removing the protection the marital exception in the "
            "Indian Penal Code gave husbands of girls aged 15 to 18.")],
         [P("green", "Society for Enlightenment and Voluntary Action v. Union of India (2024)",
            "Decided 18 October 2024, 2024 INSC 790. The Court held that child marriage infringes "
            "Article 21 and Article 21A, issued guidance on enforcing the 2006 Act, and said "
            "\"Parliament may consider outlawing child betrothals\". It stressed prevention: "
            "enforcement \"must not be solely focused on increasing prosecutions\".")]),
      H("amber", "The Bharatiya Nyaya Sanhita 2023, s. 63, Exception 2, now reads \"the wife not "
        "being under eighteen years of age\", writing the 2017 holding into the new penal code. "
        "Sources: legalauthority.in and Verdictum case reports; Bharatiya Nyaya Sanhita 2023 (Act "
        "45 of 2023), s. 63.")),

    C("Age thresholds", "Indian law has no single age of childhood",
      T(["Purpose", "Age", "Law"],
        [["Child for juvenile justice", "Under 18", "JJ Act 2015, s. 2(12)"],
         ["Child for sexual offences", "Under 18", "POCSO Act 2012, s. 2(1)(d)"],
         ["Child for personal data", "Under 18", "DPDP Act 2023, s. 2(f)"],
         ["Right to education", "6 to 14", "Article 21A; RTE Act 2009, s. 2(c)"],
         ["Early childhood care", "Under 6", "Article 45"],
         ["Child for labour law", "Under 14 (or the RTE age, if higher)", "Child and Adolescent "
          "Labour Act 1986, s. 2(ii), as amended 2016"],
         ["Adolescent for labour law", "14 to 18", "Same Act, s. 2(i)"],
         ["Child for marriage", "Female under 18; male under 21", "Prohibition of Child Marriage Act 2006, s. 2(a)"],
         ["No criminal liability", "Under 7; 7 to 12 if immature", "Bharatiya Nyaya Sanhita 2023, ss. 20 and 21"]]),
      H("cyan", "Check which definition a programme is working under. A fifteen-year-old domestic "
        "worker is a \"child\" under the JJ Act and POCSO, an \"adolescent\" under labour law, "
        "and outside the RTE Act's guarantee."), compact=True),
]

# ===================== SECTION 05 =====================
SLIDES += [
    D("05", "Section Five", "Juvenile justice: the JJ Act 2015"),

    C("Two doors", "One Act, two groups of children",
      TW([P("amber", "Child in conflict with law",
            "\"A child who is alleged or found to have committed an offence and who has not "
            "completed eighteen years of age on the date of commission of such offence\" "
            "(s. 2(13)). The deciding body is the Juvenile Justice Board, one or more in every "
            "district (s. 4)."),
          B("Age is fixed at the date of the offence, so a person arrested at nineteen for "
            "something done at seventeen is still dealt with under the Act.", sm=True)],
         [P("green", "Child in need of care and protection",
            "Twelve situations listed in s. 2(14), from a child without a home or found working "
            "or begging, to a child at \"imminent risk of marriage before attaining the age of "
            "marriage\". The deciding body is the Child Welfare Committee, one or more in every "
            "district (s. 27)."),
          B("A child can move between the doors: a working child picked up in a raid is a "
            "child in need of care, and must not be processed as an offender.", sm=True)]),
      H("cyan", "The Juvenile Justice (Care and Protection of Children) Act 2015 replaced the 2000 "
        "Act. It passed the Lok Sabha on 7 May 2015 and the Rajya Sabha on 22 December 2015 "
        "(PRS Legislative Research) and received assent on 31 December 2015 as Act No. 2 of 2016. "
        "Section numbers here are checked against that Act as published in the Gazette of India.")),

    C("Principles", "Sixteen principles in section 3 govern every decision",
      TW([BL(["Presumption of innocence up to eighteen",
              "Dignity and worth",
              "Participation: the right to be heard",
              "Best interest",
              "Family responsibility",
              "Safety",
              "Positive measures",
              "Non-stigmatising semantics"], color="cyan")],
         [BL(["Non-waiver of rights",
              "Equality and non-discrimination",
              "Right to privacy and confidentiality",
              "Institutionalisation as a measure of last resort",
              "Repatriation and restoration",
              "Fresh start",
              "Diversion",
              "Natural justice"], color="green")]),
      B("Section 3 says the Central Government, the State Governments, the Board \"and other "
        "agencies\" shall be guided by these principles while implementing the Act. That "
        "includes NGOs running homes, open shelters and helplines under the Act."),
      H("amber", "\"Non-stigmatising semantics\" is a working rule. Case files, "
        "reports and donor updates should not call children \"juvenile delinquents\", "
        "\"accused\" or \"rescued girls\".")),

    C("The Board", "Juvenile Justice Boards and what they can order",
      TW([P("indigo", "Composition (s. 4(2))",
            "A Metropolitan Magistrate or Judicial Magistrate of the First Class with at least "
            "three years' experience (the Principal Magistrate), and two social workers, at "
            "least one a woman, sitting as a Bench."),
          P("green", "Bail as the rule (s. 12(1))",
            "A child apprehended for a bailable or non-bailable offence \"shall\" be released on "
            "bail or placed under supervision, unless release would bring the child into "
            "association with a known criminal, expose the child to danger, or defeat the ends "
            "of justice.")],
         [P("cyan", "Orders after inquiry (s. 18(1))",
            "Advice or admonition; group counselling; community service; a fine; probation of "
            "good conduct with a parent, guardian or fit person; and at the far end, a special "
            "home for up to three years with education, skills and counselling."),
          P("red", "Sentences that are barred (s. 21)",
            "No child in conflict with law \"shall be sentenced to death or for life imprisonment "
            "without the possibility of release\", under this Act, the penal code or any other "
            "law. This mirrors CRC Article 37(a).")]),
      H("amber", "Offences are graded by maximum punishment: petty (up to three years, s. "
        "2(45)), serious (three to seven years, s. 2(54)), heinous (minimum seven years or more, "
        "s. 2(33)).")),

    C("Sixteen to eighteen", "The 2015 change: trying some sixteen-year-olds as adults",
      FLOW("Heinous offence alleged; child aged 16 or 17 at the time",
           "Board conducts a preliminary assessment of mental and physical capacity, understanding of consequences, and circumstances (s. 15(1))",
           "If trial as an adult is needed, Board transfers the case to the Children's Court (s. 18(3))",
           "Children's Court decides afresh: try as an adult under the CrPC, or inquire as a Board (s. 19(1))",
           "Even if tried as an adult: no death sentence, no life without release (s. 21)"),
      TW([B("This was the most contested part of the 2015 Act. Under the 2000 Act every person "
            "under eighteen at the time of the offence was dealt with as a child. PRS noted that "
            "the Standing Committee examining the Bill \"observed that the Bill was based on "
            "misleading data regarding juvenile crimes\".", sm=True)],
         [H("red", "Set against the CRC: General comment No. 24 (2019), para. 30, recommends that "
            "states which \"allow by way of exception that certain children are treated as adult "
            "offenders (for example, because of the offence category)\" change their laws so "
            "the child justice system applies fully to everyone below eighteen at the time of "
            "the offence.")]),
      B("Sources: JJ Act 2015 ss. 15, 18, 19, 21 (Act No. 2 of 2016, Gazette of India); PRS bill page; CRC/C/GC/24, paras. 29-30.",
        sm=True), compact=True),

    C("Care and protection", "Child Welfare Committees decide for children in need of care",
      TW([P("green", "Composition (s. 27(2))",
            "A Chairperson and four other members, at least one a woman and another an expert "
            "on matters concerning children. The District Child Protection Unit provides the "
            "secretary and staff (s. 27(3))."),
          P("cyan", "What a Committee decides",
            "Whether a child brought before it needs care and protection, where the child should "
            "live in the meantime, whether to restore the child to family, place the child in "
            "family-based care or an institution, or declare the child legally free for adoption.")],
         [P("indigo", "Who brings a child",
            "Section 31(1) lists police and labour inspectors, any public servant, Childline "
            "services or a recognised NGO, a probation officer, \"any social worker or a public "
            "spirited citizen\", the child, and any nurse, doctor or hospital. The child must "
            "be produced within twenty-four hours, excluding travel time."),
          P("amber", "A common failure",
            "Children kept for months in a home \"pending inquiry\" because the Committee sits "
            "rarely, files are incomplete, or no one traces the family. Delay is a decision, and "
            "it is usually the institution's.")]),
      H("cyan", "When a programme finds a child at risk, the Committee is the statutory route. "
        "Informal \"placement\" with a relative or a hostel without a Committee order leaves the "
        "child outside the Act's safeguards.")),

    C("The care ladder", "Family first, institution last",
      T(["Option", "What it is", "When it fits"],
        [["Restoration to family", "Return to parents or guardian, with follow-up", "The default, "
          "once the risk is addressed"],
         ["Sponsorship", "Financial support so a child can stay with family", "Poverty is the "
          "main reason for separation"],
         ["Family-based alternative care", "Placement with another family under a Committee "
          "order", "Family unsafe or unavailable; child needs a home "
          "now"],
         ["Adoption", "Permanent legal transfer of parenthood", "Child declared legally free; "
          "CRC Article 21 makes best interests \"the paramount consideration\""],
         ["Child care institution", "Children's home, open shelter, specialised adoption agency",
          "Short term or where no family option exists"],
         ["After care", "Support after leaving an institution at eighteen", "Transition to "
          "adult life"]]),
      H("amber", "Section 3(xii) of the JJ Act makes institutionalisation \"a measure of last "
        "resort\". Mission Vatsalya's components include institutional care and "
        "\"non-institutional community-based care\", with sponsorship as one route (PIB "
        "explainer, 11 August 2023)."), compact=True),

    C("The 2021 amendment", "What changed in 2021",
      TW([P("cyan", "Adoption orders move to the District Magistrate",
            "Under the 2015 Act a civil court issued the final adoption order. The 2021 "
            "amendment gives that power to the District Magistrate, including an Additional "
            "District Magistrate. The Statement of Objects and Reasons cited delay in courts "
            "(PRS Legislative Research)."),
          P("green", "\"Serious offences\" widened",
            "The amendment adds to serious offences those with a maximum punishment above seven "
            "years where no minimum, or a minimum under seven years, is prescribed. These were "
            "previously unclassified.")],
         [P("amber", "Issues PRS raised",
            "Whether an administrative officer should make an order creating a permanent legal "
            "relationship; whether 629 pending adoption cases (July 2018) justified the shift; "
            "and that in 2019 only 17 of 35 states and union territories had all the bodies the "
            "Act requires in every district."),
          B("Passage: Lok Sabha 24 March 2021, Rajya Sabha 28 July 2021 (PRS bill track). A "
            "similar 2018 Bill lapsed with the 16th Lok Sabha.", sm=True)]),
      H("cyan", "The infrastructure gap is the practical point. A right to a Child Welfare "
        "Committee is empty in a district that does not have one sitting regularly.")),

    C("Offences against children", "The JJ Act also punishes adults",
      T(["Section", "Conduct", "Maximum punishment"],
        [["74", "Media disclosure of the name, address, school or any detail that could "
          "identify a child in conflict with law, a child in need of care, or a child victim or "
          "witness", "Six months, or fine up to two lakh rupees, or both (s. 74(3))"],
         ["75", "Cruelty by a person in charge of a child: assault, abandonment, abuse, "
          "exposure or wilful neglect likely to cause unnecessary suffering", "Three years, or "
          "fine of one lakh rupees, or both"],
         ["76", "Employing or using a child for begging", "Five years and fine of one lakh rupees"],
         ["79", "Keeping a child in bondage for employment, or withholding the child's "
          "earnings; \"employment\" includes selling goods and services and entertainment in "
          "public places", "Rigorous imprisonment up to five years and fine of one lakh rupees"]]),
      H("red", "Section 74 binds NGOs as much as newspapers. A case study, a photograph on a "
        "fundraising page or a donor report that lets a reader identify a child in the "
        "system breaks the law. The Safeguarding and PSEA 101 deck covers image consent."),
      compact=True),
]

# ===================== SECTION 06 =====================
SLIDES += [
    D("06", "Section Six", "Sexual offences: the POCSO Act 2012"),

    C("The Act", "A gender-neutral law for every person under eighteen",
      ST([CARD("< 18", "a child is \"any person below the age of eighteen years\"", "cyan",
               "POCSO Act 2012, s. 2(1)(d)"),
          CARD("69,191", "POCSO cases registered in India in 2024, 36.9% of crimes against "
               "children (67,694 in 2023)", "red",
               "NCRB, Crime in India 2024, Vol. I; 2023 figure from Crime in India 2023 via PTI"),
          CARD("14 Nov 2012", "date the Act came into force", "indigo",
               "Notification S.O. 2705(E), noted in the Act's text")]),
      TW([B("The Protection of Children from Sexual Offences Act passed the Rajya Sabha on 10 May "
            "2012 and the Lok Sabha on 22 May 2012 (PRS). It defines offences without reference "
            "to the sex of victim or offender, so boys are protected on the same terms as girls.",
            sm=True)],
         [B("It combines three things the penal code had not: a graded set of offences, "
            "child-friendly procedure at every stage from complaint to trial, and a duty on "
            "everyone to report. Sections cited below are from the Act as amended in 2019.",
            sm=True)])),

    C("Offences", "Four graded offences, each with an aggravated form",
      T(["Offence", "Defined in", "Punishment (as amended 2019)"],
        [["Penetrative sexual assault", "s. 3", "s. 4: at least 10 years up to life, and fine; "
          "at least 20 years up to life for a child below 16"],
         ["Aggravated penetrative sexual assault", "s. 5 (by police, armed forces, public "
          "servants, relatives, staff of institutions, and other listed cases)", "s. 6: at least "
          "20 years up to life for the remainder of natural life, and fine, or death"],
         ["Sexual assault (touch with sexual intent, no penetration)", "s. 7", "s. 8"],
         ["Aggravated sexual assault", "s. 9", "s. 10"],
         ["Sexual harassment (words, gestures, showing material, stalking)", "s. 11", "s. 12"],
         ["Using a child for pornographic purposes; storing such material", "ss. 13 to 15", "ss. 14 and 15"]]),
      H("amber", "The aggravated forms matter for development workers: an offence by staff of an "
        "institution or a person in a position of trust is aggravated. The 2019 amendment added "
        "causing the death of the child, and offences \"during any natural calamity\", as "
        "aggravating grounds (Act 25 of 2019, s. 4, in force 16 August 2019)."), compact=True),

    C("Reporting", "Section 19: everyone must report",
      Q("any person (including the child), who has apprehension that an offence under this Act "
        "is likely to be committed or has knowledge that such an offence has been committed, he "
        "shall provide such information to,-- (a) the Special Juvenile Police Unit; or (b) the "
        "local police.", "POCSO Act 2012, s. 19(1)"),
      TW([P("red", "Failing to report (s. 21)",
            "Up to six months, or fine, or both, for any person who fails to report. A person "
            "in charge of a company or institution who fails to report an offence by a "
            "subordinate: up to one year and fine (s. 21(2)). A child cannot be punished for "
            "not reporting (s. 21(3))."),
          P("green", "Protection for reporters",
            "\"No person shall incur any liability, whether civil or criminal, for giving the "
            "information in good faith\" (s. 19(7)).")],
         [P("amber", "The hard cases",
            "Mandatory reporting overrides confidentiality. A counsellor, a doctor treating a "
            "pregnant sixteen-year-old, or a researcher who hears a disclosure is bound. "
            "Adolescents may then avoid health services. Programmes must tell young people, "
            "before they disclose, what the worker will have to do.")]),
      H("cyan", "Every organisation working with children needs a written POCSO reporting "
        "procedure: who reports, to which police station, within what time, and how the child "
        "is supported.")),

    C("Child-friendly procedure", "The trial is designed around the child",
      TW([BL(["<strong>s. 24:</strong> statement recorded at the child's home or a place of "
              "the child's choice, by a woman officer not below sub-inspector where practicable, "
              "not in uniform",
              "<strong>s. 28:</strong> a Court of Session designated as a Special Court in "
              "each district",
              "<strong>s. 29:</strong> for offences under ss. 3, 5, 7 and 9, the court presumes "
              "the accused committed the offence unless the contrary is proved"], color="cyan")],
         [BL(["<strong>s. 35:</strong> the child's evidence recorded within thirty days of "
              "cognizance; trial completed within one year as far as possible",
              "<strong>s. 36:</strong> the child not exposed to the accused while testifying: "
              "video link, one-way mirror or curtain",
              "<strong>s. 44:</strong> NCPCR and the state commissions monitor implementation"],
             color="green")]),
      H("amber", "Within twenty-four hours of a report, the police must inform the Child Welfare "
        "Committee and the Special Court, including whether the child needs care and protection "
        "(s. 19(6)). Track every statutory timeline in the case file: thirty days for evidence "
        "and one year for trial are targets that slip without someone watching."),
      B("Source: POCSO Act 2012 as amended, bare text on bnblegal.com.", sm=True)),

    C("The 2019 amendment", "Harsher minimums, a definition, and a death penalty",
      TW([P("red", "What the Protection of Children from Sexual Offences (Amendment) Act 2019 did",
            "Raised the minimum for penetrative sexual assault from seven to ten years, and to "
            "twenty for a child below sixteen. Raised the minimum for aggravated penetrative "
            "sexual assault from ten to twenty years and added death as a possible sentence. "
            "Inserted a definition of child pornography (s. 2(1)(da)). Act 25 of 2019, in force "
            "from 16 August 2019.")],
         [P("amber", "The debate",
            "Child rights groups warned that a death penalty for offences mostly committed by "
            "family members and acquaintances could deter reporting, because families may not "
            "want a relative executed. The Act's own list of aggravated offences (relatives, "
            "staff of institutions, persons in positions of trust) shows how often the offender "
            "is someone the child knows. Harsher sentences also raise the stakes in adolescent "
            "relationship cases (next slide).")]),
      H("cyan", "For practitioners, the amendment changes little in daily work: the reporting "
        "duty, procedures and support duties are the same. It matters for how families weigh "
        "the decision to go to the police."),
      B("Sources: PRS bill summary of the 2019 Bill; Act text with amendment notes (bnblegal.com).",
        sm=True)),

    C("Adolescents", "When both people are under eighteen, or close to it",
      TW([B("POCSO treats any sexual act with a person under eighteen as an offence, whatever "
            "the child says. So a consensual relationship between a seventeen-year-old and a "
            "nineteen-year-old can lead to a charge of penetrative sexual assault, often filed "
            "by the girl's family after an elopement.", sm=True),
          P("indigo", "Law Commission, 283rd Report (27 September 2023)",
            "Recommended keeping the age of consent at eighteen, saying \"an outright reduction "
            "in age of consent will open a Pandora's Box\". It proposed \"guided judicial "
            "discretion\" in sentencing for children aged sixteen to eighteen where there is "
            "\"tacit approval of the child, though not consent in law\", subject to conditions "
            "such as an age gap under three years and no coercion.")],
         [H("amber", "As of October 2026 this remains a recommendation; the Act has not been "
            "amended to adopt it. Source: The Leaflet's report on the Law Commission's 283rd "
            "Report."),
          P("green", "What a programme can do",
            "Offer sexual and reproductive health information without waiting for a crisis; "
            "explain the reporting duty plainly; connect families to legal aid; and avoid "
            "becoming the instrument of a family's complaint against a daughter's partner.")]),
      H("cyan", "The SRHR Basics 101 deck covers adolescent sexual and reproductive health "
        "services in more depth.")),

    C("Online abuse", "Child sexual exploitation and abuse material",
      TW([P("cyan", "Just Rights for Children Alliance v. S. Harish (2024)",
            "Decided 23 September 2024. The Madras High Court had quashed a case "
            "against a man who downloaded and watched such material. The Supreme Court restored "
            "it, holding that viewing and storing can fall within s. 15 of POCSO read with s. "
            "67B of the IT Act. It treated even accessing material online as a form of "
            "possession, and told courts to use the term \"child sexual exploitation and abuse "
            "material\" (CSEAM)."),
          B("Source: Bar and Bench analysis, and Casemine commentary, of the judgment.", sm=True)],
         [P("amber", "Section 15 as amended in 2019",
            "s. 15(1): storing or possessing such material and failing to delete, destroy or "
            "report it, with intent to share; s. 15(2): storing for transmission or "
            "distribution; s. 15(3): storing for commercial purposes."),
          P("green", "For organisations",
            "Never forward suspected material, even to report it; that is itself transmission. "
            "Note the URL and report to the police or the National Cyber Crime Reporting Portal "
            "(cybercrime.gov.in).")]),
      H("red", "The terminology point is practical: \"pornography\" suggests consent and a "
        "commercial product. CSEAM names the abuse.")),

    C("After a disclosure", "Support for the child is part of the legal process",
      FLOW("Child or adult discloses",
           "Report to police or Special Juvenile Police Unit (s. 19)",
           "Police inform the Child Welfare Committee and Special Court within 24 hours (s. 19(6))",
           "Committee decides whether the child needs care and protection",
           "Special Court trial with child-friendly procedure",
           "Compensation and rehabilitation"),
      TW([B("The Ministry of Women and Child Development runs a \"Scheme for Care and Support to "
            "Victims under Section 4 and 6 of the Protection of Children from Sexual Offences "
            "(POCSO) Act, 2012\", listed on its Mission Vatsalya page alongside the Child "
            "Helpline 1098 and PM CARES for Children.", sm=True)],
         [H("amber", "The weak point is often between the report and the trial: the case is filed, and "
            "the child can wait months with no counselling, schooling support or legal aid. "
            "That is where a support organisation is most useful.")]),
      B("Source: Ministry of Women and Child Development, Mission Vatsalya page (wcd.gov.in), "
        "viewed October 2026.", sm=True)),
]

# ===================== SECTION 07 =====================
SLIDES += [
    D("07", "Section Seven", "Education and child labour"),

    C("The RTE Act", "The Right of Children to Free and Compulsory Education Act 2009",
      TW([TERM("Free and compulsory",
               "\"Free\" means no fee, charge or expense that would stop a child from completing "
               "elementary education. \"Compulsory\" puts the duty on the appropriate government "
               "and local authority to ensure admission, attendance and completion (Ministry of Education RTE note, reproduced by Accountability "
               "Initiative)."),
          BL(["<strong>s. 2(c):</strong> a child is \"a male or female child of the age of six "
              "to fourteen years\"",
              "<strong>s. 3(1):</strong> every such child has the right to free and compulsory "
              "education \"in a neighbourhood School\"",
              "<strong>s. 4:</strong> an older child who was never admitted is placed in an "
              "age-appropriate class with special training"], color="cyan")],
         [BL(["<strong>s. 13(1):</strong> no capitation fee and no screening of the child or "
              "parents at admission",
              "<strong>s. 17:</strong> \"No child shall be subjected to physical punishment or "
              "mental harassment\"",
              "<strong>s. 21(1):</strong> every school has a School Management Committee, at "
              "least three-fourths of whose members are parents or guardians",
              "<strong>s. 25(1):</strong> pupil-teacher ratios as specified in the Schedule",
              "<strong>s. 32(1):</strong> grievances go to the local authority"], color="green")]),
      H("amber", "Section text from the Kerala government's Panchayat Wiki copy of Act 35 of 2009 "
        "as amended by Act 30 of 2012. The Act gives Article 21A its content, so every one of "
        "these is a constitutional entitlement for a child aged six to fourteen.")),

    C("Section 12(1)(c)", "A quarter of the seats in private schools",
      TW([Q("admit in class I, to the extent of at least twenty-five per cent of the strength of "
            "that class, children belonging to weaker section and disadvantaged group",
            "RTE Act 2009, s. 12(1)(c)"),
          B("It applies to unaided schools and \"specified category\" schools. Aided schools "
            "have a separate duty in s. 12(1)(b). The state reimburses unaided schools \"to the "
            "extent of per-child-expenditure incurred by the State, or the actual amount charged "
            "from the child, whichever is less\" (s. 12(2)).", sm=True)],
         [P("indigo", "Who qualifies",
            "A \"child belonging to disadvantaged group\" faces barriers by \"social, cultural, "
            "economical, geographical, linguistic, gender or such other factor\" as the "
            "government notifies (s. 2(d)). A \"child belonging to weaker section\" has parents "
            "whose income is below a notified limit (s. 2(e)). States write their own lists."),
          P("amber", "Where it goes wrong",
            "Online lotteries that families without documents cannot enter; reimbursement paid "
            "late, so schools resist; children admitted and then made to feel unwelcome through "
            "fees for uniforms, books and trips. Programmes that help families apply, and then "
            "stay in touch for the first year, change outcomes.")]),
      H("cyan", "This provision places a duty on private schools to include poor and "
        "disadvantaged children in the same classrooms as fee-paying children. Its value depends "
        "on states notifying the categories, funding reimbursement on time and checking that "
        "admitted children stay.")),

    C("Holding back", "The no-detention rule and its 2019 replacement",
      TW([P("cyan", "Section 16 as enacted in 2009",
            "\"No child admitted in a school shall be held back in any class or expelled from "
            "School till the completion of elementary education.\" The idea was that failure is "
            "the school's, and holding a child back pushes the child out."),
          P("amber", "The Right of Children to Free and Compulsory Education (Amendment) Act 2019",
            "Assent 10 January 2019. Substituted s. 16: a \"regular examination in the fifth "
            "class and in the eighth class at the end of every academic year\"; a child who "
            "fails gets additional instruction and a re-examination within two months; the "
            "appropriate government \"may allow schools to hold back a child\" who fails again.")],
         [P("green", "What stayed",
            "The new s. 16(4): \"No child shall be expelled from a school till the completion of "
            "elementary education.\" And a proviso lets a state decide not to hold back any "
            "child at all, so the rule now differs by state."),
          H("red", "For practitioners: in states that adopted detention, a child held back in "
            "class five is at higher risk of dropping out and starting work. Watch the "
            "re-examination window: two months of remedial support is the protection the law "
            "promises.")]),
      B("Source: Gazette of India, Act No. 1 of 2019, via PRS Legislative Research.", sm=True)),

    C("Corporal punishment", "Physical punishment is banned, and still common",
      TW([B("Section 17(1) of the RTE Act is absolute: \"No child shall be subjected to physical "
            "punishment or mental harassment.\" Section 17(2) makes a contravention a matter "
            "for disciplinary action under the service rules that apply to the teacher.", sm=True),
          B("The JJ Act 2015 adds a criminal route: s. 82 punishes corporal punishment \"with "
            "the aim of disciplining the child\" in a child care institution (a fine of ten "
            "thousand rupees on first conviction), and s. 75 punishes cruelty by anyone in "
            "charge of a child. "
            "CRC Article 28(2) requires school discipline consistent with the child's dignity.",
            sm=True)],
         [P("amber", "Why a ban alone does little",
            "Many teachers believe they are only disciplining the child, and many parents "
            "agree. A complaint against a teacher can cost a child more than the beating did. "
            "Programmes that train teachers in alternatives (the SEL Basics 101 deck) and set up "
            "a safe complaint route reach further than circulars."),
          P("green", "Nepal goes further",
            "Nepal's Act relating to Children 2018 gives every child the right to protection "
            "against physical or mental violence by a \"father, mother, other family member or "
            "guardian, teacher\" and others. The prohibition covers the home.")]),
      H("cyan", "Section 82 of the JJ Act covers staff of a child care institution only. A "
        "beating at school goes through RTE s. 17 and, where the facts fit, the cruelty "
        "offence in JJ s. 75.")),

    C("Child labour law", "The 2016 amendment: a ban below fourteen, with exceptions",
      T(["Group", "Rule", "Section"],
        [["Child: under 14 (or the RTE age, if higher)", "\"No child shall be employed or "
          "permitted to work in any occupation or process\"", "s. 3(1)"],
         ["Exception 1: family enterprise", "A child may help \"his family or family "
          "enterprise\", outside the hazardous list, \"after his school hours or during vacations\"",
          "s. 3(2)(a)"],
         ["Exception 2: artist", "A child may work as an artist in audio-visual entertainment "
          "or sports, except the circus, without affecting school education", "s. 3(2)(b)"],
         ["Adolescent: 14 to 18", "Not to be employed in the hazardous occupations and processes "
          "in the Schedule", "s. 3A"],
         ["The Schedule (2016)", "Mines; inflammable substances or explosives; hazardous "
          "processes as defined in the Factories Act 1948", "Schedule"],
         ["Penalty", "Six months to two years, or Rs 20,000 to Rs 50,000, or both; parents "
          "not punished unless they permit work for commercial purposes", "s. 14"]]),
      B("Source: Child Labour (Prohibition and Regulation) Amendment Act 2016 (No. 35 of 2016, "
        "assent 29 July 2016, Gazette of India), in force from 1 September 2016 (S.O. 2823(E)). "
        "The Act was renamed the Child and Adolescent Labour (Prohibition and Regulation) Act "
        "1986.", sm=True), compact=True),

    C("The family exception", "Why the family enterprise exception is contested",
      TW([P("amber", "How the law defines it",
            "\"Family\" means the child's \"mother, father, brother, sister and father's sister "
            "and brother and mother's sister and brother\". \"Family enterprise\" means work "
            "performed by family members \"with the engagement of other persons\" (s. 3, "
            "Explanation). So an uncle's workshop that employs outsiders counts."),
          P("red", "The objection",
            "Much child labour in South Asia already happens inside households and small family "
            "units: home-based garment work, agriculture, small shops. Critics argued that the "
            "exception could legalise the forms that are hardest to inspect, and that \"after "
            "school hours\" is impossible to verify.")],
         [P("green", "The defence",
            "Supporters argued that children helping parents is part of family life and skill "
            "transmission, and that a total ban would be ignored and would criminalise poor "
            "parents. The proviso to s. 14 reflects this: parents are not punished unless they "
            "permit work for commercial purposes."),
          H("cyan", "The practical test for a programme: is the child attending school "
            "regularly and learning? If not, the work is interfering with education whatever "
            "the legal category, and CRC Article 32(1) applies.")]),
      B("Definitions quoted from the Child Labour (Prohibition and Regulation) Amendment Act 2016 (No. 35 of 2016), s. 5.",
        sm=True)),

    C("Scale", "How many children work",
      ST([CARD("10.1 million", "children aged 5 to 14 working in India, 3.9% of the age group",
               "amber", "Census 2011, cited in ILO fact sheet on child labour in India"),
          CARD("138 million", "children in child labour worldwide in 2024", "red",
               "ILO and UNICEF, Child Labour: Global estimates 2024 (June 2025)"),
          CARD("28 million", "in Asia and the Pacific, down from 49 million in 2020", "green",
               "ILO and UNICEF, press release, 11 June 2025")]),
      TW([B("The Census figure counts main and marginal workers aged five to fourteen. It is "
            "fifteen years old: the next Census, with reference date 1 March 2027, will be the "
            "first new national count since. The ILO notes that child labour in India fell by "
            "2.6 million between 2001 and 2011.", sm=True)],
         [H("amber", "Globally, ILO and UNICEF report around 54 million children in hazardous "
            "work, and agriculture accounts for 61 per cent of child labour. The world missed "
            "the target of eliminating child labour by 2025.")])),

    C("Rescue and after", "Removing a child from work is the start of the job",
      FLOW("Inspection or rescue: labour inspector, police or helpline",
           "Child produced before the Child Welfare Committee as a child in need of care (JJ Act s. 2(14)(ii))",
           "Age determined; statement recorded; employer prosecuted (s. 14 of the 1986 Act; JJ Act s. 79 if bonded)",
           "Rehabilitation fund: employer's fine credited to the district Child and Adolescent Labour Rehabilitation Fund (s. 14B)",
           "Restoration with family, school admission under the RTE Act, follow-up"),
      TW([B("Rescue operations are visible and countable, so they are often what programmes "
            "report. The outcome that matters is whether the child is in school and not working "
            "a year later.", sm=True)],
         [H("red", "A child returned to a family in debt, with no income support and no school "
            "place, faces the same pressures that sent the child to work. Pair every rescue with a "
            "named person responsible for follow-up.")]),
      B("Sources: JJ Act 2015 ss. 2(14), 79; Child and Adolescent Labour Act 1986 ss. 14, 14B, as amended by Act 35 of 2016.",
        sm=True)),

    C("Education and labour together", "One child, two laws, one test",
      T(["Age", "Education law", "Labour law", "What a programme checks"],
        [["Under 6", "Article 45: early childhood care, a directive principle", "Covered by the "
          "child labour ban (any work)", "Enrolment in an anganwadi; nutrition; registration"],
         ["6 to 14", "Article 21A and RTE Act: free and compulsory education", "Banned except "
          "family enterprise after school, and artists", "Attendance and learning; hours of "
          "work at home"],
         ["14 to 18", "No statutory right to free education under the RTE Act", "Allowed except "
          "hazardous Schedule work", "Secondary enrolment; safety at work; wage and hours"]]),
      H("amber", "The gap at fourteen is the weak point. A child who finishes class eight at "
        "fourteen loses the RTE Act's guarantee in the same year that the labour law first "
        "allows non-hazardous work. Programmes should track that transition by name."),
      compact=True),
]

# ===================== SECTION 08 =====================
SLIDES += [
    D("08", "Section Eight", "Child marriage"),

    C("The law", "The Prohibition of Child Marriage Act 2006",
      TW([TERM("Child, for this Act",
               "\"a person who, if a male, has not completed twenty-one years of age, and if a "
               "female, has not completed eighteen years of age\" (s. 2(a)). A child marriage is "
               "one in which either party is a child (s. 2(b))."),
          P("cyan", "Status of the marriage",
            "Voidable \"at the option of the contracting party who was a child at the time of "
            "the marriage\" (s. 3(1)), by petition before the child \"completes two years of "
            "attaining majority\" (s. 3(3)). Void in cases of enticement, force, deceit or sale "
            "(s. 12), and void ab initio if solemnised against an injunction (s. 14).")],
         [P("red", "Offences",
            "A male adult above eighteen who contracts a child marriage (s. 9); whoever "
            "performs, conducts, directs or abets one (s. 10); a parent, guardian or any person "
            "who promotes or permits it (s. 11). Each carries rigorous imprisonment up to two "
            "years and a fine up to one lakh rupees, and \"no woman shall be punishable with "
            "imprisonment\" under s. 11. Offences are cognizable and non-bailable (s. 15)."),
          P("green", "Protection for the girl",
            "Maintenance and residence for the female party (s. 4); custody and maintenance of "
            "children (s. 5); children of an annulled child marriage are legitimate (s. 6).")]),
      B("Source: text of Act 6 of 2007 (PRS Legislative Research).", sm=True)),

    C("A long history", "Ninety years of raising the age",
      FLOW("1929: Child Marriage Restraint Act sets 14 for girls and 18 for boys",
           "1978: amendment raises the ages to 18 for women and 21 for men",
           "2006: Prohibition of Child Marriage Act replaces the 1929 Act, same ages",
           "Dec 2021: Prohibition of Child Marriage (Amendment) Bill would raise women's age to 21",
           "June 2024: the Bill lapses with the dissolution of the 17th Lok Sabha"),
      TW([B("The 2021 Bill followed a task force chaired by Jaya Jaitly, set up in June 2020 to "
            "examine age at marriage and motherhood against maternal and child health. It would "
            "also have let a person apply for annulment up to five years after majority and "
            "overridden \"any other law, custom, or practice\" (PRS Legislative Research).",
            sm=True)],
         [H("amber", "PRS asked whether a higher legal age would work when \"about a quarter of "
            "20-24 year old women are married before the age of 18 years, despite that being "
            "the minimum age of marriage since 1978\". The Bill lapsed after being referred to "
            "the Standing Committee (PTI report, 8 June 2024).")]),
      B("As of October 2026 the minimum ages remain 18 for women and 21 for men under the 2006 Act.",
        sm=True)),

    C("The trend", "Marriage before 18 is falling across South Asia, at different speeds",
      {"t": "chart", "canvas": "crMarriageChart", "type": "line",
       "title": "Women aged 20-24 first married by age 18 (%)",
       "source": "DHS surveys via the DHS Program API, indicator MA_MBAY_W_B18; India = NFHS",
       "data": {"labels": ["1992-94", "1996-2001", "2004-07", "2011-13", "2014-17", "2019-22"],
                "datasets": [
                    {"label": "Bangladesh", "data": [73.3, 65.3, 66.2, 64.9, 58.9, 50.7],
                     "borderColor": "#EF4444", "backgroundColor": "#EF4444", "tension": 0.2},
                    {"label": "Nepal", "data": [None, 56.1, 51.4, 40.7, 39.5, 34.9],
                     "borderColor": "#F59E0B", "backgroundColor": "#F59E0B", "tension": 0.2},
                    {"label": "India", "data": [50.2, 50.0, 44.5, None, 25.3, 22.3],
                     "borderColor": "#0EA5E9", "backgroundColor": "#0EA5E9", "tension": 0.2,
                     "spanGaps": True},
                    {"label": "Pakistan", "data": [31.6, None, 24.0, 21.0, 18.3, None],
                     "borderColor": "#6366F1", "backgroundColor": "#6366F1", "tension": 0.2,
                     "spanGaps": True}]},
       "options": {"__js__": "{ spanGaps:true, scales:{ y:{ min:0, max:80, title:{display:true,text:'%'} } } }"}},
      B("Survey rounds are grouped into periods for display: India 1992-93, 1998-99, 2005-06, "
        "2015-16, 2019-21; Bangladesh 1993-94, 1999-2000, 2007, 2011, 2017-18, 2022; Nepal 2001, "
        "2006, 2011, 2016, 2022; Pakistan 1990-91, 2006-07, 2012-13, 2017-18. The NFHS-5 fact "
        "sheet's own headline figure for India is about 23 per cent (PRS).", sm=True),
      compact=True),

    C("Who marries early", "Inside India, the gradient is steep",
      TW([{"t": "chart", "canvas": "crWealthChart", "type": "bar",
           "title": "Women 20-24 married by 18, by wealth quintile, India (%)",
           "source": DHS,
           "data": {"labels": ["Poorest", "Second", "Middle", "Fourth", "Richest"],
                    "datasets": [{"label": "%", "data": [38.3, 29.5, 22.2, 15.3, 7.2],
                                  "backgroundColor": "#0EA5E9"}]},
           "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:50 } } }"}}],
         [T(["Group", "% married by 18"],
            [["Rural", "25.8"], ["Urban", "14.2"], ["No schooling", "45.9"],
             ["Secondary schooling", "26.9"], ["West Bengal", "41.5"], ["Bihar", "38.7"],
             ["Kerala", "6.3"], ["Punjab", "8.7"]]),
          B("Source: " + DHS + ". State and group values as tabulated by the DHS Program; "
            "state fact sheets may differ slightly.", sm=True)]),
      H("amber", "The DHS tabulation shows steep gradients by wealth, schooling, residence and "
        "state: the poorest quintile is more than five times as likely as the richest to marry "
        "girls before eighteen. These are associations and do not show causes; they still tell "
        "a programme where to look first."), compact=True),

    C("Prevention tools", "The law gives practitioners tools before the wedding",
      T(["Tool", "Who uses it", "Section"],
        [["Complaint for an injunction to stop a marriage", "Any person with knowledge, or an "
          "NGO with reasonable information, to a Judicial Magistrate", "PCMA s. 13(1)-(2)"],
         ["Interim injunction without notice in urgency", "The court", "s. 13(6), proviso"],
         ["Suo motu action on reliable reports", "The court", "s. 13(3)"],
         ["Prevention on mass-marriage days such as Akshaya Trutiya", "District Magistrate, "
          "deemed a Child Marriage Prohibition Officer", "s. 13(4)-(5)"],
         ["Disobeying an injunction", "Up to two years, or fine up to one lakh rupees, or both",
          "s. 13(10)"],
         ["Child at imminent risk of marriage brought before the Child Welfare Committee",
          "Anyone listed in JJ Act s. 31", "JJ Act s. 2(14)(xii)"]]),
      H("green", "Child Marriage Prohibition Officers must \"prevent solemnisation of child "
        "marriages by taking such action as he may deem fit\" (s. 16(3)(a)). Find out who the "
        "officer is in your district before you need one."), compact=True),

    C("The Supreme Court in 2024", "Prevention over prosecution",
      TW([P("cyan", "Society for Enlightenment and Voluntary Action v. Union of India",
            "Supreme Court, 18 October 2024, 2024 INSC 790; Chief Justice D.Y. Chandrachud, "
            "Justices J.B. Pardiwala and Manoj Misra. The petition under Article 32 alleged that "
            "authorities were failing to prevent child marriages and to appoint Child Marriage "
            "Prohibition Officers."),
          Q("The aim of the law enforcement machinery must not be solely focused on increasing "
            "prosecutions without making the best efforts to prevent and prohibit child "
            "marriage.", "Society for Enlightenment and Voluntary Action v. UoI (2024), as reported by Verdictum")],
         [P("amber", "Betrothals",
            "The Court said \"Parliament may consider outlawing child betrothals which may be "
            "used to evade penalty under the PCMA\". A betrothal arranged at twelve and "
            "solemnised at eighteen falls outside the 2006 Act."),
          P("green", "For programmes",
            "The judgment supports community-level prevention: awareness, school retention, "
            "support to girls who refuse, and functioning prohibition officers. It is a "
            "reference point in any advocacy with district administrations.")]),
      H("red", "Prosecution can still harm the girl the law protects: a father jailed, a family "
        "income lost, a girl blamed. Weigh the child's best interests before pressing charges.")),

    C("Marriage and other laws", "Where child marriage meets criminal and personal law",
      TW([P("indigo", "Sexual offences",
            "Since Independent Thought v. Union of India (11 October 2017), sexual intercourse "
            "with a wife under eighteen is rape. The Bharatiya Nyaya Sanhita 2023, s. 63, "
            "Exception 2, writes the age of eighteen into the marital exception. POCSO applies "
            "regardless of marriage."),
          P("cyan", "Juvenile justice",
            "A girl at imminent risk of marriage is a child in need of care and protection (JJ "
            "Act s. 2(14)(xii)). She can be placed in safety by a Child Welfare Committee order "
            "while the injunction is sought.")],
         [P("amber", "Personal law",
            "Personal laws do not all use the 2006 Act's ages. The 2021 Bill would have made the "
            "Act override \"any other law, custom, or practice\" (PRS), which shows how the "
            "question was seen by Parliament. With the Bill lapsed, take legal advice on the "
            "interaction in a specific case."),
          P("green", "Registration",
            "A birth certificate is the best evidence of age. Since 1 October 2023 the "
            "Registration of Births and Deaths (Amendment) Act 2023 makes birth certificates "
            "the proof of date of birth for admission to an educational institution and other "
            "purposes (PRS bill summary). Registration makes age verifiable when a marriage is "
            "being arranged.")]),
      H("cyan", "A further amendment tightening delayed registration of births and deaths came "
        "into force on 1 October 2026 (PTI, 16 September 2026).")),
]

# ===================== SECTION 09 =====================
SLIDES += [
    D("09", "Section Nine", "Institutions and schemes"),

    C("NCPCR", "The Commissions for Protection of Child Rights Act 2005",
      TW([P("cyan", "Composition (s. 3)",
            "A Chairperson \"who is a person of eminence and has done outstanding work for "
            "promoting the welfare of children\", and six members, at least two of them women, "
            "drawn from education; child health, care, welfare or development; juvenile justice "
            "or care of neglected, marginalised or disabled children; elimination of child "
            "labour; child psychology or sociology; and laws relating to children."),
          P("indigo", "State commissions (s. 17)",
            "Each state may constitute a State Commission for Protection of Child Rights with "
            "parallel functions. Check whether your state's commission has a full bench: "
            "vacancies leave complaints unheard.")],
         [P("green", "Functions (s. 13) and powers (s. 14)",
            "Review legal safeguards; report annually; inquire into violations; examine "
            "children affected by conflict, disaster, trafficking and abuse; study treaties; "
            "promote research; spread child rights literacy; inspect custodial homes. Under s. "
            "13(1)(j) it can inquire into complaints and take suo motu notice. During such an "
            "inquiry it has the powers of a civil court (s. 14).")]),
      H("amber", "Section 2(b) defines \"child rights\" to include the rights in the CRC. The "
        "Commission is the main domestic body whose mandate is written in the Convention's "
        "terms. Source: Act 4 of 2006 text (PRS).")),

    C("What the commissions monitor", "Monitoring duties under other Acts",
      T(["Act", "Section", "Commission's role"],
        [["Commissions for Protection of Child Rights Act 2005", "s. 13(1)", "General review, "
          "inquiry and complaints; inspection of custodial homes"],
         ["Right to Education Act 2009", "s. 31(1)", "\"examine and review the safeguards for "
          "rights provided by or under this Act\" and recommend measures"],
         ["POCSO Act 2012", "s. 44(1)", "\"monitor the implementation of the provisions of this "
          "Act\""],
         ["Commissions Act 2005", "s. 25", "States may designate Children's Courts for speedy "
          "trial of offences against children, with the High Court's concurrence"]]),
      TW([B("A complaint to a state commission costs nothing and needs no lawyer. Commissions can "
            "summon records and recommend action, which often moves a district office faster "
            "than a letter from an NGO.", sm=True)],
         [H("red", "Commissions recommend; they do not enforce. Track what happens to a "
            "recommendation, and escalate to the High Court under Article 226 if nothing does.")]),
      compact=True),

    C("ICDS", "Integrated Child Development Services, since 1975",
      TW([B("ICDS was launched on 2 October 1975 (Uttar Dinajpur district administration page "
            "on ICDS). Its objectives include improving the nutrition and health of children "
            "aged 0 to 6 and laying the foundation for their psychological, physical and social "
            "development. It now runs as Anganwadi Services under Mission Saksham Anganwadi and "
            "Poshan 2.0 of the Ministry of Women and Child Development.", sm=True),
          P("green", "The six services",
            "Supplementary nutrition; pre-school non-formal education; nutrition and health "
            "education; immunisation; health check-up; referral services. \"Three of the six "
            "services, immunization, health check-up and referral services, are related to "
            "health and are provided through NHM and Public Health Infrastructure\" (MWCD).")],
         [P("indigo", "Related schemes on the same platform",
            "Poshan Abhiyaan, launched on 8 March 2018; the Scheme for Adolescent Girls aged 14 "
            "to 18, in all districts of the North-East and in Aspirational Districts elsewhere "
            "(MWCD scheme page, viewed October 2026)."),
          H("amber", "Article 45 makes early childhood care a directive principle, so ICDS is "
            "the main way the State meets it. A child under six has no fundamental right to an "
            "anganwadi place, which is why coverage and quality vary so much.")])),

    C("Mission Vatsalya", "The child protection scheme",
      TW([B("Mission Vatsalya is a centrally sponsored scheme of the Ministry of Women and Child "
            "Development. It subsumed the Child Protection Services scheme, which had run since "
            "2009-10, and supports states in delivering the JJ Act 2015 (PIB explainer, 11 "
            "August 2023).", sm=True),
          T(["Area", "Centre : State share"],
            [["States and UTs with legislature", "60 : 40"],
             ["North-Eastern states, Himachal Pradesh, Uttarakhand, Jammu and Kashmir", "90 : 10"],
             ["UTs without legislature", "100 : 0"]])],
         [P("cyan", "Components (PIB explainer)",
            "Statutory bodies; service delivery structures; institutional care and services; "
            "non-institutional community-based care; emergency outreach services; training and "
            "capacity building. Guidelines are dated 5 July 2022."),
          P("green", "What it funds in a district",
            "Child Welfare Committees and Juvenile Justice Boards, the District Child Protection "
            "Unit, child care institutions, sponsorship for children at risk of separation, and "
            "the Child Helpline 1098. The scheme provides for panchayats and urban local bodies "
            "to take part at village and ward level.")]),
      H("amber", "Name the scheme accurately in proposals: Mission Vatsalya, which subsumed the "
        "Child Protection Services scheme. Take funding rules from the guidelines dated 5 July "
        "2022.")),

    C("Budget for children", "Children's share of the Union Budget",
      {"t": "chart", "canvas": "crBudgetChart", "type": "line",
       "title": "Statement 12 (Budget for Children) as a share of the Union Budget, %",
       "source": "HAQ Centre for Child Rights, Budget for Children 2026-27 quick analysis (February 2026)",
       "data": {"labels": ["12-13", "13-14", "14-15", "15-16", "16-17", "17-18", "18-19", "19-20",
                           "20-21", "21-22", "22-23", "23-24", "24-25", "25-26", "26-27"],
                "datasets": [{"label": "Share (%)",
                              "data": [4.76, 4.64, 4.52, 3.26, 3.32, 3.32, 3.24, 3.29, 3.16,
                                       2.46, 2.35, 2.31, 2.28, 2.30, 2.47],
                              "borderColor": "#0EA5E9", "backgroundColor": "rgba(14,165,233,0.1)",
                              "fill": True, "tension": 0.2, "pointRadius": 3}]},
       "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:5 } } }"}},
      TW([B("Year labels are budget years (2012-13 to 2026-27) as charted by HAQ; HAQ notes 4.76 "
            "per cent in 2012-13 as the highest share and 3.16 per cent in 2020-21. In 2026-27 "
            "(BE) the allocation is Rs 1,32,296.85 crore, up 13.92 per cent on 2025-26.", sm=True)],
         [H("amber", "Education is 74 to 77 per cent of the children's budget and protection "
            "1.49 to 1.73 per cent (HAQ). Absolute allocations rose while the share fell by "
            "about half since 2012-13.")]),
      compact=True),

    C("Getting help", "The numbers and portals a practitioner should know",
      T(["Need", "Route", "Basis"],
        [["A child in danger now", "Child Helpline 1098, or police", "Mission Vatsalya "
          "(MWCD); JJ Act s. 31"],
         ["Sexual offence against a child", "Police or Special Juvenile Police Unit; online "
          "material via cybercrime.gov.in", "POCSO s. 19"],
         ["Child out of school or refused admission", "Local authority, then the state "
          "commission", "RTE Act ss. 32 and 31"],
         ["Child working", "Labour inspector, police, or the Child Welfare Committee", "Child "
          "Labour Act 1986 as amended; JJ Act s. 2(14)(ii)"],
         ["Marriage planned for a child", "Child Marriage Prohibition Officer, Judicial "
          "Magistrate, police", "PCMA ss. 13 and 16"],
         ["Systemic violation", "NCPCR or SCPCR complaint; High Court writ", "CPCR Act s. "
          "13(1)(j); Constitution Art. 226"]]),
      H("cyan", "Print this for every field office, with local names and phone numbers filled "
        "in. A route with no named contact in the district will fail the day it is needed."),
      compact=True),
]

# ===================== SECTION 10 =====================
SLIDES += [
    D("10", "Section Ten", "Neighbours' frameworks"),

    C("At a glance", "Child laws across South Asia",
      T(["Country", "Main child law", "Child means", "Key bodies"],
        [["India", "JJ Act 2015; POCSO 2012; RTE 2009", "Under 18 (JJ, POCSO); 6-14 (RTE)",
          "Child Welfare Committees; Juvenile Justice Boards; NCPCR"],
         ["Bangladesh", "Children Act 2013 (Shishu Ain)", "Up to 18 (s. 4)", "National, "
          "district and upazila Child Welfare Boards; Child Affairs Desk at police stations; "
          "Children's Court"],
         ["Nepal", "Act relating to Children 2018 (Act 23 of 2075)", "Under 18", "National "
          "Child Rights Council (s. 59); Child Welfare Authority; Juvenile Court"],
         ["Pakistan (federal)", "Juvenile Justice System Act 2018 (Act XXI of 2018)", "Under 18 "
          "(s. 2(b))", "Juvenile Justice Committees for diversion; juvenile courts"],
         ["Sri Lanka", "Children and Young Persons Ordinance No. 48 of 1939; Penal Code as "
          "amended", "Ordinance: child under 14, young person under 16", "Juvenile courts"]]),
      B("Sources: Supreme Court of Bangladesh commentary on the Children Act 2013; Nepal Law "
        "Commission English text (via FAOLEX); Pakistan JJSA 2018 text (ADB Law and Policy "
        "Reform); Sri Lanka Penal Code (Amendment) Act No. 10 of 2018; The Morning (Sri Lanka) "
        "on the 1939 Ordinance.", sm=True), compact=True),

    C("Bangladesh", "The Children Act 2013",
      TW([B("The Children Act 2013 (Shishu Ain) repealed the Children Act 1974. A commentary "
            "published by the Supreme Court of Bangladesh notes that its preamble describes it as "
            "enacted to implement the CRC, that s. 3 gives it overriding effect, and that s. 4 "
            "defines a child as anyone up to eighteen.", sm=True),
          P("cyan", "New structures",
            "Child Welfare Boards at national, district and upazila level, meeting every six, "
            "four and three months respectively; a Child Affairs Desk at police stations headed "
            "by a Child Affairs Police Officer; and expanded duties for Probation Officers, "
            "including diversion and family group conferencing.")],
         [P("amber", "A gap the commentary identifies",
            "Allegations against children are still decided by a Children's Court, a judicial "
            "body: \"there is no independent non-judicial forum as contemplated by the CRC to "
            "deal with children in conflict with the law\"."),
          P("green", "Arrest safeguards",
            "Under s. 45 a police officer who arrests a child must inform the parents or "
            "guardian, the Probation Officer and, where necessary, the nearest Board. A finding "
            "of guilt does not disqualify a child from later employment or elections.")]),
      H("cyan", "Bangladesh ratified the CRC on 3 August 1990 and both substantive protocols on "
        "6 September 2000, the same day it signed them (UN Treaty Collection).")),

    C("Nepal", "The Act relating to Children 2018",
      TW([B("Nepal's Act (Act No. 23 of 2075 BS) defines children as \"persons who have not "
            "completed the age of eighteen years\". Chapter 2 sets out rights in the CRC's "
            "pattern, from the right to live (s. 3) to the rights to participate (s. 8), to "
            "form a child club or organisation (s. 10), to privacy (s. 11) and to education "
            "(s. 15).", sm=True),
          P("green", "Minimum age of criminal responsibility",
            "\"If the child is less than ten years of age at the time of commission of the "
            "offence, no case and punishment of any kind shall be instituted against and imposed "
            "on him or her\" (s. 36(1)). Children aged ten to fourteen face lighter consequences.")],
         [P("cyan", "Protection in the home",
            "Every child has the right to protection against \"any type of physical or mental "
            "violence and torture, hatred, inhuman treatment, gender or untouchability-based "
            "mistreatment, sexual harassment and exploitation\" by parents, family, guardians, "
            "teachers and others."),
          P("indigo", "Institutions",
            "A National Child Rights Council chaired by the minister responsible for children "
            "(s. 59), with provincial and local counterparts, and juvenile courts that sit in "
            "camera (s. 35).")]),
      H("amber", "Naming \"untouchability-based mistreatment\" in a child protection clause is a "
        "direct statutory hook for caste discrimination against children. Source: Nepal Law "
        "Commission English translation.")),

    C("Pakistan and Sri Lanka", "Juvenile justice reform in Pakistan and Sri Lanka",
      TW([P("cyan", "Pakistan: Juvenile Justice System Act 2018",
            "Act XXI of 2018 defines a child as \"a person who has not attained the age of "
            "eighteen years\" (s. 2(b)). No person who was a juvenile offender at the time of "
            "the offence \"shall be awarded punishment of death\", and no juvenile in custody "
            "may be \"put in fetters, handcuffed or given any corporal punishment\". The Act "
            "sets up Juvenile Justice Committees for diversion."),
          B("Source: Act text on the ADB Law and Policy Reform portal. Provincial laws on "
            "child protection and marriage differ and are not covered here.", sm=True)],
         [P("green", "Sri Lanka: raising the age of criminal responsibility",
            "The Penal Code (Amendment) Act, No. 10 of 2018 (certified 21 May 2018) raised the age "
            "in s. 75 of the Penal Code from eight to twelve, and moved the s. 76 maturity test to "
            "children above twelve and under fourteen. The Children and Young Persons "
            "Ordinance of 1939 still defines a child as under 14 and a young person as under "
            "16 (The Morning, reporting on juvenile justice), leaving a gap for sixteen- and "
            "seventeen-year-olds."),
          H("amber", "Sri Lanka ratified the CRC on 12 July 1991 and OPAC on 8 September 2000, "
            "declaring a minimum age of 18 for voluntary recruitment (UN Treaty Collection).")])),

    C("Comparing", "Minimum age of criminal responsibility in the region",
      {"t": "chart", "canvas": "crMacrChart", "type": "bar",
       "title": "Age below which a child cannot be held criminally responsible (years)",
       "source": "BNS 2023 s. 20; Nepal Act relating to Children 2018 s. 36(1); Sri Lanka "
                 "Penal Code s. 75, as amended by Act No. 10 of 2018; CRC/C/GC/24 para. 22",
       "data": {"labels": ["India", "Nepal", "Sri Lanka", "CRC Committee benchmark"],
                "datasets": [{"label": "Years", "data": [7, 10, 12, 14],
                              "backgroundColor": ["#0EA5E9", "#10B981", "#6366F1", "#F59E0B"]}]},
       "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:16 } } }"}},
      TW([B("India's floor is seven under the Bharatiya Nyaya Sanhita 2023, s. 20, with a "
            "further defence for children aged seven to twelve who lack \"sufficient maturity of "
            "understanding\" (s. 21). Any child under eighteen is still dealt with under the JJ "
            "Act, so the floor matters less in practice than the procedure.", sm=True)],
         [H("cyan", "General comment No. 24 (2019), para. 22, encourages states \"to increase "
            "their minimum age accordingly, to at least 14 years of age\", citing evidence that "
            "the frontal cortex is still developing at twelve and thirteen.")]),
      compact=True),
]

# ===================== SECTION 11 =====================
SLIDES += [
    D("11", "Section Eleven", "Putting it to work"),

    C("A design checklist", "Twelve questions before a programme touches children",
      TW([T(["#", "Question", "If no"],
            [["1", "Do we know which law defines \"child\" for this activity?", "Check the age "
              "table in Section 04"],
             ["2", "Have we mapped who is excluded (Art. 2)?", "Add caste, disability, "
              "migration, documents to the baseline"],
             ["3", "Is there a written best-interests assessment for decisions about "
              "individual children?", "Use GC 14's procedural test"],
             ["4", "Have children been consulted on the design (Art. 12)?", "Run age-appropriate "
              "consultation before finalising"],
             ["5", "Is there a POCSO reporting procedure?", "Write one; name the reporter and "
              "police station"],
             ["6", "Do staff and partners sign a code of conduct?", "See Safeguarding and PSEA 101"]])],
         [T(["#", "Question", "If no"],
            [["7", "Are photos and stories cleared for identification risk (JJ s. 74)?",
              "Remove identifying detail"],
             ["8", "Do we know the district's CWC, JJB, CMPO and DCPU contacts?", "Collect them "
              "before launch"],
             ["9", "Does data collection have parental consent and child assent?", "See ICMR "
              "2017, section 6.5, and Section 12 of this deck"],
             ["10", "Will personal data of children be processed?", "Plan for DPDP s. 9 "
              "from 13 May 2027"],
             ["11", "Is there a feedback route children can use safely?", "Set one up and test it"],
             ["12", "Do outcome indicators track children's situation a year later?", "Add "
              "follow-up indicators"]])]),
      H("cyan", "Each no marks a specific gap with a specific fix. Twelve yes answers are a "
        "starting point for a rights-based programme."), compact=True),

    C("Worked example", "Two children at one learning centre (Illustrative)",
      B("<strong>Illustrative.</strong> An NGO runs an after-school learning centre in an urban "
        "settlement. In one week a volunteer learns that Raju, aged 13, washes dishes at a "
        "roadside eatery from 6 pm to midnight, and that Salma, aged 16, has stopped attending "
        "because her family has fixed her wedding for next month."),
      TW([P("cyan", "Raju",
            "Under 14, employed in an eatery: prohibited by s. 3(1) of the 1986 Act as amended. "
            "He is \"found working in contravention of labour laws\", so a child in need of "
            "care and protection (JJ Act s. 2(14)(ii)). Night work also threatens his schooling "
            "under the RTE Act. Route: inform the labour inspector or police and the Child "
            "Welfare Committee; plan with his family for income support and school attendance "
            "before any raid.")],
         [P("amber", "Salma",
            "At imminent risk of marriage (JJ Act s. 2(14)(xii)). Under the PCMA any person or an "
            "NGO may ask a Judicial Magistrate for an injunction (s. 13(1)-(2)); a marriage "
            "against it is void (s. 14). Route: talk to Salma first about what she wants; "
            "inform the Child Marriage Prohibition Officer; seek an injunction if the family "
            "will not postpone; keep her in school.")]),
      H("green", "In both cases the first step is a conversation with the child (Art. 12) and a "
        "named staff member who owns the follow-up. The law supplies routes; the programme "
        "supplies continuity.")),

    C("Decision table", "Situation, law, body, deadline",
      T(["Situation", "Law", "Body to approach", "Time limit in law"],
        [["Disclosure of sexual abuse", "POCSO 2012 s. 19", "Police or SJPU", "Police to inform "
          "CWC and Special Court within 24 hours (s. 19(6))"],
         ["Child found alone, working or begging", "JJ Act 2015 ss. 2(14), 31", "Child Welfare "
          "Committee", "Produce the child within 24 hours, excluding travel (s. 31)"],
         ["Child arrested", "JJ Act 2015 ss. 10, 12", "Juvenile Justice Board", "Bail is the "
          "default (s. 12(1))"],
         ["Child marriage arranged", "PCMA 2006 s. 13", "Judicial Magistrate; CMPO", "Interim "
          "injunction possible without notice in urgency"],
         ["Admission refused or fee demanded", "RTE 2009 ss. 12, 13", "Local authority; SCPCR",
          "Local authority to decide within three months (s. 32)"],
         ["Teacher beats a child", "RTE s. 17; JJ s. 75", "School authority; police for "
          "cruelty", "Disciplinary action; criminal case where s. 75 applies"],
         ["Children's data in an app or survey", "DPDP 2023 s. 9", "Data Protection Board",
          "Obligations apply from 13 May 2027"]]),
      H("amber", "Keep this table with local contacts in every field office. Time limits are "
        "the ones written into the law; actual practice is slower, which is why someone must "
        "follow up."), compact=True),

    C("Safeguarding", "Protecting children from your own organisation",
      TW([B("Every rights programme carries a risk that staff, volunteers, partners or "
            "visitors harm the children it serves. POCSO treats an offence by staff of an "
            "institution as aggravated, and s. 21(2) punishes the person in charge who fails to "
            "report an offence by a subordinate.", sm=True),
          BL(["A written policy, signed by every staff member and partner",
              "Safe recruitment: references and background checks",
              "Two-adult rule for one-to-one contact where practicable",
              "A designated safeguarding lead with authority to act",
              "A reporting route that bypasses the line manager"], color="cyan")],
         [P("amber", "Communications",
            "No photograph or story that identifies a child in the justice or care system (JJ "
            "s. 74). For other children, informed consent from the parent and assent from the "
            "child, with the right to withdraw. Never use a child's suffering to raise funds in "
            "a way the child would not accept as an adult."),
          P("green", "Partners",
            "Put safeguarding clauses in grant agreements, check that partners have a POCSO "
            "procedure, and fund the training. A partner's lapse is reported under your "
            "organisation's name.")]),
      H("cyan", "The Safeguarding and PSEA 101 deck covers policies, investigations and "
        "survivor-centred response in full.")),

    C("Alternative reporting", "Taking evidence to the UN Committee",
      FLOW("Watch the OHCHR treaty body database for India's next list of issues",
           "Form or join a coalition: one report carries more weight than ten",
           "Organise by the Convention's articles and the Committee's 2014 concluding observations on India",
           "Use programme data with sources, case summaries with identities removed, and children's own views",
           "Make specific, measurable recommendations",
           "After concluding observations: follow up with ministries and the NCPCR"),
      TW([B("India's 2014 review drew alternative reports from many groups, listed in the "
            "treaty body database. The fifth and sixth cycle is under the simplified reporting "
            "procedure, so input before the list of issues is adopted is the most useful.",
            sm=True)],
         [H("green", "If the report includes children's views, collect them as you would in "
            "research: consent from parents, assent from children, anonymity, and a plan for "
            "anything disclosed (Section 12).")])),

    C("Budget work", "Tracking whether money reaches children",
      TW([P("cyan", "A four-step exercise",
            "1. Find the scheme in Statement 12 of the Union Budget and in the state budget. "
            "2. Compare budget estimate, revised estimate and actual spending for three years. "
            "3. Divide by the number of children eligible to get spending per child. 4. Check "
            "what reached the district: sanctioned posts filled, institutions inspected, "
            "children supported."),
          B("General comment No. 19 (2016) on public budgeting under Article 4 sets out five "
            "principles: effectiveness, efficiency, equity, transparency and sustainability "
            "(CRC/C/GC/19).",
            sm=True)],
         [P("amber", "What usually turns up",
            "Child protection is a small slice: 1.49 to 1.73 per cent of the Budget for Children "
            "in recent years (HAQ, February 2026). Underspending on protection is common because "
            "the posts and bodies it funds are not in place, which links the budget back to the "
            "PRS finding that only 17 of 35 states and union territories had all JJ Act bodies "
            "in every district in 2019.")]),
      H("green", "The Public Finance and Budgeting 101 deck explains budget documents step by "
        "step.")),

    C("Common mistakes", "Seven errors that undermine child rights work",
      T(["Mistake", "Why it matters", "Better practice"],
        [["Quoting the CRC as if it were an Indian statute", "Treaties take effect in India "
          "through Indian law and its interpretation", "Cite the Indian Act, then the CRC as an "
          "interpretive aid"],
         ["Using an old scheme name in a proposal", "\"Child Protection Services\" now sits "
          "inside Mission Vatsalya", "Use current names and guideline dates"],
         ["Treating every adolescent relationship as abuse", "Criminalises young people; a "
          "complaint can be a family's weapon against a daughter's partner", "Report as the law "
          "requires, and support both young people"],
         ["Rescue without rehabilitation", "Children return to work", "Plan income, school and "
          "follow-up before removal"],
         ["Publishing identifiable stories", "Breaks JJ s. 74; harms the child", "Remove names, "
          "places, schools, faces"],
         ["Consulting children once, at the end", "Tokenism (Hart's ladder)", "Involve "
          "children from design, and report back what changed"],
         ["Collecting more child data than needed", "Risk under DPDP s. 9 from 2027", "Minimise "
          "and delete"]]),
      H("cyan", "None of these requires bad intent. Each can be prevented by asking the "
        "questions in this section early, and by giving one person on the team the job of "
        "asking them."), compact=True),
]

# ===================== SECTION 12 =====================
SLIDES += [
    D("12", "Section Twelve", "Participation, research and data"),

    C("Models", "Two models of children's participation",
      TW([P("cyan", "Hart's ladder (1992)",
            "Roger Hart's <em>Children's Participation: From Tokenism to Citizenship</em> "
            "(UNICEF, 1992) borrowed the ladder metaphor from Sherry Arnstein's 1969 essay on "
            "adult participation; the eight categories were his own. Its "
            "lower rungs (manipulation, decoration, tokenism) are non-participation; its upper "
            "rungs run from children assigned but informed, through consulted, to projects "
            "children initiate and share with adults."),
          B("Hart later wrote that \"the ladder metaphor is unfortunate for it seems to imply a "
            "necessary sequence\"; it is \"primarily about the degree to which adults and "
            "institutions afford or enable children to participate\" (Hart, \"Stepping back "
            "from 'the ladder'\").", sm=True)],
         [P("green", "Lundy's model (2007)",
            "Laura Lundy, \"'Voice' is not enough: conceptualising Article 12\", <em>British "
            "Educational Research Journal</em> 33(6): 927-942. Four elements: "
            "<strong>Space</strong> (an opportunity to express a view), <strong>Voice</strong> "
            "(support to express it), <strong>Audience</strong> (someone with power listens) "
            "and <strong>Influence</strong> (the view is acted on, as appropriate)."),
          H("amber", "Lundy's point is in the title: hearing children is half of Article 12. "
            "\"Due weight\" requires an audience that can act, and feedback on what happened.")]),
      H("cyan", "Use Lundy's four words as a checklist at the end of any consultation: where was "
        "the space, how was voice supported, who was the audience, what changed?")),

    C("From South Asia", "Working children, organised",
      TW([B("Hart's later chapter credits two members of the Concerned for Working Children in "
            "India, \"who work with Bhima Sangha, a union of child workers in Bangalore\", with "
            "\"valuable schemas for thinking about the varying roles adults play\" (Reddy and "
            "Ratna, <em>A Journey in Children's Participation</em>, 2002).", sm=True),
          P("cyan", "What they added",
            "Two rungs below Hart's lowest: <strong>active resistance</strong>, where adults "
            "work against children's participation, and a weaker form of hindrance that leaves "
            "children reluctant to take part. They also named \"tolerance\" and \"indulgence\" "
            "as forms of tokenism.")],
         [P("green", "In law",
            "Nepal's Act relating to Children 2018 gives a child \"competent to form his or her "
            "own opinion\" the right \"to participate in the decision-making process of family, "
            "community, school or other public institution\" (s. 8), and the right to open a "
            "child club or organisation (s. 10)."),
          H("amber", "Organised children can hold adults to account, which is the point and "
            "also the risk. Programmes that support children's groups must be ready to "
            "protect members who speak against employers, officials or elders.")]),
      B("Source: R. Hart, \"Stepping back from 'the ladder'\", chapter 2 of an edited volume on "
        "participation and learning; Nepal Law Commission English text.", sm=True)),

    C("The ethics of asking", "Participation can harm as well as help",
      T(["Risk", "Example", "Safeguard"],
        [["Tokenism", "A child speaker at a conference whose words were written by staff",
          "Let children set their own message, or do not invite them"],
         ["Exposure", "A child names an abusive employer at a public hearing", "Anonymity; "
          "group presentation; a protection plan before and after"],
         ["Burden", "Children asked again and again for their stories", "Ask only what will be "
          "used; share findings back"],
         ["Exclusion", "Only articulate, schooled, urban children are consulted", "Reach "
          "working, disabled and out-of-school children deliberately (Art. 2)"],
         ["Broken promises", "Views collected, nothing changes, nobody explains", "Report back, "
          "including when the answer is no (Lundy's influence)"]]),
      H("cyan", "Participation is subject to the same best-interests test as any other action "
        "concerning children (Art. 3). A consultation that leaves a child less safe has failed, "
        "however good the report looks."), compact=True),

    C("Consent and assent", "Research with children under the ICMR 2017 guidelines",
      TW([B("The ICMR <em>National Ethical Guidelines for Biomedical and Health Research "
            "Involving Human Participants</em> (2017), section 6.5, treat children as people "
            "\"who have not attained the legal age of consent (up to 18 years)\". The decision "
            "on participation is the parents' or legally acceptable representative's, \"in the "
            "best interests of their child/ward\". The guidelines cover social and behavioural "
            "health research as well as clinical work.", sm=True),
          T(["Age", "Assent required (Box 6.6)"],
            [["Under 7", "No need to document assent"],
             ["7 to 12", "Verbal or oral assent, in the presence of parents or LAR, recorded"],
             ["12 to 18", "Written assent, also signed by parents or LAR"]])],
         [P("green", "Dissent counts",
            "\"If the child objects, this wish has to be respected. At the same time, mere "
            "failure to object should not be construed as assent.\" The only exception is a "
            "potentially lifesaving intervention available only in the study, with parental "
            "consent and prior ethics committee approval."),
          H("amber", "Adolescents: where parental consent would defeat the study (ICMR's example "
            "is research with adolescents who inject drugs), the ethics committee can approve "
            "a waiver of the adult's consent and record it.")]),
      B("Source: ICMR National Ethical Guidelines 2017, section 6.5 and Boxes 6.5 and 6.6.", sm=True)),

    C("More on consent", "Parents, institutions and the ethics committee",
      TW([P("cyan", "One parent or both (Box 6.5)",
            "\"The EC should determine if consent of one or both parents would be required.\" "
            "Generally, one parent's consent may be enough for research involving no more than "
            "minimal risk or offering direct benefit to the child."),
          P("indigo", "Children in institutions",
            "Research with institutionalised children needs the child's assent, the consent of "
            "parents or LAR, and permission from the institution: in a school, that can mean "
            "the child, parents, teacher, principal or management.")],
         [P("amber", "Assent forms",
            "Written for the child's developmental level: what the study is, how it helps, what "
            "will be done, and that the child can refuse or stop. The language must be "
            "\"simple and appropriate to the age of the child\"."),
          P("green", "Children in care",
            "For a child in a home under the JJ Act, the Child Welfare Committee's role and the "
            "institution's permission both matter, and s. 74's ban on identification applies "
            "to research outputs as much as to the press.")]),
      H("red", "A researcher who hears a disclosure of sexual abuse is bound by POCSO s. 19 like "
        "anyone else. Tell participants and parents before the interview what you will have to "
        "report, and have a referral route ready."),
      B("Source: ICMR 2017, Box 6.5 and section 6.5; JJ Act 2015 s. 74; POCSO 2012 s. 19.", sm=True)),

    C("Children's data", "The DPDP Act 2023: children's personal data",
      TW([Q("The Data Fiduciary shall, before processing any personal data of a child or a "
            "person with disability who has a lawful guardian obtain verifiable consent of the "
            "parent of such child or the lawful guardian, as the case may be, in such manner as "
            "may be prescribed.", "DPDP Act 2023, s. 9(1)"),
          BL(["<strong>s. 2(f):</strong> a child is \"an individual who has not completed the "
              "age of eighteen years\"",
              "<strong>s. 9(2):</strong> no processing \"likely to cause any detrimental effect "
              "on the well-being of a child\"",
              "<strong>s. 9(3):</strong> no tracking, behavioural monitoring or targeted "
              "advertising directed at children",
              "<strong>Schedule:</strong> breach of s. 9 obligations, penalty up to Rs 200 crore"],
             color="cyan")],
         [P("amber", "When it applies",
            "The DPDP Rules were published in the Gazette on 13 November 2025 (G.S.R. 846(E)) and "
            "commence in three phases. Rule 10, verifiable consent of a parent, and Rule 12, the "
            "exemptions, apply from <strong>13 May 2027</strong>, eighteen months after "
            "publication (Rule 1(4)). Section 9 of the Act itself commences on the same date "
            "(G.S.R. 843(E), 13 November 2025). As of October 2026 neither is in force."),
          P("green", "Exemptions",
            "s. 9(4) lets the government exempt classes of fiduciaries or purposes from s. 9(1) "
            "and (3). Rule 12 and the Fourth Schedule exempt classes including clinical and mental "
            "health establishments, healthcare professionals, educational institutions, crèches "
            "and school transport from s. 9(1) and (3), each limited to stated purposes such as "
            "health care or the child's safety.")]),
      H("cyan", "Research: s. 17(2)(b) exempts processing \"necessary for research, archiving or "
        "statistical purposes if the personal data is not to be used to take any decision "
        "specific to a Data Principal\", following prescribed standards. A survey that then "
        "targets services to named children may fall outside it.")),

    C("Data practice", "Collecting data about children safely",
      TW([BL(["<strong>Minimise:</strong> collect only what the analysis needs; record age "
              "in completed years when a full date of birth is not required",
              "<strong>Separate:</strong> keep names and contact details apart from responses",
              "<strong>Protect:</strong> never record a child's identity in anything that "
              "links them to a JJ or POCSO case (JJ s. 74)",
              "<strong>Disclose:</strong> explain the reporting duty under POCSO s. 19 "
              "in the consent script",
              "<strong>Return:</strong> share findings with children in a form they can use"],
             color="cyan")],
         [P("green", "Learning from national surveys",
            "NFHS and the DHS surveys build child indicators from measurements of children and "
            "interviews with adults; early marriage is reported by women aged 20 to 24 looking "
            "back. Young children's own views are not recorded. Ask whose voice a dataset "
            "carries before quoting it as children's experience."),
          P("amber", "Disaggregate",
            "Article 2 cannot be monitored without data by sex, age, caste, disability, "
            "residence and wealth. The NFHS-5 gradients in Section 08 are only visible because "
            "the survey records them.")]),
      H("indigo", "The Research Ethics 101 and Data Protection and the DPDP Act 101 decks go "
        "deeper on review boards, consent design and data security.")),

    C("Where next", "Where next",
      B("Child rights sit where law, development practice and research meet. These ImpactMojo "
        "101 decks take each strand further."),
      TW([BL(["<a href=\"/101-courses/human-rights.html\">Human Rights 101</a>: the treaty "
              "system, Indian constitutional rights and remedies",
              "<a href=\"/101-courses/child-development.html\">Child Development 101</a>: "
              "growth, early childhood and what the stunting figures mean",
              "<a href=\"/101-courses/safeguarding-psea.html\">Safeguarding &amp; PSEA 101</a>: "
              "policies, codes of conduct and survivor-centred response",
              "<a href=\"/101-courses/sel-basics.html\">SEL Basics 101</a>: classroom "
              "alternatives to punishment"], color="cyan")],
         [BL(["<a href=\"/101-courses/inclusive-education.html\">Inclusive Education 101</a>: "
              "disability, the RTE Act and access to school",
              "<a href=\"/101-courses/research-ethics.html\">Research Ethics 101</a>: consent, "
              "assent, risk and review",
              "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the DPDP "
              "Act 101</a>: personal data in practice",
              "<a href=\"/101-courses/ind-constitution.html\">Indian Constitution 101</a>: "
              "fundamental rights, directive principles and writs"], color="green")]),
      H("amber", "Start with the checklist in Section 11 on a programme you know, then read the "
        "Safeguarding and PSEA deck before your next field visit.")),
]

# ===================== END =====================
SLIDES += [
    {"type": "end",
     "eyebrow": "Child Rights 101 &middot; Complete",
     "headline": "Name the duty,<br>then follow the child.",
     "byline": "Child rights become real when someone knows which law applies, which body to "
               "approach, and who will still be checking a year later. Explore the rest of the "
               "ImpactMojo 101 Series, free forever.",
     "ctas": [
         {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
         {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"}],
     "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
]

DECK = {
    "slug": "child-rights",
    "title": "Child Rights 101",
    "description": ("Child Rights 101: a free foundational course for development practitioners "
                    "in South Asia. The UN Convention on the Rights of the Child and its four "
                    "principles; the optional protocols and the Committee; Articles 15(3), 21A, "
                    "24, 39 and 45 of India's Constitution; the JJ Act 2015, POCSO 2012, the RTE "
                    "Act 2009, the child labour law as amended in 2016 and the Prohibition of "
                    "Child Marriage Act 2006; NCPCR, ICDS and Mission Vatsalya; laws in "
                    "Bangladesh, Nepal, Pakistan and Sri Lanka; participation, ICMR consent and "
                    "assent, and the DPDP Act. ImpactMojo, CC BY-NC-ND."),
    "slides": SLIDES,
}

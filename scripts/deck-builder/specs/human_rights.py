# -*- coding: utf-8 -*-
"""
Human Rights 101 - ImpactMojo 101 Series (native deck spec)
Human rights for development practitioners in South Asia: the international
bill of rights, treaty ratification in the region, the UN machinery, the
human rights-based approach, rights in the Indian Constitution, courts and
national human rights institutions, economic and social rights, civic space,
business and human rights, and how a programme uses rights.
Build: python3 scripts/deck-builder/build.py human_rights

Sources were opened and read for every figure and citation; the list is in the
build report. Treaty dates come from the OHCHR treaty body database and the UN
Treaty Collection (checked October 2026).
"""


def C(label, title, blocks, **kw):
    s = {"type": "content", "label": label, "title": title, "blocks": blocks}
    s.update(kw)
    return s


def body(html, sm=False):
    b = {"t": "body", "html": html}
    if sm:
        b["cls"] = "sm"
    return b


def hbox(html, color="cyan"):
    return {"t": "hbox", "color": color, "html": html}


def term(word, d):
    return {"t": "term", "word": word, "def": d}


def bullets(items, color=None, sm=False):
    b = {"t": "bullets", "items": items}
    if color:
        b["color"] = color
    if sm:
        b["sm"] = True
    return b


def table(head, rows):
    return {"t": "table", "head": head, "rows": rows}


def flow(steps):
    return {"t": "flow", "steps": steps}


def panel(color, title, blocks):
    return {"t": "panel", "color": color, "title": title, "blocks": blocks}


def tw(left, right, ratio="half"):
    return {"t": "twocol", "ratio": ratio, "left": left, "right": right}


def pp(color, title, html):
    """A two-column half made of one panel holding small body text."""
    return [panel(color, title, [body(html, sm=True)])]


def stats(cards, cols=None):
    return {"t": "stats", "cols": cols or len(cards), "cards": cards}


def quote(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


OHCHR_TB = "OHCHR treaty body database, ratification status by country (checked October 2026)"

# ===================== SECTION 01: FOUNDATIONS =====================
S01 = [
    D("01", "Section One", "What rights are and where they come from"),

    C("Definition", "A human right is a claim with a duty attached", [
        body("A <strong>human right</strong> is an entitlement that every person holds because they are "
             "human, which someone else is obliged to respect. That second half is what separates a right "
             "from a wish. When a village says it wants a road, that is a demand. When a woman says the "
             "state must not detain her without telling her why, and must let her see a lawyer, she is "
             "pointing to a duty that a named authority already owes her under the Constitution and under "
             "treaties India has joined."),
        term("Human right",
             "A legal and moral entitlement held by every person, matched by an obligation on a duty-bearer "
             "(usually the state) to respect, protect and fulfil it, with some route to a remedy when the "
             "obligation is broken."),
        tw(pp("cyan", "Rights-holder", "The person or group who can make the claim: a child, a pavement "
              "dweller, a detainee, a community facing eviction."),
           pp("indigo", "Duty-bearer", "The body that owes the duty: the state first, through its "
              "ministries, police, courts and local bodies; increasingly also companies and other "
              "private actors.")),
    ]),

    C("Three obligations", "Respect, protect, fulfil: the three layers of state duty", [
        body("International law and Indian courts both describe the state's obligation in three layers. "
             "The framework is useful for practitioners because it turns a vague right into specific "
             "questions about who must do what. Take the right to food as the running example, since India "
             "has a statute on it (the National Food Security Act 2013) and a long Supreme Court case."),
        table(["Layer", "What it asks of the state", "Right to food example"], [
            ["Respect", "Do not interfere with people's existing enjoyment of the right",
             "Do not destroy crops or block access to common land without lawful process"],
            ["Protect", "Stop third parties from interfering",
             "Regulate traders who divert ration grain; act against land grabs"],
            ["Fulfil", "Take positive steps so people can enjoy the right",
             "Run the public distribution system, mid-day meals and maternity support"],
        ]),
        hbox("A programme can map its own work onto these layers. Monitoring ration shops supports the "
             "protect layer. Helping families get ration cards supports the fulfil layer. Documenting "
             "evictions speaks to the respect layer.", "indigo"),
    ]),

    C("Where rights come from", "Three sources that a practitioner meets in practice", [
        body("Arguments about the origin of rights fill libraries. For field work, three sources matter "
             "because each has its own forum and its own way of being enforced. Knowing which source you "
             "are relying on tells you where to go when the right is denied."),
        tw(pp("cyan", "Moral and philosophical", "Ideas of dignity found in many traditions, including "
              "Indian ones. They give rights their force in public argument, but no court enforces a "
              "philosophy on its own."),
           pp("green", "International law", "Treaties a state has joined (such as the ICCPR and ICESCR) "
              "and customary law. Enforced through UN reporting, reviews and, for some states, individual "
              "complaints.")),
        panel("amber", "Domestic law", [body(
            "The Constitution, statutes and case law. In India this is where rights bite hardest: Article 32 "
            "lets a person go straight to the Supreme Court to enforce a fundamental right, and Article 226 "
            "lets High Courts issue writs. Most remedies a programme will ever use sit here.", sm=True)]),
    ]),

    C("Four principles", "Universal, indivisible, interdependent, interrelated", [
        body("The 1993 World Conference on Human Rights in Vienna set out the principle that still frames "
             "UN practice. Its Declaration, adopted on 25 June 1993, says in paragraph 5 of Part I:"),
        quote("All human rights are universal, indivisible and interdependent and interrelated.",
              "Vienna Declaration and Programme of Action, Part I, para 5 (UN doc A/CONF.157/23, 1993)"),
        body("The same paragraph adds that national and regional particularities and different historical, "
             "cultural and religious backgrounds must be borne in mind, while it remains the duty of all "
             "states to promote and protect all human rights. For South Asian practice this matters "
             "twice over. It rules out treating civil rights as a luxury to come after growth, and it also "
             "requires food and housing to be treated as entitlements.", sm=True),
        hbox("Indivisibility has a practical reading: a family cannot use its right to vote freely if it "
             "fears losing its ration card, and a child cannot use the right to education while hungry.",
             "green"),
    ]),

    C("Two families of rights", "Civil and political rights, economic, social and cultural rights", [
        tw([panel("cyan", "Civil and political", [bullets([
                "Life, and freedom from torture",
                "Liberty and fair trial",
                "Expression, assembly, association",
                "Religion and conscience",
                "Privacy, and political participation"], sm=True)])],
           [panel("green", "Economic, social and cultural", [bullets([
                "Work and fair conditions of work",
                "Social security",
                "An adequate standard of living: food, housing, water",
                "Health and education",
                "Taking part in cultural life"], sm=True)])]),
        body("The UDHR held both families in one text; the treaties of 1966 separated them into two "
             "Covenants with different wording on how fast states must act. India's Constitution mirrors the split in its own way: most civil rights sit "
             "in the enforceable Part III, most economic and social goals sit in the non-enforceable Part IV. "
             "Section 06 shows how Indian courts later drew the two together through Article 21.", sm=True),
    ]),

    C("Individual and collective", "Rights held by persons and rights held by groups", [
        body("Most human rights belong to individuals. Some are framed for groups or are exercised "
             "together: the right of peoples to self-determination in Article 1 of both Covenants, "
             "minority rights in Article 27 of the ICCPR, and the collective rights of Scheduled Tribes "
             "and forest-dwelling communities in Indian law. Development work often sits where the two "
             "meet, for example when a community's claim to forest land rests on both individual and "
             "community titles."),
        tw(pp("indigo", "Why the distinction matters", "Consent, representation and remedy all change. An "
              "individual can withdraw consent; a group decision needs a legitimate process, and a "
              "programme has to ask who speaks for the group."),
           pp("amber", "A caution", "Group claims can hide unequal power inside the group. Women, younger "
              "members and lower-caste households may be overruled. A rights-based design checks both "
              "levels, as Section 05 explains.")),
        hbox("India attached a declaration to Article 1 of both Covenants on self-determination. Section 03 "
             "reads it in full.", "cyan"),
    ]),

    C("Why practitioners need this", "What rights language adds to a development programme", [
        body("Development programmes already talk about needs, targets and coverage. Rights language adds "
             "four things that needs language lacks. Each one changes how a programme is designed and "
             "judged, which is why donors such as UN agencies made it a formal approach in 2003."),
        table(["Rights language adds", "What it changes in a programme"], [
            ["A named duty-bearer", "A public office is answerable when the service fails"],
            ["A legal standard", "Quality and coverage are judged against law as well as a project target"],
            ["A remedy", "A grievance has a route: a hearing, a commission, a court"],
            ["Non-discrimination", "Coverage must reach the most excluded households"],
        ]),
        hbox("This deck uses India as the main case because it is where most of our learners work, and "
             "brings in Bangladesh, Nepal, Pakistan and Sri Lanka wherever their treaty records and "
             "institutions differ in ways that matter.", "indigo"),
    ]),
]

# ===================== SECTION 02: INTERNATIONAL BILL OF RIGHTS =====================
S02 = [
    D("02", "Section Two", "The international bill of rights"),

    C("1948", "The Universal Declaration of Human Rights", [
        body("The General Assembly adopted the <strong>Universal Declaration of Human Rights (UDHR)</strong> "
             "in Paris by resolution 217 A (III) on 10 December 1948. No state voted against it and eight "
             "abstained. Human Rights Day is marked on 10 December for that reason. The UDHR has 30 articles "
             "and covers both civil and political rights and economic and social rights in one text."),
        stats([
            {"num": "10 Dec 1948", "label": "UDHR adopted, GA resolution 217 A (III)", "color": "cyan",
             "source": "United Nations, History of the Declaration (un.org)"},
            {"num": "0", "label": "states voted against; eight abstained", "color": "indigo",
             "source": "United Nations, History of the Declaration (un.org)"},
        ]),
        hbox("The UDHR is a resolution, so it was not written as a binding treaty. Its force today comes "
             "from the treaties built on it, from constitutions that copied its language, and from the "
             "argument that parts of it have become customary international law.", "amber"),
    ]),

    C("India's contribution", "Hansa Mehta and the words of Article 1", [
        body("Indian delegates took part in drafting. The UN's own history of the Declaration credits "
             "<strong>Hansa Mehta</strong> of India with changing the phrase \"All men are born free and "
             "equal\" to \"All human beings are born free and equal\" in Article 1. The change is small on "
             "the page and large in effect: a text meant to bind the world would otherwise have started by "
             "naming only half of it."),
        quote("All human beings are born free and equal in dignity and rights.",
              "Universal Declaration of Human Rights, Article 1 (1948)"),
        tw(pp("cyan", "What to take from this", "The idea that human rights are a Western import is weak "
              "history. South Asian delegates drafted, argued over and shaped the texts that now bind their "
              "states."),
           pp("green", "Using it in training", "Starting a community session with Article 1 and the story "
              "of its wording is a simple way to show that equality between women and men was argued for "
              "from this region.")),
    ]),

    C("The Covenants", "1966: the two Covenants turn the Declaration into treaties", [
        body("It took eighteen years to turn the Declaration into binding treaties. On 16 December 1966 "
             "the General Assembly adopted the <strong>International Covenant on Civil and Political Rights "
             "(ICCPR)</strong> and the <strong>International Covenant on Economic, Social and Cultural "
             "Rights (ICESCR)</strong>. India's Protection of Human Rights Act 1993 names that same date "
             "when it defines the \"International Covenants\" in section 2(1)(f)."),
        table(["Treaty", "Adopted", "In force", "Monitoring body"], [
            ["ICESCR", "16 Dec 1966", "3 Jan 1976", "Committee on Economic, Social and Cultural Rights"],
            ["ICCPR", "16 Dec 1966", "23 Mar 1976", "Human Rights Committee"],
        ]),
        body("Entry into force dates are those given by OHCHR for each treaty body. Together the UDHR and "
             "the two Covenants are often called the <strong>International Bill of Human Rights</strong>.",
             sm=True),
    ]),

    C("ICCPR", "What the civil and political Covenant protects", [
        tw([panel("cyan", "Selected articles", [bullets([
                "Art 6: right to life",
                "Art 7: no torture or cruel treatment",
                "Art 9: liberty and security, no arbitrary arrest",
                "Art 14: fair trial",
                "Art 17: privacy",
                "Art 19: opinion and expression",
                "Arts 21 and 22: assembly and association",
                "Art 26: equality before the law"], sm=True)])],
           [panel("indigo", "How it is framed", [body(
                "The ICCPR obliges each state to respect and ensure the rights immediately, without "
                "discrimination, and to provide an effective remedy (Article 2). Some rights can be "
                "limited for listed reasons such as public order, but only by law and only as far as "
                "necessary. Article 4 allows derogation in a public emergency, but never from the right to "
                "life or the ban on torture.", sm=True)])]),
        hbox("For civic space work (Section 09), Articles 19, 21 and 22 are the starting point, and the "
             "test is always the same: is a restriction provided by law, for a legitimate aim, and "
             "necessary?", "amber"),
    ]),

    C("ICESCR", "What the economic and social Covenant protects", [
        tw([panel("green", "Selected articles", [bullets([
                "Arts 6 and 7: work and just conditions of work",
                "Art 8: trade unions and the right to strike",
                "Art 9: social security",
                "Art 11: adequate standard of living, food, housing",
                "Art 12: highest attainable standard of health",
                "Arts 13 and 14: education, free primary education"], sm=True)])],
           [panel("amber", "Progressive realisation", [body(
                "Article 2(1) asks each state to take steps, to the maximum of its available resources, to "
                "achieve the rights progressively. That wording is often misread as permission to wait. It "
                "obliges a state to move forward, to avoid going backwards without justification, and to "
                "meet minimum core levels and non-discrimination at once.", sm=True)])]),
        hbox("Progressive realisation gives monitoring a shape: a programme can ask whether budgets, "
             "coverage and quality are moving in the right direction, and whether the poorest are reached "
             "first or last.", "green"),
    ]),

    C("Minimum core", "What a state must do now, whatever its resources", [
        body("The Committee on Economic, Social and Cultural Rights reads the ICESCR as containing a "
             "<strong>minimum core</strong> of each right that applies immediately: basic food to be free "
             "from hunger, essential primary health care, basic shelter, and the most basic forms of "
             "education. A state that fails to meet these has to show that it used all the resources at its "
             "disposal as a matter of priority."),
        table(["Obligation", "Immediate or progressive", "Illustration in South Asia"], [
            ["Non-discrimination", "Immediate", "A ration scheme cannot exclude a caste or religious group"],
            ["Taking steps", "Immediate", "A plan, a budget line and a law or scheme must exist"],
            ["No unjustified backward steps", "Immediate", "Cutting coverage needs strong justification"],
            ["Full realisation", "Progressive", "Universal secondary education over time"],
        ]),
        hbox("Development finance is where this test becomes concrete. Budget analysis (see Public Finance "
             "&amp; Budgeting 101) is one of the strongest rights tools a programme has.", "indigo"),
    ]),

    C("Limits and balance", "When rights can be limited, and when they cannot", [
        body("Very few rights are absolute. Freedom from torture and slavery cannot be limited at all. "
             "Most other rights can be restricted, but international law sets conditions. Indian courts "
             "apply similar ideas through Article 19's reasonable restrictions and, since Puttaswamy (2017), "
             "through a proportionality test."),
        flow(["LAWFUL: the restriction is set out in law",
              "LEGITIMATE AIM: such as public order, health, the rights of others",
              "NECESSARY: there is a pressing need",
              "PROPORTIONATE: the least restrictive option that works"]),
        tw(pp("cyan", "Absolute", "No torture, no slavery, no punishment under a law passed after the act. "
              "Not even an emergency allows these."),
           pp("amber", "Qualified", "Expression, assembly, movement, privacy. Restrictions must pass all four "
              "steps above, and courts check them.")),
    ]),

    C("Soft law", "Declarations, principles and general comments", [
        body("Alongside treaties sits a body of texts that do not bind on their own but guide how treaties "
             "are read. Practitioners meet these constantly in donor documents and in court arguments."),
        table(["Instrument", "Year", "Why it matters"], [
            ["Vienna Declaration and Programme of Action", "1993", "Universality and indivisibility"],
            ["Paris Principles on national institutions", "1993 (GA res 48/134)",
             "Standards for bodies like India's NHRC"],
            ["UN Common Understanding on the rights-based approach", "2003", "How UN agencies programme"],
            ["UN Guiding Principles on Business and Human Rights", "2011", "Duties of states and companies"],
            ["Treaty body general comments", "Ongoing", "Authoritative readings of each treaty article"],
        ]),
        hbox("Indian courts have read such instruments into fundamental rights where no Indian law "
             "conflicts with them, as the Supreme Court did with CEDAW in Vishaka (1997). Soft law can "
             "become hard law through that route.", "green"),
    ]),
]

# ===================== SECTION 03: TREATIES AND RATIFICATION =====================
S03 = [
    D("03", "Section Three", "Core treaties and South Asia's ratification record"),

    C("The nine core treaties", "The UN's nine core human rights treaties", [
        body("OHCHR lists nine core treaties, each with a committee of independent experts. A tenth body, "
             "the Subcommittee on Prevention of Torture, works under the optional protocol to the torture "
             "convention. Knowing the acronyms helps when reading UN reports on any South Asian country."),
        table(["Short name", "Full name", "Committee"], [
            ["CERD", "Elimination of All Forms of Racial Discrimination (1965)", "CERD"],
            ["ICCPR", "Civil and Political Rights (1966)", "Human Rights Committee"],
            ["ICESCR", "Economic, Social and Cultural Rights (1966)", "CESCR"],
            ["CEDAW", "Elimination of Discrimination against Women (1979)", "CEDAW"],
            ["CAT", "Against Torture (1984)", "CAT"],
            ["CRC", "Rights of the Child (1989)", "CRC"],
            ["CMW", "Rights of All Migrant Workers (1990)", "CMW"],
            ["CRPD", "Rights of Persons with Disabilities (2006)", "CRPD"],
            ["CED", "Protection from Enforced Disappearance (2006)", "CED"],
        ]),
    ], compact=True),

    C("Signing and ratifying", "Signature, ratification and accession are different acts", [
        body("A state that <strong>signs</strong> a treaty shows intent and must not defeat its object and "
             "purpose, but is not yet bound. It becomes a party by <strong>ratification</strong> (after "
             "signing) or <strong>accession</strong> (joining without having signed). The OHCHR database "
             "marks accession with an (a). India acceded to both Covenants on 10 April 1979; it never "
             "signed them first."),
        tw(pp("cyan", "Signed only", "India signed the Convention against Torture on 14 October 1997 and "
              "the Convention on Enforced Disappearance on 6 February 2007. As of October 2026 it has "
              "ratified neither, according to the OHCHR database."),
           pp("green", "Ratified or acceded", "India is a party to CERD, ICCPR, ICESCR, CEDAW, CRC and CRPD, "
              "and to the two optional protocols to the CRC on armed conflict and on sale of children.")),
        hbox("At India's 2022 Universal Periodic Review, the first recommendation listed asked it to ratify "
             "the instruments it has signed, particularly the torture convention (UN doc A/HRC/52/11, "
             "para 151.1).", "amber"),
    ]),

    C("India's record", "India and the core treaties", [
        table(["Treaty", "India's status", "Date"], [
            ["CERD", "Ratified", "3 Dec 1968"],
            ["ICCPR", "Acceded", "10 Apr 1979"],
            ["ICESCR", "Acceded", "10 Apr 1979"],
            ["CEDAW", "Ratified", "9 Jul 1993"],
            ["CRC", "Acceded", "11 Dec 1992"],
            ["CRPD", "Ratified", "1 Oct 2007"],
            ["CAT", "Signed, not ratified", "Signed 14 Oct 1997"],
            ["CED", "Signed, not ratified", "Signed 6 Feb 2007"],
            ["CMW", "Not signed", "None"],
        ]),
        body("Source: " + OHCHR_TB + ". India has not accepted any individual complaints procedure: the "
             "database records NO for the first optional protocol to the ICCPR, the CEDAW protocol and "
             "others. A person in India therefore cannot take an individual complaint to a UN treaty body.",
             sm=True),
    ], compact=True),

    C("Neighbours", "Ratification across South Asia", [
        table(["Treaty", "Bangladesh", "Nepal", "Pakistan", "Sri Lanka"], [
            ["ICCPR", "2000 (a)", "1991 (a)", "2010", "1980 (a)"],
            ["ICESCR", "1998 (a)", "1991 (a)", "2008", "1980 (a)"],
            ["CEDAW", "1984 (a)", "1991", "1996 (a)", "1981"],
            ["CAT", "1998 (a)", "1991 (a)", "2010", "1994 (a)"],
            ["CRC", "1990", "1990", "1990", "1991"],
            ["CRPD", "2007", "2010", "2011", "2016"],
            ["CMW", "2011", "Not party", "Not party", "1996 (a)"],
            ["CED", "2024 (a)", "Not party", "Not party", "2016"],
        ]),
        body("Year of ratification or accession (a). Source: " + OHCHR_TB + ". All four neighbours have "
             "joined the torture convention, which India has not. Bangladesh acceded to the Convention on "
             "Enforced Disappearance on 30 August 2024 and to the optional protocol to the torture "
             "convention on 17 July 2025.", sm=True),
    ], compact=True),

    C("Counting the record", "How many of the nine core treaties each state has joined", [
        tw([{"t": "chart", "canvas": "hrTreatyCount", "type": "bar",
             "title": "Core UN human rights treaties joined, out of nine",
             "source": OHCHR_TB,
             "data": {"labels": ["India", "Nepal", "Pakistan", "Bangladesh", "Sri Lanka"],
                      "datasets": [{"label": "Treaties joined", "data": [6, 7, 7, 9, 9],
                                    "backgroundColor": ["#F59E0B", "#0EA5E9", "#0EA5E9", "#10B981",
                                                        "#10B981"]}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{ legend:{ display:false } }, scales:{ x:{ beginAtZero:true, max:9, ticks:{ stepSize:1 } } } }"}}],
           [body("Bangladesh and Sri Lanka are party to all nine core treaties. Nepal and Pakistan are "
                 "party to seven, missing the migrant workers and enforced disappearance conventions. India "
                 "is party to six.", sm=True),
            body("A count is a crude measure. Ratification says nothing about practice, and some states with "
                 "full records have serious violations on file. The count is still useful: it shows which "
                 "UN committees can review a country at all, and which standards an advocate can cite as "
                 "binding.", sm=True)], ratio="a32"),
        hbox("For India, the missing torture convention matters most for programmes on policing, custody "
             "and prisons, where the Constitution and case law carry the load instead.", "amber"),
    ]),

    C("Reservations", "Reservations and declarations: joining on stated terms", [
        body("A state can join a treaty while excluding or modifying some provisions. A "
             "<strong>reservation</strong> excludes or changes the legal effect of a provision. An "
             "<strong>interpretative declaration</strong> states how the state reads it. The label a state "
             "uses does not settle which one it is; other states and treaty bodies look at the substance. "
             "A reservation that defeats the treaty's object and purpose is not permitted."),
        tw(pp("cyan", "Why states make them", "To fit the treaty to the constitution or to personal laws, to "
              "avoid a dispute clause, or to protect a policy such as reservations in public jobs."),
           pp("amber", "Why they matter to programmes", "A reservation marks where national law and the "
              "treaty diverge. That gap is often exactly where a programme on women's rights, detention or "
              "migration will run into trouble.")),
        hbox("Treaty bodies regularly ask states to withdraw reservations, and the UPR repeats the request. "
             "Tracking these recommendations is a low-cost advocacy task.", "indigo"),
    ]),

    C("India's declarations", "What India declared when it joined the Covenants", [
        table(["Provision", "India's declaration (UN Treaty Collection)"], [
            ["Article 1, both Covenants", "Self-determination applies only to peoples under foreign domination, "
             "not to sovereign states or a section of a people"],
            ["ICCPR Article 9", "Applied consistently with Article 22(3) to (7) of the Constitution; no "
             "enforceable right to compensation for unlawful arrest under Indian law"],
            ["ICCPR Article 13", "India reserves the right to apply its law relating to foreigners"],
            ["ICESCR 4 and 8; ICCPR 12, 19(3), 21, 22", "Applied in conformity with Article 19 of the "
             "Constitution"],
            ["ICESCR Article 7(c)", "Applied in conformity with Article 16(4) of the Constitution"],
        ]),
        body("Article 22(3) to (7) is the preventive detention clause. Since Nilabati Behera (1993) and "
             "later cases, Indian courts have in fact awarded compensation for custodial violations under "
             "Article 32, so the domestic position has moved past the declaration's second sentence.",
             sm=True),
    ], compact=True),

    C("CEDAW reservations", "Personal law and the CEDAW reservations in South Asia", [
        table(["State", "Reservation or declaration on CEDAW (UN Treaty Collection)"], [
            ["India", "Declarations on Arts 5(a) and 16(1): non-interference in the personal affairs of any "
             "community without its initiative and consent; on Art 16(2): compulsory registration of "
             "marriages is not practical; reservation to Art 29(1) (disputes)"],
            ["Bangladesh", "Does not consider binding Art 2 and Art 16(1)(c), as they conflict with Sharia "
             "law"],
            ["Pakistan", "Accession subject to the Constitution of Pakistan; reservation to Art 29(1)"],
        ]),
        body("Article 2 is CEDAW's core obligation to eliminate discrimination through law and policy, and "
             "Article 16 covers equality in marriage and family life. These reservations are where the "
             "treaty meets religious personal law, which governs marriage, divorce and inheritance for "
             "most people in the region. Programmes on child marriage, maintenance or inheritance work "
             "directly in this gap; Gender &amp; Development 101 takes it further.", sm=True),
    ], compact=True),
]

# ===================== SECTION 04: UN MACHINERY =====================
S04 = [
    D("04", "Section Four", "The UN machinery: Council, UPR, treaty bodies, special procedures"),

    C("Human Rights Council", "The Human Rights Council, created in 2006", [
        body("The General Assembly created the <strong>Human Rights Council</strong> by resolution 60/251 "
             "of 15 March 2006, replacing the Commission on Human Rights. It is the main intergovernmental "
             "UN body on human rights and meets in Geneva. Its members are states, so its decisions are "
             "political as well as legal."),
        table(["Feature", "Rule under GA resolution 60/251"], [
            ["Members", "47 states, elected individually by secret ballot by a majority of the General "
             "Assembly"],
            ["Seats for the Asian group", "13 (African 13, Eastern European 6, Latin American and "
             "Caribbean 8, Western European and others 7)"],
            ["Term", "Three years; no immediate re-election after two consecutive terms"],
            ["Suspension", "The General Assembly can suspend a member that commits gross and systematic "
             "violations, by a two-thirds majority of those present and voting"],
        ]),
        hbox("Members are themselves reviewed under the Universal Periodic Review during their term, as "
             "paragraph 9 of the resolution requires.", "cyan"),
    ]),

    C("Universal Periodic Review", "How the Universal Periodic Review works", [
        body("Resolution 60/251 told the Council to undertake a <strong>universal periodic review</strong> "
             "of every UN member state, based on objective and reliable information. Every state is "
             "reviewed in turn by other states, cycle after cycle. The review is a "
             "conversation between governments, but it draws on reports written by the UN and by civil "
             "society."),
        flow(["INPUTS: national report, UN compilation, stakeholder summary",
              "DIALOGUE: other states question the delegation in Geneva",
              "RECOMMENDATIONS: listed in the Working Group report",
              "RESPONSE: the state supports or notes each one",
              "FOLLOW-UP: a mid-term report, then the next cycle"]),
        tw(pp("cyan", "Its strength", "Universality. Every state is reviewed, including those that have "
              "joined few treaties, so India is questioned on torture even without CAT."),
           pp("amber", "Its limit", "States review states. Recommendations range from sharp to vague, and "
              "a state can note (decline) any recommendation without explanation.")),
    ]),

    C("India's fourth review", "India's 2022 review in numbers", [
        tw([stats([
                {"num": "339", "label": "recommendations made to India", "color": "cyan",
                 "source": "UN doc A/HRC/52/11, para 151"},
                {"num": "130", "label": "delegations took the floor", "color": "indigo",
                 "source": "UN doc A/HRC/52/11, para 11"},
            ], cols=2),
            body("India was reviewed at the 41st session of the UPR Working Group, on 10 November 2022. Its "
                 "delegation was headed by the Solicitor General, Tushar Mehta. The Human Rights Council "
                 "adopted the outcome at its 52nd session in 2023.", sm=True)],
           [{"t": "chart", "canvas": "hrUprIndia", "type": "doughnut",
             "title": "India's response to the 339 recommendations",
             "source": "UN doc A/HRC/52/11/Add.1 (27 February 2023), counted from India's table of positions",
             "data": {"labels": ["Supported (221)", "Noted (111)", "Marked rejected (7)"],
                      "datasets": [{"data": [221, 111, 7],
                                    "backgroundColor": ["#10B981", "#F59E0B", "#EF4444"]}]},
             "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } } }"}}]),
        hbox("Noted recommendations included ratifying the torture convention (151.1 and 151.2 were both "
             "noted). These are a ready list of issues on which the government has not yet committed.",
             "amber"),
    ]),

    C("Using the UPR", "How an Indian NGO can use the review cycle", [
        body("Most development organisations never engage with Geneva, and they do not need to travel to "
             "use the UPR. The recommendations a government supports are commitments it has made in "
             "public, and they can be quoted back to it in district and state meetings."),
        table(["Step", "What a programme team can do", "Effort"], [
            ["Before the review", "Contribute evidence to a coalition stakeholder submission", "Medium"],
            ["During the review", "Brief friendly embassies on two or three precise recommendations", "Medium"],
            ["After adoption", "Extract supported recommendations relevant to your sector", "Low"],
            ["Between reviews", "Track progress against them; publish a short shadow update", "Low"],
            ["In meetings", "Cite the supported recommendation by number in letters to officials", "Low"],
        ]),
        hbox("Illustrative: a nutrition programme in Odisha finds a supported recommendation on child "
             "malnutrition and cites its number in a letter to the district collector asking for anganwadi "
             "repairs. The letter now rests on a national commitment.", "green"),
    ]),

    C("Treaty bodies", "Treaty bodies: expert committees that review states", [
        body("Each core treaty has a committee of independent experts. OHCHR describes ten treaty bodies, "
             "whose members are elected by states parties for fixed renewable terms of four years. They do "
             "four main things, and practitioners can feed into each one."),
        tw([panel("cyan", "What treaty bodies do", [bullets([
                "Review periodic state reports and issue concluding observations",
                "Write general comments that explain treaty articles",
                "Hear individual complaints, where a state has accepted this",
                "Some run inquiries into grave or systematic violations"], sm=True)])],
           [panel("green", "Where NGOs fit", [bullets([
                "Submit alternative (shadow) reports before a review",
                "Use concluding observations as a benchmark in advocacy",
                "Quote general comments to define a right's content",
                "Follow up on the priority recommendations"], sm=True)])]),
        hbox("Reviews of any one state under any one treaty come years apart. Concluding observations stay "
             "relevant between reviews and are a strong reference in policy dialogue.", "amber"),
    ]),

    C("Individual complaints", "Who in South Asia can take a complaint to a UN committee", [
        table(["Procedure", "India", "Bangladesh", "Nepal", "Pakistan", "Sri Lanka"], [
            ["ICCPR first optional protocol", "No", "No", "Yes (1991)", "No", "Yes (1997)"],
            ["CEDAW optional protocol", "No", "Yes (2000)", "Yes (2007)", "No", "Yes (2002)"],
            ["CRPD optional protocol", "No", "Yes (2008)", "Yes (2010)", "No", "No"],
            ["CAT Article 22", "Not party", "No", "No", "No", "Yes (2016)"],
        ]),
        body("Source: " + OHCHR_TB + ", acceptance of individual complaints procedures; the CEDAW row for "
             "Bangladesh is from the UN Treaty Collection, which records it as a party to the CEDAW optional "
             "protocol since 6 September 2000, with an Article 10 opt-out from the inquiry procedure only. "
             "A complaint can "
             "only be brought after domestic remedies are exhausted, and the committee's views are "
             "recommendations, but states that have accepted the procedure are expected to respond in "
             "good faith.", sm=True),
        hbox("For India the practical consequence is clear: rights violations are remedied at home, through "
             "courts, commissions and administrative grievance routes. Section 07 covers those.", "indigo"),
    ], compact=True),

    C("Special procedures", "Special rapporteurs and working groups", [
        stats([
            {"num": "44", "label": "thematic mandates, as of August 2026", "color": "cyan",
             "source": "OHCHR, Special Procedures of the Human Rights Council"},
            {"num": "12", "label": "country mandates, as of August 2026", "color": "indigo",
             "source": "OHCHR, Special Procedures of the Human Rights Council"},
            {"num": "6 yrs", "label": "maximum tenure; mandate-holders are unpaid", "color": "green",
             "source": "OHCHR, Special Procedures of the Human Rights Council"},
        ]),
        body("Special procedures are independent experts appointed by the Council on themes (food, housing, "
             "human rights defenders, extreme poverty) or countries. They visit countries when invited, send "
             "communications to governments about individual cases, and report every year. Anyone can send "
             "them information through OHCHR's online submission tool.", sm=True),
        hbox("Rapporteurs' thematic reports are a free, authoritative source of standards. A housing "
             "programme can rely on the rapporteur on adequate housing; a land programme on the guidance on "
             "development-based evictions.", "green"),
    ]),

    C("Comparing mechanisms", "Which UN mechanism to use for which purpose", [
        table(["Mechanism", "Basis", "Who reviews", "Output", "Best use for a programme"], [
            ["Human Rights Council", "UN Charter, GA res 60/251", "States", "Resolutions",
             "Rarely direct; follow debates"],
            ["UPR", "GA res 60/251", "States", "Recommendations", "Hold government to commitments"],
            ["Treaty bodies", "Each treaty", "Independent experts", "Concluding observations",
             "Sector benchmarks, shadow reports"],
            ["Special procedures", "Council resolutions", "Independent experts", "Reports, letters",
             "Urgent cases, standards"],
            ["Individual complaints", "Optional protocols", "Experts", "Views on a case",
             "Only where accepted (not India)"],
        ]),
        hbox("The UN system persuades; it rarely compels. It works best when it supports a domestic "
             "campaign that already has evidence, allies and a legal route at home.", "amber"),
    ], compact=True),
]

# ===================== SECTION 05: HRBA =====================
S05 = [
    D("05", "Section Five", "The human rights-based approach to development"),

    C("The Common Understanding", "2003: the UN agrees what a rights-based approach means", [
        body("UN agencies needed one shared meaning for the phrase \"rights-based approach\" across "
             "their country work. In 2003 they agreed a short statement, <em>The Human Rights Based Approach to "
             "Development Cooperation: Towards a Common Understanding Among UN Agencies</em>. It has three "
             "points, and every rights-based programme design can be checked against them."),
        flow(["GOAL: programmes should further the realisation of human rights",
              "STANDARDS: human rights standards and principles guide all programming, in all phases",
              "CAPACITY: build duty-bearers' capacity to meet obligations and rights-holders' to claim them"]),
        quote("All programmes of development co-operation, policies and technical assistance should further "
              "the realisation of human rights as laid down in the Universal Declaration of Human Rights and "
              "other international human rights instruments.",
              "UN Common Understanding (2003), first point, as quoted by HREA"),
    ]),

    C("Six principles", "The human rights principles a programme applies", [
        table(["Principle", "Meaning (UNFPA wording)", "Question for a programme"], [
            ["Universality and inalienability", "All people everywhere are entitled to them",
             "Who is outside our coverage, and why?"],
            ["Indivisibility", "All rights have equal status, with no hierarchy",
             "Are we trading one right off against another?"],
            ["Interdependence and interrelatedness", "Realising one right often depends on others",
             "Which other rights block or enable our outcome?"],
            ["Equality and non-discrimination", "No discrimination on any status",
             "Are results disaggregated by caste, gender, disability?"],
            ["Participation and inclusion", "Right to take part in and get information on decisions",
             "Do communities shape design, or only receive it?"],
            ["Accountability and rule of law", "Duty-bearers are answerable",
             "Is there a grievance route that works?"],
        ]),
        body("Principle names and short definitions from UNFPA's statement of human rights principles.",
             sm=True),
    ], compact=True),

    C("Needs and rights", "What changes when a programme moves from needs to rights", [
        tw([panel("amber", "A needs-based framing", [bullets([
                "People are beneficiaries who receive help",
                "Success means targets met and goods delivered",
                "Priorities set by the agency and its funder",
                "Exclusion is a coverage gap to close later",
                "The NGO is accountable to its donor"], sm=True)])],
           [panel("green", "A rights-based framing", [bullets([
                "People are rights-holders who can claim",
                "Success also means duty-bearers perform better",
                "Priorities include the most excluded first",
                "Exclusion is a possible breach of equality",
                "Accountability runs to communities and the state"], sm=True)])]),
        body("Both framings deliver services, and a rights-based programme still has to deliver. The "
             "difference shows up in what the programme measures, whom it reports to, and what happens "
             "after it closes. A rights framing asks whether the public system will keep delivering once "
             "the project funding ends.", sm=True),
    ]),

    C("A working method", "Three analyses at the start of a rights-based design", [
        body("A common working method for rights-based design uses three linked analyses. They are "
             "a method, and teams adapt them; none of them is fixed in law."),
        flow(["CAUSES: why is the right unrealised? immediate, underlying, structural",
              "ROLES: who are the rights-holders and the duty-bearers for each cause?",
              "CAPACITY GAPS: what does each lack: knowledge, authority, resources, will?"]),
        table(["Analysis", "Illustrative finding: girls leaving school in Class 8"], [
            ["Causes", "No secondary school within 5 km; safety on the road; household work"],
            ["Roles", "Girls and parents; school management committee; block education office; state"],
            ["Capacity gaps", "Parents unaware of entitlements; block office lacks a transport budget"],
        ]),
        hbox("Illustrative example. The point of the method is to design activities for both sides of "
             "the relationship: for communities and for officials.", "indigo"),
    ], compact=True),

    C("Participation and accountability", "Making participation and accountability real", [
        body("Participation and accountability are the two principles programmes most often claim and "
             "least often show. Indian law gives several hooks that a programme can use without inventing "
             "new structures."),
        tw(pp("cyan", "Participation hooks", "Gram sabhas under state panchayat laws; school management "
              "committees under section 21 of the RTE Act 2009; ward committees in cities; consultation "
              "requirements in forest and land laws."),
           pp("green", "Accountability hooks", "Right to Information Act 2005 requests, answered within 30 "
              "days (48 hours where life or liberty is at stake, section 7(1)); public hearings; "
              "grievance portals; state human rights commissions.")),
        hbox("A test for any programme: could a rights-holder in your area find out what they are entitled "
             "to, complain if they do not get it, and get an answer? If any link is missing, building it "
             "is rights-based work.", "amber"),
    ]),

    C("Illustrative case", "Redesigning a water programme with a rights lens", [
        body("Illustrative case (hypothetical figures). A trust installs hand pumps in 40 hamlets in a drought-prone district. A "
             "rights review finds three problems: pumps in two Dalit hamlets were sited at the dominant-"
             "caste end; repairs depend on the trust; and the panchayat has a water budget it never used "
             "in these hamlets."),
        table(["Before", "After the rights review"], [
            ["Trust picks pump sites", "Hamlet meetings with women and Dalit households choose sites"],
            ["Trust repairs pumps", "Panchayat repair budget used; the trust trains a local mechanic"],
            ["Reports to donor on pumps installed", "Reports also on access by caste and gender"],
            ["Complaints go to field staff", "Complaints also go to the panchayat, with an RTI if unanswered"],
        ]),
        hbox("The service is the same. What changed is who decides, who pays over time, and who is "
             "answerable. Social Margins 101 covers caste exclusion in services in more depth.", "green"),
    ], compact=True),

    C("Critiques", "Fair criticisms of the rights-based approach", [
        body("Four criticisms of the rights-based approach deserve a straight answer, because each one "
             "points to a way the approach can fail in practice."),
        tw(pp("amber", "Relabelling", "A proposal can add the word \"rights\" while changing "
              "nothing in design or measurement. The test is whether activities, indicators and reporting "
              "lines changed."),
           pp("red", "Legalism", "Rights claims can push conflicts into courts that are slow and costly, "
              "and they can favour those with lawyers. Political organising often wins more than "
              "litigation.")),
        tw(pp("indigo", "The state as violator", "Where the duty-bearer is also the main threat, as in some "
              "conflict areas, \"building state capacity\" can strengthen the wrong actor. Programmes need "
              "a risk analysis first."),
           pp("cyan", "Resource limits", "Rights language can promise more than a budget can deliver. "
              "Progressive realisation and the minimum core give a more honest frame than absolute "
              "promises.")),
    ]),
]

# ===================== SECTION 06: CONSTITUTION =====================
S06 = [
    D("06", "Section Six", "Rights in the Indian Constitution"),

    C("Part III", "Fundamental rights in Part III", [
        table(["Article", "Right", "Note for practitioners"], [
            ["14", "Equality before law and equal protection", "Basis for challenging arbitrary action"],
            ["15, 16", "No discrimination; equal opportunity in public jobs", "Allow special provisions"],
            ["17", "Untouchability abolished", "Enforced through criminal law"],
            ["19", "Speech, assembly, association, movement, occupation", "Citizens only; reasonable "
             "restrictions"],
            ["21", "Life and personal liberty", "Expanded by courts; see next slides"],
            ["21A", "Free and compulsory education, ages 6 to 14", "Inserted in 2002"],
            ["23, 24", "No trafficking or forced labour; no child under 14 in factories, mines, "
             "hazardous work", "Apply to private actors too"],
            ["25 to 30", "Religion; cultural and educational rights of minorities", ""],
            ["32", "Right to move the Supreme Court to enforce Part III", "Itself a fundamental right"],
        ]),
    ], compact=True),

    C("Part IV", "Directive principles in Part IV", [
        body("Part IV sets out goals the state must pursue. Article 37 makes their status explicit:"),
        quote("The provisions contained in this Part shall not be enforceable by any court, but the "
              "principles therein laid down are nevertheless fundamental in the governance of the country "
              "and it shall be the duty of the State to apply these principles in making laws.",
              "Constitution of India, Article 37"),
        tw(pp("green", "Directives a programme meets often", "Art 39A equal justice and free legal aid; "
              "Art 41 right to work, education and public assistance within economic capacity; Art 42 just "
              "and humane conditions of work and maternity relief; Art 46 educational and economic "
              "interests of SCs, STs and weaker sections; Art 47 nutrition and public health."),
           pp("cyan", "Why they still matter", "Many welfare laws (food security, legal aid, maternity "
              "benefit) are the state applying these principles. Courts also read them into Part III, which "
              "is the subject of the next slide.")),
    ]),

    C("Harmony", "How the courts joined Part III and Part IV", [
        body("Early cases treated Parts III and IV as separate and sometimes in conflict. From the 1980s the "
             "Supreme Court read them together. Two passages show the shift."),
        quote("The Indian Constitution is founded on the bed-rock of the balance between Parts III and IV. "
              "To give absolute primacy to one over the other is to disturb the harmony of the "
              "Constitution.",
              "Minerva Mills Ltd v Union of India (1980), headnote"),
        quote("This right to live with human dignity enshrined in Article 21 derives its life breath from "
              "the Directive Principles of State Policy and particularly clauses (e) and (f) of Article 39 "
              "and Articles 41 and 42.",
              "Bandhua Mukti Morcha v Union of India (1983, reported 1984), Bhagwati J"),
        hbox("This is how an unenforceable directive (such as Article 47 on nutrition) becomes enforceable "
             "in part: through a fundamental right that the directive helps define.", "green"),
    ]),

    C("From Gopalan to Maneka", "A.K. Gopalan (1950) to Maneka Gandhi (1978)", [
        tw(pp("amber", "A.K. Gopalan v State of Madras (1950)", "The Court read each fundamental right as "
              "a separate compartment. \"Procedure established by law\" in Article 21 meant any procedure a "
              "valid law set out, fair or not. Puttaswamy (2017) later described this as treating rights as "
              "isolated silos."),
           pp("green", "Maneka Gandhi v Union of India (1978)", "A seven-judge bench, deciding a challenge to "
              "the impounding of a passport, held that Articles 14, 19 and 21 must be read together, and "
              "that the procedure under Article 21 must itself be reasonable.")),
        quote("The procedure contemplated by Article 21 must answer the test of reasonableness in order to be "
              "in conformity with Article 14. It must be right and just and fair and not arbitrary, fanciful "
              "or oppressive.",
              "Maneka Gandhi v Union of India, AIR 1978 SC 597"),
        hbox("Maneka opened the door to every later expansion of Article 21. After 1978, a law that takes "
             "away life or liberty must also be fair.", "cyan"),
    ]),

    C("Article 21 expands", "What Article 21 has come to include", [
        table(["Case", "Year", "What the Court read into Article 21"], [
            ["Hussainara Khatoon v Home Secretary, Bihar", "1979",
             "Speedy trial; release of undertrials on personal bond"],
            ["Francis Coralie Mullin v Administrator, UT of Delhi", "1981",
             "Life with human dignity, including adequate nutrition, clothing and shelter"],
            ["Olga Tellis v Bombay Municipal Corporation", "1985", "Right to livelihood"],
            ["Unni Krishnan v State of Andhra Pradesh", "1993",
             "Free education up to age 14 (later Article 21A)"],
            ["Nilabati Behera v State of Orissa", "1993", "Compensation for death in police custody"],
            ["Paschim Banga Khet Mazdoor Samity v State of West Bengal", "1996",
             "Emergency medical treatment in government hospitals"],
            ["K.S. Puttaswamy v Union of India", "2017", "Privacy"],
        ]),
        body("Each entry was read from the judgment text on Indian Kanoon. Together they turned a short "
             "guarantee against unlawful detention into the main source of social rights in Indian law.",
             sm=True),
    ], compact=True),

    C("Olga Tellis", "Olga Tellis (1985): livelihood and the pavement dwellers of Bombay", [
        body("Pavement and slum dwellers in Bombay challenged their eviction by the municipal corporation. "
             "A five-judge bench led by Chief Justice Chandrachud held that the right to life includes the "
             "right to livelihood."),
        quote("An equally important facet of that right is the right to livelihood because, no person can "
              "live without the means of living, that is, the means of livelihood.",
              "Olga Tellis v Bombay Municipal Corporation, (1985) 3 SCC 545"),
        tw(pp("cyan", "What the Court decided", "It did not hold that every eviction is unlawful. It held "
              "that the power to remove encroachments \"without notice\" must be exercised reasonably, "
              "fairly and justly, so fair procedure applies before people lose their homes."),
           pp("green", "Why it matters for programmes", "Livelihood and housing programmes in informal "
              "settlements still cite Olga Tellis on notice and hearing. It also shows the limits of "
              "litigation: a right recognised, an outcome that still allowed removal.")),
    ]),

    C("Puttaswamy", "Puttaswamy (2017): privacy as a fundamental right", [
        body("A nine-judge bench held unanimously that privacy is protected by Article 21 and the freedoms in "
             "Part III, and overruled M.P. Sharma and the majority in Kharak Singh to the extent they said "
             "otherwise. Justice Chandrachud's opinion set a three-part test for any intrusion: a law, a "
             "legitimate state aim, and proportionality between the aim and the means."),
        tw(pp("cyan", "For data-heavy programmes", "Surveys, beneficiary databases, biometric enrolment and "
              "case files all touch privacy. Consent, purpose limits and data minimisation are now "
              "constitutional questions as well as ethical ones."),
           pp("indigo", "The statute that followed", "The Digital Personal Data Protection Act 2023 and the "
              "DPDP Rules 2025 come into force in phases under a notification of 13 November 2025. The duties "
              "of data fiduciaries, including consent and notice, apply from 13 May 2027, and so does "
              "section 17(2)(b), which exempts processing for research and statistics when its conditions "
              "are met.")),
        hbox("Data Protection &amp; the DPDP Act 101 and Digital Rights &amp; AI 101 take this further.",
             "green"),
    ]),

    C("Education as a right", "From Unni Krishnan to Article 21A and the RTE Act", [
        flow(["1993: Unni Krishnan reads free education to age 14 into Article 21",
              "2002: Constitution (86th Amendment) inserts Article 21A",
              "2009: Right of Children to Free and Compulsory Education Act",
              "1 April 2010: RTE Act comes into force"]),
        tw(pp("green", "What the RTE Act requires", "Free and compulsory elementary education for children "
              "aged 6 to 14. Private unaided schools must admit at least 25 per cent of Class I from weaker "
              "sections and disadvantaged groups in the neighbourhood (section 12(1)(c)). School "
              "management committees, at least three-quarters parents or guardians, give parents a formal "
              "role (section 21)."),
           pp("amber", "Where the right meets reality", "The 25 per cent quota works only if families know "
              "about it, can complete the application and can appeal a refusal, and if states reimburse "
              "schools. Helping families apply and appeal is direct rights work, as Inclusive Education "
              "101 explains.")),
        hbox("Unni Krishnan held the right is limited, after age 14, by the economic capacity of the state, "
             "drawing on Article 41. Progressive realisation in Indian form.", "indigo"),
    ]),

    C("International law at home", "How treaties enter Indian courts", [
        body("India follows a dualist practice: a treaty does not change domestic law until Parliament "
             "legislates, and Article 253 gives Parliament power to make laws to implement any treaty. Courts "
             "have built a second route. Article 51(c) directs the state to respect international law and "
             "treaty obligations, and the Supreme Court uses treaties to interpret fundamental rights."),
        quote("Any International Convention not inconsistent with the fundamental rights and in harmony with "
              "its spirit must be read into these provisions to enlarge the meaning and content thereof.",
              "Vishaka v State of Rajasthan (1997)"),
        tw(pp("cyan", "Vishaka in practice", "With no statute on sexual harassment at work, the Court drew on "
              "CEDAW to frame guidelines binding until Parliament acted. Parliament later passed the Sexual "
              "Harassment of Women at Workplace Act 2013."),
           pp("amber", "Its limit", "The route only works where Indian law is silent. A clear statute "
              "prevails over a treaty in an Indian court.")),
    ]),
]

# ===================== SECTION 07: COURTS, PIL, NHRIs =====================
S07 = [
    D("07", "Section Seven", "Courts, public interest litigation and human rights commissions"),

    C("Public interest litigation", "How public interest litigation opened the courts", [
        body("Until the late 1970s, only a person who had suffered a specific legal injury could go to "
             "court. Public interest litigation (PIL) relaxed that rule so that anyone acting in good faith "
             "could bring a case for people too poor or too marginalised to bring it themselves. In S.P. "
             "Gupta v President of India (1981), Justice Bhagwati set out the principle:"),
        quote("Any member of the public acting bona fide and having sufficient interest can maintain an "
              "action for redressal of such public wrong or public injury.",
              "S.P. Gupta v President of India, 1981 Supp SCC 87"),
        tw(pp("cyan", "Letters as petitions", "Courts treated letters as writ petitions. Nilabati Behera "
              "(1993), on a death in police custody, began with a mother's letter to the Supreme Court."),
           pp("green", "Undertrials", "Hussainara Khatoon (1979) concerned undertrials held in Bihar jails for "
              "years for offences that would not have drawn more than a few months' sentence. The Court "
              "ordered their release on personal bond.")),
    ]),

    C("PIL tools", "What courts can do in a public interest case", [
        table(["Tool", "What it is", "Example"], [
            ["Continuing mandamus", "The court keeps the case open and issues orders over years",
             "PUCL v Union of India, WP (C) 196 of 2001 (right to food)"],
            ["Court commissioners", "Officers appointed to monitor compliance and report",
             "Used in the right to food case"],
            ["Guidelines pending a law", "Binding rules until Parliament legislates",
             "Vishaka (1997) on sexual harassment at work"],
            ["Compensation", "Monetary relief for breach of a fundamental right",
             "Nilabati Behera (1993), custodial death"],
            ["Fact-finding", "Commissions to visit and report on conditions",
             "Bandhua Mukti Morcha (1984), stone quarries in Faridabad"],
        ]),
        body("In Dipika Jagatram Sahani v Union of India (2021) the Supreme Court recalled that in "
             "PUCL, WP 196 of 2001, it had issued directions to protect the right to food of the poor, "
             "including children and women, and had pressed governments to run the ICDS scheme properly.",
             sm=True),
    ], compact=True),

    C("Using courts well", "When litigation helps a programme, and when it does not", [
        tw([panel("green", "Litigation tends to help when", [bullets([
                "A clear legal entitlement is being denied",
                "Evidence is documented and affected people consent",
                "Many people face the same breach",
                "Administrative routes have been tried and failed",
                "A lawyer can follow the case for years"], sm=True)])],
           [panel("amber", "It tends to hurt when", [bullets([
                "Communities have not chosen it",
                "The case exposes complainants to retaliation",
                "An adverse ruling would set a bad precedent",
                "Officials could fix it with a letter or an RTI",
                "No one will follow up on compliance"], sm=True)])]),
        body("PIL has two weaknesses worth weighing. Courts are poorly placed to run welfare schemes for "
             "years, and affected people can become the subject of cases in which they have little voice. "
             "Development "
             "organisations should treat a court case as one tool within a wider strategy, decided with "
             "the people affected. Advocacy Basics 101 covers how litigation fits into a campaign.", sm=True),
    ]),

    C("The Protection of Human Rights Act", "The Protection of Human Rights Act 1993", [
        body("Parliament created the <strong>National Human Rights Commission (NHRC)</strong> and the "
             "framework for State Human Rights Commissions through the Protection of Human Rights Act 1993 "
             "(deemed in force from 28 September 1993). Its definition of human rights links the "
             "Constitution to the Covenants:"),
        quote("\"human rights\" means the rights relating to life, liberty, equality and dignity of the "
              "individual guaranteed by the Constitution or embodied in the International Covenants and "
              "enforceable by Courts in India.",
              "Protection of Human Rights Act 1993, section 2(1)(d)"),
        table(["Feature (as amended by Act 19 of 2019)", "Rule"], [
            ["Chairperson", "A former Chief Justice of India or Supreme Court judge (s3(2)(a))"],
            ["Members", "Includes a Supreme Court judge, a High Court Chief Justice and three members with "
             "human rights knowledge, at least one a woman (s3(2))"],
            ["Term", "Three years, or until age 70; eligible for reappointment (s6)"],
        ]),
    ], compact=True),

    C("NHRC powers and limits", "What the NHRC can and cannot do", [
        tw([panel("green", "Powers (sections 12 and 18)", [bullets([
                "Inquire suo motu, on a petition, or on a court's direction, into violations or negligence "
                "by a public servant",
                "Intervene in court proceedings with the court's approval",
                "Visit jails and other institutions where people are detained",
                "Recommend compensation, prosecution and interim relief",
                "Review laws and treaties, and promote research and awareness"], sm=True)])],
           [panel("red", "Limits", [bullets([
                "No inquiry into matters more than one year old (s36(2))",
                "For the armed forces, it can only seek a report from the Central Government and make "
                "recommendations (s19)",
                "Recommendations are not binding orders",
                "Cannot take up matters pending before another commission (s36(1))"], sm=True)])]),
        hbox("The one-year bar in section 36(2) is the rule most often missed in the field. Help people file "
             "early, and keep a dated record of the incident.", "amber"),
    ]),

    C("States and districts", "State commissions and human rights courts", [
        body("The same Act provides for <strong>State Human Rights Commissions</strong> (SHRCs), which "
             "handle complaints about matters in the state lists, and for <strong>Human Rights "
             "Courts</strong>. Under section 30, a state government may, with the concurrence of the High "
             "Court's Chief Justice, specify a Court of Session in each district as a Human Rights Court to "
             "give speedy trial of offences arising from human rights violations."),
        flow(["DOCUMENT: dates, names, medical and police papers",
              "FILE: with the SHRC or NHRC, within one year",
              "FOLLOW UP: request the report the commission called for",
              "ESCALATE: High Court writ if relief is refused"]),
        hbox("Since 2006 the NHRC can transfer a complaint to the commission of the state where it arose "
             "(section 13(6), inserted by Act 43 of 2006). Filing with the state commission first often "
             "saves time.",
             "cyan"),
    ]),

    C("Paris Principles", "The Paris Principles and international accreditation", [
        body("The General Assembly endorsed the <strong>Paris Principles</strong> on national human rights "
             "institutions in resolution 48/134 of 20 December 1993. They ask for as broad a mandate as "
             "possible, independence from government, and pluralist membership. The Global Alliance of "
             "National Human Rights Institutions (GANHRI) reviews institutions against them: A status means "
             "fully compliant, B status partially compliant."),
        tw(pp("amber", "India's NHRC", "Accredited A, but GANHRI's Sub-Committee on Accreditation deferred "
              "its re-accreditation in 2023 and 2024 and in March 2025 recommended a downgrade to B "
              "(GANHRI chart, 4 June 2026). The GANHRI Bureau rejected the NHRC's challenge in December "
              "2025, and the review was postponed to November 2026 (Human Rights Watch joint submission, "
              "1 October 2026)."),
           pp("cyan", "Why this matters", "Accreditation decides whether an institution can speak in its own "
              "right at the Human Rights Council. The concerns raised (independence, pluralism in "
              "appointments) are the same ones an NGO weighs when deciding where to file a complaint.")),
        hbox("Check the latest GANHRI decision before citing India's status: the November 2026 decision "
             "was pending as of October 2026.", "red"),
    ]),

    C("Neighbours' commissions", "National human rights institutions in the neighbourhood", [
        table(["Country", "Institution and legal basis", "GANHRI status"], [
            ["Nepal", "NHRC Nepal: statutory body from 2000; constitutional body under Art 131 of the "
             "Interim Constitution 2007 and Art 248 of the Constitution 2015", "A (October 2023, March 2025)"],
            ["Pakistan", "National Commission for Human Rights, NCHR Act 2012", "A (first session 2024)"],
            ["Sri Lanka", "Human Rights Commission of Sri Lanka, Act No. 21 of 1996, established 1997",
             "B from October 2022; A again from first session 2024"],
            ["Bangladesh", "NHRC under the NHRC Act 2009; members resigned November 2024; NHRC Ordinance "
             "2025 gazetted 9 November 2025", "B (2011, 2015)"],
        ]),
        body("Sources: GANHRI accreditation chart as of 4 June 2026; NHRC Nepal and HRCSL websites; NCHR "
             "website; Bangladesh Platform for SDGs timeline (2026) and Prothom Alo (10 December 2025), which "
             "reported the commission still not functioning. Statuses can change at any GANHRI session.",
             sm=True),
    ], compact=True),

    C("Neighbours' courts", "Constitutional routes to court in the neighbourhood", [
        table(["Country", "Provision", "What it allows"], [
            ["Bangladesh", "Constitution Art 102", "High Court Division, on the application of any person "
             "aggrieved, can give directions to enforce fundamental rights"],
            ["Pakistan", "Constitution Arts 199 and 184(3)", "High Court writs; Supreme Court orders on a "
             "question of public importance about fundamental rights"],
            ["Sri Lanka", "Constitution Art 126", "Supreme Court's exclusive jurisdiction over executive or "
             "administrative infringement; petition within one month"],
            ["Nepal", "Constitution Art 46, with Arts 133 and 144", "Right to constitutional remedy "
             "through the Supreme Court and High Courts"],
        ]),
        body("Texts from the Constitute Project editions of each constitution. Sri Lanka's one-month limit "
             "is short: a programme there needs a lawyer it can reach quickly, since the time runs from "
             "the infringement.", sm=True),
        hbox("Pakistan's Article 184(3), like India's PIL, lets the Supreme Court act directly on questions "
             "of public importance about fundamental rights. In every country here, check limitation "
             "periods before advising anyone.", "indigo"),
    ], compact=True),
]

# ===================== SECTION 08: ESR IN PRACTICE =====================
S08 = [
    D("08", "Section Eight", "Economic and social rights in practice"),

    C("Right to food", "The right to food: from a court case to a statute", [
        body("The right to food in India grew from <strong>PUCL v Union of India</strong> (WP (C) 196 of "
             "2001), in which the Supreme Court turned schemes such as mid-day meals and ICDS into "
             "entitlements through interim orders. Parliament then passed the "
             "<strong>National Food Security Act 2013</strong>."),
        table(["Entitlement under the NFSA 2013", "Section"], [
            ["Coverage up to 75% of the rural and 50% of the urban population", "s3(2)"],
            ["5 kg of foodgrains per person per month for priority households", "s3(1)"],
            ["35 kg per household per month for Antyodaya Anna Yojana households", "s3(1), proviso"],
            ["Free meals and maternity benefit of at least Rs 6,000 for pregnant and lactating women",
             "s4"],
            ["One free mid-day meal on school days for children aged 6 to 14", "s5(1)(b)"],
        ]),
        hbox("An entitlement in a statute can be claimed. A household wrongly left off the ration list has "
             "a grievance route under the Act, which a programme can help it use.", "green"),
    ], compact=True),

    C("Nutrition outcomes", "Child stunting in four South Asian countries", [
        tw([{"t": "chart", "canvas": "hrStunting", "type": "bar",
             "title": "Children under five who are stunted (%), latest DHS-type survey",
             "source": "India: NFHS-6 (2023-24) India fact sheet, IIPS, May 2026. Others: the DHS Program "
                       "API, indicator CN_NUTS_C_HA2: Pakistan PDHS 2017-18, Nepal NDHS 2022, Bangladesh "
                       "BDHS 2022",
             "data": {"labels": ["Pakistan 2017-18", "India 2023-24", "Nepal 2022", "Bangladesh 2022"],
                      "datasets": [{"label": "Stunted (%)", "data": [37.6, 29.3, 24.8, 23.6],
                                    "backgroundColor": ["#EF4444", "#F59E0B", "#0EA5E9", "#10B981"]}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{ legend:{ display:false } }, scales:{ x:{ beginAtZero:true, max:50 } } }"}}],
           [body("Stunting measures long-term undernutrition. India's 29.3 per cent comes from the NFHS-6 "
                 "fact sheet (2023-24), down from 35.5 per cent in NFHS-5 (2019-21). The surveys are from "
                 "different years, so the comparison is indicative.", sm=True),
            body("A rights reading asks more than whether the number is high. It asks whether the state is "
                 "meeting the minimum core (CESCR General Comment 3 names essential foodstuffs), whether "
                 "the trend is downward, and whether the poorest groups are improving as fast as the "
                 "average.", sm=True)], ratio="a32"),
        hbox("Nutrition 101 covers the measurement and the interventions; this deck covers the duty.",
             "indigo"),
    ]),

    C("Right to health", "Health as a right: Paschim Banga (1996)", [
        body("Hakim Seikh, an agricultural labourer, fell from a train in West Bengal in July 1992 and "
             "suffered head injuries. Several government hospitals in Calcutta turned him away for lack of "
             "beds or facilities. The Supreme Court held that this breached Article 21."),
        quote("In a welfare state the primary duty of the Government is to secure the welfare of the people. "
              "Providing adequate medical facilities for the people is an essential part of the obligations "
              "undertaken by the Government in a welfare state.",
              "Paschim Banga Khet Mazdoor Samity v State of West Bengal, (1996) 4 SCC 37"),
        tw(pp("cyan", "What followed", "The Court awarded compensation and directed steps to improve "
              "emergency care, holding that lack of resources cannot excuse failure to provide emergency "
              "treatment."),
           pp("green", "Nepal goes further on paper", "Nepal's Constitution of 2015 makes basic health care "
              "a fundamental right of every citizen in Article 35, and food in Article 36. Bangladesh's "
              "Constitution lists basic necessities in Article 15 but, under Article 8, the principles in "
              "that Part are not judicially enforceable.")),
    ]),

    C("Right to work", "Work and social security in 2026", [
        body("Article 41 asks the state, within its economic capacity, to secure the right to work and to "
             "public assistance in old age, sickness and disablement. Two legal changes in 2025 and 2026 "
             "reshape how practitioners work on these rights in India (as of October 2026)."),
        tw(pp("amber", "Rural employment", "The Mahatma Gandhi National Rural Employment Guarantee Act was "
              "repealed from 1 July 2026 and replaced by the Viksit Bharat G RAM G Act 2025, which provides "
              "for 125 days of work. Programmes that helped workers demand work and wages under the old Act "
              "need to read the new Act and its rules before advising anyone."),
           pp("cyan", "Labour Codes", "The four Labour Codes came into force on 21 November 2025, replacing "
              "most central labour laws. Social security, wages and occupational safety for informal and "
              "platform workers now sit under the Codes.")),
        hbox("Work, Labour &amp; Livelihoods 101 covers both changes. In rights terms, the questions are "
             "the same as before: is the entitlement clear, can workers claim it, and is there a remedy "
             "for delay?", "green"),
    ]),

    C("Housing and eviction", "Housing, eviction and fair procedure", [
        body("India's Constitution does not name a right to housing, but Olga Tellis (1985) tied livelihood "
             "and shelter to Article 21 and required fair procedure before removal. Nepal's 2015 Constitution "
             "states a right to appropriate housing and bars eviction except in accordance with law. The UN "
             "special rapporteur on adequate housing has set out guidance on development-based evictions."),
        table(["Before an eviction, ask", "Why"], [
            ["Was notice given, in a language people read?", "Fair procedure under Article 21"],
            ["Was there a hearing or survey of who lives there?", "To establish eligibility for rehabilitation"],
            ["Is there a resettlement plan near work and schools?", "Livelihood is part of the right to life"],
            ["Is the timing safe (exams, monsoon, harvest)?", "Proportionality of the action"],
            ["Are records kept of who was moved and where?", "For later claims and remedies"],
        ]),
        hbox("Illustrative checklist for programme staff; it is not legal advice. Contact a lawyer as soon "
             "as an eviction notice appears.", "amber"),
    ], compact=True),

    C("Measuring rights", "Measuring economic and social rights", [
        body("OHCHR's guide <em>Human Rights Indicators: A Guide to Measurement and Implementation</em> "
             "(2012) groups indicators into three kinds. Programme teams can borrow the structure for "
             "their own monitoring."),
        table(["Type", "What it measures", "Example for the right to education"], [
            ["Structural", "Laws, policies and institutions in place",
             "Article 21A; RTE Act 2009; state rules notified"],
            ["Process", "Effort: budgets, programmes, coverage",
             "Share of RTE 25% seats filled; teacher vacancies; SMC meetings held"],
            ["Outcome", "Results for rights-holders",
             "Completion of Class 8 by girls, Dalit and Adivasi children, children with disabilities"],
        ]),
        hbox("Disaggregation is what turns an ordinary indicator into a rights indicator. An average that "
             "rises while one caste or district falls behind can hide a breach of non-discrimination.",
             "green"),
    ], compact=True),

    C("Budgets as evidence", "Reading a budget as a rights document", [
        body("Article 2(1) of the ICESCR speaks of the maximum of available resources, so budgets are "
             "evidence. Three questions turn a budget into a rights analysis, and each can be asked of a "
             "state or district budget using published documents and RTI."),
        tw(pp("cyan", "Allocation", "Is enough allocated for the entitlement the law promises? Compare the "
              "allocation with the number of eligible people and the unit cost."),
           pp("green", "Release and spending", "Was the money released on time, and spent? Late releases "
              "turn an entitlement into a delay.")),
        tw(pp("amber", "Equity", "Do districts with more need receive more per eligible person? Are funds "
              "for SC and ST sub-plans spent on them?"),
           pp("indigo", "Backward steps", "Did a scheme's allocation fall in real terms? A cut needs "
              "justification under the progressive realisation duty.")),
        hbox("Public Finance &amp; Budgeting 101 shows how to read Indian budget documents.", "cyan"),
    ]),
]

# ===================== SECTION 09: CIVIC SPACE =====================
S09 = [
    D("09", "Section Nine", "Civic space and its legal framework"),

    C("The standards", "Expression, assembly and association: the legal standards", [
        table(["Freedom", "ICCPR", "Constitution of India", "Permitted grounds for restriction (India)"], [
            ["Speech and expression", "Art 19", "Art 19(1)(a)", "Art 19(2): sovereignty and integrity, "
             "security, public order, decency, defamation, incitement, and others"],
            ["Peaceful assembly", "Art 21", "Art 19(1)(b)", "Art 19(3): sovereignty and integrity, public "
             "order"],
            ["Association", "Art 22", "Art 19(1)(c)", "Art 19(4): sovereignty and integrity, public order, "
             "morality"],
        ]),
        body("This section states the law as it stands in India as of October 2026. It does not judge "
             "particular cases. Development organisations need to know these laws because they govern how "
             "an NGO is funded, how its staff and partners can speak, and what risks community members "
             "take when they organise.", sm=True),
        hbox("The UN Declaration on Human Rights Defenders (GA resolution 53/144, 9 December 1998) affirms "
             "in Article 1 that everyone has the right, individually and in association with others, to "
             "promote and strive for the protection of human rights.", "cyan"),
    ], compact=True),

    C("Sedition", "Sedition: from section 124A to the Bharatiya Nyaya Sanhita", [
        flow(["IPC s124A: sedition offence since the colonial era",
              "11 May 2022: S.G. Vombatkere v Union of India order",
              "2023: Bharatiya Nyaya Sanhita (Act 45 of 2023) enacted",
              "1 July 2024: BNS in force; IPC repealed by s358"]),
        body("In <strong>S.G. Vombatkere v Union of India</strong> (WP (C) 682 of 2021), the Supreme Court's "
             "order of 11 May 2022 expected governments to refrain from registering FIRs under section 124A "
             "while the Union reconsidered it, and directed that pending trials and appeals on that charge "
             "be kept in abeyance. The BNS contains no offence named sedition. Its section 152, \"Act "
             "endangering sovereignty, unity and integrity of India\", punishes exciting secession, armed "
             "rebellion or subversive activities, or encouraging feelings of separatist activities, with up "
             "to life imprisonment.", sm=True),
        hbox("Section 152 carries an explanation that comments expressing disapproval of government "
             "measures, without exciting the listed activities, are not an offence. How courts read the "
             "section is still developing; check current case law before advising.", "amber"),
    ]),

    C("UAPA", "The Unlawful Activities (Prevention) Act 1967", [
        body("The UAPA is India's main anti-terror law. Three features matter most for anyone working on "
             "rights, because they change what happens after an arrest."),
        table(["Feature", "Provision"], [
            ["Designation of individuals as terrorists", "Section 35, as amended in 2019: individuals can be "
             "added to the Fourth Schedule by notification"],
            ["Bail", "Section 43D(5): no bail if the court finds reasonable grounds to believe the accusation "
             "is prima facie true"],
            ["Time to complete investigation", "Section 43D(2): may be extended up to 180 days"],
        ]),
        quote("The presence of statutory restrictions like Section 43-D(5) of UAPA per se does not oust the "
              "ability of Constitutional Courts to grant bail on grounds of violation of Part III of the "
              "Constitution.",
              "Union of India v K.A. Najeeb (2021), para 18"),
        body("In Najeeb the Court held that the bail bar softens where there is no likelihood of the trial "
             "ending in reasonable time and the accused has served a large part of the possible sentence.",
             sm=True),
    ], compact=True),

    C("FCRA", "Foreign funding: the FCRA 2010 as amended in 2020", [
        body("The Foreign Contribution (Regulation) Act 2010 governs any Indian organisation receiving "
             "foreign funds. The 2020 amendment (Act 33 of 2020) changed four rules that shape how "
             "development partnerships are built."),
        table(["Section", "Rule after 2020", "Effect on programmes"], [
            ["7", "No transfer of foreign contribution to any other person",
             "No sub-granting of foreign funds to partner NGOs"],
            ["8(1)(b)", "Administrative expenses capped at 20% of foreign contribution in a year",
             "Core costs need other sources"],
            ["12A", "Aadhaar (or passport, for foreigners) of office bearers may be required",
             "Identity documents for key staff"],
            ["17", "Receipt only in an FCRA account at the specified SBI branch in New Delhi",
             "Account set-up before any receipt"],
        ]),
        body("In <strong>Noel Harper v Union of India</strong> (8 April 2022) the Supreme Court held sections "
             "7, 12(1A), 12A and 17 as amended intra vires, reading section 12A to accept an Indian passport "
             "for Indian office bearers.", sm=True),
    ], compact=True),

    C("Information rights", "The right to information after the DPDP Act", [
        body("The Right to Information Act 2005 is the most used accountability law in India. Section 7(1) "
             "requires a reply within 30 days, or 48 hours where the information concerns a person's life "
             "or liberty."),
        tw(pp("amber", "The 2025 change", "Section 44(3) of the Digital Personal Data Protection Act 2023 "
              "substitutes section 8(1)(j) of the RTI Act with an exemption for \"information which relates "
              "to personal information\", removing the earlier public-interest override. The amendment took "
              "effect on 13 November 2025, the date of the Gazette notification (G.S.R. 843(E)) that "
              "brought it into force."),
           pp("cyan", "Status", "On 26 May 2026 the Supreme Court issued notice to the Union on petitions "
              "challenging the amendment (Moneylife, 26 May 2026). Social audits that depend on names of "
              "beneficiaries or officials may find requests refused while the challenge is pending.")),
        hbox("Frame RTI requests around aggregate and scheme-level records where possible: budgets, sanction "
             "orders, stock registers, inspection reports.", "green"),
    ]),

    C("Working lawfully", "Compliance as protection for an organisation", [
        body("For an NGO, careful compliance is part of protecting the people it works with. A lapsed "
             "registration or an accounting error can end a programme and expose communities who relied on "
             "it. A short internal checklist reviewed every quarter covers most risk."),
        table(["Area", "Check"], [
            ["FCRA", "Registration valid; funds only via the SBI New Delhi account; no onward transfer; "
             "admin costs within 20%; returns filed"],
            ["Data", "Preparation for DPDP Act consent and notice duties (in force from 13 May 2027); purpose "
             "limits; research exemption conditions met where relied on"],
            ["Speech", "Public statements reviewed for accuracy and sourcing; no unverified allegations"],
            ["Staff safety", "Plan for arrests or summons; lawyer contact; family contacts"],
            ["Partners", "Written agreements; no cash routing; documented decisions"],
        ]),
        hbox("Illustrative checklist, not legal advice. Use a chartered accountant and a lawyer familiar "
             "with FCRA and the DPDP Act.", "amber"),
    ], compact=True),

    C("Defenders and risk", "Protecting people who raise rights issues", [
        body("Community members who complain, testify or organise take risks that programme staff can "
             "underestimate. A rights-based programme plans for retaliation before it asks anyone to speak "
             "up, and it keeps the decision with the person at risk."),
        tw(pp("cyan", "Before", "Map who might retaliate (local officials, employers, dominant groups). "
              "Explain risks plainly. Agree what will be recorded and who sees it."),
           pp("green", "During", "Collect only the data you need; store it securely; avoid naming people in "
              "public reports without explicit consent.")),
        tw(pp("amber", "If retaliation occurs", "Record dates and details at once; contact a lawyer; "
              "consider a complaint to the SHRC within the one-year limit; inform trusted networks."),
           pp("indigo", "UN routes", "The UN special rapporteur on human rights defenders receives "
              "communications through OHCHR's online tool. Use it with the person's consent.")),
        hbox("Safeguarding &amp; PSEA 101 and Research Ethics 101 cover consent and protection in depth.",
             "cyan"),
    ]),
]

# ===================== SECTION 10: BUSINESS AND HUMAN RIGHTS =====================
S10 = [
    D("10", "Section Ten", "Business and human rights"),

    C("The UN Guiding Principles", "The UN Guiding Principles on Business and Human Rights (2011)", [
        body("The Human Rights Council endorsed the <strong>UN Guiding Principles on Business and Human "
             "Rights</strong> (UNGPs) in resolution 17/4 of 16 June 2011. They implement the \"Protect, "
             "Respect and Remedy\" framework and rest on three pillars."),
        tw([panel("cyan", "Pillar I: the state duty to protect", [body(
                "States must protect against human rights abuse by business through laws, policies, "
                "regulation and adjudication.", sm=True)]),
            panel("green", "Pillar II: corporate responsibility to respect", [body(
                "Business enterprises should respect human rights: avoid infringing them and address "
                "adverse impacts they are involved with (Principle 11).", sm=True)])],
           [panel("amber", "Pillar III: access to remedy", [body(
                "Victims need effective judicial and non-judicial remedies, run by the state and by "
                "companies themselves.", sm=True)]),
            body("The UNGPs are not a treaty. Their force comes from adoption into national law, company "
                 "policies, investor rules and supply-chain contracts.", sm=True)]),
    ]),

    C("Due diligence", "Human rights due diligence", [
        quote("In order to identify, prevent, mitigate and account for how they address their adverse human "
              "rights impacts, business enterprises should carry out human rights due diligence.",
              "UN Guiding Principles on Business and Human Rights, Principle 17"),
        flow(["ASSESS: actual and potential impacts",
              "INTEGRATE: act on the findings",
              "TRACK: check whether responses work",
              "COMMUNICATE: say how impacts are addressed"]),
        tw(pp("cyan", "For NGOs partnering with companies", "Ask to see the company's due diligence on the "
              "site or supply chain you will work in. A CSR project beside a factory with unresolved "
              "labour complaints is exposed to the same risk."),
           pp("green", "For communities", "Due diligence gives communities a question to ask: has the "
              "company assessed its impact on us, and what did it find?")),
    ]),

    C("Grievance mechanisms", "What makes a grievance mechanism work (Principle 31)", [
        table(["Criterion", "What it means", "Test in the field"], [
            ["Legitimate", "Trusted by the people it is for", "Would workers use it without fear?"],
            ["Accessible", "Known to all, with help for those facing barriers", "Is it in local languages?"],
            ["Predictable", "Clear procedure with timeframes", "Are deadlines published?"],
            ["Equitable", "Fair access to information and advice", "Can complainants get advice?"],
            ["Transparent", "Parties kept informed of progress", "Are outcomes reported?"],
            ["Rights-compatible", "Outcomes accord with human rights", "Does it block court cases?"],
            ["Source of continuous learning", "Lessons used to prevent harm", "Do policies change?"],
            ["Based on engagement and dialogue", "Designed with users (company-level mechanisms)",
             "Were workers consulted?"],
        ]),
        body("The same eight tests work for an NGO's own complaints system, and for a government grievance "
             "portal.", sm=True),
    ], compact=True),

    C("India's framework", "Business and human rights in Indian law and policy", [
        table(["Instrument", "What it does", "Status (October 2026)"], [
            ["National Action Plan on Business and Human Rights", "Zero draft by the Ministry of Corporate "
             "Affairs, February 2019", "Not adopted; globalnaps.org lists it as under development"],
            ["National Guidelines on Responsible Business Conduct (2018)", "Nine principles for business",
             "Basis for SEBI reporting"],
            ["SEBI Business Responsibility and Sustainability Report", "ESG disclosure against the nine "
             "principles (circular of 10 May 2021)", "Mandatory for the top 1,000 listed companies from "
             "FY 2022-23"],
            ["Companies Act 2013, section 135", "CSR spending duty for qualifying companies", "In force"],
            ["Four Labour Codes", "Wages, social security, safety, industrial relations",
             "In force from 21 November 2025"],
        ]),
        hbox("BRSR disclosures are public. An NGO can read a company's human rights disclosures before "
             "partnering and compare them with what workers and communities report. CSR &amp; ESG 101 "
             "explains BRSR.", "green"),
    ], compact=True),

    C("Supply chains", "Rana Plaza and supply-chain responsibility", [
        body("On 24 April 2013 the Rana Plaza building in Savar, near Dhaka, collapsed, killing more than "
             "1,100 garment workers (US Congressional Research Service, report R43085, 2014). The factories "
             "made clothes for international brands. The disaster changed how buyers, governments and unions "
             "think about responsibility along supply chains."),
        tw(pp("cyan", "What changed", "The question of whether a brand answers for conditions in the "
              "factories that supply it moved from campaign slogans into buyer contracts, investor "
              "questions and law-making on due diligence. The UNGPs, adopted two years earlier, gave that "
              "debate its vocabulary."),
           pp("amber", "What it teaches programmes", "Audits failed to stop the collapse. Worker voice "
              "(the ability to refuse unsafe work and to report without retaliation) is the mechanism "
              "that rights-based programmes can strengthen.")),
        hbox("Many Indian and Bangladeshi suppliers now face due diligence questions from buyers. Workers' "
             "organisations can use those questions as a route for grievances.", "indigo"),
    ]),

    C("NGO roles", "Where development organisations fit in business and human rights", [
        tw([panel("cyan", "Roles that work", [bullets([
                "Help communities document impacts and use company grievance mechanisms",
                "Translate company commitments into local languages and terms",
                "Provide independent monitoring where communities ask for it",
                "Partner on CSR only after reviewing due diligence and disclosures"], sm=True)])],
           [panel("red", "Roles to avoid", [bullets([
                "Running a company's grievance system with no independence",
                "Using CSR funds to deliver services the state must provide, with no exit plan",
                "Signing confidentiality terms that prevent reporting harm",
                "Speaking for communities without their mandate"], sm=True)])]),
        hbox("A clear written agreement, an exit plan and an independent complaints route protect both the "
             "NGO and the community when a company relationship goes wrong.", "amber"),
    ]),
]

# ===================== SECTION 11: PRACTICAL APPLICATION =====================
S11 = [
    D("11", "Section Eleven", "Using rights in a programme"),

    C("Design checklist", "A rights check for any programme design", [
        body("Run this check at design stage and again at mid-term. Each question links to a part of this "
             "deck. A \"no\" is a design task, and the answers belong in the proposal."),
        table(["Question", "Look for", "Deck section"], [
            ["Which rights does the programme serve, and in which law?", "Article, statute, treaty article",
             "02, 06, 08"],
            ["Who are the duty-bearers, by name and office?", "Department, officer, local body", "01, 05"],
            ["Who is most likely to be excluded?", "Disaggregated baseline", "05, 08"],
            ["How do rights-holders take part in decisions?", "Meetings, committees, consent", "05"],
            ["What is the grievance route, and does it work?", "Tested route with timelines", "07, 10"],
            ["What does the state already owe here?", "Scheme entitlements, UPR and treaty commitments",
             "04, 08"],
            ["What could go wrong for participants?", "Risk and safeguarding plan", "09"],
            ["Who sustains the gains after the project?", "Public budget line, institution", "05, 08"],
        ]),
    ], compact=True),

    C("Worked example", "Worked example: migrant workers from a Bihar district", [
        body("Illustrative case (hypothetical figures). An NGO in a source district of Bihar works with families of seasonal migrant "
             "workers who go to brick kilns and construction sites in other states. It wants to move from "
             "relief to rights."),
        table(["Problem found", "Right and source", "Duty-bearer", "Programme action"], [
            ["Families lose rations when the worker migrates", "Food: NFSA 2013", "State food department",
             "Help families use ration portability; RTI on denied cases"],
            ["Children drop out during migration months", "Education: Art 21A, RTE Act", "School and block "
             "office", "Seasonal hostels via panchayat; track enrolment"],
            ["Unpaid wages at destination", "Work: Labour Codes (2025)", "Labour department at destination",
             "Documented wage claims; partner NGO at destination"],
            ["Advance-and-debt bondage at kilns", "Art 23; Bonded Labour System (Abolition) Act 1976",
             "District magistrate", "Report to DM; SHRC complaint if no action"],
        ]),
        hbox("Every row has a law, a named office and an action. That is the shape of a rights-based "
             "workplan.", "green"),
    ], compact=True),

    C("Choosing a route", "Decision table: which route for which problem", [
        table(["Situation", "First route", "If that fails", "Avoid"], [
            ["Scheme benefit denied", "Written application; grievance portal", "RTI on the file; district "
             "official", "Going to court first"],
            ["Information withheld", "RTI request (30 days)", "First appeal, then Information Commission",
             "Informal requests only"],
            ["Police abuse or custodial harm", "Medical record; complaint to senior police", "SHRC or NHRC "
             "within one year; High Court writ", "Delay beyond one year"],
            ["Systemic denial affecting many", "Collective representation with evidence", "PIL with the "
             "affected people's consent", "Litigation without community choice"],
            ["Company harm to a community", "Company grievance mechanism", "Regulator; court; BRSR-based "
             "investor engagement", "Signing confidentiality terms"],
            ["Pattern that government ignores", "Media and allies; treaty body shadow report",
             "UN special procedure communication", "Relying on Geneva alone"],
        ]),
        body("Illustrative guidance for programme staff, not legal advice. Routes differ by state, and a "
             "lawyer should advise on any case that may go to court.", sm=True),
    ], compact=True),

    C("Documenting violations", "Documenting a rights violation so it can be used", [
        body("Evidence gathered carelessly can be useless in a commission or court, and can put people at "
             "risk. A few habits make documentation usable and safe."),
        tw(pp("cyan", "What to record", "Who, what, when, where, with dates and times; names and ranks of "
              "officials; documents such as FIRs, medical records, notices; photographs with dates; "
              "witnesses who agree to be named."),
           pp("green", "How to record it", "Informed consent in the person's language; only the data "
              "needed; secure storage with limited access; a clear chain of who holds originals.")),
        tw(pp("amber", "What to avoid", "Leading questions; promising outcomes; sharing names on messaging "
              "groups; posting identifiable images of survivors, especially children."),
           pp("indigo", "Law to respect", "The DPDP Act 2023 and Rules 2025 govern personal data you "
              "collect, with consent and notice duties applying from 13 May 2027. Laws on child victims "
              "and sexual offences restrict disclosing identities.")),
    ]),

    C("Writing to a duty-bearer", "A rights-based letter in five parts", [
        body("Most rights work starts with a letter, and a well-built letter is often enough. It also "
             "creates the record that any later complaint or petition will need."),
        flow(["FACTS: who, what, when, with documents",
              "ENTITLEMENT: the law, section or scheme rule",
              "DUTY: the office responsible and its obligation",
              "REQUEST: a specific action and a date",
              "RECORD: copy to senior office; keep proof of delivery"]),
        hbox("Illustrative: \"Under section 3(1) of the National Food Security Act 2013, the 14 households "
             "listed are entitled to 5 kg of grain per person per month. Their cards were cancelled on 3 "
             "March without notice. We request restoration within 15 days and a written reason for the "
             "cancellation.\"", "green"),
        body("A letter that names the law and asks for a dated action is harder to ignore than one that "
             "asks for help. If there is no reply, an RTI request on the file and a copy to the district "
             "collector are the next steps.", sm=True),
    ]),

    C("Rights in the results framework", "Putting rights into indicators and the logframe", [
        table(["Level", "Conventional indicator", "Rights-based version"], [
            ["Outcome", "Children enrolled", "Children completing Class 8, by sex, caste, disability"],
            ["Outcome", "Households with ration cards", "Eligible households receiving full entitlement "
             "for six consecutive months"],
            ["Output", "Trainings held", "Grievances filed and resolved within the legal time limit"],
            ["Output", "Committees formed", "Committees meeting with women and SC/ST members speaking"],
            ["Process", "Funds spent", "Public allocation for the service released on time"],
        ]),
        body("The rights-based column measures the duty-bearer's performance and equality of access, which "
             "is where a rights approach differs from a delivery approach. Logframe 101 and MEL Basics 101 "
             "show how to build these into a results framework.", sm=True),
        hbox("Disaggregate every people-level indicator by at least sex, caste or tribe, and disability. "
             "Without that, non-discrimination cannot be checked.", "indigo"),
    ], compact=True),

    C("Do no harm", "Protecting communities and staff in rights work", [
        tw([panel("amber", "Risks to plan for", [bullets([
                "Retaliation against complainants by officials or local elites",
                "Loss of benefits as punishment for speaking up",
                "Exposure of identities through data leaks",
                "Legal risk to staff from public statements",
                "Raised expectations that the programme cannot meet"], sm=True)])],
           [panel("green", "Mitigations", [bullets([
                "Consent at each step, including the right to withdraw",
                "Collective complaints where they are safer for individuals",
                "Data minimisation and secure storage",
                "Fact-checked, sourced public statements",
                "Honest explanation of what each route can and cannot do"], sm=True)])]),
        hbox("The person whose rights were violated decides whether to complain. A programme's job is to "
             "make the options and risks clear, and to stand with that decision.", "cyan"),
    ]),
]

# ===================== SECTION 12: SUMMING UP AND WHERE NEXT =====================
S12 = [
    D("12", "Section Twelve", "Summing up and where next"),

    C("Summary", "Eight points to carry into practice", [
        tw([panel("cyan", "On the law", [bullets([
                "A right is a claim with a named duty-bearer and a remedy",
                "India is party to six of nine core UN treaties; not CAT, CED or CMW",
                "Article 21, read with Part IV, carries most social rights in India",
                "Treaties enter Indian courts where Indian law is silent (Vishaka, 1997)"], sm=True)])],
           [panel("green", "On practice", [bullets([
                "Start with domestic routes: letters, RTI, commissions, courts",
                "File with an SHRC or the NHRC within one year",
                "Measure duty-bearer performance and equality as well as delivery",
                "Plan for retaliation and data protection before asking anyone to speak"], sm=True)])]),
        hbox("Check time-sensitive facts before you rely on them: GANHRI status, the DPDP and RTI "
             "litigation, the new rural employment law and the Labour Codes were all changing as of "
             "October 2026.", "amber"),
    ]),

    C("Where next", "Where next: related 101 decks", [
        tw([panel("cyan", "Law and institutions", [body(
                "<a href=\"/101-courses/ind-constitution.html\">Indian Constitution 101</a> for Parts III and "
                "IV in depth. "
                "<a href=\"/101-courses/child-rights.html\">Child Rights 101</a> for the CRC and Indian child "
                "law. "
                "<a href=\"/101-courses/governance-accountability.html\">Governance &amp; Accountability "
                "101</a> for RTI, audits and grievance systems. "
                "<a href=\"/101-courses/digital-rights-ai.html\">Digital Rights &amp; AI 101</a> for privacy "
                "and data after Puttaswamy.", sm=True)])],
           [panel("green", "Practice and people", [body(
                "<a href=\"/101-courses/advocacy-basics.html\">Advocacy Basics 101</a> for campaigns that "
                "use these routes. "
                "<a href=\"/101-courses/social-margins.html\">Social Margins 101</a> for caste, tribe and "
                "exclusion. "
                "<a href=\"/101-courses/gender-dev.html\">Gender &amp; Development 101</a> for CEDAW and "
                "personal law. "
                "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the DPDP Act "
                "101</a> and <a href=\"/101-courses/safeguarding-psea.html\">Safeguarding &amp; PSEA "
                "101</a> for protecting the people you work with.", sm=True)])]),
        hbox("Suggested order: Indian Constitution, then Governance &amp; Accountability, then Advocacy "
             "Basics. Read Child Rights before any programme that works with children.", "indigo"),
    ], compact=True),
]

TITLE = {"type": "title",
         "main": "Human<br>Rights<br>101",
         "sub": "What rights are, where they come from and how a development programme can use them: "
                "treaties, the UN system, the Indian Constitution, courts, commissions and civic space, "
                "for practitioners in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Rights in Practice"]}

TOC = {"type": "toc", "label": "Agenda", "title": "What we cover",
       "items": [
           {"name": "What rights are and where they come from"},
           {"name": "The international bill of rights"},
           {"name": "Core treaties and ratification"},
           {"name": "The UN machinery"},
           {"name": "The human rights-based approach"},
           {"name": "Rights in the Indian Constitution"},
           {"name": "Courts, PIL and commissions"},
           {"name": "Economic and social rights in practice"},
           {"name": "Civic space and its legal framework"},
           {"name": "Business and human rights"},
           {"name": "Using rights in a programme"},
           {"name": "Summing up and where next"},
       ]}

END = {"type": "end",
       "eyebrow": "Human Rights 101",
       "headline": "Name the right, name the duty-bearer, find the remedy",
       "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development practitioners "
                 "in South Asia",
       "ctas": [{"label": "Indian Constitution 101", "href": "/101-courses/ind-constitution.html"},
                {"label": "All 101 courses", "href": "/101-courses/"}],
       "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]}

DECK = {
    "slug": "human-rights",
    "title": "Human Rights 101",
    "description": ("Human Rights 101: a free foundational course for development practitioners in South "
                    "Asia. The UDHR and the two Covenants, treaty ratification across India, Bangladesh, "
                    "Nepal, Pakistan and Sri Lanka, the UN Human Rights Council, UPR, treaty bodies and "
                    "special procedures, the human rights-based approach, Part III and Part IV of the "
                    "Indian Constitution and Article 21, public interest litigation, the NHRC, economic "
                    "and social rights, civic space law, business and human rights, and how a programme "
                    "uses rights. ImpactMojo, CC BY-NC-ND."),
    "slides": ([TITLE, TOC] + S01 + S02 + S03 + S04 + S05 + S06 + S07 + S08 + S09 + S10 + S11 + S12
               + [END]),
}

# -*- coding: utf-8 -*-
"""
Participatory Methods 101 -- ImpactMojo 101 Series (native deck spec)
Participatory approaches in development practice and research, for South Asian practitioners.
Build: python3 scripts/deck-builder/build.py participatory_methods

House style: no em dashes, sentence-case headings, every statistic sourced on the slide,
made-up teaching examples labelled Illustrative.
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


SLIDES = []

# ===================== S1 TITLE, S2 TOC =====================
SLIDES += [
    {"type": "title",
     "main": "Participatory<br>Methods<br>101",
     "sub": "Research and practice done with the people they concern: origins, ladders of "
            "participation, PRA tools, social audits, scorecards, Photovoice, participatory "
            "MEL, power and ethics, for practitioners in South Asia",
     "tags": ["100 Slides", "South Asia Focus", "Free Forever", "PRA and Social Audit"]},

    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Why participation"},
         {"name": "Origins: Freire, Fals-Borda, Chambers"},
         {"name": "Ladders and typologies"},
         {"name": "PRA tools I: maps, walks, timelines"},
         {"name": "PRA tools II: calendars, ranking, Venn"},
         {"name": "Participatory governance in India"},
         {"name": "Social audits and scorecards"},
         {"name": "Photovoice, video and stories"},
         {"name": "Participatory MEL and the evidence"},
         {"name": "Doing it well: documentation and practice"},
         {"name": "Power, ethics and consent"},
     ]},
]

# ===================== SECTION 01 =====================
SLIDES += [
    D("01", "Section One", "Why participation"),

    C("The idea", "Participatory methods put people in charge of parts of the inquiry",
      TERM("Participatory methods",
           "A family of approaches in which the people a study or programme concerns take part in "
           "defining the questions, producing the information, interpreting it and deciding what "
           "to do with it. The degree of control they hold varies from method to method and from "
           "one use to the next."),
      TW([P("amber", "Extractive inquiry",
            "Outsiders design the questions, collect answers, take the data away and analyse it "
            "elsewhere. Respondents rarely see the results. Information flows one way, from the "
            "village to the office, the journal or the donor report.")],
         [P("green", "Participatory inquiry",
            "Residents draw the map, rank the problems, score the service and discuss what the "
            "pattern means while the outsider listens. The analysis happens where the data was "
            "produced, and the people who produced it keep a copy and a say in its use.")]),
      H("cyan", "Participation is a question of who decides at each stage. Every method in this "
        "deck can be run in an extractive way, so the method name tells you less than the answer "
        "to that question.")),

    C("Three justifications", "People argue for participation for three different reasons",
      B("Practitioners and funders defend participatory work on grounds that are worth keeping "
        "apart, because each one implies a different test of whether it worked."),
      T(["Justification", "The claim", "What would show it failed"],
        [["Instrumental", "Local knowledge and ownership make projects cheaper, better targeted "
          "and more likely to last", "Participatory projects cost more and deliver no better "
          "services or targeting"],
         ["Rights-based", "People have a right to a say in decisions that affect them, as the "
          "Constitution's Part IX on panchayats and PESA 1996 recognise for India", "Decisions "
          "are announced to a meeting that cannot change them"],
         ["Epistemic", "Residents know things about their own lives that surveys miss, so "
          "inquiry with them is more accurate", "The participatory exercise reproduces what "
          "the survey already showed, or only what elites wanted said"]]),
      H("indigo", "Most projects claim all three at once. Pick the one your design rests on and "
        "measure that. A programme defended on instrumental grounds has to show results; one "
        "defended on rights grounds has to show that power moved.")),

    C("With, by, on", "Research on people, with people, and by people",
      TW([P("red", "On",
            "The researcher holds every decision. People are sources of data. Most household "
            "surveys, including large official ones, are in this mode, and for good reasons: "
            "comparability across districts needs fixed questions."),
          P("amber", "With",
            "Researcher and community share decisions at some stages, often the questions and "
            "the interpretation. Most PRA exercises and community scorecards sit here.")],
         [P("green", "By",
            "The community or a people's organisation runs the inquiry and may hire outside "
            "help on its own terms. Participatory action research in the tradition of "
            "Fals-Borda and Anisur Rahman aims here."),
          P("cyan", "Mixing them",
            "A district study can use a fixed survey for prevalence and a participatory map "
            "to locate the hamlets the sampling frame missed. The modes answer different "
            "questions and can sit in one design.")])),

    C("Law as well as method", "In India, participation is also a legal requirement",
      B("Participatory methods in India are tied to statutes that give village assemblies "
        "defined powers. A practitioner working with a gram panchayat is working inside this "
        "legal frame, whether or not the project document mentions it."),
      T(["Instrument", "What it provides"],
        [["Constitution (73rd Amendment) Act 1992, in force 24 April 1993",
          "Article 243A: the Gram Sabha may exercise powers and functions a state law provides; "
          "Article 243D: not less than one-third of seats reserved for women"],
         ["PESA Act 1996, s4(e)", "In Scheduled Areas, every Gram Sabha approves plans and "
          "projects and identifies beneficiaries"],
         ["VB-G RAM G Act 2025, s20", "The Gram Sabha conducts regular social audits of all "
          "works under the rural employment scheme"],
         ["Meghalaya Act No. 7 of 2017", "A state law for participatory social audit of public "
          "services and schemes"]]),
      H("amber", "Sections 06 and 07 take each of these in turn, with the text of the "
        "provisions. Statutory status as of October 2026.")),

    C("Induced and organic", "Participation that grows and participation that is designed",
      B("Ghazala Mansuri and Vijayendra Rao's World Bank Policy Research Report <em>Localizing "
        "Development: Does Participation Work?</em> (2013) drew a distinction that runs through "
        "this deck."),
      TW([P("green", "Organic participation",
            "In the report's words, endogenous efforts by civic activists to bring about change. "
            "The Mazdoor Kisan Shakti Sangathan's public hearings in Rajasthan, which grew from a "
            "labour and farmers' organisation founded on 1 May 1990, are an Indian example.")],
         [P("amber", "Induced participation",
            "Large-scale efforts to engineer participation at the local level through projects "
            "or government schemes: village committees created by a programme, mandated "
            "meetings, required plans. Kerala's People's Plan Campaign of 1996 began this way.")]),
      H("cyan", "The report found modestly positive results for community participation in health "
        "and education, a limited impact on income poverty, and little evidence that induced "
        "participation builds long-lasting cohesion. Source: Mansuri and Rao (2013), World Bank.")),

    C("A running case", "The village we will return to throughout",
      B("To keep the tools concrete, later slides refer to one made-up place. It is a teaching "
        "device, built from features common to many South Asian villages, and none of its "
        "numbers describe a real village."),
      TW([P("indigo", "Illustrative: Pipalgaon",
            "A gram panchayat of three revenue villages and five hamlets in a drought-prone "
            "block. Roughly 900 households. A main village on the road, a Dalit hamlet across "
            "a seasonal stream, two Adivasi hamlets on the forest edge, and a fishing settlement "
            "by the tank.")],
         [P("cyan", "The questions we bring",
            "Why do some households not get work under the rural employment scheme? Why is the "
            "anganwadi under-used in two hamlets? What would a fair village plan look like? "
            "Each later section shows which tool helps with which question.")]),
      H("amber", "Illustrative. Watch for the hamlets across the stream: much of what goes wrong "
        "in participatory work happens to the people who live furthest from the meeting.")),
]

# ===================== SECTION 02 =====================
SLIDES += [
    D("02", "Section Two", "Origins: Freire, Fals-Borda, Chambers"),

    C("Paulo Freire", "Freire and the critique of banking education",
      B("Paulo Freire wrote <em>Pedagogy of the Oppressed</em> in exile in Chile after the "
        "1964 coup in Brazil. It appeared first in Spanish in 1968, in English in 1970, and in "
        "Portuguese only in 1975, delayed by Brazil's political climate (Internet Encyclopedia "
        "of Philosophy, entry on Freire)."),
      TW([P("red", "Banking education",
            "The teacher deposits knowledge into students who are treated as empty accounts. "
            "The learner receives, files and repeats. Freire argued this keeps people adapted "
            "to the world as it is.")],
         [P("green", "Problem-posing education",
            "Teacher and learners investigate a real situation together through dialogue. "
            "Adult literacy work in this mode starts from words and situations that matter in "
            "learners' own lives and uses them to discuss why things are as they are.")]),
      H("cyan", "Swap 'teacher' for 'project officer' and 'student' for 'beneficiary', and "
        "Freire's critique describes most top-down development planning.")),

    C("Conscientizacao", "Critical consciousness and the dialogue that produces it",
      TERM("Conscientizacao (critical consciousness)",
           "The process of becoming aware of social and political contradictions and then "
           "acting against the oppressive elements of one's conditions. The Internet Encyclopedia "
           "of Philosophy's summary of Freire's term."),
      B("Freire insisted that dialogue cannot be imposed and depends on respect between the "
        "parties. That condition is the hardest part of participatory practice. A meeting "
        "where the block officer speaks for forty minutes and then asks for questions is a "
        "consultation in form and a lecture in substance."),
      BL(["What participatory methods took from Freire: start from people's own words and "
          "pictures, treat analysis as shared work, and link reflection to action",
          "What they often dropped: the political aim. A wealth ranking can be run purely to "
          "target a subsidy, with no intention that anyone's consciousness changes"],
         color="indigo")),

    C("Orlando Fals-Borda", "Participatory action research from Colombia",
      B("The Colombian sociologist Orlando Fals-Borda (1925&ndash;2008) argued that academic "
        "research mostly served those who already held power, and shifted his own work from "
        "research about peasants to research with peasant organisations. He organised "
        "international conferences on participatory research in Cartagena in 1977 and 1997, "
        "which later gatherings of action researchers still treat as their reference point."),
      TW([P("cyan", "What PAR holds",
            "Knowledge is a source of power. Ordinary people produce valid knowledge about their "
            "own conditions. Research and action form one cycle, and the community owns the "
            "results and decides how they are used.")],
         [P("amber", "What it asks of researchers",
            "Return findings in forms people can use: pictures, local histories, plays, "
            "pamphlets in the local language. Expect to be judged by the people you worked with "
            "as well as by peer reviewers, and accept that the two may disagree.")]),
      H("indigo", "Sources: Moretti and Streck, 'Homage to Fals Borda', <em>International Journal "
        "of Action Research</em> 11(3): 364&ndash;374 (2015), for 1925&ndash;2008; Hall and "
        "Tandon, 'From action research to knowledge democracy. Cartagena 1977&ndash;2017', "
        "<em>Revista Colombiana de Sociolog&iacute;a</em> 41(1): 227&ndash;236 (2018), for the "
        "Cartagena meetings.")),

    C("A South Asian strand", "Anisur Rahman and the Bhoomi Sena",
      B("Participatory action research has South Asian roots of its own. Md. Anisur Rahman, a "
        "Bangladeshi economist who taught at Dhaka University and sat on Bangladesh's first "
        "Planning Commission, later coordinated the International Labour Office's programme on "
        "Participatory Organisations of the Rural Poor in Geneva."),
      TW([P("green", "The Bhoomi Sena study",
            "Rahman wrote on 'some dimensions of people's participation in the Bhoomi Sena "
            "movement', a movement of tribal landless and bonded labourers in western India, to "
            "ask what made people's own organisation work.")],
         [P("cyan", "Action and Knowledge (1991)",
            "With Fals-Borda he co-edited <em>Action and Knowledge: Breaking the Monopoly with "
            "Participatory Action Research</em> (1991), a collection that draws on some twenty "
            "years of practice in participatory action research.")]),
      H("amber", "The title names the target. The monopoly in question is the monopoly of "
        "professionals over what counts as knowledge.")),

    C("Robert Chambers", "Seeing what outsiders miss",
      B("Robert Chambers, of the Institute of Development Studies at Sussex, set out the "
        "practitioner's version of the argument in <em>Rural Development: Putting the Last "
        "First</em> (Longman, 1983). Its central theme is that rural poverty is often unseen or "
        "misperceived by outsiders who are not themselves rural and poor, and that "
        "researchers, administrators and fieldworkers rarely credit the knowledge rural "
        "people hold."),
      TW([P("amber", "The outsider's view",
            "Brief visits along tarred roads, in the cool season, meeting the sarpanch and the "
            "better-off farmers who speak the visitor's language. The poorest are absent, "
            "busy or out of sight.")],
         [P("green", "The correction Chambers proposed",
            "Spend time, go off the road, seek out women and the poorest, and above all let "
            "people show and analyse their situation in their own terms, with the outsider "
            "listening.")]),
      H("cyan", "The first panel paraphrases the argument. Read the "
        "book for Chambers's own list of the biases of rural visits.")),

    C("From RRA to PRA", "Rapid appraisal became participatory appraisal",
      B("Chambers traced the history in 'The origins and practice of participatory rural "
        "appraisal', <em>World Development</em> 22(7): 953&ndash;969 (1994), the first of a "
        "three-part series. He identified five sources: activist participatory research, "
        "agroecosystem analysis, applied anthropology, field research on farming systems, and "
        "rapid rural appraisal (RRA)."),
      T(["", "Rapid rural appraisal", "Participatory rural appraisal"],
        [["Main aim", "Quicker, cheaper learning by outsiders", "Local people's own analysis "
          "and action"],
         ["Who analyses", "Mostly the outside team", "Mostly local people, with outsiders "
          "convening"],
         ["Typical output", "A report for the agency", "Maps, plans and decisions held "
          "locally, plus a report"],
         ["Risk", "Shallow, hurried findings", "Ritual participation that changes nothing"]]),
      H("indigo", "The contrast is a teaching simplification of Chambers's account. In practice "
        "the two blur, and many 'PRAs' are RRAs with chart paper.")),

    C("India as a laboratory", "PRA spread fast through Indian NGOs around 1990",
      B("India was one of the places where PRA methods were invented and tested. A special issue "
        "of <em>RRA Notes</em> (number 13, IIED, August 1991) reported a PRA trainers' workshop "
        "held in Bangalore in February 1991."),
      ST([CARD("35", "PRA trainers at the workshop, organised by MYRADA, Bangalore",
               "cyan", "RRA Notes 13, IIED, 1991"),
          CARD("18", "institutions those trainers represented", "green",
               "RRA Notes 13, IIED, 1991"),
          CARD("2,000", "villages in South India where MYRADA developed its PALM approach",
               "amber", "RRA Notes 13, IIED, 1991")], cols=3),
      H("cyan", "The issue's papers came from MYRADA, AKRSP, SPEECH in Tamil Nadu, Krishi Gram "
        "Vikas Kendra in Bihar and ActionAid, with accounts of PRA training for NGO staff in West "
        "Bengal and for officers of a government watershed programme in Andhra Pradesh.")),

    C("Mainstream and backlash", "From method to orthodoxy to critique",
      B("Within a decade participatory appraisal moved from NGO experiment to a requirement in "
        "donor and government projects. Success brought its own problem: methods designed for "
        "slow, open-ended work were compressed into a few days to meet project timelines."),
      FLOW("1968&ndash;70: Freire's Pedagogy of the Oppressed",
           "1977: Cartagena symposium on participatory research",
           "1983: Chambers, Putting the Last First",
           "1994: Chambers, origins of PRA, World Development",
           "1997: Chambers, Whose Reality Counts?",
           "2001: Cooke and Kothari, Participation: The New Tyranny?"),
      H("amber", "<em>Whose Reality Counts? Putting the First Last</em> (Intermediate Technology "
        "Publications, 1997) argued that many development errors flowed from domination by "
        "those with power. Four years later, Bill Cooke and Uma Kothari's edited volume (Zed "
        "Books, 2001) turned that argument against participatory practice itself. Section 11 "
        "takes up their case.")),
]

ARNSTEIN_SVG = '''<div style="display:flex;justify-content:center;margin:4px 0">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Arnstein's eight-rung ladder of citizen participation" style="width:100%;max-width:720px;height:auto;font-family:inherit">
  <rect x="8" y="10" width="150" height="114" rx="6" fill="#10B981" opacity="0.14"/>
  <rect x="8" y="130" width="150" height="114" rx="6" fill="#F59E0B" opacity="0.14"/>
  <rect x="8" y="250" width="150" height="74" rx="6" fill="#EF4444" opacity="0.14"/>
  <text x="83" y="62" fill="#047857" font-size="15" font-weight="700" text-anchor="middle">CITIZEN</text>
  <text x="83" y="82" fill="#047857" font-size="15" font-weight="700" text-anchor="middle">POWER</text>
  <text x="83" y="192" fill="#B45309" font-size="15" font-weight="700" text-anchor="middle">TOKENISM</text>
  <text x="83" y="282" fill="#B91C1C" font-size="13" font-weight="700" text-anchor="middle">NON-</text>
  <text x="83" y="300" fill="#B91C1C" font-size="13" font-weight="700" text-anchor="middle">PARTICIPATION</text>
  <g font-size="14" font-weight="700">
    <rect x="180" y="12" width="560" height="34" rx="5" fill="#047857"/><text x="196" y="34" fill="#fff">8 &#183; Citizen control</text>
    <rect x="180" y="52" width="560" height="34" rx="5" fill="#047857"/><text x="196" y="74" fill="#fff">7 &#183; Delegated power</text>
    <rect x="180" y="92" width="560" height="34" rx="5" fill="#047857"/><text x="196" y="114" fill="#fff">6 &#183; Partnership</text>
    <rect x="180" y="132" width="560" height="34" rx="5" fill="#92400E"/><text x="196" y="154" fill="#fff">5 &#183; Placation</text>
    <rect x="180" y="172" width="560" height="34" rx="5" fill="#92400E"/><text x="196" y="194" fill="#fff">4 &#183; Consultation</text>
    <rect x="180" y="212" width="560" height="34" rx="5" fill="#92400E"/><text x="196" y="234" fill="#fff">3 &#183; Informing</text>
    <rect x="180" y="252" width="560" height="34" rx="5" fill="#991B1B"/><text x="196" y="274" fill="#fff">2 &#183; Therapy</text>
    <rect x="180" y="292" width="560" height="34" rx="5" fill="#991B1B"/><text x="196" y="314" fill="#fff">1 &#183; Manipulation</text>
  </g>
</svg></div>'''

# ===================== SECTION 03 =====================
SLIDES += [
    D("03", "Section Three", "Ladders and typologies"),

    C("Why typologies", "Participation comes in degrees, and the word hides which degree",
      B("'The community participated' can mean that residents were told about a road after it "
        "was sanctioned, or that they chose the road, hired the contractor and checked the bills. "
        "Typologies give practitioners a vocabulary for the difference, so a report can say "
        "which kind of participation happened and readers can judge it."),
      TW([P("cyan", "What a typology is for",
            "Diagnosing a project frankly at the design stage, comparing what was promised in "
            "the proposal with what happened in the field, and agreeing with a community what "
            "level of control it will hold at each stage.")],
         [P("amber", "What a typology cannot do",
            "Tell you which level is right. Some decisions, such as the technical design of a "
            "check dam, may properly rest with engineers. A typology describes who holds power; "
            "whether that is appropriate is a separate argument you have to make.")]),
      H("indigo", "Three typologies matter most in development practice: Arnstein (1969), "
        "Pretty (1995) and White (1996). Each was written for a different audience, and each "
        "answers a slightly different question.")),

    C("Arnstein 1969", "Arnstein's ladder of citizen participation",
      {"t": "raw", "html": ARNSTEIN_SVG},
      B("Source: Sherry R. Arnstein, 'A Ladder of Citizen Participation', <em>Journal of the "
        "American Institute of Planners</em> 35(4): 216&ndash;224 (1969). Eight rungs in three "
        "bands. Arnstein's central claim is that participation without redistribution of power "
        "is an empty ritual: it lets those in power say that all sides were considered while "
        "only some sides benefit.", sm=True)),

    C("Reading the ladder", "Nonparticipation, tokenism and citizen power",
      TW([P("red", "Nonparticipation (rungs 1&ndash;2)",
            "Manipulation and therapy. In Arnstein's words, the aim is to let powerholders "
            "'educate' or 'cure' the participants, or to get them to endorse a decision already "
            "taken. Signing an attendance register that is later presented as consent is a common "
            "South Asian example."),
          P("amber", "Tokenism (rungs 3&ndash;5)",
            "Informing, consultation and placation. People hear and are heard, and a few may "
            "sit on a committee, but those in power keep the right to decide.")],
         [P("green", "Citizen power (rungs 6&ndash;8)",
            "Partnership, delegated power and citizen control. Decision rights, budgets or "
            "management pass in part or in full to citizens, with terms that the other side "
            "cannot withdraw at will."),
          P("cyan", "Context",
            "Arnstein drew her examples from three United States federal programmes of the 1960s: "
            "urban renewal, anti-poverty work and Model Cities. Her ladder is about citizens and "
            "public agencies, written for planners.")])),

    C("Pretty 1995", "Pretty's seven types of participation",
      B("Jules Pretty wrote for agricultural research and extension, where 'farmer "
        "participation' had become a project requirement. His typology runs from participation "
        "as a formality to participation that people start themselves.", sm=True),
      T(["Type", "What it looks like"],
        [["Passive", "People are told what is going to happen or has already happened"],
         ["In information giving", "People answer questions posed by extractive researchers "
          "and have no influence on the use of the findings"],
         ["By consultation", "External agents listen to views but keep control of problem "
          "definition and solutions"],
         ["For material incentives", "People provide labour or other resources in return for "
          "food, cash or other incentives, and stop when the incentive stops"],
         ["Functional", "People form groups to meet objectives the project has already set, "
          "usually after the major decisions are made"],
         ["Interactive", "People take part in joint analysis that leads to action plans and new "
          "or stronger local groups, which then control local decisions"],
         ["Self-mobilisation", "People take initiatives independently of external institutions "
          "to change systems"]]),
      B("Source: J. N. Pretty, <em>Regenerating Agriculture</em> (Earthscan, 1995), adapted from "
        "Adnan et al. (1992). The typology also appears in Pretty, 'Participatory learning for "
        "sustainable agriculture', <em>World Development</em> 23(8): 1247&ndash;1263 (1995). "
        "Versions differ slightly; some open with 'manipulative participation'.", sm=True),
      compact=True),

    C("Using Pretty", "Functional and interactive participation look alike from outside",
      B("The hardest line to draw in Pretty's typology is between functional and interactive "
        "participation. In both, a village committee meets, keeps minutes and manages funds. "
        "The difference is where the objectives came from and whether the group would act "
        "without the project."),
      TW([P("amber", "Illustrative: a functional watershed committee",
            "Formed because the project required one. Its plan copies the template. Members "
            "were nominated by the sarpanch. It meets when the field officer visits, and it "
            "dissolves when the last instalment is released.")],
         [P("green", "Illustrative: an interactive one",
            "Formed after a transect walk and a resource map showed whose fields lose topsoil. "
            "Members chose the treatment sequence, argued over it, changed it, and still "
            "allocate tank water two years after the project left.")]),
      H("cyan", "Pretty's point was practical: only the later types change how people learn "
        "about their own farms and resources, so only they produce lasting change. Ask for "
        "minutes from meetings the project did not attend.")),

    C("White 1996", "White's four forms: who wants participation, and why",
      B("Sarah White, 'Depoliticising development: the uses and abuses of participation', "
        "<em>Development in Practice</em> 6(1): 6&ndash;15 (1996), asks a question the ladders "
        "skip: what interest does each side have in a given form of participation?", sm=True),
      T(["Form", "Top-down interest", "Bottom-up interest", "Function"],
        [["Nominal", "Legitimation", "Inclusion", "Display"],
         ["Instrumental", "Efficiency", "Cost", "Means"],
         ["Representative", "Sustainability", "Leverage", "Voice"],
         ["Transformative", "Empowerment", "Empowerment", "Means and end"]]),
      B("Adapted from White (1996), Table 1, 'Interests in participation'. In the last row White "
        "gives the same interest, empowerment, for both sides.", sm=True),
      H("indigo", "Her examples: Zambian women's groups formed by government departments "
        "(nominal), people supplying labour for services cut under structural adjustment "
        "(instrumental), a Bangladeshi NGO inviting villagers to write their own cooperative "
        "by-laws (representative), and a case from the Philippines (transformative)."),
      compact=True),

    C("White's insight", "One project, several interests at once",
      B("White's typology is less a ladder than a map of motives. The same village committee "
        "can be nominal for the agency that needs a photograph for its annual report, "
        "instrumental for the engineer who needs free labour, and representative for the women "
        "who use it to press their own claims."),
      TW([P("cyan", "Participation is political",
            "White argues that participation may challenge patterns of dominance, and may "
            "equally be the means through which existing power relations are entrenched and "
            "reproduced. Who is involved, how, and on whose terms are contested questions.")],
         [P("amber", "Forms change over time",
            "Her paper adds a dynamic. Participation tends to decline, and where a few leaders "
            "run a project it can dwindle until it is nominal. It can also deepen: her Philippine "
            "hillside families joined a health programme for inclusion, then moved to "
            "representative and transformative participation as their confidence grew.")]),
      H("green", "Practical use: before a participatory exercise, write down who wants it and "
        "why, for each actor. If the only interest you can name for the community is 'they "
        "will be included', you are probably designing nominal participation.")),

    C("Comparing the three", "Arnstein, Pretty and White side by side",
      T(["", "Arnstein (1969)", "Pretty (1995)", "White (1996)"],
        [["Written for", "Urban planners in the United States", "Agricultural research and "
          "extension", "Development practitioners, especially NGOs"],
         ["Shape", "Eight-rung ladder in three bands", "Seven types from passive to "
          "self-mobilisation", "Four forms, each with two interests and a function"],
         ["Core question", "How much power do citizens hold?", "Does participation change "
          "how people learn and act?", "Who wants participation, and for what?"],
         ["Blind spot", "Treats 'citizens' as one group", "Says less about conflict inside "
          "communities", "Harder to use as a quick rating scale"]]),
      H("cyan", "Illustrative use in Pipalgaon: the employment scheme's village plan was "
        "approved in a gram sabha that the Dalit hamlet did not attend. Arnstein would call it "
        "informing, Pretty passive participation, and White nominal for the block office. The "
        "three labels point to the same fix: hold a ward-level meeting in the hamlet first."),
      compact=True),
]

# ===================== SECTION 04 =====================
SLIDES += [
    D("04", "Section Four", "PRA tools I: maps, walks, timelines"),

    C("Principles first", "What makes a PRA tool participatory",
      B("PRA tools rely on oral and visual communication so that literacy is not a condition "
        "of taking part. Drawing on the ground with sticks, seeds and coloured powder lets "
        "people who cannot write correct a map in front of everyone. The tools are simple; the "
        "discipline lies in how they are run."),
      TW([BL(["<strong>Visual and tangible:</strong> maps, diagrams and counters that everyone "
              "can see and change",
              "<strong>Group-based:</strong> analysis happens in public, which allows "
              "correction and also creates pressure to conform",
              "<strong>Sequenced:</strong> a map leads to a walk, which leads to a ranking"],
             color="cyan")],
         [BL(["<strong>Triangulated:</strong> the same question is approached by several tools "
              "and several groups",
              "<strong>Shared:</strong> the people who made the output keep it, or a copy",
              "<strong>Self-critical:</strong> the team asks every evening who was absent and "
              "what was not said"],
             color="green")]),
      H("amber", "The Participatory Methods Lab at /Labs/participatory-methods-lab.html walks "
        "through the core PRA toolkit with a step-by-step community mapping exercise.")),

    C("Social map", "The social map: who lives where",
      B("A social map shows households, hamlets, roads, wells, schools, temples, the "
        "anganwadi and anything else residents consider important. Groups draw it on the "
        "ground or on chart paper, then mark each household with symbols for, say, a widow at "
        "the head, a disabled member or a migrant away."),
      FLOW("Agree the purpose with the gram panchayat and the hamlets",
           "Draw boundaries and landmarks first",
           "Add every household, hamlet by hamlet",
           "Mark the attributes the group chose",
           "Cross-check against the voter list or survey frame",
           "Copy it to paper; leave the original"),
      H("cyan", "A social map drawn by the whole village is a useful sampling frame. It often "
        "lists households that official lists miss, including new settlers and people living "
        "on land without title.")),

    C("Social map pitfalls", "The map shows whoever drew it",
      TW([P("red", "What goes wrong",
            "The first people to pick up the stick are usually men from the main village. "
            "They draw their own lanes in detail and the Dalit or Adivasi hamlet as a vague "
            "smudge, or leave it off. Women's water sources and the places people avoid at "
            "night rarely appear unless someone asks.")],
         [P("green", "What to do about it",
            "Run separate mapping groups by hamlet and by gender, then bring the maps together "
            "and discuss the differences. Walk to any hamlet that appears only as a smudge. "
            "Note on the final map who drew which part.")]),
      H("amber", "Illustrative: in Pipalgaon the first map showed 610 households. Mapping in "
        "the hamlet across the stream added 140 more and two handpumps the main village "
        "believed were working and residents knew had failed. Treat the gap between maps as a "
        "finding and keep both maps.")),

    C("Resource map", "The resource map: land, water, forest and who uses them",
      B("A resource map shows fields, grazing land, forest, tanks, streams, wells and soils, "
        "with who owns, uses or controls each. It is the starting point for watershed, "
        "forest rights and land-use planning, where the main question is who has access to "
        "each resource, and in which season."),
      TW([P("cyan", "Questions it answers",
            "Which plots flood or erode? Where do women collect fuelwood, and how far is it? "
            "Which grazing land has been fenced? Which wells dry first? Where are community "
            "forest resources that a claim under the Forest Rights Act 2006 might cover?")],
         [P("amber", "Cautions",
            "Maps can be used against the people who drew them: a map showing forest use may "
            "later be read as evidence of encroachment. Agree in advance who keeps the map, "
            "who may copy it, and what it may be used for.")]),
      H("green", "Overlay the resource map on the social map to see which households depend on "
        "which resources. That overlay is often where the poorest households first become "
        "visible.")),

    C("Transect walk", "The transect walk: seeing the ground with the people who use it",
      B("A transect is a planned walk across the village area with a small group of residents, "
        "chosen to cross every zone: upland, fields, settlement, stream, forest edge. The team "
        "stops in each zone, observes, asks, and records the answers in a grid.", sm=True),
      T(["Illustrative grid", "Upland", "Rainfed fields", "Settlement", "Stream bank"],
        [["Soil and water", "Thin, rocky", "Red soil, one crop", "Handpumps, two dry", "Seasonal "
          "flow, sand mining"],
         ["Main uses", "Grazing, fuelwood", "Millet, pulses", "Housing, small shops",
          "Washing, brick kilns"],
         ["Who uses it", "Adivasi and Dalit households", "Small and marginal farmers",
          "All", "Fishing families, kiln workers"],
         ["Problems named", "Fencing of commons", "Erosion, no irrigation", "Drainage, "
          "water queues", "Falling water table"],
         ["Ideas raised", "Fodder plots", "Farm ponds, bunding", "Soak pits", "Check dam "
          "upstream"]]),
      H("cyan", "Illustrative data. Walk slowly, let residents choose the route after the first "
        "transect, and record disagreements between walkers in the grid itself."),
      compact=True),

    C("Mobility map", "Mobility maps: where people go, and who cannot",
      B("A mobility map shows the places people travel to for work, health care, markets, "
        "school, courts or family, with distance, cost, transport and frequency. Drawn "
        "separately by women and men, or by older and younger people, it reveals constraints "
        "that a list of services hides."),
      TW([P("indigo", "Illustrative: women's map, Pipalgaon",
            "Ration shop and anganwadi in the main village, weekly market 6 km away by shared "
            "auto, primary health centre 14 km with one bus a day. The block office never "
            "appears. Older women had not been to the district town in years.")],
         [P("cyan", "Illustrative: men's map",
            "Daily trips to the block town, seasonal migration to brick kilns and to a city "
            "construction market several hundred kilometres away, the district court for a land "
            "case. Distance is a cost of money for men and of permission for many women.")]),
      H("amber", "Mobility maps are a quick way to see where a service should be delivered. "
        "They also expose seasonal migration that a single-round household survey can miss.")),

    C("Timeline and trends", "Timelines and trend lines: the village's own history",
      B("A historical timeline lists events the community considers important: droughts, "
        "floods, a new road, a land dispute, an epidemic, the arrival of electricity. Elders "
        "usually lead, and the exercise works best when younger people ask the questions. "
        "Trend lines then track one variable over the same years, such as rainfall, forest "
        "cover, migration or the number of girls in school."),
      TW([P("green", "Why it matters",
            "Projects arrive with a short memory. A timeline shows which earlier schemes "
            "failed and why, which promises were broken, and which conflicts are still live. "
            "Many 'new' proposals turn out to have been tried in a previous decade.")],
         [P("amber", "Handling memory",
            "Dates in oral history are approximate and often anchored to other events: 'the "
            "year of the big flood', 'when the dam was built'. Record the anchor, check it "
            "against records if you can, and present the timeline as the village's account.")]),
      H("cyan", "Timelines are also a respectful way to open fieldwork: they begin with what "
        "people know, before the team asks about anything it wants.")),

    C("Recording outputs", "A PRA output is evidence only if it is recorded properly",
      B("Ground maps wash away and chart paper fades, but the bigger loss is context. A "
        "photograph of a map is useless if nobody noted which group drew it, how many took part, "
        "who did the drawing and what was argued about."),
      T(["Record", "Why"],
        [["Date, place, duration, tool, purpose", "So the output can be located and compared"],
         ["Number of participants by sex, age, caste or tribe group, and hamlet",
          "So readers can judge whose view it represents"],
         ["Who held the marker or stick, and for how long", "Drawing is a form of control"],
         ["Disagreements and how they were settled", "Consensus that hides a dispute is a "
          "misleading finding"],
         ["Photographs at stages, plus a clean paper copy", "To show how the output changed"],
         ["What participants said the output means", "Their interpretation is part of the data"]]),
      H("indigo", "Section 10 returns to documentation in detail. For now, assume any PRA "
        "output without this record will be dismissed by a careful reviewer, and rightly."),
      compact=True),
]

# ===================== SECTION 05 =====================
SLIDES += [
    D("05", "Section Five", "PRA tools II: calendars, ranking, Venn"),

    C("Seasonal calendar", "The seasonal calendar: the year as residents live it",
      B("A seasonal calendar plots variables across the months: rainfall, crop work, labour "
        "demand, wages, illness, food stocks, debt, festivals, migration. Participants usually "
        "score each month with seeds or stones, so the calendar can be read at a glance and "
        "compared across groups."),
      TW([P("cyan", "How to run it",
            "Draw twelve columns, using the local calendar if people prefer it. Take one "
            "variable at a time. Ask the group to distribute, say, twenty seeds across the "
            "months. Discuss the peaks before moving to the next variable.")],
         [P("green", "What it shows",
            "Hungry months, the months when cash runs short, when sickness peaks, and when "
            "people cannot attend meetings. Programme calendars set in a state capital often "
            "put training in the busiest weeks of the agricultural year.")]),
      H("amber", "Use the calendar to schedule your own work. A gram sabha called during "
        "harvest or the main migration season will be attended by those who did not leave, who "
        "are rarely the poorest.")),

    C("A calendar in numbers", "Illustrative seasonal calendar for Pipalgaon",
      {"t": "chart", "canvas": "pmSeasonChart",
       "title": "Seed scores out of 20 per variable, by month (Illustrative)",
       "source": "Illustrative teaching data, not a real village",
       "type": "line",
       "data": {"labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                           "Oct", "Nov", "Dec"],
                "datasets": [
                    {"label": "Local farm work", "data": [1, 0, 1, 1, 0, 3, 4, 3, 2, 3, 2, 0],
                     "borderColor": "#0369A1", "backgroundColor": "rgba(3,105,161,0.08)",
                     "tension": 0.3, "pointRadius": 3},
                    {"label": "Migration away", "data": [3, 4, 3, 2, 2, 0, 0, 0, 0, 0, 2, 4],
                     "borderColor": "#B45309", "backgroundColor": "rgba(180,83,9,0.08)",
                     "tension": 0.3, "pointRadius": 3},
                    {"label": "Illness", "data": [1, 1, 1, 1, 2, 2, 4, 4, 2, 1, 0, 1],
                     "borderColor": "#B91C1C", "backgroundColor": "rgba(185,28,28,0.08)",
                     "tension": 0.3, "pointRadius": 3}]},
       "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:5, title:{display:true,text:'Seeds (of 20)'} } } }"}},
      B("Read it as a group would: farm work peaks with the monsoon from June to October; "
        "migration fills the dry months from November to May; illness peaks in July and "
        "August. A health camp in March reaches the people who stayed; an employment scheme "
        "that opens work in July competes with farm work. The design implications follow from "
        "the shape of the curves.", sm=True),
      compact=True),

    C("Daily activity clock", "Daily activity clocks show whose time is scarce",
      B("An activity clock asks a group to describe a typical day hour by hour. Run separately "
        "for women and men, and for different seasons, it shows the unpaid work that fills "
        "women's days and the hours when each group could attend a meeting or training."),
      TW([P("amber", "Illustrative: woman, dry season",
            "Wake at 4.30, fetch water twice, cook, send children to school, graze goats, "
            "collect fuelwood, work on a road site from 9 to 5, cook again, wash, sleep after "
            "10. Free time: none that she could name.")],
         [P("cyan", "Illustrative: man, dry season",
            "Wake at 6, tea, work on the same road site, an hour at the tea shop, the "
            "evening at a neighbour's, sleep at 10. Free time: two to three hours spread across "
            "the day.")]),
      H("green", "Two uses: schedule meetings in the hours each group named as free, and count "
        "unpaid work as a cost when a project asks women to 'contribute' time to committees. "
        "The Care Economy 101 deck covers time-use measurement in more depth.")),

    C("Wealth ranking", "Wealth ranking: local categories of who is better and worse off",
      B("In wealth or well-being ranking, a few residents who know the village well sort cards, "
        "one per household, into piles they define: for example 'those who employ others', "
        "'those who manage', 'those who work for others', 'those who depend on others'. "
        "Several panels sort independently, and the results are compared."),
      TW([P("cyan", "Why practitioners use it",
            "It produces local criteria of poverty, which often include things a survey misses: "
            "a widow without adult sons, a household that has sold its draught animals, a "
            "family with a sick earner. It can target support faster than a census.")],
         [P("green", "An early Indian record",
            "<em>RRA Notes</em> 13 (IIED, 1991), the proceedings of a Bangalore workshop of PRA "
            "trainers, already carried a report on a wealth ranking exercise at Mahilong in "
            "Bihar, run by the NGO Krishi Gram Vikas Kendra.")]),
      H("amber", "Compare the local piles with the official below-poverty-line or ration-card "
        "lists. Households poor by local criteria and absent from the official list are a "
        "common, useful finding.")),

    C("Ranking with care", "Ranking neighbours in public has costs",
      TW([P("red", "Risks",
            "A household may be shamed by its placement or angered by it. Panels may rank their "
            "own kin as poorer to steer benefits toward them. If the ranking decides who "
            "receives a subsidy, the exercise becomes a contest, and panel members may face "
            "pressure afterwards."),
          P("amber", "Information that travels",
            "A public pile labelled 'those who depend on others' may circulate in the village "
            "long after the team leaves. Treat it as personal information about every household "
            "on the list.")],
         [P("green", "Safeguards",
            "Use small panels sitting apart from the main meeting, number the cards rather than "
            "naming households on anything that leaves the room, use several panels and "
            "average, and tell panels plainly what the ranking will and will not decide."),
          P("cyan", "Combining with other data",
            "Use ranking to check and supplement official lists. Where entitlements are "
            "legally defined, such as ration cards or pensions, ranking can identify households "
            "to help apply; it cannot replace the legal criteria.")])),

    C("Venn diagram", "Venn or chapati diagrams: institutions as people see them",
      B("A Venn diagram, often called a chapati diagram in South Asia, shows the institutions "
        "that matter to a group: the panchayat, the school, the self-help group federation, a "
        "moneylender, the forest department, the temple trust. The size of each circle shows its "
        "importance; the distance from the centre shows how accessible it is."),
      TW([P("cyan", "What it reveals",
            "Institutions that are large but far away, such as the bank branch, and institutions "
            "that are small but close, such as a local trader who lends. It also shows which "
            "institutions overlap: the same family may run the panchayat and the cooperative.")],
         [P("amber", "Doing it well",
            "Cut paper circles in several sizes before the session so people can try "
            "different arrangements and argue. Draw separate diagrams by gender and hamlet. "
            "Ask what each institution has done for the group in the last year.")]),
      H("green", "The diagram is a quick political economy of the village. Compare it with the "
        "Political Economy 101 deck's tools for mapping interests and power.")),

    C("Matrix and pairwise ranking", "Matrix ranking: choosing between options with criteria",
      B("In matrix ranking, a group scores options against criteria it chooses. Pairwise "
        "ranking compares options two at a time, which is easier when there are many. Both make "
        "priorities explicit and show where groups disagree.", sm=True),
      T(["Illustrative: priority works", "Cost to village", "Benefit to poorest", "Water saved",
         "Speed", "Total"],
        [["Farm ponds on private land", "3", "1", "4", "4", "12"],
         ["Desilting the common tank", "4", "4", "4", "2", "14"],
         ["Fodder plots on the upland", "3", "4", "1", "3", "11"],
         ["Concrete lane in main village", "2", "1", "0", "5", "8"]]),
      H("amber", "Illustrative scores, 0 to 5, from a single group. Run the same matrix with the "
        "Dalit hamlet and the women's group: if the totals change order, you have found the "
        "disagreement the gram sabha needs to discuss. Criteria matter more than scores, so "
        "record where each criterion came from."),
      compact=True),

    C("Choosing tools", "Which tool for which question",
      T(["Question", "Tool", "Output", "Main caution"],
        [["Who lives here and who is missed?", "Social map", "Household list and frame",
          "Map shows the drawers' view"],
         ["Who uses which resources?", "Resource map, transect", "Access and use by group",
          "Maps can be used against users"],
         ["When are people busy, sick or away?", "Seasonal calendar, activity clock",
          "Timing of needs and availability", "Run by gender and season"],
         ["Who is poor by local criteria?", "Wealth ranking", "Local categories and lists",
          "Public ranking can shame"],
         ["Which institutions matter?", "Venn diagram", "Importance and access",
          "Powerful institutions overstated"],
         ["What should be done first?", "Matrix or pairwise ranking", "Priorities with "
          "criteria", "Group pressure to agree"],
         ["What changed and why?", "Timeline, trend lines", "Local history", "Memory "
          "is selective"]]),
      H("cyan", "Sequence tools so that each output feeds the next. A social map gives the "
        "frame, a wealth ranking places households on it, and a matrix ranking asks the poorest "
        "group which works it would choose."),
      compact=True),
]

# ===================== SECTION 06 =====================
SLIDES += [
    D("06", "Section Six", "Participatory governance in India"),

    C("The 73rd Amendment", "The 73rd Amendment made the village assembly constitutional",
      B("The Constitution (Seventy-third Amendment) Act 1992 came into force on 24 April 1993, "
        "now marked as National Panchayati Raj Day. It inserted Part IX (Articles 243 to 243-O) "
        "and the Eleventh Schedule, which lists 29 subjects that states may devolve to "
        "panchayats."),
      TW([P("cyan", "Article 243A: the Gram Sabha",
            "A Gram Sabha may exercise such powers and perform such functions at the village "
            "level as the legislature of a state may, by law, provide. The Gram Sabha is the "
            "body of all registered voters in the panchayat area; the panchayat is the elected "
            "council.")],
         [P("green", "Article 243D: reservation",
            "Seats are reserved for Scheduled Castes and Scheduled Tribes in proportion to "
            "population, and not less than one-third of seats, including chairpersons' posts, "
            "for women. Reserved seats may rotate between constituencies, reserved chairpersons' "
            "offices must rotate between panchayats, and state law sets the manner.")]),
      H("amber", "Article 243A leaves the Gram Sabha's powers to state law, so they vary "
        "widely. Before running any participatory planning exercise, read the state Panchayat "
        "Raj Act and its rules on Gram Sabha meetings, quorum and minutes.")),

    C("PESA 1996", "PESA gives Gram Sabhas in Scheduled Areas specific powers",
      B("The Provisions of the Panchayats (Extension to the Scheduled Areas) Act 1996 extends "
        "Part IX to the Fifth Schedule areas with modifications. Its starting point is that each "
        "village, which may be a hamlet or group of hamlets managing its affairs by custom, has "
        "its own Gram Sabha (s4(b) and (c)).", sm=True),
      T(["Section", "Power of the Gram Sabha"],
        [["s4(d)", "Competent to safeguard traditions and customs, community resources and the "
          "customary mode of dispute resolution"],
         ["s4(e)(i)", "Approve plans, programmes and projects for social and economic "
          "development before the panchayat implements them"],
         ["s4(e)(ii)", "Identify persons as beneficiaries under poverty alleviation and other "
          "programmes"],
         ["s4(f)", "Certify the panchayat's utilisation of funds for those plans and projects"],
         ["s4(i)", "Be consulted (Gram Sabha or panchayat at the appropriate level) before "
          "land acquisition and resettlement"]]),
      B("Source: PESA Act 1996, s4, which sets the features state panchayat laws in Scheduled "
        "Areas must follow. The powers reach a Gram Sabha through state law and rules.", sm=True),
      compact=True),

    C("A case", "Niyamgiri 2013: when the Gram Sabha decided",
      B("In <em>Orissa Mining Corporation v. Ministry of Environment and Forest</em>, decided on "
        "18 April 2013 by a three-judge bench of the Supreme Court (W.P. (Civil) No. 180 of "
        "2011), the question was bauxite mining on Niyam Dongar in the Niyamgiri hills of "
        "Odisha, a mountain the Adivasi communities living there hold sacred."),
      TW([P("cyan", "What the Court held",
            "Gram Sabhas have a role under the Scheduled Tribes and Other Traditional Forest "
            "Dwellers (Recognition of Forest Rights) Act 2006 in safeguarding the customary and "
            "religious rights of forest dwellers. It directed that the Gram Sabhas decide on "
            "those claims, with a district judge as observer.")],
         [P("green", "What happened",
            "Twelve Gram Sabhas were held in 2013, seven in Rayagada district and five in "
            "Kalahandi. All twelve rejected the mining project. On 8 January 2014 the Ministry of "
            "Environment and Forests rejected Stage II forest clearance for the mine.")]),
      H("amber", "The lesson for practitioners: a participatory forum with legal standing can "
        "change a national decision. It also shows that the first question is always who counts "
        "as the community: here, which villages would hold a Gram Sabha at all.")),

    C("Participatory budgeting", "Participatory budgeting: residents allocate part of a budget",
      TERM("Participatory budgeting (PB)",
           "A process in which residents propose, discuss and vote on how a defined share of a "
           "public budget is spent, usually on local works. The government commits in advance "
           "to fund the winning proposals within the set amount."),
      TW([P("cyan", "Porto Alegre, 1989",
            "PB began in the Brazilian city of Porto Alegre in 1989, when a new administration "
            "led by the Workers' Party introduced it to bring residents into budget decisions "
            "and redirect spending toward poorer neighbourhoods. It became the template copied "
            "worldwide.")],
         [P("green", "What makes it participatory",
            "A real budget line, rules published before the process starts, meetings in every "
            "ward, a vote, and public tracking of whether chosen works were built. Without "
            "money that follows the vote, PB is consultation under another name.")]),
      H("indigo", "India's two best-known experiments run on very different scales: Kerala's "
        "People's Plan Campaign at state level from 1996, and Pune's ward-level participatory "
        "budget from 2006.")),

    C("Kerala 1996", "Kerala's People's Plan Campaign",
      B("Kerala's decentralised planning followed the 73rd and 74th Amendments and the state's "
        "1994 enabling laws. An evaluation by the Planning Commission's Programme Evaluation "
        "Organisation records the main steps of the Ninth Five Year Plan period."),
      ST([CARD("35&ndash;40%", "of state plan funds to be devolved to local governments, "
               "decision announced July 1996", "cyan", "PEO, Planning Commission"),
          CARD("Aug 1996", "People's Plan Campaign launched, with the Kerala Sastra Sahitya "
               "Parishad among the organisations mobilising", "green",
               "PEO, Planning Commission"),
          CARD("30 / 30 / 10", "conditions: at least 30% productive sectors, at most 30% "
               "infrastructure, at least 10% for women's programmes", "amber",
               "PEO, Planning Commission")], cols=3),
      H("cyan", "Ward-level Grama Sabhas, chaired by the ward member, were the main channel for "
        "people's participation, and the evaluation found they emerged as the main body "
        "for articulating needs. The scale was new: a whole state's "
        "plan was opened to village assemblies at once.")),

    C("Kerala evaluated", "Kerala's Grama Sabhas, as an official evaluation found them",
      B("The Programme Evaluation Organisation surveyed four districts (Kollam, Ernakulam, "
        "Malappuram and Wayanad), nine gram panchayats and an independent sample of 460 "
        "household heads, with field visits in mid-2004."),
      ST([CARD("52%", "of sampled households satisfied with beneficiary selection (range 38% to "
               "87% across panchayats)", "amber", "PEO evaluation, Planning Commission"),
          CARD("72%", "of the dissatisfied said undue preference went to members' close "
               "circles", "red", "PEO evaluation, Planning Commission"),
          CARD("29%", "of selected beneficiaries received individual benefits without ever "
               "attending a Grama Sabha", "indigo", "PEO evaluation, Planning Commission")],
         cols=3),
      H("cyan", "The same report found that Grama Sabhas played a significant role in beneficiary "
        "selection, but that their representative base was low and dwindling. Non-attending "
        "beneficiaries were more common among households above the poverty line (34.7%) than "
        "below it (25.1%). Participation was real and partly captured at the same time.")),

    C("Pune since 2006", "Pune's ward-level participatory budget",
      B("The Pune Municipal Corporation formally introduced participatory budgeting in 2006. "
        "Residents submit suggestions for local works in their ward on prescribed forms, and a "
        "share of the municipal budget is set aside for them."),
      TW([P("green", "Strengths a 2013 review found",
            "The Centre for Environment Education's critical review credited the simplicity of the "
            "process for citizens, its regular annual cycle, a substantial allocation of funds, "
            "and some response to suggestions from the poor.")],
         [P("amber", "Weaknesses it found",
            "It named outreach, transparency of the process, its place in slum localities, the "
            "role of the elected corporator, public deliberation and year-round engagement as "
            "the areas needing improvement.")]),
      H("cyan", "Pune shows what a modest, durable PB looks like: low barriers to entry, but "
        "suggestions without deliberation. The step from submitting a form to debating "
        "priorities with neighbours is the part most Indian PB experiments have found hardest. "
        "Source: 'Participatory Budgeting in Pune: A critical review', CEE (2013).")),

    C("VB-G RAM G 2025", "The new rural employment law and the Gram Sabha",
      B("The Viksit Bharat Guarantee for Rozgar and Ajeevika Mission (Gramin) Act 2025 (Act 36 "
        "of 2025) repeals the Mahatma Gandhi National Rural Employment Guarantee Act 2005 "
        "(s37), with the repeal effective from 1 July 2026. It keeps a role for village "
        "assemblies in planning and audit.", sm=True),
      T(["Provision", "What it says"],
        [["s2(w)", "A Viksit Gram Panchayat Plan is formulated by the gram panchayat through a "
          "participatory and evidence-based process"],
         ["s19(d)", "The gram panchayat prepares the plan after considering the recommendations "
          "of the Gram Sabha and the Ward Sabhas"],
         ["s20(1)&ndash;(2)", "The Gram Sabha monitors all works and conducts regular social "
          "audits, in a manner the Central Government prescribes"],
         ["s20(3)", "The panchayat must give the Gram Sabha all records: muster rolls, bills, "
          "vouchers, measurement books, sanction orders, digital records, geo-tagged photos"],
         ["s24(e)", "Strengthening of the social audit mechanism and technology-enabled "
          "systems"]]),
      H("amber", "Status as of October 2026. Watch the rules made under s20(2): the "
        "participatory quality of the audit will depend on them more than on the Act."),
      compact=True),
]

# ===================== SECTION 07 =====================
SLIDES += [
    D("07", "Section Seven", "Social audits and scorecards"),

    C("Social audit", "A social audit checks public spending against what people saw",
      TERM("Social audit",
           "A process in which the people a scheme is meant to serve examine its official "
           "records, verify them against what happened on the ground, and present findings "
           "in a public meeting where officials must answer."),
      TW([P("cyan", "Financial audit",
            "Done by auditors, from records, for the government. Asks whether money was spent "
            "according to the rules. Findings go to the department and, for central funds, "
            "to the Comptroller and Auditor General.")],
         [P("green", "Social audit",
            "Done with workers and residents, from records and testimony, in public. Asks "
            "whether the work exists, whether the people on the muster roll worked and were "
            "paid, and whether the work was worth doing.")]),
      H("amber", "The two complement each other. A road can pass a financial audit with every "
        "voucher in order and fail a social audit because half the names on the muster roll "
        "belong to people who never worked on it.")),

    C("MKSS and the jan sunwai", "The public hearing that started it",
      B("The Mazdoor Kisan Shakti Sangathan, a union of workers and farmers formed in Rajasthan "
        "on 1 May 1990, developed the jan sunwai, or public hearing. Official expenditure "
        "records, such as muster rolls and bills for materials, were obtained and read aloud "
        "to villagers, who then testified about what had actually happened. The hearings were "
        "organised independently of the government."),
      TW([P("green", "Why it worked",
            "It joined documents to testimony. A muster roll listing a dead man as a labourer, "
            "read aloud in front of his widow, is evidence nobody in the room can dispute. Hard "
            "documents gave villagers' claims a weight that complaint alone never had.")],
         [P("cyan", "Where it led",
            "The hearings exposed how much depended on access to records. MKSS's 40-day protest "
            "in Beawar, beginning on 6 April 1996, became part of the campaign that produced "
            "state right to information laws and, nationally, the Right to Information Act "
            "2005.")]),
      H("indigo", "Social audit in India began as organic participation, in Mansuri and Rao's "
        "term, and the state later wrote it into law. Section 07 follows that path.")),

    C("The legal basis", "Social audit in Indian law",
      T(["Instrument", "What it requires", "Status (October 2026)"],
        [["MGNREGA 2005, s17", "Gram Sabha to conduct regular social audits of all works in "
          "the panchayat", "Repealed by VB-G RAM G Act 2025, s37, from 1 July 2026"],
         ["MGNREG Audit of Schemes Rules 2011 (June 2011)", "Social audit in every gram "
          "panchayat at least once in six months; each state to set up a Social Audit Unit; "
          "framed with the CAG", "Repealed with the parent Act by s37(1); audits pending on "
          "1 July 2026 continue under s37(4)"],
         ["VB-G RAM G Act 2025, s20 and s24(e)", "Gram Sabha monitors works and conducts "
          "regular social audits; records to be made available", "In force; manner of audit "
          "to be prescribed by the Centre"],
         ["Meghalaya Community Participation and Public Services Social Audit Act 2017 (Act 7 "
          "of 2017)", "Participatory social audit of public services and schemes across "
          "departments", "Act dated 4 April 2017; rules made in 2019"]]),
      H("amber", "Practitioners auditing works begun under MGNREGA should check the transitional "
        "provisions in s37 of the 2025 Act, which preserve actions taken under the repealed law."),
      compact=True),

    C("Independence", "Who runs the audit matters as much as the law",
      B("A social audit run by the department that spent the money is a self-assessment. "
        "Andhra Pradesh set the model for independence: since May 2009 an autonomous body, the "
        "Society for Social Audit, Accountability and Transparency (SSAAT), has been responsible "
        "for conducting social audits in the state, at arm's length from the implementing "
        "department."),
      TW([P("green", "What independence requires",
            "A unit outside the implementing department, its own budget, resource persons "
            "recruited from the community and trained, the right to see every record, and "
            "public hearings chaired by someone the implementing officials do not control.")],
         [P("red", "How it erodes",
            "Records released late or in part, hearings scheduled at short notice, resource "
            "persons dependent on the department for pay, and findings that never produce "
            "recovery of money or disciplinary action. Each of these turns audit into "
            "ritual.")]),
      H("cyan", "Ask of any social audit system: in the last year, how many findings led to "
        "money recovered or action against an official? A system that finds problems and "
        "fixes none teaches people that speaking up is pointless.")),

    C("Running a social audit", "The steps of a social audit",
      FLOW("Obtain records: muster rolls, bills, measurement books, sanctions",
           "Train village resource persons, with workers among them",
           "Verify door to door and at worksites",
           "Hold the public hearing with officials present",
           "Record findings, responses and decisions",
           "Track action taken and report back"),
      TW([P("cyan", "Verification",
            "Resource persons visit every worker listed, ask whether they worked and were paid, "
            "and measure the work. Discrepancies are written up case by case, with names, so "
            "they can be answered.")],
         [P("amber", "The hearing",
            "Findings are read out. Workers testify. Officials respond on the spot. Decisions, "
            "such as recovery of a sum or re-verification, are minuted and signed, and the "
            "minutes are displayed.")]),
      H("green", "The step most often skipped is the last. Schedule the follow-up hearing "
        "before the first one closes.")),

    C("Community score card", "The community score card: users and providers score a service",
      B("CARE Malawi developed the Community Score Card in 2002, in a project to find "
        "sustainable ways to improve health services. Users and providers each score a service "
        "on indicators they generate, then meet to compare scores and agree an action plan. "
        "CARE's 2013 toolkit sets out five phases."),
      FLOW("Planning and preparation",
           "Score card with the community",
           "Score card with service providers",
           "Interface meeting and action planning",
           "Action plan implementation and M&amp;E"),
      H("cyan", "Phases two and three can run at the same time. The interface meeting is the "
        "heart of the method: it turns complaint into negotiation. Source: CARE, <em>Community "
        "Score Card (CSC) Toolkit</em> (2013), based on CARE Malawi's original generic guide.")),

    C("Evidence", "Community monitoring of health clinics in Uganda",
      B("Martina Bj&ouml;rkman and Jakob Svensson, 'Power to the People: Evidence from a "
        "Randomized Field Experiment on Community-Based Monitoring in Uganda', <em>Quarterly "
        "Journal of Economics</em> 124(2): 735&ndash;769 (2009). Through two rounds of village "
        "meetings, local NGOs encouraged communities to be more involved with the state of "
        "health services and strengthened their capacity to hold local providers to account."),
      ST([CARD("50", "public primary health facilities, 25 treatment and 25 control", "cyan",
               "Bj&ouml;rkman and Svensson, QJE 2009"),
          CARD("33%", "reduction in under-five mortality in treatment communities", "green",
               "Bj&ouml;rkman and Svensson, QJE 2009"),
          CARD("20%", "higher use of general outpatient services after one year", "amber",
               "Bj&ouml;rkman and Svensson, QJE 2009")], cols=3),
      H("indigo", "A year on, treatment communities were more involved in monitoring and health "
        "workers appeared to exert more effort; absenteeism fell. The study also reported "
        "higher child weight. One trial in one country: Section 09 sets it beside Indian results "
        "that point the other way.")),

    C("A worked scorecard", "Illustrative: scoring the Pipalgaon anganwadi",
      T(["Indicator (chosen by mothers)", "Mothers' score", "Workers' score", "Agreed action"],
        [["Centre opens on time", "2", "4", "Display opening hours; mothers' group checks weekly"],
         ["Take-home ration received in full", "2", "3", "Read the stock register aloud at "
          "the monthly meeting"],
         ["Children from the far hamlet attend", "1", "2", "Worker visits the hamlet twice a "
          "month; panchayat repairs the footbridge"],
         ["Growth monitoring explained to mothers", "3", "4", "Use a picture chart during "
          "weighing"],
         ["Treatment of children from all castes", "2", "5", "Raised with the supervisor; "
          "seating rule agreed"]]),
      H("amber", "Illustrative scores, 1 to 5. The largest gap, on equal treatment, is the "
        "finding: providers often rate themselves well on exactly the indicator users rate "
        "worst. The interface meeting has to make that gap discussable without turning it into "
        "an attack on the worker, who is usually underpaid and overloaded herself."),
      compact=True),
]

# ===================== SECTION 08 =====================
SLIDES += [
    D("08", "Section Eight", "Photovoice, video and stories"),

    C("Photovoice", "Photovoice: people photograph their own lives",
      B("Caroline Wang and Mary Ann Burris set out the method in 'Photovoice: Concept, "
        "Methodology, and Use for Participatory Needs Assessment', <em>Health Education and "
        "Behavior</em> 24(3): 369&ndash;387 (1997), drawing on work with rural women in Yunnan "
        "Province, China."),
      TW([P("cyan", "Three goals",
            "To enable people to record and reflect their community's strengths and concerns; "
            "to promote critical dialogue and knowledge about important issues through group "
            "discussion of the photographs; and to reach policymakers.")],
         [P("green", "Three roots",
            "Freire's critical consciousness, feminist theory's attention to whose standpoint "
            "produces knowledge, and documentary photography's use of images as social evidence. "
            "The first root links Photovoice directly to Section 02.")]),
      H("amber", "Photovoice suits questions about everyday conditions that are hard to describe "
        "in an interview, such as unsafe routes to school, the state of a toilet block, or the "
        "places where adolescents gather.")),

    C("Running Photovoice", "A Photovoice project, step by step",
      FLOW("Agree the theme with participants",
           "Train on cameras, consent and safety",
           "Participants photograph over one to three weeks",
           "Each selects and captions a few images",
           "Group discussion to find themes",
           "Exhibition or meeting with decision-makers"),
      TW([P("cyan", "Participant control",
            "Participants choose which photographs to discuss and which to keep private, write "
            "the captions, and decide what is exhibited. The researcher's coding comes after "
            "theirs, and differences are reported.")],
         [P("red", "Third parties in the frame",
            "People who appear in photographs did not consent to the study. Train participants "
            "to ask permission, avoid identifiable faces where possible, and never photograph "
            "children without a guardian's agreement. Section 11 covers consent.")]),
      H("green", "Most phones now record location in image metadata. Strip it before images "
        "leave the group.")),

    C("Participatory video", "Participatory video began with the Fogo Process",
      B("In 1967 the National Film Board of Canada's Challenge for Change programme sent "
        "filmmaker Colin Low to Fogo Island, Newfoundland, following the vision of the "
        "Newfoundland academic Donald Snowden. They filmed islanders, screened the films back to the "
        "community, and used the screenings to start discussion about the island's future."),
      TW([P("green", "Process over product",
            "The guiding principle was that the films mattered for the conversations they "
            "started. Recordings were followed by debates that shaped the next recordings, a "
            "feedback cycle that participatory video projects still use.")],
         [P("cyan", "In South Asia",
            "Many community video projects train residents to report on local services and "
            "rights. The discipline is the same: the community decides what to "
            "film, watches it first, and decides who else sees it.")]),
      H("amber", "Video is persuasive, and that cuts both ways. Agree in writing who owns the "
        "footage and who may edit it before anyone presses record.")),

    C("Digital Green", "Farmer-made video for agricultural extension in India",
      B("Digital Green began as a research project in India using locally produced video of "
        "farmers demonstrating practices, screened by a local mediator to small groups. Its "
        "components were a participatory process for content production, a local video "
        "database, human-mediated dissemination and a fixed sequence for starting in new "
        "villages."),
      ST([CARD("16", "villages in a 13-month trial, eight control and eight experimental",
               "cyan", "Gandhi et al., ITID 2009"),
          CARD("1,470", "households in the trial", "green", "Gandhi et al., ITID 2009"),
          CARD("7&times;", "adoption of certain practices compared with training-and-visit "
               "extension", "amber", "Gandhi et al., ITID 2009"),
          CARD("10&times;", "more effective per dollar spent, on a cost-per-adoption basis",
               "indigo", "Gandhi et al., ITID 2009")], cols=4),
      H("cyan", "Source: Gandhi, Veeraraghavan, Toyama and Ramprasad, 'Digital Green: "
        "Participatory Video and Mediated Instruction for Agricultural Extension', <em>Information "
        "Technologies and International Development</em> 5(1) (2009). A small, early trial: treat the multiples as "
        "a promising early result that needs larger replication.")),

    C("Most Significant Change", "Most Significant Change: stories, chosen in public",
      B("Rick Davies developed the Most Significant Change (MSC) technique during PhD fieldwork "
        "with the Christian Commission for Development in Bangladesh in 1994. Davies and Jess "
        "Dart's <em>The 'Most Significant Change' (MSC) Technique: A Guide to Its Use</em> "
        "(2005) remains the standard reference."),
      FLOW("Agree broad categories of change to watch",
           "Collect stories: what was the most significant change, and why?",
           "Groups at each level select the most significant story",
           "Record the reasons for each selection",
           "Feed the selections and reasons back to storytellers"),
      H("green", "The selection is the analysis. Recording why a panel chose a story tells you "
        "what the organisation values, which is often different from what its logframe says. "
        "MSC suits large, open-ended programmes whose outcomes are hard to specify in advance, "
        "and works as a complement to indicators.")),

    C("Images and identity", "Visual methods raise their own consent problems",
      TW([P("red", "What an image discloses",
            "A face identifies a person. A house, a shrine or a caste marker can identify a "
            "family or a community. A geotag identifies a location. In a small village, a "
            "caption with a first name identifies the speaker to everyone who reads it."),
          P("amber", "Consent that changes",
            "A woman may agree to be filmed about water and object when the film is shown at the "
            "district office. Consent to record and consent to show are separate, and the second "
            "has to be asked for each audience.")],
         [P("green", "Practical rules",
            "Separate consent for capture, for group discussion, for exhibition and for "
            "publication online. Offer blurring or silhouettes. Keep raw footage on encrypted "
            "storage and destroy what is not needed."),
          P("cyan", "Personal data in law",
            "Photographs and recordings of identifiable people are personal data under the "
            "Digital Personal Data Protection Act 2023. Section 11 covers the research "
            "exemption and its conditions.")])),

    C("Analysing visual data", "Turning pictures and stories into findings",
      T(["Source", "Participants' analysis", "Researcher's analysis", "Report"],
        [["Photovoice images", "Captions and group themes", "Coding of captions and "
          "discussion transcripts", "Both sets of themes, with differences noted"],
         ["Participatory video", "What the group chose to film and screen", "Content and "
          "audience response", "Screenings held and decisions taken"],
         ["MSC stories", "Selections and reasons at each level", "Patterns across selected "
          "and unselected stories", "What the organisation values, and what it ignores"],
         ["Maps and diagrams", "Group's interpretation", "Comparison across groups and tools",
          "Agreement and disagreement between groups"]]),
      H("indigo", "The rule across all four: participants' interpretation is data, and the "
        "researcher's interpretation is a second layer. Report both. The Visual Ethnography "
        "101 and Qualitative Methods 101 decks cover coding and analysis in depth."),
      compact=True),
]

# ===================== SECTION 09 =====================
SLIDES += [
    D("09", "Section Nine", "Participatory MEL and the evidence"),

    C("Participatory MEL", "Participatory monitoring, evaluation and learning",
      B("Participatory MEL applies the logic of this deck to the question of whether a "
        "programme is working. Communities help choose what to measure, collect some of the "
        "data, interpret the results and decide what changes."),
      TW([P("amber", "Conventional M&amp;E",
            "Indicators fixed in the logframe at design. Data collected by staff or "
            "enumerators. Analysis in the office. Results reported upward to management and "
            "funders, often months later.")],
         [P("green", "Participatory M&amp;E",
            "Some indicators defined by the people the programme serves. Data collected partly "
            "by them, for example through scorecards or village registers. Results discussed "
            "where they were produced and used for decisions there.")]),
      H("cyan", "Most real systems mix the two. A funder needs comparable indicators across "
        "districts; a village needs indicators that answer its own questions. The MEL Basics "
        "101 deck covers the conventional system this one adds to.")),

    C("Community indicators", "Indicators communities choose, beside the ones funders need",
      T(["Outcome", "Standard indicator", "Indicator a community might choose (Illustrative)"],
        [["Food security", "Share of households with acceptable food consumption score",
          "Number of months the household ate two meals a day without borrowing"],
         ["Water", "Households within a set distance of an improved source", "Whether the "
          "handpump in our hamlet worked through May"],
         ["Women's voice", "Share of women attending the Gram Sabha", "Whether a woman from "
          "our group spoke and her point was minuted"],
         ["School quality", "Pupil-teacher ratio", "Whether children in Class 3 can read the "
          "story the teacher wrote on the board"],
         ["Employment scheme", "Person-days per household", "Whether wages arrived before the "
          "next market day"]]),
      H("amber", "Community indicators are often more sensitive to change and closer to what "
        "people value. They are harder to aggregate. Keep a small core of standard indicators "
        "and let each community add its own, recorded with the reasons it gave."),
      compact=True),

    C("Evidence: Uttar Pradesh", "Information alone did not bring parents into schools",
      B("Abhijit Banerjee, Rukmini Banerji, Esther Duflo, Rachel Glennerster and Stuti Khemani, "
        "'Pitfalls of Participatory Programs: Evidence from a Randomized Evaluation in "
        "Education in India', <em>American Economic Journal: Economic Policy</em> 2(1): "
        "1&ndash;30 (2010). Village Education Committees had existed in every Uttar Pradesh "
        "village since 2001."),
      ST([CARD("280", "villages in Jaunpur district: 65 in each of three interventions, 85 "
               "comparison", "cyan", "J-PAL summary of Banerjee et al. 2010"),
          CARD("No change", "in parents visiting schools or volunteering time or money after "
               "information meetings and community report cards", "red",
               "J-PAL summary of Banerjee et al. 2010"),
          CARD("7.9%", "more likely to read at least letters, for children who could not read "
               "at baseline, where volunteers ran reading camps", "green",
               "J-PAL summary of Banerjee et al. 2010")], cols=3),
      H("indigo", "The two information interventions raised what committee members knew but did "
        "not change participation or learning. Only the third, which trained local volunteers to "
        "teach reading, improved outcomes, by letting individuals act without waiting for "
        "collective action.")),

    C("Evidence: Indonesia", "Top-down audits beat grassroots monitoring of road projects",
      B("Benjamin Olken, 'Monitoring Corruption: Evidence from a Field Experiment in Indonesia', "
        "<em>Journal of Political Economy</em> 115(2): 200&ndash;249 (2007), compared two "
        "ways of reducing theft in village road projects, measured as the gap between official "
        "costs and an independent engineers' estimate."),
      TW([ST([CARD("600+", "village road projects in the experiment", "cyan",
                   "Olken, JPE 2007"),
              CARD("8 pts", "fall in missing expenditures when audit probability rose from 4% "
                   "to 100%", "green", "Olken, JPE 2007")], cols=1)],
         [P("amber", "Grassroots monitoring",
            "Increasing participation in village accountability meetings had little average "
            "impact. It reduced missing expenditures only where free-rider problems and elite "
            "capture were limited."),
          P("cyan", "The reading",
            "Participation is one accountability tool among several. Where elites control the "
            "meeting, an outside auditor with sanctions may protect villagers' money better "
            "than their own assembly.")]),
      H("indigo", "Olken concludes that traditional top-down monitoring can reduce corruption "
        "even in a highly corrupt environment.")),

    C("Why results differ", "Uganda worked and Uttar Pradesh did not: possible reasons",
      TW([P("green", "Uganda (Bj&ouml;rkman and Svensson 2009)",
            "One service, the clinic, with a clear provider who could change behaviour. Village "
            "meetings produced a joint action plan with that provider. Communities had a "
            "specific target and a specific person to hold to account.")],
         [P("amber", "Uttar Pradesh (Banerjee et al. 2010)",
            "Committees and parents were asked to act collectively on a diffuse problem, learning "
            "levels, with weak levers over teachers employed by the state. Information raised "
            "awareness but gave nobody an easy action to take.")]),
      B("These explanations are interpretations, offered by many readers of the two studies; "
        "neither paper tested them against each other. They suggest three questions for any "
        "design: is there a clear provider, can the community sanction or reward that provider, "
        "and is the action asked of people cheap enough to take?"),
      H("cyan", "Context decides. Mansuri and Rao (2013) put the importance of context at the "
        "centre of their review of participatory development.")),

    C("Representation", "Reserved seats for women changed what panchayats built",
      B("Raghabendra Chattopadhyay and Esther Duflo, 'Women as Policy Makers: Evidence from a "
        "Randomized Policy Experiment in India', <em>Econometrica</em> 72(5): 1409&ndash;1443 "
        "(2004), used the random reservation of one-third of village council head positions "
        "for women, under the 73rd Amendment, to study 265 village councils in West Bengal and "
        "Rajasthan."),
      TW([P("green", "What they found",
            "Women heads invested more in public goods closer to women's stated concerns: "
            "drinking water and roads in West Bengal, drinking water in Rajasthan. They invested "
            "less in goods closer to men's concerns, education in West Bengal and roads in "
            "Rajasthan.")],
         [P("cyan", "Why it matters here",
            "Who sits in the chair changes what a participatory process produces. Reservation "
            "is a structural guarantee of presence. Participatory methods can then work on "
            "whether those present are heard.")]),
      H("amber", "Randomised reservation makes this one of the cleanest causal results on "
        "participation in South Asia. The Gender Mainstreaming 101 deck covers gender analysis "
        "of programmes more broadly.")),

    C("The big review", "What Mansuri and Rao concluded",
      B("<em>Localizing Development: Does Participation Work?</em> (World Bank Policy Research "
        "Report, 2013) reviewed the evidence on participatory development and the "
        "World Bank's own participatory projects."),
      T(["Finding", "Implication for practice"],
        [["Community participation in health and education showed modestly positive results, "
          "mostly when combined with other inputs such as trained staff", "Pair participation "
          "with the resources a service needs"],
         ["Community-based development had a limited impact on income poverty", "Do not "
          "promise income gains from participation alone"],
         ["Little evidence that induced participation builds long-lasting cohesion",
          "Plan for what survives after the project, or accept that it may not"],
         ["Elite capture and weak collective action limit results", "Design for capture from "
          "the start (Section 11)"],
         ["Most World Bank participatory projects lacked attention to context and learning-oriented "
          "M&amp;E", "Budget for monitoring that can change the project"]]),
      H("cyan", "The report frames participatory development, done right, as a way to help "
        "repair civil society failure, and it concentrates on how hard participation is to "
        "induce through projects."),
      compact=True),

    C("Evaluating participation", "How to evaluate a participatory programme",
      B("Evaluating participation means measuring three things that are easy to confuse: "
        "whether the process happened as intended, whether it changed who holds power, and "
        "whether it changed outcomes people care about."),
      T(["Level", "Questions", "Evidence"],
        [["Process", "Who attended, who spoke, who decided? Were records shared?",
          "Attendance by sex, caste and hamlet; minutes; observation notes"],
         ["Voice and power", "Did marginal groups' proposals reach the plan? Were officials "
          "made to answer?", "Tracking proposals from ward meeting to sanctioned works"],
         ["Outcomes", "Did services, incomes or wellbeing improve, and for whom?",
          "Comparison with similar areas, ideally randomised or a credible counterfactual"],
         ["Durability", "Does the forum still meet without the project?", "Follow-up visits a "
          "year or more after exit"]]),
      H("green", "The Impact Evaluation 101 deck covers counterfactual designs. For "
        "participatory programmes, add the process and power levels: a programme can improve an "
        "outcome through a route that bypassed participation entirely, and you will want to "
        "know."),
      compact=True),
]

# ===================== SECTION 10 =====================
SLIDES += [
    D("10", "Section Ten", "Doing it well: documentation and practice"),

    C("Rigour", "Participatory work can be rigorous, and it has to show it",
      B("Reviewers often dismiss participatory evidence as anecdote. The fault usually lies in "
        "the documentation. A participatory study is rigorous when a "
        "reader can see who produced each piece of evidence, under what conditions, and how "
        "the team moved from outputs to conclusions."),
      TW([P("cyan", "What makes it credible",
            "A clear record of each session, triangulation across tools and groups, reporting of "
            "disagreement, member checking (returning findings to participants), and an "
            "explicit account of the team's own position and influence.")],
         [P("red", "What undermines it",
            "Photographs of charts with no record of who made them, a single 'community view' "
            "built from one meeting, quotations without context, and findings that match the "
            "project's prior hopes exactly.")]),
      H("amber", "The Qualitative Methods 101 deck sets out the general quality criteria. "
        "This section applies them to participatory tools.")),

    C("The session record", "A session record template",
      T(["Field", "Example entry (Illustrative)"],
        [["Session", "Social map, Dalit hamlet, Pipalgaon, 14 March, 10.30 to 12.45"],
         ["Convened by", "Two team members, one woman, one man; local language Marathi"],
         ["Participants", "23 at peak: 14 women, 9 men; ages 19 to 70; all from the hamlet"],
         ["Who drew", "Two young men for the first hour; three women after the team asked"],
         ["Main output", "Map of 140 households; two failed handpumps; footbridge washed away"],
         ["Disagreements", "Whether the new houses by the road belong to the hamlet; left "
          "unresolved and marked on the map"],
         ["Participants' reading", "'We are not on the panchayat's map, so we get nothing'"],
         ["Team reflection", "Our presence drew a landowner from the main village for twenty "
          "minutes; people spoke less while he stayed"]]),
      H("cyan", "Write the record the same day. Every row in this template answers a question a "
        "sceptical reader will ask."),
      compact=True),

    C("Triangulation", "Triangulate across tools, groups and sources",
      B("No single tool or group gives the whole picture. Triangulation means looking at the "
        "same question from several directions and treating disagreement as information."),
      T(["Type", "How", "Illustrative example"],
        [["Across tools", "Ask the same question with a map, a ranking and interviews",
          "The resource map and the transect both show the upland commons fenced"],
         ["Across groups", "Run tools separately by gender, caste, hamlet, age", "Women rank "
          "water first; men rank the road first"],
         ["Across sources", "Compare outputs with records and surveys", "Wealth ranking finds "
          "38 poor households missing from the ration list"],
         ["Across team members", "Two note-takers; compare notes before writing up",
          "One recorded the landowner's interruption; the other did not"]]),
      H("amber", "When sources disagree, report the disagreement and what you did about it. "
        "Disagreement between the women's and men's rankings is a finding about the village, "
        "and the gram sabha may need to see it."),
      compact=True),

    C("Positionality", "Who the team is changes what people say",
      B("Participants respond to who is asking. A team arriving in a government jeep, with the "
        "block officer's introduction, speaking the dominant caste's dialect, will hear a "
        "different account from a team introduced by a women's federation."),
      TW([P("cyan", "Before fieldwork",
            "Write a short positionality statement: the team's caste, gender, religion, "
            "language, institutional link and funder, and how each might shape access and "
            "answers. The Participatory Methods Lab provides a template.")],
         [P("green", "During and after",
            "Note in each session record how the team's presence seemed to matter. Ask a local "
            "co-researcher to review interpretations. Report these reflections in the method "
            "section of the report.")]),
      H("amber", "Positionality is a methods issue, so it belongs in the report. The Feminist "
        "Research 101 and Decolonial Development 101 decks take it further.")),

    C("A worked example", "Illustrative: a participatory needs assessment in Pipalgaon",
      FLOW("Week 1: meet panchayat, hamlets, women's groups; agree purpose and consent",
           "Week 2: social and resource maps by hamlet; transects",
           "Week 3: seasonal calendars and wealth ranking by group",
           "Week 4: matrix ranking of priorities by group",
           "Week 5: return findings in each hamlet; then a full Gram Sabha",
           "Week 6: written report shared with panchayat and participants"),
      TW([P("cyan", "Design choices",
            "Every tool is run in each hamlet before any village-wide meeting. The team "
            "schedules sessions in the hours the activity clocks showed as free. Findings return "
            "to each group before the Gram Sabha.")],
         [P("amber", "What it costs",
            "Six weeks of a two-person team, local co-researchers paid at the scheme wage or "
            "above, chart paper and transport. Participants' time is a cost too; record it and "
            "keep sessions short.")]),
      H("green", "Illustrative timetable. Compress it and the hamlet sessions are the first "
        "thing to go, which removes the people the exercise most needed to hear.")),

    C("Choosing an approach", "Decision table: which participatory approach for which purpose",
      T(["Purpose", "Suitable approach", "Watch for"],
        [["Understand needs before designing a programme", "PRA sequence: maps, calendars, "
          "ranking", "Raising expectations you cannot meet"],
         ["Check whether public money was spent as recorded", "Social audit with records",
          "Retaliation against witnesses"],
         ["Improve a specific service with its providers", "Community score card", "Turning "
          "the meeting into blame of frontline workers"],
         ["Understand everyday experience hard to put in words", "Photovoice", "Consent of "
          "people in the photographs"],
         ["Track change in a complex programme", "Most Significant Change plus core indicators",
          "Selecting only success stories"],
         ["Allocate a public budget", "Participatory budgeting", "No money behind the vote"],
         ["Build a movement's own knowledge", "Participatory action research", "Outsiders "
          "steering the agenda"]]),
      H("cyan", "When in doubt, ask who will decide what happens to the results. If the answer "
        "is only the project, choose a lighter method and call it consultation in the report."),
      compact=True),

    C("Checklist", "A practitioner's checklist for a participatory exercise",
      TW([BL(["<strong>Before:</strong> who asked for this, and who decides on the results?",
              "Which groups could be left out, and how will you reach them separately?",
              "What does state law say about Gram Sabha or ward meetings here?",
              "How will consent be sought, and for which uses?",
              "When are people free, by season and by hour?"], color="cyan")],
         [BL(["<strong>During:</strong> who holds the marker, and for how long?",
              "Who has not spoken? Have you asked them directly, away from the group?",
              "Are disagreements being recorded or smoothed over?",
              "<strong>After:</strong> did findings go back to each group before any report?",
              "What decision did the exercise change, and can you show it?"], color="green")]),
      H("amber", "If the last question has no answer six months later, the exercise was "
        "consultation at best. Say so in the report; it is useful evidence for the next design.")),

    C("Practise it", "The Participatory Methods Lab",
      B("ImpactMojo's Participatory Methods Studio, at <a href=\"/Labs/participatory-methods-lab.html\">"
        "/Labs/participatory-methods-lab.html</a>, turns this deck into practice. It runs in the "
        "browser as a guided studio."),
      TW([P("cyan", "What it covers",
            "Extractive and participatory research compared, the core PRA toolkit, a focus "
            "group design checklist with a sample guide for a drought-affected village, a "
            "step-by-step community mapping exercise, and participatory M&amp;E design.")],
         [P("green", "Worked material",
            "A community scorecard case for anganwadi services, a list of power dynamics to "
            "watch, an ethical checklist for participatory work, and a positionality statement "
            "template you can fill in for your own team.")]),
      H("amber", "Suggested exercise: use the Lab's mapping steps to plan the Pipalgaon social "
        "map session, fill in the positionality template for your own team, then compare your "
        "plan with the session record template two slides back.")),
]

# ===================== SECTION 11 =====================
SLIDES += [
    D("11", "Section Eleven", "Power, ethics and consent"),

    C("The tyranny critique", "Participation as tyranny",
      B("Bill Cooke and Uma Kothari's edited volume <em>Participation: The New Tyranny?</em> "
        "(Zed Books, 2001), opening with their chapter 'The case for participation as tyranny' "
        "(pp. 1&ndash;15), was presented by its publisher as the first book-length treatment of "
        "the gulf between the fashionable rhetoric of participation and what happens when "
        "consultants and activists practise it."),
      TW([P("red", "The charge",
            "Participatory development can lead to the unjust and illegitimate exercise of "
            "power. Practices that are at best naive about power may, at worst, reinforce the "
            "inequalities they claim to challenge.")],
         [P("cyan", "What practitioners took from it",
            "Treat the participatory meeting as a political space with its own hierarchies. Ask "
            "who set the agenda, whose knowledge counted, and who could afford to disagree in "
            "public. Expect consensus to need explaining.")]),
      H("amber", "The critique did not end participatory practice. It made reflexivity about "
        "power a standard part of good practice, which is why the rest of this section exists.")),

    C("Elite capture", "Elite capture: when the better-off take the benefits",
      TERM("Elite capture",
           "The appropriation of a participatory process, or of the resources it allocates, by "
           "people who already hold more land, money, status or office. It can be open, through "
           "control of meetings and lists, or quiet, through who is told about the meeting."),
      TW([P("amber", "Evidence from this deck",
            "Kerala's official evaluation found that 29% of selected beneficiaries received "
            "individual benefits without ever attending a Grama Sabha, and that 72% of "
            "dissatisfied households blamed preference for members' circles (PEO, Planning "
            "Commission). Olken (2007) found grassroots monitoring worked only where elite "
            "capture was limited.")],
         [P("green", "Design responses",
            "Hold separate meetings for marginal groups before the main one. Publish beneficiary "
            "lists and criteria in advance. Use secret ballots where choices are contested. "
            "Combine community processes with independent audit, as the Indonesian results "
            "suggest.")]),
      H("cyan", "Capture is a matter of degree. Some elite involvement brings skills and links "
        "that a project needs; the question is whether it excludes others.")),

    C("Caste and gender in the room", "Who speaks at a village meeting is not random",
      TW([P("red", "What practitioners commonly observe",
            "Dominant-caste men sit at the front and speak first. Dalit residents sit apart or "
            "stay at the edge. Women attend in smaller numbers, may sit separately, and are "
            "spoken for by husbands or the ward member. Adivasi hamlets far from the venue send "
            "one or two people, or none."),
          P("amber", "Why counts mislead",
            "A register showing that 40% of attendees were women says nothing about whether any "
            "spoke, or whether what they said reached the minutes. Attendance is necessary for "
            "voice and insufficient on its own.")],
         [P("green", "What helps",
            "Separate pre-meetings by caste, gender and hamlet, with their outputs presented by "
            "their own representatives at the main meeting. Venues neutral to caste, such as the "
            "school rather than a temple courtyard. A quorum rule that requires women's presence. "
            "Recording who spoke, as well as who came."),
          P("cyan", "Further study",
            "The Social Margins 101 deck covers caste and exclusion in depth.")])),

    C("Spotting tokenism", "Signs that participation has become ritual",
      T(["Sign", "What it suggests", "What to ask"],
        [["The plan matches the template exactly", "Decisions were made before the meeting",
          "Which item in the plan came from residents?"],
         ["Attendance register longer than the room", "Signatures collected afterwards",
          "Can you name five people who spoke?"],
         ["Every meeting ends in consensus", "Disagreement is not safe to voice", "What was the "
          "last proposal the meeting rejected?"],
         ["Findings never return to the village", "Extraction under a participatory label",
          "Who has a copy of the map?"],
         ["Committees meet only when staff visit", "Functional participation, in Pretty's terms",
          "When did the committee last meet alone?"],
         ["No budget follows the vote", "Consultation presented as decision", "What money "
          "did the meeting control?"]]),
      H("amber", "Each row maps back to Arnstein's tokenism band. Use the third column in "
        "monitoring visits; the answers are quick to check and hard to fake."),
      compact=True),

    C("Ethics: the Indian guidance", "Community permission does not replace individual consent",
      B("The Indian Council of Medical Research's <em>National Ethical Guidelines for "
        "Biomedical and Health Research Involving Human Participants</em> (2017) apply to "
        "health research. Their provisions on community engagement and consent are a useful "
        "reference for social research with communities in India."),
      T(["Provision", "What it says"],
        [["s2.10.4", "Community engagement does not replace individual informed consent; it "
          "ensures the community's needs are addressed and consent processes are appropriate"],
         ["s5.10.1", "Permission of gatekeepers, the head or leader of a group or a culturally "
          "appropriate authority, may be obtained in writing or recorded, and should be "
          "witnessed"],
         ["s5.10.2", "Where community consent is needed through a body such as a village "
          "panchayat, its quorum must be met; individual consent is still required"]]),
      H("cyan", "For participatory work the rule is two-layered: the panchayat or Gram Sabha may "
        "permit the exercise, and each person still decides whether to take part, what to say "
        "and what may be recorded."),
      compact=True),

    C("Consent in groups", "Group settings change what consent can promise",
      TW([P("red", "What you cannot promise",
            "Confidentiality within the group. Anything said at a mapping session or a social "
            "audit hearing is heard by neighbours, and may reach a landowner, a contractor or an "
            "official. Consent forms that promise confidentiality in a public meeting are "
            "promising something the team cannot deliver."),
          P("amber", "Public by design",
            "Social audits and jan sunwais are public on purpose: the public setting is what "
            "makes officials answer. Witnesses there need a different kind of protection from "
            "interviewees.")],
         [P("green", "What you can do",
            "Explain at the start that what is said in the group will be known to others in the "
            "group. Ask people to keep others' contributions to themselves, while saying plainly "
            "that this cannot be enforced. Offer a private conversation afterwards for anything "
            "sensitive."),
          P("cyan", "Children and adolescents",
            "Use a guardian's permission plus the young person's own assent, and keep "
            "sessions on topics that will not expose them to punishment at home or school.")])),

    C("Data protection", "Participatory data under the DPDP Act 2023",
      B("Maps with household names, wealth rankings, scorecards with comments, photographs and "
        "video of identifiable people are personal data under the Digital Personal Data "
        "Protection Act 2023. Its duties, with the 2025 Rules, apply from 13 May 2027; the Data "
        "Protection Board has existed since 13 November 2025."),
      TW([P("cyan", "The research exemption",
            "From 13 May 2027, section 17(2)(b) exempts processing necessary for research, archiving "
            "or statistical purposes, if the personal data is not used to take any decision specific "
            "to a data principal and the processing follows the standards in Rule 16 and the Second "
            "Schedule of the 2025 Rules.")],
         [P("amber", "Where participatory work falls outside it",
            "A wealth ranking used to decide who receives a benefit, or a scorecard used to "
            "discipline a named worker, is used to take decisions about specific people. The "
            "exemption's condition is not met, and the Act's ordinary duties apply from 13 May 2027.")]),
      H("green", "Practical steps: number households instead of naming them in anything that "
        "leaves the village, store photographs securely, delete what you do not need, and record "
        "what each output may be used for. The Data Protection and the DPDP Act 101 deck covers "
        "the Act in detail. Status as of October 2026.")),

    C("Do no harm", "Protecting the people who speak up",
      B("Participatory methods ask people to say difficult things in public: that a contractor "
        "stole wages, that a neighbour is richer than he admits, that the anganwadi worker "
        "turns some children away. Speaking up can carry a cost after the team has left."),
      TW([P("red", "Risks to anticipate",
            "Retaliation against social audit witnesses or resource persons, loss of work from a "
            "landlord or contractor named in a hearing, conflict between hamlets over a ranking, "
            "and backlash against women who speak in a mixed meeting.")],
         [P("green", "Safeguards",
            "Agree with participants what will be said publicly and by whom. Let groups present "
            "collectively, as a group. Keep a list of local legal aid and "
            "grievance contacts. Follow up after hearings, and report threats to the "
            "authority that ordered the audit.")]),
      H("amber", "A participatory exercise that exposes people to harm and then leaves has "
        "taken their information and their risk. The Research Ethics 101 and Safeguarding and "
        "PSEA 101 decks cover these duties in more detail.")),

    C("Where next", "Where next",
      B("Participatory methods sit where research methods, community practice and governance "
        "meet. These ImpactMojo 101 decks take each strand further, and the Lab gives you "
        "practice."),
      TW([BL(["<a href=\"/101-courses/community-dev.html\">Community Development 101</a>: "
              "organising, self-help groups and panchayati raj",
              "<a href=\"/101-courses/qual-methods.html\">Qualitative Methods 101</a>: "
              "interviews, focus groups, coding and quality criteria",
              "<a href=\"/101-courses/decolonize-dev.html\">Decolonial Development 101</a>: "
              "whose knowledge counts, and who decides",
              "<a href=\"/101-courses/visual-eth.html\">Visual Ethnography 101</a>: "
              "photographs, film and the ethics of images"], color="cyan")],
         [BL(["<a href=\"/101-courses/mel-basics.html\">MEL Basics 101</a>: indicators, "
              "monitoring systems and learning",
              "<a href=\"/101-courses/research-ethics.html\">Research Ethics 101</a>: consent, "
              "risk and review",
              "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the "
              "DPDP Act 101</a>: personal data in practice",
              "<a href=\"/Labs/participatory-methods-lab.html\">Participatory Methods Lab</a>: "
              "mapping, scorecards, ethics checklists"], color="green")]),
      H("amber", "Start with the Lab's community mapping exercise, then read the Qualitative "
        "Methods deck's section on focus groups before your first field session.")),
]

# ===================== END =====================
SLIDES += [
    {"type": "end",
     "eyebrow": "Participatory Methods 101 &middot; Complete",
     "headline": "Hand over the marker,<br>then keep the record.",
     "byline": "Participatory methods are only as good as the power they move and the care with "
               "which they are documented. Explore the rest of the ImpactMojo 101 Series, free "
               "forever.",
     "ctas": [
         {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
         {"label": "Participatory Methods Lab",
          "href": "https://www.impactmojo.in/Labs/participatory-methods-lab.html"},
         {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"}],
     "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
]

DECK = {
    "slug": "participatory-methods",
    "title": "Participatory Methods 101",
    "description": ("Participatory Methods 101: a free foundational course for development "
                    "practitioners and researchers in South Asia. Freire, Fals-Borda and "
                    "Chambers; the ladders of Arnstein, Pretty and White; PRA tools; Gram Sabhas, "
                    "PESA and participatory budgeting in India; social audits and community "
                    "scorecards; Photovoice, participatory video and Most Significant Change; "
                    "participatory MEL and the evidence; elite capture, consent and the DPDP Act. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": SLIDES,
}

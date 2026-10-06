# -*- coding: utf-8 -*-
"""
Inclusive Education 101 -- ImpactMojo 101 Series (native deck spec)
What inclusive education means in international and Indian law, who is excluded from school in
South Asia and why, the RTE Act 2009, the RPwD Act 2016, NEP 2020 chapter 6 and Samagra Shiksha,
the data, neighbours' laws, classroom practice, teacher preparation, measurement with the
Washington Group modules, and a practitioner's toolkit.
Build: python3 scripts/deck-builder/build.py inclusive_education

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


def PB(color, title, blocks):
    return {"t": "panel", "color": color, "title": title, "blocks": blocks}


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


# Source strings used more than once
GC4 = "CRPD Committee, General Comment No. 4 (2016), CRPD/C/GC/4"
CENSUS = "Census 2011, in MoSPI, Disabled Persons in India: A Statistical Profile 2016"
NSS = "NSS 76th round (July to December 2018), NSS Report No. 583, MoSPI"
UDISE26 = "UDISE+ 2025-26, Ministry of Education, PIB release of 7 July 2026"
DHS = ("DHS Program API, indicator ED_NARS_B_BTH: NFHS-5 India 2019-21, Bangladesh DHS 2022, "
       "Nepal DHS 2022, Pakistan DHS 2017-18")
NEP = "National Education Policy 2020, Ministry of Education"
SS21 = "PIB release on Samagra Shiksha, 4 August 2021"
UNTC = "UN Treaty Collection, CRPD status page, read 6 October 2026"

SLIDES = []

# ===================== S1 TITLE, S2 TOC =====================
SLIDES += [
    {"type": "title",
     "main": "Inclusive<br>Education<br>101",
     "sub": "What inclusion means in law and in the classroom: the CRPD and General Comment 4, the "
            "RTE Act 2009, the RPwD Act 2016, NEP 2020 and Samagra Shiksha, the data, neighbours' "
            "laws, teaching practice and how to measure it, for practitioners in South Asia",
     "tags": ["100 Slides", "South Asia Focus", "Free Forever", "RTE, RPwD and NEP 2020"]},

    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "What inclusive education means"},
         {"name": "Models of disability"},
         {"name": "Who is left out in South Asia"},
         {"name": "The Constitution and the RTE Act 2009"},
         {"name": "The RPwD Act 2016"},
         {"name": "NEP 2020 and Samagra Shiksha"},
         {"name": "What the data shows"},
         {"name": "Neighbours' laws"},
         {"name": "Classroom practice"},
         {"name": "Teachers and support staff"},
         {"name": "Measuring inclusion"},
         {"name": "A practitioner's toolkit"},
     ]},
]

# ===================== SECTION 01 =====================
SLIDES += [
    D("01", "Section One", "What inclusive education means"),

    C("The definition", "Inclusive education is a change to the school, made for every learner",
      TERM("Inclusive education",
           "A process of systemic reform that changes content, teaching methods, approaches, "
           "structures and strategies in education to overcome barriers, so that all students of "
           "the relevant age range get an equitable and participatory learning experience in the "
           "environment that best corresponds to their requirements and preferences. Wording from "
           + GC4 + ", paragraph 11."),
      TW([P("cyan", "What the definition asks of a school",
            "The duty sits with the system. The school changes its curriculum, its timetable, its "
            "buildings, its tests and its teaching so that a child who learns differently can take "
            "part. The child is not asked to become someone else before being admitted.")],
         [P("green", "Who it covers",
            "General Comment 4 is written about disability, because it interprets the disability "
            "convention. Its logic applies to any child the system leaves behind: a girl kept home "
            "to look after siblings, a Santali speaker taught only in Odia, a child of migrant brick "
            "kiln workers who moves twice a year.")]),
      H("amber", "Keep this definition in mind through the deck. Each later section asks the same "
        "question of a law, a dataset or a lesson plan: who is expected to change, the child or the "
        "school?")),

    C("Four words", "Exclusion, segregation, integration and inclusion are four different things",
      B("The CRPD Committee separates four situations that are often blurred together in Indian "
        "programme documents. The distinctions decide whether a project is moving a system forward "
        "or relabelling what already exists."),
      T(["Term", "What it means, in the Committee's words (paraphrased)", "A South Asian example (Illustrative)"],
        [["Exclusion", "Students are directly or indirectly prevented from, or denied, access to "
          "education in any form", "A child with cerebral palsy in a hill village who has never "
          "been enrolled anywhere"],
         ["Segregation", "Education of students with disabilities in separate settings designed for "
          "an impairment, in isolation from students without disabilities", "A residential school "
          "for blind children in the district town"],
         ["Integration", "Placing students with disabilities in mainstream institutions on the "
          "understanding that they adjust to its standard requirements", "A deaf child enrolled in "
          "Class 4 with no interpreter, sitting at the back"],
         ["Inclusion", "Systemic reform of content, methods, structures and strategies so that all "
          "students learn together", "The same child with an Indian Sign Language interpreter, "
          "captioned videos and a teacher trained to plan for her"]]),
      B("Source: " + GC4 + ", paragraph 11. The Committee adds that placing students in mainstream "
        "classes without structural change does not constitute inclusion.", sm=True)),

    C("A right of the learner", "General Comment 4 says what kind of thing inclusive education is",
      B("Paragraph 10 of General Comment 4 lists four ways inclusive education is to be understood. "
        "Each one has a practical consequence for how a school, a parent or a programme behaves."),
      T(["Paragraph 10 says inclusive education is", "What follows in practice"],
        [["(a) A fundamental human right of every learner; the right of the individual learner and "
          "not, for children, of a parent or caregiver, whose responsibilities are subordinate to the "
          "rights of the child", "A parent's wish to keep a disabled daughter at home does not end the "
          "state's duty to her"],
         ["(b) A principle that values the well-being of all students and respects their dignity "
          "and autonomy", "Children are consulted about their own support, in ways suited to age"],
         ["(c) A means of realising other human rights, and the primary means by which persons with "
          "disabilities can lift themselves out of poverty", "Education spending on disabled "
          "children is also poverty and employment policy"],
         ["(d) The result of continuing, proactive commitment to remove barriers, with changes to "
          "the culture, policy and practice of regular schools", "Inclusion is a process with "
          "milestones, measured over years"]]),
      H("amber", "Point (a) is the one that surprises practitioners in South Asia, where family "
        "decisions about schooling are usually taken as final. Source: " + GC4 + ", paragraph 10.")),

    C("Salamanca, 1994", "The Salamanca Statement made regular schools the starting point",
      B("More than 300 participants representing <strong>92 governments and 25 international "
        "organisations</strong> met in Salamanca, Spain, from 7 to 10 June 1994, at the World "
        "Conference on Special Needs Education organised by the Government of Spain with UNESCO. "
        "The conference adopted the Salamanca Statement and a Framework for Action."),
      Q("Regular schools with this inclusive orientation are the most effective means of combating "
        "discriminatory attitudes, creating welcoming communities, building an inclusive society and "
        "achieving education for all.",
        "Salamanca Statement, paragraph 2 (UNESCO, ED-94/WS/18, 1994)"),
      TW([P("cyan", "Why it mattered",
            "Before 1994 most international work on disability and schooling spoke of special "
            "provision. Salamanca put the regular school at the centre and treated separate schools "
            "as the exception that needs a reason.")],
         [P("amber", "Its efficiency argument",
            "The same paragraph says inclusive schools give an effective education to most children "
            "and improve the cost-effectiveness of the whole system. Finance ministries listen to "
            "that sentence more readily than to a rights argument.")])),

    C("Salamanca's reach", "The Framework for Action named many more children than disabled children",
      B("Paragraph 3 of the Salamanca Framework for Action sets its guiding principle: schools should "
        "accommodate all children regardless of their physical, intellectual, social, emotional, "
        "linguistic or other conditions. It then lists who that includes."),
      TW([BL(["Disabled and gifted children",
              "Street and working children",
              "Children from remote or nomadic populations",
              "Children from linguistic, ethnic or cultural minorities",
              "Children from other disadvantaged or marginalised areas or groups"], color="cyan")],
         [P("green", "Reading it in South Asia",
            "Each line has a local face. Working children in Sivakasi or in carpet weaving in "
            "Bhadohi; nomadic Bakarwal families in Jammu and Kashmir; Rohingya children in Cox's "
            "Bazar; Adivasi children whose language is absent from the textbook. Inclusion in this "
            "wider sense is the frame NEP 2020 later adopts with its term socio-economically "
            "disadvantaged groups.")]),
      H("cyan", "Source: Salamanca Statement and Framework for Action on Special Needs Education, "
        "UNESCO and Ministry of Education and Science, Spain (1994), Framework paragraph 3.")),

    C("CRPD Article 24 (1) and (2)", "Article 24 turns inclusion into a treaty obligation",
      B("The Convention on the Rights of Persons with Disabilities (CRPD) was adopted by the UN "
        "General Assembly on 13 December 2006. Article 24(1) requires States Parties to ensure "
        "<strong>an inclusive education system at all levels</strong> and lifelong learning. Article "
        "24(2) lists what that requires."),
      TW([BL(["(a) No exclusion from the general education system, or from free and compulsory "
              "primary or secondary education, on the basis of disability",
              "(b) Access to inclusive, quality and free primary and secondary education in the "
              "communities where children live",
              "(c) Reasonable accommodation of the individual's requirements"], color="cyan")],
         [BL(["(d) The support required, within the general education system",
              "(e) Effective individualised support measures in environments that maximise academic "
              "and social development, consistent with the goal of full inclusion"], color="green"),
          H("amber", "Clause (e) is where individual education plans come from. Clause (c) is where "
            "a ramp, a scribe or extra exam time comes from.")]),
      B("Source: CRPD (2006), Article 24, text as published by UN DESA. India ratified on "
        "1 October 2007 (" + UNTC + ").", sm=True)),

    C("CRPD Article 24 (3) to (5)", "Language, communication and teachers are part of the right",
      B("Article 24 goes beyond admission. It names the means of communication a child needs, and "
        "it puts a duty on the state to employ teachers who can use them."),
      T(["Clause", "What it requires", "What it looks like in India"],
        [["24(3)(a)", "Learning of Braille, alternative script, augmentative and alternative "
          "communication, orientation and mobility, and peer support", "Braille textbooks, "
          "communication boards for a child with cerebral palsy, cane training"],
         ["24(3)(b)", "Learning of sign language and promotion of the linguistic identity of the deaf "
          "community", "Indian Sign Language taught as a full language with its own grammar"],
         ["24(3)(c)", "Education of blind, deaf or deafblind children in the most appropriate "
          "languages, modes and means", "A choice of setting made around communication needs"],
         ["24(4)", "Employ teachers, including teachers with disabilities, qualified in sign language "
          "or Braille, and train all staff", "Deaf and blind teachers in ordinary schools"],
         ["24(5)", "Access to tertiary education, vocational training and lifelong learning",
          "Section 32 of the RPwD Act 2016 reserves at least 5% of seats in aided higher education"]]),
      B("Source: CRPD Article 24, UN DESA text; Rights of Persons with Disabilities Act 2016, s32(1).",
        sm=True)),

    C("General Comment 4", "Two lines in General Comment 4 that programme designers often miss",
      B("General Comment 4 was adopted by the CRPD Committee and issued on 25 November 2016. It is "
        "the Committee's authoritative reading of Article 24. Two of its paragraphs change how a "
        "government or a donor should plan."),
      TW([P("red", "Paragraph 31: accommodation now",
            "The denial of reasonable accommodation is discrimination, and the duty to provide it is "
            "<strong>immediately applicable and not subject to progressive realisation</strong>. A "
            "state cannot say that a ramp or a scribe will come when the budget allows. In paragraph "
            "30 the Committee adds that accommodation may not be conditional on a medical diagnosis "
            "of impairment.")],
         [P("amber", "Paragraph 40: one system",
            "Progressive realisation means moving as fast and effectively as possible towards "
            "Article 24, and the Committee says this is <strong>not compatible with sustaining two "
            "systems of education</strong>, a mainstream one and a special or segregated one. It "
            "encourages states to move budget towards inclusive education.")]),
      H("cyan", "Hold paragraph 40 against section 31 of India's RPwD Act 2016 in Section 5 of this "
        "deck, which gives a child the choice of a neighbourhood school or a special school. The two "
        "texts pull in different directions. Source: " + GC4 + ".")),

    C("SDG 4.5", "SDG target 4.5 makes equity measurable",
      B("Target 4.5 of the Sustainable Development Goals reads: <em>by 2030, eliminate gender "
        "disparities in education and ensure equal access to all levels of education and vocational "
        "training for the vulnerable, including persons with disabilities, indigenous peoples and "
        "children in vulnerable situations</em>. Indicator 4.5.1 measures it through parity indices, "
        "female to male, rural to urban, bottom to top wealth quintile and, as data become available, "
        "disability status."),
      ST([CARD("0.91", "Wealth parity index, primary completion (poorest 20% / richest 20%)", "cyan",
               "UN SDG progress, Goal 4, 2026"),
          CARD("0.68", "Wealth parity index, lower secondary completion", "amber",
               "UN SDG progress, Goal 4, 2026"),
          CARD("0.34", "Wealth parity index, upper secondary completion", "red",
               "UN SDG progress, Goal 4, 2026")]),
      H("cyan", "Read the three numbers together. Globally, the poorest children nearly match the "
        "richest in finishing primary school and fall far behind by upper secondary. Exclusion grows "
        "with every stage, which is why an inclusion programme that stops at Class 5 has done a third "
        "of the job. Source: sdgs.un.org, Goal 4 progress text, 2026.")),
]

# ===================== SECTION 02 =====================
SLIDES += [
    D("02", "Section Two", "Models of disability"),

    C("Why models matter", "The model you hold decides what you try to fix",
      B("A model of disability is a working answer to a simple question: where does the problem sit? "
        "Teachers, officials and parents rarely say which model they use, but their decisions reveal "
        "it. A headteacher who says a child is not ready for school is using one model. A district "
        "officer who asks why the school has no ramp is using another."),
      TW([P("amber", "The charity model",
            "Disability is misfortune, and the response is kindness. Disabled children are recipients "
            "of help, often in separate homes or schools run by religious or voluntary bodies. The "
            "giver decides what is given, and nobody owes the child anything.")],
         [P("red", "The medical model",
            "Disability is a defect in the body or mind, and the response is diagnosis and treatment. "
            "The specialist is in charge. Schooling waits for a certificate, a therapy plan or a cure, "
            "and the ordinary school sees the child as a case to refer elsewhere.")]),
      H("cyan", "Both models still shape South Asian systems. Disability certificates, which gate "
        "most entitlements, come from the medical model. Many special schools began in the charity "
        "model. Neither model asks the school to change.")),

    C("The social model", "The social model moves the problem from the child to the barriers",
      TERM("Social model of disability",
           "The view that people are disabled by barriers in the environment, in attitudes and in "
           "institutions, and that removing those barriers is the main task. Impairment is a fact "
           "about the body; disability is what happens when the world is built for other bodies."),
      FLOW("IMPAIRMENT: low vision in a Class 6 girl",
           "BARRIER: small print on the blackboard, no large-print book",
           "RESULT: she falls behind and is called a slow learner",
           "FIX: seat near the board, large print, a teacher who reads aloud"),
      B("The flow is Illustrative, and it shows the logic. Change the barrier and the outcome "
        "changes, though the impairment stays the same. The social model came out of disability "
        "movements, and it is the reason the CRPD speaks of barriers in its definitions."),
      H("green", "For an education planner the social model has a practical virtue. Barriers can be "
        "listed, costed and removed. A school audit, like the one in Section 12, is the social model "
        "turned into a checklist.")),

    C("The human rights model", "The rights model adds duties, remedies and dignity",
      B("The CRPD and India's RPwD Act 2016 go one step further than the social model. They treat the "
        "disabled child as a holder of rights, and the state as the bearer of duties that can be "
        "enforced. Section 2(s) of the RPwD Act defines a person with disability as a person with "
        "long term physical, mental, intellectual or sensory impairment <strong>which, in interaction "
        "with barriers, hinders his full and effective participation in society equally with "
        "others</strong>."),
      TW([P("cyan", "What the rights model adds",
            "A named duty bearer, a standard to measure against, and a remedy when it is breached. "
            "Section 3(1) of the RPwD Act obliges the appropriate Government to ensure that persons "
            "with disabilities enjoy the right to equality, life with dignity and respect for their "
            "integrity equally with others.")],
         [P("green", "What it means in a school",
            "A refused admission becomes a legal wrong with a forum to hear it. A "
            "parent can cite section 16 of the Act. A court can order posts to be filled, as the "
            "Supreme Court has been doing for special educators since 2021.")]),
      B("Source: Rights of Persons with Disabilities Act 2016 (No. 49 of 2016), ss 2(s) and 3(1).",
        sm=True)),

    C("Functioning", "The ICF describes disability as an interaction, and surveys now use it",
      B("The World Health Organization's International Classification of Functioning, Disability and "
        "Health (ICF) offers a bio-psychosocial view: disability arises from the interaction between "
        "a person's limitations in functioning and barriers in the environment, physical, social, "
        "cultural or legislative. The Washington Group on Disability Statistics built its survey "
        "questions on the ICF."),
      TW([P("cyan", "Why statisticians moved to functioning",
            "Asking 'Is anyone in this household disabled?' gets low and unreliable answers, because "
            "stigma and the word itself put people off. Asking whether a child has difficulty seeing, "
            "hearing, walking, remembering or making friends gets more consistent answers across "
            "countries.")],
         [P("amber", "What it means for schools",
            "A functional approach looks at what a child finds hard in the classroom. It can start "
            "before any diagnosis. That fits General Comment 4, paragraph 30, which says accommodation "
            "should rest on an evaluation of social barriers to education, and says it may not be "
            "made conditional on a medical diagnosis.")]),
      B("Source: Washington Group on Disability Statistics, WG Short Set page (read October 2026); "
        + GC4 + ".", sm=True)),

    C("Comparing models", "Four models side by side",
      T(["Model", "Where the problem sits", "Who decides", "Typical school response"],
        [["Charity", "In the child's misfortune", "The giver", "A separate home or school run by a "
          "trust, with gratitude expected"],
         ["Medical", "In the body or mind", "The doctor or specialist", "Wait for a certificate; refer "
          "to a special school; therapy before teaching"],
         ["Social", "In barriers of design, attitude and policy", "Disabled people and their "
          "organisations", "Remove barriers: ramps, large print, sign language, flexible tests"],
         ["Human rights", "In the failure of duty bearers", "The rights holder, backed by law and "
          "courts", "Admission without discrimination, reasonable accommodation, remedies when "
          "refused"]]),
      B("Most programmes in South Asia mix these. A Samagra Shiksha district plan may fund "
        "identification camps (a medical step), ramps (a social step) and a grievance process (a "
        "rights step) in the same year. That mix is normal. The risk is a plan that funds only the "
        "first."),
      H("amber", "A quick test for any proposal: does it spend money on finding and labelling "
        "children, or on changing the classroom they will sit in? A good proposal does both, and "
        "spends more on the second.")),

    C("Words in use", "Official language in India uses several terms, and each carries a history",
      B("Indian policy uses <strong>children with special needs (CWSN)</strong> in Samagra Shiksha "
        "and UDISE+, <strong>children with disabilities</strong> in the RPwD Act 2016, "
        "<strong>children with benchmark disabilities</strong> for those certified at 40% or more "
        "under section 2(r), and <strong>Divyang</strong>, which NEP 2020 paragraph 6.2.5 uses "
        "alongside CWSN. Disability rights groups have debated each term."),
      TW([P("cyan", "Why the label matters",
            "A term decides who is counted. 'Benchmark disability' needs a certificate showing at "
            "least 40% of a specified disability, so a child with a mild learning disability may fall "
            "outside entitlements such as free assistive devices under section 17(g), while still "
            "needing support in class.")],
         [P("green", "A practical rule",
            "In documents, follow the statute you are applying. In a classroom or a survey, ask "
            "families and disabled people's organisations which words they use, and use the child's "
            "name before any label. Avoid words that describe a child as suffering or confined.")]),
      B("Sources: RPwD Act 2016, ss 2(r) and 17(g); " + NEP + ", paragraph 6.2.5.", sm=True)),

    C("Many identities", "Disability rarely travels alone",
      B("A disabled child is also a girl or a boy, from a caste and a community, speaking a language, "
        "living in a village or a slum. Exclusion compounds. Census 2011 shows that among disabled "
        "children aged 5 to 19, 62% of boys and 60% of girls were attending an educational "
        "institution, and boys were 57% of those attending."),
      ST([CARD("62%", "Disabled boys aged 5-19 attending an educational institution", "cyan", CENSUS),
          CARD("60%", "Disabled girls aged 5-19 attending an educational institution", "amber", CENSUS),
          CARD("54%", "Children with multiple disabilities aged 5-19 who never attended", "red", CENSUS)]),
      H("cyan", "The gap between disabled boys and girls looks small. The bigger gaps lie between "
        "kinds of disability: children with multiple disabilities and children with mental illness "
        "(50% never attended, same source) are the furthest from school. A programme that serves "
        "the easiest-to-include children first will look successful and leave these children "
        "where they were.")),
]

# ===================== SECTION 03 =====================
SLIDES += [
    D("03", "Section Three", "Who is left out in South Asia"),

    C("Wealth", "Household wealth predicts who is in secondary school across the region",
      B("Net secondary attendance measures the share of children of secondary school age who attend "
        "secondary school. The Demographic and Health Surveys tabulate it by wealth quintile. The "
        "pattern is the same in all four countries, and the slope is steepest in Pakistan."),
      {"t": "chart", "canvas": "ieWealthChart", "type": "bar",
       "title": "Net secondary school attendance rate by wealth quintile (%)",
       "source": DHS,
       "data": {"labels": ["Poorest", "Second", "Middle", "Fourth", "Richest"],
                "datasets": [
                    {"label": "India 2019-21", "data": [58.2, 69.5, 74.0, 77.9, 83.6],
                     "backgroundColor": "#0EA5E9"},
                    {"label": "Bangladesh 2022", "data": [45.6, 52.4, 56.2, 59.1, 66.8],
                     "backgroundColor": "#10B981"},
                    {"label": "Nepal 2022", "data": [41.1, 43.5, 46.9, 57.7, 70.1],
                     "backgroundColor": "#F59E0B"},
                    {"label": "Pakistan 2017-18", "data": [14.6, 27.8, 39.7, 51.7, 65.9],
                     "backgroundColor": "#6366F1"}]},
       "options": {"__js__": "{ scales:{ y:{ min:0, max:100 } } }"}},
      H("amber", "In Pakistan the richest fifth attend secondary school at about four and a half "
        "times the rate of the poorest fifth (65.9% against 14.6%). In India the ratio is about 1.4. "
        "Poverty is an inclusion issue before any other identity is added. India's bars use NFHS-5 "
        "because the NFHS-6 (2023-24) fact sheets released in May 2026 do not tabulate attendance by "
        "wealth quintile.")),

    C("Disability, globally", "Children with disabilities are counted far less often than they are left out",
      B("On 10 November 2021 UNICEF released what it called its most comprehensive statistical "
        "analysis of children with disabilities. Surveys of this kind rest on functional questions "
        "such as the Child Functioning Module described in Section 11 of this deck."),
      ST([CARD("~240 m", "Children with disabilities worldwide, about 1 in 10 children", "cyan",
               "UNICEF press release, 10 November 2021"),
          CARD("49%", "More likely than other children to have never attended school", "red",
               "UNICEF press release, 10 November 2021"),
          CARD("42%", "Less likely to have foundational reading and numeracy skills", "amber",
               "UNICEF press release, 10 November 2021")]),
      TW([P("cyan", "What the numbers say",
            "Children with disabilities are disadvantaged on most measures of child well-being. Those "
            "with difficulty communicating and caring for themselves are the most likely to be out of "
            "school, and out-of-school rates rise with severity.")],
         [P("amber", "Why the 1 in 10 figure surprises",
            "It is far above the share of children that most South Asian school records identify as "
            "disabled. The gap comes from definitions: functional difficulty in a survey catches many "
            "children who will never hold a certificate.")])),

    C("Census 2011", "Census 2011 counted 2.68 crore disabled people, and 27% of disabled children never went to school",
      TW([{"t": "chart", "canvas": "ieCensusChart", "type": "doughnut",
           "title": "Disabled children aged 5-19, school attendance status (%)",
           "source": CENSUS,
           "data": {"labels": ["Attending", "Attended earlier", "Never attended"],
                    "datasets": [{"data": [61, 12, 27],
                                  "backgroundColor": ["#10B981", "#F59E0B", "#EF4444"]}]}}],
         [B("Census 2011 counted <strong>2.68 crore</strong> persons with disabilities, "
            "<strong>2.21%</strong> of the population. Among disabled children aged 5 to 19, 61% "
            "were attending an educational institution, 12% had attended earlier and 27% had never "
            "attended.", sm=True),
          B("Attendance was 65% in urban areas against 60% in rural areas. Among all disabled "
            "persons, 55% were literate: 62% of men and 45% of women.", sm=True),
          H("amber", "The 12% who attended earlier and left are a group to look for. They were "
            "enrolled once, so the barrier that pushed them out is often in the school itself.")]),
      B("Source: " + CENSUS + ". Census 2011 is the latest completed census. The next census has a "
        "reference date of 1 March 2027 and includes caste enumeration.", sm=True)),

    C("NSS 2018", "The NSS 76th round measured disability and schooling in more detail",
      B("The National Sample Survey's 76th round, July to December 2018, surveyed 1,06,894 persons "
        "with disabilities. It found a prevalence of <strong>2.2%</strong>: 2.3% in rural areas and "
        "2.0% in urban areas, 2.4% among males and 1.9% among females."),
      ST([CARD("62.9%", "Persons with disability aged 3-35 ever enrolled in an ordinary school", "cyan", NSS),
          CARD("4.1%", "Ever enrolled in a special school, among those not in an ordinary school", "amber", NSS),
          CARD("10.1%", "Aged 3-35 who attended a pre-school intervention programme", "green", NSS),
          CARD("52.2%", "Persons with disabilities aged 7 and above who were literate", "indigo", NSS)],
         cols=4),
      H("cyan", "Two lessons. First, special schools reach very few children: 4.1% of those outside "
        "ordinary school. Whatever one thinks of segregation, it is not where most disabled children "
        "are. Second, only one in ten had any early intervention, though the years before six are "
        "when support changes the most.")),

    C("Caste and tribe", "SC, ST and disabled students thin out as classes rise",
      TW([{"t": "chart", "canvas": "ieSedgChart", "type": "bar",
           "title": "Share of enrolment, primary against higher secondary, U-DISE 2016-17 (%)",
           "source": NEP + ", paragraph 6.2.1",
           "data": {"labels": ["Scheduled Castes", "Scheduled Tribes", "Children with disabilities"],
                    "datasets": [
                        {"label": "Primary", "data": [19.6, 10.6, 1.1], "backgroundColor": "#0EA5E9"},
                        {"label": "Higher secondary", "data": [17.3, 6.8, 0.25],
                         "backgroundColor": "#EF4444"}]}}],
         [B("NEP 2020 cites U-DISE 2016-17: Scheduled Castes are 19.6% of students at the primary "
            "level and 17.3% at higher secondary. For Scheduled Tribes the fall is from 10.6% to "
            "6.8%. For children with disabilities it is from 1.1% to 0.25%, a fall of more than "
            "three quarters.", sm=True),
          B("The Policy adds that declines are even greater for female students within each group. "
            "It names lack of access to quality schools, poverty, social mores and customs, and "
            "language as causes for Scheduled Castes, and says tribal children often find school "
            "irrelevant and foreign to their lives, culturally and academically (paragraphs 6.2.2 "
            "and 6.2.3).", sm=True)]),
      H("amber", "These are 2016-17 figures, quoted in a 2020 policy. They show the shape of the "
        "problem; check the latest UDISE+ tables before using them as a current level.")),

    C("Gender, religion, migration", "Several groups the law names are excluded in different ways",
      T(["Group", "What the evidence or the law says", "Source"],
        [["Girls", "Girls were 48.4% of school enrolment in 2025-26. NEP says women make up about half "
          "of every disadvantaged group and face amplified exclusion within it",
          UDISE26 + "; NEP 2020 para 6.7"],
         ["Transgender children", "NEP names transgender students alongside girls for the "
          "Gender-Inclusion Fund", "NEP 2020 paras 6.2 and 6.8"],
         ["Religious minorities", "NEP says minorities are relatively underrepresented in school and "
          "higher education", "NEP 2020 para 6.2.4"],
         ["Minority-run schools", "Excluded from the whole RTE Act by a 2014 Constitution Bench; that "
          "ruling was referred for reconsideration in 2025", "Pramati (2014); Anjuman Ishaat-e-Taleem "
          "Trust (2025)"],
         ["Migrant and urban poor children", "NEP lists migrant communities, child beggars and the "
          "urban poor among socio-economically disadvantaged groups", "NEP 2020 para 6.2"],
         ["Dalit students in Nepal", "Constitutional right to free education with scholarships from "
          "primary to higher level", "Constitution of Nepal 2015, Art 40(2)"]]),
      H("cyan", "Exclusion has many routes: fees, distance, language, safety, stigma, documents and "
        "the timing of seasonal migration. A good diagnosis names the route before choosing the "
        "remedy.")),

    C("Language", "Children taught in a language they do not understand are excluded inside the classroom",
      TW([ST([CARD("40%", "Of the global population lacks access to education in a language they "
                   "speak or understand", "red", "UNESCO GEM Report Policy Paper 24, February 2016")],
             cols=1),
          B("The same GEM paper says that in multi-ethnic societies, imposing a dominant language "
            "through school has often been a source of grievance tied to wider inequality, and gives "
            "Nepal, Pakistan and Bangladesh as examples.", sm=True)],
         [B("A child can be enrolled, present every day and still excluded, because she cannot follow "
            "the teacher. In much of tribal central India, the north-east and the Chittagong Hill "
            "Tracts, the school language is the child's second or third language.", sm=True),
          P("green", "What the GEM paper recommends",
            "At least six years of mother tongue instruction, so that early gains last; education "
            "plans that recognise home languages (fewer than half of 40 plans reviewed did); and "
            "teachers trained to teach in two languages. In Senegal a survey found only 8% of "
            "trainee teachers confident about teaching reading in local languages; in Mali, 2%.")]),
      H("amber", "Section 9 returns to this with NEP 2020 paragraph 4.11 on the medium of "
        "instruction and with classroom methods for multilingual education.")),
]

# ===================== SECTION 04 =====================
SLIDES += [
    D("04", "Section Four", "The Constitution and the RTE Act 2009"),

    C("Article 21A", "Education became a fundamental right in 2002, and a statute gave it content in 2009",
      B("The Constitution (Eighty-sixth Amendment) Act 2002 inserted <strong>Article 21A</strong>, "
        "making free and compulsory education for children aged six to fourteen a fundamental right "
        "in the manner the State determines by law. That law is the <strong>Right of Children to Free "
        "and Compulsory Education Act 2009</strong> (No. 35 of 2009), in force from 1 April 2010."),
      TW([P("cyan", "What the right covers",
            "Elementary education, defined in section 2(f) as Class 1 to Class 8, for every child aged "
            "six to fourteen. Pre-school is a matter of 'may' under section 11, and secondary "
            "education is outside the Act.")],
         [P("green", "Upheld in full by a Constitution Bench",
            "In <em>Pramati Educational and Cultural Trust v Union of India</em> (2014), five judges "
            "held that the 86th Amendment, and the 93rd Amendment inserting Article 15(5), do not "
            "alter the basic structure and are valid, and that the RTE Act does not violate Article "
            "19(1)(g).")]),
      B("Sources: RTE Act 2009, ss 2(f), 3 and 11, India Code consolidated text; Pramati Educational "
        "and Cultural Trust v Union of India, Supreme Court, 6 May 2014.", sm=True)),

    C("Section 3", "Section 3 gives every child a right to a neighbourhood school",
      B("Section 3(1), as substituted in 2012, provides that <em>every child of the age of six to "
        "fourteen years, including a child referred to in clause (d) or clause (e) of section 2, shall "
        "have the right to free and compulsory education in a neighbourhood school till the "
        "completion of his or her elementary education</em>. Section 3(2) bars any fee, charge or "
        "expense that may prevent the child from completing elementary education."),
      T(["Definition", "Text (RTE Act 2009, as amended by Act 30 of 2012)"],
        [["s2(d) Child belonging to disadvantaged group", "A child with disability, or a child of the "
          "Scheduled Caste, Scheduled Tribe, socially and educationally backward class, or such other "
          "group having disadvantage owing to social, cultural, economical, geographical, linguistic, "
          "gender or such other factor, as notified by the appropriate Government"],
         ["s2(e) Child belonging to weaker section", "A child whose parent or guardian has annual "
          "income below the limit notified by the appropriate Government"],
         ["s2(ee) Child with disability", "Defined by reference to the 1995 Persons with Disabilities "
          "Act and the National Trust Act 1999"]]),
      H("amber", "The words 'a child with disability' in section 2(d) and the whole of section 2(ee) "
        "were inserted by the 2012 amendment, with effect from 1 August 2012.")),

    C("Section 3(3)", "The RTE Act still points to a repealed disability law",
      TW([B("Section 3(3) gives a child with disability the same rights to free and compulsory "
            "elementary education that Chapter V of the <strong>Persons with Disabilities Act "
            "1995</strong> provided. Its proviso lets a child with multiple or severe disability, as "
            "defined in the National Trust Act 1999, opt for <strong>home-based "
            "education</strong>.", sm=True),
          B("Section 102(1) of the RPwD Act 2016 repealed the 1995 Act. Section 31(1) of the 2016 "
            "Act then provides, notwithstanding anything in the RTE Act, that every child with "
            "benchmark disability between six and eighteen has the right to free education in a "
            "neighbourhood school or a special school of choice.", sm=True)],
         [P("red", "What the drafting gap means",
            "A lawyer reading the RTE Act alone finds a cross-reference to a law that no longer "
            "exists. The working rule is to read the two Acts together: the RPwD Act's section 31 "
            "overrides and extends the RTE Act for children with benchmark disabilities, up to age "
            "eighteen. Section 102(2) saves action taken under the 1995 Act.")],
          ),
      H("cyan", "Home-based education is a legal option, and NEP 2020 paragraph 6.12 keeps it for "
        "children with severe and profound disabilities who cannot attend school. It also calls for "
        "an audit of its efficiency and effectiveness. Without that audit, home-based education can "
        "become a quiet form of exclusion.")),

    C("Section 12(1)(c)", "Section 12(1)(c) reserves a quarter of entry seats in private schools",
      B("Section 12(1)(c) requires unaided schools and schools of a specified category to "
        "<em>admit in class I, to the extent of at least twenty-five per cent of the strength of that "
        "class, children belonging to weaker section and disadvantaged group in the neighbourhood and "
        "provide free and compulsory elementary education till its completion</em>. Where the school "
        "has pre-school classes, the duty applies at that entry point."),
      FLOW("NOTIFY: state defines weaker section income limit and disadvantaged groups",
           "APPLY: families apply, usually online, for neighbourhood schools",
           "ALLOT: lottery or rule-based allotment, no screening",
           "STUDY: free education to Class 8 in the same school",
           "REIMBURSE: s12(2), the lower of state per-child cost or the fee charged"),
      H("amber", "Because section 2(d) includes children with disabilities, a disabled child can use "
        "the 25% quota. Admission is the start. Section 13 bars screening procedures and capitation "
        "fees, with fines up to twenty-five thousand rupees for a first contravention involving "
        "screening.")),

    C("Scale of 12(1)(c)", "Section 12(1)(c) reached tens of lakhs of children a year",
      TW([{"t": "chart", "canvas": "ie121cChart", "type": "bar",
           "title": "Children covered under s12(1)(c) of the RTE Act (lakh)",
           "source": SS21,
           "data": {"labels": ["2018-19", "2019-20", "2020-21"],
                    "datasets": [{"label": "Lakh children", "data": [16.76, 21.58, 32.67],
                                  "backgroundColor": "#0EA5E9"}]},
           "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0 } } }"}}],
         [B("The Ministry of Education reported 16.76 lakh children covered under section 12(1)(c) "
            "in 2018-19, 21.58 lakh in 2019-20 and 32.67 lakh in 2020-21, in its release on the "
            "continuation of Samagra Shiksha.", sm=True),
          P("amber", "What the count does not show",
            "It counts seats. It says nothing about experience. Families report hidden charges for uniforms, books and "
            "trips, and children admitted under the quota can be seated or treated differently. For "
            "a disabled child, a private school without an accessible toilet or a trained teacher "
            "turns a legal seat into integration in the Committee's sense, without inclusion.")]),
      B("Source: " + SS21 + ". The figures are as reported by the Ministry; state-level data vary "
        "widely and some states have reported very low use.", sm=True)),

    C("The courts", "Three Supreme Court rulings set the reach of the RTE Act",
      T(["Case", "Year", "Holding relevant to inclusion"],
        [["Society for Unaided Private Schools of Rajasthan v Union of India, (2012) 6 SCC 1",
          "2012", "Upheld the RTE Act and section 12(1)(c) against unaided non-minority schools, by a "
          "majority of two judges to one"],
         ["Pramati Educational and Cultural Trust v Union of India", "2014", "Constitution Bench: "
          "upheld Articles 21A and 15(5); held the RTE Act ultra vires insofar as it applies to "
          "minority schools, aided or unaided, under Article 30(1); overruled the 2012 view on aided "
          "minority schools"],
         ["Anjuman Ishaat-e-Taleem Trust v State of Maharashtra", "2025", "Doubted Pramati and asked "
          "the Chief Justice to consider a larger Bench; held that RTE Act provisions bind all "
          "non-minority schools and that in-service teachers must qualify the TET, subject to its "
          "transitional directions"]]),
      H("amber", "As of October 2026 the Pramati reference made on 1 September 2025 is pending. Until "
        "it is decided, minority-run schools, including many that serve poor and Muslim and "
        "Christian children, sit outside the 25% quota and the Act's other duties. Sources: "
        "judgments as published on indiankanoon.org.")),

    C("RTE and inclusion", "The RTE Act opens the door, and other laws shape the room",
      TW([P("cyan", "What the RTE Act does well",
            "It makes schooling a justiciable right, bans fees and screening, sets pupil-teacher "
            "ratios and infrastructure norms in its Schedule, creates School Management Committees "
            "with parents (section 21), and gives disadvantaged children a route into private "
            "schools. It treats children with disabilities as a disadvantaged group from 2012.")],
         [P("amber", "What it leaves to other laws",
            "It stops at Class 8 and age fourteen. It says little about how teaching changes for a "
            "child who learns differently. Reasonable accommodation, accessible buildings, Braille "
            "and sign language, special educators and the five-yearly survey of disabled children "
            "come from the RPwD Act 2016, which is the next section.")]),
      B("A practitioner working on a disabled child's admission should cite both Acts: the RTE Act "
        "for the neighbourhood school and the bar on screening, and the RPwD Act for what the school "
        "must do once the child is there and for the right to free education up to eighteen."),
      H("green", "Section 21 School Management Committees must include parents of disadvantaged "
        "and weaker-section children in proportion. A parent of a disabled child on the committee "
        "is often the most direct route to a ramp or a resource teacher.")),
]

# ===================== SECTION 05 =====================
SLIDES += [
    D("05", "Section Five", "The RPwD Act 2016"),

    C("The Act", "The RPwD Act 2016 gives effect to the CRPD in Indian law",
      B("The <strong>Rights of Persons with Disabilities Act 2016</strong> (No. 49 of 2016) received "
        "Presidential assent on 27 December 2016. Its long title says it is an Act to give effect to "
        "the CRPD. It replaced the Persons with Disabilities (Equal Opportunities, Protection of "
        "Rights and Full Participation) Act 1995."),
      ST([CARD("21", "Specified disabilities in the Schedule, as NCERT counts them", "cyan",
               "RPwD Act 2016, Schedule; NCERT PRASHAST 2.0 brochure"),
          CARD("40%", "Threshold for a benchmark disability, s2(r)", "amber", "RPwD Act 2016, s2(r)"),
          CARD("6-18", "Ages for free education for children with benchmark disabilities, s31",
               "green", "RPwD Act 2016, s31(1)"),
          CARD("5%", "Minimum reserved seats in government and aided higher education, s32",
               "indigo", "RPwD Act 2016, s32(1)")], cols=4),
      TW([P("cyan", "Chapter III: Education",
            "Sections 16, 17 and 18 apply to all children with disabilities, with or without a "
            "certificate. They set duties for every educational institution funded or recognised "
            "by government.")],
         [P("amber", "Chapter VI: Benchmark disabilities",
            "Sections 31 and 32 apply only to persons with a benchmark disability, certified at not "
            "less than 40%. Free education to eighteen and higher education reservation sit here.")])),

    C("Two definitions", "Inclusive education and reasonable accommodation are defined in the Act",
      TW([TERM("Inclusive education, s2(m)",
               "A system of education wherein students with and without disability learn together "
               "and the system of teaching and learning is suitably adapted to meet the learning "
               "needs of different types of students with disabilities.")],
         [TERM("Reasonable accommodation, s2(y)",
               "Necessary and appropriate modification and adjustments, without imposing a "
               "disproportionate or undue burden in a particular case, to ensure to persons with "
               "disabilities the enjoyment or exercise of rights equally with others.")]),
      B("NEP 2020 paragraph 6.10 quotes the section 2(m) definition word for word and says the Policy "
        "is in complete consonance with the RPwD Act. The two definitions work together. Section 2(m) "
        "describes the system; section 2(y) describes what one child is owed inside it."),
      H("amber", "Note the qualifier in section 2(y): 'without imposing a disproportionate or undue "
        "burden'. General Comment 4 accepts that resources count in judging that burden "
        "(paragraph 28), weighs them across the resources of the whole education system "
        "(paragraph 30), and bars using the burden to evade the duty (paragraph 18). A school that "
        "says it cannot afford a scribe for a Class 10 board exam will find that hard to show.")),

    C("Section 16", "Section 16 lists eight duties of every funded or recognised institution",
      B("Section 16: <em>the appropriate Government and the local authorities shall endeavour that "
        "all educational institutions funded or recognised by them provide inclusive education to "
        "the children with disabilities</em> and to that end shall:"),
      T(["Clause", "Duty", "A check a monitor can make"],
        [["(i)", "Admit without discrimination; equal sports and recreation", "Any refusal in the last year?"],
         ["(ii)", "Make building, campus and facilities accessible", "Ramp, rail, accessible toilet"],
         ["(iii)", "Reasonable accommodation to individual requirements", "Written record of what was provided"],
         ["(iv)", "Individualised support in environments that maximise development", "A plan for each child"],
         ["(v)", "Education for blind, deaf or deafblind persons in the most appropriate languages and modes", "Braille, ISL"],
         ["(vi)", "Detect specific learning disabilities early and take pedagogical measures", "Screening in early grades"],
         ["(vii)", "Monitor participation, progress and completion of every student with disability", "Records by child"],
         ["(viii)", "Transport for children with disabilities, and attendants for those with high support needs", "Escort allowance used"]]),
      H("amber", "'Shall endeavour' is softer than 'shall'. Clause (vii) is the hook for data: it makes "
        "tracking each disabled child's progress a statutory duty.")),

    C("Section 17", "Section 17 tells government how to build the system",
      TW([BL(["(a) A survey of school-going children <strong>every five years</strong> to identify "
              "children with disabilities and their needs; the first within two years of "
              "commencement",
              "(b) An adequate number of teacher training institutions",
              "(c) Train and employ teachers, including teachers with disability, qualified in sign "
              "language and Braille, and teachers trained for intellectual disability",
              "(d) Train professionals and staff to support inclusive education",
              "(e) An adequate number of resource centres at all levels of school education"],
             color="cyan")],
         [BL(["(f) Augmentative and alternative communication, Braille and sign language",
              "(g) Books, learning materials and assistive devices <strong>free up to age "
              "eighteen</strong> for students with benchmark disabilities",
              "(h) Scholarships for students with benchmark disability",
              "(i) Changes to curriculum and examinations: extra time, a scribe or amanuensis, "
              "exemption from second and third language courses",
              "(j) Research to improve learning; (k) other measures"], color="green")]),
      H("amber", "Ask a district or state for its section 17(a) survey. A five-yearly count of "
        "children with disabilities, with their needs, is the baseline every inclusion plan needs. "
        "Source: RPwD Act 2016, s17.")),

    C("Section 31 and choice", "Section 31 offers a choice that the CRPD Committee would phase out",
      B("Section 31(1): <em>notwithstanding anything contained in the Right of Children to Free and "
        "Compulsory Education Act 2009, every child with benchmark disability between the age of six "
        "to eighteen years shall have the right to free education in a neighbourhood school, or in a "
        "special school, of his choice</em>. Section 31(2) adds a duty to ensure access to free "
        "education in an appropriate environment until eighteen."),
      TW([P("green", "The case for choice",
            "Many parents of deaf or deafblind children choose special schools because that is "
            "where sign language users and trained teachers are. Article 24(3)(c) of the CRPD itself "
            "speaks of environments that suit communication needs. Taking away the only school that "
            "signs, before ordinary schools can, would harm deaf children.")],
         [P("red", "The case against a permanent dual system",
            "General Comment 4, paragraph 40, says sustaining two systems is not compatible with "
            "progressive realisation of Article 24. If special schools stay the default for some "
            "disabilities, ordinary schools never build the capacity, and the 'choice' is no choice "
            "for families who live far from a special school.")]),
      H("cyan", "A defensible position for a practitioner: keep choice open now, and measure each "
        "year whether ordinary schools are becoming able to serve the children who currently need "
        "to go elsewhere.")),

    C("The Schedule", "The Schedule groups the specified disabilities into five families and an open clause",
      T(["Group in the Schedule", "Conditions listed", "Classroom questions it raises"],
        [["1. Physical disability", "Locomotor disability (leprosy cured, cerebral palsy, dwarfism, "
          "muscular dystrophy, acid attack victims); blindness and low vision; deaf and hard of "
          "hearing; speech and language disability", "Access, seating, print size, sign language, "
          "alternative communication"],
         ["2. Intellectual disability", "Including specific learning disabilities (dyslexia, "
          "dysgraphia, dyscalculia, dyspraxia, developmental aphasia) and autism spectrum disorder",
          "Pace, structure, explicit teaching, assessment format"],
         ["3. Mental behaviour", "Mental illness", "Attendance flexibility, counselling, a calm space"],
         ["4. Chronic neurological conditions and blood disorders", "Multiple sclerosis, Parkinson's "
          "disease, haemophilia, thalassemia, sickle cell disease", "Absences for treatment, safety in "
          "play, catch-up support"],
         ["5. Multiple disabilities", "Including deaf blindness", "Intensive, individual support"],
         ["6. Any other category", "As notified by the Central Government", "Watch for notifications"]]),
      B("Source: RPwD Act 2016, the Schedule (see clause (zc) of section 2). The list brings "
        "specific learning disabilities, autism, mental illness and blood disorders into the "
        "classroom's legal frame, so a school has duties towards children it may not think of as "
        "disabled.", sm=True)),

    C("Enforcement", "The Supreme Court has been supervising special educator posts since 2016",
      B("<em>Rajneesh Kumar Pandey v Union of India</em>, Writ Petition (Civil) No. 132 of 2016, is a "
        "continuing case on the appointment of special educators for children with special needs. "
        "The Supreme Court's daily orders of 18 November 2025 and 12 February 2026 go state by state "
        "through affidavits on posts, qualifications and pay."),
      TW([P("cyan", "What the orders record",
            "On 12 February 2026 the Court noted Telangana's affidavit: 602 Bhavitha centres under "
            "Samagra Shiksha, each with two resource persons on purely contractual terms because no "
            "sanctioned posts existed, paid on a 60:40 Centre-State share. It asked the Union for the "
            "essential qualifications for special educators at each stage.")],
         [P("amber", "The 2021 judgment and the 2026 orders",
            "The judgment of 28 October 2021, (2021) 17 SCC 1, told the Centre to notify "
            "pupil-teacher norms for special teachers, create permanent posts and fill them on a "
            "regular basis, and held that special teachers must be qualified and registered with the "
            "Rehabilitation Council of India. The order of 5 May 2026 records about 4,900 vacant "
            "special educator posts in Uttar Pradesh. Whether they must also pass the TET is "
            "unresolved: on 28 April 2026 the RCI said the TET is not one of its qualifications and "
            "the Court let states that prescribe it continue recruiting; on 28 July 2026 it said, "
            "prima facie, that Bihar's TET demand for contractual special teachers went beyond "
            "Bihar's own 2023 Rules.")]),
      H("red", "The lesson for programme staff: an inclusion plan that runs on contractual resource "
        "persons is fragile, and the courts now treat regular, qualified posts as part of the right. "
        "Sources: Supreme Court judgment of 28 October 2021 and records of proceedings of "
        "18 November 2025, 12 February, 28 April, 5 May and 28 July 2026 in WP(C) 132/2016, via "
        "indiankanoon.org.")),
]

# ===================== SECTION 06 =====================
SLIDES += [
    D("06", "Section Six", "NEP 2020 and Samagra Shiksha"),

    C("NEP chapter 6", "NEP 2020 chapter 6 is titled 'Equitable and inclusive education: learning for all'",
      B("Paragraph 6.1 calls education <em>the single greatest tool for achieving social justice and "
        "equality</em>. Paragraph 6.2 groups the children the system has left behind as "
        "<strong>Socio-Economically Disadvantaged Groups (SEDGs)</strong>."),
      T(["SEDG category in paragraph 6.2", "Examples the Policy gives"],
        [["Gender identities", "Particularly female and transgender individuals"],
         ["Socio-cultural identities", "Scheduled Castes, Scheduled Tribes, OBCs and minorities"],
         ["Geographical identities", "Students from villages, small towns and aspirational districts"],
         ["Disabilities", "Including learning disabilities"],
         ["Socio-economic conditions", "Migrant communities, low income households, children in "
          "vulnerable situations, victims or children of victims of trafficking, orphans including "
          "child beggars in urban areas, and the urban poor"]]),
      H("cyan", "The SEDG frame is wide, in the spirit of Salamanca's paragraph 3. Its risk is that "
        "everything becomes a priority. Chapter 6 then gives specific measures for some groups and "
        "general ones for others, so read which group each paragraph actually funds. Source: "
        + NEP + ", paragraphs 6.1 and 6.2.")),

    C("Targeted measures", "NEP proposes funds, zones and boarding schools for disadvantaged groups",
      TW([P("cyan", "Gender-Inclusion Fund (6.8)",
            "A fund available to States for priorities the Centre sets to help female and "
            "transgender children reach and stay in school: sanitation and toilets, bicycles, "
            "conditional cash transfers, and community interventions for local barriers. Similar "
            "Inclusion Funds are proposed for other SEDGs.")],
         [P("green", "Special Education Zones (6.6)",
            "Regions with large populations from educationally disadvantaged SEDGs are to be declared "
            "Special Education Zones, where all schemes and policies are implemented to the maximum "
            "with additional effort. Aspirational Districts are named as a related category.")]),
      TW([P("amber", "Boarding and girls' schools (6.9)",
            "Free boarding to the standard of Jawahar Navodaya Vidyalayas where students come from "
            "far; Kasturba Gandhi Balika Vidyalayas to be strengthened and expanded up to Grade 12.")],
         [P("indigo", "What works, by group (6.5)",
            "Bicycles and walking groups for girls; one-on-one tutors, peer tutoring, open schooling "
            "and technology for some children with disabilities; counsellors and social workers for "
            "the urban poor.")]),
      B("Source: " + NEP + ", paragraphs 6.5 to 6.9.", sm=True)),

    C("Children with disabilities", "NEP paragraphs 6.10 to 6.12 set the policy for children with disabilities",
      B("Paragraph 6.10 gives the inclusion and equal participation of children with disabilities "
        "<strong>the highest priority</strong>, from the Foundational Stage to higher education. "
        "Paragraph 6.11 says schools and school complexes will get resources for:"),
      TW([BL(["Special educators with <strong>cross-disability training</strong>",
              "Resource centres where needed, especially for severe or multiple disabilities",
              "Barrier-free access as per the RPwD Act",
              "Assistive devices, technology-based tools and accessible, language-appropriate "
              "materials such as large print and Braille",
              "NIOS modules to teach Indian Sign Language, and other subjects in it"], color="cyan")],
         [P("amber", "Paragraph 6.12: choice and home-based education",
            "Children with benchmark disabilities keep the choice of regular or special schooling. "
            "Home-based education remains available for children with severe and profound "
            "disabilities who cannot attend school, who must be treated as equal to any other child. "
            "The Policy calls for an audit of home-based education and guidelines based on it.")]),
      H("cyan", "Paragraph 4.22 adds that Indian Sign Language will be standardised across the "
        "country, with national and state curriculum materials for deaf students. Source: " + NEP
        + ", paragraphs 4.22 and 6.10 to 6.12.")),

    C("Learning disabilities and culture", "NEP names early identification and a change of school culture",
      TW([P("cyan", "Specific learning disabilities (6.13)",
            "Most classrooms have children with specific learning disabilities who need continuous "
            "support, and the earlier it begins the better. Teachers are to be helped to identify "
            "them early. PARAKH, the proposed National Assessment Centre, is to set guidelines and "
            "tools for assessment and certification from the foundational stage to entrance exams.")],
         [P("green", "Teacher education (6.14)",
            "How to teach children with specific disabilities, including learning disabilities, is to "
            "be an integral part of all teacher education programmes, with gender sensitisation and "
            "sensitisation towards all underrepresented groups.")]),
      Q("All the above policies and measures are absolutely critical to attaining full inclusion and "
        "equity for all SEDGs, but they are not sufficient. What is also required is a change in "
        "school culture.",
        "National Education Policy 2020, paragraph 6.19"),
      H("amber", "Paragraph 6.19 also commits to recruiting more high-quality teachers and leaders "
        "from SEDGs, and paragraph 6.20 to removing biases and stereotypes from the curriculum.")),

    C("Samagra Shiksha", "Samagra Shiksha is the main central scheme that pays for inclusion in schools",
      B("Samagra Shiksha was launched in 2018 by merging Sarva Shiksha Abhiyan, Rashtriya Madhyamik "
        "Shiksha Abhiyan and Teacher Education into one scheme from pre-school to Class 12. On "
        "4 August 2021 the Cabinet Committee on Economic Affairs approved its continuation from "
        "2021-22 to 2025-26."),
      ST([CARD("Rs 2,94,283 cr", "Total outlay, 2021-22 to 2025-26", "cyan", SS21),
          CARD("Rs 1,85,398 cr", "Central share of that outlay", "indigo", SS21),
          CARD("15", "Interventions, one of which is Inclusive Education", "green", SS21),
          CARD("1.16 m", "Schools covered, government and aided", "amber", SS21)], cols=4),
      TW([P("cyan", "Where inclusion sits",
            "The fifteen interventions include Gender and Equity and Inclusive Education as separate "
            "lines, alongside access, foundational literacy and numeracy, teacher salaries and RTE "
            "entitlements such as uniforms and textbooks.")],
         [P("amber", "Status as of October 2026",
            "The approved period ended on 31 March 2026. States are approving their shares for the "
            "next phase: Madhya Pradesh's cabinet approved Rs 36,006.22 crore for Samagra Shiksha "
            "from 2026-27 to 2030-31 in September 2026 (Indian Masterminds, 16 September 2026).")])),

    C("Inclusive Education component", "What the Inclusive Education component of Samagra Shiksha pays for",
      T(["Provision (2021 revision)", "Detail", "Reported reach"],
        [["Student-oriented support for CWSN", "From pre-primary to senior secondary level",
          "Not stated in the release"],
         ["Stipend for girls with special needs", "Rs 200 per month for 10 months, in addition to the "
          "student component", "3.79 lakh (2018-19), 3.22 lakh (2019-20), 3.52 lakh (2020-21)"],
         ["Identification camps", "Annual camps at block level at Rs 10,000 per camp", "Not stated"],
         ["Block Resource Centres", "Equipped for rehabilitation and special training of CWSN",
          "Not stated"],
         ["Special educators", "Financial assistance for special educators", "23,183 (2018-19), "
          "24,030 (2019-20), 22,990 (2020-21)"],
         ["Out-of-school youth aged 16-19", "Up to Rs 2,000 per child per grade for SC, ST and "
          "disabled children to complete secondary via NIOS or state open schools", "Not stated"]]),
      H("amber", "The number of special educators supported, around 23,000 a year, is the figure to "
        "hold against the Supreme Court's supervision in <em>Rajneesh Kumar Pandey</em>. Source: "
        + SS21 + ".")),
]

# ===================== SECTION 07 =====================
SLIDES += [
    D("07", "Section Seven", "What the data shows"),

    C("UDISE+", "UDISE+ is the school census, and its 2025-26 report is the latest",
      B("The Unified District Information System for Education Plus (UDISE+) collects school-level "
        "data on schools, teachers and students; individual student records began in 2022-23, as "
        "the 2025-26 report notes. The Ministry of Education released the UDISE+ 2025-26 report on 7 July 2026."),
      ST([CARD("58.2%", "Schools with ramps and handrails, 2025-26", "amber", UDISE26),
          CARD("48.4%", "Girls' share of enrolment, 2025-26 (48.3% in 2024-25)", "cyan", UDISE26),
          CARD("7.0%", "Secondary dropout rate, 2025-26 (8.2% in 2024-25)", "green", UDISE26),
          CARD("51.9%", "Retention rate at secondary level, 2025-26 (47.2% in 2024-25)", "indigo", UDISE26)],
         cols=4),
      TW([P("cyan", "Read the ramp figure carefully",
            "A ramp is the most basic accessibility item, and 41.8% of schools still lacked one with "
            "handrails in 2025-26. A ramp alone does not make a school accessible: toilets, "
            "classrooms on upper floors and playgrounds matter as much.")],
         [P("amber", "Read the retention figure carefully",
            "Retention at secondary level rose to 51.9%, which still means that about half of a "
            "cohort does not stay through the secondary stage in the way the indicator measures. "
            "Disaggregate before celebrating.")])),

    C("CWSN in UDISE+", "Schools report far fewer children with disabilities than surveys find",
      TW([ST([CARD("22.1 lakh", "CWSN enrolled, Foundational to Secondary stage (pre-primary to "
                   "Class 12), 2025-26", "cyan", "UDISE+ 2025-26 report, Ministry of Education, Table 5.11"),
              CARD("0.89%", "CWSN share of total enrolment of 24.72 crore, 2025-26", "amber",
                   "UDISE+ 2025-26 report, Ministry of Education")], cols=1)],
         [B("The same table shows about 7.1 lakh CWSN at the Middle stage (Classes 6 to 8) and "
            "5.2 lakh at the Secondary stage (Classes 9 to 12), and boys at 57% of CWSN enrolment. In "
            "2024-25 the count was 21.5 lakh.", sm=True),
          P("red", "The gap with prevalence",
            "Census 2011 put disability at 2.21% of the population and the NSS 76th round at 2.2%. "
            "UNICEF's functional estimate is about one child in ten worldwide. A school share below 1% "
            "means that many disabled children are either out of school or enrolled without being "
            "identified. Both are inclusion failures, and they need different responses.")]),
      H("cyan", "Source: UDISE+ 2025-26 report, Ministry of Education, Table 5.11 and the "
        "national summary; UDISE+ 2024-25 report for the earlier year. The 2025-26 report also finds "
        "CWSN-friendly toilets in 40.1% of schools.")),

    C("Three sources", "Census, NSS and UDISE+ measure different things",
      T(["Source", "Latest round", "How disability is identified", "Best used for"],
        [["Census", "2011 (next reference date 1 March 2027)", "Household reports against listed "
          "disability types", "District counts, literacy and attendance of disabled persons"],
         ["NSS", "76th round, July to December 2018", "Survey questions on specified disabilities, "
          "with detailed follow-up", "Prevalence, causes, schooling history, special school use"],
         ["UDISE+", "2025-26", "School records of children identified as CWSN by type",
          "Enrolment by level, school facilities, year-on-year change"],
         ["DHS / NFHS", "NFHS-6, 2023-24 (fact sheets May 2026); wealth tables here use NFHS-5, "
          "2019-21", "Not used for disability in this deck", "Attendance by wealth, residence and sex"],
         ["ASER", "2024", "Household test of reading and arithmetic", "Whether enrolled children "
          "are learning"]]),
      B("No single source answers the question 'how many disabled children are out of school in my "
        "district?' A good situation analysis triangulates: the Census or NSS for the expected "
        "number, UDISE+ for those enrolled, and a local door-to-door survey under RPwD Act section "
        "17(a) for the rest."),
      H("amber", "When two sources disagree, ask first whether they use the same definition and the "
        "same age band before deciding which one is wrong.")),

    C("Enrolled and learning", "High enrolment and low learning can sit side by side",
      ST([CARD("98.1%", "Children aged 6-14 enrolled in school, 2024", "cyan",
               "ASER 2024 national findings, Pratham"),
          CARD("23.4%", "Std III children in government schools who can read a Std II text, 2024", "red",
               "ASER 2024 national findings, Pratham"),
          CARD("16.3%", "The same figure in 2022, after school closures", "amber",
               "ASER 2024 national findings, Pratham")]),
      TW([P("cyan", "Why this belongs in an inclusion deck",
            "General Comment 4 defines inclusion by participation and achievement as well as "
            "attendance. If three quarters of Class 3 children in government schools cannot read a "
            "Class 2 text, the ordinary classroom is already failing many children who have no "
            "disability label at all.")],
         [P("green", "The opportunity",
            "Teaching at the right level, structured reading and clear feedback help children who "
            "are behind for any reason, including undiagnosed learning disabilities. Inclusion and "
            "foundational learning are one agenda in practice.")]),
      B("Source: ASER 2024 national findings. ASER figures are from a household survey of rural "
        "children; the 2018 value for the Std III indicator was 20.9%.", sm=True)),

    C("Year on year", "UDISE+ shows small gains between 2024-25 and 2025-26",
      TW([{"t": "chart", "canvas": "ieUdiseChart", "type": "bar",
           "title": "Selected UDISE+ indicators, 2024-25 and 2025-26 (%)",
           "source": UDISE26,
           "data": {"labels": ["Secondary retention", "Middle retention", "Secondary GER",
                               "Schools with computers"],
                    "datasets": [
                        {"label": "2024-25", "data": [47.2, 82.8, 68.5, 64.7],
                         "backgroundColor": "#94A3B8"},
                        {"label": "2025-26", "data": [51.9, 83.7, 71.7, 69.9],
                         "backgroundColor": "#0EA5E9"}]},
           "options": {"__js__": "{ scales:{ y:{ min:0, max:100 } } }"}}],
         [B("Between 2024-25 and 2025-26 the secondary gross enrolment ratio rose from 68.5% to "
            "71.7%, retention at secondary level from 47.2% to 51.9%, and the share of schools with "
            "computers from 64.7% to 69.9%. The preparatory dropout rate fell from 2.3% to 1.8%.",
            sm=True),
          P("amber", "What the release does not break down",
            "The press release gives national averages. It does not report these indicators for "
            "children with special needs, Scheduled Tribes or girls separately. For an inclusion "
            "analysis, ask for the state and district tables by social group and CWSN status.")]),
      H("cyan", "A national average can rise while the groups this deck is about stand still. "
        "Disaggregation is the first question to ask of any good news. Source: " + UDISE26 + ".")),

    C("The early years", "Inclusion has to start before Class 1",
      TW([ST([CARD("10.1%", "Persons with disability aged 3-35 who ever attended a pre-school "
                   "intervention programme", "red", NSS),
              CARD("77.4%", "Three-year-olds enrolled in some pre-primary institution, 2024",
                   "cyan", "ASER 2024 national findings, Pratham")], cols=1)],
         [B("Most children aged three now attend an anganwadi or a pre-primary class: 77.4% in 2024, "
            "up from 68.1% in 2018 (ASER 2024). Among persons with disabilities aged 3 to 35, only "
            "one in ten ever had pre-school intervention (NSS 2018).", sm=True),
          P("green", "What the law and policy say",
            "RTE Act section 11 lets governments provide free pre-school education. NEP 2020 "
            "paragraph 6.10 asks for children with disabilities to take part fully from the "
            "Foundational Stage. RPwD Act section 16(vi) requires early detection of specific "
            "learning disabilities.")]),
      H("amber", "The anganwadi is the first place many developmental delays could be noticed. A "
        "district plan that links anganwadi workers, the PRASHAST screening in schools and Block "
        "Resource Centres catches children years earlier than a Class 3 referral.")),

    C("Missing data", "What the official data still cannot tell you",
      TW([BL(["How many disabled children aged 6-18 are out of school, by district and disability",
              "Whether enrolled CWSN attend, and how many days",
              "Learning levels of CWSN against their classmates",
              "How many schools have an accessible toilet that is usable, open and clean",
              "How many teachers can use Indian Sign Language or Braille"], color="red")],
         [P("cyan", "Why these gaps persist",
            "Disability is identified late and unevenly; certificates lag; school staff record what "
            "they can see; and most learning assessments are not designed with accommodations, so "
            "disabled children are left out of the sample or the test.")]),
      H("amber", "A programme can fill some gaps itself: a baseline using the Washington Group "
        "teacher module (Section 11), attendance tracked by child, and a facility audit that checks "
        "use as well as presence."),
      B("When collecting such data, treat disability information about children as sensitive. The "
        "Digital Personal Data Protection Act 2023, whose duties apply with the 2025 Rules from "
        "13 May 2027, exempts research "
        "and statistical processing that meets the conditions in section 17(2)(b); programme "
        "monitoring that identifies children needs its own lawful basis and consent process.", sm=True)),
]

# ===================== SECTION 08 =====================
SLIDES += [
    D("08", "Section Eight", "Neighbours' laws"),

    C("Ratification", "Every South Asian state is now party to the CRPD",
      T(["Country", "Signed", "Ratified or acceded", "Main domestic disability law"],
        [["India", "30 Mar 2007", "1 Oct 2007", "Rights of Persons with Disabilities Act 2016"],
         ["Bangladesh", "9 May 2007", "30 Nov 2007", "Rights and Protection of Persons with "
          "Disabilities Act 2013"],
         ["Maldives", "2 Oct 2007", "5 Apr 2010", "Not covered in this deck"],
         ["Nepal", "3 Jan 2008", "7 May 2010", "Act Relating to Rights of Persons with Disabilities "
          "2074 (2017)"],
         ["Pakistan", "25 Sep 2008", "5 Jul 2011", "ICT Rights of Persons with Disability Act 2020, "
          "and provincial laws"],
         ["Afghanistan", "", "18 Sep 2012 (accession)", "Not covered in this deck"],
         ["Sri Lanka", "30 Mar 2007", "8 Feb 2016", "Protection of the Rights of Persons with "
          "Disabilities Act No. 28 of 1996"],
         ["Bhutan", "21 Sep 2010", "13 Mar 2024", "Not covered in this deck"]]),
      B("Source: " + UNTC + ". Ratification makes Article 24 binding in international law; how far "
        "it binds domestic courts depends on each country's constitution.", sm=True),
      H("cyan", "Bhutan's ratification in March 2024 completed the region. Sri Lanka took nine years "
        "from signature to ratification.")),

    C("Bangladesh", "Bangladesh's 2013 Act names both inclusive and integrated education",
      B("The <strong>Rights and Protection of Persons with Disabilities Act 2013</strong> (Act No. 39 "
        "of 2013, dated 9 October 2013) replaced Bangladesh's earlier disability law. Its "
        "definitions separate three kinds of schooling, translated here from the Bangla text."),
      T(["Section", "Term", "Meaning (translated)"],
        [["2(2)", "Inclusive education (ekibhuto shiksha)", "Students with and without disabilities "
          "studying together in educational institutions"],
         ["2(25)", "Integrated education (shomonnito shiksha)", "Education in mainstream schools under "
          "special arrangements suited to the type of disability"],
         ["2(19)", "Special education (bishesh shiksha)", "Education by residential or non-residential "
          "institutions run under special management by type of disability, similar to the "
          "mainstream curriculum"]]),
      TW([P("cyan", "Section 16(1)(h)",
            "A right to take part in inclusive or integrated education at all levels, subject to "
            "suitable facilities being available in the institution.")],
         [P("green", "Section 33",
            "No head of an institution may refuse admission solely because of disability where the "
            "person is otherwise qualified; a complaint lies to the relevant committee, which may "
            "direct admission.")]),
      B("Source: Bangladesh Code, bdlaws.minlaw.gov.bd, Act No. 39 of 2013 (Bangla text).", sm=True)),

    C("Nepal", "Nepal puts disability and mother tongue education in its Constitution",
      TW([P("cyan", "Constitution of Nepal 2015, Article 31",
            "Every citizen has the right to compulsory and free basic education and free education up "
            "to secondary level (31(2)). Physically impaired and financially poor citizens have the "
            "right to free higher education as provided by law (31(3)). Visually impaired persons "
            "have the right to free education through Braille (31(4)). Every community has the right "
            "to education in its mother tongue up to secondary level (31(5)).")],
         [P("green", "Act Relating to Rights of Persons with Disabilities 2074 (2017), section 21",
            "No admission fee may be charged to a person with disability (21(3)). Government shall "
            "provide education through more than one means, such as Braille or alternative scripts, "
            "sign language, information technology and peer learning (21(6)). Private institutions "
            "must provide free study to a number of students with disabilities set by government "
            "(21(13)).")]),
      B("The Act was published in the Nepal Gazette on 15 October 2017 (Act No. 25 of 2074) and "
        "amended in 2018. Article 40(2) of the Constitution separately guarantees free education "
        "with scholarships for Dalit students from primary to higher level."),
      B("Sources: Constitution of Nepal 2015, English text via constituteproject.org; Nepal Law "
        "Commission English text of the 2017 Act, via the ADB Law and Policy Reform portal.", sm=True)),

    C("Pakistan", "Pakistan's federal capital law promises inclusive education and keeps special schools",
      B("Article 25A of the Constitution of Pakistan obliges the State to provide free and compulsory "
        "education to all children aged five to sixteen, in a manner determined by law. The "
        "<strong>ICT Rights of Persons with Disability Act 2020</strong> (Act No. XXXV of 2020, "
        "assented to on 22 September 2020) applies in the Islamabad Capital Territory."),
      TW([BL(["s9(1) Equal rights of access to government and private institutions, without "
              "discrimination",
              "s9(2) Free education from pre-primary to higher education",
              "s9(4) No denial of admission on ground of disability",
              "s9(5) Discrimination or abuse at a place of education is illegal and punishable"],
             color="cyan")],
         [BL(["s9(3) Special institutions for moderate to severe disabilities, <em>in addition "
              "to</em> equipping general institutions for inclusive education",
              "s9(6) Inclusive education focused on personality, creativity and capabilities",
              "s9(7) Reasonable and appropriate accommodation, including hostels",
              "s9(8) Teacher training facilities for teaching students with various disabilities"],
             color="green")]),
      H("amber", "Section 1(2) limits the Act to the Islamabad Capital Territory, so it works as a "
        "model for the provinces. Check the provincial law where you work. Sources: Constitution of "
        "Pakistan, Art 25A; Gazette of Pakistan, 24 September 2020.")),

    C("Sri Lanka", "Sri Lanka's 1996 Act bars discrimination in admission, and little more on schooling",
      B("Sri Lanka's <strong>Protection of the Rights of Persons with Disabilities Act No. 28 of "
        "1996</strong> set up a National Council for Persons with Disabilities. Its education "
        "provision is short. Section 23(1): <em>no person with a disability shall be discriminated "
        "against on the ground of such disability in recruitment for any employment or office or "
        "admission to any educational institution</em>."),
      TW([P("cyan", "What the Act provides",
            "A non-discrimination rule for admission, a rule against restrictions on access to "
            "public places in section 23(2), and a route for complaints. It predates the CRPD by a "
            "decade and does not define inclusive education or reasonable accommodation.")],
         [P("amber", "What has changed since",
            "Sri Lanka ratified the CRPD on 8 February 2016, which brings Article 24 and General "
            "Comment 4 into its reporting obligations to the CRPD Committee. Check for any newer "
            "law or amendment before citing the 1996 Act as the whole picture.")]),
      B("Sources: Act No. 28 of 1996, text hosted by UN DESA; " + UNTC + ".", sm=True),
      H("cyan", "For practitioners, Sri Lanka is a reminder that ratification and domestic law move "
        "at different speeds. Advocacy can cite both.")),

    C("Side by side", "Four laws compared on five questions",
      T(["Question", "India (RPwD 2016)", "Bangladesh (2013)", "Nepal (2017)", "Pakistan ICT (2020)"],
        [["Defines inclusive education?", "Yes, s2(m)", "Yes, s2(2)", "No separate definition in s21",
          "No; s9(6) describes its aims"],
         ["Bars refusal of admission?", "Yes, s16(i)", "Yes, s33", "Fees barred, s21(3); "
          "discrimination barred, s21(5)", "Yes, s9(4)"],
         ["Reasonable accommodation?", "Yes, s2(y), s16(iii)", "Yes, s16 rights list", "Yes, for "
          "vocational and continuing learning, s21(9)", "Yes, s9(7)"],
         ["Keeps special schools?", "Yes, choice in s31", "Yes, special and integrated education "
          "defined", "Separate provision allowed, s21(10)", "Yes, s9(3)"],
         ["Free education age range", "6-18 for benchmark disability, s31", "Not covered here",
          "Free higher education in government institutions, s21(1)", "Pre-primary to higher, s9(2)"]]),
      H("amber", "No country in the region has followed General Comment 4 paragraph 40 to a single "
        "system. All four keep special or integrated tracks beside inclusive ones. The differences "
        "lie in how far each law pushes ordinary schools to change.")),
]

# ===================== SECTION 09 =====================
SLIDES += [
    D("09", "Section Nine", "Classroom practice"),

    C("Universal Design for Learning", "Universal Design for Learning plans for variety from the start",
      B("Universal Design for Learning (UDL) is a framework from CAST, a US non-profit. Its idea comes "
        "from building design: a ramp built at the start serves wheelchair users, parents with prams "
        "and delivery workers, and costs less than one added later. In a lesson, options built in "
        "from the start serve the children you expected and those you did not. CAST released UDL "
        "Guidelines 3.0 on 30 July 2024."),
      T(["Principle", "The question it asks", "Example options (Illustrative)"],
        [["Multiple means of engagement", "Why are learners interested, and what keeps them going?",
          "Choice of topic for a project; local examples; short goals with feedback"],
         ["Multiple means of representation", "How is information presented?",
          "Spoken and written instructions; pictures and objects; text read aloud; key words in the "
          "home language"],
         ["Multiple means of action and expression", "How can learners show what they know?",
          "Oral answers, drawings, models or writing; a scribe or speech-to-text; more time"]]),
      H("cyan", "CAST states the goal of UDL as learner agency that is purposeful and reflective, "
        "resourceful and authentic, strategic and action-oriented. Source: CAST (2024), UDL "
        "Guidelines version 3.0, udlguidelines.cast.org.")),

    C("UDL in an Indian classroom", "One lesson, planned with UDL for a mixed Class 4",
      B("<strong>Illustrative.</strong> A government school in rural Jharkhand, Class 4, 38 children. "
        "The lesson is on measuring length. Two children speak Santali at home, one has low vision, "
        "one is suspected of dyslexia and several are below grade level in reading."),
      TW([P("cyan", "Before UDL",
            "The teacher reads the textbook page, writes three sums on the board and asks children "
            "to copy and solve them. The child with low vision cannot see the board. The children "
            "with weak reading cannot follow the word problems. The Santali speakers sit silent. "
            "Six children finish.")],
         [P("green", "With UDL",
            "Children measure the classroom door with string, hand spans and a ruler, in groups. The "
            "teacher names the units in Hindi and Santali. Word problems are read aloud and drawn. "
            "The child with low vision has a large-print sheet and sits in front. Children may answer "
            "by speaking, drawing or writing. Twenty-nine finish.")]),
      H("amber", "None of these changes needs a special educator or new money. They need planning "
        "time and a teacher who expects variety. That is why UDL belongs in pre-service training.")),

    C("Differentiation", "Differentiated instruction adjusts content, process and product",
      B("Differentiated instruction starts from the same learning goal for the class and varies how "
        "children reach it. Where UDL builds options into the lesson for everyone, differentiation "
        "responds to particular children the teacher knows. The two work together."),
      T(["What can vary", "Meaning", "Example from a Class 6 science lesson (Illustrative)"],
        [["Content", "What material a child works with", "A simpler text with diagrams for some; the "
          "full chapter for others"],
         ["Process", "How the child makes sense of it", "Pairs with a stronger reader; a hands-on "
          "experiment; a short video with captions"],
         ["Product", "How the child shows learning", "A labelled poster, an oral explanation or a "
          "written answer"],
         ["Learning environment", "Where and how the class is arranged", "A quiet corner; seats near "
          "the board; group tables"],
         ["Pace", "How long a child has", "Extra time for some; extension tasks for those who finish "
          "early"]]),
      H("cyan", "Differentiation fails when it becomes permanent tracking: the 'slow group' that "
        "never gets the full content. Regroup often, keep the same goal and check whether every "
        "child reached it.")),

    C("Mother tongue first", "NEP 2020 asks for the home language as the medium of instruction to at least Grade 5",
      Q("Wherever possible, the medium of instruction until at least Grade 5, but preferably till "
        "Grade 8 and beyond, will be the home language/mother tongue/local language/regional language.",
        "National Education Policy 2020, paragraph 4.11"),
      TW([P("cyan", "What paragraph 4.11 adds",
            "This applies to public and private schools. High-quality textbooks, including science, "
            "will be made available in home languages. Where they are not, the language of "
            "transaction remains the home language wherever possible, and teachers are encouraged to "
            "use a bilingual approach with bilingual materials.")],
         [P("green", "Neighbours",
            "Nepal's Constitution gives every community the right to education in its mother tongue "
            "up to secondary level (Article 31(5)). The UNESCO GEM paper of 2016 recommends at least "
            "six years of mother tongue instruction so that early gains last.")]),
      H("amber", "'Wherever possible' is the policy's escape clause. In a classroom with five home "
        "languages and one teacher, the practical answer is multilingual education that uses the "
        "children's languages as bridges, which is the next slide.")),

    C("Multilingual education", "Mother tongue based multilingual education builds a bridge, step by step",
      FLOW("HOME LANGUAGE: oral work, stories and first reading in the child's language",
           "ORAL SECOND LANGUAGE: the school language spoken, through songs and talk",
           "READING IN BOTH: transfer of decoding skills to the second script",
           "SUBJECTS IN BOTH: concepts taught bilingually, assessment allows either"),
      TW([P("cyan", "Why the bridge works",
            "Children who learn to read in a language they speak learn what reading is. That skill "
            "transfers to a second language. Children who start in a language they do not speak "
            "often learn to copy and recite without comprehension.")],
         [P("amber", "What it needs",
            "Teachers who speak the children's languages, or community assistants who do; graded "
            "reading material in those languages; and assessment that does not penalise answers in "
            "the home language in the early grades.")]),
      B("The sequence above is an Illustrative summary of the common model. NEP 2020 paragraph 4.12 "
        "says children pick up languages very quickly between ages 2 and 8 and asks for early "
        "reading and writing in the mother tongue, with reading and writing in other languages from "
        "Grade 3.", sm=True)),

    C("Assistive technology", "Assistive technology ranges from a pencil grip to a screen reader",
      T(["Need", "Low-tech option", "Higher-tech option", "Legal hook"],
        [["Low vision", "Large print, bold-lined paper, seating near light", "Magnifier, tablet with "
          "zoom, screen reader", "RPwD s17(g) free devices to 18"],
         ["Blindness", "Braille slate and stylus, tactile diagrams, abacus", "Braille display, "
          "talking books, screen reader", "RPwD s16(v); CRPD Art 24(3)(a)"],
         ["Deaf or hard of hearing", "Visual timetables, seating to see faces, ISL", "Hearing aids, "
          "captioned videos, sound field system", "RPwD s16(v); NEP para 6.11"],
         ["Physical disability", "Pencil grips, slant boards, adapted seating", "Adapted keyboard, "
          "switch access, voice input", "RPwD s16(ii), (iii)"],
         ["Speech and communication", "Picture boards, gesture, symbol cards", "Speech-generating "
          "device or app", "RPwD s17(f)"],
         ["Reading difficulty", "Coloured overlays, audio of texts, reading rulers", "Text-to-speech, "
          "speech-to-text", "RPwD s16(vi), s17(i)"]]),
      H("amber", "The table is Illustrative. Begin with what the child and family already use. A "
        "device that stays in a cupboard because nobody was trained to maintain it, or because the "
        "school has no power for charging, has cost money and changed nothing.")),

    C("Individual education plans", "An individual education plan turns rights into a weekly routine",
      TERM("Individualised education plan (IEP)",
           "A written plan for one learner that records strengths and needs, sets a small number of "
           "goals for a term, lists the accommodations and support to be provided and by whom, and "
           "says how progress will be checked. General Comment 4, paragraph 33, calls for such plans "
           "to identify reasonable accommodation and specific support for individual students."),
      TW([BL(["Who the child is: strengths, interests, how she communicates",
              "Present levels: what she can do now in reading, maths and daily routines",
              "Three to five goals for the term, written so anyone can check them"], color="cyan")],
         [BL(["Accommodations: seating, materials, time, format of tests",
              "Support: who does what, and how often (class teacher, special educator, family)",
              "Review: a date, and what will count as progress"], color="green")]),
      H("amber", "Indian law does not use the term IEP. RPwD Act section 16(iv) requires necessary "
        "support, individualised or otherwise, and section 16(vii) requires monitoring each student's "
        "progress. An IEP is the simplest way to show both.")),

    C("An IEP, worked", "A one-page IEP for a Class 3 child",
      B("<strong>Illustrative.</strong> Anjali, aged 8, Class 3, government primary school in Pune "
        "district. Moderate hearing loss in both ears, uses a hearing aid that often needs a battery. "
        "Loves drawing. Reads 15 Marathi words a minute; class average around 40."),
      T(["IEP part", "Entry for Anjali (Illustrative)"],
        [["Goal 1", "Read a Class 2 Marathi passage at 30 words a minute by the end of term"],
         ["Goal 2", "Use 50 Indian Sign Language signs for classroom routines, with two classmates "
          "learning the same signs"],
         ["Accommodations", "Front seat facing the teacher's face; key words written on the board; "
          "videos with captions; spare hearing aid batteries kept at school"],
         ["Support", "Special educator from the Block Resource Centre visits weekly; class teacher "
          "spends 10 minutes daily on reading; mother practises words at home"],
         ["Assessment", "Oral tests replaced by written or drawn answers where hearing affects the "
          "result"],
         ["Review", "Six weeks; reading rate checked monthly and recorded"]]),
      H("cyan", "Notice that Anjali stays in her own class throughout. The plan changes how the class "
        "works for her, which is the definition in RPwD section 2(m).")),

    C("Exams and climate", "Examinations and classroom culture decide whether inclusion lasts",
      TW([P("cyan", "Examinations: RPwD Act section 17(i)",
            "Government shall make suitable modifications in the curriculum and examination system "
            "for students with disabilities, such as <strong>extra time</strong> for completing the "
            "paper, the facility of a <strong>scribe or amanuensis</strong>, and <strong>exemption "
            "from second and third language courses</strong>. Board exams are where many disabled "
            "students leave school, so schools should apply for these accommodations early.")],
         [P("green", "Classroom climate",
            "Peer tutoring, cooperative group work and clear rules against teasing help every child. "
            "NEP paragraph 6.20 asks the curriculum to teach respect for all persons, empathy, "
            "tolerance and inclusion. Bullying of disabled children is often missed because the "
            "child cannot report it in the school's language.")]),
      B("A short daily routine helps: a predictable timetable on the wall in words and pictures, a "
        "buddy for each child who needs one, and two minutes at the end of the day for children to "
        "say what was hard. These cost nothing, and they help children with autism, anxiety or "
        "hearing loss the most."),
      H("amber", "Exam accommodations need paperwork. Keep the child's certificate and school "
        "records ready well before the Class 10 board registration deadline.")),
]

# ===================== SECTION 10 =====================
SLIDES += [
    D("10", "Section Ten", "Teachers and support staff"),

    C("Every teacher", "Inclusion depends on the ordinary class teacher",
      B("A special educator may visit a school once a week. The class teacher is there every day. "
        "NEP 2020 paragraph 6.14 makes teaching children with specific disabilities, including "
        "learning disabilities, an integral part of all teacher education programmes, and RPwD Act "
        "section 17(b) to (d) requires teacher training institutions and training of teachers and "
        "staff."),
      TW([P("cyan", "What a class teacher needs to know",
            "How to plan with options (UDL); how to spot a child who is struggling and record what "
            "she sees; basic accommodations; a handful of sign language and Braille basics; when and "
            "how to ask for specialist support; how to talk with families.")],
         [P("amber", "What a class teacher needs to have",
            "Time to plan; a manageable class size; a special educator or resource person who "
            "answers questions; materials in accessible formats; and a headteacher who backs "
            "accommodations when other parents complain.")]),
      H("cyan", "Training is necessary and insufficient. Teachers trained in a three-day workshop "
        "and sent back to a class of 60 with no support usually return to the old way of teaching "
        "within weeks. Plan follow-up classroom visits as part of any training budget.")),

    C("Specialists", "Special educators, resource teachers and therapists each have a role",
      T(["Role", "What they do", "Where they sit in India"],
        [["Special educator", "Plans with class teachers, teaches specific skills (Braille, ISL, "
          "reading support), writes and reviews IEPs", "Block Resource Centres and school clusters; "
          "the subject of Rajneesh Kumar Pandey v Union of India"],
         ["Resource person (contractual)", "Similar work, often itinerant across many schools",
          "Common under Samagra Shiksha, for example Telangana's Bhavitha centres"],
         ["Therapists", "Physiotherapy, speech therapy, occupational therapy", "Block camps, district "
          "hospitals, NGOs; rarely in schools"],
         ["Sign language interpreter", "Interprets lessons for deaf students", "Very rare in "
          "ordinary schools"],
         ["Counsellor", "Mental health, behaviour and family support", "NEP para 6.5 names "
          "counsellors and social workers for urban poor areas"]]),
      H("amber", "Special educators in India must be registered with the Rehabilitation Council of "
        "India; in <em>Rajneesh Kumar Pandey</em> (2021) the Supreme Court held that special "
        "teachers must be qualified and registered with the Council. Ask any programme hiring special educators to "
        "check registration.")),

    C("Models of support", "Four ways to organise specialist support, with trade-offs",
      T(["Model", "How it works", "Strength", "Weakness"],
        [["Itinerant", "One special educator visits many schools on a cycle", "Reaches remote "
          "schools at low cost", "A visit every few weeks is too thin for high support needs"],
         ["Resource room", "A room in a school where children spend part of the day with a "
          "specialist", "Intensive help, equipment in one place", "Can become a separate class by "
          "another name"],
         ["Co-teaching", "Class teacher and special educator teach the class together", "Changes "
          "the ordinary classroom", "Needs time, staff and good relationships"],
         ["Cluster resource centre", "A hub for several schools with specialists and devices",
          "Pools scarce skills; NEP para 6.11", "Distance and transport for children"]]),
      B("Most districts use a mix. The question to ask is whether the model changes what happens in "
        "the ordinary classroom, or only removes the child from it for a while. General Comment 4's "
        "test of inclusion, structural change to content and teaching, applies to support models "
        "too."),
      H("cyan", "This table is a teaching summary with no ranking implied. Choose the model by the children's "
        "needs, the distances and the staff a district can recruit and keep.")),

    C("Screening", "PRASHAST gives schools a common disability screening checklist",
      B("NCERT developed <strong>PRASHAST</strong>, a disability screening checklist and mobile app "
        "for schools covering the 21 disabilities under the RPwD Act 2016, because no uniform "
        "screening checklist for schools existed. Version 2.0 generates a school-level report that "
        "can be shared with authorities to start certification under Samagra Shiksha guidelines."),
      TW([BL(["Part 1 for regular teachers, part 2 for special educators",
              "Available on Android and iOS; e-book in Hindi and English",
              "Data intended to feed disability certification through assessment camps",
              "Described by NCERT as statistically standardised"], color="cyan")],
         [P("red", "NCERT's own warning",
            "The brochure states that PRASHAST <strong>should not be used for certification or "
            "labelling</strong>. Screening flags a child for a closer look. It does not diagnose. A "
            "teacher who tells a parent 'the app says your child is disabled' has misused it.")]),
      B("Source: NCERT, Central Institute of Educational Technology, PRASHAST 2.0 brochure.", sm=True),
      H("amber", "Screening without support afterwards raises expectations and can harm a child "
        "through a label with no service. Budget for what happens after the flag.")),

    C("Families", "Families are part of the support team",
      TW([P("cyan", "What families bring",
            "They know how the child communicates, what calms her and what she can do at home that "
            "she never shows at school. They also carry the cost of every missing service: travel to "
            "camps, lost wages, the hours of home teaching.")],
         [P("amber", "What schools often get wrong",
            "Meeting families only when there is a problem; using jargon; asking a mother to stay in "
            "class all day as the child's aide; and treating a refusal of home-based education as "
            "lack of cooperation.")]),
      BL(["Invite the family to write the first draft of the 'who the child is' part of the IEP",
          "Use School Management Committee meetings (RTE Act section 21) to discuss access as "
          "well as funds",
          "Connect families to disabled persons' organisations and parent groups in the district",
          "Explain certificates and entitlements in the family's language, with a written note"],
         color="green"),
      H("cyan", "NEP 2020 paragraph 6.12 says technology-based orientation and learning materials for "
        "parents and caregivers will be given priority, while stating that the education of children "
        "with disabilities is the responsibility of the State.")),

    C("Building a workforce", "Planning teachers for inclusion is a district-level task",
      B("<strong>Illustrative worked example.</strong> A district has 1,800 government schools in 60 "
        "clusters. UDISE+ shows 3,600 CWSN enrolled. NSS-based prevalence suggests many more children "
        "are unidentified."),
      T(["Step", "Calculation or decision (Illustrative)"],
        [["Current specialist staff", "45 contractual resource persons, about 80 enrolled CWSN each, "
          "spread over 40 schools each"],
         ["Target ratio", "One special educator per cluster as a first step: 60 posts"],
         ["Class teacher training", "Two teachers per school trained in UDL and screening: 3,600 "
          "teachers, with follow-up visits by the cluster special educator"],
         ["Equipment", "Cluster resource kit with Braille materials, hearing aid batteries, picture "
          "boards and a tablet"],
         ["Cost lines", "Map each line to Samagra Shiksha's Inclusive Education component and the "
          "state budget"]]),
      H("amber", "The numbers are invented for teaching. The method is the point: start from children, "
        "then staff, then training, then equipment, and make each line traceable to a budget head.")),
]

# ===================== SECTION 11 =====================
SLIDES += [
    D("11", "Section Eleven", "Measuring inclusion"),

    C("Why measure", "What gets counted gets planned for",
      B("SDG indicator 4.5.1 asks for parity indices by disability status as data become available. "
        "RPwD Act section 16(vii) asks every institution to monitor participation, progress and "
        "completion of each student with disability. Neither is possible without a way to identify "
        "disabled children that is consistent across schools, districts and countries."),
      TW([P("red", "The problem with yes or no",
            "A question such as 'Is this child disabled?' depends on stigma, on whether the family "
            "has a certificate and on how the interviewer asks. Counts vary wildly between surveys "
            "and between districts for reasons that have nothing to do with children.")],
         [P("green", "The functional answer",
            "Ask about difficulty with specific activities, with graded answers. The Washington "
            "Group on Disability Statistics and UNICEF built question sets on this approach, based "
            "on the WHO International Classification of Functioning, Disability and Health.")]),
      H("cyan", "Section 2 described the ICF. This section shows how its logic becomes survey "
        "questions that a programme can use in a baseline.")),

    C("WG Short Set", "The Washington Group Short Set uses six questions for adults",
      B("The <strong>Washington Group Short Set on Functioning (WG-SS)</strong> is a set of six "
        "questions for national censuses and surveys, developed, tested and adopted by the Washington "
        "Group on Disability Statistics. It covers seeing, hearing, walking or climbing steps, "
        "remembering or concentrating, self-care and communicating."),
      TW([P("cyan", "How the answers work",
            "Each question has four graded answers: no difficulty, some difficulty, a lot of "
            "difficulty, cannot do at all. The graded scale lets an analyst set a severity "
            "threshold and report it, instead of forcing a yes or no at the interview.")],
         [P("amber", "Why it is not enough for children",
            "The Washington Group recognised that the Short Set does not apply to children under five "
            "and may miss many children with developmental disabilities above that age. That is why "
            "it built the Child Functioning Module with UNICEF.")]),
      B("Sources: Washington Group, WG-SS and CFM pages, washingtongroup-disability.com (read October "
        "2026); response categories as printed in the WG/UNICEF CFM questionnaire (19 March 2020).",
        sm=True)),

    C("Child Functioning Module", "The Child Functioning Module asks about the areas that matter for children",
      B("The <strong>WG/UNICEF Child Functioning Module (CFM)</strong> was finalised in 2016. It has "
        "two versions, for children aged 2 to 4 and 5 to 17, both answered by the mother or primary "
        "caregiver. It is part of UNICEF's Multiple Indicator Cluster Surveys, and a joint statement "
        "in March 2017 recommended it for SDG data disaggregation for children."),
      T(["Age group", "Areas of functioning assessed"],
        [["All ages (2-17)", "Vision, hearing, mobility, communication or comprehension, behaviour, "
          "learning"],
         ["Ages 2-4 only", "Dexterity, playing"],
         ["Ages 5-17 only", "Self-care, remembering, focusing attention, coping with change, "
          "relationships, emotions (anxiety and depression)"]]),
      TW([B("The 5-17 questionnaire has 24 items (CF1 to CF24). Functioning items use the four-point "
            "difficulty scale. The two emotion items ask how often the child seems very anxious or "
            "very sad: daily, weekly, monthly, a few times a year or never.", sm=True)],
         [H("amber", "The emotion questions matter. A child who is very anxious every day may hold no "
            "certificate and still need accommodation at school.")]),
      B("Sources: Washington Group, CFM page; WG/UNICEF CFM ages 5-17 questionnaire.", sm=True)),

    C("Teacher version and IEM", "Two newer modules bring measurement into schools",
      TW([P("cyan", "CFM Teacher Version (CFM-TV)",
            "Developed after the 2016 CFM, with a teacher as respondent, for use in Education "
            "Management Information Systems and school-based surveys. It has <strong>20 "
            "questions</strong> for children aged 5 to 17 covering seeing, hearing, mobility, fine "
            "motor skills, communication, learning, remembering, concentrating, accepting change, "
            "controlling behaviour, making friends, and anxiety and depression. It was tested in "
            "2022-2023.")],
         [P("green", "Inclusive Education Module (IEM)",
            "A WG and UNICEF set of questions on the environmental factors that affect school "
            "participation, applicable to all children whether or not they have a disability. It has "
            "five modules, the first two on the child's educational background. Testing showed the "
            "best way to find barriers was to ask about the school environment for all children.")]),
      H("amber", "For India, the CFM-TV is the closest fit to UDISE+. A state could pilot it in a few "
        "districts beside the existing CWSN categories and compare who each method identifies. "
        "Sources: Washington Group, CFM-TV and IEM pages, read October 2026.")),

    C("Categories or functioning", "Medical categories and functional difficulty answer different questions",
      TW([P("cyan", "Impairment categories (UDISE+, RPwD Schedule)",
            "Tell you what kind of specialist support or device a child may need, and link to "
            "entitlements that require a certificate. They depend on diagnosis, which is scarce in "
            "rural areas, so they undercount, especially for learning disabilities, autism and mental "
            "illness.")],
         [P("green", "Functional difficulty (WG, CFM)",
            "Tells you how many children face difficulty in each area, in a way that can be compared "
            "across places and time, and supports SDG 4.5.1 parity indices. It does not give a "
            "diagnosis or decide entitlements.")]),
      B("A practitioner needs both. Use functional questions to find children and to compare "
        "attendance and learning between those with and without difficulty. Use categories to plan "
        "specialist services and help families obtain certificates. Never use a functional screen as "
        "if it were a certificate, and never treat the absence of a certificate as proof that a child "
        "needs nothing."),
      H("amber", "General Comment 4, paragraph 30, is the legal anchor here: reasonable accommodation "
        "may not be conditional on a medical diagnosis.")),

    C("A baseline, step by step", "How to run a functioning baseline for an inclusion programme",
      FLOW("ADAPT: translate the CFM using WG translation guidance; test with 10 families",
           "SAMPLE: all households in programme villages, or a random sample of them",
           "ASK: CFM questions to the caregiver, plus school status and class",
           "LINK: match children to school records and learning tests",
           "REPORT: out-of-school and learning gaps by difficulty, sex and social group"),
      TW([P("cyan", "Practical points (Illustrative)",
            "Train enumerators to read the answer options aloud every time, as the questionnaire "
            "instructs. Use the version for the right age band. Keep the data on functional "
            "difficulty apart from names in the analysis file.")],
         [P("amber", "Consent and data protection",
            "Explain the purpose to caregivers, seek the child's assent where age allows, and store "
            "the data securely. The DPDP Act 2023 research exemption in section 17(2)(b) applies, from "
            "13 May 2027, only when its conditions are met. Programme lists used to deliver services are personal data "
            "processing in the ordinary way.")]),
      H("green", "A baseline of this kind turns 'we do not know how many disabled children are out of "
        "school here' into a number with a method behind it, which a district officer can act on.")),

    C("Indicators", "A short set of indicators for an inclusion programme",
      T(["Dimension", "Indicator (Illustrative)", "Data source"],
        [["Access", "Out-of-school children with functional difficulty, aged 6-18, per 1,000", "Door "
          "to door survey with CFM questions; RPwD s17(a) survey"],
         ["Attendance", "Average days attended by children with and without difficulty",
          "School registers by child"],
         ["Participation", "Share of CWSN with a current IEP reviewed in the last term",
          "School records"],
         ["Learning", "Reading and maths levels of children with and without difficulty",
          "Accommodated learning assessment"],
         ["Environment", "Schools with a usable accessible toilet, ramp and at least one trained "
          "teacher", "Facility audit with observation"],
         ["Transition", "CWSN moving from Class 8 to Class 9, and from Class 10 to Class 11",
          "UDISE+ student records"]]),
      H("cyan", "These follow General Comment 4's emphasis on participation, accessibility, "
        "attendance and achievement. Compare children with and without difficulty in the same "
        "schools: the gap is the measure of inclusion.")),
]

# ===================== SECTION 12 =====================
SLIDES += [
    D("12", "Section Twelve", "A practitioner's toolkit"),

    C("School audit: building", "School audit checklist, part 1: getting in and getting around",
      TW([BL(["Is there a ramp with handrails at the main entrance, and is the path to it clear?",
              "Can a child using a wheelchair reach every classroom she needs, the toilet, the water "
              "point and the mid-day meal area?",
              "Is there an accessible toilet, and is it open, clean and used?",
              "Is lighting adequate for a child with low vision at every desk?",
              "Are the blackboard and charts at a height and contrast a child can read?",
              "Is there a quiet space a child can use when overwhelmed?"], color="cyan")],
         [P("amber", "Why each question",
            "Each item maps to RPwD Act section 16(ii), which requires buildings, campus and "
            "facilities to be accessible. UDISE+ asks whether a ramp exists; 58.2% of schools had "
            "ramps with handrails in 2025-26. The audit asks whether it works, which no national "
            "dataset records.")]),
      H("green", "Walk the route a child would walk, at the time she would walk it, and in the rain if "
        "you can. A ramp that ends at a step, or a toilet used as a store room, will show up only "
        "this way.")),

    C("School audit: teaching", "School audit checklist, part 2: teaching and support",
      TW([BL(["Does every child with an identified need have a written plan reviewed this term?",
              "Do lessons offer more than one way to take in information and to answer?",
              "Can at least one teacher use basic Indian Sign Language or Braille where a child needs "
              "it?",
              "Does a special educator visit, and how often, and what did the last visit change?",
              "Are exam accommodations (extra time, scribe, language exemption) applied for in "
              "time?"], color="green")],
         [BL(["Are children taught in a language they understand in the early grades, or with "
              "bilingual support?",
              "Are assistive devices in use, charged and repaired?",
              "Is teasing of disabled or minority children addressed when it happens?",
              "Are children with disabilities included in sport, assembly and trips (RPwD s16(i))?",
              "Do teachers know how to request support from the Block Resource Centre?"],
             color="indigo")]),
      H("amber", "Observe one full lesson and talk to three children before scoring this part. "
        "Teachers' answers about their own practice are useful and incomplete.")),

    C("School audit: data and governance", "School audit checklist, part 3: records, families and governance",
      TW([P("cyan", "Records",
            "Are CWSN recorded in UDISE+ by type? Is attendance tracked by child? Are reading and maths "
            "levels recorded for CWSN as for others (RPwD s16(vii))? Is there a list of out-of-school "
            "disabled children in the catchment, from the s17(a) survey or a local one?")],
         [P("green", "Families and governance",
            "Does the School Management Committee include parents of disadvantaged children (RTE "
            "s21)? Has it discussed access in the last year? Do families know about the girls' "
            "stipend, free devices and exam accommodations? Is there a written way to complain about "
            "a refused admission?")]),
      T(["Score", "Meaning (Illustrative scale)"],
        [["0", "Not in place"], ["1", "In place on paper only"], ["2", "In place and partly used"],
         ["3", "In place, used and checked in the last term"]]),
      H("amber", "Report scores by item. A single total hides the item that keeps a child out.")),

    C("Decision table", "A decision table for common situations",
      T(["Situation", "First action", "Legal basis to cite"],
        [["Private school refuses a disabled child under the 25% quota", "Written complaint to the "
          "district education officer; record the refusal", "RTE Act s12(1)(c), s13; RPwD Act s16(i)"],
         ["Government school says the child should go to a special school", "Ask for reasonable "
          "accommodation in writing; involve the special educator", "RPwD Act s16(iii), s31(1) "
          "(choice belongs to the child and family)"],
         ["Board exam without scribe or extra time", "Apply to the board early with the certificate",
          "RPwD Act s17(i)"],
         ["Deaf child with no sign language support", "Request ISL support and materials from the "
          "Block Resource Centre", "RPwD Act s16(v), s17(c),(f); NEP para 6.11"],
         ["Adivasi children not following lessons in the state language", "Bilingual materials and a "
          "community language assistant", "NEP para 4.11"],
         ["Child at home with severe disability, no visits", "Ask for home-based education with a "
          "plan and review", "RTE Act s3(3) proviso; NEP para 6.12"]]),
      H("cyan", "Escalate in steps: school, block, district, then the State Commissioner for Persons "
        "with Disabilities or the courts. Keep copies of every letter.")),

    C("Worked example", "Worked example: one block, one year",
      B("<strong>Illustrative.</strong> An NGO works with the education department in a block of "
        "Nandurbar district, Maharashtra, with 210 government schools and many Bhil and Pawra "
        "children. The goal for the year is to reduce the number of out-of-school children with "
        "functional difficulty."),
      FLOW("FIND: door-to-door CFM questions in 40 villages; 260 children with difficulty, 70 out of school",
           "FIX THE SCHOOLS: audit 40 schools; ramps, toilets, seating; bilingual reading materials",
           "SUPPORT: IEPs for 120 children; weekly visits by 3 special educators",
           "COUNT: attendance and reading levels each term, compared with other children"),
      TW([P("green", "End of year (Illustrative)",
            "45 of the 70 enrolled; attendance gap narrowed; reading gap unchanged. The team learns "
            "that teaching, more than access, is now the binding constraint.")],
         [P("amber", "What the example teaches",
            "Finding children is cheap compared with teaching them well. Budget the second year for "
            "teacher support and classroom practice.")])),

    C("Common mistakes", "Six mistakes that recur in inclusion programmes",
      TW([P("red", "Design mistakes",
            "Counting enrolment as success. Spending most of the budget on identification camps and "
            "devices with no classroom change. Running everything on contractual staff who leave "
            "when the project ends.")],
         [P("amber", "Practice mistakes",
            "Treating a screening flag as a diagnosis. Placing children in ordinary classes with no "
            "support, which General Comment 4 calls integration and not inclusion. Leaving out "
            "children whose difficulty is invisible: learning disabilities, mental illness and "
            "chronic illness.")]),
      B("Each mistake has a simple counter. Measure learning and transition as well as enrolment. "
        "Ring-fence money for teacher support. Push for regular posts and use the Rajneesh Kumar "
        "Pandey orders when talking to the state. Use PRASHAST as NCERT advises. Plan support before "
        "admission. Use functional questions so that hidden difficulties are counted."),
      H("cyan", "A useful habit: at every review meeting, ask which child the programme has not yet "
        "reached, and why.")),

    C("Where next", "Where next",
      B("Inclusive education connects to disability rights, to child rights, to the politics of "
        "language and caste and to the measurement of learning. These ImpactMojo 101 decks take each "
        "strand further."),
      TW([BL(["<a href=\"/101-courses/disability-inclusion.html\">Disability Inclusion 101</a>: "
              "disability rights and inclusion across sectors",
              "<a href=\"/101-courses/child-rights.html\">Child Rights 101</a>: the CRC, the RTE Act "
              "and child protection laws",
              "<a href=\"/101-courses/education-policy.html\">Education Policy 101</a>: how school "
              "systems are governed and financed",
              "<a href=\"/101-courses/fln.html\">Foundational Literacy &amp; Numeracy 101</a>: "
              "teaching every child to read and count"], color="cyan")],
         [BL(["<a href=\"/101-courses/edu-pedagogy.html\">Education &amp; Pedagogy 101</a>: "
              "classroom methods and how children learn",
              "<a href=\"/101-courses/caste-studies.html\">Caste Studies 101</a>: caste, exclusion "
              "and the law",
              "<a href=\"/101-courses/survey-design.html\">Survey Design 101</a>: building "
              "questionnaires such as a CFM baseline",
              "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the DPDP "
              "Act 101</a>: handling children's disability data lawfully"], color="green")]),
      H("amber", "Start with the three-part school audit in this section on one school you know, then "
        "read Disability Inclusion 101 for the wider rights picture.")),
]

# ===================== END =====================
SLIDES += [
    {"type": "end",
     "eyebrow": "Inclusive Education 101 &middot; Complete",
     "headline": "Change the school,<br>then count who is still outside.",
     "byline": "Inclusion is measured child by child: who is enrolled, who is learning, and who the "
               "system has not yet reached. Explore the rest of the ImpactMojo 101 Series, free "
               "forever.",
     "ctas": [
         {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
         {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"}],
     "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
]

DECK = {
    "slug": "inclusive-education",
    "title": "Inclusive Education 101",
    "description": ("Inclusive Education 101: a free foundational course for practitioners in South "
                    "Asia. CRPD Article 24 and General Comment 4, the Salamanca Statement and SDG "
                    "4.5; models of disability; who is excluded by disability, gender, caste, tribe, "
                    "religion, language, migration and poverty; Article 21A and the RTE Act 2009 "
                    "sections 3 and 12(1)(c); the RPwD Act 2016 sections 16, 17 and 31; NEP 2020 "
                    "chapter 6 and Samagra Shiksha; UDISE+, Census and NSS data; laws in Bangladesh, "
                    "Nepal, Pakistan and Sri Lanka; UDL, multilingual education, assistive technology "
                    "and IEPs; teacher preparation; the Washington Group Child Functioning Module; and "
                    "a school audit checklist. ImpactMojo, CC BY-NC-ND."),
    "slides": SLIDES,
}

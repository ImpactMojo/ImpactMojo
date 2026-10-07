# -*- coding: utf-8 -*-
"""
Programme Design 101 - ImpactMojo 101 Series (native deck spec)
Designing a development programme in South Asia, from problem analysis to an
implementation plan.
Build: python3 scripts/deck-builder/build.py programme_design
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


DECK = {
    "slug": "programme-design",
    "title": "Programme Design 101",
    "description": ("Programme Design 101: a free foundational course for development "
                    "practitioners in South Asia. Design a programme from problem to "
                    "implementation plan: problem trees, stakeholder and power analysis, "
                    "evidence review, delivery models, targeting, theory of change, "
                    "budgeting and cost per outcome, risk and safeguarding, adaptive "
                    "management, working with government schemes and designing for scale. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Programme<br>Design<br>101",
         "sub": "From a problem worth solving to a plan that can run at scale: a foundational "
                "course for practitioners designing development programmes in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Problem to Plan"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Why design decides outcomes"},
             {"name": "Problem analysis"},
             {"name": "Stakeholders and power"},
             {"name": "Evidence before design"},
             {"name": "Choosing the intervention and delivery model"},
             {"name": "Targeting"},
             {"name": "Theory of change, budget and cost per outcome"},
             {"name": "Risk and safeguarding at design stage"},
             {"name": "Implementation planning and adaptive management"},
             {"name": "Government partnership and design for scale"},
             {"name": "Practical application"},
             {"name": "Common design failures"},
         ]},

        # ===================== SECTION 01 =====================
        D("01", "Section One", "Why design decides outcomes"),

        C("Definition", "What programme design means", [
            body("<strong>Programme design</strong> is the set of decisions made before money "
                 "moves: which problem to work on, for whom, through what activities, delivered "
                 "by whom, at what cost, with what risks, and how the team will learn and change "
                 "course. A design is a written argument that a particular bundle of activities, "
                 "run in a particular place by a particular organisation, will change something "
                 "specific for a specific group of people."),
            term("Programme design",
                 "The process of moving from an analysed problem to a costed, staffed and "
                 "monitored plan of action, with the reasoning for each choice written down so "
                 "that others can test it."),
            hbox("Most of what goes wrong in implementation was decided, or left undecided, at "
                 "design stage. A field team can work around a weak plan for a while. It cannot "
                 "fix a plan aimed at the wrong problem or the wrong people."),
        ]),

        C("The design cycle", "Design is a sequence of linked decisions", [
            body("Each decision constrains the next. The problem analysis decides which causes "
                 "the programme can reach. The stakeholder map decides who can block or carry "
                 "it. The evidence review narrows the list of plausible interventions. Targeting "
                 "decides who receives them. The budget decides how many people that will be. "
                 "Risk planning and the monitoring plan decide whether the team will notice when "
                 "something stops working."),
            flow(["PROBLEM: what is wrong, for whom, and why",
                  "OPTIONS: what has worked elsewhere",
                  "CHOICE: intervention, delivery model, targeting",
                  "PLAN: budget, risks, staffing, timeline",
                  "LEARN: monitor, adapt, decide on scale"]),
            hbox("The sequence is iterative. A costing exercise that shows the plan is "
                 "unaffordable sends the team back to the delivery model, and that is a sign "
                 "the process is working.", "indigo"),
        ]),

        C("Two programmes", "Same goal, different designs, different results", [
            tw(pp("cyan", "Microcredit in Hyderabad",
                  "In 2005, 52 of 104 poor Hyderabad neighbourhoods were randomly chosen for a "
                  "Spandana branch. Banerjee, Duflo, Glennerster and Kinnan (AEJ: Applied, 2015) "
                  "found more new businesses (6.8 against 5.3 per 100 households) but no "
                  "significant rise in consumption after 15 to 18 months, no significant change "
                  "in health, education or women's empowerment, and very few differences two "
                  "years later."),
               pp("green", "Graduation in Bangladesh",
                  "BRAC's ultra-poor programme transferred livestock and skills to the poorest "
                  "women. Bandiera and co-authors (QJE, 2017), following over 21,000 households "
                  "in 1,309 villages, found that labour supply, earnings and assets rose, and "
                  "that asset accumulation and poverty reduction were sustained after four and "
                  "seven years.")),
            hbox("Both programmes aimed at poor households' livelihoods. The graduation design "
                 "addressed several binding constraints at once for a tightly targeted group. "
                 "Design choices, more than intentions, separated the results.", "amber"),
        ], compact=True),

        C("What is at stake", "Design choices move large public budgets", [
            body("In South Asia most programmes that reach scale do so through government "
                 "schemes, and a design choice made in a pilot can end up shaping spending for "
                 "tens of millions of people. Ayushman Bharat PM-JAY, launched on 23 September "
                 "2018, set out to cover about 10.74 crore families identified from the "
                 "Socio-Economic Caste Census 2011 using its deprivation (rural) and "
                 "occupational (urban) criteria. That targeting decision, taken at design "
                 "stage, shaped who was covered from the first day."),
            stats([
                {"num": "10.74 crore", "label": "families initially targeted by PM-JAY from SECC 2011 data",
                 "color": "cyan", "source": "Government scheme description, PM-JAY (gorakhpur.nic.in; Government of Goa note)"},
                {"num": "&#8377;5 lakh", "label": "cover per family per year for hospitalisation",
                 "color": "green", "source": "Government scheme description, PM-JAY (gorakhpur.nic.in)"},
                {"num": "35.5%", "label": "children under five stunted, India",
                 "color": "amber", "source": "NFHS-5 (2019-21), via DHS Program indicator data"},
            ]),
            hbox("A design that uses an old list, a narrow definition or a costly delivery "
                 "channel carries that choice into every year of the scheme.", "red"),
        ]),

        C("Who designs", "Who usually sits at the design table", [
            table(["Actor", "What they bring", "What they often miss"], [
                ["NGO programme team", "Field knowledge, relationships with communities",
                 "Costing at scale, government processes"],
                ["Donor or CSR funder", "Money, reporting templates, sometimes evidence",
                 "Local politics, seasonal and caste dynamics"],
                ["Government department", "Mandate, budget lines, frontline staff",
                 "Time to test, permission to fail"],
                ["Researchers", "Evidence, measurement, counterfactual thinking",
                 "Operations, staffing, procurement"],
                ["Community members", "Lived experience of the problem",
                 "Usually a seat at the table at all"],
            ]),
            hbox("A design written by one of these actors alone tends to inherit that actor's "
                 "blind spots. The rest of this course shows how to bring the others in "
                 "without producing a committee document.", "indigo"),
        ], compact=True),

        C("Design versus planning", "A design states reasons; a work plan states tasks", [
            tw(pp("cyan", "Design document",
                  "Answers why: why this problem, why these people, why this intervention, why "
                  "this partner, why this cost is worth paying. It names the assumptions the "
                  "argument depends on and says how each will be checked. It should be short "
                  "enough that a district official can read it in one sitting."),
               pp("indigo", "Work plan",
                  "Answers when and who: activities by month, responsible staff, procurement "
                  "steps, training calendars and reporting dates. It is derived from the design "
                  "and changes often. A work plan with no design behind it produces activity "
                  "reports and no learning.")),
            hbox("Many proposals contain a detailed work plan and a thin design. Reviewers then "
                 "fund a list of activities with no argument they can test. Write the reasons first "
                 "and the Gantt chart afterwards.", "amber"),
        ]),

        C("How this course is built", "Roadmap and companion decks", [
            body("Sections 2 to 6 move from the problem to the intervention and who receives "
                 "it. Section 7 covers the theory of change and the budget together, because a "
                 "causal chain with no cost attached cannot be compared with anything. Sections "
                 "8 to 10 cover risk, safeguarding, implementation, adaptive management, working "
                 "with government and scale. Section 11 is a worked example and checklist, and "
                 "Section 12 lists the failures that recur across South Asian programmes."),
            tw(pp("green", "Go deeper elsewhere",
                  "This deck touches the theory of change and the logframe briefly. Each has its "
                  "own 101 deck, as do MEL, cost-effectiveness, fundraising and safeguarding. "
                  "Links are on the final content slide."),
               pp("amber", "Illustrative examples",
                  "Where a slide uses an invented district, budget or programme to teach a "
                  "method, it is labelled Illustrative. Every named programme, figure and law "
                  "cited is real and carries its source.")),
        ]),

        # ===================== SECTION 02 =====================
        D("02", "Section Two", "Problem analysis"),

        C("Start with the problem", "Define the problem before choosing a solution", [
            body("The most common design error is starting with a solution: a favourite "
                 "intervention, a funder's priority or a model seen in another state. The "
                 "programme is then built backwards and the problem statement is written to fit. "
                 "A problem-first design asks what is wrong, for whom, how large the gap is, and "
                 "what causes it in this place. Only then does it look for interventions."),
            term("Problem statement",
                 "A short description of a negative condition, the people affected, its scale "
                 "and its location, written without naming a solution. 'Lack of a mobile app' is "
                 "a missing solution. 'Half of Class 5 children in the block cannot read a Class "
                 "2 text' is a problem."),
            hbox("Test: if your problem statement contains the name of your intervention, "
                 "rewrite it. 'Women lack SHG membership' assumes the answer.", "red"),
        ]),

        C("Problem trees", "The problem tree: causes below, effects above", [
            body("The European Commission's Project Cycle Management Guidelines (2004) set out "
                 "the problem tree as part of the analysis stage of the logical framework "
                 "approach, ideally built in a participatory workshop. The group picks a starter "
                 "problem, puts its direct causes below and its direct effects above, and keeps "
                 "asking what causes each one. The tree is then turned into an objectives tree "
                 "by rewriting each negative situation as a positive achievement."),
            tw([panel("red", "Roots (causes)", [bullets([
                    "Teachers teach to the textbook whatever the child's level",
                    "Children absent in harvest months",
                    "No reading material at home"], sm=True)])],
               [panel("amber", "Branches (effects)", [bullets([
                    "Children fall further behind each year",
                    "Drop-out at the Class 8 transition",
                    "Lower earnings and options later"], sm=True)])]),
            hbox("Illustrative tree for the focal problem 'children in Class 5 cannot read "
                 "fluently'. A real tree is built with teachers, parents and children, and "
                 "checked against data.", "indigo"),
        ], compact=True),

        C("Root causes", "Ask why until you reach something a programme can act on", [
            body("Root-cause analysis keeps asking why until the answer is either outside "
                 "anyone's control (rainfall, geography) or is a cause the programme can "
                 "influence. Pratham's work on Teaching at the Right Level began with a precise "
                 "diagnosis: children were enrolled, but instruction followed the grade "
                 "curriculum while many children were years behind it. The intervention grouped "
                 "children by learning level for part of the day. J-PAL reports that TaRL "
                 "learning camps in Uttar Pradesh doubled the number of children who could read "
                 "a paragraph or story."),
            flow(["Low reading levels",
                  "Instruction pitched at the grade curriculum",
                  "Curriculum and exams reward completing the syllabus",
                  "Act here: group by level, simple assessment, daily practice"]),
            hbox("Source: J-PAL, Teaching at the Right Level evidence to policy case study (six "
                 "randomised evaluations in seven Indian states, run with Pratham since 2001).",
                 "cyan"),
        ]),

        C("Evidence for the tree", "A problem tree is a hypothesis until data supports it", [
            body("Workshops produce plausible trees, and a plausible tree can still be wrong. "
                 "Each causal arrow should be checked against what data exists: NFHS for health "
                 "and nutrition, ASER and the National Achievement Survey for learning, PLFS for "
                 "work, the Census for demography, and administrative data from the scheme "
                 "itself. Where no data exists, a short diagnostic study (a few focus groups, a "
                 "rapid household survey, observation in five schools) is cheaper than a "
                 "programme built on a wrong cause."),
            table(["Claimed cause", "Evidence that would support it", "Where to look"], [
                ["Girls drop out because the school is far", "Enrolment falls with distance to secondary school",
                 "UDISE+ school locations, household survey"],
                ["Mothers do not deliver in facilities because of cost", "Out-of-pocket spending is high for deliveries",
                 "NFHS-5 district fact sheets"],
                ["Farmers do not adopt a variety because of credit", "Adoption rises when credit is offered",
                 "Prior trials, extension records"],
            ]),
        ], compact=True),

        C("Who defines the problem", "Whose problem is it", [
            tw(pp("indigo", "Outsider definition",
                  "A funder sees low institutional delivery rates and defines the problem as "
                  "women not using facilities. The design then focuses on demand: awareness, "
                  "incentives, transport."),
               pp("green", "Insider definition",
                  "Women in the same villages may describe the problem as being shouted at, "
                  "asked for informal payments, or sent onward to a district hospital at night. "
                  "The design then has to include quality of care and the behaviour of staff.")),
            body("India's Janani Suraksha Yojana, launched in 2005, paid cash for giving birth "
                 "in a health facility. Lim and colleagues (The Lancet, 2010) found it raised "
                 "antenatal care and facility births, and in their matching analysis associated "
                 "JSY payment with 3.7 fewer perinatal deaths per 1,000 pregnancies. They also "
                 "called for attention to the quality of obstetric care in facilities, a supply "
                 "side that the cash did not reach."),
            hbox("Use participatory methods to let affected people define the problem before "
                 "the design team does. See Participatory Methods 101.", "cyan"),
        ], compact=True),

        C("Scale and location", "Size the problem and find where it is concentrated", [
            body("A national average hides the places where a problem is worst. NFHS-5 "
                 "(2019-21) puts stunting among children under five at 35.5 per cent for India, "
                 "against 46.5 per cent in Meghalaya, 42.9 in Bihar, 39.7 in Uttar Pradesh and "
                 "39.6 in Jharkhand, and 23.4 in Kerala and 25.8 in Goa. Design for the "
                 "distribution of the problem: where it is concentrated, among which groups, and "
                 "whether the same cause operates everywhere."),
            tw(pp("cyan", "Questions to answer",
                  "How many people are affected? Where do they live? Which social groups carry "
                  "more of the burden (by caste, tribe, gender, disability, religion)? Is the "
                  "problem getting better or worse, and how fast?"),
               pp("amber", "Common errors",
                  "Using a state average to justify a district programme. Using data more than a "
                  "decade old as if current. Treating a problem as uniform when its causes differ "
                  "between, for example, tribal and non-tribal blocks.")),
            hbox("Note the vintage of every figure you use, and recheck it when a new round of "
                 "NFHS or the 2027 Census (reference date 1 March 2027, including caste "
                 "enumeration) is published.", "indigo"),
        ], compact=True),

        C("From tree to objectives", "Turn causes into objectives, then choose which to tackle", [
            body("Rewriting each cause as a positive condition gives an objectives tree. The "
                 "design team then chooses which branches to act on. No programme addresses "
                 "every cause. The choice depends on what evidence says can be changed, what "
                 "other actors already cover, the organisation's comparative advantage and the "
                 "budget. Writing down which causes you are deliberately leaving to others makes "
                 "the programme's boundary visible to funders and partners."),
            table(["Cause", "Objective", "Who acts on it"], [
                ["Instruction not matched to level", "Children taught at their learning level", "This programme"],
                ["Harvest-season absence", "Attendance maintained through the year", "Gram panchayat, school management committee"],
                ["No books at home", "Reading material in every hamlet", "Library partner"],
                ["Teacher vacancies", "Posts filled", "State education department (out of scope)"],
            ]),
            hbox("Illustrative example. The 'out of scope' row becomes an assumption in the "
                 "theory of change, to be monitored.", "amber"),
        ], compact=True),

        # ===================== SECTION 03 =====================
        D("03", "Section Three", "Stakeholders and power"),

        C("Stakeholders", "Map everyone who affects or is affected by the programme", [
            body("A stakeholder is any person, group or institution that can affect the "
                 "programme or is affected by it. In a South Asian district that list is long: "
                 "the intended participants and those excluded from them, frontline workers "
                 "(ASHAs, anganwadi workers, teachers, panchayat secretaries), elected "
                 "representatives, line departments, the district collector's office, local "
                 "traders and moneylenders, religious and caste leaders, other NGOs, and the "
                 "funder."),
            term("Stakeholder analysis",
                 "A structured assessment of each stakeholder's interest in the programme, "
                 "influence over it and likely response, used to plan engagement and to "
                 "identify risks."),
            hbox("Include the people who lose from the programme. A credit scheme for the "
                 "poorest households affects local moneylenders. A transparency reform affects "
                 "officials who benefited from opacity. They will act even if they are not "
                 "invited.", "red"),
        ]),

        C("Power and interest", "The power-interest grid", [
            tw([panel("indigo", "High power, high interest", [body(
                    "Manage closely. District collector, state mission director, funder. Involve "
                    "in design decisions and agree how disagreements will be resolved.", sm=True)]),
                panel("cyan", "Low power, high interest", [body(
                    "Keep informed and give voice. Intended participants, frontline workers. "
                    "Their interest is high and their formal power low, which is why design "
                    "must create channels for them.", sm=True)])],
               [panel("amber", "High power, low interest", [body(
                    "Keep satisfied. A finance department, a block development officer with "
                    "other priorities. Brief them and ask for little, until you need a "
                    "signature.", sm=True)]),
                panel("green", "Low power, low interest", [body(
                    "Monitor. Their position can change if the programme touches their "
                    "interests later.", sm=True)])]),
            hbox("The grid is a starting point. Power in a village is often informal, held "
                 "through land, caste, kinship or party, and it does not appear on an "
                 "organogram.", "cyan"),
        ], compact=True),

        C("Political economy", "Who gains, who loses, who decides", [
            body("A political economy analysis asks how power, incentives and institutions shape "
                 "whether a programme can work. The Udaipur nurse attendance study is the "
                 "standard warning. From 2005, Seva Mandir and the district health "
                 "administration in Rajasthan introduced time-stamping machines and pay "
                 "deductions for nurses who were absent. Attendance rose sharply at first. "
                 "Within about 16 months the difference between treatment and comparison centres "
                 "had disappeared."),
            quote("The local health administration, which was caught between the pressure of "
                  "the nurses and their directions to enforce the pay deductions, began to "
                  "undermine the incentive structure.",
                  "J-PAL evaluation summary, Incentives for nurses in the public health care "
                  "system in Udaipur, India (Banerjee, Duflo and Glennerster)"),
            hbox("The design worked on paper and failed in the hands of the people who had to "
                 "enforce it. Their incentives were never in the design.", "red"),
        ]),

        C("Thinking politically", "Questions a political economy analysis should answer", [
            table(["Question", "Why it matters for design"], [
                ["Who controls the resource the programme changes?", "They can redirect or block it"],
                ["Which officials must act, and what are they rewarded for?", "Unrewarded tasks are dropped first"],
                ["Which local elites benefit from the current situation?", "Expect capture or resistance"],
                ["What happens at the next election or transfer of the collector?", "Champions move; plans should not depend on one person"],
                ["Which caste, religious or gender norms shape access?", "Formal eligibility differs from actual access"],
            ]),
            hbox("Answer these in a short note, kept internal where it names individuals. A "
                 "political economy analysis that is published in full is usually rewritten to "
                 "say nothing.", "amber"),
        ], compact=True),

        C("Frontline workers", "Design for the people who will deliver it", [
            body("In India the last mile of most social programmes runs through a small number "
                 "of frontline workers: the ASHA, the anganwadi worker, the auxiliary nurse "
                 "midwife, the teacher, the gram rozgar sahayak. Each new programme tends to add "
                 "a register, an app or a meeting to their week. Nepal's Female Community Health "
                 "Volunteer programme, run since 1988 under the Ministry of Health, and "
                 "Pakistan's Lady Health Worker Programme, launched in 1994, both show how much a "
                 "health system comes to depend on this cadre."),
            tw(pp("red", "Design that overloads",
                  "A new survey every month, a separate app with its own login, a target with no "
                  "added honorarium, training scheduled during immunisation days."),
               pp("green", "Design that fits",
                  "Uses existing registers and meetings, adds data fields only when someone will "
                  "use them, pays for added work, and asks workers which tasks to drop.")),
            hbox("Time-use mapping of a frontline worker's week before design is cheap and "
                 "often decisive.", "cyan"),
        ], compact=True),

        C("Participation in design", "Bringing participants into design decisions", [
            body("Participation can mean very different things, from a consultation meeting "
                 "after decisions are made to shared control over the budget. Be specific about "
                 "which decisions participants will influence: the problem definition, the "
                 "choice of intervention, the selection criteria, the timing of activities, "
                 "the grievance process. Kerala's Kudumbashree, set up in 1997 as the State "
                 "Poverty Eradication Mission during the devolution to panchayats and the "
                 "People's Plan Campaign, built its structure on neighbourhood groups of 10 to "
                 "20 women, federated into area development societies at ward level and "
                 "community development societies at local government level."),
            stats([
                {"num": "2,57,627", "label": "neighbourhood groups under Kudumbashree (as of October 2026)",
                 "color": "green", "source": "Kudumbashree, official website, accessed October 2026"},
                {"num": "10-20", "label": "women in each neighbourhood group, one member per family",
                 "color": "cyan", "source": "Kudumbashree, official website, accessed October 2026"},
            ]),
            hbox("Participation has costs: time, travel, lost wages. Budget for them and hold "
                 "meetings at hours that suit women and daily-wage workers.", "amber"),
        ], compact=True),

        C("Exclusion in the room", "Who is missing from the stakeholder map", [
            body("Stakeholder maps are often drawn from the village centre outward and miss "
                 "people at the edges: Dalit and Adivasi hamlets, people with disabilities, "
                 "single women, migrant households, Muslim neighbourhoods in mixed villages, "
                 "transgender persons. Meetings called through the sarpanch tend to reproduce "
                 "the village's existing hierarchy. The design team has to seek these groups "
                 "out deliberately, often in separate meetings, and record what they say "
                 "separately."),
            tw(pp("indigo", "Practical steps",
                  "Walk every hamlet, including those across the road or the stream. Hold "
                  "separate women's and Dalit or Adivasi meetings. Ask an organisation of "
                  "persons with disabilities to review the design."),
               pp("cyan", "Record it",
                  "Note in the design document which groups were consulted, how, and what "
                  "changed as a result. A funder or evaluator can then check whether inclusion "
                  "shaped decisions.")),
            hbox("See Social Margins 101, Caste Studies 101 and Disability Inclusion 101.", "green"),
        ]),

        # ===================== SECTION 04 =====================
        D("04", "Section Four", "Evidence before design"),

        C("Why review evidence", "Find out what has already been tried", [
            body("Before designing an intervention, find out what is known about interventions "
                 "aimed at the same problem. Most problems in South Asian development have been "
                 "tackled many times, and some approaches have been rigorously tested. An "
                 "evidence review prevents the team from repeating designs that have already "
                 "failed, points to designs that have worked, and identifies the conditions under "
                 "which they worked."),
            tw(pp("green", "Sources to search first",
                  "3ie Development Evidence Portal (impact evaluations and systematic reviews), "
                  "Campbell Collaboration and Cochrane reviews, J-PAL and IPA evaluation "
                  "summaries, the World Bank's Strategic Impact Evaluation Fund, Ideas for "
                  "India."),
               pp("cyan", "South Asian grey literature",
                  "NITI Aayog evaluation reports, CAG performance audits, state evaluation "
                  "directorates, and the evaluation reports of large programmes such as "
                  "JEEViKA and Kudumbashree.")),
            hbox("See Systematic Reviews &amp; Evidence Synthesis 101 for how to search and "
                 "appraise properly.", "indigo"),
        ]),

        C("Reading evidence", "How much weight should a study carry", [
            table(["Type of evidence", "What it can tell you", "Main limitation"], [
                ["Systematic review or meta-analysis", "Average effect across many settings",
                 "Averages can hide where it does not work"],
                ["Randomised evaluation", "Causal effect in that setting", "May not transfer to yours"],
                ["Quasi-experimental study", "Causal effect under stated assumptions", "Assumptions may fail"],
                ["Process evaluation", "How and why delivery worked or broke", "No estimate of impact"],
                ["Monitoring data from a scheme", "Coverage, reach, cost", "No counterfactual"],
                ["Practitioner experience", "Operational detail, local fit", "Selective memory"],
            ]),
            hbox("Use each type for the question it can answer. A design needs both causal "
                 "evidence that an intervention can work and operational evidence about how to "
                 "deliver it.", "cyan"),
        ], compact=True),

        C("Transfer", "Will it work here", [
            body("A study shows that an intervention worked somewhere. Design asks whether it "
                 "will work in this district, through this organisation, for these people. "
                 "Muralidharan and Prakash (AEJ: Applied Economics, 2017) found that Bihar's "
                 "bicycle programme for girls continuing to secondary school raised girls' "
                 "age-appropriate enrolment by 32 per cent and cut the gender gap by 40 per cent. "
                 "The gains came mostly in villages farther from a secondary school, which the "
                 "authors read as a fall in the time and safety cost of getting to school."),
            tw(pp("green", "Likely to transfer",
                  "A district where secondary schools are far from villages and roads are "
                  "usable by bicycle, and where girls' mobility is the constraint."),
               pp("red", "Unlikely to transfer",
                  "A district where a secondary school is in every village, or where the "
                  "binding constraint is early marriage or the cost of fees.")),
            hbox("Transfer depends on the mechanism. Write down why the intervention worked, "
                 "then check whether that reason holds in your setting.", "amber"),
        ], compact=True),

        C("Mechanisms", "Ask what made it work", [
            body("A mechanism is the reason an intervention produces its effect. Teaching at "
                 "the Right Level works because instruction matches the child's level, so its "
                 "core is grouping by level and simple, frequent assessment. Bicycles worked in "
                 "Bihar because they reduced the time and safety cost of the journey. Graduation "
                 "programmes appear to work because several constraints (assets, consumption, "
                 "skills, confidence) are relieved together. Copying the visible features of a "
                 "programme without its mechanism produces what Andrews, Pritchett and Woolcock "
                 "call isomorphic mimicry."),
            term("Isomorphic mimicry",
                 "Adopting the form of a successful programme or institution, its names, "
                 "manuals and structures, without its function. Described in Andrews, Pritchett "
                 "and Woolcock, World Development (2013)."),
            hbox("When adapting a model, separate its core components, which carry the "
                 "mechanism, from its adaptable periphery, which can change with context.", "cyan"),
        ]),

        C("Graduation evidence", "A worked evidence review: the graduation approach", [
            body("Suppose a team wants to design a livelihoods programme for the poorest "
                 "households in a district. A short review would find BRAC's Targeting the Ultra "
                 "Poor programme in Bangladesh, the six-country trial published in Science in "
                 "2015 by Banerjee, Duflo and colleagues (Ethiopia, Ghana, Honduras, India, "
                 "Pakistan and Peru), and the long-run Bangladesh study by Bandiera and "
                 "co-authors in the Quarterly Journal of Economics (2017)."),
            table(["Finding", "Design implication"], [
                ["Impacts on consumption and psychosocial status lasted at least a year after support ended (Science, 2015)",
                 "Time-limited support can be enough"],
                ["Gains in Bangladesh persisted after four and seven years (QJE, 2017)",
                 "Plan follow-up measurement over years"],
                ["The package combines asset, stipend, training, coaching and savings",
                 "Removing components needs its own test"],
                ["Implemented by several partners in different settings",
                 "The model can be adapted, with core features kept"],
            ]),
        ], compact=True),

        C("Null results", "Evidence that something did not work is useful", [
            body("Designers tend to search for success stories. Evaluations that found no "
                 "effect are at least as useful because they remove options. The Hyderabad "
                 "microcredit evaluation found no significant rise in consumption and no "
                 "significant change in health, education or women's empowerment 15 to 18 "
                 "months after branches opened, and very few differences two years later. "
                 "Credit may still help in other ways. A design that promises "
                 "poverty reduction through microcredit alone needs a stronger argument than the "
                 "evidence currently gives."),
            tw(pp("amber", "How to use a null result",
                  "Ask whether the intervention was delivered as designed, whether the sample "
                  "was large enough to detect a plausible effect, and whether the outcome "
                  "measured was the one that should have moved."),
               pp("indigo", "Where to find them",
                  "Registered trials (AEA RCT Registry, 3ie's registry), J-PAL summaries, "
                  "and working papers, since journals publish fewer null results.")),
            hbox("Record the null and negative findings you found in the design document, with "
                 "what you concluded from each.", "cyan"),
        ], compact=True),

        C("When evidence is thin", "Designing when no good study exists", [
            body("For many questions in South Asia, such as programmes for urban informal "
                 "workers, climate adaptation for smallholders, or services for adolescents with "
                 "disabilities, rigorous evidence is thin. The design then rests on theory, "
                 "practitioner knowledge and evidence from adjacent problems. That is acceptable "
                 "if the design says so plainly and builds in ways to learn quickly: a pilot with "
                 "clear decision points, monitoring of the riskiest assumptions, and a budget for "
                 "evaluation."),
            flow(["State what is known and from where",
                  "Name the assumptions with least evidence",
                  "Design a pilot to test those first",
                  "Set decision rules: continue, adapt, stop"]),
            hbox("A design that admits uncertainty and plans to resolve it is stronger than one "
                 "that claims certainty it does not have. Funders who understand evaluation "
                 "prefer the first.", "green"),
        ]),

        # ===================== SECTION 05 =====================
        D("05", "Section Five", "Choosing the intervention and delivery model"),

        C("Options", "Generate several options before choosing one", [
            body("Teams that consider one option tend to fund it. List at least three distinct "
                 "ways of addressing the chosen causes, including doing less, working through an "
                 "existing scheme, and a cash alternative. Then compare them on the same "
                 "criteria. The comparison often shows that the most familiar option is neither "
                 "the cheapest nor the most likely to work."),
            table(["Criterion", "Question to ask of each option"], [
                ["Evidence", "Has this worked for a similar problem and group?"],
                ["Cost per outcome", "What would one unit of outcome cost?"],
                ["Feasibility", "Can our organisation and partners deliver it?"],
                ["Scalability", "Could government or others run it later?"],
                ["Equity", "Who would it reach first, and who would it miss?"],
                ["Risk", "What could go wrong, and for whom?"],
            ]),
            hbox("Score options with the people who will deliver them. A scoring exercise done "
                 "only by the proposal writer is a justification exercise.", "amber"),
        ], compact=True),

        C("Cash benchmark", "Compare against cash", [
            body("A useful discipline is to ask whether the programme would do more good than "
                 "giving its budget to participants as cash. Muralidharan and Prakash (2017) "
                 "report that Bihar's bicycle programme was much more cost-effective at raising "
                 "girls' secondary enrolment than comparable conditional cash transfer "
                 "programmes in South Asia. The cash benchmark does not always win. It forces "
                 "the designer to state what an in-kind or service programme adds."),
            tw(pp("cyan", "Cash can be better when",
                  "Needs differ across households, markets work, and participants know their "
                  "constraints better than the programme does."),
               pp("green", "In-kind or services can be better when",
                  "The good is under-supplied locally, there is a coordination or safety "
                  "problem (as with girls cycling together), or the goal is a public good such "
                  "as learning.")),
            hbox("Pakistan's Benazir Income Support Programme, launched in 2008, shows the "
                 "scale cash delivery can reach once identification and payment systems exist.",
                 "indigo"),
        ], compact=True),

        C("Delivery models", "Who delivers, and through what channel", [
            table(["Delivery model", "South Asian example", "Strength", "Weakness"], [
                ["Government frontline system", "Anganwadi services, PM POSHAN school meals",
                 "Reach and permanence", "Overloaded staff, slow change"],
                ["Community institutions", "Kudumbashree, JEEViKA SHG federations",
                 "Local ownership, low cost", "Capture by better-off members"],
                ["NGO direct delivery", "BRAC graduation in Bangladesh",
                 "Quality control, flexibility", "Hard to sustain without funding"],
                ["Community health workers and volunteers", "Nepal FCHVs, Pakistan LHWs, India's ASHAs",
                 "Trust, proximity", "Workload, pay disputes"],
                ["Private providers with public payment", "PM-JAY empanelled hospitals",
                 "Capacity, choice", "Fraud, cream-skimming"],
                ["Digital", "Direct benefit transfer, telemedicine",
                 "Speed, low marginal cost", "Excludes the unconnected"],
            ]),
        ], compact=True),

        C("Choosing the channel", "Match the delivery model to the mechanism", [
            body("The delivery model should carry the mechanism. If the mechanism is trust and "
                 "repeated contact, as in many health behaviour programmes, a community worker "
                 "who lives in the village fits. If the mechanism is rapid, uniform transfer of "
                 "money, a digital payment system fits. If the mechanism is changing what "
                 "teachers do in classrooms, the channel has to reach teachers through the "
                 "education department's own mentoring and supervision structure."),
            tw(pp("indigo", "The TaRL route",
                  "J-PAL documents two TaRL models used since 2012: learning camps in which "
                  "Pratham instructors teach children directly for short intensive periods, "
                  "and a government partnership model in which government teachers deliver "
                  "TaRL with training and on-site support from mentors inside the system."),
               pp("amber", "The trade-off",
                  "Camps run by Pratham's own instructors keep delivery under one "
                  "organisation's control. Government delivery can reach every school and "
                  "depends on the system protecting time for level-based teaching.")),
            hbox("Design the delivery model you would use at scale, then pilot that, so the "
                 "pilot tests what would actually happen.", "green"),
        ], compact=True),

        C("Dosage", "How much, how often, for how long", [
            body("Dosage is the quantity of the intervention a participant receives: number of "
                 "sessions, size of transfer, length of support. Designs often set dosage by "
                 "budget arithmetic when it should follow what the mechanism needs. TaRL learning camps, "
                 "as described by J-PAL, usually last ten days at two to three hours a day, and "
                 "three to five camps a year give 30 to 50 days of instruction. That intensity "
                 "is part of the model. "
                 "Cutting it to fit a budget changes the intervention."),
            stats([
                {"num": "10 days", "label": "length of one TaRL learning camp", "color": "cyan",
                 "source": "J-PAL, TaRL case study"},
                {"num": "3-5", "label": "camps a year in the camp model", "color": "green",
                 "source": "J-PAL, TaRL case study"},
                {"num": "30-50", "label": "instructional days in a year", "color": "amber",
                 "source": "J-PAL, TaRL case study"},
            ]),
            hbox("If the budget cannot pay for an effective dose for everyone, reach fewer "
                 "people properly before reaching more people thinly.", "red"),
        ]),

        C("Adapting a model", "Core components and the adaptable periphery", [
            tw([panel("indigo", "Keep (core)", [bullets([
                    "The component that carries the mechanism",
                    "Minimum dosage shown to matter",
                    "Selection rule for the target group",
                    "The feedback loop (assessment, coaching)"], sm=True)])],
               [panel("green", "Adapt (periphery)", [bullets([
                    "Language, examples and materials",
                    "Timing around harvest and festivals",
                    "Which local institution hosts it",
                    "The type of asset or livelihood offered"], sm=True)])]),
            body("The graduation approach was adapted across countries: the asset offered "
                 "varied from livestock to small trade inventory, while the combination of asset, "
                 "consumption support, training and coaching was kept. Document every adaptation "
                 "and the reason for it, so an evaluator can tell what was tested."),
            hbox("If you are unsure whether a component is core, assume it is until a test "
                 "shows otherwise.", "amber"),
        ], compact=True),

        C("Gender in design", "Check every design choice for gendered effects", [
            body("A delivery choice that looks neutral can have different effects for women and "
                 "men. Training scheduled at midday excludes women doing household work. "
                 "Transfers paid into a household head's account usually go to a man. Asset "
                 "transfers of livestock add to women's unpaid work unless fodder and care are "
                 "planned for. Bangladesh's Female Secondary School Stipend programme, introduced "
                 "in 1994, paid the stipend into girls' own bank accounts and conditioned it on "
                 "attendance, marks and remaining unmarried."),
            table(["Design choice", "Gender question"], [
                ["Timing and place of activities", "Can women attend without a male escort or losing wages?"],
                ["Whose name is on the account or asset", "Who controls it in practice?"],
                ["Who is hired as frontline staff", "Will women participants speak to them?"],
                ["What the programme counts", "Does monitoring capture unpaid care work?"],
            ]),
            hbox("See Gender Mainstreaming 101 and Women's Economic Empowerment 101.", "cyan"),
        ], compact=True),

        # ===================== SECTION 06 =====================
        D("06", "Section Six", "Targeting"),

        C("Why target", "Targeting decides who the programme is for", [
            body("Targeting is the set of rules and procedures that decide who receives a "
                 "programme. It is needed when the budget cannot cover everyone, or when the "
                 "intervention only helps people in a particular situation. Every targeting rule "
                 "makes two kinds of mistake, and design is the choice of which mistakes to "
                 "accept, at what administrative cost, and with what effect on the people "
                 "wrongly left out."),
            tw([term("Exclusion error",
                     "An eligible person who does not receive the programme. Often the "
                     "poorest, least documented and least connected people.")],
               [term("Inclusion error",
                     "A person who receives the programme though they do not meet the "
                     "criteria. Visible, politically embarrassing, often less harmful.")]),
            hbox("Governments and auditors tend to focus on inclusion errors because they look "
                 "like leakage. For participants, exclusion errors are usually the larger harm. "
                 "Decide explicitly which you care about more.", "red"),
        ]),

        C("Methods", "Main targeting methods", [
            table(["Method", "How it works", "South Asian example"], [
                ["Categorical", "Everyone in a group is eligible (age, sex, disability)",
                 "Old-age pensions, girls' stipends"],
                ["Geographic", "Everyone in selected areas", "Aspirational Districts Programme"],
                ["Proxy means test", "Score from observable assets predicts consumption",
                 "BISP poverty scorecard, Pakistan"],
                ["Deprivation criteria from a census", "List built from survey indicators",
                 "PM-JAY from SECC 2011"],
                ["Community-based", "Villagers rank or select households",
                 "Participatory wealth ranking in graduation programmes"],
                ["Self-targeting", "Benefit designed so only the needy apply",
                 "Public works paying a low wage for manual labour"],
            ]),
            hbox("Most large programmes combine methods: a geographic filter, then a list, then "
                 "community verification.", "cyan"),
        ], compact=True),

        C("Proxy means tests", "Pakistan's poverty scorecard", [
            body("Pakistan's Benazir Income Support Programme was launched in July 2008. Its "
                 "National Socio-Economic Registry was built through a door-to-door survey "
                 "using a Poverty Score Card based on a proxy means test, covering 27 million "
                 "households in 2010-11, and eligibility was set by a threshold on the score. "
                 "More than 85 per cent of those households were resurveyed in the 2021 update, "
                 "after which three in four beneficiaries came from the bottom two expenditure "
                 "quintiles."),
            tw(pp("green", "Strengths",
                  "Transparent rule, applied the same way everywhere, hard for local elites to "
                  "manipulate case by case, and a registry other programmes can reuse."),
               pp("red", "Weaknesses",
                  "Prediction errors are large near the threshold, the registry ages as "
                  "households' circumstances change, and households cannot easily see why they "
                  "were excluded.")),
            hbox("Source: World Bank, Implementation Completion and Results Report, Pakistan "
                 "National Social Protection Program (P158643), 2022. A registry needs a plan "
                 "and budget for updating, or its errors grow every year.", "amber"),
        ], compact=True),

        C("Community targeting", "Proxy means tests versus community ranking", [
            body("Alatas, Banerjee, Hanna, Olken and Tobias (American Economic Review, 2012) "
                 "ran a field experiment across 640 Indonesian villages comparing a proxy means "
                 "test, community ranking and a hybrid. Measured against consumption, community "
                 "targeting did somewhat worse than the proxy means test, though not by enough "
                 "to change poverty outcomes much for a typical programme. Elite capture did not "
                 "explain the gap. Communities used a different idea of poverty, and they were "
                 "more satisfied with the result."),
            hbox("The study is from Indonesia, and it is the canonical test of this question. "
                 "Its lesson for South Asia: the definition of poverty used by a formula and by "
                 "a village can differ, and legitimacy matters for a programme that has to "
                 "survive local politics.", "indigo"),
            hbox("Where caste or gender hierarchies are strong, community processes need "
                 "safeguards: separate meetings, public reading of lists, and an appeal "
                 "route.", "red"),
        ]),

        C("Old lists", "The problem of ageing lists", [
            body("Many Indian schemes identify beneficiaries from lists compiled years earlier. "
                 "PM-JAY's initial list of about 10.74 crore families came from the "
                 "Socio-Economic Caste Census of 2011, which was already seven years old at "
                 "launch in 2018. Households that became poor after the survey, new households "
                 "formed by marriage or migration, and people missed by the survey are excluded "
                 "until the list is updated."),
            tw(pp("cyan", "Design responses",
                  "A continuous enrolment window, verification of new applicants at the gram "
                  "panchayat or ward, cross-checking with ration card data, and a public "
                  "grievance route."),
               pp("amber", "Costs of those responses",
                  "Each adds administrative work and opportunities for discretion. Budget for "
                  "the staff time and monitor who uses the route.")),
            hbox("When you design within a scheme, ask how its list was built and when. That "
                 "single question often explains who your programme will miss.", "red"),
        ], compact=True),

        C("Documentation barriers", "Eligibility on paper versus access in practice", [
            body("A person can be eligible and still not receive a programme because of the "
                 "steps between eligibility and receipt: documents, a bank account, a working "
                 "mobile number, biometric authentication, travel to a block office, knowing the "
                 "scheme exists. These steps fall hardest on people who are already marginal: "
                 "migrants, people with disabilities, older people, women without documents in "
                 "their own name, homeless people."),
            table(["Step", "Who it tends to exclude", "Design response"], [
                ["Proof of identity and address", "Migrants, people without land records", "Accept alternative documents"],
                ["Bank account and mobile link", "Older people, women in some households", "Camp-based enrolment, assisted linking"],
                ["Biometric authentication", "Manual labourers with worn fingerprints, older people", "Fallback authentication route"],
                ["Travel to an office", "People with disabilities, women with care duties", "Doorstep or village-level service"],
            ]),
        ], compact=True),

        C("Targeting checklist", "Questions to settle before finalising targeting", [
            bullets([
                "<strong>Who exactly</strong> is the programme for, in one sentence, and why that group?",
                "<strong>Which method</strong> or combination identifies them, and how accurate is it likely to be?",
                "<strong>Which error</strong> (exclusion or inclusion) matters more here, and how will each be measured?",
                "<strong>How old</strong> is any list used, and how will new eligible people get in?",
                "<strong>What steps</strong> stand between eligibility and receipt, and who do they exclude?",
                "<strong>How will someone excluded</strong> complain, and who decides the complaint?",
                "<strong>What will targeting cost</strong> per person reached, compared with covering everyone in the area?",
            ]),
            hbox("Sometimes universal coverage within a small area is cheaper and fairer than "
                 "precise targeting, once the cost of identification is counted.", "green"),
        ]),

        # ===================== SECTION 07 =====================
        D("07", "Section Seven", "Theory of change, budget and cost per outcome"),

        C("Theory of change", "The theory of change, briefly", [
            body("A theory of change sets out how the programme's activities are expected to "
                 "lead to its intended outcomes, step by step, and the assumptions that must "
                 "hold at each step. It is the causal argument of the design written as a chain. "
                 "This deck covers it briefly. The Theory of Change 101 deck covers drawing one, "
                 "testing it and using it in evaluation, and the Logframe 101 deck covers turning "
                 "it into a results matrix with indicators."),
            flow(["INPUTS: staff, funds, materials",
                  "ACTIVITIES: training, transfers, sessions",
                  "OUTPUTS: people reached, services delivered",
                  "OUTCOMES: changed practice, use, behaviour",
                  "IMPACT: changed well-being"]),
            hbox("A good theory of change makes it possible to see, at each arrow, what would "
                 "have to be true and how you would know if it was not.", "cyan"),
        ]),

        C("Assumptions", "The assumptions are the design's weak points", [
            body("Between every pair of boxes in a theory of change sits an assumption. Trained "
                 "teachers will use the method. Parents will send children in harvest season. "
                 "The block office will release funds on time. Women will control the asset. "
                 "Designs fail more often at these arrows than in the boxes. List each "
                 "assumption, rate how much evidence supports it, and rate how much damage it "
                 "would do if it were false."),
            table(["Assumption (illustrative)", "Evidence", "If false", "Action"], [
                ["Mentors visit schools fortnightly", "Weak: past vacancy data", "Method fades",
                 "Monitor visits monthly"],
                ["Girls' parents allow cycling", "Good: Bihar evidence", "Low uptake", "Check in pilot"],
                ["Funds released by June", "Mixed: past years late", "Season missed", "Bridge fund"],
            ]),
            hbox("High-damage, weak-evidence assumptions are where monitoring and the pilot "
                 "should focus first.", "red"),
        ], compact=True),

        C("Budget as design", "The budget is part of the argument", [
            body("A budget translates the design into resources. Reviewers read it to check "
                 "whether the plan is serious: whether there are enough staff to deliver the "
                 "dosage, whether monitoring and evaluation are funded, whether participants' "
                 "costs are covered, whether safeguarding has a line. A budget built by "
                 "inflating last year's figures does not test the design. Building it bottom up "
                 "from activities does."),
            tw(pp("cyan", "Bottom-up budgeting",
                  "List every activity in the work plan, the inputs it needs (people, travel, "
                  "materials, venues), the quantity and unit cost of each, and add them. Include "
                  "the costs of coordination, supervision, monitoring and the organisation's "
                  "share of overheads."),
               pp("amber", "Lines often missing",
                  "Participants' travel and lost wages, frontline worker incentives, "
                  "translation, accessibility adjustments, grievance handling, data protection, "
                  "staff turnover and retraining, inflation over a multi-year grant.")),
            hbox("See Fundraising Basics 101 for presenting the budget to funders.", "indigo"),
        ], compact=True),

        C("Cost per outcome", "Divide cost by what the programme changes", [
            body("Cost per output (per training held, per kit distributed) is easy to compute "
                 "and says little about value. Cost per outcome (per child reading, per girl "
                 "enrolled, per household out of extreme poverty) lets the design be compared "
                 "with alternatives. At design stage the effect is an estimate taken from the "
                 "evidence review, so the cost per outcome is a range. Comparing options on that "
                 "range is still far better than comparing them on cost alone."),
            table(["Option (Illustrative)", "Cost per child", "Expected share who learn to read",
                   "Cost per additional reader"], [
                ["A: Level-based camps", "&#8377;1,200", "20 percentage points", "&#8377;6,000"],
                ["B: New textbooks only", "&#8377;400", "2 percentage points", "&#8377;20,000"],
                ["C: Teacher training only", "&#8377;800", "5 percentage points", "&#8377;16,000"],
            ]),
            hbox("Illustrative figures to show the method. The cheapest option per child is the "
                 "most expensive per reader. See Cost Effectiveness 101.", "amber"),
        ], compact=True),

        C("Scale and cost", "Cost per participant changes with scale", [
            {"t": "chart", "canvas": "pdScaleChart",
             "title": "Cost per participant as a programme grows (Illustrative)",
             "source": "Illustrative",
             "type": "line",
             "data": {"labels": ["500", "2k", "10k", "50k", "2 lakh", "10 lakh"],
                      "datasets": [{"label": "Cost per participant (Rs)",
                                    "data": [4200, 2100, 1300, 1050, 980, 1010],
                                    "borderColor": "#0EA5E9",
                                    "backgroundColor": "rgba(14,165,233,0.08)",
                                    "fill": True, "tension": 0.3, "pointRadius": 4}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Rs per participant'} }, x:{ title:{display:true,text:'Participants reached'} } } }"}},
            body("Fixed costs (design, training of trainers, management, software) are spread "
                 "over more people as a programme grows, so cost per participant falls. At very "
                 "large scale it can rise again: harder-to-reach areas, more supervision layers, "
                 "weaker fidelity. A pilot's cost per participant is a poor guide to the cost at "
                 "scale in either direction.", sm=True),
        ], compact=True),

        C("Costing at norms", "Cost the model at the prices the system will pay", [
            body("A design meant for government adoption has to be costed at government norms "
                 "as well as at the NGO's own prices. Honoraria for frontline workers, "
                 "training allowances, travel rates and material costs are fixed in scheme "
                 "guidelines and state orders. If the pilot pays mentors twice the government "
                 "rate, or uses printed materials the department's budget head cannot fund, the "
                 "pilot's results describe a programme the state cannot buy. Build two columns "
                 "in the budget from the start."),
            table(["Budget line (Illustrative)", "NGO pilot cost", "Government norm", "Gap and plan"], [
                ["Mentor monthly pay", "&#8377;25,000", "&#8377;18,000", "Use existing cluster staff"],
                ["Teacher training per day", "&#8377;900", "&#8377;600", "Shorter, school-based sessions"],
                ["Reading kit per school", "&#8377;3,500", "&#8377;2,000", "Simplify kit"],
                ["Assessment per child", "&#8377;60", "No head", "Fold into school tests"],
            ]),
            hbox("Illustrative figures. Look up the actual norms in the relevant scheme "
                 "guidelines and state orders before costing.", "amber"),
        ], compact=True),

        C("Outcome-linked finance", "Paying for results: the Educate Girls bond", [
            body("Some funders now pay for outcomes. In the Educate Girls development impact "
                 "bond in Rajasthan, the UBS Optimus Foundation provided US$270,000 of upfront "
                 "capital, Educate Girls delivered the programme in 166 government schools, an "
                 "independent evaluator measured results, and the Children's Investment Fund "
                 "Foundation repaid the investor according to them. About 80 per cent of "
                 "payments rested on learning gains, measured by a clustered randomised trial, "
                 "and about 20 per cent on enrolling out-of-school girls."),
            stats([
                {"num": "28%", "label": "larger average learning gains than the control group over the bond", "color": "green",
                 "source": "Brookings, Educate Girls DIB Year 3 results, July 2018"},
                {"num": "79%", "label": "more growth in learning than control schools in year three", "color": "cyan",
                 "source": "Brookings, Educate Girls DIB Year 3 results, July 2018"},
                {"num": "15%", "label": "internal rate of return paid to the investor by the outcome funder", "color": "indigo",
                 "source": "Brookings, Educate Girls DIB Year 3 results, July 2018"},
            ]),
            hbox("Outcome contracts need outcomes that can be measured credibly and an "
                 "evaluation budget. They also push effort toward what is measured, so choose "
                 "the metric with care.", "amber"),
        ], compact=True),

        C("Budget compliance", "Rules that shape an Indian programme budget", [
            body("Indian law shapes what a programme budget can contain. Under the Foreign "
                 "Contribution (Regulation) Act 2010, as amended in 2020 with effect from 29 "
                 "September 2020, section 7 prohibits transferring foreign contribution to any "
                 "other person, and section 8(1)(b) caps administrative expenses met from "
                 "foreign contribution at 20 per cent in a financial year unless the Central "
                 "Government approves more. Corporate funding under section 135 of the Companies "
                 "Act 2013 must fall within activities in Schedule VII."),
            tw(pp("red", "Design consequence of FCRA s7",
                  "A foreign-funded Indian NGO cannot pass that money to a community-based "
                  "partner as a sub-grant. Partnership designs built on re-granting foreign "
                  "funds must be restructured, for example as direct funding of each partner."),
               pp("amber", "Design consequence of s8(1)(b)",
                  "Coordination, finance and management costs funded from foreign contribution "
                  "must fit within the cap, so classify budget lines carefully and early.")),
            hbox("As of October 2026: the FCRA Amendment Bill 2026 (introduced 25 March 2026) "
                 "and amended FCRA Rules (22 June 2026) change registration and asset rules, and "
                 "the Government's FCRA FAQ (PIB, 22 July 2026) still states the 20 per cent ceiling "
                 "and the bar on sub-granting. Check the current text before finalising.",
                 "indigo"),
        ], compact=True),

        # ===================== SECTION 08 =====================
        D("08", "Section Eight", "Risk and safeguarding at design stage"),

        C("Risk", "Identify risks before they become problems", [
            body("A risk is something that may happen and would affect the programme or the "
                 "people it touches. At design stage, list risks across several categories, "
                 "rate each for likelihood and impact, and decide a response: avoid it by "
                 "changing the design, reduce it, transfer it (insurance, contract terms), or "
                 "accept and monitor it. The output is a risk register owned by a named person, "
                 "reviewed on a fixed schedule."),
            table(["Category", "Example risk (Illustrative)"], [
                ["Contextual", "Flood or heatwave disrupts the field season"],
                ["Political", "Transfer of a supportive district collector"],
                ["Operational", "Staff turnover above 30 per cent a year"],
                ["Financial", "Delayed release of government co-funding"],
                ["Harm to people", "Abuse of a child by staff or volunteer"],
                ["Data", "Leak of participants' caste or health data"],
                ["Reputational", "Media report of misused funds"],
            ]),
        ], compact=True),

        C("Do no harm", "Design for the harms a programme can cause", [
            body("Programmes can harm the people they aim to help. Cash transfers can raise "
                 "the risk of violence in some households. Microfinance groups can pressure "
                 "members over repayment. Targeting can stigmatise. Volunteers given access to "
                 "children can abuse them. Collecting data on caste, religion, HIV status or "
                 "sexuality can expose people. A design-stage harm assessment asks, for each "
                 "activity, who could be harmed, how, and what would prevent it."),
            tw(pp("red", "Harm pathways",
                  "Power over participants (staff, volunteers, lenders), exposure (data, "
                  "visibility in a list), conflict over resources (who was selected), and "
                  "displacement of existing services."),
               pp("green", "Design mitigations",
                  "Two-adult rules for work with children, confidential reporting routes, "
                  "minimum data collection, transparent selection criteria read out in public, "
                  "and coordination with existing services.")),
            hbox("Harm assessment belongs in the design document, with a budget line. See "
                 "Safeguarding &amp; PSEA 101.", "cyan"),
        ], compact=True),

        C("Child protection law", "Safeguarding obligations under Indian law", [
            body("A programme in India that works with children must be designed around legal "
                 "duties that apply to its staff and leaders. Under section 19 of the Protection "
                 "of Children from Sexual Offences Act 2012, any person who knows or apprehends "
                 "that an offence under the Act has been or is likely to be committed must "
                 "report it to the Special Juvenile Police Unit or the local police. Section 21 "
                 "makes failure to report punishable, with a longer maximum term for a person in "
                 "charge of an institution or company who fails to report about a subordinate."),
            table(["Design element", "Why the law makes it necessary"], [
                ["Written reporting procedure naming who reports to police", "Reporting is a personal legal duty"],
                ["Training for all staff and volunteers before contact with children", "Everyone is covered by s19"],
                ["Senior officer responsible for safeguarding", "Heads of institutions face higher liability under s21"],
                ["Vetting and code of conduct for anyone with access to children", "Prevention reduces harm and liability"],
            ]),
        ], compact=True),

        C("PSEA", "Preventing sexual exploitation and abuse", [
            body("Protection from sexual exploitation and abuse (PSEA) addresses the risk that "
                 "staff, volunteers or contractors use their position over participants, who "
                 "often depend on them for a benefit. The risk is highest where staff decide who "
                 "receives something of value: selection for a scheme, a loan, relief goods, a "
                 "job. Design can reduce it by removing single points of discretion, publishing "
                 "criteria, and making sure participants know that the benefit is free and how "
                 "to report abuse."),
            tw(pp("indigo", "At workplace level",
                  "The Sexual Harassment of Women at Workplace (Prevention, Prohibition and "
                  "Redressal) Act 2013 requires every employer of a workplace to constitute an "
                  "Internal Committee (section 4). Where an establishment has fewer than ten "
                  "workers, the district Local Committee hears complaints (section 6)."),
               pp("cyan", "At community level",
                  "Community feedback and complaints mechanisms, female staff available for "
                  "women participants, and a commitment that a complaint will not cost the "
                  "complainant her benefit.")),
            hbox("Labour law also matters: the four Labour Codes came into force on 21 November "
                 "2025 and apply to programme staff contracts.", "amber"),
        ], compact=True),

        C("Data protection", "Personal data in programme design", [
            body("Programmes collect personal data: names, phone numbers, Aadhaar numbers, "
                 "health status, caste, photographs. The Digital Personal Data Protection Act "
                 "2023 and the DPDP Rules 2025 impose their duties from 13 May 2027, so a programme "
                 "running past that date has to design data collection now with a lawful basis, "
                 "notice, purpose limitation and security. From the same date section 17(2)(b) exempts processing for research, archiving or statistical "
                 "purposes when its conditions are met, which helps evaluation but does not "
                 "cover routine programme operations."),
            table(["Design question", "Good practice"], [
                ["What data do we need for delivery?", "Collect only fields someone will use"],
                ["Who can see it?", "Role-based access, no shared logins"],
                ["How is consent or notice given?", "In the participant's language, read aloud where needed"],
                ["How long is it kept?", "Retention period set in the design"],
                ["What if it leaks?", "Breach procedure and named owner"],
            ]),
            hbox("See Data Protection &amp; the DPDP Act 101.", "cyan"),
        ], compact=True),

        C("Grievance redress", "Design the complaint route at the start", [
            body("Every programme needs a way for participants and non-participants to complain "
                 "and get an answer: about being excluded, about staff behaviour, about money "
                 "not received. A grievance mechanism designed at the start is cheaper than one "
                 "bolted on after a scandal. It should be accessible (free, local, in the local "
                 "language, usable by people who cannot read), safe (confidential, with no "
                 "retaliation), and answered within a stated time."),
            flow(["RECEIVE: helpline, box, field visit, WhatsApp",
                  "RECORD: logged with date and category",
                  "RESOLVE: named person, deadline",
                  "RESPOND: answer to complainant",
                  "REVIEW: patterns reported to management"]),
            hbox("Count complaints by type every month. A programme with no complaints usually "
                 "has an inaccessible mechanism.", "amber"),
        ]),

        C("Risk register", "A design-stage risk register", [
            table(["Risk (Illustrative)", "Likelihood", "Impact", "Response", "Owner"], [
                ["Staff abuse of a child participant", "Low", "Severe",
                 "Vetting, two-adult rule, POCSO training, reporting procedure", "Safeguarding lead"],
                ["Government funds released late", "High", "Medium",
                 "Bridge fund, phased plan", "Finance head"],
                ["Elite capture of selection", "Medium", "High",
                 "Public reading of lists, appeal route", "Programme manager"],
                ["Data breach of participant records", "Medium", "High",
                 "Access controls, minimum data", "Data officer"],
                ["Extreme heat stops summer activities", "High", "Medium",
                 "Reschedule to mornings, shade, water", "Field coordinator"],
            ]),
            hbox("Severe-impact risks need a response even when unlikely. Review the register "
                 "quarterly and after any incident.", "red"),
        ], compact=True),

        # ===================== SECTION 09 =====================
        D("09", "Section Nine", "Implementation planning and adaptive management"),

        C("Implementation plan", "What an implementation plan contains", [
            body("The implementation plan converts the design into a sequence of work. It sets "
                 "out the phases (preparation, pilot, expansion, consolidation), the activities "
                 "in each, who is responsible, the resources needed and the dependencies between "
                 "them. In South Asia, it also has to fit the calendar: agricultural seasons, "
                 "monsoon, school terms, festivals, examination months, the government financial "
                 "year from April to March, and the model code of conduct before elections."),
            table(["Component", "Content"], [
                ["Phasing", "Pilot, review point, expansion in waves"],
                ["Staffing plan", "Roles, numbers, hiring dates, training"],
                ["Procurement", "What is bought, when, with what lead time"],
                ["Calendar", "Seasons, school year, financial year, elections"],
                ["Monitoring plan", "Indicators, frequency, who uses them"],
                ["Decision points", "When the team will decide to continue, adapt or stop"],
            ]),
        ], compact=True),

        C("Staffing", "Staffing and supervision decide fidelity", [
            body("Fidelity, the degree to which the programme is delivered as designed, falls "
                 "as programmes grow, mostly because supervision gets thinner. Plan the ratio of "
                 "supervisors to frontline staff, how often supervisors visit, what they check, "
                 "and what support they give. Plan for turnover: in many NGO field teams a "
                 "sizeable share of staff leave each year, and every departure takes training "
                 "and relationships with it."),
            tw(pp("cyan", "Supervision that works",
                  "Regular visits with a short structured checklist, observation of actual "
                  "delivery, on-the-spot coaching, and data that the supervisor and worker "
                  "review together."),
               pp("red", "Supervision that does not",
                  "Monthly meetings at the block office that review registers, visits that "
                  "check paperwork only, and targets without support.")),
            hbox("Budget for refresher training and for training replacements. A one-time "
                 "training budget assumes no one ever leaves.", "amber"),
        ], compact=True),

        C("Pilots", "What a pilot is for", [
            body("A pilot tests whether the design can be delivered and whether its riskiest "
                 "assumptions hold, before money is committed at scale. It should be run under "
                 "conditions close to those at scale: with the staff, partners and budget per "
                 "participant that would be used later. A pilot run by the best staff, with "
                 "extra funding and close attention from the founders, will look better than the "
                 "programme can be."),
            tw(pp("green", "A useful pilot",
                  "Has written questions it must answer, decision rules agreed in advance, "
                  "monitoring of the key assumptions, cost data collected throughout, and a "
                  "review date."),
               pp("red", "A pilot that misleads",
                  "Has no stated questions, is run in the most favourable villages, is never "
                  "costed, and becomes the next phase automatically.")),
            hbox("Decide before the pilot what result would make you change the design or "
                 "stop. Deciding afterwards invites reading every result as success.", "indigo"),
        ], compact=True),

        C("Monitoring for management", "Monitoring that managers use", [
            body("Monitoring data in many programmes flows upward for reports and is rarely "
                 "used by the people who could act on it. Design the monitoring system around "
                 "decisions: which decisions will managers and field staff make each month, and "
                 "what information do they need for each? A short list of indicators that are "
                 "checked and acted on is worth more than a long list that fills a dashboard "
                 "nobody opens."),
            table(["Decision", "Information needed", "Frequency"], [
                ["Which villages need a supervisor visit?", "Attendance and session completion by village", "Weekly"],
                ["Is the dosage being delivered?", "Sessions per participant against plan", "Monthly"],
                ["Are we reaching the target group?", "Share of participants meeting criteria", "Quarterly"],
                ["Is the key assumption holding?", "Indicator for that assumption", "Monthly"],
            ]),
            hbox("See MEL Basics 101 for building the full monitoring, evaluation and learning "
                 "system.", "cyan"),
        ], compact=True),

        C("Adaptive management", "Planning to change the plan", [
            body("Adaptive management means deliberately adjusting a programme in response to "
                 "what monitoring and learning show, within agreed limits. Andrews, Pritchett "
                 "and Woolcock (World Development, 2013) proposed Problem-Driven Iterative "
                 "Adaptation: solving locally nominated and prioritised problems, encouraging "
                 "positive deviance and experimentation, creating feedback loops for rapid "
                 "learning, and engaging many agents. Its practical message for design is to build "
                 "learning cycles and authority to change into the plan from the start."),
            flow(["PLAN: a small change to test",
                  "DO: run it in a few places",
                  "CHECK: look at the data quickly",
                  "ACT: keep, change or drop"]),
            hbox("Adaptation needs permission. Agree with the funder in advance which changes "
                 "the team can make on its own and which need approval.", "amber"),
        ]),

        C("Funder agreements", "Write flexibility into the grant", [
            body("Many grants fix activities, targets and budget lines for three years, which "
                 "makes adaptation a compliance problem. At design stage, negotiate the terms "
                 "that allow learning: outcome-level targets with flexibility on activities, a "
                 "budget reallocation threshold (for example up to 10 or 15 per cent between "
                 "lines without prior approval, Illustrative), scheduled review points, and a "
                 "learning budget for small tests."),
            tw(pp("indigo", "Ask for",
                  "Annual work plans approved under a multi-year design, a reallocation "
                  "threshold, a contingency line, and agreement that a documented "
                  "adaptation is reported as learning."),
               pp("cyan", "Offer in return",
                  "Clear monitoring of the key assumptions, quarterly learning notes, and early "
                  "warning when results fall short.")),
            hbox("Funders who have seen a rigid grant fail are often open to this. Ask "
                 "explicitly. See Fundraising Basics 101.", "green"),
        ], compact=True),

        C("Exit and handover", "Plan the end at the beginning", [
            body("Every programme ends, or changes hands. The design should say what happens "
                 "then: whether the activity continues through government, a community "
                 "institution or a market, or whether the programme is time-limited by design, "
                 "as graduation programmes are. Exit planning shapes design choices from the "
                 "start. A programme that intends handover to the education department should "
                 "use the department's staff, schedules and cost norms from the pilot onward."),
            table(["Exit route", "Design requirement"], [
                ["Government takes over", "Use government staff, norms and budget heads from the start"],
                ["Community institution continues", "Build its finances and governance, plan reduced support"],
                ["Time-limited by design", "Show that outcomes persist after support ends"],
                ["Market continues", "Test that participants will pay at a viable price"],
            ]),
            hbox("Write the exit route into the theory of change as an outcome with its own "
                 "indicators.", "amber"),
        ], compact=True),

        # ===================== SECTION 10 =====================
        D("10", "Section Ten", "Government partnership and design for scale"),

        C("Why government", "Most programmes reach scale through the state", [
            body("In India, Pakistan, Bangladesh, Nepal and Sri Lanka the state runs the "
                 "schools, health systems, social protection and rural employment programmes "
                 "that reach most poor households. An NGO programme that reaches a few thousand "
                 "people is valuable mainly if it changes what those systems do. Designing with "
                 "government in mind from the start changes many design choices, compared with "
                 "hoping for adoption after a successful pilot."),
            tw(pp("cyan", "What government offers",
                  "Reach, permanence, legal mandate, frontline staff in every village, budget "
                  "lines that renew each year."),
               pp("amber", "What government constrains",
                  "Fixed cost norms, procurement rules, transfers of officers, competing "
                  "priorities, limited room to test and fail.")),
            hbox("Aim to change a scheme's design, guidelines or delivery practice. That has "
                 "more reach than a parallel programme of any size.", "green"),
        ], compact=True),

        C("Working within schemes", "Designing within a state scheme: rural employment", [
            body("Rural employment in India now runs under the Viksit Bharat Guarantee for "
                 "Rozgar and Ajeevika Mission (Gramin) Act 2025, which replaced MGNREGA from 1 "
                 "July 2026. According to the Government of India's backgrounder (PIB, December "
                 "2025), it guarantees 125 days of wage employment per financial year to rural "
                 "households whose adults volunteer for unskilled manual work, is planned "
                 "through Viksit Gram Panchayat Plans, lets states pause works for up to 60 days "
                 "at peak sowing and harvest, and gives each state a normative allocation, with "
                 "spending beyond it borne by the state."),
            table(["Scheme feature", "What it means for an NGO design"], [
                ["Panchayat-level plans", "Support gram sabhas to put useful works in the plan"],
                ["Normative allocation", "Central funds per state are capped; districts compete for them"],
                ["60-day seasonal pause", "Schedule complementary activities around it"],
                ["Social audit and disclosure", "Build community capacity to use the records"],
            ]),
        ], compact=True),

        C("Partnership models", "Ways to work with government", [
            table(["Model", "Description", "Example"], [
                ["Technical support", "NGO advises a department on design or training",
                 "Pratham with state education departments on TaRL"],
                ["Embedded implementation", "NGO staff work inside a government programme",
                 "Support units in state livelihood missions"],
                ["Government adopts a model", "State scales an NGO-tested approach",
                 "Bihar's JEEViKA, then NRLM nationally"],
                ["Contracted delivery", "Government pays NGO to deliver a service",
                 "Outsourced services in some states"],
                ["Joint evaluation", "Government and researchers test a policy change",
                 "Large-scale trials in partnership with states"],
            ]),
            hbox("Each model needs a formal agreement, usually a memorandum of understanding, "
                 "that sets roles, data sharing, branding and exit.", "indigo"),
        ], compact=True),

        C("JEEViKA to NRLM", "From a state project to a national mission", [
            body("JEEViKA began in 2007 as the World Bank supported Bihar Rural Livelihoods "
                 "Project in 42 blocks of six high-poverty districts, mobilising women into "
                 "self-help groups, village organisations and cluster-level federations. The "
                 "World Bank's completion report (2017) records that the National Rural "
                 "Livelihoods Mission, designed in 2010, was to a large degree based on the "
                 "Bihar model and on other World Bank supported livelihood projects. Bihar's "
                 "own design had drawn on Andhra Pradesh's experience of building local "
                 "institutions."),
            tw(pp("green", "Design lessons",
                  "The project was implemented by the Bihar Rural Livelihoods Promotion "
                  "Society, an autonomous society registered for the purpose. It saturated its "
                  "first blocks and then expanded in phases, to 102 blocks in the same six "
                  "districts."),
               pp("amber", "Open questions",
                  "Quality of federations at national scale, dependence on bank credit, and "
                  "whether the poorest households join and stay.")),
            hbox("Source: World Bank, Implementation Completion and Results Report, Bihar Rural "
                 "Livelihoods Project (P090764), April 2017.", "cyan"),
        ], compact=True),

        C("Design for scale", "Design for scale from the start", [
            body("The WHO and ExpandNet guide <em>Nine steps for developing a scaling-up "
                 "strategy</em> (2010) distinguishes horizontal scaling up (expansion and "
                 "replication to new places and people) from vertical scaling up "
                 "(institutionalisation through policy, budgets and legal change). It asks "
                 "designers to plan actions that increase scalability from the start, using "
                 "its CORRECT checklist: credible, observable, relevant, relative advantage, "
                 "easy to install, compatible with the user organisation, and testable."),
            tw(pp("cyan", "Horizontal",
                  "More districts, more participants. Needs a delivery model that can be "
                  "replicated without the founders, standard training and materials, and a "
                  "cost per participant the system can afford."),
               pp("indigo", "Vertical",
                  "Changes in guidelines, budget heads, curricula, job descriptions or law. "
                  "Needs policy allies, evidence in a form officials use, and patience.")),
            hbox("A design that needs a rare kind of staff, an expensive input or a charismatic "
                 "leader will not scale. Remove those dependencies early.", "red"),
        ], compact=True),

        C("Voltage drop", "Why effects shrink at scale", [
            body("Effects found in pilots often shrink when programmes grow. Bold, Kimenyi, "
                 "Mwabu, Ng'ang'a and Sandefur (Journal of Public Economics, 2018) studied "
                 "contract teachers in Kenya: teachers hired on a fixed-term contract by an NGO "
                 "raised test scores, while teachers on identical contracts hired by the "
                 "government produced no effect. The authors trace the gap to implementation "
                 "constraints and political economy forces set in motion as the programme went "
                 "to scale."),
            table(["Cause of shrinking effects", "Design response"], [
                ["Weaker implementer at scale", "Pilot through the implementer who will scale it"],
                ["Political opposition from affected groups", "Political economy analysis, early engagement"],
                ["Thinner supervision and lower fidelity", "Plan supervision ratios and core components"],
                ["Different population at scale", "Test in typical sites"],
                ["General equilibrium effects", "Measure spillovers on non-participants"],
            ]),
            hbox("The Kenyan study is the canonical example. The Udaipur nurse study shows the "
                 "same pattern in Rajasthan.", "amber"),
        ], compact=True),

        C("Testing at scale", "Evaluating in government systems", [
            body("Muralidharan and Niehaus (Journal of Economic Perspectives, 2017) argue for "
                 "experimentation at scale: larger sampling frames, more treated units and "
                 "larger units of randomisation, run through the systems that would deliver the "
                 "policy. Evaluating inside the government system answers the question a "
                 "policymaker asks: what will happen if the state itself does this, across "
                 "whole districts, with its own staff and budgets."),
            tw(pp("green", "Design implications",
                  "Plan the evaluation with the department. Randomise at block or district "
                  "level where spillovers matter. Use administrative data where it is "
                  "reliable. Agree in advance how results will be used."),
               pp("cyan", "Ethics and law",
                  "Review by an ethics committee, informed consent where required, and data "
                  "handling under the DPDP Act. See Research Ethics 101.")),
            hbox("See Impact Evaluation 101 and Causal Inference 101 for evaluation design.",
                 "indigo"),
        ], compact=True),

        # ===================== SECTION 11 =====================
        D("11", "Section Eleven", "Practical application"),

        C("Worked example", "Worked example: the problem (Illustrative)", [
            body("An NGO in a district of eastern Uttar Pradesh is asked by a CSR funder to "
                 "design a three-year programme to improve reading in government primary "
                 "schools. This example is Illustrative, with hypothetical figures, and used to walk through the design "
                 "steps. The team first gathers data: an assessment in 40 schools finds most "
                 "Class 3 to 5 children below Class 2 reading level, teacher vacancies in about "
                 "a fifth of schools, and sharp attendance drops in the wheat harvest."),
            table(["Step", "What the team decided"], [
                ["Problem statement", "Most Class 3-5 children in 4 blocks cannot read a Class 2 text"],
                ["Main causes", "Instruction at grade level; seasonal absence; vacancies"],
                ["Causes in scope", "Instruction; partly attendance"],
                ["Out of scope", "Vacancies (state department), noted as an assumption"],
                ["Stakeholders", "Block education officer, cluster resource persons, headteachers, SMCs, parents"],
            ]),
            hbox("Each decision is written down with its reason, so the funder can see what "
                 "was left out and why.", "cyan"),
        ], compact=True),

        C("Worked example", "Worked example: options and choice (Illustrative)", [
            body("The evidence review points to level-based instruction (TaRL), with two "
                 "delivery models: camps run by NGO instructors and a government model with teachers "
                 "supported by mentors. The team compares three options, with costs taken from "
                 "budget estimates and effects from published evaluations adjusted down for "
                 "expected fidelity loss."),
            table(["Option (Illustrative)", "Delivery", "Fit with scale", "Decision"], [
                ["A. NGO-run learning camps", "Pratham-style camps run by NGO instructors",
                 "Low: parallel to school", "Rejected for main design"],
                ["B. Government teacher model", "Teachers trained, cluster mentors support",
                 "High: uses department staff", "Chosen"],
                ["C. Books and libraries only", "Supply reading material", "Medium", "Kept as add-on"],
            ]),
            hbox("Option B is chosen because the funder and district want a model the "
                 "department can continue after three years. The team accepts lower fidelity "
                 "and plans mentoring to protect it.", "green"),
        ], compact=True),

        C("Worked example", "Worked example: targeting, budget and risks (Illustrative)", [
            tw([panel("cyan", "Targeting", [body(
                    "All government primary schools in four blocks (geographic). Within schools, "
                    "every child in Classes 3 to 5 is assessed and grouped by level. No household "
                    "list is needed, so no exclusion through documents.", sm=True)]),
                panel("indigo", "Budget logic", [body(
                    "Bottom-up from training days, mentor salaries, materials, assessment, "
                    "monitoring, evaluation and a safeguarding line. Cost per child and estimated "
                    "cost per additional reader computed for each year.", sm=True)])],
               [panel("red", "Top risks", [body(
                    "Mentors pulled into other duties; teacher transfers mid-year; schools "
                    "closed for elections or heat; child protection risk from adult volunteers "
                    "used in assessments.", sm=True)]),
                panel("green", "Responses", [body(
                    "Written agreement with the district on mentor time; refresher training each "
                    "term; schedule around the school calendar; POCSO-compliant procedure and "
                    "two-adult rule.", sm=True)])]),
            hbox("Illustrative example. A real design would attach the full budget and risk "
                 "register as annexes.", "amber"),
        ], compact=True),

        C("Worked example", "Worked example: implementation and learning (Illustrative)", [
            body("The plan has three phases. In year one the model runs in one block with "
                 "monthly review of three indicators: share of scheduled level-based sessions "
                 "held, mentor visits per school, and the share of children moving up a reading "
                 "level each term. A decision point at the end of year one uses agreed rules. "
                 "Years two and three expand to the other blocks if the rules are met, with a "
                 "district-level evaluation designed with the education department."),
            table(["Indicator", "Decision rule at end of year one (Illustrative)"], [
                ["Sessions held as scheduled", "Below 60%: redesign timetable with headteachers"],
                ["Mentor visits per school per month", "Below 1: renegotiate mentor time with district"],
                ["Children moving up a level per term", "Below 15%: review teaching practice before expansion"],
                ["Cost per child against budget", "Over 20% above: simplify materials or training"],
            ]),
            hbox("Rules agreed in advance turn monitoring into decisions. Without them, every "
                 "result is read as a reason to continue.", "indigo"),
        ], compact=True),

        C("Design checklist", "A programme design checklist, part one", [
            tw([panel("cyan", "Problem and people", [bullets([
                    "Problem stated without naming a solution",
                    "Size and location of the problem shown with dated sources",
                    "Root causes identified and checked against data",
                    "Affected people, including marginal groups, consulted",
                    "Causes in and out of scope stated"], sm=True)])],
               [panel("indigo", "Stakeholders and evidence", [bullets([
                    "Stakeholder and power map, including those who lose",
                    "Political economy risks named",
                    "Frontline workers' workload considered",
                    "Evidence review with sources, including null results",
                    "Mechanism of the chosen intervention stated"], sm=True)])]),
            hbox("Use this list to review your own design or a proposal you are asked to "
                 "appraise. Any unticked item is a question to ask the team.", "green"),
        ], compact=True),

        C("Design checklist", "A programme design checklist, part two", [
            tw([panel("green", "Intervention and targeting", [bullets([
                    "At least three options compared on stated criteria",
                    "Cash benchmark considered",
                    "Delivery model is the one you would use at scale",
                    "Dosage set by what the mechanism needs",
                    "Targeting method, errors and grievance route defined"], sm=True)])],
               [panel("amber", "Plan, risk and scale", [bullets([
                    "Theory of change with rated assumptions",
                    "Bottom-up budget with cost per outcome range",
                    "Risk register, safeguarding and data protection lines",
                    "Pilot questions and decision rules agreed in advance",
                    "Exit route and path to government or scale"], sm=True)])]),
            hbox("A design that ticks every item can still fail. One that ticks few has "
                 "usually not been thought through.", "amber"),
        ], compact=True),

        C("Appraising a proposal", "Questions to ask when reviewing someone else's design", [
            table(["Question", "What a weak answer looks like"], [
                ["What problem, for whom, and how do you know?", "General statements with no data or dates"],
                ["Why this intervention over others?", "No alternatives considered"],
                ["What evidence supports it, and in what setting?", "Evidence from a different mechanism"],
                ["Who exactly will receive it, and who might be missed?", "'All poor households'"],
                ["What is the cost per outcome?", "Only cost per output or per participant"],
                ["What are the riskiest assumptions?", "None listed, or all rated low"],
                ["Who will run this after the grant?", "'The community will take over'"],
            ]),
            hbox("Funders, government reviewers and CSR committees can use these questions "
                 "directly. Ask for written answers.", "cyan"),
        ], compact=True),

        # ===================== SECTION 12 =====================
        D("12", "Section Twelve", "Common design failures"),

        C("Failure patterns", "Failures that recur across South Asian programmes", [
            table(["Failure", "What it looks like", "Prevention"], [
                ["Solution first", "Programme designed around a favoured intervention", "Problem analysis before options"],
                ["Wrong cause", "Acting on a cause that is not binding here", "Check causes against data"],
                ["Ignored incentives", "Officials or staff quietly undermine it", "Political economy analysis"],
                ["Thin dosage", "Budget spread too widely to work", "Reach fewer people properly"],
                ["Pilot-only conditions", "Works with founders, fails at scale", "Pilot with the scaling implementer"],
                ["Exclusion by design", "Paperwork or channels shut out the poorest", "Map steps to receipt"],
                ["No learning loop", "Problems found at the final evaluation", "Decision rules and monitoring"],
            ]),
            hbox("Most of these are visible in the design document if someone asks the right "
                 "question before the grant is signed.", "red"),
        ], compact=True),

        C("Incentives ignored", "Failure case: when the enforcers opt out", [
            body("The Udaipur nurse attendance programme is a design failure in a precise "
                 "sense. The intervention changed nurses' incentives through monitoring and pay "
                 "deductions, and in the first months attendance rose by 15 to 29 percentage "
                 "points according to J-PAL's summary. The design relied on the local health "
                 "administration to enforce deductions, and that administration had its own "
                 "reasons not to. Monitoring machines were damaged and absences were excused."),
            tw(pp("red", "What the design assumed",
                  "That the administration wanted higher attendance enough to impose penalties "
                  "on its own staff, and would keep doing so."),
               pp("green", "What a design could add",
                  "Analysis of the enforcers' incentives, an enforcement channel outside the "
                  "local hierarchy, and early monitoring of whether penalties were actually "
                  "applied.")),
            hbox("Ask of every rule in a design: who enforces it, and what do they gain or "
                 "lose by doing so?", "amber"),
        ], compact=True),

        C("Over-promising", "Failure case: claiming more than the mechanism can deliver", [
            body("For years microcredit was presented as a route out of poverty for poor "
                 "women. The Hyderabad evaluation found more business investment and higher "
                 "profits among businesses that already existed, and no significant rise in "
                 "average consumption. Programme designs that promised poverty "
                 "reduction through credit alone set targets the mechanism could not reach, and "
                 "monitoring systems counted loans disbursed and repayment rates, which said "
                 "nothing about well-being."),
            tw(pp("indigo", "Design lesson",
                  "State outcomes the mechanism can plausibly change, and measure them. For "
                  "credit, that may be smoother consumption or business investment, with "
                  "poverty reduction as an uncertain longer-term effect."),
               pp("cyan", "Monitoring lesson",
                  "Repayment rates measure the lender's success. Add measures of borrowers' "
                  "well-being and over-indebtedness.")),
            hbox("Promises in a proposal become targets in the grant agreement. Promise what "
                 "the evidence supports.", "red"),
        ], compact=True),

        C("Parallel systems", "Failure case: building beside the state", [
            body("A frequent failure in South Asia is the parallel programme: an NGO or donor "
                 "project that hires its own workers, runs its own registers and reporting, and "
                 "pays incentives the government cannot match. It can show strong results "
                 "while funded. When funding ends, nothing in the government system has changed, "
                 "frontline workers have been drawn away from routine tasks, and the community "
                 "has learned that services arrive and disappear with projects."),
            tw(pp("red", "Warning signs",
                  "Project staff paid far above government scales, separate data systems with "
                  "no link to government MIS, branding that hides the department's role, and an "
                  "exit plan that says 'advocacy for adoption'."),
               pp("green", "Alternatives",
                  "Work through government staff with added support, use government data "
                  "systems, cost the model at government norms, and agree a handover timeline "
                  "with the department from the start.")),
            hbox("JEEViKA was implemented from 2007 by a society registered for the purpose, "
                 "and the World Bank's 2017 completion report records that the national "
                 "livelihoods mission was designed largely on its model.", "cyan"),
        ], compact=True),

        C("Pre-mortem", "A pre-mortem: imagine the programme has failed", [
            body("A pre-mortem is a short exercise run before the design is finalised. The team "
                 "is told to imagine that three years have passed and the programme has failed "
                 "badly. Each person writes down, independently, the most likely reasons. The "
                 "reasons are then pooled, grouped and checked against the design: is each one "
                 "addressed in the risk register, the assumptions, the monitoring plan or the "
                 "budget? The exercise surfaces doubts that people hesitate to raise in a "
                 "planning meeting."),
            tw(pp("cyan", "How to run it",
                  "Ninety minutes. Include field staff, a finance person, a government "
                  "counterpart if possible and someone from the participant community. Collect "
                  "reasons in writing before discussion, so senior voices do not set the "
                  "agenda."),
               pp("green", "What to do with the output",
                  "Add new risks to the register, new assumptions to the theory of change, and "
                  "new indicators to the monitoring plan. Change the design where a reason "
                  "points to a flaw that can be fixed now.")),
            hbox("Typical pre-mortem reasons in South Asian programmes: a supportive officer "
                 "transferred, funds released late, frontline workers overloaded, the poorest "
                 "households never enrolled.", "amber"),
        ], compact=True),

        C("Summary", "Ten principles of programme design", [
            tw([panel("cyan", "Before choosing", [bullets([
                    "Define the problem before the solution",
                    "Check causes against data and local voices",
                    "Map power, including who loses",
                    "Review evidence, including null results",
                    "Understand the mechanism you are copying"], sm=True)])],
               [panel("green", "When choosing and planning", [bullets([
                    "Compare options, including cash, on cost per outcome",
                    "Design the targeting errors you can accept",
                    "Name and monitor the riskiest assumptions",
                    "Budget for safeguarding, data protection and learning",
                    "Pilot with the system that will scale it"], sm=True)])]),
            hbox("Each principle corresponds to a section of this course. Return to that "
                 "section when a design review raises a question.", "indigo"),
        ], compact=True),

        C("Where next", "Where next: related 101 decks", [
            tw([panel("cyan", "Design and results", [body(
                    "<a href=\"/101-courses/toc-workbench.html\">Theory of Change 101</a> for "
                    "building and testing the causal chain. "
                    "<a href=\"/101-courses/logframe-101.html\">Logframe 101</a> for the "
                    "results matrix and indicators. "
                    "<a href=\"/101-courses/mel-basics.html\">MEL Basics 101</a> for monitoring, "
                    "evaluation and learning systems. "
                    "<a href=\"/101-courses/cost-effectiveness.html\">Cost Effectiveness 101</a> "
                    "for comparing options on cost per outcome.", sm=True)])],
               [panel("green", "Money, people and evidence", [body(
                    "<a href=\"/101-courses/fundraising-basics.html\">Fundraising Basics 101</a> "
                    "for budgets and funder relationships. "
                    "<a href=\"/101-courses/safeguarding-psea.html\">Safeguarding &amp; PSEA "
                    "101</a> for protection at design stage. "
                    "<a href=\"/101-courses/impact-eval.html\">Impact Evaluation 101</a> and "
                    "<a href=\"/101-courses/participatory-methods.html\">Participatory Methods "
                    "101</a> for evaluating and co-designing. "
                    "<a href=\"/101-courses/pol-economy.html\">Political Economy 101</a> for "
                    "power and incentives.", sm=True)])]),
            hbox("Suggested order: Theory of Change, Logframe, MEL Basics, then Cost "
                 "Effectiveness. Read Safeguarding &amp; PSEA before any programme that works "
                 "with children or vulnerable adults.", "indigo"),
        ], compact=True),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Programme Design 101",
         "headline": "Design the problem, the people and the plan before the money moves",
         "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development "
                   "practitioners in South Asia",
         "ctas": [{"label": "Theory of Change 101", "href": "/101-courses/toc-workbench.html"},
                  {"label": "All 101 courses", "href": "/101-courses/"}],
         "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]},
    ],
}

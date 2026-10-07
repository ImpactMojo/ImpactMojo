# -*- coding: utf-8 -*-
"""
Gender & Development 101 - ImpactMojo 101 Series (native deck spec)
The field of gender and development for South Asian practitioners: concepts,
household bargaining, missing women, work and its measurement, unpaid care,
education and health, violence and the law, representation, masculinities,
intersectionality and gender analysis tools.
Build: python3 scripts/deck-builder/build.py gender_dev

Sources opened while writing (October 2026) are listed on the slides
themselves. Figures marked Illustrative are teaching examples.
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


def card(num, label, color, source):
    return {"num": num, "label": label, "color": color, "source": source}


def quote(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


NFHS = "NFHS-5 India Report, IIPS and ICF, 2022"
PLFS25 = "PLFS Annual Report 2025, NSO, MoSPI, March 2026"
TUS24 = "Time Use Survey 2024, NSO, MoSPI, February 2025"

DECK = {
    "slug": "gender-dev",
    "title": "Gender &amp; Development 101",
    "description": ("Gender & Development 101: a free foundational course for development "
                    "practitioners in South Asia. Sex and gender; WID, WAD and GAD; Moser's "
                    "practical and strategic gender needs; Kabeer's resources, agency and "
                    "achievements; household bargaining and land; missing women and sex ratios; "
                    "women's work and its measurement in PLFS; unpaid care in the Time Use "
                    "Survey; education and health gaps; violence against women and the PWDVA "
                    "and POSH Acts; political representation from panchayats to the Nari Shakti "
                    "Vandan Adhiniyam; masculinities; caste, religion and intersectionality; "
                    "gender analysis tools. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Gender &amp;<br>Development<br>101",
         "sub": "How gender shapes who gets what in development, and how a practitioner in "
                "South Asia can see it, measure it and design around it",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Gender Analysis"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Sex, gender and why development cares"},
             {"name": "From WID to GAD: the ideas"},
             {"name": "Inside the household: bargaining and land"},
             {"name": "Missing women, son preference and sex ratios"},
             {"name": "Women's work and how it is measured"},
             {"name": "Unpaid care and time use"},
             {"name": "Education and health gaps"},
             {"name": "Violence against women: data and law"},
             {"name": "Political representation"},
             {"name": "Masculinities and intersectionality"},
             {"name": "Practical application: gender analysis"},
             {"name": "Bringing it together"},
         ]},

        # ===================== SECTION 01 =====================
        D("01", "Section One", "Sex, gender and why development cares"),

        C("Definitions", "Sex and gender are different questions", [
            tw(pp("cyan", "Sex",
                  "Sex refers to biological characteristics: chromosomes, hormones and "
                  "reproductive anatomy. Surveys usually record it as female, male and, "
                  "increasingly, a third category. Sex explains why only women can be "
                  "pregnant, and so why maternal health needs its own services."),
               pp("green", "Gender",
                  "Gender refers to the roles, rules, expectations and power that a society "
                  "attaches to being a woman or a man. It explains why a girl in one district "
                  "fetches water while her brother studies, and why that pattern differs in "
                  "the next state. Gender is learned, varies across places and changes over "
                  "time.")),
            term("Gender relations",
                 "The socially constructed relations of power between women and men, and "
                 "among women and among men, that shape access to resources, labour, "
                 "decision-making and voice in households, markets, communities and the "
                 "state."),
            hbox("A practitioner asks two questions of any programme: which differences are "
                 "biological and need specific services, and which are social and can be "
                 "changed by the programme or the policy around it."),
        ], compact=True),

        C("Why it matters", "Gender changes who benefits from the same programme", [
            body("A development programme distributes something: money, land, credit, "
                 "training, water, seeds, information. Gender decides who in a household "
                 "receives it, who controls it afterwards, who does the extra work it "
                 "creates and who is consulted about it. Two programmes with the same budget "
                 "can have opposite effects on women depending on whose name is on the "
                 "title, whose phone receives the message and what time the meeting is "
                 "held."),
            tw(pp("cyan", "Example: a dairy cooperative",
                  "Women in many South Asian villages do most of the milking and feeding. If "
                  "membership and payment go to the household head, the income goes to men "
                  "while the extra labour falls on women."),
               pp("amber", "Example: a drinking water scheme",
                  "A tap closer to home saves time mainly for the women and girls who carry "
                  "water. A design that measures only litres delivered misses the time "
                  "saved and who saved it.")),
            hbox("Both examples are Illustrative. The point is general: the same input "
                 "produces different outcomes for women and men because their roles, time "
                 "and control differ.", "amber"),
        ], compact=True),

        C("A quick picture", "India in five numbers from NFHS-5", [
            stats([card("1,020", "females per 1,000 males in the NFHS-5 household population",
                        "cyan", NFHS + ", Ch. 2"),
                   card("72% vs 84%", "women and men aged 15-49 who are literate", "indigo",
                        NFHS + ", Ch. 3"),
                   card("25% vs 75%", "women and men aged 15-49 currently employed", "amber",
                        NFHS + ", Ch. 3"),
                   card("32%", "ever-married women 18-49 who have experienced spousal "
                        "physical, sexual or emotional violence", "red", NFHS + ", Ch. 15")],
                  cols=4),
            body("The National Family Health Survey (NFHS-5, fieldwork 2019-21) interviewed "
                 "women and men aged 15-49 across every state and union territory. It is the "
                 "most used source for gender indicators in India because it asks the same "
                 "questions of women and men and repeats them in each round. Each number "
                 "above opens a section of this course: sex ratios, education, work and "
                 "violence. A population that has more women than men in its households can "
                 "still be one where girls are missing at birth, which is why the survey "
                 "also tracks the sex ratio among young children (928 for ages 0-6 in "
                 "NFHS-5).", sm=True),
        ], compact=True),

        C("Levels", "Where gender operates: four levels", [
            table(["Level", "What gender shapes", "South Asian example"],
                  [["Individual", "Beliefs, skills, aspirations, bodily autonomy",
                    "A girl's own expectation of marrying at 18 or studying further"],
                   ["Household", "Who works, who eats first, who owns, who decides",
                    "Land titled to the eldest son under customary practice"],
                   ["Community and market", "Norms on mobility, caste and occupation, wages",
                    "Lower daily wages for women in casual agricultural work"],
                   ["State", "Laws, schemes, budgets, representation",
                    "One-third of panchayat seats reserved for women under Article 243D"]]),
            body("Change at one level can be blocked at another. A scholarship raises a "
                 "girl's aspiration, but a household that needs her labour or fears for her "
                 "safety on the road to college can still keep her at home. Good gender "
                 "analysis traces a programme through all four levels.", sm=True),
            hbox("Each level has its own data source: surveys of individuals, household "
                 "rosters, market wage data and legal or budget documents.", "indigo"),
        ], compact=True),

        C("Equality and equity", "Gender equality, gender equity and the law", [
            tw(pp("cyan", "Equality",
                  "Equal rights, responsibilities and opportunities for women and men. The "
                  "Constitution of India guarantees equality before the law (Article 14) and "
                  "bars discrimination on grounds of sex (Article 15(1)). Article 39(d) "
                  "directs the state towards equal pay for equal work for both men and "
                  "women."),
               pp("green", "Equity",
                  "Measures that take different starting points into account so that "
                  "outcomes can become equal. Article 15(3) allows the state to make "
                  "special provision for women and children. Reservation of panchayat "
                  "seats, girls' scholarships and women-only self-help groups rest on this "
                  "logic.")),
            body("The two are complementary. Equal treatment of unequal people preserves the "
                 "gap, and special measures without a goal of equal outcomes can become "
                 "permanent tokenism. The Code on Wages, 2019 (section 3) carries the "
                 "equal-pay principle into labour law: no discrimination on the ground of "
                 "gender in wages for the same work or work of a similar nature, and none "
                 "in recruitment.", sm=True),
            hbox("Source: Constitution of India (Legislative Department edition as on 1 May "
                 "2024); Code on Wages, 2019, s. 3. The four Labour Codes came into force on "
                 "21 November 2025.", "indigo"),
        ], compact=True),

        C("Gender is relational", "Gender analysis studies relations, so it includes men", [
            body("Early development work counted women as a separate group to be added in. "
                 "Gender analysis looks at relations: how women's and men's roles depend on "
                 "each other and how power runs between them. A woman's paid work depends on "
                 "who cooks and who looks after children. A man's status may depend on being "
                 "seen as the provider. Changing one side of the relation changes the "
                 "other."),
            table(["Question", "Counting women", "Analysing relations"],
                  [["Who attends training?", "Number of women trained",
                    "Who released time for her to attend, and who covered her work"],
                   ["Who owns land?", "Share of plots with a woman's name",
                    "Who decides on sale, mortgage and crops on that plot"],
                   ["Who earns?", "Women's income", "Who spends it and on what"]]),
            hbox("Section 10 returns to men and masculinities. A gender programme that "
                 "ignores men often meets their resistance later.", "amber"),
        ], compact=True),

        C("This course", "How this course is built", [
            tw([panel("cyan", "Concepts and evidence", [bullets([
                    "The ideas: WID, WAD, GAD, Moser, Kabeer",
                    "The household: Sen's cooperative conflicts, Agarwal on land",
                    "Missing women and sex ratios",
                    "Work, care, education and health, with Indian data"], sm=True)])],
               [panel("green", "Law, politics and practice", [bullets([
                    "Violence against women: NFHS-5, PWDVA 2005, POSH 2013",
                    "Representation: 73rd and 74th Amendments, the 2023 Adhiniyam",
                    "Masculinities and intersectionality",
                    "Gender analysis tools and a worked example"], sm=True)])]),
            body("Gender budgeting and mainstreaming are covered in depth in Gender "
                 "Mainstreaming 101, women's economic empowerment in WEE 101 and the care "
                 "economy in Care Economy 101. This course introduces each and links to "
                 "those decks at the end.", sm=True),
            hbox("Statistics on each slide carry their source. Facts are stated as of "
                 "October 2026.", "indigo"),
        ], compact=True),

        # ===================== SECTION 02 =====================
        D("02", "Section Two", "From WID to GAD: the ideas"),

        C("Boserup 1970", "Ester Boserup put women into development economics", [
            body("Ester Boserup's <em>Woman's Role in Economic Development</em> (1970) "
                 "used data from Africa and Asia to show that women did a large share of "
                 "farm work in many regions, and that colonial and post-colonial "
                 "modernisation often bypassed them. Extension services, new tools and land "
                 "titles went to men, so technical change could lower women's status even "
                 "as output rose."),
            tw(pp("cyan", "What Boserup showed",
                  "Farming systems differ: in shifting cultivation women did much of the "
                  "work, while in plough agriculture men did more of the field work and "
                  "women withdrew into the home. Development policy treated the male "
                  "farmer as the norm."),
               pp("amber", "Why it mattered",
                  "The book gave planners evidence that women were economic actors. It "
                  "fed directly into the 'women in development' movement of the 1970s and "
                  "into the UN Decade for Women.")),
            hbox("Alesina, Giuliano and Nunn (NBER Working Paper 17098, 2011) tested the "
                 "plough idea: descendants of plough-using societies today show lower "
                 "female participation in work and politics.", "indigo"),
        ], compact=True),

        C("WID", "Women in development: add women and stir", [
            body("Women in Development (WID) took Boserup's evidence and argued that women "
                 "had been left out and should be integrated into existing development "
                 "programmes. Its tools were women's projects, women's units in ministries "
                 "and the collection of sex-disaggregated data."),
            tw(pp("green", "Strengths",
                  "Made women visible in statistics and plans. Created budgets and staff "
                  "for women's programmes. Argued in efficiency terms that planners could "
                  "accept: wasting half the labour force slows growth."),
               pp("red", "Limits",
                  "Treated women as a separate, homogeneous group. Left the division of "
                  "labour and power between women and men untouched. Women's projects were "
                  "often small income schemes, such as tailoring and pickle-making, that "
                  "added to women's work without changing control over income.")),
            hbox("The phrase 'add women and stir' summarises the critique: inclusion in a "
                 "process that was not designed with women in mind.", "amber"),
        ], compact=True),

        C("WAD", "Women and development: the system is the problem", [
            body("Women and Development (WAD) emerged in the late 1970s from Marxist and "
                 "dependency thinking. It argued that women had always been part of "
                 "development, as cheap labour in plantations, factories and households, "
                 "and that the problem lay in an unequal global economy that exploited both "
                 "poor women and poor men."),
            table(["Question", "WID answer", "WAD answer"],
                  [["Why are women poor?", "They were left out of development",
                    "They were included on exploitative terms"],
                   ["Unit of analysis", "Women as individuals", "Class and the world economy"],
                   ["What to do", "Projects to integrate women",
                    "Change the structures of production and trade"]]),
            body("WAD's weakness was that it tended to fold gender into class. It said less "
                 "about inequality between a poor woman and a poor man in the same "
                 "household, which is where Gender and Development began.", sm=True),
        ], compact=True),

        C("GAD", "Gender and development: relations, power and change", [
            body("Gender and Development (GAD) grew in the 1980s from the work of feminist "
                 "researchers and activists, many from the global South. It made gender "
                 "relations the object of analysis and asked how power between women and "
                 "men is produced in households, markets and the state, and how it can be "
                 "changed."),
            table(["Feature", "WID", "GAD"],
                  [["Focus", "Women", "Relations between women and men"],
                   ["Problem", "Exclusion from development", "Unequal power"],
                   ["Goal", "Efficiency, integration", "Equality, transformation"],
                   ["Women seen as", "Beneficiaries", "Agents of change"],
                   ["Typical tool", "Women's project", "Gender analysis of all projects"]]),
            hbox("GAD led to 'gender mainstreaming', adopted in the Beijing Platform for "
                 "Action (1995). Gender Mainstreaming 101 covers how it works in budgets and "
                 "institutions.", "indigo"),
        ], compact=True),

        C("DAWN", "Southern voices: DAWN and the view from below", [
            body("Development Alternatives with Women for a New Era (DAWN) grew from a "
                 "meeting of feminists from the global South in Bangalore in August 1984, "
                 "held to prepare for the 1985 Nairobi conference that closed the UN Decade "
                 "for Women. DAWN argued that "
                 "development should be judged by its effect on poor women, and that debt "
                 "crises and structural adjustment were shifting costs onto women's unpaid "
                 "work."),
            tw(pp("cyan", "What changed",
                  "The starting point moved from 'what can development do for women' to "
                  "'what does this model of development do to poor women'. Women's "
                  "organising became a means of change in its own right."),
               pp("green", "South Asian roots",
                  "Indian women's movements of the 1970s and 1980s, from the Chipko and "
                  "anti-dowry campaigns to self-employed women's unions, shaped this "
                  "view. They linked livelihoods, violence and political voice.")),
            hbox("Gita Sen and Caren Grown's <em>Development, Crises and Alternative "
                 "Visions: Third World Women's Perspectives</em>, written for DAWN, set out "
                 "this argument. Source: DAWN timeline, dawnfeminist.org.", "indigo"),
        ], compact=True),

        C("Molyneux and Moser", "Practical and strategic gender needs", [
            body("Maxine Molyneux (1985, <em>Feminist Studies</em> 11(2)) distinguished "
                 "practical gender interests from strategic ones. Caroline Moser turned this "
                 "into a planning tool in 'Gender planning in the Third World: meeting "
                 "practical and strategic gender needs' (<em>World Development</em> 17(11), "
                 "1989) and in <em>Gender Planning and Development</em> (1993)."),
            tw(pp("cyan", "Practical gender needs",
                  "Needs that arise from women's existing roles and do not challenge them: "
                  "water near the home, a creche, a health centre, cooking fuel. Meeting "
                  "them improves daily life within the current division of labour."),
               pp("green", "Strategic gender needs",
                  "Needs that arise from women's subordinate position and, if met, change "
                  "it: land rights, freedom from violence, equal wages, political "
                  "representation, control over fertility.")),
            hbox("Most projects meet practical needs. The question for a designer is "
                 "whether the way they are met also opens a strategic gain, such as women "
                 "managing the water committee that runs the new tap.", "amber"),
        ], compact=True),

        C("Moser's triple role", "Moser's triple role and the planning framework", [
            table(["Role", "What it covers", "Planning implication"],
                  [["Reproductive", "Childbearing, care, cooking, water, fuel",
                    "Unpaid, so ignored in plans and in GDP"],
                   ["Productive", "Work for income or subsistence",
                    "Women's farm and home-based work is undercounted"],
                   ["Community managing", "Running local services, often unpaid",
                    "Projects assume women's volunteer time is free"]]),
            body("Moser argued that women carry all three roles at once while men's "
                 "community work tends to be paid or carry status (community politics). A "
                 "project that adds a fourth demand on women's time without removing "
                 "another can fail, or succeed at the cost of women's rest and health. Her "
                 "framework also classifies policy approaches to women: welfare, equity, "
                 "anti-poverty, efficiency and empowerment.", sm=True),
            hbox("Source: Moser 1989, <em>World Development</em> 17(11): 1799-1825.",
                 "indigo"),
        ], compact=True),

        C("Kabeer 1999", "Kabeer: resources, agency and achievements", [
            body("Naila Kabeer's 'Resources, agency, achievements: reflections on the "
                 "measurement of women's empowerment' (<em>Development and Change</em> "
                 "30(3): 435-464, 1999) defined the process as the expansion in people's "
                 "ability to make strategic life choices in a context where this ability "
                 "was previously denied to them."),
            flow(["RESOURCES: material, human and social, plus the rules of access",
                  "AGENCY: the ability to define goals and act on them",
                  "ACHIEVEMENTS: the outcomes of choices, the well-being achieved"]),
            tw(pp("cyan", "Why three dimensions",
                  "A woman with a bank account (resource) may not decide how the money is "
                  "used (agency). Measuring only resources overstates change."),
               pp("amber", "The caution",
                  "Kabeer warned that indicators lifted out of context mislead: the same "
                  "act can mean different things in different places. Choices that "
                  "reproduce inequality can look like agency.")),
        ], compact=True),

        C("From ideas to indicators", "How the frameworks show up in survey questions", [
            table(["Kabeer dimension", "NFHS-5 indicator (women 15-49)", "India value"],
                  [["Resource", "Has a bank or savings account she uses", "79%"],
                   ["Resource", "Owns land alone or jointly", "32% (men 42%)"],
                   ["Resource", "Has a mobile phone she uses", "54%"],
                   ["Agency", "Participates in three household decisions "
                    "(currently married)", "71%"],
                   ["Agency", "Has money she alone decides how to use", "51%"]]),
            body("Source: " + NFHS + ", Chapter 14. Bank account use rose from 53% in "
                 "NFHS-4 (2015-16) to 79%, largely after the expansion of no-frills "
                 "accounts. Decision-making changed much less. That gap between a "
                 "resource and its use is exactly what Kabeer's framework asks a "
                 "practitioner to check before reporting success.", sm=True),
            hbox("When you read a gender indicator, name which of the three dimensions it "
                 "measures and what it leaves out.", "amber"),
        ], compact=True),

        C("Summary", "The frameworks side by side", [
            table(["Framework", "Unit of analysis", "Main question", "Typical use today"],
                  [["WID (1970s)", "Women", "Are women included?",
                    "Sex-disaggregated data, women's components"],
                   ["WAD (late 1970s)", "Class and the world economy",
                    "On what terms are women included?", "Critique of export and wage models"],
                   ["GAD (1980s on)", "Gender relations", "Who has power, and how does it "
                    "change?", "Gender analysis of every programme"],
                   ["Moser (1989, 1993)", "Roles and needs", "Which needs does the plan "
                    "meet?", "Planning and project review"],
                   ["Kabeer (1999)", "Choices", "Can she make strategic life choices?",
                    "Indicator design and evaluation"]]),
            body("The frameworks build on each other. A practitioner in 2026 typically uses "
                 "WID's sex-disaggregated data, GAD's attention to relations, Moser's "
                 "distinction between practical and strategic needs, and Kabeer's three "
                 "dimensions to choose indicators. Each answers a different question, and Section 11 turns them into working tools."),
            hbox("When a donor asks for a 'gender analysis', ask which of these questions "
                 "it wants answered. The answer decides the method.", "indigo"),
        ], compact=True),

        # ===================== SECTION 03 =====================
        D("03", "Section Three", "Inside the household: bargaining and land"),

        C("Unitary model", "The household as one decision-maker", [
            body("Standard economics long treated the household as a single unit with one "
                 "set of preferences and pooled income, a 'unitary model'. Under it, it "
                 "makes no difference who in the household receives a transfer: the money "
                 "is pooled and spent the same way."),
            tw(pp("red", "What the unitary model predicts",
                  "A cash transfer to the mother and the same transfer to the father "
                  "produce identical spending. Policy can ignore who holds income and "
                  "assets."),
               pp("green", "What bargaining models predict",
                  "Spending depends on who controls the income, because each member brings "
                  "different preferences and different fall-back options. Randomly "
                  "assigning the recipient of a transfer is the cleanest way to test "
                  "which model fits a given setting.")),
            body("Rejecting pooling has direct consequences for design: whose name goes on "
                 "the account, the ration card, the house title under a housing scheme, "
                 "the land record and the insurance policy.", sm=True),
            hbox("Who receives the benefit is a design choice. Record it, and test it where "
                 "you can.", "indigo"),
        ], compact=True),

        C("Sen 1990", "Amartya Sen: cooperative conflicts", [
            body("In 'Gender and cooperative conflicts' (in Irene Tinker, ed., "
                 "<em>Persistent Inequalities</em>, Oxford University Press, 1990) Amartya "
                 "Sen described the household as a site of both cooperation and conflict. "
                 "Members gain from cooperating, but they disagree about how the gains are "
                 "divided."),
            table(["Factor", "Meaning", "Why women often lose"],
                  [["Breakdown position", "How well off each person would be if "
                    "cooperation ended", "Fewer assets, lower wages, weak exit options"],
                   ["Perceived interest", "How much a person weighs her own well-being",
                    "Norms teach women to put the family first"],
                   ["Perceived contribution", "How much a person is seen to contribute",
                    "Unpaid work is invisible, so seen as contributing less"]]),
            hbox("Sen's point about perception matters for programmes: paid, visible work "
                 "can raise a woman's bargaining power even before her income rises, "
                 "because it changes how her contribution is seen.", "amber"),
        ], compact=True),

        C("Agarwal 1997", "Bina Agarwal: bargaining within and beyond the household", [
            body("Bina Agarwal's '\"Bargaining\" and gender relations: within and beyond the "
                 "household' (<em>Feminist Economics</em> 3(1): 1-51, 1997) extended "
                 "bargaining models in three directions."),
            bullets([
                "<strong>Social norms</strong> set limits on what can be bargained over at "
                "all, and norms themselves can be bargained over and changed",
                "<strong>Bargaining beyond the home</strong>: women bargain with the community, "
                "the market and the state, and outcomes there feed back into the home",
                "<strong>What strengthens a woman's position</strong>: ownership of "
                "land and other assets, access to employment, support from kin, "
                "women's groups and the state"]),
            tw(pp("cyan", "Implication",
                  "A women's collective can raise every member's fall-back position at "
                  "once, which individual assistance cannot."),
               pp("green", "South Asian example",
                  "Self-help groups and producer collectives give women a group to bargain "
                  "from with lenders, buyers and officials.")),
        ], compact=True),

        C("A field of one's own", "Land: the asset that matters most in rural South Asia", [
            body("In <em>A Field of One's Own: Gender and Land Rights in South Asia</em> "
                 "(Cambridge University Press, 1994) Agarwal argued that independent land "
                 "rights are central to women's economic well-being, social status and "
                 "bargaining power in rural South Asia, where land is the main source of "
                 "livelihood, security and standing."),
            tw(pp("cyan", "Why land, specifically",
                  "Land produces food and income, serves as collateral, is a fall-back in "
                  "widowhood or separation and confers standing in the village. Its value "
                  "rarely disappears the way wages can."),
               pp("amber", "Ownership versus control",
                  "Legal rights, social recognition of those rights and effective control "
                  "can each be missing. A daughter may inherit on paper and give up her "
                  "share to brothers under family pressure.")),
            stats([card("32% vs 42%", "women and men aged 15-49 who own land alone or "
                        "jointly", "cyan", NFHS + ", Ch. 14"),
                   card("42% vs 60%", "women and men who own a house alone or jointly",
                        "indigo", NFHS + ", Ch. 14")]),
        ], compact=True),

        C("The law", "Inheritance law: the 2005 amendment and Vineeta Sharma", [
            body("The Hindu Succession (Amendment) Act, 2005 substituted section 6 of the "
                 "Hindu Succession Act, 1956 and made daughters coparceners in joint family "
                 "property by birth, with the same rights and liabilities as sons, from 9 "
                 "September 2005. Before it, only sons were coparceners by birth in a "
                 "Mitakshara joint family."),
            tw(pp("cyan", "Vineeta Sharma v Rakesh Sharma (2020)",
                  "A three-judge bench of the Supreme Court held on 11 August 2020 that a "
                  "daughter's coparcenary right arises by birth and does not depend on her "
                  "father being alive on 9 September 2005. It resolved the conflict between "
                  "<em>Prakash v Phulavati</em> (2016) and <em>Danamma v Amar</em> (2018)."),
               pp("amber", "What the law does not settle",
                  "Muslim, Christian and Parsi women inherit under different personal laws, "
                  "and tribal customary law varies. Mutation of records and family "
                  "pressure to relinquish shares remain the main barriers in practice.")),
            hbox("Sources: Hindu Succession (Amendment) Act, 2005; <em>Vineeta Sharma v "
                 "Rakesh Sharma</em>, Supreme Court of India, 11 August 2020.", "indigo"),
        ], compact=True),

        C("Testing the models", "How researchers test who decides", [
            table(["Method", "What it does", "What it can show"],
                  [["Survey decision modules", "Ask who decides on health, purchases, "
                    "visits", "Reported say, as in NFHS-5 Chapter 14"],
                   ["Expenditure comparisons", "Compare spending when income is in "
                    "women's versus men's hands", "Whether income is pooled"],
                   ["Randomised transfers", "Assign the recipient (woman or man) at random",
                    "Causal effect of who receives the money"],
                   ["Lab-in-field games", "Spouses make private and joint choices",
                    "Hidden income, trust, efficiency"],
                   ["Qualitative interviews", "Narratives of decisions and disputes",
                    "Why and how, including norms"]]),
            body("Each method has blind spots. Reported decision-making depends on who "
                 "answers and on what 'participate' means to her. Combining a survey "
                 "measure with qualitative work is often the most informative design for "
                 "a programme evaluation. Mixed Methods 101 and Feminist Research 101 "
                 "cover how.", sm=True),
        ], compact=True),

        C("Design lessons", "What household bargaining means for programme design", [
            tw([panel("cyan", "Design choices", [bullets([
                    "Put the asset or account in the woman's name, or joint names",
                    "Pay wages and transfers directly into her account",
                    "Make women's contribution visible: registers, job cards, receipts",
                    "Support collectives that raise her fall-back position"], sm=True)])],
               [panel("amber", "Risks to plan for", [bullets([
                    "Backlash or violence when her income or say rises",
                    "Nominal ownership with male control in practice",
                    "Extra workload without relief elsewhere",
                    "Assuming a married woman's interests equal her household's"],
                    sm=True)])]),
            body("Track both resources and agency: a joint title is a resource, and who "
                 "decides on sale or mortgage is agency. Section 11 turns these into a "
                 "checklist a project team can use.", sm=True),
            hbox("Who is named on the benefit is the cheapest gender decision a programme "
                 "makes, and one of the most consequential.", "indigo"),
        ], compact=True),

        # ===================== SECTION 04 =====================
        D("04", "Section Four", "Missing women, son preference and sex ratios"),

        C("Sen 1990", "More than 100 million women are missing", [
            body("Amartya Sen's essay in the <em>New York Review of Books</em> (20 December "
                 "1990) observed that where women and men receive similar care, women "
                 "outnumber men, at a ratio of about 1.05. In South Asia, West Asia and "
                 "China the ratio could be as low as 0.94 or lower. Sen estimated the women who would be alive with equal "
                 "care and concluded that 'a great many more than 100 million women' were "
                 "missing."),
            tw(pp("cyan", "The method",
                  "Compare the actual number of women with the number expected at a "
                  "benchmark sex ratio. The gap counts excess female deaths across all "
                  "ages, from infancy to adulthood, plus sex selection before birth."),
               pp("green", "Kerala as contrast",
                  "Sen noted that Kerala's ratio of women to men, above 1.03, was closer to "
                  "Europe (1.05) than to India as a whole (0.94). A state within India "
                  "showed that the deficit was a matter of social arrangements.")),
            hbox("Sen also wrote that rapid economic development may go hand in hand with "
                 "worsening relative mortality of women. Growth alone does not close the "
                 "gap.", "amber"),
        ], compact=True),

        C("Terms", "Three sex ratios that are easily confused", [
            table(["Measure", "Definition", "Latest India value", "Source"],
                  [["Sex ratio (overall)", "Females per 1,000 males, all ages", "943",
                    "Census 2011"],
                   ["Child sex ratio", "Girls per 1,000 boys aged 0-6", "918",
                    "Census 2011"],
                   ["Sex ratio at birth (SRB)", "Girls born per 1,000 boys born", "913",
                    "SRS 2021"]]),
            body("The overall sex ratio mixes births, deaths and migration across every age "
                 "group, so it moves slowly. The child sex ratio reflects both sex "
                 "selection before birth and excess mortality of girls after birth. The "
                 "sex ratio at birth isolates selection: slightly more boys than girls are born "
                 "everywhere, so even without selection it sits a little below 1,000. Surveys of households such as NFHS give different values "
                 "from the census because they cover the usual resident household "
                 "population, which excludes people living in institutions and differs in "
                 "migration.", sm=True),
            hbox("Sources: MoSPI, Women and Men in India 2023 (943); PIB explainer on Beti "
                 "Bachao Beti Padhao, 13 June 2022 (918); SRS Statistical Report 2021 as "
                 "reported by All India Radio News, May 2025 (913).", "indigo"),
        ], compact=True),

        C("Six censuses", "The child sex ratio fell for fifty years", [
            {"t": "chart", "canvas": "gdCsrChart",
             "title": "Child sex ratio (girls per 1,000 boys aged 0-6), India, 1961-2011",
             "source": "Census of India, as tabulated in PIB explainer on Beti Bachao Beti "
                       "Padhao, 13 June 2022",
             "type": "line",
             "data": {"labels": ["1961", "1971", "1981", "1991", "2001", "2011"],
                      "datasets": [{"label": "Child sex ratio",
                                    "data": [976, 964, 962, 945, 927, 918],
                                    "borderColor": "#EF4444",
                                    "backgroundColor": "rgba(239,68,68,0.08)",
                                    "fill": True, "tension": 0.2, "pointRadius": 4}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:900, max:990, title:{display:true,text:'Girls per 1,000 boys'} } } }"}},
            body("The decline accelerated after 1981, the period when ultrasound became "
                 "cheap and widely available. The same PIB explainer records that the "
                 "child sex ratio fell in 429 of 640 districts between 2001 and 2011. A "
                 "falling ratio while the overall sex ratio rose (933 in 2001 to 943 in "
                 "2011) shows that the problem had concentrated at birth.", sm=True),
        ], compact=True),

        C("Son preference", "Son preference is stated openly in surveys", [
            stats([card("81%", "women aged 15-49 who want at least one son", "red",
                        NFHS + ", Ch. 4"),
                   card("79%", "women who want at least one daughter", "cyan",
                        NFHS + ", Ch. 4"),
                   card("15% vs 3%", "women who want more sons than daughters, and more "
                        "daughters than sons", "amber", NFHS + ", Ch. 4")], cols=3),
            body("Most families want children of both sexes. The imbalance comes from the "
                 "minority with a strong preference for sons and from the demand for at "
                 "least one son as fertility falls. When families want two children and "
                 "insist that one be a boy, sex selection at the second or third birth "
                 "becomes the means. Seema Jayachandran's review in the <em>Annual Review "
                 "of Economics</em> (7: 63-88, 2015) argues that norms such as "
                 "patrilocality, where daughters leave at marriage and sons stay to support "
                 "parents, help explain the male-skewed sex ratio in India and China."),
            hbox("Men's answers in NFHS-5 are almost identical: 81% want at least one son, "
                 "and 16% want more sons than daughters.", "indigo"),
        ], compact=True),

        C("The law", "PCPNDT Act 1994: banning sex determination", [
            body("The Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex "
                 "Selection) Act, 1994 began as the Pre-Natal Diagnostic Techniques Act and "
                 "was amended and renamed in 2003 to cover selection before conception. Its "
                 "long title now reads: an Act to provide for the prohibition of sex "
                 "selection, before or after conception."),
            table(["Provision", "Content"],
                  [["Section 6", "Prohibits pre-natal techniques, including ultrasound, for "
                    "determining the sex of a foetus, and sex selection by any means"],
                   ["Registration", "Every clinic with ultrasound must register and keep "
                    "records"],
                   ["Penalties", "Imprisonment up to three years and fines for a first "
                    "offence, higher for repeat offences"],
                   ["Authorities", "Appropriate authorities at state and district level "
                    "inspect and prosecute"]]),
            hbox("Enforcement has been uneven. Convictions are few relative to the scale of "
                 "missing births, and a ban on technology does not change the demand that "
                 "drives it.", "amber"),
        ], compact=True),

        C("Policy response", "Beti Bachao Beti Padhao and the debate on what works", [
            body("Beti Bachao Beti Padhao (BBBP) was launched at Panipat, Haryana on 22 "
                 "January 2015 by the Ministries of Women and Child Development, Health and "
                 "Family Welfare, and Education. It started in 100 districts with low child "
                 "sex ratios and was extended to all 640 districts (Census 2011) in March "
                 "2018."),
            tw(pp("green", "Reported progress",
                  "The government's explainer reports the sex ratio at birth in its Health "
                  "Management Information System rising from 918 in 2014-15 to 937 in "
                  "2020-21. The SRS sex ratio at birth rose from 899 in 2014 to 913 in "
                  "2021."),
               pp("amber", "Reading the numbers",
                  "HMIS counts births in reporting facilities, so its ratio moves with the "
                  "share of births recorded there. SRS is a sample survey. Both show "
                  "improvement, but neither isolates the scheme's effect from falling "
                  "fertility, education or enforcement.")),
            hbox("Sources: PIB explainer, 13 June 2022; SRS 2021 via All India Radio News, "
                 "May 2025. Attribution to a single scheme needs an evaluation design: see "
                 "Impact Evaluation 101.", "indigo"),
        ], compact=True),

        C("Beyond India", "Sex ratio at birth across South Asia", [
            table(["Country (2024)", "Boys born per girl", "Girls per 1,000 boys"],
                  [["India", "1.071", "934"],
                   ["Pakistan", "1.055", "948"],
                   ["Afghanistan", "1.051", "951"],
                   ["Maldives", "1.051", "951"],
                   ["Bangladesh", "1.049", "953"],
                   ["Nepal", "1.049", "953"],
                   ["Bhutan", "1.048", "954"],
                   ["Sri Lanka", "1.044", "958"]]),
            body("Source: World Bank WDI, indicator SP.POP.BRTH.MF (UN population estimates), "
                 "accessed October 2026. The last column is our conversion of the first. "
                 "India stands out in the region. Note that this modelled estimate for "
                 "India (934) differs from the SRS figure (913 in 2021): the UN series is "
                 "modelled from several sources, while SRS is a direct sample count. Quote "
                 "SRS for India and the UN series only for cross-country comparison.",
                 sm=True),
            hbox("Son preference exists across the region. Where it shows up as a deficit of "
                 "girls at birth depends on fertility decline and access to sex selection; "
                 "elsewhere it can show up as families continuing to have children until a "
                 "son is born.", "amber"),
        ], compact=True),

        C("For practitioners", "Working on son preference without harm", [
            tw([panel("cyan", "What helps", [bullets([
                    "Raise the value of daughters: inheritance, old-age support, schooling",
                    "Work with mothers-in-law and husbands, who often decide",
                    "Pair enforcement with community dialogue",
                    "Use birth registration data to monitor district SRB"], sm=True)])],
               [panel("red", "What to avoid", [bullets([
                    "Messaging that stigmatises abortion in general",
                    "Blaming women who are under family pressure",
                    "Celebrating one year's SRB rise from a small sample",
                    "Cash incentives that only reward a girl's birth"], sm=True)])]),
            body("Restricting safe abortion to stop sex selection pushes women to unsafe "
                 "providers and does not reduce son preference. The Medical Termination of "
                 "Pregnancy Act and the PCPNDT Act serve different purposes and should not "
                 "be conflated in communication. Sexual Health 101 covers reproductive "
                 "rights.", sm=True),
            hbox("Rule of thumb: target the demand for sons, protect access to safe "
                 "reproductive care.", "amber"),
        ], compact=True),

        # ===================== SECTION 05 =====================
        D("05", "Section Five", "Women's work and how it is measured"),

        C("Definitions", "Labour force participation: what is being counted", [
            term("Labour force participation rate (LFPR)",
                 "The percentage of persons in the labour force, that is working or seeking "
                 "or available for work, in the population. PLFS defines it this way."),
            tw(pp("cyan", "Usual status (ps+ss)",
                  "PLFS looks back 365 days. The principal status is the activity a person "
                  "spent most time on. Subsidiary status adds anyone who did economic "
                  "activity for 30 days or more in addition. Including subsidiary work "
                  "counts much of women's seasonal and part-time work."),
               pp("green", "Current weekly status",
                  "The reference period is the last 7 days. It captures who is working now "
                  "and is the basis of PLFS's short-period bulletins, but it misses women "
                  "whose work is seasonal.")),
            body("Source: PLFS press note, Annual Report July 2023-June 2024, NSO, "
                 "23 September 2024. The choice of reference period is a gender decision: "
                 "short windows undercount women's intermittent work.", sm=True),
            hbox("Read every women's employment figure with three questions: which age "
                 "group, which reference period, and which activities count as work.",
                 "amber"),
        ], compact=True),

        C("The trend", "Women's participation in PLFS, 2017-18 to 2025", [
            {"t": "chart", "canvas": "gdLfprChart",
             "title": "Female LFPR, usual status (ps+ss), age 15+, India (%)",
             "source": "PLFS press notes: Annual Report 2023-24 (NSO, 23 Sep 2024) for "
                       "2017-18 to 2023-24 (July-June years); Annual Report 2025 (NSO, "
                       "27 Mar 2026) for calendar 2025",
             "type": "bar",
             "data": {"labels": ["2017-18", "2018-19", "2019-20", "2020-21", "2021-22",
                                 "2022-23", "2023-24", "2025"],
                      "datasets": [{"label": "Female LFPR",
                                    "data": [23.3, 24.5, 30.0, 32.5, 32.8, 37.0, 41.7,
                                             40.0],
                                    "backgroundColor": "#6366F1"}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:50, title:{display:true,text:'% of women 15+'} } } }"}},
            body("Female LFPR rose from 23.3% to 41.7% between 2017-18 and 2023-24, while "
                 "male LFPR moved from 75.8% to 78.8%. PLFS switched to calendar-year "
                 "reporting from 2025, when female LFPR was 40.0% and male 79.1%, so the "
                 "last bar is not strictly comparable with the July-June years.", sm=True),
        ], compact=True),

        C("Rural and urban", "Most of the rise came from rural women", [
            table(["Female LFPR, usual status, 15+", "2017-18", "2023-24", "Change"],
                  [["Rural", "24.6%", "47.6%", "+23.0 points"],
                   ["Urban", "20.4%", "28.0%", "+7.6 points"],
                   ["All India", "23.3%", "41.7%", "+18.4 points"]]),
            body("Source: PLFS press note, Annual Report 2023-24, Table 1. The rise was "
                 "concentrated in rural areas. The headline rate cannot tell how much "
                 "reflects new paid jobs and how much reflects women in farm households "
                 "being recorded as working in family enterprises. In 2025, 64.2% of women workers were "
                 "self-employed against 52.0% of men, and 18.2% of women workers were in "
                 "regular wage or salaried jobs (PLFS 2025 press note).", sm=True),
            tw(pp("cyan", "A cautious reading",
                  "More women are being counted as working, especially in agriculture and "
                  "household enterprises."),
               pp("amber", "An open question",
                  "Whether this work brings women their own income and control over it, "
                  "which the participation rate does not show.")),
        ], compact=True),

        C("Earnings", "The gender gap in pay, PLFS 2025", [
            table(["Type of work (2025)", "Men", "Women", "Women as % of men"],
                  [["Regular wage or salaried (monthly)", "Rs 24,217", "Rs 18,353", "76%"],
                   ["Self-employed (monthly)", "Rs 17,914", "Rs 6,374", "36%"],
                   ["Casual labour other than public works (daily)", "Rs 455", "Rs 315",
                    "69%"]]),
            body("Source: " + PLFS25 + ". Women's earnings grew faster than men's between "
                 "2024 and 2025 in all three categories, but the levels remain far apart. "
                 "The largest gap is in self-employment, where most women workers are. Part "
                 "of it reflects hours: PLFS 2025 reports that urban self-employed men "
                 "worked about 17.5 hours a week more than women, and rural self-employed "
                 "men about 12.3 hours more.", sm=True),
            hbox("Calculations in the last column are ours from the PLFS figures. Hours "
                 "differ, so the monthly gaps overstate the gap per hour.", "indigo"),
        ], compact=True),

        C("Why women are out", "Why women are outside the labour force", [
            stats([card("44.4%", "women outside the labour force who cite child care or "
                        "personal commitments in home-making as the main reason", "red",
                        PLFS25),
                   card("69.8%", "men outside the labour force who cite wanting to "
                        "continue studies", "cyan", PLFS25)]),
            body("The contrast summarises the gender division of labour. A man outside the "
                 "labour force is usually a student; a woman is usually doing unpaid work "
                 "at home. Klasen and Pieters (<em>World Bank Economic Review</em> 29(3), "
                 "2015) found that urban married women's participation stagnated around 18% "
                 "between 1987 and 2011 despite growth, falling fertility and rising "
                 "education. They point to supply factors, such as rising household incomes "
                 "and husbands' education, and to demand: the sectors that employ women "
                 "expanded least."),
            hbox("Supply and demand both matter. A skills programme for women fails if "
                 "local employers do not hire women, and a new factory fails to recruit if "
                 "care and mobility constraints are left in place.", "amber"),
        ], compact=True),

        C("Measurement matters", "Two estimates of the same rate", [
            {"t": "chart", "canvas": "gdLfprSaChart",
             "title": "Female labour force participation, ages 15+, 2025 (%), modelled ILO "
                      "estimates",
             "source": "World Bank WDI, indicator SL.TLF.CACT.FE.ZS (ILO modelled "
                       "estimates), accessed October 2026",
             "type": "bar",
             "data": {"labels": ["Bhutan", "Maldives", "Bangladesh", "India", "Sri Lanka",
                                 "Nepal", "Pakistan", "Afghanistan"],
                      "datasets": [{"label": "Female LFPR",
                                    "data": [56.7, 40.7, 38.6, 32.4, 31.0, 27.5, 24.0, 5.1],
                                    "backgroundColor": "#0EA5E9"}]},
             "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:60 } } }"}},
            body("The ILO modelled estimate for India in 2025 is 32.4%, against 40.0% in "
                 "PLFS 2025. Modelled series harmonise definitions across countries and "
                 "fill gaps with models, while PLFS usual status includes subsidiary work "
                 "of 30 days or more. Use the national survey for India and the modelled "
                 "series for cross-country comparison, and never mix them in one "
                 "chart.", sm=True),
        ], compact=True),

        C("Evidence", "Opportunity changes decisions: two Indian studies", [
            tw(pp("cyan", "Jensen: jobs and girls' schooling",
                  "Robert Jensen provided job recruitment services for three years in "
                  "randomly chosen villages in India. Girls in "
                  "treatment villages had higher school enrolment and better nutrition "
                  "(BMI). Families invested more in daughters once the return to their "
                  "education was visible. (<em>Quarterly Journal of Economics</em> 127(2), "
                  "2012; NBER Working Paper 16021.)"),
               pp("green", "Why this matters for design",
                  "The study shows that norms can shift: households respond to "
                  "credible information about women's earning opportunities. Information "
                  "about jobs, placement services and visible role models can shift "
                  "investment in girls at low cost.")),
            body("A second line of work studies safety and mobility. Where travel to work "
                 "is unsafe or socially restricted, the effective labour market for women "
                 "is the distance they can travel. Transport, lighting and safe workplaces "
                 "are labour market policies for women.", sm=True),
            hbox("WEE 101 covers programmes on women's livelihoods in depth, including "
                 "self-help groups, credit and enterprise.", "indigo"),
        ], compact=True),

        C("Collecting data", "Asking about women's work in your own surveys", [
            table(["Problem", "What goes wrong", "Better practice"],
                  [["Proxy respondent", "Husband reports wife as 'housewife'",
                    "Interview women directly where possible"],
                   ["Single question", "'Do you work?' misses unpaid family work",
                    "Ask activity by activity: livestock, farm, sales, home-based work"],
                   ["Short recall", "Seasonal work missed", "Use a 12-month recall alongside "
                    "the last 7 days"],
                   ["Self-perception", "Women do not call their own work 'work'",
                    "Use concrete activity lists"],
                   ["Interviewer norms", "Interviewer assumes women do not work",
                    "Train and monitor; use female interviewers"]]),
            body("Survey Design 101 covers questionnaire construction. For women's work, "
                 "the practical rule is to ask about activities before asking about "
                 "status, and to ask the woman herself.", sm=True),
            hbox("Every method change alters the rate. When you report a change over time, "
                 "check that the questions did not change.", "amber"),
        ], compact=True),

        # ===================== SECTION 06 =====================
        D("06", "Section Six", "Unpaid care and time use"),

        C("Time Use Survey", "India's Time Use Survey: what it measures", [
            body("The National Statistics Office ran India's first national Time Use Survey "
                 "in 2019 and the second in January-December 2024. Every member aged 6 and "
                 "above in sampled households reports, for the previous 24 hours, what "
                 "they did in each 30-minute slot. TUS 2024 enumerated 4,54,192 persons "
                 "aged 6 and above."),
            tw(pp("cyan", "Paid and unpaid work",
                  "Activities are grouped into employment, production of goods for own "
                  "use, unpaid domestic services, unpaid caregiving, volunteer work, "
                  "learning, socialising, leisure and self-care."),
               pp("green", "Why time use matters",
                  "Labour surveys count people as working or not. Time use shows how many "
                  "minutes go to each activity, including the unpaid work that keeps "
                  "households running and that national accounts leave out.")),
            hbox("Source: " + TUS24 + ", press note of 25 February 2025.", "indigo"),
        ], compact=True),

        C("The gap", "Women do most of the unpaid work", [
            {"t": "chart", "canvas": "gdTusChart",
             "title": "Minutes per day per participant, persons aged 6+, India, 2024",
             "source": TUS24 + ", Table 2",
             "type": "bar",
             "data": {"labels": ["Unpaid domestic services", "Unpaid caregiving",
                                 "Employment and related"],
                      "datasets": [{"label": "Women", "data": [289, 137, 341],
                                    "backgroundColor": "#EF4444"},
                                   {"label": "Men", "data": [88, 75, 473],
                                    "backgroundColor": "#0EA5E9"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ title:{display:true,text:'Minutes per day'} } } }"}},
            body("These are minutes among people who did the activity. Participation also "
                 "differs: 81.5% of women aged 6+ did unpaid domestic work on the reference "
                 "day against 27.1% of men, and 34.0% of women did unpaid caregiving "
                 "against 17.9% of men (TUS 2024, Table 1).", sm=True),
        ], compact=True),

        C("Change over time", "2019 to 2024: small shifts", [
            stats([card("315 to 305", "minutes a day on unpaid domestic services, women "
                        "15-59 who did it, 2019 to 2024", "amber", TUS24),
                   card("21.8% to 25%", "women 15-59 in employment and related activities "
                        "on the reference day, 2019 to 2024", "cyan", TUS24),
                   card("16.4% vs 1.7%", "share of the whole day women and men aged 6+ "
                        "spend on unpaid domestic work", "red", TUS24 + ", Table 3")],
                  cols=3),
            body("The NSO reads the fall in unpaid domestic minutes as a shift from unpaid "
                 "to paid activities. Women aged 15-59 who gave care spent about 140 "
                 "minutes a day on it against 74 minutes for men, and 41% of these women "
                 "gave care against 21.4% of men. The press note itself says that most "
                 "caregiving for household members is borne by women."),
            hbox("Five years is a short period for norms. The change is real but small "
                 "next to a gap of more than three hours a day.", "amber"),
        ], compact=True),

        C("Concepts", "Time poverty and the double burden", [
            term("Time poverty",
                 "Having so many hours committed to paid and unpaid work that too little "
                 "time remains for rest, learning, health and participation in public "
                 "life."),
            tw(pp("cyan", "The double burden",
                  "When women take up paid work without a matching reduction in unpaid "
                  "work, total work hours rise. Rising female employment can therefore "
                  "coexist with worse well-being."),
               pp("green", "The 3R framework",
                  "Diane Elson (<em>New Labor Forum</em> 26(2), 2017) proposes to <strong>recognise</strong> unpaid care "
                  "in data and policy, <strong>reduce</strong> its drudgery through water, "
                  "fuel and infrastructure, and <strong>redistribute</strong> it between "
                  "women and men and between households and the state.")),
            body("A programme that adds meetings, training or enterprise work for women "
                 "should state whose time it uses and what it removes. Care Economy 101 "
                 "covers the 3R framework, valuation of unpaid work and care policy in "
                 "detail.", sm=True),
        ], compact=True),

        C("Design", "Designing programmes around women's time", [
            table(["Design element", "Time-blind version", "Time-aware version"],
                  [["Meetings", "Mid-morning at the block office",
                    "In the village, at times women choose"],
                   ["Training", "Five full days away",
                    "Short sessions over weeks, with child care"],
                   ["Public works", "Same task norms for all",
                    "Worksite creche, nearby sites, flexible start"],
                   ["Infrastructure", "Judged by cost per unit",
                    "Judged also by hours saved for women and girls"],
                   ["Monitoring", "Attendance counts",
                    "Time-use module before and after"]]),
            body("A short time-use module (a 24-hour recall of main activities) can be "
                 "added to a baseline and endline survey. It shows whether the programme "
                 "added to women's total work, which attendance figures cannot.", sm=True),
            hbox("Fuel, water and child care investments are often the most "
                 "cost-effective gender interventions because they release time for "
                 "everything else.", "green"),
        ], compact=True),

        C("Region", "Unpaid care across South Asia", [
            body("Several South Asian countries have run national time use surveys or added "
                 "time use questions to labour force surveys. Definitions, age groups and "
                 "reference days differ, so compare the direction of the gap across "
                 "countries and leave exact minutes to within-country analysis, and open each national statistics "
                 "office's report before quoting it. In India, the gap of more than three "
                 "hours a day in unpaid domestic work (TUS 2024) is the benchmark to use."),
            tw(pp("cyan", "Common drivers",
                  "Patrilocal marriage that places young wives under heavy domestic "
                  "duties, limited piped water and clean fuel in rural areas, and weak "
                  "public child care."),
               pp("green", "Common responses",
                  "Anganwadi and creche expansion, clean cooking fuel schemes, household "
                  "water connections and paid care work in health and nutrition "
                  "programmes.")),
            hbox("Before citing another country's figure, open its national statistics "
                 "office report and check the age group and reference day.", "amber"),
        ], compact=True),

        # ===================== SECTION 07 =====================
        D("07", "Section Seven", "Education and health gaps"),

        C("Education", "Girls' schooling: large gains, remaining gaps", [
            stats([card("72% vs 84%", "women and men aged 15-49 who are literate", "cyan",
                        NFHS + ", Ch. 3"),
                   card("41% vs 50%", "women and men with 10 or more years of schooling",
                        "indigo", NFHS + ", Ch. 3"),
                   card("33% vs 51%", "women and men aged 15-49 who have ever used the "
                        "internet", "amber", NFHS + ", Ch. 3")], cols=3),
            body("The gap is widest among older women and in poorer and rural households, "
                 "and narrows sharply among the young. In higher education the All India "
                 "Survey on Higher Education 2021-22 counted 2.07 crore women enrolled, up "
                 "from 2.01 crore a year earlier, and more women than men in the science "
                 "stream (29.8 lakh against 27.4 lakh)."),
            hbox("AISHE figures as reported by PTI from the Ministry of Education survey, "
                 "25 January 2024. Enrolment parity in college does not yet mean parity in "
                 "employment, as Section 5 showed.", "amber"),
        ], compact=True),

        C("What keeps girls out", "Why girls leave school", [
            table(["Barrier", "Mechanism", "Example response"],
                  [["Distance and safety", "Parents fear for girls on the road",
                    "Bicycles for girls, transport, nearby secondary schools"],
                   ["Domestic work", "Girls care for siblings and fetch water",
                    "Creches, water supply, school timings"],
                   ["Marriage", "Schooling stops at marriage",
                    "Conditional transfers, enforcement of the child marriage law"],
                   ["Sanitation", "No usable toilet at school",
                    "Separate functional toilets and menstrual supplies"],
                   ["Low returns", "Few jobs for educated women nearby",
                    "Information on jobs, as in Jensen's study"]]),
            body("Child marriage is the barrier with the clearest legal answer. NFHS-5 finds "
                 "that 23% of women aged 20-24 married before 18, the legal minimum for "
                 "women, compared with 47% of women aged 45-49. The decline is large but "
                 "leaves nearly one in four young women married as children.", sm=True),
            hbox("Source: " + NFHS + ", Chapter 6. Education Policy 101 and Child Rights "
                 "101 go further.", "indigo"),
        ], compact=True),

        C("Health", "Women's health: anaemia, nutrition and maternal mortality", [
            stats([card("57% vs 25%", "women and men aged 15-49 with anaemia", "red",
                        NFHS + ", Ch. 10"),
                   card("19% vs 16%", "women and men aged 15-49 who are thin", "amber",
                        NFHS + ", Ch. 10"),
                   card("93", "maternal deaths per 1,00,000 live births in 2019-21, down from "
                        "130 in 2014-16",
                        "cyan", "SRS 2021 via All India Radio News, May 2025")], cols=3),
            body("Anaemia among women rose between NFHS-4 and NFHS-5, and is more than "
                 "twice the male rate. It reflects diet, menstrual blood loss, repeated "
                 "pregnancies and the norm that women eat last and least. Maternal "
                 "mortality has fallen steeply with institutional delivery and emergency "
                 "obstetric care, but remains far higher in some states than others."),
            hbox("Maternal Health 101, Nutrition 101 and Public Health 101 cover these in "
                 "depth. Here the point is that women's health gaps are partly biological "
                 "and largely social.", "indigo"),
        ], compact=True),

        C("Care-seeking", "Gender shapes care-seeking from infancy", [
            tw(pp("cyan", "Girls in childhood",
                  "In many South Asian settings girls are taken to a health provider later "
                  "and less often when ill, and families spend less on their treatment. "
                  "Sen's missing women include these excess deaths after birth as well as "
                  "sex selection before it."),
               pp("green", "Adult women",
                  "Women need permission or company to travel to a facility, have less cash "
                  "of their own, and put their own illness last. In NFHS-5, three-fifths of "
                  "women report at least one problem in getting medical care for "
                  "themselves, and 31% worry that no female provider is available.")),
            body("Health programmes respond by bringing services closer (ASHA workers, "
                 "health and wellness centres), by insuring women in their own name, and "
                 "by counting care-seeking separately for girls and boys in routine data. "
                 "A district that reports child treatment rates without disaggregating by "
                 "sex cannot see the problem.", sm=True),
            hbox("Always disaggregate health service data by sex and age. It costs almost "
                 "nothing at the point of collection.", "amber"),
        ], compact=True),

        C("Men's health", "Gender norms also harm men", [
            body("Gender norms shape men's health too. Norms that link masculinity to risk, "
                 "toughness and not seeking help show up in behaviour. In NFHS-5, 39% of men "
                 "and 4% of women aged 15-49 use any form of tobacco, and 22% of men "
                 "against 1% of women drink alcohol. Reported tuberculosis is also higher "
                 "among men (283 per 1,00,000) than women (162). Source: " + NFHS + ", "
                 "Chapter 11."),
            table(["Norm", "Effect on men", "Programme response"],
                  [["Men do not show weakness", "Late care-seeking, untreated depression",
                    "Outreach through workplaces and men's groups"],
                   ["Men take risks", "Injuries, substance use",
                    "Road safety, harm reduction"],
                   ["Men provide alone", "Distress migration, debt stress",
                    "Social protection that counts both earners"]]),
            body("Recognising men's health needs is part of gender analysis. It also helps "
                 "programmes enlist men as allies in changing norms that hurt women. Mental "
                 "Health 101 covers suicide prevention and care.", sm=True),
        ], compact=True),

        C("Digital divide", "The gender gap in phones and the internet", [
            stats([card("54%", "women aged 15-49 who have a mobile phone they themselves "
                        "use", "cyan", NFHS + ", Ch. 14"),
                   card("71%", "women with a mobile phone who can read text messages",
                        "indigo", NFHS + ", Ch. 14"),
                   card("33% vs 51%", "women and men aged 15-49 who have ever used the "
                        "internet", "amber", NFHS + ", Ch. 3")], cols=3),
            tw(pp("cyan", "Why it matters for programmes",
                  "Information, payments, scheme enrolment and helplines now run through "
                  "phones. A programme that sends messages to 'the household number' "
                  "usually reaches the man who holds the phone."),
               pp("amber", "What to check",
                  "Whose phone receives messages, whether she can read them, who charges "
                  "and pays for it, and whether her use is monitored by others. NFHS-5 "
                  "finds phone ownership far lower in rural areas and the poorest "
                  "households.")),
            hbox("Design digital components with a non-digital route for women without a "
                 "phone of their own. Digital Rights &amp; AI 101 covers the wider "
                 "questions.", "amber"),
        ], compact=True),

        C("Summary", "Education and health: a gap table", [
            table(["Indicator (NFHS-5, ages 15-49)", "Women", "Men", "Gap"],
                  [["Literate", "72%", "84%", "12 points"],
                   ["10 or more years of schooling", "41%", "50%", "9 points"],
                   ["Ever used the internet", "33%", "51%", "18 points"],
                   ["Anaemic", "57%", "25%", "32 points"],
                   ["Currently employed", "25%", "75%", "50 points"]]),
            body("Source: " + NFHS + ", Chapters 3 and 10. Gaps are calculated from the "
                 "rounded figures in the report. The largest gap is in employment, which "
                 "connects the two sections before this one: schooling has risen faster "
                 "than paid work, and unpaid care absorbs the difference.", sm=True),
            hbox("Use this kind of side-by-side table in any gender analysis: same "
                 "indicator, same source, women and men in adjacent columns.", "indigo"),
        ], compact=True),

        # ===================== SECTION 08 =====================
        D("08", "Section Eight", "Violence against women: data and law"),

        C("Prevalence", "Violence by husbands is the most common form", [
            stats([card("32%", "ever-married women 18-49 who have experienced spousal "
                        "physical, sexual or emotional violence", "red", NFHS + ", Ch. 15"),
                   card("29%", "experienced spousal physical or sexual violence, down from "
                        "31% in NFHS-4", "amber", NFHS + ", Ch. 15"),
                   card("14%", "women who experienced physical or sexual violence who "
                        "sought help to stop it", "cyan", NFHS + ", Ch. 15")], cols=3),
            body("NFHS-5 selected only one woman per household for the domestic violence "
                 "module, interviewed her in private and stopped if privacy was lost, "
                 "following international ethical guidance. Even so, these are lower "
                 "bounds: some women do not disclose. Among women who sought help, 61% "
                 "turned to their own family and only 6% to the police."),
            hbox("Physical spousal violence (28%) is the most common form, followed by "
                 "emotional violence (14%). Six per cent of ever-married women report "
                 "spousal sexual violence.", "indigo"),
        ], compact=True),

        C("Who is affected", "Spousal violence by caste and wealth", [
            {"t": "chart", "canvas": "gdDvChart",
             "title": "Ever-married women 18-49 who have ever experienced spousal physical "
                      "or sexual violence (%), India 2019-21",
             "source": NFHS + ", Table 15.11",
             "type": "bar",
             "data": {"labels": ["Scheduled Caste", "Scheduled Tribe", "OBC", "Other",
                                 "Lowest wealth", "Highest wealth", "All women"],
                      "datasets": [{"label": "Physical or sexual spousal violence",
                                    "data": [34.7, 31.8, 30.2, 22.6, 38.4, 16.9, 29.2],
                                    "backgroundColor": ["#EF4444", "#EF4444", "#EF4444",
                                                        "#EF4444", "#F59E0B", "#F59E0B",
                                                        "#6366F1"]}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:45, title:{display:true,text:'%'} } } }"}},
            body("Violence is reported across all groups, and it is higher among women "
                 "from Scheduled Caste households and poorer households. Caste and wealth "
                 "overlap, so this chart cannot separate their effects. Section 10 returns "
                 "to this overlap.", sm=True),
        ], compact=True),

        C("Attitudes", "Norms that justify violence", [
            stats([card("45%", "women aged 15-49 who agree with one or more of seven "
                        "reasons for a husband to beat his wife", "red", NFHS + ", Ch. 14"),
                   card("44%", "men aged 15-49 who agree with one or more of the reasons",
                        "amber", NFHS + ", Ch. 14")]),
            body("NFHS-5 reports that agreement fell among women since NFHS-4 but rose "
                 "slightly among men. Women's agreement does not mean they welcome "
                 "violence. It shows how far a norm is shared, including by those it "
                 "harms, and why individual awareness campaigns are rarely enough. "
                 "Programmes that work on violence try to shift what a community regards "
                 "as normal, usually by working with groups of women and men over months "
                 "and by making services credible."),
            hbox("Attitude questions are useful for monitoring norm change in a programme "
                 "area. Use the NFHS wording so that results can be compared with the "
                 "state figure.", "indigo"),
        ], compact=True),

        C("PWDVA 2005", "Protection of Women from Domestic Violence Act, 2005", [
            body("The PWDVA gives a civil remedy alongside criminal law. Section 3 defines "
                 "domestic violence broadly, covering physical, sexual, verbal, emotional "
                 "and economic abuse, including harassment for dowry. It protects women in "
                 "a domestic relationship, which includes wives, women in relationships in "
                 "the nature of marriage, mothers, sisters and widows living in the shared "
                 "household."),
            table(["Section", "What it provides"],
                  [["8-9", "Protection Officers appointed by the state to assist women"],
                   ["12", "Application to a Magistrate; first hearing ordinarily within "
                    "three days, disposal within sixty days"],
                   ["17", "Right to reside in the shared household, whether or not she "
                    "owns it"],
                   ["18-22", "Protection, residence, monetary, custody and compensation "
                    "orders"],
                   ["31", "Breach of a protection order: up to one year or fine up to "
                    "Rs 20,000, or both"]]),
            hbox("Source: PWDVA 2005 text (PRS Legislative Research copy). The right of "
                 "residence in s. 17 is often the most valuable remedy for a woman with "
                 "nowhere else to go.", "indigo"),
        ], compact=True),

        C("Criminal law", "Criminal law after 1 July 2024", [
            body("The Bharatiya Nyaya Sanhita, 2023 (BNS) replaced the Indian Penal Code "
                 "from 1 July 2024. Cases arising before that date continue under the old "
                 "sections, so practitioners will meet both numbers."),
            table(["Offence", "IPC section", "BNS section"],
                  [["Cruelty by husband or his relatives", "498A", "85 (cruelty defined "
                    "in 86)"],
                   ["Dowry death", "304B", "80"],
                   ["Rape", "375", "63"]]),
            tw(pp("amber", "Marital rape exception",
                  "BNS section 63, Exception 2, provides that sexual intercourse or sexual "
                  "acts by a man with his own wife, the wife not being under eighteen, is "
                  "not rape. Challenges to the exception are pending before the Supreme "
                  "Court, which issued notice on a further petition in July 2026."),
               pp("cyan", "Dowry Prohibition Act, 1961",
                  "Giving and taking dowry remain offences under this separate Act. A "
                  "PWDVA Magistrate may also frame charges under criminal law where the "
                  "facts disclose an offence (PWDVA s. 31(3)).")),
            hbox("Sources: BNS 2023 text (MHA); commencement 1 July 2024 per MHA "
                 "notification reported by LiveLaw.", "indigo"),
        ], compact=True),

        C("Workplace", "Sexual harassment at work: Vishaka to POSH", [
            body("In <em>Vishaka v State of Rajasthan</em> (1997) 6 SCC 241, decided on 13 "
                 "August 1997, the Supreme Court framed binding guidelines on sexual "
                 "harassment at work after the gang rape of Bhanwari Devi, a government "
                 "social worker who had tried to stop a child marriage. Parliament "
                 "replaced the guidelines with the Sexual Harassment of Women at Workplace "
                 "(Prevention, Prohibition and Redressal) Act, 2013 (POSH Act)."),
            table(["Section", "Requirement"],
                  [["4", "Every employer must constitute an Internal Committee, presided "
                    "over by a senior woman employee, with at least half its members "
                    "women"],
                   ["6", "District Officer constitutes a Local Committee for workplaces "
                    "with fewer than ten workers, or where the complaint is against the "
                    "employer"],
                   ["9", "Complaint within three months of the incident, extendable by "
                    "three months"],
                   ["11(4)", "Inquiry to be completed within ninety days"],
                   ["26", "Employer's non-compliance: fine up to Rs 50,000"]]),
        ], compact=True),

        C("Implementation", "POSH in practice: the gaps", [
            body("In <em>Aureliano Fernandes v State of Goa</em> (12 May 2023) the Supreme "
                 "Court found serious lapses in constituting Internal Committees and directed "
                 "the Union, states and public bodies to comply. On 9 April 2024 the Court "
                 "recorded that affidavits were still awaited from the Union and most "
                 "states. On 13 August 2024 it directed the Union to set out what an online "
                 "dashboard of Internal Committees, their constitution and members, should "
                 "show, and said every state and union territory would have to do the "
                 "same."),
            tw(pp("cyan", "Common failures in organisations",
                  "No committee, or one without an external member. Members untrained in "
                  "inquiry. Complaints routed to the manager accused. No annual report."),
               pp("green", "What an NGO should do",
                  "Constitute the committee, publish its members, train them, cover "
                  "field staff and volunteers, record and report cases, and link to the "
                  "Local Committee for community workers.")),
            hbox("Safeguarding & PSEA 101 covers protection of programme participants, "
                 "which is a separate duty from POSH compliance for staff.", "amber"),
        ], compact=True),

        C("Region", "Domestic violence and harassment law in South Asia", [
            table(["Country", "Law", "Key feature"],
                  [["Bangladesh", "Domestic Violence (Prevention and Protection) Act, 2010",
                    "Civil protection orders; a 2020 study found no cases filed in a "
                    "decade in some districts"],
                   ["Sri Lanka", "Prevention of Domestic Violence Act, No. 34 of 2005",
                    "Civil interim and full protection orders; amendments proposed"],
                   ["Pakistan", "Protection against Harassment of Women at the Workplace "
                    "Act, 2010 (Act IV of 2010)", "Three-member Inquiry Committee in every "
                    "organisation and an Ombudsperson"],
                   ["India", "PWDVA 2005; POSH Act 2013",
                    "Civil remedies plus Internal and Local Committees"]]),
            body("Sources: The Financial Express (Dhaka), 23 December 2020, on an ActionAid "
                 "Bangladesh study; Polity (Colombo), 14 October 2025; Pakistan Act text "
                 "with amendments, Sindh Judicial Academy. A law that nobody uses is a "
                 "signal of weak awareness, distant courts or fear of the consequences at "
                 "home.", sm=True),
        ], compact=True),

        C("Responding", "What a programme does when violence is disclosed", [
            flow(["LISTEN: believe, do not pressure",
                  "SAFETY: ask about immediate danger",
                  "REFER: one-stop centre, 181 helpline, Protection Officer",
                  "RECORD: minimal, confidential, with consent",
                  "FOLLOW UP: only if safe for her"]),
            body("Field staff in any sector will hear disclosures. Each programme needs a "
                 "referral map before it starts: the nearest One Stop Centre, the women's "
                 "helpline, the district Protection Officer, legal aid and health services. "
                 "Staff should never mediate between a woman and her abuser or push her to "
                 "report. Data on violence are personal data of the most harmful kind if "
                 "leaked: collect only what is necessary and protect it now, ahead of the "
                 "duties in the DPDP Act 2023 and the DPDP Rules 2025 that apply from "
                 "13 May 2027."),
            hbox("Research on violence needs specific ethical protocols, such as private "
                 "interviews and one respondent per household. Research Ethics 101 covers "
                 "them.", "amber"),
        ], compact=True),

        # ===================== SECTION 09 =====================
        D("09", "Section Nine", "Political representation"),

        C("Panchayats", "The 73rd and 74th Amendments: one-third and beyond", [
            body("The Constitution (Seventy-third Amendment) Act, 1992 created Part IX on "
                 "panchayats. Article 243D(3) reserves not less than one-third of seats "
                 "filled by direct election in every panchayat for women, including women "
                 "from Scheduled Castes and Tribes, and Article 243D(4) reserves not less "
                 "than one-third of chairperson offices at each level. Article 243T, "
                 "inserted by the 74th Amendment, reserves not less than one-third of "
                 "directly elected municipal seats for women."),
            tw(pp("cyan", "States went further",
                  "Many states have raised the reservation for women in panchayats to 50%. "
                  "An ORF analysis citing UN Women data puts women's share of local body "
                  "seats in India at around 44%."),
               pp("amber", "Rotation",
                  "Reserved seats rotate between constituencies. Rotation spreads "
                  "exposure to women leaders but often prevents a woman from being "
                  "re-elected from a seat that becomes unreserved.")),
            hbox("Source: Constitution of India, Articles 243D and 243T; ORF, 'Lessons from "
                 "30 years of women's reservation in panchayats'.", "indigo"),
        ], compact=True),

        C("Evidence", "What women leaders change: evidence from Indian reservation", [
            table(["Study", "Setting", "Finding"],
                  [["Chattopadhyay and Duflo, <em>Econometrica</em> 72(5), 2004",
                    "Randomly reserved village council headships, West Bengal and "
                    "Rajasthan", "Women leaders invest more in goods women ask for, such "
                    "as drinking water"],
                   ["Beaman, Duflo, Pande and Topalova, <em>Science</em> 335, 2012",
                    "West Bengal villages with reserved leaders in 1998 and 2003",
                    "Narrowed gender gap in parents' aspirations for children; girls spent "
                    "more time in school and less on chores"],
                   ["Iyer, Mani, Mishra and Topalova, <em>AEJ: Applied</em> 4(4), 2012",
                    "State timing of reservation", "More documented crimes against women, "
                    "driven mainly by greater reporting"]]),
            body("Because reservation was assigned by rotation that was close to random, "
                 "these studies give unusually credible causal evidence on women's "
                 "leadership. The Beaman study found that attitudes changed only after a "
                 "second round of exposure to a woman leader.", sm=True),
        ], compact=True),

        C("Proxy leaders", "Proxies, capacity and real authority", [
            body("Reservation brought large numbers of first-time women leaders into "
                 "office. In some places a husband or male relative runs the office in "
                 "practice, a pattern known as 'sarpanch pati' or 'pradhan pati'. Reports "
                 "of proxy representation continue, and the ORF analysis cites media and "
                 "civil society documentation of it."),
            tw(pp("red", "Why proxies persist",
                  "Low literacy among some elected women, norms on women dealing with "
                  "officials, male control of party and contractor networks, and short "
                  "tenure under rotation."),
               pp("green", "What reduces them",
                  "Training for elected women, women's collectives that back their "
                  "representatives, rules that require the elected member's own presence "
                  "and signature, and Mahila Sabhas before Gram Sabhas.")),
            hbox("Proxy cases are real, but the causal studies on the previous slide show "
                 "that reserved seats still change policy and aspirations on average. Both "
                 "findings are true at once.", "amber"),
        ], compact=True),

        C("Parliament", "Women in Parliament across South Asia", [
            {"t": "chart", "canvas": "gdParlChart",
             "title": "Proportion of seats held by women in national parliaments (%), "
                      "latest year",
             "source": "World Bank WDI, SG.GEN.PARL.ZS (IPU data), accessed October 2026. "
                       "Years: Nepal 2024, Bangladesh 2023, others 2025",
             "type": "bar",
             "data": {"labels": ["Nepal", "Bangladesh", "Pakistan", "India", "Sri Lanka",
                                 "Bhutan", "Maldives"],
                      "datasets": [{"label": "Women's share of seats",
                                    "data": [33.1, 20.9, 17.0, 13.8, 9.8, 4.3, 3.2],
                                    "backgroundColor": "#10B981"}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:40, title:{display:true,text:'% of seats'} } } }"}},
            body("Nepal's Constitution of 2015 (Article 84(8)) requires that women account "
                 "for at least one-third of each party's members elected to the Federal "
                 "Parliament. India elected 74 women to the 18th Lok Sabha in 2024, 13.6% "
                 "of members, down from 78 in 2019 (WION, June 2024).", sm=True),
        ], compact=True),

        C("The 2023 Adhiniyam", "Nari Shakti Vandan Adhiniyam: what the text says", [
            body("The Constitution (One Hundred and Sixth Amendment) Act, 2023, known as the "
                 "Nari Shakti Vandan Adhiniyam, inserted Article 330A (Lok Sabha), Article "
                 "332A (state Legislative Assemblies) and Article 239AA changes for Delhi. "
                 "As nearly as may be, one-third of seats are reserved for women, including "
                 "one-third of the seats reserved for Scheduled Castes and Scheduled "
                 "Tribes."),
            term("Article 334A: the condition",
                 "The reservation comes into effect after a delimitation undertaken for "
                 "this purpose, after the relevant figures of the first census taken after "
                 "the commencement of the 2023 Act have been published. Clause (1) says it "
                 "ceases to have effect fifteen years 'from such commencement', clause (2) "
                 "lets Parliament continue the seats by law, and clause (3) rotates "
                 "reserved seats after each subsequent delimitation."),
            hbox("Source: Constitution of India, Legislative Department edition as on 1 May "
                 "2024, Articles 330A and 334A. The reservation does not extend to the "
                 "Rajya Sabha or state Legislative Councils.", "indigo"),
        ], compact=True),

        C("Status in 2026", "Implementation: where things stand, October 2026", [
            table(["Date", "Event"],
                  [["September 2023", "Parliament passes the 106th Amendment"],
                   ["16 April 2026", "Government notifies the Act into force; seats still "
                    "not reserved because Article 334A requires census and delimitation"],
                   ["16-17 April 2026", "Constitution (131st Amendment) Bill, 2026, to "
                    "advance implementation through earlier delimitation, is introduced and "
                    "defeated in the Lok Sabha: 298 votes, short of the 352 needed"],
                   ["1 March 2027", "Census reference date, with caste enumeration"],
                   ["After publication", "Delimitation, then reservation takes effect"]]),
            body("Sources: LiveLaw, 17 April 2026, on the notification of 16 April and "
                 "the vote (298 of 528 members present and voting); SCC Online, 17 April "
                 "2026, on the Bill's content. Watch for the census publication date and "
                 "the delimitation commission's terms.", sm=True),
        ], compact=True),

        C("Debates", "Debates around the reservation", [
            tw([panel("cyan", "Arguments made for", [bullets([
                    "Panchayat evidence shows reserved seats change policy",
                    "Women's share of the Lok Sabha has stayed below 15%",
                    "Parties have not nominated women voluntarily"], sm=True)])],
               [panel("amber", "Concerns raised", [bullets([
                    "Delay through the census and delimitation link",
                    "No sub-quota for OBC women",
                    "Rotation weakens incumbents' incentive to serve the seat",
                    "Elite capture by women from political families"], sm=True)])]),
            body("These are positions taken in public and parliamentary debate. The "
                 "constitutional text includes Scheduled Caste and Tribe women within the "
                 "one-third, and has no OBC sub-quota because the Constitution has no OBC "
                 "reservation in legislatures. Present both sides fairly when you teach "
                 "or advocate on this question.", sm=True),
            hbox("Indian Constitution 101 covers amendment procedure under Article 368, "
                 "which explains why the 131st Amendment Bill needed a two-thirds "
                 "majority of those present and voting.", "indigo"),
        ], compact=True),

        C("Beyond seats", "Representation beyond legislatures", [
            table(["Site of voice", "Gender question", "Where to look"],
                  [["Gram Sabha", "Do women attend and speak?",
                    "Attendance registers; Mahila Sabha minutes"],
                   ["Bureaucracy", "Share of women in district posts",
                    "State cadre lists"],
                   ["Judiciary", "Women judges and the treatment of women litigants",
                    "Court statistics"],
                   ["Unions and cooperatives", "Women in leadership",
                    "Cooperative registers, union records"],
                   ["Programme committees", "Women on school management, water and "
                    "health committees", "Programme MIS"]]),
            body("Many schemes require women's membership in user committees. Check whether "
                 "they hold office, attend, and influence decisions. A committee with "
                 "women members that never meets is a paper reform. Governance & "
                 "Accountability 101 covers these institutions.", sm=True),
        ], compact=True),

        # ===================== SECTION 10 =====================
        D("10", "Section Ten", "Masculinities and intersectionality"),

        C("Masculinities", "Masculinities: men are gendered too", [
            body("R. W. Connell's <em>Masculinities</em> (1995) argued that there are "
                 "several masculinities in any society, ranked against each other. "
                 "'Hegemonic masculinity' is the form most honoured at a given time and "
                 "place, which most men do not fully live up to but which shapes what they "
                 "are expected to be."),
            tw(pp("cyan", "South Asian forms",
                  "Ideals of the provider, the protector of family honour, the son who "
                  "carries the lineage and the man who controls women's mobility. Caste and "
                  "class change which ideal applies and what it costs."),
               pp("green", "Why programmes care",
                  "Unemployment, migration and debt threaten the provider ideal, and men "
                  "who cannot meet it may assert control in other ways. Working with men "
                  "on these norms is part of preventing violence, alongside services and "
                  "law.")),
            stats([card("57%", "men aged 15-49 who say a wife should have an equal or "
                        "greater say in all five specified decisions", "cyan",
                        NFHS + ", Ch. 14")], cols=1),
        ], compact=True),

        C("Working with men", "Approaches to working with men and boys", [
            table(["Approach", "What it does", "Risk"],
                  [["Men as clients", "Services for men's health and well-being",
                    "Diverts funds from women's services"],
                   ["Men as partners", "Couples' sessions, fathers in child care",
                    "Reinforces men as decision-makers"],
                   ["Men as agents of change", "Group education on gender norms, men "
                    "speaking against violence", "Rewarding men for minimal change"],
                   ["Norm-changing", "Questions the norms themselves with both "
                    "sexes", "Slow, needs skilled facilitation"]]),
            body("Good practice keeps accountability to women: women's organisations help "
                 "set the agenda, and outcomes are measured in women's lives, such as less "
                 "violence and more say, as well as in men's attitudes. School programmes "
                 "with adolescent boys and girls together are a common South Asian "
                 "entry point.", sm=True),
            hbox("A programme that works with men should report what changed for women, "
                 "measured by asking women.", "amber"),
        ], compact=True),

        C("Intersectionality", "Intersectionality: Crenshaw and beyond", [
            body("Kimberle Crenshaw introduced the term in 'Demarginalizing the intersection "
                 "of race and sex' (<em>University of Chicago Legal Forum</em>, 1989). "
                 "Analysing a US employment case, she showed that Black women could fall "
                 "between discrimination claims based on race alone and on sex alone. Their "
                 "experience was produced by both at once."),
            term("Intersectionality",
                 "The analysis of how social categories such as gender, caste, class, "
                 "religion, disability, age and sexuality combine to produce specific "
                 "forms of advantage and disadvantage that cannot be understood by "
                 "looking at one category at a time."),
            hbox("In South Asia the most consequential intersection is gender with caste. "
                 "Dalit feminists in India were making this argument before the term "
                 "travelled from the United States, and Caste Studies 101 takes it "
                 "further.", "indigo"),
        ], compact=True),

        C("Caste and gender", "Gender and caste: how they combine", [
            tw(pp("cyan", "Control over women's sexuality",
                  "Uma Chakravarti (<em>Gendering Caste: Through a Feminist Lens</em>) "
                  "argues that caste endogamy depends on controlling women's marriage and "
                  "sexuality, which she calls Brahmanical patriarchy. Restrictions on women's "
                  "mobility and 'honour' violence often enforce caste boundaries."),
               pp("green", "Dalit and Adivasi women",
                  "Dalit and Adivasi women face caste discrimination, gender discrimination "
                  "and poverty together. They are more often in casual agricultural labour "
                  "and face violence linked to caste assertion.")),
            table(["Spousal physical or sexual violence (ever)", "Value"],
                  [["Scheduled Caste women", "34.7%"],
                   ["Scheduled Tribe women", "31.8%"],
                   ["OBC women", "30.2%"],
                   ["Other women", "22.6%"]]),
            body("Source: " + NFHS + ", Table 15.11. A paradox worth teaching: in some "
                 "upper-caste households women's paid work outside the home has been "
                 "restricted as a status marker, so higher caste can mean lower "
                 "participation.", sm=True),
        ], compact=True),

        C("Religion and more", "Religion, disability, sexuality and gender identity", [
            table(["Identity", "Example of intersecting disadvantage", "Data point to check"],
                  [["Religion", "Muslim women's lower participation in paid work in some "
                    "states", "PLFS by religion"],
                   ["Disability", "Women with disabilities face higher violence and lower "
                    "schooling", "NFHS-5 disability questions; Disability Inclusion 101"],
                   ["Age", "Widows' loss of land and status", "Census marital status"],
                   ["Sexuality and gender identity", "Transgender persons' exclusion from "
                    "work and services", "Transgender Persons (Protection of Rights) Act, "
                    "2019"],
                   ["Migration", "Wives of migrants managing farms without titles",
                    "PLFS migration modules"]]),
            body("NFHS-5 reports ever-experienced spousal physical or sexual violence at "
                 "29.9% among Hindu and 27.5% among Muslim ever-married women (Table "
                 "15.11), a smaller difference than the gap between the poorest (38.4%) "
                 "and richest (16.9%) wealth quintiles. Check region, wealth and "
                 "education before attributing a gap to religion.", sm=True),
            hbox("Intersectional analysis needs sample sizes large enough for subgroups. "
                 "Plan for it at the sampling stage.", "amber"),
        ], compact=True),

        C("Method", "Doing intersectional analysis in practice", [
            flow(["DISAGGREGATE: by sex and one other axis at a time",
                  "CROSS: sex by caste, sex by wealth, sex by disability",
                  "CONTROL: check whether a gap survives other factors",
                  "LISTEN: qualitative work with the groups at the intersection"]),
            tw(pp("cyan", "Quantitative",
                  "Cross-tabulate, use interaction terms in regressions, report confidence "
                  "intervals for small groups, and avoid over-interpreting a single cell."),
               pp("green", "Qualitative",
                  "Purposive sampling of women at specific intersections, life histories, "
                  "focus groups held separately so that dominant groups do not speak for "
                  "others.")),
            body("Data Feminism 101 asks who collects data and who is counted. Social Margins "
                 "101 covers the groups most often left out of surveys altogether, such as "
                 "the homeless and nomadic communities.", sm=True),
        ], compact=True),

        # ===================== SECTION 11 =====================
        D("11", "Section Eleven", "Practical application: gender analysis"),

        C("Frameworks", "Four gender analysis frameworks compared", [
            table(["Framework", "Core question", "Best used for"],
                  [["Harvard Analytical Framework", "Who does what, who has access to and "
                    "control over which resources?", "Project data collection: activity "
                    "and access profiles"],
                   ["Moser framework", "Which roles do women carry, and which practical and "
                    "strategic needs does the plan meet?", "Planning and policy review"],
                   ["Social Relations Approach (Kabeer)", "How do institutions (household, "
                    "community, market, state) produce inequality?", "Institutional and "
                    "power analysis"],
                   ["Gender Analysis Matrix", "What changes for women, men, households and "
                    "the community in labour, time, resources and culture?",
                    "Participatory review with communities"]]),
            body("Source: March, Smyth and Mukhopadhyay, <em>A Guide to Gender-Analysis "
                 "Frameworks</em> (Oxfam, 1999). Frameworks are aids to thinking. Choose "
                 "the one that answers your question and adapt its categories to the "
                 "local setting.", sm=True),
        ], compact=True),

        C("Activity profile", "Tool one: activity and access profile", [
            table(["Activity or resource (dairy, Illustrative)", "Women", "Men",
                   "Who controls"],
                  [["Feeding and milking", "Mostly", "Sometimes", "-"],
                   ["Taking milk to the collection centre", "Sometimes", "Mostly", "-"],
                   ["Membership of the cooperative", "Few", "Most", "Men"],
                   ["Milk payment", "Rarely", "Usually", "Men"],
                   ["Decision to buy or sell an animal", "Consulted", "Decides", "Men"]]),
            body("This is an Illustrative profile of the kind a team fills in with women "
                 "and men separately in a village meeting. It shows quickly that a "
                 "programme raising milk yields would add to women's work while the income "
                 "and decisions sit with men. The design response is to enrol women as "
                 "cooperative members in their own right and pay milk money into their "
                 "own accounts.", sm=True),
            hbox("Fill in the profile with women and men separately, then compare. "
                 "Disagreements between the two versions are findings.", "amber"),
        ], compact=True),

        C("Checklist", "A gender checklist for programme design", [
            tw([panel("cyan", "Analysis", [bullets([
                    "Sex-disaggregated baseline for every outcome",
                    "Activity, access and control profile done with women",
                    "Time-use estimate of what the programme adds",
                    "Risks of backlash or violence identified",
                    "Intersections: caste, religion, disability, age"], sm=True)])],
               [panel("green", "Design and monitoring", [bullets([
                    "Benefits, titles and accounts in women's names or joint",
                    "Meeting times, places and child care set with women",
                    "Practical and strategic needs both addressed",
                    "POSH committee and safeguarding in place",
                    "Indicators for resources, agency and achievements"], sm=True)])]),
            body("Use the checklist at design, at mid-term review and before scale-up. "
                 "Each item corresponds to a section of this course, so a 'no' points to "
                 "the section to revisit. Programme Design 101 and Theory of Change 101 "
                 "show where these items sit in a full design.", sm=True),
            hbox("A checklist is a prompt for discussion with women in the programme area. "
                 "It does not replace that discussion.", "amber"),
        ], compact=True),

        C("Indicators", "Choosing gender indicators", [
            table(["Kabeer dimension", "Indicator example", "Data source"],
                  [["Resources", "Share of programme assets titled to women",
                    "Programme records"],
                   ["Resources", "Women's own income in the last month", "Survey"],
                   ["Agency", "Woman decides alone or jointly on use of her earnings",
                    "Survey using NFHS wording"],
                   ["Agency", "Woman can visit the market or health facility alone",
                    "Survey using NFHS wording"],
                   ["Achievements", "Girls' secondary completion; women's anaemia",
                    "Survey; health records"],
                   ["Norms", "Agreement with reasons for wife beating, women and men",
                    "Survey using NFHS wording"]]),
            body("Report each indicator for women and men where it applies, at baseline and "
                 "endline. Using NFHS wording lets you compare your programme area with "
                 "the district or state figure. MEL Basics 101 and Logframe 101 show how "
                 "to set targets and means of verification.", sm=True),
        ], compact=True),

        C("Worked example", "Worked example: a women's livelihood programme in Bihar", [
            body("<strong>Illustrative case (hypothetical figures).</strong> An NGO plans to train 2,000 women in "
                 "self-help groups in goat rearing and connect them to buyers. The team "
                 "applies the tools from this course."),
            table(["Tool", "Finding (Illustrative)", "Design change"],
                  [["Activity profile", "Men sell goats at the weekly market",
                    "Collective sales by the group, payment to women's accounts"],
                   ["Time use", "Grazing adds about two hours a day",
                    "Stall-feeding and shared grazing rotations"],
                   ["Bargaining", "Husbands may claim sale proceeds",
                    "Couples' sessions; goats registered in women's names"],
                   ["Intersection", "Landless Dalit women lack fodder access",
                    "Fodder plots on common land, priority enrolment"],
                   ["Risk", "Some disclosures of violence expected",
                    "Referral map, trained staff, POSH committee"]]),
            hbox("The design now meets a practical need (income) in a way that builds "
                 "strategic gains (ownership, collective bargaining).", "green"),
        ], compact=True),

        C("Decision table", "When does a programme change gender relations?", [
            table(["Type", "What it does", "Example"],
                  [["Gender-blind", "Ignores gender differences",
                    "Training scheduled when women cannot attend"],
                   ["Gender-aware or sensitive", "Recognises differences and adjusts "
                    "delivery", "Separate sessions for women"],
                   ["Gender-responsive", "Meets women's specific needs",
                    "Creche at the worksite"],
                   ["Relation-changing", "Changes the underlying relations and norms",
                    "Joint land titles plus community work on inheritance"]]),
            body("Most programmes sit in the middle. Be accurate in proposals and reports: "
                 "claiming transformation for a programme that adjusts meeting times "
                 "undermines credibility with funders and with the women involved. A "
                 "modest, well-delivered gender-responsive programme is a good programme. "
                 "Gender Mainstreaming 101 covers the continuum in organisational "
                 "practice.", sm=True),
            hbox("Ask of any claim of transformation: which relation changed, for whom, and "
                 "what evidence shows it.", "indigo"),
        ], compact=True),

        # ===================== SECTION 12 =====================
        D("12", "Section Twelve", "Bringing it together"),

        C("Common mistakes", "Six common mistakes in gender work", [
            table(["Mistake", "Why it happens", "Correction"],
                  [["Counting women as the result", "Easy to report",
                    "Measure what changed in their resources and agency"],
                   ["Assuming household pooling", "Unitary model habit",
                    "Decide and record whose name is on the benefit"],
                   ["Ignoring time", "Unpaid work is invisible",
                    "Estimate added hours; reduce other burdens"],
                   ["Treating women as one group", "Simple categories",
                    "Disaggregate by caste, class, age, disability"],
                   ["Leaving out men", "Fear of diluting focus",
                    "Work with men, accountable to women"],
                   ["Mixing data sources", "Convenience",
                    "One source per comparison; state the definition"]]),
            body("Each mistake corresponds to a concept from this course. Return to the "
                 "relevant section when a programme review raises one of them.", sm=True),
        ], compact=True),

        C("Summary", "Ten ideas to take away", [
            tw([panel("cyan", "Concepts", [bullets([
                    "Gender is social, relational and changeable",
                    "GAD analyses power between women and men",
                    "Practical needs can open strategic gains",
                    "Resources, agency and achievements differ",
                    "Households bargain; they do not simply pool"], sm=True)])],
               [panel("green", "Evidence and practice", [bullets([
                    "Missing girls reflect son preference meeting technology",
                    "Women's work is undercounted unless asked carefully",
                    "Women who do unpaid domestic work spend 289 minutes a day on it",
                    "Violence is common and help-seeking is rare",
                    "Reserved seats change policy, slowly and unevenly"], sm=True)])]),
            body("Behind each idea is a source you can open: NFHS-5, PLFS, the Time Use "
                 "Survey, the Constitution and the statutes cited. Check the latest round "
                 "before you use a figure, since PLFS, SRS and NFHS all publish new rounds "
                 "and the women's reservation timeline is still moving.", sm=True),
            hbox("Gender analysis is a habit of asking who does, who has, who decides and "
                 "who benefits, for every activity in a programme.", "indigo"),
        ], compact=True),

        C("Where next", "Where next: related 101 decks", [
            tw([panel("cyan", "Go deeper on gender", [body(
                    "<a href=\"/101-courses/gender-mainstreaming.html\">Gender Mainstreaming "
                    "101</a> for gender budgeting and mainstreaming in institutions. "
                    "<a href=\"/101-courses/wee-studies.html\">Women's Economic Empowerment "
                    "101</a> for livelihoods, credit and enterprise. "
                    "<a href=\"/101-courses/care-economy-101.html\">Care Economy 101</a> for "
                    "unpaid care, valuation and care policy. "
                    "<a href=\"/101-courses/feminist-research.html\">Feminist Research 101</a> "
                    "and <a href=\"/101-courses/data-feminism.html\">Data Feminism 101</a> "
                    "for research practice. The <a href=\"/courses/gender/\">Gender "
                    "flagship course</a> goes further on every section.", sm=True)])],
               [panel("green", "Related fields", [body(
                    "<a href=\"/101-courses/caste-studies.html\">Caste Studies 101</a> and "
                    "<a href=\"/101-courses/social-margins.html\">Social Margins 101</a> for "
                    "intersections. <a href=\"/101-courses/SRHR-basics.html\">Sexual Health "
                    "101</a> and <a href=\"/101-courses/maternal-health.html\">Maternal "
                    "Health 101</a> for health. "
                    "<a href=\"/101-courses/safeguarding-psea.html\">Safeguarding &amp; PSEA "
                    "101</a> for protection. "
                    "<a href=\"/101-courses/work-labour-livelihoods.html\">Work, Labour &amp; "
                    "Livelihoods 101</a> for labour law and the Codes. "
                    "<a href=\"/101-courses/ind-constitution.html\">Indian Constitution "
                    "101</a> for the amendments.", sm=True)])]),
            hbox("Suggested order: Gender Mainstreaming, then WEE or Care Economy depending "
                 "on your work, then the Gender flagship course.", "indigo"),
        ], compact=True),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Gender &amp; Development 101",
         "headline": "Ask who does, who has, who decides and who benefits",
         "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development "
                   "practitioners in South Asia",
         "ctas": [{"label": "Gender flagship course", "href": "/courses/gender/"},
                  {"label": "Gender Mainstreaming 101",
                   "href": "/101-courses/gender-mainstreaming.html"},
                  {"label": "All 101 courses", "href": "/101-courses/"}],
         "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]},
    ],
}

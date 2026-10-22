# -*- coding: utf-8 -*-
"""
Water, Sanitation and Hygiene 101 - ImpactMojo 101 Series (native deck spec)
WASH for Indian development practitioners: the WHO/UNICEF JMP service ladders,
India's figures from the JMP, NFHS-4, NFHS-5, NFHS-6 and the NSS 76th round,
Swachh Bharat Mission (Grameen and Urban) and the gap between ODF declarations
and survey evidence, Jal Jeevan Mission and its functionality assessment,
groundwater depletion and contamination, water governance, faecal sludge,
sanitation workers and the 2013 Act on manual scavenging, handwashing and
menstrual health, climate and drought, and how to monitor a WASH programme.
Build: python3 scripts/deck-builder/build.py wash

Every figure on a slide names its source. Sources were opened in October 2026
and are listed on the final content slide with links.
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


def chart(canvas, title, source, ctype, data, options):
    return {"t": "chart", "canvas": canvas, "title": title, "source": source,
            "type": ctype, "data": data, "options": {"__js__": options}}


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


# Source labels used on slides
JMP = "WHO/UNICEF JMP country file, India, updated August 2025"
NSS = "NSS Report No. 584, 76th round (July-December 2018), NSO, 2019"
N5 = "NFHS-5 India fact sheet, IIPS, via MoSPI eSankhyiki"
N6 = "NFHS-6 India fact sheet (provisional), IIPS, May 2026"
YER = "DDWS Year End Review 2025, PIB"
SBMN = "DDWS note on SBM(G) Phase II, January 2026"
FA = "JJM Functionality Assessment 2022, national report"
GW = "Ministry of Jal Shakti, PIB, 18 December 2025"
GWQ = "Ministry of Jal Shakti, PIB, 10 March 2025"
RICE = "Gupta et al., IZA Discussion Paper 12065, 2019"
SBMU = "SBM-Urban 2.0 portal, sbmurban.org, read October 2026"
NAM = "Ministry of Social Justice, PIB, 1 April 2026"
MSA = "Ministry of Social Justice, PIB, 25 July 2023"
WOLF = "Wolf et al., Lancet, 2023"

SLIDES_A = [

    # ===================== TITLE =====================
    {"type": "title",
     "main": "Water,<br>Sanitation<br>&amp; Hygiene 101",
     "sub": "The JMP service ladders, India's numbers and how they disagree, Swachh "
            "Bharat, Jal Jeevan, groundwater, sanitation work and the law, hygiene, "
            "and how to monitor a WASH programme",
     "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Public Health"]},

    # ===================== TOC =====================
    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Why WASH matters and what it covers"},
         {"name": "The JMP service ladders"},
         {"name": "India's numbers from the JMP, NFHS and NSS"},
         {"name": "What Swachh Bharat Mission built"},
         {"name": "ODF claims and the survey evidence"},
         {"name": "Jal Jeevan Mission, from taps to working water"},
         {"name": "Groundwater depletion and contamination"},
         {"name": "Who governs water and sanitation"},
         {"name": "Faecal sludge, sanitation work and the 2013 Act"},
         {"name": "Handwashing and menstrual health"},
         {"name": "Climate, drought and water security"},
         {"name": "Monitoring a WASH programme"},
     ]},

    # ===================== SECTION 01 =====================
    D("01", "Section One", "Why WASH matters and what it covers"),

    C("Definitions", "Three services that block one route of infection", [
        body("WASH stands for water, sanitation and hygiene. <strong>Water</strong> means "
             "drinking water that is close, available when it is needed and free of "
             "contamination. <strong>Sanitation</strong> means a toilet that separates "
             "excreta from human contact and a chain of services that keeps it separated "
             "until it is treated or safely buried. <strong>Hygiene</strong> means the "
             "practices that keep hands, food and water clean, above all washing hands "
             "with soap, and the facilities that make those practices possible, including "
             "for menstruation."),
        tw(pp("cyan", "Why the three are taught together",
              "Diarrhoea, worm infections and many enteric infections travel the same way, "
              "from one person's faeces to another person's mouth. Each service blocks a "
              "different stretch of that route. A toilet keeps faeces out of the "
              "environment, safe water keeps them out of the drink, and soap keeps them "
              "off the hands that prepare food and feed children."),
           pp("amber", "Why they are run separately",
              "In India the three sit in different programmes. Drinking water is Jal "
              "Jeevan Mission, rural sanitation is Swachh Bharat Mission (Grameen), urban "
              "sanitation is Swachh Bharat Mission (Urban), and hygiene is scattered "
              "across health, education and both missions. A district officer sees three "
              "dashboards for one route of infection.")),
        hbox("This course follows the route of infection first and the programmes "
             "second, because a child is exposed through whichever barrier is weakest.",
             "indigo"),
    ], compact=True),

    C("The burden", "Unsafe WASH still kills on the scale of a major disease", [
        stats([card("1.4 million", "deaths in 2019 that safe WASH could have prevented, "
                    "worldwide", "red", WOLF),
               card("74 million", "disability-adjusted life-years lost in the same year",
                    "amber", WOLF),
               card("2.5%", "of all deaths worldwide in 2019 attributable to unsafe WASH",
                    "indigo", WOLF)]),
        chart("washBurdenChart",
              "Share of each outcome attributable to unsafe WASH, world, 2019 (%)",
              "Wolf et al., Lancet, 2023, doi:10.1016/S0140-6736(23)00458-0",
              "bar",
              {"labels": ["Diarrhoea", "Acute respiratory infections", "Undernutrition"],
               "datasets": [{"label": "Attributable fraction (%)", "data": [69, 14, 10],
                             "backgroundColor": ["#EF4444", "#F59E0B", "#0EA5E9"]}]},
              "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:80, title:{display:true,text:'% attributable'} } } }"),
        body("The estimate uses the SDG service ladders as the yardstick, so a household "
             "counts as exposed until it reaches safely managed water and sanitation and "
             "basic hygiene. Soil-transmitted helminth infection is attributed wholly to "
             "unsafe WASH. Treat the figures as a model of what full coverage could avert, "
             "and note the authors' own counterfactual is the SDG target.", sm=True),
    ], compact=True),

    C("Pathways", "The F-diagram shows how faeces reach a mouth", [
        flow(["Faeces", "Fluids", "Fingers", "Flies", "Fields", "Food", "New host"]),
        body("Public health teaching draws transmission as the F-diagram. Pathogens leave "
             "an infected person in faeces and reach the next person through water, hands, "
             "flies, soil and the food that all of these touch. Barriers work at two "
             "points. Primary barriers stop faeces entering the environment at all. They "
             "include a toilet that is used, safe disposal of children's faeces and safe "
             "emptying of pits and tanks. Secondary barriers stop contamination already in "
             "the environment from reaching the mouth. They include handwashing, safe "
             "water storage and treatment, and food hygiene."),
        tw(pp("green", "Primary barriers",
              "A latrine that every member uses, safe disposal of small children's "
              "faeces, and a pit or tank that is emptied and treated without exposing "
              "workers or neighbours."),
           pp("cyan", "Secondary barriers",
              "Handwashing with soap after defecation, after cleaning a child and before "
              "food. Covered storage and household treatment. The NSS 76th round found "
              "65.3% of households did not treat drinking water, 72.8% in rural areas "
              "(" + NSS + ", Statement 8).")),
    ], compact=True),

    C("A public good", "Sanitation protects the neighbours as much as the owner", [
        body("A household that builds and uses a toilet lowers the exposure of every child "
             "nearby. A household that defecates in the open raises it, whatever the "
             "neighbours do. That spillover is why sanitation behaves like a public good "
             "and why health gains depend on how many people in a village stop open "
             "defecation, as well as on whether any single family has a latrine."),
        tw(pp("indigo", "The district evidence",
              "Spears, Ghosh and Cumming matched HUNGaMA 2011 stunting data from 112 "
              "districts with Census 2011 open defecation. After adjusting for wealth, "
              "maternal education and calorie availability, a 10 percentage point rise in "
              "open defecation was associated with a 0.7 point rise in stunting (PLoS ONE, "
              "2013). The design is ecological, and the authors say so."),
           pp("amber", "What that means for a programme",
              "A target of a toilet in each house measures construction. A target that "
              "matters for health counts the share of people in a settlement who use one, "
              "and how faeces are handled afterwards. Section 5 shows how far those two "
              "kinds of number have drifted apart in India.")),
        hbox("Coverage thresholds matter. A village at 60% use can still have enough "
             "faeces in its lanes and ponds to keep children sick.", "amber"),
    ], compact=True),

    C("Four measurements", "Access, use, safety and function are separate numbers", [
        table(["Measurement", "Question it answers", "Typical source in India", "What it misses"],
              [["Access", "Does the household have a toilet or a water source?",
                "Census, NSS, NFHS, SBM and JJM records", "Whether anyone uses it"],
               ["Use", "Does each member use it every time?",
                "Individual questions in NSS 76 and r.i.c.e. surveys",
                "Self-report bias, children's faeces"],
               ["Safety", "Is the water clean, is excreta contained and treated?",
                "Lab tests, JMP safely managed rungs", "Rarely measured at household level"],
               ["Function", "Does the tap give enough water every day?",
                "JJM Functionality Assessment", "Seasonal failure between survey rounds"]]),
        body("Most public claims about WASH in India are claims about access, because "
             "access is what a construction programme can count. Use, safety and function "
             "are harder to measure and they are the measurements that decide whether "
             "children get sick. When a report gives one number, ask which of the four "
             "it is."),
        hbox("Throughout the deck each figure is labelled with the measurement it "
             "represents and the survey or record it comes from.", "indigo"),
    ], compact=True),

    C("Who carries the burden", "Water collection, distance and caste shape who goes without", [
        tw(pp("cyan", "Distance and drudgery",
              "In 2018, 58.2% of rural households and 80.7% of urban households had "
              "drinking water within their premises (" + NSS + "). Someone in the other "
              "households walks to fetch it, and that person is usually a woman or a "
              "girl. In the JJM Functionality Assessment 2022, 79% of households where "
              "women used to fetch water reported less drudgery after a tap was installed "
              "(" + FA + ")."),
           pp("amber", "Caste and class",
              "The same NSS round found 71.3% of rural households had access to a "
              "latrine, against 62.8% of Scheduled Caste and 63.3% of Scheduled Tribe "
              "rural households. Across rural consumption quintiles access rose from "
              "53.5% in the poorest fifth to 86.7% in the richest (NSS 76th round, via "
              "MoSPI eSankhyiki).")),
        stats([card("58.2%", "rural households with drinking water within premises, 2018",
                    "cyan", NSS),
               card("62.8%", "rural SC households with latrine access, 2018", "amber",
                    "NSS 76th round, via MoSPI eSankhyiki"),
               card("79%", "of formerly water-fetching households report less drudgery "
                    "with a tap", "green", FA)]),
    ], compact=True),

    C("Course map", "How the twelve sections fit together", [
        flow(["Why WASH", "Ladders", "India's numbers", "Swachh Bharat", "ODF evidence", "Jal Jeevan",
              "Groundwater", "Governance", "Sludge and workers", "Hygiene", "Climate",
              "Monitoring"]),
        tw(pp("cyan", "What you will be able to do",
              "Read a JMP ladder and explain each rung. Reconcile a government ODF claim "
              "with NSS, NFHS and independent survey figures. Read a JJM dashboard number "
              "alongside the functionality assessment. Look up your block's groundwater "
              "category and contamination record. Explain the 2013 Act on manual "
              "scavenging and what NAMASTE does. Design a monitoring plan that measures "
              "use and function as well as construction."),
           pp("green", "Who this is for",
              "Programme staff in NGOs and CSR teams, district and block officials, "
              "evaluators, journalists and students who meet WASH numbers and need to "
              "know what sits behind them. No engineering background is assumed. For a "
              "reading list on behaviour and toilet use, see the ImpactMojo Deep Dive "
              "<em>Water, Sanitation, and the Behaviour Gap</em>.")),
        hbox("Figures are current to October 2026. Survey rounds named on each slide tell "
             "you how old the underlying data are.", "indigo"),
    ], compact=True),

    # ===================== SECTION 02 =====================
    D("02", "Section Two", "The JMP service ladders"),

    C("SDG 6", "Targets 6.1 and 6.2 and how the JMP measures them", [
        body("The WHO/UNICEF Joint Monitoring Programme (JMP) is the custodian of the "
             "global indicators for SDG targets 6.1 (drinking water) and 6.2 (sanitation "
             "and hygiene). It publishes an estimate for every country from national "
             "surveys, censuses and administrative records, using one set of definitions "
             "so that countries and years can be compared."),
        term("Safely managed drinking water",
             "Drinking water from an improved water source that is accessible on premises, "
             "available when needed and free from faecal and priority chemical "
             "contamination (JMP)."),
        term("Safely managed sanitation",
             "Use of improved facilities that are not shared with other households and "
             "where excreta are safely disposed of in situ or removed and treated "
             "off-site (JMP)."),
        term("Basic hygiene",
             "Availability of a handwashing facility with soap and water at home (JMP)."),
        hbox("Each definition stacks conditions. A household fails the top rung if any one "
             "condition fails, which is why safely managed figures fall well below access "
             "figures.", "amber"),
    ], compact=True),

    C("Drinking water ladder", "Five rungs from surface water to safely managed", [
        table(["Rung", "JMP definition"],
              [["Safely managed", "Improved source, accessible on premises, available when "
                "needed, free from faecal and priority chemical contamination"],
               ["Basic", "Improved source, collection time not more than 30 minutes for a "
                "round trip, including queuing"],
               ["Limited", "Improved source for which collection time exceeds 30 minutes "
                "for a round trip, including queuing"],
               ["Unimproved", "Unprotected dug well or unprotected spring"],
               ["Surface water", "Directly from a river, dam, lake, pond, stream, canal or "
                "irrigation canal"]]),
        tw(pp("cyan", "What counts as improved",
              "These are sources that by design can deliver safe water, such as piped "
              "water, boreholes and tubewells, protected dug wells and springs, rainwater and "
              "packaged or delivered water. The NFHS-6 footnote lists piped water, public "
              "taps, tubewells, protected wells and springs, rainwater, tanker trucks, "
              "carts with small tanks, bottled water and community RO plants (" + N6 + ")."),
           pp("amber", "The 30-minute line",
              "Time is measured as a round trip including the queue. A protected well an "
              "hour away is improved and still only a limited service. Surveys ask the "
              "time, so the line depends on the respondent's estimate.")),
    ], compact=True),

    C("Sanitation ladder", "Five rungs from open defecation to safely managed", [
        table(["Rung", "JMP definition"],
              [["Safely managed", "Improved facility, not shared, excreta safely disposed "
                "of in situ or removed and treated off-site"],
               ["Basic", "Improved facility not shared with other households"],
               ["Limited", "Improved facility shared with other households"],
               ["Unimproved", "Pit latrine without a slab or platform, hanging latrine or "
                "bucket latrine"],
               ["Open defecation", "Disposal of human faeces in fields, forests, bushes, "
                "open bodies of water, beaches or other open places, or with solid waste"]]),
        tw(pp("indigo", "Improved facilities",
              "Flush or pour-flush to a sewer, septic tank or pit, ventilated improved pit "
              "latrines, pit latrines with a slab and composting toilets. These are "
              "designs that separate excreta from human contact."),
           pp("amber", "Where India's counting is weakest",
              "The top rung depends on what happens after the pit or tank fills. For "
              "India the JMP records no data on sludge that is emptied and treated, and "
              "its country file states there are insufficient data to estimate safely "
              "managed sanitation at national level (" + JMP + ").")),
    ], compact=True),

    C("Hygiene ladder", "Hygiene is measured by looking at the handwashing place", [
        table(["Rung", "JMP definition"],
              [["Basic", "Availability of a handwashing facility with soap and water at home"],
               ["Limited", "Availability of a handwashing facility lacking soap and/or water "
                "at home"],
               ["No facility", "No handwashing facility at home"]]),
        tw(pp("cyan", "Why the indicator is a facility",
              "Behaviour is hard to observe in a survey visit, so enumerators ask to see "
              "the place where household members usually wash hands and record whether "
              "water and soap are there. A facility makes handwashing possible. It does "
              "not show that anyone washes at the moments that matter."),
           pp("green", "Menstrual health indicators",
              "The JMP country file has columns for use of menstrual materials, enough "
              "materials, a private place to change, awareness before the first period, "
              "ability to reduce pain, comfort seeking help and participation in school, "
              "work and social activities. For India every one of these columns is empty "
              "(" + JMP + ").")),
        hbox("India's JMP hygiene estimate in 2024 is 89.7% basic, 8.9% limited and 1.4% "
             "with no facility (" + JMP + ").", "indigo"),
    ], compact=True),

    C("Method", "How the JMP turns surveys into a yearly line", [
        body("The JMP does not run its own survey. For India it lists inputs from the "
             "Census, NSS rounds, NFHS rounds, DLHS, IHDS, LASI, the 2023 Household "
             "Consumption Expenditure Survey and the 2023 Comprehensive Annual Modular "
             "Survey, alongside administrative records from Jal Jeevan Mission, Swachh "
             "Bharat Mission (Grameen and Urban), the Central Pollution Control Board and "
             "others. It fits trend lines through these points and reads off a value for "
             "each year."),
        tw(pp("cyan", "The minimum rule",
              "For safely managed drinking water the JMP takes the lowest of three "
              "proportions among people using improved sources, which are accessible on "
              "premises, available when needed and free from contamination. It reports the estimate "
              "only if quality data cover at least half the population and accessibility "
              "or availability data are also present (" + JMP + ", Charts SM notes)."),
           pp("amber", "What this means for the reader",
              "A smooth JMP line between survey years is a fitted value. When the inputs "
              "disagree, the fit sits between them. Section 5 shows the rural open "
              "defecation points the JMP used for India, which range from under 1% to "
              "over 25% for nearby years.")),
        hbox("Values the JMP chose not to use appear in square brackets in its data "
             "summary sheet. Open the country file before quoting a single year.",
             "indigo"),
    ], compact=True),

    C("Improved sources", "An improved source describes the technology at the source", [
        body("The word <em>improved</em> carries a lot of weight in WASH statistics. It "
             "classifies the type of source or toilet, on the reasoning that some designs "
             "are more likely to deliver safe water or contain excreta. It does not record "
             "whether the water tested clean on the day, whether the tubewell runs dry in "
             "May, or whether the pit overflows into a drain."),
        tw(pp("indigo", "Two households, one category",
              "A household with a tap in the yard that runs two hours a day and a "
              "household with a handpump 25 minutes away whose water carries fluoride "
              "above the limit can both be counted as using an improved source. Their "
              "risks are very different."),
           pp("cyan", "What the quality data show",
              "Among Indians using improved sources in 2024, the JMP estimates 91.3% have "
              "water free from contamination, 84.5% have it available when needed and "
              "76.4% have it on premises (" + JMP + "). On-premises access is the lowest, "
              "so it sets the safely managed figure.")),
        stats([card("98.1%", "of Indians using an improved drinking water source, 2024",
                    "green", JMP),
               card("76.4%", "using safely managed drinking water, 2024", "amber", JMP),
               card("21.7", "percentage points between the two", "red", JMP)]),
    ], compact=True),

    C("Reading ladders", "Five habits for reading a ladder chart", [
        tw([bullets(["Read the top rung and the bottom rung together. Progress at the top "
                     "can hide people stuck at the bottom.",
                     "Check whether a figure is for people or for households. The JMP "
                     "counts people, NFHS fact sheets mostly count people, NSS highlights "
                     "count households.",
                     "Separate rural and urban before comparing states. A state average "
                     "mixes two different service models.",
                     "Look for the word <em>estimate</em>. A JMP figure for 2024 is a "
                     "fitted value. Nobody measured it in that year.",
                     "Find the oldest input behind the newest year. Several JMP series for "
                     "India rest on 2021 to 2023 surveys."], "cyan", sm=True)],
           pp("amber", "A worked example",
              "The JMP shows rural open defecation in India at 10.7% in 2024 (" + JMP + "). "
              "The most recent survey points behind it are the 2023 HCES (18.0%) and the "
              "2023 CAMS (11.4%), both rural, as listed in the JMP data summary. The 2024 "
              "figure extends the fitted trend one year past the newest survey. It may "
              "turn out to be right, and it is a projection.")),
        hbox("Ladders make progress visible. They also make it easy to quote the rung "
             "that flatters a programme. Quote the full ladder.", "indigo"),
    ], compact=True),

    # ===================== SECTION 03 =====================
    D("03", "Section Three", "India's numbers from the JMP, NFHS and NSS"),

    C("India on the ladders", "India's WASH ladders in 2024, as the JMP estimates them", [
        table(["Rung", "Drinking water", "Sanitation", "Hygiene"],
              [["Safely managed", "76.4%", "Not estimated nationally", "Not defined"],
               ["Basic", "19.3%", "83.4% at least basic (see note)", "89.7%"],
               ["Limited", "2.3%", "9.9% (shared facilities)", "8.9%"],
               ["Unimproved", "1.5%", "0.0%", "Not defined"],
               ["Surface water / open defecation / no facility", "0.4%", "6.7%", "1.4%"]]),
        body("The country file computes a safely managed sanitation value of 62.8% from "
             "in-situ disposal assumptions, and also flags that the data are insufficient "
             "for a national estimate. The JMP records no sludge as emptied and treated "
             "and puts treated wastewater at 5.9% of the population. Quote the "
             "sanitation top rung for India with that caveat, or quote "
             "<em>at least basic</em>, which is 83.4% (" + JMP + ").", sm=True),
        hbox("A population of about 145 crore (UN figures used by the JMP) means 6.7% open "
             "defecation is still roughly 9.7 crore people in 2024.", "amber"),
    ], compact=True),

    C("Two decades", "India's water and sanitation ladders since 2000", [
        chart("washJmpTrend",
              "India, JMP estimates, % of population, 2000-2024",
              JMP + " (washdata.org); fitted values from survey and administrative inputs",
              "line",
              {"labels": ["2000", "2004", "2008", "2012", "2014", "2016", "2018", "2020",
                          "2022", "2024"],
               "datasets": [
                   {"label": "At least basic drinking water",
                    "data": [79.5, 82.2, 84.9, 87.7, 89.1, 90.4, 91.8, 93.1, 94.4, 95.7],
                    "borderColor": "#0EA5E9", "backgroundColor": "#0EA5E9", "fill": False},
                   {"label": "At least basic sanitation",
                    "data": [14.7, 25.5, 36.8, 48.3, 54.2, 60.1, 66.1, 72.0, 77.8, 83.4],
                    "borderColor": "#10B981", "backgroundColor": "#10B981", "fill": False},
                   {"label": "Open defecation",
                    "data": [73.2, 61.5, 50.1, 38.8, 33.3, 27.8, 22.4, 17.0, 11.7, 6.7],
                    "borderColor": "#EF4444", "backgroundColor": "#EF4444", "fill": False}]},
              "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of population'} } } }"),
        body("Water access was high and rising before either mission began. Sanitation is "
             "the larger story. In 2000 nearly three in four Indians defecated in the open. "
             "The JMP line falls steadily through the Swachh Bharat years, and Section 5 "
             "explains why the survey points under that line disagree with each other.",
             sm=True),
    ], compact=True),

    C("Rural and urban", "Rural and urban India sit on different rungs", [
        table(["Indicator, 2024", "Rural", "Urban", "Total"],
              [["Safely managed drinking water", "72.6%", "83.0%", "76.4%"],
               ["Drinking water accessible on premises", "72.6%", "83.0%", "76.4%"],
               ["Free from contamination", "88.1%", "96.8%", "91.3%"],
               ["At least basic sanitation", "81.0%", "87.4%", "83.4%"],
               ["Shared (limited) sanitation", "8.3%", "12.6%", "9.9%"],
               ["Open defecation", "10.7%", "0.0%", "6.7%"],
               ["Sewer connection", "1.9%", "38.2%", "15.3%"],
               ["Basic hygiene", "85.9%", "96.1%", "89.7%"]]),
        tw(pp("cyan", "Rural",
              "Sanitation is mostly on-site, with pits and septic tanks serving 87.5% of "
              "rural people. Water quality is the weaker link. Among rural people using "
              "improved sources, 11.9% do not have water free from contamination "
              "(" + JMP + ")."),
           pp("amber", "Urban",
              "Shared toilets are commoner in towns, 12.6% against 8.3%. Fewer than four "
              "in ten urban residents are on a sewer, so most urban excreta still depends "
              "on emptying services (" + JMP + ").")),
    ], compact=True),

    C("Safely managed water", "For safely managed water, the binding constraint is the tap at home", [
        chart("washSmWater",
              "Components of safely managed drinking water, India, 2024 (%)",
              JMP + ", Charts SM sheet",
              "bar",
              {"labels": ["Improved source", "Available when needed",
                          "Free from contamination", "Accessible on premises",
                          "Safely managed (minimum)"],
               "datasets": [{"label": "Total", "data": [98.1, 84.5, 91.3, 76.4, 76.4],
                             "backgroundColor": ["#10B981", "#0EA5E9", "#0EA5E9",
                                                 "#F59E0B", "#EF4444"]}]},
              "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of population'} } } }"),
        body("Because the JMP takes the minimum of the three criteria, whichever is lowest "
             "decides the safely managed figure. For India that is on-premises access, so "
             "a working Jal Jeevan Mission tap can add directly to SDG 6.1. Quality "
             "sits at 91.3%, but it rests on far fewer tests than access does, and a "
             "contaminated tap at home still counts as accessible.", sm=True),
    ], compact=True),

    C("NFHS", "What the National Family Health Survey reports, round by round", [
        table(["Indicator (India, total)", "NFHS-4 2015-16", "NFHS-5 2019-21",
               "NFHS-6 2023-24"],
              [["Population with an improved drinking-water source", "89.9%", "95.9%",
                "96.5%"],
               ["Population in households using an improved sanitation facility", "48.4%",
                "70.2%", "Not on the fact sheet"],
               ["Children under 5 with diarrhoea in the past 2 weeks", "9.2%", "7.3%",
                "7.9%"],
               ["Women 15-24 using hygienic menstrual protection", "Not compared here",
                "77.3% (77.6% in NFHS-6 comparison column)", "79.2%"]]),
        tw(pp("cyan", "Rural and urban, NFHS-6",
              "Improved drinking water reached 99.1% urban and 95.4% rural. Diarrhoea "
              "prevalence among under-fives was 6.7% urban and 8.3% rural, up from a "
              "national 7.3% in NFHS-5 (" + N6 + ")."),
           pp("amber", "Reading the rows",
              "NFHS-4 and NFHS-5 values come from MoSPI's eSankhyiki NFHS dataset (" + N5 +
              "). NFHS-6 values come from the provisional fact sheet released in May "
              "2026. The diarrhoea rise is small and the survey asks about a two-week "
              "window, so season of fieldwork matters.")),
    ], compact=True),

    C("A missing row", "The NFHS-6 India fact sheet carries no sanitation indicator", [
        body("NFHS-5 reported the share of the population living in households that use an "
             "improved sanitation facility, 70.2% in 2019-21. The NFHS-6 India fact sheet "
             "released in May 2026 reports 101 key indicators and none of them concerns "
             "sanitation, toilets or handwashing. Its household profile keeps electricity, "
             "improved drinking water, iodised salt, insurance and bank accounts "
             "(" + N6 + ")."),
        tw(pp("amber", "What is lost",
              "NFHS was the only national survey that measured sanitation in the same "
              "households as child height, anaemia and diarrhoea. Without it, a district "
              "cannot set its stunting figure beside its sanitation figure from one "
              "sample. Researchers will need the unit-level data, if it is released, or "
              "other surveys."),
           pp("cyan", "Where to look instead",
              "NSS rounds, including the 76th round of 2018 and the 2020-21 round, and "
              "the 2023 HCES and CAMS surveys, carry household latrine questions, and "
              "the JMP lists them as inputs. The ImpactMojo Deep Dive <em>What NFHS-6 "
              "stopped counting</em> collects the readings on this gap.")),
        hbox("When a programme report cites NFHS-6 for sanitation, the citation is wrong. "
             "Ask which survey the figure came from.", "red"),
    ], compact=True),

    C("NSS 76th round", "The most detailed national WASH survey India has run", [
        body("The NSS 76th round surveyed 1,06,838 households between July and December "
             "2018 on drinking water, sanitation, hygiene and housing. It asked about the "
             "principal source, whether supply was sufficient through the year, distance, "
             "treatment, latrine type, who used the latrine and how often, water near the "
             "latrine and handwashing practice (" + NSS + ")."),
        table(["Highlight", "Rural", "Urban"],
              [["Used an improved source of drinking water", "94.5%", "97.4%"],
               ["Drinking water within household premises", "58.2%", "80.7%"],
               ["Sufficient drinking water throughout the year", "87.6%", "90.9%"],
               ["Improved source on premises, sufficient all year", "51.4%", "72.0%"],
               ["Access to a latrine", "71.3%", "96.2%"],
               ["Bathroom and latrine both within premises", "48.0%", "86.1%"],
               ["Drinking water not treated", "72.8%", "50.9%"]]),
        hbox("The round was fielded ten months before the national ODF declaration, so "
             "its latrine figures describe the final year of the construction drive.",
             "indigo"),
    ], compact=True),

    C("Latrine access by wealth", "In 2018 latrine access still followed household spending", [
        chart("washNssQuintile",
              "Rural households with access to a latrine, by consumption quintile, 2018 (%)",
              "NSS 76th round, Report No. 584, via MoSPI eSankhyiki (indicator 20)",
              "bar",
              {"labels": ["Poorest fifth", "Second", "Middle", "Fourth", "Richest fifth",
                          "All rural", "Rural SC", "Rural ST"],
               "datasets": [{"label": "Access to latrine (%)",
                             "data": [53.5, 61.9, 68.7, 77.3, 86.7, 71.3, 62.8, 63.3],
                             "backgroundColor": ["#EF4444", "#F59E0B", "#F59E0B",
                                                 "#0EA5E9", "#10B981", "#6366F1",
                                                 "#EF4444", "#EF4444"]}]},
              "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of households'} } } }"),
        body("A 33-point gap separated the poorest and richest rural fifths four years into "
             "Swachh Bharat. In urban India the poorest fifth was at 86.2%. Any later claim "
             "of universal coverage has to explain how the poorest rural households closed "
             "a gap of this size in the final year.", sm=True),
    ], compact=True),
]

SLIDES_B = [

    # ===================== SECTION 04 =====================
    D("04", "Section Four", "What Swachh Bharat Mission built"),

    C("SBM (Grameen)", "Swachh Bharat Mission (Grameen): the aim and the design", [
        body("Swachh Bharat Mission (Grameen) was launched on 2 October 2014 with the aim of "
             "eliminating open defecation and achieving ODF status by 2 October 2019, the "
             "150th birth anniversary of Mahatma Gandhi. Phase II began on 1 April 2020 "
             "with a focus on keeping villages ODF and adding solid and liquid waste "
             "management. The programme has been extended to 2026-27 (" + SBMN + ")."),
        tw(pp("cyan", "The household incentive",
              "An incentive of ₹12,000 is paid for building an individual household "
              "latrine to BPL households and to identified APL households, namely SC and "
              "ST households, small and marginal farmers, landless labourers with homestead, "
              "persons with disabilities and women-headed households. States may add to "
              "it from their own share (" + YER + ")."),
           pp("indigo", "Who pays",
              "The Centre and states share costs 90:10 in the eight north-eastern states, "
              "Uttarakhand, Himachal Pradesh and Jammu and Kashmir, 60:40 in other states, "
              "and the Centre pays all of it in Union Territories. Phase II also draws on "
              "15th Finance Commission grants to rural local bodies (" + YER + ").")),
        hbox("A subsidy paid on construction gives every official an incentive to report "
             "construction. Use is nobody's line item unless the programme makes it one.",
             "amber"),
    ], compact=True),

    C("What was built", "Twelve crore latrines and the money behind them", [
        stats([card("12 crore+", "individual household latrines built since 2 October 2014",
                    "green", YER + ", IMIS, 16 December 2025"),
               card("2.67 lakh", "community sanitary complexes built", "cyan",
                    YER + ", IMIS, 16 December 2025"),
               card("₹93,723 crore", "central share used, 2014-15 to 2024-25", "amber",
                    YER),
               card("₹1.40 lakh crore", "total programme outlay of Phase II", "indigo",
                    YER)], cols=4),
        tw(pp("cyan", "Where the numbers come from",
              "Every figure on this slide is what states report on the SBM(G) management "
              "information system (IMIS). A latrine is entered when it is built. The record says nothing about whether the household uses it "
              "five years later, whether the pit has filled, or whether the structure "
              "still stands."),
           pp("amber", "Maintenance as a campaign",
              "The Hamara Shauchalay, Hamara Bhavishya campaign from 19 November to 10 "
              "December 2025 reported repair and beautification of more than one lakh "
              "household toilets and over 550 community complexes (" + SBMN + "). A "
              "campaign that repairs toilets is also evidence that many need repair.")),
        hbox("Twelve crore toilets is a large public works achievement. It is a count of "
             "structures, and the next section treats it as one.", "indigo"),
    ], compact=True),

    C("ODF Plus", "What the ODF Plus (Model) label requires", [
        term("ODF Plus (Model) village",
             "A village which is sustaining its ODF status, has arrangements for both solid "
             "waste management and liquid waste management, observes visual cleanliness "
             "(minimal litter, minimal stagnant wastewater, no plastic waste dump in public "
             "places) and displays ODF Plus IEC messages (" + YER + ")."),
        table(["Phase II indicator, December 2025", "Reported"],
              [["Villages declared ODF Plus (Model)", "4,89,526"],
               ["Villages verified ODF Plus (Model)", "4,15,915"],
               ["Villages with solid waste management arrangements", "5.27 lakh+"],
               ["Villages with liquid waste management arrangements", "5.41 lakh+"],
               ["Blocks with plastic waste management", "5,300+"],
               ["Functional community biogas plants under GOBARdhan", "970+"]]),
        body("Declared and verified differ by about 74,000 villages. A declaration is a "
             "statement by the village. Verification is a further check recorded in the "
             "same programme system. Neither is an independent household survey. Source: "
             + YER + ", IMIS as on 16 December 2025.", sm=True),
    ], compact=True),

    C("SBM (Urban)", "Swachh Bharat Mission (Urban) and its four certifications", [
        table(["Certification", "What it requires, in the mission's words"],
              [["ODF", "All households have access to toilets and there is no open "
                "defecation"],
               ["ODF+", "At any point of the day, not a single person is found defecating "
                "and/or urinating in the open, and all community and public toilets are "
                "functional and well maintained"],
               ["ODF++", "Sewage including faecal sludge and septage safely managed and "
                "treated, with no open discharge or dumping"],
               ["Water+", "All domestic used water, including septage, is collected and "
                "treated to a satisfactory level and treated effluent is reused before "
                "excess is released"]]),
        tw(pp("cyan", "Timeline",
              "SBM-U launched on 2 October 2014. The ODF protocol came in 2016, ODF+ and "
              "ODF++ protocols in 2018, the Water+ protocol in 2019, and SBM-U 2.0 in "
              "October 2021 (" + SBMU + ")."),
           pp("indigo", "Used water in SBM-U 2.0",
              "SBM-U 2.0 added a used water management component. One of its objectives "
              "is to eradicate hazardous entry into sewers and septic tanks by mechanising "
              "cleaning (" + NAM + ").")),
    ], compact=True),

    C("The official claim", "What the government says Swachh Bharat achieved", [
        quote("As a result, by October 2019, all villages across the country had declared "
              "themselves ODF with this rural sanitation coverage increased from 39% in 2014 "
              "to 100% in 2019.",
              "DDWS Year End Review 2025, PIB"),
        tw(pp("cyan", "What the sentence measures",
              "It reports declarations by villages and a coverage figure from the "
              "programme's own records. Coverage here means households recorded as having "
              "a toilet. It is an access measure, the first of the four measurements in "
              "Section 1."),
           pp("amber", "Other claims in the same documents",
              "The DDWS note of January 2026 says a NITI Aayog evaluation found 96% of "
              "villages achieved ODF Plus status by March 2025, and cites the JMP 2024 "
              "report as showing 67% of India's rural population using safely managed "
              "sanitation (" + SBMN + "). The second figure rests on JMP assumptions about "
              "pits that are never emptied, as Section 3 explained.")),
        hbox("A claim made in good faith by a programme about its own records is still a "
             "claim about records. The next section sets it beside surveys of people.",
             "indigo"),
    ], compact=True),

    C("Coercion", "How targets were enforced, according to the people surveyed", [
        body("In late 2018 a team from r.i.c.e. revisited households in rural Bihar, Madhya "
             "Pradesh, Rajasthan and Uttar Pradesh first surveyed in 2014. Data were "
             "collected on 9,812 people and 156 local officials were interviewed (as "
             "reported by Down To Earth, 2019). The paper reports that many respondents "
             "said the mission tried to coerce latrine construction, including by "
             "withholding or threatening to withhold government benefits (" + RICE + ")."),
        stats([card("Over 1 in 2", "respondents had heard of coercion in their village",
                    "red", RICE + ", via Down To Earth"),
               card("Over 2x", "likelihood that Dalit toilet-owning households "
                    "experienced coercion, against others", "amber", RICE + ", via Down To Earth"),
               card("Nearly 3x", "Scheduled Tribe households' likelihood, against others",
                    "amber", RICE + ", via Down To Earth")]),
        tw(pp("indigo", "Forms reported",
              "Stopping people from defecating in the open, fines, and threats to cut "
              "rations or other benefits (Down To Earth report of the survey)."),
           pp("cyan", "What the authors asked for",
              "A transparent public discussion of the mission's costs, benefits and "
              "results based on evidence, as their abstract puts it (" + RICE + ").")),
    ], compact=True),

    C("Real progress", "Open defecation did fall fast, and the surveys agree on that", [
        tw([stats([card("70% to 44%", "people over two defecating in the open, four north "
                         "Indian states, 2014 to 2018", "green", RICE),
                    card("44.4% to 10.7%", "rural open defecation, JMP estimate, 2014 to "
                         "2024", "green", JMP)], cols=1)],
           pp("cyan", "What changed",
              "Every source used in this course shows a large fall in open defecation "
              "after 2014. The r.i.c.e. panel shows a 26-point fall in four years in the "
              "states where open defecation was most common, and 57% of its households "
              "that had no latrine in 2014 had one by 2018 (Down To Earth report). The "
              "JMP rural line falls by about 34 points from 2014 to 2024. It also fell by "
              "about 34 points from 2004 to 2014, so the fitted trend shows no break at "
              "2014, which is a reason to read the survey points directly.")),
        tw(pp("amber", "What did not change as fast",
              "Use among owners, the treatment of children's faeces, the emptying of "
              "pits, and the caste division of the work of emptying them. These appear in "
              "Sections 5 and 9."),
           pp("indigo", "How to say both",
              "Open defecation fell steeply, and it did not reach zero by October 2019. "
              "Both statements are supported by the same surveys. A report that makes only "
              "one of them is choosing a side.")),
    ], compact=True),

    # ===================== SECTION 05 =====================
    D("05", "Section Five", "ODF claims and the survey evidence"),

    C("Three verbs", "Declared, verified and measured mean different things", [
        term("Declared ODF",
             "The village or its panchayat states that no one defecates in the open, and the "
             "status is entered in the programme MIS."),
        term("Verified ODF",
             "A later check of the declaration under the programme's own protocol. It is "
             "carried out within the government that runs the programme."),
        term("Measured open defecation",
             "A sample survey asks households or individuals where they usually defecate, "
             "and estimates the share for a population with a known margin of error."),
        tw(pp("cyan", "Why the gap is structural",
              "A declaration is binary for a whole village. A survey measures a share of "
              "people. A village where 90% of people use toilets is not ODF by definition, "
              "yet a declaration can still be filed for it."),
           pp("amber", "Incentive",
              "Officials whose performance is judged on declarations have reason to file "
              "them early. Surveys run by statistical agencies have no such stake, which "
              "is why they are the right check on a declaration.")),
    ], compact=True),

    C("The comparison", "One question, several answers for the same years", [
        table(["Source", "Period", "Measure", "Figure"],
              [["SBM(G) records", "October 2019", "Rural sanitation coverage (access)",
                "100%"],
               ["NSS 76th round", "July-Dec 2018", "Rural households with latrine access",
                "71.3%"],
               ["r.i.c.e. panel, 4 states", "Sept-Dec 2018",
                "People over two defecating in the open", "44%"],
               ["NFHS-5", "2019-21", "Rural open defecation, as used by JMP", "25.5%"],
               ["NSS 78th round", "2020-21", "Rural open defecation, as used by JMP",
                "20.7%"],
               ["HCES", "2023 (JMP label)", "Rural open defecation, as used by JMP", "18.0%"],
               ["CAMS", "2023 (JMP label)", "Rural open defecation, as used by JMP", "11.4%"],
               ["JMP estimate", "2024", "Rural open defecation (fitted)", "10.7%"]]),
        body("Sources: " + YER + "; " + NSS + "; " + RICE + "; survey points from the JMP "
             "India country file, Data Summary sheet (" + JMP + "). The r.i.c.e. figure "
             "covers four states with high open defecation in 2014 and is not a national "
             "estimate.", sm=True),
        hbox("No survey in this table supports universal toilet use in 2019. Every survey "
             "shows a large fall from 2014.", "indigo"),
    ], compact=True),

    C("Survey by survey", "Rural open defecation in the data the JMP compiled", [
        chart("washOdSurveys",
              "Rural open defecation (% of people) by survey, as compiled by the JMP for India",
              JMP + ", Data Summary sheet; NARSS as labelled in the file",
              "bar",
              {"labels": ["NSS 2012", "NFHS-4 2015-16", "NSS 2017", "NARSS 2018",
                          "NSS 2018", "NARSS 2019", "NARSS 2020", "NFHS-5 2019-21",
                          "NSS 2020-21", "HCES 2023", "CAMS 2023"],
               "datasets": [{"label": "Rural open defecation (%)",
                             "data": [60.1, 54.3, 33.0, 23.0, 29.9, 6.8, 0.8, 25.5, 20.7,
                                      18.0, 11.4],
                             "backgroundColor": ["#0EA5E9", "#0EA5E9", "#0EA5E9",
                                                 "#F59E0B", "#0EA5E9", "#F59E0B",
                                                 "#F59E0B", "#0EA5E9", "#0EA5E9",
                                                 "#0EA5E9", "#0EA5E9"]}]},
              "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:70, title:{display:true,text:'% of rural population'} } } }"),
        body("Amber bars are the NARSS series. It put rural open defecation at 6.8% in "
             "2019 and 0.8% in 2020, while NFHS-5, fielded over 2019-21, found 25.5% and "
             "the NSS 78th round found 20.7%. The JMP used all of these points, so its "
             "fitted line runs between them.", sm=True),
    ], compact=True),

    C("Why surveys disagree", "Five reasons two surveys of one year give different answers", [
        table(["Reason", "How it moves the figure", "What to check"],
              [["Who answers", "One household respondent may speak for all members, "
                "including those who still go outside", "Is the question asked of each "
                "member?"],
               ["Question order", "Asking about scheme benefits first can make a "
                "respondent report a toilet", "Read the questionnaire"],
               ["Unit", "Households with a latrine differ from people who use one",
                "Household or person?"],
               ["Who runs it", "A survey commissioned by the programme has a stake in "
                "the answer", "Agency and funder"],
               ["Timing and season", "Use falls when pits fill or water is short",
                "Months of fieldwork"]]),
        body("The ImpactMojo Deep Dive on NFHS-6 summarises a study finding that asking "
             "about each member records more open defecation than asking one question "
             "about the household, with a larger gap in households that had received help "
             "to build a latrine. Read the source before relying on the size of that gap.",
             sm=True),
        hbox("When two numbers disagree, explain the gap before choosing one.", "indigo"),
    ], compact=True),

    C("A survey's own warning", "The NSS flagged its own latrine figure", [
        quote("It may be noted that there may be respondent bias in the reporting of access "
              "to latrine as question on benefits received by the households from government "
              "schemes was asked prior to the question on access of households to latrine.",
              "NSS Report No. 584, Highlights, item 9"),
        tw(pp("cyan", "What the NSO is saying",
              "Households were first asked which government benefits they had received. A "
              "household that had just said it received toilet support may then report "
              "having a toilet, whether or not it uses one or whether it was completed. "
              "The statistical office printed that caveat beside its headline number."),
           pp("amber", "What a practitioner takes from it",
              "Order your own questionnaire so that use and facility questions come before "
              "any question on scheme benefits. Ask to see the latrine. Record its state, "
              "whether the pan is clean, whether the pit is connected and whether it is "
              "being used to store fuel or grain.")),
        hbox("The 71.3% rural access figure from 2018 may be an overstatement by the "
             "survey's own account. It is still well short of 100%.", "amber"),
    ], compact=True),

    C("Use among owners", "Owning a latrine and using it are separate facts", [
        tw(pp("cyan", "What the NSS 76th round found",
              "Among households with access to a latrine, 94.7% of rural males and 95.7% "
              "of rural females used it regularly, and 3.5% of rural household members "
              "never used it. In urban areas 98.0% of males and 98.1% of females used it "
              "regularly (" + NSS + ", Statements 15-16)."),
           pp("amber", "What the r.i.c.e. panel found",
              "In the four states it surveyed, 23% of people over two in households with a "
              "toilet still defecated in the open in 2018 (" + RICE + ", as reported by "
              "Down To Earth). The survey asked each member, and it was fielded in the "
              "states where open defecation had been most common.")),
        body("The two figures cover different populations and use different questions. "
             "The NSS is national and asks about usual practice. The r.i.c.e. panel asks "
             "about the last time each person defecated, in four states with the highest "
             "open defecation in 2014. Both agree that some owners do not use their "
             "latrines. They disagree about how many."),
        stats([card("3.5%", "rural members of latrine households who never used it, 2018",
                    "cyan", NSS),
               card("23%", "toilet owners over two who defecated in the open, 4 states, "
                    "2018", "amber", RICE)]),
    ], compact=True),

    C("Caste and the pit", "Why some owners avoid the latrine they have", [
        body("Diane Coffey and Dean Spears argue in <em>Where India Goes: Abandoned Toilets, "
             "Stunted Development and the Costs of Caste</em> (HarperCollins India, 2017) "
             "that rural north Indians avoid affordable pit latrines because emptying a pit "
             "is associated with the work that caste assigned to Dalits. A household that "
             "will not empty its own pit, and will not be seen hiring someone to do it, "
             "prefers a large septic tank it cannot afford or no latrine at all."),
        tw(pp("indigo", "What it predicts",
              "Use is lower where latrines are small pits, and owners report fear of the "
              "pit filling quickly. Households build large tanks when they can. The work "
              "of emptying falls on Dalit workers, often by hand, which links Swachh "
              "Bharat to the law on manual scavenging in Section 9."),
           pp("cyan", "What a programme can do",
              "Promote twin pits with the fact that a rested pit holds decomposed "
              "material (NSS defines a rest period of one and a half years), make "
              "mechanised emptying available and visible, and never assign emptying to "
              "caste-identified workers.")),
        hbox("Treat the caste argument as a hypothesis to test in your district, with "
             "questions on pit size, fear of filling and who empties.", "amber"),
    ], compact=True),

    C("A reader's checklist", "Questions to ask of any ODF claim", [
        tw([bullets(["Is the figure a declaration, a verification or a survey estimate?",
                     "Who collected it, and does that agency run the programme?",
                     "Is the unit a village, a household or a person?",
                     "Was each household member asked, including children's faeces disposal?",
                     "When was fieldwork, and in which season?",
                     "Were scheme-benefit questions asked before facility questions?",
                     "When pits fill, who empties them, and how?"], "cyan",
                    sm=True)],
           pp("amber", "Using it in a district",
              "Take the district's ODF Plus status from the SBM(G) dashboard. Then visit "
              "a random sample of hamlets at dawn, the time when open defecation is most "
              "visible, and ask each member of sampled households where they went "
              "yesterday. Record the state of each latrine. A one-week exercise of this "
              "kind tells a programme more about use than any declaration.")),
        hbox("For a reading list on why toilets are built and not used, see the "
             "ImpactMojo Deep Dive <em>Water, Sanitation, and the Behaviour Gap</em>.",
             "indigo"),
    ], compact=True),

    # ===================== SECTION 06 =====================
    D("06", "Section Six", "Jal Jeevan Mission, from taps to working water"),

    C("The promise", "Jal Jeevan Mission promises a working tap in every rural home", [
        body("Jal Jeevan Mission (JJM) was launched on 15 August 2019 to provide a "
             "functional household tap connection to every rural household. When it "
             "began, about 3.23 crore rural households had a tap connection (Union Jal "
             "Shakti Minister C R Patil, reported by All India Radio, 16 March 2026). The February 2025 Budget extended the mission to 2028 with an "
             "enhanced total outlay to reach 100% coverage (Budget Speech 2025-26, para 55)."),
        term("Functional Household Tap Connection (FHTC)",
             "A tap connection to a rural household for providing drinking water in "
             "adequate quantity of prescribed quality on regular basis (" + FA + ")."),
        tw(pp("cyan", "The service standard",
              "Adequate quantity means at least 55 litres per capita per day. Prescribed "
              "quality means the BIS:10500 drinking water standard, which JJM adopted for "
              "tap water service delivery (Ministry of Jal Shakti, PIB, 10 March 2025)."),
           pp("indigo", "Har Ghar Jal",
              "On the JJM dashboard, Har Ghar Jal means all households in a unit are "
              "provided with tap water supply. Districts, blocks, panchayats and villages "
              "are shown as reported or certified, and certified units are included in the "
              "reported count. Both describe connections.")),
    ], compact=True),

    C("Connections", "Tap connections grew about five-fold in six years", [
        chart("washJjmTaps",
              "Rural households with a tap connection, India (crore)",
              "All India Radio, 16 March 2026; Budget Speech 2025-26; "
              + YER + " (JJM-IMIS, 26 December 2025)",
              "bar",
              {"labels": ["Aug 2019 (launch)", "Feb 2025 (Budget)", "Dec 2025 (IMIS)",
                          "Mar 2026 (Minister)"],
               "datasets": [{"label": "Crore households",
                             "data": [3.23, 15.0, 15.7, 15.83],
                             "backgroundColor": ["#94A3B8", "#0EA5E9", "#0EA5E9",
                                                 "#10B981"]}]},
              "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:20, title:{display:true,text:'crore households'} } } }"),
        body("The Budget Speech 2025-26 described 15 crore households as 80% of India's "
             "rural population. The December 2025 review puts 81.47% of rural households "
             "at Har Ghar Jal status, and the minister spoke of about 3 crore more "
             "connections in the next phase. These are administrative counts of "
             "connections from JJM-IMIS.", sm=True),
    ], compact=True),

    C("Counting water", "A connection is counted once, and water has to arrive every day", [
        tw(pp("cyan", "What IMIS records",
              "The JJM management information system records a connection when the pipe "
              "and tap are installed and the household is listed. Villages then move to "
              "Har Ghar Jal reported and, later, certified status on the dashboard. "
              "Neither step measures how many litres arrive or whether they are safe."),
           pp("amber", "What the mission now says",
              "The December 2025 review describes 2025 as a shift from infrastructure "
              "creation to service delivery, with attention to regularity, adequacy, "
              "quality and sustainability (" + YER + "). That is an admission that the "
              "first count was of pipes.")),
        table(["Stage", "Who reports", "What it shows"],
              [["Scheme sanctioned", "State water department", "Money committed"],
               ["Connection provided", "Implementing agency into IMIS", "Pipe and tap installed"],
               ["Har Ghar Jal reported", "State, on the JJM dashboard", "All households connected"],
               ["Har Ghar Jal certified", "State, on the JJM dashboard", "Connection status confirmed"],
               ["Functional", "Third-party assessment", "Quantity, regularity and quality on the day"]]),
    ], compact=True),

    C("Functionality 2022", "How the functionality assessment was designed", [
        body("For 2021-22 the National Jal Jeevan Mission engaged HTA-Kantar Public to "
             "assess household tap connections. The sample was 13,303 villages (5,298 of "
             "them Har Ghar Jal) and 2,98,377 households in 712 rural districts of 33 "
             "states and UTs, drawn with probability proportional to size from villages "
             "with piped schemes of 20 or more connections. Enumerators measured quantity, "
             "tested pH and residual chlorine on site, and sent samples to NABL-accredited "
             "district labs for twelve parameters (" + FA + ")."),
        table(["Criterion", "Fully functional", "Partially functional", "Non-functional"],
              [["Quantity", "55 lpcd or more", "Over 40 to under 55 lpcd", "Under 40 lpcd"],
               ["Regularity", "Daily, 12 months", "9-12 months or less than daily",
                "Under 9 months or less than daily"],
               ["Quality", "Potable", "Potable", "Non-potable"]]),
        hbox("A connection is fully functional only if all three conditions hold at "
             "once. This is the right standard, and the assessment deserves credit for "
             "publishing it.", "green"),
    ], compact=True),

    C("Functionality results", "Five in eight households had a fully functional tap in 2022", [
        chart("washJjmFunc",
              "Household tap connections, national, functionality assessment 2022 (%)",
              FA + " (HTA-Kantar Public), executive summary",
              "bar",
              {"labels": ["Working on survey day", "Adequate quantity*", "Fully regular*",
                          "Potable*", "Fully functional"],
               "datasets": [{"label": "% of households",
                             "data": [86, 85, 80, 87, 62],
                             "backgroundColor": ["#0EA5E9", "#0EA5E9", "#0EA5E9",
                                                 "#0EA5E9", "#EF4444"]}]},
              "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'%'} } } }"),
        body("* Among households whose connection was working. The fully functional share "
             "meets all three conditions together. In Har Ghar Jal villages 91% of "
             "connections worked and 69% were fully functional. In aspirational districts "
             "78% worked and 62% were fully functional (" + FA + ").", sm=True),
    ], compact=True),

    C("Supply in practice", "How often the tap runs, and for how long", [
        tw([stats([card("74%", "households receiving water all seven days", "green", FA),
                   card("3 hours", "average daily duration of supply", "cyan", FA),
                   card("8%", "receiving water only once a week", "red", FA)], cols=1)],
           pp("cyan", "What households said",
              "Four in five households said the tap met their daily needs. Of the 26% "
              "without daily supply, 4% received water five or six days a week, 14% three "
              "or four days and 8% once a week. More than half (57%) purified water before "
              "drinking, and no more than 3% used RO. Only 35% paid any service charge "
              "(" + FA + ").")),
        tw(pp("amber", "Why intermittent supply matters for health",
              "Pipes that empty between supply hours can draw in contaminated water "
              "through leaks, and households store water for days in containers that "
              "are easy to contaminate. Intermittent supply turns a piped system back "
              "into a storage problem."),
           pp("indigo", "What to monitor",
              "Days of supply in the past week, hours per day, and whether the household "
              "used another source. Ask in the dry season as well as after the monsoon. "
              "A single visit gives a snapshot of a service that varies by month.")),
    ], compact=True),

    C("Water quality", "Testing water is harder than laying pipe", [
        tw(pp("amber", "What the 2022 assessment found about testing",
              "District labs could return results for only 83% of the samples submitted. "
              "A lab could test 30 to 40 samples in 24 hours, for want of trained "
              "technicians and reagents, and turnaround was usually over 48 hours. Of "
              "samples tested, 93% were free of bacteriological contamination. Residual "
              "chlorine within permissible limits was found in about a quarter of "
              "households (" + FA + ")."),
           pp("cyan", "Capacity reported in December 2025",
              "2,863 water testing laboratories, of which 1,682 are NABL-accredited. Over "
              "51 lakh samples tested in labs in 2025-26 up to 29 December 2025, and over "
              "37 lakh samples tested with field test kits by trained village women in "
              "the same period (" + YER + ").")),
        stats([card("83%", "of submitted samples the district labs could report on, 2022",
                    "amber", FA),
               card("93%", "of tested samples free of bacteriological contamination", "green",
                    FA),
               card("2,863", "water testing labs, 1,682 accredited, December 2025", "cyan",
                    YER)]),
    ], compact=True),

    C("Who runs it", "Who runs the scheme after the contractor leaves", [
        body("JJM expects each village to form a village water and sanitation committee "
             "(VWSC), also called a Pani Samiti. The 2022 assessment says the JJM "
             "Operational Guidelines mandate more than 50% women members, and it measured "
             "how many villages had formed one and what it did (" + FA + "). Its first "
             "recommendation was to scale up VWSC participation in O&amp;M."),
        table(["Finding, 2022", "Share"],
              [["Villages that had constituted a VWSC or Pani Samiti", "38%"],
               ["Of those, with more than half the members women", "40%"],
               ["Villages where the VWSC was responsible for O&amp;M", "14%"],
               ["Villages with identified skilled manpower for O&amp;M", "31%"],
               ["Villages with field test kits available", "30%"],
               ["Households aware of a grievance mechanism", "71%"],
               ["Households that filed a complaint in the past year", "5%"],
               ["Households whose complaint was resolved", "3%"]]),
        hbox("From April 2025 states have inspected four schemes a month chosen by the "
             "national mission, and 1,117 schemes had been assigned by December 2025 "
             "(" + YER + "). Joint inspections are run by government teams.", "indigo"),
    ], compact=True),

    # ===================== SECTION 07 =====================
    D("07", "Section Seven", "Groundwater depletion and contamination"),

    C("The account", "India's groundwater account for 2025", [
        stats([card("448.52 BCM", "annual groundwater recharge", "cyan", GW),
               card("407.75 BCM", "annual extractable resource", "green", GW),
               card("247.22 BCM", "annual extraction for all uses", "amber", GW),
               card("60.63%", "stage of extraction, India as a whole", "red", GW)], cols=4),
        tw(pp("cyan", "How the account is built",
              "The Central Ground Water Board (CGWB) and state governments assess dynamic "
              "groundwater resources every year. The stage of extraction is annual "
              "extraction for irrigation, "
              "industry and domestic use divided by the extractable resource (" + GW + ")."),
           pp("amber", "Why drinking water depends on it",
              "In 2018 the hand pump was the principal drinking water source for 42.9% "
              "of rural households (" + NSS + "). Piped schemes that draw on borewells "
              "share the aquifer with irrigation pumps, so drinking water competes with "
              "farming for one stock.")),
    ], compact=True),

    C("Blocks by category", "One block in ten extracts more than it recharges", [
        chart("washGwCat",
              "Groundwater assessment units by category, India, 2025 (number of units)",
              GW + ", reply to Parliament on the 2025 assessment",
              "bar",
              {"labels": ["Safe (under 70%)", "Semi-critical (70-90%)", "Critical (90-100%)",
                          "Over-exploited (over 100%)", "Saline"],
               "datasets": [{"label": "Assessment units",
                             "data": [4946, 758, 201, 730, 127],
                             "backgroundColor": ["#10B981", "#F59E0B", "#F97316",
                                                 "#EF4444", "#94A3B8"]}]},
              "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, title:{display:true,text:'assessment units (blocks, taluks, mandals)'} } } }"),
        body("Of 6,762 assessment units, 730 (10.80%) are over-exploited, 201 (2.97%) "
             "critical, 758 (11.21%) semi-critical and 4,946 (73.14%) safe. A further 127 "
             "(1.88%) are saline. The national average of 60.63% hides these units, which "
             "are where drinking water sources fail first.", sm=True),
    ], compact=True),

    C("Behind the average", "Why the national figure understates local depletion", [
        tw(pp("cyan", "Irrigation drives extraction",
              "NITI Aayog's Composite Water Management Index (August 2019) reported that "
              "groundwater accounts for 62% of irrigation water and is declining in 52% of "
              "cases, and named energy subsidies that promote over-extraction and poor "
              "matching of crops to agro-climatic zones among the causes."),
           pp("amber", "Averages hide sinks",
              "A block is assessed as a whole. Within a safe block, a cluster of borewells "
              "can draw down the water table around one village. Within an over-exploited "
              "block, a hamlet with a protected spring may be fine. Check the block "
              "category, then ask what has happened to the depth of local wells.")),
        table(["Category", "Stage of extraction", "What CGWA rules impose (2020 guidelines)"],
              [["Safe", "Below 70%", "Standard regulation"],
               ["Semi-critical", "70-90%", "Stricter conditions and higher charges"],
               ["Critical", "90-100%", "Stricter conditions and higher charges"],
               ["Over-exploited", "Above 100%", "Highest charges, no new large-scale "
                "industries"]]),
        body("Categories: " + GW + ". Regulation: CGWA guidelines of 24 September 2020, as "
             "summarised by the Ministry of Jal Shakti, PIB, 29 January 2026.", sm=True),
    ], compact=True),

    C("Contamination", "What CGWB's water quality monitoring found", [
        stats([card("19.8%", "of samples with nitrate above the permissible limit", "red",
                    GWQ),
               card("9.04%", "of samples with fluoride above the limit", "amber", GWQ),
               card("3.1%", "of samples with arsenic above the limit", "amber", GWQ),
               card("32.6%", "of Punjab trace-element samples above the limit for uranium",
                    "red", "Ministry of Jal Shakti, PIB, 17 March 2025")], cols=4),
        tw(pp("cyan", "The 2024 report",
              "The Annual Groundwater Quality Report 2024 was based on sampling at 15,259 "
              "monitoring locations. In Arunachal Pradesh, Mizoram, Meghalaya and Jammu "
              "and Kashmir all samples met BIS standards. Rajasthan, Haryana and Andhra "
              "Pradesh showed contamination in isolated pockets (" + GWQ + ")."),
           pp("amber", "How the government frames it",
              "Ministry replies describe groundwater as largely potable with localised "
              "contamination in isolated pockets. A nitrate exceedance in one sample in "
              "five is a monitoring finding about many places at once, and the share in "
              "drinking water sources is what a district needs to know.")),
    ], compact=True),

    C("Arsenic and fluoride", "Responses to arsenic and fluoride, and their limits", [
        body("Arsenic and fluoride occur naturally in some aquifers and cause harm through "
             "years of drinking. The BIS permissible limit for fluoride is 1.5 mg/L (IS "
             "10500:2012, cited by the Ministry of Jal Shakti, PIB, 4 December 2025). "
             "Because the harm builds slowly, households often see no reason to stop "
             "using a familiar handpump."),
        table(["Response", "What it does", "Source"],
              [["Piped supply from a safe surface source", "Replaces the contaminated source "
                "for drinking", "Advice to states, PIB, 10 March 2025"],
               ["Deep wells with cement sealing", "Taps arsenic-free aquifers below "
                "contaminated ones. 525 wells built, 294 in Uttar Pradesh",
                "PIB, 4 December 2025"],
               ["Community water purification plants", "Interim treatment in quality-affected "
                "habitations", "PIB, 4 December 2025"],
               ["Funding weight", "10% weight in JJM allocations for population in "
                "chemically affected habitations", "PIB, 10 March 2025"],
               ["Surveillance", "Annual reports, half-yearly bulletins and fortnightly "
                "alerts from CGWB", "PIB, 4 December 2025"]]),
        hbox("An interim plant needs electricity, chemicals and an operator. Check whether "
             "it runs before counting the habitation as safe.", "amber"),
    ], compact=True),

    C("Managing the aquifer", "Recharge, regulation and community management", [
        tw(pp("green", "Atal Bhujal Yojana",
              "Implemented in 80 water-stressed districts in seven states, the scheme "
              "trained communities to manage their own groundwater. More than 83,000 "
              "rainwater harvesting and recharge structures were built or rejuvenated and "
              "more than 9 lakh hectares brought under efficient irrigation (Ministry of "
              "Jal Shakti, PIB, 29 January 2026)."),
           pp("cyan", "Mapping and planning",
              "NAQUIM has mapped about 25 lakh sq km of the country's aquifers and "
              "district aquifer maps and management plans have been shared for 654 "
              "districts. The CGWB Master Plan for Artificial Recharge 2020 outlines about "
              "1.42 crore structures with a potential of about 185 BCM (" + GW + ").")),
        tw(pp("indigo", "Campaigns",
              "Jal Shakti Abhiyan has run annually since 2019 and converges other schemes' "
              "funds into recharge works. Mission Amrit Sarovar built or rejuvenated "
              "nearly 69,000 ponds (PIB, 4 December 2025)."),
           pp("amber", "What to ask of a recharge structure",
              "Where is it relative to the drinking water source? Does it fill? Is it "
              "maintained after the campaign year? Recharge counted as structures has the "
              "same weakness as toilets counted as structures.")),
    ], compact=True),

    C("Your district", "Looking up your block's groundwater before planning a scheme", [
        table(["What to look up", "Where", "Why it matters"],
              [["Block category and stage of extraction", "National Compilation of Dynamic "
                "Ground Water Resources, 2025 (CGWB)", "Over-exploited blocks need source "
                "sustainability in the design"],
               ["Contaminants by district", "CGWB Annual Ground Water Quality Report 2025",
                "Fluoride, arsenic, nitrate and uranium need treatment or another source"],
               ["Aquifer map and management plan", "NAQUIM district plan", "Where deeper "
                "or safer aquifers exist"],
               ["Quality-affected habitations", "JJM dashboard, water quality section",
                "Which habitations are counted as affected"],
               ["Seasonal water levels", "CGWB monitoring wells", "Whether wells fail before "
                "the monsoon"]]),
        hbox("A drinking water project in an over-exploited block that does not plan "
             "recharge or an alternative source is planning for its own failure.", "red"),
    ], compact=True),
]

SLIDES_C = [

    # ===================== SECTION 08 =====================
    D("08", "Section Eight", "Who governs water and sanitation"),

    C("A State subject", "Water is a State subject, and the Centre pays and advises", [
        body("Ministry of Jal Shakti replies to Parliament repeat one sentence. Water is a "
             "State subject, and sustainable development and management of water, together "
             "with mitigation of quality problems, is primarily the responsibility of State "
             "governments. The Central Government supports states with technical and "
             "financial assistance through its schemes (PIB, 4 December 2025)."),
        tw(pp("cyan", "What states do",
              "State public health engineering departments and water supply and sewerage "
              "boards build and often run schemes. States choose technologies, set "
              "tariffs, appoint staff and decide how far to devolve functions to "
              "panchayats and municipalities."),
           pp("indigo", "What the Centre does",
              "It designs centrally sponsored schemes such as Jal Jeevan Mission and Swachh "
              "Bharat Mission, sets guidelines, shares costs, runs the CGWB and CGWA, and "
              "monitors through dashboards. The Central Ground Water Board's monitoring "
              "and mapping scheme is spent by the Board itself, without transfers to states "
              "(PIB, 18 December 2025).")),
        hbox("When a district says a problem is the Centre's, or the Centre says it is the "
             "state's, both are partly right. Find out who signs the work order.", "amber"),
    ], compact=True),

    C("Local government", "Panchayats and municipalities under the 73rd and 74th Amendments", [
        tw(pp("cyan", "Panchayats",
              "The 73rd Amendment came into force on 24 April 1993. It gave panchayats "
              "constitutional status and provided for devolving the 29 subjects listed in "
              "the Eleventh Schedule, along with State Finance Commissions and regular "
              "elections. The word that matters is <em>may</em>, because each state decides "
              "what to devolve."),
           pp("indigo", "Municipalities",
              "The Twelfth Schedule lists the functions states may give urban local bodies, "
              "including water supply for domestic, industrial and commercial purposes and "
              "public health, sanitation, conservancy and solid waste management. In "
              "several states water supply and sewerage remain with state boards or "
              "engineering departments.")),
        body("Under Jal Jeevan Mission the village water and sanitation committee is the "
             "local institution for the scheme. Under SBM(G) Phase II the gram panchayat "
             "receives funds for community sanitary complexes and waste management assets "
             "(" + YER + "). The 2022 assessment found VWSCs in charge of O&amp;M in 14% of "
             "villages, a measure of how far devolution had reached by then (" + FA + ")."),
        hbox("Sources: Constitution of India, Part IX, Part IXA and the Eleventh and Twelfth Schedules; "
             + YER + "; " + FA + ".", "indigo"),
    ], compact=True),

    C("Pollution law", "The Water (Prevention and Control of Pollution) Act, 1974", [
        body("The Water Act, 1974 set up the Central Pollution Control Board and the State "
             "Pollution Control Boards. Together with the Environment (Protection) Act, "
             "1986 it is the main law against discharge of untreated effluent and sewage "
             "into rivers, lakes and groundwater. CPCB, with the state boards and "
             "pollution control committees, sets industry-specific and general discharge "
             "standards and the state boards enforce them (Ministry of Jal Shakti, PIB, "
             "10 March 2025)."),
        tw(pp("cyan", "Why it matters for WASH",
              "Sewage and septage dumped without treatment contaminate the sources that "
              "drinking water schemes draw on. The SBM-U ODF++ and Water+ certifications "
              "are attempts to make cities treat what they collect, a duty the 1974 Act "
              "already implied for discharges."),
           pp("amber", "What practitioners can use",
              "Consent conditions and discharge standards are public documents. A "
              "community that sees a drain or tanker discharging into its pond can "
              "complain to the state pollution control board, and journalists and "
              "researchers can compare a city's treatment capacity with its sewage "
              "generation.")),
        hbox("The 1974 Act regulates pollution. It does not guarantee anyone a supply of "
             "water. Drinking water entitlements come from scheme guidelines.", "indigo"),
    ], compact=True),

    C("Who does what", "The institutions a WASH programme deals with", [
        table(["Institution", "Role in WASH", "What to ask it for"],
              [["DDWS, Ministry of Jal Shakti", "Runs JJM and SBM(G)", "Guidelines, IMIS data, "
                "functionality reports"],
               ["MoHUA", "Runs SBM-U and urban certification", "City certification status, "
                "STP and FSTP lists"],
               ["CGWB and CGWA", "Assess, map and regulate groundwater", "Block category, "
                "quality report, NOCs"],
               ["CPCB and state pollution boards", "Enforce the Water Act, 1974",
                "Consent orders, monitoring data"],
               ["State PHED or water board", "Builds and often runs schemes", "Scheme design, "
                "O&amp;M contracts"],
               ["Gram panchayat and VWSC", "Village planning, O&amp;M, user charges",
                "Village action plan, accounts"],
               ["Urban local body", "Sewerage, desludging, toilets", "Desludging register, "
                "licences"],
               ["Ministry of Social Justice and NCSK", "NAMASTE, manual scavenging law",
                "Worker registry, death records"]]),
        hbox("Map these offices for your district before the first field visit. Most "
             "WASH failures fall between two of them.", "amber"),
    ], compact=True),

    C("Money", "How WASH money flows, and where it can be traced", [
        tw(pp("cyan", "Central schemes",
              "SBM(G) shares costs 60:40 with most states, 90:10 with the north-eastern and "
              "Himalayan states and Jammu and Kashmir, and pays fully in UTs (" + YER + "). "
              "Under JJM, Uttar Pradesh had been allocated ₹60,816 crore as central share "
              "from 2019 to December 2025, and states may use up to 2% of their allocation "
              "for water quality monitoring and surveillance (PIB, 4 December 2025)."),
           pp("indigo", "Convergence",
              "Programmes are told to draw on other money: 15th Finance Commission grants "
              "to rural local bodies, rural employment funds and state budgets. The "
              "Ministry reported about ₹1.5 lakh crore spent on recharge works through "
              "convergence with the rural employment scheme since 2021 (PIB, 18 December "
              "2025).")),
        table(["Question", "Where to look"],
              [["How much did my district receive?", "Scheme dashboards, state budget "
                "documents"],
               ["What was spent on O&amp;M?", "Panchayat accounts, VWSC records"],
               ["Who was paid for desludging or repairs?", "ULB and panchayat payment "
                "records"]]),
        hbox("Construction is funded centrally. Operation and maintenance usually is not, "
             "and that is where schemes fail.", "amber"),
    ], compact=True),

    C("Accountability", "Channels for complaint and correction", [
        tw(pp("cyan", "What exists",
              "A national JJM helpline and local grievance channels, monthly joint inspections "
              "of four schemes per state since April 2025, review meetings with district "
              "collectors (729 DMs and DCs took part in Jal Jeevan Samvad in 2025), and a "
              "District Collectors' Peyjal Samvad first held on 14 October 2025 (" + YER +
              ")."),
           pp("amber", "How households use them",
              "In 2022, 71% of households knew of a grievance mechanism, 5% had complained "
              "in the past year and 3% had their complaint resolved. Of those who "
              "complained, 62% went to the pump operator. Awareness and use of the "
              "national helpline were low (" + FA + ").")),
        stats([card("71%", "households aware of a grievance mechanism, 2022", "cyan", FA),
               card("5%", "households that complained in the past year", "amber", FA),
               card("3%", "households whose complaint was resolved", "red", FA)]),
        body("A complaint channel that resolves three households in a hundred is not "
             "carrying the load. Programmes that want feedback should ask for it at the "
             "tap, in the village, on a fixed day.", sm=True),
    ], compact=True),

    # ===================== SECTION 09 =====================
    D("09", "Section Nine", "Faecal sludge, sanitation work and the 2013 Act"),

    C("Where excreta goes", "Most Indian toilets are not connected to a sewer", [
        table(["Type of latrine used (households with access)", "Rural", "Urban", "All"],
              [["Flush or pour-flush to piped sewer", "1.6%", "39.1%", "17.0%"],
               ["Flush or pour-flush to septic tank", "50.9%", "48.9%", "50.1%"],
               ["Flush or pour-flush to twin leach pit or single pit", "32.3%", "8.7%",
                "22.5%"],
               ["Pit latrine with slab", "11.0%", "1.9%", "7.3%"],
               ["Ventilated improved pit", "1.4%", "0.4%", "1.0%"],
               ["Flush to elsewhere (open drain, open pit, field)", "0.2%", "0.6%", "0.3%"],
               ["Pit latrine without slab or open pit", "0.8%", "0.1%", "0.5%"]]),
        body("In 2018 fewer than one in five Indian households with latrine access used a "
             "toilet connected to a sewer. Half used septic tanks. Every septic tank and "
             "pit fills, so their safety depends on emptying, transport and treatment "
             "services that most towns and nearly all villages did not have (" + NSS +
             ", Statement 13)."),
        hbox("The 2024 JMP estimate puts India's sewer connections at 15.3% of the "
             "population, 1.9% rural and 38.2% urban (" + JMP + ").", "indigo"),
    ], compact=True),

    C("The service chain", "On-site sanitation needs a chain of services after the toilet", [
        flow(["Containment", "Emptying", "Transport", "Treatment", "Disposal or reuse"]),
        tw(pp("cyan", "Where the chain breaks",
              "Septic tanks built without a soak pit or with an outlet to a drain discharge "
              "effluent directly. Single pits must be emptied while the contents are fresh. "
              "Where desludging trucks are private and unregistered, nothing records "
              "where they unload. The JMP country file records no sludge for India as "
              "emptied and treated, and treated wastewater at 5.9% of the population."),
           pp("amber", "Greywater and drains",
              "In 2018, 48.1% of rural households living in houses disposed of waste water "
              "untreated to open low land or streets, and 71.1% of urban households "
              "disposed of it untreated to drains (" + NSS + ", Highlights 25). Drains "
              "carry septic overflow too, so a city with full toilet coverage can still "
              "send its faeces to the river.")),
        hbox("ODF counts toilets. Safe sanitation counts the whole chain. A city or "
             "village can be the first and not the second.", "indigo"),
    ], compact=True),

    C("Pits and tanks", "Twin pits, single pits and septic tanks, as the NSS defines them", [
        term("Twin leach pit",
             "Excreta go to one of two subsurface pits at a time. When one is full, flow "
             "is diverted to the second. The filled pit can be emptied after a rest period "
             "of one and a half years, during which pathogens are inactivated and the "
             "organic matter decomposed (" + NSS + ", Concepts and Definitions)."),
        term("Single pit",
             "Desludging is needed as soon as the pit fills, which involves handling fresh, "
             "undigested excreta. The NSS calls this hazardous to health and says single "
             "pits suit only places with a mechanical vacuum tanker or where the pit is "
             "abandoned when full."),
        term("Septic tank",
             "A watertight underground settling tank. Its treated effluent usually seeps "
             "into the ground through a leaching pit. Sludge accumulates and must be "
             "removed and treated."),
        hbox("The twin pit is the design that makes manual contact with fresh excreta "
             "unnecessary. A programme that builds single pits is building future "
             "hazardous work.", "amber"),
    ], compact=True),

    C("Urban FSM", "What SBM-U reports on treating sludge in towns", [
        tw(pp("cyan", "Plants on the dashboard",
              "The SBM-U 2.0 portal lists 984 sewage treatment plants of 5 MLD or more and "
              "969 faecal sludge treatment plants of 5 KLD or more. It also lists 3,158 "
              "cities declared Safaimitra Surakshit Shehar (" + SBMU + ")."),
           pp("amber", "What to check in a town",
              "Is the FSTP running, and how many trucks reached it last month? Does the "
              "municipality license desludging operators and record each trip? Are "
              "operators paid for delivering sludge to the plant? A plant with no trucks "
              "arriving treats nothing.")),
        tw(pp("indigo", "Rural sludge",
              "The 2025 Hamara Shauchalay campaign reported over 10,800 sessions on faecal "
              "sludge transport and retrofitting, with 6.43 lakh participants (" + YER +
              "). Rural sludge management is at an early stage."),
           pp("green", "ODF++ as a target",
              "ODF++ requires that sewage, faecal sludge and septage be safely managed and "
              "treated with no open discharge or dumping (" + SBMU + "). It is the urban "
              "certification that measures the chain.")),
    ], compact=True),

    C("The 2013 Act", "The Prohibition of Employment as Manual Scavengers Act, 2013", [
        body("The Prohibition of Employment as Manual Scavengers and their Rehabilitation "
             "Act, 2013 came into force on 6 December 2013. It bans manual scavenging and "
             "the hazardous cleaning of sewers and septic tanks (Ministry of Social "
             "Justice, PIB, 25 July 2023). It also requires the identification and "
             "rehabilitation of people who did this work."),
        stats([card("58,098", "eligible manual scavengers identified in surveys of 2013 and "
                    "2018", "red", MSA),
               card("₹40,000", "one-time cash assistance paid to each identified family",
                    "amber", MSA),
               card("2,313", "given capital subsidy up to ₹5 lakh for other work", "cyan",
                    MSA),
               card("22,294", "given skill training with a ₹3,000 monthly stipend", "cyan",
                    MSA)], cols=4),
        tw(pp("cyan", "What the surveys counted",
              "The 58,098 figure is the number of eligible manual scavengers identified in "
              "the two national surveys. It is a count of people the surveys found and "
              "accepted. People the surveys missed are not in it, so treat it as a floor."),
           pp("amber", "What the Act covers",
              "The government's summary of the Act says it bans manual scavenging and the "
              "hazardous cleaning of sewers and septic tanks. The deaths reported in recent "
              "years, on the next slide, are in sewers and septic tanks.")),
    ], compact=True),

    C("Deaths", "Workers are still dying in sewers and septic tanks", [
        stats([card("317", "sanitation workers who died in hazardous cleaning of sewers and "
                    "septic tanks, 2021-2025", "red",
                    NAM + ", citing the National Commission for Safai Karamcharis")]),
        tw(pp("red", "What the figure records",
              "Deaths reported to the National Commission for Safai Karamcharis. Deaths "
              "not reported, or recorded as accidents, are not in it. Quote the date and "
              "the source with any figure on these deaths."),
           pp("amber", "Why they happen",
              "A worker enters a tank or manhole to clear a blockage, without breathing "
              "apparatus or a harness, and is overcome by gases. Others enter to rescue "
              "him. The 2013 Act bans hazardous cleaning of sewers and septic tanks, so "
              "each death records a failure of enforcement as well as of equipment.")),
        hbox("Ask who hired the worker, whether a municipality, a contractor, a housing "
             "society or a household. Each of them decided to send a person into the tank.",
             "amber"),
    ], compact=True),

    C("NAMASTE", "NAMASTE mechanises the work and registers the workers", [
        body("The National Action for Mechanised Sanitation Ecosystem (NAMASTE) was launched "
             "in 2023-24 for sewer and septic tank workers (SSWs). Its stated outcomes "
             "include zero fatalities in sanitation work, all sanitation work done by "
             "trained and formalised workers, and no worker in direct contact with human "
             "faecal matter (" + MSA + ")."),
        table(["NAMASTE component", "Status reported"],
              [["SSWs profiled and validated", "89,248"],
               ["SSWs covered under AB-PMJAY, state schemes and NAMASTE", "75,710"],
               ["PPE kit", "Helmet, eye wear, N95 mask, face mask with filter cartridge, "
                "nitrile gloves, safety shoes, body suit"],
               ["Emergency Response Sanitation Units", "Safety devices in larger ULBs"],
               ["Capital subsidy", "For sanitation machinery, for workers, groups of up to "
                "five and private operators"]]),
        body("Source: " + NAM + ". The profiling count is of workers in hazardous cleaning, "
             "a different group from the 58,098 manual scavengers identified earlier.",
             sm=True),
    ], compact=True),

    C("In your programme", "What a WASH programme can do about sanitation work", [
        tw([bullets(["Design toilets that never need manual emptying of fresh sludge, such "
                     "as twin pits and correctly built septic tanks with soak pits.",
                     "Map who empties pits and tanks in your area, how they are paid and "
                     "what equipment they have.",
                     "Link workers to NAMASTE profiling, PPE and health cover.",
                     "Write mechanised emptying into any contract, and forbid entry into "
                     "tanks and manholes.",
                     "Keep an emergency number for the ERSU or fire service in every "
                     "village and ward.",
                     "Record deaths and near misses and report them to the district."],
                    "cyan", sm=True)],
           pp("amber", "Caste is part of the design brief",
              "The work of emptying pits and cleaning sewers has been assigned by caste, "
              "which is why Section 5 linked it to the avoidance of pit latrines. "
              "A programme that ignores who will empty the pit has chosen, by default, the "
              "people who will. Say so in the programme design and budget for "
              "machines.")),
        hbox("The ImpactMojo Caste Studies 101 deck covers the history of this work and "
             "the law in more depth.", "indigo"),
    ], compact=True),

    # ===================== SECTION 10 =====================
    D("10", "Section Ten", "Handwashing and menstrual health"),

    C("What soap prevents", "Handwashing with soap cuts diarrhoea and pneumonia", [
        tw(pp("cyan", "The systematic review",
              "Curtis and Cairncross pooled intervention and observational studies and "
              "estimated that washing hands with soap could reduce the risk of diarrhoeal "
              "disease by 42-47%. They warned that many studies were of poor quality and "
              "that publication bias could inflate the figure (Lancet Infectious Diseases, "
              "2003)."),
           pp("green", "The Karachi trial",
              "Luby and colleagues randomised squatter neighbourhoods in Karachi to "
              "handwashing promotion with soap. Children under five in households with "
              "plain soap had 50% lower incidence of pneumonia, and children under fifteen "
              "53% lower incidence of diarrhoea, than controls. Plain soap did as well as "
              "antibacterial soap (Lancet, 2005).")),
        stats([card("42-47%", "reduction in diarrhoea risk from handwashing with soap",
                    "green", "Curtis &amp; Cairncross, Lancet Infect Dis, 2003"),
               card("50%", "lower pneumonia incidence in under-fives, plain soap households",
                    "cyan", "Luby et al., Lancet, 2005"),
               card("53%", "lower diarrhoea incidence in under-fifteens", "cyan",
                    "Luby et al., Lancet, 2005")]),
        hbox("These are effects when people do wash. The hard part is getting them to wash "
             "at the right moments, every day.", "amber"),
    ], compact=True),

    C("What households report", "Most households say they use soap after defecation", [
        chart("washNssHands",
              "Households washing hands with water and soap, by occasion, 2018 (%)",
              NSS + ", Statement 19",
              "bar",
              {"labels": ["Before a meal", "After defecation"],
               "datasets": [{"label": "Rural", "data": [25.3, 66.8],
                             "backgroundColor": "#F59E0B"},
                            {"label": "Urban", "data": [56.0, 88.3],
                             "backgroundColor": "#0EA5E9"},
                            {"label": "All", "data": [35.8, 74.1],
                             "backgroundColor": "#6366F1"}]},
              "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of households'} } } }"),
        body("The NSS counted a household as following a practice if most members usually "
             "did. Before meals, 60.4% of households washed with water only. After "
             "defecation, 12.4% used ash, mud or sand, 17.9% in rural areas. These are "
             "reports, and the next slide shows what observation finds.", sm=True),
    ], compact=True),

    C("What observers see", "Observed handwashing is far lower than reported handwashing", [
        chart("washSuperAmma",
              "Handwashing with soap at key events, observed, SuperAmma trial, Andhra Pradesh (%)",
              "Biran et al., Lancet Global Health, 2014, doi:10.1016/S2214-109X(13)70160-8",
              "bar",
              {"labels": ["Baseline", "6 weeks", "6 months", "12 months*"],
               "datasets": [{"label": "Intervention villages", "data": [1, 19, 37, 29],
                             "backgroundColor": "#10B981"},
                            {"label": "Control villages", "data": [2, 4, 6, 29],
                             "backgroundColor": "#94A3B8"}]},
              "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:50, title:{display:true,text:'% of key events with soap'} } } }"),
        body("Key events were after defecation, after cleaning a child's bottom, before "
             "preparing food and before eating. Observers watched 20-25 households per "
             "village and told households the study was about domestic water use. "
             "* Control villages received a shortened intervention before the 12-month "
             "round.", sm=True),
    ], compact=True),

    C("SuperAmma", "Changing behaviour without talking about germs", [
        body("The SuperAmma trial ran in 14 villages of Chittoor district, Andhra Pradesh, "
             "between May 2011 and September 2012. It tested whether a village-level "
             "campaign built on emotional drivers of behaviour, with knowledge of disease "
             "left out of the message, could change handwashing. The campaign used an animated film, "
             "skits and public pledging in community and school events (Biran et al., "
             "Lancet Global Health, 2014)."),
        tw(pp("green", "What it found",
              "Handwashing with soap at key events rose from 1% to 37% at six months in "
              "intervention villages, against 6% in control villages. At twelve months, "
              "after controls received a shorter version, both groups were at 29%."),
           pp("amber", "What to take from it",
              "Baseline handwashing with soap was close to zero by observation. The NSS "
              "in 2018 recorded 74.1% of households as using soap after defecation. The "
              "two differ in method, place and year, and the gap is a warning about "
              "self-report. Messages built on emotion moved behaviour. Fourteen "
              "villages is a small trial, and the effect at twelve months was measured "
              "after the control group was treated.")),
        hbox("If your programme reports handwashing from a questionnaire alone, it is "
             "reporting what people say. Budget for some structured observation.", "indigo"),
    ], compact=True),

    C("The big WASH trials", "Large trials found little effect of household WASH on growth", [
        table(["Trial", "Setting", "What was delivered", "Main result"],
              [["Odisha sanitation trial (Clasen 2014)", "100 villages, Odisha",
                "Latrine promotion and construction under TSC", "Coverage 9% to 63%. "
                "Diarrhoea 8.8% vs 9.1%, no effect on helminths or growth"],
               ["MP TSC trial (Patil 2014)", "80 villages, Madhya Pradesh",
                "TSC with World Bank WSP support", "Improved sanitation +19 points, adult "
                "open defecation -10 points, no child health effect"],
               ["WASH Benefits Bangladesh (Luby 2018)", "720 clusters",
                "Water, sanitation, handwashing, nutrition arms", "Diarrhoea fell in "
                "sanitation, handwashing and combined arms. No WASH effect on growth"],
               ["WASH Benefits Kenya (Null 2018)", "702 clusters", "Same arms",
                "No arm reduced diarrhoea. Handwashing adherence under 25% by year 2"],
               ["SHINE Zimbabwe (Humphrey 2019)", "211 clusters",
                "VIP latrine, handwashing stations, soap, chlorine", "No effect of WASH on "
                "stunting, anaemia or diarrhoea"]]),
        body("Sources: Clasen et al., Lancet Global Health, 2014; Patil et al., PLoS "
             "Medicine, 2014; Luby et al., Lancet Global Health, 2018; Null et al., Lancet "
             "Global Health, 2018; Humphrey et al., Lancet Global Health, 2019.", sm=True),
    ], compact=True),

    C("Reading null results", "Why the trials found so little, and what it does not mean", [
        tw(pp("cyan", "Coverage too low",
              "In Odisha latrine coverage reached 63% of households. If health gains "
              "require most of a community to stop open defecation, 63% may be below the "
              "threshold. The authors concluded that the expected health outcome cannot "
              "be assumed from coverage (Clasen et al., 2014)."),
           pp("amber", "Interventions too elementary",
              "The SHINE authors concluded that household-level elementary WASH "
              "interventions in rural low-income settings are unlikely to reduce stunting "
              "or anaemia. A latrine and a handwashing station leave animal faeces, "
              "contaminated soil and neighbours' faeces untouched.")),
        tw(pp("indigo", "Adherence fades",
              "In Kenya handwashing adherence fell below 25% by year two and water "
              "treatment below 45% in year one, so the trial tested an offer that most "
              "households stopped using (Null et al., 2018)."),
           pp("green", "What the null does not mean",
              "Bangladesh found lower diarrhoea in the sanitation and handwashing arms. "
              "Karachi found large effects of soap. The trials show that small household "
              "packages do not change growth. They do not show that safe water and "
              "sanitation for whole communities are without health value.")),
    ], compact=True),

    C("Menstrual health", "Hygienic menstrual protection, NFHS-5 and NFHS-6", [
        chart("washMhm",
              "Women aged 15-24 using hygienic methods of menstrual protection (%)",
              N5 + "; " + N6,
              "bar",
              {"labels": ["Rural", "Urban", "Total"],
               "datasets": [{"label": "NFHS-5 (2019-21)", "data": [72.3, 89.4, 77.3],
                             "backgroundColor": "#94A3B8"},
                            {"label": "NFHS-6 (2023-24)", "data": [75.0, 90.7, 79.2],
                             "backgroundColor": "#EC4899"}]},
              "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of women 15-24'} } } }"),
        body("NFHS-6 counts reusable sanitary pads, disposable sanitary pads, tampons and "
             "menstrual cups as hygienic. Its comparison column shows NFHS-5 at 77.6% "
             "where the NFHS-5 fact sheet published 77.3%, so the earlier round was "
             "recomputed on a revised basis. Compare the NFHS-6 figure with 77.6%, a rise "
             "of under two points, and not with 77.3%.", sm=True),
    ], compact=True),

    C("Beyond products", "Menstrual health needs water, privacy and disposal", [
        tw(pp("cyan", "What the JMP would measure",
              "The JMP framework covers use of menstrual materials, enough materials, a "
              "private place to wash and change, awareness before the first period, "
              "ability to reduce pain, comfort seeking help and participation in school, "
              "work and social activities. India has no national estimate on any of these "
              "in the JMP file (" + JMP + ")."),
           pp("amber", "What India's surveys show around it",
              "In 2018, 56.6% of rural households had access to a bathroom and 48.0% had "
              "both a bathroom and a latrine within their premises (" + NSS + "). A girl "
              "without a private place to change at home or at school may have to "
              "manage menstruation without privacy or miss school.")),
        tw(pp("indigo", "Disposal",
              "Disposable pads enter household garbage, drains and pits. In 2018, 80.4% of "
              "rural households living in houses had no arrangement for garbage collection "
              "(" + NSS + ", Highlights 27). Product promotion without disposal planning "
              "moves the problem into the waste stream."),
           pp("green", "What a programme can measure",
              "Water and a lockable space in school toilets, the method used and its "
              "cost, disposal facilities, and whether girls missed school days in the "
              "last period. Ask privately, and ask girls, as well as their mothers.")),
    ], compact=True),
]

SLIDES_D = [

    # ===================== SECTION 11 =====================
    D("11", "Section Eleven", "Climate, drought and water security"),

    C("Seasonal scarcity", "Shortage is already in the household data", [
        tw([stats([card("12.4%", "rural households without sufficient drinking water from "
                         "the principal source all year, 2018", "amber", NSS),
                   card("43%", "households with a tap that faced a shortage in piped supply "
                        "at some time, 2022", "red", FA),
                   card("40%", "of those households with any way to cope", "cyan", FA)],
                  cols=1)],
           pp("cyan", "Reading the two surveys",
              "The NSS 76th round found 87.6% of rural and 90.9% of urban households had "
              "sufficient drinking water from their principal source throughout the year "
              "(" + NSS + "). The 2022 JJM assessment found 43% of households with a tap had "
              "faced a shortage in piped supply at some time. In Ladakh, Mizoram, "
              "Rajasthan, Chhattisgarh, Himachal Pradesh, Jammu and Kashmir, Jharkhand, "
              "Odisha and Meghalaya almost six in ten households reported shortages, and "
              "the report found seasonal scarcity was being managed by households with "
              "limited community action (" + FA + ").")),
        hbox("A dry-season visit and a post-monsoon visit to the same village can give two "
             "different answers to the question of whether a scheme works. Plan for both.",
             "amber"),
    ], compact=True),

    C("Water stress", "Irrigation, groundwater and the projected gap", [
        tw(pp("cyan", "What NITI Aayog reported (2019)",
              "The Composite Water Management Index reported that about 74% of the area "
              "under wheat and 65% of the area under rice faces significant water "
              "scarcity, that groundwater accounts for 62% of irrigation water, and that "
              "best estimates indicate demand will exceed supply by a factor of two by "
              "2030 (NITI Aayog, CWMI, August 2019)."),
           pp("amber", "How to use a projection",
              "The doubling figure is a projection made from 2008 demand estimates and "
              "assumptions about growth. Attribute it to NITI Aayog and say it is a "
              "projection. The 2025 groundwater account, with 730 over-exploited units, "
              "is a measurement and carries more weight in a district plan.")),
        table(["Pressure", "How it reaches drinking water", "Evidence on this slide"],
              [["Irrigation pumping", "Lowers water tables under village borewells",
                "CWMI 2019; CGWB 2025"],
               ["Weak monsoon or heat", "Sources fail before the rains", "NSS 76; JJM FA 2022"],
               ["Contamination", "Fluoride, arsenic and nitrate in deeper or overused aquifers",
                "CGWB quality report 2024"]]),
    ], compact=True),

    C("Source sustainability", "A pipe network is only as reliable as its source", [
        body("The December 2025 review describes Jal Jeevan Mission moving from building "
             "assets to sustaining service, and names source sustainability planning "
             "among the topics in reviews with district collectors (" + YER + "). The 2022 "
             "assessment recorded which villages had groundwater sources and recharge "
             "structures, and recommended adding a scheme-level measure of seasonal "
             "shortage to future assessments (" + FA + ")."),
        tw(pp("green", "Recharge and storage",
              "Jal Shakti Abhiyan has run each year since 2019. Mission Amrit Sarovar "
              "built or rejuvenated nearly 69,000 ponds, which store water and recharge "
              "groundwater (PIB, 4 December 2025)."),
           pp("amber", "Questions for a scheme",
              "Is the source a borewell in an over-exploited block? Has its yield been "
              "measured in May? Is there a recharge structure upstream, and is it "
              "maintained? Is there a fallback source, and who pays for tankers when the "
              "main one fails?")),
        hbox("Source sustainability is the climate adaptation measure that a drinking "
             "water programme controls directly.", "indigo"),
    ], compact=True),

    C("Sanitation and climate", "Floods and droughts change how toilets behave", [
        tw(pp("cyan", "Floods and high water tables",
              "Pits and septic tanks that flood can release excreta into the lanes and "
              "into shallow wells nearby. Raised plinths, sealed tanks and planned "
              "emptying before the monsoon reduce the risk. DDWS's 2025 toilet repair "
              "campaign included awareness on its Climate Resilient Sanitation and "
              "Service Delivery Protocol (" + SBMN + ")."),
           pp("amber", "Drought",
              "A pour-flush toilet needs water. When water must be carried, households "
              "ration it for drinking and cooking first, and toilet use can fall. In "
              "2018, 4.5% of rural households using a latrine reported no water in or "
              "around it (" + NSS + ", Highlights 15).")),
        tw(pp("indigo", "Heat",
              "Heat raises water demand for drinking and bathing and can shorten the hours "
              "a stretched network supplies. Monitoring in summer catches failures that a "
              "winter survey misses."),
           pp("green", "Design responses",
              "Twin pits sited away from drinking water sources, rainwater storage at "
              "schools and anganwadis, and handwashing stations that use little water. "
              "Each needs a named person responsible for upkeep.")),
    ], compact=True),

    C("Climate checklist", "A climate risk checklist for a WASH plan", [
        table(["Hazard", "What fails", "What to check before investing"],
              [["Drought", "Borewell yields, pour-flush use", "Block groundwater category, "
                "May yield test, alternative source"],
               ["Flood", "Pits, septic tanks, shallow wells", "Flood history, plinth height, "
                "distance from pits to wells"],
               ["Heat", "Supply hours, demand", "Summer supply data, storage capacity"],
               ["Overextraction", "Water quality and quantity", "Fluoride, arsenic and "
                "nitrate tests at the source"],
               ["Saline intrusion (coast)", "Groundwater sources", "Whether the unit is "
                "classed saline by CGWB"]]),
        body("Groundwater categories and saline units: " + GW + ". Quality: " + GWQ +
             ". The checklist turns the evidence in Sections 6, 7 and 11 into questions a "
             "programme team can answer in its first month.", sm=True),
        hbox("Ask each question for the dry season and the wet season separately.",
             "indigo"),
    ], compact=True),

    # ===================== SECTION 12 =====================
    D("12", "Section Twelve", "Monitoring a WASH programme"),

    C("Kinds of data", "Four kinds of WASH data, each with its own typical error", [
        table(["Kind", "Examples", "Good for", "Typical error"],
              [["Programme MIS", "SBM(G) IMIS, JJM-IMIS", "What was built, where, when",
                "Records construction and declarations. Use is missing"],
               ["Government-commissioned surveys", "JJM functionality assessments",
                "Checking the programme at scale", "The commissioning agency runs the "
                "programme"],
               ["National statistical surveys", "NSS 76th and 78th rounds, NFHS, HCES, "
                "CAMS", "Independent population estimates", "Infrequent, question order "
                "and respondent effects"],
               ["Independent studies and trials", "r.i.c.e. panels, SuperAmma, Odisha trial",
                "Use, behaviour and causal effects", "Small areas only"]]),
        tw(pp("cyan", "Triangulate",
              "Use the MIS to find where things were built, a statistical survey to find "
              "how many people use them, and a small independent check to understand why."),
           pp("amber", "Disclose",
              "Every report should name its data source, its date, its unit and who "
              "collected it. Most disputes about WASH numbers disappear once those four "
              "facts are on the page.")),
    ], compact=True),

    C("Indicators", "Indicators that match the ladders", [
        table(["Indicator", "Definition to use", "How to collect"],
              [["Safe drinking water at home", "JMP safely managed (on premises, available "
                "when needed, free from contamination)", "Household survey plus water tests"],
               ["Days of supply last week", "Count of days the tap ran, 0-7",
                "Household recall, cross-checked at the source"],
               ["Litres per person per day", "Measured volume divided by members, against 55",
                "Bucket and timer at the tap"],
               ["Toilet use by each member", "Last defecation, each person over two, and "
                "child faeces disposal", "Individual questions, private"],
               ["Latrine functional", "Pan clean, water present, pit not full, door works",
                "Enumerator observation"],
               ["Basic hygiene", "Handwashing place with soap and water seen",
                "Observation of the place"],
               ["Sludge safely emptied", "Last emptying by machine, delivered to a plant",
                "Household and operator records"]]),
        hbox("Choose few indicators, define them in advance, and keep the definition fixed "
             "across rounds so that change means change.", "indigo"),
    ], compact=True),

    C("Measuring behaviour", "Self-report, observation and spot checks", [
        tw(pp("cyan", "Self-report",
              "Cheap and fast. Inflated for socially approved behaviour such as "
              "handwashing and toilet use. Ask about the last occasion, since usual "
              "practice invites the approved answer. Ask each person separately, and put programme-benefit "
              "questions at the end, as the NSS's own warning suggests."),
           pp("green", "Structured observation",
              "An observer records behaviour at key events over several hours. SuperAmma "
              "observed 20-25 households per village and told them the study was about "
              "domestic water use to reduce bias (Biran et al., 2014). Expensive, and "
              "people behave differently when watched.")),
        tw(pp("amber", "Spot checks",
              "Look for signs such as a wet pan in the morning, a worn path to the toilet, soap "
              "at the handwashing place, faeces in the lanes at dawn. Spot checks are "
              "cheaper than observation and harder to fake than a questionnaire."),
           pp("indigo", "Combining them",
              "Use self-report for scale, spot checks for a sample, and observation for a "
              "sub-sample, and report the gap between them. The gap is itself a finding "
              "about how far reports can be trusted in your area.")),
    ], compact=True),

    C("Water quality", "Monitoring drinking water quality in practice", [
        body("The 2022 JJM assessment tested twelve critical parameters in district labs. "
             "They were turbidity, total hardness, total alkalinity, chloride, ammonia, iron, nitrate, "
             "sulphate, total dissolved solids, bacteriological contamination, arsenic and "
             "fluoride. pH and residual chlorine were measured on site (" + FA + ")."),
        tw(pp("cyan", "Field test kits",
              "Village women trained to use field test kits tested over 37 lakh samples in "
              "2025-26 up to 29 December 2025 (" + YER + "). Kits screen for common "
              "problems and should trigger a lab test when they show a problem."),
           pp("amber", "Lab testing",
              "Labs returned results for 83% of samples in 2022 and took over 48 hours. A "
              "bacteriological test only describes the moment of sampling. Repeat tests "
              "at the source, the storage tank and the household tap, in more than one "
              "season (" + FA + ").")),
        hbox("Residual chlorine at the tap is the quickest daily check that a piped supply "
             "has been treated. In 2022 it was within limits in about a quarter of "
             "households sampled.", "indigo"),
    ], compact=True),

    C("A district plan", "A monitoring plan for a district WASH programme", [
        flow(["Baseline by survey", "Quarterly spot checks", "Seasonal water tests",
              "Annual use survey", "Public report"]),
        tw([bullets(["Draw a random sample of villages and households, and keep it as a "
                     "panel across rounds.",
                     "Ask each member about the last defecation, and record child faeces "
                     "disposal.",
                     "Measure litres and days of supply at the tap in May and in "
                     "October.",
                     "Test water at the source and at a household tap in each sampled "
                     "village.",
                     "Record who empties pits and tanks, by what method, and where the "
                     "sludge goes.",
                     "Publish the results with the MIS figures beside them, and explain "
                     "any gap."], "cyan", sm=True)],
           pp("amber", "Questions for any WASH claim",
              "Is it access, use, safety or function? Who collected it and do they run "
              "the programme? Person or household? Which season? What happens after the "
              "pit fills? For further reading on use and behaviour, see the ImpactMojo "
              "Deep Dive <a href=\"/deepdives/water-sanitation-behaviour-gap.html\">Water, "
              "Sanitation, and the Behaviour Gap</a>, and for the survey gap, <a "
              "href=\"/deepdives/nfhs6-stopped-counting.html\">What NFHS-6 stopped "
              "counting</a>.")),
    ], compact=True),

    C("Sources", "Sources opened for this deck (October 2026)", [
        tw([body("<strong>Data and surveys.</strong> "
                 "<a href=\"https://washdata.org/data/country/IND/household/download\">WHO/UNICEF "
                 "JMP India country file, August 2025</a>; "
                 "<a href=\"https://washdata.org/monitoring/drinking-water\">JMP drinking water "
                 "ladder</a>; "
                 "<a href=\"https://mospi.gov.in/sites/default/files/publication_reports/Report_584_final_0.pdf\">NSS "
                 "Report No. 584</a>; "
                 "<a href=\"https://esankhyiki.mospi.gov.in/\">MoSPI eSankhyiki (NSS 76, NFHS)</a>; "
                 "<a href=\"https://www.nfhsiips.in/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-2024%20Fact%20Sheets.pdf\">NFHS-6 "
                 "fact sheets, May 2026</a>; "
                 "<a href=\"https://jaljeevanmission.gov.in/sites/default/files/2022-10/national_report_of_functionality_assessment_2022.pdf\">JJM "
                 "Functionality Assessment 2022</a>; "
                 "<a href=\"https://ejalshakti.gov.in/jjmreport/JJMIndia.aspx\">JJM dashboard</a>; "
                 "<a href=\"https://www.niti.gov.in/sites/default/files/2019-08/CWMI-2.0-latest.pdf\">NITI "
                 "Aayog CWMI 2019</a>; "
                 "<a href=\"https://sbmurban.org/\">SBM-Urban 2.0 portal</a>. "
                 "<strong>Government statements.</strong> "
                 "<a href=\"https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jan/doc202611750301.pdf\">DDWS "
                 "Year End Review 2025</a>; "
                 "<a href=\"https://ejalshakti.gov.in/iwc_2026/images/Note_SBM.pdf\">DDWS note on "
                 "SBM(G)</a>; "
                 "<a href=\"https://www.indiabudget.gov.in/budget2025-26/doc/Budget_Speech.pdf\">Budget "
                 "Speech 2025-26</a>; "
                 "<a href=\"https://www.newsonair.gov.in/union-jal-shakti-minister-cr-patil-says-over-15-83-crore-households-now-have-tap-water-under-jal-jeevan-mission\">AIR, "
                 "16 March 2026</a>; PIB releases "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2206073\">18 Dec 2025</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2220203\">29 Jan 2026</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2198937\">4 Dec 2025 (arsenic)</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2198942\">4 Dec 2025 (fluoride)</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2109942\">10 Mar 2025</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2111857\">17 Mar 2025</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=1942478\">25 Jul 2023</a>, "
                 "<a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2247765\">1 Apr 2026</a>.",
                 sm=True)],
           [body("<strong>Research.</strong> "
                 "<a href=\"https://doi.org/10.1016/S0140-6736(23)00458-0\">Wolf et al., Lancet 2023</a>; "
                 "<a href=\"https://doi.org/10.1371/journal.pone.0073784\">Spears, Ghosh and "
                 "Cumming, PLoS ONE 2013</a>; "
                 "<a href=\"https://econpapers.repec.org/paper/izaizadps/dp12065.htm\">Gupta et "
                 "al., IZA DP 12065, 2019</a>; "
                 "<a href=\"https://www.downtoearth.org.in/news/waste/despite-toilets-in-place-a-quarter-of-rural-population-stuck-to-open-defecation-62770\">Down "
                 "To Earth report of that survey</a>; "
                 "<a href=\"https://doi.org/10.1016/S2214-109X(14)70307-9\">Clasen et al., 2014</a>; "
                 "<a href=\"https://doi.org/10.1371/journal.pmed.1001709\">Patil et al., 2014</a>; "
                 "<a href=\"https://doi.org/10.1016/S2214-109X(17)30490-4\">Luby et al., 2018</a>; "
                 "<a href=\"https://doi.org/10.1016/S2214-109X(18)30005-6\">Null et al., 2018</a>; "
                 "<a href=\"https://doi.org/10.1016/S2214-109X(18)30374-7\">Humphrey et al., 2019</a>; "
                 "<a href=\"https://doi.org/10.1016/S1473-3099(03)00606-6\">Curtis and Cairncross, "
                 "2003</a>; "
                 "<a href=\"https://doi.org/10.1016/S0140-6736(05)66912-7\">Luby et al., 2005</a>; "
                 "<a href=\"https://doi.org/10.1016/S2214-109X(13)70160-8\">Biran et al., 2014</a>; "
                 "Coffey and Spears, <em>Where India Goes</em>, HarperCollins India, 2017. "
                 "<strong>Background.</strong> "
                 "<a href=\"https://legislative.gov.in/constitution-of-india/\">Constitution of India</a>, "
                 "Parts IX and IXA and the Eleventh and Twelfth Schedules.", sm=True)]),
    ], compact=True),

    # ===================== END =====================
    {"type": "end",
     "eyebrow": "Water, Sanitation and Hygiene 101",
     "headline": "Count the toilets, then ask who uses them",
     "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development "
               "practitioners in South Asia",
     "ctas": [{"label": "Water, Sanitation and the Behaviour Gap",
               "href": "/deepdives/water-sanitation-behaviour-gap.html"},
              {"label": "Nutrition 101", "href": "/101-courses/nutrition.html"},
              {"label": "All 101 courses", "href": "/101-courses/"}],
     "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]},
]

DECK = {
    "slug": "wash",
    "title": "Water, Sanitation and Hygiene 101",
    "description": ("Water, Sanitation and Hygiene 101: a free foundational course for "
                    "development practitioners in India and South Asia. The WHO/UNICEF JMP "
                    "service ladders; India's figures from the JMP, NFHS-5, NFHS-6 and the "
                    "NSS 76th round; Swachh Bharat Mission and the gap between ODF "
                    "declarations and survey evidence; Jal Jeevan Mission and its "
                    "functionality assessment; groundwater depletion, arsenic and "
                    "fluoride; water governance; faecal sludge, sanitation work and the "
                    "2013 Act on manual scavenging; handwashing and menstrual health; "
                    "climate and drought; and how to monitor a WASH programme. ImpactMojo, "
                    "CC BY-NC-ND."),
    "slides": SLIDES_A + SLIDES_B + SLIDES_C + SLIDES_D,
}

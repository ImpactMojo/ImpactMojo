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
         {"name": "India's numbers: JMP, NFHS and NSS"},
         {"name": "Swachh Bharat Mission: what was built"},
         {"name": "ODF claims and the survey evidence"},
         {"name": "Jal Jeevan Mission: taps, function and quality"},
         {"name": "Groundwater: depletion and contamination"},
         {"name": "Who governs water and sanitation"},
         {"name": "Faecal sludge, sanitation work and the 2013 Act"},
         {"name": "Hygiene: handwashing and menstrual health"},
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

    C("Pathways", "The F-diagram: how faeces reach a mouth", [
        flow(["Faeces", "Fluids", "Fingers", "Flies", "Fields", "Food", "New host"]),
        body("Public health teaching draws transmission as the F-diagram. Pathogens leave "
             "an infected person in faeces and reach the next person through water, hands, "
             "flies, soil and the food that all of these touch. Barriers work at two "
             "points. Primary barriers stop faeces entering the environment at all: a "
             "toilet that is used, safe child-faeces disposal and safe emptying of pits "
             "and tanks. Secondary barriers stop contamination that is already in the "
             "environment from reaching the mouth: handwashing, safe water storage and "
             "treatment, and food hygiene."),
        tw(pp("green", "Primary barriers",
              "A latrine that every member uses, including small children whose faeces "
              "carry more pathogens than adult faeces, plus a pit or tank that is emptied "
              "and treated without exposing workers or neighbours."),
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
        flow(["Ladders", "India's numbers", "Swachh Bharat", "ODF evidence", "Jal Jeevan",
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
              "Sources that by their design can deliver safe water: piped water, "
              "boreholes and tubewells, protected dug wells and springs, rainwater and "
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
              "proportions among people using improved sources: accessible on premises, "
              "available when needed and free from contamination. It reports the estimate "
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
                     "fitted value, not a measurement taken that year.",
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
    D("03", "Section Three", "India's numbers: JMP, NFHS and NSS"),

    C("India on the ladders", "India's WASH ladders in 2024, as the JMP estimates them", [
        table(["Rung", "Drinking water", "Sanitation", "Hygiene"],
              [["Safely managed", "76.4%", "Not estimated nationally", "Not defined"],
               ["Basic", "19.3%", "20.6% above the SM line, 83.4% at least basic", "89.7%"],
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
             "the larger story: in 2000 nearly three in four Indians defecated in the open. "
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
              "Sanitation is mostly on-site: pits and septic tanks serve 87.5% of rural "
              "people. Water quality is the weaker link, with 11.9% using sources not "
              "free from contamination (" + JMP + ")."),
           pp("amber", "Urban",
              "Shared toilets are commoner in towns, 12.6% against 8.3%. Fewer than four "
              "in ten urban residents are on a sewer, so most urban excreta still depends "
              "on emptying services (" + JMP + ").")),
    ], compact=True),

    C("Safely managed water", "For safely managed water, the binding constraint is the tap at home", [
        chart("washSmWater",
              "Components of safely managed drinking water, India, 2024 (% of population)",
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
             "every Jal Jeevan Mission tap that works adds directly to SDG 6.1. Quality "
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
               ["Women 15-24 using hygienic menstrual protection", "See Section 10",
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
              "The NSS rounds (76th round in 2018, the 78th round's multiple indicator "
              "survey, HCES 2023-24 and CAMS 2022-23) carry household latrine questions, "
              "and the JMP lists them as inputs. The ImpactMojo Deep Dive <em>What NFHS-6 "
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

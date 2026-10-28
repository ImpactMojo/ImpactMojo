# -*- coding: utf-8 -*-
"""
Disaster Risk and Heat Resilience 101 -- ImpactMojo 101 Series (native deck spec)
Hazard, exposure and vulnerability; the Sendai Framework; India's Disaster Management Act 2005
and the 2025 amendment; the response and mitigation funds and the Finance Commissions;
cyclones and Odisha's record; floods, landslides, lightning and drought; heat; early warning
and anticipatory action; relief, recovery and the people relief misses; insurance and social
protection in a shock; monitoring and evaluating preparedness.
Build: python3 scripts/deck-builder/build.py disaster_heat

House style: no em dashes, sentence-case headings, every statistic sourced on the slide,
every law cited by Act, year and section, teaching examples labelled Illustrative.

Sources opened while writing (October 2026):
- UNDRR, What is the Sendai Framework: https://www.undrr.org/implementing-sendai-framework/what-sendai-framework
- Sendai Framework text: https://www.undrr.org/media/16176/download
- Disaster Management Act 2005 (NIDM copy): https://nidm.gov.in/PDF/En_DM_act2005.pdf
- Disaster Management (Amendment) Act 2025, Gazette of 29 March 2025:
  https://www.thc.nic.in/Central%20Governmental%20Acts/Disaster%20Management%20Act,%202005.pdf
- PRS Bill track: https://prsindia.org/billtrack/the-disaster-management-amendment-bill-2024
- Sixteenth Finance Commission Report, Vol I, ch 11: https://www.indiabudget.gov.in/doc/16fcvol1.pdf
- Economic Survey 2021-22, para 2.35: https://www.indiabudget.gov.in/economicsurvey/ebook_es2022/files/basic-html/page90.html
- Cyclone Fani DLNA (Govt of Odisha, 2019): https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
- IMD heat wave definitions: https://mausam.imd.gov.in/pdfs/heatcolduser/Definition.pdf
- Knowlton et al. 2014, IJERPH 11(4):3473: https://doi.org/10.3390/ijerph110403473
- Azhar et al. 2014, PLoS One 9(3):e91831: https://doi.org/10.1371/journal.pone.0091831
- Hess et al. 2018, J Environ Public Health 7973519: https://doi.org/10.1155/2018/7973519
- Sherwood and Huber 2010, PNAS 107(21):9552: https://doi.org/10.1073/pnas.0913352107
- Vecellio et al. 2022, J Appl Physiol 132(2):340: https://doi.org/10.1152/japplphysiol.00738.2021
- ILO 2019, Working on a Warmer Planet: https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@dgreports/@dcomm/@publ/documents/publication/wcms_711919.pdf
- Pillai and Dalal 2023, CPR heat action plan assessment: https://cprindia.org/wp-content/uploads/2023/03/Heat-Report_27March-23_Updated-Table.pdf
- Human Rights Watch 2005, After the Deluge: https://www.hrw.org/reports/2005/india0505/india0505.pdf
- Pakistan Floods 2022 PDNA: https://www.pc.gov.pk/uploads/downloads/PDNA-2022.pdf
- VB-G RAM G Act 2025 (Act 36 of 2025): https://www.indiacode.nic.in/bitstream/123456789/22478/1/a2025-36.pdf
- SCC Online, 12 May 2026: https://www.scconline.com/blog/post/2026/05/12/vbgramg-act-implemented-from-1-july-2026/
- ThePrint, 7 August 2026: https://theprint.in/india/house-panel-recommends-record-rs-2-84-lakh-crore-disaster-fund-heatwaves-lightning-on-disaster-list/3008901/
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


def CH(canvas, ctype, title, source, data, options):
    return {"t": "chart", "canvas": canvas, "type": ctype, "title": title, "source": source,
            "data": data, "options": {"__js__": options}}


# Short source labels used on many slides
SENDAI = "Sendai Framework for Disaster Risk Reduction 2015-2030, UNDRR"
DMA = "Disaster Management Act 2005 (Act 53 of 2005)"
DMA25 = "Disaster Management (Amendment) Act 2025 (Act 10 of 2025), Gazette of India, 29 March 2025"
FC16 = "Report of the Sixteenth Finance Commission, Vol. I, ch. 11 (November 2025)"
FANI = "Government of Odisha, Cyclone Fani Damage, Loss and Needs Assessment (2019)"
IMD = "India Meteorological Department, heat wave and warm night definitions"
ILO = "ILO, Working on a Warmer Planet (2019), Table 6.2, Southern Asia, 1995 and 2030 (projections)"
CPR = "Pillai and Dalal, How is India Adapting to Heatwaves?, CPR (March 2023)"
HRW = "Human Rights Watch, After the Deluge: India's Reconstruction Following the 2004 Tsunami (May 2005)"
PDNA = "Government of Pakistan et al., Pakistan Floods 2022 Post-Disaster Needs Assessment"
VBG = "VB-G RAM G Act 2025 (Act 36 of 2025)"

SLIDES = []

# ===================== S1 TITLE, S2 TOC =====================
SLIDES += [
    {"type": "title",
     "main": "Disaster Risk and<br>Heat Resilience 101",
     "sub": "Hazard, exposure and vulnerability, the Sendai Framework, India's Disaster "
            "Management Act and its funds, cyclones, floods, drought and heat, early warning, "
            "relief and the people it misses, insurance and shock-responsive social protection",
     "tags": ["Disaster Risk", "Heat", "South Asia Focus", "100 Slides", "Free Access"]},

    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Hazard, exposure and vulnerability"},
         {"name": "The Sendai Framework 2015-2030"},
         {"name": "India's disaster law and institutions"},
         {"name": "Paying for disasters: the funds"},
         {"name": "Cyclones and Odisha's record"},
         {"name": "Floods, landslides and lightning"},
         {"name": "Drought"},
         {"name": "Heat"},
         {"name": "Early warning and anticipatory action"},
         {"name": "Relief, recovery and who relief misses"},
         {"name": "Insurance and social protection in a shock"},
         {"name": "Monitoring preparedness, and sources"},
     ]},
]

# ===================== SECTION 01: HAZARD, EXPOSURE, VULNERABILITY =====================
SLIDES += [
    D("01", "Section One", "Hazard, exposure and vulnerability"),

    C("Definition", "A disaster is what happens when a hazard meets people who cannot cope",
      TW([TERM("Disaster (DM Act 2005, s. 2(d))",
               "A catastrophe, mishap, calamity or grave occurrence arising from natural or man "
               "made causes, or by accident or negligence, which results in substantial loss of "
               "life or human suffering or damage to property or the environment, and is of such "
               "a nature or magnitude as to be beyond the coping capacity of the community of "
               "the affected area."),
          B("The last clause carries the idea that runs through this course. A cyclone over an "
            "empty sea is weather. The same cyclone over villages of thatched houses, with no "
            "shelter and no warning, is a disaster. The wind is the same in both cases. What "
            "differs is who is in its path and what they have to protect themselves with. The "
            "2025 amendment added an Explanation to s. 2(d) saying that man made causes do not "
            "include law and order situations.")],
         [B("Disaster risk practice therefore separates three things that are often run "
            "together in news reports and in project documents. The hazard is the physical "
            "event. Exposure is the people and assets in the place where it happens. "
            "Vulnerability is the set of conditions that decide how badly those people and "
            "assets are hurt. Each one can be changed by a different kind of action, and a "
            "programme that does not say which one it is working on usually cannot show that "
            "it worked."),
          H("amber", "Practitioners often call these natural disasters. The Act's definition, "
            "and this course, treat the hazard as natural and the disaster as the result of "
            "where people live, what they own and how they are governed.")])),

    C("The three parts", "The definitions now written into Indian law",
      T(["Term", "What the Act says (as amended in 2025)", "What changes it"],
        [["Hazard, s. 2(gc)", "A process or phenomenon relating to a disaster that may cause loss "
          "of life, injury or other health impacts, damage to property, social and economic "
          "disruption, or environmental degradation", "Mostly outside human control in the short "
          "run. Some hazards are made worse by people: deforestation and landslides, paved "
          "cities and flooding, emissions and heat."],
         ["Exposure, s. 2(gb)", "The situation of people, buildings, infrastructure, production "
          "capacities and other tangible assets, the environment and natural resources located "
          "in hazard-prone areas", "Land use rules, zoning, relocation, evacuation, where "
          "schools and hospitals are built"],
         ["Vulnerability, s. 2(w)", "Conditions determined by physical, social, economic and "
          "environmental factors or processes which increase the susceptibility of an "
          "individual, community, asset, infrastructure or system to the impact of hazard",
          "Housing quality, income, savings, health, caste and gender relations, access to "
          "information, social protection"],
         ["Disaster risk, s. 2(ea)", "Potential loss of life, injury, damage, disruption and "
          "degradation in a specific period, determined probabilistically as a function of "
          "hazard, exposure, vulnerability and capacity", "Reducing any of the first three, or "
          "raising capacity"],
         ["Resilience, s. 2(oc)", "The ability of a system, community or society exposed to "
          "hazards to resist, absorb, respond to and recover from the effects of a hazard in a "
          "timely and efficient manner", "Everything above, plus recovery systems"]]),
      B("Source: " + DMA25 + ", s. 2. These definitions were added in 2025. The 2005 Act had "
        "no definition of hazard, exposure, vulnerability or disaster risk.", sm=True),
      compact=True),

    C("The risk equation", "Why the three parts are multiplied together",
      TW([B("Risk analysts write disaster risk as a product: risk = hazard &times; exposure "
            "&times; vulnerability. The Sixteenth Finance Commission built its Disaster Risk "
            "Index for allocating money to States on exactly this rule, and explained why. "
            "Disaster risk only exists when hazard, exposure and vulnerability intersect. A "
            "severe hazard over an empty place carries no risk to people. A large, poor "
            "population in a place no hazard reaches carries none either."),
          B("The product form has a practical consequence. If any one term falls towards zero, "
            "risk falls towards zero, whatever the other two are doing. Moving a village out of "
            "a floodplain cuts exposure. Building a cyclone shelter and warning people in time "
            "cuts vulnerability for the hours that matter. Neither changes the hazard."),
          B("Source: " + FC16 + ", paras 11.48 to 11.51.", sm=True)],
         [T(["Term in the FC-16 index", "Measured by"],
            [["Hazard", "Ten disasters scored by quintile from IMD, CWC, GSI, NCS, BIS and "
              "Agriculture Ministry data: flood, drought, cyclone, earthquake, landslide, "
              "hailstorm, cold wave, cloudburst, lightning, heatwave"],
             ["Exposure", "Projected State population, October 2026"],
             ["Vulnerability", "State per-capita income, average of 2018-19 to 2023-24, "
              "leaving out 2020-21"],
             ["Weighting", "Hazard scores weighted by each disaster's share of past "
              "expenditure; index then multiplied out"]]),
          H("cyan", "A State-level index uses income as its vulnerability measure because it is "
            "available for every State. Inside a district, a programme needs finer measures: "
            "housing material, who has a phone, who cannot walk to a shelter.")])),

    C("Illustration", "Two villages, one cyclone",
      TW([P("cyan", "Village A (Illustrative)",
            "Pucca houses, a multipurpose cyclone shelter 800 metres away, a trained village "
            "task force, a siren tower, a fair price shop stocked before landfall, and fishing "
            "boats hauled up two days earlier on official advice. Most families have a mobile "
            "phone and received the warning in Odia. The same wind blows the roofs off two cattle "
            "sheds and floods the fields for a week."),
          P("red", "Village B (Illustrative)",
            "Kutcha houses on a low sandbar, the nearest shelter 6 km away across a creek, "
            "landless households who work for daily wages and have no savings, older people "
            "living alone, and a hamlet of migrant salt-pan workers who are not on the panchayat "
            "list. The warning arrives, but nobody comes to move the people who cannot walk.")],
         [B("The hazard is identical. Exposure is higher in B because of where the houses stand. "
            "Vulnerability is higher in B because of what the houses are made of, who lives in "
            "them, and who the warning and transport systems were designed for. The loss in B "
            "will be measured in lives. The loss in A will be measured in crops and roofs."),
          BL(["Every disaster assessment that reports one district-level death toll averages A "
              "and B together and hides the difference.",
              "Every preparedness plan has to say how it will reach the people in B who are "
              "least visible to it: the migrants, the disabled, older people alone, and "
              "households outside the official lists.",
              "Section 10 returns to this with documented cases from the 2004 tsunami and "
              "Cyclone Fani."], "amber")])),

    C("Hazard types", "The hazards a South Asian practitioner meets",
      T(["Hazard", "Speed of onset", "Main harm", "Where in South Asia"],
        [["Tropical cyclone and storm surge", "Days of warning, hours of impact", "Wind, surge "
          "flooding, saline intrusion", "Bay of Bengal coasts: Odisha, Andhra Pradesh, West "
          "Bengal, Bangladesh, Myanmar; Arabian Sea coasts: Gujarat, Sindh"],
         ["Riverine flood", "Days", "Inundation, loss of crops and houses, disease",
          "Ganga and Brahmaputra basins, Indus plain in Pakistan"],
         ["Flash flood, cloudburst, GLOF", "Minutes to hours", "Sudden deaths, destroyed roads and "
          "bridges", "Himalaya and hill States, northern Pakistan, Nepal, Bhutan"],
         ["Landslide", "Minutes, often after days of rain", "Deaths, cut-off settlements",
          "Western Ghats, Himalaya, North-East"],
         ["Lightning", "Seconds", "Deaths of people working or sheltering outdoors",
          "Across India"],
         ["Drought", "Months to years", "Crop and income loss, water scarcity, distress migration",
          "Rainfed districts of the Deccan, Rajasthan, Bundelkhand, Balochistan"],
         ["Heatwave and humid heat", "Days, with warning", "Heatstroke, deaths of older and "
          "outdoor-working people, lost work hours", "North and central India, Pakistan's "
          "Sindh and Punjab, coastal cities in humid heat"],
         ["Earthquake and tsunami", "No warning for earthquakes; minutes to hours for tsunami",
          "Building collapse; coastal inundation", "Himalayan arc, Gujarat, Andaman and Nicobar"]]),
      B("Geographic notes are general. Hazard maps for a specific district come from IMD, CWC, "
        "GSI and the State Disaster Management Authority, which the Finance Commission also "
        "used for its hazard scores (" + FC16 + ", para 11.49).", sm=True),
      compact=True),

    C("Slow and fast", "Slow-onset hazards are disasters too, and they are financed differently",
      TW([B("A cyclone has a landfall time. A drought has no single day on which it begins, and "
            "a heatwave builds over a week. Public systems are better at responding to events "
            "with a date. Rescue teams, relief camps and ex gratia payments are designed for "
            "the cyclone. Drought and heat harm people through lost income, debt, migration "
            "and illness spread over months, and that harm is easier to miss and harder to "
            "count."),
          B("The financing shows the bias. Of what States spent on notified disasters from "
            "2019-20 to 2023-24, floods took 55.09 per cent and drought 17.26 per cent. Heat "
            "was not on the national list of notified disasters at all. It was a State-specific "
            "disaster in eleven States, paid for out of a 10 per cent window in each State's "
            "response fund (" + FC16 + ", paras 11.44, 11.65, 11.66).")],
         [CH("dhExpChart", "bar", "Disaster-wise expenditure of States, 2019-20 to 2023-24 (% of total)",
             "Sixteenth Finance Commission Report, Vol. I, Figure 11.5, from the MHA National "
             "Disaster Management Information System",
             {"labels": ["Flood", "Drought", "State-specific", "Cyclone", "Landslide", "Hailstorm",
                         "Cold wave/frost", "Pest attack", "Fire", "Cloudburst"],
              "datasets": [{"label": "% of expenditure",
                            "data": [55.09, 17.26, 13.27, 6.94, 2.59, 1.94, 1.12, 0.94, 0.51, 0.32],
                            "backgroundColor": "#0EA5E9"}]},
             "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:60, title:{display:true,text:'% of State disaster expenditure'} } } }"),
          B("Earthquake accounted for 0.002 per cent and is left off the chart.", sm=True)]),
      compact=True),

    C("Compounding", "Hazards arrive together, and one makes the next worse",
      TW([B("Disaster risk practice used to plan for one hazard at a time. Recent events in "
            "South Asia rarely arrive alone. Pakistan's 2022 floods combined torrential rain, "
            "riverine, urban and flash flooding, accelerated glacial melt and landslides. About "
            "33 million people were affected, one in seven Pakistanis, and nearly 8 million "
            "were displaced (" + PDNA + ")."),
          B("Heat and drought reinforce each other: hot days dry soil faster, and dry soil heats "
            "faster. A cyclone in the middle of a pandemic forces shelters to choose between "
            "crowding and distancing. A flood that destroys a primary health centre removes "
            "the place where heatstroke cases would have been treated the following summer.")],
         [T(["Combination", "What it does"],
            [["Heat followed by extreme rain", "Dry, hard soil runs off faster; flash floods"],
             ["Cyclone followed by flood", "Surge and river flooding after landfall; saline "
              "fields for years"],
             ["Drought followed by heat", "Water scarcity at the time people most need water"],
             ["Disaster during an epidemic", "Shelters become transmission sites; health staff "
              "are diverted"],
             ["Repeated small events", "Each one erodes savings, so the next does more harm"]]),
          H("amber", "The Sixteenth Finance Commission notes that States asked for more money "
            "because heavy rainfall, heatwaves and cloudbursts were making droughts, landslides "
            "and floods more severe (" + FC16 + ", para 11.24).")])),

    C("For practitioners", "Questions to ask of any disaster risk programme",
      TW([BL(["Which hazard is it about, and how was the hazard mapped? Whose data, at what "
              "resolution, for which years?",
              "Who is exposed? Has the programme counted people who are not on household "
              "lists: migrants, people in informal settlements, nomadic and pastoral groups?",
              "What makes people here vulnerable, and how was that established? Was there a "
              "vulnerability assessment, or a list copied from a guideline?",
              "Which of the three terms does the intervention change? A shelter, an embankment, "
              "a warning system and a cash transfer act on different terms.",
              "What happens to the person who cannot read the warning, cannot walk to the "
              "shelter, or will lose a day's wage by going?"], "cyan")],
         [B("These questions come before any discussion of law or money, because the law and the "
            "money follow from the answers. A district plan that cannot answer them is a list "
            "of departments and phone numbers. A plan that can answer them tells an officer "
            "where to send the boat first."),
          H("green", "For the climate science behind changing hazards, see ImpactMojo's "
            "<a href=\"https://www.impactmojo.in/101-courses/climate-essentials.html\">Climate "
            "Essentials 101</a>. For who bears environmental harm and why, see "
            "<a href=\"https://www.impactmojo.in/101-courses/env-justice.html\">Environmental "
            "Justice 101</a>.")])),
]

# ===================== SECTION 02: SENDAI =====================
SLIDES += [
    D("02", "Section Two", "The Sendai Framework 2015-2030"),

    C("Origins", "From Hyogo to Sendai",
      TW([B("The Sendai Framework for Disaster Risk Reduction 2015-2030 was adopted on 18 March "
            "2015 at the Third UN World Conference on Disaster Risk Reduction in Sendai, Japan, "
            "and endorsed by the UN General Assembly. It replaced the Hyogo Framework for Action "
            "2005-2015, and was the outcome of consultations that began in March 2012 and "
            "intergovernmental negotiations from July 2014 to March 2015."),
          B("It is a voluntary agreement that creates no binding obligations. Countries "
            "report against 38 global indicators through the online "
            "Sendai Framework Monitor, and UNDRR is charged with supporting implementation, "
            "follow-up and review. It sits alongside the Paris Agreement, the Addis Ababa "
            "Action Agenda, the New Urban Agenda and the Sustainable Development Goals.")],
         [T(["Shift from Hyogo identified in the Sendai foreword", "What it means"],
            [["Disaster risk management, as opposed to disaster management", "Act on risk "
              "before the event as well as on the event"],
             ["Seven global targets", "Progress measured against quantified goals, with 38 "
              "indicators"],
             ["A goal focused on preventing new risk and reducing existing risk", "Planning "
              "decisions become disaster decisions"],
             ["Scope broadened to natural and man-made hazards", "Includes environmental, "
              "technological and biological hazards"],
             ["Health resilience promoted throughout", "Hospitals and health systems count as "
              "critical infrastructure"],
             ["Primary responsibility of States, with all-of-society engagement", "Shared with "
              "local government, the private sector and others"]]),
          B("Source: UNDRR, What is the Sendai Framework; " + SENDAI + ", foreword.", sm=True)])),

    C("Goal", "One outcome and one goal",
      TW([Q("The substantial reduction of disaster risk and losses in lives, livelihoods and "
            "health and in the economic, physical, social, cultural and environmental assets of "
            "persons, businesses, communities and countries.",
            "Sendai Framework, para 16, expected outcome"),
          Q("Prevent new and reduce existing disaster risk through the implementation of "
            "integrated and inclusive economic, structural, legal, social, health, cultural, "
            "educational, environmental, technological, political and institutional measures "
            "that prevent and reduce hazard exposure and vulnerability to disaster, increase "
            "preparedness for response and recovery, and thus strengthen resilience.",
            "Sendai Framework, para 17, goal")],
         [B("Read the goal as three instructions. Preventing new risk means not building the "
            "next school on the floodplain. Reducing existing risk means retrofitting the school "
            "that is already there. Strengthening resilience means preparing to respond and "
            "recover when the remaining risk becomes a disaster."),
          B("The first instruction is the cheapest and the most often ignored. Most risk in "
            "fast-growing South Asian cities is being created now, by where housing, roads and "
            "industry are built. A framework that only funds response will keep paying for "
            "risk that planning decisions made yesterday."),
          H("cyan", "The goal names exposure and vulnerability explicitly. It says nothing about "
            "stopping hazards, because most cannot be stopped.")])),

    C("Seven targets", "The seven global targets",
      T(["Target", "What it asks for", "By"],
        [["(a) Mortality", "Substantially reduce global disaster mortality, aiming to lower the "
          "average per 100,000 mortality rate in 2020-2030 compared with 2005-2015", "2030"],
         ["(b) Affected people", "Substantially reduce the number of affected people, aiming to "
          "lower the average per 100,000 in 2020-2030 compared with 2005-2015", "2030"],
         ["(c) Economic loss", "Reduce direct disaster economic loss in relation to global GDP",
          "2030"],
         ["(d) Infrastructure and services", "Substantially reduce damage to critical "
          "infrastructure and disruption of basic services, among them health and educational "
          "facilities, including by developing their resilience", "2030"],
         ["(e) Strategies", "Substantially increase the number of countries with national and "
          "local disaster risk reduction strategies", "2020"],
         ["(f) Cooperation", "Substantially increase international cooperation with developing "
          "countries through adequate and sustainable support", "2030"],
         ["(g) Early warning", "Substantially increase the availability of and access to "
          "multi-hazard early warning systems and disaster risk information and assessments "
          "to people", "2030"]]),
      B("Source: " + SENDAI + ", para 18. Targets (a) to (d) are outcomes and are measured with "
        "loss data. Targets (e) to (g) are about means. Target (e) carried an earlier deadline "
        "because strategies were meant to be in place before the outcomes could move.",
        sm=True),
      compact=True),

    C("Four priorities", "Four priorities for action",
      TW([T(["Priority", "In plain terms"],
            [["1. Understanding disaster risk", "Know the hazard, who is exposed, who is "
              "vulnerable and what capacity exists. Use the knowledge for prevention, "
              "mitigation, preparedness and response."],
             ["2. Strengthening disaster risk governance", "Laws, institutions, plans and "
              "national platforms that assign responsibility at every level."],
             ["3. Investing in disaster risk reduction for resilience", "Public and private "
              "money for structural measures (shelters, embankments) and non-structural "
              "measures (land use rules, insurance, social protection)."],
             ["4. Preparedness and Build Back Better", "Prepare for response, act in "
              "anticipation of events, and use recovery to reduce future risk."]])],
         [B("The fourth priority contains the phrase that became a slogan, Build Back Better. "
            "UNDRR describes recovery, rehabilitation and reconstruction as a critical "
            "opportunity to integrate risk reduction into development. In practice that means "
            "a house rebuilt after a cyclone should be able to withstand the next one, and a "
            "school rebuilt after a flood should be on a plinth."),
          B("The same priority asks countries to take action in anticipation of events. That "
            "sentence is the basis for the anticipatory action discussed in section 09.",
            sm=True),
          H("amber", "The priorities are a checklist for reading a State disaster management "
            "plan. A plan that lists response equipment in detail and says nothing about "
            "priority 1 has skipped the step that decides where the equipment should go.")])),

    C("Whose framework", "The groups the framework names",
      TW([B("Paragraph 7 says governments should engage women, children and youth, persons with "
            "disabilities, poor people, migrants, indigenous peoples, volunteers, practitioners "
            "and older persons in designing and implementing policies, plans and standards."),
          B("Paragraph 36 goes further. It says persons with disabilities and their "
            "organisations are critical in assessing disaster risk and in designing plans "
            "tailored to specific requirements, taking into account universal design. It says "
            "older persons should be included in designing policies and early warning, and "
            "that migrants contribute to the resilience of communities and their knowledge "
            "can be useful in designing disaster risk reduction. Paragraph 27(h) asks that "
            "local authorities be given the regulatory and financial means to work with civil "
            "society, communities, indigenous peoples and migrants.")],
         [T(["Group", "Where named", "Why it matters in South Asia"],
            [["Persons with disabilities", "Paras 7, 32, 36(a)(iii)", "Shelters, warnings and "
              "evacuation transport are rarely designed for them"],
             ["Older persons", "Paras 7, 36(a)(iv)", "Highest heat mortality; least able to "
              "evacuate"],
             ["Migrants", "Paras 7, 27(h), 36(a)(vi)", "Often absent from household lists used "
              "for relief"],
             ["Women", "Paras 7, 32, 36(a)(i)", "Relief often paid to male heads of household"],
             ["Indigenous peoples", "Paras 7, 27(h), 36(a)(v)", "Adivasi land and forest rights shape "
              "exposure"]]),
          B("Source: " + SENDAI + ". Caste is not named in the framework. In South Asia it "
            "decides who is reached by relief, as section 10 shows.", sm=True)])),

    C("Measuring it", "How Sendai progress is measured",
      TW([B("UNDRR's Sendai Framework Monitor captures progress that member states report "
            "themselves against 38 indicators. A sub-system, DesInventar Sendai, lets countries "
            "build disaster loss databases to collect the data for targets (a) to (d): deaths, "
            "affected people, economic loss and damage to infrastructure."),
          B("Self-reporting is the framework's weakness. A country that records few heat "
            "deaths will appear to be meeting target (a) on heat whatever is actually happening. "
            "Loss databases are only as complete as the death certificates, revenue records and "
            "damage surveys that feed them."),
          B("Source: UNDRR, What is the Sendai Framework, section on monitoring scope.", sm=True)],
         [T(["Level", "What is measured", "Who defines it"],
            [["Outcome", "Global targets (a) to (g), 38 indicators", "Agreed globally; "
              "comparable"],
             ["Output", "Reduction of risk and increase in resilience", "National targets"],
             ["Input", "Public policy measures implementing the four priorities", "National "
              "indicators"],
             ["Custom", "Country-chosen targets reported in national DRR reports",
              "Member states"]]),
          H("cyan", "India's 2025 amendment requires a national disaster database and State "
            "databases covering disaster assessment, fund allocation, expenditure, plans and a "
            "risk register (" + DMA25 + ", s. 2(da) and s. 6(2)(v)). That is the domestic "
            "source a Sendai report should draw on.")])),

    C("Reading Sendai locally", "What Sendai asks of a district",
      T(["Sendai element", "District-level question", "Evidence a district can produce"],
        [["Target (a) mortality", "How many people died in disasters each year, by hazard, age "
          "and sex?", "Ex gratia records, death registration, hospital records"],
         ["Target (b) affected", "How many households were displaced, lost crops, lost work?",
          "Relief registers, crop loss surveys"],
         ["Target (d) services", "Which schools, health centres and roads were damaged, and for "
          "how long were they closed?", "Department damage reports"],
         ["Target (e) strategy", "Is there a district disaster management plan, updated, with "
          "a hazard and vulnerability assessment?", "The plan itself"],
         ["Target (g) early warning", "What share of villages received the last warning, by "
          "what channel, how long before impact?", "SMS logs, siren records, community "
          "surveys"],
         ["Priority 1", "Is there a hazard map and a list of vulnerable people by village?",
          "Maps, registers of older and disabled people"],
         ["Priority 4", "Were rebuilt houses and schools built to resist the next event?",
          "Engineering inspection"]]),
      B("Illustrative. The table is a way of translating global targets into records an Indian "
        "district already keeps or could keep.", sm=True),
      compact=True),
]

# ===================== SECTION 03: LAW AND INSTITUTIONS =====================
EPW = ("Jos Chathukulam, Disaster Management (Amendment) Act, 2025: Old Wine in a New Bottle?, "
       "Economic and Political Weekly, 26 July 2025, Vol. 60, No. 30")

SLIDES += [
    D("03", "Section Three", "India's disaster law and institutions"),

    C("The Act", "The Disaster Management Act 2005 builds three tiers of authority",
      TW([T(["Tier", "Body", "Chair", "Section"],
            [["National", "National Disaster Management Authority (NDMA)", "Prime Minister, ex "
              "officio", "s. 3"],
             ["National", "National Executive Committee", "Union Home Secretary", "s. 8, s. 10"],
             ["National", "National Crisis Management Committee", "Cabinet Secretary",
              "s. 8A (2025)"],
             ["National", "High Level Committee (central assistance)", "Minister in charge of "
              "disaster management", "s. 8B (2025)"],
             ["State", "State Disaster Management Authority (SDMA)", "Chief Minister, ex officio",
              "s. 14"],
             ["State", "State Executive Committee", "Chief Secretary", "s. 20"],
             ["District", "District Disaster Management Authority (DDMA)", "Collector or District "
              "Magistrate; elected local representative as co-chair", "s. 25"],
             ["City", "Urban Disaster Management Authority", "Municipal Commissioner",
              "s. 41A (2025)"]])],
         [B("Before 2005 India handled disasters through relief codes and relief commissioners "
            "in the States. The Act gave disaster management a statute, permanent bodies at "
            "each level, plans that must be written and approved, a specialist force and "
            "statutory funds. It applies to natural and man-made disasters alike."),
          B("The chairs show where the Act places authority. The national and State bodies are "
            "headed by the elected head of government. The district body, which does most of the "
            "work, is headed by the Collector, an appointed civil servant, with an elected "
            "representative of the local authority as co-chair."),
          B("Sources: " + DMA + ", ss. 3, 14, 25; " + DMA25 + ", ss. 8A, 8B, 41A; " + FC16 +
            ", paras 11.3 to 11.7 for the NEC and SEC chairs.", sm=True)]),
      compact=True),

    C("The district", "The DDMA is where plans meet people",
      TW([B("Section 25 requires every State to establish a DDMA for every district. Its members "
            "are the Collector as chair, the elected representative of the local authority as "
            "co-chair, the chief executive officer of the DDMA, the Superintendent of Police, "
            "the Chief Medical Officer and up to two other members. Since 2025 those two may be "
            "district officers, disaster management experts or people from civil society "
            "organisations (s. 25(2)(f), as substituted). Where a zila "
            "parishad exists, its chairperson is co-chair. In Sixth Schedule tribal areas the "
            "Chief Executive Member of the autonomous district council is co-chair."),
          B("The DDMA prepares the district disaster management plan, coordinates departments, "
            "and monitors whether local authorities comply. The Sixteenth Finance Commission "
            "calls DDMAs the critical hubs for planning, coordination and implementation, and "
            "notes that local authorities, including panchayats, municipalities and autonomous "
            "district councils, are responsible for their own plans and for relief and "
            "reconstruction in their areas (" + FC16 + ", paras 11.7, 11.8, 11.14).")],
         [P("amber", "A criticism worth knowing",
            "Jos Chathukulam argues in EPW that a DDMA headed by a bureaucrat, with the elected "
            "local functionary only as co-chair, is a sign of centralisation. He notes that in "
            "Kerala district panchayat presidents are DDMA co-chairs, but that during COVID-19 "
            "the Collectors ran DDMA meetings and the presidents' role was rare. He also argues "
            "that neither the 2005 Act nor the 2025 amendment provides financial allocations "
            "to the lower levels of administration."),
          B("Source: " + EPW + ".", sm=True),
          H("cyan", "For a practitioner, the DDMA's plan and its meeting minutes are public "
            "documents in most States. Read them before designing a district programme.")])),

    C("2025 amendment", "What the Disaster Management (Amendment) Act 2025 changed",
      T(["Change", "Provision", "What it means"],
        [["Definitions added", "s. 2: hazard, exposure, vulnerability, disaster risk, "
          "evacuation, recovery, rehabilitation, resilience, response, prevention, disaster "
          "database", "Indian law now uses the same risk vocabulary as Sendai"],
         ["Disaster risk reduction inside disaster management", "Explanation to s. 2(e)",
          "Reducing exposure and vulnerability and improving preparedness are part of the "
          "statutory meaning of disaster management"],
         ["Plans made by the Authorities", "ss. 6(2)(b), 11(2) for NDMA; ss. 18(2)(b), 23 for SDMAs",
          "NDMA and SDMAs coordinate the preparation and approval of plans, which earlier sat "
          "with the executive committees"],
         ["New NDMA functions", "s. 6(2)(k) to (w)", "Periodic stock-take of all risks including "
          "emerging risks from extreme climate events, preparedness assessment of each State, "
          "post-disaster audit, a national disaster database, minimum standards of relief"],
         ["NDMA staff", "New s. 5", "NDMA may specify its own staff with Central Government "
          "approval, and appoint experts"],
         ["NCMC and HLC made statutory", "ss. 8A, 8B", "Existing committees given a footing in "
          "law"],
         ["Urban authorities", "s. 41A", "States may create Urban Disaster Management "
          "Authorities for capitals and municipal corporation cities"],
         ["State response forces", "s. 44A", "States may constitute a State Disaster Response "
          "Force"],
         ["Relief standards and non-discrimination", "ss. 12, 13, 19 omitted; s. 61 amended",
          "Standards moved into NDMA and SDMA functions; compensation dropped from the "
          "non-discrimination clause"],
         ["Power over persons", "New s. 60A", "Union or State may by notification require anyone "
          "to act or refrain in relation to a hazard, for up to six months, with a penalty of up "
          "to ₹10,000"],
         ["Plan review", "ss. 11(4), 23(5), 31(4)", "National and State plans reviewed every three "
          "years and updated every five; district plans reviewed at least every two years"],
         ["Law and order excluded", "Explanation to s. 2(d)", "Man made causes do not include law "
          "and order situations"]]),
      B("Source: " + DMA25 + ". The Bill was introduced in the Lok Sabha on 1 August 2024, "
        "passed by the Lok Sabha on 12 December 2024 and by the Rajya Sabha on 25 March 2025 "
        "(PRS Legislative Research, Bill track), and received the President's assent on 29 "
        "March 2025.", sm=True),
      compact=True),

    C("Cities and forces", "Urban authorities and State response forces",
      TW([TERM("Urban Disaster Management Authority, s. 41A",
               "A State may, by notification, constitute a separate authority for its capital "
               "and for every city with a Municipal Corporation, except the National Capital "
               "Territory of Delhi and the Union territory of Chandigarh. The Municipal "
               "Commissioner chairs it and the District Collector is vice chair. It prepares and "
               "implements an Urban Plan for disaster management."),
          B("Cities had been planned for through district plans drawn for mostly rural "
            "districts. Urban flooding, heat islands, building collapse and fire behave "
            "differently, and the municipal corporation controls drains, building permits and "
            "street-level services. Placing the authority with the Municipal Commissioner puts "
            "it with the body that controls those levers. The Act says a State may create "
            "these authorities. It does not require them.")],
         [TERM("State Disaster Response Force, s. 44A",
               "A State may constitute a State Disaster Response Force for specialist response to "
               "a threatening disaster situation or disaster, with functions and service "
               "conditions set by the State. The 2005 Act provided only the National Disaster "
               "Response Force (s. 44)."),
          B("Many States had already raised such forces before the amendment gave them a legal "
            "basis. Odisha created the Odisha Disaster Rapid Action Force after the 1999 super "
            "cyclone and had 10 units by 2019 (" + FANI + ", ch. 15). The Sixteenth Finance "
            "Commission describes State forces as an important first line of defence alongside "
            "the NDRF (" + FC16 + ", para 11.15)."),
          H("amber", "A note on initials. NDRF means both the National Disaster Response Force "
            "(s. 44) and the National Disaster Response Fund (s. 46). SDRF means both State "
            "forces and State funds. Check which one a document means.")])),

    C("Severe disasters", "How a State gets central money after a severe disaster",
      FLOW("State meets the first costs from its State Disaster Response Fund",
           "State submits a memorandum seeking central assistance",
           "Inter-Ministerial Central Team visits and assesses damage",
           "Inter-Ministerial Group, chaired by the Union Home Secretary, scrutinises",
           "High Level Committee approves assistance from the National Disaster Response Fund"),
      TW([B("For a calamity of severe nature, an Inter-Ministerial Central Team assesses the damage "
            "and recommends assistance. The Inter-Ministerial Group headed by the Union Home "
            "Secretary, or the Secretary, Agriculture for agricultural disasters, scrutinises the "
            "assessment, and the High Level Committee of Cabinet Ministers gives final approval "
            "(" + FC16 + ", para 11.11). The 2025 amendment wrote the High Level Committee into "
            "the Act at s. 8B, as the body that provides assistance under s. 46 and approves "
            "mitigation assistance under s. 47.")],
         [B("Sequence matters for people waiting for help. A State's own fund can be spent at "
            "once. Central money comes only after a memorandum, a team visit, scrutiny and "
            "approval. Several States told the Finance Commission that NDRF approval and "
            "disbursal were delayed (" + FC16 + ", para 11.29). After Cyclone Fani, the MHA "
            "sanctioned an advance of ₹340.87 crore to Odisha on the decision of the National "
            "Crisis Management Committee (" + FANI + ", executive summary)."),
          H("cyan", "A district practitioner rarely sees this process, but its timing decides "
            "when reconstruction money reaches the village.")]),
      compact=True),

    C("Rights in the Act", "What the Act promises to people affected by disaster",
      TW([TERM("Minimum standards of relief, now s. 6(2)(w)",
               "The NDMA recommends guidelines for minimum standards of relief, which may "
               "include the minimum requirements in relief camps for shelter, food, drinking "
               "water, medical cover and sanitation, special provision for widows and orphans, "
               "ex gratia for loss of life, and assistance for damaged houses and for restoring "
               "livelihoods. Each SDMA lays down State standards, which may not be lower than the "
               "national minimum (s. 18(2)(o))."),
          TERM("Prohibition against discrimination, s. 61",
               "While providing relief to the victims of disaster, there shall be no "
               "discrimination on the ground of sex, caste, community, descent or religion.")],
         [B("In the 2005 Act the minimum standards sat in s. 12, which said the guidelines shall "
            "include those items. The 2025 amendment omitted ss. 12, 13 and 19 and moved the "
            "standards into the functions of the NDMA and SDMAs, where the list may include them. "
            "Section 13, also omitted, had let the NDMA recommend relief in loan repayment."),
          B("The amendment also deleted the words compensation and from s. 61. Before 2025 the "
            "ban on discrimination covered compensation and relief. It now names relief only. "
            "The list of grounds does not include disability, age or migrant status, so those "
            "groups rely on the general law and on the plans."),
          B("Sources: " + DMA + ", ss. 12, 13, 61; " + DMA25 + ", ss. 5, 9, 10, 11, 37 of the "
            "amending Act.", sm=True),
          H("red", "A practitioner documenting exclusion from relief should cite s. 61 as it now "
            "stands, and should not assume it reaches compensation.")])),

    C("Plans", "The plan is the document that turns the law into action",
      T(["Plan", "Prepared by", "What to look for when reading it"],
        [["National Plan", "NDMA, after 2025, through its coordination of preparation and "
          "approval (s. 6(2)(b))", "Hazard-wise responsibilities of Union ministries"],
         ["State Plan", "SDMA, in consultation with local, district and urban authorities and "
          "people's representatives (s. 23(2))", "The exposure of each part of the State and the "
          "vulnerability of its people, assets and livelihoods (s. 23(4)(a))"],
         ["District Plan", "DDMA, approved by the SDMA (s. 18(2)(ca))", "Village-level lists of "
          "vulnerable people, shelters, routes, stockpiles, contact persons; s. 31(4) now requires "
          "review at least every two years"],
         ["Urban Plan", "Urban Disaster Management Authority, s. 41A(4)", "Drainage, heat, "
          "building safety, informal settlements"],
         ["Departmental plans", "Each ministry and department", "Whether schools, hospitals and "
          "roads are built to resist local hazards"],
         ["Heat action plans", "State, district or city authorities", "Not created by the Act. "
          "Section 08 shows most do not state their legal basis."]]),
      TW([B("A plan that has not been updated since it was first written is common. A useful "
            "test is whether the plan names people and places or only departments and "
            "telephone numbers.", sm=True)],
         [H("amber", "The 2025 amendment requires NDMA to undertake post-disaster audits of "
            "preparedness and response in a State after a severe disaster (s. 6(2)(u)). Those "
            "audits, once published, are a new source of evidence on whether plans worked.")]),
      compact=True),

    C("Reading the law", "What the amendment did not do",
      TW([B("Jos Chathukulam's EPW commentary argues that most of the 2025 amendment strengthens "
            "a centralised, top-down approach. His points are that the new staffing and "
            "regulation powers of the NDMA, the statutory status of the NCMC and HLC, and the "
            "removal of the specified purposes for which the National Disaster Response Fund "
            "may be used all concentrate authority, that local governments are given no larger "
            "role, and that the amendment contains no comprehensive provisions for pandemics "
            "or for the particular vulnerability of women, persons with disabilities and "
            "marginalised groups."),
          B("Source: " + EPW + ".", sm=True)],
         [B("The government's case for the amendment rests on clarity and data: definitions "
            "aligned with Sendai, plans prepared by the Authorities themselves, a national and "
            "State disaster database, preparedness assessments and post-disaster audits. Both "
            "readings can be true at once. A database and an audit power are useful tools, and "
            "who controls them decides whom they serve."),
          BL(["Ask whether your State has notified an Urban Disaster Management Authority for "
              "its cities, and who sits on it.",
              "Ask whether the State has published its disaster database, and whether it "
              "records deaths by sex, age and social group.",
              "Ask whether panchayats have their own disaster plans and any money to act on "
              "them."], "cyan")])),
]

# ===================== SECTION 04: FUNDS =====================
SLIDES += [
    D("04", "Section Four", "Paying for disasters: the funds"),

    C("The funds", "Four statutory funds, two national and two in each State",
      TW([T(["Fund", "Section", "Used for"],
            [["National Disaster Response Fund (NDRF)", "s. 46", "Central assistance to States "
              "for severe disasters; after 2025, for different aspects of disaster management"],
             ["National Disaster Mitigation Fund (NDMF)", "s. 47", "Projects exclusively for "
              "mitigation, applied by NDMA"],
             ["State Disaster Response Fund (SDRF)", "s. 48(1)(a)", "Relief and response in the "
              "State, first call after any notified disaster"],
             ["State Disaster Mitigation Fund (SDMF)", "s. 48(1)(c)", "Mitigation projects in the "
              "State"],
             ["District response and mitigation funds", "s. 48(1)(b), (d)", "Provided in the Act; "
              "the Fifteenth Finance Commission found them not practical"]])],
         [B("The Act provided mitigation funds from 2005. They existed on paper only until the "
            "Fifteenth Finance Commission recommended they be constituted with real money. As a "
            "result, the Sixteenth Finance Commission reports that all the funds envisaged under "
            "the Act have been constituted by all the States and the Union, except the district "
            "funds (" + FC16 + ", para 11.1)."),
          B("Money flows in through the Finance Commission. Each Commission recommends how "
            "much goes into the State funds for its five-year award period, how it is split "
            "between the Union and the States, and how it is shared among States."),
          H("amber", "States contribute 25 per cent of SDRF and SDMF, and the Union 75 per cent. "
            "For north-eastern and Himalayan States the split is 90:10 (" + FC16 +
            ", para 11.61).")])),

    C("History", "From margin money to mitigation funds",
      T(["Commission", "What it introduced"],
        [["Second Finance Commission", "Margin money for calamities of moderate nature, based on "
          "average relief spending of the previous decade"],
         ["Eighth", "50 per cent Union contribution; fire to be treated as a disaster like flood, "
          "cyclone and earthquake"],
         ["Ninth", "Calamity Relief Fund, 75 per cent Union and 25 per cent State"],
         ["Tenth", "National Fund for Calamity Relief for severe calamities"],
         ["Eleventh", "Dissolved the national fund after its corpus ran out in three years; "
          "created a National Calamity Contingency Fund with ₹500 crore"],
         ["Twelfth", "Added landslides, avalanches, cloudbursts and pest attacks to the notified "
          "list"],
         ["Thirteenth", "Merged the old funds into the SDRF and NDRF under the 2005 Act"],
         ["Fourteenth", "Let States spend up to 10 per cent of SDRF on locally significant "
          "disasters not on the national list"],
         ["Fifteenth", "Mixed a Disaster Risk Index with past spending; created the mitigation "
          "funds; set sub-windows and earmarked allocations"],
         ["Sixteenth", "Expanded the risk index to ten hazards; moved preparedness to the "
          "mitigation funds; recommended heatwave and lightning as national disasters"]]),
      B("Source: " + FC16 + ", paras 11.16 to 11.19, 11.55, 11.56, 11.73.", sm=True),
      compact=True),

    C("Growth", "State disaster fund allocations, by Finance Commission",
      TW([CH("dhFcChart", "bar", "Allocation to State disaster funds, by Finance Commission award (₹ crore)",
             "FC-11 to FC-15 from Sixteenth Finance Commission Report, Vol. I, Figure 11.1; FC-16 "
             "from para 11.54 (SDRF and SDMF, 2026-27 to 2030-31). Nominal rupees.",
             {"labels": ["FC-11", "FC-12", "FC-13", "FC-14", "FC-15 (2021-26)", "FC-16 (2026-31)"],
              "datasets": [{"label": "₹ crore", "data": [11007, 21333, 33581, 61219, 160153, 204401],
                            "backgroundColor": ["#94A3B8", "#94A3B8", "#94A3B8", "#94A3B8",
                                                "#0EA5E9", "#6366F1"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, title:{display:true,text:'₹ crore'} } } }")],
         [B("Each five-year award has been larger than the last. The Fifteenth Commission's "
            "₹1,60,153 crore for 2021-26 was a 161 per cent increase. The Sixteenth "
            "Commission's ₹2,04,401 crore for 2026-31 is divided 80:20 into ₹1,63,521 crore for "
            "State response funds and ₹40,880 crore for State mitigation funds."),
          B("The figures are nominal. Part of the rise is inflation, and part is that the "
            "Commissions moved from funding relief alone to funding mitigation and "
            "reconstruction as well. The chart does not show what was released or spent."),
          ST([CARD("₹2,04,401 cr", "SDRF and SDMF, 2026-31", "indigo", "FC-16 para 11.54"),
              CARD("₹79,406 cr", "NDRF and NDMF, 2026-31", "cyan", "FC-16 para 11.60")], 2)],
         "a32"),
      compact=True),

    C("FC-16 formula", "How the Sixteenth Finance Commission shares money among States",
      TW([B("Each State's allocation is 70 per cent based on its average past expenditure on "
            "disasters from 2011-12 to 2023-24, leaving out the COVID-19 years 2020-21 and "
            "2021-22, and 30 per cent based on its score on the Disaster Risk Index. The base "
            "year allocation rises by 5 per cent a year."),
          B("The risk index multiplies a hazard score across ten disasters, an exposure score "
            "from projected population, and a vulnerability score from per-capita income. "
            "Expenditure data come from the major head 2245 accounts of each State, adjusted to "
            "remove transfers between funds and releases from the national fund."),
          B("Source: " + FC16 + ", paras 11.49 to 11.54, Box 11.1.", sm=True)],
         [T(["Design choice", "Consequence to watch"],
            [["70 per cent past spending", "States that spent more in the past get more. A State "
              "that under-spent on a slow disaster such as heat or drought is not compensated."],
             ["30 per cent risk index", "Rewards measured hazard, exposure and low income"],
             ["Per-capita income as vulnerability", "Poorer States score higher, but poor "
              "districts inside richer States are invisible"],
             ["Population as exposure", "Crops and infrastructure assumed to track population"],
             ["SDRF balance cap", "Releases withheld if unspent SDRF exceeds the last three "
              "years' allocations (para 11.58)"]]),
          H("amber", "Commentators have argued the new formula under-serves vulnerable hill and "
            "north-eastern States. Treat any claim about winners and losers by checking the "
            "State-wise Annexures 11.3 and 11.4 of the report.")])),

    C("Windows", "What the money can be spent on",
      TW([B("Under the Fifteenth Commission, the response fund had three sub-windows: Response "
            "and Relief (40 per cent), Recovery and Reconstruction (30 per cent) and "
            "Preparedness and Capacity Building (10 per cent), with the remaining 20 per cent "
            "going to the mitigation fund. The Economic Survey 2021-22 summarised the 80:20 "
            "division between response and mitigation for both State and national funds."),
          B("The Sixteenth Commission keeps 80:20 but changes the inside. States get full "
            "flexibility between Response and Relief and Recovery and Reconstruction, and "
            "Preparedness and Capacity Building moves to the mitigation funds, on the reasoning "
            "that preparedness happens before a disaster and response after it. Money may not "
            "be shifted between the response and mitigation funds because they are separate "
            "funds under the Act."),
          B("Sources: " + FC16 + ", paras 11.40, 11.55, 11.56, Summary (ii); Economic Survey "
            "2021-22, Vol. 2, para 2.35.", sm=True)],
         [CH("dhWindowChart", "bar", "NDRF sub-windows under FC-15: allocation and release to 31 July 2025 (₹ crore)",
             "Sixteenth Finance Commission Report, Vol. I, Table 11.1, from MHA",
             {"labels": ["Response and relief", "Recovery and reconstruction",
                         "Preparedness and capacity", "Fire services modernisation",
                         "Erosion resettlement"],
              "datasets": [
                  {"label": "Allocation", "data": [27385, 20539, 6846, 5000, 1000], "backgroundColor": "#94A3B8"},
                  {"label": "Released", "data": [14855, 818.74, 2778.58, 1214.68, 0], "backgroundColor": "#0EA5E9"}]},
             "{ indexAxis:'y', scales:{ x:{ min:0, title:{display:true,text:'₹ crore'} } } }")]),
      compact=True),

    C("Mitigation money", "Mitigation funds were created, and spent slowly",
      TW([CH("dhNdmfChart", "bar", "NDMF earmarked allocations under FC-15 and releases to 31 July 2025 (₹ crore)",
             "Sixteenth Finance Commission Report, Vol. I, Table 11.2, from MHA",
             {"labels": ["Urban flooding, 7 cities", "Erosion mitigation", "Drought-prone, 12 States",
                         "Landslide risk project", "Forest fire project", "Seismic and landslide, 10 States",
                         "Lightning safety", "Community DRR in PRIs", "GLOF programme"],
              "datasets": [
                  {"label": "Allocation", "data": [2500, 1500, 1200, 1000, 818.92, 750, 186.78, 163.32, 150], "backgroundColor": "#94A3B8"},
                  {"label": "Released", "data": [709.54, 0, 350, 4.54, 0, 0, 0, 0, 27.73], "backgroundColor": "#10B981"}]},
             "{ indexAxis:'y', scales:{ x:{ min:0, title:{display:true,text:'₹ crore'} } } }")],
         [B("Of ₹13,693 crore allocated to the National Disaster Mitigation Fund under the "
            "Fifteenth Commission, four original earmarked allocations covered drought-prone States, "
            "seismic and landslide risk, urban flooding in the seven most populous cities, and "
            "erosion. By 31 July 2025, four of the nine earmarked lines in the table had "
            "released any money at all."),
          B("Central releases to States for their mitigation funds were around 80 per cent of "
            "allocation in 2021-22 to 2024-25, against 95 to 100 per cent for response funds. "
            "MHA and NDMA attributed the gap to delays in States constituting the funds and in "
            "issuing guidelines (" + FC16 + ", paras 11.37, 11.38, 11.41, 11.42)."),
          H("cyan", "For a practitioner, this is an opening. Mitigation money exists and is "
            "under-used. District proposals with a clear hazard, a costed project and a "
            "monitoring plan are what the funds were waiting for.")]),
      compact=True),

    C("Where it goes", "What relief spending actually buys",
      TW([B("The MHA's National Disaster Management Information System now records State "
            "expenditure against each disaster, which the Sixteenth Commission called granular "
            "data available for the first time. After removing COVID-19 spending, more than "
            "half of relief expenditure went on agricultural inputs (55.6 per cent), followed by "
            "ex gratia payments to people (23.4 per cent) and infrastructure (13 per cent)."),
          B("Relief spending by States rose from ₹11,070 crore in 2011-12 to ₹25,638 crore in "
            "2023-24, with peaks in the COVID-19 years (" + FC16 + ", paras 11.39, 11.43, 11.44)."),
          H("amber", "Agricultural input subsidy goes to people who farm land, and ex gratia goes "
            "to the families of people who died. Landless workers who lost wages, and families "
            "whose members fell ill, appear in neither line.")],
         [CH("dhReliefChart", "doughnut", "Composition of State relief expenditure, excluding COVID-19 (%)",
             "Sixteenth Finance Commission Report, Vol. I, para 11.44, from NDMIS; other is the "
             "remainder",
             {"labels": ["Agricultural inputs", "Ex gratia to people", "Infrastructure", "Other"],
              "datasets": [{"data": [55.6, 23.4, 13.0, 8.0],
                            "backgroundColor": ["#10B981", "#EF4444", "#0EA5E9", "#94A3B8"]}]},
             "{ scales:{ x:{display:false}, y:{display:false} }, plugins:{ legend:{ position:'right' } } }")]),
      compact=True),

    C("Notified list", "Which disasters the national funds pay for",
      TW([B("SDRF money can be spent on the disasters on the Union Government's notified list: "
            "cyclone, drought, earthquake, fire, flood, tsunami, hailstorm, landslide, avalanche, "
            "cloudburst, pest attack, frost and cold wave. States may spend up to 10 per cent of "
            "SDRF on locally significant disasters they have notified with transparent norms "
            "approved by the State Executive Committee (" + FC16 + ", para 11.65)."),
          B("Eleven States had notified heatwave and sixteen had notified lightning as "
            "State-specific disasters. The Sixteenth Commission recommended adding both to the "
            "national list (paras 11.66, 11.71, 11.73). In August 2026 the Parliamentary "
            "Standing Committee on Home Affairs made the same recommendation (ThePrint, 7 "
            "August 2026). Check the current MHA list before advising a State, because the "
            "notification is a separate step from the recommendation.")],
         [T(["Disaster", "On national list", "Note"],
            [["Flood, cyclone, drought", "Yes", "Most of the spending"],
             ["Earthquake, tsunami", "Yes", ""],
             ["Landslide, cloudburst, avalanche", "Yes", "Added by FC-12"],
             ["Fire", "Yes", "Treated as a disaster since FC-8"],
             ["Hailstorm, frost, cold wave, pest attack", "Yes", ""],
             ["Heatwave", "Recommended by FC-16", "State-specific in 11 States"],
             ["Lightning", "Recommended by FC-16", "State-specific in 16 States; 2,887 of "
              "8,060 deaths from forces of nature in 2022 (NCRB, cited in FC-16)"]]),
          B("The lightning figure is NCRB data as quoted by the Commission, para 11.70.", sm=True)]),
      compact=True),
]

# ===================== SECTION 05: CYCLONES =====================
SLIDES += [
    D("05", "Section Five", "Cyclones and Odisha's record"),

    C("The coast", "Why Odisha is the place to study cyclone preparedness",
      TW([B("The Fani assessment, led by the Government of Odisha with the UN, World Bank and "
            "Asian Development Bank, records that of 1,019 cyclonic disturbances in the Indian "
            "subcontinent in the last century, 890 were on the eastern coast, and 260 of those "
            "made landfall on the Odisha coast. Odisha has ten major river systems that flood "
            "regularly, and is also exposed to flash floods, landslides, earthquakes and tsunami."),
          B("The state is poor and rural. In 2011, 83 per cent of its 4.2 crore people lived in "
            "rural areas, Scheduled Tribes were 22.8 per cent and Scheduled Castes 17.1 per cent "
            "of the population, and poverty, though it fell from about 57 per cent in 2004-05 to "
            "about 33 per cent in 2011-12, remained well above the national average of about 22 "
            "per cent. That combination of high hazard and high vulnerability is what makes its "
            "fall in cyclone deaths instructive.")],
         [ST([CARD("260", "cyclonic disturbances that made landfall in Odisha in a century, of "
                   "890 on the east coast", "cyan", FANI + ", executive summary"),
              CARD("4.2 crore", "population, 83% rural", "indigo", "Same source, citing Census 2011"),
              CARD("39.9%", "of Odisha's people were ST or SC in 2011", "amber", "Same source")], 1),
          B("Source: " + FANI + ".", sm=True)])),

    C("1999 and after", "What Odisha built after the 1999 super cyclone",
      TW([B("The super cyclone of October 1999 killed nearly 10,000 people in Odisha, in the "
            "figure the state's own assessment uses. In its immediate aftermath the government "
            "set up the Odisha State Disaster Management Authority as an autonomous "
            "organisation, before the national Act existed. It also raised the Odisha Disaster "
            "Rapid Action Force, a trained and equipped state rescue force."),
          B("Over the next two decades Odisha built multipurpose cyclone shelters with community "
            "task forces linked to each one, an Early Warning Dissemination System with five "
            "layers of communication and sirens on the coast, District Emergency Operation "
            "Centres in all 30 districts, a GIS cell, a drought monitoring cell and a lightning "
            "detection system. The statutory SDMA under the 2005 Act was constituted in 2010, "
            "with the Chief Minister as chair and the Special Relief Commissioner's office as its "
            "secretariat. Through the national Cyclone Risk Mitigation Project, Odisha "
            "strengthened its last-mile warning system and built and maintained multipurpose "
            "cyclone shelters.")],
         [T(["Component", "What it does in a cyclone"],
            [["OSDMA (after 1999)", "Plans, builds shelters, trains task forces"],
             ["Special Relief Commissioner", "Runs the State Emergency Operation Centre round the "
              "year and coordinates relief"],
             ["ODRAF, 10 units by 2019", "Search, rescue, clearing roads"],
             ["Multipurpose cyclone shelters", "Strong public buildings for people to shelter in "
              "cyclones and floods; 879 were used during Fani"],
             ["Early Warning Dissemination System", "Sirens and messages to the last mile"],
             ["Community task forces", "Trained village volunteers linked to cyclone and flood "
              "shelters in 25 districts"]]),
          B("Source: " + FANI + ", ch. 15 (Disaster Risk Reduction).", sm=True)])),

    C("The record", "Deaths in Odisha's major cyclones since 1999",
      TW([CH("dhOdishaChart", "bar", "Deaths in Odisha, by cyclone (log scale)",
             FANI + ", executive summary and ch. 15. 1999 is the report's figure of nearly "
             "10,000. Hudhud (2014) recorded 0 deaths in Odisha and cannot be shown on a log scale.",
             {"labels": ["Super cyclone 1999", "Phailin 2013", "Titli 2018", "Fani 2019"],
              "datasets": [{"label": "Deaths", "data": [10000, 44, 61, 64],
                            "backgroundColor": ["#EF4444", "#0EA5E9", "#0EA5E9", "#0EA5E9"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ type:'logarithmic', min:10, max:20000, title:{display:true,text:'Deaths (log scale)'} } } }")],
         [B("The fall is about two orders of magnitude, from nearly 10,000 deaths to 44 in "
            "Phailin (2013), none in Hudhud (2014), 61 in Titli (2018) and 64 in Fani (2019). "
            "Fani was an extremely severe cyclonic storm "
            "with sustained winds of 170 to 180 km per hour gusting to 205 km per hour at "
            "landfall."),
          B("The comparison has limits. Cyclones differ in track, strength and surge, so no two "
            "are directly comparable. The state's own assessment draws the conclusion that "
            "evacuation saved lives, and the size of the change is too large to be explained by "
            "differences between storms alone. What the record cannot show is how many people "
            "were saved by each part of the system: the forecast, the warning, the shelters or "
            "the volunteers."),
          H("amber", "The same report states the other half: zero mortality is close, but economic "
            "losses from cyclones are rising. Phailin, Titli and Fani together caused losses of "
            "about USD 5.7 billion.")]),
      compact=True),

    C("Fani, step by step", "Cyclone Fani: eleven days of warning",
      FLOW("25 April 2019: IMD identifies a low pressure area",
           "Storm meanders over the Bay of Bengal for 11 days and its forecast track is revised 9 times",
           "29 April: landfall in Odisha confirmed",
           "30 April, 1 PM: IMD cyclone watch for the Odisha coast",
           "1 May: Collectors told to move vulnerable people, older, disabled people, women and children",
           "3 May, about 8.30 AM: landfall between Satapada and Puri"),
      TW([B("The long lead time helped. Fishing was suspended two days before landfall. Food "
            "grains were placed in fair price shops, take-home rations and eggs reached "
            "pregnant and lactating women and children under three by 1 May, and nearly 600 "
            "pregnant women were moved to maternity waiting homes (Maa Gruhas) and delivery "
            "points. Inspections of anganwadi centres and food stocks were done in advance."),
          B("It was only the second time since 1891 that a cyclone made landfall in Odisha in "
            "May, which shows why a system built for the October cyclone season had to work out "
            "of season.")],
         [B("Sources: " + FANI + ", executive summary and ch. 15. The report gives landfall as "
            "between 0800 and 1000 hours in one place and about 8.30 AM in another, and wind "
            "speeds of 175 to 180 and 170 to 180 km per hour in different chapters.", sm=True),
          H("cyan", "Teaching point. Each step in the flow is a decision by a named office: IMD, "
            "the Special Relief Commissioner, the Collector. A preparedness plan is good when "
            "each of those decisions has a trigger, an owner and a deadline written down before "
            "the season.")]),
      compact=True),

    C("Evacuation", "Moving 15.5 lakh people in about a day",
      ST([CARD("15.5 lakh", "people evacuated to 9,177 shelters, including 879 multipurpose "
               "cyclone and flood shelters", "cyan", FANI),
          CARD("1.8 crore", "SMS alerts, with 274 siren alerts and 1,275 FM radio alerts, before "
               "landfall", "indigo", FANI + ", ch. 15"),
          CARD("25,000", "tourists moved out using 23 special trains and 18 buses", "amber", FANI),
          CARD("~45,000", "volunteers mobilised for relief after landfall", "green", FANI)], 4),
      TW([B("Warnings went out in Odia through the alert siren towers, with voice messages every "
            "hour in coastal areas. A location-based alert system sent SMS to phones in the "
            "projected path. Television, FM and community radio carried preparedness messages. "
            "NGOs and community volunteers went door to door and helped move people. "
            "Collectors were told to give special care to moving older people, physically "
            "challenged people, women and children to shelters, and to secure residential "
            "schools, child care institutions and old age homes.")],
         [B("Polythene sheets for temporary shelter were stocked at district and sub-district "
            "level, food packets were readied for air-dropping, and after landfall more than "
            "6,000 free kitchens served cooked meals with the help of panchayats and self-help "
            "groups. Main roads were cleared within 48 hours. Power took about two weeks to "
            "restore in Puri and Bhubaneswar, with technicians brought from Andhra Pradesh and "
            "West Bengal."),
          B("Source: " + FANI + ", executive summary and ch. 15.", sm=True)]),
      compact=True),

    C("The damage", "Few deaths, very large losses",
      TW([CH("dhFaniChart", "bar", "Cyclone Fani deaths by district",
             FANI + ", Table 0.1, from the State Emergency Operation Centre",
             {"labels": ["Puri", "Khordha", "Cuttack", "Mayurbhanj", "Jajpur", "Kendrapara"],
              "datasets": [{"label": "Deaths", "data": [39, 9, 6, 4, 3, 3], "backgroundColor": "#EF4444"}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, title:{display:true,text:'Deaths'} } } }"),
          B("The other eight affected districts reported no deaths. Total: 64.", sm=True)],
         [T(["Measure", "Fani, 2019"],
            [["People affected", "About 1.65 crore in 18,388 villages, 14 districts"],
             ["Houses damaged", "3.62 lakh (2.96 lakh rural, 66,040 urban), 95% in Puri, Khordha "
              "and Cuttack"],
             ["Trees uprooted or damaged", "21.9 lakh"],
             ["Damage", "₹16,465 crore"],
             ["Loss", "₹7,712 crore"],
             ["Recovery needs", "₹29,315 crore"],
             ["Damage and loss as share of GSDP", "About 5%"]]),
          B("Source: " + FANI + ". The assessment calls its estimates conservative because data "
            "on private losses were very limited.", sm=True),
          H("amber", "The households hit hardest lived in kutcha and semi-pucca houses in rural "
            "areas, urban slums and coastal settlements. Low deaths and high losses fall on the "
            "same people.")]),
      compact=True),

    C("Who was still hurt", "What the Fani assessment found about exclusion",
      TW([P("red", "Relief tied to ration cards",
            "The immediate cash transfer of ₹2,000 and 50 kg of rice was given only to ration "
            "card holders. The assessment records that this excluded many vulnerable families, "
            "including migrants and brick kiln workers who were non-residents and were equally "
            "affected. The 50 kg was the same for every family whatever its size. It recommended "
            "giving cash and grain to all affected people without proof of residency, and "
            "distributing grain by family size."),
          P("red", "Segregation inside shelters",
            "In the days after the cyclone, details emerged of segregated arrangements for food "
            "and use of facilities by a dominant social class, which forced socially vulnerable "
            "groups to shelter in other buildings such as anganwadi centres. The assessment "
            "recommended placing new cyclone shelters closer to Dalit hamlets.")],
         [B("These are the state government's own findings, in a report it led with the UN, the "
            "World Bank and the ADB. They show that a system which saves lives can still "
            "distribute shelter and relief unequally. Women, people with disabilities and other "
            "socially and economically vulnerable groups were, in the report's words, severely "
            "affected despite the evacuation."),
          BL(["Recovery recommendations included housing help for women-led households, cash "
              "for work, advance payment of social security entitlements, and assistive devices "
              "for persons with disabilities.",
              "It asked for the Odisha Relief Code and the SDRF and NDRF norms to be reviewed so "
              "that relief conditions do not exclude affected people.",
              "It recommended including low income communities in the bodies that decide on "
              "reconstruction."], "amber"),
          B("Source: " + FANI + ", executive summary, recommendations.", sm=True)])),

    C("Lessons", "What travels from Odisha, and what does not",
      T(["Element", "Transferable to other coasts", "Needs local adaptation"],
        [["Long-lead forecasting by IMD", "Yes; national service", "Local warning language and "
          "channels"],
         ["Shelters with community task forces", "Yes, if maintained and staffed in normal "
          "times", "Siting: within walking distance of the poorest hamlets, including Dalit "
          "hamlets"],
         ["Zero-casualty political commitment", "Yes", "Requires officers to be accountable for "
          "each death"],
         ["State rescue force", "Yes; now provided for by s. 44A", "Size and location"],
         ["Relief through ration cards", "Common practice", "Must add people who are not on the "
          "card system: migrants, brick kiln and salt pan workers, single women"],
         ["Housing reconstruction", "Build Back Better principles", "Local materials, roof "
          "anchoring, owner-driven rebuilding"]]),
      TW([B("Illustrative synthesis drawn from the Fani assessment. The first five rows are about "
            "saving lives, which Odisha does well. The last two are about protecting livelihoods "
            "and dignity, where the state's own report says the work is unfinished.", sm=True)],
         [H("cyan", "For the wider climate drivers of cyclone intensity, see ImpactMojo's "
            "<a href=\"https://www.impactmojo.in/101-courses/climate-essentials.html\">Climate "
            "Essentials 101</a>.")]),
      compact=True),
]

# ===================== SECTION 06: FLOODS, LANDSLIDES, LIGHTNING =====================
SLIDES += [
    D("06", "Section Six", "Floods, landslides and lightning"),

    C("Floods", "Floods take most of India's disaster money",
      TW([B("Floods accounted for 55.09 per cent of what States spent on notified disasters from "
            "2019-20 to 2023-24, far more than any other hazard (" + FC16 + ", Figure 11.5). "
            "They are frequent, they cover large areas, and most of their cost is in lost crops, "
            "damaged houses and broken roads. Deaths are a smaller part."),
          B("Flood risk has five sources that call for different responses. Riverine floods "
            "build over days and can be forecast from upstream gauges. Flash floods and "
            "cloudbursts in the hills give minutes of warning. Urban floods happen when drains "
            "cannot carry heavy rain, and are made worse by building over lakes and channels. "
            "Coastal floods come with cyclone surge. Glacial lake outburst floods (GLOF) follow "
            "the breach of a glacial lake and give minutes to hours of warning.")],
         [T(["Flood type", "Lead time", "What reduces risk"],
            [["Riverine", "Days", "Gauge-based forecasts, raised plinths, boats, flood shelters, "
              "embankment maintenance"],
             ["Flash flood and cloudburst", "Minutes to hours", "Keeping settlements off stream "
              "beds, warnings from rainfall thresholds"],
             ["Glacial lake outburst (GLOF)", "Minutes to hours", "Monitoring lakes, lowering "
              "levels, downstream sirens"],
             ["Urban", "Hours", "Drains, protected lakes and wetlands, no construction on "
              "floodplains"],
             ["Coastal surge", "Days", "Evacuation, mangroves and shelterbelts, raised shelters"]]),
          B("Illustrative summary of standard practice. The FC-15 national mitigation fund "
            "earmarked ₹2,500 crore for urban flooding in the seven most populous cities and "
            "₹150 crore for a national GLOF programme (" + FC16 + ", Table 11.2).", sm=True)])),

    C("Embankments", "Embankments protect some places and endanger others",
      TW([B("An embankment keeps a river out of the land behind it up to its design height. When "
            "the river exceeds that height, or the embankment breaches, the water arrives "
            "suddenly into places that people had come to believe were safe. Embankments also "
            "stop silt from spreading over the floodplain, so the river bed rises between the "
            "walls over the years and the river sits higher than the land around it."),
          B("This is why flood planners in India distinguish structural measures (embankments, "
            "dams, channels) from non-structural ones (zoning, warning, insurance, raised houses, "
            "flood-tolerant crops). The Sixteenth Commission records "
            "that States have used SDMF for flood protection walls, dam restoration, drains and "
            "groundwater recharge (" + FC16 + ", para 11.38).")],
         [T(["Question to ask about an embankment", "Why"],
            [["Who is behind it, and who is between it and the river?", "People living inside "
              "the embankments are often the poorest and get the worst floods"],
             ["When was it last inspected and repaired?", "Most breaches happen at weak points "
              "that were known"],
             ["Does it have sluices for drainage?", "Without them, rain trapped behind the wall "
              "causes waterlogging"],
             ["Does the warning system assume it will hold?", "A breach needs its own warning and "
              "evacuation plan"]]),
          B("Illustrative. These questions apply to any structural flood defence.", sm=True)])),

    C("Pakistan 2022", "The largest recent flood disaster in South Asia",
      TW([B("Between June and August 2022, torrential rain and a combination of riverine, urban "
            "and flash flooding caused what the Pakistan Post-Disaster Needs Assessment calls an "
            "unprecedented disaster. About 33 million people, one in seven Pakistanis, were "
            "affected and nearly 8 million were displaced. More than 1,700 people died, a third "
            "of them children. By 11 October, 94 districts had been declared calamity hit, and "
            "19 of the country's 25 poorest districts were among them."),
          B("The assessment projected that the floods would raise the national poverty rate by "
            "3.7 to 4.0 percentage points, pushing between 8.4 and 9.1 million people into "
            "poverty. Damage was estimated at USD 14.9 billion, about 4.8 per cent of FY22 GDP, "
            "losses at USD 15.2 billion and recovery needs at USD 16.3 billion.")],
         [CH("dhPakChart", "bar", "Pakistan floods 2022: damage, loss and needs (USD billion)",
             PDNA + ", executive summary",
             {"labels": ["Damage", "Loss", "Recovery and reconstruction needs"],
              "datasets": [{"label": "USD billion", "data": [14.9, 15.2, 16.3],
                            "backgroundColor": ["#EF4444", "#F59E0B", "#0EA5E9"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:20, title:{display:true,text:'USD billion'} } } }"),
          H("amber", "The poverty projection is the number to remember. A flood that kills 1,700 "
            "people can push more than 8 million into poverty. Counting deaths alone misses most "
            "of the harm.")]),
      compact=True),

    C("Landslides", "Landslides: small share of spending, large share of fear in the hills",
      TW([B("Landslides took 2.59 per cent of State disaster spending from 2019-20 to 2023-24, and "
            "cloudbursts 0.32 per cent (" + FC16 + ", Figure 11.5). Those shares are small "
            "because the hill States are small. For the people of the Himalayan and north-eastern "
            "States and the Western Ghats, landslides cut roads for weeks and can bury a "
            "settlement in minutes."),
          B("Landslide risk is raised by rain, by cutting slopes for roads and buildings, by "
            "removing vegetation, and by blocking natural drainage. Most landslide warning in "
            "practice uses rainfall thresholds: when accumulated rain passes a level known to "
            "trigger slides on a slope, people below are moved.")],
         [T(["National mitigation line (FC-15 NDMF)", "Allocation, ₹ crore", "Released to 31 July 2025"],
            [["Managing seismic and landslide risks in ten States", "750", "Nil"],
             ["Landslide Risk Reduction and Mitigation Project", "1,000", "4.54"],
             ["National GLOF Risk Mitigation Programme", "150", "27.73"]]),
          B("Source: " + FC16 + ", Table 11.2.", sm=True),
          H("cyan", "The Sixteenth Commission's ten-hazard risk index scores landslide hazard from "
            "Geological Survey of India data, and NEH States contribute only 10 per cent to State "
            "funds (paras 11.49, 11.61).")])),

    C("Lightning", "Lightning kills more Indians than any other force of nature",
      TW([B("NCRB data, as quoted by the Sixteenth Finance Commission, show lightning as the "
            "leading cause of death from forces of nature in India. In 2022 it accounted for "
            "2,887 of 8,060 deaths, or 35.8 per cent. The Annual Lightning Report prepared with "
            "IMD for 2020-21 recorded about 18.5 million lightning strikes, a 34 per cent rise "
            "on the previous year."),
          B("The Commission notes who dies. Agricultural labourers working in open fields, with no "
            "shelter and near water, face the highest risk, and people living in mud houses are "
            "more exposed to ground strikes. Sixteen States had notified lightning as a "
            "State-specific disaster when the Commission reported, and it recommended adding "
            "lightning to the national list (" + FC16 + ", paras 11.69 to 11.73).")],
         [ST([CARD("2,887", "lightning deaths in 2022", "red", "NCRB, cited in FC-16 para 11.70"),
              CARD("35.8%", "of all deaths from forces of nature in 2022", "amber", "Same"),
              CARD("16", "States had notified lightning as a State-specific disaster", "cyan",
                   "FC-16 para 11.71")], 1),
          H("green", "Lightning is the clearest case of a hazard where vulnerability is about work. "
            "Warnings by SMS reach phone owners. Labourers in a field need a siren, a shelter "
            "nearby and an employer who lets them stop.")])),

    C("Measuring floods", "What a flood assessment should count",
      T(["Measure", "Common source", "What it misses"],
        [["Deaths", "Ex gratia records", "Missing persons; deaths from disease after the flood"],
         ["Houses damaged", "Revenue surveys", "Rented houses, informal settlements without "
          "title"],
         ["Crop area affected", "Agriculture department", "Tenant and sharecropper losses when "
          "relief goes to owners"],
         ["Livestock lost", "Animal husbandry department", "Animals of landless households kept "
          "without records"],
         ["Days of work lost", "Rarely measured", "The main loss for daily wage workers"],
         ["School days lost", "Education department", "Schools used as shelters for weeks"],
         ["Poverty impact", "Post-disaster needs assessment", "Usually estimated once and "
          "never followed up"]]),
      TW([B("Illustrative. The Pakistan assessment's poverty estimate and the Fani assessment's "
            "chapter on employment and livelihoods are examples of measuring beyond deaths and "
            "houses.", sm=True)],
         [H("amber", "Relief follows what is counted. Agricultural inputs were 55.6 per cent of "
            "State relief spending because crop loss is counted carefully (" + FC16 +
            ", para 11.44). Lost wages are rarely counted.")]),
      compact=True),

    C("For practitioners", "Working on floods, landslides and lightning in a district",
      TW([BL(["Get the district hazard map and the list of villages flooded in each of the last "
              "ten years. The pattern usually repeats.",
              "Find out where the embankments are, when they were last repaired, and which "
              "villages sit between them and the river.",
              "For hill districts, ask whether the district has rainfall thresholds for "
              "landslide alerts and who acts on them.",
              "For lightning, ask whether the warning reaches people working in fields, and "
              "whether schools and panchayat buildings have lightning conductors.",
              "Check whether the district has proposed projects to the State mitigation fund. "
              "Under-used mitigation money is common."], "cyan")],
         [B("The same five questions work for a programme officer in an NGO and for a block "
            "development officer. They turn a general concern about floods into a short list "
            "of records to ask for and people to visit."),
          H("green", "ImpactMojo's <a href=\"https://www.impactmojo.in/Labs/climate-adaptation-lab.html\">"
            "Climate Risk and Adaptation Studio</a> lets you practise building a local risk "
            "profile and adaptation plan.")])),
]

# ===================== SECTION 07: DROUGHT =====================
SLIDES += [
    D("07", "Section Seven", "Drought"),

    C("Kinds of drought", "Drought is a slow disaster with several definitions",
      TW([T(["Kind", "What it means", "First sign"],
            [["Meteorological", "Rainfall well below normal for a place and season",
              "Rainfall deficit at IMD stations"],
             ["Agricultural", "Soil moisture too low for crops at the stage they need it",
              "Delayed sowing, wilting, low vegetation index"],
             ["Hydrological", "Reservoirs, rivers and groundwater fall below normal",
              "Falling well levels, dry tanks"],
             ["Socio-economic", "Water and food fall short of what people need, so income, "
              "nutrition and work suffer", "Distress sales of livestock, migration, debt"]]),
          B("These are standard textbook categories, used here for teaching.", sm=True)],
         [B("The categories matter because they arrive in sequence. Rain fails first. Soil dries "
            "and crops fail weeks later. Wells and tanks fail months later. People migrate, sell "
            "animals and borrow throughout. A declaration based only on rainfall comes early "
            "and may miss a district where rain was near normal but badly timed. A declaration "
            "that waits for crop-cutting results comes late, after people have already sold "
            "their assets."),
          H("amber", "Drought harms people mainly through lost work and income, which is why the "
            "response that matters most is often employment and food over months. A single relief "
            "payment does not replace lost work.")])),

    C("The money", "How drought is financed",
      TW([B("Drought is on the national list of notified disasters, and took 17.26 per cent of "
            "State disaster expenditure from 2019-20 to 2023-24, second only to floods (" + FC16 +
            ", para 11.65, Figure 11.5). Relief spending as a whole is dominated by agricultural "
            "input subsidy, at 55.6 per cent after removing COVID-19 spending, and drought is "
            "where most of that subsidy is paid."),
          B("The Fifteenth Commission earmarked ₹1,200 crore in the national mitigation fund for "
            "catalytic assistance to the twelve most drought-prone States. By 31 July 2025, ₹350 "
            "crore had been released (" + FC16 + ", Table 11.2). For agricultural disasters, "
            "the Inter-Ministerial Group that scrutinises a State's request for central "
            "assistance is chaired by the Secretary, Agriculture. For other disasters "
            "it is the Union Home Secretary (para 11.11).")],
         [ST([CARD("17.26%", "of State disaster spending went on drought, 2019-24", "amber",
                   "FC-16 Figure 11.5"),
              CARD("₹1,200 cr", "FC-15 earmark for 12 drought-prone States", "cyan",
                   "FC-16 Table 11.2"),
              CARD("₹350 cr", "released by 31 July 2025", "red", "FC-16 Table 11.2")], 1),
          H("cyan", "Input subsidy reaches cultivators. Agricultural labourers, who lose the most "
            "work in a drought, need a different instrument.")])),

    C("Work in a drought", "Rural employment law in a drought, after July 2026",
      TW([B("Rural employment guarantees have been India's main drought response for landless "
            "households. The Mahatma Gandhi National Rural Employment Guarantee Act 2005 was "
            "repealed from 1 July 2026, when the Viksit Bharat Guarantee for Rozgar and "
            "Ajeevika Mission (Gramin) Act 2025 came into force, by Ministry of Rural "
            "Development notification of 11 May 2026 (SCC Online, 12 May 2026)."),
          B("The new Act guarantees not less than 125 days of employment a year to every rural "
            "household whose adult members volunteer for unskilled manual work (s. 5(1)). It "
            "also requires States to notify sixty days a year covering peak sowing and "
            "harvesting, during which no work is undertaken (s. 6). In a drought year the "
            "notified peak season may produce little farm work, which is something to watch.")],
         [T(["Provision of " + VBG, "What it allows in a disaster"],
            [["s. 7(1)", "A State may recommend special operational relaxations during natural "
              "calamities or extraordinary circumstances"],
             ["s. 7(2)", "The Centre may allow temporary expansion of permissible works, relaxed "
              "documentation, or more wage employment"],
             ["s. 5(4)", "Work beyond the guaranteed days may be provided within economic "
              "capacity"],
             ["Schedule I, Category IV", "Works to mitigate extreme weather: shelters, "
              "embankments, ponds for flood management, shelterbelts, forest fire management"]]),
          B("Source: " + VBG + ", as published in India Code.", sm=True)])),

    C("Declaring drought", "What a declaration decides, and who is left out",
      TW([B("A drought declaration by a State government opens access to relief norms, central "
            "assistance and scheme relaxations. The timing and the unit of declaration, usually "
            "a block or tehsil, decide who gets help. A village in a block that is not declared "
            "gets nothing, however badly its own crops failed."),
          B("Declarations rely on a mix of rainfall, crop sowing, vegetation, soil moisture and "
            "water indicators, followed by field verification. The Union Agriculture Ministry "
            "publishes the procedure that States are expected to follow. Practitioners should "
            "read the current version of that procedure before advising a State, because its "
            "indicators and thresholds have been revised over time.")],
         [T(["Design question", "Who loses if it is answered badly"],
            [["How small is the unit declared?", "Villages in a block whose average looks "
              "normal"],
             ["How early is the declaration?", "Households that sell animals and borrow before "
              "relief arrives"],
             ["Is relief tied to land records?", "Tenants, sharecroppers and women farmers "
              "without title"],
             ["Is employment expanded at once?", "Landless labourers, who lose work first"],
             ["Are migrants counted?", "Families whose members left to find work and are "
              "absent from surveys"]]),
          B("Illustrative. The specific indicators and thresholds of India's drought "
            "declaration procedure are not set out here because the current text could not be "
            "verified for this course.", sm=True)])),

    C("Drought and people", "What a drought response should measure",
      TW([BL(["Days of work demanded and provided under the rural employment guarantee, by "
              "month, compared with the same months in a normal year.",
              "Prices of fodder, and the number and price of livestock sold at local markets.",
              "Seasonal migration from the district, including whole families.",
              "Children's attendance at school and anganwadi, and meals served.",
              "Debt taken for consumption, from microfinance and moneylenders.",
              "Drinking water supplied by tanker, by village, and how long the queue is."], "cyan")],
         [B("Each of these indicators moves before crop-cutting results are in. Taken together "
            "they show whether a drought response is reaching people, which input subsidy "
            "payments alone cannot."),
          H("amber", "Heat makes drought worse and the two now overlap in the same months in "
            "much of India. Section 08 turns to heat itself."),
          B("Illustrative monitoring list.", sm=True)])),
]

# ===================== SECTION 08: HEAT =====================
AZHAR = ("Azhar et al., Heat-related mortality in India: excess all-cause mortality associated "
         "with the 2010 Ahmedabad heat wave, PLoS One 9(3):e91831, 2014")
KNOW = ("Knowlton et al., Development and implementation of South Asia's first heat-health "
        "action plan in Ahmedabad, Int J Environ Res Public Health 11(4):3473-92, 2014")
HESS = ("Hess et al., Building resilience to climate change: pilot evaluation of the impact of "
        "India's first heat action plan on all-cause mortality, J Environ Public Health 2018:7973519")

SLIDES += [
    D("08", "Section Eight", "Heat"),

    C("Definition", "When IMD declares a heatwave",
      TW([T(["Criterion", "Heat wave", "Severe heat wave"],
            [["Basic condition", "Maximum temperature at least 40°C in the plains, 30°C in hilly "
              "regions", "Same"],
             ["Departure from normal", "4.5°C to 6.4°C above normal", "More than 6.4°C above "
              "normal"],
             ["Actual temperature (plains only)", "45°C or more", "47°C or more"],
             ["Coastal stations", "Departure of 4.5°C or more, with actual maximum of 37°C or "
              "more", ""],
             ["Declaration rule", "Criteria met at 2 or more stations in a meteorological "
              "sub-division for 2 consecutive days; declared on the second day", ""]]),
          B("Source: " + IMD + ".", sm=True)],
         [B("The IMD definition is based on dry air temperature. It says nothing about humidity, "
            "and it requires the heat to be widespread enough to be met at two stations for two "
            "days. That is right for a weather service. It is a blunt tool for health, because "
            "people die at lower temperatures where it is humid, where nights stay hot, and "
            "where people are not used to the heat."),
          TERM("Warm night (IMD)", "Considered only when the maximum stays at 40°C or more. A warm "
               "night is a minimum temperature 4.5°C to 6.4°C above normal. A very warm night is "
               "more than 6.4°C above normal."),
          H("amber", "Many city heat action plans set their own lower, local thresholds based on "
            "when deaths rise in that city. Pillai and Dalal found only ten of 37 plans did so "
            "(" + CPR + ").")])),

    C("Heat in India", "Hotter days, and nights that do not cool",
      TW([B("The Sixteenth Finance Commission records that the frequency and intensity of hot "
            "days in India increased significantly over 1981 to 2022, with major heatwaves in "
            "2013, 2016, 2019, 2022 and 2024, and a marked rise in very warm nights in the last "
            "decade. It explains why nights matter: warm nights stop the body recovering from "
            "daytime heat, which raises the risk of heat illness such as heatstroke "
            "(" + FC16 + ", paras 11.66, 11.67)."),
          B("CPR's review of heat action plans adds that three-day runs of concurrent hot days "
            "and hot nights increased significantly over 1951 to 2016, and are projected to "
            "increase two to four times by 2050 under moderate and high emission scenarios "
            "(" + CPR + ", citing published projections).")],
         [T(["Who is most at risk from heat", "Why"],
            [["Older people", "Weaker cooling response; often live alone; chronic illness"],
             ["Infants and young children", "Dehydrate quickly; depend on others"],
             ["Pregnant women", "Higher heat load; risks to the pregnancy"],
             ["Outdoor workers", "Exposed during the hottest hours; paid by the day or the piece"],
             ["People with chronic disease", "Heart, kidney and lung disease worsen in heat"],
             ["People in poor housing", "Tin roofs and no ventilation keep houses hot at night"],
             ["Homeless people", "No shade, no water, no place to rest"]]),
          B("Illustrative summary of standard public health guidance. CPR found that most heat "
            "action plans list groups like these drawn from NDMA's heat guidelines, without a "
            "local vulnerability assessment.", sm=True)])),

    C("Humid heat", "Wet-bulb temperature, and why humidity changes the danger",
      TW([TERM("Wet-bulb temperature",
               "The lowest temperature air can reach by evaporating water into it. It combines "
               "heat and humidity. The body cools itself mainly by evaporating sweat, so as the "
               "wet-bulb temperature approaches skin temperature, sweating stops working."),
          B("Sherwood and Huber argued in 2010 that a wet-bulb temperature above 35°C for an "
            "extended period would cause hyperthermia in humans, because metabolic heat could no "
            "longer be lost, and noted that observed peak wet-bulb temperatures then did not "
            "exceed 31°C (PNAS 107(21):9552, 2010)."),
          B("Vecellio and colleagues tested the idea on young, healthy volunteers in a chamber. "
            "In humid conditions the critical wet-bulb temperature at which heat stress became "
            "uncompensable averaged 30.55°C, well below 35°C, and no subject reached 35°C. In "
            "hot, dry conditions it was lower still (J Appl Physiol 132(2):340, 2022).")],
         [ST([CARD("35°C", "theoretical wet-bulb limit for survival, extended exposure", "red",
                   "Sherwood and Huber 2010"),
              CARD("30.55°C", "measured critical limit, young healthy adults, humid heat", "amber",
                   "Vecellio et al. 2022")], 2),
          H("cyan", "For practice, the lesson is that a coastal city at 37°C with high humidity can "
            "be more dangerous than an inland city at 44°C and dry air. A heat plan that uses dry "
            "temperature alone will warn the wrong city on the wrong day."),
          B("The volunteers were young and healthy. Older people, people with illness and people "
            "doing heavy work reach their limits sooner.", sm=True)])),

    C("Ahmedabad 2010", "The heatwave that started South Asia's first heat action plan",
      TW([B("In May 2010 Ahmedabad's temperature reached 46.8°C. Azhar and colleagues compared "
            "all-cause deaths in the city for 1 to 31 May 2010 with the average of the same "
            "period in 2009 and 2011. There were 4,462 deaths in May 2010 against a reference of "
            "3,118, an excess of 1,344 deaths, or 43.1 per cent. During the most intense week, "
            "19 to 25 May, mortality rate ratios were 1.76 to 2.12 depending on the reference "
            "period."),
          B("The excess deaths were not recorded as heat deaths. They appeared in the city's "
            "death registrations as deaths from all causes, which is why the method matters. "
            "Counting deaths certified as heatstroke would have found a small fraction of the "
            "1,344."),
          B("Source: " + AZHAR + ".", sm=True)],
         [CH("dhAhdChart", "bar", "All-cause deaths, Ahmedabad, 1 to 31 May",
             AZHAR + ". Reference is the mean of May 2009 and May 2011.",
             {"labels": ["Reference (2009 and 2011 mean)", "May 2010"],
              "datasets": [{"label": "Deaths", "data": [3118, 4462],
                            "backgroundColor": ["#94A3B8", "#EF4444"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:5000, title:{display:true,text:'All-cause deaths'} } } }")]),
      compact=True),

    C("The plan", "What Ahmedabad's 2013 heat action plan contains",
      TW([B("A coalition of the Ahmedabad Municipal Corporation, the Indian Institute of Public "
            "Health Gandhinagar, the Natural Resources Defense Council and other partners built "
            "the plan from a literature review, analysis of local temperature and mortality "
            "data, surveys of heat-vulnerable people, focus groups with health workers, and "
            "expert advice. The pilot was implemented in 2013."),
          B("A 7-day probabilistic weather forecast triggers the plan before dangerous heat. "
            "Findings were turned into policy briefs for government agencies, health "
            "professionals, outdoor workers and slum communities. Outreach used training "
            "workshops, hoardings, pamphlets and print advertisements (" + KNOW + ")."),
          B("The city's 2017 plan added a cool roofs initiative for slum residents and the urban "
            "poor, aiming to convert at least 500 slum roofs and to raise the reflectivity of "
            "government buildings and schools (ILO 2019, ch. 2).")],
         [FLOW("Forecast shows dangerous heat",
               "Alert issued to departments and public",
               "Hospitals, ambulances and water points prepare",
               "Messages reach outdoor workers and slums",
               "After the season: review deaths and update thresholds"),
          T(["Component", "Example"],
            [["Early warning", "Colour-coded alerts from a 7-day forecast"],
             ["Health system", "Training staff to recognise and treat heat illness"],
             ["Public outreach", "Messages on water, shade and timing of work"],
             ["Vulnerable groups", "Outdoor workers, slum residents"],
             ["Long-term", "Cool roofs, shade, urban design"]]),
          B("Illustrative structure based on the published description.", sm=True)]),
      compact=True),

    C("Did it work", "Evaluating the Ahmedabad plan",
      TW([B("Hess and colleagues compared summer all-cause mortality in 2014-2015, after the "
            "plan, with a 2007-2010 baseline. Before the plan, the mortality rate ratio at 47°C "
            "was 2.34 (95% CI 1.98 to 2.76). After it, the ratio at 47°C was 1.25 (1.02 to "
            "1.53). They estimated 1,190 deaths avoided a year on average (95% CI 162 to 2,218)."),
          B("Read the uncertainty as carefully as the headline. The confidence interval on "
            "avoided deaths runs from 162 to 2,218. The incidence rate ratios for days above "
            "40°C and above 45°C were 0.95 (0.73 to 1.22) and 0.73 (0.29 to 1.81), both "
            "consistent with no change. The study is a before and after comparison in one city, "
            "so other changes over the same years, such as air conditioning, could account for "
            "part of the fall. The authors call it a pilot evaluation."),
          B("Source: " + HESS + ".", sm=True)],
         [CH("dhHessChart", "bar", "Mortality rate ratio at 47°C, Ahmedabad, before and after the plan",
             HESS + ". Bars show point estimates; 95% confidence limits are given in the text.",
             {"labels": ["Before plan (2007-2010)", "After plan (2014-2015)"],
              "datasets": [{"label": "Rate ratio", "data": [2.34, 1.25],
                            "backgroundColor": ["#EF4444", "#0EA5E9"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:3, title:{display:true,text:'Mortality rate ratio'} } } }"),
          H("amber", "A 2025 study of Ahmedabad data from 2002 to 2018 also found reduced immediate "
            "heat mortality risk after the plan, but not at longer lags or under moderate heat "
            "(Sharma et al., Int J Biometeorol 69(9):2225, 2025).")]),
      compact=True),

    C("Plans across India", "What a review of 37 heat action plans found",
      TW([CH("dhCprChart", "bar", "Heat action plans meeting each test (of 37 reviewed)",
             CPR + ". Plans published 2016-2022 at city (9), district (13) and State (15) level, "
             "across 18 States.",
             {"labels": ["Local temperature thresholds", "Vulnerability assessment",
                         "Discuss funding sources", "Hierarchical accountability",
                         "State their legal authority"],
              "datasets": [{"label": "Plans", "data": [10, 2, 11, 12, 0],
                            "backgroundColor": "#F59E0B"}]},
             "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:37, title:{display:true,text:'Number of plans (of 37)'} } } }")],
         [B("Pillai and Dalal reviewed 37 heat action plans, a subset of what they describe as "
            "the purported 100 or more plans in India, and found that plan-making had spread "
            "fast after Ahmedabad and after NDMA's heat guidelines of 2016. Most follow a "
            "template. Their four main findings were that plans rarely set local thresholds or "
            "account for humidity and hot nights, that nearly all are poor at identifying and "
            "targeting vulnerable groups, that they are underfunded, and that none states the "
            "legal authority under which it operates."),
          B("Their recommendations include a national repository of plans at NDMA, an expert "
            "committee on notifying heatwaves as disasters, independent evaluation, and linking "
            "each action to an existing law or scheme so that someone is obliged and funded to "
            "carry it out (" + CPR + ")."),
          H("cyan", "The MHA told the Sixteenth Commission that existing rules already allow "
            "State and national mitigation funds to be spent on heatwave and lightning, which are "
            "non-notified disasters (" + FC16 + ", para 11.32).")]),
      compact=True),

    C("Counting the dead", "Why recorded heat deaths are a small part of the true toll",
      TW([B("The Sixteenth Finance Commission quotes NCRB data showing 3,798 deaths from heat or "
            "sunstroke in the whole of India from 2018 to 2022, about 760 a year (" + FC16 +
            ", para 11.67). In one month of 2010, in one city, Azhar and colleagues counted "
            "1,344 excess deaths from all causes during a heatwave (" + AZHAR + ")."),
          B("The two numbers measure different things, and the gap between them is the point. "
            "NCRB counts deaths that police record as caused by heat or sunstroke. Most heat "
            "deaths are certified as heart attacks, strokes, kidney failure or simply old age, "
            "often at home, and never reach that category. Excess mortality, comparing all "
            "deaths in a hot period with deaths expected in a normal one, captures them without "
            "needing a cause on the certificate.")],
         [T(["Method", "Counts", "Strength", "Weakness"],
            [["Certified heatstroke deaths", "Deaths with heat recorded as cause", "Simple, "
              "available fast", "Large undercount"],
             ["Accidental deaths (NCRB)", "Police-recorded heat and sunstroke", "National series",
              "Misses home deaths and other causes"],
             ["Excess all-cause mortality", "Deaths above expected in a hot period", "Captures "
              "uncertified heat deaths", "Needs complete, timely death registration"],
             ["Temperature-mortality models", "Deaths attributable to heat over a season",
              "Separates heat from other causes", "Needs years of daily data"]]),
          H("red", "When heat deaths are undercounted, heat looks like a small disaster, gets "
            "less money, and the Sendai mortality target looks met when it is not. An Indian "
            "city's civil registration data is the most useful heat dataset it owns.")]),
      compact=True),

    C("Outdoor work", "Heat stress takes working hours away",
      TW([CH("dhIloChart", "bar", "Working hours lost to heat stress, % of total, 1995 and 2030 (projected)",
             ILO + ". Work in agriculture and construction assumed in the shade; RCP2.6 scenario.",
             {"labels": ["India", "Bangladesh", "Pakistan", "Sri Lanka", "Nepal", "Southern Asia"],
              "datasets": [
                  {"label": "1995", "data": [4.31, 4.24, 4.19, 1.83, 1.17, 4.02], "backgroundColor": "#94A3B8"},
                  {"label": "2030", "data": [5.80, 4.84, 5.54, 2.67, 2.05, 5.29], "backgroundColor": "#EF4444"}]},
             "{ scales:{ y:{ min:0, max:7, title:{display:true,text:'% of working hours lost'} } } }")],
         [B("The ILO estimated that India lost 4.3 per cent of working hours to heat stress in "
            "1995 and projected a loss of 5.8 per cent in 2030, the equivalent of 34 million "
            "full-time jobs. Southern Asia as a whole is projected to lose 5.3 per cent of "
            "working hours in 2030, the equivalent of 43 million jobs. Worldwide, the ILO "
            "projected 2.2 per cent of working hours lost in 2030, equivalent to 80 million "
            "full-time jobs."),
          B("These figures assume agricultural and construction work is done in the shade. "
            "Work in the sun adds roughly 2 to 3°C to the heat stress index, so the real losses "
            "for people working in open fields and on building sites are larger (" + ILO + ")."),
          H("amber", "Lost hours are lost wages for people paid by the day or the piece. Heat is "
            "an income shock before it is a health emergency.")]),
      compact=True),

    C("Who works in heat", "Sectors, kilns and the law",
      TW([CH("dhIloSector", "bar", "India: working hours lost to heat stress by sector, 2030 projection (%)",
             ILO + ".",
             {"labels": ["Agriculture", "Construction", "Manufacturing", "Services"],
              "datasets": [{"label": "% of hours lost", "data": [9.04, 9.04, 5.29, 1.48],
                            "backgroundColor": ["#10B981", "#F59E0B", "#6366F1", "#0EA5E9"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:10, title:{display:true,text:'% of working hours'} } } }")],
         [B("The ILO expects most of India's loss in agriculture, with a growing share in "
            "construction, where heat stress affects both men and women. Its box on brick kilns "
            "describes workers, most of them migrants from poor villages and including young "
            "children, exposed to air temperatures of 40 to 45°C and to radiant heat from the "
            "kilns, with little or no cooling and short breaks only when exhausted. A study of "
            "women brick workers in West Bengal it cites found roughly a 2 per cent loss in "
            "productivity for each 1°C rise."),
          B("The ILO notes that the Factories Act 1948 and the Building and Other Construction "
            "Workers Act 1996 were the statutes relevant to such work, and that neither made "
            "clear how the occupational safety and health of brick workers was to be "
            "protected (" + ILO + ", Box 6.1). Labour law has changed since the report, so "
            "check which occupational safety law and rules now apply in your State."),
          H("cyan", "Practical measures that heat plans recommend for outdoor work include shifting "
            "hours away from the afternoon, water and shade at the work site, rest breaks, and "
            "protecting the wages of workers who stop in extreme heat. Illustrative.")]),
      compact=True),

    C("For practitioners", "Building a heat plan that reaches people",
      T(["Step", "What to do", "Evidence it was done"],
        [["Set local thresholds", "Analyse past daily deaths against temperature, humidity and "
          "night temperature in your city or district", "A threshold table with its data source"],
         ["Map vulnerability", "Find where older people living alone, outdoor workers, slums "
          "with tin roofs and homeless people are", "Ward or village list, updated each year"],
         ["Fix the trigger", "Agree which forecast, at what lead time, triggers which action by "
          "which department", "Signed standard operating procedures"],
         ["Prepare health services", "Train staff, stock oral rehydration salts and cooling, "
          "record heat cases daily", "Daily heat illness reports in season"],
         ["Protect workers", "Agree work hours, water, shade and wage protection with employers "
          "and labour department", "Notices issued; inspections done"],
         ["Fund and give legal basis", "Link each action to a scheme budget and a legal "
          "authority", "Budget lines; orders under the DM Act or other law"],
         ["Count deaths properly", "Track excess all-cause deaths during heat periods",
          "Monthly civil registration analysis"]]),
      TW([B("Illustrative checklist synthesised from the Ahmedabad plan and the CPR review. "
            "Each row answers one of the weaknesses CPR found.", sm=True)],
         [H("green", "For heat and work, see ImpactMojo's "
            "<a href=\"https://www.impactmojo.in/101-courses/work-labour-livelihoods.html\">Work, "
            "Labour and Livelihoods 101</a>.")]),
      compact=True),
]

# ===================== SECTION 09: EARLY WARNING AND ANTICIPATORY ACTION =====================
SLIDES += [
    D("09", "Section Nine", "Early warning and anticipatory action"),

    C("The chain", "A warning works only if every link holds",
      FLOW("Forecast: the hazard is detected and its path or intensity predicted",
           "Warning: an authority decides what it means and who must act",
           "Dissemination: the message reaches people by channels they use",
           "Understanding: people trust it and know what to do",
           "Action: people and officials act in time, with the means to act"),
      TW([B("Sendai target (g) asks countries to substantially increase the availability of and "
            "access to multi-hazard early warning systems and disaster risk information by 2030 "
            "(" + SENDAI + ", para 18). The phrase access to is important. A forecast that is "
            "accurate but reaches only people with smartphones, in English, is not an early "
            "warning system for most of rural South Asia."),
          B("Fani shows the full chain working. IMD tracked the storm for eleven days. The State "
            "turned the forecast into instructions to Collectors. Messages went out in Odia by "
            "SMS, sirens, FM and community radio. Volunteers and NGOs went door to door. "
            "Shelters, transport and food were ready, so people had somewhere to go "
            "(" + FANI + ").")],
         [T(["Link", "Typical failure"],
            [["Forecast", "Too coarse for a district; no humidity in heat forecasts"],
             ["Warning", "No one has the authority or the trigger to act"],
             ["Dissemination", "Messages in the wrong language or channel"],
             ["Understanding", "People do not trust it after past false alarms"],
             ["Action", "No shelter nearby, no transport, or leaving costs a day's wage"]]),
          B("Illustrative.", sm=True)]),
      compact=True),

    C("The last mile", "Who does not receive the warning",
      TW([B("Warnings travel along the lines of ordinary inequality. Phones are more often owned "
            "and controlled by men. People who are deaf or blind need warnings in forms they can "
            "receive. Migrant workers may not speak the local language and are often not "
            "registered in the village. People working in fields hear sirens but not SMS. Older "
            "people living alone may hear the warning and have no one to help them move."),
          B("Odisha's Collectors were told on 1 May 2019 to identify all vulnerable people and "
            "move them, with special care for older people, physically challenged people, women "
            "and children (" + FANI + ", ch. 15). An instruction like that works only if a list "
            "of those people, by village, already exists."),
          B("Illustrative analysis.", sm=True)],
         [T(["Group", "Channel that reaches them"],
            [["Fisherfolk at sea", "Radio, boat-to-boat, harbour announcements"],
             ["Farm labourers in fields", "Sirens, loudspeakers, employer and supervisor"],
             ["Women without phones", "Self-help groups, anganwadi workers, door-to-door"],
             ["Deaf and hard of hearing people", "Text, visual signals, a named neighbour"],
             ["Blind and low-vision people", "Voice calls, a named neighbour"],
             ["Migrant workers", "Employers, worksite announcements, their own language"],
             ["Older people living alone", "A named volunteer who checks on them"]]),
          H("cyan", "The Sendai Framework asks that older persons be included in designing early "
            "warning (para 36(a)(iv)). The simplest form is a register of who needs a visit.")])),

    C("Anticipatory action", "Acting on the forecast, before the disaster",
      TW([TERM("Anticipatory action",
               "Pre-agreed actions, with money set aside in advance, that are released when a "
               "forecast crosses a threshold and before the hazard strikes, to reduce its impact. "
               "Sendai's fourth priority asks countries to take action in anticipation of "
               "events (" + SENDAI + ")."),
          B("Most disaster finance waits for damage to be assessed. Anticipatory action reverses "
            "the order: decide in advance what will be done and who pays, then act on the "
            "forecast. The cost is that sometimes the hazard is weaker than forecast and the "
            "money is spent on a disaster that did not happen.")],
         [T(["Anticipatory step taken before Fani", "What it protected"],
            [["Fishing suspended two days before landfall", "Lives at sea"],
             ["Food grains placed in fair price shops", "Food access when roads closed"],
             ["Take-home rations and eggs to pregnant and lactating women and children under "
              "three by 1 May", "Nutrition through the disruption"],
             ["About 600 pregnant women moved to Maa Gruhas and delivery points",
              "Safe births during the storm"],
             ["Polythene sheets stocked at district and sub-district level", "Shelter for "
              "those whose houses fell"]]),
          B("Source: " + FANI + ". The Ahmedabad heat plan works the same way, triggered by a "
            "7-day forecast (" + KNOW + ").", sm=True)])),

    C("Designing triggers", "A trigger is a forecast, a threshold and an action",
      T(["Hazard", "Forecast used", "Lead time", "Pre-agreed action", "Cost if forecast is wrong"],
        [["Cyclone", "IMD track and intensity", "2 to 5 days", "Suspend fishing; open shelters; "
          "move people", "Lost fishing days; shelter costs"],
         ["Riverine flood", "Upstream gauge levels", "1 to 4 days", "Cash to households in the "
          "flood path; move livestock", "Cash paid to households not flooded"],
         ["Heatwave", "District temperature and humidity forecast", "3 to 7 days", "Shift work "
          "hours; open cooling spaces; alert hospitals", "Lost work hours on a normal day"],
         ["Landslide", "Accumulated rainfall threshold", "Hours to a day", "Evacuate slope-foot "
          "houses; close roads", "Disruption, loss of trust"],
         ["Drought", "Seasonal rainfall and vegetation", "Weeks to months", "Expand public "
          "works; fodder; school meals in vacation", "Spending in a year that recovers"]]),
      TW([B("Illustrative. Lead times are typical orders of magnitude and vary by event.", sm=True)],
         [H("amber", "Write down the cost of acting in vain before the season. A system with no "
            "false alarms is probably acting too late.")]),
      compact=True),

    C("Trust", "False alarms, missed alarms and trust",
      TW([B("Every warning system trades two errors. A low threshold gives more false alarms: "
            "people leave homes, lose wages and come back to find nothing happened. A high "
            "threshold gives more missed events: people stay home and the hazard arrives. After "
            "a few false alarms people stop leaving, so the second error starts to follow from "
            "the first."),
          B("Fani's forecast track was revised nine times while the storm meandered over the "
            "Bay of Bengal, and Odisha was expected to be spared in the early days (" + FANI +
            ", ch. 15). The response was still timely because evacuation began only once "
            "landfall in Odisha was confirmed, with enough lead time left to move people.")],
         [BL(["Explain uncertainty plainly: say how likely the event is and when it will be "
              "known for sure.",
              "Compensate people for the cost of acting: food in shelters, wage protection for "
              "workers who stop in heat.",
              "After every event, publish what was forecast, what happened and what was done.",
              "Keep warning language the same across seasons so people recognise it.",
              "Involve the people warned in setting the thresholds that affect them."], "cyan"),
          B("Illustrative good practice.", sm=True)])),

    C("Measuring warnings", "How to tell whether an early warning system works",
      T(["Question", "Indicator", "Source"],
        [["Did the warning reach people?", "Share of households that received it, by sex, "
          "caste, disability, migrant status", "Post-event household survey"],
         ["How early?", "Hours between the first warning received and the hazard's impact",
          "Survey; SMS and siren logs"],
         ["Did people understand?", "Share who could say what the warning asked them to do",
          "Survey"],
         ["Did they act?", "Share who evacuated or took the protective step, and reasons for not "
          "acting", "Survey; shelter registers"],
         ["Who was left out?", "Deaths and injuries among people who did not receive or could "
          "not act on the warning", "Death audits; case reviews"],
         ["Was it accurate?", "Hits, misses and false alarms over several seasons",
          "Forecast verification"]]),
      TW([B("Illustrative indicator set. Sendai's target (g) is reported at national level. These "
            "questions bring it down to the people the system is meant to reach.", sm=True)],
         [H("cyan", "The disaggregation is the hard part and the useful part. An average "
            "coverage of 90 per cent can hide a hamlet that received nothing.")]),
      compact=True),
]

# ===================== SECTION 10: RELIEF, RECOVERY, EXCLUSION =====================
SLIDES += [
    D("10", "Section Ten", "Relief, recovery and who relief misses"),

    C("Phases", "Response, relief, recovery and reconstruction mean different things",
      TW([T(["Term (DM Act, s. 2, as amended)", "Meaning"],
            [["Response, s. 2(pa)", "Action taken directly before, during or after a disaster to "
              "save lives, reduce injury and health impact, ensure public safety and meet basic "
              "subsistence needs"],
             ["Rehabilitation, s. 2(ob)", "Restoration of basic services, facilities and capacity "
              "for the functioning of an affected community"],
             ["Recovery, s. 2(oa)", "Restoration or improvement of the economic, physical, social, "
              "cultural and environmental assets, systems and activities of an affected "
              "community"],
             ["Reconstruction, s. 2(o)", "Rebuilding and restoring infrastructure, services, "
              "buildings and facilities required for the community to function"]]),
          B("Source: " + DMA25 + ", s. 2.", sm=True)],
         [B("Relief is fast, visible and mostly paid by the State response fund. Recovery is "
            "slow, harder to see and easy to underfund. Under the Fifteenth Commission's "
            "national fund, the Response and Relief window had released ₹14,855 crore of its "
            "₹27,385 crore by 31 July 2025, while the Recovery and Reconstruction window had "
            "released ₹818.74 crore of ₹20,539 crore (" + FC16 + ", Table 11.1)."),
          B("Recovery decides whether a household returns to where it was. A family that has "
            "sold its livestock, taken a high-interest loan and pulled a child out of school "
            "may be counted as relieved and still be poorer for a decade."),
          H("amber", "The definition of recovery in the Act includes improvement as well as "
            "restoration. That is the legal hook for Build Back Better.")])),

    C("Caste", "The 2004 tsunami: Dalits blocked from relief",
      TW([B("The December 2004 tsunami killed at least 10,273 people in India, 8,010 of them in "
            "Tamil Nadu, and displaced at least 6,47,556 into emergency shelters. Human Rights "
            "Watch reported consistent accounts of caste discrimination in the distribution of "
            "aid. Fishing communities, who regard themselves as a higher caste, often blocked "
            "relief from reaching Dalits."),
          B("In one case a fishing community refused to share water provided by UNICEF and other "
            "relief organisations, claiming the Dalits would pollute it. A Dalit rights activist "
            "told HRW that relief materials could not be taken to Dalit areas because the "
            "fishing community refused to let them pass. Coastal farm labourers, sharecroppers "
            "and tenants, many of them Dalits, lost their crops and wages to seawater but were "
            "ignored in the first relief because they had suffered fewer deaths."),
          B("Source: " + HRW + ".", sm=True)],
         [Q("We had problems earlier as relief materials could not be taken to Dalit areas "
            "because the fishing community refused to let us pass.",
            "Murlidharan, Dalit rights activist, quoted in " + HRW),
          B("The government changed some policies when told of discrimination, and later "
            "assessed damage in Dalit communities and distributed rations to them. HRW's "
            "conclusion was that the greatest source of trouble was discrimination against "
            "Dalits by other victims of the tsunami, and that rooting it out required proactive "
            "measures from the government."),
          H("red", "Fifteen years later, the Fani assessment recorded segregated food and "
            "facilities in cyclone shelters and recommended placing new shelters closer to "
            "Dalit hamlets (" + FANI + ").")])),

    C("Women", "When relief is paid to the head of household",
      TW([B("After the tsunami, Human Rights Watch found that women's access to aid was brokered "
            "through husbands, fathers or other male relatives, because ration cards, the main "
            "proof of identity and residence, were issued in the name of the male head of the "
            "household. Women complained that relief and compensation were distributed through "
            "male heads, and press reports described cash relief that did not reach families. "
            "Unmarried, widowed and divorced women were often absorbed into the households of "
            "relatives instead of being counted as independent households."),
          B("The government did not treat women from fishing communities as workers, although "
            "most cleaned, sold and processed fish before the tsunami. Vocational offers of "
            "basket weaving or sewing gave low, irregular income and reinforced stereotypes "
            "about women's work (" + HRW + ").")],
         [T(["Practice", "Effect on women", "Alternative"],
            [["Relief paid to the ration card holder", "Women depend on male relatives",
              "Register adults individually"],
             ["Livelihood support only for boat owners", "Women fish workers get nothing",
              "Count women's work in the fishery"],
             ["Shelters without private toilets", "Risk to privacy and safety", "Separate, lit, "
              "lockable facilities"],
             ["Housing rebuilt in the husband's name", "Women's tenure insecure", "Joint title"],
             ["Male-only relief committees", "Women's needs missed", "Women on every committee"]]),
          B("HRW recommended registering men, women and children individually and involving "
            "women at all levels of planning and distribution. The Fani assessment recommended "
            "priority housing assistance for women-led households.", sm=True)])),

    C("Migrants", "People who are not on the list",
      TW([B("Relief systems in India run on lists: ration cards, voter rolls, land records, "
            "panchayat household registers. A person who is not on the local list is invisible "
            "to relief. After Fani, the ₹2,000 cash transfer and 50 kg of rice went only to ration "
            "card holders, which excluded many migrants and brick kiln workers who were "
            "non-residents and were equally affected (" + FANI + ")."),
          B("The new rural employment law contains a model provision. In a national calamity "
            "such as a flood, cyclone, tsunami or earthquake that dislocates rural people, "
            "adults from affected areas may register and get a job card from the Gram Panchayat "
            "or Programme Officer where they have temporarily relocated, apply for work there, "
            "and get lost cards reissued. Work done there counts towards the 125 days "
            "(" + VBG + ", Schedule II, para 10).")],
         [T(["Who falls off the list", "Why"],
            [["Seasonal migrant workers", "Registered in the home village, working elsewhere"],
             ["Brick kiln and salt pan workers", "Live at the worksite, often with families"],
             ["Tenants and sharecroppers", "Crop relief follows land records"],
             ["Urban renters and pavement dwellers", "No address proof"],
             ["Nomadic and pastoral groups", "Move between districts"],
             ["Single women in relatives' households", "Counted within another household"]]),
          H("cyan", "Sendai says migrants contribute to the resilience of communities and should "
            "be engaged in designing disaster risk reduction (paras 7, 36(a)(vi)). The first "
            "practical step is to count them before the disaster.")])),

    C("Disability and age", "People who cannot reach the shelter",
      TW([B("Human Rights Watch noted after the tsunami that disasters hurt persons with existing "
            "disabilities disproportionately and create new disabilities among the injured. "
            "People lose assistive devices such as crutches, artificial limbs and hearing or "
            "visual aids, and their usual caregivers may be killed, injured or diverted to "
            "other tasks. It recommended that shelters, health centres, housing and schools "
            "rebuilt after the disaster be accessible (" + HRW + ")."),
          B("The Fani assessment found that people with disabilities were among the most "
            "affected despite the evacuation, and recommended supplying assistive devices and "
            "giving self-help groups of persons with disabilities better market links "
            "(" + FANI + ").")],
         [BL(["Keep a village register of people who need help to evacuate, and name the "
              "person responsible for each.",
              "Make at least one shelter per cluster accessible: ramps, accessible toilets, "
              "space for wheelchairs.",
              "Include organisations of persons with disabilities in drawing up the plan, as "
              "Sendai para 36(a)(iii) asks.",
              "Stock replacement assistive devices and medicines for chronic illness.",
              "For heat, check on older people living alone during every alert."], "cyan"),
          H("amber", "Section 61 of the Act, which bans discrimination in relief, names sex, "
            "caste, community, descent and religion. It does not name disability or age.")])),

    C("Inclusive relief", "A checklist for relief that reaches everyone",
      T(["Principle", "What it means in practice", "Source of the lesson"],
        [["No discrimination", "Monitor distribution by caste, religion and sex; act on "
          "complaints at once", "DM Act s. 61; HRW 2005; Fani DLNA"],
         ["Individual entitlement", "Register adults individually; pay women directly", "HRW 2005"],
         ["No residence test", "Give relief to everyone affected, including migrants and "
          "non-residents", "Fani DLNA"],
         ["Family size", "Scale food to household size", "Fani DLNA"],
         ["Count indirect losses", "Include labourers, traders and others who lost income, as well "
          "as those who lost family members or boats", "HRW 2005"],
         ["Accessible shelters", "Ramps, toilets, privacy, lighting", "HRW 2005; Sendai para 36"],
         ["Voice in recovery", "Low-income communities and women on reconstruction "
          "committees", "Fani DLNA; HRW 2005"]]),
      TW([B("Synthesised from the documents cited. Each row is a failure that has been recorded "
            "in India.", sm=True)],
         [H("green", "For environmental injustice more broadly, see "
            "<a href=\"https://www.impactmojo.in/101-courses/env-justice.html\">Environmental "
            "Justice 101</a>.")]),
      compact=True),
]

# ===================== SECTION 11: INSURANCE AND SOCIAL PROTECTION =====================
SLIDES += [
    D("11", "Section Eleven", "Insurance and social protection in a shock"),

    C("Risk layering", "Different layers of risk need different money",
      TW([B("Disaster risk finance divides losses into layers by how often they happen and how "
            "large they are. Small, frequent losses are cheapest to absorb from savings, budgets "
            "and social protection. Medium losses are what State response funds are for. Rare, "
            "very large losses are where insurance, reinsurance and catastrophe bonds can move "
            "risk off the public budget."),
          B("India relies mostly on public funds. The Sixteenth Finance Commission found that "
            "insurance as a supplement to public disaster finance remains at a nascent stage, "
            "except for crop insurance, because of few products, low penetration, low awareness "
            "and high cost, and because governments prefer post-disaster payouts to buying cover "
            "in advance (" + FC16 + ", para 11.88).")],
         [T(["Layer", "Frequency", "Who usually pays"],
            [["Household shocks", "Every year", "Savings, loans, family, social protection"],
             ["Local disasters", "Every few years", "SDRF, scheme relaxations"],
             ["Severe disasters", "Once in a decade or so", "NDRF, after IMCT assessment"],
             ["Catastrophes", "Rare", "Budget reallocation, borrowing; insurance or catastrophe "
              "bonds where they exist"]]),
          B("Illustrative. NDMA has asked for risk pools: hazard-mortality and captive insurance, "
            "a national catastrophic risk insurance pool and a national catastrophe bond (" +
            FC16 + ", para 11.31).", sm=True)])),

    C("Crop insurance", "Pradhan Mantri Fasal Bima Yojana",
      TW([B("The Sixteenth Finance Commission describes PMFBY as the world's largest crop "
            "insurance scheme. The Union and State governments together pay 85 to 90 per cent "
            "of the premium. Even so, farmer penetration had reached 40 per cent over eight "
            "years. Of farmer applications enrolled in 2024-25, 6.5 per cent were from tenant "
            "farmers, 17.6 per cent from marginal farmers and 48 per cent from loanee farmers "
            "(" + FC16 + ", para 11.89)."),
          B("The Commission names technology-based assessment of crop losses and timely "
            "payment of claims as the keys to the scheme's future. For a disaster practitioner "
            "the enrolment figures are the warning: crop insurance protects people who have land "
            "and loans. Tenant farmers are a small share of enrolment and landless labourers are "
            "not covered at all.")],
         [ST([CARD("85-90%", "of PMFBY premium paid by governments", "cyan", "FC-16 para 11.89"),
              CARD("40%", "farmer penetration after eight years", "amber", "FC-16 para 11.89"),
              CARD("6.5%", "of 2024-25 enrolled applications from tenant farmers", "red",
                   "FC-16 para 11.89")], 1),
          H("amber", "Loanee farmers made up almost half of enrolled applications. Insurance tied "
            "to credit reaches borrowers first.")])),

    C("Parametric cover", "Insurance that pays when a measurement crosses a threshold",
      TW([TERM("Parametric insurance",
               "Cover that pays a pre-agreed amount when a measured index crosses a threshold, "
               "such as rainfall at a weather station, wind speed or temperature, without a "
               "survey of each policyholder's loss. It pays fast. Its weakness is basis risk. A "
               "household can suffer a loss when the index does not trigger, or receive money "
               "when it suffered none."),
          B("Nagaland is the Sixteenth Commission's example. Its Disaster Risk Transfer "
            "Parametric Insurance Solution is described as the first initiative in India to "
            "insure an entire State against extreme rainfall, using automated weather stations "
            "to set triggers, in a partnership of the Nagaland SDMA, SBI General Insurance, Munich "
            "Re and GIC Re. The Commission calls it a success that remains isolated and limited "
            "in scale (" + FC16 + ", para 11.90).")],
         [T(["Design question", "Why it matters"],
            [["Who holds the policy?", "A State policy pays the government; a household policy "
              "pays the family"],
             ["What is the index?", "Rainfall, wind or temperature must match the harm"],
             ["How dense are the stations?", "Sparse stations increase basis risk"],
             ["Where does the payout go?", "A State payout helps people only if a plan says how "
              "it will be spent"],
             ["Who pays the premium?", "Affordability decides coverage"]]),
          B("The Commission also notes that the Department of Financial Services and NDMA are "
            "working on a single-peril parametric insurance product, and recommends that "
            "insurance and catastrophe bonds be studied for affordability, applicability and "
            "scope for customisation (para 11.91).", sm=True)])),

    C("Social protection", "Social protection that scales up in a shock",
      TW([B("Shock-responsive social protection uses programmes that already exist to deliver "
            "help when a disaster strikes. A programme can pay more to people already enrolled "
            "(vertical expansion), add affected people who were not enrolled (horizontal "
            "expansion), relax its rules for a time, or lend its payment system and lists to a "
            "relief operation. Each route is faster than building a new relief scheme after the "
            "event."),
          B("Pakistan's 2022 response used a flood relief cash transfer that gave PKR 25,000 to "
            "1.1 million targeted households to meet emergency needs (" + PDNA + ", ch. 3). "
            "After Fani, Odisha paid ₹2,000 and 50 kg of rice to ration card holders, and the "
            "assessment recommended advance payment of social security entitlements and cash "
            "for work (" + FANI + ").")],
         [T(["Route", "Indian example", "Who it misses"],
            [["Vertical: pay more to existing beneficiaries", "Advance social security payments "
              "after Fani (recommended)", "People not already enrolled"],
             ["Horizontal: add new people", "Relief to all affected without proof of residency "
              "(recommended after Fani)", "Requires a way to identify them fast"],
             ["Relax rules", "VB-G RAM G s. 7: temporary expansion of works, relaxed "
              "documentation, more employment", "Depends on the Centre agreeing"],
             ["Portability", "VB-G RAM G Schedule II para 10: job cards at the place of "
              "relocation", "People who do not know the right exists"]]),
          B("The four routes are standard categories from the social protection literature, "
            "used here for teaching.", sm=True)])),

    C("Design", "Choosing a financial response for a disaster programme",
      T(["Need", "Instrument", "Strength", "Limit"],
        [["Immediate cash after a disaster", "Social protection top-up or relief transfer",
          "Fast if lists and payment systems exist", "Lists exclude migrants and the unregistered"],
         ["Income through a long drought", "Rural employment guarantee", "Self-targeting; "
          "builds assets", "Needs work to be opened in time; peak season pause"],
         ["Crop loss for cultivators", "PMFBY", "Large scale; subsidised premium",
          "Low tenant coverage; claims delays"],
         ["Fast liquidity for a State", "Parametric cover", "Pays in days", "Basis risk; premium "
          "cost"],
         ["Reconstruction of public assets", "SDRF, NDRF recovery window", "Statutory",
          "Slow release in practice"],
         ["Reducing future losses", "SDMF, NDMF", "Money exists", "Under-used; needs good "
          "proposals"]]),
      TW([B("Illustrative comparison drawing on the evidence in this section and section 04.",
            sm=True)],
         [H("cyan", "Combine instruments. A family hit by a cyclone may need a social protection "
            "top-up in week one, employment in month two, and a rebuilt house in year one.")]),
      compact=True),
]

# ===================== SECTION 12: MONITORING AND SOURCES =====================
SLIDES += [
    D("12", "Section Twelve", "Monitoring preparedness, and sources"),

    C("What to measure", "Measuring preparedness before the disaster",
      TW([B("Preparedness is hard to evaluate because its success is a disaster that did less "
            "harm than it would have. The 2025 amendment gives NDMA two new evaluation powers: "
            "to undertake disaster preparedness assessments of each State periodically, and to "
            "undertake post-disaster audits of a State's preparedness and response after a "
            "severe disaster (" + DMA25 + ", s. 6(2)(t), (u)). States must maintain disaster "
            "databases that feed a national one (s. 18(2)(p), s. 6(2)(v))."),
          B("The Sixteenth Finance Commission recommended turning the MHA's National Disaster "
            "Management Information System into a comprehensive system for the Union and the "
            "States, capturing real-time, transaction-level disaster data as a single source of "
            "disaster information (" + FC16 + ", Summary (ix)).")],
         [T(["Level", "Example indicator for a district"],
            [["Input", "Mitigation fund money proposed, sanctioned and released"],
             ["Output", "Shelters maintained and staffed; volunteers trained; registers of "
              "vulnerable people updated this year"],
             ["Outcome", "Share of households warned in time and able to act, by group"],
             ["Impact", "Deaths, affected people and economic loss per 100,000 people, compared "
              "with earlier events of similar strength"]]),
          B("Illustrative, following the input, output and outcome levels in UNDRR's Sendai "
            "monitoring scope.", sm=True)])),

    C("Evaluating", "How to tell whether preparedness worked",
      T(["Method", "What it tells you", "Example in this course", "Main limitation"],
        [["Before and after comparison", "Change in deaths or losses after a programme",
          "Odisha cyclone deaths, 1999 and after", "Storms differ; other changes happen at "
          "the same time"],
         ["Temperature-mortality model, before and after", "Change in deaths at the same heat",
          "Ahmedabad HAP evaluation (Hess et al. 2018)", "One city; wide confidence intervals"],
         ["Excess mortality", "True death toll of an event", "Ahmedabad May 2010 (Azhar et al. "
          "2014)", "Needs complete death registration"],
         ["Damage, loss and needs assessment", "Economic and social cost and recovery needs",
          "Fani DLNA; Pakistan PDNA", "Usually done once, soon after the event"],
         ["Simulation drill", "Whether systems work under test", "Not covered here", "Drills "
          "are not real events"],
         ["After-action review", "What worked and failed, by step", "Fani DLNA recommendations",
          "Depends on candour"]]),
      TW([B("A preparedness evaluation should report results by group. Both the tsunami and Fani "
            "records show that systems which reduce total deaths can still exclude Dalits, "
            "migrants, women and disabled people.", sm=True)],
         [H("amber", "Ask what the counterfactual is. A programme that reports fewer deaths in a "
            "weaker cyclone has shown nothing.")]),
      compact=True),

    C("Data", "Where the data for disaster monitoring come from",
      T(["Data", "Held by", "Use", "Watch for"],
        [["National Disaster Management Information System", "MHA", "State expenditure by "
          "disaster and relief item", "Coverage depends on what States enter (FC-16 para 11.43)"],
         ["State and national disaster databases", "SDMAs and NDMA (2025 amendment)",
          "Assessments, funds, plans, risk registers", "Whether they are published"],
         ["Death registration", "Civil registration system in each State", "Excess mortality in "
          "heatwaves and floods", "Delays and incomplete registration"],
         ["NCRB accidental deaths data", "National Crime Records Bureau", "Deaths from heat, "
          "lightning and other forces of nature", "Records only deaths reported to police"],
         ["IMD observations and forecasts", "India Meteorological Department", "Thresholds, "
          "warnings, verification", "Station density in rural areas"],
         ["DesInventar Sendai", "National loss databases built with UNDRR's tool", "Sendai "
          "targets (a) to (d)", "Self-reported"],
         ["Post-disaster assessments", "State government with partners", "Damage, loss, needs "
          "by sector", "One-off; method varies"]]),
      TW([B("Sources: " + FC16 + "; " + DMA25 + "; UNDRR, monitoring scope of the Sendai "
            "Framework.", sm=True)],
         [H("cyan", "Before designing new data collection, list what these sources already hold "
            "for your district. Most of the gaps are in disaggregation by caste, sex, disability "
            "and migrant status.")]),
      compact=True),

    C("A results framework", "Example: results framework for a district heat plan",
      T(["Level", "Statement", "Indicator", "Source"],
        [["Impact", "Fewer people die in heatwaves", "Excess all-cause deaths in heat alert "
          "periods per 100,000", "Civil registration"],
         ["Outcome 1", "Vulnerable people protect themselves during alerts", "Share of older "
          "people living alone visited during each alert", "Volunteer logs; survey"],
         ["Outcome 2", "Outdoor workers avoid peak heat", "Share of registered worksites "
          "observing changed hours on alert days", "Labour department inspections"],
         ["Output 1", "Alerts issued on local thresholds", "Alerts issued at least 3 days ahead",
          "District control room records"],
         ["Output 2", "Health system ready", "Primary health centres with cooling and oral "
          "rehydration stocks on 1 April", "Health department checklist"],
         ["Output 3", "Cool roofs installed", "Number of slum roofs converted", "Municipal "
          "records"],
         ["Assumption", "Workers can stop without losing wages", "Wage protection orders in force",
          "Labour department"]]),
      B("Illustrative framework built on the Ahmedabad model (Knowlton et al. 2014; ILO 2019 on "
        "cool roofs) and the gaps in the CPR review. The indicators are "
        "examples.", sm=True),
      compact=True),

    C("Sources", "Sources used in this course (1 of 2)",
      BL(["UNDRR, What is the Sendai Framework for Disaster Risk Reduction? "
          "https://www.undrr.org/implementing-sendai-framework/what-sendai-framework",
          "UNDRR, Sendai Framework for Disaster Risk Reduction 2015-2030 (text). "
          "https://www.undrr.org/media/16176/download",
          "Disaster Management Act 2005 (NIDM copy). https://nidm.gov.in/PDF/En_DM_act2005.pdf",
          "Disaster Management (Amendment) Act 2025, Gazette of India, 29 March 2025. "
          "https://www.thc.nic.in/Central%20Governmental%20Acts/Disaster%20Management%20Act,%202005.pdf",
          "PRS Legislative Research, The Disaster Management (Amendment) Bill, 2024. "
          "https://prsindia.org/billtrack/the-disaster-management-amendment-bill-2024",
          "Jos Chathukulam, Disaster Management (Amendment) Act, 2025: Old Wine in a New Bottle?, "
          "EPW 60(30), 26 July 2025. https://crmindia.org/wp-content/uploads/2025/08/Diaster-Management-EPW-1.pdf",
          "Report of the Sixteenth Finance Commission, Vol. I (2026-31). "
          "https://www.indiabudget.gov.in/doc/16fcvol1.pdf",
          "Economic Survey 2021-22, Vol. 2, para 2.35. "
          "https://www.indiabudget.gov.in/economicsurvey/ebook_es2022/files/basic-html/page90.html",
          "Government of Odisha, Cyclone Fani Damage, Loss and Needs Assessment (2019). "
          "https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf",
          "Government of Pakistan et al., Pakistan Floods 2022 Post-Disaster Needs Assessment. "
          "https://www.pc.gov.pk/uploads/downloads/PDNA-2022.pdf",
          "ThePrint, House panel recommends record Rs 2.84 lakh crore disaster fund, 7 August 2026. "
          "https://theprint.in/india/house-panel-recommends-record-rs-2-84-lakh-crore-disaster-fund-heatwaves-lightning-on-disaster-list/3008901/"],
         "cyan"),
      compact=True),

    C("Sources", "Sources used in this course (2 of 2)",
      BL(["India Meteorological Department, heat wave and warm night definitions. "
          "https://mausam.imd.gov.in/pdfs/heatcolduser/Definition.pdf",
          "Azhar et al. 2014, PLoS One 9(3):e91831. https://doi.org/10.1371/journal.pone.0091831",
          "Knowlton et al. 2014, Int J Environ Res Public Health 11(4):3473-92. "
          "https://doi.org/10.3390/ijerph110403473",
          "Hess et al. 2018, J Environ Public Health 2018:7973519. https://doi.org/10.1155/2018/7973519",
          "Sharma et al. 2025, Int J Biometeorol 69(9):2225-36. https://doi.org/10.1007/s00484-025-02959-8",
          "Sherwood and Huber 2010, PNAS 107(21):9552-5. https://doi.org/10.1073/pnas.0913352107",
          "Vecellio et al. 2022, J Appl Physiol 132(2):340-5. "
          "https://doi.org/10.1152/japplphysiol.00738.2021",
          "ILO 2019, Working on a Warmer Planet: The Impact of Heat Stress on Labour Productivity "
          "and Decent Work. https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@dgreports/@dcomm/@publ/documents/publication/wcms_711919.pdf",
          "Pillai and Dalal 2023, How is India Adapting to Heatwaves?, Centre for Policy "
          "Research. https://cprindia.org/wp-content/uploads/2023/03/Heat-Report_27March-23_Updated-Table.pdf",
          "Human Rights Watch 2005, After the Deluge. https://www.hrw.org/reports/2005/india0505/india0505.pdf",
          "VB-G RAM G Act 2025 (Act 36 of 2025). https://www.indiacode.nic.in/bitstream/123456789/22478/1/a2025-36.pdf",
          "SCC Online, 12 May 2026, on commencement and repeal of MGNREGA. "
          "https://www.scconline.com/blog/post/2026/05/12/vbgramg-act-implemented-from-1-july-2026/"],
         "indigo"),
      compact=True),

    {"type": "end",
     "eyebrow": "Disaster Risk and Heat Resilience 101 &middot; Complete",
     "headline": "Know who is in the path,<br>and reach them first.",
     "byline": "A hazard becomes a disaster through exposure and vulnerability. Read the law, "
               "follow the money, count every death, and check that relief reached the "
               "people at the end of every list. Explore the rest of the ImpactMojo 101 Series, "
               "free forever.",
     "ctas": [
         {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
         {"label": "Climate Essentials 101", "href": "https://www.impactmojo.in/101-courses/climate-essentials.html"},
         {"label": "Climate Risk Studio", "href": "https://www.impactmojo.in/Labs/climate-adaptation-lab.html"}],
     "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
]

DECK = {
    "slug": "disaster-heat",
    "title": "Disaster Risk and Heat Resilience 101",
    "description": ("Disaster Risk and Heat Resilience 101, a free foundational course for "
                    "development practitioners in South Asia. Hazard, exposure and vulnerability, "
                    "the Sendai Framework, India's Disaster Management Act 2005 and its 2025 "
                    "amendment, the response and mitigation funds and the Finance Commissions, "
                    "Odisha's cyclone record, floods, lightning and drought, heatwaves, heat "
                    "action plans and outdoor work, early warning, the people relief misses, "
                    "insurance and shock-responsive social protection. ImpactMojo, CC BY-NC-ND."),
    "slides": SLIDES,
}

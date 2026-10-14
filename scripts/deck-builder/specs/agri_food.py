# -*- coding: utf-8 -*-
"""
Agriculture and Food Systems 101: ImpactMojo 101 Series (native deck spec)
Who farms and on how much land, incomes and debt, MSP and procurement, the 2020-21 farm
laws, the PDS and the National Food Security Act, input subsidies, irrigation and
groundwater, crop insurance, PM-KISAN, markets, extension, FPOs, tenancy, women in
agriculture, climate risk, nutrition, and what evaluations have found. For development
practitioners in India.
Build: python3 scripts/deck-builder/build.py agri_food

Sources opened while writing (October 2026):
- PIB, NSS Report No. 587, Situation Assessment of Agricultural Households and Land and Livestock
  Holdings of Households in Rural India, 2019 (10 September 2021):
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=1753856
- Aparajita Bakshi (2021), Situation Assessment Survey of Agricultural Households 2019: A Statistical
  Note, Review of Agrarian Studies 11(2), doi 10.25003/RAS.11.02.0009:
  https://ageconsearch.umn.edu/record/334366/files/Situation_Assessment_Survey_of_Agricultural_Households_2019_A_Statistical_Note.pdf
- Department of Agriculture, Cooperation and Farmers Welfare, All India Report on Agriculture Census
  2015-16 (via FAO World Census of Agriculture):
  https://www.fao.org/fileadmin/templates/ess/ess_test_folder/World_Census_Agriculture/WCA_2020/WCA_2020_new_doc/IND_REP_ENG_2015_2016.pdf
- PIB, Agricultural Census (2021-22), 21 July 2026: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2287251
- PIB, MSP for Kharif crops, marketing season 2026-27, 13 May 2026: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260618
- PIB, MSP for Rabi crops, marketing season 2026-27: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2173567
- PIB, MSP for Rabi crops, marketing season 2027-28, 30 September 2026:
  https://www.pib.gov.in/PressReleasepage.aspx?PRID=2316941
- Indian Express, rabi MSP 2027-28 report: https://indianexpress.com/article/india/rabi-msp-2027-28-wheat-safflower-crop-rates-10900699/
- PIB, Minimum Support Prices: From Safety Net to Self-Sufficiency, 10 October 2025:
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=2177219
- Down To Earth, report on the High Level Committee on restructuring FCI, 22 January 2015:
  https://www.downtoearth.org.in/environment/reduce-food-security-benefits-from-67-to-40-population-says-panel-on-restructuring-fci--48344
- PRS, The Farm Laws Repeal Bill 2021: https://prsindia.org/billtrack/the-farm-laws-repeal-bill-2021
- Wikipedia, 2020 Indian agriculture acts: https://en.wikipedia.org/wiki/2020_Indian_agriculture_acts
- National Food Security Act 2013 (Act 20 of 2013), Gazette text via PRS:
  https://prsindia.org/files/bills_acts/acts_parliament/2013/national-food-security-act-2013.pdf
- Ministry of Finance, Budget at a Glance 2026-27: https://www.indiabudget.gov.in/doc/Budget_at_Glance/budget_at_a_glance.pdf
- Economic Survey 2025-26, chapter 6 (Agriculture and Food Management), chapter 12 and chapter 13:
  https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap06.pdf
  https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap12.pdf
  https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap13.pdf
- ETV Bharat, Rajya Sabha reply on the Dynamic Ground Water Resource Assessment 2025, 21 July 2026:
  https://www.etvbharat.com/en/bharat/nearly-11-per-cent-groundwater-assessment-units-over-exploited-govt-enn26072007475
- Vision IAS, summary of the Dynamic Groundwater Resource Assessment Report 2025:
  https://visionias.in/current-affairs/news-today/2025-12-30/environment/ministry-of-jal-shakti-releases-dynamic-groundwater-resource-assessment-report-2025
- PIB backgrounder, Pradhan Mantri Fasal Bima Yojana, 29 August 2026:
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc_9735_20260829_18493301.pdf
- PIB backgrounder, PM-KISAN 23rd instalment, 20 June 2026:
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jun/doc2026620898101.pdf
- PIB backgrounder, The New Era of Indian Agriculture and Allied Sectors, 12 August 2026:
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc2026812952301.pdf
- MoSPI, PLFS Annual Report 2023-24 (Statement 7):
  https://mospi.gov.in/sites/default/files/publication_reports/AnnualReport_PLFS2023-24L2.pdf
- MoSPI, PLFS Annual Report 2025 press note (March 2026):
  https://www.mospi.gov.in/uploads/latestReleases/latest_release_1774607827733_3e8964a9-268b-4cc9-ad65-cfc8a9e32f08_Press_note_AR_PLFS_2025_23032025_V2.1_26032026_final.pdf
- ICAR, Lok Sabha Unstarred Question 2365, 10 December 2024 (NICRA projections):
  https://www.icar.org.in/sites/default/files/Circulars/LU-2365.pdf
- ORF, Reducing stunting, building human capital: lessons from NFHS-6 (June 2026):
  https://www.orfonline.org/expert-speak/reducing-stunting-building-human-capital-lessons-from-nfhs-6
- Wikipedia, State List (Seventh Schedule entries 14, 17, 18, 28): https://en.wikipedia.org/wiki/State_List
- Drèze and Khera (2015), Understanding Leakages in the Public Distribution System, EPW 50(7):
  https://web.iitd.ac.in/~suban/COP290/stuff/pds/Understanding_Leakages_in_the_Public_Distribution_System.pdf
- Muralidharan, Niehaus and Sukhtankar, Identity Verification Standards in Welfare Programs, NBER WP 26744:
  https://www.nber.org/papers/w26744
- Ryan and Sudarshan (2022), Rationing the Commons, JPE 130(1): 210-257:
  https://ideas.repec.org/a/ucp/jpolec/doi10.1086-717045.html
- Cole, Giné, Tobacman, Topalova, Townsend and Vickery (2013), Barriers to Household Risk Management,
  AEJ Applied 5(1): 104-35: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr373.pdf
- Goyal (2010), Information, Direct Access to Farmers, and Rural Market Performance in Central India,
  AEJ Applied 2(3): 22-45: https://ideas.repec.org/a/aea/aejapp/v2y2010i3p22-45.html
- Cole and Fernando (2021), 'Mobile'izing Agricultural Advice, Economic Journal:
  https://www.atai-research.org/wp-content/uploads/2020/06/ueaa084.pdf
- Emerick, de Janvry, Sadoulet and Dar (2016), AER 106(6): 1537-61:
  https://povertyactionlab.org/sites/default/files/research-paper/852%20Ag%20Innovation%20Risk%20Oct2015.pdf
- Varshney, Joshi, Roy and Kumar (2020), PM-KISAN and the Adoption of Modern Agricultural Technologies
  in Uttar Pradesh, IFPRI Discussion Paper 1907:
  https://cgspace.cgiar.org/server/api/core/bitstreams/e1860a45-121f-44ba-a67e-8eebf09a884a/content
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


def DIV(num, word, title):
    return {"type": "divider", "num": num, "label": "Section " + word, "title": title}


def L(path, name):
    return '<a href="/101-courses/' + path + '">' + name + '</a>'


def A(url, name):
    return '<a href="' + url + '">' + name + '</a>'


def BAR(canvas, title, source, labels, datasets, horizontal=False, ytitle="", legend=False, stacked=False):
    opts = "{ plugins:{legend:{display:" + ("true" if legend else "false") + "}}"
    if horizontal:
        opts += ", indexAxis:'y'"
    if ytitle:
        axis = "x" if horizontal else "y"
        opts += ", scales:{ " + axis + ":{ title:{display:true,text:'" + ytitle + "'} } }"
    opts += " }"
    return {"t": "chart", "canvas": canvas, "title": title, "source": source, "type": "bar",
            "data": {"labels": labels, "datasets": datasets},
            "options": {"__js__": opts}}


def DS(label, data, color):
    return {"label": label, "data": data, "backgroundColor": color}


def LINE(canvas, title, source, labels, label, data, color="#0EA5E9", ytitle=""):
    opts = "{ plugins:{legend:{display:false}}"
    if ytitle:
        opts += ", scales:{ y:{ title:{display:true,text:'" + ytitle + "'} } }"
    opts += " }"
    return {"t": "chart", "canvas": canvas, "title": title, "source": source, "type": "line",
            "data": {"labels": labels,
                     "datasets": [{"label": label, "data": data, "borderColor": color,
                                   "backgroundColor": color, "tension": 0.2, "fill": False}]},
            "options": {"__js__": opts}}


CYAN, GREEN, AMBER, INDIGO, RED = "#0EA5E9", "#10B981", "#F59E0B", "#6366F1", "#EF4444"

AGC = "Agriculture Census 2015-16, All India Report, Department of Agriculture"
AGC21 = "PIB, Agricultural Census (2021-22), 21 July 2026"
SAS = "NSS 77th round, Situation Assessment Survey 2019, NSS Report 587 (PIB, 10 Sept 2021)"
RAS = "Bakshi (2021), Review of Agrarian Studies 11(2), from NSSO 2014 and NSO 2021"
KMS = "PIB, MSP for Kharif crops 2026-27, 13 May 2026"
RMS27 = "PIB, MSP for Rabi crops 2026-27, October 2025"
RMS28 = "PIB, MSP for Rabi crops 2027-28, 30 September 2026"
PIBMSP = "PIB, Minimum Support Prices: From Safety Net to Self-Sufficiency, 10 Oct 2025"
ES = "Economic Survey 2025-26, chapter 6"
ES13 = "Economic Survey 2025-26, chapter 13, Box XIII.1"
BAG = "Budget at a Glance 2026-27, Ministry of Finance"
NFSA = "National Food Security Act 2013 (Act 20 of 2013)"
PIBAG = "PIB backgrounder, The New Era of Indian Agriculture, 12 Aug 2026"
PMFBY = "PIB backgrounder on PMFBY, 29 Aug 2026"
KISAN = "PIB backgrounder on the PM-KISAN 23rd instalment, 20 June 2026"
GW = "Dynamic Ground Water Resource Assessment 2025, Rajya Sabha reply reported 21 July 2026"
PLFS24 = "PLFS Annual Report 2023-24, Statement 7, MoSPI"
PLFS25 = "PLFS Annual Report 2025 press note, MoSPI, March 2026"
NICRA = "ICAR, Lok Sabha Unstarred Q. 2365, 10 Dec 2024"
DK = "Dr&egrave;ze and Khera (2015), EPW 50(7)"


# ===================== SECTION 01: WHO FARMS =====================
SEC1 = [
    DIV("01", "One", "Who farms, and on how much land"),

    S("Starting point", "Three official sources describe Indian farming, and each counts something different", [
        TC([B("Before quoting any number about Indian farmers, a practitioner has to know which source "
              "it came from, because the three main sources do not count the same unit. The Agriculture "
              "Census counts operational holdings, which are parcels of land run as one unit, whoever "
              "owns them. The Situation Assessment Survey of the National Statistical Office counts "
              "agricultural households, defined by the value of what they produce. The Periodic Labour "
              "Force Survey counts workers by the industry of their main and subsidiary work."),
            B("The three give different totals for the same country in the same years, and none of them "
              "is wrong. A holding run jointly by two brothers is one holding and two households. A "
              "landless family that earns its living harvesting other people's fields is outside the "
              "Situation Assessment Survey altogether, because households living entirely on farm labour "
              "are excluded by definition.", sm=True)],
           [T(["Source", "Unit counted", "Latest published round"],
              [["Agriculture Census", "Operational holdings, by size, social group and sex of holder", "2015-16 (the 2021-22 census has finished fieldwork)"],
               ["Situation Assessment Survey (NSS)", "Agricultural households: produce worth over &#8377;4,000 a year and a member self-employed in farming", "77th round, January to December 2019"],
               ["Periodic Labour Force Survey", "Workers aged 15 and over, by industry", "Calendar year 2025"],
               ["Input Survey", "Use of seed, fertiliser and machinery by holdings", "2016-17"]]),
            H("amber", "Ask of every figure which survey produced it, for which year, and what unit it counts.")]),
    ]),

    S("Agriculture Census 2015-16", "Two-thirds of holdings are under one hectare and they hold a quarter of the land", [
        TC([BAR("chHoldings", "Share of holdings and of operated area by size class, 2015-16 (%)", AGC,
                ["Marginal (&lt;1 ha)", "Small (1-2)", "Semi-medium (2-4)", "Medium (4-10)", "Large (10+)"],
                [DS("Share of holdings", [68.45, 17.62, 9.55, 3.80, 0.57], CYAN),
                 DS("Share of operated area", [24.03, 22.91, 23.84, 20.16, 9.07], AMBER)],
                legend=True, ytitle="per cent")],
           [B("India had 146.45 million operational holdings in 2015-16, up 5.8 per cent from 138.34 "
              "million in 2010-11, while the area they operated fell 1.11 per cent to 157.82 million "
              "hectares. More holdings on less land is the arithmetic of subdivision at inheritance."),
            B("Marginal holdings, below one hectare, numbered 100.25 million: 68.45 per cent of all "
              "holdings on 24.03 per cent of the area. Small holdings of one to two hectares added "
              "another 17.62 per cent. Taken together, 86 per cent of holdings are under two hectares. "
              "At the other end, 0.84 million large holdings of ten hectares or more operated 9.07 per "
              "cent of the land, at an average of 17.07 hectares each.", sm=True),
            B("A programme that targets the average farmer is designing for a farm that very few people "
              "operate. The typical holder in this table farms well under one hectare.", sm=True)], ratio="a32"),
    ]),

    S("A long decline", "The average holding has more than halved since 1970-71", [
        TC([LINE("chAvgSize", "Average size of an operational holding, all India (hectares)", AGC,
                 ["1970-71", "1976-77", "1980-81", "1985-86", "1990-91", "1995-96", "2000-01", "2005-06", "2010-11", "2015-16"],
                 "Average size (ha)", [2.28, 2.00, 1.84, 1.69, 1.55, 1.41, 1.33, 1.23, 1.15, 1.08], GREEN, "hectares")],
           [B("The average operational holding was 2.28 hectares in 1970-71 and 1.08 hectares in "
              "2015-16. The fall has been steady across ten censuses. What has not changed is the "
              "average within each class. A marginal holding averaged 0.40 hectares in 1970-71 and 0.38 "
              "hectares in 2015-16. A large holding averaged 18.10 and 17.07 hectares."),
            B("So the national average fell because the mix shifted, with more and more holdings "
              "dropping into the marginal class as land was divided among heirs. The size of a marginal "
              "farm stayed close to 0.4 hectares for half a century.", sm=True),
            H("cyan", "Read the trend as a shift in the number of small holdings. Holdings in each class "
              "kept roughly the same size.")]),
    ]),

    S("Owned and operated", "Owning land and operating a holding are different things", [
        TC([TERM("Ownership holding", "Land a household holds with permanent heritable possession, with or "
                 "without the right to transfer it. Land held in owner-like possession under a long lease, "
                 "or a tribal household's customary land, also counts as owned in the NSS 77th round."),
            TERM("Operational holding", "All land used wholly or partly for agricultural production and "
                 "managed by one household, without regard to title, size or location. It includes land "
                 "owned, leased in or otherwise possessed."),
            B("A tenant who leases in two plots and owns none has an operational holding and no "
              "ownership holding. Schemes that pay owners and schemes that pay operators therefore reach "
              "different people.", sm=True)],
           [ST([C("0.512 ha", "average land owned per rural household, 2019", "cyan", SAS),
                C("8.2%", "of rural households landless (0.002 ha or less)", "red", SAS),
                C("101.98 m", "household operational holdings in the NSS survey, July 2018 to June 2019", "amber", SAS),
                C("0.913 ha", "average area per operational holding in the same survey", "green", SAS)], cols=2),
            B("The NSS count of 101.98 million operational holdings sits well below the census figure "
              "of 146.45 million. The NSS counts rural households, and multiple holdings within one "
              "household are not distinguished. The census counts every holding.", sm=True)]),
    ]),

    S("Situation Assessment Survey", "There were 9.3 crore agricultural households in 2019, just over half of rural India", [
        TC([B("The 77th round counted 93.09 million agricultural households, up from 90.2 million in "
              "2013. Their share of rural households fell from 57.8 per cent to 54 per cent over the same "
              "six years, according to Aparajita Bakshi's analysis of the two rounds. Cultivation was "
              "the principal source of income for 68.9 per cent of agricultural households in 2019."),
            B("The table shows who they are. Other Backward Classes make up 45.8 per cent of "
              "agricultural households. Scheduled Castes are 15.9 per cent of agricultural households "
              "and 28.4 per cent of non-agricultural rural households, because many Dalit families "
              "work on land without operating any. Scheduled Tribes are over-represented among "
              "farming households.", sm=True)],
           [T(["Social group", "Agricultural households (%)", "Non-agricultural households (%)", "All rural households (%)"],
              [["Scheduled Tribes", "14.2", "10.0", "12.3"],
               ["Scheduled Castes", "15.9", "28.4", "21.6"],
               ["Other Backward Classes", "45.8", "42.8", "44.4"],
               ["Others", "24.1", "18.8", "21.7"],
               ["All", "100.0", "100.0", "100.0"]]),
            B("Source: " + SAS + ". Agricultural year July 2018 to June 2019.", sm=True)], ratio="a23"),
    ]),

    S("Land and caste", "Most agricultural households possess under one hectare, and land follows caste", [
        TC([T(["Land possessed (ha)", "Agricultural households (%)", "Non-agricultural households (%)"],
              [["Under 0.01", "0.6", "26.8"],
               ["0.01 to 0.40", "34.2", "69.0"],
               ["0.40 to 1.00", "35.6", "3.1"],
               ["1.01 to 2.00", "17.7", "0.7"],
               ["2.01 to 4.00", "8.6", "0.4"],
               ["4.01 to 10.00", "2.8", "0.0"],
               ["Over 10.00", "0.4", "0.0"]]),
            B("Source: " + SAS + ".", sm=True)],
           [B("Seven in ten agricultural households possess under one hectare. Non-agricultural rural "
              "households mostly possess a homestead and nothing more: 95.8 per cent of them have under "
              "0.4 hectares."),
            B("The Agriculture Census shows how land is divided by caste. Scheduled Castes ran 11.84 "
              "per cent of operational holdings in 2015-16 and 8.54 per cent of the operated area. "
              "Scheduled Tribes ran 8.65 per cent of holdings and 11.27 per cent of the area, because "
              "tribal holdings in hill and forest districts are larger and often less productive. Both "
              "groups are a larger share of the rural population than their share of farmland.", sm=True),
            H("amber", "A scheme that pays per hectare owned will pay Dalit households the least, "
              "because they own the least.")]),
    ]),

    S("What is current", "The newest census is still unpublished, and farming's share of jobs is falling", [
        TC([P("cyan", "The 11th Agriculture Census, reference year 2021-22",
              "Fieldwork began in 2022. On 21 July 2026 the Minister of State for Agriculture told the Lok "
              "Sabha that field work and data collection for all three phases had been completed. Phase I "
              "enumerates every holding. Phase II samples 20 per cent of villages in each tehsil for "
              "cropping pattern and irrigation, and Phase III samples 7 per cent for input use. Until the "
              "results are released, 2015-16 remains the latest published census."),
            B("Source: " + AGC21 + ".", sm=True)],
           [ST([C("46.1%", "of all workers were in agriculture, PLFS 2023-24", "amber", PLFS24),
                C("43.0%", "of workers in agriculture in calendar year 2025, down from 44.8% in 2024", "green", PLFS25),
                C("&#8377;52.08 lakh crore", "estimated GVA of agriculture and allied sectors, 2025-26, current prices", "cyan", PIBAG),
                C("4.45%", "average growth of the sector, FY16 to FY25, led by livestock (7.1%) and fishing (8.8%)", "indigo", ES)], cols=2),
            B("The 2025 PLFS changed its design and moved to the calendar year, so MoSPI cautions that "
              "it is not strictly comparable with earlier rounds.", sm=True)]),
    ]),

    S("Vocabulary", "Terms this course uses throughout", [
        TC([T(["Term", "Meaning"],
              [["Kharif", "The monsoon season. Sown June to July, harvested from October. Paddy, cotton, soybean, pulses."],
               ["Rabi", "The winter season. Sown October to December, harvested from March. Wheat, mustard, gram."],
               ["Marketing season", "The year in which a crop is sold. Rabi Marketing Season 2027-28 covers wheat sown in late 2026."],
               ["MSP", "Minimum Support Price, the price at which public agencies offer to buy a mandated crop."],
               ["Procurement", "Purchase of grain by the Food Corporation of India and state agencies for the central pool."],
               ["Central pool", "The stock of rice and wheat held for the Public Distribution System and buffer."]])],
           [T(["Term", "Meaning"],
              [["APMC", "Agricultural Produce Market Committee, which runs a regulated market (mandi) under state law."],
               ["FPO", "Farmer Producer Organisation, a company or cooperative owned by farmers."],
               ["KCC", "Kisan Credit Card, a revolving crop loan account."],
               ["GIA and GCA", "Gross irrigated area and gross cropped area; a hectare cropped twice counts twice."],
               ["Stage of extraction", "Annual groundwater use as a share of what can be extracted each year."],
               ["Lakh, crore", "One lakh is 100,000. One crore is 10 million."]]),
            H("green", "A quintal is 100 kilograms. MSPs are quoted in rupees per quintal.")]),
    ]),
]

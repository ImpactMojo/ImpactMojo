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
- PRS, The Farmers' Produce Trade and Commerce Bill 2020: https://prsindia.org/billtrack/the-farmers-produce-trade-and-commerce-promotion-and-facilitation-bill-2020
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
- IIPS, NFHS-6 (2023-24) India and State/UT Fact Sheets (May 2026), indicators 68, 69, 70, 72:
  https://www.nfhsiips.in/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-24%20Fact%20Sheets.pdf
- Legislative Department, Constitution of India, Seventh Schedule, List II, entries 14, 17, 18, 28: https://legislative.gov.in/constitution-of-india/
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
              "hectares. More holdings on less land is consistent with subdivision among heirs."),
            B("Marginal holdings, below one hectare, numbered 100.25 million, which is 68.45 per cent of all "
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
              "and 28.4 per cent of non-agricultural rural households. Scheduled Tribes are a larger "
              "share of farming households than of rural households as a whole.", sm=True)],
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
              "households mostly possess a homestead and nothing more, and 95.8 per cent of them have "
              "under 0.4 hectares."),
            B("The Agriculture Census shows how land is divided by caste. Scheduled Castes ran 11.84 "
              "per cent of operational holdings in 2015-16 and 8.54 per cent of the operated area. "
              "Scheduled Tribes ran 8.65 per cent of holdings and 11.27 per cent of the area. Both "
              "groups make up a larger share of rural households (21.6 and 12.3 per cent in the NSS "
              "survey) than of operated farmland.", sm=True),
            H("amber", "A scheme that pays per hectare owned will pay Scheduled Caste households far less than their share of rural households.")]),
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


# ===================== SECTION 02: INCOMES AND DEBT =====================
SEC2 = [
    DIV("02", "Two", "Incomes and indebtedness"),

    S("Measuring income", "The survey builds income from five sources and offers two answers", [
        TC([B("India has no regular survey of household income. The Situation Assessment Survey is the "
              "only official source of household-level income for a large part of the population, as "
              "Bakshi points out. It adds up wages and salaries, rent from land leased out, and net "
              "receipts from crops, animals and non-farm business, where net receipt is receipts less "
              "expenses for that activity."),
            B("The 77th round reports income twice. The first answer deducts only paid-out expenses, "
              "the cash a household spent. The second also deducts imputed costs, which are the market value of "
              "family labour, home-grown seed and manure, and rent on the household's own land. The "
              "second answer is closer to the cost concepts the Commission for Agricultural Costs and "
              "Prices uses for MSP.", sm=True)],
           [T(["Monthly income per agricultural household, 2018-19 (&#8377;)", "Paid-out expenses deducted", "Paid-out and imputed expenses deducted"],
              [["Wages and salaries", "4,063", "4,063"],
               ["Leasing out land", "134", "134"],
               ["Net receipt, crop production", "3,798", "3,058"],
               ["Net receipt, farming of animals", "1,582", "441"],
               ["Net receipt, non-farm business", "641", "641"],
               ["Total", "10,218", "8,337"]]),
            B("Source: " + SAS + ", Table 6.", sm=True)], ratio="a23"),
    ]),

    S("Composition", "Wages now earn farm households more than their crops do", [
        TC([BAR("chIncome", "Average monthly income of an agricultural household by source, at 2018-19 prices (&#8377;)", RAS,
                ["Wages and salaries", "Crop production", "Farming of animals", "Non-farm business"],
                [DS("2012-13 (inflated to 2018-19 prices)", [2849.4, 4239.0, 1049.8, 704.4], INDIGO),
                 DS("2018-19", [4063, 3798, 1582, 641], GREEN)], legend=True, ytitle="rupees per month")],
           [B("In 2012-13 crop production was the largest source of income, 47.9 per cent of the total. "
              "By 2018-19 its share had fallen to 37.2 per cent and wages had risen to 39.8 per cent. "
              "Bakshi deflates the 2012-13 figures with the rural consumer price index so the two years "
              "can be compared."),
            B("At constant prices, income from crops fell 10.4 per cent in six years while income from "
              "wages rose 42.6 per cent and income from animals rose 50.7 per cent. Total income rose "
              "15.6 per cent in real terms. Crop output did not fall over the period. The index of "
              "agricultural production rose from 129.8 to 138.1, so the fall in crop income points to "
              "prices received and costs paid.", sm=True)], ratio="a32"),
    ]),

    S("A day's earnings", "Cultivation paid less than a day's wage", [
        TC([ST([C("&#8377;3,798", "monthly net receipt from crops, paid-out costs only", "amber", SAS),
                C("&#8377;3,058", "the same after imputed costs of family labour and own land", "red", SAS),
                C("&#8377;441", "monthly net receipt from animals after imputed costs, down from &#8377;1,582", "indigo", SAS),
                C("15.6%", "real growth in total income, 2012-13 to 2018-19", "green", RAS)], cols=2)],
           [B("Once family labour and owned land are valued at market rates, net income from animals "
              "almost disappears. The household's own labour on its cattle earns about what the same "
              "hours would earn at market wages, so the animal income is mostly a return to family "
              "labour, much of it unpaid."),
            B("Kishore and Jha's analysis of the same survey in the Hindustan Times on "
              "14 September 2021 carried the headline that farmers earned &#8377;27 a day from "
              "cultivation in 2018-19, and set it beside MGNREGA wages. The comparison is rough, because it divides a household's crop income across the days of a year.", sm=True),
            H("cyan", "Ask for the full distribution, by size class of land, before quoting the "
              "average for a district or a programme.")]),
    ]),

    S("Debt", "Half of agricultural households were in debt in 2019", [
        TC([ST([C("50.2%", "of agricultural households had an outstanding loan on the survey date", "red", SAS),
                C("&#8377;74,121", "average outstanding loan per agricultural household, indebted or not", "amber", SAS)], cols=2),
            B("The average is taken over all agricultural households, including the half with no debt, "
              "so the average loan among indebted households is roughly twice as large. The survey asks "
              "about the amount outstanding on the day of the first visit, which falls in the first "
              "half of 2019.", sm=True)],
           [P("cyan", "Reading a debt figure",
              "Two loans of the same size, one from a bank at a low rate and one from a moneylender "
              "at a high rate, appear as the same rupees in an outstanding-debt total. The burden lies in the interest rate, the "
              "repayment schedule and what the loan was for. Ask for the share of debt from "
              "institutional sources, the purpose of borrowing, and whether the loan funds farming or "
              "consumption and health spending."),
            P("amber", "Debt and distress",
              "A high average debt is not evidence of distress on its own. A household that borrows "
              "to buy a pump and one that borrows to pay a hospital bill carry the same debt on paper. "
              "Look at debt relative to income and assets, and at who the lender is.")]),
    ]),

    S("Doubling incomes", "The 2022 target, and what the survey says about it", [
        TC([FL(["Feb 2016: the Prime Minister sets a goal of doubling farmers' incomes by 2022",
                "Apr 2016: an inter-ministerial committee under Ashok Dalwai is formed",
                "Sep 2018: the committee reports, and recommends a Situation Assessment Survey every five years",
                "2019: the 77th round is fielded, six years after the 70th"]),
            B("The Dalwai Committee set the target national farmer income for 2022-23 at "
              "&#8377;1,92,694 at 2015-16 prices, or &#8377;2,71,378 at current prices, counting farm "
              "and non-farm income together (Government of India 2018, volume 14, as quoted by Bakshi).", sm=True)],
           [B("Between 2012-13 and 2018-19 the real income of an agricultural household grew by about 15 "
              "per cent. Doubling in the following four years would have required growth far faster "
              "than anything the survey records. Bakshi concludes that the numbers point to the "
              "near-impossibility of meeting the goal."),
            B("The 2019 round is the latest Situation Assessment Survey used in this course, and it "
              "predates the 2022 deadline. A claim that incomes doubled, or did not, needs a later "
              "household survey to support it.", sm=True),
            H("amber", "When a target is announced without a measurement plan, ask which survey will "
              "measure it and when.")]),
    ]),

    S("Credit", "Kisan Credit Cards and interest subvention carry most farm lending", [
        TC([ST([C("7.28 crore", "operational Kisan Credit Card accounts, 2025-26", "cyan", PIBAG),
                C("&#8377;10.08 lakh crore", "outstanding under KCC, as on 3 August 2026", "amber", PIBAG),
                C("&#8377;22,600 crore", "Modified Interest Subvention Scheme, Budget Estimate 2026-27", "green", BAG),
                C("14.7%", "of interest subvention benefits went to the Central region, which has 30% of gross cropped area", "red", ES)], cols=2)],
           [B("The Kisan Credit Card gives a farmer a revolving crop loan sized to the crops grown and "
              "the area cultivated. Under the Modified Interest Subvention Scheme the government pays "
              "part of the interest on short-term crop loans, so a farmer who repays on time borrows "
              "at a lower rate than the bank's normal rate."),
            B("The Economic Survey 2025-26 notes that the Central region accounts for 30 per cent of "
              "gross cropped area and the largest share of PM-KISAN beneficiaries but received only "
              "14.7 per cent of interest subvention benefits, which the Survey reads as untapped "
              "potential for credit linkage.", sm=True),
            H("cyan", "Ask how tenants and sharecroppers in your area get crop credit, since they do not "
              "hold the land records that lenders usually ask for.")]),
    ]),

    S("Practice", "Questions to ask of any claim about farm incomes", [
        TC([BL(["Name the survey. A Situation Assessment Survey figure is per agricultural household. "
                "A GVA figure divided by workers is per worker and includes plantation companies.",
                "Name the cost concept. Paid-out costs give &#8377;10,218 a month in 2018-19. Paid-out and "
                "imputed costs give &#8377;8,337.",
                "Say whether a figure is nominal or real. The 2012-13 and 2018-19 totals look like a 59 per cent rise in rupees "
                "and a 15.6 per cent rise after inflation.",
                "Prefer the median to the mean where you can, because a few large commercial farms "
                "pull the mean up. Ask for incomes by "
                "size class of land.",
                "Convert household figures to per person. A household of six on &#8377;10,218 a month has about "
                "&#8377;1,700 per person."], "cyan")],
           [T(["Claim you may hear", "What to check"],
              [["Farm incomes have doubled", "Which year is the base, which survey, and whether figures are nominal"],
               ["Most farm income is now non-farm", "Wages include farm labour; the survey does not split farm and non-farm wages"],
               ["Dairy is the most profitable activity", "Net animal income falls from &#8377;1,582 to &#8377;441 once family labour is costed"],
               ["Half of farmers are in debt", "The 50.2% is a share of agricultural households, measured in 2019"]]),
            H("green", "Bakshi notes that the 77th round does not separate agricultural from "
              "non-agricultural wages, so no one can say from it how much income comes from outside farming.")]),
    ]),
]


# ===================== SECTION 03: MSP AND PROCUREMENT =====================
SEC3 = [
    DIV("03", "Three", "MSP, the CACP and procurement"),

    S("What MSP is", "A price the government announces for 22 crops, and buys at for a few", [
        TC([B("Every year the Union government announces Minimum Support Prices for 22 mandated crops on "
              "the recommendation of the Commission for Agricultural Costs and Prices (CACP), after "
              "hearing state governments and central ministries. The CACP also recommends the Fair and Remunerative Price for sugarcane."),
            B("An MSP is a price at which public agencies stand ready to buy. It is not a legal floor "
              "on private trade. A farmer who sells to a private trader below MSP breaks no law, and public agencies buy only where purchase centres operate. Rice and wheat "
              "are bought in large volumes for the central pool. Pulses, oilseeds and copra are bought "
              "under the Price Support Scheme of PM-AASHA when market prices fall below MSP, and only "
              "from pre-registered farmers with valid land records.", sm=True)],
           [T(["Season", "Mandated crops"],
              [["Kharif (14)", "Paddy, jowar, bajra, ragi, maize, arhar (tur), moong, urad, cotton, groundnut, sunflower seed, soybean, sesamum, nigerseed"],
               ["Rabi (6)", "Wheat, barley, gram, masur (lentil), rapeseed and mustard, safflower"],
               ["Commercial (2)", "Jute, copra"],
               ["Separately", "Sugarcane, through the Fair and Remunerative Price"]]),
            B("Sources: " + ES + ", footnote 98; " + PIBMSP + ".", sm=True)]),
    ]),

    S("The 1.5 times rule", "Since 2018-19 every MSP is set at least 50 per cent above a cost of production", [
        T(["Crop (kharif 2026-27)", "MSP (&#8377;/quintal)", "Cost used (&#8377;/quintal)", "Margin over cost", "MSP 2025-26", "MSP 2013-14"],
          [["Paddy, common", "2,441", "1,627", "50%", "2,369", "1,310"],
           ["Jowar, hybrid", "4,023", "2,682", "50%", "3,699", "1,500"],
           ["Bajra", "2,900", "1,858", "56%", "2,775", "1,250"],
           ["Maize", "2,410", "1,544", "56%", "2,400", "1,310"],
           ["Tur (arhar)", "8,450", "5,496", "54%", "8,000", "4,300"],
           ["Moong", "8,780", "5,438", "61%", "8,768", "4,500"],
           ["Soybean (yellow)", "5,708", "3,805", "50%", "5,328", "2,560"],
           ["Cotton, medium staple", "8,267", "5,511", "50%", "7,710", "3,700"]]),
        TC([B("The Union Budget 2018-19 announced that MSPs would be fixed at no less than 1.5 times the "
              "all-India weighted average cost of production. Recent kharif and rabi announcements say they are in line with that rule. The margin is printed crop by crop, and for kharif "
              "2026-27 it ranges from 50 per cent for paddy to 61 per cent for moong.", sm=True)],
           [B("The common paddy MSP rose by &#8377;72 a quintal for 2026-27. The government's "
              "comparison with 2013-14 shows an 86 per cent rise over thirteen years. Source: " + KMS + ".", sm=True)]),
    ], compact=True),

    S("Rabi 2027-28", "Wheat got its smallest increase in seventeen years", [
        TC([BAR("chRabi", "Rabi Marketing Season 2027-28: MSP and the cost used to set it (&#8377; per quintal)", RMS28,
                ["Wheat", "Barley", "Gram", "Masur", "Mustard", "Safflower"],
                [DS("Cost of production", [1264, 1447, 3751, 3854, 3367, 4810], AMBER),
                 DS("MSP 2027-28", [2610, 2286, 5958, 7390, 6613, 7215], CYAN)], legend=True, ytitle="rupees per quintal")],
           [B("On 30 September 2026 the Cabinet fixed the wheat MSP for Rabi Marketing Season 2027-28 "
              "at &#8377;2,610 a quintal, up &#8377;25 from &#8377;2,585. The Indian Express reported "
              "it as a 0.97 per cent rise and the smallest increase in seventeen years. Safflower rose "
              "the most, by &#8377;675 to &#8377;7,215."),
            B("The margin over cost is 106 per cent for wheat, 96 per cent for mustard, 92 per cent "
              "for masur, 59 per cent for gram, 58 per cent for barley and 50 per cent for "
              "safflower. The margin depends on how the cost is estimated as much as on the price.", sm=True),
            H("amber", "A margin of 106 per cent does not mean wheat farmers double their money. It "
              "compares the MSP with one particular cost concept, discussed on the next slide.")], ratio="a32"),
    ]),

    S("Cost concepts", "Which cost the 50 per cent is added to is the heart of the MSP dispute", [
        TC([TERM("A1 and A2", "Paid-out costs: all out-of-pocket expenses plus the imputed value of owned "
                 "animal and machine labour. A1 is the measure for an owner-cultivator and A2 for a "
                 "tenant-cultivator, who also pays rent for leased-in land."),
            TERM("Family labour (FL)", "The imputed value of the work done by the farmer's own family, "
                 "valued at market wages."),
            TERM("C2 and C3", "Comprehensive cost. C2 includes imputed costs on owned land and family "
                 "labour. C3 also includes a value for the farmer's management input.")],
           [B("Bakshi describes the CACP as using nine cost concepts, all of which include some kind "
              "of imputed cost. The Swaminathan Commission recommended that MSP be set 50 per cent "
              "above the total cost of production, defined as all paid-out and imputed costs, "
              "including family labour and the rental value of owned land. Farmers' movements have "
              "insisted on that recommendation, and Bakshi notes it was central to the debate around "
              "the 2020 farm laws."),
            B("The margin in each MSP release is calculated on the cost column printed beside it, "
              "and the release defines that cost in a footnote. If the cost leaves out the rental "
              "value of the farmer's own land, a C2 calculation of the same MSP shows a smaller "
              "margin. When someone says MSP is or is not 1.5 times cost, ask which cost.", sm=True),
            H("cyan", "The SAS 77th round collected imputed costs for the first time, which lets "
              "researchers compute farm income on cost definitions close to the CACP's.")]),
    ]),

    S("Who sells at MSP", "A minority of farmers know the MSP, and fewer sell to a procurement agency", [
        TC([T(["Agricultural households (%)", "Paddy 2013", "Paddy 2019", "Wheat 2013", "Wheat 2019"],
              [["Aware of MSP", "32.3", "40.7", "39.2", "37.1"],
               ["Aware of a procurement agency", "25.1", "30.3", "34.5", "27.2"],
               ["Sold to a procurement agency", "13.5", "14.5", "16.2", "9.7"],
               ["Share of output sold at MSP", "27.0", "23.7", "35.0", "20.8"]]),
            B("Source: " + RAS + ", Table 3, from SAS 70th and 77th rounds.", sm=True)],
           [B("In 2019 only 14.5 per cent of paddy-growing agricultural households, and 9.7 per cent of "
              "wheat growers, sold any of their crop to a procurement agency. In 2015 the High Level "
              "Committee on restructuring the Food Corporation of India, chaired by Shanta Kumar, "
              "estimated from 2012-13 NSS data that only 6 per cent of farmers benefited from MSP "
              "through sales to official procurement."),
            B("Procurement happens where states have built purchase centres and agencies to run "
              "them. A farmer in a district without a purchase centre sells at the market price, "
              "whatever the MSP says.", sm=True),
            H("amber", "Awareness of MSP among wheat growers fell between the two rounds, and the share of "
              "wheat output sold at MSP fell from 35 to 20.8 per cent.")]),
    ]),

    S("Scale", "Procurement is large, and it is mostly rice and wheat", [
        TC([ST([C("1,175 LMT", "foodgrains procured in July 2024 to June 2025, up from 761.40 LMT in 2014-15", "cyan", PIBMSP),
                C("1.84 crore", "farmers the government counts as benefiting from procurement in 2024-25", "green", PIBMSP),
                C("266 LMT", "wheat procured by FCI in RMS 2024-25, against 188 LMT in 2022-23", "amber", PIBMSP),
                C("&#8377;16.08 lakh crore", "MSP paid to paddy farmers, 2014-15 to 2025-26", "indigo", KMS)], cols=2)],
           [B("A lakh metric tonnes (LMT) is 100,000 tonnes. The government reports that paddy "
              "procurement over 2014-15 to 2025-26 totalled 8,418 LMT, against 4,590 LMT over 2004-05 "
              "to 2013-14. Over the same periods MSP payments to paddy growers rose from &#8377;4.44 "
              "lakh crore to &#8377;16.08 lakh crore. These are the government's own comparisons of two "
              "periods of different length and should be read as such."),
            B("Pulses and oilseeds are bought far less, through NAFED and NCCF under PM-AASHA, "
              "which was allocated &#8377;7,200 crore in the 2026-27 budget. The government has raised "
              "its procurement guarantee for pulses from &#8377;45,000 crore to &#8377;60,000 crore. "
              "By 25 March 2025 it had procured 2.46 LMT of tur from 1,71,569 farmers in five states.", sm=True),
            B("Sources: " + PIBMSP + "; " + KMS + "; " + BAG + ".", sm=True)]),
    ]),

    S("The cost of buying more than is needed", "The Economic Survey says rice and wheat stocks have outgrown food security needs", [
        TC([P("amber", "Economic Survey 2025-26, Box VI.5",
              "The Survey says the scale of procurement, particularly of rice and wheat, has grown faster "
              "than food security requirements, leading to persistently high buffer stocks and rising "
              "carrying costs for storage, handling, interest and stock rotation. At the same time India "
              "imports edible oils and pulses."),
            B("It proposes using savings from better stock management to pay farmers who voluntarily "
              "shift part of their rice and wheat area to pulses, oilseeds and maize, starting in "
              "eastern and central India, and over time moving from physical procurement towards "
              "price-deficiency payments, bonuses and assured offtake.", sm=True)],
           [T(["Instrument", "How it works", "Main risk"],
              [["Open-ended procurement", "Agencies buy all grain of fair average quality offered at MSP", "Stocks pile up; benefits go where purchase centres exist"],
               ["Price Support Scheme (PM-AASHA)", "Buys notified pulses, oilseeds and copra when prices fall below MSP", "Quantity caps; registration and land-record requirements"],
               ["Price-deficiency payment", "Pays the gap between MSP and the market price, without buying the grain", "Traders may lower prices knowing the state will pay the gap"],
               ["Per-acre diversification incentive", "Pays farmers to grow a different crop", "Needs reliable crop verification and a market for the new crop"]]),
            H("cyan", "The Survey frames all of this as voluntary and phased, with food security protected "
              "through procurement volumes and buffer norms.")]),
    ]),
]


# ===================== SECTION 04: THE FARM LAWS =====================
LAWS = "PRS Legislative Research, bill pages for the three 2020 Acts and The Farm Laws Repeal Bill 2021"

SEC4 = [
    DIV("04", "Four", "The 2020 farm laws and their repeal"),

    S("The three Acts", "Three laws passed in September 2020 set out to change how crops are traded", [
        T(["Act", "What it provided", "What it would have changed"],
          [["Farmers' Produce Trade and Commerce (Promotion and Facilitation) Act 2020",
            "Trade in farm produce at any place of production, collection or aggregation, including electronic trading",
            "Trade outside the state-notified APMC market yards, and a bar on states levying market fees on trade outside their designated trade areas"],
           ["Farmers (Empowerment and Protection) Agreement on Price Assurance and Farm Services Act 2020",
            "A legal framework for agreements between farmers and buyers made before sowing, including the price",
            "A national framework for contract farming, with its own dispute resolution mechanism"],
           ["Essential Commodities (Amendment) Act 2020",
            "Removed cereals, pulses, potatoes, onions and edible oils from routine stock control",
            "Stock limits allowed only in extraordinary circumstances or after a steep price rise"]]),
        TC([B("Together the Acts would have opened a second channel of trade beside the APMC mandis, "
              "free of the market fees the mandis charge, and given contract farming a national legal "
              "basis.", sm=True)],
           [B("Source: " + LAWS + ".", sm=True)]),
    ], compact=True),

    S("Timeline", "Fourteen months from passage to repeal", [
        FL(["17 Sep 2020: passed by the Lok Sabha",
            "20 Sep 2020: passed by the Rajya Sabha by voice vote",
            "Late Sep 2020: presidential assent",
            "12 Jan 2021: Supreme Court stays implementation",
            "19 Nov 2021: Prime Minister announces repeal",
            "30 Nov 2021: laws formally repealed"]),
        TC([B("The Supreme Court stayed implementation of all three laws on 12 January 2021 and "
              "appointed a committee to hear the parties. The laws therefore never operated in full. "
              "On 19 November 2021 the Prime Minister announced in a televised address that the "
              "government would repeal them in the coming session of Parliament."),
            B("The Farm Laws Repeal Bill 2021 was introduced and passed by both Houses on 29 November "
              "2021, without debate in either House, and the laws were formally repealed on 30 November "
              "2021, when the Farm Laws Repeal Act received the President's assent.", sm=True)],
           [P("cyan", "Why the timeline matters",
              "The Acts were passed in a single session as government bills and repealed within two days of "
              "the repeal bill being introduced. The Rajya Sabha vote was by voice, which meant no recorded division. Most of the "
              "argument took place outside Parliament, at the protest sites on Delhi's borders at "
              "Singhu, Tikri and Ghazipur, which farmers left in December 2021, and in the "
              "Supreme Court."),
            B("Source: " + LAWS + ".", sm=True)]),
    ]),

    S("The constitutional setting", "Agriculture, land and markets are state subjects", [
        TC([T(["State List entry", "Subject"],
              [["14", "Agriculture, including agricultural education and research, and protection against pests and plant diseases"],
               ["17", "Water: water supplies, irrigation and canals, drainage and embankments, water storage and water power"],
               ["18", "Land: rights in or over land, land tenures including the relation of landlord and tenant, and transfer and alienation of agricultural land"],
               ["28", "Markets and fairs"]]),
            B("Source: Constitution of India, Seventh Schedule, List II.", sm=True)],
           [B("Agricultural marketing in India is organised under state APMC laws, and each state "
              "decides which produce is regulated in its markets, what fee is charged and who may be "
              "licensed to trade."),
            B("A central law that barred states from charging fees on trade outside their market "
              "yards therefore reached into a subject that the Constitution assigns to the states. "
              "Six state governments (Kerala, Punjab, Chhattisgarh, Rajasthan, Delhi and West Bengal) "
              "passed resolutions against the Acts. Whatever view one takes of the "
              "economics, any future national reform of agricultural markets has to work through, or "
              "with, state law.", sm=True),
            H("amber", "Tenancy, irrigation and land records are also state subjects. Most of the "
              "reforms discussed in this course are decided in state capitals.")]),
    ]),

    S("The argument for", "What the government said the laws would do", [
        TC([P("green", "More buyers for the farmer",
              "Allowing trade outside APMC yards would let farmers sell to any buyer, including "
              "processors and exporters, in any place. Competition between the mandi and private buyers "
              "was expected to raise the price farmers received."),
            P("green", "Lower transaction costs",
              "Trade outside the yards would pay no state market fee. Electronic trading would let "
              "buyers from other districts and states bid.")],
           [P("green", "Price certainty before sowing",
              "A contract signed before sowing, with an agreed price, would shift price risk to the "
              "buyer and give the farmer access to the buyer's inputs and technical advice."),
            P("green", "Private storage investment",
              "Removing routine stock limits on cereals, pulses, onions and edible oils was meant to "
              "encourage private investment in warehouses and cold chains, on the argument that stock "
              "limits discouraged it."),
            H("cyan", "Some of these arguments have empirical support elsewhere. Goyal's study of "
              "soybean markets in Madhya Pradesh, discussed in section 9, found that a private buyer's "
              "direct purchase channel raised mandi prices.")]),
    ]),

    S("The argument against", "What farmers' organisations and critics said", [
        TC([P("red", "The fear for MSP and procurement",
              "Farmers in the states where procurement is large feared that a parallel trade channel "
              "without fees would hollow out the mandis, and with them the procurement system through "
              "which they sell rice and wheat at MSP. The protests were most widespread in Punjab, "
              "Haryana and western Uttar Pradesh."),
            P("red", "Bargaining power",
              "Critics argued that a marginal farmer with under one hectare cannot negotiate a "
              "contract with a large buyer on equal terms, and doubted that the Act's own dispute "
              "process would protect them.")],
           [P("red", "Federalism and revenue",
              "State governments lost the power to levy fees on trade outside their market yards, "
              "in a subject the Constitution gives them."),
            P("red", "Process",
              "The government promulgated the three measures as ordinances in the first week of June "
              "2020, before Parliament met, and the Rajya Sabha passed the bills by voice vote."),
            H("amber", "Among the protesters' demands was to make MSP and state procurement of crops a "
              "legal right, which goes well beyond anything the three Acts had changed.")]),
    ]),

    S("After the repeal", "The MSP question remains open", [
        TC([B("The repeal ended the laws but not the arguments behind them. Farmers' movements continue "
              "to demand MSP calculated on comprehensive cost, and a legal right to MSP and "
              "procurement. A legal guarantee for 22 crops would require either public purchase of very large "
              "volumes or a mechanism that compels private buyers, and either is expensive."),
            B("The Economic Survey 2025-26 points in a different direction. It argues for using "
              "savings from smaller rice and wheat stocks to fund voluntary diversification, and over "
              "time for price-deficiency payments, bonuses and assured offtake in place of physical "
              "procurement. That is a proposal, and no such scheme has been announced nationally.", sm=True)],
           [T(["Proposal", "Who argues for it", "Fiscal cost"],
              [["Legal guarantee of MSP for all mandated crops", "Farmers' unions", "Very high; depends on how much the state must buy or top up"],
               ["MSP on C2 cost plus 50%", "Swaminathan Commission, farmers' movements", "Raises every MSP and every procurement bill"],
               ["Price-deficiency payments", "Economic Survey 2025-26, as a longer-term option", "Pays the gap only, but needs a reliable market price"],
               ["Status quo with PM-AASHA for pulses and oilseeds", "Current policy", "Capped by budget, &#8377;7,200 crore in 2026-27"]]),
            B("Sources: " + ES + ", Box VI.5; " + RAS + "; " + BAG + ".", sm=True)]),
    ]),

    S("Reading the episode", "What the data could and could not tell either side", [
        TC([T(["Claim", "What the evidence in this course shows"],
              [["Most farmers depend on MSP", "In 2019, 14.5% of paddy-growing and 9.7% of wheat-growing agricultural households sold to a procurement agency"],
               ["The laws only affected Punjab and Haryana", "The fee and trade provisions applied nationally; the procurement stakes were highest where procurement is large"],
               ["Private markets pay farmers more", "Some studies find gains where a credible buyer enters; results depend on competition in the local market"],
               ["Small farmers would gain bargaining power", "Two-thirds of holdings are under one hectare; bargaining power depends on aggregation through FPOs or cooperatives"]])],
           [B("National averages hide how differently the effects would have fallen across states. A farmer selling wheat in Punjab at "
              "MSP and a farmer selling soybean in Madhya Pradesh to private traders faced different "
              "risks from the same law."),
            BL(["Disaggregate by state and crop before predicting the effect of a market reform.",
                "Separate the effect on prices from the effect on who captures them.",
                "Ask what replaces a revenue source a state loses.",
                "Ask what happens to the aggregation that a mandi currently provides."], "cyan")]),
    ]),
]


# ===================== SECTION 05: PDS AND NFSA =====================
SEC5 = [
    DIV("05", "Five", "The PDS and the National Food Security Act"),

    S("The Act", "The NFSA turned subsidised grain into a legal entitlement in 2013", [
        T(["Section of the NFSA", "Entitlement"],
          [["3(1)", "Every person in a priority household: 5 kg of foodgrains a month at the prices in Schedule I"],
           ["3(1), first proviso", "Antyodaya Anna Yojana households: 35 kg a household a month"],
           ["3(2)", "Coverage up to 75% of the rural population and 50% of the urban population"],
           ["4", "Pregnant women and lactating mothers: free meals through the anganwadi, and a maternity benefit of not less than &#8377;6,000"],
           ["5", "Children aged six months to six years: free meals through the anganwadi; children up to class VIII: a free mid-day meal on school days"],
           ["13", "The eldest woman aged 18 or over is head of the household for the ration card"],
           ["Schedule I", "Rice at no more than &#8377;3 a kg, wheat &#8377;2, coarse grains &#8377;1, for three years and then as the Centre fixes, capped at MSP"]]),
        TC([B("The Act received assent on 10 September 2013. It covers about two-thirds of the "
              "population and uses the existing Targeted Public Distribution System to deliver grain. "
              "Source: " + NFSA + ".", sm=True)],
           [B("Section 13 matters beyond food. Making the eldest woman the head of the household on "
              "the ration card puts the card, and the authority to use it, in a woman's name.", sm=True)]),
    ], compact=True),

    S("Free grain", "Grain under the NFSA is now distributed free of cost", [
        TC([B("Targeted PDS replaced the universal system in 1997, dividing households into Below "
              "Poverty Line and Above Poverty Line categories. The Antyodaya Anna Yojana for the poorest "
              "followed in 2000 and now covers about 2.5 crore households. The NFSA set coverage at 75 "
              "per cent of the rural and 50 per cent of the urban population, about 81.35 crore people "
              "on the 2011 Census."),
            B("The Economic Survey 2025-26 states that wheat, rice and coarse grains are now "
              "distributed free of cost to eligible households, and that the government has added "
              "Aadhaar-based de-duplication, One Nation One Ration Card portability for migrants, and "
              "fortified grain.", sm=True)],
           [ST([C("80.56 crore", "persons identified by states, Feb 2026, against 81.35 crore intended", "cyan", PIBAG),
                C("79.8 crore", "beneficiaries covered under NFSA, Dec 2025", "green", PIBAG),
                C("&#8377;2,27,629 crore", "food subsidy, Budget Estimate 2026-27", "amber", BAG),
                C("&#8377;25,530 crore", "SARTHAK PDS, for transport, handling and automation over five years", "indigo", PIBAG)], cols=2),
            H("cyan", "The food subsidy was &#8377;1,99,867 crore in 2024-25 (actual) and &#8377;2,28,154 "
              "crore in the revised estimate for 2025-26.")]),
    ]),

    S("From field to ration shop", "The PDS is the reason the state buys so much rice and wheat", [
        FL(["Farmer sells paddy or wheat at MSP at a mandi or purchase centre",
            "FCI and state agencies hold the grain in the central pool",
            "Grain is allocated to states for NFSA and other welfare schemes",
            "States move it to fair price shops",
            "Households collect their entitlement with a ration card"]),
        TC([B("Procurement and distribution are two ends of one system. The MSP purchases in section 3 "
              "fill the central pool, and the NFSA draws on it. When procurement exceeds what the PDS "
              "and buffer norms need, stocks accumulate and the carrying costs rise, which is the "
              "Economic Survey's argument for diversification."),
            B("Because the PDS distributes rice and wheat, it also shapes what is grown. A state that "
              "procures millets for its PDS creates a market for millets.", sm=True)],
           [P("amber", "Two policies, one budget line",
              "The food subsidy pays for both the purchase of grain at MSP and its distribution. A "
              "decision to raise MSP increases the cost of every tonne the PDS distributes. A decision "
              "to widen PDS coverage increases how much must be procured. Changes on one side need to "
              "be costed on the other.")]),
    ]),

    S("Leakage", "Diversion from the PDS was high and fell sharply where states reformed it", [
        TC([BAR("chLeak", "Estimated share of PDS grain that did not reach households (%)", DK,
                ["2004-05", "2011-12"],
                [DS("NSS-based estimate", [54, 42], RED), DS("IHDS-based estimate", [49, 32], AMBER)],
                legend=True, ytitle="per cent")],
           [B("Leakage is estimated by comparing the grain the FCI released to states with the grain "
              "households report buying in a survey. Dr&egrave;ze and Khera, writing in the Economic "
              "and Political Weekly in February 2015, estimated that leakage fell from 54 to 42 per "
              "cent between 2004-05 and 2011-12 using NSS data, and from about 50 to about 30 per cent "
              "using the India Human Development Survey."),
            B("They found the decline was driven by states that reformed their PDS, such as "
              "Chhattisgarh, Odisha and Bihar, and that the largest remaining source of leakage was "
              "the Above Poverty Line quota, which the NFSA was due to phase out. The Shanta Kumar "
              "committee had cited 40 to 50 per cent leakage and a figure of 47 per cent for 2011-12, "
              "which Dr&egrave;ze and Khera dispute.", sm=True),
            H("amber", "A leakage estimate depends on how the offtake is counted. Ad hoc allocations "
              "added wrongly moved the national figure from 42 to 47 per cent.")], ratio="a32"),
    ]),

    S("Identity and exclusion", "Biometric authentication cut corruption and also cut people off", [
        TC([B("Karthik Muralidharan, Paul Niehaus and Sandip Sukhtankar evaluated the rollout of "
              "Aadhaar-based biometric authentication in Jharkhand's PDS. The rollout was randomised "
              "across 132 sub-districts in 10 districts. Their NBER working paper (No. 26744) finds "
              "that the reform reduced corruption but imposed substantial costs on legitimate "
              "beneficiaries, 1.5 to 2 million of whom lost access to benefits at some point during "
              "the reforms."),
            B("The authors argue that the adverse effects were driven mainly by decisions about how "
              "the transition was managed. The table sets out, as reasoning for practitioners, how "
              "common design choices trade one kind of error against the other.", sm=True)],
           [T(["Design choice", "Effect on leakage", "Effect on exclusion"],
              [["Biometric check at the shop", "Lowers impersonation", "Raises it where machines or networks fail"],
               ["Cancel cards not seeded with Aadhaar", "Removes duplicates and ghosts", "Removes eligible people who could not seed"],
               ["Portability (One Nation One Ration Card)", "Little direct effect", "Lowers it for migrants away from home"],
               ["Fallback to manual entry or a nominee", "Some risk of misuse", "Lowers it for the old and disabled"]]),
            H("cyan", "When you evaluate a delivery reform, measure both errors. Count payments to the "
              "wrong people, and count payments missing from the right ones.")]),
    ]),

    S("Coverage", "The coverage ceiling is fixed in people counted in 2011", [
        TC([B("The coverage percentages in section 3(2) were applied to the population of the 2011 "
              "Census, giving about 81.35 crore people. As the population has grown since 2011 and no "
              "new census count has been used, the same number of people is a smaller share of today's "
              "population. Families formed after the lists were drawn, and migrants who moved, are "
              "among those at risk of being left out."),
            B("States identify the eligible households within their quota. By February 2026 they had "
              "identified 80.56 crore people, close to the ceiling.", sm=True)],
           [P("amber", "The 2015 proposals that were not adopted",
              "The High Level Committee chaired by Shanta Kumar, reporting on 20 January 2015, "
              "proposed cutting NFSA coverage from 67 per cent of the population to 40 per cent while "
              "raising the entitlement from 5 to 7 kg, moving towards cash transfers in place of grain, "
              "letting private firms procure and store grain, and paying fertiliser subsidy as cash of "
              "&#8377;7,000 a hectare. Coverage was not cut."),
            B("Source: Down To Earth's report of the committee, 22 January 2015.", sm=True)]),
    ]),

    S("Food and nutrition", "The PDS delivers calories, and the NFSA also promises meals", [
        TC([B("The PDS moves cereals. A household's need for protein, fat and micronutrients is met "
              "mostly by the pulses, milk, eggs, vegetables and oil it buys in the market. A cheaper "
              "staple frees income for these, but whether it is spent on food depends on the household."),
            B("The NFSA reaches further than the ration shop. Sections 4, 5 and 6 entitle pregnant "
              "women, lactating mothers and children to free meals through the anganwadi and the "
              "school, and section 6 requires states to identify malnourished children and feed "
              "them. Practitioners working on child nutrition should treat these entitlements as "
              "part of the same Act as the ration shop.", sm=True)],
           [T(["NFSA channel", "Who it reaches", "Section"],
              [["Ration shop (TPDS)", "Priority and Antyodaya households", "3"],
               ["Anganwadi meals", "Children 6 months to 6 years; pregnant women and lactating mothers", "4(a), 5(1)(a)"],
               ["Mid-day meal", "Children up to class VIII in government, local body and aided schools", "5(1)(b)"],
               ["Maternity benefit of at least &#8377;6,000", "Pregnant women, other than those in regular government or PSU employment", "4(b)"],
               ["Meals for malnourished children", "Children identified through the anganwadi", "6"]]),
            B("For the nutrition evidence, see " + L("nutrition.html", "Nutrition 101") + ".", sm=True)]),
    ]),
]


# ===================== SECTION 06: INPUT SUBSIDIES =====================
SEC6 = [
    DIV("06", "Six", "Input subsidies: fertiliser, power and machinery"),

    S("The money", "Fertiliser and food subsidies dwarf every other farm programme", [
        T(["Item (&#8377; crore)", "2024-25 actual", "2025-26 budget", "2025-26 revised", "2026-27 budget"],
          [["Fertiliser subsidy", "1,70,683", "1,67,887", "1,86,460", "1,70,781"],
           ["Food subsidy", "1,99,867", "2,03,420", "2,28,154", "2,27,629"],
           ["PM-KISAN", "66,121", "63,500", "63,500", "63,500"],
           ["Modified Interest Subvention Scheme", "22,600", "22,600", "22,600", "22,600"],
           ["Crop insurance scheme", "14,473", "12,242", "12,267", "12,200"],
           ["PM-AASHA (price support)", "5,438", "6,941", "6,941", "7,200"],
           ["PM-KUSUM (solar pumps)", "2,560", "2,600", "5,000", "5,000"]]),
        TC([B("Source: " + BAG + ". The fertiliser subsidy alone is more than two and a half times "
              "PM-KISAN and about fourteen times the crop insurance budget.", sm=True)],
           [B("In 2025-26 the revised fertiliser estimate came in &#8377;18,573 crore above the budget. "
              "The fertiliser bill is exposed to world prices of gas, phosphate and potash, which the "
              "budget cannot control.", sm=True)]),
    ], compact=True),

    S("How fertiliser is subsidised", "Urea is cheap at the counter, and farmers use more of it", [
        TC([B("Urea, the main source of nitrogen, is sold to farmers at a retail price set by the "
              "government, and the government meets the difference between that price and the cost "
              "of supply. Phosphatic and potassic fertilisers are supported through nutrient-based "
              "pricing, a fixed subsidy per unit of nutrient. The result is that nitrogen is much "
              "cheaper relative to phosphorus and potassium than its cost would make it."),
            B("The Economic Survey 2025-26 says plainly that the urea subsidy has increased "
              "application and that this increased use has been reported to affect soil productivity "
              "negatively. It lists neem-coating of urea, Aadhaar-linked verification at the point of "
              "sale and the Integrated Fertiliser Management System as steps that improved control "
              "over physical flows without changing the price signal farmers face.", sm=True)],
           [P("amber", "The Survey's diagnosis, in its words",
              "&ldquo;As long as one nutrient is vastly cheaper than others, its overuse is "
              "structurally embedded, regardless of monitoring or enforcement.&rdquo;"),
            B("Source: " + ES + ", Box VI.4.", sm=True),
            H("cyan", "A price subsidy reaches farmers in proportion to how much they buy. Those who use "
              "the most urea receive the most subsidy.")]),
    ]),

    S("Nutrient balance", "The ratio of nitrogen to potassium has more than doubled since 2009-10", [
        TC([BAR("chNPK", "Parts of nitrogen (N) and phosphorus (P) applied for each part of potassium (K)", ES + ", Box VI.4",
                ["2009-10", "2019-20", "2023-24", "Agronomic benchmark"],
                [DS("Nitrogen per unit K", [4, 7, 10.9, 4], CYAN), DS("Phosphorus per unit K", [3.2, 2.8, 4.1, 2], AMBER)],
                legend=True, ytitle="parts per part of potassium")],
           [B("The Survey reports the national N:P:K ratio at 4:3.2:1 in 2009-10, close to recommended "
              "levels for most Indian soils. By 2019-20 it had moved to 7:2.8:1 and by 2023-24 to "
              "about 10.9:4.1:1. Agronomic benchmarks for most crops and soils suggest a ratio closer "
              "to 4:2:1."),
            B("The Survey links excess nitrogen to lower soil organic matter, faster depletion of "
              "micronutrients, weaker soil structure and nitrate leaching into groundwater, and says "
              "that in several irrigated belts the yield response to fertiliser has plateaued or "
              "declined even as application has risen.", sm=True),
            H("amber", "More fertiliser is not more nutrition for the crop when the nutrients are out "
              "of balance.")], ratio="a32"),
    ]),

    S("A proposal", "Raise the urea price a little and pay farmers the difference per acre", [
        TC([B("The Economic Survey 2025-26 proposes separating income support from fertiliser purchase. "
              "The retail price of urea would rise modestly, and an equivalent amount would be "
              "transferred directly to cultivators per acre, indexed to agro-climatic zone and "
              "cropping pattern. Farmers keep the same purchasing power, but nitrogen's price moves "
              "closer to its agronomic cost."),
            B("The Survey expects efficient users to gain, because they receive the full transfer and "
              "spend less at the counter. Over-users face a reason to shift to balanced fertilisation. "
              "Low-input farmers growing pulses and oilseeds in rain-fed areas would gain on net. It "
              "proposes pilots across irrigated, rain-fed and mixed systems before national roll-out.", sm=True)],
           [P("red", "The tenancy problem, which the Survey raises itself",
              "A per-acre transfer is paid to someone identified with the land. Where a portion of the "
              "land is cultivated by renters, the owner may receive the transfer while the tenant pays "
              "the higher urea price. The Survey suggests that pilot designs include tenancy-heavy "
              "districts to refine the mechanism."),
            T(["Who gains or loses", "Under the proposal"],
              [["Farmer applying balanced doses", "Gains: full transfer, lower spending"],
               ["Farmer over-applying urea", "Loses unless they cut use"],
               ["Rain-fed pulse or oilseed grower", "Gains: transfer exceeds extra cost"],
               ["Tenant without recorded lease", "Loses if the transfer goes to the owner"]])]),
    ]),

    S("Power for pumps", "Free electricity is rationed, and rationing misallocates water", [
        TC([B("Where farm power is free or nearly free, the only limit on pumping is how many hours "
              "of supply the utility provides. Nicholas Ryan and Anant Sudarshan studied this system in "
              "Rajasthan (Rationing the Commons, Journal of Political Economy 2022, "
              "130(1): 210-257)."),
            B("They find that farmers face near-zero prices for pumping, but rationing binds, so on "
              "average farmers use roughly the socially optimal amount of water. The rationing regime "
              "is still very inefficient because it misallocates water across farmers. A ration of "
              "hours, for example, gives a farmer with a high-value crop the same water as a farmer with "
              "a low-value one. They estimate "
              "that a Pigouvian reform, which prices pumping at its cost to the commons, would raise agricultural surplus by 12 per cent of household income.", sm=True)],
           [ST([C("11.49 lakh", "off-grid solar pumps installed for farming under PM-KUSUM, Aug 2026", "green", PIBAG),
                C("15.89 lakh", "farm pumps covered by feeder-level solarisation", "cyan", PIBAG),
                C("1,726 MW", "decentralised solar capacity on farmers' land", "amber", PIBAG),
                C("&#8377;5,000 crore", "PM-KUSUM, Budget Estimate 2026-27", "indigo", BAG)], cols=2),
            H("red", "A solar pump has close to zero cost per extra hour of pumping. Where groundwater "
              "is already over-exploited, solar pumps without a limit on extraction can deepen the "
              "problem.")]),
    ]),

    S("Comparing instruments", "Each way of supporting farmers reaches different people", [
        T(["Instrument", "Who receives most", "Who it misses", "Effect on resource use"],
          [["Fertiliser price subsidy", "Heavy users of urea, often in irrigated rice and wheat", "Rain-fed farmers who buy little fertiliser", "Encourages excess nitrogen"],
           ["Free or flat-rate power", "Farmers with electric pumps and good aquifers", "Rain-fed and canal-dependent farmers; those without connections", "Encourages pumping where not rationed"],
           ["Interest subvention", "Farmers with bank accounts, land records and KCCs", "Tenants and those who borrow informally", "Neutral"],
           ["PM-KISAN", "Every eligible landholding family equally", "Tenants and landless labourers", "Neutral"],
           ["Per-acre transfer (proposed)", "Recorded cultivators, by area", "Unrecorded tenants unless the design includes them", "Neutral; lets input prices signal cost"],
           ["MSP procurement", "Sellers of rice and wheat near purchase centres", "Farmers in districts without procurement", "Favours rice and wheat over other crops"]]),
        TC([B("This table is a reasoning aid drawn from the evidence in this course, and the second "
              "and third columns describe tendencies. Check them against data for the district you "
              "work in.", sm=True)],
           [B("A practitioner choosing between instruments should ask who is on the list, how the "
              "list is made, and what the instrument does to the price of water, fertiliser and "
              "crops.", sm=True)]),
    ], compact=True),

    S("Machines and soil", "Small plots make machines hard to own, so hiring centres matter", [
        TC([B("Fragmented holdings and rising labour shortages, says the Economic Survey 2025-26, "
              "continue to hinder mechanisation. On a 0.38-hectare marginal holding, owning a tractor "
              "or a combine harvester makes no sense, but hiring one for a day can. Between 2014-15 "
              "and 2025-26, 25,689 Custom Hiring Centres were set up under the Sub-Mission on "
              "Agricultural Mechanisation, including 558 in 2025-26 up to 30 October 2025."),
            B("The Survey recommends collective ownership through FPOs, primary agricultural credit "
              "societies and self-help groups, and machinery designed for small plots.", sm=True)],
           [ST([C("26.09 crore", "soil health cards issued, as of July 2026", "green", PIBAG),
                C("70,002", "Krishi Sakhis trained to give soil health advice", "cyan", PIBAG),
                C("25,689", "Custom Hiring Centres set up, 2014-15 to 2025-26", "amber", ES)], cols=3),
            P("amber", "A card is not a change in practice",
              "The Survey notes that despite the scale-up of soil testing and soil health cards, "
              "fertiliser use remains inefficient and the N:P:K ratio has deteriorated, largely "
              "because of price distortions favouring nitrogen. Information alone does not overcome "
              "a price that rewards the wrong choice.")]),
    ]),
]


# ===================== SECTION 07: IRRIGATION AND GROUNDWATER =====================
SEC7 = [
    DIV("07", "Seven", "Irrigation and groundwater"),

    S("Irrigation coverage", "Just over half the cropped area is irrigated, and rice gets most of it", [
        TC([ST([C("41.7%", "gross irrigated area as a share of gross cropped area, 2001-02", "indigo", ES),
                C("55.8%", "the same share in 2022-23", "cyan", ES),
                C("about 67%", "irrigation coverage of rice", "green", ES),
                C("about 26%", "irrigation coverage of pulses", "amber", ES),
                C("under 15%", "irrigation coverage of millets", "red", ES)], cols=3),
            B("Source: Economic Survey 2025-26, paragraph 6.21.", sm=True)],
           [B("Irrigation gives a farmer water when the rain fails, which makes it possible to grow a "
              "second crop, to use fertiliser with confidence and to plant higher-value crops. The "
              "share of cropped area that is irrigated rose by about 14 percentage points in two "
              "decades."),
            B("Coverage is very uneven across crops. Rice, a water-intensive crop, is the most irrigated. Pulses and millets, which the government wants farmers to grow more of "
              "for nutrition and import reasons, are mostly rain-fed. The Survey calls expanding "
              "irrigation in lagging states and crops, while ensuring sustainability, an urgent "
              "priority, and argues that rejuvenating water bodies and increasing surface storage "
              "would earn the economy far more than other public investments.", sm=True),
            H("amber", "Gross irrigated area counts a hectare irrigated twice in a year twice. Net "
              "irrigated area counts it once. Check which one a source reports.")]),
    ]),

    S("The 2025 assessment", "India extracts about 61 per cent of the groundwater it can replenish", [
        TC([T(["Measure, 2025", "Value"],
              [["Annual groundwater recharge", "448.52 billion cubic metres"],
               ["Annual extractable resource", "407.75 BCM"],
               ["Annual extraction, all uses", "247.22 BCM"],
               ["National stage of extraction", "60.63% (60.48% in 2024; 63.33% in 2017)"],
               ["Assessment units", "6,762 blocks, mandals and talukas"]]),
            B("Sources: " + GW + "; Vision IAS summary of the 2025 report.", sm=True)],
           [T(["Category of unit", "Stage of extraction", "Units", "Share"],
              [["Safe", "Under 70%", "4,946", "73.14%"],
               ["Semi-critical", "70% to 90%", "758", "11.21%"],
               ["Critical", "90% to 100%", "201", "2.97%"],
               ["Over-exploited", "Above 100%", "730", "10.80%"],
               ["Saline", "Separate category", "127", "1.88%"]]),
            B("An over-exploited unit takes out more water each year than the rain and rivers put "
              "back. The Central Ground Water Board and the states carry out the assessment jointly.", sm=True)]),
    ]),

    S("Where the water table falls", "Punjab draws one and a half times what it recharges", [
        TC([BAR("chGW", "Stage of groundwater extraction, 2025 (% of extractable resource)", GW,
                ["Punjab", "Rajasthan", "Haryana", "Delhi", "All India", "Himachal Pradesh"],
                [DS("Stage of extraction, 2025", [156.36, 147.11, 136.75, 92.10, 60.63, 38.50], RED)],
                horizontal=True, ytitle="per cent")],
           [B("The national average hides a concentrated problem. Punjab extracted 156.36 per cent of "
              "its extractable groundwater in 2025, Rajasthan 147.11 per cent and Haryana 136.75 per "
              "cent. Over-exploited units are concentrated in the north-west, in the west and in parts "
              "of the south, in Karnataka, Tamil Nadu, Telangana and Andhra Pradesh."),
            B("Some states have improved. Delhi fell from 119.61 per cent in 2017 to 92.10 per cent in "
              "2025, and Himachal Pradesh from 86.37 to 38.50 per cent. The Minister of State for Jal "
              "Shakti gave these figures in a written reply to the Rajya Sabha in July 2026.", sm=True),
            H("red", "A stage above 100 per cent cannot continue. It means the aquifer is being mined, "
              "and wells have to go deeper over time.")], ratio="a32"),
    ]),

    S("Why it happens", "The incentives in the north-west all point towards pumping", [
        TC([P("amber", "Free or cheap power",
              "Where farm power is free or flat-rated, the cost of pumping one more hour is close to "
              "zero for the farmer. Ryan and Sudarshan show in Rajasthan that rationing hours keeps "
              "average use in check but misallocates water between farmers."),
            P("amber", "Assured prices for a thirsty crop",
              "Rice is the most irrigated crop, at about two-thirds coverage, and in the states with "
              "large procurement it is bought at MSP. A farmer comparing paddy with a less "
              "water-intensive crop that has no assured buyer has a strong reason to choose paddy.")],
           [P("cyan", "A common pool",
              "Groundwater under a village is shared. Water one farmer does not pump may be pumped by "
              "a neighbour, so restraint by one farmer brings little benefit to that farmer. This is "
              "the logic of the commons, and it is why advice to individual farmers to save water needs a collective rule behind it."),
            P("cyan", "Rules that are hard to enforce",
              "The Economic Survey notes that Uttar Pradesh's Ground Water Rules of 2020 strengthened "
              "regulation of extraction, and that by 2025 recharge had risen marginally while "
              "extraction intensity also increased."),
            H("green", "The Economic Survey's diversification proposal in section 3 is partly a "
              "groundwater policy.")]),
    ]),

    S("Programmes", "Irrigation policy now aims at efficiency as much as area", [
        TC([B("The Pradhan Mantri Krishi Sinchayee Yojana aims, in the Economic Survey's description, "
              "to coordinate irrigation investment at farm level, expand the area under assured "
              "irrigation, raise on-farm water efficiency, promote precision irrigation, recharge "
              "aquifers, and test the reuse of treated municipal wastewater in peri-urban farming."),
            B("Under its Per Drop More Crop component the government pays 55 per cent of the cost of "
              "drip and sprinkler systems for small and marginal farmers and 45 per cent for others.", sm=True)],
           [T(["State example in the Economic Survey", "What was done", "Reported result"],
              [["Telangana", "Kaleshwaram Lift Irrigation Project; Mission Kakatiya to rejuvenate tanks", "Cultivated area rose from 1.31 crore acres in 2014 to 2.2 crore acres by FY23"],
               ["Assam", "State Irrigation Plan (2022), new schemes and solar pumps", "Gross irrigated area 24.28% of agricultural land by 2024-25"],
               ["Uttar Pradesh", "Ground Water Rules (2020)", "Recharge up marginally; extraction intensity also up"]]),
            B("Source: " + ES + ", Box VI.1 and paragraph 6.21. These are the state governments' "
              "reported outcomes. None of them is an independent evaluation.", sm=True)]),
    ]),

    S("Drip and the rebound", "Water-saving technology can increase total water use", [
        TC([B("Drip irrigation delivers water to the roots and wastes less to evaporation and runoff. "
              "Per hectare, it uses less water for the same crop. The farmer, though, may use the "
              "water saved to irrigate more land or to switch to a thirstier, more profitable crop. "
              "Total extraction from the aquifer can then stay the same or rise."),
            B("This is the rebound problem. It is why water-saving subsidies work best alongside a "
              "limit on how much is extracted, such as a cap on hours, a metered connection, or a "
              "village agreement on the area under each crop.", sm=True),
            H("amber", "A programme that reports hectares under drip is reporting an input. Ask what "
              "happened to the water table and to the area irrigated.")],
           [T(["Indicator", "What it tells you", "What it misses"],
              [["Hectares under micro-irrigation", "Adoption of the technology", "Whether total pumping fell"],
               ["Water use per hectare", "Efficiency on the treated plot", "Expansion to new plots"],
               ["Depth to water table in monitoring wells", "The state of the aquifer", "Which farmers caused the change"],
               ["Stage of extraction for the block", "Balance of recharge and use", "Seasonal and local variation"]])]),
    ]),

    S("Practice", "Using groundwater data in programme design", [
        TC([BL(["Look up the category of the block you work in before promoting any crop, pump or "
                "irrigation scheme. A semi-critical block today may be over-exploited in five years.",
                "Ask whether a proposed livelihood depends on new borewells. In an over-exploited block "
                "it will compete with existing users for a falling resource.",
                "Pair any water-saving subsidy with a rule on total use, or report what happened to "
                "the area irrigated.",
                "In rain-fed blocks, treat surface storage, tanks and soil moisture conservation as the "
                "main irrigation strategy.",
                "Remember that the stage of extraction is a block average. Wells near a canal and "
                "wells at the tail end of a block can face very different conditions."], "cyan")],
           [P("green", "A note on solar pumps",
              "PM-KUSUM has installed 11.49 lakh off-grid solar pumps. In a safe block a solar pump "
              "can replace diesel and cut costs. In an over-exploited block it removes the last cost "
              "on pumping. Check the block category before promoting one."),
            B("For climate and water, see " + L("climate-essentials.html", "Climate Essentials 101") +
              " and " + L("env-justice.html", "Environmental Justice 101") + ".", sm=True)]),
    ]),
]


# ===================== SECTION 08: CROP INSURANCE AND PM-KISAN =====================
SEC8 = [
    DIV("08", "Eight", "Crop insurance and income support"),

    S("PMFBY design", "The farmer pays 2 per cent of the sum insured for kharif food crops", [
        TC([T(["Feature", "Pradhan Mantri Fasal Bima Yojana"],
              [["Launched", "18 February 2016, from kharif 2016"],
               ["Farmer's premium, maximum", "2% kharif foodgrains and oilseeds; 1.5% rabi; 5% commercial and horticultural crops"],
               ["Rest of the premium", "Centre and state 50:50; 90:10 in north-eastern and Himalayan states"],
               ["Yield losses", "Area-based: drought, dry spells, flood, cyclone, hail, pests and disease in a notified area"],
               ["Prevented sowing", "Claims up to 25% of the sum insured"],
               ["Post-harvest", "Crop drying in the field covered for up to 14 days against cyclone and unseasonal rain"],
               ["Localised calamity", "Farm-level claims for hail, landslide, inundation, cloudburst and natural fire"]]),
            B("Source: " + PMFBY + ".", sm=True)],
           [B("Most claims under PMFBY are settled on an area basis. Crop cutting experiments, and "
              "now remote sensing through the YES-TECH system with up to 50 per cent weight in some "
              "states, estimate the actual yield of each insurance unit, and claims for yield loss are "
              "calculated from that figure for everyone insured in the unit. A farmer whose own field "
              "failed in a unit that did well may receive nothing, unless the loss is one of the "
              "localised perils."),
            B("Loanee farmers, whose crop loans or KCCs are active, have the premium deducted by the "
              "bank. Non-loanee farmers enrol voluntarily. Tenants and sharecroppers can enrol with "
              "tenure agreements or sowing certificates as each state requires.", sm=True),
            H("cyan", "The Restructured Weather-Based Crop Insurance Scheme pays on weather readings "
              "at notified stations instead of yields, mostly for fruit, vegetables and plantations.")]),
    ]),

    S("Scale", "Ten years, 92 crore applications and &#8377;2 lakh crore in claims", [
        TC([ST([C("92.46 crore", "farmer applications insured, kharif 2016 to rabi 2025-26", "cyan", PMFBY),
                C("&#8377;2.06 lakh crore", "claims paid on over 26.33 crore applications", "green", PMFBY),
                C("4.19 crore", "farmers insured in 2024-25, on 6.2 crore hectares", "amber", ES),
                C("&#8377;12,200 crore", "Central allocation, Budget 2026-27", "indigo", BAG)], cols=2),
            B("Kharif 2025 insured 229.77 lakh farmers on 269.38 lakh hectares. By 27 August 2026, "
              "kharif 2026 enrolment had reached 241.38 lakh farmers.", sm=True)],
           [B("An application is one crop on one plot in one season. A farmer who insures paddy and "
              "wheat on two plots files four applications in a year. The 92.46 crore applications are "
              "therefore far more than the number of farmers. Quote them as applications."),
            B("Claims paid are about &#8377;2.06 lakh crore over ten years. Farmers pay only a small "
              "part of the premium. A full account of the scheme compares claims with the "
              "total premium paid by farmers and governments together for the same seasons.", sm=True),
            H("amber", "Tenants and sharecroppers enrolled since 2018 number more than 1.44 crore, "
              "according to the PIB backgrounder.")]),
    ]),

    S("States in and out", "States have left the scheme and come back", [
        TC([B("Insurance is voluntary for states, which pay half the subsidised premium. Several large "
              "agricultural states opted out of PMFBY or launched their own non-insurance relief schemes. The government's "
              "backgrounder of August 2026 lists Andhra Pradesh rejoining from kharif 2022, Jharkhand "
              "from kharif 2024 and West Bengal from kharif 2026. Bihar has decided to return from rabi "
              "2026-27. PMFBY is being implemented by 25 states and union territories in kharif 2026."),
            B("Enrolment can swing on a single state decision. Andhra Pradesh and Maharashtra paid the "
              "whole farmer premium in 2023 and 2024, which led to very high enrolment. When they stopped "
              "in 2025, enrolment fell sharply.", sm=True)],
           [T(["Farmers enrolled", "Kharif 2024", "Kharif 2025", "Kharif 2026 (to 28 Aug)"],
              [["Andhra Pradesh", "31.92 lakh", "7.43 lakh", "16.22 lakh"],
               ["Maharashtra", "76.59 lakh", "45.99 lakh", "42.55 lakh"],
               ["Uttar Pradesh", "15.48 lakh", "20.84 lakh", "not reported"],
               ["Rajasthan", "30.59 lakh", "36.45 lakh", "not reported"]]),
            B("Source: " + PMFBY + ".", sm=True),
            H("cyan", "When you read an enrolment trend, check whether a state changed who pays the "
              "premium.")]),
    ]),

    S("Evidence on insurance demand", "Farmers say rainfall is their biggest risk and still buy little insurance", [
        TC([B("Shawn Cole, Xavier Gin&eacute;, Jeremy Tobacman, Petia Topalova, Robert Townsend and "
              "James Vickery ran randomised experiments on rainfall index insurance in rural Andhra "
              "Pradesh and Gujarat (American Economic Journal: Applied Economics, 2013, 5(1): 104-35)."),
            B("Only 5 to 10 per cent of households bought the insurance, even though they "
              "overwhelmingly named rainfall variability as their most important risk. Demand was "
              "sensitive to price, with an estimated price elasticity between -0.66 and -0.88. Price "
              "was not the whole story. The authors point to lack of trust, liquidity constraints and "
              "limited salience, and argue that even contracts as generous as those in the United "
              "States would see limited take-up without addressing these.", sm=True)],
           [P("cyan", "What PMFBY's design does about these frictions",
              "A heavily subsidised premium answers price. Automatic enrolment of loanee farmers "
              "answers liquidity and salience for borrowers, because the premium is deducted from the "
              "loan. Trust depends on whether claims are paid on time and are seen to match losses."),
            P("amber", "What remains",
              "Area-based settlement means a farmer whose plot failed in a unit that did well may not "
              "be paid, and that experience shapes trust in the next season. The Digiclaim module, used since kharif 2022, pays claims through the Public Financial "
              "Management System and has paid over &#8377;55,000 crore.")]),
    ]),

    S("PM-KISAN", "&#8377;6,000 a year to every landholding farmer family", [
        TC([B("PM-KISAN was launched on 24 February 2019. Every eligible farmer family with cultivable "
              "land receives &#8377;6,000 a year in three instalments of &#8377;2,000, paid by direct "
              "benefit transfer into an Aadhaar-seeded bank account. Land records must be seeded on the "
              "PM-KISAN portal and e-KYC completed."),
            B("Income tax payers, government and public sector employees and holders of "
              "constitutional posts are excluded. As of December 2025, &#8377;416.75 crore "
              "had been recovered from ineligible beneficiaries. The 23rd instalment was released on "
              "20 June 2026 in Hooghly, West Bengal.", sm=True)],
           [ST([C("9.44 crore", "farmers paid in the 23rd instalment, of whom 2.18 crore women", "cyan", KISAN),
                C("&#8377;18,880 crore", "released in the 23rd instalment", "green", KISAN),
                C("&#8377;4.46 lakh crore", "paid since 2019 across 23 instalments", "amber", KISAN),
                C("&#8377;63,500 crore", "PM-KISAN, Budget Estimate 2026-27", "indigo", BAG)], cols=2),
            H("amber", "The PIB backgrounder gives the 2026-27 allocation as &#8377;60,000 crore. Budget "
              "at a Glance shows &#8377;63,500 crore. Quote the budget document and note the difference.")]),
    ]),

    S("Who PM-KISAN reaches", "A flat transfer to landholders leaves out those who work land they do not own", [
        TC([B("PM-KISAN is defined for landholding farmer families. A tenant who cultivates leased "
              "land, a sharecropper, and an agricultural labourer with no land are outside it by "
              "design, although they carry the same farming risks as owners."),
            B("The transfer is the same for a family with 0.3 hectares and for one with 10 hectares, "
              "so per hectare it is far larger for small holdings. Measured against income, "
              "&#8377;6,000 a year is &#8377;500 a month, about 5 per cent of the average agricultural "
              "household's income of &#8377;10,218 in 2018-19.", sm=True),
            H("cyan", "Because it is paid per family and needs land records, the quality of state land "
              "records decides who receives it. A family whose land is still recorded in a deceased "
              "parent's name can be left out until the record is updated.")],
           [T(["Group", "In PM-KISAN?", "Why"],
              [["Owner-cultivator with records", "Yes", "Landholding family with seeded records"],
               ["Owner whose records are not updated", "May be left out", "Land not recorded in the family's name"],
               ["Tenant or sharecropper", "No", "Not a landholder"],
               ["Landless agricultural labourer", "No", "No land"],
               ["Landowner who pays income tax", "No", "Excluded category"],
               ["Woman cultivator on family land", "Only if land is in her name", "Paid to the landholding family"]])]),
    ]),

    S("Evidence on PM-KISAN", "Early studies suggest it eased cash shortages for the most constrained farmers", [
        TC([P("cyan", "IFPRI Discussion Paper 1907 (January 2020)",
              "Deepak Varshney, Pramod Kumar Joshi, Devesh Roy and Anjani Kumar surveyed 1,406 farmers "
              "in Uttar Pradesh. PM-KISAN had reached one-third of farmers in the first three months. "
              "They found no selection bias by social, economic or agricultural characteristics. The "
              "scheme helped most those more dependent on agriculture and with poor access to credit, "
              "and it strengthened the effect of Krishi Vigyan Kendras on adoption of modern varieties. "
              "They use a triple difference with matching."),
            B("Source: " + A("https://cgspace.cgiar.org/server/api/core/bitstreams/e1860a45-121f-44ba-a67e-8eebf09a884a/content", "IFPRI DP 01907") + ".", sm=True)],
           [P("amber", "A ministry-sponsored study (2022)",
              "The Agro-Economic Research Centre at the University of Allahabad, sponsored by the "
              "Ministry of Agriculture, compared beneficiaries and non-beneficiaries in Uttar Pradesh. "
              "As reported by PIB, paddy yields were 3.08 per cent and wheat yields 1.93 per cent "
              "higher on beneficiary farms, and household farm income 9.85 per cent higher."),
            H("red", "A comparison of beneficiaries with non-beneficiaries is not a causal estimate. "
              "Families who registered may differ from those who did not in land, information and "
              "contacts. Treat such figures as associations until a design rules out selection.")]),
    ]),
]


# ===================== SECTION 09: MARKETS, EXTENSION, FPOs =====================
SEC9 = [
    DIV("09", "Nine", "Markets, extension and farmer producer organisations"),

    S("Selling the crop", "About half of households growing rice or wheat sell any of it", [
        TC([T(["Crop (agricultural households producing it)", "Producing (% of agricultural households)", "Of producers, % reporting a sale"],
              [["Paddy, July to December 2018", "53.2", "52.6"],
               ["Wheat, January to June 2019", "41.2", "50.8"],
               ["Maize, July to December 2018", "11.3", "47.1"],
               ["Soybean, July to December 2018", "6.0", "94.4"],
               ["Cotton, July to December 2018", "7.2", "94.6"],
               ["Sugarcane, July to December 2018", "3.5", "95.9"],
               ["Potato, January to June 2019", "5.3", "55.0"]]),
            B("Source: " + SAS + ", Table 5.", sm=True)],
           [B("Around half the households that grow paddy or wheat report no sale, so most of "
              "that grain stays in the household. Almost everyone who grows soybean, cotton or sugarcane sells, "
              "because these are cash crops. A market reform therefore reaches cash-crop growers directly and touches subsistence grain growers only at the margin."),
            B("Farmers sell in regulated APMC mandis, to traders and commission agents in the "
              "village, to processors and mills, to procurement agencies and to FPOs. "
              "Each state's APMC law decides what is regulated and what fee applies. The Economic "
              "Survey 2025-26 lists inadequate marketing and storage infrastructure among the main "
              "reasons for low productivity.", sm=True),
            H("cyan", "Before designing a market intervention, find out what share of the crop is sold "
              "at all, and when.")]),
    ]),

    S("e-NAM", "An electronic market across 1,656 mandis", [
        TC([B("The National Agriculture Market (e-NAM) was launched in April 2016 as a pan-India "
              "electronic trading platform that links existing APMC mandis. Each mandi that joins "
              "receives &#8377;75 lakh for hardware, software, quality assaying and related "
              "infrastructure. In principle a buyer in another district or state can bid for a lot "
              "that has been assayed and listed online."),
            B("Trade between mandis or states needs grading that distant buyers trust, payment "
              "that clears across states, and transport to move the produce. Ask how much of a "
              "mandi's e-NAM trade is with buyers from outside it.", sm=True)],
           [ST([C("1,656", "mandis integrated with e-NAM, June 2026", "cyan", PIBAG),
                C("1.89 crore", "farmers registered on e-NAM", "green", PIBAG),
                C("2.78 lakh", "traders registered on e-NAM", "amber", PIBAG),
                C("4,698", "FPOs on e-NAM, 31 December 2025", "indigo", ES)], cols=2),
            H("amber", "Registration is not trade. Ask for the volume and value traded, and the share "
              "traded between mandis or states.")]),
    ]),

    S("Information and prices", "When farmers can see prices and choose a buyer, prices rise", [
        TC([P("cyan", "Goyal (2010), soybean in Madhya Pradesh",
              "From October 2000 a private buyer set up internet kiosks and warehouses that gave "
              "soybean growers wholesale price information and a second way to sell. Aparajita Goyal "
              "used a new market-level dataset and found a significant rise in soybean mandi prices "
              "after the kiosks arrived, and a clear increase in soybean acreage. She reads this as "
              "evidence that rural markets worked better once farmers had information and an outside "
              "option (American Economic Journal: Applied Economics, 2010, 2(3): 22-45)."),
            B("This is the kind of evidence cited for opening agricultural trade. It came from a setting where a large private buyer entered and competed with the mandi.", sm=True)],
           [T(["What raised prices in Goyal's study", "What a practitioner should ask locally"],
              [["Price information at the village", "Do farmers see mandi prices before they sell?"],
               ["A second buyer at the farm gate", "Is there more than one buyer, or one trader who also lends?"],
               ["Warehouses near the village", "Can farmers store and wait, or must they sell at harvest?"],
               ["Transparent weighing and grading", "Who weighs, and who decides the grade?"]]),
            H("green", "Credit and sale are often linked. A farmer who borrowed from a trader before "
              "sowing may be obliged to sell to him.")]),
    ]),

    S("Extension", "Public extension reaches few farmers, and input dealers fill the gap", [
        TC([B("Extension is the advice that helps farmers use new seed, fertiliser, water and "
              "practices well. The Economic Survey 2025-26 says Indian extension, delivered by public "
              "agencies, Krishi Vigyan Kendras, agricultural universities, private firms and digital "
              "platforms, faces limited reach, staff shortages and fragmented delivery."),
            B("The government's own programmes recognise that farmers take advice from the shops "
              "that sell them inputs. The DAESI programme trains input dealers in a 48-week diploma, and had reached "
              "1,07,659 dealers by October 2025. Kisan Call Centres answered 30.65 lakh calls in "
              "2024-25 in 22 languages. BharatVistaar, an AI advisory platform with a "
              "&#8377;150 crore allocation in 2026-27, had served over 3 lakh farmers by July 2026.", sm=True)],
           [ST([C("731", "Krishi Vigyan Kendras set up by ICAR, as of June 2026", "cyan", PIBAG),
                C("58.02 lakh", "farmers trained by KVKs, 2021-22 to 2023-24", "green", PIBAG),
                C("39.04 lakh", "farmers reached through ATMA in 2024-25", "amber", ES),
                C("1,07,659", "input dealers trained under DAESI, October 2025", "indigo", ES)], cols=2),
            H("amber", "Compare 58 lakh farmers trained in three years with over 9 crore farmer "
              "families paid by PM-KISAN.")]),
    ]),

    S("Evidence on advice", "A phone hotline changed what farmers did, and the yield gains were unclear", [
        TC([B("Shawn Cole and A. Nilesh Fernando evaluated Avaaj Otalo, a phone service through which "
              "farmers could call agronomists with questions, among 1,200 farmers in 40 villages in "
              "Ahmedabad district, Gujarat (Economic Journal, 2021)."),
            BL(["More than half of the farmers offered the service called it in the first seven months.",
                "Treated farmers relied less on other farmers and on input sellers for advice.",
                "They adopted more effective pesticides and cut spending on less effective and "
                "hazardous ones.",
                "They sowed more cumin, a lucrative but risky crop.",
                "The accepted working paper version reports no systematic evidence of gains in yields "
                "or profits."], "cyan")],
           [P("green", "What this teaches",
              "Advice that farmers can ask for, on their own crop and their own pest, changes "
              "behaviour. Changing input choices is a real outcome, especially when it replaces "
              "hazardous pesticides. Yield and profit gains are harder to detect in a single season "
              "with weather noise, and a study powered for adoption may not be powered for yields."),
            P("amber", "Cost",
              "Farmers' willingness to pay was on average below the per-farmer cost of running the "
              "service in the study, but the authors expect it to exceed the cost at scale.")]),
    ]),

    S("FPOs", "The 10,000 FPO target has been met on paper", [
        TC([B("A Farmer Producer Organisation is a company or cooperative owned by its farmer members. "
              "It can buy inputs in bulk, hire machines, aggregate produce, grade and store it, and "
              "sell in larger lots to buyers who would not deal with a single marginal farmer."),
            B("The central scheme to form and promote 10,000 FPOs was launched in 2020 with a budget "
              "of &#8377;6,860 crore through 2027-28, according to the Economic Survey 2025-26. By 31 "
              "December 2025, 10,000 FPOs had been registered. Primary agricultural credit societies "
              "are being computerised at the same time, with 79,630 PACS sanctioned and 63,707 on the "
              "national ERP software by August 2026.", sm=True)],
           [P("amber", "Registration is the first step",
              "An FPO registered under the scheme has a legal form, a board and a support agency. "
              "Whether it trades at scale, pays dividends, keeps its members and survives after the "
              "support period ends is a separate question. Of the 10,000 registered, 4,698 were on "
              "e-NAM by December 2025."),
            T(["Stage", "Indicator worth tracking"],
              [["Formation", "Members, share capital paid up, women on the board"],
               ["Business", "Turnover, number of members selling through the FPO"],
               ["Viability", "Profit after support ends, working capital, credit access"],
               ["Benefit", "Price members receive compared with non-members"]])]),
    ]),

    S("What makes an FPO work", "Practitioner checklist for supporting a producer organisation", [
        TC([BL(["Start from a business the members already do, such as selling one crop, and do it "
                "well before adding more.",
                "Working capital decides whether an FPO can pay members on delivery. Without it, "
                "members sell to the trader who pays cash.",
                "Members who borrowed from a trader before sowing may not be free to sell to the FPO. Crop credit "
                "and marketing need to be planned together.",
                "Grading and weighing that members trust are the foundation of aggregation.",
                "Governance decides trust. Agree who sits on the board, how the CEO is paid, and how "
                "accounts are shared with members.",
                "Plan for the end of promotional support from the first year."], "cyan")],
           [T(["Common failure", "Early warning sign"],
              [["Formed to meet a target", "Members cannot say what the FPO does for them"],
               ["Captured by a few larger farmers", "Board and benefits concentrated in one group or village"],
               ["No working capital", "Members sell to traders even after the FPO opens a collection centre"],
               ["Dependence on a single buyer", "Prices dictated by one processor or retailer"],
               ["Exclusion of tenants and women", "Membership tied to land in the member's name"]]),
            B("For cooperatives and collective enterprise, see " + L("community-dev.html", "Community Development 101") +
              " and " + L("wee-studies.html", "Women's Economic Empowerment 101") + ".", sm=True)]),
    ]),
]


# ===================== SECTION 10: LAND, TENANCY, WOMEN =====================
SEC10 = [
    DIV("10", "Ten", "Land records, tenancy and women in agriculture"),

    S("Land records", "Every scheme in this course depends on knowing who cultivates which plot", [
        TC([B("PM-KISAN needs land records seeded on its portal. The Price Support Scheme buys only "
              "from registered farmers with valid land records. PMFBY validates insured area against "
              "state land records, and about 85 per cent of insured area in ten states is now checked "
              "this way. A per-acre fertiliser transfer would need the same. When land records are out "
              "of date, wrong or missing, the error passes into every scheme built on them."),
            B("The Digital Agriculture Mission, approved in September 2024, is building AgriStack, a "
              "registry of farmers linked to their plots, alongside a Krishi Decision Support System "
              "and soil maps.", sm=True)],
           [ST([C("10.31 crore", "Farmer IDs created under the Digital Agriculture Mission, Aug 2026", "cyan", PIBAG),
                C("31.3 crore", "plots covered by the Digital Crop Survey in rabi 2025-26, in 648 districts", "green", PIBAG),
                C("81 lakh", "land parcels resurveyed in Andhra Pradesh's drone-based resurvey, 6,901 villages", "amber", ES),
                C("86,000", "boundary disputes resolved in that resurvey", "indigo", ES)], cols=2),
            H("amber", "A digital registry is as accurate as the record it digitises. Ask how tenants, "
              "joint holders and women co-owners are recorded.")]),
    ]),

    S("Tenancy", "Tenants farm land that the records say belongs to someone else", [
        TC([TERM("Fixed-rent tenancy", "The tenant pays the owner an agreed amount in cash or grain for "
                 "the season, and keeps the rest of the crop and the risk."),
            TERM("Sharecropping", "The tenant gives the owner a share of the harvest. Owner and tenant "
                 "share the risk, and sometimes the input costs."),
            TERM("Informal tenancy", "An oral agreement with no written lease, which leaves the tenant with "
                 "no document to show a scheme, an insurer or a bank.")],
           [B("Tenancy is governed by state law under Entry 18 of the State List, which covers the "
              "relation of landlord and tenant. The Agriculture Census counts land leased in as part "
              "of an operational holding, but the schemes in this course pay according to recorded "
              "ownership, so a tenant who appears in the census as an operator is often invisible to "
              "the schemes."),
            B("The Economic Survey 2025-26 raises this problem itself in its proposal for per-acre "
              "fertiliser transfers, noting that a portion of the land is cultivated by renters and "
              "suggesting that pilots include tenancy-heavy districts. PMFBY has enrolled more than "
              "1.44 crore tenant and sharecropper farmers since 2018, which shows that including them "
              "is possible when a scheme allows other proof of cultivation.", sm=True),
            H("cyan", "When a programme says it covers farmers, ask whether it means owners or "
              "cultivators.")]),
    ]),

    S("Eligibility by tenure", "The same tenant is in some schemes and out of others", [
        T(["Scheme", "Owner-cultivator", "Tenant or sharecropper", "Landless labourer", "Basis"],
          [["PM-KISAN", "Yes", "No", "No", "Landholding farmer families with seeded land records"],
           ["PMFBY", "Yes", "Yes, with tenure agreement or sowing certificate as the state requires", "No crop to insure", "Insurable interest in the crop"],
           ["MSP procurement of rice and wheat", "Yes", "Depends on state registration rules", "No crop to sell", "Sale at a purchase centre"],
           ["Price Support Scheme (pulses, oilseeds)", "Yes", "Only with valid land records", "No", "Pre-registered farmers with land records"],
           ["NFSA ration", "If eligible household", "If eligible household", "If eligible household", "Household identification, not land"],
           ["VB G RAM G rural employment guarantee", "If they seek work", "If they seek work", "Yes", "Rural household, 125 days a year"]]),
        TC([B("Sources: " + KISAN + "; " + PMFBY + "; " + PIBMSP + "; " + NFSA + "; " + ES13 + ".", sm=True)],
           [B("The schemes least tied to land, the ration and the employment guarantee, are the ones "
              "that reach the landless. Under the VB G RAM G Act, states may notify up to 60 days in "
              "peak sowing and harvesting seasons when public works pause, so that farm labour is "
              "available.", sm=True)]),
    ], compact=True),

    S("Women's work", "Three in four rural women workers are in agriculture", [
        TC([BAR("chWomen", "Share of workers in agriculture by sex and area, PLFS 2023-24 (% of workers, usual status)", PLFS24,
                ["Rural men", "Rural women", "Urban men", "Urban women", "All men", "All women"],
                [DS("Share in agriculture", [49.4, 76.9, 4.8, 12.3, 36.3, 64.4], GREEN)], ytitle="per cent of workers")],
           [B("In 2023-24, 76.9 per cent of rural women workers were in agriculture, against 49.4 per "
              "cent of rural men. Across India the share was 64.4 per cent for women and 36.3 per cent "
              "for men. Rural men work in construction (17.7 per cent) and trade, hotels and "
              "restaurants (10.9 per cent) far more than rural women (3.9 per cent in each)."),
            B("The Economic Survey 2025-26 reports from PLFS for July to September 2025 that, in rural "
              "areas, 37.5 per cent of women workers are own-account workers or employers and 34.2 "
              "per cent are helpers in household enterprises, which includes unpaid work on the "
              "family farm. Only 10.8 per cent are in regular wage jobs.", sm=True),
            H("amber", "A woman who works every day on her family's farm and receives no wage is a "
              "helper in a household enterprise in the survey.")], ratio="a32"),
    ]),

    S("Women as landholders", "Women do much of the farm work and hold a small share of the land", [
        TC([ST([C("13.96%", "of operational holders were women in 2015-16, up from 12.79% in 2010-11", "cyan", AGC),
                C("11.72%", "of operated area was in women's holdings, up from 10.36%", "amber", AGC),
                C("2.18 crore", "women among the 9.44 crore paid in the 23rd PM-KISAN instalment", "green", KISAN),
                C("64.4%", "of all women workers were in agriculture, 2023-24", "indigo", PLFS24)], cols=2)],
           [B("Women make up a large share of the agricultural workforce and a small share of those who "
              "operate holdings. Schemes that pay the recorded landholder therefore pay men in most "
              "families. PM-KISAN's women recipients, about 23 per cent of the 23rd instalment, are "
              "women in whose name the land stands."),
            B("Credit and FPO membership often follow the land record too. A woman "
              "cultivating her husband's land, or land she inherited but has not had recorded, works "
              "the land without the documents that schemes ask for.", sm=True),
            B("The NFSA takes the opposite approach for the ration card, naming the eldest woman as "
              "head of household under section 13. Recording land jointly in the names of both spouses "
              "would apply the same idea to land.", sm=True)]),
    ]),

    S("Time", "Women in rural India carry farm work and care work at once", [
        TC([ST([C("41%", "of women aged 15-59 did caregiving for household members on the survey day", "red", "Time Use Survey 2024, in Economic Survey 2025-26, Box XII.1"),
                C("21.4%", "of men aged 15-59 did", "cyan", "Same"),
                C("363 min", "a day women spent on unpaid activities, against 123 minutes for men", "amber", "Same"),
                C("25%", "of women aged 15-59 did employment and related activities, up from 21.8% in 2019", "green", "Same")], cols=2)],
           [B("The Time Use Survey of 2024 measures what people did in each half-hour of a day. Women "
              "spent about 140 minutes a day on care among those who did any, against 74 minutes for "
              "men, and 363 minutes a day on unpaid activities, against about 123 for men."),
            B("For agricultural programmes this has practical consequences. Training scheduled at "
              "midday, far from the village, or over several days is likely to reach fewer women. A new "
              "practice that adds labour to tasks women already do, such as weeding or post-harvest "
              "work, may raise yields and lengthen women's working day at once.", sm=True),
            H("cyan", "Ask who does each task in the crop cycle before deciding who should be trained "
              "and who should be paid.")]),
    ]),

    S("Practice", "Designing agricultural programmes that reach women farmers", [
        T(["Design question", "What to do", "Why"],
          [["Who is the farmer on your list?", "Register the person who cultivates as well as the recorded owner", "Most women cultivators do not hold the land record"],
           ["Who controls the money?", "Pay transfers into women's own accounts where they manage the activity", "Payment to the landholder goes to men in most families"],
           ["When and where is training held?", "In the village, at times women choose, with childcare", "Care work takes over two hours a day for women who do it"],
           ["Which tasks does the new practice change?", "Map tasks by sex before and after adoption", "A yield gain can come from more unpaid female labour"],
           ["Who sits on the FPO board?", "Reserve seats and allow membership without land title", "Membership tied to land excludes most women"],
           ["Which crops and animals?", "Include livestock, dairy and kitchen gardens", "These are often women's activities and income"]]),
        TC([B("These are design principles drawn from the evidence in this section. For gender analysis "
              "methods, see " + L("gender-dev.html", "Gender and Development 101") + ".", sm=True)],
           [B("For the care economy and time use, see " + L("care-economy-101.html", "Care Economy 101") + ".", sm=True)]),
    ], compact=True),
]


# ===================== SECTION 11: CLIMATE AND NUTRITION =====================
SEC11 = [
    DIV("11", "Eleven", "Climate risk, nutrition and food systems"),

    S("Projected yield losses", "Without adaptation, rain-fed rice could lose a fifth of its yield by 2050", [
        TC([BAR("chClimate", "Projected change in yield without adaptation (%)", NICRA,
                ["Rain-fed rice", "Irrigated rice", "Wheat"],
                [DS("2050", [-20, -3.5, -19.3], AMBER), DS("2080", [-47, -5, -40], RED)],
                legend=True, ytitle="per cent change in yield")],
           [B("ICAR's network project National Innovations in Climate Resilient Agriculture (NICRA) "
              "ran computer simulation models for major crops. In a written reply to the Lok Sabha on "
              "10 December 2024, the Minister of State for Agriculture said that in the absence of "
              "adaptation, climate change is likely to reduce rain-fed rice yields by 20 per cent in "
              "2050 and 47 per cent in 2080, irrigated rice by 3.5 and 5 per cent, wheat by 19.3 and "
              "40 per cent, and kharif maize by 10 to 19 per cent in 2050 and more than 20 per cent in "
              "2080."),
            B("These are model projections under stated scenarios. Their value lies in the "
              "comparison. Irrigation buffers rice against warming, and wheat, a winter crop "
              "sensitive to heat at grain filling, is among the most exposed.", sm=True),
            H("amber", "The farmers with the least irrigation face the largest projected losses.")], ratio="a32"),
    ]),

    S("Weather shocks now", "Heat, unseasonal rain and El Ni&ntilde;o already cut yields and quality", [
        TC([P("red", "Grain quality",
              "The same Lok Sabha reply notes preliminary findings that elevated carbon dioxide and "
              "temperature reduced iron, zinc and protein in certain maize genotypes, that elevated "
              "carbon dioxide altered rice grain quality, and that heat stress in wheat caused "
              "shrivelled grains with less starch and protein, while excess rain at grain filling "
              "caused lodging and discoloured grain."),
            P("amber", "Yields below the national average",
              "A CACP report cited in the Economic Survey 2025-26 found that several major "
              "rice-producing states, including West Bengal, Uttar Pradesh, Telangana, Odisha, Andhra "
              "Pradesh and Tamil Nadu, had per-hectare yields below the national average, and named "
              "unseasonal rain, heat stress and dry spells at critical crop stages as the main causes.")],
           [P("cyan", "El Ni&ntilde;o and pulses",
              "A NITI Aayog report cited in the Economic Survey found that in 15 of the 27 El Ni&ntilde;o "
              "years between 1951 and 2024, pulse acreage fell by 2 to 9 per cent, production by 6 to 30 "
              "per cent and yields by 5 to 25 per cent year on year. During La Ni&ntilde;a years "
              "acreage, production and productivity rose. Pulses are mostly rain-fed, with about 26 per "
              "cent of their area irrigated."),
            H("green", "Climate risk shows up first in rain-fed crops and in the quality of food, as "
              "well as in the quantity of rice and wheat.")]),
    ]),

    S("Evidence on adaptation", "A flood-tolerant rice variety paid off through the investments it encouraged", [
        TC([B("Kyle Emerick, Alain de Janvry, Elisabeth Sadoulet and Manzoor Dar ran a randomised trial "
              "in 128 villages in Odisha with Swarna-Sub1, a version of the popular Swarna rice variety "
              "carrying a gene that lets it survive submergence. In normal years it yields the same as "
              "Swarna. In a flood it loses much less (American Economic Review, 2016, 106(6): 1537-61)."),
            B("Farmers given the new seed did more than plant it. They adopted a more labour-intensive "
              "planting method, cultivated more area, used more fertiliser and took more credit. A "
              "large share of the expected gain came from these crowded-in investments, because "
              "lowering the risk of total loss made it worth investing in the crop.", sm=True)],
           [T(["Lesson", "Implication for programme design"],
              [["Risk shapes investment", "Reducing the worst outcome can raise effort and inputs in every year"],
               ["Seed is a delivery problem", "A proven variety helps only if farmers can get certified seed on time"],
               ["Benefits spill into other decisions", "Measure area, inputs and credit, not only yield"],
               ["Insurance and technology complement each other", "A stress-tolerant seed lowers the losses insurance must cover"]]),
            B("See also " + L("impact-eval.html", "Impact Evaluation 101") + " for how such trials are designed.", sm=True)]),
    ]),

    S("Plenty and malnutrition", "Record harvests, and three in ten young children stunted", [
        TC([ST([C("376.56 MT", "foodgrain production, 2025-26 (third advance estimates)", "green", PIBAG),
                C("248 MT", "milk production, 2024-25, up from 146.31 MT in 2014-15", "cyan", PIBAG),
                C("377.78 MT", "horticulture production, 2025-26 (second advance estimates)", "amber", PIBAG)], cols=3),
            ST([C("29.3%", "of children under five stunted, NFHS-6 (2023-24), down from 35.5% in NFHS-5", "red", "IIPS, NFHS-6 India fact sheet, indicator 69"),
                C("31.8%", "of children under five underweight, NFHS-6", "red", "Same, indicator 72"),
                C("15.3%", "of children 6-23 months receiving an adequate diet, NFHS-6", "indigo", "Same, indicator 68")], cols=3)],
           [B("India produces more grain, milk, fruit and vegetables than ever. Yet the NFHS-6 fact "
              "sheet, published by IIPS in May 2026, finds about three "
              "in ten young children stunted, and fewer than one in six children aged 6 to 23 months receiving an adequate diet."),
            B("The gap between production and nutrition is about access, prices, diets, care, water "
              "and sanitation, and disease. Agriculture affects all the food-related parts of that "
              "chain, from what is grown and what it costs to what is in it and the time and income "
              "of the women who grow it.", sm=True),
            H("amber", "Stunting fell by about six percentage points between NFHS-5 and NFHS-6, from 35.5% to 29.3%. "
              "Wasting barely moved, from 19.3% to 19.0%.")]),
    ]),

    S("Food systems", "Farm policy decides what is cheap to grow and cheap to eat", [
        T(["Policy", "Effect on what is grown", "Effect on diets"],
          [["MSP procurement concentrated on rice and wheat", "Rice and wheat are the safe choice where procurement works", "The PDS distributes cereals; protein and micronutrients come from the market"],
           ["Urea subsidy", "Makes nitrogen cheap relative to other nutrients", "No direct effect on diets"],
           ["Irrigation concentrated on rice", "About 67% of rice is irrigated, under 15% of millets", "Millets and pulses stay exposed to rainfall shocks and price swings"],
           ["Imports of edible oils and pulses", "Domestic oilseed and pulse growers compete with imports", "Prices of protein and fat depend on world markets"],
           ["Millets in the PDS and school meals", "Creates assured demand for millets in states that buy them", "Adds micronutrient-rich grains to the ration"]]),
        TC([B("The Economic Survey 2025-26 argues for diversification out of rice and wheat into "
              "pulses, oilseeds and maize, partly to reduce import dependence and partly for "
              "nutrition. A food systems view asks the same question from the plate back to the field.", sm=True)],
           [B("Rows in this table summarise relationships discussed elsewhere in this course. The last "
              "column describes likely effects and should be checked against local evidence.", sm=True)]),
    ], compact=True),

    S("Natural and organic farming", "Promoted widely, still on a small fraction of the land", [
        TC([ST([C("10.32 lakh ha", "in 18,893 natural farming clusters formed in 2025-26, involving 20.93 lakh farmers", "green", PIBAG),
                C("14.43 lakh", "farmers certified under the Natural Farming Certification System", "cyan", PIBAG),
                C("18.93 lakh ha", "covered by the Paramparagat Krishi Vikas Yojana since inception", "amber", PIBAG),
                C("157.82 m ha", "total operated area, Agriculture Census 2015-16", "indigo", AGC)], cols=2)],
           [B("The National Mission on Natural Farming organises farmers into clusters to practise "
              "natural farming. The 10.32 lakh hectares "
              "of clusters formed in 2025-26 are about 0.65 per cent of the 157.82 million hectares "
              "operated in 2015-16."),
            B("The Economic Survey 2025-26 says plainly that organic and natural farming still cover a "
              "small fraction of cultivated land, and that limited quality inputs, uneven adoption and "
              "gaps in extension constrain scaling. Yield and income effects of natural farming at "
              "scale remain a question for careful evaluation.", sm=True),
            H("cyan", "Compare the area under a promoted practice with the total, and ask whether "
              "farmers who were counted are still practising it a season later.")]),
    ]),

    S("Practice", "Building climate risk into an agricultural programme", [
        T(["Step", "Question", "Source of evidence"],
          [["1. Exposure", "Is the area rain-fed? What share of its main crops is irrigated?", "District irrigation statistics; Economic Survey crop coverage"],
           ["2. Water", "Is the block safe, semi-critical, critical or over-exploited?", "Dynamic Ground Water Resource Assessment"],
           ["3. Hazards", "Which shocks recur: drought, flood, heat at grain filling, unseasonal rain?", "IMD records; local crop loss history"],
           ["4. Varieties", "Are stress-tolerant varieties available, and is certified seed reachable on time?", "State seed corporations; KVKs"],
           ["5. Insurance", "Is the crop notified under PMFBY or the weather-based scheme in this unit?", "National Crop Insurance Portal"],
           ["6. Diversification", "Is there a buyer for the alternative crop at a fair price?", "Mandi and procurement data; FPOs"],
           ["7. Nutrition", "Will the change raise or lower the diversity of food the household eats?", "Household diet surveys; NFHS district fact sheets"]]),
        TC([B("Much of climate adaptation in farming is about reducing the worst outcome. The Swarna-Sub1 "
              "trial shows that lowering downside risk can change how much farmers invest in every "
              "season.", sm=True)],
           [B("For climate science and policy, see " + L("climate-essentials.html", "Climate Essentials 101") + ".", sm=True)]),
    ], compact=True),
]


# ===================== SECTION 12: EVIDENCE AND PRACTICE =====================
SEC12 = [
    DIV("12", "Twelve", "What evaluations have found, and sources"),

    S("Evidence map", "Studies cited in this course, and what each one found", [
        T(["Study", "Setting", "Design", "Main finding"],
          [["Goyal (2010), AEJ: Applied", "Soybean, Madhya Pradesh", "Market-level panel around kiosk entry", "Mandi prices and soybean area rose after a private buyer's kiosks arrived"],
           ["Cole et al. (2013), AEJ: Applied", "Rainfall insurance, Andhra Pradesh and Gujarat", "Randomised price and marketing", "5-10% take-up; price elasticity -0.66 to -0.88; trust and liquidity matter"],
           ["Dr&egrave;ze and Khera (2015), EPW", "PDS, all India and states", "Offtake against survey purchases", "Leakage fell from 54% to 42% (NSS) between 2004-05 and 2011-12, fastest in reforming states"],
           ["Emerick et al. (2016), AER", "Flood-tolerant rice, Odisha", "Randomised trial, 128 villages", "Lower downside risk raised planting effort, area, fertiliser and credit"],
           ["Varshney et al. (2020), IFPRI DP 1907", "PM-KISAN, Uttar Pradesh", "Triple difference with matching", "Reached a third of farmers in three months; helped the credit-constrained"],
           ["Cole and Fernando (2021), Economic Journal", "Phone advisory, Gujarat", "Randomised, 1,200 farmers", "Changed pesticide and crop choices; no systematic yield gain reported"],
           ["Ryan and Sudarshan (2022), JPE", "Farm power and groundwater, Rajasthan", "Structural model with geological variation", "Rationing keeps average use near optimal but misallocates water"],
           ["Muralidharan, Niehaus and Sukhtankar, NBER WP 26744", "Biometric PDS, Jharkhand", "Randomised across 132 sub-districts", "Less corruption; 1.5 to 2 million lost benefits at some point"]]),
        TC([B("The list is short. This course found few rigorous evaluations of the largest farm "
              "schemes, and the ministry-sponsored PM-KISAN study it cites compares beneficiaries with "
              "non-beneficiaries, which cannot separate the scheme from the kind of farmer who joins it.", sm=True)],
           [B("Where evidence is thin, say so, and design your own monitoring so that it can answer a "
              "causal question later.", sm=True)]),
    ], compact=True),

    S("Prices and markets", "What the evidence says about selling crops", [
        TC([B("The Indian evidence on agricultural markets in this course is about information and buyer competition. Goyal's soybean study shows that when farmers could see prices and sell to "
              "a second buyer, mandi prices rose. Cole and Fernando show that farmers use advice when "
              "they can ask for it, and that changing what farmers do does not automatically raise "
              "yields within a season."),
            B("On MSP, the descriptive evidence is clear and the causal evidence is scarce. The "
              "Situation Assessment Surveys show that a minority of farmers sell to procurement "
              "agencies, and the share of wheat output sold at MSP fell between 2013 and 2019. What "
              "MSP does to prices in districts where agencies buy, and to crop choice and "
              "groundwater, needs more rigorous study.", sm=True)],
           [T(["Question", "What we know", "What we do not know well"],
              [["Do farmers get MSP?", "A minority sell to agencies; awareness is limited", "The price effect in districts without procurement"],
               ["Does information raise prices?", "Yes, where a credible buyer competes", "Effects where one trader dominates"],
               ["Do e-markets help?", "Registrations are large", "Volume traded between mandis and its price effect"],
               ["Do FPOs raise members' prices?", "10,000 are registered", "Which FPOs survive and what members gain"]])]),
    ]),

    S("Safety nets", "What the evidence says about food and income transfers", [
        TC([B("The PDS evidence shows that delivery can improve quickly when states reform it. "
              "Dr&egrave;ze and Khera found leakage fell sharply in Chhattisgarh, Odisha and Bihar and "
              "barely changed in some other large states. Technology can cut theft, and the Jharkhand "
              "experiment shows it can also cut people off, depending on how the transition is "
              "managed."),
            B("PM-KISAN's early evidence suggests that a small, regular, unconditional transfer eases "
              "the cash constraints of farmers who lack credit. It also shows the cost of tying "
              "transfers to land records, which leaves out tenants and labourers.", sm=True)],
           [P("cyan", "Principles that carry across schemes",
              "Measure exclusion as carefully as leakage. Keep a fallback for people a new verification "
              "step fails. Tie eligibility to the activity you want to support, cultivation or need, "
              "and check how well the records match it. Pay on a predictable schedule, before the "
              "season's costs fall due."),
            B("For welfare delivery and targeting, see " + L("public-policy-101.html", "Public Policy 101") +
              " and " + L("governance-accountability.html", "Governance and Accountability 101") + ".", sm=True)]),
    ]),

    S("Risk and technology", "What the evidence says about risk, inputs and water", [
        TC([B("Three findings fit together. Farmers value protection against bad weather but buy little "
              "insurance when they must pay for it, do not trust it, or lack cash when the premium is "
              "due (Cole et al. 2013). When a technology removes the worst outcome, farmers invest "
              "more in everything else (Emerick et al. 2016). And when a key input such as water is "
              "free, rationing it by quantity limits the total but sends it to the wrong farmers "
              "(Ryan and Sudarshan 2022)."),
            B("The Economic Survey 2025-26 applies the same logic to fertiliser. A price far below cost "
              "embeds overuse, and an income transfer with prices closer to cost could protect farmers "
              "and soils at once. The Survey proposes pilots, so the idea has not been tested at scale.", sm=True)],
           [T(["Finding", "Programme implication"],
              [["Insurance demand is price-sensitive and trust-sensitive", "Subsidise, pay claims fast, explain area-based settlement"],
               ["Downside protection crowds in investment", "Combine stress-tolerant seed with credit and inputs"],
               ["Free inputs are overused or misallocated", "Prefer transfers plus prices that reflect cost"],
               ["Advice changes practice before yields", "Measure adoption and input use; follow up for yields over seasons"]])]),
    ]),

    S("Practice", "Ten questions to ask of any agricultural scheme", [
        TC([BL(["Who is on the list: owners, cultivators, households or individuals?",
                "How is the list made, and how does someone left off get on?",
                "What does the scheme do to the relative prices of crops, water and fertiliser?",
                "Which crops and which regions receive most of the money?",
                "Does it reach rain-fed farmers, or mostly irrigated ones?",
                "What share of beneficiaries are women, and in whose name is the payment?"], "cyan")],
           [BL(["Is the headline figure a count of people, applications, hectares or rupees?",
                "Is spending reported as budget, revised estimate or actual?",
                "Has any evaluation compared beneficiaries with a credible counterfactual?",
                "What happens to the groundwater, the soil and the household's diet if the scheme "
                "works as intended?"], "green"),
            H("amber", "Run these questions on one scheme in your district before your next planning "
              "meeting, using the sources on the next two slides.")]),
    ]),

    S("Sources: data and government", "Where the numbers in this course come from", [
        TC([BL([A("https://www.pib.gov.in/PressReleasePage.aspx?PRID=1753856", "NSS Report 587, Situation Assessment Survey 2019 (PIB, 10 Sept 2021)"),
                A("https://www.fao.org/fileadmin/templates/ess/ess_test_folder/World_Census_Agriculture/WCA_2020/WCA_2020_new_doc/IND_REP_ENG_2015_2016.pdf", "Agriculture Census 2015-16, All India Report"),
                A("https://www.pib.gov.in/PressReleasePage.aspx?PRID=2287251", "PIB, Agricultural Census (2021-22), 21 July 2026"),
                A("https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260618", "PIB, Kharif MSP 2026-27, 13 May 2026"),
                A("https://www.pib.gov.in/PressReleasePage.aspx?PRID=2173567", "PIB, Rabi MSP 2026-27"),
                A("https://www.pib.gov.in/PressReleasepage.aspx?PRID=2316941", "PIB, Rabi MSP 2027-28, 30 Sept 2026"),
                A("https://www.pib.gov.in/PressReleasePage.aspx?PRID=2177219", "PIB, Minimum Support Prices backgrounder, 10 Oct 2025"),
                A("https://www.indiabudget.gov.in/doc/Budget_at_Glance/budget_at_a_glance.pdf", "Budget at a Glance 2026-27"),
                A("https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap06.pdf", "Economic Survey 2025-26, chapter 6"),
                A("https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap12.pdf", "Economic Survey 2025-26, chapter 12"),
                A("https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap13.pdf", "Economic Survey 2025-26, chapter 13")], sm=True)],
           [BL([A("https://prsindia.org/files/bills_acts/acts_parliament/2013/national-food-security-act-2013.pdf", "National Food Security Act 2013, Gazette text"),
                A("https://prsindia.org/billtrack/the-farm-laws-repeal-bill-2021", "PRS, Farm Laws Repeal Bill 2021"),
                A("https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc_9735_20260829_18493301.pdf", "PIB backgrounder on PMFBY, 29 Aug 2026"),
                A("https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jun/doc2026620898101.pdf", "PIB backgrounder on PM-KISAN, 20 June 2026"),
                A("https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc2026812952301.pdf", "PIB backgrounder, The New Era of Indian Agriculture, 12 Aug 2026"),
                A("https://mospi.gov.in/sites/default/files/publication_reports/AnnualReport_PLFS2023-24L2.pdf", "PLFS Annual Report 2023-24"),
                A("https://www.mospi.gov.in/uploads/latestReleases/latest_release_1774607827733_3e8964a9-268b-4cc9-ad65-cfc8a9e32f08_Press_note_AR_PLFS_2025_23032025_V2.1_26032026_final.pdf", "PLFS Annual Report 2025, press note"),
                A("https://www.icar.org.in/sites/default/files/Circulars/LU-2365.pdf", "ICAR, Lok Sabha Unstarred Question 2365, 10 Dec 2024"),
                A("https://www.etvbharat.com/en/bharat/nearly-11-per-cent-groundwater-assessment-units-over-exploited-govt-enn26072007475", "Groundwater assessment 2025, Rajya Sabha reply (ETV Bharat report)"),
                A("https://legislative.gov.in/constitution-of-india/", "Constitution of India, Seventh Schedule")], sm=True)]),
    ], compact=True),

    S("Sources: studies and analysis", "Research and analysis cited in this course", [
        TC([BL([A("https://ageconsearch.umn.edu/record/334366/files/Situation_Assessment_Survey_of_Agricultural_Households_2019_A_Statistical_Note.pdf", "Bakshi (2021), SAS 2019: A Statistical Note, Review of Agrarian Studies 11(2)"),
                A("https://ideas.repec.org/a/aea/aejapp/v2y2010i3p22-45.html", "Goyal (2010), AEJ: Applied Economics 2(3): 22-45"),
                A("https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr373.pdf", "Cole, Gin&eacute;, Tobacman, Topalova, Townsend and Vickery (2013), AEJ: Applied 5(1): 104-35"),
                A("https://web.iitd.ac.in/~suban/COP290/stuff/pds/Understanding_Leakages_in_the_Public_Distribution_System.pdf", "Dr&egrave;ze and Khera (2015), Understanding Leakages in the PDS, EPW 50(7)"),
                A("https://povertyactionlab.org/sites/default/files/research-paper/852%20Ag%20Innovation%20Risk%20Oct2015.pdf", "Emerick, de Janvry, Sadoulet and Dar (2016), AER 106(6): 1537-61"),
                A("https://cgspace.cgiar.org/server/api/core/bitstreams/e1860a45-121f-44ba-a67e-8eebf09a884a/content", "Varshney, Joshi, Roy and Kumar (2020), IFPRI Discussion Paper 1907")], sm=True)],
           [BL([A("https://www.atai-research.org/wp-content/uploads/2020/06/ueaa084.pdf", "Cole and Fernando (2021), 'Mobile'izing Agricultural Advice, Economic Journal"),
                A("https://ideas.repec.org/a/ucp/jpolec/doi10.1086-717045.html", "Ryan and Sudarshan (2022), Rationing the Commons, JPE 130(1): 210-257"),
                A("https://www.nber.org/papers/w26744", "Muralidharan, Niehaus and Sukhtankar, Identity Verification Standards in Welfare Programs, NBER WP 26744"),
                A("https://www.nfhsiips.in/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-24%20Fact%20Sheets.pdf", "IIPS (2026), NFHS-6 India and State/UT Fact Sheets"),
                A("https://www.downtoearth.org.in/environment/reduce-food-security-benefits-from-67-to-40-population-says-panel-on-restructuring-fci--48344", "Down To Earth (2015) on the Shanta Kumar committee report"),
                A("https://prsindia.org/billtrack/the-farmers-produce-trade-and-commerce-promotion-and-facilitation-bill-2020", "PRS, Farmers' Produce Trade and Commerce Bill 2020")], sm=True),
            H("cyan", "Where two official "
              "sources disagree, as on the PM-KISAN allocation, the course says so.")]),
    ], compact=True),
]


DECK = {
    "slug": "agri-food",
    "title": "Agriculture and Food Systems 101",
    "description": ("Agriculture and Food Systems 101: a free foundational course for development "
                    "practitioners in India. Who farms and on how much land from the Agriculture Census "
                    "and the Situation Assessment Survey, farm incomes and debt, MSP, the CACP and "
                    "procurement, the 2020 farm laws and their repeal, the PDS and the National Food "
                    "Security Act, fertiliser and power subsidies, irrigation and groundwater, PMFBY, "
                    "PM-KISAN, markets, extension and FPOs, tenancy and women in agriculture, climate "
                    "risk and nutrition, and what evaluations have found. ImpactMojo, CC BY-NC-ND."),
    "slides": [
        {"type": "title",
         "main": "Agriculture<br>and Food<br>Systems 101",
         "sub": "A foundational course on Indian farming for development practitioners, from land "
                "and incomes to prices, food, water, risk and the evidence",
         "tags": ["100 Slides", "India Focus", "Free Forever", "MSP to Nutrition"]},

        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Who farms, and on how much land"},
             {"name": "Incomes and indebtedness"},
             {"name": "MSP, the CACP and procurement"},
             {"name": "The 2020 farm laws and their repeal"},
             {"name": "The PDS and the National Food Security Act"},
             {"name": "Input subsidies"},
             {"name": "Irrigation and groundwater"},
             {"name": "Crop insurance and income support"},
             {"name": "Markets, extension and FPOs"},
             {"name": "Land records, tenancy and women"},
             {"name": "Climate risk, nutrition and food systems"},
             {"name": "Evidence and sources"},
         ]},
    ] + SEC1 + SEC2 + SEC3 + SEC4 + SEC5 + SEC6 + SEC7 + SEC8 + SEC9 + SEC10 + SEC11 + SEC12 + [
        {"type": "end",
         "eyebrow": "Agriculture and Food Systems 101 &middot; Complete",
         "headline": "Start with who farms<br>and who is on the list",
         "byline": "Most Indian holdings are under one hectare, and many farm schemes pay whoever the land records name. Check the source, the unit and the list before you "
                   "design. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "The 101 Series", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

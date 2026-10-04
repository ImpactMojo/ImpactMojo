/* =============================================================================
   ImpactMojo — Fundamentals: the Power Cube
   -----------------------------------------------------------------------------
   The cube is John Gaventa's, from "Finding the Spaces for Change: A Power
   Analysis", IDS Bulletin 37(6), 2006. The three dimensions and their nine
   categories are his. He builds on Steven Lukes' three dimensions of power
   (1974), and his wording of the three forms is adapted from VeneKlasen and
   Miller (2002). The teaching resource lives at powercube.net, run by IDS.

   ImpactMojo adds the Indian evidence: for each category, and for a set of
   documented Indian cases plotted on all three dimensions at once.

   Every figure below was checked against the source named beside it, and the
   wording keeps to what that source says. A claim that could not be confirmed
   was cut. Each category's `definition` is in our own words after Gaventa;
   `cite` says so on the page.
   ============================================================================= */

window.CUBE = (function () {
  "use strict";

  var AFTER_GAVENTA = "In our words, after Gaventa (2006)";
  var LEVELS_NOTE = "In our words. Gaventa (2006) describes levels as a range from local to global";

  var dims = [
    {
      id: "space", name: "Spaces", color: "#7c3aed",
      question: "Where does the decision get made, and who set the table?",
      cats: [
        { id: "closed", name: "Closed", color: "#4c1d95",
          definition: "A small set of actors decides behind closed doors, and nobody pretends to widen who takes part.",
          cite: AFTER_GAVENTA,
          evidence: [
            { stat: "Collegium", detail: "Judges of the Supreme Court and High Courts are recommended by the collegium, a body of the senior-most judges. There is no application process. Parliament tried to replace the collegium with a National Judicial Appointments Commission through the Ninety-ninth Constitutional Amendment, and a five-judge bench struck that down by four judges to one on 16 October 2015. In October 2017 the collegium resolved to publish its decisions, with reasons, on the Supreme Court website.", source: "Supreme Court Advocates-on-Record Association v. Union of India, (2016) 5 SCC 1", year: "2015" },
            { stat: "116", detail: "internet shutdowns were recorded in India in 2023, the most of any country for the sixth year running. Orders were issued by the Union or state Home Secretary under the Telegraph Act, 1885 and its 2017 suspension rules, since replaced by the Telecommunications Act, 2023 and the 2024 rules. Since Anuradha Bhasin v. Union of India (2020) they must be published, and Access Now reports that officials still fail to do so. India recorded 65 in 2025, the lowest since 2017 and second to Myanmar's 95.", source: "Access Now, #KeepItOn reports", year: "2023, 2025" },
            { stat: "Ordinances", detail: "When Parliament is not sitting, the President may promulgate an ordinance under Article 123 on the advice of ministers, and a Governor may do the same for a state under Article 213. An ordinance has the force of an Act and is made without a debate. It must be laid before the legislature, and it lapses six weeks after the legislature reassembles, or earlier if the legislature disapproves it.", source: "Constitution of India, Articles 123 and 213", year: "1950" }
          ],
          complication: "Some closed spaces have a reason. Judicial independence is the case made for keeping judicial appointments away from political pressure, and the collegium's defenders make it. The cube records who is in the room and leaves open whether the room should exist."
        },
        { id: "invited", name: "Invited", color: "#7c3aed",
          definition: "Authorities such as government, international agencies or NGOs invite people to take part. The authority sets the invitation and its terms.",
          cite: AFTER_GAVENTA,
          evidence: [
            { stat: "2.55 lakh+", detail: "village panchayats each have a gram sabha, the body of all registered voters in the village. Article 243A says a gram sabha exercises the powers and functions that the state legislature provides by law, so what it can do differs from state to state.", source: "Reserve Bank of India, Finances of Panchayati Raj Institutions (data for 2020-21 to 2022-23); Constitution of India, Article 243A", year: "2022-23" },
            { stat: "§17", detail: "Section 17 of the Mahatma Gandhi National Rural Employment Guarantee Act, 2005 said that the gram sabha \"shall conduct regular social audits of all the projects under the Scheme taken up within the Gram Panchayat\". A new law, the Viksit Bharat–Guarantee for Rozgar and Aajeevika Mission (Gramin) Act, 2025, came into force in rural areas on 1 July 2026. This evidence describes the 2005 Act.", source: "Mahatma Gandhi National Rural Employment Guarantee Act, 2005; Press Information Bureau, 31 July 2026", year: "2005" },
            { stat: "30 days", detail: "is the minimum notice for a public hearing under the EIA Notification as issued in 2006. Projects in Category A and Category B1 must hold public consultation, which includes a hearing near the site, except for listed activities such as modernising irrigation projects. If a hearing cannot be held in a way that lets local people speak freely, the authority can decide that the consultation need not include one.", source: "Ministry of Environment and Forests, EIA Notification, S.O. 1533(E)", year: "2006" }
          ],
          complication: "Most organised participation happens in invited spaces, and the invitation sets its limits. Taking a seat can give a decision legitimacy without changing it, which is why the cube asks you to look at the other two spaces before deciding what a seat is worth."
        },
        { id: "claimed", name: "Claimed", color: "#a78bfa",
          definition: "Less powerful people claim these spaces from or against the powerholders, or create them on their own. They range from social movements and community associations to ordinary places where people gather to discuss, debate and resist outside institutional policy arenas.",
          cite: AFTER_GAVENTA,
          evidence: [
            { stat: "1990s", detail: "The Mazdoor Kisan Shakti Sangathan began holding public hearings in rural Rajasthan in the mid-1990s, where payment records for local works were read out and compared with what villagers had received. The campaign for a right to see those records led to the Rajasthan Right to Information Act, 2000 and the national Right to Information Act, 2005.", source: "Mazdoor Kisan Shakti Sangathan; Rajasthan Right to Information Act, 2000; Right to Information Act, 2005", year: "1990s to 2005" },
            { stat: "1991", detail: "The Narmada Bachao Andolan campaigned against the Sardar Sarovar dam from the late 1980s. In 1991 the World Bank's president, Barber Conable, asked for an independent review of the project. The Morse Commission reported in June 1992, and the Bank described it as the first independent review of a project it had funded.", source: "World Bank press release, 18 June 1992", year: "1992" },
            { stat: "70,000+", detail: "responses reached the Justice Verma Committee, which was set up on 23 December 2012, after the Delhi gang rape of 16 December, and had asked the public for suggestions by 5 January 2013. Its report came on 23 January 2013. Parliament then passed the Criminal Law (Amendment) Act, 2013, which did not adopt every recommendation.", source: "Report of the Committee on Amendments to Criminal Law (Justice J.S. Verma), January 2013", year: "2013" }
          ],
          complication: "Claimed spaces often change the rules, and the rules then bring them inside official process. Each of the three examples above ended up there, as a statute, a Bank review or a committee report. That is a gain, and it means the space is no longer on the claimants' own terms."
        }
      ]
    },
    {
      id: "level", name: "Levels", color: "#0f766e",
      question: "At which level is the decision actually taken?",
      cats: [
        { id: "local", name: "Local", color: "#134e4a",
          definition: "The level closest to where people live, such as the village, the ward or the town.",
          cite: LEVELS_NOTE,
          evidence: [
            { stat: "29", detail: "subjects are listed in the Eleventh Schedule. Under Article 243G a state legislature may by law give panchayats the powers they need to prepare plans and carry out schemes for economic development and social justice, including on those subjects. The Constitution leaves it to each state legislature whether to do so.", source: "Constitution (73rd Amendment) Act, 1992; Constitution of India, Article 243G", year: "1992" },
            { stat: "95%+", detail: "of panchayat revenue receipts were grants from the Centre and the states in each of the three years the Reserve Bank of India reviewed, 2020-21 to 2022-23. The Fifteenth Finance Commission's grants to rural local bodies come in two parts. The untied part can be spent on local needs under the Eleventh Schedule subjects, except salaries. The tied part can be spent only on sanitation and drinking water.", source: "Reserve Bank of India, Finances of Panchayati Raj Institutions; Ministry of Panchayati Raj, Press Information Bureau, 25 March 2026", year: "2020-23" }
          ],
          complication: "Participation is easiest to organise at the local level. Whether it reaches anything that matters depends on what higher levels have already fixed, and the two items above show two such limits: powers that depend on state law, and money that arrives with conditions attached."
        },
        { id: "national", name: "National", color: "#0f766e",
          definition: "The level at which most binding law and budget is set, and where elected representatives take the place of direct participation.",
          cite: LEVELS_NOTE,
          evidence: [
            { stat: "16%", detail: "of Bills in the 17th Lok Sabha (2019 to 2024) were referred to committees for detailed scrutiny, against 28 per cent in the 16th, 71 per cent in the 15th and 60 per cent in the 14th. A Pre-Legislative Consultation Policy issued by the Ministry of Law and Justice in 2014 asks ministries to put draft Bills in the public domain for comment. It is an executive policy and not a law.", source: "PRS Legislative Research, Functioning of the 17th Lok Sabha; Ministry of Law and Justice", year: "2019-24" },
            { stat: "74 of 543", detail: "members of the 18th Lok Sabha elected in 2024 are women, which is 13.6 per cent of the seats. Women were 48.5 per cent of the population at the 2011 Census.", source: "PRS Legislative Research, Profile of the 18th Lok Sabha; Census of India", year: "2024" }
          ],
          complication: "A national space can be formally open and still unrepresentative. The figures here show it for gender, and a count of who holds national office can be run along any other axis for which a reliable count exists."
        },
        { id: "global", name: "Global", color: "#14b8a6",
          definition: "The level of treaties, lenders and standard-setters, where decisions that bind a country are taken in rooms its citizens cannot enter.",
          cite: LEVELS_NOTE,
          evidence: [
            { stat: "WTO", detail: "India has contested the rules on public stockholding for food security at the WTO since 2013. Through these programmes the government buys grain at administered prices for the public distribution system. The Bali Ministerial Decision of 2013 and a General Council decision of 27 November 2014 set up an interim \"peace clause\" that shields such programmes from disputes while members look for a permanent solution.", source: "WTO, Bali Ministerial Decision (WT/MIN(13)/38) and General Council Decision (WT/L/939)", year: "2013, 2014" },
            { stat: "3(d)", detail: "The Patents (Amendment) Act, 2005 brought India's patent law into line with the TRIPS Agreement by allowing product patents, and it also added section 3(d), which refuses a patent for a new form of a known substance unless it enhances the known efficacy of that substance. On 1 April 2013 the Supreme Court applied it in Novartis AG v. Union of India to refuse a patent on the beta crystalline form of imatinib mesylate (Glivec).", source: "Patents (Amendment) Act, 2005; Novartis AG v. Union of India", year: "2005, 2013" }
          ],
          complication: "Global decisions are the hardest to hold anyone accountable for. Section 3(d) is an example of a country writing its own rule inside a global agreement."
        }
      ]
    },
    {
      id: "form", name: "Forms", color: "#b45309",
      question: "How is the power being exercised, and can you see it?",
      cats: [
        { id: "visible", name: "Visible", color: "#78350f",
          definition: "Observable decision-making: the formal rules, structures, authorities and procedures. Who makes the law, and who sits where.",
          cite: AFTER_GAVENTA,
          evidence: [
            { stat: "Statute", detail: "Seats for Scheduled Castes and Scheduled Tribes in Parliament and the state legislatures are reserved by Articles 330 and 332, and in panchayats and municipalities by Articles 243D and 243T. For Other Backward Classes the Constitution lets the state make special provision in education (Article 15(4) and 15(5)) and in public employment (Article 16(4)), and lets a state reserve seats and offices in local bodies (Articles 243D(6) and 243T(6)). There is no reservation for Other Backward Classes in Parliament or the state legislatures. These provisions are argued over in Parliament and in court.", source: "Constitution of India, Articles 15, 16, 243D, 243T, 330 and 332", year: "1950 onward" },
            { stat: "Published", detail: "Budgets, Bills, court judgments and gazette notifications are published, so anyone can read the decisions they record and argue over them.", source: "Parliament of India; Gazette of India", year: "current" }
          ],
          complication: "Visible power is the easiest to study. A law can be public and still change little of what happens, which is why the cube adds hidden and invisible power."
        },
        { id: "hidden", name: "Hidden", color: "#b45309",
          definition: "Power exercised by setting the agenda: certain powerful people and institutions control who reaches the decision-making table and what gets on the agenda.",
          cite: AFTER_GAVENTA,
          evidence: [
            { stat: "1931", detail: "The last census to publish a count of every caste was in 1931. Census 2027 will enumerate caste in its second phase, population enumeration, in February 2027, with 1 March 2027 as the reference date. Until those results are published, claims for a proportional share have had no census count of every caste to rest on.", source: "Census of India; Ministry of Home Affairs, Press Information Bureau, 30 March 2026", year: "1931, 2027" },
            { stat: "Para 3", detail: "Paragraph 3 of the Constitution (Scheduled Castes) Order, 1950 says that no person who professes a religion different from the Hindu, the Sikh or the Buddhist religion is deemed a member of a Scheduled Caste. Dalit Christians and Dalit Muslims are therefore outside the Scheduled Castes. The 1950 text named only the Hindu religion, Sikhs were added in 1956 and Buddhists in 1990. The National Commission for Religious and Linguistic Minorities, chaired by Justice Ranganath Misra, recommended in May 2007 that the paragraph be deleted. It remains in the Order.", source: "Constitution (Scheduled Castes) Order, 1950; National Commission for Religious and Linguistic Minorities", year: "1950, 2007" },
            { stat: "23.1%", detail: "of the deaths registered in India in 2024 had a medically certified cause (20,66,117 of 89,38,301). The other 76.9 per cent carry no medically certified cause of death.", source: "Registrar General of India, Medical Certification of Cause of Death", year: "2024" }
          ],
          complication: "Hidden power is inferred and cannot be observed directly, so it is the easiest claim to overreach on. The disciplined version names the specific issue kept off the table and who benefits from its absence, and avoids asserting a general conspiracy."
        },
        { id: "invisible", name: "Invisible", color: "#f59e0b",
          definition: "Power that shapes meaning and what people accept as normal, so that an arrangement is not experienced as a decision at all and grievance does not form.",
          cite: AFTER_GAVENTA,
          evidence: [
            { stat: "27%", detail: "of surveyed households said someone in the household practises untouchability in some form: 30 per cent in rural and 20 per cent in urban India. This is what respondents said about themselves.", source: "NCAER, India Human Development Survey-II (press release of 29 November 2014)", year: "2011-12" },
            { stat: "94.6%", detail: "of married women aged 15 to 49 reported marrying within their caste, and 5.4 per cent reported an inter-caste marriage.", source: "NCAER, India Human Development Survey-II", year: "2011-12" },
            { stat: "299 vs 97", detail: "minutes a day were spent on unpaid domestic services for household members by the women and the men who did any of this work on the reference day. 81.2 per cent of women and 26.1 per cent of men aged 6 and over did some. Unpaid household services lie outside the production boundary of the UN System of National Accounts, so GDP does not count them.", source: "National Statistics Office, Time Use in India, 2019", year: "2019" }
          ],
          complication: "Invisible power is the hardest form to test. These figures show a pattern that fits internalised norms. A survey cannot tell a norm someone accepts from a constraint they cannot escape."
        }
      ]
    }
  ];

  /* Documented Indian cases, plotted on all three dimensions at once. */
  var cases = [
    { name: "MKSS public hearings, Rajasthan", space: "claimed", level: "local", form: "hidden",
      note: "Payment records for local works were read out in public and compared with what villagers had received. A claimed local space brought hidden records into view. The campaign for access to records led to Rajasthan's Right to Information Act of 2000 and the national Act of 2005.", year: "1990s" },
    { name: "Right to Information Act", space: "invited", level: "national", form: "hidden",
      note: "Gave every citizen a legal right to request records from public authorities. It acts on hidden power by making the file available on request.", year: "2005" },
    { name: "MGNREGA social audit", space: "invited", level: "local", form: "visible",
      note: "Section 17 of the 2005 Act put the audit of works in the gram sabha's hands. The law created the space and set its terms, and the records it examines are of work done in the village. A new law, the VB-G RAM G Act, 2025, came into force in rural areas on 1 July 2026.", year: "2005" },
    { name: "Niyamgiri gram sabhas", space: "invited", level: "local", form: "visible",
      note: "In April 2013 the Supreme Court directed Odisha to put the community's religious and cultural rights to the affected gram sabhas. Twelve gram sabhas met in July and August 2013 and all twelve rejected the mining. The Environment Ministry declined the project in January 2014.", year: "2013" },
    { name: "Narmada Bachao Andolan", space: "claimed", level: "global", form: "visible",
      note: "A claimed space that reached the global level. The World Bank's president asked for the first independent review of a project the Bank had funded, the Morse Commission of 1991 to 1992.", year: "Late 1980s onward" },
    { name: "Judicial collegium", space: "closed", level: "national", form: "hidden",
      note: "Judges recommend judges, with no application process. Parliament's attempt to replace the collegium with a commission was struck down in 2015.", year: "1993 onward" },
    { name: "Caste count, 1931 to 2027", space: "closed", level: "national", form: "hidden",
      note: "No census since 1931 has published a count of every caste. Without one, claims for a proportional share have had no census figure to rest on. Census 2027 will enumerate caste.", year: "1931 to 2027" },
    { name: "Untouchability in the household", space: "closed", level: "local", form: "invisible",
      note: "No decision is taken and no rule is cited. In the India Human Development Survey-II, 27 per cent of households said someone in the household practises untouchability.", year: "2011-12" }
  ];

  return { dims: dims, cases: cases };
})();

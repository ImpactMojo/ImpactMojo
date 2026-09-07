/* =============================================================================
   ImpactMojo — Fundamentals: The Results Chain
   -----------------------------------------------------------------------------
   The chain is not ImpactMojo's. Inputs → activities → outputs → outcomes →
   impact is the logical framework, developed by Practical Concepts Incorporated
   (Leon J. Rosenberg and colleagues) for USAID around 1969-70, given its
   standard definitions by the OECD Development Assistance Committee's Glossary
   of Key Terms in Evaluation and Results Based Management (2002), and taught
   since as the logic model or the theory of change. Carol Weiss's 1995 essay
   is where the second phrase comes from.

   What ImpactMojo adds is the measurement layer. For six large Indian
   programmes, each link is marked by how it is actually measured: a public
   management information system updated continuously, a national survey on a
   multi-year cycle, independent research, or nothing at all.

   The finding the page exists for is that the measurement does not fade
   gradually along the chain. It stops, and it stops at the same place in every
   one of the six: after outputs, one link before the claim the programme is
   defended with.

   Every figure names a source and a year. Figures from the National Family
   Health Survey and the Periodic Labour Force Survey were taken from the DHS
   StatCompiler and the MoSPI API respectively rather than from memory or from
   secondary reporting.
   ============================================================================= */

window.RESULTSCHAIN = (function () {
  "use strict";

  var links = [
    { id: "inputs", name: "Inputs",
      gloss: "What goes in: money, staff, buildings, equipment.",
      question: "What did it cost?" },
    { id: "activities", name: "Activities",
      gloss: "What is done with the inputs: works sanctioned, centres run, hospitals empanelled.",
      question: "What was done?" },
    { id: "outputs", name: "Outputs",
      gloss: "What the activities directly produce, counted in units the programme controls: person-days, toilets, enrolments, admissions.",
      question: "What was produced?" },
    { id: "outcomes", name: "Outcomes",
      gloss: "The change in people's condition the outputs were meant to cause: income, sanitation behaviour, learning, nutrition, financial protection.",
      question: "Did anything change?" },
    { id: "impact", name: "Impact",
      gloss: "The longer-run, wider change, net of what would have happened anyway.",
      question: "Was it because of this?" }
  ];

  /* Height in the small multiples is this weight. It is a ranking of how close
     a measurement sits to the programme and how often it arrives, not a score
     of quality: a well-run MIS can be wrong and a good study can be right. */
  var states = {
    continuous: { weight: 100, label: "Counted continuously",
                  note: "A public management information system, updated daily or monthly, at the level of the individual transaction." },
    periodic:   { weight: 62,  label: "A survey, every few years",
                  note: "A national sample survey on a multi-year cycle, run by an agency other than the programme and not designed to evaluate it." },
    research:   { weight: 30,  label: "Only where a researcher went",
                  note: "Measured by independent studies in particular districts and years. Real evidence, and not a number the programme can be managed by." },
    absent:     { weight: 8,   label: "Not measured",
                  note: "No routine instrument collects it at national scale." }
  };

  var programmes = [
    {
      id: "mgnrega", name: "MGNREGA", since: "2005", colour: "#b45309",
      what: "A legal guarantee of a hundred days of wage employment a year to any rural household whose adults will do unskilled manual work.",
      chain: {
        inputs: { state: "continuous", instrument: "Union Budget and the scheme's own fund release records",
          detail: "Allocation and state-wise release are published and revised in public through the year.",
          source: "Union Budget; Ministry of Rural Development", year: "annual" },
        activities: { state: "continuous", instrument: "The MGNREGA management information system",
          detail: "Works sanctioned, muster rolls and attendance are on a public system at the level of the individual worksite and the individual day. It is among the most granular administrative datasets any government publishes.",
          source: "Ministry of Rural Development MIS", year: "continuous" },
        outputs: { state: "continuous", instrument: "The same MIS",
          detail: "Person-days generated, by district and by day, and the count of households completing the full hundred days.",
          source: "Ministry of Rural Development MIS", year: "continuous" },
        outcomes: { state: "research", instrument: "Independent studies",
          detail: "Whether a household's income rose, whether distress migration fell, whether the guarantee raised the rural wage floor. None of this is collected routinely anywhere.",
          source: "Clément Imbert and John Papp, American Economic Journal: Applied Economics", year: "2015" },
        impact: { state: "research", instrument: "Independent studies",
          detail: "Imbert and Papp found private-sector wage increases in districts where the scheme started earlier. Muralidharan, Niehaus and Sukhtankar found that biometric payment in Andhra Pradesh cut leakage and delay without cutting the work done. Both are district studies of particular years.",
          source: "Karthik Muralidharan, Paul Niehaus and Sandip Sukhtankar, American Economic Review", year: "2016" }
      },
      breaks: "outcomes",
      breakNote: "The scheme counts a person-day to the individual worker and the calendar day, and publishes it. Whether the household was better off at the end of the year is measured by nobody, on any cycle. The most granular administrative dataset in Indian government sits directly next to the largest hole."
    },
    {
      id: "swachh", name: "Swachh Bharat (Gramin)", since: "2014", colour: "#0369a1",
      what: "A national mission to end open defecation in rural India, largely through subsidised household latrine construction.",
      chain: {
        inputs: { state: "continuous", instrument: "Mission budget and release records",
          detail: "Allocation, central and state shares, and incentive payments per household.",
          source: "Department of Drinking Water and Sanitation", year: "annual" },
        activities: { state: "continuous", instrument: "The mission MIS",
          detail: "Construction sanctioned and completed, household by household, with photographs in later years.",
          source: "Swachh Bharat Mission (Gramin) MIS", year: "continuous" },
        outputs: { state: "continuous", instrument: "The same MIS",
          detail: "Latrines built and villages declared open-defecation free, reported village by village and aggregated to a national declaration in October 2019.",
          source: "Swachh Bharat Mission (Gramin) MIS", year: "2019" },
        outcomes: { state: "periodic", instrument: "The National Annual Rural Sanitation Survey, and independent survey work",
          detail: "Use is a different variable from ownership, and the distinction is the whole outcome. The SQUAT survey across five north Indian states found open defecation continuing in a large share of households that already owned a working latrine, which is the finding the output measure cannot see.",
          source: "SQUAT survey, r.i.c.e.; and Diane Coffey and Dean Spears, Where India Goes", year: "2014, 2017" },
        impact: { state: "research", instrument: "Independent studies",
          detail: "Whether child height, diarrhoea or mortality moved, and how much of any movement belongs to the mission rather than to rising incomes over the same decade. Contested, and studied in particular districts.",
          source: "Independent epidemiological and economic studies", year: "various" }
      },
      breaks: "outcomes",
      breakNote: "The chain here does not break for want of an instrument. It breaks at a definition: the output was written as a latrine existing, and the outcome the mission was for is a latrine being used. Everything downstream of that substitution is unmeasured by the system that made it."
    },
    {
      id: "schooling", name: "Right to Education", since: "2010", colour: "#7c3aed",
      what: "A justiciable right to free and compulsory elementary education for every child from six to fourteen, with norms for schools, teachers and admission.",
      chain: {
        inputs: { state: "continuous", instrument: "UDISE+ and state education budgets",
          detail: "Schools, teachers, classrooms, toilets and drinking water, reported annually for every recognised school in the country.",
          source: "UDISE+, Ministry of Education", year: "annual" },
        activities: { state: "continuous", instrument: "UDISE+",
          detail: "Teacher deployment, pupil-teacher ratios and compliance with the Act's own infrastructure norms.",
          source: "UDISE+, Ministry of Education", year: "annual" },
        outputs: { state: "continuous", instrument: "UDISE+ and ASER",
          detail: "Enrolment. Rural enrolment of children aged six to fourteen has been above 96 per cent in every ASER round since 2010 and reached 98.4 per cent in 2022. On the output measure the Act has essentially succeeded.",
          source: "Annual Status of Education Report, Pratham", year: "2022" },
        outcomes: { state: "periodic", instrument: "ASER, a citizen-run household survey, and the National Achievement Survey",
          detail: "Learning. In ASER 2022, 42.8 per cent of children in Class 5 in rural India could read a Class 2 text, down from just over half in 2018. The gap between this and the enrolment figure is the most examined output-outcome wedge in Indian development.",
          source: "Annual Status of Education Report, Pratham", year: "2022" },
        impact: { state: "research", instrument: "Independent studies",
          detail: "Whether more schooling produced more earnings, mobility or civic participation, and for whom. Studied, never routinely.",
          source: "Independent studies", year: "various" }
      },
      breaks: "outcomes",
      breakNote: "The state measures enrolment continuously, for every school, and does not measure reading. The number that everyone quotes for Indian learning comes from a household survey run by an NGO. That is not an accident of capacity: enrolment is what the Act made justiciable, so enrolment is what the system was built to count."
    },
    {
      id: "icds", name: "ICDS and Poshan Abhiyaan", since: "1975", colour: "#be123c",
      what: "Supplementary nutrition, immunisation and pre-school education for children under six and for pregnant and nursing women, delivered through anganwadi centres.",
      chain: {
        inputs: { state: "continuous", instrument: "Scheme budgets and the Poshan Tracker",
          detail: "Allocation, centres sanctioned, workers in post.",
          source: "Ministry of Women and Child Development", year: "annual" },
        activities: { state: "continuous", instrument: "The Poshan Tracker",
          detail: "Centres operating, days open, growth monitoring sessions held, recorded on a national application.",
          source: "Poshan Tracker, Ministry of Women and Child Development", year: "continuous" },
        outputs: { state: "continuous", instrument: "The Poshan Tracker",
          detail: "Beneficiaries registered and receiving supplementary nutrition, reported daily.",
          source: "Poshan Tracker, Ministry of Women and Child Development", year: "continuous" },
        outcomes: { state: "periodic", instrument: "The National Family Health Survey",
          detail: "Stunting among children under five fell from 38.4 per cent in 2015-16 to 35.5 per cent in 2019-21. Wasting did not move: 19.5 per cent in 1998-99, 19.8 in 2005-06, 21.0 in 2015-16 and 19.3 in 2019-21, four measurements across twenty-two years inside a range of under two points.",
          source: "National Family Health Survey rounds 2 to 5, via the DHS StatCompiler", year: "2021" },
        impact: { state: "research", instrument: "Independent studies",
          detail: "How much of the stunting decline belongs to the scheme rather than to income, sanitation, maternal education or later childbearing. Not separable from national survey data.",
          source: "Independent studies", year: "various" }
      },
      breaks: "impact",
      breakNote: "This is the one programme on the page whose outcome is genuinely measured, and it shows what measurement alone cannot do. The stunting series moves and the wasting series does not, across four surveys and twenty-two years, and nothing in the measurement can say which part of either belongs to the largest child nutrition programme in the world."
    },
    {
      id: "pmjay", name: "Ayushman Bharat PM-JAY", since: "2018", colour: "#047857",
      what: "Public insurance covering hospital treatment up to five lakh rupees a year for the poorest two-fifths of households.",
      chain: {
        inputs: { state: "continuous", instrument: "Scheme budget and state contributions",
          detail: "Premium or trust funding, central and state shares.",
          source: "National Health Authority", year: "annual" },
        activities: { state: "continuous", instrument: "The PM-JAY dashboard",
          detail: "Hospitals empanelled, public and private, by district.",
          source: "National Health Authority", year: "continuous" },
        outputs: { state: "continuous", instrument: "The same dashboard",
          detail: "Cards issued and hospital admissions authorised, per transaction, with the amount claimed.",
          source: "National Health Authority", year: "continuous" },
        outcomes: { state: "periodic", instrument: "The National Health Accounts and NSS health rounds",
          detail: "Financial protection: whether households were spared catastrophic expenditure. Out-of-pocket spending as a share of total health expenditure has fallen substantially over the scheme's lifetime, on an instrument that covers all health spending and cannot attribute the fall.",
          source: "National Health Accounts Estimates for India, National Health Systems Resource Centre", year: "various" },
        impact: { state: "research", instrument: "Independent studies",
          detail: "Whether the scheme reduced impoverishment, changed treatment-seeking, or shifted care towards private hospitals. Studied in particular states.",
          source: "Independent studies", year: "various" }
      },
      breaks: "outcomes",
      breakNote: "Outputs here are exact to the rupee and the admission. The outcome the scheme exists for, a household not ruined by a hospital bill, is measured by an instrument built for something else, on a cycle the scheme does not control, in a period when several other things changed at once."
    },
    {
      id: "pmkisan", name: "PM-KISAN", since: "2019", colour: "#4338ca",
      what: "An unconditional income transfer of six thousand rupees a year to landholding farmer families, in three instalments.",
      chain: {
        inputs: { state: "continuous", instrument: "Union Budget",
          detail: "Allocation and disbursement.",
          source: "Ministry of Agriculture and Farmers' Welfare", year: "annual" },
        activities: { state: "continuous", instrument: "The PM-KISAN portal",
          detail: "Registration, verification and the removal of ineligible beneficiaries.",
          source: "Ministry of Agriculture and Farmers' Welfare", year: "continuous" },
        outputs: { state: "continuous", instrument: "The same portal",
          detail: "Instalments paid and beneficiaries paid, published per instalment and per state.",
          source: "Ministry of Agriculture and Farmers' Welfare", year: "continuous" },
        outcomes: { state: "absent", instrument: "None",
          detail: "What the household did with the money: input purchase, debt repayment, consumption, or none of these. No routine national instrument collects it, and the scheme's entire theory is a claim about exactly this.",
          source: "No national instrument", year: "—" },
        impact: { state: "research", instrument: "A small number of independent studies",
          detail: "Effects on agricultural investment and on borrowing, in particular states and seasons.",
          source: "Independent studies", year: "various" }
      },
      breaks: "outcomes",
      breakNote: "The starkest case on the page. A transfer programme is a theory about what a household does with money, and the money is counted to the rupee while the doing is not counted at all. The measurement is not weak here; it is absent, and the scheme is defended in public with the output figure."
    }
  ];

  return { links: links, states: states, programmes: programmes };
})();

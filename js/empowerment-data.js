/* =============================================================================
   ImpactMojo — Fundamentals: Resources, Agency, Achievements
   -----------------------------------------------------------------------------
   The framework is Naila Kabeer's, from "Resources, Agency, Achievements:
   Reflections on the Measurement of Women's Empowerment", Development and
   Change 30(3), 1999. Empowerment, in her definition, is the expansion in
   people's ability to make strategic life choices in a context where that
   ability was previously denied them, and it has three inseparable parts:
   resources as the pre-conditions, agency as the process, achievements as the
   outcomes.

   The half of the paper that is usually dropped is the measurement half. A
   choice is only meaningful if alternatives existed, if the person could see
   them, and if the choice carried consequence; an indicator that moves without
   those conditions has not measured empowerment. Kabeer's warning is that
   almost every available proxy can move for the wrong reason.

   What ImpactMojo adds is the Indian test of that warning. Every series below
   was pulled from the source rather than from secondary reporting: the National
   Family Health Survey rounds through the DHS StatCompiler, and the Periodic
   Labour Force Survey through the MoSPI API. Each indicator carries the
   companion series or breakdown that changes how it reads, because that pairing
   is the method, not a caveat.
   ============================================================================= */

window.EMPOWERMENT = (function () {
  "use strict";

  var dimensions = [
    { id: "resources", name: "Resources", colour: "#0369a1",
      gloss: "The pre-conditions. Material, human and social resources, and the terms on which they are held.",
      caution: "A resource distributed on terms someone else sets is not the same as a resource held. Kabeer's example is credit given to a woman and used by her husband." },
    { id: "agency", name: "Agency", colour: "#7c3aed",
      gloss: "The process. The ability to define one's goals and act on them, including the quieter forms: bargaining, negotiation, and resistance that is not visible.",
      caution: "Agency measured by asking about decisions cannot see the decisions nobody raised, and preferences formed inside a constraint will report as satisfaction." },
    { id: "achievements", name: "Achievements", colour: "#047857",
      gloss: "The outcomes. What the resources and the agency actually produced in a person's life.",
      caution: "An outcome can improve for reasons that have nothing to do with anyone's choice, and Kabeer's test is whether the alternative was genuinely available." }
  ];

  var indicators = [
    {
      id: "flfpr", dimension: "resources",
      name: "Women in the labour force",
      unit: "% of women aged 15+",
      definition: "Labour force participation rate, women aged 15 and above, usual status (principal plus subsidiary), rural and urban combined.",
      series: [
        { label: "2017-18", value: 23.3 }, { label: "2018-19", value: 24.5 },
        { label: "2023", value: 41.3 }, { label: "2024", value: 40.3 }, { label: "2025", value: 40.0 }
      ],
      source: "Periodic Labour Force Survey, MoSPI, retrieved from the MoSPI API",
      headline: "It nearly doubled in six years. Read as a resource indicator, this is the largest movement in any Indian gender statistic this century.",
      companionTitle: "The same year, by education (2017-18)",
      companion: [
        { label: "Not literate", value: 27.8 }, { label: "Up to primary", value: 25.1 },
        { label: "Middle", value: 17.6 }, { label: "Secondary", value: 14.6 },
        { label: "Higher secondary", value: 13.5 }, { label: "Graduate", value: 29.2 },
        { label: "Post-graduate", value: 45.6 }
      ],
      complication: "The curve is U-shaped and it has been for decades. Participation is highest among women with no schooling at all and among post-graduates, and lowest in the middle. One end is a career and the other is necessity, and the indicator cannot tell them apart. By social group in 2023 the gradient runs the same way: 64.1 per cent among Scheduled Tribes, 43.3 among Scheduled Castes, 41.0 among Other Backward Classes and 32.2 among others. Participation is highest where poverty is deepest.",
      test: "Kabeer's condition is that the alternative must have existed. For a woman who works because the household cannot eat otherwise, it did not, and counting her as more empowered than the woman who withdrew from the workforce when her household's income rose reverses the reading."
    },
    {
      id: "healthsay", dimension: "agency",
      name: "Final say in her own health care",
      unit: "% of currently married women",
      definition: "Women who say they alone or jointly have the final say in decisions about their own health care.",
      series: [
        { label: "2005-06", value: 62.2 }, { label: "2015-16", value: 74.5 }, { label: "2019-21", value: 81.1 }
      ],
      source: "National Family Health Survey rounds 3, 4 and 5, retrieved from the DHS StatCompiler",
      headline: "Four in five married women now report a say in decisions about their own body, up nineteen points in fifteen years.",
      companionTitle: "Final say in all three decisions, and in none",
      companion: [
        { label: "All three, 2005-06", value: 39.3 }, { label: "All three, 2015-16", value: 63.0 },
        { label: "All three, 2019-21", value: 71.0 },
        { label: "None, 2005-06", value: 23.5 }, { label: "None, 2015-16", value: 16.0 },
        { label: "None, 2019-21", value: 11.3 }
      ],
      complication: "The indicator counts a woman who has the say alone and a woman who has it jointly with her husband as the same answer. Its own definition says so: alone or jointly. Whether the household changed or the joint answer became the expected one is not separable from the number, and both would move it the same way.",
      test: "The direction is real and the series is consistent across three rounds and a second question. What it cannot establish is whether the ability to choose expanded or the description of an unchanged arrangement did."
    },
    {
      id: "norms", dimension: "agency",
      name: "Wife-beating justified for at least one reason",
      unit: "% agreeing",
      definition: "Percentage who agree that a husband is justified in hitting or beating his wife for at least one specific reason. Women interviewed; men aged 15-49.",
      series: [
        { label: "2005-06", value: 47.2 }, { label: "2015-16", value: 44.6 }, { label: "2019-21", value: 38.2 }
      ],
      source: "National Family Health Survey rounds 3, 4 and 5, retrieved from the DHS StatCompiler",
      headline: "Agreement among women has fallen nine points since 2005-06, to 38.2 per cent.",
      companionTitle: "The same question, asked of men",
      companion: [
        { label: "Men, 2005-06", value: 42.1 }, { label: "Men, 2015-16", value: 31.9 },
        { label: "Men, 2019-21", value: 33.5 }
      ],
      complication: "In every round, a larger share of women than of men agrees that a husband is sometimes justified in beating his wife, and the gap has widened: 38.2 per cent of women against 33.5 per cent of men in 2019-21, with the men's figure having risen since the previous round rather than continued to fall.",
      test: "This is the sharpest available Indian evidence for the thing Kabeer's agency chapter warns about. Preferences formed inside a constraint are reported as preferences, so an instrument that asks a woman what she thinks is right will record the constraint as her view. A decision-making score and this score come from the same questionnaire and the same woman."
    },
    {
      id: "violence", dimension: "achievements",
      name: "Freedom from spousal violence",
      unit: "% of ever-married women 15-49",
      definition: "Women who have ever experienced physical or sexual violence committed by a husband or partner.",
      series: [
        { label: "2005-06", value: 37.2 }, { label: "2015-16", value: 30.9 }, { label: "2019-21", value: 29.1 }
      ],
      source: "National Family Health Survey rounds 3, 4 and 5, retrieved from the DHS StatCompiler",
      headline: "Lifetime experience of spousal violence has fallen eight points in fifteen years, from 37.2 per cent to 29.1.",
      companionTitle: "The same violence, in the last twelve months",
      companion: [
        { label: "2005-06", value: 23.0 }, { label: "2015-16", value: 23.9 }, { label: "2019-21", value: 24.0 }
      ],
      complication: "The twelve-month measure did not move at all: 23.0 per cent, then 23.9, then 24.0, across the same three rounds and the same survey. Lifetime exposure fell because the women being asked are younger and have been married for less time; current exposure is where it was.",
      test: "Two numbers from one instrument, pointing opposite ways, and only one of them is quoted. This is the case to keep for the moment someone in a workshop says an outcome has improved: which measure, and what else moved that could produce it?"
    }
  ];

  return { dimensions: dimensions, indicators: indicators };
})();

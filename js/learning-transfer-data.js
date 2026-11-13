/* =============================================================================
   ImpactMojo - Fundamentals: the Wheel of Learning Transfer
   -----------------------------------------------------------------------------
   Learning transfer means a trainee still does something differently at work
   after the training. The idea that transfer depends on three groups of
   inputs (the learner, the design of the training, and the workplace) is from
   Baldwin and Ford, "Transfer of training: a review and directions for future
   research", Personnel Psychology 41(1), 1988. Burke and Hutchins (2007) and
   Blume and others (2010) later reviewed the evidence on each group.

   The ten-factor, three-level wheel format was popularised in a graphic by
   Matt Furness (@matthewfurness). Every sentence here is ImpactMojo's own
   wording, written against the research literature, and the three-level
   scoring is ours to defend. Nothing is copied from that graphic.

   Rule for this file: a source is named only for what the source actually
   studied. Where a level is a practitioner judgement and not a finding, the
   factor's "limits" says so. No statistic is given that was not read.
   ============================================================================= */

window.LTRANSFER = (function () {
  "use strict";

  /* Rings run from the centre outward. "stick" is the best position. */
  var RING_ORDER = ["stick", "risk", "drop"];
  var RINGS = {
    stick: { label: "Likely to stick", short: "Sticks", score: 2, note: "The trainee meets this condition in full." },
    risk:  { label: "At risk",         short: "At risk", score: 1, note: "The condition is partly there, so use depends on luck and on the individual." },
    drop:  { label: "Unlikely to stick", short: "Drops", score: 0, note: "The condition is missing or works against the new practice." }
  };

  var BANDS = {
    learner:   { label: "The learner",       note: "What the trainee brings into the room." },
    design:    { label: "The training",      note: "What the programme does while the trainee is in it." },
    workplace: { label: "The workplace",     note: "What the trainee goes back to." }
  };

  var factors = [
    {
      id: "motivation", name: "Motivation", band: "learner", color: "#e03131",
      asks: "Did the trainee want to be there, and want to use what they learned?",
      levels: {
        stick: "The trainee chose the training, or accepted it after seeing a use for it. They arrive wanting a specific skill.",
        risk:  "The trainee was willing but was sent by someone else. Their interest is real and has not been tested against their daily work.",
        drop:  "Attendance is compulsory and counted by headcount. The trainee is present to be marked present."
      },
      research: [
        { ref: "Colquitt, LePine and Noe", year: "2000", detail: "A meta-analysis in the Journal of Applied Psychology 85(5) of what raises and follows from motivation to learn in training." }
      ],
      do: "Tell people before the training what they will be able to do after it and why it matters in their job. Where attendance is mandatory, say what each person gets out of it.",
      ask: "Did anyone select the participants for a reason they can explain to the participants?",
      limits: "Motivation is partly a product of the other nine factors. A person who sees no manager support will, reasonably, report low motivation."
    },
    {
      id: "confidence", name: "Confidence", band: "learner", color: "#e8590c",
      asks: "Does the trainee believe they can actually do the new thing?",
      levels: {
        stick: "The trainee has done the task during training, with feedback, and leaves sure of the first step they will take on Monday.",
        risk:  "The trainee follows the method in theory and has not tried it with real material. They think it should work.",
        drop:  "The trainee leaves unsure where to begin, or with the sense that the method is for people with more authority or skill than they have."
      },
      research: [
        { ref: "Bandura", year: "1977", detail: "Self-efficacy, the belief that you can carry out a specific action, as a predictor of whether you attempt it and persist." },
        { ref: "Blume, Ford, Baldwin and Huang", year: "2010", detail: "A meta-analysis in the Journal of Management 36(4) of predictors of transfer, including self-efficacy." }
      ],
      do: "Finish with each trainee naming one task they will do in the next week and rehearsing its first five minutes.",
      ask: "Can each participant say, without notes, what they will do first?",
      limits: "Confidence and competence are different. Over-confident trainees apply a half-learned method, so pair this factor with Practice."
    },
    {
      id: "practice", name: "Practice", band: "design", color: "#2f9e44",
      asks: "Did the trainee rehearse the skill, and did anyone tell them how it went?",
      levels: {
        stick: "The training includes rehearsal on tasks like the real ones, with feedback from a coach or peer, and a second attempt.",
        risk:  "The training shows examples and lets each person try the method once, with no feedback or second attempt.",
        drop:  "The training is presentation and discussion. Nobody performs the skill before leaving."
      },
      research: [
        { ref: "Taylor, Russ-Eft and Chan", year: "2005", detail: "A meta-analysis in the Journal of Applied Psychology 90(4) of behaviour modelling training, where trainees watch a skill, rehearse it and get feedback." }
      ],
      do: "Cut content until there is time for each participant to perform the skill and get a response. Two practised skills beat ten described ones.",
      ask: "How many minutes did each participant spend doing the skill, rather than hearing about it?",
      limits: "Behaviour modelling has the strongest evidence for skills that can be shown step by step. For judgement skills, practice is harder to design and the evidence is thinner."
    },
    {
      id: "relevance", name: "Relevance", band: "design", color: "#099268",
      asks: "Does the training look like the job the trainee goes back to?",
      levels: {
        stick: "The tasks, tools, forms and constraints used in training match the trainee's actual work.",
        risk:  "The examples are plausible for the field but generic. The trainee has to work out the translation to their own setting.",
        drop:  "The content is abstract or drawn from a different context, and the trainee sees no occasion to use it."
      },
      research: [
        { ref: "Thorndike and Woodworth", year: "1901", detail: "The identical elements idea: learning carries over to the extent a new situation shares elements with the one where it was learned." },
        { ref: "Baldwin and Ford", year: "1988", detail: "Placed similarity between the training and the work setting inside the training design factors that affect transfer." }
      ],
      do: "Build exercises from the participants' own documents, cases, data or forms, collected before the session.",
      ask: "Could a participant use the training materials unchanged in their next piece of work?",
      limits: "Close matching can teach a procedure that is wrong or outdated for the job. Relevance does not replace checking that the method is sound."
    },
    {
      id: "workload", name: "Workload", band: "workplace", color: "#0c8599",
      asks: "Will the trainee have time and a real occasion to use the skill?",
      levels: {
        stick: "Time is protected for the new practice, and the trainee's work in the next weeks includes tasks that call for it.",
        risk:  "The trainee is busy but could fit the skill in if they chose to, and no task obliges them to.",
        drop:  "The trainee goes straight back to a full schedule with no space and no task that needs the new skill."
      },
      research: [
        { ref: "Ford, Quinones, Sego and Sorra", year: "1992", detail: "Studied opportunity to perform trained tasks on the job in Personnel Psychology 45(3), and found that trainees differ widely in how much chance they get to use what they learned." }
      ],
      do: "Agree a first application task with the trainee's manager before the training starts, and clear time for it.",
      ask: "What will this person be doing in the two weeks after training, and does any of it use the skill?",
      limits: "A heavy workload can also be a symptom of a missing process. If the skill would save time, the case for protecting time has to be made with that evidence."
    },
    {
      id: "manager", name: "Manager support", band: "workplace", color: "#1971c2",
      asks: "Did the trainee's manager prepare them, and do they follow up?",
      levels: {
        stick: "The manager discussed the goals beforehand, agrees an application task afterward, and asks how it is going.",
        risk:  "The manager approves of the training and does not mention it again. Use of the skill depends on the trainee's own drive.",
        drop:  "The manager does not know what the training covered, or discourages the trainee from changing how work is done."
      },
      research: [
        { ref: "Burke and Hutchins", year: "2007", detail: "An integrative review in Human Resource Development Review 6(3), which found supervisor support to be one of the most consistently reported work environment factors in transfer." },
        { ref: "Blume, Ford, Baldwin and Huang", year: "2010", detail: "Included supervisor support among the predictors in a meta-analysis of transfer." }
      ],
      do: "Brief managers in ten minutes before the training and give them two questions to ask afterward.",
      ask: "Could the trainee's manager say what the training was for?",
      limits: "In hierarchical settings the manager's support may matter more, and a manager's absence of interest may reflect their own workload. Support from a manager also depends on their own incentives."
    },
    {
      id: "social", name: "Social reinforcement", band: "workplace", color: "#3b5bdb",
      asks: "Do colleagues treat the new way of working as normal?",
      levels: {
        stick: "Peers who were also trained work together on the skill, share what is working, and others in the team expect it.",
        risk:  "Colleagues are neutral. Nobody objects and nobody joins in, so the trainee is on their own.",
        drop:  "The group's habits pull the other way. Trying the new method brings jokes, resistance or being seen as a show-off."
      },
      research: [
        { ref: "Burke and Hutchins", year: "2007", detail: "Reviewed peer support, including peers who encourage use and who model it, among the work environment influences on transfer." }
      ],
      do: "Train people in teams or pairs where you can, and set up a short recurring slot where they report what they tried.",
      ask: "Is there anyone in this trainee's workplace they can use the skill with, this month?",
      limits: "Evidence on peer effects is mostly from corporate and military settings. How it plays out in a village health team or a block office is not well studied."
    },
    {
      id: "accountability", name: "Accountability", band: "workplace", color: "#6741d9",
      asks: "Will anyone ask whether the trainee used what they learned?",
      levels: {
        stick: "The trainee reports on use of the skill to someone who reads the report and responds, at a date set before the training ended.",
        risk:  "A plan was written at the end of training and nobody has been named to look at it again.",
        drop:  "No follow-up exists. The training ends and nothing is asked of the trainee afterwards."
      },
      research: [
        { ref: "Burke and Saks", year: "2009", detail: "Applied a model of responsibility to training transfer in Human Resource Development Review 8(4), arguing that people use training more when they expect to answer for it." }
      ],
      do: "Fix a follow-up date and a named person before the participants leave the room.",
      ask: "Who will ask, and when, and what will they do with the answer?",
      limits: "Accountability that works as punishment pushes people to report use without using. It works when the follow-up is a conversation about what got in the way."
    },
    {
      id: "leadership", name: "Leadership modelling", band: "workplace", color: "#9c36b5",
      asks: "Do the people at the top do what the training teaches?",
      levels: {
        stick: "Senior people use the method themselves, in public, and are known to have gone through the same training.",
        risk:  "Senior people endorse the method and praise it, and do not change how they work.",
        drop:  "Senior people exempt themselves, or work in a way that contradicts the training."
      },
      research: [
        { ref: "Bandura", year: "1977", detail: "Social learning theory: people pick up which behaviours are worth adopting by watching what others, especially those with status, do and are rewarded for." },
        { ref: "Rouiller and Goldstein", year: "1993", detail: "Showed in Human Resource Development Quarterly 4(4) that the climate of the receiving organisation, including cues from those in charge, relates to whether trained behaviour is used." }
      ],
      do: "Put leaders through the same programme first, and ask them to describe publicly how they will use it.",
      ask: "Has a senior person in the organisation been seen using the skill?",
      limits: "Leaders who attend and then do not use the skill damage the programme more than leaders who never attend. A leader's visible use cannot be forced."
    },
    {
      id: "systems", name: "Systems fit", band: "workplace", color: "#c2255c",
      asks: "Do the forms, targets, tools and rules make the new behaviour easy or costly?",
      levels: {
        stick: "Processes, reports and targets are built so that doing the new thing is the easy way to meet them.",
        risk:  "The systems are indifferent. The trainee can use the skill only by working around forms and routines built for the old way.",
        drop:  "Targets, reporting formats or tools penalise the new behaviour, so doing it costs the trainee something."
      },
      research: [
        { ref: "Rouiller and Goldstein", year: "1993", detail: "Studied transfer climate, which includes consequences and cues in the workplace, in Human Resource Development Quarterly 4(4)." },
        { ref: "Holton", year: "1996", detail: "Proposed in Human Resource Development Quarterly 7(1) that transfer depends on a learning transfer system that includes organisational factors beyond the training itself." }
      ],
      do: "Before training, list the three forms, targets or tools a trainee will meet when applying the skill, and change one.",
      ask: "If a trainee does exactly what we taught, what happens to their monthly report or their target?",
      limits: "Changing systems is slow and often outside the trainer's authority. When you cannot change them, tell trainees honestly which parts of the training will meet resistance."
    }
  ];

  var SOURCES = [
    "Baldwin, T. T. and Ford, J. K. (1988). Transfer of training: a review and directions for future research. Personnel Psychology 41(1), 63-105.",
    "Bandura, A. (1977). Social Learning Theory. Prentice Hall.",
    "Blume, B. D., Ford, J. K., Baldwin, T. T. and Huang, J. L. (2010). Transfer of training: a meta-analytic review. Journal of Management 36(4), 1065-1105.",
    "Burke, L. A. and Hutchins, H. M. (2007). Training transfer: an integrative literature review. Human Resource Development Review 6(3), 263-296.",
    "Burke, L. A. and Saks, A. M. (2009). Accountability in training transfer: adapting Schlenker's model of responsibility to improve training outcomes. Human Resource Development Review 8(4), 382-402.",
    "Colquitt, J. A., LePine, J. A. and Noe, R. A. (2000). Toward an integrative theory of training motivation: a meta-analytic path analysis of 20 years of research. Journal of Applied Psychology 85(5), 678-707.",
    "Ford, J. K., Quinones, M. A., Sego, D. J. and Sorra, J. S. (1992). Factors affecting the opportunity to perform trained tasks on the job. Personnel Psychology 45(3), 511-527.",
    "Holton, E. F. (1996). The flawed four-level evaluation model. Human Resource Development Quarterly 7(1), 5-21.",
    "Rouiller, J. Z. and Goldstein, I. L. (1993). The relationship between organizational transfer climate and positive transfer of training. Human Resource Development Quarterly 4(4), 377-390.",
    "Taylor, P. J., Russ-Eft, D. F. and Chan, D. W. L. (2005). A meta-analytic review of behavior modeling training. Journal of Applied Psychology 90(4), 692-709.",
    "Thorndike, E. L. and Woodworth, R. S. (1901). The influence of improvement in one mental function upon the efficiency of other functions. Psychological Review 8, 247-261."
  ];

  return { RING_ORDER: RING_ORDER, RINGS: RINGS, BANDS: BANDS, factors: factors, SOURCES: SOURCES };
})();

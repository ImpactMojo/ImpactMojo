/* =============================================================================
   ImpactMojo - Fundamentals: the Wheel of Learning Transfer
   -----------------------------------------------------------------------------
   Learning transfer means a trainee still does something differently at work
   after the training. The idea that transfer depends on three groups of
   inputs (the learner, the design of the training, and the workplace) is from
   Baldwin and Ford, "Transfer of training: a review and directions for future
   research", Personnel Psychology, 1988. Burke and Hutchins (2007) and
   Blume and others (2010) later reviewed the evidence on each group.

   The ten-factor, three-level wheel format was popularised in a graphic by
   Matt Furness (@matthewfurness). Every sentence here is ImpactMojo's own
   wording, written against the research literature, and the three-level
   scoring is ours to defend. Nothing is copied from that graphic.

   Rule for this file: a source is named only for what its abstract says it
   studied. All eleven sources were looked up on 13 November 2026 (Consensus
   index of Semantic Scholar, OpenAlex and PubMed). Volume and page numbers were
   not confirmed in that lookup and are left off. Where a level is a practitioner judgement and not a finding, the
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
      tags: { stick: "Chose it|wants it", risk: "Willing, but|sent by|someone else", drop: "Attends to|be counted" },
      levels: {
        stick: "The trainee chose the training, or accepted it after seeing a use for it. They arrive wanting a specific skill.",
        risk:  "The trainee was willing but was sent by someone else. Their interest is real and has not been tested against their daily work.",
        drop:  "Attendance is compulsory and counted by headcount. The trainee is present to be marked present."
      },
      research: [
        { ref: "Colquitt, LePine and Noe", year: "2000", detail: "A meta-analysis in the Journal of Applied Psychology of 20 years of research on training motivation, its antecedents, and its links to learning, skill acquisition and transfer." },
        { ref: "Blume, Ford, Baldwin and Huang", year: "2010", detail: "A meta-analysis of 89 studies in the Journal of Management that found motivation positively related to transfer, and more strongly so when the training was for open skills such as leadership than for closed skills such as software." }
      ],
      do: "Tell people before the training what they will be able to do after it and why it matters in their job. Where attendance is mandatory, say what each person gets out of it.",
      ask: "Did anyone select the participants for a reason they can explain to the participants?",
      limits: "Motivation is partly a product of the other nine factors. A person who sees no manager support will, reasonably, report low motivation."
    },
    {
      id: "confidence", name: "Confidence", band: "learner", color: "#e8590c",
      asks: "Does the trainee believe they can actually do the new thing?",
      tags: { stick: "Sure of the|first step", risk: "Believes it|works in|theory", drop: "Unsure|where to|start" },
      levels: {
        stick: "The trainee has done the task during training, with feedback, and leaves sure of the first step they will take on Monday.",
        risk:  "The trainee follows the method in theory and has not tried it with real material. They think it should work.",
        drop:  "The trainee leaves unsure where to begin, or with the sense that the method is for people with more authority or skill than they have."
      },
      research: [
        { ref: "Bandura", year: "1977", detail: "Proposed in Psychological Review that expectations of personal efficacy decide whether a behaviour is attempted, how much effort goes into it and how long it is sustained, and that they grow from performance accomplishments, vicarious experience, verbal persuasion and physiological states." },
        { ref: "Grossman and Salas", year: "2011", detail: "A review in the International Journal of Training and Development that lists self-efficacy among the trainee characteristics with the strongest, most consistent relationships to transfer." }
      ],
      do: "Finish with each trainee naming one task they will do in the next week and rehearsing its first five minutes.",
      ask: "Can each participant say, without notes, what they will do first?",
      limits: "Confidence and competence are different. Over-confident trainees apply a half-learned method, so pair this factor with Practice."
    },
    {
      id: "practice", name: "Practice", band: "design", color: "#2f9e44",
      asks: "Did the trainee rehearse the skill, and did anyone tell them how it went?",
      tags: { stick: "Rehearsed|with feedback", risk: "Tried it|once", drop: "Heard it,|never did it" },
      levels: {
        stick: "The training includes rehearsal on tasks like the real ones, with feedback from a coach or peer, and a second attempt.",
        risk:  "The training shows examples and lets each person try the method once, with no feedback or second attempt.",
        drop:  "The training is presentation and discussion. Nobody performs the skill before leaving."
      },
      research: [
        { ref: "Taylor, Russ-Eft and Chan", year: "2005", detail: "A meta-analysis of 117 studies of behaviour modelling training, in which trainees watch a skill, rehearse it and get feedback. Effects on skills and job behaviour stayed stable or grew over time, and transfer was greatest when practice included scenarios the trainees generated themselves." }
      ],
      do: "Cut content until there is time for each participant to perform the skill and get a response. Two practised skills beat ten described ones.",
      ask: "How many minutes did each participant spend doing the skill, rather than hearing about it?",
      limits: "The evidence here is about behaviour modelling training. It does not show that other kinds of practice work as well."
    },
    {
      id: "relevance", name: "Relevance", band: "design", color: "#099268",
      asks: "Does the training look like the job the trainee goes back to?",
      tags: { stick: "Same tasks|as the job", risk: "Generic|examples", drop: "Abstract,|no use seen" },
      levels: {
        stick: "The tasks, tools, forms and constraints used in training match the trainee's actual work.",
        risk:  "The examples are plausible for the field but generic. The trainee has to work out the translation to their own setting.",
        drop:  "The content is abstract or drawn from a different context, and the trainee sees no occasion to use it."
      },
      research: [
        { ref: "Thorndike and Woodworth", year: "1901", detail: "Experiments in Psychological Review on whether practice at one mental function improves others. The idea that transfer depends on how much two situations share is usually traced to this work." },
        { ref: "Grossman and Salas", year: "2011", detail: "Lists realistic training environments among the training design factors with the strongest, most consistent relationships to transfer." }
      ],
      do: "Build exercises from the participants' own documents, cases, data or forms, collected before the session.",
      ask: "Could a participant use the training materials unchanged in their next piece of work?",
      limits: "Close matching can teach a procedure that is wrong or outdated for the job. Relevance does not replace checking that the method is sound."
    },
    {
      id: "workload", name: "Workload", band: "workplace", color: "#0b7285",
      asks: "Will the trainee have time and a real occasion to use the skill?",
      tags: { stick: "Time set|aside", risk: "Busy, could|squeeze it in", drop: "No time|to apply" },
      levels: {
        stick: "Time is protected for the new practice, and the trainee's work in the next weeks includes tasks that call for it.",
        risk:  "The trainee is busy but could fit the skill in if they chose to, and no task obliges them to.",
        drop:  "The trainee goes straight back to a full schedule with no space and no task that needs the new skill."
      },
      research: [
        { ref: "Ford, Quinones, Sego and Sorra", year: "1992", detail: "Studied 180 Air Force technical training graduates and their supervisors four months after training, in Personnel Psychology. Graduates got very different opportunities to perform what they had learned, and the differences were related to supervisors' attitudes, workgroup support, self-efficacy and cognitive ability." }
      ],
      do: "Agree a first application task with the trainee's manager before the training starts, and clear time for it.",
      ask: "What will this person be doing in the two weeks after training, and does any of it use the skill?",
      limits: "A heavy workload can also be a symptom of a missing process. If the skill would save time, the case for protecting time has to be made with that evidence."
    },
    {
      id: "manager", name: "Manager support", band: "workplace", color: "#1971c2",
      asks: "Did the trainee's manager prepare them, and do they follow up?",
      tags: { stick: "Briefs and|follows up", risk: "Approves,|never asks", drop: "Unaware or|opposed" },
      levels: {
        stick: "The manager discussed the goals beforehand, agrees an application task afterward, and asks how it is going.",
        risk:  "The manager approves of the training and does not mention it again. Use of the skill depends on the trainee's own drive.",
        drop:  "The manager does not know what the training covered, or discourages the trainee from changing how work is done."
      },
      research: [
        { ref: "Burke and Hutchins", year: "2007", detail: "An integrative review in Human Resource Development Review that sorts the factors influencing transfer into learner characteristics, intervention design and delivery, and work environment influences." },
        { ref: "Blume, Ford, Baldwin and Huang", year: "2010", detail: "Found a supportive work environment among the predictors positively related to transfer in a meta-analysis of 89 studies." },
        { ref: "Taylor, Russ-Eft and Chan", year: "2005", detail: "Found transfer greatest when the trainees' superiors were also trained." }
      ],
      do: "Brief managers in ten minutes before the training and give them two questions to ask afterward.",
      ask: "Could the trainee's manager say what the training was for?",
      limits: "In hierarchical settings the manager's support may matter more, and a manager who shows no interest may be short of time. Support from a manager also depends on their own incentives. These are our judgements."
    },
    {
      id: "social", name: "Social reinforcement", band: "workplace", color: "#3b5bdb",
      asks: "Do colleagues treat the new way of working as normal?",
      tags: { stick: "Peers do it|together", risk: "Colleagues|neutral", drop: "Group pulls|against it" },
      levels: {
        stick: "Peers who were also trained work together on the skill, share what is working, and others in the team expect it.",
        risk:  "Colleagues are neutral. Nobody objects and nobody joins in, so the trainee is on their own.",
        drop:  "The group's habits pull the other way. Trying the new method brings jokes, resistance or being seen as a show-off."
      },
      research: [
        { ref: "Ford, Quinones, Sego and Sorra", year: "1992", detail: "Found that the opportunity airmen got to use trained tasks was related to workgroup support as well as to supervisors' attitudes." }
      ],
      do: "Train people in teams or pairs where you can, and set up a short recurring slot where they report what they tried.",
      ask: "Is there anyone in this trainee's workplace they can use the skill with, this month?",
      limits: "Our reading, not a finding: peer effects are likely to differ across workplaces. The study cited covers Air Force technical training, and how peers matter in a village health team or a block office has not been studied in the sources used here."
    },
    {
      id: "accountability", name: "Accountability", band: "workplace", color: "#6741d9",
      asks: "Will anyone ask whether the trainee used what they learned?",
      tags: { stick: "Reports to|someone who|reads it", risk: "Plan made,|nobody checks", drop: "No follow-up" },
      levels: {
        stick: "The trainee reports on use of the skill to someone who reads the report and responds, at a date set before the training ended.",
        risk:  "A plan was written at the end of training and nobody has been named to look at it again.",
        drop:  "No follow-up exists. The training ends and nothing is asked of the trainee afterwards."
      },
      research: [
        { ref: "Burke and Saks", year: "2009", detail: "A conceptual paper in Human Resource Development Review that applies Schlenker's pyramid of accountability to training transfer. It argues accountability is central to the transfer problem and recommends an accountability audit. It reports no new data." },
        { ref: "Taylor, Russ-Eft and Chan", year: "2005", detail: "Found transfer greatest when rewards and sanctions were put in place in the trainees' work environments." }
      ],
      do: "Fix a follow-up date and a named person before the participants leave the room.",
      ask: "Who will ask, and when, and what will they do with the answer?",
      limits: "Our judgement, not a finding: follow-up that works as punishment may push people to report use without using. It works better as a conversation about what got in the way."
    },
    {
      id: "leadership", name: "Leadership modelling", band: "workplace", color: "#9c36b5",
      asks: "Do the people at the top do what the training teaches?",
      tags: { stick: "Leaders use it|visibly", risk: "Leaders|praise it,|don't use it", drop: "Leaders|exempt|themselves" },
      levels: {
        stick: "Senior people use the method themselves, in public, and are known to have gone through the same training.",
        risk:  "Senior people endorse the method and praise it, and do not change how they work.",
        drop:  "Senior people exempt themselves, or work in a way that contradicts the training."
      },
      research: [
        { ref: "Bandura", year: "1977", detail: "Named vicarious experience, seeing others perform a behaviour, as one of four sources of the expectation that a person can do it." },
        { ref: "Taylor, Russ-Eft and Chan", year: "2005", detail: "Found transfer greatest when the trainees' superiors were also trained." }
      ],
      do: "Put leaders through the same programme first, and ask them to describe publicly how they will use it.",
      ask: "Has a senior person in the organisation been seen using the skill?",
      limits: "No source cited here tests a leader's visible use of the skill directly. The support is that training superiors helps (Taylor and others) and that seeing others perform a behaviour shapes efficacy (Bandura). The rest is inference."
    },
    {
      id: "systems", name: "Systems fit", band: "workplace", color: "#c2255c",
      asks: "Do the forms, targets, tools and rules make the new behaviour easy or costly?",
      tags: { stick: "Easy way is|the new way", risk: "Needs|workarounds", drop: "Targets|punish the|new way" },
      levels: {
        stick: "Processes, reports and targets are built so that doing the new thing is the easy way to meet them.",
        risk:  "The systems are indifferent. The trainee can use the skill only by working around forms and routines built for the old way.",
        drop:  "Targets, reporting formats or tools penalise the new behaviour, so doing it costs the trainee something."
      },
      research: [
        { ref: "Rouiller and Goldstein", year: "1993", detail: "Studied manager trainees in over a hundred fast-food restaurants of one franchise, in Human Resource Development Quarterly. Trainees placed in units with a more positive transfer climate were rated better at the behaviours they had learned." },
        { ref: "Holton", year: "1996", detail: "Proposed an evaluation model in Human Resource Development Quarterly in which transfer of training conditions, with motivation to learn, trainability, job attitudes and personal characteristics, are intervening variables between training and outcomes." }
      ],
      do: "Before training, list the three forms, targets or tools a trainee will meet when applying the skill, and change one.",
      ask: "If a trainee does exactly what we taught, what happens to their monthly report or their target?",
      limits: "Changing systems is slow and often outside the trainer's authority. When you cannot change them, tell trainees honestly which parts of the training will meet resistance."
    }
  ];

  var SOURCES = [
    "Baldwin, T. T. and Ford, J. K. (1988). Transfer of training: a review and directions for future research. Personnel Psychology.",
    "Bandura, A. (1977). Self-efficacy: toward a unifying theory of behavioral change. Psychological Review.",
    "Blume, B. D., Ford, J. K., Baldwin, T. T. and Huang, J. L. (2010). Transfer of training: a meta-analytic review. Journal of Management.",
    "Burke, L. A. and Hutchins, H. M. (2007). Training transfer: an integrative literature review. Human Resource Development Review.",
    "Burke, L. A. and Saks, A. M. (2009). Accountability in training transfer: adapting Schlenker's model of responsibility to a persistent but solvable problem. Human Resource Development Review.",
    "Colquitt, J. A., LePine, J. A. and Noe, R. A. (2000). Toward an integrative theory of training motivation: a meta-analytic path analysis of 20 years of research. Journal of Applied Psychology.",
    "Ford, J. K., Quinones, M. A., Sego, D. J. and Sorra, J. S. (1992). Factors affecting the opportunity to perform trained tasks on the job. Personnel Psychology.",
    "Grossman, R. and Salas, E. (2011). The transfer of training: what really matters. International Journal of Training and Development.",
    "Holton, E. F. (1996). The flawed four-level evaluation model. Human Resource Development Quarterly.",
    "Rouiller, J. Z. and Goldstein, I. L. (1993). The relationship between organizational transfer climate and positive transfer of training. Human Resource Development Quarterly.",
    "Taylor, P. J., Russ-Eft, D. F. and Chan, D. W. L. (2005). A meta-analytic review of behavior modeling training. Journal of Applied Psychology.",
    "Thorndike, E. L. and Woodworth, R. S. (1901). The influence of improvement in one mental function upon the efficiency of other functions. Psychological Review."
  ];

  return { RING_ORDER: RING_ORDER, RINGS: RINGS, BANDS: BANDS, factors: factors, SOURCES: SOURCES };
})();

# -*- coding: utf-8 -*-
"""
Academic Writing & Publishing 101 — ImpactMojo 101 Series (native deck spec)
From the thesis chapter to the journal article: argument, structure, clarity, tables and
figures, citation and integrity, the Indian PhD process, choosing a journal, surviving peer
review, and the ethics of authorship. For researchers and practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py academic_writing
"""

DECK = {
    "slug": "academic-writing",
    "title": "Academic Writing & Publishing 101",
    "description": ("Academic Writing & Publishing 101 — a free foundational course for researchers "
                    "and practitioners in South Asia. How to build an argument, structure a paper or "
                    "thesis, write clearly, present numbers and figures, cite and avoid plagiarism, "
                    "get through the Indian PhD process, choose a journal and avoid predatory ones, "
                    "respond to peer review, and handle authorship and AI use. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Academic<br>Writing &amp;<br>Publishing 101",
         "sub": "From the Thesis Chapter to the Journal Article &mdash; Argument, Structure, "
                "Clarity, Integrity, and Getting Through Peer Review",
         "tags": ["Research Methods", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Academic Writing Is For"},
             {"name": "The Argument"},
             {"name": "Structure"},
             {"name": "The Literature Review"},
             {"name": "Sentences and Paragraphs"},
             {"name": "Numbers, Tables and Figures"},
             {"name": "Citation and Integrity"},
             {"name": "The Thesis in India"},
             {"name": "Choosing and Reaching a Journal"},
             {"name": "Peer Review and Revision"},
             {"name": "Authorship, Ethics and Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Academic Writing Is For"},

        {"type": "content", "label": "Definition", "title": "Academic writing is an argument made checkable",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Academic writing",
                        "def": "Prose that makes a claim, shows the evidence and reasoning behind "
                        "it, places it against what others have found, and gives a reader enough "
                        "to disagree. Its distinguishing feature is not vocabulary or length but "
                        "that every step can be checked."},
                       {"t": "body", "html": "A thesis, a journal article, a working paper and a "
                        "policy brief share this contract and differ in audience, length and how "
                        "much of the checking apparatus is shown. The mistakes most writers make "
                        "come from confusing the contract with its costume: long words, passive "
                        "verbs and hedged sentences are not what makes writing academic. Claims "
                        "with evidence are."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "A reader should be able to state your claim in one sentence after the first page.",
                  "Every empirical statement should point to a table, a figure, a source or a calculation the reader can find.",
                  "The reader should know what would have changed your mind, because you have said what evidence would.",
                  "The prose should be no harder than the ideas require. Difficulty that comes from the sentences rather than the content is a defect."]},
                        {"t": "hbox", "color": "amber", "html": "Booth, Colomb and Williams, "
                         "<em>The Craft of Research</em> (4th ed., University of Chicago Press, "
                         "2016) is the one book on this course that every reader should own."}]},
         ]},

        {"type": "content", "label": "Genres", "title": "The genres, and what each one owes the reader",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Genre", "Typical length", "Reader", "What it must do"],
              "rows": [
                  ["Journal article", "6,000&ndash;10,000 words", "Specialists who will check the method", "One contribution, stated early, defended fully, with everything needed to replicate"],
                  ["PhD thesis", "60,000&ndash;100,000 words (social sciences, India)", "Two or three examiners, then almost nobody", "Demonstrate independent research competence; each chapter a defensible unit"],
                  ["Working paper", "As the article, often longer", "Peers before review; the seminar circuit", "Get feedback; establish priority; be citable before the journal"],
                  ["Policy brief", "2&ndash;6 pages", "Officials and funders with ten minutes", "Findings first, recommendations that name an actor, evidence in an annex"],
                  ["Research report (donor)", "30&ndash;80 pages plus annexes", "Programme staff, the commissioning officer", "Answer the terms of reference; executive summary carries the whole thing"],
                  ["Book chapter", "6,000&ndash;9,000 words", "Students and adjacent fields", "Synthesis and argument; less method, more context"],
                  ["Conference paper", "As the article, earlier draft", "A discussant and a room", "Be finished enough to be criticised"]]},
             {"t": "body", "cls": "sm", "html": "The same study can produce four of these. The "
              "error is writing one and relabelling it: a thesis chapter submitted as an article "
              "carries 3,000 words of literature the journal does not want; an article pasted "
              "into a policy brief buries the recommendation on page nine."},
         ]},

        {"type": "content", "label": "The Reader", "title": "Write for the reader who is busy, sceptical and not you",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The reader of an academic paper is reading it "
                        "because it may be useful, not because it is yours. They read the title, "
                        "the abstract, the first figure and the conclusion, in that order, and "
                        "decide whether to read the rest. A referee reads the whole thing looking "
                        "for the reason to reject it. Neither has the context in your head, and "
                        "neither will supply it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Assume intelligence and assume ignorance of your particular study. Explain the setting; do not explain what a regression is.",
                           "Put the claim where the reader looks first: the abstract, the last paragraph of the introduction, the first sentence of the conclusion.",
                           "Anticipate the objection. If a referee will ask about attrition, the paragraph on attrition comes before they think of it."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The curse of knowledge", "html":
                         "Pinker (<em>The Sense of Style</em>, Viking, 2014) names the main cause "
                         "of bad academic prose: the writer cannot remember what it was like not "
                         "to know what they know. Abbreviations that were defined once in chapter "
                         "two, the district that was described in the proposal but not the paper, "
                         "the 'obvious' step in the identification argument. The cure is a reader "
                         "who does not know, and the discipline to believe them when they say "
                         "they were lost."},
                        {"t": "hbox", "color": "cyan", "html": "Give a draft to someone outside the "
                         "sub-field and ask them to mark every sentence they had to read twice. "
                         "Those sentences are the edit list."}]},
         ]},

        {"type": "content", "label": "Two Bad Models", "title": "Two models to unlearn: the school essay and the report",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "The school essay", "html":
                         "Teaches that length shows effort, that the conclusion comes at the end, "
                         "that a topic is an argument, and that quotation is evidence. An Indian "
                         "postgraduate arrives with ten years of it. A journal article does the "
                         "opposite on all four counts: it is as short as the argument allows, "
                         "states the conclusion first, argues a claim rather than surveying a "
                         "topic, and uses quotation only when the wording itself is the evidence."},
                        {"t": "panel", "color": "red", "title": "The consultancy report", "html":
                         "Teaches that every finding gets a bullet, that the executive summary is "
                         "written last and by someone else, that recommendations can float free "
                         "of evidence, and that the audience is the client. Many practitioners "
                         "arrive with ten years of this. Its virtues (findings first, plain "
                         "sentences) carry over. Its habit of asserting rather than showing does "
                         "not."}],
              "right": [{"t": "body", "html": "Both models are fine for what they are. The trouble "
                        "is that neither shows its reasoning in a form a stranger can check, and "
                        "that is the whole difference. An article that reads like an essay gets "
                        "the referee comment 'the contribution is unclear'; one that reads like a "
                        "report gets 'the claims are not supported by the analysis'. Both are "
                        "polite ways of saying the argument is missing."},
                        {"t": "hbox", "color": "green", "html": "The test: could a hostile reader, "
                         "with your data, reproduce your main table and then argue with your "
                         "reading of it? If yes, it is academic writing, whatever it sounds "
                         "like."}]},
         ]},

        {"type": "content", "label": "South Asia", "title": "Writing in English as a second, third or fourth language",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Most researchers in South Asia write academic "
                        "English as a learned register, and most referees at international "
                        "journals read it as native speakers. Two things follow. Simple sentences "
                        "are an advantage, not a limitation: a plain sentence written by a "
                        "second-language writer reads as clear, while an ornate one reads as "
                        "strained. And referees do notice language, unfairly, so the language "
                        "should not give them a reason."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Prefer the short word and the short sentence. Nobody has ever been rejected for clarity.",
                           "Learn the twenty constructions that mark Indian English in referees' eyes (the article system, 'discuss about', 'revert', 'the same' as a pronoun, 'prepone') and decide deliberately which to keep.",
                           "Use a grammar checker for mechanics, never for style; the style suggestions push toward the generic.",
                           "A language edit before submission is money well spent if the journal is international and the argument is sound. It cannot fix an argument."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What not to apologise for", "html":
                         "Indian English is a standard variety with its own dictionary entries. "
                         "Spelling (colour, programme), 'lakh' and 'crore' with the figure in "
                         "millions beside them, Indian place names without gloss for an Indian "
                         "journal: all fine. What to change is only what stops the reader, and "
                         "an editor's job is to say which that is. Be consistent within a "
                         "paper; the journal's style guide decides between British and American "
                         "spelling, and either is correct."},
                        {"t": "hbox", "color": "green", "html": "Write the first draft in whatever "
                         "language you think in, if that is faster. Argument first; English "
                         "second."}]},
         ]},

        {"type": "content", "label": "Time", "title": "How long it takes, honestly",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "12 weeks", "label": "Belcher's plan from a draft to a submitted article, at about an hour a day", "color": "cyan", "source": "Belcher, <em>Writing Your Journal Article in Twelve Weeks</em>, 2nd ed., 2019"},
                 {"num": "6%", "label": "acceptance rate at the top five economics journals by 2012, down from about 15% around 1980", "color": "amber", "source": "Card and DellaVigna, <em>J Econ Lit</em> 2013, 51:144"},
                 {"num": "8 to 16 months", "label": "time a paper spends at one economics journal between submission and acceptance, more than doubled over thirty years", "color": "red", "source": "Ellison, <em>J Polit Econ</em> 2002, 110:947"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The writing is the shorter part. A paper that "
                        "takes three months to draft can take two years to publish, through one "
                        "rejection, a resubmission and two rounds of revision. Plan a pipeline, "
                        "not a paper: something under review, something being revised, something "
                        "being drafted, at all times. A PhD that produces one paper at the end has "
                        "left the pipeline empty for four years."}],
              "right": [{"t": "hbox", "color": "cyan", "html": "The thesis chapter and the article "
                        "should be written as one document with two outputs, from the start. "
                        "Deciding after the viva which chapter becomes a paper costs a year."}]},
         ]},

        {"type": "content", "label": "This Course", "title": "How the course is arranged",
         "blocks": [
             {"t": "flow", "steps": [
                 "ARGUMENT: what you are claiming and why it matters",
                 "STRUCTURE: where each part of the argument goes",
                 "PROSE: sentences and paragraphs that carry it",
                 "EVIDENCE: numbers, tables, figures and citations that support it",
                 "PROCESS: the thesis, the journal, the referees",
                 "ETHICS: authorship, integrity, and AI"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Sections 02 to 07 apply to any genre and any "
                        "discipline in the social sciences and development studies. Sections 08 "
                        "to 11 are about the process, and are written for a researcher in India, "
                        "Bangladesh, Nepal, Pakistan or Sri Lanka submitting to Indian and "
                        "international outlets, with the Indian regulations named because they "
                        "are the ones most readers of this course work under."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Everything here can be read "
                        "alongside Systematic Reviews 101 (for the literature review) and "
                        "Research Ethics 101 (for consent and data). This course is about the "
                        "writing."}]},
         ]},

        # ===================== SECTION 02: THE ARGUMENT =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Argument"},

        {"type": "content", "label": "Question to Claim", "title": "A topic is not a question, and a question is not a claim",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "TOPIC: women's self-help groups in Bihar",
                  "QUESTION: does SHG membership change who decides household spending?",
                  "CLAIM: membership raises the share of decisions women report making alone by 8 points, driven by savings rather than credit",
                  "SO WHAT: the design lesson is the savings component, which is the cheap part"]},
                       {"t": "body", "html": "Most stalled drafts are stuck at the first or "
                        "second step. A paper about a topic has no natural end; a paper answering "
                        "a question ends when the question is answered; a paper making a claim "
                        "can be organised around defending it. Booth, Colomb and Williams call "
                        "the last step the 'so what' and say the reader asks it whether or not "
                        "you answer."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Write the claim before the paper", "html":
                         "One sentence, on a card, before drafting: 'This paper shows that X, "
                         "because Y, which matters for Z.' If the sentence cannot be written, the "
                         "analysis is not finished. If it can, every section of the paper has a "
                         "job: the introduction states it, the data and method make it credible, "
                         "the results show it, the discussion defends it against alternatives, "
                         "the conclusion says what follows."},
                        {"t": "hbox", "color": "amber", "html": "The card changes as the work does. "
                         "Keep the old versions; the distance between the first and the last is "
                         "what you learned."}]},
         ]},

        {"type": "content", "label": "Contribution", "title": "What counts as a contribution, and what does not",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Kind of contribution", "Example", "What the paper must show"],
              "rows": [
                  ["A new finding", "Cash transfers reduce child labour in a setting where nobody had measured it", "That the setting matters and the finding was uncertain before"],
                  ["A better estimate", "The same effect, but identified more credibly or measured on a larger sample", "Why the earlier estimates were doubtful and how this one fixes it"],
                  ["A mechanism", "The effect runs through school fees, not through income", "Evidence that separates the channels, not just a story"],
                  ["A measurement", "A validated scale for women's decision-making in Hindi and Bangla", "Reliability, validity, and what the old measure got wrong"],
                  ["A method", "A cheaper way to sample migrant households", "That it works, against a benchmark, and what it costs"],
                  ["A synthesis", "The evidence on SHGs, read together for the first time", "A systematic method (see Systematic Reviews 101)"],
                  ["A theory or framework", "A model that explains why evaluations disagree", "That it explains something the alternatives do not, with testable implications"]]},
             {"t": "body", "cls": "sm", "html": "Not contributions: applying a standard method "
              "to a new dataset with no reason the answer would differ; describing a programme; "
              "'filling a gap' where the gap exists because nobody needed it filled. Thomson "
              "(<em>A Guide for the Young Economist</em>, 2nd ed., MIT Press, 2011) and "
              "Cochrane's 'Writing Tips for PhD Students' (2005) both put it the same way: the "
              "paper is about one thing, and you should be able to say what it is in the "
              "lift."},
         ]},

        {"type": "content", "label": "The Hourglass", "title": "The shape of an argument: wide, narrow, wide",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Bem's hourglass (in <em>The Compleat Academic</em>, "
                        "2nd ed., 2004) describes almost every good empirical paper. It opens on "
                        "the problem everyone recognises, narrows to the specific question and "
                        "the specific study, spends its middle in the narrow neck of data and "
                        "results, and widens again to what the result means for the problem it "
                        "opened with. A paper that stays narrow reads as a technical note. One "
                        "that stays wide reads as an opinion."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Opening width: one paragraph, at most two. The referee knows child labour is bad.",
                           "The neck: everything the reader needs to believe the number. This is where length is earned.",
                           "Closing width: what follows, for whom, with the certainty the evidence allows. Not a repeat of the results."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The economics variant", "html":
                         "Economics papers front-load the whole hourglass into the introduction: "
                         "problem, question, method, main result with the number, why it is "
                         "credible, what it adds, and a roadmap, in three to five pages. Cochrane "
                         "and Thomson both insist on it. A reader who stops after the "
                         "introduction should know everything except the details. Development "
                         "studies and sociology journals let the introduction stay shorter and "
                         "put the result later; read three recent articles in the target journal "
                         "and copy the shape."},
                        {"t": "hbox", "color": "green", "html": "Whatever the field: the main "
                         "result, with its number, appears in the introduction. Suspense is for "
                         "novels."}]},
         ]},

        {"type": "content", "label": "Anticipating Objections", "title": "The argument includes the case against it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A claim is only as strong as the best objection "
                        "it survives. Referees are paid nothing and read for the reason to "
                        "reject, so the objections they will raise are the ones you should have "
                        "raised first. List them before drafting. For an impact estimate they are "
                        "predictable: selection, attrition, spillovers, measurement, the "
                        "comparison group, external validity, and whether the outcome is the one "
                        "that matters."},
                       {"t": "bullets", "color": "amber", "items": [
                           "Each serious objection gets a named paragraph or subsection, an analysis that addresses it, and a sentence saying how far it is answered.",
                           "'We acknowledge this limitation' is not an answer. Either bound the problem, test for it, or say what the result would be if the objection held.",
                           "Objections you cannot answer go in the limitations, stated precisely, with what evidence would settle them."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The referee's questions, in order", "html":
                         "What is the claim? Is it new? Is the identification credible? Are the "
                         "data adequate? Do the results support the claim as stated, or a weaker "
                         "one? Are the alternatives ruled out? Is the interpretation the right "
                         "size for the evidence? Would I cite this? A paper that answers all "
                         "eight before the referee asks them is a paper that gets a revise "
                         "rather than a reject."},
                        {"t": "hbox", "color": "green", "html": "Present a draft in a seminar "
                         "before submission. Every question asked there is a paragraph the "
                         "paper was missing."}]},
         ]},

        {"type": "content", "label": "Title and Abstract", "title": "The two hundred words most people will read",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The title", "html":
                         "Say what the paper found or asked, in plain words a search engine will "
                         "match. 'Savings, not credit: how self-help groups change household "
                         "decisions in Bihar' beats 'An empirical investigation into the "
                         "socio-economic determinants of intra-household bargaining outcomes'. "
                         "Letchford, Moat and Preis (<em>Royal Society Open Science</em> 2015, "
                         "2:150266) found shorter titles associated with more citations across "
                         "140,000 papers. Colons are fine; questions are fine; puns date."},
                        {"t": "panel", "color": "amber", "title": "The abstract", "html":
                         "150 to 250 words. Setting and question, one sentence. Data and method, "
                         "one or two. Main result with the number and its direction, one or two. "
                         "Mechanism or heterogeneity if it is the point. Implication, one. No "
                         "citations, no abbreviations, no 'this paper explores'. Write it last, "
                         "rewrite it first."}],
              "right": [{"t": "body", "html": "The abstract is indexed, translated, read on phones "
                        "and quoted in policy documents by people who will never open the PDF. "
                        "It should survive all four. A structured abstract (Background, Methods, "
                        "Results, Conclusions) is required by many health journals and is a good "
                        "drafting scaffold even where the final version runs as one paragraph."},
                        {"t": "bullets", "color": "green", "sm": True, "items": [
                            "Keywords: five to eight, including the country, the method and the outcome, none already in the title.",
                            "JEL codes for economics journals; pick three from the classification, not one.",
                            "Highlights or a 'key messages' box where the journal asks: three plain sentences, findings not methods."]}]},
         ]},

        {"type": "content", "label": "The Introduction", "title": "The introduction, paragraph by paragraph",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Paragraph", "Job", "Length"],
                        "rows": [
                            ["1", "The problem, with one number that shows it matters", "4&ndash;6 sentences"],
                            ["2", "What is known and the specific gap or disagreement, three to six citations", "5&ndash;8 sentences"],
                            ["3", "This study: setting, design, data, in enough detail to be credible", "5&ndash;8 sentences"],
                            ["4", "The main result, with its magnitude, and the second result if there is one", "4&ndash;6 sentences"],
                            ["5", "Why the reader should believe it: the identification, the checks", "4&ndash;6 sentences"],
                            ["6", "The contribution, against named papers, in two or three sentences each", "6&ndash;10 sentences"],
                            ["7", "Roadmap, one sentence per section, or omit if the journal dislikes it", "2&ndash;4 sentences"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Seven paragraphs, two to four pages. "
                        "This is the economics form and it transfers well to development "
                        "studies with paragraph 6 shortened. Public health and sociology "
                        "journals prefer a shorter introduction (paragraphs 1, 2, 3) with the "
                        "results held for later; check three recent issues."},
                        {"t": "hbox", "color": "amber", "html": "Paragraph 6 is where most "
                         "rejections are decided. 'Our paper contributes to three literatures' "
                         "followed by three lists is a list, not a contribution. Name the two "
                         "or three closest papers and say exactly what differs."}]},
         ]},

        {"type": "content", "label": "The Conclusion", "title": "The conclusion is not a summary",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A conclusion that restates the results has wasted "
                        "the reader's last two minutes. Its job is to say what follows from the "
                        "results: for the question the paper opened with, for the policy the "
                        "programme belongs to, for the next study. It should be the part of the "
                        "paper a policymaker could read alone and act on, hedged exactly as much "
                        "as the evidence requires and no more."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "One paragraph of findings, in words, without repeating every coefficient.",
                           "One or two paragraphs on what they mean, including for the settings the study did not cover.",
                           "One paragraph on what the study could not do and what would do it, specific enough to fund.",
                           "No new results, no new citations, no 'further research is needed' without saying which."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Policy implications, done properly", "html":
                         "A policy implication names an actor, an action and the evidence for "
                         "expecting the action to work. 'Governments should invest in women's "
                         "empowerment' is none of the three. 'A state SHG programme that adds a "
                         "savings component at about Rs 40 per member per month could expect "
                         "the decision-making effect we measure; whether it survives government "
                         "delivery is the open question' is all three, and it is honest about "
                         "the limit."},
                        {"t": "hbox", "color": "green", "html": "Scale the verb to the evidence: "
                         "'shows' for the main result, 'suggests' for the mechanism, 'is "
                         "consistent with' for the story you like but did not test."}]},
         ]},

        # ===================== SECTION 03: STRUCTURE =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Structure"},

        {"type": "content", "label": "IMRaD", "title": "IMRaD and its social-science variants",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Section", "Health, psychology", "Economics", "Development studies, sociology"],
                        "rows": [
                            ["Introduction", "Short; the question", "Long; result and contribution included", "Medium; context heavy"],
                            ["Background / literature", "In the introduction", "Folded into the introduction", "Often a separate section"],
                            ["Context / setting", "Brief", "A section: the programme, the setting", "A section, often long"],
                            ["Data and methods", "Methods, detailed and standardised", "Data section, then empirical strategy with equations", "Methods, with reflexivity where qualitative"],
                            ["Results", "Tables in order, minimal interpretation", "Results with interpretation woven in", "Findings, thematic where qualitative"],
                            ["Discussion", "Separate; interpretation, limitations", "Merged with results or short", "Separate, often the longest"],
                            ["Conclusion", "Brief", "Short, implications", "Substantive"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "IMRaD (Introduction, Methods, "
                        "Results, and Discussion) is the health-science default and the one "
                        "EQUATOR reporting guidelines (CONSORT, STROBE, PRISMA) assume. "
                        "Economics keeps the parts and renames them; development studies keeps "
                        "them and adds context. None is better. The rule is to use the shape of "
                        "the journal you are sending to, which you find by reading it."},
                        {"t": "hbox", "color": "cyan", "html": "Whatever the headings, the reader "
                         "must be able to find, in under a minute, the sample size, the "
                         "comparison group, the main estimate and its confidence interval."}]},
         ]},

        {"type": "content", "label": "Setting", "title": "The setting section: enough for a stranger, no more",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Development papers need a section the health "
                        "sciences do not: the programme and the place. The reader in Boston does "
                        "not know what a gram panchayat is, what an ASHA does, or that Bihar's "
                        "female labour force participation is among the lowest in India. The "
                        "reader in Patna does, and will be irritated by a page of it. Write for "
                        "the first and keep it to what the argument uses."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The programme: who runs it, what it delivers, to whom, since when, at what cost, with a citation to its own documents.",
                           "The place: the two or three facts about the setting that the identification or the interpretation depends on, with a source for each.",
                           "The timeline: when the programme started, when the data were collected, and anything else that happened in between (a drought, an election, a pandemic).",
                           "A map if geography matters to the design. A photograph never."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What the section is really for", "html":
                         "External validity. A reader deciding whether the result transfers "
                         "needs to know what was particular about this place: the density of "
                         "front-line workers, the presence of other programmes, the local "
                         "wage. Every fact in the setting section should reappear in the "
                         "discussion when you say where the result might and might not "
                         "hold."},
                        {"t": "hbox", "color": "green", "html": "Test: delete a sentence from the "
                         "setting. If nothing later in the paper refers back to it, it was "
                         "tourism."}]},
         ]},

        {"type": "content", "label": "Data", "title": "The data section: what, from whom, how many, how good",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Item", "What to state", "Where"],
              "rows": [
                  ["Source", "Survey name, round, collecting agency, or your own fieldwork with dates and instrument", "First paragraph"],
                  ["Sample", "Frame, sampling design, target and achieved n at each level, response and attrition rates", "Second paragraph and a flow table or diagram"],
                  ["Variables", "Definition of every outcome and key covariate, exactly as measured, with the question wording in an appendix", "Third paragraph; a variable table in the appendix"],
                  ["Descriptives", "Means, SDs and n by group, with a balance test where relevant", "Table 1"],
                  ["Quality", "Missingness, known problems, cleaning decisions, and how the analysis handles them", "Fourth paragraph"],
                  ["Access", "Where the data can be obtained or why they cannot; the replication package", "Final paragraph and a data availability statement"]]},
             {"t": "body", "cls": "sm", "html": "Table 1 is read more than any other. Referees "
              "check that the n matches the text, that the groups look comparable, and that "
              "the outcome's mean is plausible for the setting. Every number in Table 1 should "
              "be reproducible from the replication package by a stranger. The American "
              "Economic Association has required that of every accepted paper since 2019, and "
              "other journals are following."},
         ]},

        {"type": "content", "label": "Methods", "title": "The methods section: the equation, the assumption, the test",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A quantitative methods section has three parts "
                        "and most drafts have one. The <strong>equation</strong> says what was "
                        "estimated, with every term defined and the coefficient of interest "
                        "named. The <strong>assumption</strong> says what has to be true for that "
                        "coefficient to be the effect: parallel trends, the exclusion restriction, "
                        "no manipulation at the threshold. The <strong>test</strong> says what "
                        "evidence the paper offers for the assumption and where the reader can "
                        "see it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Standard errors: clustered at what level and why, stated once, in the text and under every table.",
                           "Pre-registration: the registry, the number, and any departures from the plan, listed.",
                           "Multiple outcomes: the correction used, or the reason none was.",
                           "Software and packages, with versions, in a footnote or the appendix."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Qualitative and mixed methods", "html":
                         "The same three parts in different words. What was done (how many "
                         "interviews, with whom, selected how, over what period, in what "
                         "language, transcribed and translated by whom); what makes it credible "
                         "(the analytic approach, coding, who coded, how disagreements were "
                         "handled, saturation); and how the reader can check (excerpts tied to "
                         "the claims, a reflexivity statement, the codebook in an appendix). "
                         "'Thematic analysis was conducted' is one sentence where a page is "
                         "owed."},
                        {"t": "hbox", "color": "green", "html": "Write the methods so a hostile "
                         "expert with your data would get your Table 2. That is the whole "
                         "standard."}]},
         ]},

        {"type": "content", "label": "Results", "title": "The results section: lead with the finding, not the table",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The weak results paragraph starts 'Table 3 "
                        "presents the estimates' and then reads the table aloud. The strong one "
                        "starts with the finding: 'Membership raises the share of decisions "
                        "women report making alone by 8 percentage points (Table 3, column 2), "
                        "about a quarter of the control mean.' Then the number, the reference, "
                        "the scale, the precision, and only then the secondary columns."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "One paragraph per table or figure, in the order the argument needs, which is not always the order of the analysis.",
                           "Give magnitudes in units a reader can feel: percentage points, share of the control mean, standard deviations, rupees per month.",
                           "Say what is not significant as plainly as what is; a precise zero is a result.",
                           "Robustness checks get one paragraph and an appendix table each, not a section of their own unless one changes the answer."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Words that need care", "html":
                         "<em>Significant</em> means statistically significant and should say "
                         "at what level; for importance use a different word. <em>Effect</em> "
                         "and <em>impact</em> claim causation; use <em>association</em> where "
                         "that is what you have. <em>Marginally significant</em> means not "
                         "significant. <em>Trend toward</em> means nothing. <em>Robust</em> "
                         "means survived the specific checks you ran, which should be listed."},
                        {"t": "hbox", "color": "green", "html": "Every number in the prose must "
                         "match the table to the decimal. Referees check, and one mismatch "
                         "poisons their trust in all the others."}]},
         ]},

        {"type": "content", "label": "Discussion", "title": "The discussion: what it means, why it might be wrong, where it applies",
         "blocks": [
             {"t": "flow", "steps": [
                 "RESTATE the main finding in one sentence, in words",
                 "COMPARE with what earlier studies found, and explain the differences",
                 "MECHANISM: what the evidence says about why, and what it cannot say",
                 "ALTERNATIVES: the explanations you can rule out, and the one you cannot",
                 "APPLICABILITY: where else this would hold, and where it would not, from the setting section",
                 "LIMITS: precisely, with the direction of bias each would produce"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The comparison step is where the paper joins the "
                        "literature. 'Our estimate is larger than Kumar et al. (2019) because "
                        "their sample was urban and the savings channel we identify is weaker "
                        "where banks are near' is a sentence a referee remembers. 'Our findings "
                        "are broadly consistent with the literature' is one they skip."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Limitations are stated with a "
                        "direction. 'Attrition was 12% and higher among migrants, who tend to "
                        "be poorer; if the programme helped them less, our estimate is biased "
                        "upward' tells the reader what to do with the number. 'Attrition is a "
                        "limitation' does not."}]},
         ]},

        {"type": "content", "label": "Appendices", "title": "What goes in the appendix, and what the appendix is for",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Belongs in the appendix", "Belongs in the paper"],
                        "rows": [
                            ["Robustness tables that confirm the main result", "The one robustness check that changes it"],
                            ["Variable definitions and question wording", "The definition of the main outcome"],
                            ["Full regression tables with all covariates", "The coefficient of interest with its standard error"],
                            ["Balance tables beyond Table 1", "Table 1"],
                            ["Attrition analysis, sample flow", "Attrition rate and its direction of bias"],
                            ["Derivations, proofs, simulation details", "The result of the derivation"],
                            ["Interview guides, codebooks", "The analytic approach"],
                            ["Additional figures, maps, photographs of instruments", "The one figure that carries the finding"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Online appendices are unlimited in "
                        "length and read by almost nobody, which makes them the right place for "
                        "everything a referee might ask for and a general reader will not. "
                        "Number them (Appendix Table A1) and refer to each from the main text, "
                        "so a reader who wants the robustness check can find it and one who "
                        "does not can skip it."},
                        {"t": "hbox", "color": "cyan", "html": "A thesis has no online appendix: "
                         "everything is bound together. Examiners still read appendices last, "
                         "so the same division applies, and the thesis chapter's appendix "
                         "becomes the article's online appendix unchanged."}]},
         ]},

        {"type": "content", "label": "Thesis Structure", "title": "The thesis: monograph or three papers",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The monograph", "html":
                         "Introduction; literature; context; theory or framework; methods; two "
                         "to four empirical chapters; discussion; conclusion. One argument "
                         "carried across chapters, with each chapter opening on what it "
                         "contributes to it and closing on what it hands to the next. The "
                         "traditional Indian form, expected by most examiners in the "
                         "humanities and social sciences, and the harder one to turn into "
                         "articles afterwards."},
                        {"t": "panel", "color": "amber", "title": "The three-paper thesis", "html":
                         "An introduction that states the shared question and how the papers "
                         "answer it; three self-contained papers, each publishable, each with "
                         "its own literature, data, methods and conclusion; a concluding "
                         "chapter that reads across them. Standard in economics and increasingly "
                         "accepted in Indian social-science departments, but check the "
                         "university's ordinance, which may require a specific chapter list."}],
              "right": [{"t": "body", "html": "Whichever form, the examiner's questions are the "
                        "same: is there an argument, is it the candidate's own, is the method "
                        "sound, does the evidence support the conclusions, and does the "
                        "candidate know the field. Dunleavy (<em>Authoring a PhD</em>, Palgrave, "
                        "2003) and Murray (<em>How to Write a Thesis</em>, 4th ed., Open "
                        "University Press, 2017) are the two standard guides; Dunleavy is the "
                        "one to read on structure."},
                        {"t": "hbox", "color": "green", "html": "Decide the form in the first "
                         "year with the supervisor, in writing. Changing it in year four means "
                         "rewriting year two."}]},
         ]},

        {"type": "content", "label": "Outlining", "title": "Outline before drafting, reverse-outline after",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "An outline is the argument written as headings "
                        "with one sentence under each saying what that part establishes. It "
                        "should be finished before the prose begins and shown to the supervisor "
                        "or a co-author, because disagreements about structure are cheap to fix "
                        "at this stage and expensive after 8,000 words. The sentence under each "
                        "heading becomes the topic sentence of the section."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Headings are claims where possible: '4.2 The effect runs through savings, not credit', not '4.2 Mechanisms'.",
                           "Every table and figure is placed in the outline before it is made. If it has no place, it is not needed.",
                           "The outline has a word budget per section. Overruns are decided consciously."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Reverse outlining", "html":
                         "After a draft, write one sentence beside each paragraph saying what it "
                         "does. Read only the sentences. Paragraphs that do the same job are "
                         "merged; paragraphs that do two jobs are split; paragraphs whose "
                         "sentence cannot be written are cut; paragraphs out of order are "
                         "moved. It takes an hour on an article and finds the structural "
                         "problems that reading the prose hides, because the prose is yours "
                         "and reads well to you."},
                        {"t": "hbox", "color": "green", "html": "Reverse-outline every draft "
                         "before sending it to anyone. It is the single most useful editing "
                         "technique in this course."}]},
         ]},

        # ===================== SECTION 04: THE LITERATURE REVIEW =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Literature Review"},

        {"type": "content", "label": "Purpose", "title": "A literature review is an argument about the literature",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The annotated bibliography, one paragraph per "
                        "paper in the order they were read, is the commonest failure in Indian "
                        "theses and the reason examiners ask 'what is your argument?' A "
                        "literature review organises what is known around the question the "
                        "thesis asks: what is settled, what is disputed, what is missing, and "
                        "why the missing piece matters. Papers appear where the argument needs "
                        "them, several to a paragraph, and some appear only in a footnote."},
                       {"t": "term", "word": "Literature review",
                        "def": "A structured account of the existing evidence and argument on a "
                        "question, organised by theme, method or finding rather than by author, "
                        "that ends by stating what this study adds and why the existing work "
                        "could not."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Organise by theme, finding or method. Never by author, and never chronologically unless the history is the point.",
                  "Each paragraph makes a claim about the literature ('the evidence on credit is mixed; on savings it is consistent') and cites the papers that support it.",
                  "Disagreement is the interesting part. Where two good studies conflict, say why (setting, method, measure), because that is where your study finds its place.",
                  "End on the gap, stated as a question your data can answer, not as 'no study has examined X in Y'."]},
                        {"t": "hbox", "color": "amber", "html": "For the search itself, use the "
                         "methods in Systematic Reviews 101 even when the review is narrative. "
                         "A search you can describe is a review you can defend."}]},
         ]},

        {"type": "content", "label": "Reading", "title": "Reading for a review: fast, structured, recorded",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Pass", "Read", "Time", "Record"],
                        "rows": [
                            ["1. Triage", "Title, abstract, first figure, conclusion", "5 minutes", "Keep / discard / maybe; one line on why"],
                            ["2. Structure", "Introduction, headings, tables, discussion", "20 minutes", "Question, design, sample, main result with number, setting"],
                            ["3. Close", "Everything, including the appendix", "1&ndash;3 hours", "The identification argument, the limits, what you would ask the authors, exact quotes with page numbers"]]},
                       {"t": "body", "cls": "sm", "html": "Most papers stop at pass 1; the "
                        "twenty closest to your question get pass 3. Keep the record in a "
                        "spreadsheet or in Zotero notes with a fixed set of fields, so that a "
                        "year later the review can be written from the record rather than from "
                        "rereading."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The synthesis matrix", "html":
                         "One row per study, one column per theme or variable the review will "
                         "discuss: setting, design, sample, outcome measure, direction and size "
                         "of effect, main limitation. Sort it by column and the structure of "
                         "the review appears: the studies that agree, the ones that do not, "
                         "and the reason. Every claim in the review then points to a row. "
                         "Examiners can be shown the matrix; some ask for it."},
                        {"t": "hbox", "color": "amber", "html": "Read the primary source. Citing "
                         "a paper for what a textbook says it says is how errors travel for "
                         "decades."}]},
         ]},

        {"type": "content", "label": "Synthesis", "title": "From matrix to paragraph: three moves",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "1. Group", "html":
                         "'Four randomised studies of SHG programmes measure women's decision-"
                         "making (Desai and Joshi 2014; ...). Three find positive effects of "
                         "5&ndash;12 points; one finds none.' The claim is about the group; the "
                         "citations are its evidence."},
                        {"t": "panel", "color": "amber", "title": "2. Explain", "html":
                         "'The null result comes from the only study in which groups had no "
                         "savings component, which is consistent with the mechanism we test.' "
                         "Disagreement explained is a contribution of the review itself."},
                        {"t": "panel", "color": "green", "title": "3. Position", "html":
                         "'None of the four separates the savings and credit channels; the "
                         "designs bundle them. We do, by exploiting the staggered introduction "
                         "of credit across blocks.' The gap is specific, and the study is "
                         "placed in it."}],
              "right": [{"t": "body", "html": "Three moves, one paragraph each, repeated for "
                        "every theme. The review can be four paragraphs in an article or forty "
                        "pages in a thesis and the moves are the same. What changes is how many "
                        "themes and how much explanation each disagreement gets."},
                        {"t": "bullets", "color": "cyan", "sm": True, "items": [
                            "Quote only when the wording is the evidence (a definition, a contested claim). Paraphrase everything else, with the citation.",
                            "Cite the finding, not the paper's existence: 'Kumar (2019) finds X', not 'Kumar (2019) studied X'.",
                            "Cite the original, not the review that cited it, unless the review's synthesis is the point."]}]},
         ]},

        {"type": "content", "label": "Grey Literature", "title": "Reports, working papers and the evidence that is not in journals",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "In development, a large share of the evidence "
                        "lives in evaluation reports, working papers, government documents and "
                        "NGO studies that never reach a journal. A review that ignores them "
                        "misses the programme-scale evidence and over-weights the small academic "
                        "studies. A review that treats them as equal to peer-reviewed work "
                        "invites the examiner's question about quality. The answer is to use "
                        "them, appraise them, and say so."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Sources: 3ie's repository, J-PAL and IPA evaluation pages, World Bank Policy Research Working Papers, NBER, IZA, RePEc, IDS and ODI, the implementing agency's own reports.",
                           "Cite them fully: author or organisation, year, title, series and number, publisher, URL, date accessed.",
                           "Appraise them as you would a paper: design, sample, who paid, whether the outcome was pre-specified.",
                           "Prefer the working paper's later published version where one exists, and note differences between them."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Government data and documents", "html":
                         "Census tables, NFHS and PLFS reports, budget documents, programme "
                         "guidelines and CAG audits are primary sources and should be cited as "
                         "such, with the issuing body as author, the exact title, the year and "
                         "table number. 'According to government data' is not a citation. Where "
                         "a figure has been revised, cite the version used and the date."},
                        {"t": "hbox", "color": "green", "html": "Wikipedia, news reports and blog "
                         "posts are pointers, not sources. Follow them to the document they "
                         "summarise and cite that."}]},
         ]},

        {"type": "content", "label": "Theory", "title": "The theoretical framework, when one is needed",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Many Indian theses carry a 'theoretical "
                        "framework' chapter because the ordinance expects one, and many of those "
                        "chapters summarise three theories and use none of them. A framework "
                        "earns its place by doing work: it says what mechanisms to look for, "
                        "which variables matter and why, and what pattern of results would "
                        "support or undermine it. If a chapter of theory changes nothing in "
                        "the empirical chapters, it is decoration."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "State the theory in the form of testable implications: 'if bargaining power works through the threat point, effects should be larger where women's outside options are worse'.",
                           "One framework, argued for, beats three described. Say why the alternatives fit less well.",
                           "Return to the theory in the discussion. The results either supported its implications or they did not, and either is worth saying."]}],
              "right": [{"t": "panel", "color": "amber", "title": "In economics", "html":
                         "The theory section is often a simple model whose comparative statics "
                         "are the hypotheses. It should be as simple as will produce the "
                         "predictions the empirics test, and no simpler; a model with no "
                         "empirical implication is a model for a different paper. If the "
                         "predictions are obvious without algebra, state them in words and "
                         "put the model in an appendix."},
                        {"t": "hbox", "color": "green", "html": "Test: name the result in your "
                         "empirical chapters that would have come out differently under a "
                         "different framework. If you cannot, the framework is not doing "
                         "anything."}]},
         ]},

        {"type": "content", "label": "Keeping Current", "title": "A review dated the year the thesis started is a review examiners notice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A four-year PhD produces a literature review "
                        "written in year one and defended in year five. Examiners look for the "
                        "gap. The fix is cheap: saved searches with email alerts in Google "
                        "Scholar and Scopus, a table-of-contents alert for the six journals "
                        "closest to the topic, and RePEc's NEP reports for the working papers. "
                        "One hour a fortnight keeps the review current; a month before "
                        "submission does not."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Re-run the search the month before submission and update the synthesis matrix, not just the reference list.",
                           "A new paper that scoops the study is not a disaster; it is a comparison. Say what differs and what your study adds.",
                           "Cite by year of publication, and give the working-paper year in brackets where the gap is large enough to matter for priority."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Zotero, and why it is not optional", "html":
                         "A reference manager stores every paper with its PDF and notes, inserts "
                         "citations in Word, LibreOffice or Google Docs, and rebuilds the "
                         "bibliography in any style in seconds. Zotero is free and open, works "
                         "offline, and with the Better BibTeX plugin feeds LaTeX and Quarto. "
                         "Starting a thesis without one means retyping four hundred references "
                         "by hand in the last month, in the wrong style, with errors that "
                         "examiners find."},
                        {"t": "hbox", "color": "green", "html": "Set it up in week one. Import "
                         "every paper you read, and add the note the same day."}]},
         ]},

        {"type": "content", "label": "Length", "title": "How long the review should be, by genre",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Genre", "Literature review", "Where it sits", "Notes"],
              "rows": [
                  ["Economics article", "1&ndash;2 pages, inside the introduction", "Paragraphs 2 and 6 of the introduction", "Named papers, specific differences, no survey"],
                  ["Development studies article", "2&ndash;4 pages, own section", "After the introduction", "Thematic; positions the paper in a debate"],
                  ["Health article", "3&ndash;6 paragraphs, inside the introduction", "Introduction", "Cites the systematic reviews, then the direct comparators"],
                  ["Sociology, political science article", "3&ndash;6 pages", "Own section, often with theory", "Argument with the literature is a large part of the contribution"],
                  ["PhD thesis (monograph)", "25&ndash;60 pages", "Chapter 2, sometimes 2 and 3", "Demonstrates command of the field; still an argument, not a catalogue"],
                  ["PhD thesis (three papers)", "Short in each paper, plus a framing chapter", "Introduction and each paper", "The framing chapter reads across the three"],
                  ["Policy brief", "One paragraph or a box", "After the summary", "'What the evidence says', three to five citations"]]},
             {"t": "body", "cls": "sm", "html": "Lengths are typical, not rules; the target "
              "journal's recent articles set the norm. The examiner's expectation in India is "
              "the widest gap: a 60-page chapter is expected in many humanities departments "
              "and would be cut to six by an economics supervisor. Ask the supervisor for two "
              "recent theses from the department that passed well, and measure."},
         ]},

        # ===================== SECTION 05: SENTENCES AND PARAGRAPHS =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Sentences and Paragraphs"},

        {"type": "content", "label": "Clarity", "title": "Clear writing is a set of habits, and the habits can be listed",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Williams and Bizup (<em>Style: Lessons in Clarity "
                        "and Grace</em>, 12th ed., Pearson, 2017) reduce clarity to two rules "
                        "that cover most cases: make the main characters of the sentence its "
                        "grammatical subjects, and make their main actions its verbs. 'An "
                        "increase in enrolment was observed following the implementation of "
                        "the transfer' has no character and no action. 'Enrolment rose after "
                        "the transfer began' has both. Almost every unclear academic sentence "
                        "breaks one of the two."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Nominalisations (implementation, utilisation, examination) hide the verb. Turn them back: implement, use, examine.",
                           "The passive is fine when the actor is unknown or unimportant ('the data were collected in 2023') and a fault when it hides who did what ('mistakes were made').",
                           "Long subjects delay the verb. Keep subject and verb within seven words of each other.",
                           "One idea per sentence; twenty-five words on average; a long sentence beside a short one."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Before and after", "html":
                         "<em>Before</em>: 'The utilisation of a difference-in-differences "
                         "estimation strategy was undertaken in order to facilitate the "
                         "identification of the causal impact of programme exposure on the "
                         "educational outcomes of children in beneficiary households.' (33 "
                         "words, no character, one buried action.)<br><br>"
                         "<em>After</em>: 'We use difference-in-differences to estimate the "
                         "programme's effect on children's schooling.' (13 words.) Nothing "
                         "was lost."},
                        {"t": "hbox", "color": "green", "html": "Orwell's sixth rule (1946): "
                         "break any of these rules sooner than say anything outright "
                         "barbarous. The rules serve the reader, not the other way round."}]},
         ]},

        {"type": "content", "label": "Position", "title": "Where the reader looks: topic position and stress position",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Gopen and Swan ('The Science of Scientific "
                        "Writing', <em>American Scientist</em> 1990, 78:550) showed that readers "
                        "expect the beginning of a sentence to tell them what it is about (the "
                        "topic position) and the end to carry the new or important information "
                        "(the stress position). A sentence that puts the new information first "
                        "and trails off into old information reads as confusing even when every "
                        "word is right."},
                       {"t": "panel", "color": "cyan", "title": "Old before new", "html":
                         "'Membership raised women's decision-making. <em>This effect</em> is "
                         "larger in villages with no bank branch. <em>Distance to a bank</em> "
                         "is also where the savings channel should matter most.' Each sentence "
                         "opens on something the previous one established and ends on the "
                         "next step. The reader is never lost."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Put the thing you want the reader to remember at the end of the sentence, after the last comma.",
                  "Put the thing the sentence is about at the start, and keep it the same across a paragraph unless you signal a change.",
                  "Keep the subject and its verb together; a twenty-word interruption between them loses the reader.",
                  "Use 'this' with a noun ('this effect', 'this estimate'); a bare 'this' makes the reader guess. McCloskey (<em>Economical Writing</em>, 3rd ed., University of Chicago Press, 2019) lists it among the worst habits in economics prose.",
                  "Numbers and names go in the stress position too: 'The effect is 8 percentage points', not '8 percentage points is the effect'."]},
                        {"t": "hbox", "color": "green", "html": "Read the last word of each "
                         "sentence in a paragraph. If they are all prepositions, dates and "
                         "citations, the stress positions are wasted."}]},
         ]},

        {"type": "content", "label": "Paragraphs", "title": "The paragraph: one claim, its support, a link forward",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "TOPIC SENTENCE: the claim, in one sentence a reader could skim",
                  "SUPPORT: the evidence, example, number or citation, two to six sentences",
                  "QUALIFICATION: the limit or the exception, if any",
                  "LINK: the sentence that hands over to the next paragraph"]},
                       {"t": "body", "html": "A reader skimming the first sentence of every "
                        "paragraph should get the whole argument. That is the test: copy the "
                        "topic sentences into a file, read them in order, and see if they make "
                        "a case. Where they do not, the paragraph is either doing two jobs, "
                        "doing none, or opening on a detail rather than the claim."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Length: 100 to 200 words in an article; a single-sentence paragraph is allowed once in a while for emphasis and never for a citation.",
                  "One paragraph, one claim. Two claims means two paragraphs, even if each is short.",
                  "Transitions come from content ('The savings channel implies...'), not from connective words. 'Moreover', 'furthermore' and 'additionally' announce that nothing connects.",
                  "The last sentence of a paragraph is a stress position for the whole paragraph. Do not spend it on a citation."]},
                        {"t": "hbox", "color": "amber", "html": "Paragraphs in a thesis chapter "
                         "run longer than in an article. The structure does not change; the "
                         "support does."}]},
         ]},

        {"type": "content", "label": "Hedging", "title": "Hedging: exactly as much as the evidence needs",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Evidence", "Verb", "Example"],
                        "rows": [
                            ["Randomised, precise, direct", "shows, finds, raises, reduces", "'The transfer raises enrolment by 6 points.'"],
                            ["Credible quasi-experiment", "finds, indicates; 'effect' with the design named", "'Difference-in-differences estimates indicate an effect of 6 points.'"],
                            ["Correlational", "is associated with, predicts", "'Membership is associated with higher enrolment.'"],
                            ["Mechanism inferred, not tested", "suggests, is consistent with", "'The pattern suggests a savings channel.'"],
                            ["Speculation", "may, could, one possibility is", "'One possibility is that husbands' migration mattered.'"],
                            ["Not supported", "does not", "'We find no evidence that credit alone changes decisions.'"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "The two failures are symmetrical. "
                        "Over-hedging ('it may perhaps be suggested that there could be some "
                        "tendency') tells the reader you do not believe your own result. "
                        "Under-hedging ('proves', 'demonstrates conclusively', 'impact' for a "
                        "cross-sectional correlation) is a claim the evidence cannot carry, and "
                        "a referee will name it. Pick the verb from the row the evidence "
                        "belongs to, use it once, and do not stack qualifiers on it."},
                        {"t": "hbox", "color": "amber", "html": "Sword (<em>Stylish Academic "
                         "Writing</em>, Harvard University Press, 2012) found that the "
                         "most-read academics hedge less and say 'I' or 'we' more. Confidence "
                         "with precision reads as authority; vagueness reads as doubt."}]},
         ]},

        {"type": "content", "label": "Words", "title": "Words to cut, words to replace, words to keep",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Cut", "Why"],
                        "rows": [
                            ["very, quite, rather, somewhat, fairly", "Intensifiers and softeners that carry no information"],
                            ["it is important to note that; it should be mentioned that", "Say the thing"],
                            ["in order to; due to the fact that; in terms of", "to; because; delete"],
                            ["the present study; the current paper", "this study; we"],
                            ["respectively", "Rewrite so each number sits beside its noun"],
                            ["utilise, methodology, conceptualise", "use, method, think of"],
                            ["a number of, a majority of", "the number"]]}],
              "right": [{"t": "table",
                         "head": ["Keep", "Why"],
                         "rows": [
                             ["Technical terms, defined once", "'Heteroskedasticity' is shorter than its definition"],
                             ["'I' and 'we'", "Every major style guide now permits them; the passive to avoid them is worse"],
                             ["Short Anglo-Saxon verbs: show, find, use, give, mean", "Clear, and no referee has ever objected"],
                             ["Numbers as figures from 10 up; words below", "Journal style varies; be consistent"],
                             ["'Because', not 'as' or 'since'", "'As' and 'since' also mean time"],
                             ["Indian terms with a gloss on first use", "'panchayat (elected village council)'"]]},
                        {"t": "hbox", "color": "cyan", "html": "After the first draft, search "
                         "the document for each word in the left column. Most drafts lose "
                         "10% of their length and nothing else."}]},
         ]},

        {"type": "content", "label": "Jargon", "title": "Jargon, abbreviations and the reader from the next field",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A technical term is jargon only when the reader "
                        "does not need it. 'Intention-to-treat' saves a paragraph for the "
                        "reader who knows it and costs a footnote for the one who does not; "
                        "keep it and define it once. 'Leveraging synergies to operationalise "
                        "the empowerment paradigm' saves nothing for anyone. The test is "
                        "whether the term has a definition the field agrees on."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Define each technical term at first use, in the text, not in a glossary the reader will not find.",
                           "Abbreviations: define at first use, use consistently, and limit to five or six a paper. A reader who has to look back for 'WEE', 'SHG', 'CCT' and 'DiD' in one sentence stops reading.",
                           "Never abbreviate something used fewer than four times. Never start a sentence with an abbreviation.",
                           "Development-sector abbreviations (MEL, ToC, LFA, IEC) are unknown outside the sector. Spell them out for a journal."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Discipline dialects", "html":
                         "Economists say 'treatment', 'identification' and 'exogenous'; "
                         "sociologists say 'intervention', 'causal claim' and 'external'. Public "
                         "health says 'exposure' and 'confounder'; development studies says "
                         "'programme' and 'context'. A paper submitted to a journal in one "
                         "field using another field's dialect reads as foreign before the "
                         "argument starts. Read the target journal and borrow its words for "
                         "the same ideas."},
                        {"t": "hbox", "color": "green", "html": "Give the draft to a colleague "
                         "from the neighbouring discipline. Every word they query is a word to "
                         "define or replace."}]},
         ]},

        {"type": "content", "label": "Revision", "title": "Drafting and revising are different jobs on different days",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The first draft's job is to exist. Write it "
                        "fast, badly, from the outline, without stopping to fix sentences, and "
                        "with placeholders where a number or a citation is missing. Revising "
                        "while drafting produces a beautiful first page and no paper. Belcher's "
                        "twelve-week plan and every writing coach since Boice have made the same "
                        "point: short daily sessions, drafted forward, revised later."},
                       {"t": "flow", "steps": [
                           "DRAFT: from the outline, fast, with [TK] placeholders",
                           "STRUCTURE: reverse outline; move, merge, cut paragraphs",
                           "ARGUMENT: check every claim against its evidence and its hedge",
                           "SENTENCES: characters, actions, stress positions, cuts",
                           "SURFACE: numbers, citations, spelling, style guide, references"]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Revise in passes, each with one question. Trying to fix structure and commas in one read fixes the commas.",
                  "Read the draft aloud, or have the computer read it. Sentences that cannot be spoken cannot be read.",
                  "Leave it for a week between passes if the deadline allows. What was clear on Friday is not on Monday, and Monday is right.",
                  "Cut 10% at the end. Every draft has it."]},
                        {"t": "hbox", "color": "amber", "html": "Version the drafts (v1, v2, "
                         "supervisor comments, v3) and never edit the only copy. A cloud "
                         "folder or a Git repository; the choice matters less than the "
                         "habit."}]},
         ]},

        {"type": "content", "label": "Feedback", "title": "Getting and using comments",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Comments on a draft are the cheapest research "
                        "input there is and the one PhD students in India most often go "
                        "without, because supervisors are busy and peers are competitors. Build "
                        "the habit anyway: a writing group of three who exchange drafts monthly, "
                        "a seminar slot, a colleague in another department. Ask for specific "
                        "things: 'Is the claim clear by page 2? Where did you stop believing "
                        "me?'"},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Treat every comment as data about a reader, even when it is wrong. A wrong comment means the text let the reader go wrong.",
                           "Do not defend the draft in the meeting. Write the comments down, decide later.",
                           "Reply to the commenter with what you changed. It is how you get a second round.",
                           "A supervisor who returns a draft after four months needs a shorter draft and a deadline agreed in advance."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Reading the supervisor's silence", "html":
                         "Indian supervisors often correct grammar and leave the argument "
                         "alone, either from courtesy or from pressure of time. The grammar "
                         "corrections are welcome; the silence on the argument is not "
                         "approval. Ask directly: 'Is the contribution enough for the "
                         "thesis?' and 'Which chapter is weakest?' Both questions are "
                         "answerable in one sentence and both are asked too late."},
                        {"t": "hbox", "color": "green", "html": "Thank people in the "
                         "acknowledgements by name and for what they did. It costs nothing and "
                         "it is the record of who helped."}]},
         ]},

        {"type": "content", "label": "Tools", "title": "Writing tools: Word, LaTeX, Quarto, and what each is for",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Use it when", "Trade-off"],
              "rows": [
                  ["Word or LibreOffice Writer with Zotero", "Free (LibreOffice) or licensed", "Co-authors and supervisors use it; the journal requires .docx; tracked changes matter", "Equations, cross-references and large documents are fragile"],
                  ["Google Docs with Zotero", "Free", "Live co-writing with a team; comments in place", "Weak reference and figure handling; export to Word for submission"],
                  ["LaTeX (Overleaf or local)", "Free", "Economics journals, equations, a thesis with many cross-references, consistent numbering", "Learning curve; supervisors may not read it; Overleaf's free tier is limited"],
                  ["Quarto or R Markdown", "Free", "Papers whose tables and figures come straight from code; reproducibility; one source for PDF, Word and HTML", "The document is code; co-authors need the toolchain"],
                  ["Plain text with Markdown, then Pandoc", "Free", "Drafting without formatting distractions; version control with Git", "Converting to journal templates takes a step"],
                  ["Grammar checkers", "Free tier", "Mechanics: agreement, articles, spelling", "Style suggestions push toward the bland; ignore them"]]},
             {"t": "body", "cls": "sm", "html": "For an Indian social-science PhD, Word with "
              "Zotero is still the safe default because the university's thesis template and "
              "the supervisor's habits assume it. For economics, LaTeX from the start. For "
              "anyone whose results come from R or Stata, Quarto removes the copying of "
              "numbers by hand, which is where the errors referees find come from."},
         ]},

        # ===================== SECTION 06: NUMBERS, TABLES AND FIGURES =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Numbers, Tables and Figures"},

        {"type": "content", "label": "Numbers in Prose", "title": "Writing numbers so they can be read",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Rule", "Example"],
                        "rows": [
                            ["Two significant figures in prose, more in tables", "'about 8 points', not '8.37 percentage points'"],
                            ["Percent vs percentage points", "Enrolment rose from 75% to 81%: 6 percentage points, or 8 percent"],
                            ["Give the base", "'6 points, from a control mean of 75%'"],
                            ["Give the precision", "'8 points (95% CI 3 to 13)' or '(SE 2.5)'"],
                            ["Give the scale", "'about 0.2 standard deviations' or 'a quarter of the control mean'"],
                            ["Lakh and crore with the international figure", "'Rs 12 crore (Rs 120 million, about US$1.4 million)'"],
                            ["Currency year", "'in 2023 rupees'"],
                            ["Units every time", "'per household per month'"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Ehrenberg ('Rudiments of numeracy', "
                        "<em>Journal of the Royal Statistical Society A</em> 1977, 140:277) "
                        "made the case for rounding half a century ago: a reader cannot hold "
                        "'8.37' and '6.92' in mind to compare them, and can hold '8' and '7'. "
                        "The table keeps the decimals; the sentence rounds them. A p-value in "
                        "prose is 'p = 0.03', never 'p = 0.0312' and never 'p &lt; 0.05' when "
                        "the exact value is known."},
                        {"t": "hbox", "color": "amber", "html": "'Increased by 200%' and "
                         "'increased threefold' mean the same thing and readers get both wrong. "
                         "Say 'tripled' or give both numbers."}]},
         ]},

        {"type": "content", "label": "Tables", "title": "A table is an argument in rows and columns",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Title says what the table shows, including the outcome and the sample: 'Effect of SHG membership on women's decision-making, treatment villages, 2023'.",
                  "Rows are what you compare; columns are what you compare them across. Readers compare down a column more easily than along a row (Ehrenberg).",
                  "Order rows by size or by logic, never alphabetically, unless the reader will look things up.",
                  "Two or three significant figures. Align decimals. No vertical lines, and horizontal lines only above and below the header and at the foot.",
                  "Standard errors in parentheses under the coefficient, or confidence intervals in a column; say which, once, in the note.",
                  "The note carries everything needed to read the table alone: sample, controls, clustering, significance convention, data source."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The regression table", "html":
                         "Columns are specifications, from the sparest on the left to the "
                         "fullest on the right, so the reader sees what each addition does. The "
                         "coefficient of interest is the first row. Controls appear as a row of "
                         "Yes/No, not as thirty coefficients. n, the control mean and R&sup2; "
                         "close the table. Significance stars are still common; several "
                         "journals now prefer standard errors or intervals alone, and a table "
                         "that reads well without stars is a better table."},
                        {"t": "hbox", "color": "green", "html": "Generate the table from code "
                         "(<em>modelsummary</em> in R, <em>estout</em> in Stata) and never "
                         "retype a number. The transcription error is the one referees find."}]},
         ]},

        {"type": "content", "label": "Figures", "title": "When a figure beats a table, and how to draw it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A table is for looking numbers up; a figure is "
                        "for seeing a pattern. A trend over eight years, an event-study plot, "
                        "the distribution of an outcome in two groups, heterogeneity across "
                        "twenty districts: figures. Four coefficients with standard errors: a "
                        "table. Schwabish ('An economist's guide to visualizing data', "
                        "<em>Journal of Economic Perspectives</em> 2014, 28:209) is the short "
                        "guide; Tufte's data-ink ratio is the principle behind it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Show the data, not the decoration: no 3-D, no gridlines heavier than the data, no legend when labels can sit on the lines.",
                           "Axes start at zero for bars; not necessarily for lines. Label them with units.",
                           "Confidence intervals on every estimate plotted. A coefficient plot without them is a drawing.",
                           "One message per figure, stated in the title: 'Effects appear only after the second year'.",
                           "Greyscale-safe and colour-blind-safe; a fifth of readers print, and one in twelve men cannot separate red from green."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Chart types that earn their place", "html":
                         "Line for time; dot-and-interval for coefficients; bar for a few "
                         "categories; histogram or density for a distribution; scatter with a "
                         "fitted line for a relationship; small multiples for the same plot "
                         "across groups. Pie charts almost never (Cleveland and McGill, "
                         "<em>JASA</em> 1984, 79:531, showed readers judge angles badly); "
                         "stacked bars only when the total matters more than the parts."},
                        {"t": "hbox", "color": "green", "html": "Export as vector (PDF, SVG, EPS) "
                         "for print and at 300 dpi for raster. A screenshot of a chart is a "
                         "desk-reject signal at most journals."}]},
         ]},

        {"type": "content", "label": "Equations", "title": "Equations: numbered, defined, and readable as sentences",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The estimating equation", "html":
                         "<em>Y<sub>ivt</sub> = &alpha; + &beta; SHG<sub>v</sub> &times; "
                         "Post<sub>t</sub> + &gamma;<sub>v</sub> + &delta;<sub>t</sub> + "
                         "X&prime;<sub>ivt</sub>&theta; + &epsilon;<sub>ivt</sub></em> &nbsp;(1)<br><br>"
                         "'where <em>Y<sub>ivt</sub></em> is the decision-making index for "
                         "woman <em>i</em> in village <em>v</em> in year <em>t</em>; "
                         "<em>SHG<sub>v</sub></em> is 1 for treatment villages; "
                         "<em>Post<sub>t</sub></em> is 1 after 2021; <em>&gamma;<sub>v</sub></em> "
                         "and <em>&delta;<sub>t</sub></em> are village and year fixed effects; "
                         "<em>X</em> is a vector of household controls; and standard errors "
                         "are clustered at the village level. The coefficient of interest is "
                         "<em>&beta;</em>.'"},
                        {"t": "body", "cls": "sm", "html": "Every symbol defined in the sentence "
                         "after the equation, in the order it appears; the coefficient of "
                         "interest named; the error structure stated. The equation is part of "
                         "the sentence and takes its punctuation."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Number every displayed equation and refer to it by number. Inline equations only for a single term.",
                  "Use the same symbol for the same thing throughout; a thesis with three different notations for the outcome across chapters is three papers stapled together.",
                  "Log means natural log in economics; say so once if any reader might assume otherwise.",
                  "Hats for estimates, no hats for parameters. Bold for vectors, or a prime for transposes, consistently.",
                  "A theory section's model gets the same treatment: assumptions numbered, results stated as propositions, proofs in the appendix."]},
                        {"t": "hbox", "color": "green", "html": "If the paper has one equation, "
                         "it can be written in words. If it has ten, use LaTeX; Word's equation "
                         "editor breaks at about eight."}]},
         ]},

        {"type": "content", "label": "Descriptive Tables", "title": "Table 1 and the balance table",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["", "Treatment (n = 1,204)", "Control (n = 1,187)", "Difference", "p"],
                        "rows": [
                            ["Woman's age (years)", "34.2 (8.1)", "34.6 (8.4)", "&minus;0.4", "0.29"],
                            ["Completed primary school (share)", "0.41 (0.49)", "0.39 (0.49)", "0.02", "0.41"],
                            ["Household size", "5.6 (2.1)", "5.5 (2.0)", "0.1", "0.35"],
                            ["Monthly consumption (Rs, 2023)", "9,840 (4,210)", "9,610 (4,050)", "230", "0.22"],
                            ["Distance to bank branch (km)", "6.8 (4.9)", "6.5 (4.7)", "0.3", "0.18"],
                            ["Decision-making index (0&ndash;1)", "0.32 (0.21)", "0.31 (0.20)", "0.01", "0.44"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. Means with standard "
                        "deviations in parentheses; the note would state the survey round, "
                        "that p-values are from a regression of each variable on treatment "
                        "with village-clustered standard errors, and the joint F-test."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the reader checks", "html":
                         "That n matches the text. That the means are plausible for the "
                         "setting (a consumption figure that is double the state average will "
                         "be queried). That the groups are balanced, and, if not, that the "
                         "imbalance is discussed and controlled. That the outcome's baseline "
                         "mean is here, because every later effect is read against it. A "
                         "qualitative study's Table 1 lists participants by the "
                         "characteristics that sampling was designed around."},
                        {"t": "hbox", "color": "amber", "html": "Do not star a balance table. "
                         "With twenty variables, one is 'significant' by chance and readers "
                         "over-read it; report the joint test instead."}]},
         ]},

        {"type": "content", "label": "Qualitative Evidence", "title": "Presenting interviews and documents",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Qualitative findings are evidence too, and they "
                        "are presented badly more often than numbers are: a claim, a long "
                        "quotation that half-supports it, and the next claim. A quotation is "
                        "an exhibit. It gets an introduction saying what it shows, the excerpt "
                        "itself with an identifier (role, place, date), and a sentence after it "
                        "saying how it supports the claim and how typical it was."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Say how many participants said something like this, and who said the opposite. 'Several' is not a number.",
                           "Translate into English and keep the original phrase where the wording matters, in brackets or a footnote.",
                           "Anonymise consistently (Respondent 14, ASHA, Gaya district) and say how in the methods.",
                           "Documents are cited like any source: issuing body, title, date, page."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Tables for qualitative work", "html":
                         "A matrix of themes by participant group, with counts or with "
                         "representative phrases in the cells, shows the pattern a page of "
                         "quotations hides. A table of participants (role, sex, district, "
                         "number interviewed) replaces a paragraph. A code tree in the "
                         "appendix shows the reader how the themes were built. None of this "
                         "makes the work quantitative; it makes it checkable."},
                        {"t": "hbox", "color": "green", "html": "The most persuasive qualitative "
                         "paragraph is a claim, one short exact quotation, and the number of "
                         "people who agreed and disagreed."}]},
         ]},

        {"type": "content", "label": "Reproducibility", "title": "The replication package is part of the paper",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A replication package is the data (or the "
                        "instructions to obtain it), the code that turns raw data into every "
                        "table and figure, a README saying how to run it, and the software "
                        "versions. AEA journals have required and checked one since 2019; "
                        "<em>World Development</em>, the <em>Journal of Development Economics</em> "
                        "and most health journals require a data availability statement and "
                        "increasingly the code. A thesis examiner can ask for it, and some "
                        "Indian universities now require data deposit with the thesis."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "One script that runs everything from raw data to the last figure. If a number in the paper cannot be traced to a line of code, it is not reproducible.",
                           "Deposit on a repository with a DOI: Harvard Dataverse, Zenodo, OSF, ICPSR's openICPSR. A personal website is not a repository.",
                           "Where data cannot be shared (identifiable, licensed), share the code and a synthetic or restricted-access version, and say how a reader can request the real one.",
                           "Consent forms should have said this would happen. See Research Ethics 101."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters beyond the rule", "html":
                         "Building the package before submission is when the errors are "
                         "found: the table made from an older data version, the figure whose "
                         "axis was mislabelled, the coefficient copied from the wrong column. "
                         "Every one of those is a correction after publication if a reader "
                         "finds it first. Quarto and Stata's <em>dyndoc</em> remove the copying "
                         "step altogether."},
                        {"t": "hbox", "color": "green", "html": "Run the package on a clean "
                         "machine before submitting. If it does not run for you, it will not "
                         "run for the data editor."}]},
         ]},

        # ===================== SECTION 07: CITATION AND INTEGRITY =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Citation and Integrity"},

        {"type": "content", "label": "Why Cite", "title": "Citation is the checking apparatus, not a courtesy",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A citation tells the reader where a claim came "
                        "from so they can check it, gives credit to the person who did the "
                        "work, and shows where the paper sits in the literature. All three "
                        "matter, and the first is the one that makes writing academic. A "
                        "claim without a citation is either the author's own finding, common "
                        "knowledge, or unsupported, and the reader should be able to tell "
                        "which."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Cite for every factual claim that is not yours and not common knowledge. 'India's female labour force participation is among the lowest in the world' needs a source and a year.",
                           "Cite the specific work, not the author's oeuvre; a page number for a quotation or a specific figure.",
                           "Cite what you read. A source read only through another source is cited as 'X, cited in Y'.",
                           "Do not cite to decorate. Twelve citations after a platitude signal a padded review."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Common knowledge", "html":
                         "What a reader of the target journal would know without looking it "
                         "up. That randomisation balances covariates in expectation: common "
                         "knowledge in economics, cite it in a nursing journal. That Bihar is "
                         "in eastern India: common knowledge. That Bihar's per capita income "
                         "is the lowest among Indian states: a fact that changes, so cite it "
                         "with the year. When in doubt, cite."},
                        {"t": "hbox", "color": "green", "html": "Self-citation is fine when the "
                         "earlier work is the source. Self-citation to raise a count is visible "
                         "and counts against you."}]},
         ]},

        {"type": "content", "label": "Styles", "title": "Citation styles: what each looks like and who uses it",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Style", "In text", "Reference list", "Used by"],
              "rows": [
                  ["APA 7th (2019)", "(Kumar & Sen, 2019, p. 12)", "Kumar, A., & Sen, R. (2019). Title in sentence case. <em>Journal, 12</em>(3), 100&ndash;120. https://doi.org/...", "Psychology, education, public health, many Indian social-science departments"],
                  ["Chicago author-date, 18th (2024)", "(Kumar and Sen 2019, 12)", "Kumar, Anil, and Rina Sen. 2019. 'Title in Headline Case.' <em>Journal</em> 12 (3): 100&ndash;20.", "Economics journals (variants), development studies"],
                  ["Chicago notes-bibliography", "Footnote 1", "Full note first time, short note after, plus bibliography", "History, law, some humanities"],
                  ["Harvard", "(Kumar and Sen 2019)", "No single authority; each journal's version differs", "UK and Commonwealth journals, many Indian universities"],
                  ["Vancouver / ICMJE", "Superscript or bracketed number [1]", "Numbered in order of citation; abbreviated journal names", "Medicine, <em>The Lancet</em>, IJMR"],
                  ["MLA 9th (2021)", "(Kumar and Sen 12)", "Works Cited, alphabetical", "Literature and languages"],
                  ["Bluebook / OSCOLA", "Footnotes with case and statute conventions", "Table of cases, table of statutes", "Law reviews (Bluebook US, OSCOLA UK and increasingly India)"]]},
             {"t": "body", "cls": "sm", "html": "The style is the journal's choice, not yours, "
              "and a reference manager makes changing it a click. What you control is "
              "completeness: authors, year, title, journal, volume, issue, pages and DOI for "
              "every reference, and a URL with an access date for anything that is only "
              "online. A reference list with missing volumes and dead links is the first "
              "thing a careful examiner notices."},
         ]},

        {"type": "content", "label": "Plagiarism", "title": "Plagiarism: what it is, in the UGC's terms and everyone else's",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Similarity (UGC 2018 Regulations)", "Level", "Consequence for a thesis"],
                        "rows": [
                            ["Up to 10%", "Level 0", "Minor; no penalty"],
                            ["Above 10% to 40%", "Level 1", "Revised script to be submitted within six months"],
                            ["Above 40% to 60%", "Level 2", "Debarred from submitting a revised script for one year"],
                            ["Above 60%", "Level 3", "Registration cancelled"]]},
                       {"t": "body", "cls": "sm", "html": "The University Grants Commission "
                        "(Promotion of Academic Integrity and Prevention of Plagiarism in "
                        "Higher Educational Institutions) Regulations, 2018, set these tiers "
                        "and exclude quoted material with attribution, references, the table "
                        "of contents, generic terms, standard equations and the like from the "
                        "count. Faculty face penalties on the same tiers, up to dismissal. "
                        "INFLIBNET's Shodh Shuddhi programme supplies detection software to "
                        "universities."}],
              "right": [{"t": "panel", "color": "amber", "title": "What the similarity score is not", "html":
                         "A low score is not proof of originality, and a high score is not "
                         "proof of plagiarism; the software finds matching strings. Plagiarism "
                         "is presenting another's words, data, ideas or structure as your own, "
                         "and it is possible at 3% (one stolen idea, paraphrased) and absent at "
                         "25% (a methods section that necessarily repeats standard wording, "
                         "with the thesis's own earlier chapters counted). The regulations "
                         "govern the score; the ethics govern the act."},
                        {"t": "hbox", "color": "red", "html": "Patchwriting, changing a few words "
                         "in a copied paragraph, is plagiarism at every journal and most "
                         "detectors now catch it. Paraphrase from notes, not from the open "
                         "source."}]},
         ]},

        {"type": "content", "label": "Self-Plagiarism", "title": "Text recycling, salami slicing and duplicate submission",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Text recycling", "html":
                         "Reusing your own published paragraphs in a new paper. A methods "
                         "description or a setting paragraph repeated across papers from one "
                         "study is generally tolerated if cited ('as described in Kumar 2021'); "
                         "a reused introduction or results section is not. Journals check "
                         "against your own earlier work. Thesis chapters published as articles "
                         "are fine, and expected, provided the thesis says so and the journal "
                         "knows."},
                        {"t": "panel", "color": "amber", "title": "Salami slicing", "html":
                         "Splitting one study into the smallest publishable units to raise the "
                         "count. Three papers on three outcomes from one survey, each with the "
                         "same introduction, is salami; three papers asking different questions "
                         "of the same data is a research programme. The test is whether each "
                         "paper stands alone and cites the others."}],
              "right": [{"t": "panel", "color": "red", "title": "Duplicate submission", "html":
                         "Sending the same paper to two journals at once. Prohibited by every "
                         "journal, discovered routinely (referees overlap), and a reason for "
                         "rejection at both and a note to your institution. A working paper "
                         "or a preprint is not a duplicate submission; a conference "
                         "proceedings paper may be, depending on the journal's policy, which "
                         "you check before submitting."},
                        {"t": "body", "cls": "sm", "html": "COPE (the Committee on Publication "
                         "Ethics) publishes flowcharts editors follow for each of these, and "
                         "reading them tells you what will happen. The common thread is "
                         "disclosure: tell the editor in the cover letter about the thesis, "
                         "the working paper, the companion paper, the conference version."},
                        {"t": "hbox", "color": "green", "html": "When unsure, disclose. Editors "
                         "forgive what they were told and not what they found."}]},
         ]},

        {"type": "content", "label": "Paraphrase", "title": "Paraphrasing properly",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A paraphrase restates a source's idea in your own "
                        "words and structure, with the citation. It is the normal way to use a "
                        "source; quotation is the exception. The safe method is mechanical: "
                        "read the passage, close it, write what it says from memory in the "
                        "form your argument needs, then reopen it to check the facts and add "
                        "the citation. A paraphrase written with the source open turns into "
                        "patchwriting."},
                       {"t": "panel", "color": "red", "title": "Patchwriting", "html":
                         "<em>Source</em>: 'Participation in savings groups increased women's "
                         "reported autonomy in household purchasing decisions by roughly ten "
                         "percentage points.'<br><em>Patchwriting</em>: 'Participating in "
                         "savings groups raised women's reported autonomy in purchasing "
                         "decisions in the household by about ten percentage points (Kumar "
                         "2019).' Cited, and still plagiarism: the sentence is theirs."}],
              "right": [{"t": "panel", "color": "green", "title": "Paraphrase", "html":
                         "'Kumar (2019) finds a ten-point rise in women's say over household "
                         "purchases among savings-group members.' Your structure, your words, "
                         "their finding, their credit. Shorter, too, because a paraphrase "
                         "keeps only what the argument needs."},
                        {"t": "bullets", "color": "cyan", "sm": True, "items": [
                            "Quote when the exact words are the evidence: a definition being contested, a policy's own language, a striking phrase you will discuss.",
                            "Quotations over forty words are set as a block, without quotation marks, with the citation and page.",
                            "Never alter a quotation silently. Use square brackets for insertions and an ellipsis for cuts, and never cut so the meaning changes."]},
                        {"t": "hbox", "color": "amber", "html": "Translations of a quotation are "
                         "yours; say 'author's translation' and give the original in a "
                         "footnote where the wording matters."}]},
         ]},

        {"type": "content", "label": "Data and Images", "title": "Integrity beyond text: data, images and results",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Fabrication</strong> is inventing data or results. <strong>Falsification</strong> is changing them: dropping observations to reach significance, trimming an axis, reporting the one specification that worked. Both are misconduct everywhere.",
                  "<strong>Specification search</strong> without disclosure is falsification by another name. Report what was pre-specified, what was exploratory, and how many things were tried.",
                  "<strong>Figures</strong> are data. Adjusting contrast on a photograph of a document is fine; removing a bar is not. Keep the raw file.",
                  "<strong>Reusing a dataset</strong> collected for another project needs that project's consent terms to allow it, and a citation to it."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The pre-analysis plan", "html":
                         "A registered plan (AEA RCT Registry, OSF, the Registry for "
                         "International Development Impact Evaluations) states the outcomes, "
                         "the specification and the subgroups before the data are seen. It "
                         "makes a null result publishable, because the reader knows it was not "
                         "one of thirty tries. It is required by many funders of trials now "
                         "and is good practice for any confirmatory quantitative study."},
                        {"t": "hbox", "color": "red", "html": "Retraction Watch's database holds "
                         "thousands of retractions, and image manipulation and data problems "
                         "are among the leading causes. A retraction follows a researcher for "
                         "a career."}]},
         ]},

        {"type": "content", "label": "Permissions", "title": "Copyright, licences and reusing other people's material",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Material", "Can you reuse it?", "What to do"],
              "rows": [
                  ["A short quotation with citation", "Yes, under fair dealing (India, Copyright Act 1957, s. 52) and fair use", "Cite; keep it short; no permission needed"],
                  ["A published figure or table, redrawn from the data", "Usually yes, with citation", "'Author's figure, from data in Kumar (2019, Table 2)'"],
                  ["A published figure, reproduced as is", "Only with permission, unless openly licensed", "Request via the publisher's RightsLink; many grant free reuse for theses"],
                  ["Your own figure from your own published article", "Depends on what you signed", "Check the copyright transfer; most publishers permit reuse in a thesis"],
                  ["A government table or map (India)", "Government works are copyright but reuse with attribution is generally permitted; check the source", "Cite the issuing body, title, year, table"],
                  ["Creative Commons material", "Yes, under the licence terms", "Attribute; respect NC (non-commercial) and ND (no derivatives) where present"],
                  ["Survey instruments from other studies", "Often, with citation; some are licensed", "Check the instrument's terms (many DHS-derived modules are open; some psychological scales are not)"]]},
             {"t": "body", "cls": "sm", "html": "Your own paper: read what you sign. A copyright "
              "transfer gives the publisher the paper; a licence to publish keeps it yours. "
              "Open access under CC BY keeps it yours and lets anyone reuse it with credit. "
              "Most publishers allow the accepted manuscript to be posted on a repository "
              "after an embargo; Sherpa Romeo lists each journal's policy."},
         ]},

        {"type": "content", "label": "Referencing Workflow", "title": "A referencing workflow that survives a thesis",
         "blocks": [
             {"t": "flow", "steps": [
                 "CAPTURE: every paper into Zotero the day you read it, with the PDF",
                 "CHECK: fix the metadata then (authors, year, journal, DOI); it will not fix itself later",
                 "NOTE: your summary and the page numbers of anything you might quote",
                 "CITE: insert from Zotero while writing; never type a citation by hand",
                 "BUILD: generate the reference list in the journal's style at the end",
                 "VERIFY: check every reference against its DOI before submission"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The last step catches the errors that "
                        "referencing software introduces: a preprint cited where the published "
                        "version exists, a duplicated entry under two spellings, a page range "
                        "from the wrong issue. A thesis with 300 references has a dozen of "
                        "these and the examiner will find three."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Language-model tools invent "
                        "plausible references with real authors and fake titles. Every "
                        "citation a tool suggests is checked against the DOI or it does not go "
                        "in. Fabricated references have led to retractions and to theses "
                        "being failed."}]},
         ]},

        # ===================== SECTION 08: THE THESIS IN INDIA =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "The Thesis in India"},

        {"type": "content", "label": "The Regulations", "title": "The UGC PhD Regulations, 2022: what they require",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Stage", "Requirement", "Note"],
                        "rows": [
                            ["Entry", "NET/JRF or a university entrance test and interview", "Part-time PhDs permitted for the employed"],
                            ["Coursework", "A minimum of 12 credits, including research methodology and ethics", "In the first year; must be passed before research proper"],
                            ["Research Advisory Committee", "Supervisor plus two members; reviews progress every semester", "Written progress reports; the committee can recommend cancellation"],
                            ["Duration", "Minimum three years including coursework; maximum six, extendable", "Extensions are the university's decision"],
                            ["Publication before submission", "No longer mandatory nationally", "Removed in 2022 after the 2016 rule fed predatory journals; universities may still require it"],
                            ["Plagiarism check", "Required before submission, under the 2018 regulations", "The report is part of the submission"],
                            ["Evaluation", "Supervisor and at least two external examiners not from the institution", "Reports may require revision before the viva"],
                            ["Viva voce", "Open, before the examiners and the department", "Evaluation reports are shared with the candidate beforehand"],
                            ["Deposit", "Electronic copy to INFLIBNET's Shodhganga", "Within a set period after the award; the thesis becomes public"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "The University Grants Commission "
                        "(Minimum Standards and Procedures for Award of Ph.D. Degree) "
                        "Regulations, 2022, replaced the 2016 rules and apply to every "
                        "university the UGC recognises. Each university writes its own "
                        "ordinance within them, and the ordinance is what governs you: chapter "
                        "lists, word limits, format, synopsis, pre-submission seminar. Get the "
                        "ordinance in the first month and read it twice."},
                        {"t": "hbox", "color": "amber", "html": "The removal of the publication "
                         "rule is not permission to publish nothing. It is the removal of a "
                         "rule that pushed scholars into paying to publish. Publish well, "
                         "later."}]},
         ]},

        {"type": "content", "label": "The Proposal", "title": "The synopsis or proposal: the thesis in miniature",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Most Indian universities require a research "
                        "proposal or synopsis approved by a departmental committee before "
                        "registration is confirmed, and again a pre-submission synopsis before "
                        "the thesis goes out. Treat the first as the thesis in miniature: "
                        "question, contribution, literature in brief, design, data, timeline, "
                        "chapter outline. Everything in the proposal is provisional and "
                        "everything should still be defensible."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The question comes first and the methods follow from it, not the reverse. A proposal that opens with 'a mixed-methods approach will be adopted' has chosen the tool before the job.",
                           "Feasibility is the committee's main worry: access to the field or the data, the cost, the time, ethical clearance. Address each explicitly.",
                           "A timeline by semester with deliverables; the Research Advisory Committee will hold you to it and that is useful.",
                           "The chapter outline is the thesis outline from section 03 and it should be written with the same care."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The pre-submission synopsis", "html":
                         "Typically 20&ndash;40 pages: the argument, the findings chapter by "
                         "chapter, the contribution, the main tables. Examiners read it before "
                         "the thesis and sometimes instead of parts of it, so it is written "
                         "as the case for the degree, not as a summary. Many universities "
                         "require a presentation to the department at this stage; treat it "
                         "as the viva's rehearsal and invite the hardest questioners."},
                        {"t": "hbox", "color": "green", "html": "The proposal's literature "
                         "review becomes chapter 2's first draft; its design section becomes "
                         "chapter 3's. Nothing written for a proposal is wasted."}]},
         ]},

        {"type": "content", "label": "The Supervisor", "title": "Working with a supervisor",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A supervisor in an Indian university may be "
                        "guiding six or eight scholars, teaching, administering and publishing, "
                        "and the 2022 regulations cap the number rather than the workload. The "
                        "relationship works when the scholar manages it: regular meetings "
                        "asked for and prepared for, drafts sent with a specific request and a "
                        "date, written notes of what was agreed, and progress reports that "
                        "say what was done and what is next."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Send a one-page agenda before each meeting and a one-page note after. The note is the record when memories differ.",
                           "Ask for feedback on structure early and on prose late; the reverse wastes both your time.",
                           "The Research Advisory Committee's other members are a resource, not a formality. A methodologist on the committee is worth two meetings a year.",
                           "Co-authorship of thesis papers with the supervisor is normal and should be discussed in year one, with the order of names."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When it goes wrong", "html":
                         "Supervisors leave, retire, fall ill or stop responding. The ordinance "
                         "provides for a change of supervisor and the Research Advisory "
                         "Committee is the route. Document the silence (dates of drafts sent, "
                         "meetings requested) before raising it; a scholar with a record is "
                         "taken seriously, and one without is a complaint. The UGC's 2022 "
                         "regulations also set grievance procedures every university must "
                         "have."},
                        {"t": "hbox", "color": "green", "html": "The supervisor's name goes on "
                         "the thesis; the work is yours. Examiners ask the candidate, not the "
                         "supervisor, and can tell the difference."}]},
         ]},

        {"type": "content", "label": "Format", "title": "Format, front matter and the things that get theses sent back",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Element", "What is usually required", "Common fault"],
              "rows": [
                  ["Title page", "Exact wording from the ordinance: degree, university, department, month and year", "Wrong degree title; missing 'submitted in partial fulfilment'"],
                  ["Declaration and certificate", "Candidate's declaration of originality; supervisor's certificate; both signed", "Unsigned; plagiarism certificate missing"],
                  ["Acknowledgements", "Funders, field teams, participants, colleagues, family", "Omitting the funder, which some funders require naming"],
                  ["Abstract", "One to two pages; the whole argument", "A description of chapters instead of findings"],
                  ["Contents, lists of tables and figures, abbreviations", "Auto-generated", "Page numbers wrong because the list was typed by hand"],
                  ["Chapters", "Numbered headings; consistent style; tables and figures numbered by chapter (Table 4.2)", "Inconsistent numbering across chapters written in different years"],
                  ["References", "One list, one style, complete", "Two styles; in-text citations with no reference; references never cited"],
                  ["Appendices", "Instruments, ethics approval, additional tables, code or its location", "Instrument in the language of the field with no English version"],
                  ["Length", "Set by the ordinance; commonly 60,000&ndash;100,000 words in the social sciences", "Padding to reach a minimum; there is rarely a minimum"]]},
             {"t": "body", "cls": "sm", "html": "None of this is the argument, and all of it "
              "is what the examiner sees first. A thesis returned for format corrections "
              "loses two months. Build the template in year one from the ordinance and two "
              "recently passed theses, and write into it."},
         ]},

        {"type": "content", "label": "Examiners", "title": "How examiners read, and what their reports say",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "An external examiner receives a thesis of 250 "
                        "pages, unpaid or nearly, and reads it over two or three sittings "
                        "looking for the answer to one question: does this candidate deserve "
                        "the degree? They read the abstract, the contents, the introduction "
                        "and the conclusion first, then the methods, then the findings, then "
                        "the literature. A thesis whose argument is visible in the first and "
                        "last chapters starts with the examiner on its side."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The report recommends: award; award after minor corrections; resubmit after major revision; or reject. The middle two are the common outcomes and neither is a disaster.",
                           "Corrections are listed. Do all of them, make a table saying where each was done, and have the supervisor certify it.",
                           "A request for major revision means the argument or the evidence was not enough, not that the prose was bad. Read the report for which."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What examiners' reports most often say", "html":
                         "The research question is not stated clearly. The literature review "
                         "describes rather than argues. The methods do not justify the "
                         "choices made. The findings are presented without interpretation. "
                         "The conclusions go beyond the evidence. The contribution is not "
                         "stated. Sections 02 to 05 of this course are the answer to each; "
                         "the list has not changed in decades because the faults are the "
                         "natural ones."},
                        {"t": "hbox", "color": "green", "html": "Ask the supervisor to nominate "
                         "examiners who publish on your question, and read their work. You "
                         "are writing for two named people."}]},
         ]},

        {"type": "content", "label": "The Viva", "title": "The viva voce: what it is for and how to prepare",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "In India the viva is usually open: the "
                        "examiners, the department and any faculty and scholars who wish to "
                        "attend, with a presentation of twenty to forty minutes followed by "
                        "questions. Its purpose is to establish that the work is the "
                        "candidate's, that the candidate understands it, and that the "
                        "examiners' concerns have been met. It is rarely where a thesis fails; "
                        "the reports decided that. It is where a thesis is defended."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The presentation follows the hourglass: problem, question, design, findings with the main figures, contribution, limits. Not one slide per chapter.",
                           "Reread the thesis in the week before. Know where every number is.",
                           "Prepare answers to the examiners' written concerns and say so: 'The report asked about attrition; here is what I found.'",
                           "A mock viva with two faculty who have not read the thesis closely is the best hour of preparation available."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Answering questions", "html":
                         "Listen to the whole question. Pause. Answer the question asked, "
                         "briefly, and stop. 'I don't know, but here is how I would find out' "
                         "is a good answer. 'That is beyond the scope of this thesis' is a "
                         "good answer once and a bad one three times. Disagree with an "
                         "examiner when you are right, with evidence and without heat; "
                         "examiners respect it and some ask a wrong question to see whether "
                         "you will."},
                        {"t": "hbox", "color": "green", "html": "The viva ends with corrections "
                         "and a date. Write them down before you leave the room, because you "
                         "will not remember them afterwards."}]},
         ]},

        {"type": "content", "label": "Shodhganga", "title": "Shodhganga and the thesis as a public document",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Shodhganga, run by INFLIBNET since 2011, holds "
                        "the full text of Indian doctoral theses, and the UGC regulations "
                        "require deposit after the award. The thesis therefore becomes a "
                        "public document read by anyone, indexed by Google, and checked by "
                        "plagiarism software at every other university. Three things follow "
                        "for the writing."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Nothing identifiable about participants goes in. Pseudonymise and describe how in the methods; put the instrument in, not the responses.",
                           "Figures and tables reproduced from copyrighted sources need permission for a public thesis, not only for a bound one.",
                           "A thesis chapter later published as an article will show as 'similar' to the thesis in the journal's check. Say in the cover letter that it derives from the deposited thesis; most journals accept that, some ask for an embargo on the thesis first."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Use it as a source", "html":
                         "Shodhganga is also the largest open collection of Indian "
                         "social-science research and almost nobody searches it. A thesis on "
                         "your district from a neighbouring university, with its instrument "
                         "and its descriptive tables, is worth more than most journal articles "
                         "for context, and it is citable: author, year, title, degree, "
                         "university, and the Shodhganga handle."},
                        {"t": "hbox", "color": "green", "html": "Search Shodhganga in year one, "
                         "before the proposal. It is where you find that your question was "
                         "asked in 2014 and what came of it."}]},
         ]},

        {"type": "content", "label": "Thesis to Papers", "title": "From thesis to articles: plan it in year one",
         "blocks": [
             {"t": "flow", "steps": [
                 "YEAR 1: decide the form (monograph or three papers) and which chapters will be articles",
                 "YEAR 2: write the first empirical chapter as an article; present it; submit a working paper",
                 "YEAR 3: submit chapter 1's article to a journal; draft chapter 2's",
                 "YEAR 4: revise under review; write the thesis introduction and conclusion last",
                 "AFTER: chapter 3's article from the examiners' comments; the thesis is deposited and cited"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A thesis chapter becomes an article by cutting: "
                        "the literature review to two pages, the setting to one, the methods "
                        "to what a specialist needs, the appendices to an online file. What "
                        "remains is the argument, and if there is no argument left after the "
                        "cutting, the chapter was a report. The three-paper thesis makes the "
                        "cut at the outline stage instead of afterwards, which is its point."}],
              "right": [{"t": "hbox", "color": "amber", "html": "One article under review "
                        "before the viva is worth more to a job application than three "
                        "chapters in a bound volume. Examiners also read a published chapter "
                        "differently."}]},
         ]},

        # ===================== SECTION 09: CHOOSING AND REACHING A JOURNAL =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Choosing and Reaching a Journal"},

        {"type": "content", "label": "Fit First", "title": "Choosing a journal: fit, then reach, then speed, then cost",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The journal that will publish your paper is the "
                        "one whose readers need it and whose recent issues contain papers like "
                        "it. Reach (indexing, citation metrics), speed and cost come after "
                        "fit, because a paper at the wrong journal is rejected at the desk "
                        "regardless of its quality, and two months are gone. Make a shortlist "
                        "of four in order and write for the first."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Look at your own reference list. The journals that appear three times or more are candidates.",
                           "Read the aims and scope, then the last two issues. If no paper resembles yours in method and setting, it is the wrong journal whatever the scope says.",
                           "Check the word limit, the format, the reporting guidelines required, and whether they take the paper's design at all (some journals no longer publish cross-sectional studies).",
                           "Note the editor's name and the associate editors who handle your topic. A cover letter addressed to the right person helps."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The four questions of reach", "html":
                         "Is it indexed where your institution and funders look (Scopus, Web "
                         "of Science, DOAJ, the ABDC or ABS lists for management schools)? "
                         "Since February 2025 India has no national journal list: the UGC "
                         "discontinued UGC-CARE and issued 36 suggestive parameters under "
                         "eight heads for institutions to apply themselves, so check what "
                         "your own university's committee accepts. Who reads it: "
                         "academics only, or the policymakers and practitioners you want? "
                         "Will it be found: is it open access, or behind a wall most Indian "
                         "readers cannot pass?"},
                        {"t": "hbox", "color": "green", "html": "A good paper in a solid "
                         "field journal read by the right 500 people does more for a career "
                         "than a rejection from a general journal read by 50,000."}]},
         ]},

        {"type": "content", "label": "Outlets", "title": "Where development and social-science research from South Asia is published",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Journal", "Publisher and field", "Notes"],
              "rows": [
                  ["<em>World Development</em>", "Elsevier; interdisciplinary development", "Large, well read by policy audiences; long review times"],
                  ["<em>Journal of Development Economics</em>", "Elsevier; economics", "Highly selective; identification expected; registered reports track"],
                  ["<em>Journal of Development Studies</em>", "Taylor &amp; Francis; interdisciplinary", "Takes qualitative and mixed methods; policy-relevant"],
                  ["<em>Economic Development and Cultural Change</em>", "Chicago; economics", "Applied micro; long-standing South Asia coverage"],
                  ["<em>Development and Change</em>", "Wiley; critical development studies", "Political economy, argument-driven work"],
                  ["<em>Journal of Development Effectiveness</em>", "Taylor &amp; Francis; evaluation", "Impact evaluations and systematic reviews; 3ie-linked"],
                  ["<em>Economic and Political Weekly</em>", "Sameeksha Trust, Mumbai; since 1966", "Read by Indian policy and academic audiences alike; Special Articles are peer reviewed; shorter forms too"],
                  ["<em>Indian Journal of Labour Economics</em>", "Springer, for the Indian Society of Labour Economics", "Work, wages, employment; Scopus-indexed"],
                  ["<em>Indian Economic Review</em>; <em>Journal of Quantitative Economics</em>", "Springer, for the Delhi School of Economics and TIES", "Economics with an Indian base; theory and applied"],
                  ["<em>Indian Journal of Human Development</em>; <em>Indian Journal of Gender Studies</em>; <em>Contributions to Indian Sociology</em>", "Sage, for IHD, CWDS and the Institute of Economic Growth", "Interdisciplinary, gender, sociology; established peer review"],
                  ["<em>Indian Journal of Medical Research</em>; <em>Indian Journal of Community Medicine</em>", "ICMR; IAPSM", "Public health; IJMR is open access without a fee"]]},
             {"t": "body", "cls": "sm", "html": "A list, not a ranking. Every one of these has "
              "published work by first-time authors from Indian universities and every one "
              "rejects most of what it receives."},
         ]},

        {"type": "content", "label": "Predatory Journals", "title": "Predatory journals: the definition, the signs, the checks",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Predatory journal",
                        "def": "An outlet that prioritises self-interest at the expense of "
                        "scholarship, characterised by false or misleading information, "
                        "deviation from best editorial and publication practices, a lack of "
                        "transparency, and aggressive, indiscriminate solicitation. The "
                        "consensus definition of Grudniewicz and colleagues, <em>Nature</em> "
                        "2019, 576:210."},
                       {"t": "bullets", "color": "red", "items": [
                           "An email inviting you to submit, praising a paper the sender has not read, promising decision in days.",
                           "A fee mentioned only after acceptance, or a 'fast track' fee.",
                           "An 'impact factor' from a body you have not heard of; claims of indexing that the index itself does not confirm.",
                           "An editorial board of names without affiliations, or with affiliations that do not know them.",
                           "A scope that covers every field; hundreds of papers an issue; papers accepted in a week."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The checks, in order", "html":
                         "Is it in DOAJ (for open access), Scopus's source list, or Web of "
                         "Science's Master Journal List, checked on those sites and not on "
                         "the journal's? Is the publisher a member of COPE? Does Think. "
                         "Check. Submit.'s checklist come out clean? Can you find the "
                         "journal's articles cited by papers you trust? Has anyone you know "
                         "reviewed for it? Cabells' Predatory Reports is a paid list; the "
                         "archived Beall's list, closed in 2017, is dated but still "
                         "instructive."},
                        {"t": "hbox", "color": "amber", "html": "Indian scholars are targeted "
                         "heavily because promotion rules once rewarded counts. A paper in a "
                         "predatory journal is not neutral: it can be held against you, and "
                         "it cannot be published again elsewhere."}]},
         ]},

        {"type": "content", "label": "Open Access", "title": "Open access: the routes and what each costs",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Route", "What it means", "Cost to author", "Example"],
                        "rows": [
                            ["Gold", "The journal publishes the final version openly, usually for an article processing charge", "Typically US$1,500&ndash;4,000; waivers for some countries and funders", "<em>PLOS ONE</em>, <em>BMJ Global Health</em>"],
                            ["Hybrid", "A subscription journal that will make one article open for a fee", "As above, often higher", "Most Elsevier, Wiley and Springer titles"],
                            ["Green", "You post the accepted manuscript on a repository after an embargo", "Nothing", "Any journal; check Sherpa Romeo for the embargo"],
                            ["Diamond", "Open, no fee to author or reader; funded by a society or institution", "Nothing", "<em>Indian Journal of Medical Research</em>; many society journals"],
                            ["Preprint", "The manuscript posted before or during review", "Nothing", "SSRN, arXiv's economics section, OSF, medRxiv"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "For a South Asian author the "
                        "practical route is green plus a preprint: free, immediate, and "
                        "compliant with almost every funder. Gold is worth paying for only "
                        "when a funder pays or the readers you want cannot otherwise reach "
                        "the paper. Some publishers waive the charge for authors in "
                        "lower-income countries; India is usually not on those lists, so "
                        "ask before assuming."},
                        {"t": "hbox", "color": "cyan", "html": "Since 1 January 2025, One "
                         "Nation One Subscription gives about 6,400 Indian institutions "
                         "access to 13,000-plus journals from 30 publishers through "
                         "INFLIBNET, on a Rs 6,000 crore budget for 2025&ndash;27. It covers "
                         "reading, not publishing; the article processing charge is still "
                         "yours."}]},
         ]},

        {"type": "content", "label": "Preprints", "title": "Working papers and preprints: priority, feedback and reach",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Economics has run on working papers for fifty "
                        "years: NBER, CEPR, IZA, the World Bank series, and RePEc's index of "
                        "all of them. A paper is read, cited and discussed as a working paper "
                        "for the two years it takes to appear in a journal, and the journal "
                        "version is the archival record. The rest of the social sciences and "
                        "public health have moved the same way since 2020, through SSRN, OSF "
                        "Preprints, medRxiv and SocArXiv."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Post when the paper is ready for criticism, not before. A preprint with a wrong table is a wrong table with a DOI.",
                           "Post the version you submitted, and update it as it improves. Most servers keep every version.",
                           "Check the target journal's policy first; almost all accept preprinted work now, and a few in medicine still do not.",
                           "Cite preprints as preprints, with the server and the DOI, and update to the published version when it exists."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Institutional series", "html":
                         "An Indian institution's own working-paper series (IGIDR, ISI, "
                         "CDS, NCAER, IIMs, the Centre for Policy Research) gives a paper a "
                         "number, a date and a place on RePEc, and it is where seminar "
                         "audiences look. If your institution has none, IZA and the World "
                         "Bank's series take affiliated authors, and SSRN takes anyone. A "
                         "working paper is also what a job market or a grant application "
                         "can cite while the journal decides."},
                        {"t": "hbox", "color": "green", "html": "Google Scholar indexes "
                         "preprints and counts their citations. Your paper starts its public "
                         "life the day it is posted, not the day it is accepted."}]},
         ]},

        {"type": "content", "label": "Submission", "title": "The submission: cover letter, files, and the form",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The cover letter", "html":
                         "Half a page, to the editor by name. The title. One paragraph on "
                         "the question and the main finding, in numbers. One sentence on why "
                         "it fits this journal, naming a paper the journal published. "
                         "Disclosures: the thesis or working paper it derives from, any "
                         "related paper under review elsewhere, funding, conflicts, ethics "
                         "approval and its number, trial or study registration. Suggested "
                         "reviewers if asked, with no co-authors or supervisors among them. "
                         "Nothing else."},
                        {"t": "bullets", "color": "amber", "sm": True, "items": [
                            "Anonymise the manuscript if review is double-blind: no names, no 'our earlier work (Kumar 2019)', no acknowledgements, metadata stripped from the file.",
                            "Follow the format instructions exactly. Editors desk-reject papers that ignore them, because ignoring them predicts ignoring referees.",
                            "Supplementary files named and listed; the replication package's link in the data statement."]}],
              "right": [{"t": "body", "html": "Then the wait. Most journals send an editor's "
                        "decision on whether to review within two to four weeks; a desk "
                        "rejection at that point says the paper did not fit or did not "
                        "persuade the editor of its contribution, and the letter usually says "
                        "which. Full review takes two to six months in economics and "
                        "development studies and less in health. Query politely after the "
                        "journal's own stated time has passed, not before."},
                        {"t": "hbox", "color": "green", "html": "The day you submit, start the "
                         "next paper. Waiting is not a stage of the pipeline."}]},
         ]},

        {"type": "content", "label": "Metrics", "title": "Journal metrics: what they measure and what they do not",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Metric", "Source", "Measures", "Do not use it to"],
                        "rows": [
                            ["Journal Impact Factor", "Clarivate (Web of Science)", "Mean citations in year t to items from t&minus;1 and t&minus;2", "Judge a single paper or an author"],
                            ["CiteScore", "Elsevier (Scopus)", "Four-year citation window, all document types", "Compare across fields"],
                            ["SJR, SNIP", "Scopus-based", "Prestige-weighted and field-normalised journal citation", "Rank journals within a field precisely"],
                            ["h5-index", "Google Scholar", "h-index of a journal's last five years", "Compare with Web of Science figures"],
                            ["Acceptance rate", "The journal, if it publishes it", "Selectivity", "Infer quality; low rates also mean poor fit"],
                            ["Time to first decision", "The journal", "Speed", "Choose a journal by this alone"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Every metric is a journal average "
                        "and says nothing about the paper in front of you. The San Francisco "
                        "Declaration on Research Assessment (DORA, 2012) and the Leiden "
                        "Manifesto (Hicks and colleagues, <em>Nature</em> 2015, 520:429) "
                        "asked institutions to stop using them for individuals; many still "
                        "do, and Indian promotion rules have leaned on them heavily. Know "
                        "the numbers your committee uses, and do not mistake them for your "
                        "reader."},
                        {"t": "hbox", "color": "amber", "html": "A journal advertising an "
                         "impact factor to five decimal places from a body you cannot find "
                         "is advertising that it is predatory."}]},
         ]},

        {"type": "content", "label": "Special Issues and Books", "title": "Special issues, edited volumes and conference proceedings",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A special issue of a good journal, with a "
                        "guest editor who knows the field, is a fast route to a themed "
                        "readership and is reviewed like any other issue. A special issue "
                        "solicited by email from a journal you have not heard of, with a "
                        "guest editor you cannot find, is the predatory model's current form; "
                        "several large publishers have retracted whole issues since 2022. "
                        "Apply the checks from the predatory-journal slide to the issue, not "
                        "only the journal."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Edited volumes from university presses and established academic publishers count in most Indian departments; volumes from vanity presses that print anything for a fee do not.",
                           "A chapter is reviewed by the editor, rarely by referees, and cited less than an article. Publish the article first and the chapter as its extension.",
                           "Conference proceedings count in engineering and computer science and barely at all in the social sciences. Check what your committee's rules say."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The book", "html":
                         "A monograph from a thesis is the humanities' and some social "
                         "sciences' standard, and an academic press (Oxford University Press "
                         "India, Cambridge, Sage, Routledge, Orient BlackSwan, Permanent "
                         "Black) will send the proposal and sample chapters for review. The "
                         "thesis is not the book: examiners wanted proof of competence; "
                         "readers want an argument, and the literature review and the "
                         "methods chapter mostly go. Budget a year of rewriting."},
                        {"t": "hbox", "color": "red", "html": "An email offering to publish "
                         "your thesis as a book, free, from a press you have not heard of, "
                         "is an offer to make it unpublishable anywhere else."}]},
         ]},

        {"type": "content", "label": "Timeline", "title": "A realistic timeline from draft to print",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Stage", "Typical time", "What you do"],
                        "rows": [
                            ["Draft to working paper", "2&ndash;4 months", "Seminar, comments, revise; post"],
                            ["Submission to editor's first decision", "2&ndash;4 weeks", "Desk reject, or sent to referees"],
                            ["Referee reports", "2&ndash;6 months", "Start the next paper"],
                            ["First decision", "", "Reject (most), major revision, minor revision, accept (rare)"],
                            ["Revision", "1&ndash;3 months", "Point-by-point response; new analyses"],
                            ["Second round", "1&ndash;3 months", "Referees see the response"],
                            ["Acceptance to online publication", "2&ndash;8 weeks", "Proofs, in 48 hours; data editor's checks where applicable"],
                            ["Online to print issue", "0&ndash;12 months", "Nothing; the online version is citable"],
                            ["Total from first submission, one journal", "9&ndash;18 months", ""],
                            ["Total including one rejection first", "18&ndash;30 months", "Which is the usual case"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Typical ranges for economics and "
                        "development studies; health journals are faster, top economics "
                        "journals slower. None of this is in your control except the "
                        "quality of the first submission and the speed of the revision, so "
                        "keep three papers moving at once and the average comes out."},
                        {"t": "hbox", "color": "amber", "html": "A PhD student who submits the "
                         "first paper in year two has a publication by the viva. One who "
                         "submits in year four has a submission."}]},
         ]},

        # ===================== SECTION 10: PEER REVIEW AND REVISION =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Peer Review and Revision"},

        {"type": "content", "label": "How Review Works", "title": "What happens to a paper between submission and decision",
         "blocks": [
             {"t": "flow", "steps": [
                 "EDITOR reads: fit, contribution, format; desk-rejects most",
                 "REFEREES: two or three, chosen from the references and the editor's network; unpaid",
                 "REPORTS: strengths, major and minor concerns, a recommendation",
                 "EDITOR decides, weighing reports; not a vote",
                 "LETTER: the decision with the reports attached",
                 "YOU: revise and respond, or take it elsewhere"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The referee is a colleague reading your paper "
                        "in an evening for no reward except duty, looking for what is wrong "
                        "because that is what they were asked. Their report is the most "
                        "expert reading the paper will ever get, including the ones that are "
                        "unfair. Single-blind review (they know you, you do not know them) "
                        "is the norm in economics; double-blind in most social sciences; "
                        "open review is growing in health."}],
              "right": [{"t": "hbox", "color": "cyan", "html": "Become a referee as soon as you "
                        "can. Nothing teaches how papers are judged faster than judging "
                        "them, and editors remember who reviews well."}]},
         ]},

        {"type": "content", "label": "Reading Reports", "title": "Reading the decision letter and the reports",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Read the letter once, close it for a day, and "
                        "read it again with a pen. The first reading is emotional and useless. "
                        "The second sorts the comments: what the editor emphasised (that is "
                        "the list that decides), what each referee asked for, which requests "
                        "overlap, which contradict, which are misunderstandings caused by the "
                        "text, and which are simply wrong. A referee who misunderstood was "
                        "misled by your paper, and the fix is in the paper."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Major revision means the editor wants the paper if the concerns can be met. Treat it as a conditional acceptance to be earned.",
                           "Minor revision is nearly accepted; do everything asked, quickly.",
                           "Reject with encouragement to resubmit is a real invitation and is worth taking.",
                           "Reject is final at that journal. Do not appeal unless a referee's factual error decided it, and even then rarely."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Reading between the lines", "html":
                         "'The contribution is unclear' means the introduction failed. 'The "
                         "identification is not convincing' means a specific assumption needs "
                         "a specific test. 'The paper is too long' means the appendix is in "
                         "the main text. 'The authors should cite ...' followed by five papers "
                         "by one person is a referee asking to be cited; cite the relevant "
                         "ones. 'The English needs work' means a language edit, and also "
                         "that the argument was hard to follow."},
                        {"t": "hbox", "color": "green", "html": "Make a table: every comment, "
                         "numbered, in one column. It becomes the response document."}]},
         ]},

        {"type": "content", "label": "The Response", "title": "The response to reviewers: point by point, in full",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Referee 2, comment 3", "Response", "Where"],
                        "rows": [
                            ["'The authors do not address differential attrition between arms, which could bias the estimates upward.'",
                             "We agree this needed direct treatment. Attrition was 11.8% in treatment and 13.9% in control (new Table A4). Attriters were poorer at baseline in both arms; the difference between arms is not significant (p = 0.31). We now bound the estimate using Lee (2009) bounds; the effect remains positive at 5.1 to 9.4 points (new Table 5, column 3). We have added a paragraph to the results and a sentence to the limitations.",
                             "pp. 14&ndash;15; Table 5; Appendix A4"],
                            ["'The literature review omits Sen and Rao (2020).'",
                             "Added, with a sentence on how their setting differs (urban, credit-only groups). We note their null result is consistent with our mechanism.",
                             "p. 4, paragraph 2"],
                            ["'The paper should also examine effects on children's schooling.'",
                             "We measured schooling but treat it as secondary because the pre-analysis plan named decision-making as the primary outcome. We now report schooling in Appendix Table A6 (a positive but imprecise 2.1 points, p = 0.19) and refer to it in the discussion. A full treatment is beyond this paper's scope and we say so.",
                             "p. 19; Appendix A6"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Every comment quoted in full, every "
                        "response starting with what was done, every change located by page "
                        "and table. Agree where the referee is right and say so plainly. Where "
                        "they are wrong, show why with evidence, without heat, and change the "
                        "text so the next reader does not make the same mistake. Where a "
                        "request is beyond the paper, do the cheap version and say why the "
                        "full one is a different paper."},
                        {"t": "hbox", "color": "amber", "html": "The response document is often "
                         "longer than the paper. That is normal. Referees read it first and "
                         "the paper second."}]},
         ]},

        {"type": "content", "label": "Revising", "title": "Revising the paper itself",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Do the analyses first, all of them, before touching the text. Some will change the story and the text should follow the story.",
                  "Revise the introduction and abstract last; they must match the paper that now exists, not the one that was submitted.",
                  "Submit a tracked-changes or highlighted version alongside the clean one, if the journal allows. Referees are grateful.",
                  "Do not sneak in unrelated changes. Referees compare versions, and an unexplained change reads as a concealed one.",
                  "Meet the deadline. If you cannot, write and ask before it passes; editors extend readily and forget papers that simply vanish."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When the referees disagree", "html":
                         "Referee 1 wants the model; Referee 2 wants it gone. The editor's "
                         "letter usually says which way to go; if not, do what strengthens "
                         "the argument, say in the response that the referees differed and "
                         "what you chose and why, and offer the other version in the appendix. "
                         "Editors respect a reasoned choice more than a paper that tries to "
                         "please both and satisfies neither."},
                        {"t": "hbox", "color": "green", "html": "Send the revised paper to a "
                         "colleague who has not seen it with the reports. If they cannot find "
                         "the changes, the referees will not either."}]},
         ]},

        {"type": "content", "label": "Rejection", "title": "Rejection: the normal outcome, and what to do with it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Most submissions to most journals are rejected, "
                        "and at selective journals more than nine in ten. A rejection is "
                        "information about fit and about the paper, not about you, and the "
                        "reports are free expert advice. The productive response is "
                        "mechanical: read the reports after a day, fix everything they were "
                        "right about, send it to the next journal on the list within a month. "
                        "Papers that sit in a drawer after rejection are the commonest way "
                        "good work is lost."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Do not resubmit unchanged. The next journal may use the same referee, and referees remember.",
                           "Do not add the previous reports to the new submission unless the journal asks; some now do, and some accept transferred reviews.",
                           "Reframe if the fit was the problem: the same evidence can answer a different journal's question.",
                           "After three rejections with similar concerns, the concern is real. Fix it or shelve the paper."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Appeals", "html":
                         "An appeal succeeds when a referee made a demonstrable factual "
                         "error that the editor relied on: misread the design, cited a "
                         "result the paper does not contain. It does not succeed on a "
                         "difference of judgement, and it burns the editor's goodwill. Most "
                         "journals allow one appeal, in writing, and decide within weeks. "
                         "Use it once in a career, if that."},
                        {"t": "hbox", "color": "green", "html": "Keep a log: journal, dates, "
                         "outcome, the main objections. Patterns across papers are the "
                         "feedback nobody else will give you."}]},
         ]},

        {"type": "content", "label": "Proofs and After", "title": "Proofs, publication, and making the paper found",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Proofs arrive with 48 hours to return them. "
                        "Check every number against the accepted manuscript, every author "
                        "name and affiliation, every reference, the figures' rendering, and "
                        "the copy-editor's changes, which occasionally alter meaning. This is "
                        "the last time the paper can be corrected without a published "
                        "erratum. Then the DOI is live and the paper is public forever."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Post the accepted manuscript on your institutional repository and a preprint server the day the embargo allows. Sherpa Romeo says when.",
                           "Update Google Scholar, ORCID and RePEc profiles; the ORCID iD should be on every submission from the start.",
                           "Write the two-paragraph plain-language summary and send it to the people who will use the result: the programme, the ministry, the funder, the journalists who cover the topic.",
                           "Deposit the replication package with a DOI and link it from the paper."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Corrections", "html":
                         "An error found after publication is corrected with an erratum "
                         "(the journal's) or a corrigendum (yours), published and linked. "
                         "An error that changes the conclusions is a retraction, which "
                         "authors can and should initiate themselves. Both are ordinary "
                         "parts of science, and a self-reported correction costs a "
                         "reputation nothing. An error discovered by someone else after you "
                         "knew of it costs everything."},
                        {"t": "hbox", "color": "green", "html": "The paper is the start of a "
                         "conversation, not its end. Answer the emails it brings."}]},
         ]},

        {"type": "content", "label": "Being a Referee", "title": "Refereeing: how to do it well, and why",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "READ the paper once for the argument, once for the evidence",
                  "SUMMARISE it in a paragraph, so the author knows you read it",
                  "MAJOR concerns: the two or three things that decide whether it is publishable, with what would fix each",
                  "MINOR: errors, unclear passages, missing citations, numbered",
                  "RECOMMEND, in the confidential note, with your confidence"]},
                       {"t": "body", "html": "A good report is specific, constructive and "
                        "proportionate: it says what is wrong, why it matters, and what would "
                        "put it right, in about two pages, within the journal's deadline. It "
                        "does not rewrite the paper the referee would have written, demand "
                        "citations of the referee's own work, or comment on the authors."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Decline if you cannot do it in time or have a conflict; say so at once so the editor can find someone else.",
                  "Confidential means confidential: no sharing, no using the results, no citing the manuscript.",
                  "Sign your reviews if the journal allows and you are comfortable; unsigned, write as if you had.",
                  "Record it on ORCID or Web of Science Reviewer Recognition; it counts in some promotion files and it should."]},
                        {"t": "hbox", "color": "amber", "html": "Every paper you submit costs "
                         "the community three reviews. Refereeing three papers for each one "
                         "you submit is the only fair rate."}]},
         ]},

        # ===================== SECTION 11: AUTHORSHIP, ETHICS AND PRACTICE =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Authorship, Ethics and Practice"},

        {"type": "content", "label": "Authorship", "title": "Who is an author: the ICMJE criteria and what they exclude",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The International Committee of Medical Journal "
                        "Editors' four criteria are the standard most journals across fields "
                        "now cite. An author has made a substantial contribution to the "
                        "conception or design of the work, or to acquiring, analysing or "
                        "interpreting the data; has drafted the work or revised it "
                        "critically; has approved the final version; and agrees to be "
                        "accountable for all of it. All four, not any."},
                       {"t": "bullets", "color": "red", "items": [
                           "<strong>Gift authorship</strong>: a head of department or supervisor added for rank alone. Common in India; misconduct under most journals' rules.",
                           "<strong>Ghost authorship</strong>: someone who wrote or analysed and is left off, often a junior researcher or a paid writer.",
                           "<strong>Guest authorship</strong>: a famous name added for credibility. As above.",
                           "<strong>Coercive authorship</strong>: a demand for a byline as the price of data, access or approval."]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The CRediT taxonomy", "html":
                         "Fourteen contributor roles (conceptualisation, methodology, "
                         "software, validation, formal analysis, investigation, resources, "
                         "data curation, writing: original draft, writing: review and "
                         "editing, visualisation, supervision, project administration, "
                         "funding acquisition), stated per author in the paper. Many "
                         "journals now require it, and it makes the authorship conversation "
                         "concrete: someone who is only 'supervision' and 'funding "
                         "acquisition' does not meet the ICMJE criteria."},
                        {"t": "hbox", "color": "amber", "html": "Field staff, data collectors "
                         "and research assistants who did not meet the criteria are named "
                         "in the acknowledgements, with their permission, and paid."}]},
         ]},

        {"type": "content", "label": "Author Order", "title": "Author order: conventions differ, so agree in writing",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Field", "Convention", "What position signals"],
                        "rows": [
                            ["Economics", "Alphabetical, regardless of contribution", "Nothing; readers know this, and the convention penalises later surnames measurably (Einav and Yariv, <em>J Econ Perspect</em> 2006, 20:175)"],
                            ["Public health, medicine, psychology", "By contribution; first author did most; last author is the senior or lab head", "First and last matter for careers; middle authors less"],
                            ["Sociology, political science, development studies", "By contribution, first author leads; sometimes alphabetical with a note", "First author matters; a note explaining equal contribution is common"],
                            ["Interdisciplinary teams", "Whatever was agreed, stated in a contribution note", "The note is the signal"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Disputes over order end "
                        "collaborations and, in India, have ended careers. The prevention is "
                        "a written agreement at the start of the project: who will be an "
                        "author, in what order, with what responsibilities, and how the "
                        "order changes if contributions change. Revisit it when the draft "
                        "exists. A supervisor's place on a thesis paper is decided the same "
                        "way, in the first year, and 'the supervisor is always last author' "
                        "is a convention of some fields and not a rule."},
                        {"t": "hbox", "color": "green", "html": "Corresponding author is a job "
                         "(handling submission and queries), not a rank. It is usually the "
                         "person who will still be reachable in ten years."}]},
         ]},

        {"type": "content", "label": "Declarations", "title": "What every paper now declares",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Declaration", "What it says", "Where it goes"],
              "rows": [
                  ["Ethics approval", "The committee, the approval number and date; or the reason approval was not required", "Methods, and a statement at the end"],
                  ["Consent", "That participants gave informed consent, how, and for what use including data sharing", "Methods"],
                  ["Registration", "Trial or study registry and number (CTRI for clinical trials in India; AEA RCT Registry; RIDIE; OSF)", "Abstract and methods"],
                  ["Funding", "Every funder, grant number, and the funder's role if any in design, analysis or publication", "Acknowledgements or a funding statement"],
                  ["Competing interests", "Financial or other interests of any author that a reader might think relevant; 'none' if none", "A statement; the ICMJE form at many journals"],
                  ["Data availability", "Where the data and code are, or why they cannot be shared and how to request them", "A statement, often with the DOI of the deposit"],
                  ["Author contributions", "CRediT roles per author", "A statement"],
                  ["AI use", "Any generative tool used, for what, and how the output was checked", "Methods or acknowledgements, per the journal's policy"]]},
             {"t": "body", "cls": "sm", "html": "A missing or vague declaration is now a "
              "reason for desk rejection at many journals, and a false one is misconduct. "
              "Collect the numbers (approval, registration, grant) in one file at the start "
              "of the project; they are needed for every output and are hardest to find "
              "three years later."},
         ]},

        {"type": "content", "label": "AI", "title": "Generative AI in academic writing: what is allowed and what is disclosed",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Since early 2023 the major publishers, the "
                        "ICMJE and COPE have converged: a language model cannot be an author, "
                        "because it cannot take responsibility; its use in writing must be "
                        "disclosed; the authors are accountable for everything it produced, "
                        "including invented references; and its use to create or alter "
                        "images and data is prohibited. Journals differ on the details, and "
                        "the policy on the journal's site is the one that binds you."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Reasonable uses, disclosed: language editing of your own draft, reformatting references, suggesting synonyms, checking code, summarising your own notes.",
                           "Uses that get papers retracted: generating text presented as your own analysis, generating references, generating results or images, summarising papers you have not read and citing them.",
                           "Disclosure is one sentence: the tool, the version, what it was used for, and that the authors reviewed and take responsibility for the output.",
                           "Never paste unpublished data or a manuscript under review into a tool whose terms let it retain them."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The deeper problem", "html":
                         "A model produces fluent, generic academic prose on any topic, and "
                         "fluent generic prose is exactly what sections 02 to 05 of this "
                         "course are teaching you not to write. The tell is not grammar; it "
                         "is the absence of anything a stranger could check: no specific "
                         "number, no named study, no sentence that could be wrong. Referees "
                         "have learned the register and read it as a signal that the "
                         "thinking was outsourced too."},
                        {"t": "hbox", "color": "green", "html": "Use it the way you would use a "
                         "clever, confident, unreliable research assistant: for tasks you can "
                         "check, and never for the claim."}]},
         ]},

        {"type": "content", "label": "Habits", "title": "Writing habits that produce papers",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Boice's studies of new faculty in the 1980s and "
                        "Silvia's <em>How to Write a Lot</em> (American Psychological "
                        "Association, 2nd ed., 2019) make the same case with data: people who "
                        "write in short scheduled sessions produce several times more than "
                        "people who wait for large blocks of free time, and the blocks never "
                        "come. The habit is the method. Thirty minutes at the same time every "
                        "working day, before email, with the door closed."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Track words or minutes, not quality. A log of daily sessions is the most reliable predictor of a finished thesis.",
                           "Stop mid-paragraph. Starting is the hard part; a sentence to finish removes it.",
                           "Writing includes outlining, revising and making tables. It does not include reading, which expands to fill any time given to it.",
                           "A writing group of two or three, meeting weekly for an hour to report and set targets, doubles most people's output."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The blocked writer", "html":
                         "Perfectionism (the first sentence must be right), fear (the "
                         "supervisor will hate it), and the missing argument (there is "
                         "nothing to say yet) look identical from outside and have different "
                         "cures. Write the bad first draft; send the draft anyway; go back "
                         "to the card with the one-sentence claim. If the claim cannot be "
                         "written, the block is not in the writing."},
                        {"t": "hbox", "color": "green", "html": "Fieldwork, teaching and family "
                         "will not leave a gap for writing. The gap is made, at the same "
                         "hour, and defended."}]},
         ]},

        {"type": "content", "label": "Policy Audiences", "title": "The same study for a policy reader: the brief",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A journal article is read by a few hundred "
                        "specialists over several years. A policy brief is read by a few "
                        "dozen officials in a week, and one of them may act. The two use the "
                        "same evidence and reverse the order: the brief opens on the "
                        "recommendation and the number that supports it, gives the evidence "
                        "in a page, puts the method in a box, and ends with what it would "
                        "cost and who would do it. Nothing in it is less rigorous; everything "
                        "in it is shorter."},
                       {"t": "flow", "steps": [
                           "HEADLINE: the finding in one sentence a minister could repeat",
                           "WHY IT MATTERS: the problem, with one number, in one paragraph",
                           "WHAT WE FOUND: three findings, each with its evidence and its certainty",
                           "WHAT TO DO: actions that name an actor and a cost",
                           "HOW WE KNOW: the study in a box; the link to the paper"]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Two to four pages; one figure that carries the finding; no regression table.",
                  "Plain verbs, no discipline dialect, numbers rounded and given with their base.",
                  "Hedge exactly as the paper does, in fewer words: 'probably', 'in settings like Bihar', 'we could not test whether'.",
                  "Cite the paper and the data, so the reader who wants the apparatus can find it.",
                  "J-PAL's policy insights, 3ie's briefs and IFPRI's are worked examples; read five before writing one."]},
                        {"t": "hbox", "color": "amber", "html": "The brief is written after the "
                         "paper is accepted, not before. A brief built on a result that "
                         "changes in review is a retraction in the ministry."}]},
         ]},

        {"type": "content", "label": "Checklist", "title": "Before you submit: the checklist",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Argument and structure", "Done"],
                        "rows": [
                            ["The claim is stated in one sentence in the abstract and the introduction", ""],
                            ["The main result, with its number, appears in the introduction", ""],
                            ["The contribution is stated against named papers", ""],
                            ["Every section's first sentence carries its claim (reverse outline done)", ""],
                            ["Objections are anticipated with analyses, not acknowledgements", ""],
                            ["The conclusion says what follows, not what was found", ""],
                            ["Limitations have a direction of bias each", ""]]}],
              "right": [{"t": "table",
                         "head": ["Evidence and apparatus", "Done"],
                         "rows": [
                             ["Every number in the text matches its table", ""],
                             ["Every table and figure is referred to in the text and can be read alone", ""],
                             ["Every citation in the text is in the list and every entry is cited; DOIs checked", ""],
                             ["The similarity report has been run and read", ""],
                             ["Declarations complete: ethics, registration, funding, conflicts, data, contributions, AI", ""],
                             ["The replication package runs on a clean machine", ""],
                             ["Format, word count and anonymisation match the journal's instructions", ""],
                             ["Cover letter written, to the editor by name, with disclosures", ""]]},
                        {"t": "hbox", "color": "cyan", "html": "Fifteen lines. A paper that "
                         "passes all fifteen has removed every reason for desk rejection "
                         "that is within the author's control."}]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Book or resource", "What it is for", "Notes"],
              "rows": [
                  ["Booth, Colomb, Williams et al., <em>The Craft of Research</em> (4th ed., University of Chicago Press, 2016)", "Argument: from topic to question to claim to evidence", "The one to read first"],
                  ["Williams and Bizup, <em>Style: Lessons in Clarity and Grace</em> (12th ed., Pearson, 2017)", "Sentences: characters, actions, cohesion, concision", "Work through the exercises"],
                  ["Sword, <em>Stylish Academic Writing</em> (Harvard University Press, 2012)", "What the most readable academics do differently", "Short; read in a weekend"],
                  ["Pinker, <em>The Sense of Style</em> (Viking, 2014)", "Why clear writing is hard, and the classic style as the cure", "Chapter 3 on the curse of knowledge"],
                  ["McCloskey, <em>Economical Writing</em> (3rd ed., University of Chicago Press, 2019)", "Economics prose, in 35 short rules", "Blunt and correct"],
                  ["Cochrane, 'Writing Tips for PhD Students' (2005, online); Thomson, <em>A Guide for the Young Economist</em> (2nd ed., MIT Press, 2011)", "The economics paper and seminar", "Both free or cheap; Cochrane is twelve pages"],
                  ["Belcher, <em>Writing Your Journal Article in Twelve Weeks</em> (2nd ed., University of Chicago Press, 2019)", "A week-by-week workbook from draft to submission", "Used by writing groups worldwide"],
                  ["Dunleavy, <em>Authoring a PhD</em> (Palgrave, 2003); Murray, <em>How to Write a Thesis</em> (4th ed., Open University Press, 2017)", "The thesis: structure, chapters, the process", "Dunleavy on structure, Murray on habits"],
                  ["Silvia, <em>How to Write a Lot</em> (2nd ed., APA, 2019)", "Habits, schedules, the writing group", "Ninety pages"],
                  ["COPE guidelines; ICMJE Recommendations; Think. Check. Submit.; Sherpa Romeo", "Ethics, authorship, journal checks, open-access policies", "All free online"],
                  ["UGC PhD Regulations 2022; UGC Plagiarism Regulations 2018; your university's ordinance", "The rules you are examined under", "Read the ordinance twice"]]},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Academic Writing &amp; Publishing 101 &middot; Complete",
         "headline": "Now go write<br>something checkable.",
         "byline": "A claim, the evidence, the reasoning, and enough for a stranger to disagree: "
                   "that is the whole contract, in a thesis or a journal. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

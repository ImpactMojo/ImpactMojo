# -*- coding: utf-8 -*-
"""
Qualitative Analysis Software 101 — ImpactMojo 101 Series (native deck spec)
What QDA software does and does not do; preparing transcripts in Indian languages; the coding
workflow; Taguette and QualCoder (free); NVivo, MAXQDA and ATLAS.ti compared; queries and
matrices; team coding and agreement; mixed methods; rigour and reporting; AI features and
what to disclose. For researchers, students and NGO teams in South Asia.
Build: python3 scripts/deck-builder/build.py qda_software
"""

DECK = {
    "slug": "qda-software",
    "title": "Qualitative Analysis Software 101",
    "description": ("Qualitative Analysis Software 101 — a free foundational course on NVivo, "
                    "MAXQDA, ATLAS.ti and the free tools Taguette and QualCoder. What the software "
                    "does and does not do, preparing transcripts in Hindi, Bangla and Tamil, the "
                    "coding workflow from codebook to memo, queries and matrices, coding in teams "
                    "with agreement checks, integrating with survey data, rigour and reporting to "
                    "COREQ and SRQR, and the AI features with their risks. For researchers, students "
                    "and NGO teams in South Asia. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Qualitative<br>Analysis<br>Software 101",
         "sub": "NVivo, MAXQDA, ATLAS.ti, Taguette and QualCoder &mdash; from Transcript to "
                "Theme, with the Thinking Left to You",
         "tags": ["Research Methods", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What the Software Does, and Does Not"},
             {"name": "Preparing the Data"},
             {"name": "The Coding Workflow"},
             {"name": "Taguette: The Free Start"},
             {"name": "QualCoder: Free and Full"},
             {"name": "NVivo, MAXQDA and ATLAS.ti"},
             {"name": "Queries, Matrices and Visuals"},
             {"name": "Coding in Teams"},
             {"name": "Mixed Methods"},
             {"name": "Rigour and Reporting"},
             {"name": "AI, Choosing a Tool, and Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What the Software Does, and Does Not"},

        {"type": "content", "label": "Definition", "title": "QDA software is a filing system for evidence, not an analyst",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Qualitative data analysis software (QDAS, CAQDAS)",
                        "def": "A program that stores texts, audio, video and images; lets the "
                        "researcher attach codes to segments of them; keeps memos and "
                        "attributes alongside; and retrieves, counts, cross-tabulates and "
                        "displays what was coded. It does the bookkeeping of analysis. It "
                        "does not do the analysis."},
                       {"t": "body", "html": "Forty interviews in three languages, coded by "
                        "hand with highlighters and index cards, is possible and was done for "
                        "decades. Software makes the retrieval instant ('every passage coded "
                        "<em>fear of the bank</em> among women in Gaya'), the codebook "
                        "consistent, the audit trail automatic, and the team's work "
                        "mergeable. The interpretation, the codes' meanings, the themes and "
                        "the claims come from the researcher, exactly as before."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "What it stores: documents, transcripts, PDFs, audio and video with time-stamped coding, images, survey open-ends, field notes, photographs.",
                  "What it attaches: codes (a hierarchy), memos (your thinking), attributes (respondent age, district, arm), links between segments.",
                  "What it retrieves: all segments by code, by code and attribute, by co-occurrence, by proximity; word frequencies; matrices of codes by cases.",
                  "What it displays: code trees, matrices, co-occurrence tables, networks, comparison diagrams, word clouds (of little use)."]},
                        {"t": "hbox", "color": "amber", "html": "The recurring failure in "
                         "student work: a project with 240 codes and no argument. The "
                         "software made the codes easy; nothing made the argument."}]},
         ]},

        {"type": "content", "label": "The Field", "title": "The tools: five to know, and what each is",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Maker", "Cost (approximate, 2026)", "Where it stands"],
              "rows": [
                  ["Taguette", "R&eacute;mi Rampin and contributors; open source", "Free; runs locally or on a server; a hosted version at taguette.org", "The simplest tool: highlight and tag text; exports everything. The right first tool and enough for many projects"],
                  ["QualCoder", "Colin Curtain and contributors; open source, Python", "Free; desktop", "Full-featured: text, PDF, image, audio and video coding; attributes; queries; coder comparison; REFI-QDA export"],
                  ["NVivo", "Lumivero (formerly QSR International)", "Student licences roughly US$100 a year; institutional site licences common at Indian universities", "The most widely taught; strong queries and matrices; transcription and AI add-ons"],
                  ["MAXQDA", "VERBI Software, Berlin", "Similar student pricing; educational licences", "Strong on mixed methods and visual tools; a Stats module; team cloud"],
                  ["ATLAS.ti", "ATLAS.ti Scientific Software Development, Berlin", "Similar; a web version by subscription", "Quotation-based; networks; the earliest AI coding features"],
                  ["Also: Dedoose, Quirkos, Delve", "Various", "Monthly subscriptions", "Web-based, simpler; Dedoose is built for mixed-methods teams"]]},
             {"t": "body", "cls": "sm", "html": "Prices change; check the vendors. What does "
              "not change: the free tools now cover the coding workflow completely, the "
              "commercial three differ in interface and advanced features more than in "
              "what they let you conclude, and every tool can export a project to the "
              "REFI-QDA exchange format so a team need not agree on one."},
         ]},

        {"type": "content", "label": "Method First", "title": "The method is not in the software",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Thematic analysis, framework analysis, "
                        "grounded theory, content analysis, narrative analysis and discourse "
                        "analysis all use codes and all can be done in any of these tools. "
                        "The software does not know which you are doing, and a project that "
                        "starts in NVivo without a stated method ends as an inductive "
                        "thematic analysis by default, because that is what unstructured "
                        "coding produces. Decide the method from the question; then use the "
                        "software to do that method's steps."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Reflexive thematic analysis (Braun and Clarke, <em>Qualitative Research in Psychology</em> 2006, 3:77; updated 2019 and 2021): codes are the researcher's interpretive labels; themes are built, not found; no codebook agreement is sought.",
                           "Framework analysis (Gale and colleagues, <em>BMC Medical Research Methodology</em> 2013, 13:117): a matrix of cases by themes, charted; built for applied policy research with deadlines and teams.",
                           "Grounded theory (Charmaz, <em>Constructing Grounded Theory</em>, 2nd ed., Sage, 2014): open, focused and theoretical coding toward a theory; constant comparison; memos central.",
                           "Content analysis: counting categories in text; the one method where the software's counts are the result."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Saldaña's manual", "html":
                         "<em>The Coding Manual for Qualitative Researchers</em> (4th ed., "
                         "Sage, 2021) catalogues thirty-odd coding methods (descriptive, in "
                         "vivo, process, values, versus, and so on) and says which suit which "
                         "questions. It is method-neutral about software and the best "
                         "companion to this course. Qualitative Methods 101 in this series "
                         "is the course on the methods themselves; this one is on the tools "
                         "that carry them."},
                        {"t": "hbox", "color": "green", "html": "Write the method and the "
                         "coding approach in the protocol before opening the software. The "
                         "tool then has a job."}]},
         ]},

        {"type": "content", "label": "When", "title": "When software helps, and when a table in Word is enough",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Situation", "Software worth it?", "Why"],
              "rows": [
                  ["Six key-informant interviews, one analyst, a report in three weeks", "Marginal", "A framework matrix in Word or a spreadsheet does it; the software's setup costs a day"],
                  ["Forty interviews, two languages, two coders, a thesis", "Yes", "Retrieval, consistency, merging and the audit trail; hand methods fail at this scale"],
                  ["Two hundred open-ended survey responses", "Yes, a simple tool", "Taguette or the spreadsheet route (section 09); coding is fast, counting is the point"],
                  ["Focus groups with audio, needing time-stamped coding of who said what", "Yes, a fuller tool", "QualCoder, NVivo, MAXQDA and ATLAS.ti code audio directly"],
                  ["A multi-year programme with recurring qualitative monitoring", "Yes, with a shared codebook", "The codebook and the project persist across rounds and staff"],
                  ["Documents and policy texts, hundreds of pages", "Yes", "Search, auto-coding by structure, and document attributes"],
                  ["Photographs and video from participatory work", "Yes, a fuller tool", "Region coding of images; video time-stamps"]]},
             {"t": "body", "cls": "sm", "html": "The threshold is roughly a dozen sources or "
              "two coders. Below it, the software is a habit to build for later; above it, "
              "the alternative is a filing system that cannot be searched."},
         ]},

        {"type": "content", "label": "Vocabulary", "title": "Vocabulary: the same ideas under five names",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Idea", "NVivo", "MAXQDA", "ATLAS.ti", "QualCoder", "Taguette"],
              "rows": [
                  ["A source file", "File (formerly Source)", "Document", "Document", "File", "Document"],
                  ["A coded passage", "Reference / coded content", "Coded segment", "Quotation", "Coded segment", "Highlight"],
                  ["A code", "Code (formerly Node)", "Code", "Code", "Code", "Tag"],
                  ["A code hierarchy", "Code tree; parent and child codes", "Code system", "Code groups; folders", "Code categories", "Nested by naming"],
                  ["Respondent characteristics", "Case classification attributes", "Document variables", "Document groups; attributes", "Attributes", "&mdash;"],
                  ["A note to yourself", "Memo; annotation", "Memo", "Memo; comment", "Memo; journal", "&mdash;"],
                  ["Cases by codes table", "Matrix coding query; framework matrix", "Code matrix browser; crosstab", "Code-document table", "Coding matrix", "Export and count"],
                  ["Co-occurrence", "Matrix coding query (code &times; code)", "Code relations browser", "Code co-occurrence table", "Code co-occurrence", "&mdash;"],
                  ["Project exchange", "REFI-QDA export/import", "Same", "Same", "Same", "CSV / DOCX export"]]},
             {"t": "body", "cls": "sm", "html": "This course uses the plain words (source, "
              "segment, code, attribute, memo, matrix) and names the tool's term where a "
              "menu is described. A researcher who knows the ideas can learn any of the "
              "five in a week."},
         ]},

        {"type": "content", "label": "South Asia", "title": "What is different about qualitative work here",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Languages.</strong> Interviews in Hindi, Bangla, Tamil, Marathi, Odia or a mix, with code-switching within a sentence; transcription and translation decisions decide what can be coded and by whom. Section 02.",
                  "<strong>Scripts.</strong> Every tool here handles Unicode Indic text for display and search; word frequencies and auto-coding are built for English and behave unpredictably on inflected Indian languages. Test before relying on them.",
                  "<strong>Teams.</strong> Field researchers who did the interviews, an analyst who did not, and a supervisor who reads English: the workflow has to carry meaning across all three. Section 08.",
                  "<strong>Connectivity and cost.</strong> Desktop tools that run offline (QualCoder, NVivo, MAXQDA, ATLAS.ti desktop) versus web tools that need a connection (Taguette hosted, Dedoose, ATLAS.ti Web). District offices decide this.",
                  "<strong>Data protection.</strong> Interview recordings and transcripts are personal data under India's Digital Personal Data Protection Act 2023; where they are stored, and whether an AI feature sends them abroad, is a compliance question. Sections 02 and 11."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The commonest South Asian "
                        "workflow, translating everything to English first and coding the "
                        "English, is also the one that loses the most. Section 02 sets out "
                        "the alternatives and their costs."}]},
         ]},

        {"type": "content", "label": "This Course", "title": "How the course is arranged",
         "blocks": [
             {"t": "flow", "steps": [
                 "PREPARE: consent, transcription, translation, file formats, attributes (02)",
                 "CODE: codebook, first cycle, second cycle, memos, saturation (03)",
                 "TOOLS: Taguette (04), QualCoder (05), the commercial three (06)",
                 "ANALYSE: queries, matrices, visuals (07)",
                 "TEAM: agreement, merging, versions (08)",
                 "INTEGRATE: with surveys and numbers (09)",
                 "REPORT: rigour, transparency, COREQ and SRQR (10)",
                 "DECIDE: AI features, tool choice, a worked project (11)"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Sections 02, 03, 07 to 10 are about the work "
                        "and apply whatever the tool. Sections 04 to 06 are about the tools, "
                        "with the free ones first and in more detail because they are the "
                        "ones most readers of this course can install today. Worked examples "
                        "follow one illustrative study: 36 interviews with women in "
                        "self-help groups in Bihar and West Bengal, in Hindi and Bangla, "
                        "about savings and household decisions."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Qualitative Methods 101 "
                        "covers interviewing, sampling and the methods; Research Ethics "
                        "101 covers consent. This course starts where the recordings "
                        "exist."}]},
         ]},

        # ===================== SECTION 02: PREPARING THE DATA =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Preparing the Data"},

        {"type": "content", "label": "Consent", "title": "Consent decides what the software may hold and where",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Before a recording is imported, three "
                        "questions from the consent form decide the workflow. Did the "
                        "participant agree to recording, to transcription by a third party, "
                        "and to storage of the transcript? Did they agree to quotation in "
                        "publications, with what anonymisation? Did they agree to the data "
                        "being processed by an external service (a transcription API, a "
                        "cloud QDA tool, an AI assistant)? A 'no' to the last removes most "
                        "cloud features from the project."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Store recordings and transcripts on encrypted, access-controlled storage; the QDA project file contains the transcripts and needs the same protection.",
                           "Pseudonymise at transcription (a participant ID, place names generalised to district) and keep the key separately.",
                           "Under India's DPDP Act 2023, participants are data principals with rights to know and to erasure; a research exemption exists for specified purposes but does not cover careless handling. Data Protection & the DPDP Act 101 in this series is the reference.",
                           "For cross-border processing (most AI and transcription services), check the consent wording and the institution's policy."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Data sharing later", "html":
                         "Funders increasingly ask for qualitative data to be archived "
                         "(the Qualitative Data Repository at Syracuse, UK Data Service). "
                         "That is possible only if consent covered it and the transcripts "
                         "are de-identified to a documented standard. Decide at the consent "
                         "stage; it cannot be added afterwards."},
                        {"t": "hbox", "color": "green", "html": "Record in the project's first "
                         "memo what each participant consented to. The software can carry "
                         "it as an attribute (quotation permitted: yes/no) and filter on "
                         "it."}]},
         ]},

        {"type": "content", "label": "Transcription", "title": "Transcription: what level, by whom, in what script",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Level", "What is captured", "Cost", "Suits"],
                        "rows": [
                            ["Intelligent verbatim", "Every word, with fillers and false starts removed", "About 4&ndash;6 hours per hour of audio by hand; minutes by machine plus checking", "Thematic and framework analysis; most applied work"],
                            ["Full verbatim", "Every word, filler, repetition and pause", "6&ndash;8 hours per hour", "Discourse and conversation analysis; where the how matters"],
                            ["Jefferson-style", "Timing, overlap, intonation marked", "10+ hours per hour", "Conversation analysis only"],
                            ["Summary or notes", "Content summarised by the interviewer", "Under an hour", "Rapid appraisal; not for coding"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "For Indian languages, machine "
                        "transcription has become usable: ImpactMojo's own VaniScribe runs on "
                        "Sarvam's Indic speech models and returns Hindi, Tamil, Bangla and "
                        "other transcripts in native script for a few rupees a minute; "
                        "open-weight Indic models (Bodhan AI's Indic-Transcribe, released "
                        "September 2026) can run locally where data may not leave the "
                        "machine. All machine output needs a human pass by someone who "
                        "heard the interview; the error rate on rural speech, mixed "
                        "languages and named places is not small."},
                        {"t": "hbox", "color": "amber", "html": "Transcribe in the language "
                         "spoken, in its script, with a speaker label and a timestamp every "
                         "minute. Translation is a separate step and a separate decision."}]},
         ]},

        {"type": "content", "label": "Translation", "title": "Translation: three workflows and what each loses",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "A. Code in the source language", "html":
                         "Transcripts stay in Hindi and Bangla; coders read those languages; "
                         "codes and memos are in English or bilingual; only the quotations "
                         "used in the report are translated, by the analyst, with the "
                         "original beside them. Loses least. Requires coders in each "
                         "language and a bilingual codebook."},
                        {"t": "panel", "color": "amber", "title": "B. Translate everything, code the English", "html":
                         "One translated corpus; any coder can work; supervisors can read "
                         "it. Loses idiom, register, the word the respondent chose, and "
                         "introduces the translator's interpretation before the analysis "
                         "starts (Temple and Young, <em>Qualitative Research</em> 2004, "
                         "4:161). The commonest workflow and the most lossy."},
                        {"t": "panel", "color": "green", "title": "C. Parallel: source and translation side by side", "html":
                         "Both versions imported; coding on the source with the "
                         "translation visible (MAXQDA and NVivo can display paired "
                         "documents; QualCoder via a second file). Keeps the original in "
                         "reach; doubles the storage; the practical compromise."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Whatever the workflow, record who translated, whether the translation was checked, and how untranslatable terms were handled (kept in transliteration with a gloss: <em>izzat</em> (honour, standing)).",
                  "Keep the source-language words for the concepts that carry the analysis. A theme called 'shame' built from <em>sharam</em> and <em>lajja</em> in two languages is a theme that needs both words in the report.",
                  "Machine translation of transcripts (Sarvam's Mayura, Bodhan's Indic-Translate, or general models) is now good enough for a coder's first read and not for a quotation in print.",
                  "The report says which workflow was used. Reviewers ask."]}]},
         ]},

        {"type": "content", "label": "Files", "title": "File formats, structure and what imports cleanly",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Material", "Format to import", "Notes"],
              "rows": [
                  ["Transcripts", ".docx or .txt, UTF-8; one file per interview", "Speaker labels on their own line ('I:' and 'R:', or names); a header block with ID, date, place, language; consistent formatting lets NVivo and MAXQDA auto-code speakers"],
                  ["Audio", ".mp3, .wav, .m4a", "QualCoder, NVivo, MAXQDA and ATLAS.ti code audio with time-stamps and can link a transcript to it; Taguette does not take audio"],
                  ["Video", ".mp4", "Large files; compress first; region and time coding"],
                  ["PDFs (policy documents, reports)", "Text-based PDF, not scanned", "Scanned PDFs need OCR first (Bodhan's IndicOCR or Tesseract for Indic scripts); ATLAS.ti and MAXQDA code PDFs in place"],
                  ["Images, photographs", ".jpg, .png", "Region coding in QualCoder, NVivo, MAXQDA, ATLAS.ti"],
                  ["Survey open-ends", "A spreadsheet: one row per respondent, one column per question, plus attribute columns", "Import as a dataset (NVivo), a survey (MAXQDA), or a table of documents; each cell becomes codeable"],
                  ["Field notes, diaries", ".docx, .txt", "Date each entry; the researcher's own notes are data too"],
                  ["Social media, web pages", "Exported text; NCapture (NVivo) or copy", "Terms of service and ethics apply"]]},
             {"t": "body", "cls": "sm", "html": "Name files by a convention (INT_BR_014_HI for "
              "interview, Bihar, participant 14, Hindi) and keep a master sheet of files "
              "with attributes. The attributes are imported once and used in every "
              "matrix."},
         ]},

        {"type": "content", "label": "Attributes", "title": "Attributes: the variables that make qualitative data cross-tabulable",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Each interview carries characteristics of the "
                        "participant and the setting: state, district, SHG member or not, "
                        "years of membership, age band, education, language, interviewer, "
                        "date. Entered as attributes (NVivo case classifications, MAXQDA "
                        "document variables, ATLAS.ti document groups, QualCoder attributes), "
                        "they let every later query ask 'how does this theme appear among "
                        "members versus non-members' or 'in Bihar versus Bengal', which is "
                        "the comparison a mixed-methods evaluation needs."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Prepare a spreadsheet with one row per file and one column per attribute, and import it; typing attributes one by one is where errors enter.",
                           "Use the same codes as the survey (the same district names, the same arm labels) so qualitative and quantitative results line up in section 09.",
                           "Include the interviewer as an attribute. Interviewer effects are real and a matrix by interviewer is a quality check.",
                           "Attributes are for facts known before analysis. Judgements made during analysis (this woman is 'highly empowered') are codes, not attributes; keep them apart."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Focus groups", "html":
                         "A focus group is one file with many speakers. Attributes belong "
                         "to the group (village, date, composition) and speakers are coded "
                         "as speakers (NVivo and MAXQDA auto-code by speaker label), so that "
                         "'what did the older women say' is a query on speaker code &times; "
                         "theme. Without speaker coding, a focus group is one undifferentiated "
                         "voice, which is the commonest way focus-group data is wasted."},
                        {"t": "hbox", "color": "green", "html": "Ten attributes, a spreadsheet, "
                         "an hour. The return is every comparison in section 07."}]},
         ]},

        {"type": "content", "label": "Project Setup", "title": "Setting up the project: folders, naming, the first memo",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Element", "Convention", "Why"],
              "rows": [
                  ["Project file", "One per study; named with the study and date; on encrypted storage; backed up daily to a second place", "Project files corrupt and laptops are stolen"],
                  ["Source folders", "By type and site: Interviews/Bihar, Interviews/Bengal, FGDs, Documents, Field notes", "Attributes do the fine sorting; folders do the coarse"],
                  ["File names", "TYPE_SITE_ID_LANG (INT_WB_022_BN)", "Sortable; language visible; ID matches the master sheet and the survey"],
                  ["Attribute sheet", "One spreadsheet, imported; the master list", "Section 02"],
                  ["Codebook", "Started from the protocol's a priori codes, with definitions; versioned", "Section 03"],
                  ["Memos", "A project memo (decisions, dated), a methods memo, a memo per emerging theme, and coding memos as needed", "The audit trail; section 10"],
                  ["Versions", "Save-as with a date at each milestone; never overwrite the only copy", "Recovery and the trail"],
                  ["Team", "One master project; coders work on copies and merge (section 08), or use a server or cloud version", "Merging is where projects break"]]},
             {"t": "body", "cls": "sm", "html": "The first memo, written before any coding, "
              "states the question, the method, the coding approach, the translation "
              "workflow, the team's roles and the consent constraints. It is the methods "
              "section's first draft and the document a new team member reads first."},
         ]},

        {"type": "content", "label": "Cleaning Text", "title": "Cleaning transcripts before import: what to fix and what to leave",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Fix</strong>: speaker labels (consistent, on their own line); encoding (UTF-8, so Devanagari and Bangla render); identifying details (names, phone numbers, specific villages) replaced with placeholders in square brackets; headers with ID and attributes.",
                  "<strong>Fix</strong>: transcription errors found on the checking pass, with the audio timestamp noted where the correction is a judgement.",
                  "<strong>Leave</strong>: the respondent's grammar, dialect, mixed languages and hesitations at the transcription level chosen. Cleaning speech into standard prose is editing the data.",
                  "<strong>Leave</strong>: the interviewer's questions. They are context for every answer and evidence of leading."]}],
              "right": [{"t": "panel", "color": "amber", "title": "A checking pass", "html":
                         "Someone who was present, or who speaks the language natively, "
                         "reads each transcript against the audio for ten minutes at three "
                         "points and corrects; if the error rate is high, the whole "
                         "transcript is rechecked. Record the check as an attribute "
                         "(checked: yes/no, by whom). Machine transcripts of Bhojpuri-"
                         "inflected Hindi from a noisy courtyard need the whole pass."},
                        {"t": "hbox", "color": "green", "html": "Do the cleaning in the word "
                         "processor before import. Editing text inside a QDA project after "
                         "coding has started can detach codes from their passages in some "
                         "tools."}]},
         ]},

        {"type": "content", "label": "Data Checklist", "title": "Before coding: the data checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Check", "Done"],
              "rows": [
                  ["Consent for recording, transcription, storage, quotation and external processing recorded per participant", ""],
                  ["Recordings and transcripts on encrypted storage with a backup", ""],
                  ["Transcription level chosen and stated; language and script decided", ""],
                  ["Every machine transcript checked by a native speaker; the check recorded", ""],
                  ["Translation workflow chosen (A, B or C) and stated; translators named", ""],
                  ["Files named by convention; one file per interview or group", ""],
                  ["Speaker labels consistent; focus-group speakers identifiable", ""],
                  ["Pseudonymised; key stored separately", ""],
                  ["Attribute sheet complete and imported; codes match the survey's", ""],
                  ["Project folders, first memo and a priori codebook in place", ""],
                  ["Project file backed up and versioned", ""]]},
             {"t": "body", "cls": "sm", "html": "A week for a 36-interview study, most of it "
              "the transcript checking. It is the week that decides whether the coding can "
              "be trusted, and it is the week most often compressed."},
         ]},

        # ===================== SECTION 03: THE CODING WORKFLOW =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The Coding Workflow"},

        {"type": "content", "label": "What a Code Is", "title": "A code is a label with a definition, an example and a boundary",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Code",
                        "def": "A word or short phrase that assigns a summative, salient, "
                        "essence-capturing attribute to a portion of data (Salda&ntilde;a). "
                        "In software, a named container to which segments are attached. In "
                        "a codebook, a name, a definition, when to use it, when not to, and "
                        "an example."},
                       {"t": "body", "html": "The difference between a project that yields "
                        "findings and one that yields a code list is the definition. "
                        "'Fear' is a word; 'FEAR OF FORMAL FINANCE: expressions of anxiety, "
                        "avoidance or distrust toward banks, loan officers or paperwork, "
                        "including stories of others' bad experiences; not general worry "
                        "about money (see MONEY WORRY)' is a code another coder can apply "
                        "and a reader can check."}],
              "right": [{"t": "table",
                         "head": ["Codebook field", "Example"],
                         "rows": [
                             ["Name", "FEAR_FORMAL_FINANCE"],
                             ["Definition", "Anxiety, avoidance or distrust toward banks, officers, forms"],
                             ["Use when", "Respondent describes her own or others' fear or avoidance"],
                             ["Do not use when", "Worry about money in general (MONEY_WORRY); anger at a specific officer (BANK_MISTREATMENT)"],
                             ["Example", "'I never went inside; they would ask for papers I don't have' (INT_BR_014)"],
                             ["Source", "A priori, from the theory of change; revised 2026-03-04 after five transcripts"]]},
                        {"t": "hbox", "color": "amber", "html": "Every tool has a field for "
                         "a code's description. Fill it. A code without a definition is a "
                         "guess about what you meant, made later, by you."}]},
         ]},

        {"type": "content", "label": "The Cycle", "title": "First-cycle and second-cycle coding",
         "blocks": [
             {"t": "flow", "steps": [
                 "READ: every transcript once, without coding, with notes",
                 "A PRIORI CODES: from the protocol and theory of change, defined",
                 "FIRST CYCLE: code five transcripts closely; add inductive codes as they arise; memo",
                 "REVISE: merge, split, define; version the codebook; recode the five",
                 "CODE ALL: the rest, with the revised codebook; new codes flagged and reviewed",
                 "SECOND CYCLE: group codes into categories and themes; pattern coding; matrices",
                 "WRITE: themes as claims with evidence; back to the data to check"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "First-cycle coding labels the data; second-cycle "
                        "coding (Salda&ntilde;a's pattern, focused, axial and theoretical "
                        "coding) organises the labels into an account. The software serves "
                        "both: the first through attaching codes to segments, the second "
                        "through the code hierarchy, merging, and the matrices of section "
                        "07. The revision step after five transcripts is where most of the "
                        "codebook's quality is made, and it is the step most often skipped."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Recoding the first five "
                        "transcripts after the codebook is revised is not wasted work. "
                        "Those five were coded with a codebook that no longer exists."}]},
         ]},

        {"type": "content", "label": "Hierarchies", "title": "Code hierarchies: how deep, how many, and the two failure modes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Codes nest: SAVINGS contains SAVINGS_PURPOSE, "
                        "SAVINGS_BARRIER, SAVINGS_GROUP_RULES; each of those contains two or "
                        "three children. Two or three levels is workable; five is not. A "
                        "project for 36 interviews on a focused question ends with perhaps "
                        "40 to 80 codes after revision, organised under eight to fifteen "
                        "parents. Two hundred codes is a project that labelled every "
                        "sentence and has not yet begun to analyse."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Too many codes: every segment gets its own label; retrieval returns one segment per code; nothing accumulates. Merge by definition.",
                           "Too few: 'EMPOWERMENT' holds 300 segments and every retrieval is the whole dataset. Split by the distinctions the segments show.",
                           "Descriptive parents (topics: SAVINGS, DECISIONS, HUSBAND) and analytic children (what is said about them) is a workable first structure; themes emerge across the parents.",
                           "Coding at the parent as well as the child is a setting in NVivo and MAXQDA ('aggregate'); decide it once."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Themes are not codes", "html":
                         "A theme is a claim about the data ('women use group savings as "
                         "a shield against household demands, which reshapes who decides'), "
                         "built across codes and cases. In the software it may be a "
                         "parent code that collects the evidence, or a memo that argues "
                         "it, or a set (NVivo) or a document group (ATLAS.ti). Braun and "
                         "Clarke's insistence that themes are constructed, not found, is a "
                         "warning against reading the code tree as the findings."},
                        {"t": "hbox", "color": "green", "html": "Print the code tree at each "
                         "version. The sequence of trees is the history of the analysis "
                         "and belongs in the appendix."}]},
         ]},

        {"type": "content", "label": "Segments", "title": "How much to code: the unit of analysis",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A code attaches to a segment: a phrase, a "
                        "sentence, a paragraph, a whole answer. Too small and the segment "
                        "means nothing out of context when retrieved; too large and every "
                        "retrieval is a page to reread. The working rule is the smallest "
                        "unit that makes sense on its own when retrieved, which is usually "
                        "a sentence or two with the question that prompted it. Decide it in "
                        "the codebook and apply it consistently, because inter-coder "
                        "agreement (section 08) depends on it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Overlapping codes on one segment are normal and are what co-occurrence queries use.",
                           "Code the interviewer's question with the answer when the question shaped it.",
                           "In vivo codes (the respondent's own phrase as the code name: <em>'mera paisa'</em>, my money) keep the language in the analysis and are worth a parent of their own.",
                           "Uncodeable material (small talk, the tea break) is left uncoded; 'everything must be coded' is a superstition."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Auto-coding and its limits", "html":
                         "NVivo and MAXQDA can auto-code by structure (every answer to "
                         "question 4 gets code Q4; every speaker gets a speaker code) and by "
                         "text search (every passage containing 'bank' gets BANK_MENTION). "
                         "The first is reliable and saves hours. The second finds words, "
                         "not meanings, misses synonyms and Indian-language variants, and "
                         "should be treated as a way to find passages to read, never as "
                         "coding. AI-assisted coding (section 11) is the second kind with "
                         "better vocabulary and the same limit."},
                        {"t": "hbox", "color": "green", "html": "A human coder reading with "
                         "a defined codebook does about eight to twelve transcript pages "
                         "an hour. Budget from that."}]},
         ]},

        {"type": "content", "label": "Memos", "title": "Memos: where the analysis actually happens",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A memo is a dated note in the project: about a "
                        "code (what it is coming to mean, how it differs from its "
                        "neighbour), about a case (what is distinctive about this woman's "
                        "account), about a pattern (members in Bengal talk about the bank "
                        "differently from Bihar), about the method (why the codebook changed), "
                        "or about the researcher (what I expected and am seeing). Every tool "
                        "has them and links them to codes, files and segments. Grounded "
                        "theorists treat memo-writing as the analysis; every method benefits "
                        "from it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Write a memo whenever you make a decision, notice a pattern, or feel surprised. Surprise is data about your assumptions.",
                           "Date every entry; the sequence is the audit trail.",
                           "Theme memos become the findings' first drafts; method memos become the methods section; reflexive memos become the reflexivity statement.",
                           "Link memos to the segments that prompted them, so the evidence is one click away."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Illustrative theme memo, 2026-03-11", "html":
                         "'Across the eleven Bihar members coded so far, SAVINGS_PURPOSE "
                         "co-occurs with HUSBAND_DEMANDS in seven; the phrase is some version "
                         "of the money being \"in the group\" and therefore not available. "
                         "Non-members describe savings as at home and \"taken\". The group "
                         "seems to function as a socially acceptable refusal. Check: Bengal "
                         "members (not yet coded); whether the four Bihar exceptions are "
                         "women whose husbands are migrants (attribute query). Possible "
                         "theme: the group as shield. Related: Kabeer's control over "
                         "resources.'"},
                        {"t": "hbox", "color": "green", "html": "That memo is a finding, a "
                         "test, a hypothesis and a citation, in one paragraph, written at "
                         "transcript eleven."}]},
         ]},

        {"type": "content", "label": "Saturation", "title": "Saturation: what the software can show and what it cannot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Saturation is the point at which further data "
                        "add no new codes or refine no themes. The software can show when "
                        "new codes stopped appearing (a count of codes created per "
                        "transcript, in order coded) and when a theme's evidence stopped "
                        "growing. It cannot tell you whether you would have found something "
                        "new had you interviewed a different kind of person. Guest, Bunce "
                        "and Johnson (<em>Field Methods</em> 2006, 18:59) found most new "
                        "codes within the first twelve interviews of a homogeneous sample; "
                        "Braun and Clarke argue saturation is the wrong frame for reflexive "
                        "thematic analysis at all."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Report the code-creation curve if you claim saturation; it is a matrix of transcript order by new codes, available in any tool.",
                           "Report which subgroups the claim covers: saturation among Bihar members says nothing about Bengal non-members.",
                           "'Data saturation was reached' without evidence is the qualitative equivalent of 'the model fit'."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The honest sentence: 'No new "
                        "codes were created after the twenty-eighth of thirty-six "
                        "interviews; the last eight added instances to existing codes. "
                        "The sample was not designed to reach saturation among "
                        "non-members in Bengal (n = 5), and findings for that group are "
                        "indicative.'"}]},
         ]},

        {"type": "content", "label": "Worked Codebook", "title": "A worked codebook extract: the SHG study after revision",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Code", "Definition (abridged)", "Origin", "Segments", "Files"],
                        "rows": [
                            ["SAVINGS", "Parent: any talk of saving money, in group or otherwise", "A priori", "&mdash;", "36"],
                            ["&nbsp;&nbsp;SAVINGS_PURPOSE", "What the money is for: emergencies, school, ceremonies, business", "A priori", "94", "34"],
                            ["&nbsp;&nbsp;SAVINGS_SHIELD", "Savings described as protected from household demands by being 'in the group'", "Inductive, transcript 6", "41", "22"],
                            ["&nbsp;&nbsp;SAVINGS_BARRIER", "What prevents saving: income, husband, group rules, distance", "A priori", "67", "31"],
                            ["DECISIONS", "Parent: who decides what, and how that is negotiated", "A priori", "&mdash;", "36"],
                            ["&nbsp;&nbsp;DECISION_SMALL", "Daily purchases, food, children's small needs", "A priori", "58", "33"],
                            ["&nbsp;&nbsp;DECISION_LARGE", "Assets, loans, ceremonies, migration", "A priori", "72", "35"],
                            ["&nbsp;&nbsp;DECISION_STRATEGY", "How women get a say: timing, allies, group backing, withholding", "Inductive, transcript 9", "53", "27"],
                            ["FORMAL_FINANCE", "Parent: banks, officers, forms, phones", "A priori", "&mdash;", "30"],
                            ["&nbsp;&nbsp;FEAR_FORMAL_FINANCE", "Anxiety, avoidance, distrust", "A priori, redefined", "38", "21"],
                            ["IN_VIVO", "Respondents' own phrases kept as codes", "Inductive", "29", "19"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative. Eleven of the "
                        "study's 46 codes, with their origin and their counts from the "
                        "code-summary report every tool produces. Two inductive codes "
                        "(SHIELD, STRATEGY) became the analytic centre of the study and "
                        "neither was in the protocol. The counts are for orientation (a "
                        "code in 22 of 36 files is widespread; one in 3 is not) and are not "
                        "findings."},
                        {"t": "hbox", "color": "amber", "html": "Version 3 of the codebook, "
                         "dated. Versions 1 and 2 are in the appendix with what changed and "
                         "why."}]},
         ]},

        {"type": "content", "label": "Coding Checklist", "title": "The coding workflow: the checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Practice", "Done"],
              "rows": [
                  ["Method and coding approach stated in the first memo", ""],
                  ["A priori codes defined from the protocol before coding", ""],
                  ["Every transcript read once before coding", ""],
                  ["First five transcripts coded closely; codebook revised; the five recoded", ""],
                  ["Every code has a definition, use and do-not-use rules, and an example", ""],
                  ["Codebook versioned with dates and reasons", ""],
                  ["Segment size decided and consistent", ""],
                  ["Memos written at decisions, patterns and surprises; dated; linked", ""],
                  ["Inductive codes flagged and reviewed by a second person", ""],
                  ["Second-cycle grouping done deliberately, with theme memos", ""],
                  ["Saturation, if claimed, evidenced by the code-creation curve", ""],
                  ["Auto-coding and text search used to find, never to code", ""]]},
             {"t": "body", "cls": "sm", "html": "Twelve rows. They apply in Taguette and in "
              "NVivo equally, and they are what a methods reviewer means by 'systematic'."},
         ]},

        # ===================== SECTION 04: TAGUETTE =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Taguette: The Free Start"},

        {"type": "content", "label": "What It Is", "title": "Taguette: highlight, tag, export, and nothing else",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Taguette is a free, open-source tool that "
                        "runs in the browser: install it with one command on a laptop, or "
                        "use the hosted version at taguette.org. A project holds documents; "
                        "you select a passage and give it one or more tags; tags have "
                        "descriptions; everything exports to Word, CSV or HTML. It handles "
                        "text (.docx, .pdf, .txt, .html, .odt, .rtf, .epub) and nothing "
                        "else: no audio, no video, no attributes, no memos beyond tag "
                        "descriptions, no queries beyond 'show me everything with this "
                        "tag'."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Right for: a first qualitative project; a small study of text; teaching coding without a licence; a team that needs to code together in a browser.",
                           "Not right for: audio coding, attribute comparisons, co-occurrence analysis, large corpora.",
                           "Everything you tag can be taken to a fuller tool later: the highlight export is a spreadsheet of segment, tag and document."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Install and run", "html":
                         "On a machine with Python: <code>pip install taguette</code>, "
                         "then <code>taguette</code>, and the browser opens at a local "
                         "address; data stays on the machine. Windows and Mac installers "
                         "exist. The hosted service at app.taguette.org needs an account "
                         "and stores your documents on its server, which the consent form "
                         "must allow; a self-hosted server (the same software on an "
                         "institution's machine) gives the collaboration without the "
                         "storage question."},
                        {"t": "hbox", "color": "green", "html": "Ten minutes from download to "
                         "first tag. That is the argument for starting here."}]},
         ]},

        {"type": "content", "label": "Workflow", "title": "A Taguette project, step by step",
         "blocks": [
             {"t": "flow", "steps": [
                 "NEW PROJECT: name it; add a description that is the first memo",
                 "ADD DOCUMENTS: one per interview; the file name carries the ID and language",
                 "CREATE TAGS: the a priori codebook, each with its definition in the description field",
                 "HIGHLIGHT: select text, choose tags (several at once), save",
                 "REVIEW: click a tag to see every highlight; merge or rename tags as the codebook evolves",
                 "EXPORT: codebook, highlights by tag, and the whole project, for the appendix and the next tool"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Tags are flat, so a hierarchy is made by "
                        "naming: SAVINGS.purpose, SAVINGS.shield, SAVINGS.barrier. Searching "
                        "'SAVINGS' then finds the family. Merging two tags (select both, "
                        "merge) reassigns every highlight, which is how first-cycle codes "
                        "become second-cycle ones. Tag descriptions are the only memo field, "
                        "so the codebook's definitions live there and the analytic memos "
                        "live in a separate document."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Highlights can overlap and a "
                        "passage can carry several tags. The 'all highlights' view with "
                        "its tag filter is the retrieval tool, and for a study of twenty "
                        "documents it is enough."}]},
         ]},

        {"type": "content", "label": "Collaboration", "title": "Coding together in Taguette",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "On a server (hosted or self-hosted), a "
                        "project owner adds collaborators by username with full or "
                        "view-only access, and several people can tag the same documents "
                        "at once; each highlight records who made it. That makes Taguette "
                        "the simplest tool for a small team coding together, and for a "
                        "supervisor who wants to see a student's coding as it happens. It "
                        "does not compute agreement; section 08's spreadsheet method does "
                        "that from the highlight export."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Agree the codebook in the tag descriptions first, so every coder reads the same definition.",
                           "For an agreement check, two coders tag the same three documents with distinct tag sets (A.SAVINGS, B.SAVINGS), export, and compare.",
                           "The local version is single-user; sharing a local project means sharing the .sqlite3 file, which is not simultaneous."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "A self-hosted Taguette on an "
                        "institutional server is the cheapest collaborative QDA "
                        "environment that keeps data inside the institution. An IT "
                        "department can set it up in an afternoon."}]},
         ]},

        {"type": "content", "label": "Exports", "title": "What comes out, and what to do with it",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Export", "Format", "Use"],
              "rows": [
                  ["Codebook", ".csv, .docx, .xlsx, .html", "The appendix table of tags and definitions; the codebook for a fuller tool"],
                  ["Highlights for one tag", ".docx, .html, .csv", "The evidence for a theme, ready to quote; a document to read through when writing"],
                  ["All highlights", ".csv (document, tag, text)", "A spreadsheet for counting tags by document, for the agreement check, and for pivot tables by attribute if you add the attribute columns by hand"],
                  ["A document with its highlights", ".docx, .html", "A marked-up transcript for a supervisor or a participant check"],
                  ["The whole project", ".sqlite3", "The backup; reimportable into another Taguette"],
                  ["REFI-QDA", "Not supported", "Move to a fuller tool via the CSV export and re-code, or via QualCoder's import of the CSV as a starting point"]]},
             {"t": "body", "cls": "sm", "html": "The all-highlights CSV is the most useful "
              "object Taguette produces: opened in a spreadsheet with the attribute sheet "
              "joined on document name, it supports every count and matrix in section 07, "
              "by pivot table. That is a serviceable analysis for a small study and a good "
              "way to learn what the fuller tools automate."},
         ]},

        {"type": "content", "label": "Limits", "title": "Where Taguette runs out, and the signs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Need", "Taguette", "Move to"],
              "rows": [
                  ["Coding audio or video directly", "No", "QualCoder (free), or the commercial three"],
                  ["Attributes (district, arm) and matrices by them", "By hand in the CSV export", "QualCoder or the commercial three"],
                  ["Memos linked to segments and codes", "Tag descriptions only", "Any fuller tool"],
                  ["Co-occurrence and proximity queries", "No", "QualCoder (basic), commercial (full)"],
                  ["A real hierarchy with aggregation", "Naming convention only", "Any fuller tool"],
                  ["Inter-coder agreement statistics", "By hand from the export", "QualCoder, NVivo, MAXQDA, ATLAS.ti"],
                  ["Hundreds of documents", "Slows; the flat tag list becomes unwieldy", "Any fuller tool"],
                  ["REFI-QDA exchange", "No", "QualCoder and the commercial three"]]},
             {"t": "body", "cls": "sm", "html": "The sign is usually the third time you build "
              "the same pivot table by hand. A project that started in Taguette moves to "
              "QualCoder with a morning's re-coding from the highlight export, and the "
              "codebook comes with it."},
         ]},

        {"type": "content", "label": "Teaching", "title": "Taguette in the classroom: a three-session sequence",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Session", "Activity", "Output"],
                        "rows": [
                            ["1", "Install; import three anonymised transcripts; create six a priori tags from a supplied codebook; tag one transcript each", "A tagged transcript; a first argument about a definition"],
                            ["2", "Two students tag the same transcript with prefixed tags; export; compare in a spreadsheet; revise the codebook together", "An agreement table; codebook version 2"],
                            ["3", "Tag the rest; export highlights by tag; write one theme memo with three quotations", "A one-page theme memo"]]}],
              "right": [{"t": "body", "html": "Three sessions teach what coding is, why "
                        "definitions matter, why coders disagree, and what a theme looks "
                        "like when it is built from evidence. None of it requires a licence, "
                        "an account (the local version) or a fast machine. Students who "
                        "then meet NVivo find the ideas familiar and the menus merely "
                        "larger."},
                        {"t": "hbox", "color": "amber", "html": "The disagreement in session "
                         "2 is the lesson. Do not resolve it for them."}]},
         ]},

        {"type": "content", "label": "Worked Taguette", "title": "A worked mini-study in Taguette: twelve interviews, one question",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Tag", "Description (abridged)", "Highlights", "Documents"],
                        "rows": [
                            ["SAVINGS.purpose", "What the savings are for", "31", "12"],
                            ["SAVINGS.shield", "Savings protected from household demands by being in the group", "14", "8"],
                            ["SAVINGS.barrier", "What prevents saving", "22", "11"],
                            ["DECISION.large", "Assets, loans, ceremonies", "24", "12"],
                            ["DECISION.strategy", "How a say is obtained", "18", "9"],
                            ["FINANCE.fear", "Fear or avoidance of banks", "13", "7"],
                            ["INVIVO", "Respondents' phrases", "11", "8"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative: the Bihar members "
                        "only, coded in Taguette by one analyst in two days. The "
                        "SAVINGS.shield tag, created at the sixth transcript, appears in "
                        "eight of twelve; the export of its fourteen highlights is the "
                        "evidence for the theme memo on the earlier slide."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What was possible, what was not", "html":
                         "Possible: the codebook, the coding, the retrieval by tag, the "
                         "theme, a report with quotations, and an appendix with the "
                         "codebook and counts. Not possible without the spreadsheet: "
                         "'does SHIELD co-occur with HUSBAND demands' (section 07) and "
                         "'is SHIELD more common among women with migrant husbands' "
                         "(attributes). For twelve interviews the spreadsheet did both in "
                         "an hour."},
                        {"t": "hbox", "color": "amber", "html": "The study was then extended "
                         "to 36 interviews in two languages, and moved to QualCoder. The "
                         "next section."}]},
         ]},

        # ===================== SECTION 05: QUALCODER =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "QualCoder: Free and Full"},

        {"type": "content", "label": "What It Is", "title": "QualCoder: most of NVivo, for nothing, on your own machine",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "QualCoder is a free, open-source desktop "
                        "program written in Python by Colin Curtain and contributors. It "
                        "codes text, PDFs, images, audio and video; has a code hierarchy "
                        "with categories; memos on codes, files, cases, segments and a "
                        "journal; cases and attributes for files and cases; text search "
                        "and auto-coding; reports by code, file, case and attribute; code "
                        "frequencies and a co-occurrence matrix; a coder comparison with "
                        "agreement statistics; charts; and import and export in the "
                        "REFI-QDA exchange format. It runs offline. The project is a folder "
                        "with a database inside."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Right for: any project this course describes, up to the size where a team needs simultaneous access.",
                           "The interface is functional rather than polished; the documentation (a wiki and a manual) is thorough.",
                           "Audio and video need VLC installed; PDFs are read with their text layer."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Install", "html":
                         "Windows and Mac installers from the project's GitHub releases; "
                         "on Linux, <code>pip install qualcoder</code>. Recent versions add "
                         "optional LLM-assisted features that call an external model with "
                         "an API key you supply; they are off by default and section 11 "
                         "says what to think about before turning them on."},
                        {"t": "hbox", "color": "green", "html": "A student with a five-year-old "
                         "laptop, no budget and 36 interviews in two languages has "
                         "everything they need here."}]},
         ]},

        {"type": "content", "label": "The Windows", "title": "The QualCoder interface: files, codes, cases, reports",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Menu or tab", "What it does", "Used for"],
              "rows": [
                  ["Project", "New, open, close; import survey; project memo; settings (coder name, fonts, backups)", "Setup; set the coder name before coding"],
                  ["Manage &rarr; Files", "Import text, PDF, images, AV; edit file memos; assign attributes; bulk import from a folder", "Section 02's data in"],
                  ["Manage &rarr; Cases", "Create cases (a participant across several files); attach files or portions; case attributes", "A woman interviewed twice; a focus-group speaker"],
                  ["Manage &rarr; Attributes", "Define attributes for files and cases; import from CSV", "District, arm, language, interviewer"],
                  ["Coding &rarr; Code text / image / AV", "The coding workspace: file on the left, code tree on the right, memos and annotations", "Sections 03's work"],
                  ["Coding &rarr; Codebook", "Export the code tree with memos", "The appendix"],
                  ["Reports", "Coding reports by code, file, case, attribute; code frequencies; coder comparison; code relations; co-occurrence matrix; text mining", "Section 07 and 08"],
                  ["Action log; Journals", "The record of what was done; free-text journals", "The audit trail and the memos"]]},
             {"t": "body", "cls": "sm", "html": "The coding workspace does the day's work; the "
              "reports do the analysis; the journals hold the thinking. Set the coder "
              "name in settings before the first code: the comparison report depends on "
              "it."},
         ]},

        {"type": "content", "label": "Coding in QualCoder", "title": "Coding text: the moves you make a hundred times a day",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Open a file in Code text; select a passage; click a code (or right-click for the menu); the passage colours with the code's colour.",
                  "Create a code in place (right-click the tree); give it a memo (the definition) immediately.",
                  "Categories are folders in the tree; drag codes into them; a code can be in one category. Colours help; assign them by parent.",
                  "Annotations (a note on a passage without a code) and segment memos (a note on a coded segment) are both available; use annotations for 'come back to this' and memos for 'this is why'.",
                  "Overlapping codes show as overlapping colours; the segment list at the bottom shows every code on the selection.",
                  "Auto-code: by exact text, by sentence containing a phrase, or by speaker for structured transcripts. Use it to find, then read."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Indic text", "html":
                         "Devanagari, Bangla and Tamil display and select correctly; set the "
                         "font in settings to one with the script's coverage (Noto Sans "
                         "Devanagari, Noto Sans Bengali). Text search works on exact "
                         "strings; there is no stemming, so search for the root and the "
                         "common inflections separately. The parallel-translation workflow "
                         "(section 02, C) is done by opening the source-language file for "
                         "coding with the English file in a second window."},
                        {"t": "hbox", "color": "green", "html": "Backups: QualCoder can save "
                         "a timestamped copy of the project on every open; turn it on."}]},
         ]},

        {"type": "content", "label": "AV Coding", "title": "Coding audio and video: time-stamped segments",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Coding &rarr; Code audio/video opens the "
                        "file with a player; you mark a start and end time and attach a "
                        "code, exactly as with text, and the segment is the time span. A "
                        "transcript can be linked to the audio so that the two scroll "
                        "together, and coding either one codes both if the timestamps "
                        "line up. For focus groups, where who said what is half the "
                        "analysis, and for interviews where tone matters, this is the "
                        "feature that justifies leaving Taguette."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Transcripts with timestamps every minute (section 02) make the linking work; VaniScribe's output carries them.",
                           "Code the audio for delivery (hesitation, laughter, a change of voice when the husband enters) and the transcript for content; the two code sets join in the reports.",
                           "Video is heavy: compress to 720p, and keep the originals elsewhere."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "A qualitative study that "
                        "codes only the transcript has thrown away the recording's "
                        "information about how things were said. For most applied studies "
                        "that is an acceptable loss and should be a stated one."}]},
         ]},

        {"type": "content", "label": "Reports", "title": "QualCoder's reports: retrieval, counts and the coder comparison",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Report", "What it gives", "Section 07 or 08 equivalent"],
              "rows": [
                  ["Coding report", "Every segment for chosen codes, filtered by file, case or attribute value; exported to HTML, ODT, CSV", "Retrieval: 'SHIELD among Bengal members'"],
                  ["Code frequencies", "Counts of segments per code, by coder", "The code-summary table"],
                  ["Code relations", "Which codes overlap or are adjacent, with counts", "Co-occurrence"],
                  ["Co-occurrence matrix", "Code by code counts of overlapping segments", "The co-occurrence table"],
                  ["Case and attribute reports", "Codes by case; codes by attribute value", "The matrix of cases by codes"],
                  ["Coder comparison", "Agreement between two coders on selected codes and files: percentage agreement and Cohen's kappa", "Section 08"],
                  ["Text mining", "Word frequencies with a stop list", "Orientation only"],
                  ["Charts", "Bar and pie charts of code counts, hierarchy sunbursts", "Report figures, with care"]]},
             {"t": "body", "cls": "sm", "html": "Every report exports as a file. The coding "
              "report filtered by attribute is the one used most: it is how 'what did "
              "non-members in Bihar say about the bank' becomes a document to read and "
              "quote from."},
         ]},

        {"type": "content", "label": "REFI-QDA", "title": "REFI-QDA: moving a project between tools without losing the coding",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The REFI-QDA project exchange standard (2019, "
                        "from the Rotterdam Exchange Format Initiative) defines a .qdpx file "
                        "that carries sources, codes, coded segments, memos, cases and "
                        "attributes between tools. QualCoder, NVivo, MAXQDA, ATLAS.ti, "
                        "Dedoose, Quirkos and Transana read and write it. A student can code "
                        "in QualCoder and hand the project to a supervisor who uses NVivo; a "
                        "team can move from a commercial licence to a free tool when the "
                        "grant ends; an archive can accept the project in a documented "
                        "format."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Not everything transfers perfectly: tool-specific objects (maps, queries, some memo links) are dropped; check the import and keep the original.",
                           "Export a .qdpx at every milestone as the archival copy, alongside the tool's own project file.",
                           "The codebook alone can be exchanged as REFI-QDC (.qdc) for sharing definitions across projects."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The standard is the reason "
                        "the choice of tool matters less than it did. Choose for the work "
                        "and the budget; the coding is portable."}]},
         ]},

        {"type": "content", "label": "Worked QualCoder", "title": "The SHG study in QualCoder: 36 interviews, two languages, two coders",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "QualCoder", "Result"],
                        "rows": [
                            ["Import", "36 source-language transcripts and 36 English translations; 12 audio files linked; attributes from CSV (state, member, language, migrant husband, interviewer)", "Project of 72 files, 36 cases"],
                            ["Codebook", "Version 3 imported as a tree with memos", "46 codes in 9 categories"],
                            ["Coding", "Coder A (Hindi) and coder B (Bangla) on their language; each also codes four of the other's English translations for comparison", "Coded in three weeks"],
                            ["Agreement", "Coder comparison on the eight shared files, twelve key codes", "Kappa 0.61 to 0.84; SHIELD 0.58 before, 0.79 after redefinition"],
                            ["Retrieval", "Coding reports by attribute: SHIELD by state, by migrant husband", "SHIELD in 15/18 with migrant husbands, 7/18 without"],
                            ["Co-occurrence", "SHIELD &times; HUSBAND_DEMANDS matrix", "Overlap in 19 segments across 14 files"],
                            ["Memos", "Theme memos for SHIELD, STRATEGY, FEAR; a methods journal", "The findings' first drafts"],
                            ["Export", "Codebook, coding reports for the appendix, .qdpx for the archive", "Report and deposit"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative. The attribute "
                        "retrieval is the moment the study found its central pattern: the "
                        "group-as-shield theme was concentrated among women whose husbands "
                        "migrated, whose remittances arrived as lumps that relatives claimed. "
                        "The number (15 of 18) is a pointer, not a statistic; the fifteen "
                        "accounts are the finding."},
                        {"t": "hbox", "color": "amber", "html": "Everything in the table is "
                         "free software on two laptops. The commercial tools (next) would "
                         "have done it with more polish and no different conclusion."}]},
         ]},

        # ===================== SECTION 06: NVIVO, MAXQDA AND ATLAS.TI =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "NVivo, MAXQDA and ATLAS.ti"},

        {"type": "content", "label": "Side by Side", "title": "The commercial three: the same job, three designs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "NVivo", "MAXQDA", "ATLAS.ti"],
              "rows": [
                  ["Maker; since", "Lumivero (QSR International); 1999", "VERBI, Berlin; 1989 (as winMAX)", "ATLAS.ti GmbH, Berlin; 1993"],
                  ["Organising idea", "Files, codes and cases in a database; queries as the analytic engine", "Four windows: documents, codes, browser, retrieved segments; everything visible at once", "Quotations as first-class objects; codes, memos and networks link to them"],
                  ["Strengths", "Queries (matrix coding, coding comparison, crosstab); framework matrices; survey and social-media import; the most-taught", "Mixed methods (crosstabs, joint displays, typology tables); visual tools (MAXMaps); paraphrasing and summary grids; a built-in Stats module", "Networks; the query tool's operators (co-occurrence, proximity, embedding); PDF coding; the earliest and most developed AI features"],
                  ["Platforms", "Windows and Mac (features differ); Collaboration Cloud", "Windows and Mac; TeamCloud", "Windows and Mac; a full Web version"],
                  ["Transcription", "NVivo Transcription (paid, per hour); English-centred", "Via partner services; a transcription mode with foot-pedal support", "Via the Web version and partners"],
                  ["AI", "AI Assistant: summaries, code suggestions", "AI Assist: summaries, suggested codes, chat with data", "Intentional AI coding, AI summaries, conversational AI"],
                  ["Learning curve", "Steeper; many objects and windows", "Gentlest of the three", "Middle; the quotation model takes a day to click"],
                  ["Typical licence", "Student around US$100 a year; institutional site licences common in India", "Similar; educational licences; a free Reader", "Similar; Web by subscription"]]},
             {"t": "body", "cls": "sm", "html": "Prices and features change yearly; verify "
              "with the vendor. The differences that matter for a project are the "
              "organising idea (which shapes how you think), the query engine (section "
              "07), and which one your team and supervisor already use."},
         ]},

        {"type": "content", "label": "NVivo", "title": "NVivo: files, codes, cases and the query menu",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Data: Files (transcripts, PDFs, audio, video, "
                        "pictures, datasets from surveys, web captures via NCapture) in "
                        "folders. Codes in a tree, with Sentiment and Relationship codes as "
                        "special kinds. Cases (a participant, a site) with classifications "
                        "and attributes. Notes: memos and annotations. Queries: text search, "
                        "word frequency, coding, matrix coding (codes by codes or by "
                        "attributes), coding comparison (agreement between users), compound, "
                        "crosstab. Explore: maps, charts, hierarchy charts, framework "
                        "matrices. Everything is a saved object that can be rerun."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Auto-coding by paragraph style and by speaker is strong; a transcript with consistent speaker labels codes itself into speaker cases in seconds.",
                           "Framework matrices (cases by themes, with summaries typed into cells) are the framework method built in.",
                           "The coding comparison query gives kappa per code per file, which is section 08's table."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Cautions", "html":
                         "The Mac version has lagged the Windows version in features for "
                         "years; check before buying. Project files grow large with media "
                         "and corrupt occasionally; the backup habit is not optional. The "
                         "sentiment auto-coding is trained on English and should not be "
                         "used on Indian-language or translated text as evidence. The "
                         "word-frequency query's 'stemmed words' and 'synonyms' options "
                         "are English-only."},
                        {"t": "hbox", "color": "green", "html": "NVivo is the tool most Indian "
                         "universities license and teach. If the institution has it, learn "
                         "it; the ideas transfer."}]},
         ]},

        {"type": "content", "label": "MAXQDA", "title": "MAXQDA: four windows and the mixed-methods menu",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The screen is four panes: the Document System "
                        "(files in groups, with variables), the Code System (the tree, with "
                        "colours and frequencies), the Document Browser (the file being "
                        "coded, with coding stripes in the margin), and Retrieved Segments "
                        "(every segment for the activated codes in the activated documents). "
                        "'Activation' is the central move: activate documents and codes and "
                        "the retrieval updates. Memos attach to anything and show as icons "
                        "in the margin. The Analysis menu holds the Code Matrix Browser, the "
                        "Code Relations Browser, the Summary Grid and paraphrasing; the "
                        "Mixed Methods menu holds crosstabs, joint displays and typology "
                        "tables; MAXMaps draws concept maps from the project's objects."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Document variables are attributes and can be imported from a spreadsheet and exported to one, which is the bridge to section 09.",
                           "The Summary Grid (a summary per document per code, written by you) is the framework method's charting step.",
                           "MAXDictio adds word frequency and dictionary-based content analysis; the Stats module runs descriptive and inferential statistics on variables without leaving the program."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "MAXQDA's gentleness is the "
                        "reason many methods teachers prefer it: a student sees the "
                        "documents, the codes and the retrieved evidence at once, and the "
                        "idea of coding as retrieval is on the screen."}]},
         ]},

        {"type": "content", "label": "ATLAS.ti", "title": "ATLAS.ti: quotations, networks and the query tool",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "In ATLAS.ti a selected passage becomes a "
                        "quotation, an object with an ID that exists whether or not it is "
                        "coded, can carry a comment, and can be linked to other quotations "
                        "(supports, contradicts, explains). Codes attach to quotations; "
                        "code groups and document groups organise them; memos are "
                        "documents in their own right. Networks draw the links between "
                        "codes, quotations and memos as a graph. The query tool combines "
                        "codes with Boolean, semantic (within a hierarchy) and proximity "
                        "operators (co-occurs, follows, within), which is the most "
                        "expressive retrieval language of the three."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The quotation model suits work where the passages themselves are analysed and linked (discourse, narrative), less so where codes are counted.",
                           "Co-occurrence table, code-document table and Sankey diagrams are one click each.",
                           "The Web version runs in a browser with most desktop features and is the easiest route for a distributed team."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "ATLAS.ti was first to build "
                        "AI coding into the product (2023) and its 'Intentional AI coding' "
                        "codes a document from a stated intent. Section 11 is about "
                        "whether to use it and what to disclose."}]},
         ]},

        {"type": "content", "label": "Which One", "title": "Choosing among the three: a decision table",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["If", "Lean toward", "Because"],
              "rows": [
                  ["Your institution licenses one", "That one", "Support, training, and a supervisor who can open your project"],
                  ["Your team is on Mac", "MAXQDA or ATLAS.ti", "Feature parity across platforms"],
                  ["The study is mixed methods with a survey", "MAXQDA", "Variables, crosstabs, joint displays and the Stats module in one place"],
                  ["The study is framework analysis for a policy client", "NVivo (framework matrices) or MAXQDA (Summary Grid)", "The charting step is built in"],
                  ["The analysis links passages to each other and draws conceptual maps", "ATLAS.ti", "Quotations and networks"],
                  ["Large document corpora, PDFs, policy texts", "ATLAS.ti or MAXQDA", "PDF handling and document-level coding"],
                  ["A distributed team with no server", "ATLAS.ti Web, or MAXQDA TeamCloud, or NVivo Collaboration Cloud", "Simultaneous access; check data-residency terms"],
                  ["No budget", "QualCoder, or Taguette", "Sections 04 and 05; the coding is the same"],
                  ["A thesis to be examined", "Whatever the examiners can open", "REFI-QDA export covers the rest"]]},
             {"t": "body", "cls": "sm", "html": "None of the three will make a weak analysis "
              "strong or a strong one weak. The advice for a first project is the tool "
              "closest to hand; for a team, the one the team agrees on; for a career, "
              "learn two."},
         ]},

        {"type": "content", "label": "Licensing", "title": "Licences, trials and what to check before paying",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "All three offer 14- to 30-day free trials with full features; time a trial to a coding sprint, not to an idle month.",
                  "Student licences require proof of enrolment and expire; a thesis that runs a year past the licence needs a plan (export to REFI-QDA and continue in QualCoder is one).",
                  "Institutional site licences at Indian universities often cover NVivo; ask the library before buying anything.",
                  "Subscription versus perpetual: the vendors have moved to subscriptions; a perpetual licence, where offered, is worth it for a multi-year programme.",
                  "Cloud and web versions store project data on the vendor's servers, usually outside India; check the consent form and the institution's data policy, and the vendor's data-processing terms, before uploading transcripts.",
                  "Free readers (MAXQDA Reader; NVivo's read-only export) let a supervisor or examiner open a project without a licence."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The question to ask a vendor "
                        "in writing: where is my data stored, who can access it, is it used "
                        "to train models, and how do I delete it. The answers decide whether "
                        "the cloud version is usable for interview data at all."}]},
         ]},

        {"type": "content", "label": "Transcription Tools", "title": "Transcription inside and outside the tools, for Indian languages",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Route", "Languages", "Cost", "Notes"],
              "rows": [
                  ["NVivo Transcription", "English-centred; some other languages; weak on Indian languages", "Per audio hour, paid", "Convenient for English interviews; not the route for Hindi or Bangla"],
                  ["VaniScribe (ImpactMojo)", "Hindi, Tamil, Bangla, Marathi, Telugu and others via Sarvam's models; native script or transliteration", "A few rupees a minute with your own key", "Built for this course's readers; output has timestamps and speaker turns"],
                  ["Bodhan AI Indic-Transcribe (open weights)", "The scheduled languages", "Free to run locally; hosted API by the minute", "Data stays on the machine if run locally; needs a capable computer or a notebook"],
                  ["Whisper and its Indic fine-tunes", "Hindi and major languages, variable quality on others", "Free locally", "Hallucinates in silence; check every transcript"],
                  ["Human transcription (in-house or agency)", "Any", "Rs 300&ndash;1,500 per audio hour depending on level and language", "Still the standard for full verbatim and for dialects; quality varies with the agency"],
                  ["Interviewer's own transcription", "Any", "Their time: 4&ndash;8 hours per hour", "Slow, and the best first analysis there is"]]},
             {"t": "body", "cls": "sm", "html": "The workflow most South Asian teams now use: "
              "machine transcription in the source language, a native-speaker checking "
              "pass against the audio, then import. Whatever the route, the transcript is "
              "the coder's data and the audio is the truth; keep both."},
         ]},

        {"type": "content", "label": "Migration", "title": "Moving between tools, and what to check after",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "EXPORT a REFI-QDA .qdpx from the source tool at a clean milestone",
                  "IMPORT into the destination; open a coded file and check the segments match",
                  "COUNT: code frequencies before and after must agree",
                  "CHECK memos, attributes, cases; note what was dropped",
                  "RE-LINK media if audio and transcripts were separated",
                  "ARCHIVE both project files with the date and the versions used"]},
                       {"t": "body", "html": "The exchange works well for text coding, "
                        "codes, memos and attributes, and less well for tool-specific "
                        "objects. A count of segments per code before and after is the "
                        "test; a mismatch of more than a handful means something was lost "
                        "and the original is the record."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Migrate at a milestone, "
                        "never mid-coding. Two coders on two tools with one exchange "
                        "between them is a workable team; two coders swapping the project "
                        "back and forth weekly is not."}]},
         ]},

        # ===================== SECTION 07: QUERIES, MATRICES AND VISUALS =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Queries, Matrices and Visuals"},

        {"type": "content", "label": "Retrieval", "title": "Retrieval is the analysis: reading what was coded, together",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The point of coding is to be able to read "
                        "every passage about one thing at once, across all the interviews, "
                        "and to notice what they share and where they differ. A coding "
                        "report or retrieval (all segments for SHIELD) is the primary "
                        "analytic object: read it as a document, annotate it, write the "
                        "memo from it. Filtering it by attribute (SHIELD among Bengal "
                        "members) is the comparison; reading the two filtered retrievals "
                        "side by side is the finding's evidence."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Retrieve with context: a segment with the question before it and a sentence after. Every tool has a context setting; use it.",
                           "Read the whole retrieval before counting anything. The exceptions are usually more informative than the pattern.",
                           "Export the retrieval and write in its margins; the writing is the second-cycle coding.",
                           "A retrieval that is too long to read (300 segments) is a code that needs splitting."]}],
              "right": [{"t": "panel", "color": "amber", "title": "In each tool", "html":
                         "NVivo: open a code, or a Coding query with attribute criteria. "
                         "MAXQDA: activate documents and codes; Retrieved Segments updates; "
                         "activate by variable for the attribute filter. ATLAS.ti: the "
                         "quotation manager filtered by code and document group; or the "
                         "query tool. QualCoder: Reports &rarr; Coding report with file, "
                         "case or attribute filters. Taguette: click the tag; filter by "
                         "hand in the export."},
                        {"t": "hbox", "color": "green", "html": "The first hour of analysis "
                         "is reading one retrieval. Everything below is a way of choosing "
                         "which retrieval to read next."}]},
         ]},

        {"type": "content", "label": "Matrices", "title": "The matrix: codes by attributes, and what its cells mean",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Code", "Bihar member (n = 12)", "Bihar non-member (7)", "Bengal member (12)", "Bengal non-member (5)"],
                        "rows": [
                            ["SAVINGS_SHIELD", "10 files, 24 seg.", "1, 1", "8, 14", "0, 0"],
                            ["SAVINGS_BARRIER", "9, 17", "7, 22", "10, 19", "5, 9"],
                            ["DECISION_STRATEGY", "9, 21", "3, 5", "10, 24", "2, 3"],
                            ["FEAR_FORMAL_FINANCE", "4, 6", "6, 13", "5, 8", "5, 11"],
                            ["HUSBAND_DEMANDS", "11, 26", "6, 12", "9, 18", "4, 8"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. NVivo's matrix "
                        "coding query (codes by attribute values), MAXQDA's crosstab, "
                        "ATLAS.ti's code-document table by document group, QualCoder's "
                        "attribute report. Each cell: number of files containing the code, "
                        "and number of segments."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading the cells", "html":
                         "Files matter more than segments: 10 of 12 Bihar members raised "
                         "SHIELD; one of seven non-members did. That is a pattern worth a "
                         "theme. Segment counts say how much a respondent talked, which "
                         "reflects the interviewer and the respondent's style as much as "
                         "the topic. FEAR is more common among non-members in both states, "
                         "which is a second pattern. The cells are pointers into "
                         "retrievals; the finding is in what the retrievals say."},
                        {"t": "hbox", "color": "amber", "html": "Never report a matrix cell as "
                         "a proportion of a population. The sample was purposive; the "
                         "numbers describe the sample and locate the evidence."}]},
         ]},

        {"type": "content", "label": "Co-occurrence", "title": "Co-occurrence and proximity: what is said together",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A co-occurrence table counts the segments (or "
                        "files) where two codes overlap. SHIELD &times; HUSBAND_DEMANDS "
                        "co-occur in 19 segments across 14 files: women describe the shield "
                        "in the same breath as the demands it shields against. Reading those "
                        "19 segments is how the theme's mechanism is stated. Proximity "
                        "queries (ATLAS.ti's 'follows', NVivo's 'near') find codes within a "
                        "set distance, which catches cause-and-effect talk where the two "
                        "ideas are in adjacent sentences."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Co-occurrence depends on segment size (section 03): long segments co-occur with everything. Consistency makes the table meaningful.",
                           "A code that co-occurs with nothing is either a topic on its own or a code nobody used precisely.",
                           "Heat-map versions (MAXQDA's Code Relations Browser, ATLAS.ti's co-occurrence table with coefficients) show the structure of the codebook at a glance and are useful for revising it.",
                           "The co-occurrence coefficient (ATLAS.ti's c-coefficient) is a normalised count, not a correlation; treat it as a ranking."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "Co-occurrence is the closest "
                        "QDA software comes to finding something for you. It finds where "
                        "to look. What is there is still yours to read."}]},
         ]},

        {"type": "content", "label": "Text Queries", "title": "Word frequency, text search and their limits in Indian languages",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Word-frequency queries list the most common "
                        "words; text search finds every passage with a term and can code "
                        "them. Both are built for English: stemming, stop words and "
                        "synonyms are English lists, and Hindi's postpositions, Bangla's "
                        "inflections and Tamil's agglutination defeat them. A word "
                        "frequency on a Hindi corpus returns <em>hai</em>, <em>ka</em>, "
                        "<em>ki</em>, <em>ko</em>, <em>mein</em> and tells you nothing. On "
                        "the English translations it tells you about the translator's "
                        "vocabulary."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Use text search to find passages by a known term and its variants (<em>samooh</em>, <em>samuh</em>, group, SHG, <em>dal</em>), then read and code by hand.",
                           "Build a project stop-word list for the language; NVivo and MAXQDA allow custom lists.",
                           "Word clouds are decoration. A frequency table of a few chosen terms by group can be evidence of emphasis; say what it is.",
                           "For real text mining of Indian-language corpora, the tools are outside QDA software (Python with Indic NLP libraries), and the question is usually different."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The commonest misuse: a "
                        "word cloud on the title slide of a presentation about 36 "
                        "interviews. It is not analysis and the audience knows."}]},
         ]},

        {"type": "content", "label": "Framework Matrix", "title": "The framework matrix: charting cases by themes",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Case", "Savings purpose", "Shield", "Decision strategy", "Formal finance"],
                        "rows": [
                            ["BR_003 (member, migrant husband)", "School fees; a buffalo", "Strong: 'the money is the group's until I take it'; husband's family cannot ask", "Times requests for when remittance arrives; group president as ally", "Never entered the bank; group leader deposits"],
                            ["BR_007 (member, husband present)", "Emergencies", "Weak: husband knows the schedule and asks", "Concedes small, holds large", "Fear of forms; went once with the group"],
                            ["BR_011 (non-member)", "'Nothing to save'", "&mdash;", "None described; husband decides", "Distrust from a relative's experience"],
                            ["WB_015 (member, migrant husband)", "Daughter's marriage; a phone", "Strong; explicit comparison with pre-membership", "Uses group meeting days as cover for market visits", "Has an account; uses it with the group"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, four of 36 rows. "
                        "Cells are the analyst's summaries of what that case said under that "
                        "theme, with a phrase quoted, written from the retrievals. NVivo's "
                        "framework matrix and MAXQDA's Summary Grid hold it inside the "
                        "project, linked to the segments; a spreadsheet does it outside."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Why it works", "html":
                         "Reading down a column shows the range of a theme across cases; "
                         "reading across a row shows one woman's account as a whole; "
                         "sorting rows by an attribute (migrant husband) shows whether the "
                         "column changes with it. Gale and colleagues (2013) built the "
                         "method for applied health research with teams and deadlines, "
                         "and it is the most transparent qualitative analysis a policy "
                         "reader can be shown."},
                        {"t": "hbox", "color": "amber", "html": "Charting 36 cases by eight "
                         "themes is about three days. It is the analysis, not preparation "
                         "for it."}]},
         ]},

        {"type": "content", "label": "Visuals", "title": "Visuals that earn their place, and those that do not",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Visual", "Tool", "Use when", "Avoid when"],
              "rows": [
                  ["Code tree (the codebook as a diagram)", "All", "Showing the structure of the analysis in the methods", "It is decoration for a list that reads better as a table"],
                  ["Matrix heat map (codes by attributes)", "NVivo, MAXQDA, ATLAS.ti", "Showing where a theme concentrates, as a pointer", "The reader will read cell shading as proportions of a population"],
                  ["Co-occurrence network", "ATLAS.ti networks; MAXMaps; NVivo maps", "Showing how themes relate, with the links labelled and argued", "It is a hairball of every code linked to every other"],
                  ["Concept map from memos", "MAXMaps, ATLAS.ti networks", "The theory of change that emerged; a figure for the discussion", "It restates the code tree"],
                  ["Comparison diagram (two cases)", "NVivo", "Showing what two contrasting cases share and do not", "Rarely; it is a two-row framework matrix"],
                  ["Hierarchy chart, sunburst", "NVivo, QualCoder", "Showing coverage of codes as a diagnostic during coding", "In a report; it is a pie chart of segment counts"],
                  ["Word cloud", "All", "Never in a report", "Always"],
                  ["Joint display (qual and quant side by side)", "MAXQDA; by hand", "Mixed methods, section 09", "&mdash;"]]},
             {"t": "body", "cls": "sm", "html": "The best qualitative figure in most reports "
              "is a table of quotations by theme and case, or a framework matrix. A "
              "diagram is justified when the relationships between themes are the finding "
              "and the diagram is drawn from an argument, not from the software's "
              "auto-layout."},
         ]},

        {"type": "content", "label": "From Query to Claim", "title": "From a query to a claim: the chain of evidence",
         "blocks": [
             {"t": "flow", "steps": [
                 "PATTERN noticed in a memo or a matrix cell",
                 "RETRIEVAL read in full, with context; exceptions listed",
                 "COMPARISON across attributes; the counterexamples explained or admitted",
                 "CLAIM written as a sentence with its scope ('among members with migrant husbands')",
                 "EVIDENCE: three quotations that show the range, not three that agree",
                 "CHECK: a search for disconfirming cases; a second reader"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The software makes the first three steps "
                        "fast and leaves the last three where they were. A claim that "
                        "arrived by this chain can be traced back through the project: "
                        "the memo, the query, the retrieval, the segments. That "
                        "traceability is what section 10 means by an audit trail, and the "
                        "project file is it."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Illustrative claim: 'Among "
                        "members whose husbands migrate, group savings were described as a "
                        "protected fund that relatives could not claim; three of the "
                        "eighteen described the opposite, a husband who demanded the "
                        "group's money, and all three were in groups without a written "
                        "withdrawal rule.' Scope, pattern, exceptions, and a mechanism to "
                        "check."}]},
         ]},

        {"type": "content", "label": "Query Checklist", "title": "Queries and matrices: the checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Practice", "Done"],
              "rows": [
                  ["Every retrieval read in full before any count is reported", ""],
                  ["Matrices report files (cases) first, segments second, and the sample size per column", ""],
                  ["No matrix cell presented as a population proportion", ""],
                  ["Co-occurrence read as a pointer; the overlapping segments read", ""],
                  ["Text search and word frequency used to find, not to code or to conclude", ""],
                  ["Framework matrix or equivalent charted for the main themes", ""],
                  ["Every claim traceable: memo, query, retrieval, segments", ""],
                  ["Disconfirming cases searched for and reported", ""],
                  ["Visuals limited to those that carry an argument", ""]]},
             {"t": "body", "cls": "sm", "html": "Nine rows. The third is the one a "
              "quantitative reader will test you on, and the seventh is the one a "
              "qualitative reviewer will."},
         ]},

        # ===================== SECTION 08: CODING IN TEAMS =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Coding in Teams"},

        {"type": "content", "label": "Why Teams", "title": "Team coding: for capacity, for languages, and for challenge",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Thirty-six interviews in two languages are "
                        "more than one person can code in the time an evaluation allows, "
                        "and more languages than one person usually reads. A team also "
                        "brings a second reading: the field researcher who heard the "
                        "interview, the analyst who did not, the supervisor who knows the "
                        "literature. The software's job is to let them code separately and "
                        "bring the work together; the method's job is to decide what "
                        "'together' means."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "One codebook, owned by one person, versioned; every coder works from the current version.",
                           "Coding meetings weekly: new inductive codes proposed and decided; definitions revised; disagreements discussed on the segments.",
                           "Each coder's work identified (coder name in the software) so that comparison and attribution are possible.",
                           "A merging protocol (next slides) agreed before anyone codes."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The field researcher as coder", "html":
                         "The person who did the interview codes it best and worst: best "
                         "because they heard the tone and know the context, worst because "
                         "they know what they meant to ask. A common arrangement: the "
                         "interviewer codes their own interviews first cycle, a second "
                         "person codes a sample, and the analyst does second-cycle "
                         "grouping across all. The interviewer's memos are data of their "
                         "own."},
                        {"t": "hbox", "color": "green", "html": "Budget the coding meetings. "
                         "An hour a week for the coding period, with the segments on the "
                         "screen."}]},
         ]},

        {"type": "content", "label": "Agreement", "title": "Inter-coder agreement: when to measure it, and what the number means",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Two coders code the same transcripts "
                        "independently with the same codebook; the software compares "
                        "segment by segment and reports agreement, usually as percentage "
                        "agreement and Cohen's kappa (chance-corrected) per code, sometimes "
                        "Krippendorff's alpha. Kappa above 0.8 is conventionally 'strong', "
                        "0.6 to 0.8 'moderate to substantial'. O'Connor and Joffe "
                        "(<em>International Journal of Qualitative Methods</em> 2020, 19) "
                        "review the debate and give practical guidance; Campbell and "
                        "colleagues (<em>Sociological Methods &amp; Research</em> 2013, "
                        "42:294) show how much segment boundaries ('unitisation') drive the "
                        "number."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Measure it when the method is codebook-based (content analysis, framework, template analysis) and the codes are meant to be applied consistently. Report it per code, not as one average.",
                           "Do not measure it for reflexive thematic analysis, where codes are the researcher's interpretation and agreement is not the goal (Braun and Clarke are explicit); describe the collaborative process instead.",
                           "Low kappa on a code is a finding about the definition, and the fix is in the codebook, then a recode of the shared sample.",
                           "Agreement on a sample of files (10&ndash;20%) is standard; agreement on everything is a different design."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "'Inter-coder reliability was "
                        "established (&kappa; = 0.82)' as one number for forty codes is not "
                        "informative. Per code, with the range, and what was done about "
                        "the low ones, is."}]},
         ]},

        {"type": "content", "label": "Worked Agreement", "title": "A worked agreement table, and what changed after it",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Code", "% agreement", "&kappa; round 1", "Action", "&kappa; round 2"],
                        "rows": [
                            ["SAVINGS_PURPOSE", "94", "0.84", "None", "&mdash;"],
                            ["SAVINGS_SHIELD", "86", "0.58", "Redefined: requires explicit reference to the money being inaccessible to others; added two examples and a do-not-use", "0.79"],
                            ["SAVINGS_BARRIER", "91", "0.76", "None", "&mdash;"],
                            ["DECISION_STRATEGY", "83", "0.52", "Split into STRATEGY_TIMING, STRATEGY_ALLY, STRATEGY_WITHHOLD", "0.71, 0.77, 0.74"],
                            ["FEAR_FORMAL_FINANCE", "92", "0.74", "Boundary with BANK_MISTREATMENT clarified", "0.81"],
                            ["HUSBAND_DEMANDS", "90", "0.71", "None", "&mdash;"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative; eight shared files, "
                        "two coders, QualCoder's coder comparison (NVivo's coding comparison "
                        "query and MAXQDA's intercoder agreement give the same table). "
                        "Round 2 was on four new shared files after the codebook revision."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the table did", "html":
                         "Two codes were unclear and became clearer, one by redefinition "
                         "and one by splitting; the splitting turned out to be analytically "
                         "useful, because STRATEGY_WITHHOLD became part of the shield theme. "
                         "The table goes in the appendix with the two codebook versions. "
                         "Percentage agreement is high everywhere because most text is "
                         "uncoded and both coders agree it is; kappa corrects for that."},
                        {"t": "hbox", "color": "amber", "html": "Agreement measured once at "
                         "the start and never again is a ritual. Measured at the start, "
                         "acted on, and re-measured, it is a method."}]},
         ]},

        {"type": "content", "label": "Merging", "title": "Merging coders' work: the three arrangements",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Arrangement", "How", "Tools", "Risks"],
              "rows": [
                  ["Divide the files", "Each coder codes different files in a copy of the master; the master imports each copy (NVivo import project; MAXQDA merge; ATLAS.ti merge; QualCoder import coding)", "All four", "Codebook drift between coders; new codes created in two places under different names; merge conflicts on files coded twice"],
                  ["Simultaneous on a shared project", "A server or cloud project everyone opens (NVivo Collaboration Cloud, MAXQDA TeamCloud, ATLAS.ti Web, hosted Taguette)", "Cloud versions; Taguette", "Data residency and consent; subscription cost; connectivity"],
                  ["Sequential", "One project file passed from coder to coder with a lock (only one person edits at a time)", "Any", "Slow; someone always has it; the lock is broken by email"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "The first is the usual "
                        "arrangement for desktop tools. Its risk is managed by the codebook "
                        "owner: coders may not create codes, only propose them in a memo; "
                        "the owner adds them to the master; coders reimport the codebook "
                        "weekly. Merging then goes cleanly, and the coder comparison "
                        "reports work because the same codes have the same identities."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Test the merge with two "
                        "small copies before the real one. A failed merge of three weeks' "
                        "coding is recoverable only from the copies, so keep them."}]},
         ]},

        {"type": "content", "label": "Across Languages", "title": "Teams across languages: keeping one analysis from two corpora",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The Hindi coder and the Bangla coder each "
                        "code their own language with a shared, bilingual codebook whose "
                        "definitions carry the source-language terms that anchor each code. "
                        "Agreement is checked on the English translations of a shared "
                        "sample, which measures whether the codebook travels, not whether "
                        "the two coders read Hindi and Bangla the same way. Theme memos are "
                        "written in English with quotations in both languages. The "
                        "analyst reads across both coders' retrievals."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Weekly meetings compare how a code looks in each language; a code that means something different in Bangla is a finding, and may need splitting by language.",
                           "The in vivo parent holds each language's key terms; the report glosses them.",
                           "Where a supervisor reads only English, the translation workflow (section 02, C) with the source visible lets the coder show them the original when a quotation is disputed."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "A theme found only in one "
                        "language's corpus is either a real difference between the states "
                        "or an artefact of the coder. Section 10's reflexivity statement "
                        "says which you think, and why."}]},
         ]},

        {"type": "content", "label": "Versioning", "title": "Versions, backups and the project log",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["What", "When", "How"],
              "rows": [
                  ["Project file backup", "Daily during coding; automatic where the tool offers it", "A dated copy on a second drive or institutional storage; not only the laptop"],
                  ["Milestone version", "After the codebook revision; after the merge; before second-cycle coding; at submission", "Save-as with a date; keep them all"],
                  ["Codebook version", "At every revision", "Export the codebook with date and a change note; keep the sequence for the appendix"],
                  ["REFI-QDA export", "At milestones", "The tool-independent archive"],
                  ["Project log", "Continuous", "A dated memo of decisions: what changed, why, who decided; NVivo's event log and QualCoder's action log supplement it"],
                  ["Coder copies", "Until the merge is verified", "Each coder's project before merging, kept"]]},
             {"t": "body", "cls": "sm", "html": "A qualitative project with a log, versioned "
              "codebooks and milestone files can be audited by an examiner in an "
              "afternoon; one with a single project file cannot be audited at all. The "
              "difference is habit, not software."},
         ]},

        {"type": "content", "label": "Team Checklist", "title": "Coding in teams: the checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Practice", "Done"],
              "rows": [
                  ["One codebook owner; coders propose, owner decides", ""],
                  ["Coder names set in the software before coding", ""],
                  ["Merging arrangement agreed and tested before coding starts", ""],
                  ["Shared sample (10&ndash;20% of files) coded independently by two coders", ""],
                  ["Agreement computed per code, acted on, and re-measured; reported in the appendix", ""],
                  ["Weekly coding meeting with segments on screen; decisions logged", ""],
                  ["Bilingual codebook with source-language anchors where languages differ", ""],
                  ["Backups daily; milestone versions kept; coder copies kept until the merge is verified", ""],
                  ["Cloud use consistent with consent and data policy", ""]]},
             {"t": "body", "cls": "sm", "html": "Nine rows, and the one that fails most often "
              "is the third: teams merge for the first time on the day it matters."},
         ]},

        # ===================== SECTION 09: MIXED METHODS =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Mixed Methods"},

        {"type": "content", "label": "Integration", "title": "Integration: where the qualitative and the survey meet",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Most development evaluations collect both a "
                        "survey and interviews and report them in separate chapters that "
                        "never touch. Integration is the work of making them answer each "
                        "other: the survey says the programme raised decision-making by "
                        "0.9 points; the interviews say how, for whom, and what 0.9 points "
                        "means in a household. Fetters, Curry and Creswell (<em>Health "
                        "Services Research</em> 2013, 48:2134) set out the ways: at the "
                        "design (one strand informs the other's sampling or instrument), "
                        "the methods (connecting, building, merging), and the "
                        "interpretation (joint displays, narrative weaving)."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Connecting: interviewees sampled from the survey, so attributes are survey variables and the qualitative cases sit inside the quantitative sample.",
                           "Building: interview findings become survey items in the next round (the shield theme becomes a question about who can access group savings).",
                           "Merging: the two sets of results brought together in a joint display and interpreted as one."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The software's contribution "
                        "is attributes. If the 36 interviewees are also survey respondents "
                        "with their survey values as attributes, every matrix in section "
                        "07 is a mixed-methods table."}]},
         ]},

        {"type": "content", "label": "Joint Displays", "title": "The joint display: one table, both kinds of evidence",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Survey result (n = 640)", "Qualitative finding (36 interviews)", "Integrated reading"],
                        "rows": [
                            ["Members score 0.9 points higher on decision-making (95% CI 0.4 to 1.3)", "Members describe group savings as a protected fund; decisions over large purchases are timed to its availability", "The effect is concentrated in large-purchase decisions and works through control over a lump sum"],
                            ["Effect larger where husband is a migrant (interaction, p = .03)", "SHIELD theme present in 15 of 18 migrant-husband cases, 7 of 18 others; remittance lumps attract relatives' claims, the group's fund does not", "The mechanism is protection from claims, which matters most where lump sums arrive"],
                            ["No effect on 'own income' (2 points, CI &minus;4 to 8)", "Few members describe new income; several describe the group as changing control, not earnings", "The programme changes control over money more than the amount; the survey's income item was the wrong outcome for the mechanism"],
                            ["Non-members report higher fear of banks (62% vs 41%)", "Non-members' fear draws on relatives' stories; members' fear is reduced by going 'with the group'", "Exposure through the group reduces avoidance; a bank-linkage component would build on it"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative. Guetterman, Fetters "
                        "and Creswell (<em>Annals of Family Medicine</em> 2015, 13:554) "
                        "describe the joint display; MAXQDA's Mixed Methods menu builds "
                        "several kinds from variables and codes; the rest of the tools "
                        "leave it to a table in Word, which is fine. The third column is "
                        "the integration and it is the paragraph a policy reader "
                        "remembers."},
                        {"t": "hbox", "color": "amber", "html": "The third row is the useful "
                         "kind: the strands disagree, and the disagreement explains the "
                         "survey's null."}]},
         ]},

        {"type": "content", "label": "Open-Ended Items", "title": "Survey open-ends: coding hundreds of short answers",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A survey's 'why did you stop attending?' with "
                        "480 free-text answers is qualitative data at scale. Import the "
                        "spreadsheet as a dataset (NVivo), a survey import (MAXQDA), a "
                        "document table (ATLAS.ti) or a survey (QualCoder's Project &rarr; "
                        "Import survey), so each respondent is a case with attributes and "
                        "each answer a codeable cell. Auto-code by question; then code the "
                        "answers with a short codebook (ten to fifteen codes); then export "
                        "codes by case as a binary matrix back to the survey file."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Answers are short; segments are whole answers; multiple codes per answer are normal.",
                           "Here counts are legitimate results: the sample is the survey's sample, and '31% cited distance' is a proportion with a denominator. Report it with the n and the multiple-response note.",
                           "Two coders on a 10% sample with kappa, as in section 08; short answers code fast and disagree often.",
                           "The exported code matrix (case &times; code, 0/1) joins the survey data by ID and becomes variables for the quantitative analysis: 'cited distance' as a predictor of re-enrolment."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "Sandelowski, Voils and Knafl "
                        "(<em>Journal of Mixed Methods Research</em> 2009, 3:208) on "
                        "'quantitizing': what it is legitimate to count and what the count "
                        "then means. Open-ends are the clearest case where it is."}]},
         ]},

        {"type": "content", "label": "Sampling", "title": "Sampling interviewees from the survey: attributes by design",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "When the qualitative sample is drawn from the "
                        "survey (a nested or connected design), the interviewee's survey "
                        "record is the attribute sheet: her arm, her baseline and endline "
                        "scores, her household characteristics. Purposive selection can then "
                        "be principled: maximum variation on the outcome (high gainers, no "
                        "change, decliners), extreme cases, or stratified by the moderator "
                        "the survey found (migrant husband). The interviews then explain "
                        "the survey's numbers with the numbers attached."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Import the survey extract as the attribute file; the join key is the participant ID, which consent must have allowed to be linked.",
                           "A matrix of themes by outcome group (gainers, no change, decliners) is the mixed-methods analysis of mechanism.",
                           "Deviant cases (a member who declined) are selected on purpose and are the most informative interviews in the study."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Illustrative", "html":
                         "Twelve members who gained more than 2 points, twelve who did not "
                         "change, twelve non-members, balanced across states and "
                         "migrant-husband status. The SHIELD theme appears in eleven of the "
                         "twelve gainers and four of the twelve no-change members; the four "
                         "were in groups without a withdrawal rule. That is a mechanism "
                         "hypothesis the survey could not have produced and the next survey "
                         "can test."},
                        {"t": "hbox", "color": "green", "html": "The interview guide changes "
                         "when the survey results are known. Sequential designs plan for "
                         "that; parallel ones cannot."}]},
         ]},

        {"type": "content", "label": "Quantitising", "title": "Counting qualitative codes: when it is evidence and when it is not",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Count", "Legitimate?", "Because"],
              "rows": [
                  ["'31% of 480 survey respondents cited distance'", "Yes, as a proportion", "The sample is the survey's; every respondent answered the question; the denominator is known"],
                  ["'15 of 18 interviewees with migrant husbands described a shield'", "Yes, as a description of the purposive sample and a pointer", "The denominator is the interview sample, which was chosen, not drawn"],
                  ["'42% of women in the district feel the group protects their savings'", "No", "A purposive sample of 36 cannot support a population proportion"],
                  ["'The theme of fear was mentioned 94 times'", "Rarely", "Segment counts reflect talkativeness and segment size; say files, not segments, if anything"],
                  ["'Members were more likely than non-members to mention X (p = .04, Fisher's exact on 36)'", "Not as a test", "The interviews were not a random sample and the codes were not pre-specified as outcomes; report the pattern and its scope"],
                  ["'Coded open-ends as variables, then regressed re-enrolment on them (n = 480)'", "Yes", "Quantitised survey data with a defined sample and pre-specified codes"]]},
             {"t": "body", "cls": "sm", "html": "The rule is the denominator. Where the "
              "denominator is a defined sample that answered a defined question, a count "
              "is a statistic. Where it is a purposive set of conversations, a count "
              "locates evidence and describes the set, and the sentence should make that "
              "plain."},
         ]},

        {"type": "content", "label": "Mixed Tools", "title": "The tools for mixed methods: what each does natively",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Need", "MAXQDA", "NVivo", "ATLAS.ti", "QualCoder", "Outside the tool"],
              "rows": [
                  ["Import survey variables as attributes", "Yes (variables)", "Yes (classifications)", "Yes (document groups; attributes)", "Yes (attributes from CSV)", "&mdash;"],
                  ["Import open-ends as codeable cells", "Survey import", "Dataset import", "Survey import", "Import survey", "&mdash;"],
                  ["Crosstab codes by variables", "Crosstab; Code Matrix Browser", "Matrix coding query", "Code-document table", "Attribute report", "Pivot table on the export"],
                  ["Joint display", "Mixed Methods menu builds several", "By hand", "By hand", "By hand", "A table in Word"],
                  ["Export code matrix to statistics", "Yes; the Stats module runs it in place", "Yes (export to Excel/SPSS)", "Yes", "Yes (CSV)", "jamovi or R"],
                  ["Typology from codes and variables", "Typology table; Similarity analysis", "By hand", "By hand", "By hand", "Cluster analysis in R"]]},
             {"t": "body", "cls": "sm", "html": "MAXQDA is the tool built with mixed methods "
              "in mind and the one to choose when integration is the study's centre. Every "
              "other tool gets there with an export and a spreadsheet, which is a "
              "morning's work."},
         ]},

        {"type": "content", "label": "Mixed Checklist", "title": "Mixed methods: the checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Practice", "Done"],
              "rows": [
                  ["Integration point stated in the design: connecting, building, merging, or several", ""],
                  ["Interviewees linked to survey records where consent allows; attributes imported", ""],
                  ["Purposive qualitative sampling justified from the survey (variation, extremes, moderators)", ""],
                  ["Matrices of themes by survey-defined groups produced and read", ""],
                  ["A joint display drafted, with the integrated reading in the third column", ""],
                  ["Disagreements between strands reported and interpreted, not suppressed", ""],
                  ["Counts labelled by their denominator: proportion, description, or pointer", ""],
                  ["Open-ends coded with a short codebook, agreement checked, and exported as variables", ""],
                  ["The report weaves the strands rather than stacking chapters", ""]]},
             {"t": "body", "cls": "sm", "html": "Nine rows. Mixed Methods 101 in this series "
              "covers the designs; this list is what the software has to support to make "
              "them work."},
         ]},

        # ===================== SECTION 10: RIGOUR AND REPORTING =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Rigour and Reporting"},

        {"type": "content", "label": "Trustworthiness", "title": "Trustworthiness: the four criteria and what the software contributes to each",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Criterion (Lincoln and Guba 1985)", "Question", "Practices", "What the project file shows"],
              "rows": [
                  ["Credibility", "Is the account believable to those who lived it and to careful readers?", "Prolonged engagement; triangulation across sources; member checking; negative case analysis; peer debriefing", "The retrievals behind every claim; the disconfirming cases coded and memoed"],
                  ["Transferability", "Could a reader judge whether this applies elsewhere?", "Thick description of setting and sample; purposive sampling stated", "Attributes; the sampling memo; the case descriptions"],
                  ["Dependability", "Was the process consistent and could it be followed?", "Audit trail; codebook versions; team procedures; agreement checks", "The log, the codebook versions, the comparison reports, the milestone files"],
                  ["Confirmability", "Are the findings grounded in the data rather than the researcher's preferences?", "Reflexivity; the chain from data to claim; a second reader", "Reflexive memos; the query and retrieval behind each theme; a second coder's work"]]},
             {"t": "body", "cls": "sm", "html": "The project file is the audit trail if it "
              "was kept as sections 03 and 08 describe. A reviewer or examiner given the "
              "file, the codebook versions and the log can follow every step, which is what "
              "'dependability' meant before software and what the software makes routine."},
         ]},

        {"type": "content", "label": "Audit Trail", "title": "The audit trail: what to keep, and what an examiner asks for",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "The raw data: recordings and checked transcripts, in the languages spoken, with the checking recorded.",
                  "The project file at milestones, and the REFI-QDA export.",
                  "Every codebook version with dates and reasons.",
                  "The log of decisions: sampling, transcription, translation, coding, merging, theme building.",
                  "The memos: methods, theme, case, reflexive.",
                  "The agreement reports, with what was done about low agreement.",
                  "The retrievals and matrices behind each reported theme.",
                  "The quotation register: every quotation in the report, its source ID, its original language, and the consent status."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What examiners actually ask", "html":
                         "'Show me how you got from the interviews to theme three.' The "
                         "answer is a memo dated before the theme was named, a matrix, a "
                         "retrieval, and three cases including one that did not fit. 'How "
                         "did you handle the Bangla interviews?' The translation workflow "
                         "memo and the bilingual codebook. 'Who coded what?' The coder "
                         "names and the comparison table. An examiner who gets these "
                         "answers from the project itself stops asking."},
                        {"t": "hbox", "color": "green", "html": "Nothing in the list is "
                         "extra work if the project was run as this course describes. It is "
                         "the project."}]},
         ]},

        {"type": "content", "label": "Reflexivity", "title": "Reflexivity: the researcher in the analysis, written down",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Who did the interviews, in what language, "
                        "with what relationship to the programme and the participants; what "
                        "the analyst expected to find; how the team's positions (caste, "
                        "class, gender, urban, employed by the implementer) shaped what was "
                        "asked and what was heard. A reflexivity statement is not a "
                        "confession; it is the information a reader needs to weigh the "
                        "account. The reflexive memos written during coding are its "
                        "source, and the software keeps them dated."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Write the first reflexive memo before the first interview: expectations, worries, what would surprise you.",
                           "Write one when something does surprise you, and one when a theme starts to feel settled.",
                           "Name the constraints: the evaluation was commissioned by the implementer; the interviewers were its field staff; participants knew that.",
                           "In the report: a paragraph in the methods, and a sentence where a finding could plausibly reflect the position rather than the data."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "Illustrative: 'The Bihar "
                        "interviews were conducted by the programme's own community "
                        "mobilisers, known to the participants; accounts of the group's "
                        "benefits may be more positive than they would be to a stranger, "
                        "and the three most critical accounts came from the Bengal "
                        "interviews conducted by an independent researcher.' That sentence "
                        "changes how the findings are read, and it belongs in the report."}]},
         ]},

        {"type": "content", "label": "Checks", "title": "Member checking, negative cases, and peer debriefing: how each is done",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Member checking", "html":
                         "Taking findings back to participants: a summary read aloud in a "
                         "group meeting, or the framework row for one woman shown to her. "
                         "Birt and colleagues (<em>Qualitative Health Research</em> 2016, "
                         "26:1802) distinguish checking transcripts (low value) from "
                         "checking synthesised findings (higher, and harder). Record what "
                         "participants said in a memo; a disagreement is data."},
                        {"t": "panel", "color": "amber", "title": "Negative case analysis", "html":
                         "Search the retrievals for cases that contradict the theme; code "
                         "them as such; explain them or revise the theme. The three "
                         "women whose husbands claimed the group's money are the shield "
                         "theme's negative cases and its boundary."}],
              "right": [{"t": "panel", "color": "green", "title": "Peer debriefing and second reading", "html":
                         "A colleague outside the team reads the theme memos and a sample "
                         "of retrievals and asks whether the claims follow. In the "
                         "software: give them the project or a REFI-QDA export and the "
                         "codebook; ask them to code two transcripts blind and compare. "
                         "Their questions are logged and answered in the memo."},
                        {"t": "hbox", "color": "amber", "html": "None of these is a "
                         "guarantee. Each is a check a careful reader would expect, and "
                         "each is a paragraph in the methods."}]},
         ]},

        {"type": "content", "label": "Thick Description", "title": "Transferability: the description that lets a reader judge",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A qualitative finding travels only as far as "
                        "a reader can see the setting it came from. Thick description "
                        "means enough about the villages, the groups, the households, the "
                        "programme's delivery and the interviews themselves for a reader in "
                        "Odisha or Sindh to judge whether the shield mechanism would apply "
                        "there. The attributes, the sampling memo and the case descriptions "
                        "in the project are its raw material; a paragraph per site and a "
                        "table of cases with their attributes are its form in the report."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Describe the sample by the attributes that the findings turned on (migration status, group rules, distance to a bank), not only the demographic ones.",
                           "Describe the programme as delivered in these sites, which is rarely the programme as designed.",
                           "Describe the interviews: where, who was present, how long, in what language, whether the husband came in.",
                           "State what the sample cannot speak to, by group and by setting."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "Illustrative: 'Bihar groups "
                        "met fortnightly in a member's courtyard with a written withdrawal "
                        "rule in eleven of twelve; Bengal groups met monthly at the "
                        "panchayat office and four of twelve had no written rule. The "
                        "three cases in which a husband took the group's money were all in "
                        "groups without one.' That paragraph is the transferability "
                        "argument and it came from three attributes."}]},
         ]},

        {"type": "content", "label": "COREQ and SRQR", "title": "Reporting standards: COREQ and SRQR, and how the software answers their items",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["COREQ domain (Tong et al., <em>Int J Qual Health Care</em> 2007, 19:349; 32 items)", "Items the software helps answer"],
                        "rows": [
                            ["Research team and reflexivity (items 1&ndash;8)", "Coder names; reflexive memos; interviewer attribute"],
                            ["Study design (9&ndash;23): theory, sampling, setting, data collection", "Sampling memo; attributes; transcription and translation memos; saturation evidence"],
                            ["Analysis and findings (24&ndash;32): coders, codebook, derivation of themes, software, participant checking, quotations, consistency, clarity of themes", "Codebook versions; agreement table; the chain from retrieval to claim; software and version; quotation register"]]}],
              "right": [{"t": "table",
                         "head": ["SRQR (O'Brien et al., <em>Academic Medicine</em> 2014, 89:1245; 21 items)", "Note"],
                         "rows": [
                             ["Title, abstract, problem, purpose", "As any paper"],
                             ["Approach and paradigm; researcher characteristics and reflexivity", "Method memo; reflexivity statement"],
                             ["Context; sampling; ethics; data collection methods and instruments; units of study; data processing; data analysis; trustworthiness techniques", "The memos and log, in order"],
                             ["Synthesis and interpretation; links to empirical data", "Themes with quotations traced to sources"],
                             ["Integration with prior work; limitations; conflicts of interest; funding", "The discussion"]]},
                        {"t": "hbox", "color": "cyan", "html": "COREQ is written for "
                         "interviews and focus groups in health; SRQR is general. Health "
                         "journals ask for COREQ; most others accept either. Fill the "
                         "checklist against the draft; every unanswerable item is a gap."}]},
         ]},

        {"type": "content", "label": "Quotations", "title": "Quotations in the report: choosing, presenting and protecting",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Choose quotations that show the range of a theme, including its edges, not three that say the same thing well.",
                  "Introduce each: what it shows; then the quotation; then who (pseudonym or ID, attributes that matter: 'member, Bihar, husband a migrant'); then a sentence on how typical it was.",
                  "Give the original where the wording matters, with the translation; mark the translator's choices ('<em>izzat</em>' kept, glossed).",
                  "Keep the interviewer's question where it shaped the answer.",
                  "Never alter meaning by cutting; mark cuts with ellipses and insertions with brackets.",
                  "Check consent for quotation per participant (the attribute from section 02); a woman who agreed to interview but not to quotation is paraphrased."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Anonymisation in small places", "html":
                         "In a village of 400 households, 'the SHG president whose husband "
                         "works in Surat' identifies one woman. Generalise attributes in "
                         "quotations to the level that protects ('a group office-bearer'), "
                         "change the district name where the story is distinctive, and "
                         "let the quotation register hold the real source for the audit. "
                         "The software's ID and the report's pseudonym are linked only in "
                         "the register, which is stored with the consent forms."},
                        {"t": "hbox", "color": "green", "html": "A quotation register is a "
                         "spreadsheet with one row per quotation used: report page, "
                         "pseudonym, source file, segment, language, consent status. It "
                         "takes an hour and it is what a data-protection query is answered "
                         "from."}]},
         ]},

        {"type": "content", "label": "Methods Paragraph", "title": "The methods paragraph, assembled from the project",
         "blocks": [
             {"t": "panel", "color": "cyan", "title": "Illustrative", "html":
              "'We conducted 36 semi-structured interviews (median 52 minutes) with women in "
              "Bihar (n = 19) and West Bengal (n = 17), purposively sampled from the "
              "evaluation survey to vary by SHG membership, change in decision-making score "
              "and husband's migration status (Appendix B). Interviews were conducted in "
              "Hindi or Bangla by two field researchers (one employed by the implementing "
              "organisation) and one independent researcher, audio-recorded with consent, "
              "machine-transcribed in the source language (VaniScribe, Sarvam Saaras v3) and "
              "checked in full against the audio by a native speaker. Analysis followed the "
              "framework method (Gale et al. 2013) in QualCoder 3.6 with source-language "
              "transcripts and parallel English translations. An a priori codebook of 31 "
              "codes from the programme's theory of change was revised after the first five "
              "transcripts and again after an agreement check on eight transcripts coded "
              "independently by two coders (Cohen's &kappa; 0.52 to 0.84 by code before "
              "revision, 0.71 to 0.84 after; Appendix C); the final codebook of 46 codes in "
              "nine categories is in Appendix D with its three versions. Themes were built "
              "through weekly team meetings, memos and a framework matrix of 36 cases by "
              "eight themes; negative cases were sought for each theme. Findings were "
              "presented to two participant groups, whose responses are recorded in "
              "Appendix E. The project file (REFI-QDA export) and codebook are deposited at "
              "[repository], with transcripts withheld under the consent terms.'"},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Every number and every claim in "
                        "the paragraph is a file, a memo or a report in the project. That "
                        "is what 'systematic' means and it is what COREQ and SRQR ask for."}],
              "right": [{"t": "hbox", "color": "amber", "html": "One paragraph, five "
                        "appendices, and a project file. Most qualitative sections in "
                        "evaluation reports have the paragraph without the rest, which is "
                        "why they are not believed."}]},
         ]},

        {"type": "content", "label": "Archiving", "title": "Archiving qualitative data: what can be deposited and where",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Object", "Deposit?", "Where", "Conditions"],
              "rows": [
                  ["Codebook with versions", "Yes, always", "OSF, Zenodo, the institution's repository, with the paper", "None"],
                  ["Project file (REFI-QDA) with coding and memos, transcripts removed", "Usually", "As above", "Memos may contain identifying detail; review them"],
                  ["De-identified transcripts", "Where consent allows", "Qualitative Data Repository (Syracuse), UK Data Service, ICPSR; with access controls", "Consent for archiving; de-identification to a documented standard; often restricted access"],
                  ["Audio", "Rarely", "Restricted repositories only", "Voices identify; consent rarely covers it"],
                  ["Quotation register", "No", "With the consent forms, institutional storage", "The link between pseudonyms and people"],
                  ["Interview guide, consent forms (blank), sampling memo", "Yes", "With the paper", "None"]]},
             {"t": "body", "cls": "sm", "html": "Depositing the codebook and the coded project "
              "without transcripts lets a reader see the analysis's structure while "
              "protecting participants, and it is more than most qualitative papers "
              "offer. Funders increasingly require a data availability statement for "
              "qualitative work; this table is the answer to it."},
         ]},

        # ===================== SECTION 11: AI, CHOOSING A TOOL, AND PRACTICE =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "AI, Choosing a Tool, and Practice"},

        {"type": "content", "label": "AI Features", "title": "The AI features: what they do, tool by tool",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Feature", "What it does", "Where the data go"],
              "rows": [
                  ["ATLAS.ti", "Intentional AI coding; AI summaries; conversational AI", "Codes a document against a stated intent; summarises documents or code groups; answers questions about the project", "To OpenAI via Azure, under ATLAS.ti's terms; opt-in per project"],
                  ["MAXQDA", "AI Assist", "Summarises segments and documents; suggests codes and subcodes; chats with a document; paraphrases", "To OpenAI under VERBI's terms; opt-in; can be disabled institution-wide"],
                  ["NVivo", "AI Assistant", "Summarises files and coded content; suggests codes; explains", "To Lumivero's provider; opt-in"],
                  ["QualCoder", "Optional AI assistance", "Semantic search and code suggestions via an API key the user supplies (OpenAI or compatible)", "To whichever provider the key belongs to; off by default"],
                  ["Taguette", "None", "&mdash;", "&mdash;"],
                  ["Outside the tools", "General LLMs (ChatGPT, Claude, Gemini), Indic models", "Anything, on pasted text", "To the provider; usually outside India; terms vary on training use"]]},
             {"t": "body", "cls": "sm", "html": "Each feature sends transcript text to an "
              "external model. That is the first fact about every one of them, and it "
              "decides whether it can be used at all under the consent given (section 02) "
              "and the institution's data policy."},
         ]},

        {"type": "content", "label": "AI Risks", "title": "Five risks, and the practices that contain them",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Risk", "What happens", "Practice"],
              "rows": [
                  ["Data leaves the machine", "Transcripts of vulnerable women's accounts go to a server abroad, under terms the participants did not see", "No AI features without consent that names external processing; prefer local models (Bodhan's open weights on a lab machine) where consent is narrow; strip identifiers first regardless"],
                  ["Hallucinated summaries", "A summary states something no participant said; a suggested code has no segment", "Every AI summary is checked against the retrieval; every AI code is read before it is kept; the model's output is a draft, never evidence"],
                  ["Homogenisation", "The model codes in the register of English-language psychology; Indian-language nuance and in vivo phrasing disappear", "Code in the source language by hand for the analytic codes; use AI, if at all, for structural and descriptive first-pass codes"],
                  ["Weak Indian-language performance", "Hindi and Bangla transcripts summarised badly; code-switching mishandled", "Test on three transcripts with a bilingual reader before any use; prefer models built for Indian languages"],
                  ["Undisclosed use", "Reviewers and readers assume human coding; the paper's claims about method are false", "Disclose the tool, version, what it was used for, on what, and how its output was validated, in the methods (COPE and most journals now require it)"]]},
             {"t": "body", "cls": "sm", "html": "A defensible use, illustrative: AI summaries "
              "of each transcript as a reading aid, on de-identified English translations, "
              "with consent covering external processing, checked by the interviewer, and "
              "disclosed. An indefensible one: AI coding of Hindi transcripts as the "
              "analysis, reported as thematic analysis."},
         ]},

        {"type": "content", "label": "AI Validation", "title": "If you use AI coding: validate it like a second coder, and report the table",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Treat the model as a coder with unknown "
                        "reliability. Give it the codebook; have it code the same eight "
                        "files a human coded; run the coder comparison; report kappa per "
                        "code. Read the disagreements. Where the model is reliable (often "
                        "descriptive and topic codes), it may be used for a first pass that "
                        "a human reviews; where it is not (interpretive codes, in vivo, "
                        "anything requiring the context of the interview), it is not used. "
                        "The validation table goes in the appendix beside the human one."},
                       {"t": "table",
                        "head": ["Code", "Human-human &kappa;", "Human-model &kappa;", "Decision"],
                        "rows": [
                            ["SAVINGS_PURPOSE", "0.84", "0.77", "Model first pass, human review"],
                            ["SAVINGS_SHIELD", "0.79", "0.41", "Human only"],
                            ["DECISION_STRATEGY_TIMING", "0.71", "0.38", "Human only"],
                            ["FEAR_FORMAL_FINANCE", "0.81", "0.69", "Model first pass, human review"]]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Illustrative. The pattern is typical: the model finds topics and misses interpretation, especially the codes that became the study's findings.",
                  "Cost the review time honestly. Reviewing a model's coding of a transcript takes half the time of coding it, not a tenth.",
                  "Re-validate when the codebook changes or the model version does.",
                  "State in the methods exactly which codes were model-assisted and how."]},
                        {"t": "hbox", "color": "amber", "html": "The question a referee will "
                         "ask: 'What did the model code that a human would not have, and "
                         "what did it miss?' Have the answer from the comparison, not from "
                         "impression."}]},
         ]},

        {"type": "content", "label": "Disclosure", "title": "Disclosing AI and software use: the sentences",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Software", "html":
                         "'Coding and retrieval were carried out in QualCoder 3.6 (Curtain, "
                         "2025); the project was exported in REFI-QDA format for archiving.' "
                         "Name the tool and version; the version changes defaults and "
                         "features."},
                        {"t": "panel", "color": "amber", "title": "Transcription", "html":
                         "'Transcripts were produced by automatic speech recognition "
                         "(VaniScribe on Sarvam Saaras v3) in Hindi and Bangla and checked "
                         "in full against the audio by native-speaking members of the team; "
                         "participants consented to third-party transcription.'"},
                        {"t": "panel", "color": "green", "title": "AI assistance", "html":
                         "'MAXQDA's AI Assist (OpenAI GPT-4o via VERBI, May 2026) was used "
                         "to generate document summaries as reading aids on de-identified "
                         "English translations, under consent covering external processing; "
                         "summaries were not used as data and all coding was by the authors. "
                         "No AI tool was used to generate or edit the text of this report.'"}],
              "right": [{"t": "body", "html": "Three sentences, one per use, each naming the "
                        "tool, the version, the data it saw, the consent basis, and the "
                        "limit of its role. Where no AI was used, one sentence says so; "
                        "journals now ask, and silence reads as concealment. Academic "
                        "Writing 101, section 11, covers the publisher policies."},
                        {"t": "hbox", "color": "amber", "html": "Write the disclosure before "
                         "the analysis. If it cannot be written honestly, the use should "
                         "not happen."}]},
         ]},

        {"type": "content", "label": "Choosing", "title": "Choosing a tool: the decision table",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Situation", "Choose", "Because"],
              "rows": [
                  ["First project; under twenty text sources; one analyst", "Taguette", "Ten minutes to start; everything exports; nothing to unlearn"],
                  ["Any project with audio, attributes or a second coder; no budget", "QualCoder", "The full workflow, free, offline, REFI-QDA"],
                  ["Institution licenses NVivo, MAXQDA or ATLAS.ti", "That one", "Support, supervisors, and site-licensed collaboration"],
                  ["Mixed methods with a survey at the centre", "MAXQDA", "Variables, crosstabs, joint displays, Stats"],
                  ["Framework analysis for a policy client with a deadline", "NVivo or MAXQDA", "Framework matrix and Summary Grid"],
                  ["Discourse or narrative work linking passages", "ATLAS.ti", "Quotations and networks"],
                  ["Distributed team, no server, cloud permitted by consent", "ATLAS.ti Web, MAXQDA TeamCloud or NVivo Collaboration Cloud", "Simultaneous access"],
                  ["Distributed team, data must stay in the institution", "Self-hosted Taguette, or QualCoder with the divide-and-merge arrangement", "No external storage"],
                  ["Teaching a methods class with no budget", "Taguette, then QualCoder", "Section 04's sequence"],
                  ["Long programme, staff turnover, recurring rounds", "Any REFI-QDA tool, with the codebook as the persistent asset", "The tool may change; the codebook and the archive should not"]]},
             {"t": "body", "cls": "sm", "html": "The last row is the general principle. "
              "Invest in the codebook, the memos and the archive; the software is where "
              "they live this year."},
         ]},

        {"type": "content", "label": "Worked Project", "title": "The full worked project: from recordings to a deposited archive",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Week", "Work", "Tool", "Section"],
                        "rows": [
                            ["1", "Consent review; transcription in source languages; native-speaker checking; pseudonymisation; attribute sheet", "VaniScribe; Word; a spreadsheet", "02"],
                            ["2", "Project setup; a priori codebook with definitions; first memo; five transcripts coded; codebook revised; five recoded", "QualCoder", "03"],
                            ["3&ndash;5", "Coding by two coders in their languages; weekly meetings; inductive codes proposed and adopted; agreement on eight files; revision; second agreement check", "QualCoder; coder comparison", "03, 08"],
                            ["6", "Merge; retrievals read; matrices by state, membership and migration; co-occurrence; theme memos", "QualCoder reports", "07"],
                            ["7", "Framework matrix charted (36 &times; 8); negative cases; joint display with survey results; two member-checking meetings", "QualCoder export; Word; the survey's jamovi file", "07, 09, 10"],
                            ["8", "Findings written with quotations from the register; methods paragraph; appendices (codebook versions, agreement, sampling, member checking, code-creation curve); REFI-QDA export deposited", "Word; OSF", "10"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, for the 36-interview "
                        "SHG study. Eight weeks for a two-coder team, of which the first is "
                        "data preparation and the last is writing. The tools cost nothing; "
                        "the transcription cost a few thousand rupees; the checking cost a "
                        "week of a native speaker's time and was the best-spent week."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the archive holds", "html":
                         "The codebook in three versions; the REFI-QDA project without "
                         "transcripts; the agreement tables; the sampling and translation "
                         "memos; the interview guide in three languages; the framework "
                         "matrix; the joint display. Enough for an examiner to follow every "
                         "step, and nothing that identifies a participant."},
                        {"t": "hbox", "color": "amber", "html": "The same project in NVivo "
                         "or MAXQDA would differ in the menus and in nothing that matters "
                         "to the findings."}]},
         ]},

        {"type": "content", "label": "Pitfalls", "title": "The dozen errors QDA software makes easy",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Error", "Section", "Fix in one line"],
              "rows": [
                  ["Translating everything to English and coding the translation, without saying so", "02", "Choose a workflow; state it; keep the source"],
                  ["Machine transcripts uncorrected", "02", "A native-speaker check against the audio, recorded"],
                  ["Codes without definitions", "03", "Fill the memo field for every code"],
                  ["Two hundred codes and no theme", "03", "Merge by definition; write theme memos"],
                  ["Auto-coding or text search reported as coding", "03, 07", "Use to find; code by reading"],
                  ["Matrix cells reported as population proportions", "07", "Files first, denominator stated, purposive sample named"],
                  ["Word clouds as analysis", "07", "Delete them"],
                  ["Teams merging for the first time on the deadline", "08", "Test the merge with copies in week 2"],
                  ["One kappa for forty codes", "08", "Per code, with the action taken"],
                  ["Qualitative and survey chapters that never meet", "09", "A joint display with an integrated column"],
                  ["Transcripts uploaded to an AI feature without consent for external processing", "11", "Check consent; strip identifiers; prefer local models; disclose"],
                  ["No audit trail beyond the project file", "10", "Codebook versions, log, memos, milestone files, REFI-QDA export"]]},
         ]},

        {"type": "content", "label": "Checklist", "title": "Before you submit: the qualitative software checklist",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Data and process", "Done"],
                        "rows": [
                            ["Consent covers recording, transcription, storage, quotation and any external processing", ""],
                            ["Transcripts in the source language, checked, pseudonymised", ""],
                            ["Translation workflow stated", ""],
                            ["Attributes imported; sample described", ""],
                            ["Codebook with definitions, versioned, in the appendix", ""],
                            ["Agreement checked per code where the method calls for it; reported", ""],
                            ["Memos and log kept; milestone files and REFI-QDA export saved", ""]]}],
              "right": [{"t": "table",
                         "head": ["Analysis and reporting", "Done"],
                         "rows": [
                             ["Every theme traceable to retrievals, matrices and cases", ""],
                             ["Negative cases sought and reported", ""],
                             ["Counts labelled by denominator; no purposive-sample proportions", ""],
                             ["Framework matrix or equivalent for the main themes", ""],
                             ["Joint display where a survey exists", ""],
                             ["Quotations chosen for range, introduced, sourced, consented, registered", ""],
                             ["COREQ or SRQR checklist completed", ""],
                             ["Software, versions and any AI use disclosed; codebook and project deposited", ""]]},
                        {"t": "hbox", "color": "cyan", "html": "Fifteen lines. The "
                         "translation workflow and the AI disclosure are the two most "
                         "often missing from South Asian qualitative reports."}]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "What it covers", "Notes"],
              "rows": [
                  ["Salda&ntilde;a, <em>The Coding Manual for Qualitative Researchers</em> (4th ed., Sage, 2021)", "Coding methods, first and second cycle, memos", "The companion to section 03"],
                  ["Miles, Huberman and Salda&ntilde;a, <em>Qualitative Data Analysis: A Methods Sourcebook</em> (4th ed., Sage, 2020)", "Displays, matrices, drawing and verifying conclusions", "Section 07"],
                  ["Gale et al., <em>BMC Med Res Methodol</em> 2013, 13:117", "The framework method, step by step", "Sections 03 and 07"],
                  ["Braun and Clarke, <em>Thematic Analysis: A Practical Guide</em> (Sage, 2021)", "Reflexive thematic analysis and what it is not", "Why agreement is not always the goal"],
                  ["O'Connor and Joffe, <em>Int J Qual Methods</em> 2020, 19", "Intercoder reliability: debates and guidelines", "Section 08"],
                  ["Fetters, Curry and Creswell, <em>Health Serv Res</em> 2013, 48:2134; Guetterman et al. 2015", "Integration and joint displays", "Section 09"],
                  ["Tong et al. 2007 (COREQ); O'Brien et al. 2014 (SRQR)", "Reporting standards", "Section 10"],
                  ["Silver and Lewins, <em>Using Software in Qualitative Research: A Step-by-Step Guide</em> (2nd ed., Sage, 2014); the CAQDAS Networking Project (University of Surrey)", "Tool-independent software strategy; comparative reviews of every package", "The reference for sections 04 to 06"],
                  ["QualCoder wiki and manual; Taguette documentation; vendor manuals", "The tools", "Free"],
                  ["ImpactMojo: Qualitative Methods 101, Mixed Methods 101, Research Ethics 101, Data Protection & the DPDP Act 101; VaniScribe", "The methods, the ethics, the law, and the transcription tool", "impactmojo.in"]]},
         ]},

        {"type": "content", "label": "Summary", "title": "What to remember",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "The software files, retrieves and counts. The method, the codes' meanings and the claims are yours.",
                  "Transcribe in the language spoken; check against the audio; decide the translation workflow and say what it lost.",
                  "A code is a definition. A codebook is versioned. A memo is where the analysis happens.",
                  "Free tools cover the whole workflow: Taguette to start, QualCoder for everything else; REFI-QDA makes the coding portable.",
                  "Retrievals are read, matrices are pointers, and no purposive count is a proportion of anyone but the sample."]}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "Teams share one codebook, test the merge early, and measure agreement per code where the method calls for it.",
                  "Attributes from the survey make the qualitative data cross-tabulable, and a joint display makes the strands one study.",
                  "The project file, the codebook versions, the log and the memos are the audit trail; deposit what consent allows.",
                  "AI features send transcripts abroad, hallucinate, and miss interpretation; validate like a second coder, or do not use them; disclose either way.",
                  "Report to COREQ or SRQR, with a quotation register behind every quotation."]},
                        {"t": "hbox", "color": "amber", "html": "The best QDA project is one an "
                         "examiner can walk through from any theme back to the recording "
                         "in ten minutes. Build for that reader."}]},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Qualitative Analysis Software 101 &middot; Complete",
         "headline": "Now go code it,<br>and keep the thinking.",
         "byline": "The software holds the evidence and the trail; the interpretation stays "
                   "with the researcher who heard the interviews. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}

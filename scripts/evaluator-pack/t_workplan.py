"""Kick-off Checklist and Workplan (Excel workbook and Word guide)."""
from openpyxl import Workbook

from xl_pack import grid_sheet, package, readme

BASE = "ImpactMojo-Kickoff-Workplan"
FILE = BASE + ".zip"
STATUS = ["Not started", "In progress", "Done", "Late"]

DAYS = lambda r: f'=IF(OR(D{r}="",E{r}=""),"",E{r}-D{r}+1)'
FLAG = lambda r: f'=IF(OR(E{r}="",H{r}="Done"),"",IF(E{r}<TODAY(),"Past end date",""))'
CHK_PCT = '=IF(COUNTA(C5:C24)=0,"",COUNTIF(D5:D24,"Done")/COUNTA(C5:C24))'


def build(out):
    wb = Workbook()
    ws = wb.active
    ws.title = "Read me"
    readme(ws, "Kick-off checklist and workplan", "What to settle at the first meeting, and a task-level plan that shows who does what by when.", [
        ("What is in the workbook", True),
        ("Kick-off checklist: 20 things to confirm with the client and the team in the first week, each with an owner, a status and a note.", False),
        ("Workplan: tasks grouped by phase with an owner, start and end dates and the deliverable each task feeds. Days and a past-end-date flag calculate.", False),
        ("Week view: a plan over 13 weeks. Type a week number for the start and the end, and the bar fills.", False),
        ("Worked example: the first rows of the plan for a maternal and newborn health evaluation.", False),
        ("How to use it", True),
        ("Yellow cells are yours to fill. Grey cells calculate. Agree the workplan with the client at the kick-off, and update the status column before every weekly call.", False),
    ])
    chk = [
        "Client contact and decision-maker named, with a backup",
        "Scope, questions and deliverables confirmed against the statement of work",
        "Single channel and single set of comments agreed",
        "Review periods and deemed-acceptance rule confirmed",
        "Data the client will share listed, with dates",
        "Data protection and consent terms agreed",
        "Access to facilities, officials and respondents arranged",
        "Ethics approval route agreed, if needed",
        "Team roles and days confirmed",
        "Subcontractors and partners confirmed in writing",
        "Weekly call time fixed",
        "Reporting format for the weekly note agreed",
        "Invoice contact and payment milestones confirmed",
        "Site visit and field calendar drafted",
        "Language and translation needs listed",
        "Branding and acknowledgement rules confirmed",
        "Who will receive the final report and the summary",
        "Shared folder and naming rules set up",
        "Risks and assumptions logged",
        "Date of the inception report fixed",
    ]
    c = wb.create_sheet("Kick-off checklist")
    grid_sheet(c, "Kick-off checklist", "Confirm each item at or soon after the first meeting.",
               [("No.", 6), ("Date confirmed", 12), ("Item to confirm", 62), ("Status", 14), ("Owner", 16), ("Note", 44)], 20,
               rows=[[i + 1, None, t] for i, t in enumerate(chk)], drops={3: ["Open", "Confirmed", "Not needed"]})
    c["H4"] = "Share confirmed"
    c["H5"] = '=IF(COUNTA(C5:C24)=0,"",COUNTIF(D5:D24,"Confirmed")/COUNTA(C5:C24))'
    c["H5"].number_format = "0%"
    cols = [("No.", 6), ("Phase", 16), ("Task", 46), ("Start", 12), ("End", 12), ("Days", 8), ("Owner", 16), ("Status", 13), ("Deliverable it feeds", 28), ("Flag", 14)]
    w = wb.create_sheet("Workplan")
    grid_sheet(w, "Workplan", "One row per task. Days and the flag calculate.", cols, 40, calc={5: DAYS, 9: FLAG}, drops={7: STATUS}, fmts={3: "dd mmm yyyy", 4: "dd mmm yyyy"})
    wk = wb.create_sheet("Week view")
    grid_sheet(wk, "Week view", "Type the start week and end week (1 to 13). The bar fills.",
               [("Task", 40), ("From week", 10), ("To week", 10)] + [(f"W{i}", 5) for i in range(1, 14)], 25,
               calc={j: (lambda r, k=j - 2: f'=IF(OR($B{r}="",$C{r}=""),"",IF(AND({k}>=$B{r},{k}<=$C{r}),"█",""))') for j in range(3, 16)})
    ex = [
        [1, "Inception", "Kick-off meeting and document handover", "2026-11-02", "2026-11-06", None, "Project manager", "Done", "Inception report"],
        [2, "Inception", "Desk review of programme documents", "2026-11-02", "2026-11-13", None, "Evaluator", "In progress", "Inception report"],
        [3, "Inception", "Draft evaluation matrix and sampling plan", "2026-11-09", "2026-11-20", None, "Team leader", "In progress", "Inception report"],
        [4, "Fieldwork", "Train enumerators and pilot the tools", "2026-12-07", "2026-12-12", None, "Field lead", "Not started", "Data set"],
        [5, "Fieldwork", "Facility surveys and interviews in three blocks", "2026-12-14", "2027-01-15", None, "Field lead", "Not started", "Data set"],
    ]
    x = wb.create_sheet("Worked example")
    grid_sheet(x, "Worked example: workplan", "Five tasks from the Surakshit Maa evaluation. Days calculate.", cols, 5, rows=ex, calc={5: DAYS, 9: FLAG}, drops={7: STATUS}, fmts={3: "dd mmm yyyy", 4: "dd mmm yyyy"})
    x.title = "Worked example"
    return package(out, BASE, wb, GUIDE)


GUIDE = dict(
    file=BASE + "-GUIDE.docx",
    cover=("Kick-off Checklist and Workplan", "Twenty things to settle in the first week, and a task-level plan that everyone can read", "Guide to the Excel workbook · ₹199"),
    inside=[
        "**Part A.** Why the first week decides the rest.",
        "**Part B.** The method in four steps: prepare, hold the kick-off, build the plan and keep it current.",
        "**Part C.** Reference assets: a kick-off agenda, a short list of questions for the client and a glossary.",
        "**Part D.** A worked example: the opening tasks for a maternal and newborn health evaluation.",
    ],
    intro="This guide goes with the Excel workbook. Use it after the statement of work is signed and before the inception report is due.",
    parts=[
        ("PART A", "Why the first week matters", [
            ("body", "Most of what goes wrong in an evaluation can be traced to something nobody asked in the first week: who approves the report, how many rounds of comments, when the data will arrive. The kick-off meeting is the cheapest moment to ask, because the client is still pleased to have appointed you and nobody has yet missed a date."),
            ("body", "The checklist lists the twenty things to settle. The workplan turns the statement of work into tasks with owners and dates, so that a late task is visible while it can still be fixed."),
            ("body", "Two habits help. Send the agenda two days ahead, so that the right people attend. Send the plan and the confirmed list within a day of the meeting, so that decisions are on record."),
        ]),
        ("PART B", "The method", [
            ("h", "1.  Prepare"),
            ("purpose", "Arrive with a list of what you need to know."),
            ("guide", "Read the statement of work again and mark every item that depends on the client. Open the checklist and note which items you can fill in yourself."),
            ("good", "You know which five items matter most for this client."),
            ("mistakes", "Using the meeting to read the statement of work aloud."),
            ("h", "2.  Hold the kick-off"),
            ("purpose", "Settle the items only the client can settle."),
            ("guide", "Follow the agenda in Part C. Go through the checklist and mark each item Confirmed, Open or Not needed. Write the owner and a date against every Open item before anyone leaves."),
            ("good", "At the end, every open item has an owner and a date."),
            ("mistakes", "Leaving with 'we will get back to you' and no date."),
            ("h", "3.  Build the plan"),
            ("purpose", "Turn the statement of work into tasks."),
            ("guide", "In the Workplan sheet, list the tasks under the phases of inception, fieldwork, analysis and reporting. Give each an owner, a start date and an end date. The sheet calculates the days and flags a task that is past its end date and not done. Use the Week view to see the plan on one page."),
            ("table", ["Column", "What goes in it"], [
                ["Phase", "Inception, Fieldwork, Analysis or Reporting."],
                ["Task", "A verb and an object, small enough to finish in two weeks."],
                ["Owner", "One person."],
                ["Deliverable it feeds", "The deliverable in the statement of work that depends on the task."],
                ["Status", "Not started, In progress, Done or Late."],
            ], [4.2, 11.7]),
            ("good", "No task is longer than two weeks, and every deliverable has its tasks."),
            ("mistakes", "A task called 'fieldwork' that runs for six weeks."),
            ("h", "4.  Keep it current"),
            ("purpose", "Make the plan the thing you look at each week."),
            ("guide", "Update the status column before the weekly call. If a date moves, change it and note why in the weekly status note."),
            ("good", "The plan on the screen matches the plan in people's heads."),
            ("mistakes", "Keeping the plan as a file that nobody opens after the first week."),
        ]),
        ("PART C", "Reference assets", [
            ("h", "C1.  Kick-off agenda (60 minutes)"),
            ("numbered", [
                "Introductions and roles (5 minutes).",
                "What the evaluation is for and who will use it (10 minutes).",
                "Scope, questions and deliverables (10 minutes).",
                "Data, access and consent (10 minutes).",
                "Comments, approvals and payments (10 minutes).",
                "The plan and the next two weeks (10 minutes).",
                "Open items, owners and dates (5 minutes).",
            ]),
            ("h", "C2.  Questions that are easy to forget"),
            ("bullets", [
                "Who signs off the report, and does anyone else have a veto?",
                "Is there anything the client does not want us to say?",
                "What has been tried before, and why did it stop?",
                "Which officials or partners should hear from the client before we call?",
            ]),
            ("h", "C3.  Glossary"),
            ("table", ["Term", "Meaning"], [
                ["Kick-off", "The first formal meeting between the client and the team."],
                ["Workplan", "A list of tasks with owners and dates."],
                ["Deliverable", "A document or data set the client has agreed to receive."],
                ["Milestone", "A deliverable or date on which a payment depends."],
            ], [3.6, 12.3]),
        ]),
        ("PART D", "Worked example: maternal and newborn health evaluation", [
            ("body", "The kick-off held on 2 November 2026 confirmed 16 of the 20 items. The four open items were the list of facilities, the ethics route, the data-sharing agreement and the single set of comments. Each was given an owner and a date within the week."),
            ("table", ["No.", "Phase", "Task", "Start", "End", "Days"], [
                ["1", "Inception", "Kick-off meeting and document handover", "2 Nov", "6 Nov", "5"],
                ["2", "Inception", "Desk review of programme documents", "2 Nov", "13 Nov", "12"],
                ["3", "Inception", "Draft evaluation matrix and sampling plan", "9 Nov", "20 Nov", "12"],
                ["4", "Fieldwork", "Train enumerators and pilot the tools", "7 Dec", "12 Dec", "6"],
                ["5", "Fieldwork", "Facility surveys and interviews in three blocks", "14 Dec", "15 Jan", "33"],
            ], [1.0, 2.2, 7.0, 1.9, 1.9, 1.9]),
            ("figures", "The dates are illustrative. Days count calendar days, with both the start and the end included."),
        ]),
    ],
)

PAGE = dict(
    slug="kickoff-workplan-template",
    title="Kick-off Checklist and Workplan",
    file=FILE,
    ext="XLSX",
    eyebrow="Template · XLSX",
    crumb="Template",
    meta="An Excel kick-off checklist of 20 items and a task-level workplan with a 13-week view, plus a Word guide and a worked example. ₹199.",
    og="A 20-item kick-off checklist and a task-level workplan with a week view. ₹199.",
    lede="Twenty things to settle in the first week, and a task-level plan that everyone can read.",
    note="Editable XLSX workbook + a Word guide · delivered to your inbox within 24 hours of payment.",
    letter_h="Settle the first week properly",
    letter=[
        "Most of what goes wrong in an evaluation can be traced to something nobody asked in the first week: who approves the report, how many rounds of comments, when the data will arrive. The kick-off meeting is the cheapest moment to ask.",
        "This workbook gives you a checklist of twenty items to confirm, a workplan with owners, dates and a flag for late tasks, and a 13-week view that fills as you type. A Word guide adds a 60-minute kick-off agenda and a worked example.",
        'It follows the <a href="/products/engagement-charter-template/">Engagement Charter</a>, whose terms the kick-off confirms, and feeds the <a href="/products/weekly-status-note-template/">Weekly Status Note</a>.',
    ],
    inside=[
        "A kick-off checklist of 20 items, with owner, status and a share-confirmed figure",
        "A workplan with phases, owners, dates, days and a past-end-date flag",
        "A 13-week view that fills from the start and end weeks",
        "A Word guide with a 60-minute agenda and questions that are easy to forget",
        "A worked example: the opening tasks of a maternal and newborn health evaluation",
    ],
    sample=[
        ("Kick-off checklist", "20 items, with a share confirmed"),
        ("Workplan", "owner, dates, days and a late flag"),
        ("Week view", "13 weeks on one page"),
        ("Kick-off agenda", "60 minutes, seven items"),
    ],
    sample_file=None,
    faq=[
        ("What format is it?", "An Excel workbook (.xlsx) with live formulas and dropdowns, plus a Word guide. It also opens in Google Sheets and LibreOffice."),
        ("Does it draw a Gantt chart?", "It draws a simple bar over 13 weeks from the start and end weeks you type. It is not a project management system."),
        ("When do I use it?", "After the statement of work is signed and before the inception report is due."),
        ("How fast is delivery?", "Within 24 hours of confirming payment, usually much sooner."),
    ],
    search_desc="An Excel kick-off checklist and workplan for evaluations with a 13-week view, a Word guide and a worked example. Buy for ₹199 via UPI.",
    search_tags=["template", "kick-off", "workplan", "project management", "consulting", "evaluation", "Excel", "premium", "paid", "₹199"],
    search_id="PROD-KICKOFF-WORKPLAN",
    card="Kick-off Checklist and Workplan",
    card_p="Twenty items and a plan everyone can read.",
    before="Stakeholder Map",
)

# -*- coding: utf-8 -*-
"""KoboToolbox and ODK: Building Survey Forms with XLSForm. A guided tool course with Python cells that check
a form definition and a downloaded dataset.

Facts checked on 6 October 2026 against kobotoolbox.org (pricing), support.kobotoolbox.org, the KoboToolbox
community forum announcement of 1 September 2023, xlsform.org, docs.getodk.org, getodk.org, the DPDP Act 2023
(Gazette, 11 August 2023) and the DPDP Rules 2025 (G.S.R. 846(E), 13 November 2025). Sources are listed in the
agent report.
"""

A = 'style="color:var(--accent-color)"'


def link(href, text):
    return '<a href="%s" rel="noopener" target="_blank" %s>%s</a>' % (href, A, text)


def IC(s):
    return '<code class="inline">%s</code>' % s


DL = '<a href="/code/data/households.csv" download %s>households.csv</a>' % A

# The form used throughout the course, written as the three XLSForm sheets in CSV text so Python can read it.
FORM = '''import pandas as pd, io

survey = pd.read_csv(io.StringIO("""type,name,label,hint,relevant,constraint,constraint_message,required,choice_filter
select_one state,state,State,,,,,yes,
select_one district,district,District,,,,,yes,state=${state}
select_one area,area,Is this household rural or urban?,,,,,yes,
integer,hh_size,How many people usually live in this household?,Count everyone who ate from the same kitchen last night,,. >= 1 and . <= 30,Enter a number from 1 to 30,yes,
decimal,land_acres,How many acres of land does the household own?,,${area} = 'rural',. >= 0 and . <= 100,Enter 0 to 100 acres,yes,
select_one yes_no,has_bank_account,Does anyone in the household have a bank account?,,,,,yes,
select_one yes_no,received_transfer,Did the household receive a cash transfer in the last 12 months?,,,,,yes,
integer,transfer_amount,How much did the household receive in total (Rs)?,,${received_transfer} = 'yes',. > 0,Enter an amount above zero,yes,
"""), keep_default_na=False)

choices = pd.read_csv(io.StringIO("""list_name,name,label,state
state,bihar,Bihar,
state,kerala,Kerala,
district,gaya,Gaya,bihar
district,purnia,Purnia,bihar
district,kozhikode,Kozhikode,kerala
district,wayanad,Wayanad,kerala
area,rural,Rural,
area,urban,Urban,
yes_no,yes,Yes,
yes_no,no,No,
"""), keep_default_na=False)
'''

C = {}
C["lint"] = FORM + '''import re

problems = []
names = list(survey["name"])

# 1. Names: unique, start with a letter or _, then letters, digits, - _ .
for n in names:
    if names.count(n) > 1:
        problems.append(f"duplicate name: {n}")
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.-]*", n):
        problems.append(f"invalid name: {n!r}")

# 2. Every select_one or select_multiple list exists in choices
lists = set(choices["list_name"])
for t in survey["type"]:
    parts = t.split()
    if parts[0] in ("select_one", "select_multiple") and parts[1] not in lists:
        problems.append(f"no choice list called {parts[1]}")

# 3. Every ${name} refers to a question asked earlier in the form
for i, row in survey.iterrows():
    for col in ("relevant", "constraint", "choice_filter"):
        for ref in re.findall(r"\\$\\{(\\w+)\\}", row[col]):
            if ref not in names[:i]:
                problems.append(f"{row['name']}: {col} refers to {ref}, which is not asked before it")

# 4. A value compared in relevant must be a choice name in that question's list
qlist = {r["name"]: r["type"].split()[1] for _, r in survey.iterrows() if r["type"].startswith("select")}
for _, row in survey.iterrows():
    for ref, val in re.findall(r"\\$\\{(\\w+)\\}\\s*=\\s*'([^']*)'", row["relevant"]):
        ok = set(choices.loc[choices["list_name"] == qlist.get(ref, ""), "name"])
        if val not in ok:
            problems.append(f"{row['name']}: relevant compares {ref} with '{val}', but its choices are {sorted(ok)}")

print(len(survey), "questions,", len(choices), "choices,", len(lists), "choice lists")
print("\\n".join(problems) if problems else "No problems found")'''

C["constraints"] = '''import pandas as pd

def check(df):
    """Apply the form's constraints and skip logic to a downloaded file. One row per problem."""
    rules = {
        "hh_size outside 1 to 30":        ~df["hh_size"].between(1, 30),
        "land_acres outside 0 to 100":    ~df["land_acres"].between(0, 100),
        "urban household with land":      (df["area"] == "Urban") & (df["land_acres"] > 0),
        "has_bank_account not Yes/No":    ~df["has_bank_account"].isin(["Yes", "No"]),
        "received_transfer not Yes/No":   ~df["received_transfer"].isin(["Yes", "No"]),
        "hh_id appears more than once":   df["hh_id"].duplicated(keep=False),
    }
    out = [pd.DataFrame({"hh_id": df.loc[m, "hh_id"], "problem": name}) for name, m in rules.items()]
    return pd.concat(out, ignore_index=True)

hh = pd.read_csv("households.csv")
print("households.csv:", len(hh), "rows,", len(check(hh)), "problems")

# A practice copy with five entry errors planted in it
bad = hh.copy()
bad.loc[bad["hh_id"] == 12, "hh_size"] = 0
bad.loc[bad["hh_id"] == 57, "hh_size"] = 44
bad.loc[bad["hh_id"] == 88, "land_acres"] = -2
bad.loc[bad["hh_id"] == 101, "received_transfer"] = "Y"
first_urban = bad.loc[bad["area"] == "Urban", "hh_id"].iloc[0]
bad.loc[bad["hh_id"] == first_urban, "land_acres"] = 2.0
bad = pd.concat([bad, bad[bad["hh_id"] == 200]], ignore_index=True)   # one submission sent twice

problems = check(bad)
print("practice copy:", len(bad), "rows,", len(problems), "problems")
print(problems.sort_values("hh_id").to_string(index=False))'''

C["daily"] = '''import pandas as pd
hh = pd.read_csv("households.csv")
d = pd.read_csv("districts.csv")
m = hh.merge(d, on="district", how="left", validate="many_to_one")
print("rows after the join:", len(m), " unmatched districts:", m["field_team"].isna().sum())

# A daily check by field team: how many interviews, and do the answers look alike?
m["transfer"] = (m["received_transfer"] == "Yes").astype(int)
m["bank"] = (m["has_bank_account"] == "Yes").astype(int)
by_team = m.groupby("field_team").agg(
    interviews=("hh_id", "size"),
    districts=("district", "nunique"),
    mean_hh_size=("hh_size", "mean"),
    pct_bank=("bank", "mean"),
    pct_transfer=("transfer", "mean"),
)
by_team[["pct_bank", "pct_transfer"]] *= 100
print(by_team.round(1))'''

C["lang"] = '''import pandas as pd, io

survey = pd.read_csv(io.StringIO("""type,name,label::English (en),label::Hindi (hi),constraint,constraint_message::English (en),constraint_message::Hindi (hi)
select_one district,district,District,जिला,,,
integer,hh_size,How many people usually live in this household?,इस परिवार में आमतौर पर कितने लोग रहते हैं?,. >= 1 and . <= 30,Enter a number from 1 to 30,1 से 30 के बीच कोई संख्या लिखें
select_one yes_no,has_bank_account,Does anyone in the household have a bank account?,क्या परिवार में किसी का बैंक खाता है?,,,
select_one yes_no,shg_member,Is anyone in the household a member of a self-help group?,,,,
"""), keep_default_na=False)

choices = pd.read_csv(io.StringIO("""list_name,name,label::English (en),label::Hindi (hi)
yes_no,yes,Yes,हाँ
yes_no,no,No,नहीं
"""), keep_default_na=False)

# Every English column needs its Hindi partner, filled in on every row that has English text
for sheet_name, sheet in [("survey", survey), ("choices", choices)]:
    for col in [c for c in sheet.columns if c.endswith("::English (en)")]:
        hi = col.replace("English (en)", "Hindi (hi)")
        if hi not in sheet.columns:
            print(f"{sheet_name}: no column {hi}")
            continue
        gaps = sheet[(sheet[col] != "") & (sheet[hi] == "")]
        for _, r in gaps.iterrows():
            print(f"{sheet_name}: row '{r['name']}' has {col} but no Hindi")
    plain = [c for c in sheet.columns if c in ("label", "hint", "constraint_message")]
    if plain:
        print(f"{sheet_name}: column(s) {plain} have no language, so they appear as a separate 'Default' language")
print("check finished")'''

C["pseudo"] = '''import pandas as pd, hmac, hashlib
hh = pd.read_csv("households.csv")

# Keep this key out of the dataset, out of email and out of any Git repository.
KEY = b"replace-with-a-long-random-key-kept-by-the-data-manager"

def code(x):
    return hmac.new(KEY, str(x).encode(), hashlib.sha256).hexdigest()[:10]

share = hh.copy()
share.insert(0, "pid", share["hh_id"].map(code))
key_table = share[["pid", "hh_id"]]          # stays with the data manager, encrypted
share = share.drop(columns=["hh_id"])
share["land_band"] = pd.cut(share["land_acres"], [-0.01, 0, 1, 2.5, 100],
                            labels=["none", "up to 1", "1 to 2.5", "over 2.5"])
share = share.drop(columns=["land_acres"])

print(share.head(5).to_string(index=False))
print()
print("columns shared:", list(share.columns))
print("pids unique:", share["pid"].is_unique, " rows:", len(share))'''


def py(key):
    return {"t": "code", "lang": "py", "pkgs": "pandas", "code": C[key]}


SURVEY_SHEET = """sheet: survey
type                   name               label                                              relevant                    constraint              constraint_message              required  choice_filter
select_one state       state              State                                                                                                                               yes
select_one district    district           District                                                                                                                            yes       state=${state}
select_one area        area               Is this household rural or urban?                                                                                                   yes
integer                hh_size            How many people usually live in this household?                                 . >= 1 and . <= 30      Enter a number from 1 to 30     yes
decimal                land_acres         How many acres of land does the household own?    ${area} = 'rural'           . >= 0 and . <= 100     Enter 0 to 100 acres            yes
select_one yes_no      has_bank_account   Does anyone in the household have a bank account?                                                                                   yes
select_one yes_no      received_transfer  Did the household receive a cash transfer in the last 12 months?                                                                    yes
integer                transfer_amount    How much did the household receive in total (Rs)? ${received_transfer} = 'yes'  . > 0               Enter an amount above zero      yes"""

CHOICES_SHEET = """sheet: choices
list_name   name        label       state
state       bihar       Bihar
state       kerala      Kerala
district    gaya        Gaya        bihar
district    purnia      Purnia      bihar
district    kozhikode   Kozhikode   kerala
district    wayanad     Wayanad     kerala
area        rural       Rural
area        urban       Urban
yes_no      yes         Yes
yes_no      no          No"""

SETTINGS_SHEET = """sheet: settings
form_title                      form_id            version       instance_name
Household baseline 2026         hh_baseline_2026   2026100601    concat(${district}, '-', ${hh_size})"""

REPEAT_SHEET = """sheet: survey (a household roster)
type               name           label                               repeat_count   relevant               constraint
integer            hh_size        How many people usually live here?                                        . >= 1 and . <= 30
begin repeat       member         Household member                    ${hh_size}
text               member_name    First name of this member
integer            age            Age in completed years                                                    . >= 0 and . <= 110
select_one yes_no  in_school      Is this member attending school?                   ${age} >= 5 and ${age} <= 17
end repeat"""

CALC_SHEET = """sheet: survey
type          name          label                                         calculation
integer       hh_size       How many people usually live here?
integer       monthly_exp   Total household spending last month (Rs)?
calculate     pc_exp                                                      ${monthly_exp} div ${hh_size}
note          pc_note       Spending per person: ${pc_exp} rupees. Is that right?"""

LANG_SHEET = """sheet: survey
type                 name          label::English (en)                               label::Hindi (hi)
integer              hh_size       How many people usually live in this household?   इस परिवार में आमतौर पर कितने लोग रहते हैं?
select_one yes_no    has_bank      Does anyone in the household have a bank account? क्या परिवार में किसी का बैंक खाता है?

sheet: choices
list_name   name   label::English (en)   label::Hindi (hi)
yes_no      yes    Yes                   हाँ
yes_no      no     No                    नहीं

sheet: settings
form_title                form_id            version       default_language
Household baseline 2026   hh_baseline_2026   2026100601    Hindi (hi)"""

ENCRYPT_SHEET = """sheet: settings
form_title                form_id            version      submission_url                             public_key
Household baseline 2026   hh_baseline_2026   2026100602   https://kc.kobotoolbox.org/submission      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA... (your whole key on one line)"""

OPENSSL = """# From the ODK documentation on encrypted forms. Run in a terminal (macOS, Linux)
# or after installing OpenSSL on Windows.
openssl genpkey -out MyPrivateKey.pem -outform PEM -algorithm RSA -pkeyopt rsa_keygen_bits:2048
openssl rsa -in MyPrivateKey.pem -pubout -out MyPublicKey.pem
# Paste the text of MyPublicKey.pem, without the BEGIN and END lines and without line breaks,
# into the public_key column. Keep MyPrivateKey.pem off shared drives and out of email."""

PAGE = {
    "slug": "kobo-odk",
    "order": 16,
    "kind": "guide",
    "tool": "KoboToolbox and ODK",
    "title": "KoboToolbox and ODK: Building Survey Forms with XLSForm",
    "h1": "KoboToolbox and ODK: building survey forms with XLSForm",
    "lede": ("Write a household survey once, as a spreadsheet, and run it on Android phones with no network: "
             "skip logic, range checks, Hindi and English labels, a household roster. KoboToolbox and ODK both "
             "read the same XLSForm standard. Python cells on this page check a form for common mistakes and "
             "check a downloaded dataset against the form's rules."),
    "description": ("A free guided course in KoboToolbox, ODK Collect and ODK Central for development "
                    "practitioners in South Asia: the XLSForm survey, choices and settings sheets, skip logic, "
                    "constraints, cascading selects, repeat groups, Hindi labels, offline collection, data "
                    "download, encryption, the DPDP Act 2023, and pilot testing."),
    "card": "XLSForm from the ground up: skip logic, constraints, Hindi labels, rosters, offline collection and encryption.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>KoboToolbox and ODK do not run on this page.</strong> You build forms in a "
                    "spreadsheet, upload them to a server and collect on a phone. The grey boxes are XLSForm "
                    "sheets for you to type into Excel or Google Sheets, laid out in columns as they would appear "
                    "there. This page shows no screenshots of either tool, because it cannot produce them. The "
                    "Python cells check a form definition and a downloaded file, and run here. The first Python "
                    "run downloads the engine once (about 10&nbsp;MB)."),
    "modules": [
        {"tab": "Tools",
         "title": "KoboToolbox, ODK Collect and ODK Central",
         "blocks": [
             {"t": "p", "html": "Most household surveys in South Asian programmes are now collected on Android "
                                "phones. Two families of free tools dominate, and they are closely related."},
             {"t": "ul", "items": [
                 "<strong>ODK</strong> is open source software. " + link("https://docs.getodk.org/getting-started/",
                 "Its documentation") + " describes three parts: <strong>ODK Collect</strong>, an Android app that "
                 "fills forms offline and sends them when a connection is found; <strong>ODK Central</strong>, the "
                 "server where you upload forms, manage users and download submissions; and <strong>Web "
                 "Forms</strong>, for filling a form in a browser. The Collect source code is published under the "
                 "Apache License 2.0.",
                 "<strong>KoboToolbox</strong> is a hosted service run by Kobo, a nonprofit. Its own Android app, "
                 "<strong>KoboCollect</strong>, is described in the " + link(
                     "https://support.kobotoolbox.org/glossary.html", "KoboToolbox glossary") + " as the app "
                 "\"used for mobile data collection, allowing enumerators to download forms, complete them "
                 "offline, and submit data when connected\". KoboToolbox also has a point-and-click Formbuilder.",
                 "<strong>XLSForm</strong> is the shared language. The " + link("https://xlsform.org/en/",
                 "XLSForm reference") + " defines a form as an Excel workbook with a survey sheet, a choices "
                 "sheet and a settings sheet. KoboToolbox and ODK Central both accept the same file, so a form you "
                 "write here works on either.",
             ]},
             {"t": "h3", "html": "What it costs, checked 6 October 2026"},
             {"t": "ul", "items": [
                 "<strong>KoboToolbox Community plan: free</strong> for organisations in its Nonprofit category, "
                 "which the " + link("https://www.kobotoolbox.org/pricing/", "pricing page") + " says \"includes "
                 "nonprofits, government agencies, UN organizations, and educational institutions\". It allows "
                 "5,000 submissions a month and 1 GB of file storage, with unlimited projects and data collectors. "
                 "Private companies, for-profit organisations and personal use fall in the Other category, where "
                 "the same plan is listed at US$99 a month (US$88 a month billed yearly) and a smaller Starter "
                 "plan at US$25 a month.",
                 "<strong>ODK</strong>: the " + link("https://getodk.org/", "ODK home page") + " says \"ODK is "
                 "open-source software. If you're technical, you can self-host and self-support it for free.\" "
                 "Its paid hosting, ODK Cloud, lists a Standard plan at US$199 a month (the figure shown with "
                 "yearly billing; the page says paying yearly saves up to 20%) with 10,000 submissions a month, and "
                 "says data can be stored in the US, the EU or India.",
             ]},
             {"t": "h3", "html": "Which KoboToolbox server"},
             {"t": "p", "html": "KoboToolbox runs two public servers with the same features. The " + link(
                 "https://support.kobotoolbox.org/creating_account.html", "account guide") + " (updated 3 October "
                 "2026) calls the <strong>Global server</strong> (" + IC("kf.kobotoolbox.org") + ") the one "
                 "\"used by most KoboToolbox users\"; the glossary says it is hosted in the United States. The "
                 "<strong>European Union server</strong> (" + IC("eu.kobotoolbox.org") + ") is \"hosted in "
                 "Ireland\". Projects cannot be moved between them, so choose before you build."},
             {"t": "info", "html": "<strong>The \"humanitarian server\".</strong> Older manuals and trainers refer "
                                   "to " + IC("kobo.humanitarianresponse.info") + ", the KoboToolbox server owned "
                                   "by UN OCHA. Kobo " + link(
                                       "https://community.kobotoolbox.org/t/transfer-of-the-former-ocha-server-to-kobo/44668",
                                       "announced on 1 September 2023") + " that it had taken full responsibility "
                                   "for that server, which became the European Union server at "
                                   + IC("eu.kobotoolbox.org") + ". The old addresses forwarded until 29 February "
                                   "2024. If an old form or phone still points at a humanitarianresponse.info "
                                   "address, change it to the EU server's addresses."},
             {"t": "info", "html": "<strong>Exercise.</strong> Before you open an account, write down three "
                                   "things for your project: whether your organisation is a nonprofit, government "
                                   "agency or university (which decides the free plan); roughly how many "
                                   "submissions a month you expect at peak; and whether your donor or ethics "
                                   "committee says where the data must be stored (which decides the server)."},
         ]},
        {"tab": "XLSForm",
         "title": "The three sheets of an XLSForm",
         "blocks": [
             {"t": "p", "html": "An XLSForm is an ordinary .xlsx workbook. Each row of the <strong>survey</strong> "
                                "sheet is one question; each row of the <strong>choices</strong> sheet is one answer "
                                "option; the <strong>settings</strong> sheet names and versions the form. "
                                "Formatting, colours and column order are ignored, so you can shade and freeze "
                                "rows to make the sheet readable."},
             {"t": "h3", "html": "The survey sheet"},
             {"t": "p", "html": "Three columns are required: " + IC("type") + ", " + IC("name") + " and "
                                + IC("label") + ". The grey box shows the form this course uses. Each column "
                                "below is explained in the next module."},
             {"t": "syntax", "label": "XLSForm: survey sheet", "code": SURVEY_SHEET},
             {"t": "ul", "items": [
                 IC("type") + ": " + IC("integer") + ", " + IC("decimal") + ", " + IC("text") + ", "
                 + IC("date") + ", " + IC("geopoint") + ", " + IC("note") + " (shows text, takes no answer), "
                 + IC("select_one listname") + " and " + IC("select_multiple listname") + ".",
                 IC("name") + ": the variable name in your data. The XLSForm reference says names must be "
                 "unique, must start with a letter or the " + IC("_") + " character, may contain only letters, "
                 "digits, hyphens, " + IC("_") + " and periods, and are case-sensitive.",
                 IC("label") + ": the question exactly as the enumerator reads it. " + IC("hint") + " adds "
                 "smaller guidance text under it.",
             ]},
             {"t": "h3", "html": "The choices sheet"},
             {"t": "p", "html": "Three required columns: " + IC("list_name") + ", " + IC("name") + " and "
                                + IC("label") + ". The word after " + IC("select_one") + " in the survey sheet "
                                "must match a " + IC("list_name") + " exactly. The " + IC("name") + " column is "
                                "what is saved in the data, so keep it short, lower case and free of spaces; the "
                                "reference warns that choice names for " + IC("select_multiple") + " must not "
                                "contain spaces, because a space separates the selected answers."},
             {"t": "syntax", "label": "XLSForm: choices sheet", "code": CHOICES_SHEET},
             {"t": "h3", "html": "The settings sheet"},
             {"t": "p", "html": "Optional, but the reference recommends " + IC("form_title") + ", "
                                + IC("form_id") + " and " + IC("version") + " at minimum. A common convention "
                                "for " + IC("version") + " is " + IC("yyyymmddrr") + ": " + IC("2026100601") +
                                " is the first revision of 6 October 2026. Change it every time you change the "
                                "form, so you can tell which version produced each submission. "
                                + IC("instance_name") + " builds a readable name for each submission from its "
                                "answers."},
             {"t": "syntax", "label": "XLSForm: settings sheet", "code": SETTINGS_SHEET},
             {"t": "h3", "html": "Check a form before you upload it"},
             {"t": "p", "html": "The cell below holds the same survey and choices sheets as CSV text and checks "
                                "four mistakes that are easy to make by hand: duplicate or invalid names, a "
                                "select pointing at a list that does not exist, a " + IC("${name}") + " that "
                                "refers to a question not yet asked, and a skip rule comparing a select with a "
                                "choice name it does not have."},
             py("lint"),
             {"t": "p", "html": "The form has 8 questions, 10 choices in 4 lists, and the check reports no "
                                "problems."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the survey text, change "
                                   + IC("${area} = 'rural'") + " to " + IC("${area} = 'Rural'") + " and run "
                                   "again. The check reports that " + IC("area") + "'s choices are "
                                   + IC("['rural', 'urban']") + ". The capital R is the label; the data holds the "
                                   "name. This mistake hides a question from every enumerator and raises no error "
                                   "on the phone. Then change " + IC("hh_size") + " in the first column of its row "
                                   "to " + IC("hh size") + " and see what the name check says."},
         ]},
        {"tab": "Logic",
         "title": "Skip logic, constraints and calculations",
         "blocks": [
             {"t": "p", "html": "These columns are where a form stops entry errors before they reach your data. "
                                "Every expression refers to an earlier answer as " + IC("${name}") + "."},
             {"t": "ul", "items": [
                 IC("relevant") + ": show the question only when the expression is true. "
                 + IC("${area} = 'rural'") + " asks about land only in rural households.",
                 IC("constraint") + ": reject an answer unless the expression is true. The dot stands for the "
                 "answer being entered: " + IC(". >= 1 and . <= 30") + ".",
                 IC("constraint_message") + ": what the enumerator sees when the constraint fails. Write it as "
                 "an instruction (\"Enter a number from 1 to 30\").",
                 IC("required") + ": " + IC("yes") + " stops the enumerator moving on without an answer. "
                 + IC("required_message") + " customises the warning.",
                 IC("choice_filter") + ": narrows a choice list using an earlier answer. Add a column (here "
                 + IC("state") + ") to the choices sheet, then " + IC("state=${state}") + " on the district "
                 "question shows only districts of the chosen state. The XLSForm reference calls these "
                 "cascading selects.",
                 IC("calculation") + ", with type " + IC("calculate") + ": computes a value from earlier "
                 "answers. The reference notes that a calculation with no label and no hint is hidden.",
             ]},
             {"t": "syntax", "label": "XLSForm: a calculation shown back to the enumerator", "code": CALC_SHEET},
             {"t": "p", "html": "Showing a derived figure in a " + IC("note") + " is one of the cheapest checks "
                                "you can add: an enumerator who sees \"Spending per person: 23 rupees\" knows "
                                "something was typed wrong. In ODK expressions, " + IC("div") + " is division."},
             {"t": "h3", "html": "Repeat groups: one set of questions per household member"},
             {"t": "p", "html": "Wrap questions between " + IC("begin repeat") + " and " + IC("end repeat") +
                                " rows to ask them once per member, plot or child. " + IC("repeat_count") + " "
                                "fixes the number of repeats; the XLSForm reference shows it set from an earlier "
                                "answer, so the roster opens exactly " + IC("${hh_size}") + " times. "
                                + IC("begin group") + " and " + IC("end group") + " group questions on one "
                                "screen without repeating them."},
             {"t": "syntax", "label": "XLSForm: a household roster", "code": REPEAT_SHEET},
             {"t": "info", "tone": "warning",
              "html": "<strong>A roster is a second table.</strong> When you download data from a form with a "
                      "repeat, the members arrive in their own table, linked to the household. KoboToolbox's "
                      "export guide recommends the XLS format when collecting repeat group data, because the "
                      "repeat goes to its own sheet. Plan the analysis join before fieldwork."},
             {"t": "h3", "html": "Run the same rules on the data you download"},
             {"t": "p", "html": "Constraints catch errors at entry, but not every error: a form version without "
                                "the constraint, an answer edited on the server, a submission sent twice. The "
                                "cell applies the form's rules to " + DL + " (illustrative data, invented for "
                                "teaching: 240 households in ten real district names, with made-up answers). "
                                "It then plants five entry errors and one duplicate submission in a practice "
                                "copy and runs the same check."},
             py("constraints"),
             {"t": "p", "html": "The original file has 240 rows and 0 problems. The practice copy has 241 rows "
                                "and 7 problems: the two out-of-range household sizes, the negative land, the "
                                "urban household reporting land, the " + IC("Y") + " that should be "
                                + IC("Yes") + ", and household 200 listed twice (one row per copy)."},
             {"t": "info", "html": "<strong>Exercise.</strong> Add a rule that flags "
                                   + IC("monthly_pc_exp") + " above Rs 15,000 as \"check with the enumerator\". "
                                   "Write it as " + IC('"pc_exp above 15000": df["monthly_pc_exp"] > 15000,') +
                                   " inside " + IC("rules") + " and run again. A flag to check is different from "
                                   "an error: a large value can be true. Look at how many households it flags in "
                                   "the original file before you decide on the cut-off."},
         ]},
        {"tab": "Languages",
         "title": "Hindi and English in one form",
         "blocks": [
             {"t": "p", "html": "One form can carry every language your enumerators use. The XLSForm reference "
                                "names each language column " + IC("label::language (code)") + ". The " + link(
                                    "https://docs.getodk.org/form-language/", "ODK form language guide") + " "
                                "explains: \"Each language column adds two colons and the language name, followed "
                                "by the two letter language code in parentheses\", for example "
                                + IC("label::English (en)") + ". For Hindi the code is " + IC("hi") + ", so the "
                                "column is " + IC("label::Hindi (hi)") + "; Bengali is " + IC("bn") + ", Tamil "
                                + IC("ta") + ", Telugu " + IC("te") + ", Marathi " + IC("mr") + ", Urdu "
                                + IC("ur") + "."},
             {"t": "syntax", "label": "XLSForm: two languages", "code": LANG_SHEET},
             {"t": "ul", "items": [
                 "The same suffix works on " + IC("hint") + ", " + IC("constraint_message") + ", "
                 + IC("required_message") + " and media columns, and on the choices sheet's " + IC("label") + ".",
                 IC("default_language") + " on the settings sheet sets the language the form opens in. Without "
                 "it, the ODK guide says the form opens in the first language defined.",
                 "<strong>There is no fallback language.</strong> The ODK guide warns that if a column has "
                 "language versions, a plain " + IC("label") + " column is treated as a separate language and "
                 "listed as <em>Default</em> in the language menu. Translate every column or none.",
                 "In KoboToolbox, " + IC("form_title") + " cannot take a language suffix; the " + link(
                     "https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html", "XLSForm guide") + " says "
                 "translating it produces an error.",
             ]},
             {"t": "p", "html": "A translation added by hand is easy to leave half-finished: someone adds a "
                                "question in English during the pilot and forgets the Hindi. The cell finds "
                                "every row with English text and no Hindi."},
             py("lang"),
             {"t": "p", "html": "It reports one gap: the " + IC("shg_member") + " question has an English label "
                                "and no Hindi. The " + IC("hh_size") + " row passes because both its label and "
                                "its constraint message are translated."},
             {"t": "info", "html": "<strong>Exercise.</strong> Fill in a Hindi label for "
                                   + IC("shg_member") + " (between the two commas after the English text) and "
                                   "run again. Then rename the column " + IC("label::Hindi (hi)") + " in the "
                                   "choices text to " + IC("label::Hindi") + " and see what the check says. Have "
                                   "a fluent speaker who did not write the translation read every label aloud "
                                   "during the pilot; a check like this one finds missing text and cannot judge "
                                   "whether the Hindi is right."},
         ]},
        {"tab": "Collect",
         "title": "Deploy, collect offline and download",
         "blocks": [
             {"t": "h3", "html": "Upload and deploy in KoboToolbox"},
             {"t": "steps", "items": [
                 "On the Projects page, select <strong>NEW</strong>, then <strong>Upload an XLSForm</strong>, "
                 "and choose your .xlsx file (from the " + link(
                     "https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html", "KoboToolbox XLSForm "
                     "guide") + ", updated 28 August 2026).",
                 "Enter the project details and click <strong>Create project</strong>.",
                 "Click <strong>Preview</strong> and fill the form yourself, trying wrong answers on purpose to see "
                 "each constraint message.",
                 "Deploy the form. To change it later, open the <strong>FORM</strong> page, click "
                 "<strong>Replace form</strong>, upload the new .xlsx and redeploy. Raise " + IC("version") +
                 " first.",
             ]},
             {"t": "h3", "html": "Set up phones"},
             {"t": "steps", "items": [
                 "Install KoboCollect from the Google Play Store. The " + link(
                     "https://support.kobotoolbox.org/kobocollect_on_android_latest.html", "setup guide") + " "
                 "(updated 23 April 2026) says newer versions require Android 8.0 or higher; older phones can "
                 "install the last version that supports them.",
                 "Enter the server URL, which differs from the login address: " + IC("https://kc.kobotoolbox.org/")
                 + " for the Global server and " + IC("https://kc-eu.kobotoolbox.org/") + " for the EU server. "
                 "The project's FORM tab also shows it under <em>Collect data</em>.",
                 "Enter the enumerator's username and password. Once one phone is set up, its QR code configures "
                 "the rest of the team's phones with the same settings.",
                 "Select <strong>Download form</strong> and tick the form. ODK Collect uses the same menu; it is "
                 "on " + link("https://play.google.com/store/apps/details?id=org.odk.collect.android",
                              "Google Play") + " too.",
             ]},
             {"t": "h3", "html": "Collecting with no network"},
             {"t": "p", "html": "Once the blank form is on the phone, no connection is needed to fill it. The " + link(
                 "https://docs.getodk.org/collect-forms/", "ODK Collect guide") + " explains the cycle: a form "
                 "saved part-way is a draft; tapping <strong>Finalize</strong> at the end locks it; finalized "
                 "forms wait in <strong>Ready to send</strong> until the phone is online, then go to the server. "
                 "Ask enumerators to sync every evening they have signal, so a lost phone loses one day's work at "
                 "most."},
             {"t": "h3", "html": "Download the data"},
             {"t": "steps", "items": [
                 "Open the project and go to <strong>DATA &gt; Downloads</strong> (" + link(
                     "https://support.kobotoolbox.org/export_download.html", "export guide") + ", updated 6 May "
                 "2026).",
                 "Choose the type: XLS (recommended when the form has repeats), CSV, SPSS Labels, GeoJSON, GPS "
                 "coordinates (KML) or media attachments (ZIP).",
                 "Choose the value and header format. <strong>Labels</strong> is the default: question text as "
                 "headers and choice labels as values. <strong>XML values and headers</strong> gives the "
                 + IC("name") + " columns and choice names. Pick XML values for analysis: question text makes poor "
                 "column names, and labels change between languages.",
                 "Click <strong>EXPORT</strong>, then <strong>DOWNLOAD</strong> when the file appears in the list.",
             ]},
             {"t": "h3", "html": "A daily check by field team"},
             {"t": "p", "html": "During fieldwork, download every day and compare teams. Large differences between "
                                "teams working in similar areas are often a training problem. The cell joins "
                                + DL + " to districts.csv (both invented for teaching) to get each household's "
                                "field team."},
             py("daily"),
             {"t": "p", "html": "All 240 rows join, with no unmatched districts. Team A covers four districts "
                                "and 96 interviews; Teams B and C cover three districts and 72 interviews each. "
                                "Read the three percentages side by side: here the bank account share runs from "
                                "84.4% to 88.9% across teams and the transfer share from 33.3% to 41.7%. In "
                                "real fieldwork, a gap far wider than this deserves a phone call to the "
                                "supervisor."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change " + IC('groupby("field_team")') + " to "
                                   + IC('groupby(["field_team", "area"])') + " and run again. Teams cover "
                                   "different mixes of rural and urban households, and a difference that "
                                   "disappears within area was a difference in where they worked."},
         ]},
        {"tab": "Protection",
         "title": "Data protection: encryption, access and the DPDP Act",
         "blocks": [
             {"t": "p", "html": "A household survey holds names, phone numbers, locations, caste and income. Three "
                                "layers protect it: who can see submissions, whether the server can read them, and "
                                "what the law requires of you."},
             {"t": "h3", "html": "Who can see submissions"},
             {"t": "p", "html": "In KoboToolbox, open the project's <strong>SETTINGS</strong> page and select "
                                "<strong>Sharing</strong>. The " + link(
                                    "https://support.kobotoolbox.org/managing_permissions.html", "permissions guide")
                                + " lists separate permissions to view the form, edit the form, view, add, edit, "
                                "validate and delete submissions, and manage the project. Enumerators need "
                                "<em>Add submissions</em> only. Permissions can also be limited by row, so a "
                                "district coordinator sees only submissions from their own enumerators."},
             {"t": "h3", "html": "Encrypted forms"},
             {"t": "p", "html": "The XLSForm reference says encryption keeps finalized records private while they "
                                "are \"stored on the device and server as well as during transport\", and that encrypted records "
                                "\"are completely inaccessible to anyone not possessing the private key\". You "
                                "make a key pair, put the public key in the form and keep the private key."},
             {"t": "syntax", "label": "Terminal: make a key pair (OpenSSL)", "code": OPENSSL},
             {"t": "syntax", "label": "XLSForm: settings sheet for an encrypted KoboToolbox form", "code": ENCRYPT_SHEET},
             {"t": "ul", "items": [
                 "KoboToolbox's " + link("https://support.kobotoolbox.org/encrypting_forms.html",
                                         "encryption guide") + " (updated 22 July 2026) gives "
                 + IC("https://kc.kobotoolbox.org/submission") + " as the " + IC("submission_url") + " for "
                 "the Global server and the kc-eu address for the EU server.",
                 "After deployment, anything that reads the data inside KoboToolbox stops working, including "
                 "the map view and exports. You download and decrypt on your own computer with ODK Briefcase "
                 "and the private key.",
                 "ODK Central can manage encryption for a project; the " + link(
                     "https://docs.getodk.org/encrypted-forms/", "ODK encryption guide") + " says Central's "
                 "managed option lets you download a decrypted file without another tool.",
                 "Lose the private key and the data is gone. Keep two copies, offline, with named custodians.",
             ]},
             {"t": "h3", "html": "The DPDP Act 2023"},
             {"t": "p", "html": "India's " + link(
                 "https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf",
                 "Digital Personal Data Protection Act, 2023") + " (published 11 August 2023) applies to "
                                "digital personal data, and a phone survey is digital from the first answer. The "
                                "organisation that decides why and how the data is processed is the Data "
                                "Fiduciary; the respondent is the Data Principal. The duties below, the "
                                "exemption and the penalties apply from 13 May 2027 (notification G.S.R. "
                                "843(E), 13 November 2025), so design forms to them now. Sections that "
                                "matter for a survey:"},
             {"t": "ul", "items": [
                 "<strong>Section 5</strong>: a request for consent must come with or after a notice telling the "
                 "respondent what personal data is collected and why, and how to exercise their rights.",
                 "<strong>Section 6(1)</strong>: consent must be \"free, specific, informed, unconditional and "
                 "unambiguous with a clear affirmative action\", limited to the data necessary for the stated "
                 "purpose. Put the notice and a consent question at the start of the form and end the form if "
                 "the answer is no (a " + IC("relevant") + " on every later group does this).",
                 "<strong>Section 8(5)</strong>: the Data Fiduciary must take \"reasonable security safeguards to "
                 "prevent personal data breach\", including for processing done on its behalf by a Data "
                 "Processor such as a survey firm or a hosting service. The Schedule to the Act sets a penalty "
                 "for breaching this duty that may extend to Rs 250 crore.",
                 "<strong>Section 17(2)(b)</strong>: the Act's provisions do not apply to processing "
                 "\"necessary for research, archiving or statistical purposes if the personal data is not to be "
                 "used to take any decision specific to a Data Principal and such processing is carried on in "
                 "accordance with such standards as may be prescribed\".",
             ]},
             {"t": "info", "tone": "warning",
              "html": "<strong>The research exemption has conditions.</strong> The " + link(
                  "https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf",
                  "DPDP Rules, 2025") + " (G.S.R. 846(E), 13 November 2025) set those standards in rule 16 and "
                      "the Second Schedule: processing must be lawful, limited to the data necessary, made "
                      "reasonably accurate, kept only as long as needed, protected by reasonable security "
                      "safeguards, and someone must be accountable for it. Rule 1(4) says rules 3 and 5 to 16 come "
                      "into force eighteen months after publication. A baseline used to select beneficiaries is a "
                      "decision specific to a person and falls outside the exemption. Ask your organisation's "
                      "data protection lead, and see the " + link("/101-courses/data-protection-dpdp.html",
                                                                  "Data Protection and the DPDP Act deck") + "."},
             {"t": "h3", "html": "Share a file without identities"},
             {"t": "p", "html": "Before you share data with an analyst, replace the identifier with a code only the "
                                "data manager can reverse, and coarsen exact values that could identify a "
                                "household. The cell does both on " + DL + " (invented data) with a keyed hash."},
             py("pseudo"),
             {"t": "p", "html": "The shared file keeps all 240 rows with a 10-character " + IC("pid") + " in "
                                "place of " + IC("hh_id") + ", every pid is unique, and land is reported in four "
                                "bands. The key table linking pid to hh_id stays with the data manager."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change one character of " + IC("KEY") + " and run "
                                   "again: every pid changes. That is why the key must be kept, and kept apart "
                                   "from the data. A keyed code makes the file pseudonymous; a village name, a "
                                   "household size and a caste together can still point to one family, so check "
                                   "small groups before you publish anything."},
         ]},
        {"tab": "Pilot",
         "title": "Pilot testing a form",
         "blocks": [
             {"t": "p", "html": "Every form has errors that only show up when a real enumerator asks a real "
                                "respondent. A pilot finds them while they are still cheap to fix."},
             {"t": "steps", "items": [
                 "<strong>Desk test.</strong> Fill the form yourself in Preview, once with ordinary answers and "
                 "once trying to break every constraint. Check that each skip opens and closes when it should.",
                 "<strong>Phone test.</strong> Install the form on the cheapest phone your team will use, switch "
                 "on airplane mode, fill five forms, then sync. This tests offline storage, the screen size and "
                 "the Hindi font on that phone.",
                 "<strong>Field pilot.</strong> Interview 15 to 30 households outside the sample, in each "
                 "language. Note every question respondents ask to have repeated, and every answer that did not "
                 "fit the choices.",
                 "<strong>Check the data.</strong> Download the pilot submissions as XML values and run your "
                 "checks (module 3) on them. A constraint that never fires may be too loose; one that fires "
                 "often may be wrong, or the question may be unclear.",
                 "<strong>Fix and version.</strong> Change the form, raise " + IC("version") + ", replace the "
                 "form, delete the pilot submissions or mark them, and record each change and its reason in a "
                 "change log.",
             ]},
             {"t": "h3", "html": "What to look for in pilot data"},
             {"t": "ul", "items": [
                 "Many answers of \"other\": the choice list is missing a common answer.",
                 "Answers piling up at the edge of a constraint (exactly 30 members, exactly 100 acres): the "
                 "limit is probably wrong or enumerators are using it to get past the screen.",
                 "A question skipped far more or less often than you expected: check the " + IC("relevant") +
                 " expression and the choice names it compares.",
                 "Interview length by enumerator: the XLSForm metadata types " + IC("start") + " and " + IC("end")
                 + " record the start and end date and time of the survey; add them as rows in the survey sheet "
                 "if your form does not have them.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> Take the survey sheet from module 2 and add three "
                                   "rows at the top: " + IC("start") + ", " + IC("end") + " and a consent "
                                   "question " + IC("select_one yes_no") + " named " + IC("consent") + ". Wrap "
                                   "the rest of the form in " + IC("begin group") + " and " + IC("end group") +
                                   " rows with " + IC("${consent} = 'yes'") + " in the group's "
                                   + IC("relevant") + ". Upload it to KoboToolbox and test that answering no ends "
                                   "the interview."},
         ]},
    ],
    "next": [
        {"href": "/code/spreadsheets.html", "title": "Spreadsheets for M&amp;E",
         "desc": "Build indicator tables from the data you downloaded."},
        {"href": "/code/pandas.html", "title": "pandas for development data",
         "desc": "Clean, check and summarise survey exports in Python."},
        {"href": "/code/openrefine.html", "title": "OpenRefine",
         "desc": "Fix district and village names typed five different ways."},
        {"href": "/101-courses/survey-design.html", "title": "Survey Design 101",
         "desc": "Questions, sampling and piloting before you build the form."},
        {"href": "/101-courses/data-protection-dpdp.html", "title": "Data Protection and the DPDP Act",
         "desc": "What the law asks of you when you collect personal data."},
    ],
}

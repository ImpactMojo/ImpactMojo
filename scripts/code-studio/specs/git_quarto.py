# -*- coding: utf-8 -*-
"""Git and Quarto: Reproducible Reports. A guided tool course in version control and Quarto documents, with
Python and R cells that run the steps that can run in a browser.

Facts checked on 6 October 2026 against git-scm.com (downloads, install pages, reference manual, Pro Git),
docs.github.com, quarto.org (download, computations, parameters, PDF, Word, licence) and the quarto-cli source
for the render command's flags. Sources are listed in the agent report.
"""

A = 'style="color:var(--accent-color)"'


def link(href, text):
    return '<a href="%s" rel="noopener" target="_blank" %s>%s</a>' % (href, A, text)


def IC(s):
    return '<code class="inline">%s</code>' % s


DL = '<a href="/code/data/households.csv" download %s>households.csv</a>' % A

C = {}
C["diff"] = '''import difflib

before = """district,households,pct_toilet,mean_pc_exp
Barmer,24,75.0,2745
Purnia,24,75.0,2395
Rewa,24,50.0,2557
""".splitlines(keepends=True)

# The same table after a cleaning fix changed one household's answer in Purnia
after = """district,households,pct_toilet,mean_pc_exp
Barmer,24,75.0,2745
Purnia,24,79.2,2395
Rewa,24,50.0,2557
""".splitlines(keepends=True)

print("".join(difflib.unified_diff(before, after, "a/district_table.csv", "b/district_table.csv")))'''

C["ignore"] = '''from pathlib import Path
from fnmatch import fnmatch
import re

# Build a small practice project (all names and phone numbers are invented)
files = {
    "README.md": "District profiles, baseline 2026\\n",
    "analysis/profile.qmd": "---\\ntitle: District profile\\n---\\n",
    "data/raw/beneficiaries.csv": "hh_id,name,phone\\n1,Asha Devi,9876543210\\n2,Ramesh Kumar,8123456789\\n",
    "data/clean/households.csv": open("households.csv").read(),
    "outputs/purnia.html": "<html></html>",
    "notes/contacts.xlsx": "binary",
}
root = Path("project")
for name, text in files.items():
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)

gitignore = """
# personal data never goes into the repository
data/raw/
*.xlsx
# rendered outputs can be rebuilt from the code
outputs/
"""
patterns = [l.strip() for l in gitignore.splitlines() if l.strip() and not l.startswith("#")]

def ignored(rel):
    # A simplified version of Git's rules: "dir/" ignores a folder, "*.ext" ignores by name anywhere
    for pat in patterns:
        if pat.endswith("/") and (rel + "/").startswith(pat):
            return True
        if "/" not in pat and fnmatch(rel.split("/")[-1], pat):
            return True
    return False

phone = re.compile(r"(?<![0-9])[6-9][0-9]{9}(?![0-9])")   # a 10-digit Indian mobile number
for p in sorted(root.rglob("*")):
    if p.is_file():
        rel = p.relative_to(root).as_posix()
        status = "ignored " if ignored(rel) else "COMMIT  "
        hits = len(phone.findall(p.read_text(errors="ignore")))
        print(status, rel, f"  <- {hits} phone-like numbers" if hits else "")'''

R_PROFILE = '''params <- list(district = "Purnia")   # in a .qmd this comes from the YAML header

hh <- read.csv("households.csv")
d  <- read.csv("districts.csv")
g  <- hh[hh$district == params$district, ]
info <- d[d$district == params$district, ]

cat("District profile:", params$district, "(", info$state, ")\\n")
cat("Households surveyed:", nrow(g), "\\n")
cat("With a toilet:", round(100 * mean(g$has_toilet == "Yes"), 1), "%\\n")
cat("With a bank account:", round(100 * mean(g$has_bank_account == "Yes"), 1), "%\\n")
cat("Mean monthly spending per person: Rs", round(mean(g$monthly_pc_exp)), "\\n")
table(g$caste)'''

PY_PROFILE = '''import pandas as pd
district = "Purnia"   # in a .qmd this is the cell tagged parameters

hh = pd.read_csv("households.csv")
d = pd.read_csv("districts.csv")
g = hh[hh["district"] == district]
state = d.loc[d["district"] == district, "state"].iloc[0]

print(f"District profile: {district} ({state})")
print("Households surveyed:", len(g))
print("With a toilet:", round(100 * (g["has_toilet"] == "Yes").mean(), 1), "%")
print("With a bank account:", round(100 * (g["has_bank_account"] == "Yes").mean(), 1), "%")
print("Mean monthly spending per person: Rs", round(g["monthly_pc_exp"].mean()))
print(g["caste"].value_counts().sort_index())'''


def py(key):
    return {"t": "code", "lang": "py", "pkgs": "pandas", "code": C[key]}


SETUP = """# Tell Git who you are (once per computer). Use the name and email you want on your commits.
git config --global user.name "Asha Kumari"
git config --global user.email "asha@example.org"

# Name the first branch of every new repository "main"
git config --global init.defaultBranch main

# Check what Git has recorded
git config --list
git --version"""

LOOP = """cd district-profiles          # your project folder
git init                      # start a repository here (creates a hidden .git folder)
git status                    # what has changed since the last commit?

git add README.md analysis/profile.qmd     # stage these files for the next commit
git commit -m "Add district profile template"

# ...edit analysis/profile.qmd...
git diff                      # line-by-line changes not yet staged
git add analysis/profile.qmd
git commit -m "Report toilet coverage as a percentage"

git log --oneline             # one line per commit, newest first"""

BRANCH = """git branch                         # list branches; * marks the one you are on
git switch -c caste-tables         # create a branch and move to it
# ...edit, add, commit on the branch...
git switch main                    # back to main; the branch's work is set aside
git merge caste-tables             # bring the branch's commits into main
git branch -d caste-tables         # delete the branch once merged"""

REMOTE = """# Connect the folder to an empty private repository you created on GitHub
git remote add origin https://github.com/YOUR-ORG/district-profiles.git
git remote -v                       # check the address
git push -u origin main             # send main to GitHub; -u remembers the pairing

# Every working day
git pull                            # get colleagues' commits first
# ...work, add, commit...
git push                            # send your commits

# A colleague starting on a new laptop
git clone https://github.com/YOUR-ORG/district-profiles.git"""

GITIGNORE = """# .gitignore at the top of the repository

# Personal data never goes into the repository
data/raw/
*.xlsx
*.sav
*.dta

# Rendered output can be rebuilt from the code
outputs/
*_files/

# Credentials and local settings
.env
.Rhistory
.Rproj.user/"""

UNTRACK = """# A file was committed before it was listed in .gitignore.
# Stop tracking it (the file stays on your disk), then commit.
git rm --cached data/raw/beneficiaries.csv
git commit -m "Stop tracking raw beneficiary list"
# The file is still inside every earlier commit. If it was ever pushed,
# treat it as disclosed: tell your data protection lead."""

QMD_R = """---
title: "District profile"
author: "MEL team"
date: today
format:
  html:
    embed-resources: true
  docx: default
execute:
  echo: false
---

## Coverage

```{r}
#| label: load
hh <- read.csv("households.csv")
```

Households surveyed: `r nrow(hh)`.

```{r}
#| label: toilet-by-district
#| warning: false
round(100 * tapply(hh$has_toilet == "Yes", hh$district, mean), 1)
```"""

QMD_PY = """---
title: "District profile"
format: html
jupyter: python3
---

```{python}
#| echo: false
import pandas as pd
hh = pd.read_csv("households.csv")
print(len(hh), "households")
```"""

RENDER = """quarto preview profile.qmd               # render and open in a browser, re-rendering on save
quarto render profile.qmd --to html      # a single HTML file
quarto render profile.qmd --to docx      # a Word document
quarto render profile.qmd --to pdf       # a PDF (needs a TeX installation, below)

quarto install tinytex                   # the TeX distribution Quarto recommends for PDF"""

PARAMS_R = """---
title: "District profile: `r params$district`"
format: html
params:
  district: "Purnia"
---

```{r}
hh <- read.csv("households.csv")
g  <- hh[hh$district == params$district, ]
```

`r params$district` has `r nrow(g)` surveyed households."""

PARAMS_PY = """```{python}
#| tags: [parameters]
district = "Purnia"
```"""

PARAMS_RENDER = """# One district
quarto render profile.qmd -P district:Gaya --output gaya.html

# Every district, in a terminal (macOS, Linux, or Git Bash on Windows)
for d in Barmer Betul Gaya Indore Kozhikode Patna Purnia Rewa Udaipur Wayanad; do
  quarto render profile.qmd -P district:$d --output profile-$d.html
done"""

LAYOUT = """district-profiles/
  README.md              what this is, how to run it, who to ask
  .gitignore             data/raw/, outputs/, credentials
  data/
    raw/                 exports exactly as downloaded: never edited, never committed
    clean/               written only by the cleaning script
  scripts/
    01_clean.R           raw -> clean, with checks that stop on a problem
  analysis/
    profile.qmd          the parameterised report
  outputs/               rendered reports: rebuilt, never edited by hand"""

PAGE = {
    "slug": "git-quarto",
    "order": 18,
    "kind": "guide",
    "tool": "Git and Quarto",
    "title": "Git and Quarto: Reproducible Reports",
    "h1": "Git and Quarto: reproducible reports",
    "lede": ("Keep a record of every change to your analysis, share it with colleagues without emailing files, "
             "and turn one report template into ten district profiles with a single command. Git records "
             "versions; Quarto turns R or Python code and text into HTML, Word or PDF reports. Both are free. "
             "Cells on this page run the parts that can run in a browser."),
    "description": ("A free guided course in Git and Quarto for development practitioners in South Asia: install "
                    "Git, the init-add-commit-log-diff loop, branches, GitHub remotes, .gitignore and keeping "
                    "personal data out of repositories under the DPDP Act, Quarto documents with R or Python, "
                    "rendering to HTML, Word and PDF, parameterised district profiles, and a reproducible "
                    "project layout."),
    "card": "Commit, branch and push; keep personal data out of Git; render one Quarto template into ten district profiles.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>Git and Quarto run on your own computer, in a terminal.</strong> The grey boxes are "
                    "commands and files for you to type there; this page shows no terminal output from them, "
                    "because it cannot run them. Each module says what to look for. The code cells run the steps "
                    "a browser can: a diff, a check for personal data before a commit, and the calculation "
                    "inside a district profile. The first run downloads the engine once (R about 7&nbsp;MB, "
                    "Python about 10&nbsp;MB)."),
    "modules": [
        {"tab": "Why Git",
         "title": "Why version control, and installing Git",
         "blocks": [
             {"t": "p", "html": "A folder of " + IC("report_final.docx") + ", " + IC("report_final_v2.docx") + " "
                                "and " + IC("report_final_v2_AK_comments.docx") + " is a version control system "
                                "with no record of what changed, who changed it or why. Git keeps that record. "
                                "Each <em>commit</em> is a saved snapshot of the project with a message. You can "
                                "see the difference between any two snapshots, go back to one, and work on a "
                                "change without disturbing the version others rely on."},
             {"t": "p", "html": "Git suits text files: R and Python scripts, Quarto documents, CSV codebooks, "
                                "XLSForms saved as CSV. It stores Word and Excel files but cannot show what "
                                "changed inside them."},
             {"t": "info", "html": "<strong>Version and cost, checked 6 October 2026.</strong> The " + link(
                 "https://git-scm.com/", "Git home page") + " lists the latest source release as "
                                   "<strong>2.56.0</strong> (release notes dated 28 September 2026). Git is "
                                   "\"released under the GNU General Public License version 2.0\", so it costs "
                                   "nothing. The " + link("https://git-scm.com/install/windows",
                                                          "Windows download page") + " offers Git for Windows "
                                   "2.56.0(2), released 5 October 2026."},
             {"t": "h3", "html": "Install"},
             {"t": "ul", "items": [
                 "<strong>Windows</strong>: download the installer from the " + link(
                     "https://git-scm.com/install/windows", "Windows page") + ". The default choices are fine. It "
                 "adds <em>Git Bash</em>, a terminal where every command on this page works. A portable version "
                 "is offered for computers where you cannot install software.",
                 "<strong>macOS</strong>: the " + link("https://git-scm.com/install/mac", "macOS page") + " says "
                 "Apple ships Git with the Xcode Command Line Tools: run " + IC("xcode-select --install") + " in "
                 "Terminal. With Homebrew, " + IC("brew install git") + ".",
                 "<strong>Linux</strong>: Debian and Ubuntu, " + IC("sudo apt-get install git") + "; Fedora, "
                 + IC("sudo dnf install git") + " (" + link("https://git-scm.com/install/linux", "Linux page")
                 + ").",
             ]},
             {"t": "h3", "html": "First-time setup"},
             {"t": "p", "html": "These lines come from the " + link(
                 "https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup", "Pro Git book's setup "
                 "chapter") + ". Your name and email are written into every commit you make."},
             {"t": "syntax", "label": "Terminal: set up Git once", "code": SETUP},
             {"t": "info", "html": "<strong>Exercise.</strong> Run " + IC("git --version") + " after installing. "
                                   "It should print a version number starting with " + IC("git version") + ". If "
                                   "the terminal says the command is not found, close it, open a new one, and "
                                   "try again; on Windows, use Git Bash."},
         ]},
        {"tab": "The loop",
         "title": "The basic loop: init, add, commit, log, diff",
         "blocks": [
             {"t": "p", "html": "Almost all daily Git work is four commands: change files, " + IC("git add") +
                                " the ones you want in the snapshot, " + IC("git commit") + " with a message, "
                                "and look back with " + IC("git log") + " and " + IC("git diff") + "."},
             {"t": "syntax", "label": "Terminal: the basic loop", "code": LOOP},
             {"t": "ul", "items": [
                 IC("git init") + " creates an empty repository: the " + link(
                     "https://git-scm.com/docs/git-init", "manual") + " describes it as \"basically a .git "
                 "directory\". Run it once per project.",
                 IC("git status") + " is the command to run whenever you are unsure. It lists files that changed, "
                 "files staged for the next commit, and files Git is not tracking.",
                 IC("git add") + " stages a file. Only staged changes go into the next commit, so you can commit "
                 "one fix at a time.",
                 IC("git commit -m") + " saves the snapshot. Write the message as what the commit does: "
                 "\"Fix Purnia district code\", \"Add caste table\".",
                 IC("git diff") + " shows changed lines. " + IC("git log --oneline") + " lists commits with a "
                 "short ID you can refer to.",
             ]},
             {"t": "h3", "html": "Reading a diff"},
             {"t": "p", "html": "Git shows changes in the unified diff format: a line starting with " + IC("-") +
                                " was removed and a line starting with " + IC("+") + " was added, with unchanged "
                                "lines around them for context. Python's " + IC("difflib") + " writes the same "
                                "format, so the cell shows what " + IC("git diff") + " would report after a "
                                "cleaning fix changed one figure in a district table (figures from " + DL + ", "
                                "illustrative data invented for teaching)."},
             py("diff"),
             {"t": "p", "html": "The output names the old and new file, then shows the Purnia row twice: once "
                                "with " + IC("-") + " and 75.0, once with " + IC("+") + " and 79.2. Barmer and "
                                "Rewa appear unmarked, as context. This is why Git suits CSV tables and code: "
                                "a reviewer sees exactly which number moved."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the " + IC("after") + " text, also change "
                                   "Rewa's mean spending from 2557 to 2575, and run again. Both changes appear. "
                                   "Then add a new line for Gaya at the end of " + IC("after") + ": it appears "
                                   "with a " + IC("+") + " and no matching " + IC("-") + "."},
         ]},
        {"tab": "Branches",
         "title": "Branches: try a change without breaking main",
         "blocks": [
             {"t": "p", "html": "A branch is a separate line of commits. Keep " + IC("main") + " as the version "
                                "that works, and make a branch for anything that might not: a new table, a "
                                "different poverty line, a colleague's suggested rewrite."},
             {"t": "syntax", "label": "Terminal: branches", "code": BRANCH},
             {"t": "ul", "items": [
                 IC("git switch -c name") + " creates the branch and moves to it; the " + link(
                     "https://git-scm.com/docs/git-switch", "git switch manual") + " describes " + IC("-c") +
                 " as \"Create a new branch\" before switching to it. Older tutorials use "
                 + IC("git checkout -b") + " for the same thing.",
                 "Files in your folder change when you switch branches. Commit before switching.",
                 IC("git merge") + " brings the branch's commits into the branch you are on. If both changed the "
                 "same lines, Git stops and marks the conflict in the file for you to resolve, then you add and "
                 "commit.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> In a practice folder, commit a file with one line, "
                                   "create a branch, change the line and commit. Switch back to " + IC("main") +
                                   " and open the file: it shows the old line. Merge the branch and open it "
                                   "again. Run " + IC("git log --oneline") + " at each step to see where you "
                                   "are."},
         ]},
        {"tab": "GitHub",
         "title": "Remotes: GitHub, push and pull",
         "blocks": [
             {"t": "p", "html": "A remote is a copy of the repository on a server, which is how a team shares "
                                "work and how a laptop's work survives the laptop. GitHub is the most common "
                                "host. Its " + link(
                                    "https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories",
                                    "documentation") + " says a free account can own unlimited public and private "
                                "repositories, and that private repositories are only accessible to you and the "
                                "people you share them with."},
             {"t": "steps", "items": [
                 "On GitHub, create a new repository. Choose <strong>Private</strong>. Leave it empty (no README) "
                 "if your folder already has commits.",
                 "Copy its HTTPS address and add it as a remote called " + IC("origin") + ", as below.",
                 "Push. GitHub's " + link("https://docs.github.com/en/get-started/git-basics/about-remote-repositories",
                                          "remote repositories guide") + " says that when Git asks for your "
                 "password over HTTPS, you enter a <strong>personal access token</strong>, because password "
                 "authentication for Git has been removed. The same guide mentions Git Credential Manager as "
                 "an alternative that remembers your login.",
             ]},
             {"t": "syntax", "label": "Terminal: remotes", "code": REMOTE},
             {"t": "info", "html": "<strong>Pull before you push.</strong> If a colleague pushed first, your push "
                                   "is refused until you pull their commits. Pull at the start of each day and "
                                   "before each push, and conflicts stay small."},
             {"t": "info", "html": "<strong>Exercise.</strong> Create a private repository, push your practice "
                                   "folder, then edit README.md on the GitHub website and commit it there. Back "
                                   "on your computer, run " + IC("git pull") + " and open README.md: the website "
                                   "edit is now in your folder."},
         ]},
        {"tab": "Personal data",
         "title": ".gitignore and keeping personal data out",
         "blocks": [
             {"t": "p", "html": "Every file you commit stays in the repository's history, on every computer that "
                                "clones it and on the server. A beneficiary list with names and phone numbers "
                                "committed once is, for practical purposes, permanent. Under the " + link(
                                    "https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf",
                                    "DPDP Act 2023") + ", section 8(5), which applies from 13 May 2027, your organisation must take \"reasonable "
                                "security safeguards to prevent personal data breach\". A private repository is "
                                "access control, and it holds only as long as the access list stays right. Keep "
                                "personal data out of Git from the start."},
             {"t": "p", "html": "A " + IC(".gitignore") + " file lists files Git should not track. From the " + link(
                 "https://git-scm.com/docs/gitignore", "gitignore manual") + ": a line starting with " + IC("#") +
                                " is a comment; a pattern ending in " + IC("/") + " matches only directories; "
                                + IC("*") + " \"matches anything except a slash\"."},
             {"t": "syntax", "label": ".gitignore", "code": GITIGNORE},
             {"t": "p", "html": "The cell builds a small practice project with an invented beneficiary list, "
                                "applies a simplified version of these rules, and scans every file for strings "
                                "that look like Indian mobile numbers (ten digits starting with 6 to 9)."},
             py("ignore"),
             {"t": "p", "html": "Three files would be committed (README.md, the .qmd and the clean household "
                                "file) and three are ignored: the raw beneficiary list in " + IC("data/raw/") +
                                ", the Excel file, and the rendered output. The scan finds 2 phone-like numbers, "
                                "both in the ignored raw file."},
             {"t": "info", "html": "<strong>Exercise.</strong> Delete the " + IC("data/raw/") + " line from "
                                   + IC("gitignore") + " and run again. The beneficiary list is now marked "
                                   + IC("COMMIT") + " with its two numbers flagged. A check like this, run "
                                   "before every commit, catches the mistake while it is still on your laptop. "
                                   "The cell's matcher is simpler than Git's; on your computer, "
                                   + IC("git status --ignored") + " lists what Git itself ignores."},
             {"t": "h3", "html": "If personal data was already committed"},
             {"t": "p", "html": "The gitignore manual says files already tracked are not affected by "
                                ".gitignore, and points to " + IC("git rm --cached") + ", which removes a file "
                                "from the index while leaving it on disk (" + link(
                                    "https://git-scm.com/docs/git-rm", "git rm manual") + ")."},
             {"t": "syntax", "label": "Terminal: stop tracking a file", "code": UNTRACK},
             {"t": "info", "tone": "warning",
              "html": "<strong>Removing a file in a new commit does not remove it from history.</strong> Anyone "
                      "with a clone, or with access to the remote, can still check out the earlier commit. If the "
                      "file was pushed, report it to whoever handles data protection in your organisation, as a "
                      "possible breach, and get help to rewrite the history. From 13 May 2027, section 8(6) of the DPDP Act requires "
                      "a Data Fiduciary to inform the Data Protection Board and each affected person of a "
                      "personal data breach."},
         ]},
        {"tab": "Quarto",
         "title": "Quarto documents: text and code in one file",
         "blocks": [
             {"t": "p", "html": "A Quarto document (" + IC(".qmd") + ") is a plain text file: a YAML header between "
                                "two " + IC("---") + " lines, then text in Markdown and code chunks in R or "
                                "Python. Rendering runs the code and writes the results into the report, so the "
                                "numbers in the text always come from the data."},
             {"t": "info", "html": "<strong>Version and cost, checked 6 October 2026.</strong> The " + link(
                 "https://quarto.org/docs/download/", "Quarto download page") + "'s current release is "
                                   "<strong>1.10.19</strong>, published 6 October 2026. The " + link(
                                       "https://quarto.org/license.html", "licence page") + " says the Quarto "
                                   "command-line tool \"is licensed under the MIT License (version 1.4 and "
                                   "later)\". It is free. Installers are listed for Windows, macOS and Linux."},
             {"t": "ul", "items": [
                 "<strong>With R</strong>: install the rmarkdown package, " + IC('install.packages("rmarkdown")') +
                 ". The " + link("https://quarto.org/docs/computations/r.html", "Quarto R guide") + " says this "
                 "also installs knitr, which runs R chunks.",
                 "<strong>With Python</strong>: install Jupyter, " + IC("python3 -m pip install jupyter") + " "
                 "(on Windows, " + IC("py -m pip install jupyter") + "), from the " + link(
                     "https://quarto.org/docs/computations/python.html", "Quarto Python guide") + ".",
             ]},
             {"t": "syntax", "label": "profile.qmd (R)", "code": QMD_R},
             {"t": "ul", "items": [
                 "The YAML header sets the title and the output formats. " + IC("embed-resources: true") + " "
                 "makes a single HTML file with no separate folder, which is easier to email.",
                 "Lines starting with " + IC("#|") + " at the top of a chunk are chunk options: "
                 + IC("label") + ", " + IC("echo: false") + " (hide the code, show the result), "
                 + IC("warning: false") + ". Under " + IC("execute:") + " in the header they apply to every "
                 "chunk.",
                 "Inline R, " + IC("`r nrow(hh)`") + ", puts a number into a sentence.",
             ]},
             {"t": "syntax", "label": "profile.qmd (Python)", "code": QMD_PY},
             {"t": "h3", "html": "Render to HTML, Word and PDF"},
             {"t": "syntax", "label": "Terminal: render", "code": RENDER},
             {"t": "p", "html": "The " + link("https://quarto.org/docs/get-started/hello/text-editor.html",
                                             "Quarto tutorial") + " notes that the file name should come first "
                                "after " + IC("quarto render") + ". For PDF, the " + link(
                                    "https://quarto.org/docs/output-formats/pdf-basics.html", "PDF guide") + " says "
                                "you need a TeX distribution and recommends TinyTeX, installed with the last "
                                "command above. Word output needs nothing extra."},
             {"t": "info", "html": "<strong>Exercise.</strong> Save the R version as " + IC("profile.qmd") + " in "
                                   "a folder with " + DL + ", run " + IC("quarto render profile.qmd --to html") +
                                   ", and open the HTML file. Look for the sentence \"Households surveyed: 240.\" "
                                   "and a table of ten district percentages. Then render " + IC("--to docx") +
                                   " and open the Word file: the same numbers, no copying."},
         ]},
        {"tab": "Parameters",
         "title": "Parameterised reports: one template, ten district profiles",
         "blocks": [
             {"t": "p", "html": "A parameter is a value the report reads from outside, such as the district name. "
                                "Write the report once, then render it once per district. The " + link(
                                    "https://quarto.org/docs/computations/parameters.html", "Quarto parameters "
                                    "guide") + " gives one syntax for each engine."},
             {"t": "ul", "items": [
                 "<strong>R (knitr)</strong>: declare " + IC("params:") + " in the YAML header and use "
                 + IC("params$district") + " in code.",
                 "<strong>Python (Jupyter)</strong>: tag one cell " + IC("parameters") + " and set default "
                 "values there; Quarto injects a cell after it with the values you pass.",
             ]},
             {"t": "syntax", "label": "profile.qmd with a parameter (R)", "code": PARAMS_R},
             {"t": "syntax", "label": "The parameters cell (Python)", "code": PARAMS_PY},
             {"t": "syntax", "label": "Terminal: render with parameters", "code": PARAMS_RENDER},
             {"t": "p", "html": IC("-P district:Gaya") + " sets the parameter (the guide's own example is "
                                + IC("-P alpha:0.2") + ") and " + IC("--output") + " names the file, so the ten "
                                "renders do not overwrite each other."},
             {"t": "p", "html": "The cell runs what the report's chunk computes, for one district. Switch between "
                                "R and Python with the tabs on the cell."},
             {"t": "dual", "r": R_PROFILE, "py": PY_PROFILE, "pypkgs": "pandas"},
             {"t": "p", "html": "For Purnia (Bihar) it reports 24 households, 75.0% with a toilet, 75.0% with a "
                                "bank account and mean monthly spending of Rs 2,395 per person, then the count of "
                                "households in each caste group. Your rendered Purnia profile should show the same "
                                "figures."},
             {"t": "info", "html": "<strong>Exercise.</strong> Change the district to " + IC("Kozhikode") + " "
                                   "and run again; then to " + IC("Kozhikkode") + ". The misspelt name finds no "
                                   "households: R prints 0 households and NaN percentages, and Python stops with "
                                   "an error when it looks up the state. Add a check at the top of your .qmd that "
                                   "stops the render when the district is not in districts.csv, so a typo in a "
                                   "loop cannot produce an empty profile with a confident title."},
         ]},
        {"tab": "Layout",
         "title": "A reproducible project layout",
         "blocks": [
             {"t": "p", "html": "A project is reproducible when someone else can take the repository and the raw "
                                "data, run it, and get the same report. A plain folder layout and three rules get "
                                "most of the way."},
             {"t": "syntax", "label": "Project folders", "code": LAYOUT},
             {"t": "ul", "items": [
                 "<strong>Raw data is read-only.</strong> Scripts read " + IC("data/raw/") + " and write "
                 + IC("data/clean/") + "; nobody edits a raw export by hand. Raw data stays out of Git and is "
                 "shared through your organisation's controlled storage.",
                 "<strong>Outputs are rebuilt.</strong> Anything in " + IC("outputs/") + " can be deleted and "
                 "regenerated with the render loop, so it does not need to be committed.",
                 "<strong>Numbered scripts run in order.</strong> " + IC("01_clean.R") + " before the report. "
                 "The README says which command to run.",
                 "<strong>Record versions.</strong> Note the R or Python version and package versions in the "
                 "README (R's " + IC("sessionInfo()") + " prints them), so a result can be traced to the software "
                 "that produced it.",
                 "<strong>Commit small and often</strong>, each commit doing one thing, with a message that says "
                 "what.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> Set up this layout for a real project, with the "
                                   ".gitignore from module 5. Commit, push to a private repository, then clone "
                                   "it into a new folder, copy the raw data in, and run the README's command. If "
                                   "the reports come out the same, the project is reproducible. If something is "
                                   "missing, the clone tells you what."},
         ]},
    ],
    "next": [
        {"href": "/code/r-python.html", "title": "R and Python side by side",
         "desc": "The language for the code chunks in your reports."},
        {"href": "/code/tidyverse.html", "title": "The tidyverse",
         "desc": "Write the tables and charts your Quarto profiles will hold."},
        {"href": "/code/spreadsheets.html", "title": "Spreadsheets for M&amp;E",
         "desc": "Where most of the numbers start, and when to leave them."},
        {"href": "/101-courses/data-protection-dpdp.html", "title": "Data Protection and the DPDP Act",
         "desc": "What the law asks before personal data goes anywhere."},
        {"href": "/101-courses/research-ethics.html", "title": "Research Ethics 101",
         "desc": "Consent, confidentiality and data handling in field research."},
    ],
}

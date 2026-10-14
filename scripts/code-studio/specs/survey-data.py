# -*- coding: utf-8 -*-
"""Analysing Indian survey data: weights, design and the errors that matter.
NFHS/DHS, PLFS and HCES in R (survey package) and Python (numpy, pandas), on synthetic files."""

IC = lambda s: '<code class="inline">%s</code>' % s
TAG = '<span class="illustrative-tag">Synthetic data</span>'


def p(h):
    return {"t": "p", "html": h}


def h3(h):
    return {"t": "h3", "html": h}


def info(h, tone=None):
    b = {"t": "info", "html": h}
    if tone:
        b["tone"] = tone
    return b


def synth(h):
    return info("<strong>These files are synthetic.</strong> " + h, "warning")


def dual(r, py, pkgs="", pypkgs="pandas,numpy"):
    b = {"t": "dual", "r": r, "py": py, "pypkgs": pypkgs}
    if pkgs:
        b["pkgs"] = pkgs
    return b


# A Taylor-linearised standard error for a weighted mean, written out so the method is visible.
SVY = '''import numpy as np, pandas as pd

def svy_mean(df, y, weight, strata, psu, domain=None):
    """Weighted mean and its design-based standard error (Taylor linearisation).
    PSUs are treated as drawn with replacement within strata, as R's survey package
    does by default. A domain keeps every PSU and gives rows outside it zero weight."""
    d = np.ones(len(df)) if domain is None else df[domain].to_numpy(dtype=float)
    w = df[weight].to_numpy(dtype=float) * d
    yv = df[y].to_numpy(dtype=float)
    est = np.sum(w * yv) / np.sum(w)
    z = w * (yv - est) / np.sum(w)                 # each row's share of the error
    t = pd.DataFrame({"h": df[strata].to_numpy(), "j": df[psu].to_numpy(), "z": z})
    t = t.groupby(["h", "j"], as_index=False)["z"].sum()   # add up within each PSU
    var = 0.0
    for _, g in t.groupby("h"):                     # compare PSUs within each stratum
        n_h = len(g)
        var += n_h / (n_h - 1) * np.sum((g["z"] - g["z"].mean()) ** 2)
    return est, np.sqrt(var)

'''

R = {}
PY = {}

# ---------- Module 1: why weights and design ----------
R["look"] = '''hh <- read.csv("survey_hh.csv")
head(hh)
cat("Households:", nrow(hh), " PSUs:", length(unique(hh$psu)),
    " Strata:", length(unique(hh$stratum)), "\\n")'''
PY["look"] = '''import pandas as pd
pd.set_option("display.width", 150)
pd.set_option("display.max_columns", None)
hh = pd.read_csv("survey_hh.csv")
print(hh.head())
print("Households:", len(hh), " PSUs:", hh["psu"].nunique(),
      " Strata:", hh["stratum"].nunique())'''

R["share"] = '''hh <- read.csv("survey_hh.csv")
n_sample <- tapply(hh$weight, hh$sector, length)
n_pop <- tapply(hh$weight, hh$sector, sum)
data.frame(interviewed = n_sample,
           sample_share_pct = round(100 * n_sample / sum(n_sample), 1),
           represented = round(n_pop),
           population_share_pct = round(100 * n_pop / sum(n_pop), 1))'''
PY["share"] = '''import pandas as pd
hh = pd.read_csv("survey_hh.csv")
t = hh.groupby("sector").agg(interviewed=("hh_id", "size"),
                             represented=("weight", "sum"))
t["sample_share_pct"] = (100 * t["interviewed"] / t["interviewed"].sum()).round(1)
t["population_share_pct"] = (100 * t["represented"] / t["represented"].sum()).round(1)
t["represented"] = t["represented"].round()
print(t)'''

R["weighted"] = '''hh <- read.csv("survey_hh.csv")
cat("Households with LPG, unweighted:", round(100 * mean(hh$has_lpg), 1), "%\\n")
cat("Households with LPG, weighted:  ", round(100 * weighted.mean(hh$has_lpg, hh$weight), 1), "%\\n")
cat("Mean MPCE, unweighted: Rs", round(mean(hh$mpce)), "\\n")
cat("Mean MPCE, weighted:   Rs", round(weighted.mean(hh$mpce, hh$weight)), "\\n")'''
PY["weighted"] = '''import pandas as pd, numpy as np
hh = pd.read_csv("survey_hh.csv")
print("Households with LPG, unweighted:", round(100 * hh["has_lpg"].mean(), 1), "%")
print("Households with LPG, weighted:  ", round(100 * np.average(hh["has_lpg"], weights=hh["weight"]), 1), "%")
print("Mean MPCE, unweighted: Rs", round(hh["mpce"].mean()))
print("Mean MPCE, weighted:   Rs", round(np.average(hh["mpce"], weights=hh["weight"])))'''

R["se"] = '''library(survey)
hh <- read.csv("survey_hh.csv")
# What an ordinary formula assumes: every household drawn independently
naive_se <- sd(hh$has_lpg) / sqrt(nrow(hh))
cat("SE assuming simple random sampling:", round(100 * naive_se, 2), "points\\n")
# The design: PSUs drawn within strata, households within PSUs
des <- svydesign(ids = ~psu, strata = ~stratum, weights = ~weight,
                 data = hh, nest = TRUE)
m <- svymean(~has_lpg, des)
print(m)
cat("Design-based SE:", round(100 * SE(m), 2), "points\\n")'''
PY["se"] = SVY + '''hh = pd.read_csv("survey_hh.csv")
naive_se = hh["has_lpg"].std() / np.sqrt(len(hh))
print("SE assuming simple random sampling:", round(100 * naive_se, 2), "points")
est, se = svy_mean(hh, "has_lpg", "weight", "stratum", "psu")
print("Weighted share:", round(est, 4))
print("Design-based SE:", round(100 * se, 2), "points")'''

# ---------- Module 2: NFHS / DHS ----------
R["dhs_look"] = '''kids <- read.csv("dhs_kids.csv")
head(kids)
kids$wt <- kids$hv005 / 1000000
summary(kids$wt)
# hc70 is the height-for-age z-score times 100.
# Values of 9990 and above are flags, not scores.
table(flagged = kids$hc70 >= 9990)
table(kids$hc70[kids$hc70 >= 9990])'''
PY["dhs_look"] = '''import pandas as pd
pd.set_option("display.width", 150)
kids = pd.read_csv("dhs_kids.csv")
print(kids.head())
kids["wt"] = kids["hv005"] / 1_000_000
print(kids["wt"].describe())
# hc70 is the height-for-age z-score times 100.
# Values of 9990 and above are flags, not scores.
print((kids["hc70"] >= 9990).value_counts())
print(kids.loc[kids["hc70"] >= 9990, "hc70"].value_counts().sort_index())'''

R["dhs_flags"] = '''kids <- read.csv("dhs_kids.csv")
kids$wt <- kids$hv005 / 1000000
kids <- kids[kids$hv103 == 1 & kids$hc1 <= 59, ]   # de facto children 0-59 months

# Wrong: divide first. 9996 becomes 99.96, a child who looks very tall.
wrong_z <- kids$hc70 / 100
# Right: drop the flags, then divide.
ok <- kids$hc70 < 9990
right_z <- kids$hc70[ok] / 100

cat("Stunted, flags left in: ", round(100 * weighted.mean(wrong_z < -2, kids$wt), 1), "%\\n")
cat("Stunted, flags dropped: ", round(100 * weighted.mean(right_z < -2, kids$wt[ok]), 1), "%\\n")
cat("Mean z-score, flags left in: ", round(weighted.mean(wrong_z, kids$wt), 2), "\\n")
cat("Mean z-score, flags dropped: ", round(weighted.mean(right_z, kids$wt[ok]), 2), "\\n")'''
PY["dhs_flags"] = '''import pandas as pd, numpy as np
kids = pd.read_csv("dhs_kids.csv")
kids["wt"] = kids["hv005"] / 1_000_000
kids = kids[(kids["hv103"] == 1) & (kids["hc1"] <= 59)]   # de facto children 0-59 months

# Wrong: divide first. 9996 becomes 99.96, a child who looks very tall.
wrong_z = kids["hc70"] / 100
# Right: drop the flags, then divide.
ok = kids["hc70"] < 9990
right_z = kids.loc[ok, "hc70"] / 100

print("Stunted, flags left in: ", round(100 * np.average(wrong_z < -2, weights=kids["wt"]), 1), "%")
print("Stunted, flags dropped: ", round(100 * np.average(right_z < -2, weights=kids.loc[ok, "wt"]), 1), "%")
print("Mean z-score, flags left in: ", round(np.average(wrong_z, weights=kids["wt"]), 2))
print("Mean z-score, flags dropped: ", round(np.average(right_z, weights=kids.loc[ok, "wt"]), 2))'''

R["dhs_design"] = '''library(survey)
kids <- read.csv("dhs_kids.csv")
kids$wt <- kids$hv005 / 1000000
kids$valid <- kids$hv103 == 1 & kids$hc1 <= 59 & kids$hc70 < 9990
kids$stunted <- as.numeric(kids$hc70 < -200)      # below -2 SD
des <- svydesign(ids = ~hv021, strata = ~hv023, weights = ~wt,
                 data = kids, nest = TRUE)
kid_des <- subset(des, valid)    # a domain: every cluster stays in the design
m <- svymean(~stunted, kid_des)
print(m)
confint(m)
# hv025: 1 = urban, 2 = rural
svyby(~stunted, ~hv025, kid_des, svymean)'''
PY["dhs_design"] = SVY + '''kids = pd.read_csv("dhs_kids.csv")
kids["wt"] = kids["hv005"] / 1_000_000
kids["valid"] = (kids["hv103"] == 1) & (kids["hc1"] <= 59) & (kids["hc70"] < 9990)
kids["stunted"] = (kids["hc70"] < -200).astype(float)      # below -2 SD
est, se = svy_mean(kids, "stunted", "wt", "hv023", "hv021", domain="valid")
print("Stunted:", round(est, 4), " SE:", round(se, 4))
print("95% CI:", round(est - 1.96 * se, 4), "to", round(est + 1.96 * se, 4))
# hv025: 1 = urban, 2 = rural
for res in (1, 2):
    kids["dom"] = kids["valid"] & (kids["hv025"] == res)
    e, s = svy_mean(kids, "stunted", "wt", "hv023", "hv021", domain="dom")
    print("hv025 =", res, " stunted:", round(e, 4), " SE:", round(s, 4))'''

# ---------- Module 3: PLFS ----------
R["plfs_wt"] = '''p <- read.csv("plfs_persons.csv")
head(p)
p$wt <- ifelse(p$nss == p$nsc, p$mlt / 100, p$mlt / 200)
p$wt_wrong <- p$mlt / 100                      # the common mistake
aggregate(cbind(right = wt, wrong = wt_wrong) ~ stratum, data = p, FUN = sum)
cat("Persons 15+ represented, right weight:     ",
    format(round(sum(p$wt)), big.mark = ","), "\\n")
cat("Persons 15+ represented, MLT/100 everywhere:",
    format(round(sum(p$wt_wrong)), big.mark = ","), "\\n")'''
PY["plfs_wt"] = '''import pandas as pd, numpy as np
pd.set_option("display.width", 150)
pd.set_option("display.max_columns", None)
p = pd.read_csv("plfs_persons.csv")
print(p.head())
p["wt"] = np.where(p["nss"] == p["nsc"], p["mlt"] / 100, p["mlt"] / 200)
p["wt_wrong"] = p["mlt"] / 100                 # the common mistake
print(p.groupby("stratum")[["wt", "wt_wrong"]].sum().round())
print("Persons 15+ represented, right weight:     ", f"{round(p['wt'].sum()):,}")
print("Persons 15+ represented, MLT/100 everywhere:", f"{round(p['wt_wrong'].sum()):,}")'''

R["plfs_rates"] = '''p <- read.csv("plfs_persons.csv")
p$wt <- ifelse(p$nss == p$nsc, p$mlt / 100, p$mlt / 200)
# Usual status (ps+ss): works in the principal status, or for 30 days or more in a subsidiary one
p$us_worker <- p$ups %in% 11:51 | (!is.na(p$uss) & p$uss %in% 11:51)
p$us_lf <- p$us_worker | p$ups == 81
# Current weekly status: the 7 days before the interview
p$cws_worker <- p$cws %in% 11:72
p$cws_lf <- p$cws_worker | p$cws %in% 81:82
rates <- function(d, worker, lf) {
  c(LFPR = 100 * weighted.mean(d[[lf]], d$wt),
    WPR  = 100 * weighted.mean(d[[worker]], d$wt),
    UR   = 100 * sum(d$wt * (d[[lf]] & !d[[worker]])) / sum(d$wt * d[[lf]]))
}
women <- p[p$sex == 2, ]
men <- p[p$sex == 1, ]
round(rbind(
  "Usual status, all"   = rates(p, "us_worker", "us_lf"),
  "Usual status, women" = rates(women, "us_worker", "us_lf"),
  "Usual status, men"   = rates(men, "us_worker", "us_lf"),
  "CWS, all"            = rates(p, "cws_worker", "cws_lf"),
  "CWS, women"          = rates(women, "cws_worker", "cws_lf"),
  "CWS, men"            = rates(men, "cws_worker", "cws_lf")), 1)'''
PY["plfs_rates"] = '''import pandas as pd, numpy as np
p = pd.read_csv("plfs_persons.csv")
p["wt"] = np.where(p["nss"] == p["nsc"], p["mlt"] / 100, p["mlt"] / 200)
# Usual status (ps+ss): works in the principal status, or for 30 days or more in a subsidiary one
p["us_worker"] = p["ups"].between(11, 51) | p["uss"].between(11, 51)
p["us_lf"] = p["us_worker"] | (p["ups"] == 81)
# Current weekly status: the 7 days before the interview
p["cws_worker"] = p["cws"].between(11, 72)
p["cws_lf"] = p["cws_worker"] | p["cws"].between(81, 82)

def rates(d, worker, lf):
    w = d["wt"]
    return pd.Series({
        "LFPR": 100 * np.average(d[lf], weights=w),
        "WPR": 100 * np.average(d[worker], weights=w),
        "UR": 100 * (w * (d[lf] & ~d[worker])).sum() / (w * d[lf]).sum()})

women, men = p[p["sex"] == 2], p[p["sex"] == 1]
out = pd.DataFrame({
    "Usual status, all": rates(p, "us_worker", "us_lf"),
    "Usual status, women": rates(women, "us_worker", "us_lf"),
    "Usual status, men": rates(men, "us_worker", "us_lf"),
    "CWS, all": rates(p, "cws_worker", "cws_lf"),
    "CWS, women": rates(women, "cws_worker", "cws_lf"),
    "CWS, men": rates(men, "cws_worker", "cws_lf")}).T
print(out.round(1))'''

# ---------- Module 4: HCES ----------
R["hces_mpce"] = '''hh <- read.csv("survey_hh.csv")
hh$person_wt <- hh$weight * hh$hh_size        # households x persons in each
avg <- function(var, w) sapply(split(hh, hh$sector),
                               function(d) weighted.mean(d[[var]], d[[w]]))
data.frame(
  per_person_without_free_items = round(avg("mpce", "person_wt")),
  per_person_with_free_items    = round(avg("mpce_free_items", "person_wt")),
  per_household_without         = round(avg("mpce", "weight")))'''
PY["hces_mpce"] = '''import pandas as pd, numpy as np
hh = pd.read_csv("survey_hh.csv")
hh["person_wt"] = hh["weight"] * hh["hh_size"]   # households x persons in each

def avg(var, w):
    return hh.groupby("sector")[[var, w]].apply(lambda d: np.average(d[var], weights=d[w]))

out = pd.DataFrame({
    "per_person_without_free_items": avg("mpce", "person_wt"),
    "per_person_with_free_items": avg("mpce_free_items", "person_wt"),
    "per_household_without": avg("mpce", "weight")}).round()
pd.set_option("display.width", 150)
print(out)'''

R["hces_se"] = '''library(survey)
hh <- read.csv("survey_hh.csv")
hh$person_wt <- hh$weight * hh$hh_size
des <- svydesign(ids = ~psu, strata = ~stratum, weights = ~person_wt,
                 data = hh, nest = TRUE)
svyby(~mpce + mpce_free_items, ~sector, des, svymean)'''
PY["hces_se"] = SVY + '''hh = pd.read_csv("survey_hh.csv")
hh["person_wt"] = hh["weight"] * hh["hh_size"]
for sector in ["Rural", "Urban"]:
    hh["dom"] = hh["sector"] == sector
    for var in ["mpce", "mpce_free_items"]:
        est, se = svy_mean(hh, var, "person_wt", "stratum", "psu", domain="dom")
        print(sector, var, " mean:", round(est), " SE:", round(se, 1))'''

# ---------- Module 5: standard errors, domains, design effects ----------
R["ci"] = '''library(survey)
hh <- read.csv("survey_hh.csv")
des <- svydesign(ids = ~psu, strata = ~stratum, weights = ~weight,
                 data = hh, nest = TRUE)
m <- svymean(~has_lpg, des, deff = "replace")
print(m)
cat("Degrees of freedom (PSUs minus strata):", degf(des), "\\n")
confint(m)                    # normal approximation
confint(m, df = degf(des))    # t on the design degrees of freedom'''
PY["ci"] = SVY + '''from scipy import stats
hh = pd.read_csv("survey_hh.csv")
est, se = svy_mean(hh, "has_lpg", "weight", "stratum", "psu")
# Design effect: the design variance over the variance a simple random sample of the same size would give
w, y, n = hh["weight"], hh["has_lpg"], len(hh)
s2 = np.sum(w * (y - est) ** 2) / np.sum(w) * n / (n - 1)
deff = se ** 2 / (s2 / n)
df = hh["psu"].nunique() - hh["stratum"].nunique()
t = stats.t.ppf(0.975, df)
print("Share:", round(est, 4), " SE:", round(se, 4), " DEff:", round(deff, 2))
print("Degrees of freedom (PSUs minus strata):", df)
print("95% CI, normal:", round(est - 1.96 * se, 4), "to", round(est + 1.96 * se, 4))
print("95% CI, t:     ", round(est - t * se, 4), "to", round(est + t * se, 4))
print("Effective sample size:", round(n / deff), "of", n, "households")'''

R["domain"] = '''library(survey)
hh <- read.csv("survey_hh.csv")
# Wrong: cut the data to ST households, then declare the design
st_only <- hh[hh$social_group == "ST", ]
cat("PSUs left after cutting the data:", length(unique(st_only$psu)), "of",
    length(unique(hh$psu)), "\\n")
des_wrong <- svydesign(ids = ~psu, strata = ~stratum, weights = ~weight,
                       data = st_only, nest = TRUE)
print(svymean(~mpce, des_wrong))
# Right: declare the design on the whole file, then take the domain
des <- svydesign(ids = ~psu, strata = ~stratum, weights = ~weight,
                 data = hh, nest = TRUE)
print(svymean(~mpce, subset(des, social_group == "ST")))
# Every group at once, as domains
svyby(~mpce, ~social_group, des, svymean)'''
PY["domain"] = SVY + '''hh = pd.read_csv("survey_hh.csv")
# Wrong: cut the data to ST households, then compute
st_only = hh[hh["social_group"] == "ST"]
print("PSUs left after cutting the data:", st_only["psu"].nunique(), "of", hh["psu"].nunique())
est, se = svy_mean(st_only, "mpce", "weight", "stratum", "psu")
print("Cut first:   mean", round(est), " SE", round(se, 1))
# Right: keep the whole file and mark the domain
hh["st"] = hh["social_group"] == "ST"
est, se = svy_mean(hh, "mpce", "weight", "stratum", "psu", domain="st")
print("As a domain: mean", round(est), " SE", round(se, 1))
for g in ["ST", "SC", "OBC", "Others"]:
    hh["dom"] = hh["social_group"] == g
    est, se = svy_mean(hh, "mpce", "weight", "stratum", "psu", domain="dom")
    print(g, " mean:", round(est), " SE:", round(se, 1))'''


def code(key, pkgs="", pypkgs="pandas,numpy"):
    return dual(R[key], PY[key], pkgs, pypkgs)


GUIDE = "https://dhsprogram.com/data/Guide-to-DHS-Statistics/"
SOURCES = [
    ('The DHS Program, <em>Guide to DHS Statistics</em> (DHS-8), "Analyzing DHS Data"',
     GUIDE + "Analyzing_DHS_Data.htm"),
    ('The DHS Program, <em>Guide to DHS Statistics</em> (DHS-8), "Nutritional Status"',
     GUIDE + "Nutritional_Status.htm"),
    ("The DHS Program, India: Standard DHS, 2019-21 (NFHS-5), survey page",
     "https://dhsprogram.com/what-we-do/survey/survey-display-541.cfm"),
    ("NSO, MoSPI, README for PLFS unit-level data, January to December 2022",
     "https://www.mospi.gov.in/sites/default/files/main_menu/plfs_cy_22/README.pdf"),
    ("MoSPI microdata portal, PLFS quarterly release, study description (weights for quarterly files)",
     "https://microdata.gov.in/NADA/index.php/catalog/254/study-description"),
    ("PIB, Periodic Labour Force Survey (PLFS) Annual Report, 2025, released 27 March 2026",
     "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2246009"),
    ("MoSPI, Changes in Periodic Labour Force Survey (PLFS) from 2025",
     "https://www.mospi.gov.in/sites/default/files/publication_reports/PLFS_Changes-in-2025_rev.pdf"),
    ("IMF Dissemination Standards Bulletin Board, India, labour market: unemployment (NSS activity status codes)",
     "https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/UEM00"),
    ("PIB, Household Consumption Expenditure Survey: 2023-24, released 30 January 2025",
     "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2097601"),
    ("MoSPI microdata portal, Household Consumption Expenditure Survey: 2023-24, study description",
     "https://microdata.gov.in/NADA/index.php/catalog/237/study-description"),
    ("Thomas Lumley and others, survey: Analysis of Complex Survey Samples, R package version 4.5 (CRAN)",
     "https://CRAN.R-project.org/package=survey"),
]
SOURCE_LIST = "".join('<li><a href="%s" rel="noopener" target="_blank" style="color:var(--accent-color)">%s</a></li>'
                      % (u, t) for t, u in SOURCES)

PAGE = {
    "slug": "survey-data",
    "order": 3.5,
    "kind": "runnable",
    "title": "Analysing Indian survey data: weights, design and the errors that matter",
    "h1": "Analysing Indian survey data: weights, design and the errors that matter",
    "lede": ("NFHS, PLFS and HCES are sample surveys, and every figure you take from their unit-level files depends "
             "on three things beyond the data itself. These are the weight each record carries, the strata and "
             "primary sampling units the sample was drawn from, and the rules each survey sets for its own "
             "variables. This course works through all three in R and Python side by side, running in your "
             "browser. The files it uses are synthetic, built to show the method, so their numbers say nothing "
             "about India."),
    "description": ("Learn to analyse NFHS/DHS, PLFS and HCES unit-level data correctly in R and Python, covering survey "
                    "weights, strata and PSUs, anthropometry flags, the PLFS combined weight, MPCE by sector, "
                    "design-based standard errors, domains and design effects. Runs in your browser on synthetic "
                    "files."),
    "card": ("Weights, strata and PSUs in NFHS, PLFS and HCES, with design-based standard errors, in R and Python "
             "side by side."),
    "datasets": ["survey_hh", "dhs_kids", "plfs_persons"],
    "engine_note": ("<strong>How the live code works.</strong> Each cell has an R tab and a Python tab. The first "
                    "Run downloads the language engine once (R about 7&nbsp;MB, Python about 10&nbsp;MB). The R "
                    "cells that set a survey design install the " + IC("survey") + " package the first time, and "
                    "one Python cell loads " + IC("scipy") + ", so those take longer. The working folder already "
                    "holds three files, " + IC("survey_hh.csv") + ", " + IC("dhs_kids.csv") + " and " +
                    IC("plfs_persons.csv") + ". <strong>All three are synthetic.</strong> They copy the shape and "
                    "the variable names of the real files so that the code carries over, but every value was "
                    "generated for this page and none of them describes any place or person in India. The real "
                    "unit-level files come with terms of use from the DHS Program and from MoSPI, and you request "
                    "them yourself."),
    "modules": [
        {"tab": "Why design", "title": "Why survey estimates need weights and design", "blocks": [
            p("A national survey does not interview a simple random sample of households. It divides the country "
              "into <strong>strata</strong> (in Indian surveys, usually rural and urban parts of each state or "
              "district), draws a small number of <strong>primary sampling units</strong> (PSUs, which are "
              "villages or urban blocks) in each stratum, and then interviews a fixed number of households in "
              "each PSU. Two things follow from that. Some households had a much higher chance of being picked "
              "than others, so each record carries a <strong>weight</strong>, the number of households in the "
              "population it stands for. And households in the same village resemble each other, so 12 "
              "interviews in one village carry less information than 12 interviews in 12 villages."),
            synth("This course uses " + IC("survey_hh.csv") + ", a household file shaped like an HCES file. It holds 720 "
                  "households in 60 PSUs across 6 strata, with a weight, household size, social group, MPCE and "
                  "an LPG indicator. " + TAG + " The values were generated for this page and mean nothing about "
                  "India."),
            code("look"),
            p("The design of this file oversamples urban households. The next cell compares each sector's share of the interviews with its "
              "share of the households the weights say it represents."),
            code("share"),
            p("Urban households are half of the interviews and about a fifth of the population. Any figure that "
              "ignores the weights treats them as half the population. The cost shows in the numbers."),
            code("weighted"),
            p("Both the unweighted share of households with LPG and the unweighted mean MPCE are higher than the "
              "weighted ones, because the richer, oversampled urban households pull them up. The weighted figures "
              "are the estimates of the population. The unweighted ones describe the 720 households interviewed "
              "and nothing else."),
            h3("The design changes the standard error too"),
            p("Weights correct the point estimate. The standard error needs the design as well. An ordinary formula such as "
              + IC("sd(x) / sqrt(n)") + " assumes 720 independent draws. The real sample is 60 villages and "
              "blocks, and households in each are alike, so the true uncertainty is larger. R's " + IC("survey") +
              " package takes the design in " + IC("svydesign()") + ". The Python tab writes the same calculation "
              "out with numpy and pandas, so you can see what it does."),
            code("se", pkgs="survey"),
            p("The design-based standard error is more than twice the naive one. A confidence interval built on "
              "the naive figure would be less than half as wide as it should be, and a difference between two "
              "groups that looks significant may not be. " + IC("nest = TRUE") + " tells R that PSU numbers are "
              "unique only within a stratum, which is the safe setting for Indian files."),
            info("Python and R agree here to every printed digit. Both use the same method, Taylor linearisation "
                 "with PSUs treated as drawn with replacement within strata."),
        ]},
        {"tab": "NFHS / DHS", "title": "The weight and the anthropometry flags in NFHS and DHS files", "blocks": [
            p("The National Family Health Survey is India's Demographic and Health Survey. The DHS Program "
              "distributes NFHS-5 (2019-21) as a standard DHS survey in its DHS-7 recode structure, so its files "
              "use the standard DHS variable names, and the DHS Program's <em>Guide to DHS Statistics</em> is the "
              "reference for how each indicator is computed."),
            p("Three rules from the Guide matter on almost every analysis. The weight is " + IC("v005") + " in "
              "the women's file, " + IC("mv005") + " in the men's and " + IC("hv005") + " in the household and "
              "household-member files, and it must be divided by 1,000,000, because the weights are stored "
              "without the decimal point. The PSU is usually " + IC("v021") + " (" + IC("hv021") + ") and the "
              "stratum usually " + IC("v023") + " (" + IC("hv023") + "), though the Guide warns that "
              "stratification was not defined consistently across surveys and should be checked against "
              "Appendix A of the survey report. And the z-scores for child anthropometry, " + IC("hc70") +
              " for height-for-age, are stored as the z-score times 100, with values of 9990 and above used as "
              "flags for implausible or incomplete measurements."),
            synth(IC("dhs_kids.csv") + " is shaped like the child rows of a DHS household-member (PR) file. It has "
                  "cluster, stratum, residence, weight, whether the child slept in the household the night "
                  "before, age in months, sex and " + IC("hc70") + ". " + TAG + " It holds 397 invented children, "
                  "and the flag values were scattered at random to show the error."),
            code("dhs_look"),
            p("For a mean or a percentage, dividing the weight by 1,000,000 changes nothing, because the scale "
              "cancels. It matters for anything that counts, such as a frequency weight in software that reads "
              "the weight as a number of cases. The Guide divides it, and so should you."),
            h3("Drop the flags before dividing by 100"),
            p("The Guide defines stunting as a height-for-age z-score below -2 standard deviations from the median "
              "of the WHO Child Growth Standards, " + IC("hc70 &lt; -200") + ". Its denominator is de facto "
              "children aged 0 to 59 months (" + IC("hv103 == 1") + ") with a valid, non-flagged score, "
              + IC("hc70 &lt; 9990") + ". The order of operations is the trap. Divide " + IC("hc70") + " by 100 "
              "first and a flag of 9996 becomes a z-score of 99.96. That child is counted as not stunted, so "
              "every flag adds one to the denominator and nothing to the numerator, and the stunting rate falls. "
              "The mean z-score is worse, because each flag adds a value near 100."),
            code("dhs_flags"),
            p("In this synthetic file about a tenth of children carry a flag, more than you should expect in a "
              "real survey, so the error is large on purpose. In a real file it is smaller and harder to see. "
              "The mean z-score is the giveaway, since a mean "
              "height-for-age above zero in an Indian sample would be a very strange result."),
            h3("With the design"),
            p("The Guide's own R example sets the design with " + IC("svydesign()") + " from the " + IC("survey") +
              " package. The children who fail the filter are not removed from the data. They are left out of "
              "the estimate with " + IC("subset()") + " on the design, which keeps every cluster in the "
              "variance calculation. Module 5 shows why that matters."),
            code("dhs_design", pkgs="survey"),
        ]},
        {"tab": "PLFS", "title": "The PLFS combined weight, usual status and current weekly status", "blocks": [
            p("Until December 2024 the Periodic Labour Force Survey drew its first-stage units (FSUs) in two "
              "independent <strong>sub-samples</strong>. Each sub-sample on its own gives an estimate of the "
              "whole population, and the unit-level file carries a multiplier for each record calculated for "
              "its own sub-sample. The NSO's README for the calendar-year 2022 files names three variables. "
              + IC("NSS") + " is the number of FSUs surveyed in the record's sub-sample within its stratum and sub-stratum, "
              + IC("NSC") + " is the number surveyed in both sub-samples together, and " + IC("MLTS") + " is the "
              "multiplier. For a combined estimate from both sub-samples the README sets the final weight to "
              + IC("MLTS/100") + " where " + IC("NSS = NSC") + " and " + IC("MLTS/200") + " otherwise."),
            p("The reason for the two cases is that a stratum with FSUs in both sub-samples has two estimates of "
              "its total, which must be averaged, hence 200. A stratum where only one sub-sample was surveyed "
              "has one estimate, and its multiplier is used whole, hence 100. Applying " + IC("MLT/100") + " to "
              "every record counts most of the population twice."),
            info("<strong>Check which release you have.</strong> The README's exact variable name and rule differ "
                 "between releases (quarterly files use a different divisor), so read the README shipped with "
                 "your files. From January 2025 PLFS changed its design. MoSPI's release of the PLFS Annual Report "
                 "2025 says FSUs are now drawn \"with one FSU drawn per stratum/sub-stratum each month and no "
                 "provision for independent sub-samples\", so the two-case rule above belongs "
                 "to files up to 2024. Take the weight for 2025 files from their own README."),
            synth(IC("plfs_persons.csv") + " is shaped like a pre-2025 PLFS person file, restricted to persons "
                  "aged 15 and over, in 4 strata. Stratum 4 has FSUs in one sub-sample only, so its records have "
                  + IC("nss == nsc") + ". " + TAG + " The sex codes (1 male, 2 female) and status codes follow "
                  "the NSS conventions, but every value was generated for this page."),
            code("plfs_wt"),
            p("With " + IC("MLT/100") + " everywhere the three strata that have both sub-samples double, and the "
              "population total is close to twice the right one. Ratios such as the unemployment rate move less, "
              "because the error partly cancels between numerator and denominator, which is exactly why it goes "
              "unnoticed. Any total, such as the number of workers, is wrong by nearly a factor of two."),
            h3("Usual status and current weekly status"),
            p("PLFS classifies each person's activity in two ways. The <strong>usual status</strong> uses the 365 "
              "days before the survey. The principal status (ps) is the activity on which the person spent "
              "relatively long time in that year, and the subsidiary status (ss) records economic activity "
              "pursued for 30 days or more in addition to the principal one. A person counts as a worker in "
              "usual status (ps+ss) if either is work. The <strong>current weekly status</strong> (CWS) uses "
              "the 7 days before the survey. CWS figures are lower for work done in season, because a person "
              "who works for part of the year may not have worked in the reference week."),
            p("The three rates are defined by MoSPI as follows. The <strong>labour force participation rate "
              "(LFPR)</strong> is the percentage of persons in the labour force, meaning working or seeking or "
              "available for work, in the population. The <strong>worker population ratio (WPR)</strong> is the "
              "percentage of employed persons in the population. The <strong>unemployment rate (UR)</strong> is "
              "the percentage of persons unemployed among those in the labour force. The UR's denominator is the "
              "labour force, which is smaller than the population, so a UR and an LFPR are shares of different "
              "bases and cannot be added."),
            p("The status codes follow the NSS scheme. Codes 11 to 51 are kinds of work (own-account work, "
              "employer, unpaid helper in a household enterprise, regular wage or salaried work, casual labour). "
              "Codes 61 to 72 are people who had work but did not work in the reference period. "
              "Code 81 is seeking or available for work, with 82 added in the weekly status for those available "
              "but not seeking. Codes 91 to 99 are outside the labour force (education, domestic duties, "
              "rentiers and pensioners, disability, young children and others)."),
            code("plfs_rates"),
            p("In this file LFPR and WPR are lower in CWS than in usual status, because the synthetic data has "
              "some people who work during the year but did not work in the reference week. Always say which status a figure uses. PLFS publishes both, and MoSPI's headline "
              "annual figures are in usual status (ps+ss) for persons aged 15 and over."),
        ]},
        {"tab": "HCES", "title": "MPCE in HCES 2023-24, the two sectors and imputed free items", "blocks": [
            p("The Household Consumption Expenditure Survey measures what households consume. Its main indicator "
              "is <strong>monthly per capita consumption expenditure</strong> (MPCE), a household's consumption "
              "in a month divided by its size. MoSPI's press release of 30 January 2025 on HCES 2023-24 (August "
              "2023 to July 2024, 2,61,953 households) puts average MPCE at ₹4,122 in rural India and ₹6,996 in "
              "urban India. It reports every figure for rural and urban India separately and gives no single "
              "figure for the two together, and the same is true of its state tables."),
            p("The sectors are separate by construction. The microdata portal's study description says the rural "
              "sample is drawn from a frame of Census 2011 villages and the urban sample from a frame of Urban "
              "Frame Survey blocks, with sub-units formed by different rules in each. Rural and urban are "
              "estimated as two populations. A pooled all-India average can be computed from the unit-level "
              "data with the weights, but it is your own calculation. MoSPI has published no such figure, so label "
              "it as yours and never set it beside the published rural and urban numbers as if it were one of "
              "them."),
            h3("With and without imputation of free items"),
            p("HCES 2022-23 and 2023-24 publish two sets of MPCE. The first leaves out the value of items "
              "households received free through welfare programmes. The second imputes a value for them. The "
              "imputed items are named in the release, among them rice, wheat and atta, millets, pulses, salt, "
              "sugar and edible oil, and laptops, tablets, mobile handsets, bicycles, motorcycles, school "
              "uniforms and school shoes. Free health care such as PM-JAY and fee waivers in education were not "
              "imputed. With imputation, average MPCE in 2023-24 is ₹4,247 in rural India and ₹7,078 in urban "
              "India. The release reports the first set in its main section and the second after it. Whichever you use, say so, and compare like "
              "with like across years."),
            synth("The MPCE columns in " + IC("survey_hh.csv") + " (" + IC("mpce") + " without free items, "
                  + IC("mpce_free_items") + " with them) were generated for this page. " + TAG + " Their "
                  "averages are not the published figures above and should not be compared with them."),
            h3("Per person or per household"),
            p("An average across persons gives each household its weight times its size. An average across "
              "households uses the weight alone. Because larger households tend to have lower MPCE, the two "
              "differ. Find out which one a published table reports before you try to match it."),
            code("hces_mpce"),
            p("Both sectors are reported side by side, never as one number. Standard errors by sector come from "
              "the design in the same way as before, with each sector as a domain."),
            code("hces_se", pkgs="survey"),
        ]},
        {"tab": "Standard errors", "title": "Design-based standard errors, domains and design effects", "blocks": [
            p("Every estimate in the earlier modules has a design-based standard error behind it. This module "
              "sets out the three tools you need to report one properly."),
            synth("The cells below use " + IC("survey_hh.csv") + " again. " + TAG + " Its numbers are invented "
                  "and mean nothing about India."),
            h3("Confidence intervals and design effects"),
            p("The <strong>design effect</strong> (DEff) is the variance of an estimate under the real design "
              "divided by the variance a simple random sample of the same size would have given. A DEff of 4 "
              "means the 720 households carry as much information as 180 drawn at random. That smaller number "
              "is the <strong>effective sample size</strong>. For a confidence interval, R's " + IC("confint()") +
              " uses the normal distribution by default. With few PSUs a t distribution on the design's degrees "
              "of freedom, the number of PSUs minus the number of strata, is more honest. " + IC("deff = \"replace\"") +
              " compares against simple random sampling with replacement, the right choice when the weights are "
              "relative, as DHS weights are."),
            code("ci", pkgs="survey", pypkgs="pandas,numpy,scipy"),
            h3("Subgroups are domains, so do not cut the data first"),
            p("To estimate for a subgroup, such as Scheduled Tribe households, the tempting move is to keep only "
              "those rows and then declare the design. That throws away the PSUs where no ST household was "
              "interviewed. Those PSUs carry information. They tell you that this part of the sample contributed "
              "zero ST households, and the number of ST households in a PSU is itself random. Dropping them "
              "understates the standard error, and if a stratum is left with one PSU the variance cannot be "
              "computed at all. Declare the design on the whole file, then take the subgroup as a "
              "<strong>domain</strong> with " + IC("subset()") + " on the design or " + IC("svyby()") + " in R, "
              "or by giving rows outside the domain zero weight while keeping every PSU, as the Python function "
              "does."),
            code("domain", pkgs="survey"),
            p("The point estimate is the same both ways, and the standard error differs. The " + IC("survey") +
              " package's documentation includes a vignette, \"Estimates in subpopulations\", on exactly this."),
            info("<strong>Small domains.</strong> A standard error is itself an estimate, and with few PSUs in a "
                 "domain it is unreliable. If a subgroup has very few households or appears in only a handful of "
                 "PSUs, report that alongside the estimate, or do not report the estimate."),
        ]},
        {"tab": "Checklist", "title": "A checklist of the errors that matter", "blocks": [
            p("Each item below is a way to get a wrong number from these files with no error message to "
              "warn you. Go through them before you report a figure from NFHS, PLFS or HCES unit-level data."),
            {"t": "steps", "items": [
                "<strong>Use the weight.</strong> An unweighted mean describes the people interviewed and no one "
                "else. Indian surveys do not give every household the same chance of selection. HCES 2023-24, "
                "for one, allotted every state and UT at least 40 FSUs whatever its population.",
                "<strong>Use the right weight.</strong> DHS and NFHS weights are " + IC("v005/1000000") + " (or "
                + IC("mv005") + ", " + IC("hv005") + "). PLFS files up to 2024 use " + IC("MLT/100") + " where "
                + IC("NSS = NSC") + " and " + IC("MLT/200") + " otherwise, for combined estimates. Read the README "
                "that ships with your release.",
                "<strong>Use the right unit.</strong> MPCE per person weights households by weight times size. "
                "PLFS rates are per person. NFHS women's indicators come from the women's file.",
                "<strong>Drop anthropometry flags before dividing by 100.</strong> Valid scores are "
                + IC("hc70 &lt; 9990") + ". Restrict to de facto children aged 0 to 59 months.",
                "<strong>Say which activity status.</strong> Usual status (ps+ss) and current weekly status give "
                "different LFPR, WPR and UR. The unemployment rate is a share of the labour force.",
                "<strong>Keep rural and urban HCES figures apart</strong> and say whether MPCE includes imputed "
                "free items. A pooled figure is your own calculation and must be labelled as one.",
                "<strong>Declare the design.</strong> Strata and PSUs, with " + IC("nest = TRUE") + " where PSU "
                "numbers repeat across strata. Check the stratum variable against the survey report.",
                "<strong>Estimate subgroups as domains.</strong> Never cut the file before setting the design.",
                "<strong>Report the uncertainty.</strong> Give design-based standard errors or confidence "
                "intervals, and the design effect where it helps a reader judge the sample.",
                "<strong>Do not compare across a design change without saying so.</strong> MoSPI states that "
                "PLFS annual estimates for 2025 may not be strictly comparable with earlier ones because the "
                "sampling design changed in January 2025.",
                "<strong>Do not share the microdata.</strong> The DHS Program and MoSPI each set terms for their "
                "files. Share your code and your aggregate results instead.",
            ]},
            synth("Every number this course printed came from three synthetic files made for this page. " + TAG +
                  " They show how the method works. They say nothing about India, its states, or any group in it."),
            h3("Sources"),
            {"t": "ul", "items": [SOURCE_LIST]},
        ]},
    ],
    "next": [
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "The basics of both languages, if any of the code here was new."},
        {"href": "/code/pandas.html", "title": "pandas for Development Data",
         "desc": "Cleaning, joining and reshaping survey tables in Python."},
        {"href": "/code/tidyverse.html", "title": "The tidyverse for development data",
         "desc": "The same work in R with dplyr and ggplot2."},
    ],
}

# -*- coding: utf-8 -*-
"""pandas for Development Data: DataFrames, groupby, merge, reshaping, weights and matplotlib on the households and districts tables."""

RD = 'import pandas as pd\nhh = pd.read_csv("households.csv")\n'

C = {}
C["read"] = 'import pandas as pd\nhh = pd.read_csv("households.csv")\nprint(hh.head())'
C["info"] = RD + 'hh.info()'
C["shape"] = RD + 'print(hh.shape)\nprint(type(hh))\nprint(hh["district"].unique())'
C["select"] = RD + ('print(hh["monthly_pc_exp"].head(3))\n'
                    'print(hh[["hh_id", "district", "monthly_pc_exp"]].head(3))\n'
                    'print(hh.loc[0:2, ["district", "caste"]])\n'
                    'print(hh.iloc[0:3, 0:4])')
C["filter"] = RD + ('rural_f = hh[(hh["area"] == "Rural") & (hh["head_gender"] == "Female")]\n'
                    'print(rural_f[["hh_id", "district", "caste", "hh_size", "monthly_pc_exp"]]\n'
                    '      .sort_values("monthly_pc_exp"))')
C["query"] = RD + ('out = (hh.query("district in [\'Gaya\', \'Purnia\', \'Patna\'] and head_edu_years <= 5")\n'
                   '         [["hh_id", "district", "head_edu_years", "monthly_pc_exp"]]\n'
                   '         .sort_values("monthly_pc_exp", ascending=False))\n'
                   'print(len(out), "households")\n'
                   'print(out.head(10))')
C["assign"] = RD + ('out = hh.assign(annual_pc_exp=hh["monthly_pc_exp"] * 12,\n'
                    '                hh_monthly_exp=hh["monthly_pc_exp"] * hh["hh_size"],\n'
                    '                below_2000=hh["monthly_pc_exp"] < 2000)\n'
                    'print(out[["hh_id", "district", "monthly_pc_exp", "annual_pc_exp",\n'
                    '           "hh_monthly_exp", "below_2000"]].head(8))')
C["count"] = RD + 'print(hh["caste"].value_counts())\nprint(hh.value_counts(["area", "caste"]).sort_index())'
C["groupby"] = RD + ('out = (hh.groupby("district")\n'
                     '         .agg(n=("hh_id", "size"),\n'
                     '              mean_exp=("monthly_pc_exp", "mean"),\n'
                     '              median_exp=("monthly_pc_exp", "median"),\n'
                     '              pct_toilet=("has_toilet", lambda s: 100 * (s == "Yes").mean()))\n'
                     '         .sort_values("median_exp", ascending=False)\n'
                     '         .round(1))\n'
                     'print(out)')
C["groupby2"] = RD + ('out = (hh.groupby(["caste", "head_gender"], as_index=False)\n'
                      '         .agg(n=("hh_id", "size"), median_exp=("monthly_pc_exp", "median")))\n'
                      'print(out)')
C["merge"] = RD + ('districts = pd.read_csv("districts.csv")\n'
                   'print(districts)\n'
                   'hh_d = hh.merge(districts, on="district", how="left", validate="many_to_one")\n'
                   'print(hh_d.value_counts(["state", "district"]).sort_index())')
C["indicator"] = RD + ('districts = pd.read_csv("districts.csv")\n'
                       '# a misspelt district name, the kind you meet in real files\n'
                       'bad = districts.replace({"district": {"Purnia": "Purnea"}})\n'
                       'm = hh.merge(bad, on="district", how="left", indicator=True)\n'
                       'print(m["_merge"].value_counts())\n'
                       'print(m.loc[m["_merge"] == "left_only", "district"].value_counts())')
C["bystate"] = RD + ('districts = pd.read_csv("districts.csv")\n'
                     'out = (hh.merge(districts, on="district", how="left")\n'
                     '         .groupby(["state", "programme_phase"], as_index=False)\n'
                     '         .agg(households=("hh_id", "size"),\n'
                     '              pct_transfer=("received_transfer", lambda s: round(100 * (s == "Yes").mean(), 1))))\n'
                     'print(out)')
YN = 'yn = ["has_toilet", "has_bank_account", "shg_member", "received_transfer"]\n'
C["melt"] = RD + YN + ('long = hh.melt(id_vars=["hh_id", "district"], value_vars=yn,\n'
                       '               var_name="indicator", value_name="answer")\n'
                       'print(len(long))\n'
                       'print(long.head(8))\n'
                       'summary = (long.assign(yes=long["answer"] == "Yes")\n'
                       '               .groupby(["district", "indicator"], as_index=False)["yes"].mean())\n'
                       'summary["pct_yes"] = (100 * summary["yes"]).round()\n'
                       'print(summary.head(8))')
C["pivot"] = RD + YN + ('pd.set_option("display.width", 120)\n'
                        'long = hh.melt(id_vars=["hh_id", "district"], value_vars=yn,\n'
                        '               var_name="indicator", value_name="answer")\n'
                        'summary = (long.assign(yes=long["answer"] == "Yes")\n'
                        '               .groupby(["district", "indicator"], as_index=False)["yes"].mean())\n'
                        'summary["pct_yes"] = (100 * summary["yes"]).round()\n'
                        'wide = summary.pivot(index="district", columns="indicator", values="pct_yes")\n'
                        'print(wide)')
C["cat"] = RD + ('print(hh["caste"].value_counts().sort_index())\n'
                 'hh["caste"] = pd.Categorical(hh["caste"], categories=["SC", "ST", "OBC", "General"])\n'
                 'print(hh["caste"].value_counts().sort_index())\n'
                 'print(hh["caste"].cat.categories)')
C["cut"] = RD + ('hh["edu_band"] = pd.cut(hh["head_edu_years"],\n'
                 '                        bins=[-1, 0, 5, 10, 100],\n'
                 '                        labels=["No schooling", "1-5 years", "6-10 years", "Over 10 years"])\n'
                 'print(hh["edu_band"].value_counts().sort_index())')
C["map"] = RD + YN + ('hh[yn] = hh[yn].apply(lambda s: s.map({"Yes": True, "No": False}))\n'
                      'hh["area"] = hh["area"].map({"Rural": "Rural household", "Urban": "Urban household"})\n'
                      'print((100 * hh.groupby("area")[yn].mean()).round())')
C["weights"] = ('import pandas as pd, numpy as np\nhh = pd.read_csv("households.csv")\n'
                '# Illustrative design: rural households drawn 1 in 500, urban 1 in 1,000\n'
                'hh["prob"] = np.where(hh["area"] == "Rural", 1/500, 1/1000)\n'
                'hh["weight"] = 1 / hh["prob"]\n'
                'print(hh.value_counts(["area", "weight"]))\n'
                'toilet = (hh["has_toilet"] == "Yes").astype(float)\n'
                'print("unweighted mean:", round(hh["monthly_pc_exp"].mean(), 1))\n'
                'print("weighted mean:  ", round(np.average(hh["monthly_pc_exp"], weights=hh["weight"]), 1))\n'
                'print("toilet % unweighted:", round(100 * toilet.mean(), 1))\n'
                'print("toilet % weighted:  ", round(100 * np.average(toilet, weights=hh["weight"]), 1))')
C["wgroup"] = ('import pandas as pd, numpy as np\nhh = pd.read_csv("households.csv")\n'
               'hh["weight"] = np.where(hh["area"] == "Rural", 500, 1000)\n'
               'def wmean(g):\n'
               '    return np.average(g["monthly_pc_exp"], weights=g["weight"])\n'
               'out = pd.DataFrame({\n'
               '    "unweighted": hh.groupby("caste")["monthly_pc_exp"].mean(),\n'
               '    "weighted": hh.groupby("caste")[["monthly_pc_exp", "weight"]].apply(wmean),\n'
               '}).round(0)\n'
               'print(out)')
C["nfhs"] = ('import pandas as pd, numpy as np\n'
             '# Three made-up rows shaped like an NFHS women\'s file\n'
             'women = pd.DataFrame({"caseid": ["A1", "A2", "A3"],\n'
             '                      "v005": [1234567, 876543, 2045110],\n'
             '                      "anaemic": [1, 0, 1]})\n'
             'women["wt"] = women["v005"] / 1_000_000\n'
             'print(women)\n'
             'print("unweighted:", round(women["anaemic"].mean(), 3))\n'
             'print("weighted:  ", round(np.average(women["anaemic"], weights=women["wt"]), 3))')
PL = ('import pandas as pd\nimport matplotlib\nmatplotlib.use("AGG")\nimport matplotlib.pyplot as plt\n'
      'hh = pd.read_csv("households.csv")\n')
C["bar"] = PL + ('m = hh.groupby("caste")["monthly_pc_exp"].median()\n'
                 'fig, ax = plt.subplots(figsize=(6, 3.5))\n'
                 'ax.bar(m.index, m.values, color="#0369A1")\n'
                 'ax.set_title("Median monthly per-capita expenditure by caste")\n'
                 'ax.set_ylabel("Rupees per person per month")\n'
                 'ax.set_ylim(bottom=0)\n'
                 'print(m)\n'
                 'show(fig)')
C["scatter"] = PL + ('fig, ax = plt.subplots(figsize=(6, 4))\n'
                     'for area, colour in [("Rural", "#047857"), ("Urban", "#0369A1")]:\n'
                     '    d = hh[hh["area"] == area]\n'
                     '    ax.scatter(d["head_edu_years"], d["monthly_pc_exp"], s=14, alpha=0.7,\n'
                     '               color=colour, label=area)\n'
                     'ax.set_yscale("log")\n'
                     'ax.set_xlabel("Years of schooling, household head")\n'
                     'ax.set_ylabel("Rupees per person per month (log scale)")\n'
                     'ax.legend()\n'
                     'show(fig)')
C["facet"] = PL + ('t = (hh.assign(toilet=hh["has_toilet"] == "Yes")\n'
                   '       .groupby(["district", "area"])["toilet"].mean() * 100)\n'
                   'districts = sorted(hh["district"].unique())\n'
                   'fig, axes = plt.subplots(2, 5, figsize=(10, 4.5), sharey=True)\n'
                   'for ax, d in zip(axes.flat, districts):\n'
                   '    s = t.loc[d]\n'
                   '    ax.bar(s.index, s.values, color="#047857")\n'
                   '    ax.set_title(d, fontsize=9)\n'
                   '    ax.set_ylim(0, 100)\n'
                   'axes[0, 0].set_ylabel("% with toilet")\n'
                   'axes[1, 0].set_ylabel("% with toilet")\n'
                   'fig.suptitle("Households with a toilet, by district and area")\n'
                   'fig.tight_layout()\n'
                   'show(fig)')
C["axes"] = PL + ('m = hh.groupby("area")["monthly_pc_exp"].median()\n'
                  'print(m)\n'
                  'fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.2))\n'
                  'a1.bar(m.index, m.values, color="#0369A1"); a1.set_ylim(2000, 5000)\n'
                  'a1.set_title("Axis starts at 2,000")\n'
                  'a2.bar(m.index, m.values, color="#0369A1"); a2.set_ylim(bottom=0)\n'
                  'a2.set_title("Axis starts at zero")\n'
                  'fig.tight_layout()\n'
                  'show(fig)')
C["pipeline"] = ('import pandas as pd, numpy as np\n'
                 '\n'
                 '# 1. Read\n'
                 'hh = pd.read_csv("households.csv")\n'
                 'districts = pd.read_csv("districts.csv")\n'
                 '\n'
                 '# 2. Join, and stop if any household fails to match\n'
                 'df = hh.merge(districts, on="district", how="left",\n'
                 '              validate="many_to_one", indicator=True)\n'
                 'assert (df["_merge"] == "both").all(), "unmatched districts"\n'
                 '\n'
                 '# 3. Derive: illustrative weights and True/False indicators\n'
                 'yn = ["has_toilet", "has_bank_account", "shg_member", "received_transfer"]\n'
                 'df["weight"] = np.where(df["area"] == "Rural", 500, 1000)\n'
                 'df[yn] = df[yn] == "Yes"\n'
                 '\n'
                 '# 4. Summarise: one row per state, weighted per cent\n'
                 'def wpct(g):\n'
                 '    return pd.Series({c: round(100 * np.average(g[c], weights=g["weight"]), 1) for c in yn})\n'
                 'table_out = df.groupby("state")[yn + ["weight"]].apply(wpct)\n'
                 'print(table_out)\n'
                 '\n'
                 '# 5. Save, then read back to prove the file is right\n'
                 'table_out.to_csv("state_indicators.csv")\n'
                 'print(len(pd.read_csv("state_indicators.csv")), "rows written")')



def py(key):
    pk = "pandas"
    if "numpy" in C[key] or "np." in C[key]:
        pk += ",numpy"
    if "matplotlib" in C[key]:
        pk += ",matplotlib"
    return {"t": "code", "lang": "py", "code": C[key], "pkgs": pk}


def p(h):
    return {"t": "p", "html": h}


def ex(h):
    return {"t": "info", "html": "<strong>Try it.</strong> " + h}


IC = lambda s: '<code class="inline">%s</code>' % s

PAGE = {
    "slug": "pandas",
    "order": 3,
    "kind": "runnable",
    "title": "pandas for Development Data",
    "h1": "pandas for development data",
    "lede": ("Clean, join, reshape, weight and chart household survey data with Python's pandas, numpy and "
             "matplotlib, running live in your browser. For people who have finished the basics in "
             '<a href="/code/r-python.html" style="color:var(--accent-color)">R &amp; Python for Development</a>.'),
    "description": ("Learn pandas for development data: DataFrames, read_csv, selection, filtering, groupby, merge, "
                    "melt and pivot, categoricals, survey weights with numpy and matplotlib charts, on a "
                    "240-household illustrative survey. Runs in your browser, nothing to install."),
    "card": ("DataFrames, groupby, merge, melt and pivot, weights with numpy and matplotlib charts on a "
             "240-household survey."),
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>How the live code works.</strong> Your first Run downloads Pyodide (Python for the "
                    "browser, about 10&nbsp;MB) and pandas; numpy and matplotlib follow when a cell needs them. "
                    "Give the first click up to a minute on a slow connection; after that it is quick. Two files "
                    "are already in the working folder: " + IC("households.csv") + " and " + IC("districts.csv") +
                    ". Both are illustrative data, invented for teaching. The district names are real places, but "
                    "no number here describes them."),
    "modules": [
        {"tab": "DataFrames", "title": "Reading data into a DataFrame", "blocks": [
            p("pandas is Python's library for tables. A table is a <strong>DataFrame</strong>: rows with an "
              "<strong>index</strong> (the row labels on the left) and named columns, each column a "
              "<strong>Series</strong> of one type. This course also uses <strong>numpy</strong> for weighted "
              "means and <strong>matplotlib</strong> for charts."),
            p('The data is a household survey of 240 households across 10 districts in four states. '
              '<span class="illustrative-tag">Illustrative data, invented for teaching</span> '
              + IC("pd.read_csv()") + " reads it."),
            py("read"),
            p(IC(".head()") + " shows the first five rows. The " + IC("...") + " in the middle means pandas hid "
              "some columns to fit the width; the last line says the table has 13 columns. The numbers 0 to 4 on "
              "the left are the index, which pandas adds when the file has none."),
            py("info"),
            p(IC(".info()") + " lists every column with its count of non-missing values and its type. All 240 rows "
              "are complete. " + IC("int64") + " and " + IC("float64") + " are numbers; " + IC("object") + " is "
              "text, which includes the four Yes/No indicators."),
            py("shape"),
            p(IC(".shape") + " is (rows, columns): (240, 13). " + IC(".unique()") + " lists the 10 districts."),
            ex("Change " + IC('"households.csv"') + " to " + IC('"districts.csv"') + " in the third cell. What is "
               "its shape?"),
        ]},
        {"tab": "Selecting", "title": "Selecting, filtering and new columns", "blocks": [
            p("Square brackets with one name return one column as a Series; with a list of names they return a "
              "DataFrame. " + IC(".loc") + " selects by label and " + IC(".iloc") + " by position."),
            py("select"),
            p("Note the difference: " + IC("hh.loc[0:2, ...]") + " includes row label 2 and returns three rows, "
              "while " + IC("hh.iloc[0:3, 0:4]") + " stops before position 3, the usual Python rule. Use "
              + IC(".loc") + " with names in analysis code; positions break when someone adds a column."),
            {"t": "h3", "html": "Filtering rows"},
            p("A condition on a column gives a True/False Series. Put it inside square brackets to keep the True "
              "rows. Combine conditions with " + IC("&amp;") + " (and) or " + IC("|") + " (or), and wrap each in "
              "parentheses."),
            py("filter"),
            p("26 rural households are headed by a woman, and the poorest, in Gaya, spends &#8377;880 per person "
              "per month. The numbers on the left are the original row labels, kept through the filter and the "
              "sort."),
            py("query"),
            p(IC(".query()") + " takes the condition as a string, which reads closer to plain language. The three "
              "Bihar districts have 41 households whose head had five years of schooling or fewer; " +
              IC("ascending=False") + " sorts from largest down."),
            ex("Select urban households in Kozhikode and Wayanad whose head had more than 10 years of schooling, "
               "and show only " + IC("hh_id") + ", " + IC("district") + " and " + IC("land_acres") + "."),
            {"t": "h3", "html": "Adding columns"},
            p(IC(".assign()") + " returns a copy of the table with new columns, computed from existing ones row by "
              "row. You can also write " + IC('hh["new"] = ...') + ", which changes " + IC("hh") + " in place."),
            py("assign"),
            p(IC("below_2000") + " is a True/False flag, the way to mark households under a threshold such as a "
              "poverty line. Household 7 has one member, so its household total equals its per-person figure."),
            {"t": "h3", "html": "Counting"},
            py("count"),
            p(IC(".value_counts()") + " counts each value, largest first. Given a list of columns it counts each "
              "combination, sorted here with " + IC(".sort_index()") + ". OBC households are the largest group (108 of 240), and 20 are ST, of whom only 5 are "
              "urban."),
            ex("Add a column " + IC("big_hh") + " that is True when " + IC("hh_size &gt;= 6") + ", then count it "
               "by " + IC("area") + "."),
                ]},
        {"tab": "groupby", "title": "Group and aggregate", "blocks": [
            p(IC(".groupby()") + " splits the table by one or more columns; " + IC(".agg()") + " reduces each "
              "group to one row. Named aggregation, " + IC('new_name=("column", "function")') + ", sets the output "
              "column names in the same line. A share is the mean of a True/False Series, so "
              + IC('100 * (s == "Yes").mean()') + " is a percentage."),
            py("groupby"),
            p("Look at Udaipur: a mean of &#8377;3,610.8 and a median of &#8377;2,795. A few high-spending "
              "households pull the mean up, which is normal for consumption and income data. Report the median "
              "for a typical household. Kozhikode has the highest median, &#8377;6,080, and Rewa the lowest "
              "toilet coverage, 50 per cent."),
            py("groupby2"),
            p(IC("as_index=False") + " keeps the group columns as ordinary columns, which is easier to merge or "
              "save later. Check " + IC("n") + " before reading any median: the SC female-headed group holds 2 "
              "households, so its median of &#8377;4,240 says almost nothing. In a real report you would "
              "suppress or flag cells that small."),
            ex("Group by " + IC('["district", "area"]') + " and add " + IC("pct_bank") + " for bank accounts. "
               "Which district has the widest rural-urban gap in median spending?"),
        ]},
        {"tab": "merge", "title": "Merging households with districts", "blocks": [
            p("The household file has the district name; a separate district file has the state, region, "
              "programme phase and field team. " + IC(".merge()") + " matches rows on a shared key."),
            py("merge"),
            p(IC('how="left"') + " keeps every household. " + IC('validate="many_to_one"') + " makes pandas raise "
              "an error if a district appears twice in the district file, which would duplicate households. "
              "Every district has 24 households after the merge, so nothing was lost or doubled."),
            p("Merges fail silently when keys are spelt differently. Purnia is often written Purnea. Watch what "
              "happens when the district file uses the other spelling:"),
            py("indicator"),
            p(IC("indicator=True") + " adds a " + IC("_merge") + " column saying where each row came from. 216 "
              "rows matched and 24, all from Purnia, are " + IC("left_only") + ": still in the table but with "
              "missing state, so every state total would be quietly short. Check " + IC("_merge") + " after every "
              "merge."),
            py("bystate"),
            p("Kerala has rows for phases 1 and 3 only, because none of its districts is in phase 2. A missing row "
              "is a fact about the design, worth a footnote in a report."),
            ex("Group by " + IC("field_team") + " instead and compute the share of SHG members for each team."),
        ]},
        {"tab": "Reshape", "title": "melt and pivot for indicator tables", "blocks": [
            p("The four Yes/No indicators sit in four columns: <strong>wide</strong> form. " + IC(".melt()") +
              " makes it <strong>long</strong>: one row per household per indicator, so one groupby computes all "
              "four shares."),
            py("melt"),
            p("240 households times 4 indicators gives 960 rows. The grouped result has one row per district per "
              "indicator, 40 in all; the first eight are shown."),
            p(IC(".pivot()") + " goes the other way, spreading one column's values into new columns. That gives the "
              "table a report needs: districts down the side, indicators across the top."),
            py("pivot"),
            p("Rewa has 92 per cent of households with a bank account and 50 per cent with a toilet, and the "
              "lowest SHG membership, 4 per cent. Long form is for computing and charting, wide form is for "
              "reading."),
            ex("Add " + IC('"head_gender"') + " to " + IC("id_vars") + " and to the " + IC("groupby") + " list, "
               "then pivot with " + IC('index=["district", "head_gender"]') + "."),
        ]},
        {"tab": "Categoricals", "title": "Categoricals, bands and labels", "blocks": [
            p("Text sorts alphabetically, which puts General before SC and ST. A <strong>categorical</strong> "
              "column stores a fixed set of categories in the order you choose."),
            py("cat"),
            p("After the conversion, " + IC(".sort_index()") + " follows the category order instead of the "
              "alphabet. Categoricals also use less memory on large files, which helps on a modest laptop."),
            py("cut"),
            p(IC("pd.cut()") + " turns a number into bands. Each bin includes its right edge, so " + IC("(-1, 0]") +
              " is no schooling and " + IC("(0, 5]") + " is one to five years. 36 heads had no schooling and 25 "
              "more than 10 years. A value outside every bin becomes missing, so check the counts add up to 240."),
            py("map"),
            p(IC(".map()") + " replaces values using a dictionary: Yes/No become True/False, and short codes become "
              "readable labels. Here 63 per cent of rural and 92 per cent of urban households have a toilet."),
            ex("Band " + IC("land_acres") + " into landless, under 1 acre, 1 to 2.5 acres and over 2.5 acres, "
               "then count each band."),
        ]},
        {"tab": "Weights", "title": "Weighted means and survey weights", "blocks": [
            p("Most large surveys do not give every household the same chance of selection. A household drawn "
              "with probability 1 in 500 stands for 500 households, so its <strong>design weight</strong> is 500. "
              "Unweighted means describe the sample; weighted means estimate the population. pandas has no "
              "weighted mean of its own, so we use " + IC("np.average(values, weights=...)") + "."),
            p("Our file has no weight column, so we invent a design for teaching: rural households drawn 1 in 500 "
              "and urban households 1 in 1,000."),
            py("weights"),
            p("Weighting raises mean spending from &#8377;3,400.9 to &#8377;3,856.9 and toilet coverage from 72.5 "
              "to 77.2 per cent, because urban households, which spend more and more often have toilets, now "
              "count for twice as much."),
            py("wgroup"),
            p("For weighted means by group, write a small function and apply it to each group. Weighting moves "
              "every caste group upward here, because each contains urban households."),
            {"t": "h3", "html": "NFHS weights"},
            p("The DHS Program lists NFHS-5 (2019-21) as India's Standard DHS survey. Its "
              '<a href="https://dhsprogram.com/data/Guide-to-DHS-Statistics/Analyzing_DHS_Data.htm" rel="noopener" '
              'target="_blank" style="color:var(--accent-color)">Guide to DHS Statistics</a> (checked October 2026) '
              "explains that the women's weight " + IC("v005") + " is stored without its decimal point and must be "
              "divided by 1,000,000 before use. Three made-up rows show the step:"),
            py("nfhs"),
            {"t": "info", "tone": "warning", "html": (
                "<strong>Weights fix the estimate; they do not fix the standard error.</strong> "
                + IC("np.average()") + " gives the right point estimate but knows nothing about clusters and "
                "strata, so a confidence interval built from it will be too narrow. For design-based standard "
                'errors in Python, look at <a href="https://pypi.org/project/samplics/" rel="noopener" '
                'target="_blank" style="color:var(--accent-color)">samplics</a> (0.6.1 on PyPI as of October '
                "2026). The most widely used tool is R's "
                '<a href="https://cran.r-project.org/package=survey" rel="noopener" target="_blank" '
                'style="color:var(--accent-color)">survey package</a>, covered in the '
                '<a href="/code/tidyverse.html" style="color:var(--accent-color)">tidyverse course</a>.')},
            ex("Set both weights to 500 and run the first weights cell again. Weighted and unweighted results "
               "should now agree."),
        ]},
        {"tab": "Charts", "title": "Charts with matplotlib", "blocks": [
            p("matplotlib draws on a <strong>figure</strong> holding one or more <strong>axes</strong> (plot "
              "areas). " + IC("plt.subplots()") + " makes both; you draw on the axes and call " + IC("show(fig)") +
              ", a helper this page provides, to display the chart under the code. The first run downloads "
              "matplotlib."),
            py("bar"),
            p("Medians range from &#8377;2,050 for SC households to &#8377;3,170 for General. "
              + IC("set_ylim(bottom=0)") + " fixes the axis at zero, because a bar's length is its value."),
            py("scatter"),
            p("Each point is a household. Spending is skewed, so a log scale spreads out the crowded lower end; "
              "say so in the axis label, because a reader will otherwise read the gaps as equal."),
            py("facet"),
            p("Small multiples: one panel per district, all on a shared 0 to 100 scale (" + IC("sharey=True") +
              "), so panels can be compared at a glance. Giving each panel its own scale would let a short bar in "
              "one panel stand for more than a tall bar in another. Kozhikode shows no rural bar because the value is zero: none of its 3 rural households has a toilet. Three households are far too few to report a percentage for."),
            {"t": "h3", "html": "Honest axes"},
            py("axes"),
            p("The median is &#8377;2,380 for rural and &#8377;4,515 for urban households, about 1.9 times. In the "
              "left chart the axis starts at 2,000 and the urban bar looks more than six times as tall; the right "
              "chart, from zero, shows the real ratio. See "
              '<a href="/101-courses/data-viz.html" style="color:var(--accent-color)">Data Visualization 101</a>.'),
            ex("In the bar chart, group by " + IC("district") + " instead of " + IC("caste") + " and set "
               + IC("figsize=(9, 3.5)") + " so the ten names fit."),
        ]},
        {"tab": "Script", "title": "A reproducible script", "blocks": [
            p("Put the whole analysis in one script that runs from the raw files to the final table with no hand "
              "edits. Anyone with the files can then reproduce every number."),
            py("pipeline"),
            p("The script stops with an error if any household fails to match a district, builds the weights and "
              "indicators, and writes a four-row state table: Bihar 80.9 per cent toilet coverage, Kerala 82.2, "
              "Madhya Pradesh 72.9 and Rajasthan 71.7 (weighted, on illustrative data). It then reads the file "
              "back and confirms 4 rows."),
            {"t": "ul", "items": [
                IC("assert") + " turns a silent problem into a loud one. Add one after every merge and filter "
                "you depend on.",
                "Keep raw files read-only and write outputs to new files.",
                "Keep names, phone numbers and other identifiers out of files you share. "
                '<a href="/101-courses/data-protection-dpdp.html" style="color:var(--accent-color)">Data Protection '
                "&amp; the DPDP Act 101</a> covers what India's Digital Personal Data Protection Act, 2023 asks "
                "of survey teams.",
                "On your own laptop, save it as a " + IC(".py") + " file and run it with " + IC("python analysis.py")
                + ", or use a Jupyter notebook and restart and run all cells before sharing.",
            ]},
            ex("Group by " + IC('["state", "region"]') + " in step 4 and change the output file name. Run it and "
               "check the row count."),
        ]},
    ],
    "next": [
        {"href": "/code/tidyverse.html", "title": "Tidyverse for Development Data",
         "desc": "The same analysis on the same files, in R."},
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "Back to the basics, side by side in both languages."},
        {"href": "/101-courses/eda-hhs.html", "title": "Exploratory Data Analysis 101",
         "desc": "What to look for in a household survey before you model it."},
        {"href": "/101-courses/survey-design.html", "title": "Survey Design 101",
         "desc": "Where sampling weights come from."},
        {"href": "/101-courses/data-viz.html", "title": "Data Visualization 101",
         "desc": "Design principles for the charts you can now draw."},
    ],
}

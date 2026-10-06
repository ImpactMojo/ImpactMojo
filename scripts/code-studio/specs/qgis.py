# -*- coding: utf-8 -*-
"""QGIS: Maps for Development Data. A guided tool course with Python cells that prepare the table, test the join
and compare classification methods on the page.

Facts checked on 6 October 2026 against qgis.org (download page, road map, LTR announcement), the QGIS 3.44 user
manual (docs.qgis.org), DataMeet's maps project pages and repository, GADM's licence page, the Department of
Science and Technology's geospatial guidelines of 15 February 2021, and the Survey of India website. Sources are
listed in the agent report.
"""

DL = '<a href="/code/data/households.csv" download style="color:var(--accent-color)">households.csv</a>'
DD = '<a href="/code/data/districts.csv" download style="color:var(--accent-color)">districts.csv</a>'
A = 'style="color:var(--accent-color)"'


def link(href, text):
    return '<a href="%s" rel="noopener" target="_blank" %s>%s</a>' % (href, A, text)


SUM = '''import pandas as pd
hh = pd.read_csv("households.csv")
dist = pd.read_csv("districts.csv")
summary = (hh.groupby("district")
             .agg(households=("hh_id", "size"),
                  mean_pc_exp=("monthly_pc_exp", "mean"),
                  pct_toilet=("has_toilet", lambda s: 100 * (s == "Yes").mean()))
             .round(1)
             .reset_index()
             .merge(dist[["district", "state"]], on="district"))
'''

JENKS = '''def jenks(x, k):
    # exact natural breaks for a short list: try every split, keep the one with
    # the smallest total squared deviation within classes
    x = list(x)
    n = len(x)
    def ssd(a, b):
        seg = x[a:b]
        m = sum(seg) / len(seg)
        return sum((s - m) ** 2 for s in seg)
    best = (float("inf"), None)
    from itertools import combinations
    for cuts in combinations(range(1, n), k - 1):
        edges = (0,) + cuts + (n,)
        cost = sum(ssd(edges[i], edges[i + 1]) for i in range(k))
        if cost < best[0]:
            best = (cost, edges)
    e = best[1]
    return [x[0]] + [x[e[i] - 1] for i in range(1, k)] + [x[-1]]

'''

C = {}
C["summary"] = SUM + '''print(summary.sort_values("mean_pc_exp").to_string(index=False))
summary.to_csv("district_summary.csv", index=False)
print()
print("Copy the lines below into a text file named district_summary.csv")
print(summary.to_csv(index=False))'''

C["mismatch"] = '''import pandas as pd
# Names and census codes as they appear in the DataMeet district file
# (Districts/Census_2011/2011_Dist, fields DISTRICT, ST_NM and censuscode), checked 6 October 2026
boundary = pd.DataFrame({
    "DISTRICT": ["Barmer", "Betul", "Gaya", "Indore", "Kozhikode",
                 "Patna", "Purnia", "Rewa", "Udaipur", "Wayanad"],
    "ST_NM": ["Rajasthan", "Madhya Pradesh", "Bihar", "Madhya Pradesh", "Kerala",
              "Bihar", "Bihar", "Madhya Pradesh", "Rajasthan", "Kerala"],
    "censuscode": [115, 447, 236, 439, 591, 230, 211, 430, 130, 590],
})
# A district table as it might come out of an MIS, with names typed by hand
mis = pd.DataFrame({
    "district": ["Barmer", "Baitul", "Gaya ", "Indore", "Calicut",
                 "PATNA", "Purnea", "Rewa", "Udaipur", "Wayanad"],
    "mean_pc_exp": [2150.0, 1980.0, 1720.0, 3900.0, 3550.0, 3100.0, 1650.0, 2300.0, 2400.0, 2800.0],
})
j = boundary.merge(mis, left_on="DISTRICT", right_on="district", how="left", indicator=True)
print("Matched:", (j["_merge"] == "both").sum(), "of", len(boundary))
print("Boundaries left with no value:", list(j.loc[j["_merge"] == "left_only", "DISTRICT"]))
print("MIS names that matched nothing:", sorted(set(mis["district"]) - set(boundary["DISTRICT"])))'''

C["fixjoin"] = '''import pandas as pd
boundary = pd.DataFrame({
    "DISTRICT": ["Barmer", "Betul", "Gaya", "Indore", "Kozhikode",
                 "Patna", "Purnia", "Rewa", "Udaipur", "Wayanad"],
    "censuscode": [115, 447, 236, 439, 591, 230, 211, 430, 130, 590],
})
mis = pd.DataFrame({
    "district": ["Barmer", "Baitul", "Gaya ", "Indore", "Calicut",
                 "PATNA", "Purnea", "Rewa", "Udaipur", "Wayanad"],
    "mean_pc_exp": [2150.0, 1980.0, 1720.0, 3900.0, 3550.0, 3100.0, 1650.0, 2300.0, 2400.0, 2800.0],
})
# 1. Tidy what can be tidied, 2. map the rest with a written lookup
mis["district_clean"] = mis["district"].str.strip().str.title()
lookup = {"Baitul": "Betul", "Calicut": "Kozhikode", "Purnea": "Purnia"}
mis["district_clean"] = mis["district_clean"].replace(lookup)
j = boundary.merge(mis, left_on="DISTRICT", right_on="district_clean", how="left", validate="one_to_one")
print("Matched:", j["mean_pc_exp"].notna().sum(), "of", len(boundary))
print(j[["DISTRICT", "censuscode", "district", "mean_pc_exp"]].to_string(index=False))

# The same name in two states: a name-only join doubles the row
two = pd.DataFrame({"DISTRICT": ["Aurangabad", "Aurangabad"], "ST_NM": ["Bihar", "Maharashtra"]})
row = pd.DataFrame({"district": ["Aurangabad"], "state": ["Bihar"], "value": [10]})
print()
print("Join on name only:", len(row.merge(two, left_on="district", right_on="DISTRICT")), "rows")
print("Join on name and state:", len(row.merge(two, left_on=["district", "state"],
                                                right_on=["DISTRICT", "ST_NM"])), "row")'''

C["classes"] = SUM + '''import numpy as np
''' + JENKS + '''
v = summary.set_index("district")["mean_pc_exp"].sort_values()
k = 4

def equal_interval(x, k):
    return list(np.linspace(x.min(), x.max(), k + 1))

def quantile(x, k):
    return list(np.quantile(x, np.linspace(0, 1, k + 1)))

table = pd.DataFrame({"mean_pc_exp": v})
for name, f in [("equal_interval", equal_interval), ("quantile", quantile), ("natural_breaks", jenks)]:
    br = f(v.values, k)
    table[name] = np.searchsorted(br[1:-1], v.values, side="left") + 1
    print(f"{name:15}", [round(b) for b in br])
print()
print(table.to_string())
print()
print("Districts in the top class:",
      {m: list(table.index[table[m] == k]) for m in ["equal_interval", "quantile", "natural_breaks"]})'''

C["plot"] = SUM + '''import numpy as np
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
''' + JENKS + '''v = summary.set_index("district")["mean_pc_exp"].sort_values()
k = 4
schemes = {
    "Equal interval": np.linspace(v.min(), v.max(), k + 1),
    "Quantile": np.quantile(v, np.linspace(0, 1, k + 1)),
    "Natural breaks": jenks(v.values, k),
}
fig, axes = plt.subplots(len(schemes), 1, figsize=(7, 7), sharex=True)
for ax, (name, br) in zip(axes, schemes.items()):
    ax.scatter(v.values, [0] * len(v), color="#0369A1", zorder=3)
    for b in br[1:-1]:
        ax.axvline(b, color="#9A3412", linestyle="--")
    for i, (x, d) in enumerate(zip(v.values, v.index)):
        up = i % 2 == 0
        ax.annotate(d, (x, 0), xytext=(0, 7 if up else -7), textcoords="offset points", rotation=90,
                    fontsize=7, ha="center", va="bottom" if up else "top")
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_title(name + ": dashed lines are class breaks", fontsize=9, loc="left")
axes[-1].set_xlabel("Mean monthly per capita expenditure, Rs (illustrative data)")
fig.tight_layout()
show(fig)'''


def py(key, pkgs="pandas"):
    return {"t": "code", "lang": "py", "pkgs": pkgs, "code": C[key]}


PAGE = {
    "slug": "qgis",
    "order": 15,
    "kind": "guide",
    "tool": "QGIS",
    "title": "QGIS: Maps for Development Data",
    "h1": "QGIS: maps for development data",
    "lede": ("Turn a district table into a map you can put in a report: load openly licensed boundaries, join "
             "your survey figures to them by district name, choose how to group the values into colours, write "
             "a legend that does not mislead, and export a print layout. QGIS is free. Python cells on this page "
             "prepare the table and show what the join and the classification choices do to the same data."),
    "description": ("A free guided course in QGIS for development practitioners in South Asia: LTR or latest "
                    "release, layers, district boundaries from DataMeet, joining a CSV by district name, choropleth "
                    "classes (equal interval, quantile, natural breaks), honest legends, the official map of India "
                    "requirement, and exporting a print layout."),
    "card": "District boundaries, a CSV join that survives spelling differences, honest classes and legends, and a print layout.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>QGIS is desktop software.</strong> It does not run on this page, and this page shows "
                    "no QGIS screenshots or maps, because it cannot produce them. The steps tell you what to "
                    "click and what to look for. Menu paths follow the QGIS 3.44 user manual. The Python cells "
                    "build the table you will join, test the join, and compare classification methods on the "
                    "same numbers. The first Python run downloads the engine once (about 10&nbsp;MB)."),
    "modules": [
        {"tab": "Install",
         "title": "Install QGIS: long-term release or latest",
         "blocks": [
             {"t": "p", "html": "QGIS is a free and open source geographic information system. Its home page says "
                                "it is \"licensed under GNU GPLv2+\", and the download page says the software "
                                "\"is, and always will be, available free of charge if downloaded from QGIS.org\". "
                                "The download page asks for an optional donation; you can skip it."},
             {"t": "info", "html": "<strong>Versions, checked 6 October 2026</strong> on the "
                                   + link("https://qgis.org/download/", "QGIS download page") + " and "
                                   + link("https://qgis.org/resources/roadmap/", "road map") + ". The latest "
                                   "release is <strong>QGIS 4.2.3</strong>, released 25 September 2026. The "
                                   "long-term release (LTR) builds provide <strong>QGIS 3.44.15</strong>. On 3 "
                                   "October 2026 the project " + link("https://feed.qgis.org/169", "announced") +
                                   " that the next LTR is delayed and that it plans to release QGIS 4.4.4 as the "
                                   "LTR on 5 March 2027. Until then, 3.44 is the long-term release."},
             {"t": "h3", "html": "Which one to choose"},
             {"t": "p", "html": "The download page says LTR builds \"are intended for those who value stability over "
                                "having the latest features\", and \"if you are unsure which version is best for "
                                "you, download the LTR\". For a programme team that shares project files, choose "
                                "the LTR and have everyone use the same one. The menu paths on this page are from "
                                "the " + link("https://docs.qgis.org/3.44/en/docs/user_manual/", "QGIS 3.44 user "
                                "manual") + "; the 4.x releases may place some items differently."},
             {"t": "ul", "items": [
                 "<strong>Windows:</strong> the download page offers the OSGeo4W network installer (it "
                 "describes this as the best way to keep QGIS up to date and run several versions) and standalone "
                 "installers for the LTR (3.44) and the latest (4.2). Since QGIS 3.20 only 64-bit Windows "
                 "executables are shipped. On a slow connection, the standalone installer is one file you can "
                 "copy to a USB stick for colleagues.",
                 "<strong>macOS:</strong> signed installers for the LTR (3.44) and the latest (4.2).",
                 "<strong>Linux:</strong> packages for each distribution, chosen on the same page.",
             ]},
         ]},
        {"tab": "Layers",
         "title": "Layers, the map canvas and coordinate systems",
         "blocks": [
             {"t": "p", "html": "A QGIS <strong>project</strong> (a <code class=\"inline\">.qgz</code> file) holds a "
                                "list of <strong>layers</strong> and how each is drawn. The project file stores the "
                                "path to your data, so keep the project and its data in one folder and move them "
                                "together."},
             {"t": "ul", "items": [
                 "The <strong>Layers panel</strong> lists the layers. A layer higher in the list is drawn on top. "
                 "Tick a layer to show or hide it.",
                 "The <strong>Browser panel</strong> shows folders and data sources; you can drag a file from it "
                 "onto the map.",
                 "The <strong>map canvas</strong> draws the visible layers.",
                 "A <strong>vector layer</strong> holds features (points, lines or polygons) with an "
                 "<strong>attribute table</strong>: one row per feature. District boundaries are polygons, one "
                 "row per district.",
             ]},
             {"t": "h3", "html": "Coordinate reference systems"},
             {"t": "p", "html": "Every layer has a coordinate reference system (CRS) that says how its numbers map to "
                                "places on the earth. DataMeet's boundaries are in WGS84, EPSG:4326 (latitude and "
                                "longitude in degrees), as their project page states. QGIS shows the project's CRS "
                                "at the bottom right of the window. For a district choropleth of India, WGS84 is "
                                "fine to start with; if you measure areas or distances, reproject to a projected "
                                "CRS first, because degrees are not a unit of length."},
             {"t": "h3", "html": "Opening the attribute table"},
             {"t": "p", "html": "Select a layer in the Layers panel and choose <strong>Layer &#9658; Open Attribute "
                                "Table</strong>, or right-click it and choose <strong>Open Attribute Table</strong>, "
                                "or press <strong>F6</strong>. Do this every time you load or join something: the "
                                "table is where mistakes show first."},
         ]},
        {"tab": "Boundaries",
         "title": "Load district boundaries",
         "blocks": [
             {"t": "h3", "html": "Where to get boundaries, and their licences"},
             {"t": "ul", "items": [
                 "<strong>DataMeet, Community Created Maps of India</strong> (" +
                 link("http://projects.datameet.org/maps/", "projects.datameet.org/maps") + "). The " +
                 link("http://projects.datameet.org/maps/districts/", "district boundaries page") + " says the "
                 "dataset is \"shared under Creative Commons Attribution 2.5 India license\" (CC BY 2.5 IN), and "
                 "gives an attribution line to use. The " + link("https://github.com/datameet/maps", "repository")
                 + " README says that, unless stated otherwise, its datasets are under CC BY 4.0, so read the "
                 "licence stated for the folder you download: the files differ. The district file sits at "
                 "<code class=\"inline\">Districts/Census_2011/</code> in the repository, and its README says the "
                 "names and extents come from the Census of India 2011 Administrative Atlas. The project page warns "
                 "that the data \"is not perfect\".",
                 "<strong>GADM</strong> (" + link("https://gadm.org/license.html", "gadm.org") + ", version 4.1 on "
                 "the download page). Its licence page says the data \"are freely available for academic use and "
                 "other non-commercial use. Redistribution or commercial use is not allowed without prior "
                 "permission.\" It allows maps made with GADM data in published academic articles. For an NGO "
                 "report or a consultancy deliverable, check with GADM first.",
             ]},
             {"t": "info", "tone": "warning",
              "html": "<strong>District maps go out of date.</strong> India has created many districts since the "
                      "2011 Census, and the 2011 boundaries do not show them. If your survey uses current districts "
                      "and your boundaries are from 2011, some of your districts will have no polygon and some "
                      "polygons will cover two of your districts. Decide which set of boundaries matches your "
                      "sampling frame before you map anything."},
             {"t": "h3", "html": "Load the layer"},
             {"t": "steps", "items": [
                 "Download the district shapefile from DataMeet. A shapefile is several files with the same name "
                 "and different extensions (<code class=\"inline\">.shp</code>, <code class=\"inline\">.shx</code>, "
                 "<code class=\"inline\">.dbf</code>, <code class=\"inline\">.prj</code>, sometimes more). Keep them "
                 "together in one folder; the <code class=\"inline\">.shp</code> alone is useless.",
                 "In QGIS choose <strong>Layer &#9658; Add Layer &#9658; Add Vector Layer&hellip;</strong> "
                 "(<strong>Ctrl + Shift + V</strong>), or open the Data Source Manager with <strong>Ctrl + L</strong>.",
                 "Select the <code class=\"inline\">.shp</code> file (or a <code class=\"inline\">.geojson</code> "
                 "file, which is a single file) and click <strong>Add</strong>.",
                 "Open the attribute table (F6). In the DataMeet 2011 district file the fields are "
                 "<code class=\"inline\">DISTRICT</code>, <code class=\"inline\">ST_NM</code> (state name), "
                 "<code class=\"inline\">ST_CEN_CD</code>, <code class=\"inline\">DT_CEN_CD</code> and "
                 "<code class=\"inline\">censuscode</code>. When we read the file on 6 October 2026 it held 641 "
                 "districts.",
             ]},
         ]},
        {"tab": "Join",
         "title": "Join a CSV to the boundaries",
         "blocks": [
             {"t": "p", "html": "A choropleth needs one value per district in the boundary layer's attribute table. "
                                "Your survey figures are in a separate table, so you <strong>join</strong> them, "
                                "matching rows by a field the two tables share."},
             {"t": "h3", "html": "Make the district table"},
             {"t": "p", "html": "The course files are " + DL + " (240 households) and " + DD + " (10 districts). "
                                "<span class=\"illustrative-tag\">Illustrative data, invented for teaching</span> "
                                "The district names are real places; every number is made up, so a map of them "
                                "says nothing about the real districts. The cell summarises the households to one "
                                "row per district and prints it as CSV for you to save."},
             py("summary"),
             {"t": "p", "html": "Each district has 24 households. Mean monthly per capita expenditure runs from "
                                "Rs&nbsp;2,395.0 in Purnia to Rs&nbsp;6,757.5 in Kozhikode, and the share of "
                                "households with a toilet from 50.0% in Rewa to 83.3% in Indore, Kozhikode and "
                                "Patna. Copy the CSV lines into a text file called "
                                "<code class=\"inline\">district_summary.csv</code>."},
             {"t": "h3", "html": "Load the CSV and join it"},
             {"t": "steps", "items": [
                 "Open the Data Source Manager (<strong>Ctrl + L</strong>) and choose the <strong>Delimited "
                 "Text</strong> tab. Browse to <code class=\"inline\">district_summary.csv</code>, choose CSV as "
                 "the format, and under geometry choose <strong>No geometry (attribute only table)</strong>. Add "
                 "it. It appears in the Layers panel as a table.",
                 "Open the boundary layer's properties: double-click the layer, or right-click it and choose "
                 "<strong>Properties&hellip;</strong>. Go to the <strong>Joins</strong> tab and click the "
                 "<strong>Add new join</strong> button.",
                 "Set <strong>Join layer</strong> to <code class=\"inline\">district_summary</code>, <strong>Join "
                 "field</strong> to <code class=\"inline\">district</code> and <strong>Target field</strong> to "
                 "<code class=\"inline\">DISTRICT</code>.",
                 "Under <strong>Joined fields</strong>, tick only the columns you need, and set a short "
                 "<strong>Custom field name prefix</strong> such as <code class=\"inline\">s_</code> so the new "
                 "columns are easy to find. Click OK, then OK again.",
                 "Open the attribute table. The ten districts now carry values; the other 631 rows hold NULL in "
                 "the joined columns. That is correct here, because the survey covers ten districts.",
             ]},
             {"t": "p", "html": "The QGIS manual describes this join as one-to-one, based on an attribute that both "
                                "layers share, so the values must match exactly, letter for letter."},
             {"t": "h3", "html": "The name-mismatch problem"},
             {"t": "p", "html": "District names in survey and MIS files rarely match a boundary file exactly. The "
                                "cell below joins a hand-typed MIS table to the ten names as they appear in the "
                                "DataMeet file."},
             py("mismatch"),
             {"t": "p", "html": "Only <strong>5 of 10</strong> districts match. Betul, Gaya, Kozhikode, Patna and "
                                "Purnia get no value, because the MIS typed <em>Baitul</em>, <em>Gaya</em> with a "
                                "trailing space, <em>Calicut</em>, <em>PATNA</em> and <em>Purnea</em>. QGIS would give no warning: those districts would "
                                "simply be blank on the map, which reads as \"no data\" or, with some colour ramps, "
                                "as \"lowest\"."},
             py("fixjoin"),
             {"t": "p", "html": "After trimming spaces, fixing case and a three-line lookup, all 10 match. The second "
                                "part shows the other trap: <em>Aurangabad</em> is a district in both Bihar and "
                                "Maharashtra (the DataMeet 2011 file has both, along with other repeated names "
                                "such as Bilaspur, Hamirpur and Pratapgarh), so joining on the name alone turns one "
                                "row into two. Join on district <em>and</em> state, or better, on a code."},
             {"t": "info", "html": "<strong>Join on a code when you can.</strong> A census or LGD district code does "
                                   "not change with spelling or script. If your survey carries the 2011 census code, "
                                   "join it to <code class=\"inline\">censuscode</code> and the spelling problem "
                                   "disappears. If it carries only names, clean them first (see the "
                                   "<a href=\"/code/openrefine.html\" " + A + ">OpenRefine course</a>) and keep the "
                                   "lookup table with your project, so the next round's join uses the same fixes."},
             {"t": "info", "html": "<strong>Exercise.</strong> In the fix cell, delete "
                                   "<code class=\"inline\">\"Calicut\": \"Kozhikode\"</code> from the lookup and run. "
                                   "The count drops to 9 of 10, and the printed table shows which district lost its "
                                   "value."},
         ]},
        {"tab": "Choropleth",
         "title": "Choropleth styling and classification",
         "blocks": [
             {"t": "steps", "items": [
                 "Open the boundary layer's properties and go to <strong>Symbology</strong>.",
                 "Change the renderer at the top from Single Symbol to <strong>Graduated</strong>.",
                 "Set <strong>Value</strong> to the joined field, for example "
                 "<code class=\"inline\">s_mean_pc_exp</code>.",
                 "Pick a <strong>Color ramp</strong>: one hue from light to dark for a quantity where more is more.",
                 "On the <strong>Classes</strong> tab, set the number of classes and the <strong>Mode</strong>, "
                 "then click <strong>Classify</strong>. The <strong>Histogram</strong> tab shows where the class "
                 "breaks fall on the distribution of values.",
             ]},
             {"t": "h3", "html": "The classification modes"},
             {"t": "p", "html": "The QGIS manual lists these modes for a graduated renderer:"},
             {"t": "ul", "items": [
                 "<strong>Equal Interval</strong>: every class covers the same range of values.",
                 "<strong>Equal Count (Quantile)</strong>: every class holds the same number of features.",
                 "<strong>Natural Breaks (Jenks)</strong>: \"the variance within each class is minimized while the "
                 "variance between classes is maximized\".",
                 "Also: Fixed Interval, Logarithmic scale, Pretty Breaks (round numbers) and Standard Deviation.",
             ]},
             {"t": "p", "html": "Same data, different modes, different maps. The cell below puts the ten district "
                                "means into four classes three ways. The breaks come from code written for this "
                                "course (numpy quantiles, and an exact search for natural breaks); QGIS computes "
                                "its own, which may differ slightly, so compare them with the Histogram tab."},
             py("classes"),
             {"t": "p", "html": "The three methods disagree. <strong>Equal interval</strong> (breaks at about Rs 3,486, "
                                "4,576 and 5,667) puts six districts in the lowest class, three in the second, "
                                "<em>none</em> in the third and only Kozhikode in the top, because Kozhikode's "
                                "Rs 6,757.5 stretches the range. <strong>Quantile</strong> puts Indore, Wayanad and "
                                "Kozhikode together in the top class, although Kozhikode's mean is Rs 2,800 above "
                                "Wayanad's, and it separates Udaipur (class 3) from Indore (class 4), which are "
                                "Rs 147 apart. <strong>Natural breaks</strong> (about Rs 2,569, 2,962 and 3,957) "
                                "keeps Udaipur, Indore and Wayanad together and leaves Kozhikode alone at the top. "
                                "Three honest-looking maps of the same ten numbers would tell three different "
                                "stories about Indore."},
             py("plot", "pandas,matplotlib"),
             {"t": "p", "html": "The chart draws each district as a dot on one line and the class breaks as dashed "
                                "lines. In the equal-interval panel two of the three breaks fall in the empty "
                                "stretch between Wayanad and Kozhikode; in the quantile panel the breaks crowd into "
                                "the cluster of low values; the natural-breaks panel ends each class at the last district before a wide gap, so its "
                                "lines sit on Patna, Betul and Wayanad."},
             {"t": "h3", "html": "Why the choice matters"},
             {"t": "ul", "items": [
                 "<strong>Equal interval</strong> is easy to read (\"Rs 500 bands\"), and honest about distances "
                 "between values, but one outlier leaves most districts in one colour.",
                 "<strong>Quantile</strong> uses every colour equally, which makes any map look varied. Two "
                 "districts Rs 30 apart can land in different colours, and a reader will assume they differ.",
                 "<strong>Natural breaks</strong> fits this particular dataset, so the classes change when the "
                 "data change: two survey rounds classed this way cannot be compared colour for colour.",
                 "For a series of maps (two rounds, or the same indicator across states), fix the breaks by hand "
                 "with round numbers, and use the same breaks on every map.",
             ]},
             {"t": "info", "html": "<strong>Exercise.</strong> In the classes cell, change "
                                   "<code class=\"inline\">k = 4</code> to <code class=\"inline\">k = 3</code> and "
                                   "run. Does any method move Indore out of a class of its own?"},
         ]},
        {"tab": "Legends",
         "title": "Honest legends",
         "blocks": [
             {"t": "p", "html": "A legend is part of the claim the map makes. In the Classes list of the Graduated "
                                "renderer, double-click a label to edit it; the QGIS manual notes you can also set "
                                "the legend format and its precision. An empty class, like the third equal-interval "
                                "class in the last module, still shows in the legend: delete it or change the "
                                "breaks."},
             {"t": "ul", "items": [
                 "<strong>State the unit and the measure</strong>: \"Mean monthly per capita expenditure (Rs), "
                 "households surveyed\". A bare \"Expenditure\" leaves the reader guessing.",
                 "<strong>Round the class labels</strong> to what the data can support. \"Rs 2,395.0 to "
                 "2,569.2\" claims a precision that 24 households per district cannot give; \"Rs 2,400 to "
                 "2,600\" does not.",
                 "<strong>Show no-data districts as no data</strong>, in grey, with their own legend entry. A blank "
                 "district can read as zero. One way: put a second copy of the boundary layer underneath, styled "
                 "with a single grey fill, and name it \"No survey data\".",
                 "<strong>Use one hue, light to dark</strong>, for a quantity. Rainbow ramps have no natural order, "
                 "and red-green ramps fail for many colour-blind readers.",
                 "<strong>Say how many observations stand behind each value</strong>, in a note or a label. A "
                 "district mean from 24 households is a rough estimate; map the sample size too if it varies.",
                 "<strong>For survey estimates, use the weights</strong>. NFHS household weights are "
                 "<code class=\"inline\">hv005 / 1,000,000</code> and women's weights "
                 "<code class=\"inline\">v005 / 1,000,000</code>; compute the weighted district value before you "
                 "join it, in your statistics software. QGIS styles the numbers it is given and applies "
                 "no survey weights.",
                 "<strong>Write the source and the licence</strong> on the map: the survey, its year, and the "
                 "boundary file's attribution line.",
             ]},
         ]},
        {"tab": "India map",
         "title": "Publishing a map of India",
         "blocks": [
             {"t": "p", "html": "Maps of India that show the national or state boundaries carry an extra "
                                "requirement. The Department of Science and Technology's " +
                                link("https://dst.gov.in/sites/default/files/Final%20Approved%20Guidelines%20on%20Geospatial%20Data.pdf",
                                     "Guidelines for acquiring and producing Geospatial Data and Geospatial Data "
                                     "Services including Maps") + " (F.No.SM/25/02/2020 (Part-I), dated 15 February "
                                "2021) say in paragraph xiii:"},
             {"t": "info", "html": "\"For political Maps of India of any scale including national, state and other "
                                   "boundaries, SoI published maps or SoI digital boundary data are the standard to "
                                   "be used, which shall be made easily downloadable for free and their digital "
                                   "display and printing shall be permissible. Others may publish such maps that "
                                   "adhere to these standards.\""},
             {"t": "p", "html": "SoI is the Survey of India. Its " + link("https://surveyofindia.gov.in/",
                                "website") + " lists a Political Map of India, an Outline Map of India and state "
                                "maps among its products. The same guidelines' paragraph xv says violations \"will be "
                                "dealt with under the applicable laws\"."},
             {"t": "h3", "html": "What that means for your map"},
             {"t": "ul", "items": [
                 "If your map shows India's outline or state boundaries, the outline must match the Survey of "
                 "India's, including the boundaries in Jammu and Kashmir and Ladakh and in Arunachal Pradesh. "
                 "Compare your boundary file with the Survey of India's political map before you publish.",
                 "Global boundary sets do not necessarily follow it. GADM, Natural Earth and many web basemaps draw "
                 "India's borders differently in places, so do not assume a downloaded file complies.",
                 "DataMeet's repository has a <code class=\"inline\">Country</code> folder whose README describes "
                 "an India outline \"in accordance with the Official boundary of India as per the Survey of "
                 "India\" (<code class=\"inline\">india-composite.geojson</code>, licensed CC0) and a file "
                 "<code class=\"inline\">india-soi.geojson</code>, which it describes as \"dissolved shapefiles from "
                 "the official Indian shapefile data available\" (licence given as CC-by-sa 2.5 / ODbL). Check "
                 "either against the Survey of India map yourself.",
                 "A map of a few districts with no national or state outline still benefits from a state boundary "
                 "for context; take that boundary from a source that follows the official one.",
             ]},
         ]},
        {"tab": "Print layout",
         "title": "Export a print layout",
         "blocks": [
             {"t": "p", "html": "A print layout is a page on which you arrange the map, legend, scale bar, title and "
                                "notes, and from which you export a PDF or an image. The steps follow the QGIS 3.44 "
                                "manual's " + link("https://docs.qgis.org/3.44/en/docs/user_manual/print_layout/overview_layout.html",
                                "print layout overview") + " and " +
                                link("https://docs.qgis.org/3.44/en/docs/user_manual/print_layout/create_output.html",
                                     "output") + " pages."},
             {"t": "steps", "items": [
                 "Style the map in the main window first. Then choose <strong>Project &#9658; New Print "
                 "Layout&hellip;</strong> and give the layout a name.",
                 "Click <strong>Add map</strong> on the toolbar and drag a rectangle on the page. The current map "
                 "view is drawn inside it.",
                 "Click <strong>Add legend</strong> and drag a rectangle. In the legend's item properties, remove "
                 "layers that should not appear (the CSV table, for instance) and rename entries.",
                 "Click <strong>Add scale bar</strong> and click on the page. Add a north arrow from the same "
                 "toolbar if your audience expects one.",
                 "Add labels for the title, the source line (survey, year, sample size) and the boundary "
                 "attribution, for example DataMeet's suggested line with its licence.",
                 "Export with <strong>Layout &#9658; Export as PDF&hellip;</strong> or <strong>Layout &#9658; "
                 "Export as Image&hellip;</strong>. The manual notes that a PDF export puts every page of the layout "
                 "into one file, and that image export writes one file per page.",
                 "Save the project (<strong>Ctrl + S</strong>): the layout is saved inside it.",
             ]},
             {"t": "info", "html": "<strong>Before you send it.</strong> Read the exported PDF at the size it will be "
                                   "printed. Check that every class has a readable label with units, that no-data "
                                   "districts say so, that the source and licence lines are there, and, for a map "
                                   "of India, that the outline is the official one."},
         ]},
    ],
    "next": [
        {"href": "/code/openrefine.html", "title": "OpenRefine: cleaning messy survey and MIS data",
         "desc": "Clean district and village names so the join matches."},
        {"href": "/code/open-data-editor.html", "title": "Open Data Editor",
         "desc": "Check the district table before you share it."},
        {"href": "/code/pandas.html", "title": "pandas for development data",
         "desc": "Build weighted district summaries in code."},
        {"href": "/101-courses/data-viz.html", "title": "Data Visualization 101",
         "desc": "Choosing charts and colours that tell the truth."},
        {"href": "/101-courses/survey-design.html", "title": "Survey Design 101",
         "desc": "Sampling frames, districts and what an estimate can support."},
    ],
}

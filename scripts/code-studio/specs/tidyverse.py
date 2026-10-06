# -*- coding: utf-8 -*-
"""Tidyverse for Development Data: dplyr, tidyr, readr and ggplot2 on the households and districts tables."""

RD = "suppressPackageStartupMessages({library(readr); library(dplyr)})\n" \
     "hh <- read_csv(\"households.csv\", show_col_types = FALSE)\n"

C = {}
C["read"] = 'library(readr)\nhh <- read_csv("households.csv")\nhh'
C["glimpse"] = RD + "glimpse(hh)"
C["shape"] = RD + 'nrow(hh)\nncol(hh)\nclass(hh)\nhh |> distinct(district)'
C["filter"] = RD + ('hh |>\n'
                    '  filter(area == "Rural", head_gender == "Female") |>\n'
                    '  select(hh_id, district, caste, hh_size, monthly_pc_exp) |>\n'
                    '  arrange(monthly_pc_exp)')
C["mutate"] = RD + ('hh |>\n'
                    '  mutate(annual_pc_exp = monthly_pc_exp * 12,\n'
                    '         hh_monthly_exp = monthly_pc_exp * hh_size,\n'
                    '         below_2000 = monthly_pc_exp < 2000) |>\n'
                    '  select(hh_id, district, monthly_pc_exp, annual_pc_exp, hh_monthly_exp, below_2000) |>\n'
                    '  head(8)')
C["in"] = RD + ('hh |>\n'
                '  filter(district %in% c("Gaya", "Purnia", "Patna"),\n'
                '         between(head_edu_years, 0, 5)) |>\n'
                '  select(hh_id, district, head_edu_years, monthly_pc_exp) |>\n'
                '  arrange(desc(monthly_pc_exp))')
C["count"] = RD + 'hh |> count(caste)\nhh |> count(area, caste)'
C["summ"] = RD + ('hh |>\n'
                  '  group_by(district) |>\n'
                  '  summarise(n = n(),\n'
                  '            mean_exp = mean(monthly_pc_exp),\n'
                  '            median_exp = median(monthly_pc_exp),\n'
                  '            pct_toilet = 100 * mean(has_toilet == "Yes")) |>\n'
                  '  arrange(desc(median_exp))')
C["summ2"] = RD + ('hh |>\n'
                   '  group_by(caste, head_gender) |>\n'
                   '  summarise(n = n(),\n'
                   '            median_exp = median(monthly_pc_exp),\n'
                   '            .groups = "drop")')
C["join"] = RD + ('districts <- read_csv("districts.csv", show_col_types = FALSE)\n'
                  'districts\n'
                  'hh_d <- hh |> left_join(districts, by = "district")\n'
                  'hh_d |> count(state, district)')
C["anti"] = RD + ('districts <- read_csv("districts.csv", show_col_types = FALSE)\n'
                  '# a misspelt district name, the kind you meet in real files\n'
                  'bad <- districts |> mutate(district = if_else(district == "Purnia", "Purnea", district))\n'
                  'hh |> anti_join(bad, by = "district") |> count(district)\n'
                  'joined <- hh |> left_join(bad, by = "district")\n'
                  'sum(is.na(joined$state))')
C["bystate"] = RD + ('districts <- read_csv("districts.csv", show_col_types = FALSE)\n'
                     'hh |>\n'
                     '  left_join(districts, by = "district") |>\n'
                     '  group_by(state, programme_phase) |>\n'
                     '  summarise(households = n(),\n'
                     '            pct_transfer = round(100 * mean(received_transfer == "Yes"), 1),\n'
                     '            .groups = "drop")')
TR = "suppressPackageStartupMessages({library(readr); library(dplyr); library(tidyr)})\n" \
     "hh <- read_csv(\"households.csv\", show_col_types = FALSE)\n"
C["longer"] = TR + ('long <- hh |>\n'
                    '  select(hh_id, district, has_toilet, has_bank_account, shg_member, received_transfer) |>\n'
                    '  pivot_longer(c(has_toilet, has_bank_account, shg_member, received_transfer),\n'
                    '               names_to = "indicator", values_to = "answer")\n'
                    'nrow(long)\n'
                    'head(long, 8)\n'
                    'long |>\n'
                    '  group_by(district, indicator) |>\n'
                    '  summarise(pct_yes = round(100 * mean(answer == "Yes")), .groups = "drop")')
C["wider"] = TR + ('hh |>\n'
                   '  pivot_longer(c(has_toilet, has_bank_account, shg_member, received_transfer),\n'
                   '               names_to = "indicator", values_to = "answer") |>\n'
                   '  group_by(district, indicator) |>\n'
                   '  summarise(pct_yes = round(100 * mean(answer == "Yes")), .groups = "drop") |>\n'
                   '  pivot_wider(names_from = indicator, values_from = pct_yes)')
C["factor"] = RD + ('hh |> count(caste)\n'
                    'hh2 <- hh |> mutate(caste = factor(caste, levels = c("SC", "ST", "OBC", "General")))\n'
                    'hh2 |> count(caste)\n'
                    'levels(hh2$caste)')
C["cut"] = RD + ('hh |>\n'
                 '  mutate(edu_band = cut(head_edu_years,\n'
                 '                        breaks = c(-Inf, 0, 5, 10, Inf),\n'
                 '                        labels = c("No schooling", "1-5 years", "6-10 years", "Over 10 years"))) |>\n'
                 '  count(edu_band)')
C["across"] = RD + ('yn <- c("has_toilet", "has_bank_account", "shg_member", "received_transfer")\n'
                    'hh |>\n'
                    '  mutate(across(all_of(yn), \\(x) x == "Yes"),\n'
                    '         area = case_when(area == "Rural" ~ "Rural household",\n'
                    '                          area == "Urban" ~ "Urban household")) |>\n'
                    '  group_by(area) |>\n'
                    '  summarise(across(all_of(yn), \\(x) round(100 * mean(x))))')
C["weights"] = RD + ('# Illustrative design: rural households drawn 1 in 500, urban 1 in 1,000\n'
                     'hh <- hh |> mutate(prob = if_else(area == "Rural", 1/500, 1/1000),\n'
                     '                   weight = 1 / prob)\n'
                     'hh |> count(area, weight)\n'
                     'hh |>\n'
                     '  summarise(unweighted = mean(monthly_pc_exp),\n'
                     '            weighted = weighted.mean(monthly_pc_exp, weight),\n'
                     '            pct_toilet_unw = 100 * mean(has_toilet == "Yes"),\n'
                     '            pct_toilet_w = 100 * weighted.mean(has_toilet == "Yes", weight))')
C["nfhs"] = ('suppressPackageStartupMessages(library(dplyr))\n'
             '# Three made-up rows shaped like an NFHS women\'s file\n'
             'women <- tibble(caseid = c("A1", "A2", "A3"),\n'
             '                v005 = c(1234567, 876543, 2045110),\n'
             '                anaemic = c(1, 0, 1))\n'
             'women |>\n'
             '  mutate(wt = v005 / 1000000) |>\n'
             '  summarise(unweighted = mean(anaemic),\n'
             '            weighted = weighted.mean(anaemic, wt))')
GG = "suppressPackageStartupMessages({library(readr); library(dplyr); library(ggplot2)})\n" \
     "hh <- read_csv(\"households.csv\", show_col_types = FALSE)\n"
C["bar"] = GG + ('by_caste <- hh |>\n'
                 '  group_by(caste) |>\n'
                 '  summarise(median_exp = median(monthly_pc_exp))\n'
                 'ggplot(by_caste, aes(x = caste, y = median_exp)) +\n'
                 '  geom_col(fill = "#0369A1") +\n'
                 '  labs(title = "Median monthly per-capita expenditure by caste",\n'
                 '       subtitle = "Illustrative data, 240 households",\n'
                 '       x = NULL, y = "Rupees per person per month") +\n'
                 '  theme_minimal()')
C["scatter"] = GG + ('ggplot(hh, aes(x = head_edu_years, y = monthly_pc_exp, colour = area)) +\n'
                     '  geom_point(alpha = 0.7) +\n'
                     '  scale_y_log10() +\n'
                     '  labs(title = "Head\'s schooling and household spending",\n'
                     '       x = "Years of schooling, household head",\n'
                     '       y = "Rupees per person per month (log scale)") +\n'
                     '  theme_minimal()')
C["facet"] = GG + ('districts <- read_csv("districts.csv", show_col_types = FALSE)\n'
                   'hh |>\n'
                   '  left_join(districts, by = "district") |>\n'
                   '  group_by(state, district, area) |>\n'
                   '  summarise(pct_toilet = 100 * mean(has_toilet == "Yes"), .groups = "drop") |>\n'
                   '  ggplot(aes(x = area, y = pct_toilet)) +\n'
                   '  geom_col(fill = "#047857") +\n'
                   '  facet_wrap(~ district, nrow = 2) +\n'
                   '  labs(title = "Households with a toilet, by district and area",\n'
                   '       x = NULL, y = "Per cent of households") +\n'
                   '  theme_minimal()')
C["axes"] = GG + ('by_area <- hh |> group_by(area) |> summarise(median_exp = median(monthly_pc_exp))\n'
                  'by_area\n'
                  'p <- ggplot(by_area, aes(x = area, y = median_exp)) + geom_col(fill = "#0369A1") +\n'
                  '  theme_minimal() + labs(x = NULL, y = "Rupees per person per month")\n'
                  '# 1. Misleading: the bars start at 2,000\n'
                  'print(p + coord_cartesian(ylim = c(2000, 5000)) + ggtitle("Axis starts at 2,000"))\n'
                  '# 2. Honest: the bars start at zero\n'
                  'print(p + ggtitle("Axis starts at zero"))')
TRG = "suppressPackageStartupMessages({library(readr); library(dplyr); library(tidyr)})\n"
C["pipeline"] = TRG + (
    '# 1. Read\n'
    'hh <- read_csv("households.csv", show_col_types = FALSE)\n'
    'districts <- read_csv("districts.csv", show_col_types = FALSE)\n'
    '\n'
    '# 2. Check the join before trusting it\n'
    'stopifnot(nrow(anti_join(hh, districts, by = "district")) == 0)\n'
    '\n'
    '# 3. Derive: illustrative weights and logical indicators\n'
    'yn <- c("has_toilet", "has_bank_account", "shg_member", "received_transfer")\n'
    'clean <- hh |>\n'
    '  left_join(districts, by = "district") |>\n'
    '  mutate(weight = if_else(area == "Rural", 500, 1000),\n'
    '         across(all_of(yn), \\(x) x == "Yes"))\n'
    '\n'
    '# 4. Summarise: one row per state, weighted per cent\n'
    'table_out <- clean |>\n'
    '  pivot_longer(all_of(yn), names_to = "indicator", values_to = "yes") |>\n'
    '  group_by(state, indicator) |>\n'
    '  summarise(pct = round(100 * weighted.mean(yes, weight), 1), .groups = "drop") |>\n'
    '  pivot_wider(names_from = indicator, values_from = pct)\n'
    'table_out\n'
    '\n'
    '# 5. Save, then read back to prove the file is right\n'
    'write_csv(table_out, "state_indicators.csv")\n'
    'read_csv("state_indicators.csv", show_col_types = FALSE) |> nrow()')



def r(key, extra=""):
    pk = "readr,dplyr"
    if "tidyr" in C[key]:
        pk += ",tidyr"
    if "ggplot2" in C[key]:
        pk += ",ggplot2"
    if key == "nfhs":
        pk = "dplyr"
    return {"t": "code", "lang": "r", "code": C[key], "pkgs": pk}


def p(h):
    return {"t": "p", "html": h}


def ex(h):
    return {"t": "info", "html": "<strong>Try it.</strong> " + h}


IC = lambda s: '<code class="inline">%s</code>' % s

PAGE = {
    "slug": "tidyverse",
    "order": 2,
    "kind": "runnable",
    "title": "Tidyverse for Development Data",
    "h1": "Tidyverse for development data",
    "lede": ("Clean, join, reshape, weight and chart household survey data with R's tidyverse: readr, dplyr, "
             "tidyr and ggplot2, running live in your browser. For people who have finished the basics in "
             '<a href="/code/r-python.html" style="color:var(--accent-color)">R &amp; Python for Development</a>.'),
    "description": ("Learn R's tidyverse for development data: readr, dplyr verbs, joins, tidyr reshaping, factors, "
                    "survey weights and ggplot2, on a 240-household illustrative survey. Runs in your browser, "
                    "nothing to install."),
    "card": ("dplyr, tidyr, readr and ggplot2 on a 240-household survey: filter, summarise, join to districts, "
             "reshape indicator tables, weight and chart."),
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>How the live code works.</strong> Your first Run downloads WebR (R for the browser, "
                    "about 7&nbsp;MB) and then each package a cell asks for: readr and dplyr first, tidyr and "
                    "ggplot2 when you reach them. Give the first click of each module up to a minute on a slow "
                    "connection; after that it is quick. Two files are already in the working folder: "
                    + IC("households.csv") + " and " + IC("districts.csv") + ". Both are illustrative data, "
                    "invented for teaching. The district names are real places, but no number here describes them."),
    "modules": [
        {"tab": "Tibbles", "title": "Reading data into a tibble", "blocks": [
            p("The tidyverse is a family of R packages that share one way of working: every dataset is a table "
              "with one row per observation and one column per variable, and every function takes that table as "
              "its first argument. This course uses four of them. <strong>readr</strong> reads files, "
              "<strong>dplyr</strong> transforms tables, <strong>tidyr</strong> reshapes them and "
              "<strong>ggplot2</strong> draws them. We load each one by name instead of the "
              + IC("tidyverse") + " meta-package, which would pull in about thirty packages you do not need here."),
            p('The data is a household survey of 240 households across 10 districts in four states. '
              '<span class="illustrative-tag">Illustrative data, invented for teaching</span> '
              + IC('read_csv()') + ' from readr reads it into a <strong>tibble</strong>, the tidyverse version of '
              'a data frame.'),
            r("read"),
            p("A tibble prints only the first 10 rows and as many columns as fit, then tells you what it left "
              "out: here 230 more rows and 5 more variables. Under each column name is its type: "
              + IC("&lt;dbl&gt;") + " for numbers and " + IC("&lt;chr&gt;") + " for text. Printing a 50,000-row "
              "NFHS extract this way is safe; printing it as a base R data frame floods the console."),
            r("glimpse"),
            p(IC("glimpse()") + " turns the table on its side: one line per column, with its type and first few "
              "values. It is the fastest way to see every variable in a wide file. Here it confirms 240 rows and "
              "13 columns, and that the four yes/no indicators were read as text."),
            r("shape"),
            p("The class line shows that a tibble is still a " + IC("data.frame") + ", so base R functions you "
              "already know keep working. " + IC("distinct()") + " lists the 10 districts."),
            ex("Change " + IC('"households.csv"') + " to " + IC('"districts.csv"') + " in the first cell and run "
               "it. How many rows and columns does the district table have?"),
        ]},
        {"tab": "dplyr verbs", "title": "Filter, select, arrange and mutate", "blocks": [
            p("dplyr gives you one verb per job. " + IC("filter()") + " keeps rows, " + IC("select()") + " keeps "
              "columns, " + IC("arrange()") + " sorts and " + IC("mutate()") + " adds columns. The pipe "
              + IC("|&gt;") + " passes the table on the left into the function on the right, so a chain reads top "
              "to bottom as a list of steps."),
            p("Rural households headed by a woman, poorest first:"),
            r("filter"),
            p("Two conditions separated by a comma inside " + IC("filter()") + " must both be true. 26 households "
              "pass, and the poorest, in Gaya, spends &#8377;880 per person per month."),
            r("mutate"),
            p(IC("mutate()") + " computes new columns from existing ones, row by row. " + IC("below_2000") + " is a "
              "logical column (TRUE or FALSE), which is how you build a flag for a threshold such as a poverty "
              "line. Household 7 has one member, so its household total equals its per-person figure."),
            r("in"),
            p(IC("%in%") + " matches any value in a list, and " + IC("between()") + " is shorthand for "
              + IC("x &gt;= 0 &amp; x &lt;= 5") + ". The three Bihar districts have 41 households whose head had "
              "five years of schooling or fewer. " + IC("desc()") + " sorts from largest down."),
            ex("Filter for urban households in Kozhikode and Wayanad with more than 10 years of schooling. Then "
               "add a column " + IC("big_hh") + " that is TRUE when " + IC("hh_size &gt;= 6") + "."),
        ]},
        {"tab": "Summaries", "title": "Group, summarise and count", "blocks": [
            p(IC("count()") + " is the quickest table of frequencies. Give it two columns for a cross-tab in long "
              "form."),
            r("count"),
            p("OBC households are the largest group (108 of 240), and 20 are ST, of whom only 5 are urban."),
            p(IC("group_by()") + " splits the table and " + IC("summarise()") + " reduces each piece to one row. "
              "Every function inside " + IC("summarise()") + " must return one number per group. A share is the "
              "mean of a TRUE/FALSE condition, so " + IC('100 * mean(has_toilet == "Yes")') + " is a percentage."),
            r("summ"),
            p("Look at Udaipur: a mean of &#8377;3,611 and a median of &#8377;2,795. A few high-spending households "
              "pull the mean up, which is normal for consumption and income data. Report the median for a typical "
              "household. Kozhikode has the highest median, &#8377;6,080, and Rewa the lowest toilet coverage, "
              "50 per cent."),
            r("summ2"),
            p(IC('.groups = "drop"') + " removes the grouping after summarising, so the next step does not "
              "quietly run within groups. Check the " + IC("n") + " column before reading any median: the SC "
              "female-headed cell holds 2 households, so its median of &#8377;4,240 says almost nothing. In a "
              "real report you would suppress or flag cells that small."),
            ex("Group by " + IC("district, area") + " instead, and add " + IC("pct_bank") + " for bank accounts. "
               "Which district has the widest rural-urban gap in median spending?"),
        ]},
        {"tab": "Joins", "title": "Joining households to districts", "blocks": [
            p("Survey files rarely carry every variable you need. Here the household file has the district name, "
              "and a separate district file has the state, region, programme phase and field team. A "
              "<strong>join</strong> matches rows on a shared key."),
            r("join"),
            p(IC("left_join()") + " keeps every household and adds the district columns where the names match. "
              "Each district appears once in " + IC("districts.csv") + ", so every household gets exactly one "
              "match and the row count stays at 240."),
            p("Joins fail silently when keys are spelt differently. Purnia is often written Purnea. Watch what "
              "happens when the district file uses the other spelling:"),
            r("anti"),
            p(IC("anti_join()") + " returns the rows that found no partner: all 24 Purnia households. After a "
              "left join those households are still there, but with " + IC("NA") + " for state, so every state "
              "total would be quietly short. Run an " + IC("anti_join()") + " after every join; it should return "
              "zero rows."),
            r("bystate"),
            p("With the join done you can summarise at any level the district table offers. Kerala has rows for "
              "phases 1 and 3 only, because none of its districts is in phase 2. A missing row is a fact about the "
              "design, worth a footnote in a report."),
            ex("Change the grouping to " + IC("field_team") + " and compute the share of SHG members for each "
               "team."),
        ]},
        {"tab": "Reshape", "title": "Reshaping indicator tables with tidyr", "blocks": [
            p("The four yes/no indicators sit in four columns. That is <strong>wide</strong> form. To summarise all "
              "four with one line of code, turn them into <strong>long</strong> form: one row per household per "
              "indicator. " + IC("pivot_longer()") + " does this."),
            r("longer"),
            p("240 households times 4 indicators gives 960 rows. Each row now holds a household, an indicator name "
              "and its answer, so a single " + IC("group_by(district, indicator)") + " computes every share at "
              "once: 40 rows, one per district per indicator."),
            p("Reports want the opposite shape: districts down the side, indicators across the top. "
              + IC("pivot_wider()") + " spreads the long table back out."),
            r("wider"),
            p("This is the standard indicator table. Rewa has 92 per cent of households with a bank account and "
              "50 per cent with a toilet, and the lowest SHG membership, 4 per cent. Long form is for "
              "computing and charting, wide form is for reading."),
            ex("Add " + IC("head_gender") + " next to " + IC("district") + " in " + IC("group_by()") + " and run "
               "the second cell again. The wide table gets one row per district per gender."),
        ]},
        {"tab": "Factors", "title": "Factors, bands and labels", "blocks": [
            p("Text columns sort alphabetically, which puts General before SC and ST. A <strong>factor</strong> "
              "stores a fixed set of categories in the order you choose, and that order carries through to "
              "tables and charts."),
            r("factor"),
            p("The second count follows the order in " + IC("levels") + ". Choose an order that means something "
              "for the reader, such as a fixed order used across all your tables, or ranked by the indicator."),
            r("cut"),
            p(IC("cut()") + " turns a number into bands. The breaks are the edges: " + IC("(-Inf, 0]") + " is no "
              "schooling, " + IC("(0, 5]") + " is one to five years, and so on. 36 heads had no schooling and 25 "
              "had more than 10 years. Always check that the bands cover every value; a value outside every break "
              "becomes " + IC("NA") + "."),
            r("across"),
            p(IC("across()") + " applies the same function to several columns at once: first to turn each Yes/No "
              "into TRUE/FALSE, then to compute four shares in one " + IC("summarise()") + ". "
              + IC("case_when()") + " rewrites values by rule and is how you replace codes with readable labels. "
              "Here 63 per cent of rural households and 92 per cent of urban households have a toilet."),
            ex("Recode " + IC("land_acres") + " into bands (landless, under 1 acre, 1 to 2.5 acres, over 2.5 acres) "
               "with " + IC("cut()") + " and count each band."),
        ]},
        {"tab": "Weights", "title": "Weighted summaries and survey weights", "blocks": [
            p("Most large surveys do not give every household the same chance of selection. A household drawn "
              "with probability 1 in 500 stands for 500 households in the population, so its "
              "<strong>design weight</strong> is 500. Unweighted means describe the sample; weighted means "
              "estimate the population."),
            p("Our illustrative file has no weight column, so we invent a design for teaching: rural households "
              "drawn 1 in 500 and urban households 1 in 1,000. Urban households are under-sampled, so each one "
              "carries a weight of 1,000."),
            r("weights"),
            p("The weighted mean spending, &#8377;3,857, is higher than the unweighted &#8377;3,401, and toilet "
              "coverage rises from 72.5 to 77.2 per cent, because urban households (which spend more and more "
              "often have toilets) now count for twice as much. Same data, different question answered."),
            {"t": "h3", "html": "NFHS weights"},
            p("The DHS Program lists NFHS-5 (2019-21) as India's Standard DHS survey. The DHS Program's "
              '<a href="https://dhsprogram.com/data/Guide-to-DHS-Statistics/Analyzing_DHS_Data.htm" rel="noopener" '
              'target="_blank" style="color:var(--accent-color)">Guide to DHS Statistics</a> (checked October 2026) '
              "explains that the women's weight " + IC("v005") + " is stored without its decimal point and must be "
              "divided by 1,000,000 before use. Three made-up rows show the step:"),
            r("nfhs"),
            p("Dividing by a constant does not change a weighted mean, so " + IC("weighted.mean(anaemic, v005)") +
              " gives the same 0.789. The division matters when you sum weights to estimate a count of women."),
            {"t": "info", "tone": "warning", "html": (
                "<strong>Weights fix the estimate; they do not fix the standard error.</strong> "
                + IC("weighted.mean()") + " gives the right point estimate but knows nothing about clusters and "
                "strata, so any confidence interval built from it will be too narrow. For standard errors use the "
                '<a href="https://cran.r-project.org/package=survey" rel="noopener" target="_blank" '
                'style="color:var(--accent-color)">survey package</a> by Thomas Lumley (version 4.5 on CRAN as of '
                "October 2026): declare the design once with " + IC("svydesign(ids = ~psu, strata = ~strata, "
                "weights = ~wt, data = df)") + ", then use " + IC("svymean()") + " and " + IC("svyby()") + ".")},
            ex("Change the urban weight to 500 so both areas match, and run the weights cell again. The weighted "
               "and unweighted results should now agree."),
        ]},
        {"tab": "ggplot2", "title": "Charts with ggplot2", "blocks": [
            p("ggplot2 builds a chart in layers: the data, an " + IC("aes()") + " mapping that says which column "
              "goes on which axis, and a " + IC("geom") + " that says how to draw it. Add layers with " + IC("+") +
              ". The first run of this module downloads ggplot2 and its dependencies, so give it a minute."),
            r("bar"),
            p(IC("geom_col()") + " draws bars from values you computed. Bars always start at zero in ggplot2, "
              "which is right: a bar's length is its value."),
            r("scatter"),
            p("Each point is a household. Spending is skewed, so a log scale spreads out the crowded lower end; "
              "say so in the axis label, as here, because a reader will otherwise read the gaps as equal."),
            r("facet"),
            p(IC("facet_wrap(~ district)") + " draws one small panel per district on a shared scale, so the "
              "panels can be compared at a glance. Avoid " + IC('scales = "free_y"') + " when readers will "
              "compare panels: it gives each panel its own axis, and a short bar in one panel can stand for a "
              "larger value than a tall bar in another. Kozhikode shows no rural bar because the value is zero: none of its 3 rural households has a toilet. Three households are far too few to report a percentage for."),
            {"t": "h3", "html": "Honest axes"},
            r("axes"),
            p("The median is &#8377;2,380 for rural and &#8377;4,515 for urban households, so urban spending is "
              "about 1.9 times rural. In the first chart the axis starts at 2,000 and the urban bar looks more "
              "than six times as tall. The second chart, from zero, shows the real ratio. For bar charts, start "
              "at zero. See "
              '<a href="/101-courses/data-viz.html" style="color:var(--accent-color)">Data Visualization 101</a> '
              "for more."),
            ex("In the facet chart, swap " + IC("x = area") + " for " + IC("x = caste") + " and add "
               + IC("caste") + " to " + IC("group_by()") + ". Which districts have caste groups with very few "
               "households?"),
        ]},
        {"tab": "Pipeline", "title": "A reproducible pipeline", "blocks": [
            p("Put the whole analysis in one script that runs from the raw files to the final table with no hand "
              "edits. Anyone with the files can then reproduce every number, including you in six months."),
            r("pipeline"),
            p("The script reads both files, stops with an error if any household fails to match a district, "
              "builds the weights and indicators, and writes a four-row state table: Bihar 80.9 per cent toilet "
              "coverage, Kerala 82.2, Madhya Pradesh 72.9 and Rajasthan 71.7 (weighted, on illustrative data). It "
              "then reads the file back and confirms 4 rows."),
            {"t": "ul", "items": [
                IC("stopifnot()") + " turns a silent problem into a loud one. Add a check after every join and "
                "every filter you depend on.",
                "Keep raw files read-only. Write outputs to new files, as " + IC("write_csv()") + " does here.",
                "Keep names, phone numbers and other identifiers out of files you share. "
                '<a href="/101-courses/data-protection-dpdp.html" style="color:var(--accent-color)">Data Protection '
                "&amp; the DPDP Act 101</a> covers what India's Digital Personal Data Protection Act, 2023 asks "
                "of survey teams.",
                "On your own laptop, save the script as a " + IC(".R") + " file inside an RStudio project, or "
                "write it up in Quarto so the text and numbers come from the same run.",
            ]},
            ex("Add " + IC("region") + " to the " + IC("group_by()") + " in step 4, then change the output file "
               "name. Run it and check the row count printed at the end."),
        ]},
    ],
    "next": [
        {"href": "/code/pandas.html", "title": "pandas for Development Data",
         "desc": "The same analysis on the same files, in Python."},
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

# -*- coding: utf-8 -*-
"""SQL for Development Data: SQLite in the browser, on the three teaching tables."""

DATA_NOTE = ('<span class="illustrative-tag">Illustrative data</span> All three tables are invented for '
             'teaching. The district names are real places, but no number in these tables describes them.')


def sql(code):
    return {"t": "code", "lang": "sql", "code": code}


def p(h):
    return {"t": "p", "html": h}


def h3(h):
    return {"t": "h3", "html": h}


def info(h, tone=None):
    b = {"t": "info", "html": h}
    if tone:
        b["tone"] = tone
    return b


def ul(items):
    return {"t": "ul", "items": items}


MIS_BUILD = """-- Build an invented MIS-style export from the households table.
-- Run this cell first; the table lasts until you reload the page.
DROP TABLE IF EXISTS mis_payments;
CREATE TEMP TABLE mis_payments (
  payment_id   INTEGER,
  beneficiary_id INTEGER,  -- the household's id in the programme register
  district     TEXT,
  month        TEXT,       -- YYYY-MM, stored as text
  amount       REAL,
  status       TEXT
);
-- One credited payment for most households that reported a transfer
INSERT INTO mis_payments
SELECT hh_id * 10, hh_id, district, '2026-04', 500, 'Credited'
FROM households
WHERE received_transfer = 'Yes' AND hh_id % 9 <> 0;
-- A few failed payments, and one row entered twice
INSERT INTO mis_payments
SELECT hh_id * 10 + 1, hh_id, district, '2026-04', 500, 'Failed'
FROM households
WHERE received_transfer = 'No' AND hh_id % 13 = 0;
INSERT INTO mis_payments
SELECT payment_id, beneficiary_id, district, month, amount, status
FROM mis_payments
WHERE beneficiary_id = (SELECT MIN(beneficiary_id) FROM mis_payments);
SELECT COUNT(*) AS rows_in_export FROM mis_payments;"""

PAGE = {
    "slug": "sql",
    "order": 4,
    "kind": "runnable",
    "title": "SQL for Development Data",
    "h1": "SQL for Development Data",
    "lede": ("Learn SQL from zero on household and district tables, with SQLite running in your browser. "
             "Select, filter, summarise, recode, join, and use window functions, then apply them to the kind "
             "of export a scheme MIS gives you."),
    "description": ("Learn SQL from zero for development data in South Asia, with SQLite running live in your "
                    "browser: SELECT, WHERE, GROUP BY, CASE, joins, CTEs, window functions and NULLs, on "
                    "illustrative household and district tables."),
    "card": "Query household and district tables with SQLite in your browser, from SELECT to window functions.",
    "datasets": ["households", "districts", "survey"],
    "engine_note": ("<strong>How the live SQL works.</strong> Your first Run downloads SQLite (compiled to "
                    "WebAssembly by the sql.js project, under 1&nbsp;MB) and loads three small tables: "
                    "<code class=\"inline\">households</code> (240 rows), <code class=\"inline\">districts</code> "
                    "(10 rows) and <code class=\"inline\">survey</code> (16 rows). Every query runs on your "
                    "own machine, and nothing you type is sent anywhere. Reload the page to get the tables back "
                    "as they started."),
    "modules": [
        {"tab": "First query", "title": "Your first query", "blocks": [
            p("SQL (Structured Query Language) is how you ask questions of data held in tables. Most "
              "government and NGO systems keep their records in a database: a scheme's beneficiary register, "
              "a survey platform's server, a district MIS. SQL is the common language for reading them."),
            p("This course runs <strong>SQLite</strong>, a small database engine that lives in a single file "
              "and here runs inside your browser. The core of SQL is shared across databases, so what you "
              "learn transfers to PostgreSQL, MySQL and SQL Server. Where SQLite behaves differently, the "
              "course says so in a box marked <em>Other databases</em>."),
            h3("Three tables"),
            p("<code class=\"inline\">households</code> has 240 households across 10 districts, with caste, "
              "the head's gender and education, household size, monthly per-capita expenditure (in rupees), "
              "land, and Yes/No columns for a toilet, a bank account, self-help group membership and a cash "
              "transfer. <code class=\"inline\">districts</code> has one row per district with its state, "
              "region, programme phase and field team. <code class=\"inline\">survey</code> is a 16-person "
              "sample from three districts. " + DATA_NOTE),
            p("Click <strong>Run</strong>. The star means every column; <code class=\"inline\">LIMIT 5</code> "
              "keeps the first five rows."),
            sql("SELECT * FROM households LIMIT 5;"),
            p("Name the columns you want instead of using the star. Each column is separated by a comma, "
              "and the statement ends with a semicolon."),
            sql("SELECT hh_id, district, caste, monthly_pc_exp\nFROM households\nLIMIT 8;"),
            p("Which version of SQLite is this? Ask it."),
            sql("SELECT sqlite_version();"),
            info("<strong>Other databases.</strong> <code class=\"inline\">LIMIT</code> works in SQLite, "
                 "PostgreSQL and MySQL. SQL Server writes <code class=\"inline\">SELECT TOP 5 *</code> instead, "
                 "and the SQL standard form is <code class=\"inline\">FETCH FIRST 5 ROWS ONLY</code>."),
            p("<strong>Try it:</strong> in the second cell, add <code class=\"inline\">hh_size</code> and "
              "<code class=\"inline\">land_acres</code> to the column list and run again. Then change the "
              "table to <code class=\"inline\">districts</code> and select every column."),
        ]},
        {"tab": "Filter and sort", "title": "Filter with WHERE, sort with ORDER BY", "blocks": [
            p("<code class=\"inline\">WHERE</code> keeps the rows that meet a condition. Text values go in "
              "single quotes and must match exactly, including capital letters."),
            sql("SELECT hh_id, district, caste, monthly_pc_exp\nFROM households\n"
                "WHERE district = 'Gaya' AND area = 'Rural';"),
            p("Combine conditions with <code class=\"inline\">AND</code> and <code class=\"inline\">OR</code>, "
              "use <code class=\"inline\">IN</code> for a list of values and <code class=\"inline\">BETWEEN</code> "
              "for a range (both ends included). Brackets make the order of a mixed AND/OR explicit."),
            sql("SELECT hh_id, district, caste, head_gender, monthly_pc_exp\nFROM households\n"
                "WHERE caste IN ('SC', 'ST')\n  AND head_gender = 'Female'\n"
                "  AND monthly_pc_exp BETWEEN 1000 AND 3000;"),
            h3("Sort and keep the top rows"),
            p("<code class=\"inline\">ORDER BY</code> sorts, ascending by default; add <code "
              "class=\"inline\">DESC</code> for largest first. With <code class=\"inline\">LIMIT</code> this "
              "gives you the poorest or richest households in a few words."),
            sql("SELECT hh_id, district, caste, hh_size, monthly_pc_exp\nFROM households\n"
                "ORDER BY monthly_pc_exp ASC\nLIMIT 10;"),
            p("<code class=\"inline\">LIKE</code> matches patterns: <code class=\"inline\">%</code> stands "
              "for any run of characters. Here, every district whose name starts with P."),
            sql("SELECT * FROM districts WHERE district LIKE 'P%';"),
            info("<strong>Other databases.</strong> SQLite's <code class=\"inline\">LIKE</code> ignores case "
                 "for English letters, so <code class=\"inline\">'p%'</code> also matches Patna. PostgreSQL's "
                 "<code class=\"inline\">LIKE</code> is case-sensitive; it has <code class=\"inline\">ILIKE</code> "
                 "for the case-insensitive version."),
            p("<strong>Try it:</strong> change the third query to list the ten <em>highest</em>-spending "
              "households, then add <code class=\"inline\">WHERE area = 'Rural'</code> before the "
              "<code class=\"inline\">ORDER BY</code>."),
        ]},
        {"tab": "Summarise", "title": "Aggregates, GROUP BY and HAVING", "blocks": [
            p("Aggregate functions collapse many rows into one number: <code class=\"inline\">COUNT</code>, "
              "<code class=\"inline\">SUM</code>, <code class=\"inline\">AVG</code>, <code class=\"inline\">MIN</code>, "
              "<code class=\"inline\">MAX</code>. <code class=\"inline\">AS</code> gives the result a name, and "
              "<code class=\"inline\">ROUND(x, 0)</code> trims the decimals."),
            sql("SELECT COUNT(*)                     AS households,\n"
                "       ROUND(AVG(monthly_pc_exp), 0) AS mean_pc_exp,\n"
                "       MIN(monthly_pc_exp)           AS lowest,\n"
                "       MAX(monthly_pc_exp)           AS highest\nFROM households;"),
            h3("One row per group"),
            p("<code class=\"inline\">GROUP BY</code> runs the aggregate separately for each value of a "
              "column. This is disaggregation, the same split you would make in a pivot table."),
            sql("SELECT caste,\n       COUNT(*)                      AS households,\n"
                "       ROUND(AVG(monthly_pc_exp), 0) AS mean_pc_exp\nFROM households\n"
                "GROUP BY caste\nORDER BY mean_pc_exp DESC;"),
            p("In this invented table, SC households average 2,356 rupees and General households 3,771. The "
              "overall mean of 3,401 in the first query hides that gap."),
            p("A share is an average of a 0/1 column. In SQLite a comparison such as <code "
              "class=\"inline\">has_toilet = 'Yes'</code> returns 1 or 0, so its average is the proportion "
              "of households with a toilet."),
            sql("SELECT district,\n       COUNT(*) AS households,\n"
                "       ROUND(100.0 * AVG(has_toilet = 'Yes'), 1)       AS pct_toilet,\n"
                "       ROUND(100.0 * AVG(has_bank_account = 'Yes'), 1) AS pct_bank\n"
                "FROM households\nGROUP BY district\nORDER BY pct_toilet;"),
            info("<strong>Other databases.</strong> PostgreSQL will not average a true/false value directly. "
                 "Write <code class=\"inline\">AVG(CASE WHEN has_toilet = 'Yes' THEN 1.0 ELSE 0 END)</code>, "
                 "which works everywhere, including here. Also watch integer division: in PostgreSQL and SQL "
                 "Server <code class=\"inline\">7 / 2</code> is 3. Multiplying by <code class=\"inline\">100.0</code> "
                 "first keeps the decimals."),
            h3("Filter groups with HAVING"),
            p("<code class=\"inline\">WHERE</code> filters rows before grouping; <code class=\"inline\">HAVING</code> "
              "filters the groups after. This query groups by district and caste, then keeps only the cells "
              "with at least 5 households, a habit worth keeping before you report any small-group average."),
            sql("SELECT district, caste,\n       COUNT(*) AS households,\n"
                "       ROUND(AVG(monthly_pc_exp), 0) AS mean_pc_exp\nFROM households\n"
                "WHERE area = 'Rural'\nGROUP BY district, caste\nHAVING COUNT(*) >= 5\n"
                "ORDER BY district, mean_pc_exp;"),
            p("<strong>Try it:</strong> in the second query, change <code class=\"inline\">caste</code> to "
              "<code class=\"inline\">head_gender</code> in both places and run again. In the last query, "
              "raise the threshold to 8 and see which cells drop out."),
        ]},
        {"tab": "Recode", "title": "Recoding with CASE", "blocks": [
            p("<code class=\"inline\">CASE</code> turns values into categories. SQL checks each <code "
              "class=\"inline\">WHEN</code> in order and stops at the first one that is true, so put the "
              "narrowest band first or order the cut-offs from low to high."),
            sql("SELECT hh_id, monthly_pc_exp,\n       CASE\n"
                "         WHEN monthly_pc_exp < 1500 THEN '1 below 1,500'\n"
                "         WHEN monthly_pc_exp < 3000 THEN '2 1,500 to 2,999'\n"
                "         WHEN monthly_pc_exp < 6000 THEN '3 3,000 to 5,999'\n"
                "         ELSE '4 6,000 and above'\n       END AS exp_band\n"
                "FROM households\nLIMIT 10;"),
            p("The bands are invented for teaching. In real work, cut-offs come from a stated source, such "
              "as a poverty line for a named year and sector. The number at the start of each label makes "
              "the bands sort in order."),
            h3("Group by the new category"),
            p("You can group by the <code class=\"inline\">CASE</code> expression itself. SQLite also lets "
              "you group by the alias, <code class=\"inline\">exp_band</code>, which saves repeating it."),
            sql("SELECT CASE\n         WHEN monthly_pc_exp < 1500 THEN '1 below 1,500'\n"
                "         WHEN monthly_pc_exp < 3000 THEN '2 1,500 to 2,999'\n"
                "         WHEN monthly_pc_exp < 6000 THEN '3 3,000 to 5,999'\n"
                "         ELSE '4 6,000 and above'\n       END AS exp_band,\n"
                "       COUNT(*) AS households,\n"
                "       ROUND(100.0 * AVG(received_transfer = 'Yes'), 1) AS pct_transfer\n"
                "FROM households\nGROUP BY exp_band\nORDER BY exp_band;"),
            info("<strong>Other databases.</strong> Grouping by an alias works in SQLite, PostgreSQL and "
                 "MySQL. SQL Server and Oracle reject it; repeat the whole <code class=\"inline\">CASE</code> "
                 "in the <code class=\"inline\">GROUP BY</code>, or compute it in a CTE (module 6)."),
            h3("Recode land into the agricultural census classes"),
            p("The Agriculture Census groups operational holdings into five size classes: marginal (below "
              "1 hectare), small (1 to 2), semi-medium (2 to 4), medium (4 to 10) and large (10 and above), as "
              "the Ministry of Agriculture and Farmers Welfare set out in a <a "
              "href=\"https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1562687\" rel=\"noopener\" "
              "target=\"_blank\" style=\"color:var(--accent-color)\">PIB release of 5 February 2019</a>. The "
              "table records land in acres, and one acre is about 0.405 hectares, so the query converts first. "
              "The last three classes are merged because so few households here hold that much."),
            sql("SELECT CASE\n         WHEN land_acres = 0 THEN '0 landless'\n"
                "         WHEN land_acres * 0.4047 < 1 THEN '1 marginal (under 1 ha)'\n"
                "         WHEN land_acres * 0.4047 < 2 THEN '2 small (1 to 2 ha)'\n"
                "         ELSE '3 larger (2 ha and above)'\n       END AS land_class,\n"
                "       COUNT(*) AS households\nFROM households\nWHERE area = 'Rural'\n"
                "GROUP BY land_class\nORDER BY land_class;"),
            p("<strong>Try it:</strong> add a fourth column to the second query, "
              "<code class=\"inline\">ROUND(100.0 * AVG(caste IN ('SC','ST')), 1) AS pct_sc_st</code>, and run "
              "again. Then move the first cut-off from 1,500 to 2,000 in all three places you need to."),
        ]},
        {"tab": "Joins", "title": "Joining households to districts", "blocks": [
            p("The <code class=\"inline\">households</code> table knows each household's district but not its "
              "state or field team. Those live in <code class=\"inline\">districts</code>, one row per district. "
              "A <strong>join</strong> brings them together on the column they share."),
            sql("SELECT h.hh_id, h.district, d.state, d.field_team, h.monthly_pc_exp\n"
                "FROM households AS h\nJOIN districts AS d ON h.district = d.district\nLIMIT 8;"),
            p("<code class=\"inline\">h</code> and <code class=\"inline\">d</code> are short names (aliases) for "
              "the tables, so <code class=\"inline\">h.district</code> means the district column of households. "
              "Once joined, you can group by any column from either table."),
            sql("SELECT d.state,\n       COUNT(*) AS households,\n"
                "       ROUND(AVG(h.monthly_pc_exp), 0) AS mean_pc_exp,\n"
                "       ROUND(100.0 * AVG(h.has_toilet = 'Yes'), 1) AS pct_toilet\n"
                "FROM households AS h\nJOIN districts AS d ON h.district = d.district\n"
                "GROUP BY d.state\nORDER BY mean_pc_exp DESC;"),
            h3("Inner join against left join"),
            p("A plain <code class=\"inline\">JOIN</code> is an <strong>inner join</strong>: it keeps only rows "
              "that find a match on both sides. A <strong>left join</strong> keeps every row of the left-hand "
              "table, and fills the right-hand columns with NULL where there is no match."),
            p("Every household's district appears in <code class=\"inline\">districts</code>, so the joins above "
              "lose nothing. The 16-person <code class=\"inline\">survey</code> is different: it covers only "
              "three districts. Count survey respondents per district with an inner join first."),
            sql("SELECT d.district, d.state, COUNT(s.id) AS respondents\n"
                "FROM districts AS d\nJOIN survey AS s ON s.district = d.district\n"
                "GROUP BY d.district, d.state\nORDER BY d.district;"),
            p("Three rows: the inner join has silently dropped the seven districts the survey never reached. "
              "Now the same query with <code class=\"inline\">LEFT JOIN</code>."),
            sql("SELECT d.district, d.state, COUNT(s.id) AS respondents\n"
                "FROM districts AS d\nLEFT JOIN survey AS s ON s.district = d.district\n"
                "GROUP BY d.district, d.state\nORDER BY respondents DESC, d.district;"),
            p("All ten districts appear, and the seven without a respondent show 0. For a coverage report "
              "that difference is the whole point: an inner join would make the gaps disappear."),
            info("<strong>Count the right thing.</strong> <code class=\"inline\">COUNT(s.id)</code> counts only "
                 "rows where the survey id is not NULL, which is why unmatched districts show 0. "
                 "<code class=\"inline\">COUNT(*)</code> counts rows, and would show 1 for each of them, because "
                 "the left join keeps one row of NULLs for every unmatched district. Change it and run again "
                 "to see.", "warning"),
            p("<strong>Try it:</strong> add <code class=\"inline\">d.programme_phase</code> to the last query "
              "(in the SELECT and the GROUP BY). Then, in the state query, group by "
              "<code class=\"inline\">d.field_team</code> instead."),
        ]},
        {"tab": "CTEs", "title": "Subqueries and CTEs", "blocks": [
            p("A <strong>subquery</strong> is a query inside another query. This one finds households spending "
              "more than the overall mean: the inner query computes the mean once, and the outer query uses "
              "it as a number."),
            sql("SELECT COUNT(*) AS above_mean\nFROM households\n"
                "WHERE monthly_pc_exp > (SELECT AVG(monthly_pc_exp) FROM households);"),
            p("A subquery can also stand in for a table. Here the inner query builds district means, and the "
              "outer query keeps the districts above 3,000."),
            sql("SELECT *\nFROM (\n  SELECT district, ROUND(AVG(monthly_pc_exp), 0) AS mean_pc_exp\n"
                "  FROM households\n  GROUP BY district\n) AS dm\nWHERE mean_pc_exp > 3000\n"
                "ORDER BY mean_pc_exp DESC;"),
            h3("WITH: name each step"),
            p("Nested brackets get hard to read after two levels. A <strong>common table expression</strong> "
              "(CTE), written with <code class=\"inline\">WITH</code>, names each step and lets the next step "
              "use it, top to bottom. This query compares each district's mean with its state's mean."),
            sql("WITH district_means AS (\n"
                "  SELECT district, AVG(monthly_pc_exp) AS d_mean, COUNT(*) AS n\n"
                "  FROM households\n  GROUP BY district\n),\nstate_means AS (\n"
                "  SELECT d.state, AVG(h.monthly_pc_exp) AS s_mean\n"
                "  FROM households AS h\n  JOIN districts AS d ON h.district = d.district\n"
                "  GROUP BY d.state\n)\n"
                "SELECT dm.district, d.state, dm.n,\n       ROUND(dm.d_mean, 0) AS district_mean,\n"
                "       ROUND(sm.s_mean, 0) AS state_mean,\n"
                "       ROUND(dm.d_mean - sm.s_mean, 0) AS gap\n"
                "FROM district_means AS dm\nJOIN districts AS d ON dm.district = d.district\n"
                "JOIN state_means AS sm ON sm.state = d.state\nORDER BY d.state, gap DESC;"),
            p("Each CTE can be run on its own while you build the query: copy the inside of "
              "<code class=\"inline\">district_means</code> into a fresh SELECT to check it before you rely on "
              "it. That habit catches most join mistakes early."),
            p("<strong>Try it:</strong> in the CTE query, add <code class=\"inline\">WHERE area = 'Rural'</code> "
              "to both CTEs, so the comparison is rural households only. Remember that the second CTE needs "
              "<code class=\"inline\">h.area</code>."),
        ]},
        {"tab": "Window functions", "title": "Window functions: rank and compare within groups", "blocks": [
            p("<code class=\"inline\">GROUP BY</code> collapses each group to one row. A <strong>window "
              "function</strong> computes across a group but keeps every row. The group is set by "
              "<code class=\"inline\">OVER (PARTITION BY ...)</code>. SQLite has supported window functions "
              "since version 3.25 (2018); the version check in module 1 shows the one running here."),
            h3("Each household against its district mean"),
            sql("SELECT hh_id, district, monthly_pc_exp,\n"
                "       ROUND(AVG(monthly_pc_exp) OVER (PARTITION BY district), 0) AS district_mean,\n"
                "       ROUND(monthly_pc_exp - AVG(monthly_pc_exp) OVER (PARTITION BY district), 0) AS gap\n"
                "FROM households\nORDER BY district, hh_id\nLIMIT 12;"),
            h3("Number the rows within each group"),
            p("<code class=\"inline\">ROW_NUMBER()</code> numbers rows 1, 2, 3 within each partition, in the "
              "order you give. Wrap it in a CTE and keep numbers 1 to 3 to get the three lowest-spending "
              "households in every district: a common first step when drawing a list for a field visit."),
            sql("WITH ranked AS (\n  SELECT hh_id, district, caste, monthly_pc_exp,\n"
                "         ROW_NUMBER() OVER (PARTITION BY district ORDER BY monthly_pc_exp) AS rn\n"
                "  FROM households\n)\nSELECT district, rn, hh_id, caste, monthly_pc_exp\n"
                "FROM ranked\nWHERE rn <= 3\nORDER BY district, rn;"),
            p("Look at Indore: households 59 and 62 both spend 1,640 but get numbers 1 and 2. "
              "<code class=\"inline\">ROW_NUMBER()</code> breaks ties in an order you did not choose, and it "
              "can change between runs or databases. Add a second sort key, <code class=\"inline\">ORDER BY "
              "monthly_pc_exp, hh_id</code>, to make the list repeatable."),
            h3("RANK and ties"),
            p("<code class=\"inline\">RANK()</code> gives tied values the same rank and then skips; "
              "<code class=\"inline\">ROW_NUMBER()</code> never ties. Here the districts are ranked by the share "
              "of households with a bank account, computed in a CTE first."),
            sql("WITH d AS (\n  SELECT district,\n"
                "         ROUND(100.0 * AVG(has_bank_account = 'Yes'), 1) AS pct_bank\n"
                "  FROM households\n  GROUP BY district\n)\n"
                "SELECT district, pct_bank,\n       RANK()       OVER (ORDER BY pct_bank DESC) AS rnk,\n"
                "       ROW_NUMBER() OVER (ORDER BY pct_bank DESC) AS row_num\n"
                "FROM d\nORDER BY rnk, district;"),
            p("Barmer, Kozhikode, Patna and Rewa all have 91.7 per cent, so all four get rank 1 and the next "
              "district, Gaya, gets rank 5. "
              "<code class=\"inline\">DENSE_RANK()</code> does the same without skipping; add it as a third "
              "column and compare."),
            p("<strong>Try it:</strong> in the ROW_NUMBER query, add <code class=\"inline\">DESC</code> after "
              "<code class=\"inline\">monthly_pc_exp</code> inside <code class=\"inline\">OVER (...)</code> to "
              "list the three highest spenders instead. Then partition by <code class=\"inline\">caste</code>."),
        ]},
        {"tab": "NULLs", "title": "Missing values: NULL", "blocks": [
            p("NULL means <em>unknown</em> or <em>not recorded</em>. SQL keeps it apart from zero and from an "
              "empty string, and it follows its own rules. The three teaching tables have no missing values, so this cell "
              "makes a small table that does: a follow-up visit log where some visits recorded no "
              "expenditure. The table is invented."),
            sql("DROP TABLE IF EXISTS followup;\n"
                "CREATE TEMP TABLE followup (hh_id INTEGER, visit_month TEXT, pc_exp_followup INTEGER);\n"
                "INSERT INTO followup VALUES\n  (1, '2026-06', 3400),\n  (2, '2026-06', NULL),\n"
                "  (3, '2026-06', 2900),\n  (4, '2026-06', NULL),\n  (5, '2026-06', 0);\n"
                "SELECT * FROM followup;"),
            h3("Counting and averaging skip NULL"),
            sql("SELECT COUNT(*)               AS visits,\n       COUNT(pc_exp_followup) AS recorded,\n"
                "       AVG(pc_exp_followup)   AS mean_recorded,\n"
                "       SUM(pc_exp_followup) / COUNT(*) AS mean_if_missing_were_zero\nFROM followup;"),
            p("<code class=\"inline\">AVG</code> divides by the 3 recorded values and leaves out the 2 visits with nothing recorded. That is "
              "usually what you want, but say so when you report it: \"mean of 3 households with a recorded "
              "value\". Treating a missing value as zero, as the last column does, pulls the mean down "
              "without any evidence that those households spent nothing."),
            h3("Test for NULL with IS NULL"),
            p("Any comparison with NULL gives NULL, which <code class=\"inline\">WHERE</code> treats as false. "
              "So <code class=\"inline\">= NULL</code> matches nothing. Run this and compare the two counts."),
            sql("SELECT\n  (SELECT COUNT(*) FROM followup WHERE pc_exp_followup = NULL)  AS with_equals,\n"
                "  (SELECT COUNT(*) FROM followup WHERE pc_exp_followup IS NULL) AS with_is_null;"),
            h3("COALESCE and NULLIF"),
            p("<code class=\"inline\">COALESCE(a, b)</code> returns the first value that is not NULL, which is "
              "useful for labels. <code class=\"inline\">NULLIF(x, 0)</code> turns a zero into NULL, which "
              "protects a division from a zero denominator."),
            sql("SELECT hh_id,\n       COALESCE(CAST(pc_exp_followup AS TEXT), 'not recorded') AS shown,\n"
                "       ROUND(1000.0 / NULLIF(pc_exp_followup, 0), 3) AS per_1000\nFROM followup;"),
            info("<strong>Other databases.</strong> SQLite returns NULL when you divide by zero. PostgreSQL and "
                 "SQL Server stop with an error instead, which is why <code class=\"inline\">NULLIF(x, 0)</code> "
                 "is worth writing every time."),
            p("Left joins create NULLs too, as module 5 showed. To find households in the follow-up log "
              "that match nothing in <code class=\"inline\">households</code>, or the other way round, join "
              "and keep the rows where the right-hand key <code class=\"inline\">IS NULL</code>. The next "
              "module uses exactly that."),
            p("<strong>Try it:</strong> add a row with <code class=\"inline\">INSERT INTO followup VALUES (6, "
              "'2026-06', NULL);</code> at the top of the second cell, run it, and check which counts change."),
        ]},
        {"tab": "MIS data", "title": "Working with an MIS export", "blocks": [
            p("Scheme and programme MIS systems hold records as rows: one per beneficiary, per payment, per "
              "visit or per month. When you download an export, you get a table, and the questions you ask "
              "of it are the ones in this course: how many, where, how much, who is missing, which rows "
              "repeat."),
            p("The cell below builds a small export from the households table. Every value in it is "
              "invented, including the amount and the month, and its columns are chosen for teaching: they "
              "do not copy any real portal's layout. Run it first; it reports how many rows it made (93)."),
            sql(MIS_BUILD),
            h3("Check for duplicates before you count anything"),
            p("A payment entered twice inflates every total built on it. Group by the id and keep the groups "
              "that appear more than once."),
            sql("SELECT payment_id, beneficiary_id, COUNT(*) AS copies\nFROM mis_payments\n"
                "GROUP BY payment_id, beneficiary_id\nHAVING COUNT(*) > 1;"),
            p("One payment, number 30 for beneficiary 3, appears twice."),
            h3("Totals by district and status"),
            p("Count distinct beneficiaries as well as rows, so a duplicate cannot pass as an extra person."),
            sql("SELECT district, status,\n       COUNT(*) AS payment_rows,\n"
                "       COUNT(DISTINCT beneficiary_id) AS beneficiaries,\n       SUM(amount) AS amount\n"
                "FROM mis_payments\nGROUP BY district, status\nORDER BY district, status;"),
            p("Rewa shows 11 credited rows but 10 beneficiaries, and 5,500 rupees where the true figure is "
              "5,000. That is the duplicate from the last query. Drop it with "
              "<code class=\"inline\">SELECT DISTINCT</code> in a CTE, or sum over distinct payment ids, before "
              "any total leaves your hands."),
            h3("Reconcile the export with the survey"),
            p("Households that told the survey they received a transfer, but have no credited payment in the "
              "export, are the cases to follow up. A left join from the survey side, keeping rows where the "
              "MIS side is NULL, finds them. This pattern is often called an <em>anti-join</em>."),
            sql("SELECT h.district, COUNT(*) AS reported_but_not_in_mis\nFROM households AS h\n"
                "LEFT JOIN mis_payments AS m\n  ON m.beneficiary_id = h.hh_id AND m.status = 'Credited'\n"
                "WHERE h.received_transfer = 'Yes'\n  AND m.beneficiary_id IS NULL\n"
                "GROUP BY h.district\nORDER BY reported_but_not_in_mis DESC;"),
            p("A gap here has several possible causes, and the query cannot tell them apart: the survey "
              "answer may be wrong, the payment may sit in a month outside the export, or the household may "
              "be missing from the register. The query tells you where to look."),
            info("<strong>Real MIS data is personal data.</strong> A beneficiary export usually carries names, "
                 "phone numbers, bank details or ID numbers. Work with the fewest columns you need, replace "
                 "identifiers with a study id before analysis, and check your obligations under the Digital "
                 "Personal Data Protection Act, 2023. The <a href=\"/101-courses/data-protection-dpdp.html\" "
                 "style=\"color:var(--accent-color)\">Data Protection &amp; the DPDP Act</a> deck covers them.",
                 "warning"),
            p("<strong>Try it:</strong> change the reconciliation to count households that said "
              "<em>No</em> to a transfer but do have a credited payment. You need to flip the survey "
              "condition and change <code class=\"inline\">IS NULL</code> to <code class=\"inline\">IS NOT NULL</code>."),
        ]},
    ],
    "next": [
        {"href": "/code/shiny.html", "title": "Shiny Dashboards for Development Data",
         "desc": "Put a summary like the ones above into an interactive dashboard, in R or Python."},
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "Do the same grouping and joining with data frames, and add charts and regression."},
        {"href": "/101-courses/data-lit.html", "title": "Data Literacy 101",
         "desc": "Reading numbers critically before you query them."},
        {"href": "/101-courses/eda-hhs.html", "title": "Exploratory Data Analysis 101",
         "desc": "What to look for first in a household survey."},
        {"href": "/101-courses/data-protection-dpdp.html", "title": "Data Protection &amp; the DPDP Act 101",
         "desc": "Handling beneficiary and survey records lawfully."},
    ],
}

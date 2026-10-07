# -*- coding: utf-8 -*-
"""Power BI for M&E Dashboards: a guided course in Power Query M and DAX, with R cells that check each number here.

Facts checked on 7 October 2026 against Microsoft Learn: "Download Power BI Desktop" (requirements, monthly
releases, Store and installer), the Power BI pricing page (Pro US$14, Premium Per User US$24, per user per month,
billed yearly), "Power BI Desktop projects (PBIP)", "Publish to web from Power BI" (the public-access warning),
the DAX reference for DIVIDE and the Power Query M reference for Table.UnpivotOtherColumns. Every R cell was run
in a browser through WebR on 7 October 2026.
"""

PAGE = {'slug': 'powerbi',
 'order': 17.5,
 'kind': 'guide',
 'tool': 'Power BI',
 'title': 'Power BI for M&E Dashboards',
 'h1': 'Power BI for M&amp;E dashboards',
 'lede': 'Build a district dashboard in Power BI Desktop from two survey files: clean them in Power Query, '
         'model one district to many households, write DAX measures for coverage rates and weighted means, '
         'and publish a report that is accessible and does not leak the data behind it. Follow along in your '
         'own copy of Power BI Desktop, and check every number in R on this page.',
 'description': 'A free guided course in Power BI Desktop for development practitioners in South Asia: Power '
                'Query and M for cleaning survey exports, a district and household data model, DAX measures, '
                'CALCULATE and filter context, population-weighted means with SUMX, accessible report pages, '
                'safe sharing and Power BI project files for Git.',
 'card': 'Power Query M to clean a survey export, a district model, DAX measures and CALCULATE, weighted '
         'means, and sharing without leaking data.',
 'datasets': ['households', 'districts'],
 'engine_note': '<strong>Power BI does not run in a browser tab.</strong> The grey boxes are Power Query M '
                'and DAX for you to type into your own Power BI Desktop, which runs on Windows. This page '
                'does not show Power BI output, because it cannot produce any; each module tells you what to '
                'look for on your screen instead. Where the same number can be computed in R, an R cell '
                'computes it here on the same data, so you can check your cards and tables against it. The '
                'first R run downloads the R engine once (about 7&nbsp;MB).',
 'modules': [{'tab': 'Set up',
              'title': 'Power BI Desktop, the service and your project folder',
              'blocks': [{'t': 'html',
                          'html': "<p>Power BI is Microsoft's business intelligence software. Most M&amp;E "
                                  'teams meet it as the tool behind a donor dashboard: a page of indicator '
                                  'cards, a district map and a few slicers. Two parts matter. <strong>Power '
                                  'BI Desktop</strong> is the free Windows application in which you load '
                                  'data, build the model, write the formulas and design the report. The '
                                  '<strong>Power BI service</strong> (app.powerbi.com) is where a report is '
                                  'published, refreshed and shared.</p>\n'
                                  '<div class="info-box"><strong>Cost and requirements, checked 7 October '
                                  '2026.</strong> Microsoft offers Power BI Desktop as a free download from '
                                  'the Microsoft Store or as a 64-bit installer. It needs Windows 10, '
                                  'Windows Server 2016 or later, at least 2&nbsp;GB of free memory '
                                  '(4&nbsp;GB recommended) and a screen of at least 1440x900. There is no '
                                  'Mac version; Microsoft supports Desktop on Azure Virtual Desktop and '
                                  'Windows 365, which is one route for Mac users. Microsoft releases a new '
                                  'version every month and supports only the latest. Sharing is what costs '
                                  "money: Microsoft's <a "
                                  'href="https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing" '
                                  'rel="noopener" target="_blank" style="color:var(--accent-color)">pricing '
                                  'page</a> lists Power BI Pro at US$14 per user per month and Premium Per '
                                  'User at US$24 (both billed yearly), and says the free account must '
                                  'upgrade to share reports. Ask your organisation first; many already pay '
                                  'for Microsoft 365 licences that include Pro.</div>\n'
                                  '<h3>Two languages, two jobs</h3>\n'
                                  '<p>Power BI has two formula languages, and most confusion comes from '
                                  'mixing them up.</p>\n'
                                  '<ul><li><strong>M</strong> is the language of Power Query, the editor '
                                  'that gets and cleans data <em>before</em> it reaches the model. Every '
                                  'click in Power Query writes a line of M. It runs when the data is '
                                  'refreshed.</li><li><strong>DAX</strong> (Data Analysis Expressions) is '
                                  'the language of the model. You use it to write measures, the numbers on '
                                  'your report, such as coverage rates and means. It runs every time a '
                                  'reader clicks a slicer.</li></ul>\n'
                                  '<p>The rule of thumb: shape and clean in M, calculate in DAX.</p>\n'
                                  '<h3>Set up the course folder</h3>\n'
                                  '<ol class="guide-steps"><li>Install Power BI Desktop from the <a '
                                  'href="https://aka.ms/pbidesktopstore" rel="noopener" target="_blank" '
                                  'style="color:var(--accent-color)">Microsoft Store</a> (updates arrive by '
                                  'themselves, and you do not need administrator rights) or the <a '
                                  'href="https://www.microsoft.com/download/details.aspx?id=58494" '
                                  'rel="noopener" target="_blank" style="color:var(--accent-color)">Download '
                                  'Center</a>.</li><li>Make a project folder with a short path, for example '
                                  '<code class="inline">C:\\impactmojo\\powerbi</code>.</li><li>Download the '
                                  'two course files into it: <a href="/code/data/households.csv" download '
                                  'style="color:var(--accent-color)">households.csv</a> (240 households) and '
                                  '<a href="/code/data/districts.csv" download '
                                  'style="color:var(--accent-color)">districts.csv</a> (10 districts). <span '
                                  'class="illustrative-tag">Illustrative data, invented for teaching</span> '
                                  'The district names are real places; every number is made up.</li><li>Open '
                                  'Power BI Desktop, close the start screen and choose <strong>File &gt; '
                                  'Save as</strong>. Save as type <strong>Power BI project files '
                                  '(*.pbip)</strong> and name it <code '
                                  'class="inline">mne_dashboard</code>.</li></ol>\n'
                                  '<p>A <code class="inline">.pbix</code> file is one closed package. A '
                                  'Power BI project saves the same report as a folder of plain text files: '
                                  '<code class="inline">mne_dashboard.pbip</code>, a <code '
                                  'class="inline">mne_dashboard.Report</code> folder and a <code '
                                  'class="inline">mne_dashboard.SemanticModel</code> folder, plus a <code '
                                  'class="inline">.gitignore</code>. Text files can be compared line by line '
                                  'and kept in Git, so you can see which measure changed between the June '
                                  'and the September dashboard. You can convert back to <code '
                                  'class="inline">.pbix</code> at any time with <strong>File &gt; Save '
                                  'as</strong>.</p>\n'
                                  '<div class="info-box"><strong>Exercise.</strong> After saving, open the '
                                  'project folder in File Explorer. Find the <code '
                                  'class="inline">.gitignore</code> file Power BI wrote, open it in Notepad '
                                  'and note which two files it keeps out of Git: the local settings and the '
                                  'data cache.</div>'}]},
             {'tab': 'Get data',
              'title': 'Get data and read the M that Power Query writes',
              'blocks': [{'t': 'html',
                          'html': '<p>Every dataset enters Power BI through <strong>Get data</strong>. For a '
                                  'CSV the steps are the same whether it came from KoboToolbox, an MIS '
                                  'export or a government portal.</p>\n'
                                  '<ol class="guide-steps"><li>On the <strong>Home</strong> ribbon choose '
                                  '<strong>Get data &gt; Text/CSV</strong> and pick <code '
                                  'class="inline">households.csv</code>.</li><li>A preview opens. Do '
                                  '<em>not</em> press Load. Press <strong>Transform data</strong>, which '
                                  'opens the Power Query Editor.</li><li>Repeat for <code '
                                  'class="inline">districts.csv</code>. Both now appear under '
                                  '<strong>Queries</strong> on the left.</li></ol>\n'
                                  '<p>Look at the <strong>Applied steps</strong> pane on the right. Power '
                                  'Query has already taken three steps for you: <em>Source</em>, '
                                  '<em>Promoted Headers</em> and <em>Changed Type</em>. Open <strong>Home '
                                  '&gt; Advanced Editor</strong> to see them as M. It will look much like '
                                  'this; your file path, and possibly the encoding number, will differ.</p>'},
                         {'t': 'syntax',
                          'label': 'Power Query M: households (as generated, abridged)',
                          'code': 'let\n'
                                  '    Source = '
                                  'Csv.Document(File.Contents("C:\\impactmojo\\powerbi\\households.csv"),\n'
                                  '        [Delimiter = ",", Columns = 13, Encoding = 65001, QuoteStyle = '
                                  'QuoteStyle.None]),\n'
                                  '    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars '
                                  '= true]),\n'
                                  '    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers", {\n'
                                  '        {"hh_id", Int64.Type}, {"district", type text}, {"area", type '
                                  'text},\n'
                                  '        {"caste", type text}, {"head_edu_years", Int64.Type}, {"hh_size", '
                                  'Int64.Type},\n'
                                  '        {"monthly_pc_exp", Int64.Type}, {"land_acres", type number},\n'
                                  '        {"has_toilet", type text}, {"has_bank_account", type text}})\n'
                                  'in\n'
                                  '    #"Changed Type"'},
                         {'t': 'html',
                          'html': '<h3>How to read it</h3>\n'
                                  '<ul><li>An M query is a <code class="inline">let ... in</code> '
                                  'expression. Each line names a step and refers to the step before it. The '
                                  'name after <code class="inline">in</code> is what the query '
                                  'returns.</li><li>A step name with a space is written <code '
                                  'class="inline">#&quot;Changed Type&quot;</code>.</li><li><code '
                                  'class="inline">Columns = 13</code> is fixed at the moment of import. If '
                                  "next month's export has a fourteenth column, the extra column is silently "
                                  'dropped. Delete <code class="inline">Columns = 13,</code> from that line '
                                  'if your exports change shape.</li><li>The automatic type step guesses '
                                  "from the first rows. Check every column's icon in the header: <code "
                                  'class="inline">123</code> for whole numbers, <code '
                                  'class="inline">1.2</code> for decimals, <code class="inline">ABC</code> '
                                  'for text. An ID stored as a number loses its leading zeros, so a village '
                                  'code <code class="inline">0042</code> becomes <code '
                                  'class="inline">42</code>. Set such columns to text.</li></ul>\n'
                                  '<p>The same import and type check in R, on the same file, runs here. Use '
                                  'it to confirm the row and column counts Power Query shows in its status '
                                  'bar.</p>'},
                         {'t': 'code',
                          'lang': 'r',
                          'code': 'hh <- read.csv("households.csv")\n'
                                  'dim(hh)          # rows, columns: compare with the Power Query status '
                                  'bar\n'
                                  "str(hh)          # int, num and chr are Power Query's whole number, "
                                  'decimal and text\n'
                                  'd <- read.csv("districts.csv")\n'
                                  'd'},
                         {'t': 'html',
                          'html': '<div class="info-box"><strong>Exercise.</strong> In Power Query, click '
                                  'the <em>Changed Type</em> step and change <code '
                                  'class="inline">land_acres</code> to <strong>Whole number</strong>. Look '
                                  'at what happens to the values, then delete your change from Applied '
                                  'steps. A wrong type does not raise an error; it rounds your '
                                  'data.</div>'}]},
             {'tab': 'Clean in Power Query',
              'title': 'Clean in Power Query: indicators, bands and a district table',
              'blocks': [{'t': 'html',
                          'html': '<p>Survey exports arrive with Yes/No text, raw years of schooling and '
                                  'stray spaces. Fix them in Power Query, once, so every measure downstream '
                                  'starts from clean columns. Each step below can be done with a menu, and '
                                  'the menu writes the M shown.</p>\n'
                                  '<h3>Yes/No to 1/0</h3>\n'
                                  '<p>Select the households query, then <strong>Add Column &gt; Custom '
                                  'column</strong>. Name it <code class="inline">toilet</code> and enter the '
                                  'formula below. Repeat for <code class="inline">bank</code>.</p>'},
                         {'t': 'syntax',
                          'label': 'Power Query M: custom columns',
                          'code': '#"Added toilet" = Table.AddColumn(#"Changed Type", "toilet",\n'
                                  '    each if [has_toilet] = "Yes" then 1 else 0, Int64.Type),\n'
                                  '#"Added bank" = Table.AddColumn(#"Added toilet", "bank",\n'
                                  '    each if [has_bank_account] = "Yes" then 1 else 0, Int64.Type)'},
                         {'t': 'html',
                          'html': '<p><code class="inline">each</code> means "for each row", and <code '
                                  'class="inline">[has_toilet]</code> is that row\'s value. The last '
                                  "argument sets the new column's type, so the column arrives as a whole "
                                  'number and not as type <code class="inline">any</code>.</p>\n'
                                  '<h3>Education bands</h3>'},
                         {'t': 'syntax',
                          'label': 'Power Query M: a banded column',
                          'code': '#"Added edu band" = Table.AddColumn(#"Added bank", "edu_band",\n'
                                  '    each if [head_edu_years] = 0 then "None"\n'
                                  '    else if [head_edu_years] <= 5 then "Primary (1-5)"\n'
                                  '    else if [head_edu_years] <= 10 then "Secondary (6-10)"\n'
                                  '    else "Higher (11+)", type text)'},
                         {'t': 'html',
                          'html': '<h3>Tidy text keys before you join on them</h3>\n'
                                  '<p>District names typed by hand carry trailing spaces and mixed case, and '
                                  '<code class="inline">&quot;Gaya &quot;</code> will not match <code '
                                  'class="inline">&quot;Gaya&quot;</code> in a relationship. Select the '
                                  '<code class="inline">district</code> column in <em>both</em> queries and '
                                  'choose <strong>Transform &gt; Format &gt; Trim</strong>.</p>'},
                         {'t': 'syntax',
                          'label': 'Power Query M: trim',
                          'code': '#"Trimmed district" = Table.TransformColumns(#"Added edu band", '
                                  '{{"district", Text.Trim, type text}})'},
                         {'t': 'html',
                          'html': '<h3>A district summary with Group By</h3>\n'
                                  '<p>To build a separate one-row-per-district table (for export, or to '
                                  'check totals), right-click the households query, choose '
                                  '<strong>Reference</strong>, then <strong>Transform &gt; Group '
                                  'By</strong>, Advanced.</p>'},
                         {'t': 'syntax',
                          'label': 'Power Query M: Group By',
                          'code': 'let\n'
                                  '    Source = households,\n'
                                  '    Grouped = Table.Group(Source, {"district"}, {\n'
                                  '        {"households", each Table.RowCount(_), Int64.Type},\n'
                                  '        {"toilet_rate", each List.Average([toilet]), type number},\n'
                                  '        {"mean_pc_exp", each List.Average([monthly_pc_exp]), type '
                                  'number}})\n'
                                  'in\n'
                                  '    Grouped'},
                         {'t': 'html',
                          'html': '<p>The R version of the indicator, the bands and the district table. '
                                  'Check the district counts against your Group By result.</p>'},
                         {'t': 'code',
                          'lang': 'r',
                          'code': 'hh <- read.csv("households.csv")\n'
                                  'hh$toilet <- as.integer(hh$has_toilet == "Yes")\n'
                                  'hh$edu_band <- cut(hh$head_edu_years, breaks = c(-Inf, 0, 5, 10, Inf),\n'
                                  '                   labels = c("None", "Primary (1-5)", "Secondary '
                                  '(6-10)", "Higher (11+)"))\n'
                                  'table(hh$edu_band)\n'
                                  'aggregate(cbind(toilet, monthly_pc_exp) ~ district, data = hh, FUN = '
                                  'mean)\n'
                                  'table(hh$district)'},
                         {'t': 'html',
                          'html': '<div class="info-box"><strong>Exercise.</strong> Add a column <code '
                                  'class="inline">shg</code> that is 1 when <code '
                                  'class="inline">shg_member</code> is "Yes". Then right-click the <code '
                                  'class="inline">has_toilet</code> column and choose '
                                  '<strong>Remove</strong>: you no longer need the text once the 1/0 column '
                                  'exists. Close Power Query with <strong>Home &gt; Close &amp; '
                                  'Apply</strong>.</div>'}]},
             {'tab': 'The data model',
              'title': 'The data model: one district, many households',
              'blocks': [{'t': 'html',
                          'html': '<p>A Power BI report is only as right as its model. The model for most '
                                  'survey dashboards is a <strong>star schema</strong>: one <em>fact</em> '
                                  'table with a row per unit observed (here, households), and '
                                  '<em>dimension</em> tables that describe something the facts belong to '
                                  '(here, districts). Facts carry numbers to add up; dimensions carry the '
                                  'labels you slice by.</p>\n'
                                  '<ol class="guide-steps"><li>Open <strong>Model view</strong> (the third '
                                  'icon on the left edge).</li><li>Power BI may already have drawn a line '
                                  'between the two tables on <code class="inline">district</code>. If not, '
                                  'drag <code class="inline">district</code> from <em>districts</em> onto '
                                  '<code class="inline">district</code> in '
                                  '<em>households</em>.</li><li>Double-click the line. Check that '
                                  '<strong>Cardinality</strong> reads <em>Many to one (*:1)</em> from '
                                  'households to districts, and <strong>Cross filter direction</strong> '
                                  'reads <em>Single</em>.</li></ol>\n'
                                  '<ul><li><strong>Many to one</strong> says each household belongs to one '
                                  'district and each district has many households. If Power BI proposes '
                                  '<em>many to many</em>, the districts table has a duplicate district, '
                                  'which is a data problem. Fix it in Power Query before you go '
                                  'on.</li><li><strong>Single</strong> direction means a slicer on districts '
                                  'filters households, and not the other way. Leave it single unless you can '
                                  'say why you need both; two-way filters make totals hard to '
                                  'explain.</li><li>Slice by the column on the <em>one</em> side. Put <code '
                                  'class="inline">districts[state]</code> and <code '
                                  'class="inline">districts[district]</code> in slicers, and hide <code '
                                  'class="inline">households[district]</code> (right-click, <strong>Hide in '
                                  'report view</strong>) so nobody slices by the wrong copy.</li></ul>\n'
                                  '<h3>Wide indicator sheets: unpivot before you load</h3>\n'
                                  '<p>Programme teams often keep indicators one column per round: <code '
                                  'class="inline">district, baseline, midline, endline</code>. Power BI '
                                  'wants one column for the round and one for the value, so a single line '
                                  'chart can draw all three. Select <code class="inline">district</code>, '
                                  'then <strong>Transform &gt; Unpivot Columns &gt; Unpivot Other '
                                  'Columns</strong>.</p>'},
                         {'t': 'syntax',
                          'label': 'Power Query M: unpivot',
                          'code': '#"Unpivoted" = Table.UnpivotOtherColumns(Source, {"district"}, "round", '
                                  '"value")'},
                         {'t': 'html',
                          'html': '<p><code class="inline">Table.UnpivotOtherColumns(table, pivotColumns, '
                                  'attributeColumn, valueColumn)</code> keeps the columns you name and turns '
                                  'every other column into round/value pairs. "Other columns" matters: when '
                                  'an endline column is added next year, it is unpivoted too, with no change '
                                  'to the query.</p>\n'
                                  '<p>In R, <code class="inline">merge()</code> does what the relationship '
                                  'does, and the <code class="inline">all.x</code> check tells you whether '
                                  'any household failed to find its district.</p>'},
                         {'t': 'code',
                          'lang': 'r',
                          'code': 'hh <- read.csv("households.csv")\n'
                                  'd  <- read.csv("districts.csv")\n'
                                  'anyDuplicated(d$district)                 # 0 means the one side really '
                                  'is one\n'
                                  'm <- merge(hh, d, by = "district", all.x = TRUE)\n'
                                  'sum(is.na(m$state))                       # households with no matching '
                                  'district\n'
                                  'table(m$state)'},
                         {'t': 'html',
                          'html': '<div class="info-box"><strong>Exercise.</strong> In <em>Report view</em>, '
                                  'put a <strong>Table</strong> visual on the page with <code '
                                  'class="inline">districts[state]</code> and a count of <code '
                                  'class="inline">households[hh_id]</code>. The counts should add to 240. If '
                                  "a row reads <em>(Blank)</em>, some household's district has no match in "
                                  'the districts table.</div>'}]},
             {'tab': 'Measures',
              'title': 'DAX measures, and why a rate is never a column',
              'blocks': [{'t': 'html',
                          'html': '<p>DAX gives you two ways to calculate. A <strong>calculated '
                                  'column</strong> is worked out once per row when the data loads, and '
                                  'stored. A <strong>measure</strong> is worked out when a visual asks for '
                                  "it, for whatever rows the reader's slicers leave in play. Indicators on a "
                                  'dashboard (rates, means, counts) are measures.</p>\n'
                                  '<ol class="guide-steps"><li>In <em>Report view</em> select the households '
                                  'table in the <strong>Data</strong> pane, then <strong>Home &gt; New '
                                  'measure</strong>.</li><li>Type each measure below into the formula bar '
                                  'and press Enter. Each one is a separate measure.</li><li>Set the format '
                                  'on the <strong>Measure tools</strong> ribbon: percentage for the rate, '
                                  'whole number for the count.</li></ol>'},
                         {'t': 'syntax',
                          'label': 'DAX: first measures (each line is one measure)',
                          'code': 'Households = COUNTROWS ( households )\n'
                                  '\n'
                                  'Toilet coverage = DIVIDE ( SUM ( households[toilet] ), [Households] )\n'
                                  '\n'
                                  'Mean MPCE = AVERAGE ( households[monthly_pc_exp] )\n'
                                  '\n'
                                  'Bank account rate = DIVIDE ( SUM ( households[bank] ), [Households] )'},
                         {'t': 'html',
                          'html': '<ul><li><code class="inline">DIVIDE(numerator, denominator [, '
                                  'alternateresult])</code> returns BLANK, or your alternate result, when '
                                  'the denominator is zero. With the <code class="inline">/</code> operator '
                                  'a district with no households would show an error in the middle of your '
                                  'dashboard.</li><li><code class="inline">[Households]</code> reuses a '
                                  'measure inside another. Define the denominator once and every rate that '
                                  'uses it stays consistent.</li><li>Put the table name before the column '
                                  '(<code class="inline">households[toilet]</code>) and not before a measure '
                                  '(<code class="inline">[Households]</code>). That convention tells a '
                                  'reader at a glance which is which.</li></ul>\n'
                                  '<h3>Why the rate must be a measure</h3>\n'
                                  '<p>Suppose you stored coverage as a column of group rates and let the '
                                  'total row average them. That gives every group equal weight, so a '
                                  'district of 20 households would count as much as one of 2,000. The '
                                  'measure above divides total toilets by total households for whatever is '
                                  'selected, so the total row is the true pooled rate.</p>\n'
                                  '<p>In the course file every district has 24 households, so for districts '
                                  'the two answers happen to agree. Rural and urban households are unequal '
                                  'groups (164 and 76), and there they part company. The R cell shows '
                                  'both.</p>'},
                         {'t': 'code',
                          'lang': 'r',
                          'code': 'hh <- read.csv("households.csv")\n'
                                  'hh$toilet <- as.integer(hh$has_toilet == "Yes")\n'
                                  'table(hh$area)                          # unequal groups\n'
                                  'rates <- tapply(hh$toilet, hh$area, mean)\n'
                                  'rates\n'
                                  'mean(rates)          # average of the two area rates: the wrong total\n'
                                  'mean(hh$toilet)      # pooled rate: what the DAX measure shows in the '
                                  'total row'},
                         {'t': 'html',
                          'html': '<h3>When a calculated column is right</h3>\n'
                                  '<p>Use a column for something you will slice <em>by</em>, which belongs '
                                  'to one row and does not change with the filters. An expenditure band is '
                                  'one.</p>'},
                         {'t': 'syntax',
                          'label': 'DAX: a calculated column (Table tools > New column)',
                          'code': 'MPCE band =\n'
                                  'SWITCH (\n'
                                  '    TRUE (),\n'
                                  '    households[monthly_pc_exp] < 2000, "Under 2,000",\n'
                                  '    households[monthly_pc_exp] < 4000, "2,000 to 3,999",\n'
                                  '    "4,000 and above"\n'
                                  ')'},
                         {'t': 'html',
                          'html': '<p><code class="inline">SWITCH(TRUE(), ...)</code> tests each condition '
                                  'in order and returns the first that holds, so the bands cannot '
                                  'overlap.</p>\n'
                                  '<div class="info-box"><strong>Exercise.</strong> Make a '
                                  '<strong>Matrix</strong> visual with <code '
                                  'class="inline">households[area]</code> on rows and the measures <code '
                                  'class="inline">[Households]</code> and <code class="inline">[Toilet '
                                  'coverage]</code>. Read the total row, then compare it with the two '
                                  'numbers the R cell printed.</div>'}]},
             {'tab': 'CALCULATE',
              'title': 'CALCULATE and filter context',
              'blocks': [{'t': 'html',
                          'html': '<p>Every number in a visual is computed under a <strong>filter '
                                  'context</strong>: the set of filters from the row it sits in, the slicers '
                                  'on the page and any page or report filters. <code '
                                  'class="inline">CALCULATE</code> evaluates an expression under a filter '
                                  'context you change. It is the most used function in DAX and the one that '
                                  'explains almost every "why does my total look wrong" question.</p>'},
                         {'t': 'syntax',
                          'label': 'DAX: CALCULATE',
                          'code': 'Rural households = CALCULATE ( [Households], households[area] = "Rural" '
                                  ')\n'
                                  '\n'
                                  'Rural toilet coverage = CALCULATE ( [Toilet coverage], households[area] = '
                                  '"Rural" )\n'
                                  '\n'
                                  'SC/ST households =\n'
                                  'CALCULATE ( [Households], households[caste] IN { "SC", "ST" } )'},
                         {'t': 'html',
                          'html': '<p>A filter argument such as <code class="inline">households[area] = '
                                  '&quot;Rural&quot;</code> replaces any filter already on that column. Put '
                                  '<code class="inline">[Rural households]</code> in a matrix by area and '
                                  'the Urban row also shows the rural count, because the measure overrides '
                                  "the row's own filter. Wrap the filter in <code "
                                  'class="inline">KEEPFILTERS( )</code> when you want it to intersect with '
                                  'the row instead.</p>\n'
                                  '<h3>Share of the total</h3>\n'
                                  "<p>To show each district's share of all households, the denominator must "
                                  'ignore the district filter. <code class="inline">REMOVEFILTERS</code> (or '
                                  'the older <code class="inline">ALL</code>) clears it.</p>'},
                         {'t': 'syntax',
                          'label': 'DAX: share of total',
                          'code': 'Share of households =\n'
                                  'DIVIDE ( [Households], CALCULATE ( [Households], REMOVEFILTERS ( '
                                  'districts ) ) )'},
                         {'t': 'html',
                          'html': '<p><code class="inline">REMOVEFILTERS ( districts )</code> clears filters '
                                  'from every column of the districts table, so the share still sums to 100% '
                                  'when the reader also slices by state. A state slicer would still filter '
                                  'the numerator; decide whether your share is "of the state" or "of the '
                                  'whole sample", and write it into the visual title.</p>\n'
                                  '<h3>Reading the selection</h3>'},
                         {'t': 'syntax',
                          'label': 'DAX: a dynamic title',
                          'code': 'Selected district title =\n'
                                  '"Toilet coverage, " & SELECTEDVALUE ( districts[district], "all '
                                  'districts" )'},
                         {'t': 'html',
                          'html': '<p><code class="inline">SELECTEDVALUE</code> returns the value when '
                                  'exactly one is selected and the alternate text otherwise. Use it as a '
                                  'card or as a visual title (Format pane, <strong>Title &gt; fx</strong>) '
                                  'so a screenshot sent on WhatsApp still says what it shows.</p>\n'
                                  '<p>The same three numbers in R, to check your cards against:</p>'},
                         {'t': 'code',
                          'lang': 'r',
                          'code': 'hh <- read.csv("households.csv")\n'
                                  'hh$toilet <- as.integer(hh$has_toilet == "Yes")\n'
                                  'sum(hh$area == "Rural")                          # Rural households\n'
                                  'mean(hh$toilet[hh$area == "Rural"])              # Rural toilet coverage\n'
                                  'round(100 * prop.table(table(hh$district)), 1)   # Share of households, '
                                  '%'},
                         {'t': 'html',
                          'html': '<div class="info-box"><strong>Exercise.</strong> Make a measure <code '
                                  'class="inline">Urban toilet coverage</code> and a third measure for the '
                                  'rural minus urban gap, written as <code class="inline">[Rural toilet '
                                  'coverage] - [Urban toilet coverage]</code>. Put all three in a matrix by '
                                  'state and check one state by hand in the R cell.</div>'}]},
             {'tab': 'Weighted figures',
              'title': 'Population-weighted figures with SUMX',
              'blocks': [{'t': 'html',
                          'html': '<p><code class="inline">Mean MPCE</code> from Module 5 averages over '
                                  'households: every household counts once, whether it has two members or '
                                  'nine. A per-person figure, the mean expenditure of the average '
                                  "<em>person</em>, weights each household by its size. DAX's iterators do "
                                  'this: <code class="inline">SUMX(table, expression)</code> evaluates the '
                                  'expression row by row and adds the results.</p>'},
                         {'t': 'syntax',
                          'label': 'DAX: a population-weighted mean',
                          'code': 'Persons = SUM ( households[hh_size] )\n'
                                  '\n'
                                  'Mean MPCE per person =\n'
                                  'DIVIDE (\n'
                                  '    SUMX ( households, households[monthly_pc_exp] * households[hh_size] '
                                  '),\n'
                                  '    [Persons]\n'
                                  ')'},
                         {'t': 'html',
                          'html': '<p>The same pattern takes any weight. If your file carries a survey '
                                  'weight column, as NFHS and PLFS unit-level files do, replace <code '
                                  'class="inline">households[hh_size]</code> with it in both places.</p>\n'
                                  '<div class="info-box warning"><strong>Weights give the right estimate. '
                                  'Its uncertainty needs survey software.</strong> SUMX gives a correctly '
                                  'weighted point estimate. Power BI has no survey design features, so it '
                                  'cannot give a standard error or confidence interval that allows for '
                                  'stratification and clustering. If your dashboard reports estimates from a '
                                  'sample survey, compute the intervals in Stata (<code '
                                  'class="inline">svy:</code>), R (<code class="inline">survey</code>) or '
                                  'SPSS Complex Samples, bring them in as a table, and show them beside the '
                                  'estimate. Do not let a dashboard imply that a district difference of two '
                                  'points is real when the interval is ten points wide.</div>\n'
                                  '<p>Check both means in R. If larger households here spend less per head, '
                                  'the weighted mean comes out lower, because those households now count '
                                  'once for each member.</p>'},
                         {'t': 'code',
                          'lang': 'r',
                          'code': 'hh <- read.csv("households.csv")\n'
                                  'mean(hh$monthly_pc_exp)                               # Mean MPCE '
                                  '(households)\n'
                                  'weighted.mean(hh$monthly_pc_exp, w = hh$hh_size)      # Mean MPCE per '
                                  'person\n'
                                  'sum(hh$hh_size)                                       # Persons'},
                         {'t': 'html',
                          'html': '<h3>Iterators and the total row</h3>\n'
                                  '<p><code class="inline">SUMX</code>, <code class="inline">AVERAGEX</code> '
                                  'and their relatives loop over whatever rows the filter context leaves. '
                                  'That is why the total row of a matrix is computed afresh over all rows, '
                                  'never by adding up the rows above it. For a sum the two agree; for a mean '
                                  'or a rate they do not, and the fresh computation is the correct one.</p>\n'
                                  '<div class="info-box"><strong>Exercise.</strong> Add <code '
                                  'class="inline">[Mean MPCE]</code> and <code class="inline">[Mean MPCE per '
                                  'person]</code> to the matrix by district. In which districts do they '
                                  'differ most? Check one in the R cell with <code class="inline">subset(hh, '
                                  'district == &quot;Purnia&quot;)</code>.</div>'}]},
             {'tab': 'Report and share',
              'title': 'A report people can read, and sharing it safely',
              'blocks': [{'t': 'html',
                          'html': '<p>A dashboard is read by a district officer on a phone, a programme '
                                  'manager on a projector and a donor in a PDF. Build for all three.</p>\n'
                                  '<h3>Page design</h3>\n'
                                  '<ul><li>Put the three or four headline measures as <strong>Card</strong> '
                                  'visuals across the top, each with a title that says the unit ("Households '
                                  'with a toilet, %").</li><li>Use a bar chart, sorted by value, for '
                                  "comparing districts. Sort by clicking the visual's <strong>More options "
                                  '(...) &gt; Sort axis</strong>. A pie chart with ten districts cannot be '
                                  'read.</li><li>Keep slicers for state, area and caste group in one place '
                                  'on the page, and add the dynamic title from Module 6 so every visual says '
                                  'what selection it shows.</li><li>Show the sample size. A card for <code '
                                  'class="inline">[Households]</code> beside the rates stops a reader '
                                  'trusting a rate computed on six households.</li></ul>\n'
                                  '<h3>Accessibility</h3>\n'
                                  '<ul><li>Give every visual <strong>Alt text</strong> (Format pane, '
                                  '<strong>General &gt; Alt text</strong>). A screen reader reads it in '
                                  'place of the chart. It accepts a DAX measure, so the alt text can state '
                                  'the current value.</li><li>Set the keyboard order in <strong>View &gt; '
                                  'Selection</strong>, on the <strong>Tab order</strong> tab, so it follows '
                                  'the reading order of the page.</li><li>Never use colour alone to carry '
                                  'meaning. If red means "below target", say so in the label or a data label '
                                  'too.</li></ul>\n'
                                  '<h3>Sharing: the one setting that can leak a dataset</h3>\n'
                                  '<div class="info-box warning"><strong>Publish to web makes a report '
                                  "public.</strong> Microsoft's documentation says that anyone on the "
                                  'internet can view a report published this way, with no sign-in, and that '
                                  'this includes detail-level data the report aggregates: anyone can reach '
                                  'the underlying data in the model even if no visual shows it. A household '
                                  'survey with names, phone numbers or GPS points must never be published '
                                  'this way, even if the visuals show only district totals. Remove personal '
                                  'identifiers in Power Query before the data reaches the model, and share '
                                  'through a workspace, an app or a secure embed instead.</div>\n'
                                  '<p>To publish, choose <strong>Home &gt; Publish</strong> and pick a '
                                  'workspace. Colleagues need access to that workspace or an app built from '
                                  "it, and both you and they need the licence your organisation's workspace "
                                  'requires. Schedule refresh in the service only when the source is '
                                  'somewhere the service can reach, such as SharePoint or a database; a CSV '
                                  'on your laptop cannot refresh on its own.</p>\n'
                                  '<h3>Version control</h3>\n'
                                  '<p>Because you saved as a Power BI project in Module 1, the model is '
                                  'stored as text. Put the project folder in a Git repository (the <a '
                                  'href="/code/git-quarto.html" style="color:var(--accent-color)">Git and '
                                  'Quarto course</a> covers the commands) and commit after each working '
                                  'change. A diff then shows exactly which measure definition changed '
                                  'between two versions of a donor report. Keep raw survey files out of the '
                                  'repository; the <code class="inline">.gitignore</code> Power BI wrote '
                                  'keeps out its data cache, and you should add your data files to it as '
                                  'well.</p>\n'
                                  '<div class="info-box"><strong>Exercise.</strong> Build one page: three '
                                  'cards, a sorted bar chart of <code class="inline">[Toilet '
                                  'coverage]</code> by district, slicers for state and area, a dynamic '
                                  'title, and alt text on every visual. Then press Tab from the top of the '
                                  'page and check that focus moves in the order you read.</div>\n'
                                  "<h3>Microsoft's own documentation</h3>\n"
                                  '<ul><li><a '
                                  'href="https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop" '
                                  'rel="noopener" target="_blank" style="color:var(--accent-color)">Download '
                                  'Power BI Desktop</a>, with the system requirements.</li><li><a '
                                  'href="https://learn.microsoft.com/en-us/powerquery-m/" rel="noopener" '
                                  'target="_blank" style="color:var(--accent-color)">Power Query M function '
                                  'reference</a> and <a href="https://learn.microsoft.com/en-us/dax/" '
                                  'rel="noopener" target="_blank" style="color:var(--accent-color)">DAX '
                                  'function reference</a>.</li><li><a '
                                  'href="https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview" '
                                  'rel="noopener" target="_blank" style="color:var(--accent-color)">Power BI '
                                  'Desktop projects (PBIP)</a>.</li><li><a '
                                  'href="https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-publish-to-web" '
                                  'rel="noopener" target="_blank" style="color:var(--accent-color)">Publish '
                                  'to web</a>, including the warning quoted above.</li></ul>'}]}],
 'next': [{'href': '/courses/powerBI/powerbi.html',
           'title': 'Power BI flagship course',
           'desc': 'Eight modules with labs on NFHS, ASER and World Bank data, and where the free version '
                   'stops.'},
          {'href': '/courses/powerBI/lexicon.html',
           'title': 'Power BI Lexicon',
           'desc': 'Plain definitions of the terms used in this course and many more.'},
          {'href': '/code/spreadsheets.html',
           'title': 'Spreadsheets for M&amp;E',
           'desc': 'Tidy sheets, validation and indicator tables before the data reaches Power BI.'},
          {'href': '/code/sql.html',
           'title': 'SQL for Development Data',
           'desc': 'When the data lives in a database, Power BI can query it; SQL is how you check what it '
                   'gets.'}]}

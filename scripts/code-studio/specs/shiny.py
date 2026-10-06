# -*- coding: utf-8 -*-
"""Shiny Dashboards for Development Data: R and Python Shiny apps that open in Shinylive."""

# District summaries computed from the Code Studio households table (invented data).
# Module 5 recomputes them on the page; keep the two in step if the table changes.
ROWS = [
    ("Bihar", "Gaya", 2698, 70.8, 87.5, 33.3),
    ("Bihar", "Patna", 2569, 83.3, 91.7, 45.8),
    ("Bihar", "Purnia", 2395, 75.0, 75.0, 25.0),
    ("Kerala", "Kozhikode", 6758, 83.3, 91.7, 20.8),
    ("Kerala", "Wayanad", 3957, 66.7, 83.3, 54.2),
    ("Madhya Pradesh", "Betul", 2962, 75.0, 79.2, 45.8),
    ("Madhya Pradesh", "Indore", 3758, 83.3, 83.3, 33.3),
    ("Madhya Pradesh", "Rewa", 2557, 50.0, 91.7, 45.8),
    ("Rajasthan", "Barmer", 2745, 75.0, 91.7, 50.0),
    ("Rajasthan", "Udaipur", 3611, 62.5, 83.3, 29.2),
]
COLS = ["state", "district", "mean_pc_exp", "pct_toilet", "pct_bank", "pct_transfer"]


def _fmt(v):
    return '"%s"' % v if isinstance(v, str) else (str(v) if isinstance(v, int) else "%.1f" % v)


def r_data(cols):
    idx = [COLS.index(c) for c in cols]
    lines = []
    for c, i in zip(cols, idx):
        vals = [_fmt(r[i]) for r in ROWS]
        lines.append("  %s = c(%s,\n        %s)" % (c, ", ".join(vals[:5]), ", ".join(vals[5:])))
    return ("# Illustrative data, invented for teaching: one row per district,\n"
            "# summarised from the Code Studio households table.\n"
            "districts <- data.frame(\n" + ",\n".join(lines) + "\n)")


def py_data(cols):
    idx = [COLS.index(c) for c in cols]
    lines = []
    for c, i in zip(cols, idx):
        vals = [_fmt(r[i]) for r in ROWS]
        lines.append('    "%s": [%s,\n        %s],' % (c, ", ".join(vals[:5]), ", ".join(vals[5:])))
    return ("# Illustrative data, invented for teaching: one row per district,\n"
            "# summarised from the Code Studio households table.\n"
            "districts = pd.DataFrame({\n" + "\n".join(lines) + "\n})")


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


def shiny_r(code):
    return {"t": "code", "lang": "shiny-r", "code": code}


def shiny_py(code):
    return {"t": "code", "lang": "shiny-py", "code": code}


HELLO_R = """library(shiny)

ui <- fluidPage(
  h2("Hello from Shiny"),
  textInput("name", "Your district", value = "Gaya"),
  textOutput("greeting")
)

server <- function(input, output, session) {
  output$greeting <- renderText({
    paste("Dashboard for", input$name)
  })
}

shinyApp(ui, server)"""

HELLO_PY = """from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Hello from Shiny for Python"),
    ui.input_text("name", "Your district", value="Gaya"),
    ui.output_text("greeting"),
)


def server(input, output, session):
    @render.text
    def greeting():
        return f"Dashboard for {input.name()}"


app = App(app_ui, server)"""

STATE_R = """library(shiny)

%s

ui <- fluidPage(
  h2("Households with a toilet, by state"),
  selectInput("state", "State", choices = unique(districts$state)),
  textOutput("summary")
)

server <- function(input, output, session) {
  output$summary <- renderText({
    d <- districts[districts$state == input$state, ]
    paste0(nrow(d), " districts. Mean share with a toilet: ",
           round(mean(d$pct_toilet), 1), "%%")
  })
}

shinyApp(ui, server)""" % r_data(["state", "district", "pct_toilet"])

STATE_PY = """from shiny import App, render, ui
import pandas as pd

%s

app_ui = ui.page_fluid(
    ui.h2("Households with a toilet, by state"),
    ui.input_select("state", "State", choices=sorted(districts["state"].unique().tolist())),
    ui.output_text("summary"),
)


def server(input, output, session):
    @render.text
    def summary():
        d = districts[districts["state"] == input.state()]
        return (f"{len(d)} districts. Mean share with a toilet: "
                f"{d['pct_toilet'].mean():.1f}%%")


app = App(app_ui, server)""" % py_data(["state", "district", "pct_toilet"])

SLIDER_R = """library(shiny)

%s

ui <- fluidPage(
  h2("Which districts are below a toilet-coverage threshold?"),
  sliderInput("cutoff", "Threshold (%% of households)",
              min = 40, max = 100, value = 75, step = 5),
  checkboxInput("show_state", "Show the state column", value = TRUE),
  tableOutput("below")
)

server <- function(input, output, session) {
  output$below <- renderTable({
    d <- districts[districts$pct_toilet < input$cutoff, ]
    if (!input$show_state) d$state <- NULL
    d
  })
}

shinyApp(ui, server)""" % r_data(["state", "district", "pct_toilet"])

SLIDER_PY = """from shiny import App, render, ui
import pandas as pd

%s

app_ui = ui.page_fluid(
    ui.h2("Which districts are below a toilet-coverage threshold?"),
    ui.input_slider("cutoff", "Threshold (%% of households)",
                    min=40, max=100, value=75, step=5),
    ui.input_checkbox("show_state", "Show the state column", value=True),
    ui.output_data_frame("below"),
)


def server(input, output, session):
    @render.data_frame
    def below():
        d = districts[districts["pct_toilet"] < input.cutoff()]
        if not input.show_state():
            d = d.drop(columns="state")
        return d


app = App(app_ui, server)""" % py_data(["state", "district", "pct_toilet"])

REACT_R = """library(shiny)

%s

ui <- fluidPage(
  h2("One filter, two outputs"),
  selectInput("state", "State", choices = c("All", unique(districts$state))),
  textOutput("count"),
  tableOutput("table")
)

server <- function(input, output, session) {
  # The filter is written once, as a reactive expression.
  selected <- reactive({
    if (input$state == "All") districts
    else districts[districts$state == input$state, ]
  })

  output$count <- renderText({
    paste(nrow(selected()), "districts selected")
  })

  output$table <- renderTable({
    selected()
  })
}

shinyApp(ui, server)""" % r_data(["state", "district", "mean_pc_exp"])

REACT_PY = """from shiny import App, reactive, render, ui
import pandas as pd

%s

app_ui = ui.page_fluid(
    ui.h2("One filter, two outputs"),
    ui.input_select("state", "State",
                    choices=["All"] + sorted(districts["state"].unique().tolist())),
    ui.output_text("count"),
    ui.output_data_frame("table"),
)


def server(input, output, session):
    # The filter is written once, as a reactive calculation.
    @reactive.calc
    def selected():
        if input.state() == "All":
            return districts
        return districts[districts["state"] == input.state()]

    @render.text
    def count():
        return f"{len(selected())} districts selected"

    @render.data_frame
    def table():
        return selected()


app = App(app_ui, server)""" % py_data(["state", "district", "mean_pc_exp"])

DASH_R = """library(shiny)

%s

labels <- c(
  mean_pc_exp  = "Mean monthly per-capita expenditure (Rs)",
  pct_toilet   = "Households with a toilet (%%)",
  pct_bank     = "Households with a bank account (%%)",
  pct_transfer = "Households that received a transfer (%%)"
)

ui <- fluidPage(
  titlePanel("District dashboard (illustrative data)"),
  sidebarLayout(
    sidebarPanel(
      selectInput("state", "State", choices = c("All", unique(districts$state))),
      selectInput("indicator", "Indicator", choices = setNames(names(labels), labels)),
      checkboxInput("sorted", "Sort from highest to lowest", value = TRUE)
    ),
    mainPanel(
      plotOutput("bars", height = "360px"),
      tableOutput("table")
    )
  )
)

server <- function(input, output, session) {
  selected <- reactive({
    d <- districts
    if (input$state != "All") d <- d[d$state == input$state, ]
    if (input$sorted) d <- d[order(d[[input$indicator]], decreasing = TRUE), ]
    d
  })

  output$bars <- renderPlot({
    d <- selected()
    d <- d[rev(seq_len(nrow(d))), ]   # barplot draws the first row at the bottom
    par(mar = c(5, 8, 1, 1))
    barplot(d[[input$indicator]], names.arg = d$district, horiz = TRUE,
            las = 1, col = "#0369A1", border = NA,
            xlim = c(0, 1.1 * max(d[[input$indicator]])),
            xlab = labels[[input$indicator]])
  })

  output$table <- renderTable({
    selected()[, c("state", "district", input$indicator)]
  })
}

shinyApp(ui, server)""" % r_data(COLS)

DASH_PY = """from shiny import App, reactive, render, ui
import pandas as pd
import matplotlib.pyplot as plt

%s

LABELS = {
    "mean_pc_exp": "Mean monthly per-capita expenditure (Rs)",
    "pct_toilet": "Households with a toilet (%%)",
    "pct_bank": "Households with a bank account (%%)",
    "pct_transfer": "Households that received a transfer (%%)",
}

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("state", "State",
                        choices=["All"] + sorted(districts["state"].unique().tolist())),
        ui.input_select("indicator", "Indicator", choices=LABELS),
        ui.input_checkbox("sorted", "Sort from highest to lowest", value=True),
    ),
    ui.output_plot("bars", height="360px"),
    ui.output_data_frame("table"),
    title="District dashboard (illustrative data)",
)


def server(input, output, session):
    @reactive.calc
    def selected():
        d = districts
        if input.state() != "All":
            d = d[d["state"] == input.state()]
        if input.sorted():
            d = d.sort_values(input.indicator(), ascending=False)
        return d

    @render.plot
    def bars():
        d = selected().iloc[::-1]  # barh draws the first row at the bottom
        fig, ax = plt.subplots()
        ax.barh(d["district"], d[input.indicator()], color="#0369A1")
        ax.set_xlabel(LABELS[input.indicator()])
        return fig

    @render.data_frame
    def table():
        return selected()[["state", "district", input.indicator()]]


app = App(app_ui, server)""" % py_data(COLS)

PROTO_SUMMARY_R = """h <- read.csv("households.csv")
d <- read.csv("districts.csv")
m <- merge(h, d, by = "district")

# Yes/No columns become 0/100, so their mean is a percentage
for (v in c("has_toilet", "has_bank_account", "received_transfer")) {
  m[[v]] <- 100 * (m[[v]] == "Yes")
}

summ <- aggregate(cbind(monthly_pc_exp, has_toilet, has_bank_account, received_transfer)
                  ~ state + district, data = m, FUN = mean)
names(summ) <- c("state", "district", "mean_pc_exp", "pct_toilet", "pct_bank", "pct_transfer")
summ$mean_pc_exp <- round(summ$mean_pc_exp)
summ[, 4:6] <- round(summ[, 4:6], 1)
summ"""

PROTO_SUMMARY_PY = """import pandas as pd

h = pd.read_csv("households.csv")
d = pd.read_csv("districts.csv")
m = h.merge(d, on="district")

# Yes/No columns become 0/100, so their mean is a percentage
for v in ["has_toilet", "has_bank_account", "received_transfer"]:
    m[v] = 100 * (m[v] == "Yes")

summ = (m.groupby(["state", "district"], as_index=False)
          .agg(mean_pc_exp=("monthly_pc_exp", "mean"),
               pct_toilet=("has_toilet", "mean"),
               pct_bank=("has_bank_account", "mean"),
               pct_transfer=("received_transfer", "mean")))
summ["mean_pc_exp"] = summ["mean_pc_exp"].round().astype(int)
summ = summ.round(1)
print(summ.to_string(index=False))"""

PROTO_FILTER_R = """h <- read.csv("households.csv")
d <- read.csv("districts.csv")
m <- merge(h, d, by = "district")
m$pct_toilet <- 100 * (m$has_toilet == "Yes")
summ <- aggregate(pct_toilet ~ state + district, data = m, FUN = mean)
summ$pct_toilet <- round(summ$pct_toilet, 1)

# The two choices the dashboard will offer, written as plain variables
state <- "Madhya Pradesh"
indicator <- "pct_toilet"

sel <- summ[summ$state == state, ]
sel <- sel[order(sel[[indicator]], decreasing = TRUE), ]
sel

sel <- sel[rev(seq_len(nrow(sel))), ]
par(mar = c(5, 8, 1, 1))
barplot(sel[[indicator]], names.arg = sel$district, horiz = TRUE, las = 1,
        col = "#0369A1", border = NA, xlab = "Households with a toilet (%)")"""

PROTO_FILTER_PY = """import pandas as pd
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt

h = pd.read_csv("households.csv")
d = pd.read_csv("districts.csv")
m = h.merge(d, on="district")
m["pct_toilet"] = 100 * (m["has_toilet"] == "Yes")
summ = m.groupby(["state", "district"], as_index=False)["pct_toilet"].mean().round(1)

# The two choices the dashboard will offer, written as plain variables
state = "Madhya Pradesh"
indicator = "pct_toilet"

sel = summ[summ["state"] == state].sort_values(indicator, ascending=False)
print(sel.to_string(index=False))

sel = sel.iloc[::-1]
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(sel["district"], sel[indicator], color="#0369A1")
ax.set_xlabel("Households with a toilet (%)")
show(fig)"""

OPENS = ('<strong>Where the apps run.</strong> A Shiny cell does not run on this page. '
         '<strong>Open in Shinylive</strong> packs the code into a link and opens it in a new tab on '
         '<a href="https://shinylive.io" rel="noopener" target="_blank" style="color:var(--accent-color)">'
         'shinylive.io</a>, Posit\'s site, where the app starts in an editor beside its code. The first start '
         'downloads R or Python into your browser (about 13&nbsp;MB for a Python app, by Posit\'s own count), '
         'so give it time on a slow connection. The code travels after the '
         '<code class="inline">#</code> in the link, which browsers do not send to the server, so Posit\'s '
         'site does not receive your app\'s code.')

PAGE = {
    "slug": "shiny",
    "order": 5,
    "kind": "runnable",
    "title": "Shiny Dashboards for Development Data",
    "h1": "Shiny Dashboards for Development Data",
    "lede": ("Build interactive dashboards in R and in Python with Shiny. Learn the ui and server model, "
             "inputs, outputs and reactivity, prototype the summary on this page, then open a working district "
             "dashboard in Posit's Shinylive editor."),
    "description": ("Learn Shiny from zero for development data in South Asia: the ui and server model, inputs, "
                    "outputs and reactivity, and a filterable district dashboard in both R and Shiny for Python, "
                    "opened in Shinylive in your browser."),
    "card": "Build a filterable district dashboard in R and Python Shiny, opened in Shinylive.",
    "datasets": ["households", "districts"],
    "engine_note": ("<strong>Two kinds of cell on this page.</strong> Ordinary R and Python cells run here, as in "
                    "the other Code Studio courses: the first Run downloads the engine once (R about 7&nbsp;MB, "
                    "Python about 10&nbsp;MB), with <code class=\"inline\">households.csv</code> and <code "
                    "class=\"inline\">districts.csv</code> loaded for you. Shiny cells carry an <strong>Open in "
                    "Shinylive</strong> button instead. It opens the app on Posit's Shinylive site in a new tab. "
                    "A Shinylive app cannot read this page's files, so every app here carries its own small data "
                    "frame typed into the code."),
    "modules": [
        {"tab": "What Shiny is", "title": "What Shiny is", "blocks": [
            p("Shiny is a framework from Posit for building interactive web pages out of R or Python code. You "
              "write the analysis you already know, add a few controls, and a programme officer can pick a "
              "state or an indicator from a menu and see the chart change, without opening R or Python "
              "themselves."),
            p("It began as an R package. <strong>Shiny for Python</strong> is a separate package with the same "
              "ideas and slightly different spelling. This course teaches both side by side, so you can use "
              "whichever language your team already works in."),
            p("A Shiny app usually needs a server running R or Python. <strong>Shinylive</strong> removes that: "
              "it runs R (through webR) or Python (through Pyodide) inside the visitor's browser, so the browser "
              "is both the client and the server. That is how the apps in this course open with nothing "
              "installed."),
            info(OPENS),
            h3("Your first app"),
            p("Click <strong>Open in Shinylive</strong>. When the app appears on the right of the Shinylive "
              "editor, type a different district into the box and watch the line below it change."),
            shiny_r(HELLO_R),
            p("The same app in Shiny for Python:"),
            shiny_py(HELLO_PY),
            p("<strong>Try it:</strong> in the Shinylive editor, change the text inside "
              "<code class=\"inline\">paste()</code> or the f-string, then re-run the app from the editor. "
              "Edits made there stay on Posit's page; to keep them, copy the code back into a file of your "
              "own."),
        ]},
        {"tab": "ui and server", "title": "Two halves: ui and server", "blocks": [
            p("Every Shiny app has two parts."),
            ul(["The <strong>ui</strong> describes the page: headings, the controls a reader can change "
                "(<em>inputs</em>) and empty slots where results will appear (<em>outputs</em>). Each input and "
                "output has an id, a short name in quotes such as <code class=\"inline\">\"state\"</code>.",
                "The <strong>server</strong> is a function that fills the output slots. It reads the inputs by "
                "id and recomputes an output whenever an input it uses changes.",
                "The last line joins the two: <code class=\"inline\">shinyApp(ui, server)</code> in R, "
                "<code class=\"inline\">App(app_ui, server)</code> in Python."]),
            p("In R the server reads <code class=\"inline\">input$state</code> and writes to "
              "<code class=\"inline\">output$summary</code>. In Python it reads "
              "<code class=\"inline\">input.state()</code> (note the brackets: it is a function call) and the "
              "output is a function decorated with <code class=\"inline\">@render.text</code> whose name is the "
              "output id."),
            p("This app embeds a ten-row data frame of district results. The data is invented for teaching "
              "<span class=\"illustrative-tag\">Illustrative data</span>; module 5 shows where the numbers "
              "come from. Pick a state and read the sentence."),
            shiny_r(STATE_R),
            shiny_py(STATE_PY),
            p("<strong>Try it:</strong> change <code class=\"inline\">pct_toilet</code> to report the highest "
              "value instead of the mean (<code class=\"inline\">max()</code> in R, "
              "<code class=\"inline\">.max()</code> in Python), and edit the sentence to match."),
        ]},
        {"tab": "Inputs and outputs", "title": "Inputs and outputs", "blocks": [
            p("Inputs and outputs come in pairs of functions: one in the ui to place them, one in the server to "
              "fill an output. The ones a monitoring dashboard needs most:"),
            ul([
                "<strong>Drop-down menu</strong>: <code class=\"inline\">selectInput()</code> in R, <code class=\"inline\">ui.input_select()</code> in Python.",
                "<strong>Slider</strong>: <code class=\"inline\">sliderInput()</code> in R, <code class=\"inline\">ui.input_slider()</code> in Python.",
                "<strong>Tick box</strong>: <code class=\"inline\">checkboxInput()</code> in R, <code class=\"inline\">ui.input_checkbox()</code> in Python.",
                "<strong>Text box</strong>: <code class=\"inline\">textInput()</code> in R, <code class=\"inline\">ui.input_text()</code> in Python.",
                "<strong>Text output</strong>: <code class=\"inline\">textOutput()</code> with <code class=\"inline\">renderText()</code> in R, <code class=\"inline\">ui.output_text()</code> with <code class=\"inline\">@render.text</code> in Python.",
                "<strong>Table output</strong>: <code class=\"inline\">tableOutput()</code> with <code class=\"inline\">renderTable()</code> in R, <code class=\"inline\">ui.output_data_frame()</code> with <code class=\"inline\">@render.data_frame</code> in Python.",
                "<strong>Chart output</strong>: <code class=\"inline\">plotOutput()</code> with <code class=\"inline\">renderPlot()</code> in R, <code class=\"inline\">ui.output_plot()</code> with <code class=\"inline\">@render.plot</code> in Python."]),
            p("This app uses a slider, a tick box and a table. Move the slider: the table lists the districts "
              "whose toilet coverage is below the threshold."),
            shiny_r(SLIDER_R),
            shiny_py(SLIDER_PY),
            info("A threshold slider makes a cut-off visible and adjustable. When a dashboard flags districts "
                 "as \"lagging\", say where the cut-off came from, and let the reader see what moves when it "
                 "changes."),
            p("<strong>Try it:</strong> change the slider's default <code class=\"inline\">value</code> to 70 "
              "and its <code class=\"inline\">step</code> to 1, then re-run the app in the Shinylive editor."),
        ]},
        {"tab": "Reactivity", "title": "Reactivity: write the filter once", "blocks": [
            p("Shiny keeps track of which inputs each output reads. When an input changes, Shiny reruns only "
              "the outputs that depend on it. This is <strong>reactivity</strong>, and it is why you never "
              "write \"when the menu changes, redraw the chart\" yourself."),
            p("When two outputs need the same filtered data, do not filter twice. Put the filter in a "
              "<strong>reactive expression</strong>: <code class=\"inline\">reactive({ ... })</code> in R, a "
              "function decorated with <code class=\"inline\">@reactive.calc</code> in Python. Call it like a "
              "function, <code class=\"inline\">selected()</code>, from each output. Shiny computes it once per "
              "change and both outputs share the result."),
            shiny_r(REACT_R),
            shiny_py(REACT_PY),
            ul(["The menu feeds <code class=\"inline\">selected()</code>.",
                "<code class=\"inline\">selected()</code> feeds both the count and the table.",
                "Change the menu, and Shiny marks <code class=\"inline\">selected()</code> out of date, then "
                "recomputes it and both outputs."]),
            info("Keep heavy work (reading a file, joining tables, fitting a model) outside the server function "
                 "or inside a reactive expression. Code at the top of the app runs once when the app starts; "
                 "code inside an output runs every time that output updates."),
            p("<strong>Try it:</strong> add a third output that shows the highest <code "
              "class=\"inline\">mean_pc_exp</code> among the selected districts. Place it in the ui and fill it "
              "from <code class=\"inline\">selected()</code>."),
        ]},
        {"tab": "Prototype here", "title": "Prototype the summary before it goes into the app", "blocks": [
            p("A dashboard is an analysis with controls attached. Get the analysis right first, in ordinary "
              "code you can run and check, and only then wrap it in Shiny. These cells run on this page, on "
              "<code class=\"inline\">households.csv</code> and <code class=\"inline\">districts.csv</code>. "
              "<span class=\"illustrative-tag\">Illustrative data</span> Both tables are invented for teaching; "
              "the district names are real places, but no number describes them."),
            h3("Step 1: one row per district"),
            p("Join households to districts, turn the Yes/No columns into 0 or 100, and average by district. "
              "Run it in R, then switch the tab to Python and run again."),
            {"t": "dual", "r": PROTO_SUMMARY_R, "py": PROTO_SUMMARY_PY, "pypkgs": "pandas"},
            p("Ten rows, one per district, and the same numbers in both languages. R lists the rows by district "
              "and Python by state; the values agree. Kozhikode has the highest mean expenditure, 6,758 rupees "
              "a month, and Rewa the lowest toilet coverage, 50 per cent. These ten rows are the data frame "
              "the apps in this course carry."),
            h3("Step 2: the filter and the chart, with the inputs as plain variables"),
            p("Before there is a menu, the reader's choices are just two variables. Write the filter and the "
              "chart with them. When this works, each variable becomes an input, and the code moves into the "
              "server almost unchanged."),
            {"t": "dual", "r": PROTO_FILTER_R, "py": PROTO_FILTER_PY, "pypkgs": "pandas,matplotlib"},
            p("The three Madhya Pradesh districts, sorted: Indore 83.3, Betul 75.0 and Rewa 50.0 per cent, and "
              "a bar chart with the highest at the top. The rows are reversed just before plotting because "
              "a horizontal bar chart draws the first row at the bottom."),
            p("<strong>Try it:</strong> set <code class=\"inline\">state</code> to <code "
              "class=\"inline\">\"Kerala\"</code> and run again. Then follow the same steps for "
              "<code class=\"inline\">has_bank_account</code>."),
        ]},
        {"tab": "Dashboard in R", "title": "The district dashboard in R", "blocks": [
            p("This app puts modules 2 to 5 together. The sidebar has three inputs: a state (or All), an "
              "indicator and a sort switch. The main panel has a horizontal bar chart and a table, both fed "
              "by one reactive expression. The data frame at the top holds the ten rows that the Step 1 cell "
              "printed, typed in, because a Shinylive app cannot read <code class=\"inline\">households.csv</code> "
              "from this page."),
            info(OPENS),
            shiny_r(DASH_R),
            h3("How the code maps to what you see"),
            ul(["<code class=\"inline\">sidebarLayout()</code> puts the inputs on the left and the outputs on the "
                "right; on a narrow screen they stack.",
                "<code class=\"inline\">setNames(names(labels), labels)</code> shows readable labels in the "
                "menu while the server receives the column name, such as <code class=\"inline\">pct_bank</code>.",
                "<code class=\"inline\">selected()</code> is the same filter-and-sort as the Step 2 cell, with "
                "<code class=\"inline\">input$state</code> and <code class=\"inline\">input$indicator</code> in "
                "place of the plain variables.",
                "The chart uses base R graphics, so the app needs no package beyond shiny and starts faster in "
                "Shinylive."]),
            p("<strong>Try it:</strong> add a fifth indicator. Put a column into the data frame (for example "
              "<code class=\"inline\">pct_shg</code>, the share in a self-help group, computed the way Step 1 "
              "computes the others), then add a line for it to <code class=\"inline\">labels</code>. The menu, "
              "chart and table pick it up with no other change."),
        ]},
        {"tab": "Dashboard in Python", "title": "The district dashboard in Shiny for Python", "blocks": [
            p("The same dashboard in Shiny for Python, using the same ten rows. The structure is identical; "
              "the spelling differs."),
            info(OPENS),
            shiny_py(DASH_PY),
            h3("Differences from the R version"),
            ul(["<code class=\"inline\">ui.page_sidebar()</code> with <code class=\"inline\">ui.sidebar()</code> "
                "plays the part of <code class=\"inline\">sidebarLayout()</code>.",
                "<code class=\"inline\">ui.input_select()</code> accepts a dictionary for "
                "<code class=\"inline\">choices</code>: the keys are what the server receives, the values are "
                "what the reader sees.",
                "Inputs are read with brackets, <code class=\"inline\">input.indicator()</code>, and outputs are "
                "functions named after their ids, decorated with <code class=\"inline\">@render.plot</code> or "
                "<code class=\"inline\">@render.data_frame</code>.",
                "<code class=\"inline\">@render.plot</code> displays the matplotlib figure the function returns."]),
            p("<strong>Try it:</strong> add <code class=\"inline\">ax.axvline(districts[input.indicator()].mean(), "
              "color=\"#B45309\")</code> before <code class=\"inline\">return fig</code> to draw the ten-district "
              "average as a line, and re-run."),
        ]},
        {"tab": "Sharing", "title": "Sharing a dashboard, and what not to put in one", "blocks": [
            p("Three ways to get a dashboard to the people who need it, from lightest to heaviest:"),
            ul(["<strong>A Shinylive link.</strong> The link in your browser's address bar, after you open an app "
                "from this page, contains the whole app. Anyone who opens it runs the app in their own browser. "
                "Good for small apps with small, non-sensitive data.",
                "<strong>A static Shinylive site.</strong> The shinylive package turns an app folder into plain "
                "web files you can put on any static host (GitHub Pages, Netlify, your organisation's web "
                "server). It needs a web server: opening the files straight from disk does not work.",
                "<strong>A Shiny server.</strong> For large data, private data, or heavy computation, run the "
                "app on a server with R or Python installed, such as Posit Connect or a server your "
                "organisation runs. The data then stays on the server."]),
            h3("Export an app to a static site"),
            p("On your own computer, with the app saved as <code class=\"inline\">myapp/app.R</code> or "
              "<code class=\"inline\">myapp/app.py</code>, the commands from Posit's documentation are:"),
            {"t": "syntax", "label": "R (in an R console)",
             "code": 'install.packages("shinylive")\nshinylive::export("myapp", "site")\n'
                     'httpuv::runStaticServer("site/")   # preview it locally'},
            {"t": "syntax", "label": "Python (in a terminal, with uv installed)",
             "code": "uvx shinylive export myapp site"},
            p("Sources: the <a href=\"https://posit-dev.github.io/r-shinylive/\" rel=\"noopener\" target=\"_blank\" "
              "style=\"color:var(--accent-color)\">shinylive R package site</a> and the "
              "<a href=\"https://shiny.posit.co/py/get-started/shinylive.html\" rel=\"noopener\" target=\"_blank\" "
              "style=\"color:var(--accent-color)\">Shiny for Python Shinylive guide</a>, both read in October "
              "2026."),
            info("<strong>A Shinylive app has no secrets.</strong> Posit's Shinylive guide says it plainly: the "
                 "code and data must be sent to the browser, so they cannot be kept from the user. Anything you "
                 "embed in a Shinylive app, or in its link, can be read by anyone who opens it. Put only "
                 "aggregated, non-identifying figures in one: district percentages, never beneficiary names, "
                 "phone numbers, ID numbers or household-level rows. For data about people, follow the "
                 "<a href=\"/101-courses/data-protection-dpdp.html\" style=\"color:var(--accent-color)\">"
                 "Data Protection &amp; the DPDP Act</a> deck, and use a server-based app with access control.",
                 "warning"),
            info("<strong>Small cells mislead.</strong> A district average from 24 households moves a lot when "
                 "one household changes. Before a dashboard goes to a district officer, show the number of "
                 "households behind each bar, or suppress cells below a minimum size, as the HAVING example in "
                 "the SQL course does."),
            p("<strong>Try it:</strong> add a <code class=\"inline\">households</code> column (24 for every "
              "district here) to the dashboard's data frame and show it in the table, so every bar comes with "
              "its sample size."),
        ]},
    ],
    "next": [
        {"href": "/code/sql.html", "title": "SQL for Development Data",
         "desc": "Pull and summarise the rows a dashboard needs, straight from a database."},
        {"href": "/code/r-python.html", "title": "R &amp; Python for Development",
         "desc": "The data-frame skills underneath every Shiny app."},
        {"href": "/101-courses/data-viz.html", "title": "Data Visualization 101",
         "desc": "Choosing the chart before you build the dashboard."},
        {"href": "/101-courses/mel-basics.html", "title": "MEL Basics 101",
         "desc": "Which indicators a monitoring dashboard should carry."},
        {"href": "/101-courses/data-protection-dpdp.html", "title": "Data Protection &amp; the DPDP Act 101",
         "desc": "What may and may not go into a shared app."},
    ],
}

# -*- coding: utf-8 -*-
"""Code Studio landing page. Cards are generated from every other spec."""

PAGE = {
    "slug": "index",
    "title": "Code Studio",
    "h1": "Code Studio",
    "lede": ("Learn the languages and tools of development data work by doing it. Write and run R, Python and "
             "SQL in your browser with nothing to install, then follow guided courses for the desktop software "
             "your organisation already uses."),
    "description": ("ImpactMojo Code Studio: free, hands-on courses for development data work in South Asia. "
                    "Run R, Python, tidyverse, pandas and SQL live in your browser, build Shiny apps, and learn "
                    "Stata, SPSS, jamovi, JASP, OpenRefine, QGIS, KoboToolbox, spreadsheets, Git and Quarto "
                    "through guided courses."),
    "intro": ('<div class="info-box"><strong>Two kinds of course.</strong> The first group runs real code in '
              'your browser: R through WebR, Python through Pyodide, SQL through SQLite. The engine downloads '
              'once, on your first Run, and stays loaded while the page is open. The second group teaches '
              'software that cannot run in a browser, such as Stata and QGIS. Those courses show you the '
              'commands and the steps, and tell you what to look for on your own screen; they do not pretend '
              'to run the software for you.</div>'),
    "sections": [
        ("runnable", "Run code in your browser",
         "Nothing to install. A small illustrative household survey is loaded into every environment."),
        ("guide", "Guided tool courses",
         "Step-by-step courses for software you install or use online, with the commands written out."),
    ],
}

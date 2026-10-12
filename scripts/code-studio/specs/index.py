# -*- coding: utf-8 -*-
"""Code School landing page. Cards are generated from every other spec."""

PAGE = {
    "slug": "index",
    "title": "Code School",
    "h1": "Code School",
    "lede": ("Learn the languages and tools of development data work by doing it. Write and run R, Python and "
             "SQL in your browser with nothing to install, then follow guided courses for the desktop software "
             "your organisation already uses."),
    "description": ("ImpactMojo Code School: free, hands-on courses for development data work in South Asia. "
                    "Run R, Python, tidyverse, pandas and SQL live in your browser, build Shiny apps, and learn "
                    "Stata, SPSS, jamovi, JASP, OpenRefine, QGIS, KoboToolbox, spreadsheets, Git and Quarto "
                    "through guided courses."),
    "intro": ('<div class="info-box"><strong>There are two kinds of course here.</strong> The courses '
              'in the first group run real code in your browser, with R through WebR, Python through Pyodide '
              'and SQL through SQLite. The engine downloads once, the first time you press Run, and stays '
              'loaded while the page is open. The second group teaches software that cannot run in a browser, '
              'such as Stata and QGIS. Those courses set out the commands and the steps and tell you what to '
              'look for on your own screen. They do not try to run the software for you.</div>'),
    "sections": [
        ("runnable", "Run code in your browser",
         "There is nothing to install. Every course loads the same small household survey, made up for practice."),
        ("guide", "Guided courses for desktop and online tools",
         "Step-by-step courses for software you install or use online, with every command written out."),
    ],
}

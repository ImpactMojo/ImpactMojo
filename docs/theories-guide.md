# Theories of Development

**Live at [impactmojo.in/theories](https://www.impactmojo.in/theories/)**

Twelve theories about why some places are poor and what would change it, each drawn
as a causal chain the reader steps through, placed on four axes, and then set
against what the evidence actually shows. The global canon and South Asian
traditions sit in one catalogue rather than in separate literatures, so Rostow
and Nehru, or Ambedkar and Gandhi, can be read next to each other.

## What is on a theory page

Five things, in this order.

**The argument.** Two to four paragraphs stating what the theory claims, in the
terms its own authors used.

**The causal chain.** The theory as a diagram, revealed one layer at a time with
the arrow keys or the buttons. Each step adds the boxes it introduces and the
arrows into them, so the reader watches the argument being assembled instead of
meeting it finished. Boxes are coloured by what they are: a starting condition,
a mechanism, or an outcome. A dashed arrow running back up the page is a
feedback loop the theory relies on, such as reinvested profit in Lewis.

**Four placements.** Where the theory sits on who allocates, what comes first,
where hierarchy sits, and who moves. Each placement carries the sentence that
justifies it, because the scores are editorial and are meant to be argued with.

**What happened.** One entry per major claim: what the theory predicted, what
the record shows, and a named source with a year. This section is the reason
the library exists. It is deliberately unkind to the theory it belongs to,
including the theories we find persuasive.

**What it does not settle**, and how the theory landed in India.

## The four axes

Catalogues of political thought normally sort on a left-to-right axis. That axis
sorts Indian thought badly: it separates Ambedkar and Nehru, who shared most of
their economics, and it has nowhere sensible to put Gandhi. These four ask
questions the theories on this shelf actually disagree about.

| Axis | Runs from | to |
|---|---|---|
| Who allocates | The state decides | Markets decide |
| What comes first | Redistribute first | Grow first |
| Where hierarchy sits | Hierarchy is its own cause | Hierarchy follows from economics |
| Who moves | Movements and the poor | Experts and the state |

Scores run from -3 to +3 and were assigned by the editorial team from each
theory's own texts. They are a way of arranging a shelf, not a measurement.

## Using it in teaching

Give a group two theories that contrast, one from the global canon and one from
South Asia, and ask them to find the sentence in each that the other would
refuse. The disagreement is usually not about facts and usually not about values
either; it is about which mechanism is doing the work, which is what the
diagrams are for.

A second exercise: take a programme the group runs, and ask which theory on the
shelf its design assumes. Most programme documents turn out to be committed to
one without saying so.

## Adding a theory

One JSON file per theory in `data/theories/`, then run the build:

```bash
python3 scripts/build-theories.py          # writes the pages, data file, sitemap and search rows
python3 scripts/build-theories.py --check  # what CI runs
```

The build refuses to run on a file that is incomplete or inconsistent. It checks
that every axis is scored and carries a note explaining the score, that every
piece of evidence has a named source and a year, that the compare and contrast
links point at theories that exist, and that every edge in the diagram points at
a node that exists. That last check is the one worth having: a renderer drops an
edge to a renamed node without complaining, so the diagram goes on looking
finished while an arrow the argument depends on is missing.

An edge that loops back to an earlier layer must say so, as
`["from", "to", "feedback"]`. Anything else running backwards is treated as a
typo, because that is almost always what it is.

## Related

- [Fundamentals](https://www.impactmojo.in/fundamentals/) — the diagrams development
  work already uses, with the Indian evidence behind them. Frameworks you apply,
  where this library holds positions people hold.
- [Development Discourses](https://varnasr.github.io/development-discourses/) — the
  open-access reading library each theory page points into.

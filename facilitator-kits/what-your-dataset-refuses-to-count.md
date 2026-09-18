# Welcome — what your dataset refuses to count

A 45-minute session on the decisions taken before a dataset reaches you: what was made a category, what was made a residual, and who was made invisible by an entirely reasonable choice.

Bring a dataset you use regularly. You do not need to open it. You need to be able to describe its columns.

Mark each step **done**, or **stuck** to bring the facilitator over.

# Every column was a decision

A dataset arrives looking like a description of the world. It is closer to a record of arguments that were settled before you got there.

Someone decided that occupation would have fourteen categories rather than forty. Someone decided that "housewife" is a category and "unpaid family worker on our own land" is a different one, or the same one. Someone decided whether a person doing three things is recorded as doing the one they spend most time on, or most of their income from, or the one they name first.

None of that is visible in the file. It is visible in the questionnaire and the classification manual, which almost nobody reads.

# The residual category

Find the residual in your dataset. Almost every classification has one: **Other**, **Not elsewhere classified**, **NEC**, **Not stated**, **Miscellaneous**.

Answer three questions about it:

1. How large is it, as a share?
2. Who is in it? Not in principle — in your data, for your population.
3. Would your analysis change if it were split into its real components?

A large residual is not sloppiness. It is where the classification stopped matching the world, and it is often the most informative column in the file.

One live example worth knowing: in India's CSR spending data, `PAN India`, `PAN India (Other Centralized Funds)` and `NEC/Not Mentioned` together account for around a fifth of all reported spending, attributed to no state at all. Drop them and every state's share inflates. Assign them to a state and you have invented a fact.

#[quiz] Categories and residuals

## A residual category ("Other", "NEC") that holds 20 per cent of records is best treated as:

- [ ] Noise, to be excluded from analysis
- [ ] Evidence the data collection was poor
- [x] A finding in itself, and a limit on what the other categories can support
- [ ] Missing data, to be imputed

## A classification with fourteen occupation categories rather than forty primarily affects:

- [ ] The sample size
- [x] Which distinctions the data can express at all
- [ ] The response rate
- [ ] The confidence intervals

# Who is structurally absent

Some people are missing from a dataset not because of a sampling accident but because of the frame itself.

Household surveys are built on households. That makes them systematically weak on people who do not sit inside one: those in institutions, on the street, in workers' accommodation, in seasonal migration at the time of enumeration.

Ask of your own dataset:

- **Who cannot appear here, by construction?**
- **Is that population the one your programme most cares about?**
- **If so, what do you have instead, and how bad is it?**

Write the answers down. This paragraph belongs in your method section and is almost always omitted.

# The proxy that became the thing

Find one variable in your dataset that stands in for something else, and trace the substitution.

Common ones: years of schooling standing in for learning. Asset ownership standing in for wealth, and then for poverty. Bank account existence standing in for financial inclusion. Attendance standing in for participation.

For your chosen variable, write:

1. What it actually records.
2. What it is being used to mean.
3. One plausible case where the two come apart badly.

A proxy is fine. A proxy whose gap with the real thing is never stated is how a measurement error becomes a policy.

#[quiz] Frames and proxies

## A household survey will systematically under-represent:

- [ ] Women, because of response rates
- [x] People who do not live in a conventional household at the time of enumeration
- [ ] Younger respondents
- [ ] Urban populations

## Stating the gap between a proxy and the concept it stands for is mainly a defence against:

- [ ] Sampling error
- [x] A measurement decision hardening into an unexamined fact
- [ ] Non-response
- [ ] Multiple comparisons

# Close

Take one paragraph back to your team: for the dataset you use most, write what cannot appear in it and who that excludes. Three sentences.

Put it in the next output that uses that data. Not as a limitation buried at the end — near the number, where someone deciding something will read it.

**Going further.** [Data Feminism 101](https://www.impactmojo.in/101-courses/data-feminism.html) is a hundred slides on power in classification and display, and the [Data Feminism Studio](https://www.impactmojo.in/Labs/data-feminism-lab.html) runs this interrogation against a dataset you choose.

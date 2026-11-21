# ImpactLex content refresh, November 2026

Record of a pass over ImpactLex entries on 21 November 2026. This file is in `ops/`, which `netlify.toml` answers with a forced 404, so it is not served to readers.

## What was done

54 entries were checked against a published source that was opened and read on 21 November 2026. Each now has an entry in `impactlex/data/reviewed.json` with its definition, example, sources and `checkedAt: 2026-11-21`. `impactlex/app.js` lays that file over the snapshot and shows the line "Definition checked against the source cited above on 2026-11-21". Nothing in `impactlex/data/seed-snapshot.json` was changed.

No status was changed. No entry was marked reviewed or published, and no `aiProvider` marker was removed. The page already separates "Reviewed" (an editor's decision, read from `status`) from "Checked against a source" (read from `checkedAt`), so the existing schema had a truthful place for this work and no field was invented. The entries below still need an editor's sign-off before their status changes.

What 'checked' means here: the definition was compared with the source cited, and every figure, date, section number and page number in the new text was seen in that source. Sentences that explain why a term matters are my own plain summary. Examples are illustrations and are written so that they assert no fact about a named scheme or organisation unless the cited source states it. Where I could not open the original work (Kingdon, Tufte, Hill, Jenkins's page numbers), the note says which secondary source was read.

## Counts

| | Before | After |
|---|---|---|
| Terms | 494 | 494 |
| Status published (shown as Reviewed) | 335 | 335 |
| Status seed (shown as Not yet reviewed) | 159 | 159 |
| First drafted by a language model | 226 | 226 |
| Entries in reviewed.json (checked against a source) | 348 | 400 |
| With a source, after reviewed.json is applied | 382 | 434 |
| With no source | 112 | 60 |
| Not yet reviewed and no source | 42 | 20 |
| Not yet reviewed and not checked | 56 | 34 |
| Reviewed and no source | 70 | 40 |
| Model-drafted and no source | 56 | 35 |

The snapshot alone still carries a citation on 34 terms; that is the figure `scripts/check-impactlex.py` prints, because it reads the snapshot and not `reviewed.json`. The brief for this pass said 'about 159 not yet reviewed' and 'a large share with no citation'. The first is right. The second was out of date: 348 entries had already been checked and sourced on 14 October 2026, so 112 terms had no source when this pass began. The figure of 460 in the repository's notes counts the snapshot alone.

Of the 54 entries: 39 were corrected (definition or example changed in substance) and 15 were found to agree with the source and were rewritten in full sentences with the source added. 2 of the 54 had been checked on 14 October and were re-sourced (absolute-poverty, impact).

## Where authoritative sources disagree

- **Quasi-Federal** (`quasi-federal`): Within S.R. Bommai (1994) the judges differ. Ahmadi J. calls the Constitution 'quasi-federal' (para 24); another opinion says it is not necessary to decide whether it is federal, quasi-federal or unitary (para 100); Jeevan Reddy J. says the greater power of the Centre does not make the states 'mere appendages' (para 276).
- **RCT Limitations** (`rct-limitations`): Deaton and Cartwright argue that demanding 'external validity' expects too much of an RCT; proponents such as J-PAL treat RCTs as the most credible single design for causal effects. The entry reports the limits and does not rank designs.
- **Open Defecation Free** (`open-defecation-free`): The Government of India defines ODF as an area status with two conditions (no visible faeces; every household and institution using a safe technology option). The WHO/UNICEF JMP measures the share of people practising open defecation from household surveys. The two can give different pictures of the same place.
- **Absolute Poverty** (`absolute-poverty`): The World Bank's international line ($3.00 a day, 2021 PPP, from June 2025) and India's national Tendulkar lines (Rs. 816 rural and Rs. 1,000 urban per person per month, 2011-12) are set by different methods and give different counts of the poor. The Rangarajan committee's higher lines (2014) were not opened and are not cited.
- **Impact** (`impact`): OECD DAC criterion sense (higher-level, longer-term effects) versus the counterfactual sense used in impact evaluation (any causal effect of the intervention). Both appear in the OECD glossary itself.
- **Midline** (`midline`): the OECD glossary defines 'mid-term evaluation' and has no entry for 'midline'. The entry says so.
- **Leading indicator, lagging indicator**: the only formal definitions opened are from occupational safety (OSHA). The OECD's 'leading indicators' are a different thing (composite indicators of the business cycle). The entries say where the definition comes from.

## Formulae

One touched entry states a formula. Lie factor = size of effect shown in graphic / size of effect in data. It matches the source read (lecture notes reproducing Tufte). No touched entry has a value in the snapshot's `formula` field.

## Entries checked, one by one

Old text is quoted as it stood, including its punctuation.

### Natural Monopoly (`natural-monopoly`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** A market where unit costs fall so sharply with scale that a single firm can serve demand more cheaply than multiple firms. Electricity transmission, water supply, and rail infrastructure are standard examples.

**Its example said:** Building two competing electricity grids in a city would be wasteful — fixed costs are so large that the natural structure is a single regulated provider.

**It says now:** A natural monopoly exists in a market where a single firm can serve the whole market at a lower cost than any combination of two or more firms. It arises from the technology of production, usually economies of scale and scope that are large relative to demand, and does not arise from the actions of governments or rivals. Long-run average and marginal costs fall so steeply that there is room for only one firm to use the available economies of scale. Parts of the electricity, railway, natural gas and telecommunications industries are the usual examples, and they are typically regulated on price, quality or entry.

**Its example now:** Building two competing electricity grids in a city would duplicate very large fixed costs, so the usual arrangement is a single regulated provider.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Natural monopoly' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf

**Note:** Agrees with the source. Rewritten in full sentences; added that the cause lies in production technology and that such industries are typically regulated.

### Natural Monopoly Regulation (`natural-monopoly-regulation`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Government oversight of industries where a single firm is most efficient due to large fixed costs and economies of scale — setting tariffs, quality standards, and preventing monopoly pricing.

**Its example said:** TRAI regulates telecom tariffs because spectrum and tower infrastructure create natural monopoly tendencies — without regulation, a dominant firm could price out smaller competitors.

**It says now:** Natural monopoly regulation is government oversight of an industry in which one firm can supply the market at the lowest cost. The OECD defines regulation as rules imposed by government, backed by penalties, that are intended to change the economic behaviour of firms and individuals. In a natural monopoly the stated reasons are to curb market power, increase efficiency and avoid duplicating facilities. The instruments most often used are controls on prices, output, the rate of return, quality standards, disclosure of information and conditions of entry.

**Its example now:** A state sets up a regulator to approve the tariff that its single water utility may charge and the service standards it must meet, because a second network of pipes would cost more than it would save.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Regulation' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf
- OECD, OECD Glossary of Statistical Terms, entry 'Natural monopoly' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf

**Note:** Agrees with the source. The old example said TRAI regulates telecom tariffs because spectrum and towers create natural monopoly tendencies; no source was found for that reasoning, so the example is now a generic one.

### Market Failure (`market-failure`)

Status: published. Model draft: groq. Result: corrected.

**It said:** A market failure occurs when free markets fail to allocate resources efficiently, resulting in issues like public goods, externalities, natural monopoly, and information asymmetry. Practitioners use this term when identifying situations where government intervention is necessary to correct these inefficiencies, such as in the case of public health or environmental degradation, where the market alone cannot provide optimal outcomes.

**Its example said:** The Indian government's National Rural Employment Guarantee Act (NREGA) addresses a market failure by providing a safety net for rural laborers, ensuring a minimum wage and employment opportunities.

**It says now:** Market failure is a general term for situations in which market outcomes are not Pareto efficient, which means that someone could be made better off without making anyone else worse off. The main sources are market power, externalities (costs or benefits imposed on others for which the market sets no price), public goods (goods with low or zero marginal cost from which it is hard to exclude users) and incomplete markets, for example for some kinds of insurance. Market failures give a rationale for government intervention, such as regulation or public provision.

**Its example now:** A factory that pollutes a river does not bear the cost it imposes on people downstream. That negative externality is a market failure, and it is the usual argument for pollution standards or charges.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Market failure' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf
- OpenStax, Principles of Economics 3e, chapter 12 key terms, 'market failure' (2022). https://openstax.org/books/principles-economics-3e/pages/12-key-terms

**Note:** Broadly agreed with the source. The old text listed natural monopoly and information asymmetry as examples; the OECD entry frames the sources as market power, externalities, public goods and incomplete markets, and the entry now follows it and states the Pareto efficiency test.

### NITI Aayog (`niti-aayog`)

Status: seed. Model draft: no. Result: corrected.

**It said:** National Institution for Transforming India. Replaced the Planning Commission in 2015. Advisory body chaired by the Prime Minister with no financial allocation power. Produces strategy documents.

**Its example said:** NITI Aayog's SDG India Index and Aspirational Districts Programme are its most concrete policy contributions — rankings and benchmarks without budget authority.

**It says now:** NITI Aayog, the National Institution for Transforming India, was set up by a resolution of the Union Cabinet dated 1 January 2015. The resolution superseded the resolution of 15 March 1950 that had set up the Planning Commission. The Prime Minister is its Chairperson, and its Governing Council consists of the Chief Ministers of all the states and the Lieutenant Governors of the union territories. The resolution describes it as a think tank of the government that gives strategic and technical advice to the Centre and the states. Its listed objectives include fostering cooperative federalism, designing long-term policy and programme frameworks, and monitoring and evaluating programmes. They do not include allocating funds to states or ministries.

**Its example now:** A state takes part in NITI Aayog through its Chief Minister, who sits on the Governing Council, and can ask it for policy advice. It cannot look to NITI Aayog for a grant, because the resolution that created the body lists no role in allocating funds.

**Sources (all accessed 21 November 2026):**

- Cabinet Secretariat, Government of India, Resolution No. 511/2/1/2015-Cab. of 1 January 2015, Gazette of India Extraordinary, Part I, Section 1, paragraphs 12, 13 and 15 (2015). https://www.niti.gov.in/sites/default/files/2022-11/Cabinet_Secretariat_Resolution_dated_01-01-2015.pdf

**Note:** Agrees with the source. Added the date and legal form of its creation, its composition, and its stated functions. The statement that it has no power to allocate funds is now tied to the list of objectives in the resolution. The old example called the SDG India Index and the Aspirational Districts Programme its most concrete contributions, which is an opinion with no source; the example now uses only what the resolution says.

### Normative Analysis (`normative-analysis`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** Policy analysis asking what should be done — which outcomes are preferred, according to what values. Contrasts with positive analysis (describing what is and what effects a policy has). Always involves value judgements.

**Its example said:** Saying the PDS should be universal (not targeted) is a normative claim — it depends on how you weight inclusion errors versus exclusion errors.

**It says now:** Normative analysis asks what should be done: which outcomes are preferable, and according to which values. A normative statement describes how the world should be, while a positive statement describes the world as it is. Normative conclusions always rest on value judgements, so two analysts who agree on every fact can still disagree about the policy.

**Its example now:** Saying that the Public Distribution System should be universal is a normative claim. It depends on how much weight you give to wrongly excluding poor households compared with wrongly including better-off ones.

**Sources (all accessed 21 November 2026):**

- OpenStax, Principles of Economics 3e, chapter 2 key terms, 'normative statement' and 'positive statement' (2022). https://openstax.org/books/principles-economics-3e/pages/2-key-terms

**Note:** Agrees with the source. Rewritten in full sentences.

### Positive Analysis (`positive-analysis`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** Policy analysis describing what is — what a policy does, who gains, who loses, what the effects are. Distinguished from normative analysis. Good positive analysis is a precondition for meaningful normative debate.

**Its example said:** Measuring how much the PAHAL DBT scheme reduced LPG ghost connections is positive analysis; deciding whether DBT is preferable to in-kind subsidy involves normative choices.

**It says now:** Positive analysis describes what is: what a policy does, who gains, who loses and how large the effects are. A positive statement describes the world as it is and can in principle be checked against evidence, while a normative statement describes how the world should be. Sound positive analysis is needed before a normative debate can be an informed one.

**Its example now:** Measuring how far a direct benefit transfer scheme reduced duplicate LPG connections is positive analysis. Deciding whether cash transfers are preferable to subsidies in kind also involves normative choices.

**Sources (all accessed 21 November 2026):**

- OpenStax, Principles of Economics 3e, chapter 2 key terms, 'positive statement' and 'normative statement' (2022). https://openstax.org/books/principles-economics-3e/pages/2-key-terms

**Note:** Agrees with the source. Rewritten in full sentences.

### Proxy Indicator (`proxy-indicator`)

Status: seed. Model draft: no. Result: corrected.

**It said:** An indirect measure used when the concept of interest cannot be directly observed or is too expensive to measure directly.

**Its example said:** Using 'ownership of mobile phone' as a proxy for household wealth when comprehensive asset surveys are too costly.

**It says now:** A proxy indicator is a less direct way of measuring progress against a result. It is used when the result cannot be measured directly, or when data for the most suitable indicator are not available or would cost too much to collect. A proxy rests on an assumption that it moves with the thing of interest, and that assumption may not hold, so a proxy needs more careful interpretation than a direct measure.

**Its example now:** A programme that cannot track the reliability of a municipal waste service directly asks residents in a survey whether they are satisfied with it. Rising satisfaction suggests that the service has improved and does not prove it.

**Sources (all accessed 21 November 2026):**

- UNDP, Handbook on Planning, Monitoring and Evaluating for Development Results, section 'Proxy indicators', p. 64 (2009). http://web.undp.org/evaluation/handbook/documents/english/pme-handbook.pdf
- United Nations Development Group, Results-Based Management Handbook, Part 2 (2011). https://unsdg.un.org/sites/default/files/UNDG-RBM-Handbook-2012.pdf

**Note:** Agrees with the source. Added the caution, from the UNDP handbook, that the assumption behind a proxy may not hold. The example now follows the handbook's own (client satisfaction with a waste service).

### Quasi-Federal (`quasi-federal`)

Status: seed. Model draft: no. Result: corrected.

**It said:** A federal system with a strong central tilt. India's Constitution is quasi-federal — formally federal but with emergency provisions, Governor appointments, Concurrent List dominance, and historically Planning Commission allocation power favouring the centre.

**Its example said:** The Governor's power to delay state bills for Presidential assent, and the Centre's ability to invoke Article 356, give India's federation its central-tilt character.

**It says now:** Quasi-federal is a label for a constitution that divides power between a centre and states but tilts it towards the centre. It is often applied to India. In S.R. Bommai v. Union of India (1994), Justice Ahmadi wrote that the Constitution is more appropriately described as 'quasi-federal' because it is a mixture of federal and unitary elements, leaning more towards the latter. The label is contested. Other opinions in the same case said that the practical effect of the provisions matters more than the label, and that the greater power of the Centre does not make the states mere appendages of it.

**Its example now:** The Centre's power to impose President's Rule in a state under Article 356 is one of the features that lead writers to call India's federation quasi-federal. The Bommai judgment made the use of that power subject to judicial review.

**Sources (all accessed 21 November 2026):**

- Supreme Court of India, S.R. Bommai v. Union of India, judgment of 11 March 1994, 1994 AIR 1918, 1994 SCC (3) 1, opinion of Ahmadi J. at paragraph 24. https://indiankanoon.org/doc/60799/

**Note:** Corrected. The old entry stated flatly that India's Constitution is quasi-federal and listed 'Concurrent List dominance' and Planning Commission allocations as features, with no source. The entry now attributes the description to the Bommai judgment and says the label is contested within that judgment.

**Sources disagree:** Within S.R. Bommai (1994) the judges differ. Ahmadi J. calls the Constitution 'quasi-federal' (para 24); another opinion says it is not necessary to decide whether it is federal, quasi-federal or unitary (para 100); Jeevan Reddy J. says the greater power of the Centre does not make the states 'mere appendages' (para 276).

### Structural Transformation (`structural-transformation`)

Status: seed. Model draft: no. Result: corrected.

**It said:** The reallocation of economic activity from agriculture to manufacturing and services that accompanies development, involving changes in output, employment, and urbanization.

**Its example said:** China's share of agricultural employment fell from 70% in 1980 to under 25% by 2020 as workers moved to manufacturing and services.

**It says now:** Structural transformation is the reallocation of economic activity across the broad sectors of agriculture, manufacturing and services. As economies grow richer, the shares of agriculture in employment and value added fall and the shares of services rise, while the shares of manufacturing follow a hump shape, rising at lower levels of development and falling at higher ones. It is measured by sectoral shares of employment and value added.

**Its example now:** A country in which seven in ten workers farmed a generation ago and one in four does today, with the rest in factories and services, has gone through structural transformation.

**Sources (all accessed 21 November 2026):**

- Herrendorf, B., Rogerson, R. and Valentinyi, A., Growth and Structural Transformation, NBER Working Paper 18996, abstract and section 2 (2013). https://www.nber.org/papers/w18996

**Note:** Agrees with the source. The old example gave figures for China's agricultural employment (70% in 1980, under 25% by 2020) with no source, so the example is now generic. The definition no longer lists urbanisation as part of the definition, which the source does not.

### Multiple Equilibria (`multiple-equilibria`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** Same fundamentals can produce different stable outcomes—a key insight of development economics explaining persistent poverty.

**It says now:** Multiple equilibria describes a situation in which the same economic fundamentals are consistent with more than one stable outcome. In development economics the standard case is the big push. Murphy, Shleifer and Vishny (1989) show that when one firm's industrialisation raises demand for the products of other sectors, an economy can rest either in an equilibrium where no sector industrialises or in one where all do, and they interpret industrialisation as a move from the bad equilibrium to the good one. The idea is used to explain why poverty can persist without any difference in resources or technology, and why coordinated investment may be needed to leave the bad equilibrium.

**Its example now:** No firm in a poor region builds a factory because local demand is too small, and local demand stays small because no factories pay factory wages. If many firms invested at once, each would find a market.

**Sources (all accessed 21 November 2026):**

- Murphy, K. M., Shleifer, A. and Vishny, R. W., Industrialization and the Big Push, NBER Working Paper 2708 (1988), published in the Journal of Political Economy 97(5), 1989. https://www.nber.org/papers/w2708

**Note:** Agrees with the source. The old entry was one sentence with no example; it now names the standard model and what it shows.

### RCT Limitations (`rct-limitations`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Randomised Controlled Trials generate strong internal validity but face external validity problems: equilibrium effects at scale, political feasibility of the solution, and inability to test institutional reforms.

**Its example said:** An RCT showing a specific nutrition supplement works in selected blocks does not tell us whether a national ICDS supplementation programme would produce similar effects at scale.

**It says now:** A randomised controlled trial (RCT) gives an unbiased estimate of the average effect of a treatment in the sample that was studied, and it has known limits. Deaton and Cartwright (2018) set out the main ones. Randomisation does not make the treatment and control groups identical in any single trial, and it does not by itself give a precise estimate. The estimate applies to the trial sample only, so extending it to another population or to a programme at national scale needs separate justification. An RCT also shows whether something worked in one setting and says little about why. Other limits often raised are effects that appear only when a programme is scaled up, and reforms of institutions that cannot be randomised.

**Its example now:** An RCT that finds a nutrition supplement works in selected blocks does not by itself show that a national supplementation programme run through the regular system would have the same effect.

**Sources (all accessed 21 November 2026):**

- Deaton, A. and Cartwright, N., Understanding and Misunderstanding Randomized Controlled Trials, NBER Working Paper 22595 (2016, revised 2017), published in Social Science and Medicine 210, 2018. https://www.nber.org/papers/w22595

**Note:** Corrected. The old entry said RCTs 'generate strong internal validity' without qualification; the source says randomisation does not equalise everything across groups in a given trial and does not by itself deliver precision. The entry now says so and attributes the points.

**Sources disagree:** Deaton and Cartwright argue that demanding 'external validity' expects too much of an RCT; proponents such as J-PAL treat RCTs as the most credible single design for causal effects. The entry reports the limits and does not rank designs.

### Endline (`endline`)

Status: published. Model draft: groq. Result: corrected.

**It said:** An endline refers to the final data collection point at the conclusion of a program or intervention. Practitioners use endline data to assess the impact of their work by comparing it with baseline data, thereby measuring change over the program period. This comparison helps evaluate the effectiveness of the intervention and identify areas for improvement.

**Its example said:** The endline survey of the Janani Suraksha Yojana program showed a significant increase in institutional deliveries, indicating a positive impact on maternal health outcomes.

**It says now:** An endline is the round of data collection at the end of a programme or period. The OECD defines the end line as the conditions existing after an intervention or at the end of the period, against which changes from the baseline can be measured, monitored and evaluated. Comparing endline with baseline shows how much changed. It does not by itself show that the programme caused the change, which needs a comparison group or another way of estimating what would have happened without the programme.

**Its example now:** A sanitation programme surveys the same villages before it starts and after it closes. The second survey is the endline, and the difference from the baseline shows how far toilet use has changed.

**Sources (all accessed 21 November 2026):**

- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'End line', p. 30 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf
- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Counterfactual', p. 25 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf

**Note:** Corrected. The old entry said practitioners use endline data 'to assess the impact' of a programme. A baseline to endline comparison measures change and does not by itself establish impact, and the entry now says so.

### Midline (`midline`)

Status: published. Model draft: no. Result: agrees with the source; source added.

**It said:** A data-collection round conducted partway through a programme to track progress and allow course correction before the endline.

**Its example said:** A midline survey after 12 months showed uptake was lagging, prompting a redesign of the outreach.

**It says now:** A midline is a round of data collection carried out partway through a programme, using the same measures as the baseline, to track progress and allow corrections before the endline. The OECD glossary does not define 'midline'. Its nearest term is the mid-term evaluation, an evaluation performed towards the middle of the period of implementation of the intervention.

**Its example now:** Halfway through a five-year reading programme, the team repeats the baseline reading test in a sample of schools and finds that two districts are behind, so it adds teacher support there.

**Sources (all accessed 21 November 2026):**

- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Mid-term evaluation', p. 43 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf

**Note:** Agrees with the nearest defined term. The source defines 'mid-term evaluation' and not 'midline'; the entry says so.

### Aggregation (`aggregation`)

Status: published. Model draft: groq. Result: agrees with the source; source added.

**It said:** Aggregation refers to the process of combining multiple data points into summary statistics like sums, means, or counts. A practitioner would use aggregation when they need to simplify complex data, identify trends, or make informed decisions, such as analyzing the overall impact of a program like the Janani Suraksha Yojana on maternal health outcomes across different regions.

**Its example said:** The National Sample Survey Office (NSSO) aggregates data from various states to calculate the national poverty rate in India.

**It says now:** Aggregation is the combining of data into a summary. In official statistics it has two related senses: combining related categories of a classification to give information at a broader level than the one at which observations were taken, and compounding primary data into an aggregate such as a total, a mean or an index number. Aggregation makes patterns easier to see and hides variation inside each group, so a conclusion that holds for the aggregate may not hold for the units within it.

**Its example now:** District figures for school enrolment are added up to give a state total. The total can rise while enrolment falls in several districts, which only the district figures show.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Aggregation' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf

**Note:** Agrees with the source. Added the caution that aggregation hides variation within groups.

### Data Dictionary (`data-dictionary`)

Status: published. Model draft: groq. Result: agrees with the source; source added.

**It said:** A data dictionary is a documentation that describes data elements, including definitions, formats, allowed values, and relationships. Practitioners use data dictionaries when designing surveys, monitoring and evaluation frameworks, or databases to ensure data consistency and accuracy, particularly when working with large datasets or multiple stakeholders.

**Its example said:** The National Sample Survey Office (NSSO) uses a data dictionary to standardize data collection for its surveys, such as specifying the format for date of birth or occupation codes.

**It says now:** A data dictionary is a store of metadata: data that describe the use and structure of other data. For a dataset it lists each field with its name, definition, format and permitted values, and describes how the tables are structured. It lets someone who did not collect the data read and use them correctly.

**Its example now:** A household survey team shares its dataset with a data dictionary that says the variable 'hh_size' counts usual residents, is a whole number from 1 to 30, and is coded 99 where missing.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Data dictionary' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf

**Note:** Agrees with the source. Rewritten in plain sentences.

### Collateral (`collateral`)

Status: published. Model draft: groq. Result: agrees with the source; source added.

**It said:** Collateral refers to assets pledged by a borrower to secure a loan, which can be seized by the lender in case of default. Practitioners use this term when designing credit programs or assessing the financial inclusion of marginalized groups, such as farmers or low-income households, who often lack acceptable collateral to access formal credit.

**Its example said:** In India, the Kisan Credit Card scheme allows farmers to use their land as collateral to access credit for agricultural purposes.

**It says now:** Collateral is something of value, often property or equipment, that a borrower pledges to a lender and that the lender has the right to seize and sell if the loan is not repaid. It lowers the lender's loss from default and so makes lending possible to borrowers whose ability or intention to repay the lender cannot observe. Poor households often have no assets a formal lender will accept, which is one reason they are refused credit or pay more for it.

**Its example now:** A bank lends against a title deed to land. A landless labourer has nothing comparable to pledge, so she borrows from a moneylender at a higher rate or joins a self-help group that lends without physical collateral.

**Sources (all accessed 21 November 2026):**

- OpenStax, Principles of Economics 3e, chapter 16 key terms, 'collateral' (2022). https://openstax.org/books/principles-economics-3e/pages/16-key-terms
- OECD, OECD Glossary of Statistical Terms, entry 'Collateral' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf

**Note:** Agrees with the source. The OECD glossary's entry is narrower (assets pledged to central banks); the general definition follows the textbook.

### Rent-Seeking (`rent-seeking`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Using political processes to capture economic rents rather than to create value. Bardhan applies this to India's dominant proprietary classes — industrial capital, rich farmers, professionals — who used planning to protect rents.

**Its example said:** Firms spending resources lobbying for import licences rather than improving productivity is rent-seeking — socially wasteful competition for policy-created privileges.

**It says now:** Rent-seeking is the spending of scarce resources to capture a rent, a return above what a competitive market would pay, without creating new value. The OECD describes it as the use of resources to secure the right to become a monopolist, usually by persuading governments to impose regulations such as entry restrictions and import controls. Anne Krueger's 1974 paper on the rent-seeking society showed that competition for import licences uses up real resources, and estimated that rents from government controls came to about 7.3 per cent of India's national income in 1964. Rent-seeking can be legal, as with lobbying, or illegal, as with bribery and smuggling.

**Its example now:** Firms that spend money and staff time lobbying for a scarce import licence, when they could have spent it on raising productivity, are rent-seeking. The licence transfers income to whoever wins it and adds nothing to output.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Rent seeking' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf
- Krueger, A. O., The Political Economy of the Rent-Seeking Society, American Economic Review 64(3), 291-303 (1974). https://www.aeaweb.org/aer/top20/64.3.291-303.pdf

**Note:** Corrected. The old entry attributed an application of the idea to Pranab Bardhan's account of India's dominant proprietary classes. I could not open Bardhan's book, so that sentence is removed. The entry now cites the OECD definition and Krueger's 1974 paper, including her estimate for India.

### Policy Window (`policy-window`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** Kingdon's concept of the brief period when a problem stream, political stream, and policy solution stream align, opening an opportunity for significant policy change. Windows open unpredictably and close quickly.

**Its example said:** India's 1991 BOP crisis opened a window for liberalisation — the problem (reserve crisis), politics (Congress mandate), and solution (Manmohan Singh's framework) all aligned.

**It says now:** A policy window is a short period in which a problem is recognised, a workable solution is available and the political will to act exists, so that a change in policy becomes possible. The term comes from John Kingdon's multiple streams framework (1984), in which the problem, policy and politics streams run separately until they are joined. Policy entrepreneurs use the window to couple a problem with a solution and press decision-makers to adopt it. Windows often close without any action being taken.

**Its example now:** India's 1991 balance of payments crisis is often read as a policy window. The crisis defined the problem, proposals for liberalisation had been circulating for years, and a new government had the will to act.

**Sources (all accessed 21 November 2026):**

- Hoefer, R., The Multiple Streams Framework: Understanding and Applying the Problems, Policies, and Politics Approach, Journal of Policy Practice and Research 3(1), 1-5 (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8861624/

**Note:** Agrees with the source. Kingdon's own book could not be opened, so the citation is to a peer-reviewed summary of his framework. The 1991 example is kept and is now worded as an interpretation.

### Agenda-Setting (`agenda-setting`)

Status: published. Model draft: gemini. Result: corrected.

**It said:** Agenda-setting describes the critical process by which social issues or problems gain enough public and political attention to be considered for government action and policy formulation. For practitioners, understanding agenda-setting is vital for advocating for specific interventions, designing effective programs, and framing proposals to align with current policy priorities. It involves identifying windows of opportunity where problems, political will, and feasible solutions converge. Misuse often occurs when practitioners assume a problem's severity alone guarantees policy attention, overlooking the political and institutional dynamics required for an issue to move onto the official agenda.

**Its example said:** Sustained advocacy by civil society organizations and public interest litigations (PILs) played a key role in placing the right to food on India's policy agenda, culminating in schemes like Antyodaya Anna Yojana (AAY) and the National Food Security Act. This wasn't just about the problem of hunger, but about creating the political and policy momentum for action.

**It says now:** Agenda-setting is the stage of policy-making at which some problems gain enough public and political attention to be considered for government action while others do not. In John Kingdon's multiple streams framework, an issue reaches the agenda when a recognised problem, an available solution and favourable politics come together in a policy window, often through the work of policy entrepreneurs. The severity of a problem does not by itself put it on the agenda.

**Its example now:** A coalition that wants a state to act on child malnutrition publishes district survey figures to define the problem, offers a costed proposal, and waits for a new government or a budget to press its case.

**Sources (all accessed 21 November 2026):**

- Hoefer, R., The Multiple Streams Framework: Understanding and Applying the Problems, Policies, and Politics Approach, Journal of Policy Practice and Research 3(1), 1-5 (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8861624/

**Note:** Corrected. The old example said that advocacy and public interest litigation on the right to food 'culminated in' Antyodaya Anna Yojana; no source was found for that sequence, so the example is now a generic one. The definition is shortened and tied to Kingdon's framework.

### Reform by Stealth (`reform-by-stealth`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Achieving policy change through administrative action that avoids legislative visibility — DBT replacing PDS cash flows, Aadhaar expansion, LPG subsidy transfer — faster but less durable than legislation.

**Its example said:** The PAHAL scheme shifting LPG subsidy to bank transfers was implemented administratively without legislation — enabling fast rollout but vulnerable to reversal by executive order.

**It says now:** Reform by stealth is Rob Jenkins's term, from his 1999 study of India's economic liberalisation, for the way governing elites introduced reforms without provoking organised resistance. He argues that they relied on political skill and obfuscation more than on open persuasion. The tactics he lists include presenting policy change as continuity, shifting blame to opponents, quietly compensating selected interests, concealing intentions, and sequencing reforms to their own advantage. The term is now also used more loosely for reform carried out through low-visibility administrative action in place of legislation.

**Its example now:** A government raises an administered price in several small steps, describes each step as a routine revision, and offers an affected group a separate concession, so that no single moment gives opponents an occasion to mobilise.

**Sources (all accessed 21 November 2026):**

- Jenkins, R., Democratic Politics and Economic Reform in India, Cambridge University Press (1999), introduction and conclusion, as posted by the author. https://www2.hunter.cuny.edu/pending-migration/polsci/faculty/jenkins/1999-democratic-politics-and-economic-reform-in-india-intro-and-conclusion.pdf

**Note:** Corrected. The old entry defined the term as policy change through administrative action that avoids legislation and gave direct benefit transfers, Aadhaar and the PAHAL scheme as examples. Jenkins's term, coined in 1999, describes the political tactics used to introduce liberalisation in the 1990s. The entry now gives his meaning first and marks the looser usage as such. The file is a scan, so page numbers could not be read and none are given.

### Regulatory Impact Assessment (RIA) (`regulatory-impact-assessment`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Structured analysis of a proposed regulation's costs, benefits, and alternatives. Standard in OECD countries; not systematically required in India.

**Its example said:** India has no mandatory RIA process — regulations are often promulgated without cost-benefit analysis, creating compliance burden without documented evidence of net benefit.

**It says now:** Regulatory impact assessment, which the OECD calls regulatory impact analysis (RIA), is a systemic approach to critically assessing the positive and negative effects of proposed and existing regulations and of non-regulatory alternatives. It asks what problem the rule is meant to solve, what the options are, who bears the costs and who receives the benefits, before the rule is made.

**Its example now:** Before requiring all small food businesses to install a new kind of equipment, a regulator estimates the cost to the businesses, the expected fall in illness, and whether training or labelling would achieve the same result at lower cost.

**Sources (all accessed 21 November 2026):**

- OECD, Regulatory Impact Analysis: A Tool for Policy Coherence, OECD Reviews of Regulatory Reform (2009). https://www.oecd.org/en/publications/2009/09/regulatory-impact-analysis_g1ghb202.html

**Note:** Agrees with the source. The old entry and example said RIA is not systematically required in India; no source was found for that statement, so it is removed.

### Sunset Clause (`sunset-clause`)

Status: seed. Model draft: no. Result: corrected.

**It said:** A provision requiring a regulation or programme to expire on a specific date unless actively renewed. Prevents regulatory accumulation and forces periodic review of appropriateness.

**Its example said:** India has no systematic sunset clause requirement — old regulations pile up alongside new ones, creating compliance burden without commensurate benefit review.

**It says now:** A sunset clause is a provision under which a law or regulation expires automatically after a specified period, so that further legislative action is needed for it to remain in force. It differs from a review clause, which requires the rule to be reviewed by a set date and leaves it in force unless someone acts to remove it. Sunset clauses are used to force a periodic decision on whether a rule is still needed.

**Its example now:** A regulation made during an emergency states that it will lapse two years after it comes into force. If the government still wants it then, it must make the regulation again and justify it.

**Sources (all accessed 21 November 2026):**

- HM Government (United Kingdom), Sunsetting Regulations: Guidance, paragraph 15 (2011). http://data.parliament.uk/DepositedPapers/Files/DEP2011-0504/DEP2011-0504.pdf

**Note:** Agrees with the source. Added the distinction between a sunset clause and a review clause. The old example said India has no systematic sunset clause requirement; no source was found, so it is removed.

### Veto Player (`veto-player`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Tsebelis's concept — an actor whose agreement is necessary for a policy change. More veto players means greater policy stability and reform difficulty.

**Its example said:** India's coalition era (1989–2014) had more veto players than single-party majority governments — making reforms slower but sometimes more durable through broader consensus.

**It says now:** A veto player is an individual or collective actor whose agreement is required for a change of the status quo. George Tsebelis, who introduced the concept in 1995, distinguishes institutional veto players, such as a president or a legislative chamber, from partisan ones, such as the parties in a governing coalition. In his framework the potential for policy change falls as the number of veto players rises and as their policy positions move further apart.

**Its example now:** A single-party majority government has one veto player and can change policy quickly. A coalition of five parties has five, and a reform must be acceptable to each of them.

**Sources (all accessed 21 November 2026):**

- Tsebelis, G., Decision Making in Political Systems: Veto Players in Presidentialism, Parliamentarism, Multicameralism and Multipartyism, British Journal of Political Science 25(3), 289-325 (1995). https://doi.org/10.1017/S0007123400007225

**Note:** Agrees with the source. The old example stated that India's coalition era of 1989 to 2014 made reforms slower but sometimes more durable; that is an empirical claim with no source, so the example is now generic. The abstract was read through the publisher's Crossref record because the journal page blocks automated access.

### Zero-Based Budgeting (`zero-based-budgeting`)

Status: seed. Model draft: no. Result: corrected.

**It said:** A budgeting approach requiring each programme to justify its full allocation from zero every year, rather than using the prior year's allocation as the base.

**Its example said:** Zero-based budgeting is rarely implemented in practice but used rhetorically by governments signalling fiscal reform intent — India has never applied it systematically.

**It says now:** Zero-based budgeting (also zero-base budgeting, ZBB) is a budgeting process that asks managers to build a budget from the ground up, starting from zero, so that every activity has to be justified and not only the changes from last year. It is the opposite of incremental budgeting. Its value is disputed, because the analysis it requires is costly to carry out.

**Its example now:** A department head preparing next year's request cannot start from this year's figure. She has to list each service, what it would cost at different levels of provision, and why it should be funded at all.

**Sources (all accessed 21 November 2026):**

- Kavanagh, S., Zero-Base Budgeting, Government Finance Officers Association (2011). https://www.gfoa.org/materials/zero-base-budgeting

**Note:** Corrected. The old example said India has never applied zero-based budgeting systematically; no source was found for that, so it is removed. The source is a professional association's research paper; no definition by the IMF or OECD could be opened.

### Zamindari Abolition (`zamindari-abolition`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Post-independence land reforms eliminating intermediary landlords. Partially successful—land often transferred to upper castes rather than tillers.

**It says now:** Zamindari abolition refers to the laws passed by Indian states after independence to abolish zamindars and other intermediaries who stood between the state and the cultivator. The laws let the state acquire the estates and extinguish the intermediaries' rights. Their validity was challenged in litigation under the fundamental rights, which held up implementation, and Parliament responded with the Constitution (First Amendment) Act, 1951. It inserted Article 31A, which protects laws for the acquisition of estates from challenge under the fundamental rights, and Article 31B with the Ninth Schedule, which validated named state Acts.

**Its example now:** A state Act vests a zamindar's estate in the government, pays him compensation, and makes the cultivators who had paid him rent pay land revenue directly to the state.

**Sources (all accessed 21 November 2026):**

- Government of India, The Constitution (First Amendment) Act, 1951, Statement of Objects and Reasons and section 4 (inserting Article 31A). https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2023/03/2023030234-2.pdf

**Note:** Corrected. The old entry said the reforms were 'partially successful' and that land was 'often transferred to upper castes rather than tillers'. No source was opened that supports that assessment, so it is removed. The entry now states what the laws did and how the Constitution was amended to protect them.

### Person-Days (`person-days`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Standard unit measuring NREGA employment: one person working one day. Annual target measured in crore person-days generated.

**It says now:** A person-day is one person working for one day. It is the unit in which employment under India's rural employment guarantee is counted: the persondays generated in a year are the total days of work done by registered workers in that financial year. Under the Mahatma Gandhi National Rural Employment Guarantee Act, 2005, a household was entitled to at least 100 days of work in a financial year. The Viksit Bharat Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, 2025, which replaces it, guarantees 125 days.

**Its example now:** If 40 workers in a Gram Panchayat each work 25 days on a pond in one year, the work has generated 1,000 person-days.

**Sources (all accessed 21 November 2026):**

- Accountability Initiative, Centre for Policy Research, Budget Briefs vol. 10, issue 9: Mahatma Gandhi National Rural Employment Guarantee Scheme, GoI, 2018-19 (2018). https://cprindia.org/wp-content/uploads/2021/12/Mahatma-Gandhi-National-Rural-Employment-Guarantee-Scheme_0.pdf
- Government of India, The Viksit Bharat Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, 2025 (No. 36 of 2025), long title, as published by PRS Legislative Research. https://prsindia.org/files/bills_acts/bills_parliament/2025/Viksit_Bharat_G_RAM_G_Act_2025.pdf

**Note:** Agrees with the source. Added the statutory entitlements and the 2025 Act. The old entry said an 'annual target' is set in crore person-days; the official term is the labour budget, which I did not verify, so the sentence is removed. No definition in a Ministry of Rural Development document could be opened; the definition cited is from a budget brief that draws on the Ministry's MIS.

### Kuznets Curve (`kuznets-curve`)

Status: published. Model draft: groq. Result: corrected.

**It said:** The Kuznets Curve is a hypothesis that describes the relationship between economic development and income inequality. It suggests that as an economy grows, inequality initially increases and then decreases, forming an inverted-U shape. Practitioners use this concept to understand the potential impact of economic development on social inequality and to inform policies that address poverty and inequality, particularly in the context of South Asian countries like India, where schemes like the Antyodaya Anna Yojana (AAY) aim to reduce poverty.

**Its example said:** India's economic liberalization in the 1990s led to increased inequality, but later initiatives like the Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) helped reduce it.

**It says now:** The Kuznets curve is the hypothesis that income inequality first rises and then falls as an economy develops, tracing an inverted U. It comes from Simon Kuznets's 1955 paper, which suggested a long swing in inequality: widening in the early phases of economic growth, when the shift from a pre-industrial to an industrial economy is fastest, stabilising for a while, and narrowing in the later phases. Kuznets called his own account preliminary speculation based on scarce data. It is a hypothesis about a pattern, and it may or may not hold in a given country.

**Its example now:** A country's Gini coefficient rises for three decades as workers move from farms to better-paid city jobs, and falls later as most workers are already in the modern sector and schooling spreads. That path would fit the hypothesis.

**Sources (all accessed 21 November 2026):**

- Kuznets, S., Economic Growth and Income Inequality, American Economic Review 45(1), 1-28, at p. 18 (1955). https://www.aeaweb.org/aer/top20/45.1.1-28.pdf

**Note:** Corrected. The old example stated as fact that India's liberalisation raised inequality and that MGNREGA later reduced it, and the definition linked the curve to Antyodaya Anna Yojana. Neither has a source and neither follows from the hypothesis. The entry now quotes Kuznets's own formulation and his caution about the evidence.

### Licence Raj (`licence-raj`)

Status: published. Model draft: groq. Result: corrected.

**It said:** Licence Raj refers to India's pre-1991 system of pervasive government licensing of industrial activity, where firms required licences for production, capacity expansion, import, and technology choice. Practitioners may use this term when analyzing the historical context of India's economic reforms, understanding the challenges of doing business in a heavily regulated environment, or evaluating the impact of deregulation on industrial growth.

**Its example said:** The Indian cement industry, prior to 1991, had to obtain multiple licences from various ministries to expand production, illustrating the bureaucratic hurdles of Licence Raj.

**It says now:** Licence Raj is the name given to the system of industrial licensing introduced by the Industries (Development and Regulation) Act, 1951, under which the central government regulated and restricted the entry of new firms and the expansion of existing ones in registered manufacturing. It was dismantled in stages: about a third of industries were exempted from licensing in March 1985, and most of the rest were delicensed in 1991.

**Its example now:** A manufacturer that wanted to build a second plant had to apply to the central government for a licence before it could invest, whatever the demand for its product.

**Sources (all accessed 21 November 2026):**

- Aghion, P., Burgess, R., Redding, S. J. and Zilibotti, F., The Unequal Effects of Liberalization: Evidence from Dismantling the License Raj in India, American Economic Review 98(4), 1397-1412 (2008). https://www.aeaweb.org/articles?id=10.1257/aer.98.4.1397
- Aghion, P., Burgess, R., Redding, S. and Zilibotti, F., The Unequal Effects of Liberalization: Evidence from Dismantling the License Raj in India, NBER Working Paper 12031, introduction (2006). https://www.nber.org/system/files/working_papers/w12031/w12031.pdf

**Note:** Corrected. The old entry said licences were needed for 'production, capacity expansion, import, and technology choice' and described the system as 'pre-1991'. The source describes industrial licensing of entry and expansion under the 1951 Act and dates delicensing to 1985 and 1991. The old example about the cement industry had no source and is replaced.

### Concurrent List (`concurrent-list`)

Status: published. Model draft: groq. Result: corrected.

**It said:** The Concurrent List refers to a list of 52 subjects in the Seventh Schedule where both Parliament and state legislatures have the power to legislate. Practitioners working on policy implementation, particularly in areas like education or healthcare, use this term to understand the division of legislative powers between the central government and states, and to navigate potential conflicts between central and state laws.

**Its example said:** The Right to Education Act, a central law, and state-specific education acts, such as the Maharashtra Education Act, coexist because education is on the Concurrent List.

**It says now:** The Concurrent List is List III in the Seventh Schedule to the Constitution of India. Under Article 246(2), both Parliament and the legislature of a state may make laws on the matters it lists, which include criminal law, forests, education, labour welfare and economic and social planning. The list has 47 numbered entries and five more inserted by amendment (11A, 17A, 17B, 20A and 33A), 52 in all. Under Article 254, where a state law on a Concurrent List matter is repugnant to a law made by Parliament, the central law prevails and the state law is void to the extent of the repugnancy, unless the state law was reserved for the President and received assent.

**Its example now:** Education is entry 25 of the Concurrent List, so both Parliament and a state legislature can make laws on schools, subject to the rule in Article 254.

**Sources (all accessed 21 November 2026):**

- Legislative Department, Ministry of Law and Justice, The Constitution of India, as on 1 May 2026, Articles 246 and 254 and Seventh Schedule, List III (2026). https://www.legislative.gov.in/static/uploads/2025/07/c9fe9c9b6840524844316f74bb1c556c.pdf

**Note:** Agrees with the source on the count of 52. Added the Articles that give the list its effect and the rule on repugnancy. The old example named a 'Maharashtra Education Act', which could not be verified, so it is replaced.

### Subsidiarity (`subsidiarity`)

Status: published. Model draft: no. Result: agrees with the source; source added.

**It said:** The principle that decisions and functions should be handled at the lowest or most local level capable of doing so effectively, with higher levels intervening only when local action is insufficient. It provides a normative rationale for decentralisation and for assigning responsibilities across tiers of government. It balances local responsiveness against the need for coordination and economies of scale.

**Its example said:** Subsidiarity suggests village-level bodies should manage local water and sanitation, while inter-state river disputes rise to a national body better placed to resolve them.

**It says now:** Subsidiarity is the principle that decisions should be taken at the lowest level of government able to take them effectively, with a higher level acting only where it can do better. Its best-known legal statement is Article 5(3) of the Treaty on European Union. Under it the Union does not act, outside the areas of its exclusive competence, unless its action is more effective than action taken at national, regional or local level. The aim is that decisions are taken as closely as possible to the citizen. The principle gives a reasoned basis for decentralisation and for dividing functions among tiers of government.

**Its example now:** Subsidiarity suggests that a village body should manage its own drinking water supply, while a dispute between states over a shared river goes to a national body.

**Sources (all accessed 21 November 2026):**

- Publications Office of the European Union, EUR-Lex Glossary of summaries, 'Principle of subsidiarity'. https://eur-lex.europa.eu/EN/legal-content/glossary/principle-of-subsidiarity.html

**Note:** Agrees with the source. Added the legal source of the principle in EU law.

### Inter-Rater Reliability (`inter-rater-reliability`)

Status: published. Model draft: no. Result: agrees with the source; source added.

**It said:** The degree to which different observers or coders assign the same rating to the same thing.

**Its example said:** Two enumerators scored the same interviews to check inter-rater reliability before full coding.

**It says now:** Inter-rater reliability is the extent to which different data collectors or coders assign the same score to the same thing. The simplest measure is per cent agreement, the number of agreements divided by the number of scores. Cohen's kappa adjusts for the agreement expected by chance and ranges from -1 to +1. Low inter-rater reliability means that the data partly reflect who collected them.

**Its example now:** Two enumerators independently score the same 30 classroom observations. They agree on 24, which is 80 per cent agreement, and the team computes kappa before deciding whether the scoring guide needs revision.

**Sources (all accessed 21 November 2026):**

- McHugh, M. L., Interrater reliability: the kappa statistic, Biochemia Medica 22(3), 276-282 (2012). https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/

**Note:** Agrees with the source. Expanded from one line to say how it is measured.

### Infant Industry Argument (`infant-industry-argument`)

Status: published. Model draft: groq. Result: corrected.

**It said:** The Infant Industry Argument is an economic concept that advocates for temporary protection of new industries until they achieve scale economies and learning-by-doing benefits to compete internationally. Practitioners use this argument when designing industrial policies or trade agreements to support the growth of domestic industries, such as textiles or manufacturing, in countries like India or Bangladesh, where they face competition from established foreign firms.

**Its example said:** India's protection of its textile industry in the 1980s allowed companies like Reliance Industries to grow and compete globally.

**It says now:** The infant industry argument is the case for protecting a new domestic industry from imports for a limited time, so that it can reach the scale and experience it needs to compete, after which the protection is removed. Economists accept that the argument can hold in theory. In practice the protection is hard to withdraw, and many protected industries have never become competitive.

**Its example now:** A country bars imports of computers for a decade to let local makers grow. Consumers pay more for worse machines throughout, and whether the policy succeeds depends on whether the firms can compete once the barrier is lifted.

**Sources (all accessed 21 November 2026):**

- OpenStax, Principles of Economics 3e, section 34.3, Arguments in Support of Restricting Imports (2022). https://openstax.org/books/principles-economics-3e/pages/34-3-arguments-in-support-of-restricting-imports

**Note:** Corrected. The old example said India's protection of textiles in the 1980s allowed Reliance Industries to grow and compete globally; no source supports that causal claim, so it is removed. The entry now states the standard objection alongside the argument.

### Leading Indicator (`leading-indicator`)

Status: published. Model draft: groq. Result: corrected.

**It said:** A leading indicator is a predictive measure that changes before the outcome of interest, enabling early warning and course correction. Practitioners use leading indicators to identify potential issues before they escalate, allowing for timely interventions and adjustments to programs or policies, such as monitoring school attendance rates to predict learning outcomes.

**Its example said:** The Janani Suraksha Yojana program uses institutional delivery rates as a leading indicator to predict maternal and infant mortality rates.

**It says now:** A leading indicator is a measure that changes before the outcome of interest and so gives early warning. In workplace safety, where the pairing is formally defined, the United States Occupational Safety and Health Administration describes leading indicators as proactive and preventive measures that show whether activities are working and reveal problems early. In a programme, a leading indicator is useful only if there is evidence that it does move ahead of the outcome.

**Its example now:** A reading programme tracks how many days teachers taught the new lessons each month. If that number falls, the team can act long before the end-of-year reading test.

**Sources (all accessed 21 November 2026):**

- Occupational Safety and Health Administration, United States Department of Labor, Leading Indicators. https://www.osha.gov/leading-indicators

**Note:** Corrected. The old example said the Janani Suraksha Yojana 'uses institutional delivery rates as a leading indicator to predict' mortality; no source was found for that, so it is replaced. The only formal definition opened is from occupational safety, and the entry says so.

### Lagging Indicator (`lagging-indicator`)

Status: published. Model draft: groq. Result: corrected.

**It said:** A lagging indicator is a measure that changes after an outcome has occurred, used to validate whether intended changes happened. Practitioners use lagging indicators to assess the long-term impact of their interventions, often after a significant period has passed, to determine if their efforts have been successful.

**Its example said:** The reduction in stunting prevalence among children in India's Antyodaya Anna Yojana (AAY) scheme is a lagging indicator of the effectiveness of nutrition interventions.

**It says now:** A lagging indicator measures an outcome after it has happened. In workplace safety, where the pairing is formally defined, lagging indicators measure the occurrence and frequency of past events, such as the rate of injuries. Lagging indicators confirm whether the intended change took place. They arrive too late to correct the course of the activity that produced them, which is why they are paired with leading indicators.

**Its example now:** The share of children who are stunted, measured in a survey every few years, is a lagging indicator for a nutrition programme. It shows the result of several years of feeding, illness and care.

**Sources (all accessed 21 November 2026):**

- Occupational Safety and Health Administration, United States Department of Labor, Leading Indicators. https://www.osha.gov/leading-indicators

**Note:** Corrected. The old example referred to 'children in India's Antyodaya Anna Yojana scheme', which is a food subsidy category for households and has no stunting indicator of its own. The example is now generic.

### Empowerment (`empowerment`)

Status: published. Model draft: no. Result: agrees with the source; source added.

**It said:** The process by which people who have been denied power expand their ability to make strategic life choices and act on them, spanning economic, social, political and personal dimensions. Naila Kabeer's framing links it to resources, agency and achievements. It is a process of change from within, not something that can simply be delivered to people from outside.

**Its example said:** A women's self-help group in Andhra Pradesh reported empowerment when members began negotiating crop prices and contesting local elections, not just accessing loans.

**It says now:** Empowerment, in Naila Kabeer's widely used definition, is the process by which those who have been denied the ability to make strategic life choices acquire that ability. She describes the ability to exercise choice through three connected dimensions: resources (material, human and social, including future claims to them), agency (decision-making, and also negotiation and resistance) and achievements (well-being outcomes). She argues that an indicator of empowerment can be read correctly only when all three are considered together.

**Its example now:** Members of a women's self-help group begin to negotiate crop prices and to stand in local elections. Access to loans was the resource, and the new choices they make are the evidence of empowerment.

**Sources (all accessed 21 November 2026):**

- Kabeer, N., Resources, Agency, Achievements: Reflections on the Measurement of Women's Empowerment, Development and Change 30(3), 435-464 (1999). https://doi.org/10.1111/1467-7660.00125

**Note:** Agrees with the source. The wording of the definition now follows Kabeer's abstract. The abstract was read through the publisher's Crossref record.

### Cabinet Note (`cabinet-note`)

Status: published. Model draft: groq. Result: corrected.

**It said:** A Cabinet Note is a formal document that presents a policy proposal to the Union Cabinet for approval. Practitioners use Cabinet Notes when they need to understand how policies are proposed and approved at the highest levels of government, such as when analyzing the implementation of schemes like the Janani Suraksha Yojana or the Antyodaya Anna Yojana (AAY).

**Its example said:** The draft National Health Policy would have been presented to the Union Cabinet through a Cabinet Note before being introduced in Parliament.

**It says now:** A Cabinet Note is the document through which a ministry or department of the Government of India places a proposal before the Union Cabinet or a Committee of the Cabinet for a decision. The cases that need such approval are listed in the schedules to the Government of India (Transaction of Business) Rules, 1961, and include proposals for legislation and ordinances. The Cabinet Secretariat's handbook requires a note to set out the background, the proposal, its justification and the results of consultation with other ministries.

**Its example now:** Before a ministry introduces a Bill in Parliament, it circulates a draft note to the other ministries concerned, records their comments, and sends the final 'Note for the Cabinet' to the Cabinet Secretariat.

**Sources (all accessed 21 November 2026):**

- Cabinet Secretariat, Government of India, Handbook on Writing Cabinet Notes, updated till 23 July 2021, sections 1 to 3. https://cabsec.gov.in/report_document/handbook/english/1_Upload_3722.pdf

**Note:** Agrees with the source. Added the rules that decide when a note is needed and what it must contain. The old example speculated about the National Health Policy; it is replaced with the general procedure.

### Data Types (`data-types`)

Status: published. Model draft: groq. Result: corrected.

**It said:** Data types refer to categories of data, including nominal, ordinal, interval, and ratio, which determine how data is measured and analyzed. Practitioners use data types to choose the appropriate visual encoding and statistical methods for their data, ensuring accurate interpretation and effective communication of results, especially in monitoring and evaluation plans.

**Its example said:** In the Antyodaya Anna Yojana scheme, household income is an example of ratio data, while education level of household members is an example of ordinal data.

**It says now:** Data types, also called levels of measurement, describe what kind of information a variable carries. A categorical or nominal variable has categories with no intrinsic order, such as district. An ordinal variable has ordered categories whose spacing is not known to be equal, such as level of schooling. An interval or numerical variable has equally spaced values, such as income in rupees. Many texts also separate ratio variables, which have a true zero. The type decides which summaries and charts are valid: a mean is meaningful for an interval variable and not for a nominal one.

**Its example now:** In a household survey, monthly income in rupees is numerical, the highest class a member completed is ordinal, and religion is nominal.

**Sources (all accessed 21 November 2026):**

- UCLA Office of Advanced Research Computing, Statistical Methods and Data Analytics, What is the difference between categorical, ordinal and interval variables? https://stats.oarc.ucla.edu/other/mult-pkg/whatstat/what-is-the-difference-between-categorical-ordinal-and-interval-variables/

**Note:** Agrees with the source for nominal, ordinal and interval. The source does not define ratio variables, and the entry says only that many texts add them. The old example tied the types to the Antyodaya Anna Yojana scheme for no reason; it is now a plain survey example.

### Small Multiples (`small-multiples`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** A series of similar charts using the same scale and axes, allowing comparison across different categories or time periods.

**Its example said:** Showing literacy rates for 10 states as 10 identical line charts side-by-side enables easy comparison of trends.

**It says now:** Small multiples are a set of small charts of the same kind, each showing one category or period, placed side by side so that they can be compared. The United Kingdom's Government Analysis Function recommends them in place of a crowded stacked or multi-line chart, because it is easier to see what is happening in each category and the reader does not have to rely on colour to tell the categories apart.

**Its example now:** Ten small line charts, one for each state and all with the same axes, show the literacy rate over time. A reader can compare the shapes at a glance.

**Sources (all accessed 21 November 2026):**

- Government Analysis Function (United Kingdom), Data visualisation: charts. https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/

**Note:** Agrees with the source. The source does not say the charts must share scales; the example uses shared axes because the comparison depends on it.

### Dose-Response Relationship (`dose-response-relationship`)

Status: published. Model draft: no. Result: corrected.

**It said:** The pattern by which outcomes change with the amount or intensity of an intervention received, borrowed from pharmacology. Showing that more exposure produces more effect strengthens a causal claim and helps identify a minimum effective 'dose'. Use it when participants receive varying amounts of a program and you want to test whether intensity matters.

**Its example said:** A financial-literacy program in Maharashtra found a dose-response pattern: women who attended all six sessions saved substantially more than those who attended only one or two.

**It says now:** A dose-response relationship is a pattern in which the size of an effect changes with the amount of exposure. It is one of the considerations Austin Bradford Hill set out for judging whether an association is causal, under the name biological gradient: if a dose response is seen, the association is more likely to be causal. In evaluation, the 'dose' is the amount or intensity of a programme a participant received. Dose-response curves are often not straight lines, and the people who take up more of a programme may differ from those who take up less, so the pattern supports a causal claim and does not prove one.

**Its example now:** In a financial literacy programme, women who attended all six sessions saved more than those who attended one or two. Before reading that as a dose-response effect, the evaluator checks whether the women who attended every session were already better savers.

**Sources (all accessed 21 November 2026):**

- Fedak, K. M., Bernal, A., Capshaw, Z. A. and Gross, S., Applying the Bradford Hill criteria in the 21st century: how data integration has changed causal inference in molecular epidemiology, Emerging Themes in Epidemiology 12:14, section 'Criteria 5: biological gradient' (2015). https://pmc.ncbi.nlm.nih.gov/articles/PMC4589117/

**Note:** Agrees with the source. Added the origin of the idea in Hill's criteria and the caution that the curve need not be monotonic. The warning about self-selection into higher doses is my addition and is standard evaluation practice; the editor should confirm the wording. The old example cited a programme 'in Maharashtra' as if it were a real study; it is now presented as an illustration.

### Open Defecation Free (`open-defecation-free`)

Status: published. Model draft: no. Result: corrected.

**It said:** Open defecation free is a status certifying that no one in a defined area, such as a village, defecates in the open and that safe sanitation is universally used. It shifts the goal from counting toilets built to ensuring behaviour change and sustained use. Verification typically involves community declaration followed by third-party checks.

**Its example said:** Under Swachh Bharat Mission, thousands of Indian gram panchayats were declared open defecation free, though later surveys highlighted the challenge of sustaining toilet use.

**It says now:** Open defecation free (ODF) is a status given to a village or other area. The Government of India defined it in June 2015 as 'the termination of faecal-oral transmission, defined by a) no visible faeces found in the environment/village; and b) every household as well as public/community institutions using safe technology option for disposal of faeces'. A safe technology option means no contamination of soil or water, excreta inaccessible to flies and animals, no handling of fresh excreta, and freedom from odour. The WHO and UNICEF Joint Monitoring Programme does not certify areas. It measures the share of the population practising open defecation, which it defines as the disposal of human faeces in fields, forests, bushes, open bodies of water, beaches and other open spaces, or with solid waste.

**Its example now:** A Gram Panchayat declares itself ODF after every household has a toilet and no faeces are visible in the village. A household survey a few years later may still find some residents defecating in the open, because the declaration records a moment and the survey measures practice.

**Sources (all accessed 21 November 2026):**

- Ministry of Drinking Water and Sanitation, Government of India, Swachh Bharat Mission (Gramin), letter No. S-11011/3/2015-SBM, Definition of Open Defecation Free, 9 June 2015. https://archive.ids.ac.uk/clts/sites/communityledtotalsanitation.org/files/ODF_Definition_Government_of_India.pdf
- WHO/UNICEF Joint Monitoring Programme for Water Supply, Sanitation and Hygiene, Sanitation: the sanitation ladder. https://washdata.org/monitoring/sanitation

**Note:** Corrected. The old entry gave a general description and said verification 'typically involves community declaration followed by third-party checks', without a source. The entry now quotes the Government of India's 2015 definition and sets it beside the JMP's measure of practice. The old example's statement about later surveys had no source and is reworded as a general caution.

**Sources disagree:** The Government of India defines ODF as an area status with two conditions (no visible faeces; every household and institution using a safe technology option). The WHO/UNICEF JMP measures the share of people practising open defecation from household surveys. The two can give different pictures of the same place.

### Water, Sanitation and Hygiene (`water-sanitation-and-hygiene`)

Status: published. Model draft: no. Result: corrected.

**It said:** WASH is the collective term for the interlinked sectors of safe drinking water, adequate sanitation, and hygiene practices such as handwashing. Because these determinants of health work together, they are programmed as a bundle rather than in isolation. Weak WASH is a leading driver of diarrhoeal disease, stunting, and lost school days.

**Its example said:** India's Swachh Bharat Mission and Jal Jeevan Mission together target the WASH agenda by building toilets and delivering piped water to rural households.

**It says now:** WASH stands for water, sanitation and hygiene: safe drinking water, sanitation that separates excreta from human contact, and hygiene practices such as handwashing. The World Health Organization treats them together because unsafe water and untreated excreta spread the same diseases, above all diarrhoea, and because safe WASH also supports school attendance, livelihoods and dignity. The WHO and UNICEF Joint Monitoring Programme tracks each on a service ladder, which for sanitation runs from open defecation through unimproved, limited and basic to safely managed services.

**Its example now:** A district plan that builds toilets, extends piped water and runs a handwashing campaign in schools is a WASH plan. Progress is reported as the share of households at each step of the service ladder.

**Sources (all accessed 21 November 2026):**

- World Health Organization, Water, sanitation and hygiene (WASH), health topic overview. https://www.who.int/health-topics/water-sanitation-and-hygiene-wash
- WHO/UNICEF Joint Monitoring Programme for Water Supply, Sanitation and Hygiene, Sanitation: the sanitation ladder. https://washdata.org/monitoring/sanitation

**Note:** Corrected. The old entry called weak WASH 'a leading driver of diarrhoeal disease, stunting, and lost school days'. The WHO page supports the link to diarrhoeal disease and to school attendance and does not mention stunting, so stunting is removed. Added the JMP service ladder.

### Sphere Standards (`sphere-standards`)

Status: published. Model draft: no. Result: corrected.

**It said:** The Sphere Standards are a set of internationally recognised minimum standards for quality and accountability in humanitarian response, covering water and sanitation, food security, shelter, and health. Grounded in a humanitarian charter and rights-based principles, they define what disaster-affected people are entitled to. Aid agencies use them as a common benchmark during emergencies.

**Its example said:** Relief agencies responding to floods in Assam reference Sphere Standards to ensure each displaced person in a camp receives a minimum quantity of safe drinking water per day.

**It says now:** The Sphere standards are minimum standards for humanitarian response, set out in the Sphere Handbook. The Handbook consists of the Humanitarian Charter, the Protection Principles, the Core Humanitarian Standard, and minimum standards in four areas: water supply, sanitation and hygiene promotion; food security and nutrition; shelter and settlement; and health. Sphere describes it as one of the most widely known and internationally recognised tools for delivering a quality humanitarian response. The edition offered on Sphere's site is the 2018 Handbook.

**Its example now:** Agencies running a relief camp after a flood check their water supply, toilets and shelter space against the Sphere minimum standards and report where they fall short.

**Sources (all accessed 21 November 2026):**

- Sphere, The Sphere Handbook (handbook overview page; current edition 2018). https://spherestandards.org/handbook/

**Note:** Agrees with the source. The contents of the Handbook are now listed as Sphere lists them. The old example named floods in Assam and a per-person water quantity; the example is now generic because no figure was checked.

### Results-Based Financing (`results-based-financing`)

Status: published. Model draft: no. Result: agrees with the source; source added.

**It said:** A financing approach that ties the release of funds to the achievement of verified outputs or outcomes rather than to inputs or activities. By paying for measured results, it shifts performance risk to providers and sharpens incentives to deliver, but it requires credible, low-cost verification and careful outcome definition to avoid gaming. It is used in health, education, and increasingly in development bonds.

**Its example said:** A maternal-health programme might pay a facility a fixed amount per verified institutional delivery, rather than reimbursing staff salaries regardless of how many mothers are served.

**It says now:** Results-based financing (RBF) is, in the World Bank Group's definition, an umbrella term for any programme or intervention that provides rewards upon the credible, independent verification of an achieved result. The rewards can be monetary or non-monetary and can be part or all of the payment. A result is any element of the results chain beyond inputs: an output, an intermediate outcome or a final outcome. RBF moves some of the risk of non-delivery to the implementer and depends on verification that is credible and affordable.

**Its example now:** A maternal health programme pays a clinic a fixed amount for each institutional delivery that an independent verifier confirms, in place of reimbursing salaries whatever the number of mothers served.

**Sources (all accessed 21 November 2026):**

- World Bank Group, Results-Based Financing in Education: Financing Results to Strengthen Systems, section 'Operating Definitions of RBF'. https://documents1.worldbank.org/curated/en/715791489054110215/pdf/113265-REVISED-RBF-Approach-Final-Digital-Apr21.pdf

**Note:** Agrees with the source. The definition now uses the World Bank Group's wording, which requires independent verification. The document carries no clear publication year in the text I read, so none is given.

### MEAL (`meal`)

Status: published. Model draft: groq. Result: corrected.

**It said:** MEAL stands for Monitoring, Evaluation, Accountability, and Learning. It is a framework used by practitioners to ensure that programs are effective, accountable, and responsive to the needs of participants. Practitioners use MEAL when they need to assess the impact of their programs, identify areas for improvement, and make data-driven decisions to optimize their interventions.

**Its example said:** The Indian government's Antyodaya Anna Yojana (AAY) scheme uses MEAL frameworks to monitor and evaluate the effectiveness of its food distribution programs, ensuring accountability to its participants.

**It says now:** MEAL stands for monitoring, evaluation, accountability and learning. The MEAL DPro Guide, a sector standard developed with Catholic Relief Services, the Humanitarian Leadership Academy and Humentum, defines the four parts. Monitoring is the continuous and systematic collection and analysis of data about project progress and changes in the project context. Evaluation is the user-focused assessment of an ongoing or completed project's design, implementation and results. Accountability is a commitment to respond to and balance the needs of all project stakeholders, including the people the project serves. Learning means building in regular reflection, so that data and questions lead to better project decisions.

**Its example now:** An NGO's MEAL plan for a livelihoods project lists the indicators it will track each month, the evaluation it will commission at the end, the complaints line through which participants can raise problems, and the quarterly meetings at which the team reviews all three.

**Sources (all accessed 21 November 2026):**

- PM4NGOs, MEAL DPro Guide: Monitoring, Evaluation, Accountability and Learning for Development Professionals (guide first published 2019). https://pm4ngos.org/methodologies-guides/meal-dpro/

**Note:** Corrected. The old example said the Government of India's Antyodaya Anna Yojana 'uses MEAL frameworks'. No source supports that, and MEAL is an NGO sector term. The example is replaced and the four parts are now defined from the guide.

### MEL (`mel`)

Status: published. Model draft: groq. Result: corrected.

**It said:** MEL refers to the systematic collection and analysis of data to track progress, assess impact, and generate insights for program improvement. Practitioners use MEL to inform decision-making, identify areas for improvement, and demonstrate accountability to funders and participants, particularly in complex programs like NREGA or ASHA where data-driven insights can enhance service delivery.

**Its example said:** The Janani Suraksha Yojana program's MEL system tracks maternal healthcare outcomes and conducts regular reviews to improve service quality.

**It says now:** MEL stands for monitoring, evaluation and learning. The OECD defines monitoring as a continuing process of systematic collection or collation of data that shows managers and stakeholders how implementation is progressing and whether intended results are being achieved. It defines evaluation as the systematic and objective assessment of a planned, ongoing or completed intervention, its design, implementation and results. Learning is the use of both to change what the programme does. The term MEAL adds accountability, and MLE places learning before evaluation.

**Its example now:** A maternal health programme's MEL system records each month how many women received antenatal check-ups, commissions an evaluation after three years, and holds review meetings where staff decide what to change.

**Sources (all accessed 21 November 2026):**

- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Monitoring', p. 44 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf
- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Evaluation', p. 31 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf

**Note:** Corrected. The old entry did not say what the letters stand for and its example said the Janani Suraksha Yojana has a 'MEL system', which no source supports. The entry now expands the acronym and uses the OECD definitions of monitoring and evaluation.

### MLE (`mle`)

Status: seed. Model draft: no. Result: corrected.

**It said:** Monitoring, Learning & Evaluation—sequence emphasizes that learning should be continuous throughout implementation, not just post-evaluation.

**Its example said:** The Hewlett Foundation uses MLE to emphasize real-time learning alongside traditional monitoring.

**It says now:** MLE stands for monitoring, learning and evaluation. It names the same three activities as MEL and places learning second, to signal that learning should happen throughout implementation and should not wait for an evaluation at the end. The OECD defines monitoring as a continuing process of systematic data collection on progress and results, and evaluation as the systematic and objective assessment of an intervention's design, implementation and results.

**Its example now:** A team that reviews its monitoring data every quarter and changes its activities in response is practising the learning that the order of the letters in MLE is meant to stress.

**Sources (all accessed 21 November 2026):**

- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Monitoring', p. 44 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf
- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Evaluation', p. 31 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf

**Note:** Corrected. The old example said the Hewlett Foundation uses the term MLE to stress real-time learning. I could not confirm that from a Hewlett document, so it is removed. The source defines monitoring and evaluation; no standard-setting body's definition of 'MLE' as a term was found.

### Doorstep Delivery (`doorstep-delivery`)

Status: published. Model draft: groq. Result: corrected.

**It said:** Doorstep delivery refers to a public distribution system reform where essential commodities, such as grains, are delivered directly to villages or households, rather than requiring residents to travel to a Fair Price Shop. Practitioners use this term when discussing ways to improve the efficiency and accessibility of social welfare programs, such as the Public Distribution System, by reducing the need for participants to travel long distances to access essential goods.

**Its example said:** The Indian government's Antyodaya Anna Yojana scheme has implemented doorstep delivery in some states to improve access to subsidized grains for low-income households.

**It says now:** Doorstep delivery, in the National Food Security Act, 2013, is one of the reforms of the Targeted Public Distribution System listed in section 12: 'doorstep delivery of foodgrains to the Targeted Public Distribution System outlets'. It means that the grain is carried from the godown to the door of the fair price shop by the government and not by the dealer. The term is also used for schemes in which rations are delivered to the homes of beneficiaries. That is a different arrangement and is not what section 12 describes.

**Its example now:** Under doorstep delivery, a state agency's truck brings the month's rice and wheat to each fair price shop and records the quantity unloaded, so the dealer cannot claim that less was received.

**Sources (all accessed 21 November 2026):**

- Government of India, The National Food Security Act, 2013 (Act No. 20 of 2013), section 12(2), text as reproduced by Indian Kanoon. https://indiankanoon.org/doc/193125601/
- Department of Food and Public Distribution, National Food Security Act (NFSA), 2013, NFSA portal. https://nfsa.gov.in/portal/nfsa-act

**Note:** Corrected. The old entry defined doorstep delivery as delivery 'directly to villages or households' and said Antyodaya Anna Yojana had implemented it in some states. In the Act the term means delivery to the fair price shop. The entry now gives the statutory meaning first. Home delivery of rations is mentioned as a separate usage; no source on any state's home delivery scheme was opened. The Act's text was read on Indian Kanoon, which notes that it could not verify its copy against the original publication; the wording of section 12(2)(a) matches the description on the Department's NFSA portal.

### Diversion/Leakage (`diversionleakage`)

Status: published. Model draft: groq. Result: corrected.

**It said:** Diversion or leakage refers to the loss of resources, such as food grains, between procurement and delivery to intended recipients. Practitioners use this term when assessing the effectiveness of social welfare programs, like the Public Distribution System (PDS), to identify areas where resources are being misallocated or stolen, and to develop strategies to reduce these losses.

**Its example said:** In India, the Antyodaya Anna Yojana (AAY) has implemented measures to reduce diversion of PDS grains, resulting in significant declines in leakage rates.

**It says now:** Diversion, also called leakage, is the loss of subsidised goods between the point where the government releases them and the people entitled to them, for example foodgrains that leave the godown and never reach ration card holders. The National Food Security Act, 2013, names the prevention of diversion as a purpose of computerising the Targeted Public Distribution System from end to end. Estimates of leakage depend on the method used, and usually compare the grain released by the government with the grain households report receiving in surveys.

**Its example now:** If a state lifts 100 tonnes of rice for its ration shops in a month and household surveys imply that 80 tonnes reached card holders, the estimated leakage is 20 per cent.

**Sources (all accessed 21 November 2026):**

- Government of India, The National Food Security Act, 2013 (Act No. 20 of 2013), section 12(2), text as reproduced by Indian Kanoon. https://indiankanoon.org/doc/193125601/
- Department of Food and Public Distribution, National Food Security Act (NFSA), 2013, NFSA portal. https://nfsa.gov.in/portal/nfsa-act

**Note:** Corrected. The old example said Antyodaya Anna Yojana 'has implemented measures to reduce diversion of PDS grains, resulting in significant declines in leakage rates'. No source supports that claim, so it is replaced by an arithmetic illustration. The Act is cited for the term; the description of how leakage is estimated is my summary and is not from the Act.

### Lie Factor (`lie-factor`)

Status: published. Model draft: groq. Result: corrected.

**It said:** The Lie Factor is a measure of the distortion in the representation of data in a graphic. It is the ratio of the size of an effect shown in a graphic to the size of the effect in the data. Practitioners use the Lie Factor to evaluate the accuracy of visual representations of data, particularly in reports and presentations, to ensure that the data is not being misrepresented or exaggerated. A Lie Factor of 1 is accurate, while values above 1 indicate exaggeration and values below 1 indicate understatement.

**Its example said:** If the National Rural Employment Guarantee Act (NREGA) reports a 20% increase in employment, but the graphic shows a 50% increase, the Lie Factor is 2.5, indicating a significant distortion.

**It says now:** The lie factor is Edward Tufte's measure of how far a graphic distorts the data. It is the size of the effect shown in the graphic divided by the size of the effect in the data. A lie factor of 1 means the graphic represents the change accurately. A value above 1 means the graphic overstates the change, and a value below 1 means it understates it.

**Its example now:** The data show a 20 per cent rise, and the bars in the chart differ in height by 50 per cent because the axis does not start at zero. The lie factor is 50 divided by 20, which is 2.5.

**Sources (all accessed 21 November 2026):**

- Stasko, J., Tufte's Design Principles, lecture notes for CS 7450 Information Visualization, Georgia Institute of Technology (2012), reproducing E. R. Tufte, The Visual Display of Quantitative Information. https://faculty.cc.gatech.edu/~stasko/7450/12/Notes/tufte.pdf

**Note:** Agrees with the source, including the formula (lie factor = size of effect shown in graphic / size of effect in data). Tufte's book could not be opened, so the citation is to university lecture notes that reproduce it. The old example attributed an invented figure to the rural employment guarantee; the example now uses neutral numbers.

### Graphical Integrity (`graphical-integrity`)

Status: published. Model draft: groq. Result: corrected.

**It said:** Graphical integrity refers to the principle that visual representation should accurately reflect the underlying data without distortion or deception. A practitioner would use this term when creating data visualizations for reports or proposals to ensure that their charts and graphs honestly represent the data, avoiding misleading representations that could misinform decision-makers or the public.

**Its example said:** The National Sample Survey Office (NSSO) maintains graphical integrity in its reports by using clear and consistent visualizations, such as using zero baselines for bar charts, to accurately represent data on poverty rates in India.

**It says now:** Graphical integrity is Edward Tufte's principle that a graphic should tell the truth about the data. The visual size of what is drawn should be in direct proportion to the numbers it represents, scales and baselines should be shown, and the data should be shown in context. The lie factor is his measure of how far a graphic departs from this.

**Its example now:** A bar chart of school enrolment starts its vertical axis at zero, so that a bar twice as tall stands for twice as many pupils.

**Sources (all accessed 21 November 2026):**

- Stasko, J., Tufte's Design Principles, lecture notes for CS 7450 Information Visualization, Georgia Institute of Technology (2012), reproducing E. R. Tufte, The Visual Display of Quantitative Information. https://faculty.cc.gatech.edu/~stasko/7450/12/Notes/tufte.pdf

**Note:** Corrected. The old example said the National Sample Survey Office 'maintains graphical integrity in its reports by using clear and consistent visualizations'. No source supports that statement about NSSO, so it is replaced. Tufte's book could not be opened; the citation is to lecture notes that summarise it.

### Pilot (`pilot`)

Status: seed. Model draft: no. Result: agrees with the source; source added.

**It said:** A small-scale test of an intervention or technology before full rollout. Allows learning and iteration.

**Its example said:** Testing the AI targeting system in 5 villages before scaling to 500.

**It says now:** A pilot is a small-scale trial of an intervention, a tool or a survey before it is used in full, carried out to learn what needs to change. In survey practice a pilot survey is a survey, usually on a small scale, carried out before the main survey, mainly to gain information that will make the main survey more efficient, for example by testing the questionnaire or finding out how long fieldwork takes.

**Its example now:** A team tests a new targeting tool in five villages, finds that two questions are misunderstood, and rewrites them before using the tool in five hundred.

**Sources (all accessed 21 November 2026):**

- OECD, OECD Glossary of Statistical Terms, entry 'Pilot survey' (2008). https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/09/oecd-glossary-of-statistical-terms_g1gh9ad7/9789264055087-en.pdf

**Note:** Agrees with the source for surveys. The source defines 'pilot survey'; no standard-setting body's definition of a pilot of an intervention was opened, and the first sentence generalises from the survey definition.

### Absolute Poverty (`absolute-poverty`)

Status: published. Model draft: gemini. Result: corrected.

**It said:** Absolute poverty describes a condition where individuals lack the minimum income to meet basic needs like food, shelter, and healthcare, typically measured against a fixed monetary poverty line. Practitioners use this concept to identify the most vulnerable populations for targeted interventions, such as food security programmes or direct cash transfers. While useful for broad comparisons and tracking progress, relying solely on an income-based absolute line can overlook other dimensions of deprivation, like access to education or sanitation, which matter a great deal in South Asia. It's often contrasted with relative poverty.

**Its example said:** India's Antyodaya Anna Yojana (AAY) targets households identified as 'poorest of the poor' for subsidised food grains, aiming to address absolute poverty by ensuring basic nutritional needs are met for those furthest below the poverty line.

**It says now:** Absolute poverty is poverty measured against a fixed standard of living, set as a poverty line in money terms, which does not move when average incomes change. Different bodies set the line differently. The World Bank's international poverty line identifies people in absolute monetary poverty by the standards of the world's poorest countries. Since June 2025 it has been $3.00 per person per day at 2021 purchasing power parity, replacing $2.15 at 2017 parity, and the Bank also reports lines of $4.20 and $8.30 for lower-middle-income and upper-middle-income countries. India's official national lines for 2011-12, on the Tendulkar method, were Rs. 816 per person per month in rural areas and Rs. 1,000 in urban areas for 2011-12. A money line leaves out deprivations such as poor schooling and sanitation, which multidimensional measures add. It is contrasted with relative poverty.

**Its example now:** A rural household of five spending Rs. 3,500 a month in 2011-12 was below the Tendulkar line of Rs. 4,080 for a family of that size and was counted as poor, whatever its neighbours spent.

**Sources (all accessed 21 November 2026):**

- World Bank, June 2025 Update to Global Poverty Lines, factsheet (2025). https://www.worldbank.org/en/news/factsheet/2025/06/05/june-2025-update-to-global-poverty-lines
- Planning Commission, Government of India, Poverty Estimates for 2011-12, press note of 23 July 2013, Press Information Bureau. https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=97365

**Note:** Corrected and re-sourced. The entry was checked on 2026-10-14 against Encyclopaedia Britannica and gave no line. It now cites the World Bank and the Planning Commission and states the lines each uses. The entry is model-drafted (gemini) and that marker is unchanged.

**Sources disagree:** The World Bank's international line ($3.00 a day, 2021 PPP, from June 2025) and India's national Tendulkar lines (Rs. 816 rural and Rs. 1,000 urban per person per month, 2011-12) are set by different methods and give different counts of the poor. The Rangarajan committee's higher lines (2014) were not opened and are not cited.

### Impact (`impact`)

Status: published. Model draft: groq. Result: corrected.

**It said:** Impact refers to the significant positive or negative, intended or unintended, higher-level effects of an intervention. Practitioners use this term when evaluating the outcomes of a project or program, such as the Janani Suraksha Yojana, to understand its broader influence on the community, beyond its immediate objectives.

**Its example said:** A livelihoods programme's outputs are trainings held and loans given, and its outcomes are new enterprises started. Its impact would be lasting changes in household income and in women's say in household decisions, including any unintended effects such as children leaving school to help in the new enterprise.

**It says now:** Impact has two meanings in evaluation, and it helps to say which one is meant. In the OECD's evaluation criteria, impact is the extent to which an intervention has generated or is expected to generate significant positive or negative, intended or unintended, higher-level effects: its longer-term and broader social, environmental and economic consequences. In impact evaluation, impact means the causal effect of the intervention, estimated as the difference between what happened and the counterfactual, which the OECD defines as the situation that would hypothetically prevail were there no intervention. A result can be an impact in the second sense, such as a rise in test scores caused by a tutoring programme, without being a higher-level effect in the first.

**Its example now:** An evaluation of a maternity benefit scheme reports that it raised the share of births in health facilities, which is its impact in the causal sense. Whether maternal deaths fell as a result is a question about impact in the higher-level sense.

**Sources (all accessed 21 November 2026):**

- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Impact', p. 36 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf
- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Impact evaluation', p. 37 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf
- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Counterfactual', p. 25 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf

**Note:** Corrected. The entry, checked on 2026-10-14, gave only the OECD criterion sense. The same glossary uses a causal, counterfactual sense under 'Impact evaluation', and the entry now sets out both. The source link now points to the OECD's own copy of the glossary, with page numbers. The old example named the Janani Suraksha Yojana; the example is now unnamed.

**Sources disagree:** OECD DAC criterion sense (higher-level, longer-term effects) versus the counterfactual sense used in impact evaluation (any causal effect of the intervention). Both appear in the OECD glossary itself.

### Accountability Mechanism (`accountability-mechanism`)

Status: published. Model draft: groq. Result: corrected.

**It said:** An accountability mechanism is an institutional feature that enables citizens to hold officials responsible for their actions. Practitioners use accountability mechanisms, such as social audits and grievance redressal, to ensure transparency and responsiveness in government programs, particularly in schemes like NREGA and Janani Suraksha Yojana, where citizen participation is crucial.

**Its example said:** The Right to Information (RTI) Act in India is an example of an accountability mechanism, allowing citizens to demand information from public authorities.

**It says now:** An accountability mechanism is an arrangement through which one party can be held responsible to another for what it has done. The OECD defines accountability as a state of or a process for holding someone responsible to someone else for something, and for public managers as being answerable to taxpayers, civil society and communities for what was done, why and how, including the costs and any negative results. In government programmes the mechanisms include audits, public disclosure of records, grievance redress and social audits. The OECD distinguishes community, bottom-up, horizontal and top-down accountability.

**Its example now:** A Gram Sabha reads out the list of works and payments under a rural employment programme and villagers point out a road that was paid for and never built. The public reading is the accountability mechanism.

**Sources (all accessed 21 November 2026):**

- OECD, Glossary of Key Terms in Evaluation and Results-Based Management for Sustainable Development, 2nd ed., entry 'Accountability', p. 16 (2023). https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/glossary-of-key-terms-in-evaluation-and-results-based-management-for-sustainable-development-second-edition_2767e14e/632da462-en-fr-es.pdf

**Note:** Agrees with the source in substance. The old entry limited the term to citizens holding officials responsible; the OECD definition is wider and the entry now follows it. The old example about the Right to Information Act is replaced by a social audit illustration.

## Examined, no source that could be opened

These entries are unchanged. A source was looked for and either could not be opened or did not define the term.

- **Credit Constraints** (`credit-constraints`, published): No definition found in the sources opened.
- **Export-Oriented Industrialization** (`export-oriented-industrialization`, published): OpenStax lists 'export-led industrialization' only in connection with the East Asian Tigers and does not define it.
- **Group Lending** (`group-lending`, published): Ghatak and Guinnane (1999) has no abstract in Crossref; the J-PAL microcredit page does not define the term.
- **Implementation Failure** (`implementation-failure`, published): Same as theory failure.
- **Incremental Budgeting** (`incremental-budgeting`, published): The GFOA paper on zero-base budgeting does not define incremental budgeting on the page read. The example presents the rural employment guarantee budget as incremental budgeting, which has no source and is doubtful, because the scheme was demand-driven by law.
- **Institutional Isomorphism** (`institutional-isomorphism`, published): DiMaggio and Powell (1983), American Sociological Review. The Crossref record has no abstract and JSTOR was not opened. The example about NREGA project implementation units has no source.
- **Jan Sunwai** (`jan-sunwai`, published): mkssindia.org failed its TLS certificate check. Not opened. The example says MKSS used Jan Sunwai to verify muster rolls 'under NREGA'; MKSS's public hearings are usually dated to the 1990s, before the 2005 Act, so the example needs checking.
- **Learning Agenda** (`learning-agenda`, published): evaluation.gov failed its TLS certificate check. Not opened.
- **Log Scale** (`log-scale`, published): No authoritative source opened. The example says National Health Mission data on Janani Suraksha Yojana 'is often plotted on a log scale', which has no source.
- **Mahalanobis Model** (`mahalanobis-model`, published): The Second Five Year Plan was found only as a scan whose text layer is unreadable. Mahalanobis's 1955 paper was not opened.
- **MKSS** (`mkss`, published): mkssindia.org failed its TLS certificate check. Not opened.
- **Option Value** (`option-value`, seed): Weisbrod (1964), Quarterly Journal of Economics, is the origin. SSRN and the publisher blocked the request. The entry's claim about NREGA and non-participants has no source.
- **Pause-and-Reflect** (`pause-and-reflect`, seed): USAID Learning Lab returned HTTP 502.
- **Policy Cycle** (`policy-cycle`, seed): Jann and Wegrich, Theories of the Policy Cycle (2007), was blocked on ResearchGate. Not opened.
- **Political Economy** (`political-economy`, seed): DFID's Political Economy Analysis How To Note (2009) returned 404 at GSDRC. Not opened.
- **Political Economy of Reform** (`political-economy-of-reform`, seed): No source opened. The example makes claims about the 2020 farm laws that need a source.
- **Sankey Diagram** (`sankey-diagram`, seed): The UK Government Analysis Function guidance lists Sankey charts for flows and does not define them.
- **Slope Chart** (`slope-chart`, seed): The UK Government Analysis Function guidance lists slope charts for rankings and does not define them.
- **SPICED** (`spiced`, seed): Chris Roche, Impact Assessment for Development Agencies (Oxfam, 1999) is the usual origin. Oxfam's repository refused the request (HTTP 403). Not opened.
- **Theory Failure** (`theory-failure`, seed): Only training slides (UNDP NEC, 2019) were found that name the distinction, and they do not define it. Suchman (1967) and Weiss could not be opened.
- **USAID ADS** (`usaid-ads`, seed): usaid.gov returned HTTP 403 and the State Department page returned 405. The entry describes ADS 201 in the present tense. Whether USAID's directives are still in force needs an editor's decision and a source; I did not change the entry.
- **Ecological Fallacy** (`ecological-fallacy`, published): Robinson (1950, reprinted 2009 in the International Journal of Epidemiology) was blocked (403). The Catalogue of Bias page returned 404.
- **Do No Harm** (`do-no-harm`, published): Sphere's overview page was read; the Protection Principles themselves were not, so no source is added.

## Not reached

37 entries with no source were not examined in this pass. They are unchanged.

- seed (10): Narrative Arc (`narrative-arc`), Object Detection (`object-detection`), Observable (`observable`), Scalability (`scalability`), Scrollytelling (`scrollytelling`), Tableau (`tableau`), Violin Plot (`violin-plot`), Visual Hierarchy (`visual-hierarchy`), Waffle Chart (`waffle-chart`), White Space (`white-space`)
- published (27): Accountability-Learning Tension (`accountability-learning-tension`), Asset Depletion (`asset-depletion`), Bump Chart (`bump-chart`), Call to Action (`call-to-action`), Change Blindness (`change-blindness`), Chart Title (`chart-title`), Citizen-State Interface (`citizen-state-interface`), Code-Switching (`code-switching`), Convergence Failure (`convergence-failure`), Data Lake (`data-lake`), Data Pipeline (`data-pipeline`), DME (`dme`), Economic Development (`economic-development`), ETL (Extract, Transform, Load) (`etl`), Exploratory vs. Explanatory (`exploratory-vs-explanatory`), Import Substitution Industrialization (ISI) (`import-substitution-industrialization`), Indicator Proliferation (`indicator-proliferation`), Information Density (`information-density`), Insurance Function (`insurance-function`), Justiciable Entitlement (`justiciable-entitlement`), Key Informant Interview (`key-informant-interview`), Lifecycle Risk (`lifecycle-risk`), Missing Middle (`missing-middle`), Mission Mode Governance (`mission-mode-governance`), Last-Mile Delivery (`last-mile-delivery`), Agency versus Structure (`agency-versus-structure`), Dashboard Fatigue (`dashboard-fatigue`)

The 346 entries checked on 14 October 2026 and not touched here were not re-examined. Three of them still cite Encyclopaedia Britannica and could be moved to a primary source.

## Things the editor should know

- Several model-drafted entries that were not reached attach invented facts to real schemes in their examples (for example that a named scheme 'uses' a framework). Those seen while listing terms: `dme`, `learning-agenda`, `institutional-isomorphism`, `incremental-budgeting`, `import-substitution-industrialization` (credits NITI Aayog, created in 2015, with post-independence policy), `economic-development`, `key-informant-interview`, `log-scale`, `credit-constraints`, `jan-sunwai`, `mkss`. They were not changed because no source was opened for them.
- Two abstracts (Tsebelis 1995, Kabeer 1999) were read through the publisher's Crossref record, because the journal pages refuse automated requests. The entries cite the DOI.
- Three cited addresses answer 403 to a script and open in a browser: the Wiley DOI for Kabeer, spherestandards.org and the OECD page for Regulatory Impact Analysis. The last two were read through a browser-based fetch.
- The National Food Security Act was read on Indian Kanoon, whose page says it could not verify its copy against the original publication. India Code timed out. The section quoted matches the Department's NFSA portal.
- `impactlex/sw.js` precaches `reviewed.json` and serves it stale-while-revalidate, so a returning reader sees the new text on the second visit after deploy. I did not touch `sw.js`.
- `docs/changelog.md` was not edited. The release that carries this change should add a line for learners.
- `data/counts.json` and the term counts on the ImpactLex pages are unchanged: no term was added or removed.


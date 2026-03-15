/**
 * ImpactMojo Assessment Question Banks
 * Question data for flagship course assessments
 *
 * Question types:
 *   - "single"  : single-select multiple choice
 *   - "multi"   : multi-select (checkboxes)
 *   - "tf"      : true / false
 *
 * Each question has:
 *   id, type, question, options (array), correct (value or array), explanation
 */

const ASSESSMENT_DATA = {

    /* =====================================================
       MEL — Monitoring, Evaluation & Learning
       ===================================================== */
    mel: {
        title: "MEL Comprehensive Assessment",
        description: "Test your understanding of Monitoring, Evaluation & Learning concepts across all modules.",
        passingScore: 60,
        questions: [
            {
                id: "mel-1",
                type: "single",
                question: "Which component of a Theory of Change describes the long-term systemic change a programme aims to contribute to?",
                options: [
                    { value: "a", label: "Outputs" },
                    { value: "b", label: "Outcomes" },
                    { value: "c", label: "Impact" },
                    { value: "d", label: "Activities" }
                ],
                correct: "c",
                explanation: "Impact refers to the long-term, systemic change that a programme ultimately aims to contribute to, beyond immediate outcomes."
            },
            {
                id: "mel-2",
                type: "tf",
                question: "A logical framework (logframe) and a Theory of Change are essentially the same tool and can be used interchangeably.",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ],
                correct: "false",
                explanation: "While both are planning tools, a Theory of Change maps the causal pathway of how change happens (including assumptions), whereas a logframe is a matrix summarising objectives, indicators, means of verification, and assumptions in a linear format."
            },
            {
                id: "mel-3",
                type: "single",
                question: "In USAID's Collaborating, Learning, and Adapting (CLA) framework, what does 'adaptive management' primarily refer to?",
                options: [
                    { value: "a", label: "Rigidly following the original project plan" },
                    { value: "b", label: "Using real-time evidence to adjust strategies during implementation" },
                    { value: "c", label: "Changing programme goals at the end of each fiscal year" },
                    { value: "d", label: "Delegating monitoring responsibilities to external evaluators" }
                ],
                correct: "b",
                explanation: "Adaptive management in the CLA framework means intentionally using evidence and learning from monitoring and evaluation to make informed adjustments to strategies during implementation."
            },
            {
                id: "mel-4",
                type: "multi",
                question: "Which of the following are characteristics of SMART indicators? (Select all that apply)",
                options: [
                    { value: "a", label: "Specific" },
                    { value: "b", label: "Measurable" },
                    { value: "c", label: "Subjective" },
                    { value: "d", label: "Time-bound" },
                    { value: "e", label: "Achievable" }
                ],
                correct: ["a", "b", "d", "e"],
                explanation: "SMART stands for Specific, Measurable, Achievable, Relevant, and Time-bound. 'Subjective' is not a SMART criterion — indicators should ideally be objective and verifiable."
            },
            {
                id: "mel-5",
                type: "single",
                question: "What is the primary purpose of a counterfactual in impact evaluation?",
                options: [
                    { value: "a", label: "To measure programme outputs" },
                    { value: "b", label: "To estimate what would have happened without the intervention" },
                    { value: "c", label: "To track budget expenditure" },
                    { value: "d", label: "To conduct stakeholder consultations" }
                ],
                correct: "b",
                explanation: "A counterfactual estimates what would have happened to the target population in the absence of the intervention, which is essential for attributing observed changes to the programme."
            },
            {
                id: "mel-6",
                type: "single",
                question: "Which evaluation design is considered the gold standard for establishing causal attribution?",
                options: [
                    { value: "a", label: "Pre-post comparison" },
                    { value: "b", label: "Most Significant Change" },
                    { value: "c", label: "Randomised Controlled Trial (RCT)" },
                    { value: "d", label: "Outcome Harvesting" }
                ],
                correct: "c",
                explanation: "RCTs randomly assign participants to treatment and control groups, providing the strongest basis for causal attribution by eliminating selection bias."
            },
            {
                id: "mel-7",
                type: "tf",
                question: "Qualitative data collection methods such as focus group discussions can generate findings that are generalisable to the entire target population.",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ],
                correct: "false",
                explanation: "Qualitative methods provide depth and context but typically use purposive (non-random) sampling, so findings cannot be statistically generalised to a wider population. They are complementary to quantitative methods."
            },
            {
                id: "mel-8",
                type: "single",
                question: "What does 'contribution analysis' help evaluators assess?",
                options: [
                    { value: "a", label: "The exact percentage of impact caused by each funder" },
                    { value: "b", label: "Whether and how an intervention contributed to observed outcomes, alongside other factors" },
                    { value: "c", label: "The cost-effectiveness ratio of an intervention" },
                    { value: "d", label: "The number of beneficiaries reached by a programme" }
                ],
                correct: "b",
                explanation: "Contribution analysis builds a credible causal story of how a programme contributed to observed outcomes, acknowledging that other factors may also have played a role — without claiming sole attribution."
            }
        ]
    },

    /* =====================================================
       DataViz — Data Visualization for Development
       ===================================================== */
    dataviz: {
        title: "Data Visualization Assessment",
        description: "Assess your knowledge of data visualization principles, chart selection, and storytelling with data.",
        passingScore: 60,
        questions: [
            {
                id: "dv-1",
                type: "single",
                question: "According to Edward Tufte's principles, what is the 'data-ink ratio'?",
                options: [
                    { value: "a", label: "The ratio of colour to white space in a chart" },
                    { value: "b", label: "The proportion of ink used to display actual data versus total ink used in the graphic" },
                    { value: "c", label: "The number of data points per chart" },
                    { value: "d", label: "The ratio of charts to text in a report" }
                ],
                correct: "b",
                explanation: "Tufte's data-ink ratio encourages maximising the share of ink (or pixels) devoted to presenting data itself, and minimising non-data ink like unnecessary gridlines, borders, and decorative elements."
            },
            {
                id: "dv-2",
                type: "single",
                question: "Which chart type is most appropriate for showing the composition of a whole (parts to whole) at a single point in time?",
                options: [
                    { value: "a", label: "Line chart" },
                    { value: "b", label: "Scatter plot" },
                    { value: "c", label: "Stacked bar chart or pie chart" },
                    { value: "d", label: "Histogram" }
                ],
                correct: "c",
                explanation: "Stacked bar charts and pie charts are designed to show how parts relate to a whole. Pie charts work well with few categories; stacked bars scale better with more categories."
            },
            {
                id: "dv-3",
                type: "tf",
                question: "Using 3D effects on bar charts improves readability and helps audiences compare values more accurately.",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ],
                correct: "false",
                explanation: "3D effects distort perception and make it harder to read exact values. Best practice is to use flat, 2D charts for accurate visual comparison."
            },
            {
                id: "dv-4",
                type: "multi",
                question: "Which of the following are pre-attentive visual attributes that the human brain processes almost instantly? (Select all that apply)",
                options: [
                    { value: "a", label: "Colour hue" },
                    { value: "b", label: "Font family" },
                    { value: "c", label: "Size / length" },
                    { value: "d", label: "Orientation" },
                    { value: "e", label: "Position" }
                ],
                correct: ["a", "c", "d", "e"],
                explanation: "Colour hue, size/length, orientation, and spatial position are pre-attentive attributes — processed by the visual system in under 250 milliseconds. Font family requires conscious reading and is not pre-attentive."
            },
            {
                id: "dv-5",
                type: "single",
                question: "When visualising data for a development report, why is it important to annotate key data points directly on the chart?",
                options: [
                    { value: "a", label: "It makes the chart look more professional" },
                    { value: "b", label: "It reduces cognitive load by eliminating the need to cross-reference legends" },
                    { value: "c", label: "It is required by all style guides" },
                    { value: "d", label: "It increases the data-ink ratio unnecessarily" }
                ],
                correct: "b",
                explanation: "Direct labelling and annotation reduce the viewer's cognitive load — they no longer need to look back and forth between the legend and the data, leading to faster and more accurate comprehension."
            },
            {
                id: "dv-6",
                type: "single",
                question: "What is the primary risk of using a dual-axis chart?",
                options: [
                    { value: "a", label: "It uses too much screen space" },
                    { value: "b", label: "Viewers may incorrectly assume a causal relationship between the two variables" },
                    { value: "c", label: "It cannot display more than two data series" },
                    { value: "d", label: "It is not supported by major charting libraries" }
                ],
                correct: "b",
                explanation: "Dual-axis charts are often misleading because the two scales can be manipulated to suggest correlation or causation. Viewers may draw incorrect conclusions about the relationship between the variables."
            },
            {
                id: "dv-7",
                type: "tf",
                question: "Colour-blind-safe palettes (e.g., using blue-orange instead of red-green) are only necessary when you know your audience includes colour-blind individuals.",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ],
                correct: "false",
                explanation: "Approximately 8% of men and 0.5% of women have some form of colour vision deficiency. Accessible colour palettes should be a default practice, not an exception, especially in public-facing development reports."
            },
            {
                id: "dv-8",
                type: "single",
                question: "In data storytelling, what does the 'inverted pyramid' structure recommend?",
                options: [
                    { value: "a", label: "Start with methodology, then show findings" },
                    { value: "b", label: "Lead with the most important insight, then provide supporting details" },
                    { value: "c", label: "Present data chronologically from oldest to newest" },
                    { value: "d", label: "Place all charts at the end of the document" }
                ],
                correct: "b",
                explanation: "Borrowed from journalism, the inverted pyramid leads with the key finding or message and follows with supporting evidence and context — ensuring busy decision-makers get the critical insight first."
            }
        ]
    },

    /* =====================================================
       DevAI — AI for Development & M&E
       ===================================================== */
    devai: {
        title: "AI for Development Assessment",
        description: "Evaluate your understanding of how AI and machine learning apply to development practice and M&E.",
        passingScore: 60,
        questions: [
            {
                id: "ai-1",
                type: "single",
                question: "What is a key advantage of using Natural Language Processing (NLP) for analysing qualitative M&E data?",
                options: [
                    { value: "a", label: "It eliminates the need for any human interpretation" },
                    { value: "b", label: "It can process large volumes of text data (e.g., survey open-ends, FGD transcripts) much faster than manual coding" },
                    { value: "c", label: "It always produces more accurate results than human coders" },
                    { value: "d", label: "It requires no training data or configuration" }
                ],
                correct: "b",
                explanation: "NLP can rapidly analyse large text corpora, identifying themes, sentiments, and patterns. However, it complements rather than replaces human interpretation, especially for nuanced cultural contexts."
            },
            {
                id: "ai-2",
                type: "tf",
                question: "AI models trained on data from high-income countries can be directly applied to low-income contexts without any risk of bias.",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ],
                correct: "false",
                explanation: "Models trained on data from specific contexts often carry biases reflecting those contexts. Applying them elsewhere without adaptation can produce inaccurate or harmful results — a key concern in development applications."
            },
            {
                id: "ai-3",
                type: "single",
                question: "In the context of development, what does 'algorithmic targeting' refer to?",
                options: [
                    { value: "a", label: "Using algorithms to target advertisements" },
                    { value: "b", label: "Using machine learning models to identify and prioritise beneficiaries for social programmes" },
                    { value: "c", label: "Targeting specific algorithms for removal from a system" },
                    { value: "d", label: "Setting performance targets for AI models" }
                ],
                correct: "b",
                explanation: "Algorithmic targeting uses predictive models (e.g., poverty prediction from satellite imagery or mobile data) to identify households or communities that should receive programme benefits."
            },
            {
                id: "ai-4",
                type: "multi",
                question: "Which of the following are ethical concerns when deploying AI in development contexts? (Select all that apply)",
                options: [
                    { value: "a", label: "Data privacy and informed consent" },
                    { value: "b", label: "Algorithmic bias and discrimination" },
                    { value: "c", label: "Faster processing speed" },
                    { value: "d", label: "Lack of transparency in model decisions" },
                    { value: "e", label: "Digital divide and unequal access" }
                ],
                correct: ["a", "b", "d", "e"],
                explanation: "Ethical concerns include privacy, bias, transparency (black-box models), and the digital divide. Faster processing speed is a benefit, not an ethical concern."
            },
            {
                id: "ai-5",
                type: "single",
                question: "How can satellite imagery combined with computer vision support development M&E?",
                options: [
                    { value: "a", label: "By replacing all field-based data collection" },
                    { value: "b", label: "By tracking changes in land use, infrastructure, or environmental conditions over time at scale" },
                    { value: "c", label: "By conducting household surveys remotely" },
                    { value: "d", label: "By generating qualitative narratives about communities" }
                ],
                correct: "b",
                explanation: "Satellite imagery with computer vision can monitor deforestation, urbanisation, crop health, and infrastructure development at scale — complementing traditional monitoring with objective, frequent, large-area data."
            },
            {
                id: "ai-6",
                type: "single",
                question: "What is a 'human-in-the-loop' approach to AI in M&E?",
                options: [
                    { value: "a", label: "Humans design the AI but never interact with it again" },
                    { value: "b", label: "Human judgement is integrated at key decision points in the AI workflow" },
                    { value: "c", label: "AI fully replaces human evaluators" },
                    { value: "d", label: "Humans are only involved in data entry" }
                ],
                correct: "b",
                explanation: "A human-in-the-loop approach ensures that human judgement, contextual knowledge, and ethical reasoning are integrated into AI-assisted processes — particularly important for high-stakes development decisions."
            },
            {
                id: "ai-7",
                type: "tf",
                question: "Real-time monitoring dashboards powered by AI can completely replace the need for periodic programme evaluations.",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ],
                correct: "false",
                explanation: "Real-time dashboards track outputs and immediate outcomes, but periodic evaluations are still needed to assess deeper impact, causality, sustainability, and unintended consequences — questions that dashboards alone cannot answer."
            },
            {
                id: "ai-8",
                type: "single",
                question: "When building an AI strategy for a development organisation, what should be the first step?",
                options: [
                    { value: "a", label: "Purchasing the most advanced AI tools available" },
                    { value: "b", label: "Conducting a needs assessment to identify where AI can add the most value" },
                    { value: "c", label: "Hiring a large team of data scientists" },
                    { value: "d", label: "Automating all existing manual processes immediately" }
                ],
                correct: "b",
                explanation: "A needs assessment identifies specific problems where AI can add value, evaluates data readiness, and ensures the organisation invests in solutions aligned with its mission and capacity."
            }
        ]
    }
};

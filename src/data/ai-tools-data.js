// src/data/ai-tools-data.js
export const aiToolsData = [
  {
    id: 'data-viz',
    title: 'Data Visualization Generator',
    description: 'Create clear, compelling data visualizations from your dataset with automatic chart selection, color schemes, and accessibility features.',
    prompt: `I need a data visualization that effectively communicates insights from my dataset.
Dataset Details:
- Type: [survey/time series/categorical/numerical]
- Size: [number of data points]
- Key Variables: [list main variables]
- Story to Tell: [what insight do you want to highlight]
Target Audience: [researchers/policymakers/community/general public]
Context: [report/presentation/website/social media]
Please provide:
1. Recommended chart type with justification
2. Complete code (R/Python/JavaScript) for creating the visualization
3. Color palette that's accessible and meaningful
4. Title, labels, and annotations
5. Alternative text description for accessibility
6. Tips for presenting this data effectively`,
    systemMessage: 'You are a data visualization expert who understands both the technical and storytelling aspects of data presentation. You prioritize clarity, accessibility, and impact in your designs.',
    exampleInput: `Type: Survey data on gender wage gaps
Size: 500 respondents across 5 industries
Variables: Gender, Industry, Years of Experience, Salary Range
Story: Show persistent wage gaps across all experience levels
Audience: Policy makers
Context: Policy brief on workplace equality`,
    icon: 'BarChart',
    color: 'blue'
  },
  {
    id: 'theory-change',
    title: 'Theory of Change Builder',
    description: 'Develop comprehensive Theory of Change frameworks with clear pathways from activities to impact.',
    prompt: `Help me develop a Theory of Change for my development program.
Program Overview:
- Problem Statement: [describe the problem]
- Target Population: [who are you serving]
- Geographic Context: [where]
- Timeframe: [program duration]
Current Activities: [list main activities/interventions]
Resources Available: [budget, staff, partners]
Desired Long-term Change: [ultimate goal]
Please create:
1. Complete Theory of Change narrative
2. Visual diagram showing:
   - Inputs → Activities → Outputs → Outcomes → Impact
3. Assumptions and risks at each level
4. Indicators for measuring progress
5. Feedback loops and adaptation points`,
    systemMessage: 'You are a strategic planning expert specializing in Theory of Change development for social impact programs. You understand complex causal pathways and can identify critical assumptions.',
    exampleInput: `Problem: High youth unemployment in rural areas
Target: Youth aged 18-25 in rural districts
Context: Southeast Asia
Timeframe: 3-year program
Activities: Skills training, mentorship, job placement support
Resources: $500K budget, 10 staff, 5 partner organizations
Goal: Sustainable employment for 1000 youth`,
    icon: 'Target',
    color: 'green'
  },
  {
    id: 'grant-proposal',
    title: 'Grant Proposal Writer',
    description: 'Craft compelling grant proposals with clear narratives, strong evidence, and aligned budgets.',
    prompt: `I need help writing a grant proposal for my development project.
Funder Details:
- Organization: [funder name]
- Priority Areas: [what they fund]
- Grant Size: [amount requesting]
- Requirements: [specific requirements/format]
Project Information:
- Title: [project name]
- Problem/Need: [what problem does this solve]
- Solution/Approach: [your approach]
- Target Beneficiaries: [who benefits]
- Timeline: [project duration]
- Expected Outcomes: [measurable results]
Organization Background:
- Track Record: [relevant experience]
- Capacity: [why you can deliver]
Please provide:
1. Executive summary (250 words)
2. Problem statement with evidence
3. Project description with methodology
4. Impact and sustainability plan
5. Budget narrative
6. Evaluation framework`,
    systemMessage: 'You are a grant writing expert who knows how to align project narratives with funder priorities while maintaining authenticity and impact focus.',
    exampleInput: `Funder: Global Education Foundation
Priorities: Girls' education, STEM, rural areas
Amount: $250,000
Project: Mobile STEM Labs for Rural Girls
Problem: Only 15% of rural girls pursue STEM
Solution: Mobile labs visiting 20 schools monthly
Beneficiaries: 2000 girls aged 12-16
Timeline: 2 years
Outcomes: 50% increase in STEM enrollment`,
    icon: 'FileText',
    color: 'purple'
  },
  {
    id: 'stakeholder-map',
    title: 'Stakeholder Mapping Tool',
    description: 'Create comprehensive stakeholder maps with power/interest analysis and engagement strategies.',
    prompt: `Help me create a stakeholder map for my development initiative.
Project Context:
- Initiative: [describe your project]
- Sector: [education/health/governance/etc]
- Geographic Scope: [local/national/regional]
- Phase: [planning/implementation/evaluation]
Known Stakeholders: [list key stakeholders you've identified]
Project Goals: [what you're trying to achieve]
Potential Challenges: [any conflicts or sensitivities]
Please provide:
1. Comprehensive stakeholder identification by category:
   - Primary (direct beneficiaries)
   - Secondary (indirect beneficiaries)
   - Key (decision makers/funders)
2. Power/Interest matrix placement
3. Influence/Impact assessment
4. Engagement strategy for each stakeholder group
5. Risk analysis and mitigation strategies
6. Communication plan outline`,
    systemMessage: 'You are a stakeholder engagement specialist who understands power dynamics, cultural contexts, and the importance of inclusive participation in development work.',
    exampleInput: `Initiative: Community health worker program
Sector: Public health
Scope: District-level in rural areas
Phase: Planning phase
Known Stakeholders: Ministry of Health, village councils, existing health workers
Goals: Reduce maternal mortality by 30%
Challenges: Resistance from traditional healers`,
    icon: 'Users',
    color: 'indigo'
  },
  {
    id: 'indicator-framework',
    title: 'M&E Indicator Designer',
    description: 'Design SMART indicators with clear measurement frameworks and data collection plans.',
    prompt: `I need help developing monitoring and evaluation indicators for my program.
Program Details:
- Objective: [main program objective]
- Activities: [key activities]
- Target Population: [who and how many]
- Duration: [timeframe]
- Budget for M&E: [available resources]
Current M&E Capacity:
- Staff Skills: [existing M&E expertise]
- Data Systems: [what systems are in place]
- Reporting Requirements: [donor/organizational needs]
Please create:
1. Results chain with clear logic
2. SMART indicators for each level:
   - Input indicators
   - Output indicators  
   - Outcome indicators
   - Impact indicators (if applicable)
3. Indicator reference sheets including:
   - Definition and calculation method
   - Data source and collection method
   - Frequency and responsible party
   - Baseline and targets
4. Data collection tools outline
5. Data quality assurance plan`,
    systemMessage: 'You are an M&E expert who designs practical, measurable indicators that balance rigor with feasibility, ensuring they provide actionable insights for program improvement.',
    exampleInput: `Objective: Improve girls' literacy in rural schools
Activities: Teacher training, reading clubs, library setup
Target: 5000 girls in 50 schools
Duration: 3 years
M&E Budget: $50,000
Staff: 1 M&E officer, program staff can support
Systems: Basic Excel tracking
Reporting: Quarterly to donor, annual evaluation`,
    icon: 'CheckCircle',
    color: 'teal'
  },
  {
    id: 'policy-brief',
    title: 'Policy Brief Creator',
    description: 'Transform research into actionable policy briefs with clear recommendations.',
    prompt: `Help me create a policy brief from my research/program findings.
Research/Evidence Base:
- Topic: [issue area]
- Key Findings: [main findings/data]
- Methodology: [how evidence was gathered]
- Context: [country/region specific factors]
Policy Landscape:
- Current Policies: [existing relevant policies]
- Policy Gaps: [what's missing]
- Decision Makers: [target audience]
- Political Context: [opportunities/constraints]
Desired Change: [what policy change you're advocating for]
Please provide:
1. Executive Summary (1 paragraph)
2. Problem Statement with evidence
3. Policy Options Analysis (2-3 options with pros/cons)
4. Recommendations (specific and actionable)
5. Implementation Roadmap
6. Cost-Benefit Analysis (if applicable)
7. Visual elements suggestions (infographics/charts)`,
    systemMessage: 'You are a policy communication expert who can distill complex research into clear, persuasive policy recommendations that resonate with decision-makers.',
    exampleInput: `Topic: School dropout rates among adolescent girls
Key Findings: 40% dropout rate, mainly due to early marriage
Methodology: Survey of 1000 households, 20 focus groups
Context: Rural Bangladesh
Current Policies: Compulsory education until age 14
Gaps: No enforcement, no support for at-risk girls
Decision Makers: Ministry of Education, local officials
Desired Change: Conditional cash transfer program for girls' education`,
    icon: 'Scale',
    color: 'amber'
  },
  {
    id: 'interview-guide',
    title: 'Interview Guide Generator',
    description: 'Create structured interview guides for qualitative research with cultural sensitivity.',
    prompt: `I need an interview guide for my qualitative research.
Research Context:
- Research Question: [main question you're exploring]
- Participant Profile: [who you're interviewing]
- Cultural Context: [relevant cultural considerations]
- Language: [interview language/translation needs]
- Setting: [where interviews will happen]
Interview Details:
- Type: [structured/semi-structured/unstructured]
- Duration: [expected length]
- Sensitivity: [any sensitive topics]
- Recording: [audio/video/notes only]
Research Goals: [what insights you need]
Please provide:
1. Interview protocol with:
   - Introduction script
   - Consent process
   - Warm-up questions
   - Main questions with probes
   - Closing questions
2. Cultural adaptation notes
3. Tips for building rapport
4. Sensitive topic navigation strategies
5. Note-taking template`,
    systemMessage: 'You are a qualitative research expert who understands the nuances of conducting culturally sensitive interviews while maintaining research rigor.',
    exampleInput: `Research Question: How do women entrepreneurs navigate social norms?
Participants: Women running small businesses
Context: Conservative rural communities in South Asia
Language: Local dialect with translator
Setting: Participants' shops/homes
Type: Semi-structured
Duration: 45-60 minutes
Sensitivity: Family dynamics, income
Goals: Understand barriers and coping strategies`,
    icon: 'MessageCircle',
    color: 'rose'
  },
  {
    id: 'workshop-agenda',
    title: 'Workshop Agenda Designer',
    description: 'Design engaging, participatory workshop agendas with clear learning objectives.',
    prompt: `Help me design a workshop agenda for my development program.
Workshop Overview:
- Topic: [workshop subject]
- Participants: [number and profile]
- Duration: [total time available]
- Objectives: [learning/outcome objectives]
- Venue: [physical/virtual/hybrid]
Participant Context:
- Prior Knowledge: [what they already know]
- Language: [language needs]
- Cultural Considerations: [important cultural factors]
- Accessibility Needs: [any special requirements]
Resources Available:
- Facilitators: [number and expertise]
- Materials: [available materials/budget]
- Technology: [available tech tools]
Please create:
1. Detailed agenda with timings
2. Session plans with:
   - Objectives for each session
   - Activities and methodologies
   - Materials needed
   - Facilitation notes
3. Energizers and icebreakers
4. Participation strategies
5. Evaluation methods
6. Follow-up action plan template`,
    systemMessage: 'You are a workshop facilitation expert who designs inclusive, engaging sessions that balance content delivery with participatory learning and account for diverse learning styles.',
    exampleInput: `Topic: Community-Based Child Protection
Participants: 30 village leaders and social workers
Duration: 2 days
Objectives: Build skills in identifying and responding to child protection issues
Venue: Community center (basic facilities)
Prior Knowledge: Basic understanding, no formal training
Language: Local language with some English
Cultural: Hierarchical society, gender-mixed group
Facilitators: 2 trained facilitators`,
    icon: 'Calendar',
    color: 'cyan'
  },
  {
    id: 'report-synthesizer',
    title: 'Research Report Synthesizer',
    description: 'Synthesize multiple research sources into coherent, actionable reports.',
    prompt: `I need help synthesizing multiple research sources into a comprehensive report.
Research Materials:
- Number of Sources: [how many documents/studies]
- Types: [academic papers/reports/data sets/interviews]
- Key Topics: [main themes covered]
- Quality: [peer-reviewed/grey literature/internal]
Report Requirements:
- Purpose: [inform/advocacy/evaluate]
- Audience: [who will read this]
- Length: [word/page limit]
- Format: [academic/policy/donor report]
- Deadline: [when needed]
Specific Needs:
- Focus Areas: [what to emphasize]
- Questions to Answer: [key questions]
- Recommendations Needed: [yes/no and what type]
Please provide:
1. Report outline with sections
2. Executive summary template
3. Literature review synthesis
4. Key findings organized by theme
5. Evidence assessment/quality notes
6. Gaps identified in current research
7. Recommendations based on evidence
8. References/citation format`,
    systemMessage: 'You are a research synthesis expert who can identify patterns across diverse sources, assess evidence quality, and create coherent narratives that serve specific purposes.',
    exampleInput: `Sources: 15 studies on cash transfer programs
Types: 10 academic papers, 3 evaluations, 2 datasets
Topics: Impact on education, health, women's empowerment
Purpose: Inform program design
Audience: Development practitioners
Length: 20 pages
Focus: What works for conditional vs unconditional transfers
Questions: Which approach is more cost-effective? What are implementation best practices?`,
    icon: 'BookOpen',
    color: 'violet'
  },
  {
    id: 'budget-template',
    title: 'Program Budget Builder',
    description: 'Create detailed program budgets with proper cost categories and justifications.',
    prompt: `Help me create a comprehensive budget for my development program.
Program Information:
- Duration: [program length]
- Total Budget Ceiling: [if known]
- Funding Source: [donor/organization]
- Budget Format Required: [specific template?]
Program Components:
- Main Activities: [list key activities]
- Staff Required: [positions and time allocation]
- Geographic Coverage: [locations]
- Direct Beneficiaries: [number]
Cost Categories Needed:
- Personnel: [salaries/consultants]
- Operations: [office/utilities]
- Program Activities: [direct costs]
- Travel: [local/international]
- Equipment: [what's needed]
- M&E: [monitoring costs]
- Overhead: [indirect cost rate]
Please provide:
1. Detailed line-item budget
2. Budget narrative/justification
3. Cost per beneficiary calculation
4. Budget by quarter/year
5. Co-funding/matching requirements
6. Cost-effectiveness analysis
7. Contingency planning (10% variance scenarios)`,
    systemMessage: 'You are a program finance expert who understands donor requirements, cost-effectiveness, and realistic budgeting for development programs.',
    exampleInput: `Duration: 2 years
Ceiling: $300,000
Funder: USAID
Activities: Training, mentorship, job placement for youth
Staff: Project manager (100%), 3 field coordinators (100%), M&E officer (50%)
Coverage: 3 districts
Beneficiaries: 500 youth
Overhead: 15% allowed`,
    icon: 'TrendingUp',
    color: 'emerald'
  },
  {
    id: 'survey-designer',
    title: 'Survey Questionnaire Designer',
    description: 'Design effective surveys with proper question construction and flow.',
    prompt: `I need help designing a survey questionnaire for my research/program.
Survey Purpose:
- Objective: [what you're measuring]
- Population: [who you're surveying]
- Sample Size: [planned number]
- Method: [face-to-face/phone/online]
Information Needed:
- Demographics: [what demographic data]
- Main Topics: [key areas to cover]
- Sensitive Topics: [any sensitive questions]
- Baseline/Endline: [comparison needed?]
Constraints:
- Length: [time/question limit]
- Language: [survey language(s)]
- Literacy Level: [respondent literacy]
- Cultural Factors: [relevant considerations]
Please provide:
1. Survey structure/flow
2. Question bank with:
   - Demographic questions
   - Main topic questions
   - Question types (multiple choice/scale/open)
   - Skip logic/branching
3. Response scales and options
4. Introduction and consent script
5. Data quality check questions
6. Pilot testing plan
7. Translation notes`,
    systemMessage: 'You are a survey methodology expert who understands question construction, survey flow, cultural adaptation, and how to minimize bias while maximizing response quality.',
    exampleInput: `Objective: Assess impact of nutrition program
Population: Mothers with children under 5
Sample: 400 households
Method: Face-to-face tablet survey
Demographics: Age, education, income, family size
Topics: Feeding practices, nutrition knowledge, health seeking
Sensitive: Household income, food insecurity
Length: 30 minutes maximum
Language: Local language, low literacy`,
    icon: 'FileText',
    color: 'orange'
  },
  {
    id: 'case-study',
    title: 'Case Study Developer',
    description: 'Develop compelling case studies that demonstrate impact and learning.',
    prompt: `Help me develop a case study about my program/intervention.
Case Study Focus:
- Subject: [specific intervention/person/community]
- Purpose: [learning/advocacy/documentation]
- Audience: [who will read this]
- Length: [word count/pages]
Context and Background:
- Setting: [geographic/social context]
- Timeline: [when this happened]
- Key Actors: [people/organizations involved]
- Initial Situation: [problem/challenge]
The Story:
- Intervention: [what was done]
- Process: [how it unfolded]
- Challenges: [obstacles faced]
- Solutions: [how challenges were addressed]
- Results: [what changed]
Evidence Available:
- Data: [quantitative evidence]
- Quotes: [testimonials available]
- Photos: [visual documentation]
Please provide:
1. Case study structure/outline
2. Compelling narrative with:
   - Hook/opening
   - Context setting
   - Challenge presentation
   - Solution journey
   - Impact demonstration
   - Lessons learned
3. Sidebar elements (stats, quotes, timeline)
4. Discussion questions
5. Replication guidance`,
    systemMessage: 'You are a storytelling expert who can craft engaging narratives that balance human interest with evidence-based insights and practical learning.',
    exampleInput: `Subject: Village savings group transforms community
Purpose: Demonstrate model for replication
Audience: NGOs and donors
Setting: Rural Kenya, drought-prone area
Timeline: 2022-2024
Intervention: Established women's savings groups
Challenges: Initial mistrust, low literacy
Results: 200 women saving, 50 businesses started
Evidence: Savings data, 20 interviews, photos`,
    icon: 'Award',
    color: 'pink'
  },
  {
    id: 'training-curriculum',
    title: 'Training Curriculum Developer',
    description: 'Create comprehensive training curricula with modules, materials, and assessments.',
    prompt: `I need help developing a training curriculum for my program.
Training Overview:
- Topic: [subject matter]
- Target Learners: [who and background]
- Duration: [total training period]
- Format: [in-person/online/blended]
- Certification: [any certification needs]
Learning Objectives:
- Knowledge: [what they should know]
- Skills: [what they should be able to do]
- Attitudes: [mindset changes needed]
Context:
- Prior Learning: [existing knowledge/skills]
- Language: [training language]
- Resources: [available materials/budget]
- Venue/Platform: [where training happens]
Post-Training:
- Application: [how they'll use learning]
- Support: [follow-up available]
Please create:
1. Curriculum framework with:
   - Module outline and sequencing
   - Learning objectives per module
   - Time allocation
2. For each module:
   - Content outline
   - Teaching methods
   - Activities/exercises
   - Materials needed
   - Assessment methods
3. Participant materials list
4. Trainer's guide outline
5. Assessment strategy
6. Training evaluation plan`,
    systemMessage: 'You are a curriculum development expert who understands adult learning principles, competency-based training, and how to create engaging, practical learning experiences.',
    exampleInput: `Topic: Community Health Worker Training
Learners: 30 village volunteers, basic education
Duration: 5 days initial + monthly refreshers
Format: In-person with WhatsApp follow-up
Knowledge: Basic health, danger signs, referral
Skills: Health education, basic first aid, record keeping
Prior: Traditional health knowledge, no formal training
Application: Serve 50 households each`,
    icon: 'BookOpen',
    color: 'slate'
  },
  {
    id: 'advocacy-strategy',
    title: 'Advocacy Strategy Planner',
    description: 'Develop comprehensive advocacy strategies with clear pathways to change.',
    prompt: `Help me develop an advocacy strategy for my cause/issue.
Issue Overview:
- Problem: [issue you're addressing]
- Current Situation: [status quo]
- Desired Change: [specific policy/practice change]
- Geographic Focus: [local/national/global]
Stakeholder Landscape:
- Decision Makers: [who can make the change]
- Allies: [supporters/partners]
- Opposition: [who might resist]
- Influencers: [who influences decision makers]
Organizational Capacity:
- Resources: [budget/staff for advocacy]
- Expertise: [advocacy experience]
- Network: [connections/coalitions]
- Time Frame: [urgency/timeline]
Context:
- Political Climate: [opportunities/risks]
- Public Opinion: [current attitudes]
- Media Environment: [media landscape]
Please provide:
1. Theory of Change for advocacy
2. Stakeholder power analysis
3. Key messages and framing
4. Tactical options with pros/cons:
   - Inside tactics (lobbying, meetings)
   - Outside tactics (media, mobilization)
5. Coalition building strategy
6. Media and communications plan
7. Risk assessment and mitigation
8. Timeline with milestones
9. Success metrics`,
    systemMessage: 'You are an advocacy strategy expert who understands power dynamics, policy processes, and how to build movements for social change.',
    exampleInput: `Problem: Lack of menstrual hygiene facilities in schools
Current: No policy requiring facilities
Desired Change: Mandatory facilities in all schools
Focus: State level
Decision Makers: Education Ministry, School Board
Allies: Parent associations, health NGOs
Opposition: Some conservative groups
Resources: Small team, $50K budget
Timeline: Policy window in 6 months`,
    icon: 'Zap',
    color: 'red'
  },
  {
    id: 'learning-assessment',
    title: 'Learning Assessment Creator',
    description: 'Design assessments that effectively measure learning outcomes and competencies.',
    prompt: `I need help creating learning assessments for my educational program.
Program Context:
- Subject/Skills: [what you're teaching]
- Learner Profile: [age, background, level]
- Program Duration: [length of learning]
- Setting: [formal/informal education]
Learning Objectives:
- Knowledge: [what they should know]
- Skills: [what they should do]
- Competencies: [integrated abilities]
Assessment Requirements:
- Purpose: [formative/summative/diagnostic]
- Format: [test/project/portfolio/observation]
- Frequency: [when assessments occur]
- Stakes: [high/low stakes]
Constraints:
- Time Available: [for assessment]
- Resources: [what's available]
- Literacy/Language: [considerations]
- Technology: [available tools]
Please provide:
1. Assessment framework aligned to objectives
2. Assessment methods mix:
   - Knowledge assessments
   - Skill demonstrations
   - Competency evaluations
3. Assessment tools:
   - Rubrics with criteria
   - Question banks
   - Performance tasks
   - Self-assessment tools
4. Marking schemes/answer keys
5. Feedback templates
6. Progress tracking system
7. Remediation strategies`,
    systemMessage: 'You are an educational assessment expert who designs fair, valid assessments that promote learning while accurately measuring achievement.',
    exampleInput: `Subject: Digital literacy for adults
Learners: 25 adults, basic education, no computer experience
Duration: 10-week course
Objectives: Basic computer use, internet, email, documents
Purpose: Summative for certification
Format: Practical + written test
Time: 2 hours total
Resources: Computer lab available`,
    icon: 'Trophy',
    color: 'yellow'
  },
  {
    id: 'escape-room',
    title: 'Educational Escape Room Designer',
    description: 'Create immersive educational escape rooms that make learning unforgettable through puzzle-solving and teamwork.',
    prompt: `Design an educational escape room experience for my learning objectives.
**Learning Context**:
- Subject/Topic: [main content area]
- Learning Objectives: [specific skills/knowledge to teach]
- Target Audience: [age group and prior knowledge]
- Group Size: [number of participants]
- Time Limit: [duration of escape room]
- Physical Space: [room size and layout available]
- Technology Available: [tablets/computers/props available]
**Theme Preferences**:
- Setting: [historical/fantasy/mystery/scientific]
- Narrative Style: [serious/playful/dramatic]
- Difficulty Level: [beginner/intermediate/advanced]
Please create:
1. **Immersive Storyline**:
   - Compelling narrative hook that connects to learning objectives
   - Character roles for participants (if applicable)
   - Story progression through puzzle completion
   - Dramatic conclusion that reinforces key concepts
2. **Puzzle Sequence** (5-8 interconnected puzzles):
   - Each puzzle directly teaches/reinforces a learning objective
   - Variety of puzzle types (codes, physical, logic, word, math)
   - Clear connection between puzzle solution and curriculum
   - Progressive difficulty with built-in hints system
3. **Complete Implementation Guide**:
   - Room setup instructions and materials list
   - Detailed puzzle instructions and solutions
   - Facilitator guide with hints system
   - Student handouts and clue sheets
   - Assessment rubric for learning objectives
   - Alternative versions for different ability levels
4. **Learning Integration**:
   - Clear connections between each puzzle and curriculum
   - Debrief questions to reinforce learning
   - Extension activities for early finishers
Ensure all puzzles are solvable, age-appropriate, and directly tied to learning goals.`,
    systemMessage: 'You are an immersive learning experience designer who creates educational escape rooms. You understand game mechanics, puzzle design, and how to seamlessly integrate curriculum content into engaging storylines that promote deep learning.',
    exampleInput: `Topic: Chemical Bonding and Molecular Structure
Objectives: 1) Identify ionic vs covalent bonds 2) Predict molecular shapes 3) Understand electronegativity 4) Apply bonding theory to real compounds
Theme: Secret laboratory - students are chemists who must prevent a dangerous reaction
Grade: 10th grade Chemistry
Time: 45 minutes
Size: Groups of 4-5 students
Tech: Tablets available for digital clues/simulations`,
    icon: 'Puzzle',
    color: 'purple'
  }
];

// src/App.js
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Search, Bookmark, Heart, MessageCircle, 
  Download, ExternalLink, Play, Pause, SkipForward, Volume2,
  User, LogOut, ChevronRight, Star, Clock, Users, Target,
  Gamepad2, BookOpen, Mail, Phone, Globe, Twitter, Linkedin,
  Github, Coffee, Zap, TrendingUp, Award, Filter, Calendar,
  FileText, BarChart, Settings, ArrowRight, CheckCircle,
  AlertCircle, Info, HelpCircle, Share2, PlayCircle, Scale,
  Lightbulb, Compare, Send, Edit3, Brain, PenTool, FolderOpen,
  Loader2, Copy, Sparkles, Wand2, Bot, Puzzle, Trophy, Shield, ArrowLeft
} from 'lucide-react';

// Firebase imports
import { initializeApp } from 'firebase/app';
import { 
  getAuth, 
  GoogleAuthProvider, 
  signInWithPopup, 
  signOut as firebaseSignOut, 
  onAuthStateChanged 
} from 'firebase/auth';
import { 
  getFirestore, 
  collection, 
  doc, 
  setDoc, 
  getDoc, 
  addDoc, 
  query, 
  where, 
  getDocs,
  deleteDoc 
} from 'firebase/firestore';

// Firebase Configuration
const firebaseConfig = {
  apiKey: "AIzaSyDnF0eJsTULzOJUnBskybd44dG5w-f46vE",
  authDomain: "impactmojo.firebaseapp.com",
  projectId: "impactmojo",
  storageBucket: "impactmojo.firebasestorage.app",
  messagingSenderId: "529198336589",
  appId: "1:529198336589:web:1664b5344de5bfb31bea04",
  measurementId: "G-ZHPPXXMRGV"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const googleProvider = new GoogleAuthProvider();

// Course Data (37 Courses)
const courseData = [
  {
    id: "C1",
    title: "Gender Studies 101",
    track: "Gender Studies",
    description: "Introduction to gender theory and its practical implications.",
    url: "https://101.www.impactmojo.in/gender-studies",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Eye-opening exploration of gender norms."',
  },
  {
    id: "C2",
    title: "Women's Economic Empowerment 101",
    track: "Gender Studies",
    description: "Strategies and frameworks for women's economic participation.",
    url: "https://101.www.impactmojo.in/WEE",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Essential for inclusive development."',
  },
  {
    id: "C3",
    title: "LGBTQ+ Rights and Inclusion 101",
    track: "Gender Studies",
    description: "Understanding LGBTQ+ issues and building inclusive communities.",
    url: "https://101.www.impactmojo.in/LGBTQ",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Building bridges through understanding."',
  },
  {
    id: "C4",
    title: "Masculinities and Development 101",
    track: "Gender Studies",
    description: "Exploring masculinities and their role in development.",
    url: "https://101.www.impactmojo.in/masculinities",
    level: "Intermediate",
    duration: "2 hours",
    quote: '"Redefining strength and vulnerability."',
  },
  {
    id: "C5",
    title: "Care Economy 101",
    track: "Gender Studies",
    description: "Understanding the economics of care work and its societal value.",
    url: "https://101.www.impactmojo.in/careeconomy",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Making invisible work visible."',
  },
  {
    id: "C6",
    title: "Data Feminism 101",
    track: "Gender Studies",
    description: "Applying feminist principles to data science and analysis.",
    url: "https://101.www.impactmojo.in/DataFem",
    level: "Advanced",
    duration: "3 hours",
    quote: '"Data has gender - let\'s talk about it."',
  },
  {
    id: "C7",
    title: "Development Economics 101",
    track: "Policy and Economics",
    description: "Foundations of development economics for practitioners.",
    url: "https://101.www.impactmojo.in/DevEcon",
    level: "Beginner",
    duration: "2.5 hours",
    quote: '"Economics meets social impact."',
  },
  {
    id: "C8",
    title: "Political Economy 101",
    track: "Policy and Economics",
    description: "Understanding political economy dynamics in development.",
    url: "https://101.www.impactmojo.in/polecon",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Where politics meets economics."',
  },
  {
    id: "C9",
    title: "Poverty and Inequality 101",
    track: "Policy and Economics",
    description: "Measuring and addressing poverty and inequality.",
    url: "https://101.www.impactmojo.in/pov&inq",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Understanding the wealth gap."',
  },
  {
    id: "C10",
    title: "Livelihoods 101",
    track: "Policy and Economics",
    description: "Sustainable livelihoods framework and applications.",
    url: "https://101.www.impactmojo.in/Livelihoods",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Building economic resilience."',
  },
  {
    id: "C11",
    title: "Social Welfare and Safety Nets 101",
    track: "Policy and Economics",
    description: "Design and implementation of social protection systems.",
    url: "https://101.www.impactmojo.in/safetynets",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Protecting the vulnerable."',
  },
  {
    id: "C12",
    title: "Fundraising 101",
    track: "Policy and Economics",
    description: "Strategic fundraising for development organizations.",
    url: "https://101.www.impactmojo.in/fundraising",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Turning vision into resources."',
  },
  {
    id: "C13",
    title: "Decent Work 101",
    track: "Policy and Economics",
    description: "ILO's decent work agenda and labor rights.",
    url: "https://101.www.impactmojo.in/DecentWork",
    level: "Intermediate",
    duration: "2 hours",
    quote: '"Work with dignity for all."',
  },
  {
    id: "C14",
    title: "Marginalized Identities 101",
    track: "Policy and Economics",
    description: "Understanding and addressing marginalization.",
    url: "https://101.www.impactmojo.in/identities",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Centering the margins."',
  },
  {
    id: "C15",
    title: "Data Literacy 101",
    track: "Data Analysis",
    description: "Building foundational data literacy skills.",
    url: "https://101.www.impactmojo.in/data-lit",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Data-driven decision making."',
  },
  {
    id: "C16",
    title: "Econometrics 101",
    track: "Data Analysis",
    description: "Applied econometrics for development research.",
    url: "https://101.www.impactmojo.in/econometrics",
    level: "Advanced",
    duration: "3 hours",
    quote: '"Statistics meets economics."',
  },
  {
    id: "C17",
    title: "Bivariate Analysis 101",
    track: "Data Analysis",
    description: "Understanding relationships between two variables.",
    url: "https://101.www.impactmojo.in/bivariateA",
    level: "Intermediate",
    duration: "2 hours",
    quote: '"Finding connections in data."',
  },
  {
    id: "C18",
    title: "Multivariate Analysis 101",
    track: "Data Analysis",
    description: "Advanced statistical analysis with multiple variables.",
    url: "https://101.www.impactmojo.in/MultivariateA",
    level: "Advanced",
    duration: "3 hours",
    quote: '"Complex data, clear insights."',
  },
  {
    id: "C19",
    title: "Exploratory Data Analysis for Household Surveys 101",
    track: "Data Analysis",
    description: "EDA techniques for household survey data.",
    url: "https://101.www.impactmojo.in/HH-EDA",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Survey data demystified."',
  },
  {
    id: "C20",
    title: "Observation to Insight 101",
    track: "Data Analysis",
    description: "Transforming observations into actionable insights.",
    url: "https://101.www.impactmojo.in/obs2insight",
    level: "Advanced",
    duration: "3 hours",
    quote: '"From data to decisions."',
    isPremium: true
  },
  {
    id: "C21",
    title: "Item Response Theory 101",
    track: "Data Analysis",
    description: "Advanced measurement theory for assessment design.",
    url: "https://101.www.impactmojo.in/IRT",
    level: "Advanced",
    duration: "3 hours",
    quote: '"Precision in measurement."',
    isPremium: true
  },
  {
    id: "C22",
    title: "Research Ethics 101",
    track: "Research Methods",
    description: "Ethical considerations in development research.",
    url: "https://101.www.impactmojo.in/ResearchEthics",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Do no harm, do good."',
  },
  {
    id: "C23",
    title: "Qualitative Research Methods 101",
    track: "Research Methods",
    description: "Qualitative research design and implementation.",
    url: "https://101.www.impactmojo.in/QualR",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Stories behind the numbers."',
  },
  {
    id: "C24",
    title: "Visual Ethnography 101",
    track: "Research Methods",
    description: "Using visual methods in ethnographic research.",
    url: "https://101.www.impactmojo.in/VEthno",
    level: "Advanced",
    duration: "3 hours",
    quote: '"Seeing culture differently."',
  },
  {
    id: "C25",
    title: "Monitoring, Evaluation, Accountability and Learning 101",
    track: "Research Methods",
    description: "Comprehensive MEAL framework and tools.",
    url: "https://101.www.impactmojo.in/MEAL",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Measuring what matters."',
  },
  {
    id: "C26",
    title: "Behavior Change Communication Programming 101",
    track: "Research Methods",
    description: "Designing effective behavior change interventions.",
    url: "https://101.www.impactmojo.in/BCCP",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Inspiring positive change."',
  },
  {
    id: "C27",
    title: "Climate Science 101",
    track: "Thematic Areas",
    description: "Understanding climate change and its impacts.",
    url: "https://101.www.impactmojo.in/ClimateScience",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Our planet, our future."',
  },
  {
    id: "C28",
    title: "Environmental Justice 101",
    track: "Thematic Areas",
    description: "Intersection of environment and social justice.",
    url: "https://101.www.impactmojo.in/env-jus",
    level: "Intermediate",
    duration: "2 hours",
    quote: '"Justice for people and planet."',
  },
  {
    id: "C29",
    title: "Public Health 101",
    track: "Thematic Areas",
    description: "Foundations of public health in development.",
    url: "https://101.www.impactmojo.in/ph",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Health for all."',
  },
  {
    id: "C30",
    title: "Sexual and Reproductive Health Rights 101",
    track: "Thematic Areas",
    description: "Understanding SRHR in development contexts.",
    url: "https://101.www.impactmojo.in/srhr",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Rights, dignity, choice."',
  },
  {
    id: "C31",
    title: "Digital Ethics 101",
    track: "Thematic Areas",
    description: "Ethical considerations in digital development.",
    url: "https://101.www.impactmojo.in/DigitalEthics",
    level: "Intermediate",
    duration: "2 hours",
    quote: '"Technology with conscience."',
  },
  {
    id: "C32",
    title: "Law and Constitution 101",
    track: "Thematic Areas",
    description: "Legal frameworks for development work.",
    url: "https://101.www.impactmojo.in/Law&Cons",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Justice through law."',
  },
  {
    id: "C33",
    title: "Community Development 101",
    track: "Thematic Areas",
    description: "Participatory approaches to community development.",
    url: "https://101.www.impactmojo.in/community-dev",
    level: "Beginner",
    duration: "2 hours",
    quote: '"By the community, for the community."',
  },
  {
    id: "C34",
    title: "Decolonising Development 101",
    track: "Thematic Areas",
    description: "Critical perspectives on development practice.",
    url: "https://101.www.impactmojo.in/decolonD",
    level: "Advanced",
    duration: "3 hours",
    quote: '"Reimagining development."',
  },
  {
    id: "C35",
    title: "Post-Truth Politics 101",
    track: "Thematic Areas",
    description: "Navigating misinformation in development.",
    url: "https://101.www.impactmojo.in/post-truth-pol",
    level: "Advanced",
    duration: "2.5 hours",
    quote: '"Truth in a complex world."',
  },
  {
    id: "C36",
    title: "Global Development Architecture 101",
    track: "Thematic Areas",
    description: "Understanding global development institutions.",
    url: "https://101.www.impactmojo.in/GDArch",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"The big picture of aid."',
  },
  {
    id: "C37",
    title: "Social Emotional Learning 101",
    track: "Thematic Areas",
    description: "SEL approaches in development programs.",
    url: "https://101.www.impactmojo.in/SEL",
    level: "Intermediate",
    duration: "2 hours",
    quote: '"Hearts and minds together."',
    isPremium: true
  }
];

// Labs Data (10 Interactive Labs)
const labsData = [
  {
    id: "L1",
    title: "Gender Timeline: Climate Edition",
    description: "Interactive timeline exploring the intersection of gender and climate change through history.",
    url: "https://gen-cc-timelines.netlify.app/",
    icon: "timeline",
    category: "Gender Studies",
    difficulty: "Beginner",
    duration: 45,
    status: "Available"
  },
  {
    id: "L2",
    title: "Research Lab: Methods Comparison",
    description: "Compare and contrast different research methodologies for your project.",
    url: "https://researchmethodology-lab.netlify.app/",
    icon: "flask",
    category: "Research Methods",
    difficulty: "Intermediate",
    duration: 60,
    status: "Available"
  },
  {
    id: "L3",
    title: "Policy Advocacy Impact Lab",
    description: "Simulate policy advocacy campaigns and measure their potential impact.",
    url: "https://pol-advocacy4impact.netlify.app/",
    icon: "megaphone",
    category: "Policy Analysis", 
    difficulty: "Intermediate",
    duration: 65,
    status: "Available"
  },
  {
    id: "L4",
    title: "Partnership and Collaboration Lab",
    description: "Framework for building effective partnerships.",
    url: "https://impact-partnerships.netlify.app/",
    icon: "handshake",
    category: "Stakeholder Engagement",
    difficulty: "Intermediate",
    duration: 55,
    status: "Available"
  },
  {
    id: "L5",
    title: "MLE Framework Workbench",
    description: "Monitoring, Learning and Evaluation framework design.",
    url: "https://mle-frameworkdesign.netlify.app/",
    icon: "wrench",
    category: "Monitoring & Evaluation",
    difficulty: "Advanced",
    duration: 90,
    status: "Available"
  },
  {
    id: "L6",
    title: "MLE Framework Builder Lab", 
    description: "Build comprehensive MLE frameworks for your projects.",
    url: "https://mle-plan-lab.netlify.app/",
    icon: "build", 
    category: "Monitoring & Evaluation",
    difficulty: "Advanced",
    duration: 85,
    status: "Available"
  },
  {
    id: "L7",
    title: "Community Engagement Lab",
    description: "Tools for meaningful community engagement and participation.",
    url: "https://community-engagement.netlify.app/",
    icon: "users",
    category: "Community Development",
    difficulty: "Intermediate", 
    duration: 60,
    status: "Available"
  },
  {
    id: "L8",
    title: "Impact Storytelling Lab",
    description: "Craft compelling narratives about your impact work.",
    url: "https://impact-storytelling.netlify.app/",
    icon: "book-open",
    category: "Communications",
    difficulty: "Beginner",
    duration: 45,
    status: "Available"
  },
  {
    id: "L9",
    title: "Innovation and Design Thinking Lab",
    description: "Apply design thinking to development challenges.",
    url: "https://impactdesign-thinking.netlify.app/",
    icon: "lightbulb",
    category: "Innovation",
    difficulty: "Intermediate",
    duration: 70,
    status: "Available"
  },
  {
    id: "L10",
    title: "TOC Workbench",
    description: "Theory of Change development and visualization tools.",
    url: "https://toc-workbench.netlify.app/",
    icon: "target",
    category: "Strategic Planning",
    difficulty: "Advanced",
    duration: 80,
    status: "Available"
  },
];

// AI Tools Data
const aiToolsData = [
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
    icon: BarChart,
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
    icon: Target,
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
    icon: FileText,
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
    icon: Users,
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
    icon: CheckCircle,
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
    icon: Scale,
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
    icon: MessageCircle,
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
    icon: Calendar,
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
- Purpose: [inform/advocate/evaluate]
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
    icon: BookOpen,
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
    icon: TrendingUp,
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
    icon: FileText,
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
    icon: Award,
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
    icon: BookOpen,
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
    icon: Zap,
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
    icon: Trophy,
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
    icon: Puzzle,
    color: 'purple'
  }
];

// Authentication Context
const AuthContext = createContext();
const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user);
      if (user) {
        // Load user bookmarks
        try {
          const userDoc = await getDoc(doc(db, 'users', user.uid));
          if (userDoc.exists()) {
            setBookmarks(userDoc.data().bookmarks || []);
          }
        } catch (error) {
          console.error('Error loading bookmarks:', error);
        }
      } else {
        setBookmarks([]);
      }
      setLoading(false);
    });
    return unsubscribe;
  }, []);

  const signInWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, googleProvider);
      const user = result.user;
      
      // Create or update user document
      await setDoc(doc(db, 'users', user.uid), {
        name: user.displayName,
        email: user.email,
        photoURL: user.photoURL,
        lastLogin: new Date()
      }, { merge: true });
      
      return user;
    } catch (error) {
      console.error('Error signing in:', error);
      throw error;
    }
  };

  const signOut = async () => {
    try {
      await firebaseSignOut(auth);
    } catch (error) {
      console.error('Error signing out:', error);
      throw error;
    }
  };

  const toggleBookmark = async (itemId) => {
    if (!user) return;
    
    try {
      const newBookmarks = bookmarks.includes(itemId)
        ? bookmarks.filter(id => id !== itemId)
        : [...bookmarks, itemId];
      
      await setDoc(doc(db, 'users', user.uid), {
        bookmarks: newBookmarks
      }, { merge: true });
      
      setBookmarks(newBookmarks);
    } catch (error) {
      console.error('Error toggling bookmark:', error);
    }
  };

  return (
    <AuthContext.Provider value={{
      user,
      loading,
      bookmarks,
      signInWithGoogle,
      signOut,
      toggleBookmark
    }}>
      {children}
    </AuthContext.Provider>
  );
};

const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

// Page Context
const PageContext = createContext();
const PageProvider = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('home');
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    // Check for saved theme preference
    const isDark = localStorage.getItem('darkMode') === 'true';
    setDarkMode(isDark);
  }, []);

  useEffect(() => {
    // Save theme preference
    localStorage.setItem('darkMode', darkMode);
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  return (
    <PageContext.Provider value={{ currentPage, setCurrentPage, darkMode, setDarkMode }}>
      {children}
    </PageContext.Provider>
  );
};

const usePage = () => {
  const context = useContext(PageContext);
  if (!context) {
    throw new Error('usePage must be used within PageProvider');
  }
  return context;
};

// Navigation Component
const Navigation = () => {
  const { user, signOut, signInWithGoogle } = useAuth();
  const { currentPage, setCurrentPage, darkMode, setDarkMode } = usePage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <nav className="bg-white dark:bg-gray-800 shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0 flex items-center">
              <div className="h-8 w-8 rounded-md bg-indigo-600 flex items-center justify-center">
                <span className="text-white font-bold">IM</span>
              </div>
              <span className="ml-2 text-xl font-bold text-gray-900 dark:text-white">ImpactMojo</span>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <button
                onClick={() => setCurrentPage('home')}
                className={`${currentPage === 'home' ? 'border-indigo-500 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:border-gray-300 hover:text-gray-700 dark:hover:text-gray-200'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
              >
                Home
              </button>
              <button
                onClick={() => setCurrentPage('courses')}
                className={`${currentPage === 'courses' ? 'border-indigo-500 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:border-gray-300 hover:text-gray-700 dark:hover:text-gray-200'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
              >
                Courses
              </button>
              <button
                onClick={() => setCurrentPage('labs')}
                className={`${currentPage === 'labs' ? 'border-indigo-500 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:border-gray-300 hover:text-gray-700 dark:hover:text-gray-200'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
              >
                Labs
              </button>
              <button
                onClick={() => setCurrentPage('ai-tools')}
                className={`${currentPage === 'ai-tools' ? 'border-indigo-500 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:border-gray-300 hover:text-gray-700 dark:hover:text-gray-200'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
              >
                AI Tools
              </button>
            </div>
          </div>
          <div className="hidden sm:ml-6 sm:flex sm:items-center">
            {/* Theme toggle button */}
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-gray-200 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
            >
              {darkMode ? (
                <Sun className="h-5 w-5 text-yellow-400" /> // Sun icon in yellow for dark mode
              ) : (
                <Moon className="h-5 w-5 text-gray-700" /> // Moon icon in gray for light mode
              )}
            </button>

            {/* Authentication button */}
            {user ? (
              <div className="ml-3 relative">
                <div>
                  <button className="flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    <span className="sr-only">Open user menu</span>
                    <img className="h-8 w-8 rounded-full" src={user.photoURL} alt={user.displayName} />
                  </button>
                </div>
                {/* User dropdown menu would go here if needed */}
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Sign In
              </button>
            )}
          </div>
          <div className="-mr-2 flex items-center sm:hidden">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
            >
              <span className="sr-only">Open main menu</span>
              {mobileMenuOpen ? (
                <X className="block h-6 w-6" />
              ) : (
                <Menu className="block h-6 w-6" />
              )}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="sm:hidden">
          <div className="pt-2 pb-3 space-y-1">
            <button
              onClick={() => { setCurrentPage('home'); setMobileMenuOpen(false); }}
              className={`${currentPage === 'home' ? 'bg-indigo-50 border-indigo-500 text-indigo-700' : 'border-transparent text-gray-600 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-800'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium`}
            >
              Home
            </button>
            <button
              onClick={() => { setCurrentPage('courses'); setMobileMenuOpen(false); }}
              className={`${currentPage === 'courses' ? 'bg-indigo-50 border-indigo-500 text-indigo-700' : 'border-transparent text-gray-600 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-800'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium`}
            >
              Courses
            </button>
            <button
              onClick={() => { setCurrentPage('labs'); setMobileMenuOpen(false); }}
              className={`${currentPage === 'labs' ? 'bg-indigo-50 border-indigo-500 text-indigo-700' : 'border-transparent text-gray-600 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-800'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium`}
            >
              Labs
            </button>
            <button
              onClick={() => { setCurrentPage('ai-tools'); setMobileMenuOpen(false); }}
              className={`${currentPage === 'ai-tools' ? 'bg-indigo-50 border-indigo-500 text-indigo-700' : 'border-transparent text-gray-600 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-800'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium`}
            >
              AI Tools
            </button>
          </div>
          <div className="pt-4 pb-3 border-t border-gray-200">
            <div className="flex items-center px-4">
              {user ? (
                <>
                  <div className="flex-shrink-0">
                    <img className="h-10 w-10 rounded-full" src={user.photoURL} alt={user.displayName} />
                  </div>
                  <div className="ml-3">
                    <div className="text-base font-medium text-gray-800">{user.displayName}</div>
                    <div className="text-sm font-medium text-gray-500">{user.email}</div>
                  </div>
                </>
              ) : (
                <div className="text-base font-medium text-gray-800">Not signed in</div>
              )}
            </div>
            <div className="mt-3 space-y-1">
              {user ? (
                <button
                  onClick={signOut}
                  className="block px-4 py-2 text-base font-medium text-gray-500 hover:text-gray-800 hover:bg-gray-100"
                >
                  Sign out
                </button>
              ) : (
                <button
                  onClick={signInWithGoogle}
                  className="block px-4 py-2 text-base font-medium text-gray-500 hover:text-gray-800 hover:bg-gray-100"
                >
                  Sign in
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};

// Home Page Component
const HomePage = () => {
  const { darkMode, setCurrentPage } = usePage();
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 dark:text-white sm:text-5xl md:text-6xl">
            <span className="block">Welcome to</span>
            <span className="block text-indigo-600 dark:text-indigo-400">ImpactMojo</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-500 dark:text-gray-400 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Your platform for development learning and tools. Explore courses, labs, and AI-powered tools to enhance your impact.
          </p>
          <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
            <div className="rounded-md shadow">
              <button
                onClick={() => setCurrentPage('courses')}
                className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-4 md:text-lg md:px-10"
              >
                Get started
              </button>
            </div>
            <div className="mt-3 rounded-md shadow sm:mt-0 sm:ml-3">
              <button
                onClick={() => setCurrentPage('ai-tools')}
                className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-indigo-600 dark:text-indigo-400 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 md:py-4 md:text-lg md:px-10"
              >
                Try AI Tools
              </button>
            </div>
          </div>
        </div>
        
        <div className="mt-16">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-white text-center">Featured Content</h2>
          <div className="mt-12 grid gap-5 max-w-lg mx-auto lg:grid-cols-3 lg:max-w-none">
            <div className="flex flex-col rounded-lg shadow-lg overflow-hidden">
              <div className="flex-1 bg-white dark:bg-gray-800 p-6 flex flex-col justify-between">
                <div className="flex-1">
                  <p className="text-sm font-medium text-indigo-600 dark:text-indigo-400">
                    <span>Course</span>
                  </p>
                  <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-white">Gender Studies 101</h3>
                  <p className="mt-3 text-base text-gray-500 dark:text-gray-400">
                    Introduction to gender theory and its practical implications in development work.
                  </p>
                </div>
                <div className="mt-6">
                  <button
                    onClick={() => setCurrentPage('courses')}
                    className="text-base font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300"
                  >
                    Explore courses
                  </button>
                </div>
              </div>
            </div>
            
            <div className="flex flex-col rounded-lg shadow-lg overflow-hidden">
              <div className="flex-1 bg-white dark:bg-gray-800 p-6 flex flex-col justify-between">
                <div className="flex-1">
                  <p className="text-sm font-medium text-indigo-600 dark:text-indigo-400">
                    <span>Lab</span>
                  </p>
                  <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-white">Gender Timeline: Climate Edition</h3>
                  <p className="mt-3 text-base text-gray-500 dark:text-gray-400">
                    Interactive timeline exploring the intersection of gender and climate change through history.
                  </p>
                </div>
                <div className="mt-6">
                  <button
                    onClick={() => setCurrentPage('labs')}
                    className="text-base font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300"
                  >
                    Explore labs
                  </button>
                </div>
              </div>
            </div>
            
            <div className="flex flex-col rounded-lg shadow-lg overflow-hidden">
              <div className="flex-1 bg-white dark:bg-gray-800 p-6 flex flex-col justify-between">
                <div className="flex-1">
                  <p className="text-sm font-medium text-indigo-600 dark:text-indigo-400">
                    <span>AI Tool</span>
                  </p>
                  <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-white">Theory of Change Builder</h3>
                  <p className="mt-3 text-base text-gray-500 dark:text-gray-400">
                    Develop comprehensive Theory of Change frameworks with clear pathways from activities to impact.
                  </p>
                </div>
                <div className="mt-6">
                  <button
                    onClick={() => setCurrentPage('ai-tools')}
                    className="text-base font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300"
                  >
                    Try AI Tools
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Courses Page Component
const CoursesPage = () => {
  const { darkMode, setCurrentPage } = usePage();
  const { bookmarks, toggleBookmark } = useAuth();
  
  // Get unique tracks
  const tracks = [...new Set(courseData.map(course => course.track))];
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white sm:text-4xl">
            Development Courses
          </h1>
          <p className="mt-3 max-w-2xl mx-auto text-xl text-gray-500 dark:text-gray-400 sm:mt-4">
            Explore our comprehensive library of courses designed for development professionals.
          </p>
        </div>
        
        <div className="mt-12">
          {tracks.map(track => (
            <div key={track} className="mb-12">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">{track}</h2>
              <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
                {courseData
                  .filter(course => course.track === track)
                  .map(course => (
                    <div key={course.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                      <div className="p-6">
                        <div className="flex justify-between items-start">
                          <div>
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-200">
                              {course.level}
                            </span>
                            <h3 className="mt-3 text-lg font-medium text-gray-900 dark:text-white">{course.title}</h3>
                            <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">{course.description}</p>
                          </div>
                          <button 
                            onClick={() => toggleBookmark(course.id)}
                            className="text-gray-400 hover:text-yellow-500 focus:outline-none"
                          >
                            {bookmarks.includes(course.id) ? (
                              <Bookmark className="h-5 w-5 text-yellow-500 fill-current" />
                            ) : (
                              <Bookmark className="h-5 w-5" />
                            )}
                          </button>
                        </div>
                        
                        <div className="mt-4 flex items-center text-sm text-gray-500 dark:text-gray-400">
                          <Clock className="flex-shrink-0 mr-1.5 h-4 w-4" />
                          {course.duration}
                        </div>
                        
                        <div className="mt-6">
                          <div className="flex items-center justify-between">
                            <span className="text-sm font-medium text-indigo-600 dark:text-indigo-400">
                              {course.isPremium ? 'Premium' : 'Free'}
                            </span>
                            <a
                              href={course.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="inline-flex items-center px-3 py-1 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                            >
                              Start Course
                              <ExternalLink className="ml-1 h-4 w-4" />
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Labs Page Component
const LabsPage = () => {
  const { darkMode, setCurrentPage } = usePage();
  const { bookmarks, toggleBookmark } = useAuth();
  
  // Get unique categories
  const categories = [...new Set(labsData.map(lab => lab.category))];
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white sm:text-4xl">
            Interactive Labs
          </h1>
          <p className="mt-3 max-w-2xl mx-auto text-xl text-gray-500 dark:text-gray-400 sm:mt-4">
            Hands-on learning experiences to apply development concepts in practice.
          </p>
        </div>
        
        <div className="mt-12">
          {categories.map(category => (
            <div key={category} className="mb-12">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">{category}</h2>
              <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
                {labsData
                  .filter(lab => lab.category === category)
                  .map(lab => (
                    <div key={lab.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                      <div className="p-6">
                        <div className="flex justify-between items-start">
                          <div>
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">
                              {lab.difficulty}
                            </span>
                            <h3 className="mt-3 text-lg font-medium text-gray-900 dark:text-white">{lab.title}</h3>
                            <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">{lab.description}</p>
                          </div>
                          <button 
                            onClick={() => toggleBookmark(lab.id)}
                            className="text-gray-400 hover:text-yellow-500 focus:outline-none"
                          >
                            {bookmarks.includes(lab.id) ? (
                              <Bookmark className="h-5 w-5 text-yellow-500 fill-current" />
                            ) : (
                              <Bookmark className="h-5 w-5" />
                            )}
                          </button>
                        </div>
                        
                        <div className="mt-4 flex items-center text-sm text-gray-500 dark:text-gray-400">
                          <Clock className="flex-shrink-0 mr-1.5 h-4 w-4" />
                          {lab.duration} minutes
                        </div>
                        
                        <div className="mt-6">
                          <div className="flex items-center justify-between">
                            <span className="text-sm font-medium text-green-600 dark:text-green-400">
                              {lab.status}
                            </span>
                            <a
                              href={lab.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="inline-flex items-center px-3 py-1 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
                            >
                              Start Lab
                              <ExternalLink className="ml-1 h-4 w-4" />
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// AI Tools Page Component
const AIToolsPage = () => {
  const { darkMode, setCurrentPage } = usePage();
  const { bookmarks, toggleBookmark } = useAuth();
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white sm:text-4xl">
            AI-Powered Tools
          </h1>
          <p className="mt-3 max-w-2xl mx-auto text-xl text-gray-500 dark:text-gray-400 sm:mt-4">
            Leverage artificial intelligence to enhance your development work.
          </p>
        </div>
        
        <div className="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {aiToolsData.map(tool => (
            <div key={tool.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
              <div className="p-6">
                <div className="flex justify-between items-start">
                  <div className="flex items-center">
                    <div className={`flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-${tool.color}-100 dark:bg-${tool.color}-900`}>
                      <tool.icon className={`h-6 w-6 text-${tool.color}-600 dark:text-${tool.color}-400`} />
                    </div>
                    <h3 className="ml-3 text-lg font-medium text-gray-900 dark:text-white">{tool.title}</h3>
                  </div>
                  <button 
                    onClick={() => toggleBookmark(tool.id)}
                    className="text-gray-400 hover:text-yellow-500 focus:outline-none"
                  >
                    {bookmarks.includes(tool.id) ? (
                      <Bookmark className="h-5 w-5 text-yellow-500 fill-current" />
                    ) : (
                      <Bookmark className="h-5 w-5" />
                    )}
                  </button>
                </div>
                
                <p className="mt-3 text-sm text-gray-500 dark:text-gray-400">{tool.description}</p>
                
                <div className="mt-6">
                  <button
                    onClick={() => setCurrentPage('ai-tools')}
                    className="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Try This Tool
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Main App Content Component
const AppContent = () => {
  const { currentPage, darkMode } = usePage();
  const { loading } = useAuth();

  if (loading) {
    return (
      <div className={`min-h-screen flex items-center justify-center ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
        <Loader2 className="h-12 w-12 animate-spin text-indigo-600" />
      </div>
    );
  }

  return (
    <div className={darkMode ? 'dark' : ''}>
      <Navigation />
      {currentPage === 'home' && <HomePage />}
      {currentPage === 'courses' && <CoursesPage />}
      {currentPage === 'labs' && <LabsPage />}
      {currentPage === 'ai-tools' && <AIToolsPage />}
    </div>
  );
};

// Main App Component
const App = () => {
  return (
    <AuthProvider>
      <PageProvider>
        <AppContent />
      </PageProvider>
    </AuthProvider>
  );
};

export default App;

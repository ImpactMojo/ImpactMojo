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
  Loader2, Copy, Sparkles, Wand2, Bot, Puzzle, Trophy, Shield, ArrowLeft, Crown
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
Please create:
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
Please create:
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
  },
  // Premium Tools
  {
    id: 'im-qual-lab',
    title: 'IM QualLab',
    description: 'Advanced qualitative research analysis tool for professional researchers',
    url: 'https://101.www.impactmojo.in/IMQualLab',
    isPremium: true,
    icon: PenTool,
    color: 'purple',
    prompt: 'Advanced qualitative research analysis prompt...',
    systemMessage: 'You are an expert in qualitative research analysis...',
    exampleInput: 'Example input for IM QualLab...'
  },
  {
    id: 'im-stats-assist',
    title: 'IM StatsAssist',
    description: 'Statistical analysis assistant for complex data interpretation',
    url: 'https://101.www.impactmojo.in/IMStatsAssist',
    isPremium: true,
    icon: BarChart,
    color: 'teal',
    prompt: 'Statistical analysis assistance prompt...',
    systemMessage: 'You are an expert statistician specializing in development research...',
    exampleInput: 'Example input for IM StatsAssist...'
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
  const { user, signOut } = useAuth();
  const { currentPage, setCurrentPage, darkMode, setDarkMode } = usePage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  const navItems = [
    { id: 'home', label: 'Home', icon: null },
    { id: 'courses', label: 'Courses', icon: null },
    { id: 'labs', label: 'Labs', icon: null },
    { id: 'handouts', label: 'Resources', icon: null },
    { id: 'ai-tools', label: 'AI Tools', icon: null },
    { id: 'premium-tools', label: 'Premium Tools', icon: null, premium: true },
    { id: 'dashboard', label: 'Dashboard', icon: null },
    { id: 'about', label: 'About', icon: null },
    { id: 'contact', label: 'Contact', icon: null },
  ];

  return (
    <nav className="bg-white dark:bg-gray-800 shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <button
              onClick={() => setCurrentPage('home')}
              className="text-2xl font-bold text-blue-600 dark:text-blue-400"
            >
              ImpactMojo
            </button>
          </div>
          
          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-4">
            {navItems.map(item => {
              // Skip premium tools if not logged in
              if (item.premium && !user) return null;
              
              return (
                <button
                  key={item.id}
                  onClick={() => setCurrentPage(item.id)}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center ${
                    currentPage === item.id
                      ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-200'
                      : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
                  }`}
                >
                  {item.label}
                  {item.premium && <Crown className="w-4 h-4 ml-1 text-yellow-500" />}
                </button>
              );
            })}
            
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              aria-label="Toggle dark mode"
            >
              {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
            </button>
            
            {user && (
              <button
                onClick={signOut}
                className="flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900 transition-colors"
              >
                <LogOut className="w-4 h-4" />
                <span>Sign Out</span>
              </button>
            )}
          </div>
          
          {/* Mobile menu button */}
          <div className="md:hidden flex items-center">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
              aria-label="Toggle menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
        
        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <div className="md:hidden pb-4">
            <div className="flex flex-col space-y-2">
              {navItems.map(item => {
                if (item.premium && !user) return null;
                
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      setCurrentPage(item.id);
                      setMobileMenuOpen(false);
                    }}
                    className={`px-3 py-2 rounded-md text-sm font-medium text-left transition-colors flex items-center ${
                      currentPage === item.id
                        ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-200'
                        : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
                    }`}
                  >
                    {item.label}
                    {item.premium && <Crown className="w-4 h-4 ml-1 text-yellow-500" />}
                  </button>
                );
              })}
              
              <div className="flex items-center justify-between pt-2 border-t border-gray-200 dark:border-gray-700">
                <button
                  onClick={() => setDarkMode(!darkMode)}
                  className="flex items-center space-x-2 p-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
                  <span>{darkMode ? 'Light Mode' : 'Dark Mode'}</span>
                </button>
                
                {user && (
                  <button
                    onClick={signOut}
                    className="flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900 transition-colors"
                  >
                    <LogOut className="w-4 h-4" />
                    <span>Sign Out</span>
                  </button>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

// Home Page Component
const HomePage = () => {
  const { user, signInWithGoogle } = useAuth();
  const { setCurrentPage } = usePage();
  
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-600 via-purple-600 to-indigo-700">
      {/* Hero Section */}
      <section className="relative px-4 py-20 text-center text-white">
        <div className="max-w-5xl mx-auto">
          <h1 className="text-4xl md:text-6xl font-bold mb-6 animate-fade-in">
            ImpactMojo
          </h1>
          <p className="text-xl md:text-2xl mb-8 opacity-90">
            Your Gateway to Development Knowledge
          </p>
          <p className="text-lg mb-12 max-w-3xl mx-auto opacity-80">
            Explore 37 comprehensive courses, 10 interactive labs, and powerful AI tools designed for social impact professionals.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            {!user ? (
              <button
                onClick={signInWithGoogle}
                className="bg-white text-blue-600 px-8 py-4 rounded-lg font-medium hover:bg-gray-100 transition-colors flex items-center justify-center space-x-2 shadow-lg"
              >
                <User className="w-5 h-5" />
                <span>Sign in with Google</span>
              </button>
            ) : (
              <button
                onClick={() => setCurrentPage('dashboard')}
                className="bg-white text-blue-600 px-8 py-4 rounded-lg font-medium hover:bg-gray-100 transition-colors flex items-center justify-center space-x-2 shadow-lg"
              >
                <Target className="w-5 h-5" />
                <span>Go to Dashboard</span>
              </button>
            )}
            <button
              onClick={() => setCurrentPage('courses')}
              className="bg-transparent border-2 border-white text-white px-8 py-4 rounded-lg font-medium hover:bg-white hover:text-blue-600 transition-colors"
            >
              Explore Courses
            </button>
          </div>
        </div>
      </section>
      
      {/* Stats Section */}
      <section className="py-16 bg-white dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 p-6 rounded-xl shadow-md">
              <div className="text-3xl font-bold text-blue-600 dark:text-blue-300">37</div>
              <div className="text-gray-600 dark:text-gray-300">Courses</div>
            </div>
            <div className="bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900 dark:to-green-800 p-6 rounded-xl shadow-md">
              <div className="text-3xl font-bold text-green-600 dark:text-green-300">10</div>
              <div className="text-gray-600 dark:text-gray-300">Labs</div>
            </div>
            <div className="bg-gradient-to-br from-purple-50 to-purple-100 dark:from-purple-900 dark:to-purple-800 p-6 rounded-xl shadow-md">
              <div className="text-3xl font-bold text-purple-600 dark:text-purple-300">16</div>
              <div className="text-gray-600 dark:text-gray-300">AI Tools</div>
            </div>
            <div className="bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900 dark:to-orange-800 p-6 rounded-xl shadow-md">
              <div className="text-3xl font-bold text-orange-600 dark:text-orange-300">Free</div>
              <div className="text-gray-600 dark:text-gray-300">Forever</div>
            </div>
          </div>
        </div>
      </section>
      
      {/* Features Section */}
      <section className="py-16 bg-gray-50 dark:bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-900 dark:text-white">
            Everything You Need for Impact
          </h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white dark:bg-gray-700 p-8 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1">
              <BookOpen className="w-12 h-12 text-blue-600 dark:text-blue-400 mb-4" />
              <h3 className="text-xl font-bold mb-3 text-gray-900 dark:text-white">Comprehensive Courses</h3>
              <p className="text-gray-600 dark:text-gray-300">
                From Gender Studies to Data Analysis, explore 37 expertly crafted courses covering all aspects of development work.
              </p>
            </div>
            
            <div className="bg-white dark:bg-gray-700 p-8 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1">
              <Gamepad2 className="w-12 h-12 text-green-600 dark:text-green-400 mb-4" />
              <h3 className="text-xl font-bold mb-3 text-gray-900 dark:text-white">Interactive Labs</h3>
              <p className="text-gray-600 dark:text-gray-300">
                Practice with real-world scenarios in our 10 hands-on labs covering MLE, advocacy, community engagement, and more.
              </p>
            </div>
            
            <div className="bg-white dark:bg-gray-700 p-8 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1">
              <Sparkles className="w-12 h-12 text-purple-600 dark:text-purple-400 mb-4" />
              <h3 className="text-xl font-bold mb-3 text-gray-900 dark:text-white">AI-Powered Tools</h3>
              <p className="text-gray-600 dark:text-gray-300">
                Accelerate your work with 16 specialized AI tools for grant writing, M&E design, data visualization, and more.
              </p>
            </div>
          </div>
        </div>
      </section>
      
      {/* CTA Section */}
      <section className="py-16 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="max-w-4xl mx-auto text-center px-4">
          <h2 className="text-3xl font-bold mb-4">Ready to Make an Impact?</h2>
          <p className="text-xl mb-8 opacity-90">
            Join thousands of development professionals advancing their skills
          </p>
          <button
            onClick={() => setCurrentPage('courses')}
            className="bg-white text-blue-600 px-8 py-3 rounded-lg font-medium hover:bg-gray-100 transition-colors inline-flex items-center space-x-2 shadow-lg"
          >
            <span>Start Learning Now</span>
            <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </section>
    </div>
  );
};

// Course Card Component
const CourseCard = ({ course, isBookmarked, onBookmark }) => {
  const handleCourseAccess = () => {
    if (course.isPremium) {
      alert('This is a premium course. Please contact us for access.');
    } else {
      window.open(course.url, '_blank');
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1 h-full flex flex-col">
      <div className="p-6 flex-grow">
        <div className="flex justify-between items-start mb-4">
          <span className="text-sm font-bold text-blue-600 dark:text-blue-400">
            {course.id}
          </span>
          <div className="flex space-x-2">
            {course.isPremium && (
              <Shield className="w-5 h-5 text-yellow-500" title="Premium Course" />
            )}
            {onBookmark && (
              <button
                onClick={() => onBookmark(course.id)}
                className="hover:scale-110 transition-transform"
                aria-label={isBookmarked ? "Remove bookmark" : "Add bookmark"}
              >
                <Bookmark 
                  className={`w-5 h-5 ${isBookmarked ? 'fill-yellow-400 text-yellow-400' : 'text-gray-400'}`} 
                />
              </button>
            )}
          </div>
        </div>
        
        <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">
          {course.title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-300 mb-4 line-clamp-3">
          {course.description}
        </p>
        
        {course.quote && (
          <blockquote className="text-sm italic text-blue-600 dark:text-blue-400 mb-4 border-l-2 border-blue-200 pl-3">
            {course.quote}
          </blockquote>
        )}
        
        <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
          <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded">
            {course.track}
          </span>
          <span className="flex items-center">
            <Clock className="w-4 h-4 mr-1" />
            {course.duration}
          </span>
        </div>
      </div>
      
      <div className="p-6 pt-0 mt-auto">
        <button
          onClick={handleCourseAccess}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
        >
          <ExternalLink className="w-4 h-4" />
          <span>Start Course</span>
        </button>
      </div>
    </div>
  );
};

// Courses Page Component
const CoursesPage = () => {
  const { bookmarks, toggleBookmark } = useAuth();
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('all');
  const [selectedLevel, setSelectedLevel] = useState('all');
  
  const filteredCourses = courseData.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         course.description.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesTrack = selectedTrack === 'all' || course.track === selectedTrack;
    const matchesLevel = selectedLevel === 'all' || course.level === selectedLevel;
    return matchesSearch && matchesTrack && matchesLevel;
  });
  
  const uniqueTracks = [...new Set(courseData.map(course => course.track))];
  const uniqueLevels = [...new Set(courseData.map(course => course.level))];
  
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Course Catalog
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Explore our comprehensive collection of 37 development courses
          </p>
        </div>
        
        {/* Search and Filters */}
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow-md">
          <div className="grid md:grid-cols-3 gap-4">
            <div>
              <label htmlFor="search" className="block text-sm font-medium mb-2">Search</label>
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  id="search"
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Search courses..."
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
            </div>
            
            <div>
              <label htmlFor="track" className="block text-sm font-medium mb-2">Track</label>
              <select
                id="track"
                value={selectedTrack}
                onChange={(e) => setSelectedTrack(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
              >
                <option value="all">All Tracks</option>
                {uniqueTracks.map(track => (
                  <option key={track} value={track}>{track}</option>
                ))}
              </select>
            </div>
            
            <div>
              <label htmlFor="level" className="block text-sm font-medium mb-2">Level</label>
              <select
                id="level"
                value={selectedLevel}
                onChange={(e) => setSelectedLevel(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
              >
                <option value="all">All Levels</option>
                {uniqueLevels.map(level => (
                  <option key={level} value={level}>{level}</option>
                ))}
              </select>
            </div>
          </div>
        </div>
        
        {/* Course Grid */}
        {filteredCourses.length > 0 ? (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredCourses.map(course => (
              <CourseCard
                key={course.id}
                course={course}
                isBookmarked={bookmarks.includes(course.id)}
                onBookmark={toggleBookmark}
              />
            ))}
          </div>
        ) : (
          <div className="text-center py-12 bg-white dark:bg-gray-800 rounded-lg shadow-md">
            <Search className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
              No courses found
            </h3>
            <p className="text-gray-600 dark:text-gray-300">
              Try adjusting your search criteria
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

// Labs Page Component
const LabsPage = () => {
  const handleLabAccess = (lab) => {
    if (lab.status === 'Available') {
      window.open(lab.url, '_blank');
    } else {
      alert(`${lab.title} - Coming Soon!`);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Interactive Labs
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            10 hands-on labs for real-world practice and skill development
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {labsData.map(lab => (
            <div key={lab.id} className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1 h-full flex flex-col">
              <div className="p-6 flex-grow">
                <div className="flex justify-between items-start mb-4">
                  <span className="text-sm font-bold text-green-600 dark:text-green-400">
                    {lab.id}
                  </span>
                  <span className={`px-2 py-1 rounded-lg text-xs font-medium ${
                    lab.status === 'Available' 
                      ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                      : 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300'
                  }`}>
                    {lab.status}
                  </span>
                </div>
                
                <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">
                  {lab.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 mb-4">
                  {lab.description}
                </p>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 px-2 py-1 rounded">
                    {lab.category}
                  </span>
                  <span className="flex items-center">
                    <Clock className="w-4 h-4 mr-1" />
                    {lab.duration} min
                  </span>
                </div>
              </div>
              
              <div className="p-6 pt-0 mt-auto">
                <button
                  onClick={() => handleLabAccess(lab)}
                  className={`w-full font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2 ${
                    lab.status === 'Available'
                      ? 'bg-green-600 hover:bg-green-700 text-white'
                      : 'bg-gray-300 dark:bg-gray-600 text-gray-500 dark:text-gray-400 cursor-not-allowed'
                  }`}
                  disabled={lab.status !== 'Available'}
                >
                  <PlayCircle className="w-4 h-4" />
                  <span>{lab.status === 'Available' ? 'Launch Lab' : 'Coming Soon'}</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Handouts Page Component
const HandoutsPage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-600 via-purple-600 to-blue-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        {/* Header */}
        <div className="bg-white/95 backdrop-blur-md rounded-xl p-8 mb-8 shadow-2xl">
          <div className="mb-6">
            <button
              onClick={() => window.history.back()}
              className="text-blue-600 hover:text-blue-800 font-medium text-sm mb-4 flex items-center"
            >
              <ArrowLeft className="w-4 h-4 mr-1" /> Back to ImpactMojo
            </button>
          </div>
          
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Educational Handouts
          </h1>
          <div className="text-xl text-gray-600 mb-6">
            Structured Learning Pathways for Development Education
          </div>
          
          <div className="bg-gradient-to-r from-blue-50 to-purple-50 p-6 rounded-xl border-l-4 border-blue-500 mb-6">
            <p className="text-gray-700 leading-relaxed">
              <strong>Curriculum-ready teaching materials</strong> organized into progressive learning pathways for educators working in development studies, public policy, and social research across South Asian contexts. Each pathway builds systematically from foundational concepts to advanced applications.
            </p>
          </div>
          
          {/* Stats Banner */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-white rounded-lg p-4 text-center shadow-md">
              <div className="text-3xl font-bold text-blue-600">37</div>
              <div className="text-sm text-gray-600">Courses</div>
            </div>
            <div className="bg-white rounded-lg p-4 text-center shadow-md">
              <div className="text-3xl font-bold text-green-600">4</div>
              <div className="text-sm text-gray-600">Learning Tracks</div>
            </div>
            <div className="bg-white rounded-lg p-4 text-center shadow-md">
              <div className="text-3xl font-bold text-purple-600">100+</div>
              <div className="text-sm text-gray-600">Resources</div>
            </div>
            <div className="bg-white rounded-lg p-4 text-center shadow-md">
              <div className="text-3xl font-bold text-orange-600">Free</div>
              <div className="text-sm text-gray-600">Open Access</div>
            </div>
          </div>
        </div>
        
        {/* Main Pathways */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-white mb-6">Core Learning Pathways</h2>
          <div className="grid md:grid-cols-2 gap-6">
            
            {/* Data Analysis Track */}
            <div className="bg-white/95 backdrop-blur-md rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all">
              <div className="flex items-center mb-4">
                <BarChart className="w-8 h-8 text-blue-600 mr-3" />
                <h3 className="text-xl font-bold text-gray-900">
                  <a href="/extras/Handouts/Data%20Analysis%20Track/" className="hover:text-blue-600 transition-colors">
                    Data Analysis Track
                  </a>
                </h3>
              </div>
              <p className="text-gray-600 mb-4">
                From basic data literacy to advanced multivariate analysis. Master R, Python, Excel, and statistical methods for development research.
              </p>
              <div className="flex flex-wrap gap-2 mb-4">
                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">Data Literacy</span>
                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">Statistics</span>
                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">Visualization</span>
              </div>
              <div className="bg-gray-50 rounded-lg p-4">
                <h4 className="font-semibold text-gray-700 mb-2">📁 Includes:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Bivariate Analysis</li>
                  <li>• Data Analysis - Examples and Templates</li>
                  <li>• Data Literacy</li>
                  <li>• Econometrics</li>
                  <li>• EDA</li>
                  <li>• Multivariate Analysis</li>
                </ul>
              </div>
            </div>
            
            {/* Gender Studies Track */}
            <div className="bg-white/95 backdrop-blur-md rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all">
              <div className="flex items-center mb-4">
                <Users className="w-8 h-8 text-purple-600 mr-3" />
                <h3 className="text-xl font-bold text-gray-900">
                  <a href="/extras/Handouts/Gender%20Studies%20Track/" className="hover:text-purple-600 transition-colors">
                    Gender Studies Track
                  </a>
                </h3>
              </div>
              <p className="text-gray-600 mb-4">
                Comprehensive frameworks for gender analysis, women's economic empowerment, and inclusive development practices.
              </p>
              <div className="flex flex-wrap gap-2 mb-4">
                <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">Care Economy</span>
                <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">Data Feminism</span>
                <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">WEE</span>
              </div>
              <div className="bg-gray-50 rounded-lg p-4">
                <h4 className="font-semibold text-gray-700 mb-2">📁 Includes:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Care Economy</li>
                  <li>• Data Feminism</li>
                  <li>• Gender Studies</li>
                  <li>• Women's Economic Empowerment</li>
                </ul>
              </div>
            </div>
            
            {/* Policy and Economics Track */}
            <div className="bg-white/95 backdrop-blur-md rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all">
              <div className="flex items-center mb-4">
                <TrendingUp className="w-8 h-8 text-green-600 mr-3" />
                <h3 className="text-xl font-bold text-gray-900">
                  <a href="/extras/Handouts/Policy%20and%20Economics%20Track/" className="hover:text-green-600 transition-colors">
                    Policy and Economics Track
                  </a>
                </h3>
              </div>
              <p className="text-gray-600 mb-4">
                Development economics, poverty analysis, livelihood frameworks, and social protection systems for policy practitioners.
              </p>
              <div className="flex flex-wrap gap-2 mb-4">
                <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">Development</span>
                <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">Poverty</span>
                <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">Policy</span>
              </div>
              <div className="bg-gray-50 rounded-lg p-4">
                <h4 className="font-semibold text-gray-700 mb-2">📁 Includes:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Development Economics</li>
                  <li>• Livelihoods</li>
                  <li>• Marginalised Identities</li>
                  <li>• Policy Tracking</li>
                  <li>• Political Economy</li>
                  <li>• Post Truth Politics</li>
                  <li>• Poverty and Inequality</li>
                  <li>• Social Safety Nets</li>
                </ul>
              </div>
            </div>
            
            {/* Research Methods Track */}
            <div className="bg-white/95 backdrop-blur-md rounded-xl p-6 shadow-xl hover:shadow-2xl transition-all">
              <div className="flex items-center mb-4">
                <BookOpen className="w-8 h-8 text-orange-600 mr-3" />
                <h3 className="text-xl font-bold text-gray-900">
                  <a href="/extras/Handouts/Quick%20Reference%20Cards/" className="hover:text-orange-600 transition-colors">
                    Research Methods Track
                  </a>
                </h3>
              </div>
              <p className="text-gray-600 mb-4">
                Essential research design, ethics, qualitative methods, and evaluation frameworks for rigorous field research.
              </p>
              <div className="flex flex-wrap gap-2 mb-4">
                <span className="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-sm">Ethics</span>
                <span className="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-sm">Methods</span>
                <span className="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-sm">Evaluation</span>
              </div>
              <div className="bg-gray-50 rounded-lg p-4">
                <h4 className="font-semibold text-gray-700 mb-2">📁 Quick Reference Components:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Research Ethics</li>
                  <li>• Qualitative Research</li>
                  <li>• MLE (Monitoring, Learning & Evaluation)</li>
                  <li>• Assumptions Checklist</li>
                  <li>• Research Design - Resources</li>
                  <li>• Research Design Worksheet</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        
        {/* Additional Resources Section */}
        <div className="bg-white/95 backdrop-blur-md rounded-xl p-8 shadow-2xl">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Additional Resources & Thematic Areas</h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Thematic Areas */}
            <div className="bg-gray-50 rounded-lg p-6 border-l-4 border-gray-400 hover:border-blue-500 transition-all">
              <a href="/extras/Handouts/Thematic%20Areas/" className="text-lg font-semibold text-gray-800 hover:text-blue-600 transition-colors">
                🌍 Thematic Areas
              </a>
              <p className="text-sm text-gray-600 mt-2">
                Specialized topic collections including:
              </p>
              <ul className="text-xs text-gray-500 mt-2 space-y-1">
                <li>• Climate Change - Science, Mitigation, Adaptation, Resilience and Futures</li>
                <li>• Constitution, Law, Justice and Jurisprudence</li>
                <li>• Digital Development Ethics</li>
                <li>• Health and Wellbeing</li>
                <li>• Justice and Governance</li>
                <li>• South Asia Region</li>
              </ul>
            </div>
            
            {/* Cross-Cutting Resources */}
            <div className="bg-gray-50 rounded-lg p-6 border-l-4 border-gray-400 hover:border-purple-500 transition-all">
              <a href="/extras/Handouts/Cross%20Cutting%20Resources/" className="text-lg font-semibold text-gray-800 hover:text-purple-600 transition-colors">
                🔗 Cross-Cutting Resources
              </a>
              <p className="text-sm text-gray-600 mt-2">
                Essential tools that support all learning tracks:
              </p>
              <ul className="text-xs text-gray-500 mt-2 space-y-1">
                <li>• Case Studies</li>
                <li>• Communications</li>
                <li>• Local Application Worksheet</li>
                <li>• Software Tools Guide</li>
              </ul>
            </div>
            
            {/* Quick Reference Cards */}
            <div className="bg-gray-50 rounded-lg p-6 border-l-4 border-gray-400 hover:border-green-500 transition-all">
              <a href="/extras/Handouts/Quick%20Reference%20Cards/" className="text-lg font-semibold text-gray-800 hover:text-green-600 transition-colors">
                ⚡ Quick Reference Cards
              </a>
              <p className="text-sm text-gray-600 mt-2">
                Condensed reference materials for quick lookup during workshops, research, or fieldwork. Perfect for printing and desk reference.
              </p>
            </div>
            
            {/* Education & Pedagogy */}
            <div className="bg-gray-50 rounded-lg p-6 border-l-4 border-gray-400 hover:border-orange-500 transition-all">
              <a href="/extras/Handouts/Education%20and%20Pedagogy/" className="text-lg font-semibold text-gray-800 hover:text-orange-600 transition-colors">
                📚 Education & Pedagogy
              </a>
              <p className="text-sm text-gray-600 mt-2">
                Specialized resources for educators focusing on learning theory, curriculum design, and effective teaching practices in development education.
              </p>
            </div>
          </div>
        </div>
        
        {/* Footer */}
        <div className="bg-white/95 backdrop-blur-md rounded-xl p-8 mt-8 text-center shadow-xl">
          <p className="text-lg font-semibold text-gray-900 mb-2">Open Educational Resources</p>
          <p className="text-gray-600 mb-4">All materials are licensed under CC BY-NC-SA 4.0 and available for adaptation.</p>
          <p className="text-gray-600 mb-4">Perfect for university instructors, training coordinators, and workshop facilitators.</p>
          <p className="text-blue-600 font-medium italic">ImpactMojo is provided completely free through the generous support of Pinpoint Ventures.</p>
          <div className="mt-6 p-4 bg-blue-50 rounded-lg">
            <p className="text-sm text-gray-700">
              <strong>How to Use:</strong> Click any pathway or resource to explore materials. 
              Use your browser's print function (Ctrl+P or Cmd+P) to save handouts as PDFs.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

// AI Tools Page Component
const AIToolsPage = () => {
  const [selectedTool, setSelectedTool] = useState(null);
  const [userInput, setUserInput] = useState('');
  const [toolOutput, setToolOutput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  
  const handleGenerateAI = async () => {
    if (!selectedTool || !userInput.trim()) {
      alert('Please select a tool and provide input');
      return;
    }
    
    setIsProcessing(true);
    
    // Simulate AI processing
    setTimeout(() => {
      setToolOutput(`Generated ${selectedTool.title} Output:\n\nBased on your input, here's a comprehensive response tailored to your needs...\n\n[This is a demo. In production, this would connect to an AI service to generate actual content based on the tool's system message and your input.]`);
      setIsProcessing(false);
    }, 2000);
  };
  
  const handleCopyOutput = () => {
    navigator.clipboard.writeText(toolOutput);
    alert('Output copied to clipboard!');
  };
  
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            AI-Powered Development Tools
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            16 specialized AI tools to accelerate your development work
          </p>
        </div>
        
        {/* Tool Selection Grid */}
        <div className="grid md:grid-cols-3 lg:grid-cols-4 gap-4 mb-8">
          {aiToolsData.map(tool => {
            const Icon = tool.icon;
            return (
              <button
                key={tool.id}
                onClick={() => {
                  setSelectedTool(tool);
                  setUserInput('');
                  setToolOutput('');
                }}
                className={`p-4 rounded-lg border-2 transition-all text-left ${
                  selectedTool?.id === tool.id
                    ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20'
                    : 'border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600'
                }`}
              >
                <Icon className={`w-6 h-6 mb-2 ${
                  selectedTool?.id === tool.id ? 'text-blue-600' : 'text-gray-500'
                }`} />
                <h3 className="font-semibold text-sm text-gray-900 dark:text-white">
                  {tool.title}
                </h3>
              </button>
            );
          })}
        </div>
        
        {/* Selected Tool Interface */}
        {selectedTool && (
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
            <div className="mb-6">
              <div className="flex items-center mb-4">
                {React.createElement(selectedTool.icon, { 
                  className: `w-8 h-8 text-${selectedTool.color}-600 mr-3` 
                })}
                <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                  {selectedTool.title}
                </h2>
              </div>
              <p className="text-gray-600 dark:text-gray-300">
                {selectedTool.description}
              </p>
            </div>
            
            {/* Example Input */}
            <div className="mb-6 p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
              <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">
                Example Input:
              </h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                {selectedTool.exampleInput}
              </p>
            </div>
            
            {/* User Input */}
            <div className="mb-6">
              <label htmlFor="userInput" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Your Input:
              </label>
              <textarea
                id="userInput"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                rows={10}
                className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="Enter your specific requirements here..."
              />
            </div>
            
            {/* Action Buttons */}
            <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 mb-6">
              <button
                onClick={handleGenerateAI}
                disabled={isProcessing || !userInput.trim()}
                className={`flex items-center justify-center space-x-2 px-6 py-3 rounded-lg font-medium transition-colors ${
                  isProcessing || !userInput.trim()
                    ? 'bg-gray-300 dark:bg-gray-600 text-gray-500 dark:text-gray-400 cursor-not-allowed'
                    : 'bg-blue-600 hover:bg-blue-700 text-white'
                }`}
              >
                {isProcessing ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    <span>Processing...</span>
                  </>
                ) : (
                  <>
                    <Wand2 className="w-5 h-5" />
                    <span>Generate with AI</span>
                  </>
                )}
              </button>
              <button
                onClick={() => {
                  setUserInput('');
                  setToolOutput('');
                }}
                className="px-6 py-3 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
              >
                Clear All
              </button>
            </div>
            
            {/* Output Display */}
            {toolOutput && (
              <div className="mt-8 border-t pt-6">
                <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-4">
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white flex items-center mb-2 sm:mb-0">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-2" />
                    Generated Result
                  </h3>
                  <button
                    onClick={handleCopyOutput}
                    className="flex items-center justify-center space-x-2 text-blue-600 dark:text-blue-400 hover:underline text-sm"
                  >
                    <Copy className="w-4 h-4" />
                    <span>Copy</span>
                  </button>
                </div>
                <div className="bg-gray-50 dark:bg-gray-700 p-6 rounded-lg border">
                  <div className="prose dark:prose-invert max-w-none">
                    <pre className="whitespace-pre-wrap text-sm text-gray-700 dark:text-gray-300 font-normal leading-relaxed">
                      {toolOutput}
                    </pre>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

// Premium Tools Page Component
const PremiumToolsPage = () => {
  const { user } = useAuth();
  const premiumTools = aiToolsData.filter(tool => tool.isPremium);
  
  if (!user) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-4">
            Premium Access Required
          </h2>
          <p className="text-gray-600 dark:text-gray-300 mb-8">
            Please sign in to access premium tools
          </p>
          <button
            onClick={() => setCurrentPage('home')}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium"
          >
            Sign In
          </button>
        </div>
      </div>
    );
  }
  
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4 flex items-center">
            Premium Tools
            <Crown className="w-6 h-6 ml-3 text-yellow-500" />
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Advanced tools for professional development work
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 gap-8">
          {premiumTools.map(tool => (
            <div key={tool.id} className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1 h-full flex flex-col">
              <div className="p-6 flex-grow">
                <div className="flex justify-between items-start mb-4">
                  <span className="text-sm font-bold text-purple-600 dark:text-purple-400">
                    {tool.id}
                  </span>
                  <div className="flex items-center space-x-2">
                    <Crown className="w-5 h-5 text-yellow-500" title="Premium Tool" />
                    <Star className="w-5 h-5 text-yellow-500" title="Premium" />
                  </div>
                </div>
                
                <div className="flex items-center mb-4">
                  {React.createElement(tool.icon, { 
                    className: `w-10 h-10 text-${tool.color}-600 mr-3` 
                  })}
                  <h3 className="text-xl font-bold text-gray-900 dark:text-white">
                    {tool.title}
                  </h3>
                </div>
                
                <p className="text-gray-600 dark:text-gray-300 mb-6">
                  {tool.description}
                </p>
                
                <div className="mt-auto">
                  <button
                    onClick={() => window.open(tool.url, '_blank')}
                    className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-medium py-3 px-4 rounded-lg transition-all transform hover:scale-[1.02] flex items-center justify-center space-x-2 shadow-lg"
                  >
                    <ExternalLink className="w-5 h-5" />
                    <span>Access Premium Tool</span>
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

// Dashboard Page Component
const DashboardPage = () => {
  const { user, bookmarks, signOut } = useAuth();
  const { setCurrentPage } = usePage();
  
  const bookmarkedCourses = courseData.filter(course => bookmarks.includes(course.id));
  
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-2">
            Dashboard
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Welcome back, {user?.displayName || 'User'}!
          </p>
        </div>
        
        {/* User Profile Card */}
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 mb-8">
          <div className="flex items-center mb-6">
            {user?.photoURL ? (
              <img 
                src={user.photoURL} 
                alt={user.displayName} 
                className="w-16 h-16 rounded-full mr-4"
              />
            ) : (
              <div className="w-16 h-16 rounded-full bg-blue-100 dark:bg-blue-900 flex items-center justify-center mr-4">
                <User className="w-8 h-8 text-blue-600 dark:text-blue-400" />
              </div>
            )}
            <div>
              <h2 className="text-xl font-bold text-gray-900 dark:text-white">
                {user?.displayName || 'User'}
              </h2>
              <p className="text-gray-600 dark:text-gray-300">
                {user?.email}
              </p>
            </div>
          </div>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-blue-50 dark:bg-blue-900/30 p-4 rounded-lg text-center">
              <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                {bookmarks.length}
              </div>
              <div className="text-sm text-gray-600 dark:text-gray-300">Bookmarks</div>
            </div>
            <div className="bg-green-50 dark:bg-green-900/30 p-4 rounded-lg text-center">
              <div className="text-2xl font-bold text-green-600 dark:text-green-400">
                {bookmarkedCourses.length}
              </div>
              <div className="text-sm text-gray-600 dark:text-gray-300">Courses</div>
            </div>
            <div className="bg-purple-50 dark:bg-purple-900/30 p-4 rounded-lg text-center">
              <div className="text-2xl font-bold text-purple-600 dark:text-purple-400">
                16
              </div>
              <div className="text-sm text-gray-600 dark:text-gray-300">AI Tools</div>
            </div>
            <div className="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-lg text-center">
              <div className="text-2xl font-bold text-orange-600 dark:text-orange-400">
                10
              </div>
              <div className="text-sm text-gray-600 dark:text-gray-300">Labs</div>
            </div>
          </div>
          
          <button
            onClick={signOut}
            className="flex items-center space-x-2 px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors"
          >
            <LogOut className="w-4 h-4" />
            <span>Sign Out</span>
          </button>
        </div>
        
        {/* Premium Tools Section */}
        <div className="mb-8">
          <div className="flex items-center mb-4">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Premium Tools</h2>
            <Crown className="w-5 h-5 ml-2 text-yellow-500" />
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            {aiToolsData
              .filter(tool => tool.isPremium)
              .map(tool => (
                <div key={tool.id} className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1 h-full flex flex-col">
                  <div className="p-6 flex-grow">
                    <div className="flex justify-between items-start mb-4">
                      <span className="text-sm font-bold text-purple-600 dark:text-purple-400">
                        {tool.id}
                      </span>
                      <div className="flex items-center space-x-2">
                        <Crown className="w-5 h-5 text-yellow-500" title="Premium Tool" />
                        <Star className="w-5 h-5 text-yellow-500" title="Premium" />
                      </div>
                    </div>
                    
                    <div className="flex items-center mb-4">
                      {React.createElement(tool.icon, { 
                        className: `w-10 h-10 text-${tool.color}-600 mr-3` 
                      })}
                      <h3 className="text-xl font-bold text-gray-900 dark:text-white">
                        {tool.title}
                      </h3>
                    </div>
                    
                    <p className="text-gray-600 dark:text-gray-300 mb-6">
                      {tool.description}
                    </p>
                    
                    <div className="mt-auto">
                      <button
                        onClick={() => window.open(tool.url, '_blank')}
                        className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-medium py-3 px-4 rounded-lg transition-all transform hover:scale-[1.02] flex items-center justify-center space-x-2 shadow-lg"
                      >
                        <ExternalLink className="w-5 h-5" />
                        <span>Access Premium Tool</span>
                      </button>
                    </div>
                  </div>
                </div>
              ))}
          </div>
        </div>
        
        {/* Bookmarked Courses */}
        {bookmarkedCourses.length > 0 && (
          <div className="mb-8">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
              Your Bookmarked Courses
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {bookmarkedCourses.map(course => (
                <CourseCard
                  key={course.id}
                  course={course}
                  isBookmarked={true}
                />
              ))}
            </div>
          </div>
        )}
        
        {/* Quick Actions */}
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
            Quick Actions
          </h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <button
              onClick={() => setCurrentPage('courses')}
              className="flex flex-col items-center justify-center p-4 bg-blue-50 dark:bg-blue-900/30 rounded-lg hover:bg-blue-100 dark:hover:bg-blue-900/50 transition-colors"
            >
              <BookOpen className="w-8 h-8 text-blue-600 dark:text-blue-400 mb-2" />
              <span className="text-sm text-gray-700 dark:text-gray-300">Browse Courses</span>
            </button>
            <button
              onClick={() => setCurrentPage('labs')}
              className="flex flex-col items-center justify-center p-4 bg-green-50 dark:bg-green-900/30 rounded-lg hover:bg-green-100 dark:hover:bg-green-900/50 transition-colors"
            >
              <Gamepad2 className="w-8 h-8 text-green-600 dark:text-green-400 mb-2" />
              <span className="text-sm text-gray-700 dark:text-gray-300">Explore Labs</span>
            </button>
            <button
              onClick={() => setCurrentPage('ai-tools')}
              className="flex flex-col items-center justify-center p-4 bg-purple-50 dark:bg-purple-900/30 rounded-lg hover:bg-purple-100 dark:hover:bg-purple-900/50 transition-colors"
            >
              <Sparkles className="w-8 h-8 text-purple-600 dark:text-purple-400 mb-2" />
              <span className="text-sm text-gray-700 dark:text-gray-300">Try AI Tools</span>
            </button>
            <button
              onClick={() => setCurrentPage('handouts')}
              className="flex flex-col items-center justify-center p-4 bg-orange-50 dark:bg-orange-900/30 rounded-lg hover:bg-orange-100 dark:hover:bg-orange-900/50 transition-colors"
            >
              <FileText className="w-8 h-8 text-orange-600 dark:text-orange-400 mb-2" />
              <span className="text-sm text-gray-700 dark:text-gray-300">Resources</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

// About Page Component
const AboutPage = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            About ImpactMojo
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Empowering development professionals with knowledge and tools
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 mb-8">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">Our Mission</h2>
          <p className="text-gray-600 dark:text-gray-300 mb-6">
            ImpactMojo is dedicated to providing free, high-quality educational resources and tools for development professionals, researchers, and practitioners worldwide. We believe that knowledge should be accessible to everyone working to create positive social change.
          </p>
          
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">What We Offer</h2>
          <ul className="space-y-3 text-gray-600 dark:text-gray-300 mb-6">
            <li className="flex items-start">
              <CheckCircle className="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
              <span>37 comprehensive courses covering all aspects of development work</span>
            </li>
            <li className="flex items-start">
              <CheckCircle className="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
              <span>10 interactive labs for hands-on learning and practice</span>
            </li>
            <li className="flex items-start">
              <CheckCircle className="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
              <span>16 AI-powered tools to accelerate your development work</span>
            </li>
            <li className="flex items-start">
              <CheckCircle className="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
              <span>Extensive library of educational handouts and resources</span>
            </li>
          </ul>
          
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">Our Approach</h2>
          <p className="text-gray-600 dark:text-gray-300 mb-6">
            We combine academic rigor with practical application, ensuring that our courses and tools are both theoretically sound and immediately useful in real-world settings. Our content is developed by experts in the field and continuously updated to reflect the latest research and best practices.
          </p>
          
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">Our Team</h2>
          <p className="text-gray-600 dark:text-gray-300">
            ImpactMojo is brought to you by a team of passionate development professionals, educators, and technologists committed to making knowledge accessible and actionable. We are supported by the generous contributions of Pinpoint Ventures.
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">Contact Us</h2>
          <p className="text-gray-600 dark:text-gray-300 mb-6">
            Have questions, feedback, or suggestions? We'd love to hear from you!
          </p>
          
          <div className="grid md:grid-cols-2 gap-6">
            <div className="flex items-start">
              <Mail className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
              <div>
                <h3 className="font-semibold text-gray-900 dark:text-white">Email</h3>
                <p className="text-gray-600 dark:text-gray-300">hello@impactmojo.in</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <Globe className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
              <div>
                <h3 className="font-semibold text-gray-900 dark:text-white">Website</h3>
                <p className="text-gray-600 dark:text-gray-300">www.impactmojo.in</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <Twitter className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
              <div>
                <h3 className="font-semibold text-gray-900 dark:text-white">Twitter</h3>
                <p className="text-gray-600 dark:text-gray-300">@impactmojo</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <Linkedin className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
              <div>
                <h3 className="font-semibold text-gray-900 dark:text-white">LinkedIn</h3>
                <p className="text-gray-600 dark:text-gray-300">ImpactMojo</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Contact Page Component
const ContactPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitSuccess, setSubmitSuccess] = useState(false);
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    setTimeout(() => {
      setIsSubmitting(false);
      setSubmitSuccess(true);
      setFormData({
        name: '',
        email: '',
        subject: '',
        message: ''
      });
    }, 1500);
  };
  
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Contact Us
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            We'd love to hear from you
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 gap-8">
          {/* Contact Form */}
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
              Send us a message
            </h2>
            
            {submitSuccess ? (
              <div className="bg-green-50 dark:bg-green-900/30 border border-green-200 dark:border-green-800 rounded-lg p-4 mb-6">
                <div className="flex items-center">
                  <CheckCircle className="w-5 h-5 text-green-500 mr-2" />
                  <span className="text-green-700 dark:text-green-300 font-medium">
                    Thank you! Your message has been sent successfully.
                  </span>
                </div>
              </div>
            ) : (
              <form onSubmit={handleSubmit}>
                <div className="mb-4">
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                    Name
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div className="mb-4">
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                    Email
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div className="mb-4">
                  <label htmlFor="subject" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                    Subject
                  </label>
                  <input
                    type="text"
                    id="subject"
                    name="subject"
                    value={formData.subject}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div className="mb-6">
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                    Message
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    required
                    rows={5}
                    className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  ></textarea>
                </div>
                
                <button
                  type="submit"
                  disabled={isSubmitting}
                  className={`w-full py-3 px-4 rounded-lg font-medium transition-colors ${
                    isSubmitting
                      ? 'bg-blue-400 cursor-not-allowed'
                      : 'bg-blue-600 hover:bg-blue-700'
                  } text-white`}
                >
                  {isSubmitting ? 'Sending...' : 'Send Message'}
                </button>
              </form>
            )}
          </div>
          
          {/* Contact Information */}
          <div>
            <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 mb-8">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                Get in touch
              </h2>
              
              <div className="space-y-4">
                <div className="flex items-start">
                  <Mail className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
                  <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white">Email</h3>
                    <p className="text-gray-600 dark:text-gray-300">hello@impactmojo.in</p>
                  </div>
                </div>
                
                <div className="flex items-start">
                  <Phone className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
                  <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white">Phone</h3>
                    <p className="text-gray-600 dark:text-gray-300">+91 12345 67890</p>
                  </div>
                </div>
                
                <div className="flex items-start">
                  <Globe className="w-6 h-6 text-blue-600 dark:text-blue-400 mr-3 mt-1" />
                  <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white">Website</h3>
                    <p className="text-gray-600 dark:text-gray-300">www.impactmojo.in</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                Follow us
              </h2>
              
              <div className="flex space-x-4">
                <a 
                  href="https://twitter.com/impactmojo" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="w-10 h-10 rounded-full bg-blue-100 dark:bg-blue-900 flex items-center justify-center hover:bg-blue-200 dark:hover:bg-blue-800 transition-colors"
                  aria-label="Twitter"
                >
                  <Twitter className="w-5 h-5 text-blue-600 dark:text-blue-400" />
                </a>
                
                <a 
                  href="https://linkedin.com/company/impactmojo" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="w-10 h-10 rounded-full bg-blue-100 dark:bg-blue-900 flex items-center justify-center hover:bg-blue-200 dark:hover:bg-blue-800 transition-colors"
                  aria-label="LinkedIn"
                >
                  <Linkedin className="w-5 h-5 text-blue-600 dark:text-blue-400" />
                </a>
                
                <a 
                  href="https://github.com/impactmojo" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="w-10 h-10 rounded-full bg-blue-100 dark:bg-blue-900 flex items-center justify-center hover:bg-blue-200 dark:hover:bg-blue-800 transition-colors"
                  aria-label="GitHub"
                >
                  <Github className="w-5 h-5 text-blue-600 dark:text-blue-400" />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Plausible Analytics Component
const PlausibleAnalytics = () => {
  useEffect(() => {
    // Add Plausible Analytics script
    const script = document.createElement('script');
    script.src = 'https://plausible.io/js/plausible.js';
    script.async = true;
    script.defer = true;
    script.dataset.domain = 'impactmojo.in';
    document.head.appendChild(script);
    
    return () => {
      document.head.removeChild(script);
    };
  }, []);
  
  return null;
};

// Main App Component
const App = () => {
  const { currentPage } = usePage();
  
  const renderPage = () => {
    switch(currentPage) {
      case 'home':
        return <HomePage />;
      case 'courses':
        return <CoursesPage />;
      case 'labs':
        return <LabsPage />;
      case 'handouts':
        return <HandoutsPage />;
      case 'ai-tools':
        return <AIToolsPage />;
      case 'premium-tools':
        return <PremiumToolsPage />;
      case 'dashboard':
        return <DashboardPage />;
      case 'about':
        return <AboutPage />;
      case 'contact':
        return <ContactPage />;
      default:
        return <HomePage />;
    }
  };
  
  return (
    <div className="min-h-screen flex flex-col">
      <PlausibleAnalytics />
      <Navigation />
      <main className="flex-grow">
        {renderPage()}
      </main>
      <footer className="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 py-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="mb-4 md:mb-0">
              <p className="text-gray-600 dark:text-gray-300">
                © {new Date().getFullYear()} ImpactMojo. All rights reserved.
              </p>
            </div>
            <div className="flex space-x-4">
              <a 
                href="https://twitter.com/impactmojo" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
                aria-label="Twitter"
              >
                <Twitter className="w-5 h-5" />
              </a>
              <a 
                href="https://linkedin.com/company/impactmojo" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
                aria-label="LinkedIn"
              >
                <Linkedin className="w-5 h-5" />
              </a>
              <a 
                href="https://github.com/impactmojo" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
                aria-label="GitHub"
              >
                <Github className="w-5 h-5" />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

// Wrap App with providers
const AppWithProviders = () => {
  return (
    <AuthProvider>
      <PageProvider>
        <App />
      </PageProvider>
    </AuthProvider>
  );
};

export default AppWithProviders;

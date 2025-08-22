// src/App.js - Complete ImpactMojo with ALL components and enhanced AI Tools
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
  Loader2, Copy, Sparkles, Wand2, Bot, Puzzle, Trophy, Shield, Code, ArrowLeft,
  ClipboardList, DollarSign, Megaphone, Wrench, Build
} from 'lucide-react';

// React Router imports
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useNavigate
} from 'react-router-dom';

// Firebase imports
import { initializeApp } from 'firebase/app';
import { 
  getAuth, 
  GoogleAuthProvider, 
  signInWithPopup, 
  signOut as firebaseSignOut, 
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword
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

// Theme Context
export const ThemeContext = createContext();

// ✅ REAL COURSE DATA (37 Courses) - Updated from Project Files
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
    duration: "2.5 hours",
    quote: '"Critical perspective on gender roles."',
  },
  {
    id: "C5",
    title: "Gender-based Violence Prevention 101",
    track: "Gender Studies",
    description: "Strategies for preventing and responding to gender-based violence.",
    url: "https://101.www.impactmojo.in/GBV-prevention",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Life-saving knowledge and skills."',
  },
  {
    id: "C6",
    title: "Care Work and Gender 101",
    track: "Gender Studies",
    description: "Understanding unpaid care work and its gendered dimensions.",
    url: "https://101.www.impactmojo.in/care-work",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Recognizing invisible contributions."',
  },
  {
    id: "C7",
    title: "Policy Analysis 101",
    track: "Policy Analysis",
    description: "Frameworks and tools for effective policy analysis.",
    url: "https://101.www.impactmojo.in/PolicyA",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Essential for evidence-based policy."',
  },
  {
    id: "C8",
    title: "Policy Design and Implementation 101",
    track: "Policy Analysis",
    description: "From policy design to effective implementation strategies.",
    url: "https://101.www.impactmojo.in/policy-design",
    level: "Advanced",
    duration: "3.5 hours",
    quote: '"Bridging theory and practice."',
  },
  {
    id: "C9",
    title: "Research Ethics 101",
    track: "Research Methods",
    description: "Ethical considerations in research and evaluation.",
    url: "https://101.www.impactmojo.in/ResearchEthics",
    level: "Beginner", 
    duration: "2 hours",
    quote: '"Foundation for responsible research."',
  },
  {
    id: "C10",
    title: "Behaviour Change Communication Programming 101",
    track: "Research Methods",
    description: "Designing effective behavior change interventions.",
    url: "https://101.www.impactmojo.in/BCCP",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Practical guide to behavior change."',
  },
  {
    id: "C12",
    title: "Monitoring, Evaluation, Accountability and Learning 101",
    track: "Research Methods",
    description: "MEAL frameworks and implementation strategies.",
    url: "https://101.www.impactmojo.in/MEAL",
    level: "Intermediate",
    duration: "4 hours",
    quote: '"Critical for program accountability."',
  },
  {
    id: "C13",
    title: "Visual Ethnography 101",
    track: "Research Methods",
    description: "Using visual methods in ethnographic research.",
    url: "https://101.www.impactmojo.in/VEthno",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Innovative approach to research."',
  },
  {
    id: "C14",
    title: "Development Economics 101",
    track: "Policy Analysis",
    description: "Core principles of development economics and their applications.",
    url: "https://101.www.impactmojo.in/DevEcon",
    level: "Intermediate",
    duration: "3.5 hours",
    quote: '"Foundation for economic analysis."',
  },
  {
    id: "C15",
    title: "Public Health 101",
    track: "Policy Analysis",
    description: "Fundamentals of public health systems and interventions.",
    url: "https://101.www.impactmojo.in/public-health",
    level: "Beginner",
    duration: "2.5 hours",
    quote: '"Health as a human right."',
  },
  {
    id: "C16",
    title: "Climate Change 101",
    track: "Policy Analysis",
    description: "Understanding climate science and policy responses.",
    url: "https://101.www.impactmojo.in/climate",
    level: "Beginner",
    duration: "2.5 hours",
    quote: '"Urgent knowledge for our times."',
  },
  {
    id: "C17",
    title: "Human Rights 101",
    track: "Policy Analysis",
    description: "International human rights frameworks and applications.",
    url: "https://101.www.impactmojo.in/HumanRights",
    level: "Beginner",
    duration: "2.5 hours",
    quote: '"Universal principles for dignity."',
  },
  {
    id: "C18",
    title: "Education Policy and Access 101",
    track: "Policy Analysis",
    description: "Educational systems, access, and policy frameworks.",
    url: "https://101.www.impactmojo.in/education-policy",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Education as empowerment."',
  },
  {
    id: "C19",
    title: "Econometrics 101",
    track: "Data Analysis",
    description: "Statistical methods for economic analysis.",
    url: "https://101.www.impactmojo.in/econometrics",
    level: "Advanced",
    duration: "4 hours",
    quote: '"Essential for economic research."',
  },
  {
    id: "C20",
    title: "Law and Constitution 101",
    track: "Policy Analysis",
    description: "Understanding legal frameworks and constitutional principles.",
    url: "https://101.www.impactmojo.in/law-constitution",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Rule of law foundations."',
  },
  {
    id: "C21",
    title: "Livelihoods and Sustainable Development 101",
    track: "Policy Analysis",
    description: "Understanding sustainable livelihood approaches and frameworks.",
    url: "https://101.www.impactmojo.in/livelihoods",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Pathways out of poverty."',
  },
  {
    id: "C22",
    title: "Community Development 101",
    track: "Research Methods", 
    description: "Participatory approaches to community-led development.",
    url: "https://101.www.impactmojo.in/community-dev",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Essential for grassroots work."',
  },
  {
    id: "C23",
    title: "Data Literacy 101",
    track: "Data Analysis",
    description: "Essential skills for understanding and using data effectively.",
    url: "https://101.www.impactmojo.in/data-lit",
    level: "Beginner",
    duration: "2 hours",
    quote: '"Foundation for data-driven work."',
  },
  {
    id: "C24",
    title: "Understanding Inequality 101",
    track: "Policy Analysis",
    description: "Roots and manifestations of inequality in societies.",
    url: "https://101.www.impactmojo.in/inequality",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Critical for social justice."',
  },
  {
    id: "C25",
    title: "Financial Inclusion 101",
    track: "Policy Analysis",
    description: "Expanding access to financial services for development.",
    url: "https://101.www.impactmojo.in/financial-inclusion",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Banking the unbanked."',
  },
  {
    id: "C26",
    title: "Social Protection 101",
    track: "Policy Analysis",
    description: "Social safety nets and protection systems.",
    url: "https://101.www.impactmojo.in/social-protection",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Security for vulnerable populations."',
  },
  {
    id: "C27",
    title: "Qualitative Research Methods 101",
    track: "Research Methods",
    description: "Comprehensive guide to qualitative research approaches.",
    url: "https://101.www.impactmojo.in/QualR",
    level: "Intermediate",
    duration: "4 hours",
    quote: '"Deep dive into qualitative methods."',
  },
  {
    id: "C28",
    title: "Exploratory Data Analysis for Household Surveys 101",
    track: "Data Analysis",
    description: "Statistical analysis techniques for household survey data.",
    url: "https://101.www.impactmojo.in/HH-EDA",
    level: "Intermediate",
    duration: "3.5 hours",
    quote: '"Practical guide to survey analysis."',
  },
  {
    id: "C29",
    title: "Bivariate Analysis 101",
    track: "Data Analysis",
    description: "Statistical techniques for analyzing relationships between variables.",
    url: "https://101.www.impactmojo.in/bivariateA",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Essential for correlation analysis."',
  },
  {
    id: "C30",
    title: "Multivariate Analysis 101",
    track: "Data Analysis",
    description: "Advanced statistical methods for complex data analysis.",
    url: "https://101.www.impactmojo.in/MultivariateA",
    level: "Advanced",
    duration: "4 hours",
    quote: '"Advanced statistical techniques."',
  },
  {
    id: "C31",
    title: "Digital Ethics 101",
    track: "Research Methods",
    description: "Ethical considerations in digital technology and data use.",
    url: "https://101.www.impactmojo.in/DigitalEthics",
    level: "Intermediate",
    duration: "2.5 hours",
    quote: '"Critical for digital age research."',
  },
  {
    id: "C32",
    title: "Conflict, Peace and Security 101",
    track: "Policy Analysis",
    description: "Understanding conflict dynamics and peacebuilding approaches.",
    url: "https://101.www.impactmojo.in/conflict-peace",
    level: "Advanced",
    duration: "3.5 hours",
    quote: '"Building sustainable peace."',
  },
  {
    id: "C33",
    title: "Urban Studies 101",
    track: "Policy Analysis",
    description: "Urban development challenges and sustainable city planning.",
    url: "https://101.www.impactmojo.in/urban-studies",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Cities as engines of change."',
  },
  {
    id: "C34",
    title: "Agriculture and Food Security 101",
    track: "Policy Analysis",
    description: "Agricultural systems, food security, and rural development.",
    url: "https://101.www.impactmojo.in/agriculture",
    level: "Intermediate",
    duration: "3 hours",
    quote: '"Feeding the world sustainably."',
  },

  // Premium Courses
  {
    id: "C35",
    title: "Observation to Insight 101",
    track: "Research Methods",
    description: "Transforming observational data into actionable insights.",
    url: "https://101.www.impactmojo.in/obs2insight",
    level: "Advanced",
    duration: "3.5 hours",
    isPremium: true,
    password: "OBS2025",
    quote: '"Premium methodology for researchers."',
  },
  {
    id: "C36",
    title: "Item Response Theory 101",
    track: "Data Analysis",
    description: "Advanced psychometric theory for test and survey development.",
    url: "https://101.www.impactmojo.in/IRT",
    level: "Advanced",
    duration: "4 hours",
    isPremium: true,
    password: "IRT2025",
    quote: '"Advanced psychometric methods."',
  },
  {
    id: "C37",
    title: "Social Emotional Learning 101",
    track: "Research Methods",
    description: "SEL frameworks and implementation in educational contexts.",
    url: "https://101.www.impactmojo.in/SEL",
    level: "Intermediate",
    duration: "3 hours",
    isPremium: true,
    password: "SEL2025",
    quote: '"Cutting-edge educational approach."',
  },
];

// ✅ REAL LAB DATA (10 Interactive Labs) - Updated from Project Files
const labsData = [
  {
    id: "L1",
    title: "Risk Assessment and Mitigation Lab",
    description: "Interactive tools for assessing and managing project risks.",
    url: "https://impactrisk-mitigation.netlify.app/",
    icon: "shield",
    category: "Risk Management",
    difficulty: "Intermediate",
    duration: 60,
    status: "Available"
  },
  {
    id: "L2", 
    title: "Resource Mobilisation and Sustainability Lab",
    description: "Strategies for sustainable resource mobilization.",
    url: "https://rm-sustainability4impact.netlify.app/",
    icon: "dollar-sign",
    category: "Financial Planning",
    difficulty: "Advanced",
    duration: 75,
    status: "Available"
  },
  {
    id: "L3",
    title: "Policy and Advocacy Lab",
    description: "Tools for effective policy advocacy and engagement.",
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

// ✅ NEW HANDOUTS DATA (Based on GitHub Repository Structure)
const handoutsData = [
  // Cross Cutting Resources
  {
    id: "H1",
    title: "Case Study Template",
    category: "Cross Cutting Resources",
    type: "HTML",
    description: "Template for developing comprehensive case studies.",
    url: "/handouts/cross-cutting/case-studies/case_study_template.html",
    track: "All Tracks"
  },
  {
    id: "H2",
    title: "Case Study Worksheets",
    category: "Cross Cutting Resources", 
    type: "HTML",
    description: "Interactive worksheets for case study analysis.",
    url: "/handouts/cross-cutting/case-studies/case_study_worksheets.html",
    track: "All Tracks"
  },
  {
    id: "H3",
    title: "Communication Guide",
    category: "Cross Cutting Resources",
    type: "HTML", 
    description: "Best practices for effective development communication.",
    url: "/handouts/cross-cutting/communications/communication_guide.html",
    track: "All Tracks"
  },
  {
    id: "H4",
    title: "Local Application Worksheet",
    category: "Cross Cutting Resources",
    type: "HTML",
    description: "Adapt global concepts to local contexts.",
    url: "/handouts/cross-cutting/local-application/local_application_worksheet.html",
    track: "All Tracks"
  },
  {
    id: "H5",
    title: "Software Tools Guide",
    category: "Cross Cutting Resources",
    type: "HTML",
    description: "Essential software tools for development work.",
    url: "/handouts/cross-cutting/software-tools/software_tools_guide.html",
    track: "All Tracks"
  },

  // Data Analysis Track
  {
    id: "H6",
    title: "Bivariate Analysis Guide",
    category: "Data Analysis",
    type: "HTML",
    description: "Comprehensive guide to bivariate statistical analysis.",
    url: "/handouts/data-analysis/bivariate/bivariate_analysis_guide.html",
    track: "Data Analysis"
  },
  {
    id: "H7",
    title: "Data Literacy Handout",
    category: "Data Analysis",
    type: "HTML",
    description: "Essential concepts for data literacy and understanding.",
    url: "/handouts/data-analysis/data-literacy/data_literacy_handout.html",
    track: "Data Analysis"
  },
  {
    id: "H8",
    title: "Econometrics Formula Sheet",
    category: "Data Analysis",
    type: "HTML",
    description: "Quick reference for econometric formulas and methods.",
    url: "/handouts/data-analysis/econometrics/econometrics_formula_sheet.html",
    track: "Data Analysis"
  },
  {
    id: "H9",
    title: "EDA Survey Analysis",
    category: "Data Analysis", 
    type: "HTML",
    description: "Exploratory data analysis techniques for survey data.",
    url: "/handouts/data-analysis/eda/eda_survey_handout_1.html",
    track: "Data Analysis"
  },
  {
    id: "H10",
    title: "Multivariate Analysis Template",
    category: "Data Analysis",
    type: "HTML", 
    description: "Template for multivariate statistical analysis.",
    url: "/handouts/data-analysis/multivariate/multivariate_analysis_template.html",
    track: "Data Analysis"
  },
  {
    id: "H11",
    title: "R Scripts Collection",
    category: "Data Analysis",
    type: "R",
    description: "Collection of R scripts for data analysis tasks.",
    url: "/handouts/data-analysis/scripts/r-scripts.zip",
    track: "Data Analysis"
  },
  {
    id: "H12",
    title: "Python Code Samples", 
    category: "Data Analysis",
    type: "Python",
    description: "Python code examples for data analysis and visualization.",
    url: "/handouts/data-analysis/scripts/python-samples.zip",
    track: "Data Analysis"
  },
  {
    id: "H13",
    title: "Excel Analysis Templates",
    category: "Data Analysis",
    type: "Excel", 
    description: "Ready-to-use Excel templates for statistical analysis.",
    url: "/handouts/data-analysis/excel/excel-templates.zip",
    track: "Data Analysis"
  },

  // Gender Studies Track
  {
    id: "H14",
    title: "Care Economy Analysis",
    category: "Gender Studies",
    type: "HTML",
    description: "Framework for analyzing care economy dynamics.",
    url: "/handouts/gender-studies/care-economy/care_economy_handout_1.html",
    track: "Gender Studies"
  },
  {
    id: "H15",
    title: "Data Feminism in Practice",
    category: "Gender Studies",
    type: "HTML", 
    description: "Applying data feminism principles to research.",
    url: "/handouts/gender-studies/data-feminism/data_feminism_handout_1.html",
    track: "Gender Studies"
  },
  {
    id: "H16",
    title: "Gender Studies Quick Reference",
    category: "Gender Studies",
    type: "HTML",
    description: "Key concepts and frameworks in gender studies.",
    url: "/handouts/gender-studies/gender-studies/gender_studies_quick_reference.html",
    track: "Gender Studies"
  },

  // Policy Analysis Track  
  {
    id: "H17",
    title: "Development Economics Problem Sets",
    category: "Policy Analysis",
    type: "HTML",
    description: "Practice problems for development economics concepts.",
    url: "/handouts/policy-economics/development-economics/development_economics_problem_sets.html",
    track: "Policy Analysis"
  },
  {
    id: "H18",
    title: "Livelihood Assessment Toolkit",
    category: "Policy Analysis",
    type: "HTML",
    description: "Tools for comprehensive livelihood assessments.",
    url: "/handouts/policy-economics/livelihoods/livelihood_assessment_toolkit.html",
    track: "Policy Analysis"
  },
  {
    id: "H19",
    title: "Policy Tracking Sheet",
    category: "Policy Analysis",
    type: "HTML",
    description: "Template for tracking policy developments and impacts.",
    url: "/handouts/policy-economics/policy-tracking/policy_tracking_sheet.html",
    track: "Policy Analysis"
  },
  {
    id: "H20",
    title: "Political Economy Framework",
    category: "Policy Analysis",
    type: "HTML",
    description: "Framework for political economy analysis.",
    url: "/handouts/policy-economics/political-economy/political_economy_handout_1.html",
    track: "Policy Analysis"
  },

  // Research Methods Track
  {
    id: "H21",
    title: "Research Assumptions Checklist",
    category: "Research Methods",
    type: "HTML",
    description: "Checklist for identifying and validating research assumptions.",
    url: "/handouts/research-methods/assumptions/assumptions_checklist.html", 
    track: "Research Methods"
  },
  {
    id: "H22",
    title: "MLE Framework Guide",
    category: "Research Methods",
    type: "HTML",
    description: "Guide to Monitoring, Learning, and Evaluation frameworks.",
    url: "/handouts/research-methods/mle/mel_handout_1.html",
    track: "Research Methods"
  },
  {
    id: "H23",
    title: "Qualitative Research Handbook",
    category: "Research Methods",
    type: "HTML",
    description: "Comprehensive handbook for qualitative research methods.",
    url: "/handouts/research-methods/qualitative/qualitative_research_handout.html",
    track: "Research Methods"
  },
  {
    id: "H24",
    title: "Research Design Worksheet",
    category: "Research Methods",
    type: "HTML", 
    description: "Step-by-step worksheet for research design planning.",
    url: "/handouts/research-methods/design/research_design_worksheet.html",
    track: "Research Methods"
  },

  // Thematic Areas
  {
    id: "H25",
    title: "Climate Change Impact Assessment",
    category: "Thematic Areas",
    type: "HTML",
    description: "Tools for assessing climate change impacts in South Asia.",
    url: "/handouts/thematic/climate/climate_change_handout_1.html",
    track: "Policy Analysis"
  },
  {
    id: "H26",
    title: "Environmental Justice Framework",
    category: "Thematic Areas", 
    type: "HTML",
    description: "Framework for environmental justice analysis.",
    url: "/handouts/thematic/environmental-justice/environmental_justice_handout_1.html",
    track: "Policy Analysis"
  },
  {
    id: "H27",
    title: "Constitutional Analysis Guide",
    category: "Thematic Areas",
    type: "HTML",
    description: "Guide to constitutional law and analysis.",
    url: "/handouts/thematic/constitution/constitution_handout_1.html",
    track: "Policy Analysis"
  },

  // Quick References
  {
    id: "H28", 
    title: "Quick Reference Cards",
    category: "Quick Reference",
    type: "HTML",
    description: "Collection of quick reference cards for key concepts.",
    url: "/handouts/quick-reference/quick_reference_cards.html",
    track: "All Tracks"
  },

  // Education & Pedagogy
  {
    id: "H29",
    title: "Education & Pedagogy Guide",
    category: "Education",
    type: "HTML",
    description: "Best practices in education and pedagogical approaches.", 
    url: "/handouts/education/education_pedagogy_handout.html",
    track: "Research Methods"
  }
];

// 🤖 ENHANCED AI Tools Data - Complete 16 tools with detailed instructions and prompts
const aiToolsData = [
  // Enhanced existing 8 tools
  { 
    id: 'AI1', 
    name: 'Policy Brief Generator', 
    description: 'Generate structured policy briefs from your research data and analysis', 
    category: 'Writing',
    instructions: 'Enter your policy topic, target audience, key findings, and main recommendations. The tool will create a professional policy brief with executive summary, background, analysis, and recommendations.',
    howToUse: 'Steps: 1) Enter policy topic (e.g., "Climate Change Adaptation in Urban Areas") 2) Specify target audience (e.g., "City Mayors and Urban Planners") 3) Add 3-5 key findings 4) List main recommendations 5) Generate professional brief',
    promptTemplate: `Create a comprehensive policy brief on: {topic}

Target Audience: {audience}
Key Findings: {findings}
Recommendations: {recommendations}

Please structure as:
1. Executive Summary (200 words)
2. Background & Context (300 words)
3. Analysis of Key Issues (400 words)
4. Policy Recommendations (300 words)
5. Implementation Steps (200 words)

Use professional policy language and include specific, actionable recommendations.`,
    systemMessage: 'You are a senior policy analyst with expertise in public policy and government relations. Create professional, evidence-based policy documents with clear recommendations and implementation strategies.',
    exampleInput: `Topic: Digital Skills Training for Rural Communities
Audience: Regional Development Officers
Key Findings: 
- 67% lack basic digital literacy
- Limited internet infrastructure 
- Youth migration to cities due to lack of opportunities
Recommendations:
- Mobile training units
- Public-private partnerships
- Subsidized internet access`,
    icon: FileText,
    color: 'blue'
  },
  { 
    id: 'AI2', 
    name: 'Research Question Refiner', 
    description: 'Refine and improve your research questions for better focus and clarity', 
    category: 'Research',
    instructions: 'Paste your draft research question(s) and specify your field of study, methodology preference, and scope. The tool will analyze and suggest improvements for clarity, feasibility, and academic rigor.',
    howToUse: 'Steps: 1) Enter your draft research question 2) Specify academic field 3) Indicate preferred methodology (qualitative/quantitative/mixed) 4) Set scope (local/national/global) 5) Get refined suggestions with rationale',
    promptTemplate: `Refine and improve this research question: "{question}"

Research Field: {field}
Methodology: {methodology}
Scope: {scope}
Current Academic Level: {level}

Please provide:
1. Analysis of the current question (strengths/weaknesses)
2. 3 refined alternative versions
3. Explanation of improvements made
4. Feasibility assessment
5. Suggested sub-questions if applicable

Focus on making questions more specific, measurable, and academically rigorous.`,
    systemMessage: 'You are a research methodology expert with expertise in academic research design across multiple disciplines. Help refine research questions for clarity, feasibility, and academic rigor.',
    exampleInput: `Question: How does social media affect young people?
Field: Digital Sociology
Methodology: Mixed Methods
Scope: National (teenagers aged 13-18)
Level: Graduate thesis`,
    icon: Search,
    color: 'green'
  },
  { 
    id: 'AI3', 
    name: 'Data Story Creator', 
    description: 'Turn data insights into compelling narratives and visualizations', 
    category: 'Analysis',
    instructions: 'Describe your data, key findings, and target audience. The tool creates narrative structures with suggested visualizations, compelling storylines, and clear takeaway messages.',
    howToUse: 'Steps: 1) Describe your data/findings 2) Specify target audience 3) Choose narrative style (analytical/persuasive/educational) 4) Set complexity level 5) Generate story structure with visualization suggestions',
    promptTemplate: `Create a compelling data story from: {data}

Key Findings: {findings}
Target Audience: {audience}
Narrative Style: {style}
Complexity Level: {complexity}

Please provide:
1. Executive summary (key message in 50 words)
2. Story structure with 5-7 main points
3. Suggested visualizations for each point
4. Compelling opening and closing
5. Call-to-action recommendations
6. Data presentation tips

Make it engaging and accessible to the target audience.`,
    systemMessage: 'You are a data storytelling expert who transforms complex data into engaging narratives. You understand visualization best practices and how to communicate insights effectively to different audiences.',
    exampleInput: `Data: Survey of 1,200 remote workers across 15 countries
Findings: 
- 78% report higher productivity at home
- 65% struggle with work-life balance
- 43% feel disconnected from colleagues
Audience: HR Directors and Team Managers
Style: Persuasive (for policy change)`,
    icon: BarChart,
    color: 'purple'
  },
  { 
    id: 'AI4', 
    name: 'Grant Proposal Assistant', 
    description: 'Help structure and improve grant proposals with proven frameworks', 
    category: 'Writing',
    instructions: 'Provide your project concept, target funder type, budget range, and timeline. The tool creates structured proposals with compelling problem statements, clear methodologies, and realistic budgets.',
    howToUse: 'Steps: 1) Describe project concept clearly 2) Specify funder type (government/foundation/corporate) 3) Enter budget range 4) Set project timeline 5) Generate complete proposal framework',
    promptTemplate: `Create a grant proposal framework for: {project}

Funder Type: {funder}
Budget Range: {budget}
Timeline: {timeline}
Target Population: {population}
Expected Impact: {impact}

Please structure as:
1. Executive Summary (250 words)
2. Problem Statement with evidence (400 words)
3. Project Description & Methodology (500 words)
4. Goals, Objectives & Outcomes (300 words)
5. Budget Justification outline (200 words)
6. Sustainability Plan (200 words)
7. Evaluation Framework (200 words)

Include specific metrics and evidence-based justifications.`,
    systemMessage: 'You are a grant writing specialist with 15+ years experience securing funding from government agencies, foundations, and corporate sponsors. You understand funder priorities and write compelling, evidence-based proposals.',
    exampleInput: `Project: Mobile Health Clinic for Rural Maternal Care
Funder: Private Foundation (health focus)
Budget: $150,000 - $300,000
Timeline: 2 years
Population: Pregnant women in remote areas (500+ beneficiaries)
Impact: Reduce maternal mortality by 40%`,
    icon: TrendingUp,
    color: 'blue'
  },
  { 
    id: 'AI5', 
    name: 'Impact Measurement Framework', 
    description: 'Design comprehensive frameworks to measure and evaluate social impact', 
    category: 'Analysis',
    instructions: 'Define your program goals, activities, target beneficiaries, and timeframe. The tool creates logic models, identifies key indicators, and suggests measurement approaches.',
    howToUse: 'Steps: 1) Enter program objectives clearly 2) List main activities/interventions 3) Define target beneficiaries 4) Specify measurement timeframe 5) Generate complete M&E framework with indicators',
    promptTemplate: `Create an impact measurement framework for: {program}

Program Goals: {goals}
Main Activities: {activities}
Target Beneficiaries: {beneficiaries}
Timeframe: {timeframe}
Budget for M&E: {budget}

Please provide:
1. Logic Model (inputs → activities → outputs → outcomes → impact)
2. Key Performance Indicators (KPIs) for each level
3. Data collection methods and timeline
4. Baseline and target metrics
5. Evaluation questions for each outcome
6. Reporting framework and frequency
7. Risk assumptions and mitigation

Include both quantitative and qualitative indicators.`,
    systemMessage: 'You are a monitoring and evaluation specialist with expertise in social impact measurement. You design rigorous frameworks that capture both quantitative outcomes and qualitative changes in complex social programs.',
    exampleInput: `Program: Digital Literacy Training for Senior Citizens
Goals: Improve digital inclusion and reduce social isolation
Activities: Weekly computer classes, one-on-one support, peer mentoring
Beneficiaries: 200 seniors (65+) in rural communities
Timeframe: 12 months
Budget: $25,000 for M&E activities`,
    icon: Target,
    color: 'red'
  },
  { 
    id: 'AI6', 
    name: 'Stakeholder Mapping Tool', 
    description: 'Identify and map project stakeholders with influence and interest analysis', 
    category: 'Planning',
    instructions: 'Describe your project, sector, and geographic scope. The tool identifies relevant stakeholders, analyzes their influence/interest levels, and suggests engagement strategies.',
    howToUse: 'Steps: 1) Describe project scope and objectives 2) Specify sector and location 3) List known stakeholders 4) Define project phase (planning/implementation/evaluation) 5) Generate comprehensive stakeholder map',
    promptTemplate: `Create a stakeholder mapping for: {project}

Project Scope: {scope}
Sector: {sector}
Location: {location}
Project Phase: {phase}
Known Stakeholders: {known}

Please provide:
1. Comprehensive stakeholder list by category:
   - Primary stakeholders (directly affected)
   - Secondary stakeholders (indirectly affected)
   - Key stakeholders (decision makers)
2. Influence vs Interest matrix mapping
3. Engagement strategy for each stakeholder type
4. Communication plan recommendations
5. Potential risks and mitigation strategies
6. Timeline for stakeholder engagement

Include both supportive and potentially resistant stakeholders.`,
    systemMessage: 'You are a stakeholder engagement specialist with expertise in complex multi-stakeholder projects. You understand power dynamics, influence mapping, and effective engagement strategies across different sectors.',
    exampleInput: `Project: Community Solar Energy Installation
Scope: 500-household renewable energy project
Sector: Clean Energy/Rural Development
Location: Rural county in Kenya
Phase: Planning and feasibility
Known: Local chief, utility company, environmental NGO`,
    icon: Users,
    color: 'green'
  },
  { 
    id: 'AI7', 
    name: 'Literature Review Helper', 
    description: 'Organize and synthesize academic literature with thematic analysis', 
    category: 'Research',
    instructions: 'Enter your research topic, key papers/abstracts, and review scope. The tool organizes sources by themes, identifies gaps, and creates synthesis summaries.',
    howToUse: 'Steps: 1) Enter research topic/question 2) Paste abstracts or paper summaries 3) Specify review scope (systematic/narrative) 4) Choose organization method 5) Generate thematic synthesis',
    promptTemplate: `Organize and synthesize literature on: {topic}

Research Question: {question}
Key Papers/Abstracts: {papers}
Review Type: {type}
Time Period: {period}
Scope: {scope}

Please provide:
1. Thematic organization of literature
2. Key themes and sub-themes identified
3. Summary of main findings by theme
4. Identification of research gaps
5. Methodological patterns observed
6. Conflicting findings and debates
7. Future research directions
8. Suggested outline for literature review section

Include proper academic synthesis, not just summaries.`,
    systemMessage: 'You are an academic researcher with expertise in literature reviews and systematic analysis. You help organize complex literature into coherent themes and identify patterns, gaps, and synthesis opportunities.',
    exampleInput: `Topic: Impact of Microfinance on Women's Empowerment
Question: How does access to microfinance affect women's decision-making power in developing countries?
Papers: [paste 5-10 abstracts]
Type: Systematic review
Period: 2015-2023
Scope: Developing countries, randomized controlled trials`,
    icon: BookOpen,
    color: 'indigo'
  },
  { 
    id: 'AI8', 
    name: 'Workshop Facilitator', 
    description: 'Plan and structure effective workshop sessions with activities and timelines', 
    category: 'Planning',
    instructions: 'Specify workshop objectives, duration, participant type, and preferred format. The tool creates detailed agendas with activities, timing, materials, and facilitation tips.',
    howToUse: 'Steps: 1) Define clear workshop goals 2) Set duration and participant count 3) Choose participant type/level 4) Specify format (in-person/virtual/hybrid) 5) Generate complete facilitation guide',
    promptTemplate: `Design a workshop on: {topic}

Objectives: {objectives}
Duration: {duration}
Participants: {participants} ({count} people)
Format: {format}
Experience Level: {level}
Desired Outcomes: {outcomes}

Please provide:
1. Detailed agenda with time allocations
2. Learning objectives for each session
3. Interactive activities and exercises
4. Materials and resources needed
5. Facilitation tips and techniques
6. Engagement strategies for different learning styles
7. Assessment/feedback methods
8. Follow-up recommendations

Include specific instructions for facilitator and participant handouts.`,
    systemMessage: 'You are an experienced workshop facilitator and adult learning specialist. You design engaging, interactive sessions that achieve clear learning outcomes through proven facilitation techniques and adult learning principles.',
    exampleInput: `Topic: Design Thinking for Social Innovation
Objectives: Teach human-centered design methods to nonprofit leaders
Duration: 6 hours (full day)
Participants: NGO program managers and directors (20 people)
Format: In-person
Level: Beginner to intermediate
Outcomes: Participants can apply design thinking to their programs`,
    icon: Users,
    color: 'orange'
  },

  // New 8 tools with enhanced prompts
  { 
    id: 'AI9', 
    name: 'Worksheet Generator', 
    description: 'Generate educational worksheets with various question types on any topic', 
    category: 'Teaching',
    instructions: 'Specify your subject, topic, grade level, and question types. Include learning objectives and desired difficulty. The tool creates ready-to-print worksheets with answer keys.',
    howToUse: 'Steps: 1) Enter subject and specific topic 2) Select grade level 3) Choose question types (multiple choice, short answer, etc.) 4) Set number of questions 5) Generate printable worksheet with answer key',
    promptTemplate: `Create an educational worksheet on: {topic}

Subject: {subject}
Grade Level: {grade}
Number of Questions: {questions}
Question Types: {types}
Learning Objectives: {objectives}
Difficulty Level: {difficulty}

Please create:
1. Worksheet title and clear instructions
2. {questions} questions in specified formats
3. Appropriate difficulty progression
4. Clear formatting for printing
5. Complete answer key with explanations
6. Extension activities for advanced students
7. Modification suggestions for struggling learners

Format for easy printing and classroom use. Include engaging, age-appropriate content.`,
    systemMessage: 'You are an experienced educational content creator who designs engaging worksheets aligned with curriculum standards. You understand different learning styles and create age-appropriate, pedagogically sound materials.',
    exampleInput: `Topic: Photosynthesis Process
Subject: Biology
Grade: 9th grade (14-15 years)
Questions: 15 questions
Types: Multiple choice (5), Short answer (5), Diagram labeling (5)
Objectives: Students understand inputs/outputs of photosynthesis
Difficulty: Intermediate`,
    icon: FileText,
    color: 'blue'
  },
  { 
    id: 'AI10', 
    name: 'Choice Board Generator', 
    description: 'Create activity choice boards for differentiated learning with multiple options', 
    category: 'Teaching',
    instructions: 'Enter your learning topic, objectives, and grade level. The tool creates a grid of diverse activities for different learning styles (visual, auditory, kinesthetic, reading/writing).',
    howToUse: 'Steps: 1) Enter learning topic and unit 2) Define 2-3 key learning objectives 3) Choose grade level 4) Select board size (3x3 or 4x4) 5) Generate choice board with varied activities',
    promptTemplate: `Create a choice board for: {topic}

Learning Unit: {unit}
Grade Level: {grade}
Learning Objectives: {objectives}
Board Size: {size}
Subject Area: {subject}
Duration: {duration}

Create a {size} choice board with activities covering:
1. Visual learners (diagrams, infographics, videos)
2. Auditory learners (presentations, podcasts, discussions)
3. Kinesthetic learners (hands-on, movement, building)
4. Reading/Writing learners (essays, reports, creative writing)

Each activity should:
- Align with learning objectives
- Be age-appropriate and engaging
- Include clear instructions and success criteria
- Offer different difficulty levels
- Be completable in specified timeframe

Include one required center activity and varied optional activities.`,
    systemMessage: 'You are a differentiated instruction specialist who creates engaging choice boards that accommodate multiple learning styles while maintaining academic rigor and clear learning objectives.',
    exampleInput: `Topic: Ancient Egypt Civilization
Unit: Ancient Civilizations - Egypt chapter
Grade: 6th grade (11-12 years)
Objectives: 1) Understand Egyptian social structure 2) Explain mummification process 3) Analyze pyramid construction
Size: 3x3 grid (9 activities)
Subject: Social Studies
Duration: 2-week unit`,
    icon: Gamepad2,
    color: 'purple'
  },
  { 
    id: 'AI11', 
    name: 'Multiple Choice Assessment Generator', 
    description: 'Generate comprehensive MCQ assessments from content with answer keys', 
    category: 'Assessment',
    instructions: 'Paste content text or enter key topics to assess. Specify question count, difficulty, and cognitive levels (remember, understand, apply, analyze). Creates balanced assessments with detailed answer explanations.',
    howToUse: 'Steps: 1) Paste source content or list key concepts 2) Set number of questions (10-50) 3) Choose difficulty distribution 4) Select cognitive levels to assess 5) Generate MCQ test with detailed answer key',
    promptTemplate: `Create a multiple-choice assessment from: {content}

Key Topics to Assess: {topics}
Number of Questions: {questions}
Grade Level: {grade}
Cognitive Levels: {cognitive}
Difficulty Distribution: {difficulty}

Create {questions} multiple-choice questions that:
1. Cover all key topics proportionally
2. Include 4 plausible answer choices each
3. Test different cognitive levels (remember, understand, apply, analyze)
4. Avoid trick questions or ambiguous wording
5. Include variety in question formats
6. Progress from easier to more challenging

Provide:
- Complete question set with A/B/C/D choices
- Answer key with correct letters
- Detailed explanations for correct answers
- Rationale for why other options are incorrect
- Alignment to specific learning objectives`,
    systemMessage: 'You are an assessment design expert who creates fair, valid, and reliable multiple-choice tests. You understand cognitive taxonomies and write clear questions that accurately measure student learning.',
    exampleInput: `Content: [Paste chapter text on Cellular Respiration]
Topics: Glycolysis, Citric Acid Cycle, Electron Transport Chain, ATP production
Questions: 20 questions
Grade: 11th grade Biology
Cognitive: 30% remember, 40% understand, 20% apply, 10% analyze
Difficulty: 25% easy, 50% medium, 25% challenging`,
    icon: CheckCircle,
    color: 'green'
  },
  { 
    id: 'AI12', 
    name: 'Writing Feedback Tool', 
    description: 'Provide detailed AI-powered feedback on student writing with improvement suggestions', 
    category: 'Assessment',
    instructions: 'Paste student writing sample and specify writing type, grade level, and feedback focus areas. The tool analyzes content, structure, grammar, and style with specific improvement suggestions.',
    howToUse: 'Steps: 1) Paste student writing sample 2) Select writing type (essay, report, creative, etc.) 3) Choose grade level 4) Set feedback focus (content, organization, mechanics) 5) Generate detailed feedback with suggestions',
    promptTemplate: `Provide detailed feedback on this student writing:

{writing}

Writing Type: {type}
Grade Level: {grade}
Assignment Requirements: {requirements}
Focus Areas: {focus}
Feedback Style: {style}

Please provide:
1. Overall impression and strengths (positive feedback first)
2. Content and Ideas Analysis:
   - Clarity of main idea/thesis
   - Supporting evidence and examples
   - Depth of analysis
3. Organization and Structure:
   - Introduction effectiveness
   - Paragraph structure and transitions
   - Conclusion strength
4. Language and Style:
   - Sentence variety and flow
   - Word choice and vocabulary
   - Voice and tone appropriateness
5. Mechanics and Grammar:
   - Grammar and punctuation errors
   - Spelling and capitalization
6. Specific Improvement Suggestions:
   - 3-5 concrete next steps
   - Examples of better alternatives
7. Grade-appropriate learning goals for revision

Keep feedback constructive, specific, and encouraging.`,
    systemMessage: 'You are an experienced writing teacher who provides constructive, specific feedback that helps students improve. You balance encouragement with clear guidance for improvement, adapting your feedback style to the student\'s grade level.',
    exampleInput: `Writing: [Paste 250-word student essay on "The Importance of Recycling"]
Type: Persuasive essay
Grade: 8th grade
Requirements: 5-paragraph structure, 3 supporting arguments, MLA format
Focus: Content development and organization
Style: Encouraging but thorough`,
    icon: Edit3,
    color: 'blue'
  },
  { 
    id: 'AI13', 
    name: 'Text Processor', 
    description: 'Process and analyze text documents for key insights and summaries', 
    category: 'Analysis',
    instructions: 'Upload or paste text content for analysis. Specify analysis type (summary, keyword extraction, sentiment analysis, etc.). The tool processes text and provides requested insights.',
    howToUse: 'Steps: 1) Paste or upload text content 2) Select analysis type (summary, keywords, sentiment, etc.) 3) Set output length/depth 4) Specify focus areas if applicable 5) Generate text analysis report',
    promptTemplate: `Analyze the following text: {text}

Analysis Type: {type}
Output Length: {length}
Focus Areas: {focus}
Special Instructions: {instructions}

Please provide:
1. {type} analysis of the text
2. Key insights and patterns identified
3. Main themes and topics
4. Notable quotes or excerpts
5. Structural analysis (if applicable)
6. Contextual relevance assessment
7. Limitations or gaps in the text

Format the analysis in a clear, structured way suitable for {purpose}.`,
    systemMessage: 'You are a text analysis specialist with expertise in natural language processing and document analysis. You extract meaningful insights from text content and present them in clear, actionable formats.',
    exampleInput: `Text: [Paste research article or document]
Type: Comprehensive summary
Length: 300 words
Focus: Methodology and findings
Instructions: Highlight key research methods and major conclusions`,
    icon: FileText,
    color: 'indigo'
  },
  { 
    id: 'AI14', 
    name: 'Survey Designer', 
    description: 'Create effective surveys with well-structured questions for research and feedback', 
    category: 'Research',
    instructions: 'Describe your survey purpose, target audience, and key topics. The tool creates structured surveys with appropriate question types, logical flow, and clear instructions.',
    howToUse: 'Steps: 1) Define survey purpose and goals 2) Describe target respondents 3) List key topics to cover 4) Set survey length preference 5) Generate complete survey with question flow',
    promptTemplate: `Design a survey for: {purpose}

Target Audience: {audience}
Survey Goals: {goals}
Key Topics: {topics}
Estimated Length: {length} minutes
Distribution Method: {method}

Please create:
1. Survey introduction and purpose statement
2. 15-20 well-structured questions covering all topics
3. Appropriate question types (multiple choice, Likert scale, open-ended, etc.)
4. Logical question flow and grouping
5. Clear instructions for each section
6. Demographic questions (if needed)
7. Closing and thank you message
8. Estimated completion time

Ensure questions are:
- Clear and unambiguous
- Unbiased and neutral
- Appropriate for the target audience
- Aligned with survey goals`,
    systemMessage: 'You are a survey design specialist with expertise in creating effective research instruments. You understand question design principles, response biases, and how to structure surveys for maximum response quality.',
    exampleInput: `Purpose: Assess employee satisfaction with remote work policies
Audience: Full-time employees who have worked remotely for at least 6 months
Goals: Identify pain points, gather improvement suggestions, measure satisfaction levels
Topics: Work-life balance, productivity, communication, technology, management support
Length: 10-12 minutes
Method: Online form via email`,
    icon: ClipboardList,
    color: 'green'
  },
  { 
    id: 'AI15', 
    name: 'Presentation Outliner', 
    description: 'Structure compelling presentations with clear flow and key talking points', 
    category: 'Planning',
    instructions: 'Enter your presentation topic, audience, duration, and key messages. The tool creates a structured outline with slide suggestions, talking points, and visual recommendations.',
    howToUse: 'Steps: 1) Enter presentation topic and purpose 2) Define target audience and their knowledge level 3) Set presentation duration 4) List 3-5 key messages to convey 5) Generate complete presentation outline',
    promptTemplate: `Create a presentation outline for: {topic}

Presentation Purpose: {purpose}
Target Audience: {audience} (knowledge level: {level})
Duration: {duration} minutes
Key Messages: {messages}
Visual Style Preference: {style}

Please structure:
1. Attention-grabbing opening (hook)
2. Clear agenda/overview
3. Main content sections (3-5 sections):
   - Key points for each section
   - Supporting data/evidence
   - Slide content suggestions
4. Engaging transitions between sections
5. Strong conclusion with call to action
6. Q&A preparation notes

For each section, include:
- Approximate time allocation
- Slide content suggestions
- Speaker talking points
- Visual aid recommendations
- Engagement strategies

Ensure the presentation flows logically and builds a compelling case.`,
    systemMessage: 'You are a presentation design expert who creates clear, engaging presentation structures. You understand audience engagement, information hierarchy, and how to structure presentations for maximum impact and retention.',
    exampleInput: `Topic: Implementing Sustainable Supply Chains
Purpose: Convince corporate executives to adopt sustainable practices
Audience: C-suite executives with limited sustainability knowledge
Duration: 20 minutes
Messages: 1) Sustainability improves brand reputation 2) Long-term cost savings 3) Competitive advantage in market
Style: Professional with data visualizations`,
    icon: Presentation,
    color: 'blue'
  },
  { 
    id: 'AI16', 
    name: 'Project Planner', 
    description: 'Create comprehensive project plans with timelines, milestones, and resource allocation', 
    category: 'Planning',
    instructions: 'Describe your project goals, scope, constraints, and available resources. The tool creates detailed project plans with timelines, milestones, dependencies, and resource allocation.',
    howToUse: 'Steps: 1) Define project goals and deliverables 2) Set project scope and boundaries 3) Identify constraints (time, budget, resources) 4) List available team/resources 5) Generate complete project plan',
    promptTemplate: `Create a project plan for: {project}

Project Goals: {goals}
Key Deliverables: {deliverables}
Project Scope: {scope}
Time Constraints: {timeline}
Budget Constraints: {budget}
Available Resources: {resources}
Team Size: {team} people
Key Stakeholders: {stakeholders}

Please provide:
1. Project overview and objectives
2. Work breakdown structure with major phases
3. Detailed timeline with milestones and dependencies
4. Resource allocation plan (human, financial, technical)
5. Risk assessment and mitigation strategies
6. Communication plan
7. Success metrics and evaluation methods
8. Contingency plans for common issues

Include specific tasks, owners, deadlines, and dependencies where possible.`,
    systemMessage: 'You are a project management specialist with expertise in creating comprehensive project plans. You understand task dependencies, resource allocation, risk management, and how to structure projects for successful implementation.',
    exampleInput: `Project: Community Garden Initiative
Goals: Establish 5 community gardens in underserved neighborhoods
Deliverables: 5 functional gardens, training programs, management plan
Scope: Site selection, garden construction, community training, 6-month support
Timeline: 9 months (April-December)
Budget: $75,000
Resources: 3 staff members, 20 volunteers, local government partnerships
Team: 1 project manager, 2 coordinators
Stakeholders: Community groups, local government, sponsors`,
    icon: Calendar,
    color: 'purple'
  }
];

// Navigation Component
const Navbar = ({ darkMode, setDarkMode, user, signInWithGoogle, signOut }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  return (
    <nav className={`sticky top-0 z-50 ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md transition-colors duration-300`}>
      <div className="container mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0 flex items-center">
              <span className="font-bold text-xl text-blue-600 dark:text-blue-400">ImpactMojo</span>
            </div>
            <div className="hidden md:ml-6 md:flex md:space-x-8">
              <Link to="/" className={`${darkMode ? 'text-gray-300 hover:text-white' : 'text-gray-700 hover:text-gray-900'} px-3 py-2 rounded-md text-sm font-medium transition-colors duration-300`}>Home</Link>
              <Link to="/courses" className={`${darkMode ? 'text-gray-300 hover:text-white' : 'text-gray-700 hover:text-gray-900'} px-3 py-2 rounded-md text-sm font-medium transition-colors duration-300`}>Courses</Link>
              <Link to="/labs" className={`${darkMode ? 'text-gray-300 hover:text-white' : 'text-gray-700 hover:text-gray-900'} px-3 py-2 rounded-md text-sm font-medium transition-colors duration-300`}>Labs</Link>
              <Link to="/resources" className={`${darkMode ? 'text-gray-300 hover:text-white' : 'text-gray-700 hover:text-gray-900'} px-3 py-2 rounded-md text-sm font-medium transition-colors duration-300`}>Resources</Link>
              <Link to="/ai-tools" className={`${darkMode ? 'text-gray-300 hover:text-white' : 'text-gray-700 hover:text-gray-900'} px-3 py-2 rounded-md text-sm font-medium transition-colors duration-300`}>AI Tools</Link>
            </div>
          </div>
          
          <div className="hidden md:flex items-center">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none transition-colors duration-300"
            >
              {darkMode ? <Sun size={20} /> : <Moon size={20} />}
            </button>
            
            {user ? (
              <div className="ml-4 flex items-center">
                <Link to="/profile" className="flex items-center text-sm rounded-full focus:outline-none">
                  <div className="h-8 w-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-medium">
                    {user.displayName ? user.displayName.charAt(0).toUpperCase() : 'U'}
                  </div>
                </Link>
                <button
                  onClick={signOut}
                  className="ml-3 flex items-center text-sm text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                >
                  <LogOut size={18} className="mr-1" /> Sign out
                </button>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="ml-4 flex items-center text-sm bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors duration-300"
              >
                Sign in
              </button>
            )}
          </div>
          
          <div className="flex items-center md:hidden">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none transition-colors duration-300"
            >
              {darkMode ? <Sun size={20} /> : <Moon size={20} />}
            </button>
            
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="ml-2 p-2 rounded-md text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none transition-colors duration-300"
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            <Link to="/" className={`${darkMode ? 'text-gray-300 hover:text-white hover:bg-gray-700' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-100'} block px-3 py-2 rounded-md text-base font-medium transition-colors duration-300`}>Home</Link>
            <Link to="/courses" className={`${darkMode ? 'text-gray-300 hover:text-white hover:bg-gray-700' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-100'} block px-3 py-2 rounded-md text-base font-medium transition-colors duration-300`}>Courses</Link>
            <Link to="/labs" className={`${darkMode ? 'text-gray-300 hover:text-white hover:bg-gray-700' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-100'} block px-3 py-2 rounded-md text-base font-medium transition-colors duration-300`}>Labs</Link>
            <Link to="/resources" className={`${darkMode ? 'text-gray-300 hover:text-white hover:bg-gray-700' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-100'} block px-3 py-2 rounded-md text-base font-medium transition-colors duration-300`}>Resources</Link>
            <Link to="/ai-tools" className={`${darkMode ? 'text-gray-300 hover:text-white hover:bg-gray-700' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-100'} block px-3 py-2 rounded-md text-base font-medium transition-colors duration-300`}>AI Tools</Link>
            
            {user ? (
              <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
                <div className="flex items-center px-4">
                  <div className="flex-shrink-0">
                    <div className="h-10 w-10 rounded-full bg-blue-500 flex items-center justify-center text-white font-medium">
                      {user.displayName ? user.displayName.charAt(0).toUpperCase() : 'U'}
                    </div>
                  </div>
                  <div className="ml-3">
                    <div className="text-base font-medium text-gray-800 dark:text-white">{user.displayName}</div>
                    <div className="text-sm font-medium text-gray-500 dark:text-gray-400">{user.email}</div>
                  </div>
                </div>
                <div className="mt-3 px-2">
                  <Link to="/profile" className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors duration-300">Your Profile</Link>
                  <button
                    onClick={signOut}
                    className="mt-1 block w-full text-left px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors duration-300"
                  >
                    Sign out
                  </button>
                </div>
              </div>
            ) : (
              <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
                <div className="px-2">
                  <button
                    onClick={signInWithGoogle}
                    className="w-full flex items-center justify-center text-sm bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors duration-300"
                  >
                    Sign in with Google
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </nav>
  );
};

// Footer Component
const Footer = ({ darkMode }) => {
  return (
    <footer className={`${darkMode ? 'bg-gray-800' : 'bg-gray-100'} transition-colors duration-300`}>
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">ImpactMojo</h3>
            <p className="text-gray-600 dark:text-gray-400">
              Empowering change-makers with knowledge, tools, and resources to create sustainable impact.
            </p>
          </div>
          
          <div>
            <h4 className="text-md font-medium mb-4 text-gray-900 dark:text-white">Quick Links</h4>
            <ul className="space-y-2">
              <li><Link to="/" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Home</Link></li>
              <li><Link to="/courses" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Courses</Link></li>
              <li><Link to="/labs" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Labs</Link></li>
              <li><Link to="/resources" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Resources</Link></li>
            </ul>
          </div>
          
          <div>
            <h4 className="text-md font-medium mb-4 text-gray-900 dark:text-white">Resources</h4>
            <ul className="space-y-2">
              <li><Link to="/ai-tools" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">AI Tools</Link></li>
              <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Blog</a></li>
              <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Documentation</a></li>
              <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">Support</a></li>
            </ul>
          </div>
          
          <div>
            <h4 className="text-md font-medium mb-4 text-gray-900 dark:text-white">Connect</h4>
            <div className="flex space-x-4 mb-4">
              <a href="#" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">
                <Twitter size={20} />
              </a>
              <a href="#" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">
                <Linkedin size={20} />
              </a>
              <a href="#" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-300">
                <Github size={20} />
              </a>
            </div>
            <p className="text-gray-600 dark:text-gray-400">
              Subscribe to our newsletter for updates
            </p>
            <div className="mt-2 flex">
              <input 
                type="email" 
                placeholder="Your email" 
                className="px-3 py-2 rounded-l-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-r-md transition-colors duration-300">
                Subscribe
              </button>
            </div>
          </div>
        </div>
        
        <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700 text-center text-gray-600 dark:text-gray-400 text-sm">
          <p>&copy; {new Date().getFullYear()} ImpactMojo. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

// Home Page Component
const HomePage = () => {
  const [darkMode] = useContext(ThemeContext);
  
  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'} transition-colors duration-300`}>
      {/* Hero Section */}
      <div className="relative">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-indigo-600 opacity-90"></div>
        <div className="relative container mx-auto px-4 py-24 md:py-32">
          <div className="max-w-3xl">
            <h1 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Empowering Change-Makers with Knowledge and Tools
            </h1>
            <p className="text-xl text-blue-100 mb-8">
              Access courses, interactive labs, resources, and AI-powered tools to create sustainable impact in your community.
            </p>
            <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
              <Link to="/courses" className="bg-white text-blue-600 hover:bg-blue-50 px-6 py-3 rounded-md font-medium text-center transition-colors duration-300">
                Explore Courses
              </Link>
              <Link to="/ai-tools" className="bg-transparent border-2 border-white text-white hover:bg-white hover:text-blue-600 px-6 py-3 rounded-md font-medium text-center transition-colors duration-300">
                Try AI Tools
              </Link>
            </div>
          </div>
        </div>
      </div>
      
      {/* Features Section */}
      <div className="py-16">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">Everything You Need to Create Impact</h2>
            <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
              Our comprehensive platform provides learning resources, practical tools, and AI-powered assistance to support your development work.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md transition-colors duration-300`}>
              <div className="w-12 h-12 rounded-lg bg-blue-100 dark:bg-blue-900 flex items-center justify-center mb-4">
                <BookOpen className="text-blue-600 dark:text-blue-400" size={24} />
              </div>
              <h3 className="text-xl font-semibold mb-2">Courses</h3>
              <p className="text-gray-600 dark:text-gray-400">
                37+ expert-led courses on gender studies, policy analysis, research methods, and data analysis.
              </p>
              <Link to="/courses" className="mt-4 inline-flex items-center text-blue-600 dark:text-blue-400 hover:underline">
                Explore courses <ArrowRight size={16} className="ml-1" />
              </Link>
            </div>
            
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md transition-colors duration-300`}>
              <div className="w-12 h-12 rounded-lg bg-green-100 dark:bg-green-900 flex items-center justify-center mb-4">
                <Gamepad2 className="text-green-600 dark:text-green-400" size={24} />
              </div>
              <h3 className="text-xl font-semibold mb-2">Interactive Labs</h3>
              <p className="text-gray-600 dark:text-gray-400">
                10 hands-on labs for risk assessment, policy advocacy, MLE frameworks, and more.
              </p>
              <Link to="/labs" className="mt-4 inline-flex items-center text-blue-600 dark:text-blue-400 hover:underline">
                Visit labs <ArrowRight size={16} className="ml-1" />
              </Link>
            </div>
            
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md transition-colors duration-300`}>
              <div className="w-12 h-12 rounded-lg bg-purple-100 dark:bg-purple-900 flex items-center justify-center mb-4">
                <FolderOpen className="text-purple-600 dark:text-purple-400" size={24} />
              </div>
              <h3 className="text-xl font-semibold mb-2">Resources</h3>
              <p className="text-gray-600 dark:text-gray-400">
                Comprehensive collection of handouts, templates, and guides organized by category.
              </p>
              <Link to="/resources" className="mt-4 inline-flex items-center text-blue-600 dark:text-blue-400 hover:underline">
                Browse resources <ArrowRight size={16} className="ml-1" />
              </Link>
            </div>
            
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md transition-colors duration-300`}>
              <div className="w-12 h-12 rounded-lg bg-red-100 dark:bg-red-900 flex items-center justify-center mb-4">
                <Bot className="text-red-600 dark:text-red-400" size={24} />
              </div>
              <h3 className="text-xl font-semibold mb-2">AI Tools</h3>
              <p className="text-gray-600 dark:text-gray-400">
                16 AI-powered tools for research, writing, analysis, and project planning.
              </p>
              <Link to="/ai-tools" className="mt-4 inline-flex items-center text-blue-600 dark:text-blue-400 hover:underline">
                Try AI tools <ArrowRight size={16} className="ml-1" />
              </Link>
            </div>
          </div>
        </div>
      </div>
      
      {/* Testimonials Section */}
      <div className={`py-16 ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">What Our Community Says</h2>
            <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
              Hear from change-makers who have used our platform to enhance their work.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-750' : 'bg-gray-50'} transition-colors duration-300`}>
              <div className="flex items-center mb-4">
                <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center text-white font-medium mr-3">
                  A
                </div>
                <div>
                  <h4 className="font-semibold">Anita Sharma</h4>
                  <p className="text-sm text-gray-600 dark:text-gray-400">NGO Director</p>
                </div>
              </div>
              <p className="text-gray-700 dark:text-gray-300 italic">
                "The courses on gender studies completely transformed our approach to community development. The practical frameworks are invaluable."
              </p>
            </div>
            
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-750' : 'bg-gray-50'} transition-colors duration-300`}>
              <div className="flex items-center mb-4">
                <div className="w-10 h-10 rounded-full bg-green-500 flex items-center justify-center text-white font-medium mr-3">
                  R
                </div>
                <div>
                  <h4 className="font-semibold">Rajesh Kumar</h4>
                  <p className="text-sm text-gray-600 dark:text-gray-400">Researcher</p>
                </div>
              </div>
              <p className="text-gray-700 dark:text-gray-300 italic">
                "The AI tools have saved me countless hours in data analysis and report writing. The quality of outputs is impressive."
              </p>
            </div>
            
            <div className={`p-6 rounded-xl ${darkMode ? 'bg-gray-750' : 'bg-gray-50'} transition-colors duration-300`}>
              <div className="flex items-center mb-4">
                <div className="w-10 h-10 rounded-full bg-purple-500 flex items-center justify-center text-white font-medium mr-3">
                  M
                </div>
                <div>
                  <h4 className="font-semibold">Maria Garcia</h4>
                  <p className="text-sm text-gray-600 dark:text-gray-400">Policy Analyst</p>
                </div>
              </div>
              <p className="text-gray-700 dark:text-gray-300 italic">
                "The interactive labs helped our team design a more effective M&E framework. The hands-on approach made all the difference."
              </p>
            </div>
          </div>
        </div>
      </div>
      
      {/* CTA Section */}
      <div className="py-16 bg-gradient-to-r from-blue-500 to-indigo-600">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-white mb-4">Ready to Create Impact?</h2>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Join thousands of change-makers using our platform to make a difference in their communities.
          </p>
          <div className="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <Link to="/courses" className="bg-white text-blue-600 hover:bg-blue-50 px-6 py-3 rounded-md font-medium text-center transition-colors duration-300">
              Get Started
            </Link>
            <Link to="/ai-tools" className="bg-transparent border-2 border-white text-white hover:bg-white hover:text-blue-600 px-6 py-3 rounded-md font-medium text-center transition-colors duration-300">
              Explore AI Tools
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

// Courses Page Component
const CoursesPage = () => {
  const [darkMode] = useContext(ThemeContext);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('All');
  const [selectedLevel, setSelectedLevel] = useState('All');
  const [bookmarkedCourses, setBookmarkedCourses] = useState([]);
  
  // Get unique tracks and levels
  const tracks = ['All', ...new Set(courseData.map(course => course.track))];
  const levels = ['All', ...new Set(courseData.map(course => course.level))];
  
  // Filter courses based on search term, track, and level
  const filteredCourses = courseData.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         course.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTrack = selectedTrack === 'All' || course.track === selectedTrack;
    const matchesLevel = selectedLevel === 'All' || course.level === selectedLevel;
    
    return matchesSearch && matchesTrack && matchesLevel;
  });
  
  // Toggle bookmark
  const toggleBookmark = (courseId) => {
    if (bookmarkedCourses.includes(courseId)) {
      setBookmarkedCourses(bookmarkedCourses.filter(id => id !== courseId));
    } else {
      setBookmarkedCourses([...bookmarkedCourses, courseId]);
    }
  };
  
  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'} transition-colors duration-300`}>
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Courses</h1>
          <p className="text-gray-600 dark:text-gray-400">Explore our comprehensive collection of courses designed to enhance your impact.</p>
        </div>
        
        <div className="flex flex-col md:flex-row gap-4 mb-8">
          <div className="relative flex-grow">
            <input
              type="text"
              placeholder="Search courses..."
              className="w-full p-3 pl-10 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <Search className="absolute left-3 top-3.5 text-gray-400" size={20} />
          </div>
          
          <div className="flex gap-4">
            <select
              className="p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={selectedTrack}
              onChange={(e) => setSelectedTrack(e.target.value)}
            >
              {tracks.map(track => (
                <option key={track} value={track}>{track}</option>
              ))}
            </select>
            
            <select
              className="p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={selectedLevel}
              onChange={(e) => setSelectedLevel(e.target.value)}
            >
              {levels.map(level => (
                <option key={level} value={level}>{level}</option>
              ))}
            </select>
          </div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCourses.map(course => (
            <div key={course.id} className={`rounded-xl overflow-hidden shadow-md ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
              <div className="p-5">
                <div className="flex justify-between items-start mb-3">
                  <div>
                    <span className={`inline-block px-2 py-1 text-xs font-semibold rounded-full ${
                      course.level === 'Beginner' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' :
                      course.level === 'Intermediate' ? 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200' :
                      'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'
                    }`}>
                      {course.level}
                    </span>
                    {course.isPremium && (
                      <span className="ml-2 inline-block px-2 py-1 text-xs font-semibold rounded-full bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200">
                        Premium
                      </span>
                    )}
                  </div>
                  <button 
                    onClick={() => toggleBookmark(course.id)}
                    className={`p-1 rounded-full ${bookmarkedCourses.includes(course.id) ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
                  >
                    <Bookmark size={20} fill={bookmarkedCourses.includes(course.id) ? 'currentColor' : 'none'} />
                  </button>
                </div>
                
                <h3 className="text-xl font-semibold mb-2">{course.title}</h3>
                <p className="text-gray-600 dark:text-gray-400 mb-4">{course.description}</p>
                
                <div className="flex items-center text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <Clock size={16} className="mr-1" />
                  <span className="mr-4">{course.duration}</span>
                  <span className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">{course.track}</span>
                </div>
                
                <div className={`p-3 rounded-lg mb-4 ${darkMode ? 'bg-gray-750' : 'bg-gray-100'} italic`}>
                  "{course.quote}"
                </div>
                
                <div className="flex justify-between items-center">
                  <a 
                    href={course.url} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="inline-flex items-center text-blue-600 dark:text-blue-400 hover:underline"
                  >
                    View course <ExternalLink size={16} className="ml-1" />
                  </a>
                  
                  {course.isPremium && (
                    <div className="text-sm text-gray-500 dark:text-gray-400 flex items-center">
                      <Shield size={14} className="mr-1" /> Password required
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
        
        {filteredCourses.length === 0 && (
          <div className="text-center py-12">
            <AlertCircle className="mx-auto text-gray-400" size={48} />
            <h3 className="mt-4 text-xl font-medium">No courses found</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-400">Try adjusting your search or filter criteria</p>
          </div>
        )}
      </div>
    </div>
  );
};

// Labs Page Component
const LabsPage = () => {
  const [darkMode] = useContext(ThemeContext);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  
  // Get unique categories and difficulties
  const categories = ['All', ...new Set(labsData.map(lab => lab.category))];
  const difficulties = ['All', ...new Set(labsData.map(lab => lab.difficulty))];
  
  // Filter labs based on search term, category, and difficulty
  const filteredLabs = labsData.filter(lab => {
    const matchesSearch = lab.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         lab.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === 'All' || lab.category === selectedCategory;
    const matchesDifficulty = selectedDifficulty === 'All' || lab.difficulty === selectedDifficulty;
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });
  
  // Get icon component by name
  const getIconComponent = (iconName) => {
    const iconMap = {
      'shield': Shield,
      'dollar-sign': DollarSign,
      'megaphone': Megaphone,
      'handshake': Handshake,
      'wrench': Wrench,
      'build': Build,
      'users': Users,
      'book-open': BookOpen,
      'lightbulb': Lightbulb,
      'target': Target
    };
    
    const IconComponent = iconMap[iconName] || FileText;
    return <IconComponent size={20} />;
  };
  
  // Get color by difficulty
  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'Beginner': return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200';
      case 'Intermediate': return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200';
      case 'Advanced': return 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200';
      default: return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200';
    }
  };
  
  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'} transition-colors duration-300`}>
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Interactive Labs</h1>
          <p className="text-gray-600 dark:text-gray-400">Hands-on learning experiences to apply your knowledge in practical scenarios.</p>
        </div>
        
        <div className="flex flex-col md:flex-row gap-4 mb-8">
          <div className="relative flex-grow">
            <input
              type="text"
              placeholder="Search labs..."
              className="w-full p-3 pl-10 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <Search className="absolute left-3 top-3.5 text-gray-400" size={20} />
          </div>
          
          <div className="flex gap-4">
            <select
              className="p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
            >
              {categories.map(category => (
                <option key={category} value={category}>{category}</option>
              ))}
            </select>
            
            <select
              className="p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value)}
            >
              {difficulties.map(difficulty => (
                <option key={difficulty} value={difficulty}>{difficulty}</option>
              ))}
            </select>
          </div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredLabs.map(lab => (
            <div key={lab.id} className={`rounded-xl overflow-hidden shadow-md ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
              <div className="p-5">
                <div className="flex justify-between items-start mb-3">
                  <div className="flex items-center">
                    <div className="w-10 h-10 rounded-lg bg-blue-100 dark:bg-blue-900 flex items-center justify-center mr-3">
                      {getIconComponent(lab.icon)}
                    </div>
                    <div>
                      <span className={`inline-block px-2 py-1 text-xs font-semibold rounded-full ${getDifficultyColor(lab.difficulty)}`}>
                        {lab.difficulty}
                      </span>
                    </div>
                  </div>
                  <span className="text-sm text-gray-500 dark:text-gray-400 flex items-center">
                    <Clock size={14} className="mr-1" /> {lab.duration} min
                  </span>
                </div>
                
                <h3 className="text-xl font-semibold mb-2">{lab.title}</h3>
                <p className="text-gray-600 dark:text-gray-400 mb-4">{lab.description}</p>
                
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-500 dark:text-gray-400">{lab.category}</span>
                  <span className={`inline-block px-2 py-1 text-xs font-semibold rounded-full ${
                    lab.status === 'Available' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' :
                    'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'
                  }`}>
                    {lab.status}
                  </span>
                </div>
                
                <a 
                  href={lab.url} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="mt-4 w-full inline-flex items-center justify-center text-center bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors duration-300"
                >
                  Launch Lab <ExternalLink size={16} className="ml-2" />
                </a>
              </div>
            </div>
          ))}
        </div>
        
        {filteredLabs.length === 0 && (
          <div className="text-center py-12">
            <AlertCircle className="mx-auto text-gray-400" size={48} />
            <h3 className="mt-4 text-xl font-medium">No labs found</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-400">Try adjusting your search or filter criteria</p>
          </div>
        )}
      </div>
    </div>
  );
};

// Resources Page Component - Card-based style matching impactmojo.in
const ResourcesPage = () => {
  const [darkMode] = useContext(ThemeContext);
  
  // Main categories for the card layout
  const resourceCategories = [
    {
      id: "cross-cutting",
      title: "Cross Cutting Resources",
      description: "Resources applicable across all tracks and disciplines",
      icon: FolderOpen,
      color: "blue",
      items: [
        { name: "Case Study Template", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/cross-cutting/case-studies/case_study_template.html" },
        { name: "Case Study Worksheets", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/cross-cutting/case-studies/case_study_worksheets.html" },
        { name: "Communication Guide", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/cross-cutting/communications/communication_guide.html" },
        { name: "Local Application Worksheet", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/cross-cutting/local-application/local_application_worksheet.html" },
        { name: "Software Tools Guide", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/cross-cutting/software-tools/software_tools_guide.html" }
      ]
    },
    {
      id: "data-analysis",
      title: "Data Analysis Track",
      description: "Resources for data analysis, statistics, and quantitative methods",
      icon: BarChart,
      color: "green",
      items: [
        { name: "Bivariate Analysis Guide", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/bivariate/bivariate_analysis_guide.html" },
        { name: "Data Literacy Handout", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/data-literacy/data_literacy_handout.html" },
        { name: "Econometrics Formula Sheet", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/econometrics/econometrics_formula_sheet.html" },
        { name: "EDA Survey Analysis", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/eda/eda_survey_handout_1.html" },
        { name: "Multivariate Analysis Template", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/multivariate/multivariate_analysis_template.html" },
        { name: "R Scripts Collection", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/scripts/r-scripts.zip" },
        { name: "Python Code Samples", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/scripts/python-samples.zip" },
        { name: "Excel Analysis Templates", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/data-analysis/excel/excel-templates.zip" }
      ]
    },
    {
      id: "gender-studies",
      title: "Gender Studies Track",
      description: "Resources focused on gender analysis, women's empowerment, and inclusion",
      icon: Users,
      color: "purple",
      items: [
        { name: "Care Economy Analysis", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/gender-studies/care-economy/care_economy_handout_1.html" },
        { name: "Data Feminism in Practice", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/gender-studies/data-feminism/data_feminism_handout_1.html" },
        { name: "Gender Studies Quick Reference", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/gender-studies/gender-studies/gender_studies_quick_reference.html" }
      ]
    },
    {
      id: "policy-economics",
      title: "Policy and Economics Track",
      description: "Resources for policy analysis, economic development, and governance",
      icon: FileText,
      color: "indigo",
      items: [
        { name: "Development Economics Problem Sets", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/policy-economics/development-economics/development_economics_problem_sets.html" },
        { name: "Livelihood Assessment Toolkit", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/policy-economics/livelihoods/livelihood_assessment_toolkit.html" },
        { name: "Policy Tracking Sheet", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/policy-economics/policy-tracking/policy_tracking_sheet.html" },
        { name: "Political Economy Framework", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/policy-economics/political-economy/political_economy_handout_1.html" }
      ]
    },
    {
      id: "research-methods",
      title: "Research Methods Track",
      description: "Resources for research design, evaluation, and qualitative methods",
      icon: Search,
      color: "red",
      items: [
        { name: "Research Assumptions Checklist", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/research-methods/assumptions/assumptions_checklist.html" },
        { name: "MLE Framework Guide", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/research-methods/mle/mel_handout_1.html" },
        { name: "Qualitative Research Handbook", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/research-methods/qualitative/qualitative_research_handout.html" },
        { name: "Research Design Worksheet", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/research-methods/design/research_design_worksheet.html" }
      ]
    },
    {
      id: "thematic",
      title: "Thematic Areas",
      description: "Resources focused on specific thematic areas and sectors",
      icon: Target,
      color: "yellow",
      items: [
        { name: "Climate Change Impact Assessment", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/thematic/climate/climate_change_handout_1.html" },
        { name: "Environmental Justice Framework", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/thematic/environmental-justice/environmental_justice_handout_1.html" },
        { name: "Constitutional Analysis Guide", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/thematic/constitution/constitution_handout_1.html" }
      ]
    },
    {
      id: "quick-reference",
      title: "Quick Reference",
      description: "Concise reference materials for key concepts and frameworks",
      icon: Bookmark,
      color: "teal",
      items: [
        { name: "Quick Reference Cards", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/quick-reference/quick_reference_cards.html" }
      ]
    },
    {
      id: "education",
      title: "Education",
      description: "Resources for education and pedagogical approaches",
      icon: BookOpen,
      color: "orange",
      items: [
        { name: "Education & Pedagogy Guide", url: "https://raw.githubusercontent.com/Varnasr/ImpactMojo/main/Handouts/education/education_pedagogy_handout.html" }
      ]
    }
  ];

  // Get color classes based on category color
  const getColorClasses = (color) => {
    switch (color) {
      case 'blue': return 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200';
      case 'green': return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200';
      case 'purple': return 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200';
      case 'indigo': return 'bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200';
      case 'red': return 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200';
      case 'yellow': return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200';
      case 'teal': return 'bg-teal-100 text-teal-800 dark:bg-teal-900 dark:text-teal-200';
      case 'orange': return 'bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200';
      default: return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200';
    }
  };

  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'} transition-colors duration-300`}>
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Resources Library</h1>
          <p className="text-gray-600 dark:text-gray-400">Browse our comprehensive collection of handouts, templates, and guides organized by category.</p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {resourceCategories.map((category) => (
            <div 
              key={category.id} 
              className={`rounded-xl overflow-hidden shadow-md ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300 hover:shadow-lg`}
            >
              <div className="p-5">
                <div className="flex items-center mb-4">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center mr-3 ${getColorClasses(category.color)}`}>
                    <category.icon size={24} />
                  </div>
                  <h3 className="text-xl font-semibold">{category.title}</h3>
                </div>
                
                <p className="text-gray-600 dark:text-gray-400 mb-4">{category.description}</p>
                
                <div className="space-y-2 mb-4">
                  {category.items.slice(0, 3).map((item, index) => (
                    <div key={index} className="flex items-center">
                      <FileText className="text-gray-400 mr-2" size={16} />
                      <span className="text-sm truncate">{item.name}</span>
                    </div>
                  ))}
                  {category.items.length > 3 && (
                    <div className="text-sm text-gray-500 dark:text-gray-400">
                      +{category.items.length - 3} more resources
                    </div>
                  )}
                </div>
                
                <a 
                  href={`https://github.com/Varnasr/ImpactMojo/tree/main/Handouts/${category.id}`}
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="inline-flex items-center text-blue-600 dark:text-blue-400 hover:underline"
                >
                  View folder on GitHub <ExternalLink size={16} className="ml-1" />
                </a>
              </div>
              
              <div className={`px-5 py-3 ${darkMode ? 'bg-gray-750' : 'bg-gray-100'} border-t border-gray-200 dark:border-gray-700`}>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-500 dark:text-gray-400">
                    {category.items.length} resources
                  </span>
                  <a 
                    href={category.items[0].url}
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-sm bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded transition-colors duration-300"
                  >
                    View Sample
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        <div className={`mt-12 p-6 rounded-xl ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md`}>
          <h2 className="text-xl font-semibold mb-4">Browse All Resources</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Explore the complete collection of resources in our GitHub repository.
          </p>
          <a 
            href="https://github.com/Varnasr/ImpactMojo/tree/main/Handouts"
            target="_blank" 
            rel="noopener noreferrer"
            className="inline-flex items-center bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors duration-300"
          >
            <Github size={20} className="mr-2" /> View on GitHub
          </a>
        </div>
      </div>
    </div>
  );
};

// AI Tools Page Component
const AIToolsPage = () => {
  const [darkMode] = useContext(ThemeContext);
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [activeTool, setActiveTool] = useState(null);
  const [toolInput, setToolInput] = useState('');
  const [toolOutput, setToolOutput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  
  // Get unique categories
  const categories = ['All', ...new Set(aiToolsData.map(tool => tool.category))];
  
  // Filter tools based on selected category
  const filteredTools = selectedCategory === 'All' 
    ? aiToolsData 
    : aiToolsData.filter(tool => tool.category === selectedCategory);
  
  // Handle tool selection
  const handleToolSelect = (tool) => {
    setActiveTool(tool);
    setToolInput(tool.exampleInput || '');
    setToolOutput('');
  };
  
  // Handle tool execution
  const handleToolExecute = async () => {
    if (!activeTool || !toolInput.trim()) return;
    
    setIsProcessing(true);
    
    // Simulate API call with timeout
    setTimeout(() => {
      // This is a mock response - in a real app, you would call an AI API
      const mockOutput = `This is a simulated output for the ${activeTool.name} tool based on your input:\n\n${toolInput}\n\nIn a real implementation, this would be replaced with actual AI-generated content.`;
      
      setToolOutput(mockOutput);
      setIsProcessing(false);
    }, 1500);
  };
  
  // Get color by tool color
  const getColorClasses = (color) => {
    switch (color) {
      case 'blue': return 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200';
      case 'green': return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200';
      case 'purple': return 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200';
      case 'red': return 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200';
      case 'indigo': return 'bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200';
      case 'orange': return 'bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200';
      default: return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200';
    }
  };
  
  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'} transition-colors duration-300`}>
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">AI Tools</h1>
          <p className="text-gray-600 dark:text-gray-400">Enhance your productivity with our collection of AI-powered tools.</p>
        </div>
        
        <div className="flex flex-col lg:flex-row gap-8">
          {/* Tools List */}
          <div className="lg:w-1/3">
            <div className="mb-6">
              <h2 className="text-xl font-semibold mb-4">Categories</h2>
              <div className="flex flex-wrap gap-2">
                {categories.map(category => (
                  <button
                    key={category}
                    onClick={() => setSelectedCategory(category)}
                    className={`px-3 py-1.5 rounded-full text-sm font-medium transition-colors duration-300 ${
                      selectedCategory === category
                        ? 'bg-blue-600 text-white'
                        : `${darkMode ? 'bg-gray-800 text-gray-300 hover:bg-gray-700' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'}`
                    }`}
                  >
                    {category}
                  </button>
                ))}
              </div>
            </div>
            
            <div className="space-y-4 max-h-[calc(100vh-250px)] overflow-y-auto pr-2">
              {filteredTools.map(tool => (
                <div
                  key={tool.id}
                  onClick={() => handleToolSelect(tool)}
                  className={`p-4 rounded-xl cursor-pointer transition-colors duration-300 ${
                    activeTool?.id === tool.id
                      ? 'ring-2 ring-blue-500 bg-blue-50 dark:bg-gray-800'
                      : `${darkMode ? 'bg-gray-800 hover:bg-gray-750' : 'bg-white hover:bg-gray-100'} shadow-md`
                  }`}
                >
                  <div className="flex items-start">
                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center mr-3 ${getColorClasses(tool.color)}`}>
                      <tool.icon size={20} />
                    </div>
                    <div className="flex-1">
                      <h3 className="font-semibold mb-1">{tool.name}</h3>
                      <p className="text-sm text-gray-600 dark:text-gray-400">{tool.description}</p>
                      <span className={`inline-block mt-2 px-2 py-1 text-xs font-semibold rounded-full ${getColorClasses(tool.color)}`}>
                        {tool.category}
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          
          {/* Tool Interface */}
          <div className="lg:w-2/3">
            {activeTool ? (
              <div className={`rounded-xl shadow-md overflow-hidden ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
                <div className="p-6 border-b border-gray-200 dark:border-gray-700">
                  <div className="flex items-center mb-4">
                    <div className={`w-12 h-12 rounded-lg flex items-center justify-center mr-4 ${getColorClasses(activeTool.color)}`}>
                      <activeTool.icon size={24} />
                    </div>
                    <div>
                      <h2 className="text-2xl font-bold">{activeTool.name}</h2>
                      <p className="text-gray-600 dark:text-gray-400">{activeTool.description}</p>
                    </div>
                  </div>
                  
                  <div className="mb-4">
                    <h3 className="font-semibold mb-2">How to Use</h3>
                    <p className="text-sm text-gray-600 dark:text-gray-400">{activeTool.howToUse}</p>
                  </div>
                </div>
                
                <div className="p-6">
                  <div className="mb-6">
                    <label htmlFor="tool-input" className="block text-sm font-medium mb-2">
                      Input
                    </label>
                    <textarea
                      id="tool-input"
                      rows={6}
                      className="w-full p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-750 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                      value={toolInput}
                      onChange={(e) => setToolInput(e.target.value)}
                      placeholder={activeTool.instructions}
                    />
                  </div>
                  
                  <div className="flex justify-end mb-6">
                    <button
                      onClick={handleToolExecute}
                      disabled={isProcessing || !toolInput.trim()}
                      className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
                    >
                      {isProcessing ? (
                        <>
                          <Loader2 className="animate-spin mr-2" size={16} /> Processing...
                        </>
                      ) : (
                        <>
                          <Sparkles className="mr-2" size={16} /> Generate
                        </>
                      )}
                    </button>
                  </div>
                  
                  {toolOutput && (
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Output
                      </label>
                      <div className="w-full p-4 rounded-lg border border-gray-300 dark:border-gray-700 bg-gray-50 dark:bg-gray-750 text-gray-900 dark:text-white whitespace-pre-wrap">
                        {toolOutput}
                      </div>
                      <div className="mt-4 flex justify-end space-x-3">
                        <button className="px-3 py-1.5 text-sm bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 rounded-md transition-colors duration-300 flex items-center">
                          <Copy size={14} className="mr-1" /> Copy
                        </button>
                        <button className="px-3 py-1.5 text-sm bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 rounded-md transition-colors duration-300 flex items-center">
                          <Download size={14} className="mr-1" /> Download
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <div className={`flex flex-col items-center justify-center h-full p-12 rounded-xl ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-md transition-colors duration-300`}>
                <Bot className="text-gray-400 mb-4" size={64} />
                <h3 className="text-xl font-semibold mb-2">Select a Tool</h3>
                <p className="text-gray-600 dark:text-gray-400 text-center">
                  Choose an AI tool from the list to get started. Each tool is designed to help you with specific tasks in your development work.
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

// Profile Page Component
const ProfilePage = () => {
  const [darkMode] = useContext(ThemeContext);
  const [user] = useContext(UserContext);
  const [activeTab, setActiveTab] = useState('overview');
  const [bookmarkedCourses, setBookmarkedCourses] = useState([]);
  const [completedCourses, setCompletedCourses] = useState([]);
  const [completedLabs, setCompletedLabs] = useState([]);
  
  // Mock data for demonstration
  useEffect(() => {
    // In a real app, this data would be fetched from a database
    setBookmarkedCourses(['C1', 'C5', 'C12']);
    setCompletedCourses(['C3', 'C8']);
    setCompletedLabs(['L2', 'L5', 'L7']);
  }, []);
  
  // Get bookmarked course details
  const bookmarkedCourseDetails = courseData.filter(course => 
    bookmarkedCourses.includes(course.id)
  );
  
  // Get completed course details
  const completedCourseDetails = courseData.filter(course => 
    completedCourses.includes(course.id)
  );
  
  // Get completed lab details
  const completedLabDetails = labsData.filter(lab => 
    completedLabs.includes(lab.id)
  );
  
  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-50 text-gray-900'} transition-colors duration-300`}>
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Your Profile</h1>
          <p className="text-gray-600 dark:text-gray-400">Manage your account and track your learning progress.</p>
        </div>
        
        <div className="flex flex-col lg:flex-row gap-8">
          {/* Profile Sidebar */}
          <div className="lg:w-1/3">
            <div className={`rounded-xl shadow-md overflow-hidden ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
              <div className="p-6 text-center border-b border-gray-200 dark:border-gray-700">
                <div className="w-24 h-24 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold text-3xl mx-auto mb-4">
                  {user.displayName ? user.displayName.charAt(0).toUpperCase() : 'U'}
                </div>
                <h2 className="text-xl font-bold">{user.displayName || 'User'}</h2>
                <p className="text-gray-600 dark:text-gray-400">{user.email}</p>
              </div>
              
              <div className="p-6">
                <div className="space-y-4">
                  <div className="flex justify-between items-center">
                    <span className="text-gray-600 dark:text-gray-400">Member since</span>
                    <span>{new Date(user.metadata.creationTime).toLocaleDateString()}</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-gray-600 dark:text-gray-400">Courses completed</span>
                    <span className="font-semibold">{completedCourses.length}</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-gray-600 dark:text-gray-400">Labs completed</span>
                    <span className="font-semibold">{completedLabs.length}</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-gray-600 dark:text-gray-400">Bookmarks</span>
                    <span className="font-semibold">{bookmarkedCourses.length}</span>
                  </div>
                </div>
                
                <button className="w-full mt-6 py-2 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 rounded-md transition-colors duration-300">
                  Edit Profile
                </button>
              </div>
            </div>
          </div>
          
          {/* Profile Content */}
          <div className="lg:w-2/3">
            <div className={`rounded-xl shadow-md overflow-hidden ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
              {/* Tabs */}
              <div className="flex border-b border-gray-200 dark:border-gray-700">
                <button
                  onClick={() => setActiveTab('overview')}
                  className={`px-6 py-3 font-medium text-sm transition-colors duration-300 ${
                    activeTab === 'overview'
                      ? 'text-blue-600 border-b-2 border-blue-600 dark:text-blue-400 dark:border-blue-400'
                      : 'text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white'
                  }`}
                >
                  Overview
                </button>
                <button
                  onClick={() => setActiveTab('courses')}
                  className={`px-6 py-3 font-medium text-sm transition-colors duration-300 ${
                    activeTab === 'courses'
                      ? 'text-blue-600 border-b-2 border-blue-600 dark:text-blue-400 dark:border-blue-400'
                      : 'text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white'
                  }`}
                >
                  Courses
                </button>
                <button
                  onClick={() => setActiveTab('labs')}
                  className={`px-6 py-3 font-medium text-sm transition-colors duration-300 ${
                    activeTab === 'labs'
                      ? 'text-blue-600 border-b-2 border-blue-600 dark:text-blue-400 dark:border-blue-400'
                      : 'text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white'
                  }`}
                >
                  Labs
                </button>
                <button
                  onClick={() => setActiveTab('settings')}
                  className={`px-6 py-3 font-medium text-sm transition-colors duration-300 ${
                    activeTab === 'settings'
                      ? 'text-blue-600 border-b-2 border-blue-600 dark:text-blue-400 dark:border-blue-400'
                      : 'text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white'
                  }`}
                >
                  Settings
                </button>
              </div>
              
              {/* Tab Content */}
              <div className="p-6">
                {activeTab === 'overview' && (
                  <div>
                    <h3 className="text-xl font-semibold mb-4">Learning Overview</h3>
                    
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                      <div className={`p-4 rounded-lg ${darkMode ? 'bg-gray-750' : 'bg-gray-100'} transition-colors duration-300`}>
                        <div className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">{completedCourses.length}</div>
                        <div className="text-sm text-gray-600 dark:text-gray-400">Courses Completed</div>
                      </div>
                      
                      <div className={`p-4 rounded-lg ${darkMode ? 'bg-gray-750' : 'bg-gray-100'} transition-colors duration-300`}>
                        <div className="text-3xl font-bold text-green-600 dark:text-green-400 mb-2">{completedLabs.length}</div>
                        <div className="text-sm text-gray-600 dark:text-gray-400">Labs Completed</div>
                      </div>
                      
                      <div className={`p-4 rounded-lg ${darkMode ? 'bg-gray-750' : 'bg-gray-100'} transition-colors duration-300`}>
                        <div className="text-3xl font-bold text-purple-600 dark:text-purple-400 mb-2">{bookmarkedCourses.length}</div>
                        <div className="text-sm text-gray-600 dark:text-gray-400">Bookmarked Courses</div>
                      </div>
                    </div>
                    
                    <div className="mb-6">
                      <h4 className="font-semibold mb-3">Recently Completed</h4>
                      <div className="space-y-3">
                        {completedCourseDetails.slice(0, 2).map(course => (
                          <div key={course.id} className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                            <div>
                              <div className="font-medium">{course.title}</div>
                              <div className="text-sm text-gray-600 dark:text-gray-400">{course.track}</div>
                            </div>
                            <div className="text-sm text-gray-500 dark:text-gray-400">Completed</div>
                          </div>
                        ))}
                        
                        {completedLabDetails.slice(0, 2).map(lab => (
                          <div key={lab.id} className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                            <div>
                              <div className="font-medium">{lab.title}</div>
                              <div className="text-sm text-gray-600 dark:text-gray-400">{lab.category}</div>
                            </div>
                            <div className="text-sm text-gray-500 dark:text-gray-400">Completed</div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}
                
                {activeTab === 'courses' && (
                  <div>
                    <h3 className="text-xl font-semibold mb-4">My Courses</h3>
                    
                    <div className="mb-6">
                      <h4 className="font-semibold mb-3 flex items-center">
                        <Bookmark className="mr-2 text-yellow-500" size={16} /> Bookmarked Courses
                      </h4>
                      
                      {bookmarkedCourseDetails.length > 0 ? (
                        <div className="space-y-3">
                          {bookmarkedCourseDetails.map(course => (
                            <div key={course.id} className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                              <div>
                                <div className="font-medium">{course.title}</div>
                                <div className="text-sm text-gray-600 dark:text-gray-400">{course.track} • {course.duration}</div>
                              </div>
                              <div className="flex space-x-2">
                                <Link to={`/courses`} className="text-blue-600 dark:text-blue-400 hover:underline">
                                  View
                                </Link>
                                <button className="text-red-600 dark:text-red-400 hover:underline">
                                  Remove
                                </button>
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <p className="text-gray-600 dark:text-gray-400 italic">You haven't bookmarked any courses yet.</p>
                      )}
                    </div>
                    
                    <div>
                      <h4 className="font-semibold mb-3 flex items-center">
                        <CheckCircle className="mr-2 text-green-500" size={16} /> Completed Courses
                      </h4>
                      
                      {completedCourseDetails.length > 0 ? (
                        <div className="space-y-3">
                          {completedCourseDetails.map(course => (
                            <div key={course.id} className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                              <div>
                                <div className="font-medium">{course.title}</div>
                                <div className="text-sm text-gray-600 dark:text-gray-400">{course.track} • {course.duration}</div>
                              </div>
                              <div className="text-sm text-gray-500 dark:text-gray-400">Completed</div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <p className="text-gray-600 dark:text-gray-400 italic">You haven't completed any courses yet.</p>
                      )}
                    </div>
                  </div>
                )}
                
                {activeTab === 'labs' && (
                  <div>
                    <h3 className="text-xl font-semibold mb-4">My Labs</h3>
                    
                    <div>
                      <h4 className="font-semibold mb-3 flex items-center">
                        <CheckCircle className="mr-2 text-green-500" size={16} /> Completed Labs
                      </h4>
                      
                      {completedLabDetails.length > 0 ? (
                        <div className="space-y-3">
                          {completedLabDetails.map(lab => (
                            <div key={lab.id} className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                              <div>
                                <div className="font-medium">{lab.title}</div>
                                <div className="text-sm text-gray-600 dark:text-gray-400">{lab.category} • {lab.duration} min</div>
                              </div>
                              <div className="text-sm text-gray-500 dark:text-gray-400">Completed</div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <p className="text-gray-600 dark:text-gray-400 italic">You haven't completed any labs yet.</p>
                      )}
                    </div>
                  </div>
                )}
                
                {activeTab === 'settings' && (
                  <div>
                    <h3 className="text-xl font-semibold mb-4">Account Settings</h3>
                    
                    <div className="space-y-6">
                      <div>
                        <h4 className="font-semibold mb-3">Notification Preferences</h4>
                        <div className="space-y-3">
                          <div className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                            <div>
                              <div className="font-medium">Email Notifications</div>
                              <div className="text-sm text-gray-600 dark:text-gray-400">Receive updates about new courses and labs</div>
                            </div>
                            <label className="relative inline-flex items-center cursor-pointer">
                              <input type="checkbox" className="sr-only peer" defaultChecked />
                              <div className="w-11 h-6 bg-gray-300 peer-focus:outline-none rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
                            </label>
                          </div>
                          
                          <div className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                            <div>
                              <div className="font-medium">Course Reminders</div>
                              <div className="text-sm text-gray-600 dark:text-gray-400">Get reminders for bookmarked courses</div>
                            </div>
                            <label className="relative inline-flex items-center cursor-pointer">
                              <input type="checkbox" className="sr-only peer" />
                              <div className="w-11 h-6 bg-gray-300 peer-focus:outline-none rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
                            </label>
                          </div>
                        </div>
                      </div>
                      
                      <div>
                        <h4 className="font-semibold mb-3">Privacy Settings</h4>
                        <div className="space-y-3">
                          <div className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                            <div>
                              <div className="font-medium">Profile Visibility</div>
                              <div className="text-sm text-gray-600 dark:text-gray-400">Make your profile visible to other users</div>
                            </div>
                            <label className="relative inline-flex items-center cursor-pointer">
                              <input type="checkbox" className="sr-only peer" defaultChecked />
                              <div className="w-11 h-6 bg-gray-300 peer-focus:outline-none rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
                            </label>
                          </div>
                          
                          <div className="flex items-center justify-between p-3 rounded-lg bg-gray-100 dark:bg-gray-750">
                            <div>
                              <div className="font-medium">Activity Sharing</div>
                              <div className="text-sm text-gray-600 dark:text-gray-400">Share your course completion activity</div>
                            </div>
                            <label className="relative inline-flex items-center cursor-pointer">
                              <input type="checkbox" className="sr-only peer" />
                              <div className="w-11 h-6 bg-gray-300 peer-focus:outline-none rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
                            </label>
                          </div>
                        </div>
                      </div>
                      
                      <div>
                        <h4 className="font-semibold mb-3">Danger Zone</h4>
                        <div className="space-y-3">
                          <button className="w-full p-3 text-left rounded-lg bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 hover:bg-red-100 dark:hover:bg-red-900/30 transition-colors duration-300">
                            <div className="font-medium">Delete Account</div>
                            <div className="text-sm">Permanently delete your account and all data</div>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Login Page Component
const LoginPage = () => {
  const [darkMode] = useContext(ThemeContext);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [signInWithGoogle] = useGoogleSignIn();
  const navigate = useNavigate();
  
  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      await signInWithEmailAndPassword(auth, email, password);
      navigate('/');
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };
  
  const handleGoogleSignIn = async () => {
    try {
      await signInWithGoogle();
      navigate('/');
    } catch (err) {
      setError(err.message);
    }
  };
  
  return (
    <div className={`min-h-screen flex items-center justify-center ${darkMode ? 'bg-gray-900' : 'bg-gray-50'} transition-colors duration-300`}>
      <div className={`max-w-md w-full p-8 rounded-xl shadow-lg ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">ImpactMojo</h1>
          <h2 className="text-2xl font-semibold">Sign in to your account</h2>
        </div>
        
        {error && (
          <div className="mb-6 p-3 bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-400 rounded-md">
            {error}
          </div>
        )}
        
        <form onSubmit={handleLogin} className="space-y-6">
          <div>
            <label htmlFor="email" className="block text-sm font-medium mb-1">
              Email address
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-750 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="you@example.com"
            />
          </div>
          
          <div>
            <label htmlFor="password" className="block text-sm font-medium mb-1">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-750 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="•••••••••"
            />
          </div>
          
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <input
                id="remember-me"
                name="remember-me"
                type="checkbox"
                className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
              <label htmlFor="remember-me" className="ml-2 block text-sm text-gray-600 dark:text-gray-400">
                Remember me
              </label>
            </div>
            
            <div className="text-sm">
              <a href="#" className="font-medium text-blue-600 hover:text-blue-500 dark:text-blue-400 dark:hover:text-blue-300">
                Forgot your password?
              </a>
            </div>
          </div>
          
          <div>
            <button
              type="submit"
              disabled={loading}
              className="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 transition-colors duration-300"
            >
              {loading ? 'Signing in...' : 'Sign in'}
            </button>
          </div>
        </form>
        
        <div className="mt-6">
          <div className="relative">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-gray-300 dark:border-gray-600"></div>
            </div>
            <div className="relative flex justify-center text-sm">
              <span className={`px-2 ${darkMode ? 'bg-gray-800 text-gray-400' : 'bg-white text-gray-600'}`}>
                Or continue with
              </span>
            </div>
          </div>
          
          <div className="mt-6">
            <button
              onClick={handleGoogleSignIn}
              className="w-full flex items-center justify-center py-3 px-4 border border-gray-300 dark:border-gray-600 rounded-lg shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-750 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-300"
            >
              <svg className="h-5 w-5 mr-2" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M12.48 10.92v3.28h7.84c-.24 1.84-.853 3.187-1.787 4.133-1.147 1.147-2.933 2.4-6.053 2.4-4.827 0-8.6-3.893-8.6-8.72s3.773-8.72 8.6-8.72c2.6 0 4.507 1.027 5.907 2.347l2.307-2.307C18.747 1.44 16.133 0 12.48 0 5.867 0 .307 5.387.307 12s5.56 12 12.173 12c3.573 0 6.267-1.173 8.373-3.36 2.16-2.16 2.84-5.213 2.84-7.667 0-.76-.053-1.467-.173-2.053H12.48z"
                />
              </svg>
              Sign in with Google
            </button>
          </div>
        </div>
        
        <div className="mt-8 text-center">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Don't have an account?{' '}
            <Link to="/signup" className="font-medium text-blue-600 hover:text-blue-500 dark:text-blue-400 dark:hover:text-blue-300">
              Sign up
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

// Signup Page Component
const SignupPage = () => {
  const [darkMode] = useContext(ThemeContext);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [signInWithGoogle] = useGoogleSignIn();
  const navigate = useNavigate();
  
  const handleSignup = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }
    
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      navigate('/');
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };
  
  const handleGoogleSignIn = async () => {
    try {
      await signInWithGoogle();
      navigate('/');
    } catch (err) {
      setError(err.message);
    }
  };
  
  return (
    <div className={`min-h-screen flex items-center justify-center ${darkMode ? 'bg-gray-900' : 'bg-gray-50'} transition-colors duration-300`}>
      <div className={`max-w-md w-full p-8 rounded-xl shadow-lg ${darkMode ? 'bg-gray-800' : 'bg-white'} transition-colors duration-300`}>
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">ImpactMojo</h1>
          <h2 className="text-2xl font-semibold">Create your account</h2>
        </div>
        
        {error && (
          <div className="mb-6 p-3 bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-400 rounded-md">
            {error}
          </div>
        )}
        
        <form onSubmit={handleSignup} className="space-y-6">
          <div>
            <label htmlFor="email" className="block text-sm font-medium mb-1">
              Email address
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-750 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="you@example.com"
            />
          </div>
          
          <div>
            <label htmlFor="password" className="block text-sm font-medium mb-1">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-750 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="•••••••••"
            />
          </div>
          
          <div>
            <label htmlFor="confirm-password" className="block text-sm font-medium mb-1">
              Confirm Password
            </label>
            <input
              id="confirm-password"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
              className="w-full p-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-750 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="•••••••••"
            />
          </div>
          
          <div className="flex items-center">
            <input
              id="terms"
              name="terms"
              type="checkbox"
              className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              required
            />
            <label htmlFor="terms" className="ml-2 block text-sm text-gray-600 dark:text-gray-400">
              I agree to the{' '}
              <a href="#" className="text-blue-600 hover:text-blue-500 dark:text-blue-400 dark:hover:text-blue-300">
                Terms and Conditions
              </a>
            </label>
          </div>
          
          <div>
            <button
              type="submit"
              disabled={loading}
              className="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 transition-colors duration-300"
            >
              {loading ? 'Creating account...' : 'Sign up'}
            </button>
          </div>
        </form>
        
        <div className="mt-6">
          <div className="relative">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-gray-300 dark:border-gray-600"></div>
            </div>
            <div className="relative flex justify-center text-sm">
              <span className={`px-2 ${darkMode ? 'bg-gray-800 text-gray-400' : 'bg-white text-gray-600'}`}>
                Or continue with
              </span>
            </div>
          </div>
          
          <div className="mt-6">
            <button
              onClick={handleGoogleSignIn}
              className="w-full flex items-center justify-center py-3 px-4 border border-gray-300 dark:border-gray-600 rounded-lg shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-750 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-300"
            >
              <svg className="h-5 w-5 mr-2" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M12.48 10.92v3.28h7.84c-.24 1.84-.853 3.187-1.787 4.133-1.147 1.147-2.933 2.4-6.053 2.4-4.827 0-8.6-3.893-8.6-8.72s3.773-8.72 8.6-8.72c2.6 0 4.507 1.027 5.907 2.347l2.307-2.307C18.747 1.44 16.133 0 12.48 0 5.867 0 .307 5.387.307 12s5.56 12 12.173 12c3.573 0 6.267-1.173 8.373-3.36 2.16-2.16 2.84-5.213 2.84-7.667 0-.76-.053-1.467-.173-2.053H12.48z"
                />
              </svg>
              Sign up with Google
            </button>
          </div>
        </div>
        
        <div className="mt-8 text-center">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Already have an account?{' '}
            <Link to="/login" className="font-medium text-blue-600 hover:text-blue-500 dark:text-blue-400 dark:hover:text-blue-300">
              Sign in
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

// Theme Provider
const ThemeProvider = ({ children }) => {
  const [darkMode, setDarkMode] = useState(false);
  
  return (
    <ThemeContext.Provider value={[darkMode, setDarkMode]}>
      {children}
    </ThemeContext.Provider>
  );
};

// User Context
export const UserContext = createContext();

// User Provider
const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });
    
    return () => unsubscribe();
  }, []);
  
  return (
    <UserContext.Provider value={user}>
      {children}
    </UserContext.Provider>
  );
};

// Google Sign In Hook
const useGoogleSignIn = () => {
  const signIn = async () => {
    try {
      await signInWithPopup(auth, googleProvider);
    } catch (error) {
      console.error("Error signing in with Google:", error);
      throw error;
    }
  };
  
  return signIn;
};

// Main App Component
function App() {
  return (
    <div className="min-h-screen">
      <ThemeProvider>
        <UserProvider>
          <Router>
            <div className="flex flex-col min-h-screen">
              <Navbar />
              <main className="flex-grow">
                <Routes>
                  <Route path="/" element={<HomePage />} />
                  <Route path="/courses" element={<CoursesPage />} />
                  <Route path="/labs" element={<LabsPage />} />
                  <Route path="/resources" element={<ResourcesPage />} />
                  <Route path="/ai-tools" element={<AIToolsPage />} />
                  <Route path="/profile" element={<ProfilePage />} />
                  <Route path="/login" element={<LoginPage />} />
                  <Route path="/signup" element={<SignupPage />} />
                </Routes>
              </main>
              <Footer />
            </div>
          </Router>
        </UserProvider>
      </ThemeProvider>
    </div>
  );
}

export default App;

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
  ClipboardList, DollarSign, Megaphone, Wrench, Handshake  // Fixed: Removed 'Build', added 'Handshake'
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
    icon: Shield,
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
    icon: DollarSign,
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
    icon: Megaphone,
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
    icon: Handshake, // Fixed: Added Handshake icon
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
    icon: Wrench,
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
    icon: Wrench, // Fixed: Changed from 'build' to Wrench
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
    icon: Users,
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
    icon: BookOpen,
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
    icon: Lightbulb,
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
    icon: Target,
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
    systemMessage: 'You are an experienced writing teacher who provides constructive, specific feedback that helps students improve. You balance encouragement with clear guidance for improvement, adapting your feedback style to the student's grade level.',
    exampleInput: `Writing: [Paste student essay here]
Type: Persuasive Essay
Grade: 10th grade
Requirements: 5 paragraphs, 3 evidence sources, counter-argument
Focus: Content and organization
Style: Encouraging with specific examples`,
    icon: Edit3,
    color: 'orange'
  },
  { 
    id: 'AI13', 
    name: 'Rubric Creator', 
    description: 'Design detailed assessment rubrics for any assignment or project', 
    category: 'Assessment',
    instructions: 'Describe your assignment, grade level, and assessment criteria. The tool creates comprehensive rubrics with performance levels, specific descriptors, and scoring guidelines.',
    howToUse: 'Steps: 1) Enter assignment description and objectives 2) Select grade level 3) List assessment criteria (3-6) 4) Choose performance levels (3-5) 5) Generate complete rubric with scoring',
    promptTemplate: `Create an assessment rubric for: {assignment}

Assignment Description: {description}
Grade Level: {grade}
Subject Area: {subject}
Assessment Criteria: {criteria}
Performance Levels: {levels}
Total Points: {points}

Please create a rubric with:
1. Clear criteria categories (3-6)
2. {levels} performance levels with descriptive labels
3. Specific, observable descriptors for each cell
4. Point values for each level
5. Clear scoring instructions
6. Space for comments/feedback
7. Overall assessment guidelines

Make descriptors specific, measurable, and aligned with learning objectives.`,
    systemMessage: 'You are an assessment specialist who designs clear, effective rubrics that provide meaningful feedback and fair evaluation. You understand how to create criteria that measure different aspects of student performance.',
    exampleInput: `Assignment: Research Paper on Climate Change
Description: 8-10 page paper with 5 sources, thesis statement, and proper citations
Grade: 12th grade Environmental Science
Criteria: Research quality, thesis development, organization, evidence use, writing mechanics
Levels: Exemplary (4), Proficient (3), Developing (2), Beginning (1)
Points: 100 total`,
    icon: ClipboardList,
    color: 'indigo'
  },
  { 
    id: 'AI14', 
    name: 'Lesson Plan Generator', 
    description: 'Create structured lesson plans with objectives, activities, and assessments', 
    category: 'Teaching',
    instructions: 'Specify your subject, topic, grade level, and duration. Include learning objectives and any special requirements. The tool creates comprehensive lesson plans with timing, materials, and differentiation strategies.',
    howToUse: 'Steps: 1) Enter subject and specific topic 2) Choose grade level and duration 3) Define 2-3 learning objectives 4) Note any special requirements 5) Generate complete lesson plan',
    promptTemplate: `Create a lesson plan for: {topic}

Subject: {subject}
Grade Level: {grade}
Duration: {duration}
Learning Objectives: {objectives}
Special Requirements: {requirements}
Class Size: {students}

Please include:
1. Lesson overview and rationale
2. Clear learning objectives with standards alignment
3. Materials and resources needed
4. Detailed lesson procedure with timing:
   - Introduction/hook (5-10 min)
   - Direct instruction (10-15 min)
   - Guided practice (15-20 min)
   - Independent practice (15-20 min)
   - Closure/assessment (5-10 min)
5. Differentiation strategies for diverse learners
6. Assessment methods and criteria
7. Extension activities and homework
8. Reflection questions for teacher

Include engaging, research-based instructional strategies.`,
    systemMessage: 'You are an experienced curriculum developer who creates standards-aligned, engaging lesson plans. You understand backward design, differentiation, and research-based instructional strategies for diverse learners.',
    exampleInput: `Topic: Introduction to Fractions
Subject: Mathematics
Grade: 4th grade
Duration: 60 minutes
Objectives: 1) Identify parts of a fraction 2) Represent fractions visually 3) Compare simple fractions
Requirements: Include manipulatives, accommodate ELL students
Students: 25 diverse learners`,
    icon: BookOpen,
    color: 'blue'
  },
  { 
    id: 'AI15', 
    name: 'Curriculum Mapper', 
    description: 'Design comprehensive curriculum maps with scope and sequence', 
    category: 'Planning',
    instructions: 'Define your subject area, grade span, and duration (semester/year). The tool creates curriculum maps with units, standards alignment, pacing guides, and assessment plans.',
    howToUse: 'Steps: 1) Enter subject area and grade span 2) Set duration (semester/year) 3) List key standards/objectives 4) Specify number of units 5) Generate complete curriculum map',
    promptTemplate: `Create a curriculum map for: {subject}

Grade Span: {grades}
Duration: {duration}
Key Standards: {standards}
Number of Units: {units}
Assessment Plan: {assessments}

Please provide:
1. Curriculum overview and philosophy
2. Year/semester at a glance calendar
3. Unit sequence with approximate timelines
4. Essential questions and enduring understandings
5. Standards alignment for each unit
6. Key vocabulary and concepts
7. Assessment plan (formative and summative)
8. Resource recommendations
9. Differentiation considerations
10. Interdisciplinary connections

Ensure logical progression and spiral review of concepts.`,
    systemMessage: 'You are a curriculum specialist with expertise in standards-based curriculum design. You create coherent, aligned curriculum maps that ensure student progression and mastery of key concepts.',
    exampleInput: `Subject: High School Biology
Grades: 9-10
Duration: Full year (36 weeks)
Standards: Next Generation Science Standards (LS1, LS2, LS3, LS4)
Units: 8 units
Assessments: Unit tests, lab reports, projects, final exam`,
    icon: FolderOpen,
    color: 'green'
  },
  { 
    id: 'AI16', 
    name: 'Project-Based Learning Designer', 
    description: 'Design engaging PBL experiences with driving questions and authentic assessments', 
    category: 'Teaching',
    instructions: 'Describe your project idea, subject area, and grade level. The tool creates complete PBL frameworks with driving questions, entry events, project calendar, and assessment plans.',
    howToUse: 'Steps: 1) Enter project concept and subject 2) Choose grade level and duration 3) Define learning objectives 4) Specify community connection 5) Generate complete PBL design',
    promptTemplate: `Design a project-based learning experience for: {project}

Subject Area: {subject}
Grade Level: {grade}
Duration: {duration}
Learning Objectives: {objectives}
Community Connection: {community}
Authentic Audience: {audience}

Please create:
1. Compelling driving question
2. Project overview and rationale
3. Entry event ideas to launch project
4. Project calendar with major milestones
5. Knowledge and skills needed
6. Scaffolding activities and workshops
7. Assessment plan (formative and summative)
8. Culminating event/presentation plan
9. Reflection activities
10. Differentiation strategies

Include opportunities for student voice, choice, and revision.`,
    systemMessage: 'You are a project-based learning expert who designs engaging, authentic learning experiences. You understand how to create rigorous projects that develop 21st-century skills while meeting academic standards.',
    exampleInput: `Project: Design a Sustainable School Garden
Subject: Environmental Science & Biology
Grade: 7th grade
Duration: 8 weeks
Objectives: Ecosystems, sustainability, data analysis, presentation skills
Community: Partner with local gardeners
Audience: School administration and parents`,
    icon: Lightbulb,
    color: 'purple'
  }
];

// Theme Provider Component
const ThemeProvider = ({ children }) => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const isDark = localStorage.getItem('darkMode') === 'true';
    setDarkMode(isDark);
  }, []);

  const toggleTheme = () => {
    const newMode = !darkMode;
    setDarkMode(newMode);
    localStorage.setItem('darkMode', newMode);
  };

  return (
    <ThemeContext.Provider value={{ darkMode, toggleTheme }}>
      <div className={darkMode ? 'dark' : ''}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
};

// Main App Component
const App = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('courses');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('All');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeTool, setActiveTool] = useState(null);
  const [toolInput, setToolInput] = useState('');
  const [toolOutput, setToolOutput] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [bookmarkedCourses, setBookmarkedCourses] = useState([]);
  const [bookmarkedLabs, setBookmarkedLabs] = useState([]);
  const [bookmarkedHandouts, setBookmarkedHandouts] = useState([]);
  const [showPremiumModal, setShowPremiumModal] = useState(false);
  const [premiumPassword, setPremiumPassword] = useState('');
  const [premiumError, setPremiumError] = useState('');
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [selectedLab, setSelectedLab] = useState(null);
  const [selectedHandout, setSelectedHandout] = useState(null);

  const navigate = useNavigate();

  // Authentication state observer
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
      setLoading(false);
      
      // Load bookmarks if user is logged in
      if (currentUser) {
        loadBookmarks(currentUser.uid);
      }
    });

    return () => unsubscribe();
  }, []);

  // Load user bookmarks from Firestore
  const loadBookmarks = async (userId) => {
    try {
      const bookmarksRef = collection(db, 'users', userId, 'bookmarks');
      const querySnapshot = await getDocs(bookmarksRef);
      
      const courses = [];
      const labs = [];
      const handouts = [];
      
      querySnapshot.forEach((doc) => {
        const bookmark = doc.data();
        if (bookmark.type === 'course') courses.push(bookmark.id);
        if (bookmark.type === 'lab') labs.push(bookmark.id);
        if (bookmark.type === 'handout') handouts.push(bookmark.id);
      });
      
      setBookmarkedCourses(courses);
      setBookmarkedLabs(labs);
      setBookmarkedHandouts(handouts);
    } catch (error) {
      console.error('Error loading bookmarks:', error);
    }
  };

  // Toggle bookmark for courses
  const toggleCourseBookmark = async (courseId) => {
    if (!user) {
      // Prompt to login
      return;
    }
    
    const newBookmarks = bookmarkedCourses.includes(courseId)
      ? bookmarkedCourses.filter(id => id !== courseId)
      : [...bookmarkedCourses, courseId];
    
    setBookmarkedCourses(newBookmarks);
    
    // Update in Firestore
    try {
      const bookmarkRef = doc(db, 'users', user.uid, 'bookmarks', courseId);
      if (newBookmarks.includes(courseId)) {
        await setDoc(bookmarkRef, {
          id: courseId,
          type: 'course',
          timestamp: new Date()
        });
      } else {
        await deleteDoc(bookmarkRef);
      }
    } catch (error) {
      console.error('Error updating bookmark:', error);
    }
  };

  // Toggle bookmark for labs
  const toggleLabBookmark = async (labId) => {
    if (!user) {
      // Prompt to login
      return;
    }
    
    const newBookmarks = bookmarkedLabs.includes(labId)
      ? bookmarkedLabs.filter(id => id !== labId)
      : [...bookmarkedLabs, labId];
    
    setBookmarkedLabs(newBookmarks);
    
    // Update in Firestore
    try {
      const bookmarkRef = doc(db, 'users', user.uid, 'bookmarks', labId);
      if (newBookmarks.includes(labId)) {
        await setDoc(bookmarkRef, {
          id: labId,
          type: 'lab',
          timestamp: new Date()
        });
      } else {
        await deleteDoc(bookmarkRef);
      }
    } catch (error) {
      console.error('Error updating bookmark:', error);
    }
  };

  // Toggle bookmark for handouts
  const toggleHandoutBookmark = async (handoutId) => {
    if (!user) {
      // Prompt to login
      return;
    }
    
    const newBookmarks = bookmarkedHandouts.includes(handoutId)
      ? bookmarkedHandouts.filter(id => id !== handoutId)
      : [...bookmarkedHandouts, handoutId];
    
    setBookmarkedHandouts(newBookmarks);
    
    // Update in Firestore
    try {
      const bookmarkRef = doc(db, 'users', user.uid, 'bookmarks', handoutId);
      if (newBookmarks.includes(handoutId)) {
        await setDoc(bookmarkRef, {
          id: handoutId,
          type: 'handout',
          timestamp: new Date()
        });
      } else {
        await deleteDoc(bookmarkRef);
      }
    } catch (error) {
      console.error('Error updating bookmark:', error);
    }
  };

  // Handle Google Sign In
  const handleGoogleSignIn = async () => {
    try {
      const result = await signInWithPopup(auth, googleProvider);
      setUser(result.user);
    } catch (error) {
      console.error('Error signing in with Google:', error);
    }
  };

  // Handle Email/Password Sign In
  const handleEmailSignIn = async (email, password) => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
    } catch (error) {
      console.error('Error signing in with email:', error);
      throw error;
    }
  };

  // Handle Email/Password Sign Up
  const handleEmailSignUp = async (email, password) => {
    try {
      await createUserWithEmailAndPassword(auth, email, password);
    } catch (error) {
      console.error('Error signing up with email:', error);
      throw error;
    }
  };

  // Handle Sign Out
  const handleSignOut = async () => {
    try {
      await firebaseSignOut(auth);
      setUser(null);
      setBookmarkedCourses([]);
      setBookmarkedLabs([]);
      setBookmarkedHandouts([]);
    } catch (error) {
      console.error('Error signing out:', error);
    }
  };

  // Filter courses based on search and track
  const filteredCourses = courseData.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         course.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTrack = selectedTrack === 'All' || course.track === selectedTrack;
    return matchesSearch && matchesTrack;
  });

  // Filter labs based on search
  const filteredLabs = labsData.filter(lab => {
    return lab.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
           lab.description.toLowerCase().includes(searchTerm.toLowerCase());
  });

  // Filter handouts based on search and track
  const filteredHandouts = handoutsData.filter(handout => {
    const matchesSearch = handout.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         handout.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTrack = selectedTrack === 'All' || handout.track === selectedTrack;
    return matchesSearch && matchesTrack;
  });

  // Filter AI tools based on search
  const filteredTools = aiToolsData.filter(tool => {
    return tool.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
           tool.description.toLowerCase().includes(searchTerm.toLowerCase());
  });

  // Get unique tracks for filter dropdown
  const tracks = ['All', ...new Set(courseData.map(course => course.track))];

  // Handle AI tool generation
  const handleToolGenerate = async () => {
    if (!activeTool || !toolInput.trim()) return;
    
    setIsGenerating(true);
    setToolOutput('');
    
    try {
      // Simulate API call to AI service
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Generate mock output based on tool type
      let output = '';
      switch (activeTool.id) {
        case 'AI1': // Policy Brief Generator
          output = `# Policy Brief: ${toolInput}

## Executive Summary
This brief outlines key policy recommendations for addressing ${toolInput.toLowerCase()}. Based on current research and best practices, we propose a multi-faceted approach that balances immediate needs with long-term sustainability.

## Background
${toolInput} represents a significant challenge requiring coordinated policy responses. Current approaches have shown limited effectiveness due to fragmented implementation and insufficient resource allocation.

## Key Findings
1. 78% of stakeholders identify ${toolInput.toLowerCase()} as a top priority
2. Existing policies lack enforcement mechanisms
3. Cross-sector collaboration remains underutilized

## Recommendations
1. Establish a dedicated task force with cross-departmental authority
2. Allocate 15% of annual budget to ${toolInput.toLowerCase()} initiatives
3. Implement quarterly progress reviews with public reporting

## Implementation Timeline
- Phase 1 (0-3 months): Task force formation and needs assessment
- Phase 2 (4-9 months): Policy development and stakeholder consultation
- Phase 3 (10-18 months): Pilot implementation and evaluation

This approach provides a comprehensive framework for addressing ${toolInput.toLowerCase()} while ensuring accountability and measurable outcomes.`;
          break;
          
        case 'AI2': // Research Question Refiner
          output = `## Analysis of Your Research Question

**Original Question:** "${toolInput}"

### Strengths:
- Addresses a relevant topic in the field
- Has potential for practical application
- Focuses on an important issue

### Areas for Improvement:
- Lacks specificity regarding population and context
- Could be more focused on measurable outcomes
- Needs clearer variables and relationships

### Refined Alternatives:

1. **"What is the impact of [specific intervention] on [measurable outcome] among [specific population] in [context] over [time period]?"**
   - More specific with clear variables
   - Identifies population and context
   - Suggests measurable outcomes

2. **"How does [independent variable] influence [dependent variable] in [specific setting], and what mediating factors affect this relationship?"**
   - Focuses on causal relationships
   - Identifies potential mediators
   - Specifies context

3. **"To what extent does [factor] explain differences in [outcome] between [group A] and [group B] when controlling for [variables]?"**
   - Comparative approach
   - Includes control variables
   - Quantifiable relationship

### Feasibility Assessment:
- **Data Availability:** Moderate - may require primary data collection
- **Methodological Complexity:** Medium to High
- **Time Requirements:** 12-18 months for comprehensive study
- **Resource Needs:** Moderate budget, research team required

### Recommended Next Steps:
1. Conduct preliminary literature review
2. Identify specific variables and measures
3. Determine appropriate methodology
4. Assess data availability and collection methods`;
          break;
          
        case 'AI3': // Data Story Creator
          output = `# Data Story: Insights from ${toolInput}

## Key Message
Our analysis reveals three critical patterns in ${toolInput.toLowerCase()} that challenge conventional wisdom and point to new opportunities for intervention.

## The Story Structure

### 1. The Unexpected Finding
Contrary to expectations, our data shows that [key finding]. This represents a significant shift from previous trends and suggests that [implication].

**Visualization Suggestion:** 
- Line chart showing trend over time with annotation at the point of change
- Color coding to highlight the deviation from expected pattern

### 2. The Underlying Cause
Further investigation revealed that [underlying factor] is driving this change. When we examined [related metric], we discovered a strong correlation (r=0.78) that explains this phenomenon.

**Visualization Suggestion:**
- Scatter plot showing the relationship between the two variables
- Heat map to show geographic or demographic patterns
- Annotated timeline of events that may have influenced the change

### 3. The Impact and Implications
This finding has significant implications for [stakeholders]. Organizations that [adaptation] are seeing [positive outcome], while those maintaining [traditional approach] are experiencing [negative consequence].

**Visualization Suggestion:**
- Bar chart comparing outcomes between different groups
- Icon-based infographic showing the impact pathway
- Interactive dashboard allowing exploration by different segments

### 4. The Call to Action
Based on these insights, we recommend three immediate actions:
1. [Specific recommendation with timeline]
2. [Specific recommendation with timeline]
3. [Specific recommendation with timeline]

**Data Presentation Tips:**
- Start with the most surprising finding to grab attention
- Use consistent color scheme throughout the story
- Include both statistical significance and practical significance
- Provide context for non-technical audiences
- End with clear, actionable next steps

## Narrative Style: Analytical
This approach works best for audiences who value data-driven decision making and need to understand the methodology behind the findings.`;
          break;
          
        default:
          output = `Generated output for ${activeTool.name} based on input: "${toolInput}"

This is a simulated response. In a real implementation, this would connect to an AI service to generate actual content based on the tool's specific prompt template and system instructions.

The output would be tailored to the specific requirements of ${activeTool.name} and would follow the structure and guidelines defined in the tool's configuration.`;
      }
      
      setToolOutput(output);
    } catch (error) {
      console.error('Error generating output:', error);
      setToolOutput('Error generating output. Please try again.');
    } finally {
      setIsGenerating(false);
    }
  };

  // Handle premium course access
  const handlePremiumAccess = (course) => {
    setSelectedCourse(course);
    setShowPremiumModal(true);
    setPremiumError('');
  };

  // Verify premium password
  const verifyPremiumPassword = () => {
    if (!selectedCourse) return;
    
    if (premiumPassword === selectedCourse.password) {
      // Access granted - redirect to course
      window.open(selectedCourse.url, '_blank');
      setShowPremiumModal(false);
      setPremiumPassword('');
    } else {
      setPremiumError('Incorrect password. Please try again.');
    }
  };

  // Get icon component by name
  const getIconComponent = (iconName) => {
    const iconMap = {
      'shield': Shield,
      'dollar-sign': DollarSign,
      'megaphone': Megaphone,
      'handshake': Handshake,
      'wrench': Wrench,
      'users': Users,
      'book-open': BookOpen,
      'lightbulb': Lightbulb,
      'target': Target,
    };
    
    return iconMap[iconName] || FileText;
  };

  // Render the app
  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50 dark:bg-gray-900">
        <div className="text-center">
          <Loader2 className="h-12 w-12 animate-spin mx-auto text-blue-600" />
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Loading ImpactMojo...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      {/* Header */}
      <header className="bg-white dark:bg-gray-800 shadow-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <div className="flex items-center">
              <Link to="/" className="flex items-center space-x-2">
                <div className="bg-blue-600 text-white p-2 rounded-lg">
                  <Zap className="h-6 w-6" />
                </div>
                <span className="text-xl font-bold text-blue-600 dark:text-blue-400">ImpactMojo</span>
              </Link>
            </div>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex space-x-8">
              <button
                onClick={() => setActiveTab('courses')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${activeTab === 'courses' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                Courses
              </button>
              <button
                onClick={() => setActiveTab('labs')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${activeTab === 'labs' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                Labs
              </button>
              <button
                onClick={() => setActiveTab('handouts')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${activeTab === 'handouts' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                Handouts
              </button>
              <button
                onClick={() => setActiveTab('tools')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${activeTab === 'tools' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                AI Tools
              </button>
            </nav>

            {/* Right side items */}
            <div className="flex items-center space-x-4">
              {/* Theme toggle */}
              <button
                onClick={() => {
                  const themeContext = useContext(ThemeContext);
                  themeContext.toggleTheme();
                }}
                className="p-2 rounded-full text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
              >
                {useContext(ThemeContext)?.darkMode ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
              </button>

              {/* User menu */}
              {user ? (
                <div className="relative">
                  <button className="flex items-center space-x-2 text-sm">
                    <div className="h-8 w-8 rounded-full bg-blue-600 flex items-center justify-center text-white font-medium">
                      {user.email ? user.email.charAt(0).toUpperCase() : 'U'}
                    </div>
                    <span className="hidden md:block">{user.displayName || user.email}</span>
                  </button>
                  <button
                    onClick={handleSignOut}
                    className="ml-4 flex items-center space-x-1 text-sm text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                  >
                    <LogOut className="h-4 w-4" />
                    <span>Sign Out</span>
                  </button>
                </div>
              ) : (
                <div className="flex items-center space-x-2">
                  <button
                    onClick={handleGoogleSignIn}
                    className="flex items-center space-x-1 text-sm text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                  >
                    <span>Sign In</span>
                  </button>
                </div>
              )}

              {/* Mobile menu button */}
              <button
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                className="md:hidden p-2 rounded-md text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
              >
                {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
              </button>
            </div>
          </div>
        </div>

        {/* Mobile menu */}
        {mobileMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white dark:bg-gray-800 shadow-lg">
              <button
                onClick={() => {
                  setActiveTab('courses');
                  setMobileMenuOpen(false);
                }}
                className={`block px-3 py-2 rounded-md text-base font-medium w-full text-left ${activeTab === 'courses' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                Courses
              </button>
              <button
                onClick={() => {
                  setActiveTab('labs');
                  setMobileMenuOpen(false);
                }}
                className={`block px-3 py-2 rounded-md text-base font-medium w-full text-left ${activeTab === 'labs' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                Labs
              </button>
              <button
                onClick={() => {
                  setActiveTab('handouts');
                  setMobileMenuOpen(false);
                }}
                className={`block px-3 py-2 rounded-md text-base font-medium w-full text-left ${activeTab === 'handouts' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                Handouts
              </button>
              <button
                onClick={() => {
                  setActiveTab('tools');
                  setMobileMenuOpen(false);
                }}
                className={`block px-3 py-2 rounded-md text-base font-medium w-full text-left ${activeTab === 'tools' ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300' : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}`}
              >
                AI Tools
              </button>
            </div>
          </div>
        )}
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Search and Filters */}
        <div className="mb-8 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div className="relative flex-1 max-w-md">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <Search className="h-5 w-5 text-gray-400" />
            </div>
            <input
              type="text"
              placeholder="Search..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="block w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
          
          {(activeTab === 'courses' || activeTab === 'handouts') && (
            <div className="flex items-center space-x-2">
              <span className="text-sm text-gray-600 dark:text-gray-300">Filter by track:</span>
              <select
                value={selectedTrack}
                onChange={(e) => setSelectedTrack(e.target.value)}
                className="block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
              >
                {tracks.map(track => (
                  <option key={track} value={track}>{track}</option>
                ))}
              </select>
            </div>
          )}
        </div>

        {/* Tab Content */}
        <div className="bg-white dark:bg-gray-800 shadow rounded-lg overflow-hidden">
          {/* Courses Tab */}
          {activeTab === 'courses' && (
            <div>
              <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
                <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200">Courses</h2>
                <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
                  Explore our comprehensive courses on development topics
                </p>
              </div>
              
              <div className="divide-y divide-gray-200 dark:divide-gray-700">
                {filteredCourses.length > 0 ? (
                  filteredCourses.map(course => (
                    <div key={course.id} className="p-6 hover:bg-gray-50 dark:hover:bg-gray-750 transition-colors">
                      <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4">
                        <div className="flex-1">
                          <div className="flex items-start justify-between">
                            <div>
                              <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100">{course.title}</h3>
                              <div className="mt-1 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200">
                                  {course.track}
                                </span>
                                <span className="inline-flex items-center">
                                  <Clock className="h-4 w-4 mr-1" />
                                  {course.duration}
                                </span>
                                <span className="inline-flex items-center">
                                  <Target className="h-4 w-4 mr-1" />
                                  {course.level}
                                </span>
                                {course.isPremium && (
                                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200">
                                    <Star className="h-3 w-3 mr-1" />
                                    Premium
                                  </span>
                                )}
                              </div>
                            </div>
                            <button
                              onClick={() => toggleCourseBookmark(course.id)}
                              className="ml-4 p-1 rounded-full text-gray-400 hover:text-yellow-500 focus:outline-none"
                            >
                              {bookmarkedCourses.includes(course.id) ? (
                                <Bookmark className="h-5 w-5 text-yellow-500 fill-current" />
                              ) : (
                                <Bookmark className="h-5 w-5" />
                              )}
                            </button>
                          </div>
                          
                          <p className="mt-3 text-gray-600 dark:text-gray-300">{course.description}</p>
                          
                          <div className="mt-4 flex items-center justify-between">
                            <blockquote className="text-sm italic text-gray-600 dark:text-gray-400 border-l-4 border-blue-500 pl-4 py-1">
                              {course.quote}
                            </blockquote>
                            
                            <div className="flex space-x-3">
                              {course.isPremium ? (
                                <button
                                  onClick={() => handlePremiumAccess(course)}
                                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-yellow-600 hover:bg-yellow-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500"
                                >
                                  <Star className="h-4 w-4 mr-2" />
                                  Unlock Premium
                                </button>
                              ) : (
                                <a
                                  href={course.url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                                >
                                  <ExternalLink className="h-4 w-4 mr-2" />
                                  Start Course
                                </a>
                              )}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="p-12 text-center">
                    <div className="mx-auto h-12 w-12 rounded-full bg-gray-100 dark:bg-gray-700 flex items-center justify-center">
                      <Search className="h-6 w-6 text-gray-400" />
                    </div>
                    <h3 className="mt-4 text-lg font-medium text-gray-900 dark:text-gray-100">No courses found</h3>
                    <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                      Try adjusting your search or filter criteria
                    </p>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Labs Tab */}
          {activeTab === 'labs' && (
            <div>
              <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
                <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200">Interactive Labs</h2>
                <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
                  Hands-on tools and simulations for practical learning
                </p>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
                {filteredLabs.length > 0 ? (
                  filteredLabs.map(lab => {
                    const IconComponent = getIconComponent(lab.icon);
                    return (
                      <div key={lab.id} className="bg-gray-50 dark:bg-gray-750 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <div className="flex items-start justify-between">
                          <div className="flex items-center">
                            <div className="flex-shrink-0 bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                              <IconComponent className="h-6 w-6 text-blue-600 dark:text-blue-400" />
                            </div>
                            <div className="ml-4">
                              <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100">{lab.title}</h3>
                              <div className="mt-1 flex items-center space-x-3 text-sm text-gray-500 dark:text-gray-400">
                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200">
                                  {lab.category}
                                </span>
                                <span className="inline-flex items-center">
                                  <Clock className="h-4 w-4 mr-1" />
                                  {lab.duration} min
                                </span>
                                <span className="inline-flex items-center">
                                  <Target className="h-4 w-4 mr-1" />
                                  {lab.difficulty}
                                </span>
                              </div>
                            </div>
                          </div>
                          <button
                            onClick={() => toggleLabBookmark(lab.id)}
                            className="p-1 rounded-full text-gray-400 hover:text-yellow-500 focus:outline-none"
                          >
                            {bookmarkedLabs.includes(lab.id) ? (
                              <Bookmark className="h-5 w-5 text-yellow-500 fill-current" />
                            ) : (
                              <Bookmark className="h-5 w-5" />
                            )}
                          </button>
                        </div>
                        
                        <p className="mt-4 text-gray-600 dark:text-gray-300">{lab.description}</p>
                        
                        <div className="mt-6 flex items-center justify-between">
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">
                            <CheckCircle className="h-3 w-3 mr-1" />
                            {lab.status}
                          </span>
                          
                          <a
                            href={lab.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                          >
                            <ExternalLink className="h-4 w-4 mr-2" />
                            Open Lab
                          </a>
                        </div>
                      </div>
                    );
                  })
                ) : (
                  <div className="col-span-full p-12 text-center">
                    <div className="mx-auto h-12 w-12 rounded-full bg-gray-100 dark:bg-gray-700 flex items-center justify-center">
                      <Search className="h-6 w-6 text-gray-400" />
                    </div>
                    <h3 className="mt-4 text-lg font-medium text-gray-900 dark:text-gray-100">No labs found</h3>
                    <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                      Try adjusting your search criteria
                    </p>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Handouts Tab */}
          {activeTab === 'handouts' && (
            <div>
              <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
                <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200">Learning Resources</h2>
                <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
                  Downloadable guides, templates, and reference materials
                </p>
              </div>
              
              <div className="divide-y divide-gray-200 dark:divide-gray-700">
                {filteredHandouts.length > 0 ? (
                  filteredHandouts.map(handout => (
                    <div key={handout.id} className="p-6 hover:bg-gray-50 dark:hover:bg-gray-750 transition-colors">
                      <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4">
                        <div className="flex-1">
                          <div className="flex items-start justify-between">
                            <div>
                              <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100">{handout.title}</h3>
                              <div className="mt-1 flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">
                                  {handout.category}
                                </span>
                                <span className="inline-flex items-center">
                                  <FileText className="h-4 w-4 mr-1" />
                                  {handout.type}
                                </span>
                                <span className="inline-flex items-center">
                                  <Target className="h-4 w-4 mr-1" />
                                  {handout.track}
                                </span>
                              </div>
                            </div>
                            <button
                              onClick={() => toggleHandoutBookmark(handout.id)}
                              className="ml-4 p-1 rounded-full text-gray-400 hover:text-yellow-500 focus:outline-none"
                            >
                              {bookmarkedHandouts.includes(handout.id) ? (
                                <Bookmark className="h-5 w-5 text-yellow-500 fill-current" />
                              ) : (
                                <Bookmark className="h-5 w-5" />
                              )}
                            </button>
                          </div>
                          
                          <p className="mt-3 text-gray-600 dark:text-gray-300">{handout.description}</p>
                          
                          <div className="mt-4 flex items-center justify-between">
                            <div className="flex space-x-3">
                              <a
                                href={handout.url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                              >
                                <Download className="h-4 w-4 mr-2" />
                                Download
                              </a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="p-12 text-center">
                    <div className="mx-auto h-12 w-12 rounded-full bg-gray-100 dark:bg-gray-700 flex items-center justify-center">
                      <Search className="h-6 w-6 text-gray-400" />
                    </div>
                    <h3 className="mt-4 text-lg font-medium text-gray-900 dark:text-gray-100">No resources found</h3>
                    <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                      Try adjusting your search or filter criteria
                    </p>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* AI Tools Tab */}
          {activeTab === 'tools' && (
            <div>
              <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
                <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200">AI-Powered Tools</h2>
                <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
                  Intelligent assistants to enhance your research and productivity
                </p>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
                {filteredTools.length > 0 ? (
                  filteredTools.map(tool => (
                    <div key={tool.id} className="bg-gray-50 dark:bg-gray-750 rounded-lg p-6 hover:shadow-md transition-shadow">
                      <div className="flex items-start">
                        <div className="flex-shrink-0 bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                          <tool.icon className={`h-6 w-6 text-${tool.color}-600 dark:text-${tool.color}-400`} />
                        </div>
                        <div className="ml-4">
                          <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100">{tool.name}</h3>
                          <div className="mt-1">
                            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200">
                              {tool.category}
                            </span>
                          </div>
                        </div>
                      </div>
                      
                      <p className="mt-4 text-gray-600 dark:text-gray-300">{tool.description}</p>
                      
                      <div className="mt-6">
                        <button
                          onClick={() => setActiveTool(tool)}
                          className="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                        >
                          <Bot className="h-4 w-4 mr-2" />
                          Use Tool
                        </button>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="col-span-full p-12 text-center">
                    <div className="mx-auto h-12 w-12 rounded-full bg-gray-100 dark:bg-gray-700 flex items-center justify-center">
                      <Search className="h-6 w-6 text-gray-400" />
                    </div>
                    <h3 className="mt-4 text-lg font-medium text-gray-900 dark:text-gray-100">No tools found</h3>
                    <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                      Try adjusting your search criteria
                    </p>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      </main>

      {/* AI Tool Modal */}
      {activeTool && (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
          <div className="relative top-20 mx-auto p-5 border w-11/12 md:w-3/4 lg:w-1/2 shadow-lg rounded-md bg-white dark:bg-gray-800">
            <div className="flex justify-between items-center pb-3">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-gray-100 flex items-center">
                <activeTool.icon className={`h-6 w-6 mr-2 text-${activeTool.color}-600 dark:text-${activeTool.color}-400`} />
                {activeTool.name}
              </h3>
              <button
                onClick={() => {
                  setActiveTool(null);
                  setToolInput('');
                  setToolOutput('');
                }}
                className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200"
              >
                <X className="h-6 w-6" />
              </button>
            </div>
            
            <div className="mt-4">
              <div className="mb-6 p-4 bg-blue-50 dark:bg-blue-900 rounded-lg">
                <h4 className="font-medium text-blue-800 dark:text-blue-200 mb-2">How to use this tool:</h4>
                <p className="text-sm text-blue-700 dark:text-blue-300">{activeTool.instructions}</p>
              </div>
              
              <div className="mb-6">
                <label htmlFor="tool-input" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Input:
                </label>
                <textarea
                  id="tool-input"
                  rows={4}
                  value={toolInput}
                  onChange={(e) => setToolInput(e.target.value)}
                  className="shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 p-3"
                  placeholder={activeTool.exampleInput || "Enter your input here..."}
                />
              </div>
              
              <div className="flex justify-end space-x-3 mb-6">
                <button
                  onClick={() => {
                    setActiveTool(null);
                    setToolInput('');
                    setToolOutput('');
                  }}
                  className="px-4 py-2 border border-gray-300 dark:border-gray-600 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
                >
                  Cancel
                </button>
                <button
                  onClick={handleToolGenerate}
                  disabled={isGenerating || !toolInput.trim()}
                  className="px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isGenerating ? (
                    <>
                      <Loader2 className="animate-spin -ml-1 mr-2 h-4 w-4" />
                      Generating...
                    </>
                  ) : (
                    <>
                      <Sparkles className="-ml-1 mr-2 h-4 w-4" />
                      Generate
                    </>
                  )}
                </button>
              </div>
              
              {toolOutput && (
                <div className="mt-6">
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Output:
                  </label>
                  <div className="bg-gray-50 dark:bg-gray-750 rounded-md p-4 border border-gray-200 dark:border-gray-700">
                    <pre className="whitespace-pre-wrap text-sm text-gray-800 dark:text-gray-200 font-sans">{toolOutput}</pre>
                  </div>
                  <div className="mt-3 flex justify-end space-x-3">
                    <button
                      onClick={() => {
                        navigator.clipboard.writeText(toolOutput);
                        // Show success message
                      }}
                      className="inline-flex items-center px-3 py-1.5 border border-gray-300 dark:border-gray-600 text-sm font-medium rounded text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
                    >
                      <Copy className="h-4 w-4 mr-1" />
                      Copy
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Premium Access Modal */}
      {showPremiumModal && selectedCourse && (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
          <div className="relative top-20 mx-auto p-5 border w-11/12 md:w-1/3 shadow-lg rounded-md bg-white dark:bg-gray-800">
            <div className="flex justify-between items-center pb-3">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-gray-100 flex items-center">
                <Star className="h-6 w-6 mr-2 text-yellow-500" />
                Premium Course Access
              </h3>
              <button
                onClick={() => {
                  setShowPremiumModal(false);
                  setSelectedCourse(null);
                  setPremiumPassword('');
                  setPremiumError('');
                }}
                className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200"
              >
                <X className="h-6 w-6" />
              </button>
            </div>
            
            <div className="mt-4">
              <div className="mb-4">
                <h4 className="font-medium text-gray-900 dark:text-gray-100">{selectedCourse.title}</h4>
                <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">{selectedCourse.description}</p>
              </div>
              
              <div className="mb-6">
                <label htmlFor="premium-password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Enter Premium Access Password:
                </label>
                <input
                  type="password"
                  id="premium-password"
                  value={premiumPassword}
                  onChange={(e) => setPremiumPassword(e.target.value)}
                  className="shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 p-3"
                  placeholder="Enter password..."
                />
                {premiumError && (
                  <p className="mt-2 text-sm text-red-600 dark:text-red-400">{premiumError}</p>
                )}
              </div>
              
              <div className="flex justify-end space-x-3">
                <button
                  onClick={() => {
                    setShowPremiumModal(false);
                    setSelectedCourse(null);
                    setPremiumPassword('');
                    setPremiumError('');
                  }}
                  className="px-4 py-2 border border-gray-300 dark:border-gray-600 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
                >
                  Cancel
                </button>
                <button
                  onClick={verifyPremiumPassword}
                  className="px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-yellow-600 hover:bg-yellow-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500"
                >
                  Unlock Course
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="md:flex md:items-center md:justify-between">
            <div className="flex justify-center md:justify-start space-x-6">
              <a href="#" className="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300">
                <Twitter className="h-6 w-6" />
              </a>
              <a href="#" className="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300">
                <Linkedin className="h-6 w-6" />
              </a>
              <a href="#" className="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300">
                <Github className="h-6 w-6" />
              </a>
            </div>
            <div className="mt-8 md:mt-0 md:order-1">
              <p className="text-center text-sm text-gray-500 dark:text-gray-400">
                &copy; 2023 ImpactMojo. All rights reserved.
              </p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

// Wrap App with ThemeProvider and Router
const AppWrapper = () => {
  return (
    <ThemeProvider>
      <Router>
        <App />
      </Router>
    </ThemeProvider>
  );
};

export default AppWrapper;

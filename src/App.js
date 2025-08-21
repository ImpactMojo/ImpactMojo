// src/App.js - Complete ImpactMojo with ALL components and pages + PREMIUM FEATURES
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Search, Bookmark, Heart, MessageCircle, 
  Download, ExternalLink, Play, Pause, SkipForward, Volume2,
  User, LogOut, ChevronRight, Star, Clock, Users, Target,
  Gamepad2, BookOpen, Mail, Phone, Globe, Twitter, Linkedin,
  Github, Coffee, Zap, TrendingUp, Award, Filter, Calendar,
  FileText, BarChart, Settings, ArrowRight, CheckCircle,
  AlertCircle, Info, HelpCircle, Share2, PlayCircle, Scale,
  Lightbulb, Compare, Send, Edit3, Brain, PenTool, FolderOpen
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

// ✅ PREMIUM LAB DATA (12 Interactive Labs) - Updated with Premium Features
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
  // 🌟 NEW PREMIUM LABS
  {
    id: "L11",
    title: "Statistical Assistant Lab",
    description: "AI-powered statistical analysis and interpretation support.",
    url: "https://stats-assistant-lab.netlify.app/",
    icon: "bar-chart",
    category: "Data Analysis",
    difficulty: "Advanced",
    duration: 90,
    status: "Available",
    isPremium: true,
    password: "STATS2025"
  },
  {
    id: "L12",
    title: "Qualitative Field Notes Lab",
    description: "Advanced tools for qualitative data collection and analysis.",
    url: "https://qual-fieldnotes-lab.netlify.app/",
    icon: "edit",
    category: "Research Methods",
    difficulty: "Intermediate",
    duration: 75,
    status: "Available",
    isPremium: true,
    password: "QUAL2025"
  }
];

// ✅ ENHANCED HANDOUTS DATA with Featured Content
const handoutsData = [
  // 🌟 FEATURED HANDOUT
  {
    id: "H0",
    title: "The Real Middle Game",
    category: "Premium Content",
    type: "Interactive Guide",
    description: "Advanced strategic framework for navigating complex development challenges.",
    url: "https://www.therealmidevthree.com/",
    track: "All Tracks",
    isFeatured: true,
    isPremium: true
  },

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

// 🌟 ENHANCED AI TOOLS DATA (13 Premium Tools)
const aiToolsData = [
  { id: 'AI1', name: 'Text Proofreader', description: 'Advanced proofreading for academic and professional texts', category: 'Writing' },
  { id: 'AI2', name: 'Sentence Starter Generator', description: 'Generate compelling opening sentences for any content', category: 'Writing' },
  { id: 'AI3', name: 'Policy Brief Generator', description: 'Generate structured policy briefs from your research', category: 'Writing' },
  { id: 'AI4', name: 'Research Question Refiner', description: 'Refine and improve your research questions', category: 'Research' },
  { id: 'AI5', name: 'Data Story Creator', description: 'Turn data insights into compelling narratives', category: 'Analysis' },
  { id: 'AI6', name: 'Grant Proposal Assistant', description: 'Help structure and improve grant proposals', category: 'Writing' },
  { id: 'AI7', name: 'Impact Measurement Framework', description: 'Design frameworks to measure social impact', category: 'Analysis' },
  { id: 'AI8', name: 'Stakeholder Mapping Tool', description: 'Identify and map project stakeholders', category: 'Planning' },
  { id: 'AI9', name: 'Literature Review Helper', description: 'Organize and synthesize academic literature', category: 'Research' },
  { id: 'AI10', name: 'Workshop Facilitator', description: 'Plan and structure workshop sessions', category: 'Planning' },
  { id: 'AI11', name: 'Survey Design Assistant', description: 'Create effective surveys and questionnaires', category: 'Research' },
  { id: 'AI12', name: 'Statistical Analysis Helper', description: 'Guide statistical analysis and interpretation', category: 'Analysis' },
  { id: 'AI13', name: 'Communication Optimizer', description: 'Optimize content for different audiences and platforms', category: 'Writing' }
];

// 🌟 PREMIUM PATHWAY QUIZ COMPONENT
const PremiumPathwayQuiz = ({ user }) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);
  const [recommendedPath, setRecommendedPath] = useState(null);

  const questions = [
    {
      id: 1,
      text: "What's your primary area of interest?",
      options: [
        { value: "gender", label: "Gender equality and social justice" },
        { value: "policy", label: "Policy analysis and governance" },
        { value: "research", label: "Research methods and evaluation" },
        { value: "data", label: "Data analysis and statistics" }
      ]
    },
    {
      id: 2,
      text: "What's your current experience level?",
      options: [
        { value: "beginner", label: "New to development work" },
        { value: "intermediate", label: "Some experience in the field" },
        { value: "advanced", label: "Seasoned professional" },
        { value: "expert", label: "Looking for advanced specialization" }
      ]
    },
    {
      id: 3,
      text: "What type of learning do you prefer?",
      options: [
        { value: "theory", label: "Theoretical frameworks and concepts" },
        { value: "practical", label: "Hands-on tools and applications" },
        { value: "mixed", label: "Combination of theory and practice" },
        { value: "research", label: "Academic research and methodology" }
      ]
    }
  ];

  const calculateRecommendation = () => {
    const { 1: interest, 2: level, 3: style } = answers;
    
    const recommendations = {
      gender: {
        title: "Gender Studies Track",
        description: "Focus on gender equality, women's empowerment, and inclusive development",
        courses: ["C1", "C2", "C3", "C4", "C5", "C6"],
        labs: ["L7", "L8"],
        color: "purple"
      },
      policy: {
        title: "Policy Analysis Track", 
        description: "Develop expertise in policy frameworks, economics, and governance",
        courses: ["C7", "C8", "C14", "C15", "C16", "C17"],
        labs: ["L3", "L5", "L6"],
        color: "blue"
      },
      research: {
        title: "Research Methods Track",
        description: "Master research design, ethics, and evaluation methodologies",
        courses: ["C9", "C10", "C12", "C22", "C27", "C31"],
        labs: ["L7", "L9", "L12"],
        color: "green"
      },
      data: {
        title: "Data Analysis Track",
        description: "Build skills in statistics, econometrics, and data interpretation",
        courses: ["C19", "C23", "C28", "C29", "C30"],
        labs: ["L11"],
        color: "red"
      }
    };

    setRecommendedPath(recommendations[interest]);
    setShowResults(true);
  };

  if (!user) return null;

  if (showResults && recommendedPath) {
    return (
      <div className="bg-gradient-to-r from-purple-600 to-blue-600 text-white py-16">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-8">
            <Award className="w-16 h-16 mx-auto mb-4 text-yellow-300" />
            <h2 className="text-3xl font-bold mb-4">Your Personalized Learning Path</h2>
            <div className={`inline-block px-4 py-2 rounded-full bg-${recommendedPath.color}-100 text-${recommendedPath.color}-800 mb-4`}>
              {recommendedPath.title}
            </div>
            <p className="text-xl mb-8">{recommendedPath.description}</p>
            <div className="grid md:grid-cols-2 gap-6 text-left">
              <div>
                <h4 className="font-bold mb-2">Recommended Courses</h4>
                <p className="text-sm opacity-90">{recommendedPath.courses.length} courses tailored for you</p>
              </div>
              <div>
                <h4 className="font-bold mb-2">Interactive Labs</h4>
                <p className="text-sm opacity-90">{recommendedPath.labs.length} hands-on learning experiences</p>
              </div>
            </div>
            <button
              onClick={() => setShowResults(false)}
              className="mt-6 bg-white text-purple-600 px-6 py-2 rounded-lg font-medium hover:bg-gray-100 transition-colors"
            >
              Retake Quiz
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-gradient-to-r from-purple-600 to-blue-600 text-white py-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-8">
          <Target className="w-16 h-16 mx-auto mb-4 text-yellow-300" />
          <h2 className="text-3xl font-bold mb-4">Find Your Learning Path</h2>
          <p className="text-xl text-blue-100">Premium pathway recommendation for logged-in users</p>
        </div>

        <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-8">
          <div className="mb-6">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-xl font-bold">Question {currentQuestion + 1} of {questions.length}</h3>
              <div className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm">
                {Math.round(((currentQuestion + 1) / questions.length) * 100)}%
              </div>
            </div>
            <div className="w-full bg-white bg-opacity-20 rounded-full h-2">
              <div 
                className="bg-yellow-300 h-2 rounded-full transition-all duration-300"
                style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
              ></div>
            </div>
          </div>

          <div className="mb-8">
            <h4 className="text-xl mb-6">{questions[currentQuestion].text}</h4>
            <div className="space-y-3">
              {questions[currentQuestion].options.map((option) => (
                <button
                  key={option.value}
                  onClick={() => setAnswers({...answers, [questions[currentQuestion].id]: option.value})}
                  className={`w-full text-left p-4 rounded-lg border-2 transition-all ${
                    answers[questions[currentQuestion].id] === option.value
                      ? 'border-yellow-300 bg-white bg-opacity-20'
                      : 'border-white border-opacity-30 hover:border-opacity-50 hover:bg-white hover:bg-opacity-10'
                  }`}
                >
                  {option.label}
                </button>
              ))}
            </div>
          </div>

          <div className="flex justify-between">
            <button
              onClick={() => setCurrentQuestion(currentQuestion - 1)}
              disabled={currentQuestion === 0}
              className="px-6 py-2 rounded-lg bg-white bg-opacity-20 hover:bg-opacity-30 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              Previous
            </button>
            {currentQuestion === questions.length - 1 ? (
              <button
                onClick={calculateRecommendation}
                disabled={!answers[questions[currentQuestion].id]}
                className="px-6 py-2 rounded-lg bg-yellow-500 text-purple-900 font-bold hover:bg-yellow-400 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                Get My Path
              </button>
            ) : (
              <button
                onClick={() => setCurrentQuestion(currentQuestion + 1)}
                disabled={!answers[questions[currentQuestion].id]}
                className="px-6 py-2 rounded-lg bg-white bg-opacity-20 hover:bg-opacity-30 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                Next
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

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
      
      setBookmarks(newBookmarks);
      
      await setDoc(doc(db, 'users', user.uid), {
        bookmarks: newBookmarks
      }, { merge: true });
    } catch (error) {
      console.error('Error updating bookmarks:', error);
    }
  };

  const value = {
    user,
    loading,
    signInWithGoogle,
    signOut,
    bookmarks,
    toggleBookmark
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

// Course Card Component
const CourseCard = ({ course, isBookmarked, onBookmark }) => {
  const { user } = useAuth();

  const handleCourseAccess = () => {
    if (course.isPremium) {
      const password = prompt(`This is a premium course. Please enter the access password:`);
      if (password === course.password) {
        window.open(course.url, '_blank');
      } else if (password !== null) {
        alert('Incorrect password. Please contact support for access.');
      }
    } else {
      window.open(course.url, '_blank');
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1">
      <div className="p-6">
        <div className="flex justify-between items-start mb-4">
          <span className="text-sm font-bold text-blue-600 dark:text-blue-400">
            {course.id}
          </span>
          <div className="flex items-center space-x-2">
            {course.isPremium && (
              <span className="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200 rounded font-medium flex items-center space-x-1">
                <Star className="w-3 h-3" />
                <span>Premium</span>
              </span>
            )}
            {user && (
              <button
                onClick={() => onBookmark(course.id)}
                className="p-1 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
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

// Handout Card Component  
const HandoutCard = ({ handout }) => {
  const getTypeIcon = (type) => {
    switch (type.toLowerCase()) {
      case 'html': return <FileText className="w-5 h-5" />;
      case 'interactive guide': return <Star className="w-5 h-5" />;
      case 'pdf': return <FileText className="w-5 h-5" />;
      case 'excel': return <BarChart className="w-5 h-5" />;
      case 'r': return <Settings className="w-5 h-5" />;
      case 'python': return <Settings className="w-5 h-5" />;
      default: return <FolderOpen className="w-5 h-5" />;
    }
  };

  const getTypeColor = (type) => {
    switch (type.toLowerCase()) {
      case 'html': return 'text-blue-600 dark:text-blue-400';
      case 'interactive guide': return 'text-purple-600 dark:text-purple-400';
      case 'pdf': return 'text-red-600 dark:text-red-400'; 
      case 'excel': return 'text-green-600 dark:text-green-400';
      case 'r': return 'text-purple-600 dark:text-purple-400';
      case 'python': return 'text-yellow-600 dark:text-yellow-400';
      default: return 'text-gray-600 dark:text-gray-400';
    }
  };

  const handleDownload = () => {
    if (handout.isPremium) {
      window.open(handout.url, '_blank');
    } else {
      // For now, show alert since files need to be uploaded
      alert(`${handout.title} - File will be available after upload to GitHub. URL: ${handout.url}`);
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1">
      <div className="p-6">
        <div className="flex justify-between items-start mb-4">
          <span className="text-sm font-bold text-green-600 dark:text-green-400">
            {handout.id}
          </span>
          <div className="flex items-center space-x-2">
            {handout.isPremium && (
              <span className="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200 rounded font-medium flex items-center space-x-1">
                <Star className="w-3 h-3" />
                <span>Premium</span>
              </span>
            )}
            <div className={`p-2 rounded-lg bg-gray-100 dark:bg-gray-700 ${getTypeColor(handout.type)}`}>
              {getTypeIcon(handout.type)}
            </div>
          </div>
        </div>
        
        <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">
          {handout.title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-300 mb-4 line-clamp-3">
          {handout.description}
        </p>
        
        <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
          <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 px-2 py-1 rounded">
            {handout.category}
          </span>
          <span className="bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 px-2 py-1 rounded">
            {handout.type}
          </span>
        </div>
        
        <div className="mb-4">
          <span className="text-xs text-gray-500 dark:text-gray-400">Track: {handout.track}</span>
        </div>
        
        <button
          onClick={handleDownload}
          className="w-full bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
        >
          <Download className="w-4 h-4" />
          <span>{handout.isPremium ? 'Access Premium' : 'Download'}</span>
        </button>
      </div>
    </div>
  );
};

// HomePage Component
const HomePage = ({ setCurrentPage }) => {
  const { user } = useAuth();
  
  const featuredCourses = courseData.slice(0, 6);
  const tracks = [
    { name: 'Gender Studies', color: 'purple', courses: courseData.filter(c => c.track === 'Gender Studies').length },
    { name: 'Policy Analysis', color: 'blue', courses: courseData.filter(c => c.track === 'Policy Analysis').length },
    { name: 'Research Methods', color: 'green', courses: courseData.filter(c => c.track === 'Research Methods').length },
    { name: 'Data Analysis', color: 'red', courses: courseData.filter(c => c.track === 'Data Analysis').length }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-blue-600 via-purple-600 to-blue-800 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="mb-8">
            <Zap className="w-16 h-16 mx-auto mb-4 text-yellow-300" />
            <h1 className="text-5xl md:text-6xl font-bold mb-6">
              ImpactMojo
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-blue-100">
              101 Knowledge Series for Social Impact
            </p>
            <p className="text-lg mb-8 max-w-3xl mx-auto text-blue-100">
              A curated library exploring justice, equity, and development in South Asia. 
              Learn from 37 courses, 12 interactive labs, and comprehensive handouts.
            </p>
          </div>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => setCurrentPage('courses')}
              className="bg-white text-blue-600 font-bold py-3 px-8 rounded-lg hover:bg-blue-50 transition-colors flex items-center justify-center space-x-2"
            >
              <BookOpen className="w-5 h-5" />
              <span>Browse Courses</span>
            </button>
            {user ? (
              <button
                onClick={() => setCurrentPage('dashboard')}
                className="bg-transparent border-2 border-white text-white font-bold py-3 px-8 rounded-lg hover:bg-white hover:text-blue-600 transition-colors"
              >
                Go to Dashboard
              </button>
            ) : (
              <button
                onClick={() => setCurrentPage('about')}
                className="bg-transparent border-2 border-white text-white font-bold py-3 px-8 rounded-lg hover:bg-white hover:text-blue-600 transition-colors"
              >
                Learn More
              </button>
            )}
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white dark:bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">37</div>
              <div className="text-gray-600 dark:text-gray-300">Courses</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-green-600 dark:text-green-400 mb-2">12</div>
              <div className="text-gray-600 dark:text-gray-300">Interactive Labs</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-orange-600 dark:text-orange-400 mb-2">30</div>
              <div className="text-gray-600 dark:text-gray-300">Handouts</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-red-600 dark:text-red-400 mb-2">Free</div>
              <div className="text-gray-600 dark:text-gray-300">Open Source</div>
            </div>
          </div>
        </div>
      </section>

      {/* 🌟 PREMIUM PATHWAY QUIZ */}
      <PremiumPathwayQuiz user={user} />

      {/* Learning Tracks */}
      <section className="py-16 bg-gray-50 dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-900 dark:text-white">
            Learning Tracks
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {tracks.map(track => (
              <div key={track.name} className="bg-white dark:bg-gray-800 rounded-lg p-6 hover:shadow-lg transition-shadow">
                <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">{track.name}</h3>
                <p className="text-gray-600 dark:text-gray-300 mb-4">{track.courses} courses available</p>
                <button
                  onClick={() => setCurrentPage('courses')}
                  className="text-blue-600 dark:text-blue-400 font-medium hover:underline"
                >
                  Explore Track →
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Courses */}
      <section className="py-16 bg-white dark:bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-900 dark:text-white">
            Featured Courses
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredCourses.map(course => (
              <CourseCard 
                key={course.id} 
                course={course} 
                isBookmarked={false}
                onBookmark={() => {}}
              />
            ))}
          </div>
          <div className="text-center mt-8">
            <button
              onClick={() => setCurrentPage('courses')}
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg transition-colors"
            >
              View All Courses
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};

// Courses Page Component
const CoursesPage = () => {
  const { user, bookmarks, toggleBookmark } = useAuth();
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
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8">
          <div className="grid md:grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium mb-2">Search</label>
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  placeholder="Search courses..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Track</label>
              <select
                value={selectedTrack}
                onChange={(e) => setSelectedTrack(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="all">All Tracks</option>
                {uniqueTracks.map(track => (
                  <option key={track} value={track}>{track}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Level</label>
              <select
                value={selectedLevel}
                onChange={(e) => setSelectedLevel(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
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
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredCourses.map(course => (
            <CourseCard
              key={course.id}
              course={course}
              isBookmarked={bookmarks.includes(course.id)}
              onBookmark={toggleBookmark}
            />
          ))}
        </div>

        {filteredCourses.length === 0 && (
          <div className="text-center py-12">
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

// 🌟 ENHANCED Labs Page Component with Premium Features
const LabsPage = () => {
  const { user } = useAuth();

  const handleLabAccess = (lab) => {
    if (lab.isPremium && !user) {
      alert('Please sign in to access premium labs.');
      return;
    }
    
    if (lab.isPremium) {
      const password = prompt(`This is a premium lab. Please enter the access password:`);
      if (password === lab.password) {
        window.open(lab.url, '_blank');
      } else if (password !== null) {
        alert('Incorrect password. Please contact support for access.');
      }
    } else if (lab.status === 'Available') {
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
            12 hands-on labs for real-world practice and skill development
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {labsData.map(lab => (
            <div key={lab.id} className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <span className="text-sm font-bold text-green-600 dark:text-green-400">
                    {lab.id}
                  </span>
                  <div className="flex items-center space-x-2">
                    {lab.isPremium && (
                      <span className="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200 rounded font-medium flex items-center space-x-1">
                        <Star className="w-3 h-3" />
                        <span>Premium</span>
                      </span>
                    )}
                    <span className={`px-2 py-1 rounded-lg text-xs font-medium ${
                      lab.status === 'Available' 
                        ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                        : 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'
                    }`}>
                      {lab.status}
                    </span>
                  </div>
                </div>
                
                <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">
                  {lab.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 mb-4">
                  {lab.description}
                </p>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded">
                    {lab.category}
                  </span>
                  <span className="flex items-center">
                    <Clock className="w-4 h-4 mr-1" />
                    {lab.duration} min
                  </span>
                </div>
                
                <div className="mb-4">
                  <span className={`text-xs px-2 py-1 rounded ${
                    lab.difficulty === 'Beginner' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' :
                    lab.difficulty === 'Intermediate' ? 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200' :
                    'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'
                  }`}>
                    {lab.difficulty}
                  </span>
                </div>
                
                <button
                  onClick={() => handleLabAccess(lab)}
                  disabled={lab.status !== 'Available'}
                  className={`w-full font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2 ${
                    lab.status === 'Available'
                      ? 'bg-green-600 hover:bg-green-700 text-white'
                      : 'bg-gray-300 dark:bg-gray-600 text-gray-500 dark:text-gray-400 cursor-not-allowed'
                  }`}
                >
                  <PlayCircle className="w-4 h-4" />
                  <span>{lab.status === 'Available' ? (lab.isPremium ? 'Launch Premium Lab' : 'Launch Lab') : 'Coming Soon'}</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// 🌟 ENHANCED Handouts Page Component with Featured Content
const HandoutsPage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedTrack, setSelectedTrack] = useState('all');

  const filteredHandouts = handoutsData.filter(handout => {
    const matchesSearch = handout.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         handout.description.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategory = selectedCategory === 'all' || handout.category === selectedCategory;
    const matchesTrack = selectedTrack === 'all' || handout.track === selectedTrack;
    return matchesSearch && matchesCategory && matchesTrack;
  });

  const uniqueCategories = [...new Set(handoutsData.map(handout => handout.category))];
  const uniqueTracks = [...new Set(handoutsData.map(handout => handout.track))];
  const featuredHandout = handoutsData.find(handout => handout.isFeatured);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Handouts & Resources
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Downloadable guides, templates, and reference materials for your development work
          </p>
        </div>

        {/* Search and Filters */}
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8">
          <div className="grid md:grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium mb-2">Search</label>
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  placeholder="Search handouts..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Category</label>
              <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="all">All Categories</option>
                {uniqueCategories.map(category => (
                  <option key={category} value={category}>{category}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Track</label>
              <select
                value={selectedTrack}
                onChange={(e) => setSelectedTrack(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="all">All Tracks</option>
                {uniqueTracks.map(track => (
                  <option key={track} value={track}>{track}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* 🌟 FEATURED CONTENT SECTION */}
        {featuredHandout && (
          <div className="mb-8">
            <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-white flex items-center">
              <Star className="w-6 h-6 text-yellow-500 mr-2" />
              Featured Resource
            </h2>
            <div className="bg-gradient-to-r from-purple-600 to-blue-600 rounded-xl p-8 text-white">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center space-x-2 mb-4">
                    <span className="px-3 py-1 bg-yellow-400 text-purple-900 rounded-full text-sm font-bold">
                      Premium
                    </span>
                    <span className="px-3 py-1 bg-white bg-opacity-20 rounded-full text-sm">
                      {featuredHandout.type}
                    </span>
                  </div>
                  <h3 className="text-3xl font-bold mb-4">{featuredHandout.title}</h3>
                  <p className="text-xl mb-6 text-blue-100">{featuredHandout.description}</p>
                  <button
                    onClick={() => window.open(featuredHandout.url, '_blank')}
                    className="bg-white text-purple-600 px-6 py-3 rounded-lg font-bold hover:bg-gray-100 transition-colors flex items-center space-x-2"
                  >
                    <ExternalLink className="w-5 h-5" />
                    <span>Access Featured Resource</span>
                  </button>
                </div>
                <div className="ml-8 hidden md:block">
                  <div className="w-24 h-24 bg-white bg-opacity-20 rounded-full flex items-center justify-center">
                    <Star className="w-12 h-12 text-yellow-300" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Handouts Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredHandouts.filter(handout => !handout.isFeatured).map(handout => (
            <HandoutCard
              key={handout.id}
              handout={handout}
            />
          ))}
        </div>

        {filteredHandouts.filter(handout => !handout.isFeatured).length === 0 && (
          <div className="text-center py-12">
            <Search className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
              No handouts found
            </h3>
            <p className="text-gray-600 dark:text-gray-300">
              Try adjusting your search criteria
            </p>
          </div>
        )}

        {/* Upload Notice */}
        <div className="mt-8 bg-yellow-50 dark:bg-yellow-900 border border-yellow-200 dark:border-yellow-700 rounded-lg p-6">
          <div className="flex items-start">
            <AlertCircle className="w-5 h-5 text-yellow-600 dark:text-yellow-400 mr-3 mt-0.5" />
            <div>
              <h3 className="text-sm font-medium text-yellow-800 dark:text-yellow-200 mb-1">
                Files Currently Being Uploaded
              </h3>
              <p className="text-sm text-yellow-700 dark:text-yellow-300">
                Handout files are being uploaded to the repository. Download links will be active once the files are available.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// AI Tools Page Component
const AIToolsPage = () => {
  const { user } = useAuth();
  const [selectedTool, setSelectedTool] = useState(null);
  const [userInput, setUserInput] = useState('');
  const [toolOutput, setToolOutput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleToolUse = async () => {
    if (!userInput.trim() || !selectedTool) return;
    
    setIsProcessing(true);
    setToolOutput('');
    
    try {
      // Firebase Cloud Function URL for your project
      const response = await fetch('https://us-central1-impactmojo.cloudfunctions.net/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          toolId: selectedTool.id,
          toolName: selectedTool.name,
          userInput: userInput,
          userId: user?.uid
        })
      });

      if (!response.ok) {
        throw new Error('Failed to process request');
      }

      const data = await response.json();
      setToolOutput(data.output || 'Tool processed successfully!');
    } catch (error) {
      console.error('Error using AI tool:', error);
      setToolOutput('Sorry, there was an error processing your request. Please try again.');
    } finally {
      setIsProcessing(false);
    }
  };

  if (!user) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <Brain className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
            AI Tools Access
          </h2>
          <p className="text-gray-600 dark:text-gray-300 mb-8">
            Please sign in to access our AI-powered tools for development work.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            AI Tools
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            13 AI-powered tools to enhance your development work
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Tools List */}
          <div className="lg:col-span-1">
            <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-white">Available Tools</h2>
            <div className="space-y-3">
              {aiToolsData.map(tool => (
                <button
                  key={tool.id}
                  onClick={() => setSelectedTool(tool)}
                  className={`w-full text-left p-4 rounded-lg border transition-colors ${
                    selectedTool?.id === tool.id
                      ? 'bg-blue-50 dark:bg-blue-900 border-blue-200 dark:border-blue-700'
                      : 'bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                  }`}
                >
                  <h3 className="font-medium text-gray-900 dark:text-white">{tool.name}</h3>
                  <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{tool.description}</p>
                  <span className="inline-block mt-2 px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 rounded">
                    {tool.category}
                  </span>
                </button>
              ))}
            </div>
          </div>

          {/* Tool Interface */}
          <div className="lg:col-span-2">
            {selectedTool ? (
              <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
                <h2 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">
                  {selectedTool.name}
                </h2>
                <p className="text-gray-600 dark:text-gray-300 mb-6">
                  {selectedTool.description}
                </p>
                
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                      Your Input
                    </label>
                    <textarea
                      value={userInput}
                      onChange={(e) => setUserInput(e.target.value)}
                      placeholder={`Enter your content for ${selectedTool.name}...`}
                      rows={6}
                      className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                    />
                  </div>
                  
                  <button
                    onClick={handleToolUse}
                    disabled={!userInput.trim() || isProcessing}
                    className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-medium py-2 px-6 rounded-lg transition-colors flex items-center space-x-2"
                  >
                    <Brain className="w-4 h-4" />
                    <span>{isProcessing ? 'Processing...' : `Generate ${selectedTool.name}`}</span>
                  </button>
                  
                  {toolOutput && (
                    <div>
                      <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">Output</label>
                      <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg border">
                        <pre className="whitespace-pre-wrap text-sm text-gray-900 dark:text-white">{toolOutput}</pre>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <div className="bg-white dark:bg-gray-800 rounded-lg p-6 text-center">
                <Brain className="w-12 h-12 text-gray-400 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
                  Select an AI Tool
                </h3>
                <p className="text-gray-600 dark:text-gray-300">
                  Choose a tool from the left to get started
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

// Dashboard Page Component
const DashboardPage = () => {
  const { user, bookmarks } = useAuth();
  const bookmarkedCourses = courseData.filter(course => bookmarks.includes(course.id));

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Your Dashboard
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Welcome back, {user?.displayName}!
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Bookmarked Courses */}
          <div className="lg:col-span-2">
            <h2 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">Bookmarked Courses</h2>
            {bookmarkedCourses.length > 0 ? (
              <div className="grid md:grid-cols-2 gap-6">
                {bookmarkedCourses.map(course => (
                  <CourseCard 
                    key={course.id} 
                    course={course} 
                    isBookmarked={true}
                    onBookmark={() => {}}
                  />
                ))}
              </div>
            ) : (
              <div className="text-center py-12 bg-white dark:bg-gray-800 rounded-lg">
                <Bookmark className="w-12 h-12 text-gray-400 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
                  No bookmarked courses yet
                </h3>
                <p className="text-gray-600 dark:text-gray-300">
                  Start bookmarking courses you're interested in!
                </p>
              </div>
            )}
          </div>

          {/* Profile & Stats */}
          <div className="space-y-6">
            <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
              <h3 className="text-lg font-bold mb-4 text-gray-900 dark:text-white">Profile</h3>
              <div className="flex items-center space-x-4">
                <img 
                  src={user?.photoURL} 
                  alt={user?.displayName}
                  className="w-16 h-16 rounded-full"
                />
                <div>
                  <h4 className="font-medium text-gray-900 dark:text-white">{user?.displayName}</h4>
                  <p className="text-sm text-gray-600 dark:text-gray-300">{user?.email}</p>
                </div>
              </div>
            </div>

            <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
              <h3 className="text-lg font-bold mb-4 text-gray-900 dark:text-white">Your Stats</h3>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-gray-600 dark:text-gray-300">Handouts</span>
                  <span className="font-medium text-gray-900 dark:text-white">30</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600 dark:text-gray-300">AI Tools</span>
                  <span className="font-medium text-gray-900 dark:text-white">13</span>
                </div>
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
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    try {
      const response = await fetch('https://formspree.io/f/xpwdvgzp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        setSubmitted(true);
        setFormData({ name: '', email: '', subject: '', message: '' });
      }
    } catch (error) {
      console.error('Error submitting form:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8 text-center">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Contact Us
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Get in touch with the ImpactMojo team
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Contact Form */}
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
            <h2 className="text-xl font-bold mb-6 text-gray-900 dark:text-white">Send us a message</h2>
            
            {submitted ? (
              <div className="text-center py-8">
                <CheckCircle className="w-16 h-16 text-green-500 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
                  Message sent successfully!
                </h3>
                <p className="text-gray-600 dark:text-gray-300">
                  We'll get back to you as soon as possible.
                </p>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                    Name
                  </label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                    Email
                  </label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                    Subject
                  </label>
                  <input
                    type="text"
                    name="subject"
                    value={formData.subject}
                    onChange={handleChange}
                    required
                    className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                    Message
                  </label>
                  <textarea
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    required
                    rows={6}
                    className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  />
                </div>
                
                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
                >
                  <Send className="w-4 h-4" />
                  <span>{isSubmitting ? 'Sending...' : 'Send Message'}</span>
                </button>
              </form>
            )}
          </div>

          {/* Contact Info */}
          <div className="space-y-6">
            <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
              <h3 className="text-lg font-bold mb-4 text-gray-900 dark:text-white">Get in Touch</h3>
              <div className="space-y-4">
                <div className="flex items-center space-x-3">
                  <Mail className="w-5 h-5 text-blue-600" />
                  <span className="text-gray-600 dark:text-gray-300">hello@impactmojo.in</span>
                </div>
                <div className="flex items-center space-x-3">
                  <Globe className="w-5 h-5 text-blue-600" />
                  <span className="text-gray-600 dark:text-gray-300">www.impactmojo.in</span>
                </div>
                <div className="flex items-center space-x-3">
                  <Github className="w-5 h-5 text-blue-600" />
                  <a 
                    href="https://github.com/Varnasr/ImpactMojo" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-600 dark:text-gray-300 hover:text-blue-600"
                  >
                    GitHub Repository
                  </a>
                </div>
              </div>
            </div>

            <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
              <h3 className="text-lg font-bold mb-4 text-gray-900 dark:text-white">Office Hours</h3>
              <div className="space-y-2 text-gray-600 dark:text-gray-300">
                <p>Monday - Friday: 9:00 AM - 6:00 PM IST</p>
                <p>Saturday: 10:00 AM - 4:00 PM IST</p>
                <p>Sunday: Closed</p>
              </div>
            </div>

            <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
              <h3 className="text-lg font-bold mb-4 text-gray-900 dark:text-white">Follow Us</h3>
              <div className="flex space-x-4">
                <a href="#" className="text-gray-400 hover:text-blue-600">
                  <Twitter className="w-6 h-6" />
                </a>
                <a href="#" className="text-gray-400 hover:text-blue-600">
                  <Linkedin className="w-6 h-6" />
                </a>
                <a href="https://github.com/Varnasr/ImpactMojo" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-blue-600">
                  <Github className="w-6 h-6" />
                </a>
              </div>
            </div>
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
        <div className="mb-8 text-center">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            About ImpactMojo
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            101 Knowledge Series for Social Impact
          </p>
        </div>

        <div className="space-y-8">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
            <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Our Mission</h2>
            <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
              ImpactMojo is a curated library of knowledge decks exploring justice, equity, and development 
              in South Asia. We aim to democratize access to high-quality educational content that helps 
              build understanding of complex social issues and empowers individuals to create positive change 
              in their communities.
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
            <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">What We Offer</h2>
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <h3 className="text-lg font-medium mb-2 text-gray-900 dark:text-white">📚 37 Comprehensive Courses</h3>
                <p className="text-gray-600 dark:text-gray-300">
                  From development economics to gender studies, our courses cover essential topics for social impact work.
                </p>
              </div>
              <div>
                <h3 className="text-lg font-medium mb-2 text-gray-900 dark:text-white">🔬 12 Interactive Labs</h3>
                <p className="text-gray-600 dark:text-gray-300">
                  Hands-on simulations and tools to practice concepts in real-world scenarios.
                </p>
              </div>
              <div>
                <h3 className="text-lg font-medium mb-2 text-gray-900 dark:text-white">📁 30 Handouts & Resources</h3>
                <p className="text-gray-600 dark:text-gray-300">
                  Downloadable guides, templates, and reference materials for practical application.
                </p>
              </div>
              <div>
                <h3 className="text-lg font-medium mb-2 text-gray-900 dark:text-white">🌏 South Asia Focus</h3>
                <p className="text-gray-600 dark:text-gray-300">
                  Context-specific content that addresses the unique challenges and opportunities in the region.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
            <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Learning Tracks</h2>
            <div className="grid md:grid-cols-2 gap-4">
              <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-4">
                <h3 className="font-medium text-purple-600 dark:text-purple-400">Gender Studies</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">
                  Gender theory, women's empowerment, and inclusive development
                </p>
              </div>
              <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-4">
                <h3 className="font-medium text-blue-600 dark:text-blue-400">Policy Analysis</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">
                  Policy frameworks, economic theory, and governance
                </p>
              </div>
              <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-4">
                <h3 className="font-medium text-green-600 dark:text-green-400">Research Methods</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">
                  Research design, ethics, and community engagement approaches
                </p>
              </div>
              <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-4">
                <h3 className="font-medium text-red-600 dark:text-red-400">Data Analysis</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">
                  Statistical methods, econometrics, and data literacy
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
            <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Open Source</h2>
            <p className="text-gray-600 dark:text-gray-300 leading-relaxed mb-4">
              ImpactMojo is released under the MIT License, making it free for everyone to use, modify, and distribute. 
              We believe in the power of open collaboration to improve education and welcome contributions from the community.
            </p>
            <a
              href="https://github.com/Varnasr/ImpactMojo"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-2 text-blue-600 dark:text-blue-400 hover:underline"
            >
              <Github className="w-5 h-5" />
              <span>View Source Code</span>
            </a>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg p-6">
            <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Disclaimer</h2>
            <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
              ImpactMojo is an educational resource and does not provide official certifications or endorsements. 
              The content is designed for learning purposes and should be supplemented with formal education and 
              professional development as appropriate for your goals.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

// Navigation Component 
const Navigation = ({ darkMode, setDarkMode, currentPage, setCurrentPage }) => {
  const { user, signInWithGoogle, signOut } = useAuth();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navItems = [
    { id: 'home', label: 'Home', requiresAuth: false },
    { id: 'courses', label: 'Courses', requiresAuth: false },
    { id: 'labs', label: 'Labs', requiresAuth: false },
    { id: 'handouts', label: 'Handouts', requiresAuth: false },
    { id: 'dashboard', label: 'Dashboard', requiresAuth: true },
    { id: 'ai-tools', label: 'AI Tools', requiresAuth: true },
    { id: 'contact', label: 'Contact', requiresAuth: false },
    { id: 'about', label: 'About', requiresAuth: false }
  ];

  return (
    <nav className="bg-white dark:bg-gray-900 shadow-lg sticky top-0 z-40">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <div className="flex items-center">
            <button
              onClick={() => setCurrentPage('home')}
              className="flex items-center space-x-2 text-xl font-bold text-blue-600 dark:text-blue-400"
            >
              <Zap className="w-8 h-8" />
              <span>ImpactMojo</span>
            </button>
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-6">
            {navItems.map(item => {
              if (item.requiresAuth && !user) return null;
              return (
                <button
                  key={item.id}
                  onClick={() => setCurrentPage(item.id)}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                    currentPage === item.id
                      ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-200'
                      : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
                  }`}
                >
                  {item.label}
                </button>
              );
            })}
          </div>

          {/* Right side controls */}
          <div className="flex items-center space-x-4">
            {/* Dark mode toggle */}
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
            >
              {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
            </button>

            {/* Authentication */}
            {user ? (
              <div className="flex items-center space-x-3">
                <img 
                  src={user.photoURL} 
                  alt={user.displayName}
                  className="w-8 h-8 rounded-full"
                />
                <button
                  onClick={signOut}
                  className="flex items-center space-x-2 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                >
                  <LogOut className="w-4 h-4" />
                  <span className="hidden sm:block">Sign Out</span>
                </button>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors flex items-center space-x-2"
              >
                <User className="w-4 h-4" />
                <span>Sign In</span>
              </button>
            )}

            {/* Mobile menu button */}
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden p-2 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
            >
              {isMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-200 dark:border-gray-700">
            <div className="flex flex-col space-y-2">
              {navItems.map(item => {
                if (item.requiresAuth && !user) return null;
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      setCurrentPage(item.id);
                      setIsMenuOpen(false);
                    }}
                    className={`text-left px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                      currentPage === item.id
                        ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-200'
                        : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
                    }`}
                  >
                    {item.label}
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

// Main App Component
function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [currentPage, setCurrentPage] = useState('home');
  const [showCookieConsent, setShowCookieConsent] = useState(true);

  useEffect(() => {
    const savedDarkMode = localStorage.getItem('darkMode');
    if (savedDarkMode) {
      setDarkMode(JSON.parse(savedDarkMode));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const handleCookieAccept = () => {
    setShowCookieConsent(false);
    localStorage.setItem('cookieConsent', 'true');
  };

  useEffect(() => {
    const cookieConsent = localStorage.getItem('cookieConsent');
    if (cookieConsent) {
      setShowCookieConsent(false);
    }
  }, []);

  return (
    <AuthProvider>
      <div className={`min-h-screen ${darkMode ? 'dark' : ''}`}>
        <div className="min-h-screen bg-white dark:bg-gray-900 text-gray-900 dark:text-white transition-colors">
          <Navigation 
            darkMode={darkMode}
            setDarkMode={setDarkMode}
            currentPage={currentPage}
            setCurrentPage={setCurrentPage}
          />
          
          <main className="pt-0">
            {currentPage === 'home' && <HomePage setCurrentPage={setCurrentPage} />}
            {currentPage === 'courses' && <CoursesPage />}
            {currentPage === 'labs' && <LabsPage />}
            {currentPage === 'handouts' && <HandoutsPage />}
            {currentPage === 'dashboard' && <DashboardPage />}
            {currentPage === 'ai-tools' && <AIToolsPage />}
            {currentPage === 'contact' && <ContactPage />}
            {currentPage === 'about' && <AboutPage />}
          </main>

          {/* Cookie Consent */}
          {showCookieConsent && (
            <div className="fixed bottom-0 left-0 right-0 bg-gray-800 text-white p-4 z-50">
              <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between space-y-3 md:space-y-0">
                <div className="flex-1">
                  <p className="text-sm">
                    We use cookies and privacy-friendly analytics to improve your experience. 
                    By continuing to use this site, you agree to our use of cookies.
                  </p>
                </div>
                <div className="flex space-x-4">
                  <button
                    onClick={handleCookieAccept}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded text-sm transition-colors"
                  >
                    Accept
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Footer */}
          <footer className="bg-gray-100 dark:bg-gray-800 py-8 mt-16">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
              <p className="text-gray-600 dark:text-gray-400 mb-4">
                ImpactMojo is an open-source project. No endorsements or certificates are provided.
              </p>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                © 2025 ImpactMojo. Released under MIT License.
              </p>
            </div>
          </footer>
        </div>
      </div>
    </AuthProvider>
  );
}

export default App;

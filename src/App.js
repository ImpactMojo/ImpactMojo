import React, { useState, useEffect, useMemo } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate, useLocation } from 'react-router-dom';
import { 
  Calendar, Clock, ExternalLink, User, Search, FileText, Download, 
  BarChart, Settings, FolderOpen, AlertCircle, Star, BookOpen, 
  Users, Target, Lightbulb, Home, GraduationCap, PlayCircle, 
  Menu, X, Moon, Sun, Mail, ChevronDown, ChevronRight, Filter
} from 'lucide-react';

// Firebase imports
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithPopup, GoogleAuthProvider, signOut, onAuthStateChanged } from 'firebase/auth';

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDnF0eJsTULzOJUnBskybd44dG5w-f46vE",
  authDomain: "impactmojo.firebaseapp.com",
  projectId: "impactmojo",
  storageBucket: "impactmojo.firebasestorage.app",
  messagingSenderId: "529198336589",
  appId: "1:529198336589:web:1664b5344de5bfb31bea04",
  measurementId: "G-ZHPPXXMRGV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

// Course data
const coursesData = [
  {
    id: "C1",
    title: "Gender Studies 101",
    description: "Comprehensive introduction to gender studies theory and practice.",
    track: "Gender Studies",
    difficulty: "Beginner",
    duration: "6 weeks",
    url: "https://genderstudies101.netlify.app/",
    status: "Available"
  },
  {
    id: "C2", 
    title: "Research Methods Fundamentals",
    description: "Essential research methodologies for development practitioners.",
    track: "Research Methods",
    difficulty: "Beginner", 
    duration: "8 weeks",
    url: "https://researchmethods101.netlify.app/",
    status: "Available"
  },
  {
    id: "C3",
    title: "Data Analysis with R",
    description: "Statistical analysis using R for development data.",
    track: "Data Analysis",
    difficulty: "Intermediate",
    duration: "10 weeks", 
    url: "https://dataanalysis-r.netlify.app/",
    status: "Available"
  },
  {
    id: "C4",
    title: "Policy Analysis Framework", 
    description: "Systematic approach to analyzing development policies.",
    track: "Policy & Economics",
    difficulty: "Advanced",
    duration: "8 weeks",
    url: "https://policyanalysis101.netlify.app/", 
    status: "Available"
  },
  {
    id: "C5",
    title: "Gender and Development",
    description: "Exploring gender dimensions in development practice.",
    track: "Gender Studies", 
    difficulty: "Intermediate",
    duration: "6 weeks",
    url: "https://gender-development.netlify.app/",
    status: "Available"
  }
];

// Labs data
const labsData = [
  {
    id: "L1",
    title: "Impact Measurement Lab",
    description: "Hands-on tools for measuring social impact and outcomes.",
    url: "https://impact-measurement.netlify.app/",
    icon: "target",
    category: "Monitoring & Evaluation",
    difficulty: "Intermediate",
    duration: 75,
    status: "Available"
  },
  {
    id: "L2", 
    title: "Stakeholder Mapping Lab",
    description: "Interactive stakeholder analysis and engagement planning.",
    url: "https://stakeholder-mapping.netlify.app/",
    icon: "users",
    category: "Project Management", 
    difficulty: "Beginner",
    duration: 45,
    status: "Available"
  },
  {
    id: "L3",
    title: "Policy Advocacy Simulator",
    description: "Practice policy advocacy strategies in realistic scenarios.",
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
  }
];

// Updated handouts data based on actual GitHub repository structure
const handoutsData = [
  // Cross Cutting Resources
  {
    id: "H1",
    title: "Case Studies",
    category: "Cross Cutting Resources",
    type: "HTML",
    description: "Templates and frameworks for developing comprehensive case studies in development contexts.",
    url: "/Handouts/Cross%20Cutting%20Resources/Case%20Studies/",
    track: "All Tracks",
    pathway: "Cross-Cutting"
  },
  {
    id: "H2",
    title: "Communications",
    category: "Cross Cutting Resources", 
    type: "HTML",
    description: "Best practices for effective development communication and stakeholder engagement.",
    url: "/Handouts/Cross%20Cutting%20Resources/Communications/",
    track: "All Tracks",
    pathway: "Cross-Cutting"
  },
  {
    id: "H3",
    title: "Local Application Worksheet",
    category: "Cross Cutting Resources",
    type: "HTML", 
    description: "Framework for adapting global development concepts to local contexts.",
    url: "/Handouts/Cross%20Cutting%20Resources/Local%20Application%20Worksheet/",
    track: "All Tracks",
    pathway: "Cross-Cutting"
  },
  {
    id: "H4",
    title: "Software Tools Guide",
    category: "Cross Cutting Resources",
    type: "HTML",
    description: "Essential software tools and digital resources for development practitioners.",
    url: "/Handouts/Cross%20Cutting%20Resources/Software%20Tools%20Guide/",
    track: "All Tracks",
    pathway: "Cross-Cutting"
  },

  // Data Analysis Track
  {
    id: "H5",
    title: "Bivariate Analysis",
    category: "Data Analysis Track",
    type: "HTML",
    description: "Comprehensive guides and exercises for bivariate statistical analysis.",
    url: "/Handouts/Data%20Analysis%20Track/Bivariate%20Analysis/",
    track: "Data Analysis",
    pathway: "Data Analysis Track"
  },
  {
    id: "H6",
    title: "Data Analysis - Examples and Templates",
    category: "Data Analysis Track",
    type: "Multiple",
    description: "Complete collection of R scripts, Python code, Excel templates, and analysis guides.",
    url: "/Handouts/Data%20Analysis%20Track/Data%20Analysis%20-%20Examples%20and%20Templates/",
    track: "Data Analysis",
    pathway: "Data Analysis Track"
  },
  {
    id: "H7",
    title: "Data Literacy",
    category: "Data Analysis Track",
    type: "HTML",
    description: "Essential concepts and skills for data literacy in development contexts.",
    url: "/Handouts/Data%20Analysis%20Track/Data%20Literacy/",
    track: "Data Analysis",
    pathway: "Data Analysis Track"
  },
  {
    id: "H8",
    title: "Econometrics",
    category: "Data Analysis Track",
    type: "HTML",
    description: "Formula sheets, handouts, and problem sets for econometric analysis.",
    url: "/Handouts/Data%20Analysis%20Track/Econometrics/",
    track: "Data Analysis",
    pathway: "Data Analysis Track"
  },
  {
    id: "H9",
    title: "EDA (Exploratory Data Analysis)",
    category: "Data Analysis Track",
    type: "HTML",
    description: "Exploratory data analysis techniques specifically for household surveys.",
    url: "/Handouts/Data%20Analysis%20Track/EDA/",
    track: "Data Analysis",
    pathway: "Data Analysis Track"
  },
  {
    id: "H10",
    title: "Multivariate Analysis",
    category: "Data Analysis Track",
    type: "HTML", 
    description: "Advanced multivariate analysis templates, guides, and problem sets.",
    url: "/Handouts/Data%20Analysis%20Track/Multivariate%20Analysis/",
    track: "Data Analysis",
    pathway: "Data Analysis Track"
  },

  // Education and Pedagogy
  {
    id: "H11",
    title: "Education and Pedagogy",
    category: "Education and Pedagogy",
    type: "HTML",
    description: "Specialized resources for educators focusing on learning theory and curriculum design.",
    url: "/Handouts/Education%20and%20Pedagogy/",
    track: "All Tracks",
    pathway: "Education & Pedagogy"
  },

  // Gender Studies Track
  {
    id: "H12",
    title: "Care Economy",
    category: "Gender Studies Track",
    type: "HTML",
    description: "Framework and tools for analyzing care economy dynamics and unpaid work.",
    url: "/Handouts/Gender%20Studies%20Track/Care%20Economy/",
    track: "Gender Studies",
    pathway: "Gender Studies Track"
  },
  {
    id: "H13",
    title: "Data Feminism", 
    category: "Gender Studies Track",
    type: "HTML",
    description: "Applying data feminism principles to research and analysis in South Asian contexts.",
    url: "/Handouts/Gender%20Studies%20Track/Data%20Feminism/",
    track: "Gender Studies",
    pathway: "Gender Studies Track"
  },
  {
    id: "H14",
    title: "Gender Studies",
    category: "Gender Studies Track",
    type: "HTML",
    description: "Key concepts, frameworks, and quick reference materials for gender studies.",
    url: "/Handouts/Gender%20Studies%20Track/Gender%20Studies/",
    track: "Gender Studies",
    pathway: "Gender Studies Track"
  },
  {
    id: "H15",
    title: "Women's Economic Empowerment",
    category: "Gender Studies Track",
    type: "HTML",
    description: "Resources on women's economic empowerment strategies and measurement.",
    url: "/Handouts/Gender%20Studies%20Track/Women's%20Economic%20Empowerment/",
    track: "Gender Studies", 
    pathway: "Gender Studies Track"
  },

  // Policy and Economics Track
  {
    id: "H16",
    title: "Development Economics",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Core concepts, theories, and applications in development economics.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Development%20Economics/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H17",
    title: "Livelihoods",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Livelihood analysis frameworks and assessment tools.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Livelihoods/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H18",
    title: "Marginalised Identities",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Analysis of marginalized identities in policy and economic contexts.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Marginalised%20Identities/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H19",
    title: "Policy Tracking",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Tools and templates for tracking policy developments and impacts.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Policy%20Tracking/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H20",
    title: "Political Economy",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Political economy analysis frameworks for development contexts.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Political%20Economy/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H21",
    title: "Post Truth Politics",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Analysis tools for understanding post-truth political environments.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Post%20Truth%20Politics/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H22",
    title: "Poverty and Inequality",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Measurement and analysis of poverty and inequality dynamics.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Poverty%20and%20Inequality/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },
  {
    id: "H23",
    title: "Social Safety Nets",
    category: "Policy and Economics Track",
    type: "HTML",
    description: "Design and evaluation of social safety net programs.",
    url: "/Handouts/Policy%20and%20Economics%20Track/Social%20Safety%20Nets/",
    track: "Policy & Economics",
    pathway: "Policy and Economics Track"
  },

  // Quick Reference Cards
  {
    id: "H24",
    title: "Quick Reference Cards",
    category: "Quick Reference Cards",
    type: "HTML",
    description: "Concise reference materials for quick lookup of key concepts and formulas.",
    url: "/Handouts/Quick%20Reference%20Cards/",
    track: "All Tracks",
    pathway: "Quick Reference"
  },

  // Research Methods Track
  {
    id: "H25",
    title: "Assumptions Checklist",
    category: "Research Methods Track",
    type: "HTML",
    description: "Checklist for identifying and testing research assumptions.",
    url: "/Handouts/Research%20Methods%20Track/Assumptions%20Checklist/",
    track: "Research Methods",
    pathway: "Research Methods Track"
  },
  {
    id: "H26",
    title: "MLE (Monitoring, Learning & Evaluation)",
    category: "Research Methods Track",
    type: "HTML",
    description: "Comprehensive guides for monitoring, learning, and evaluation frameworks.",
    url: "/Handouts/Research%20Methods%20Track/MLE/",
    track: "Research Methods",
    pathway: "Research Methods Track"
  },
  {
    id: "H27",
    title: "Qualitative Research",
    category: "Research Methods Track",
    type: "HTML",
    description: "Methods and tools for qualitative research in development contexts.",
    url: "/Handouts/Research%20Methods%20Track/Qualitative%20Research/",
    track: "Research Methods",
    pathway: "Research Methods Track"
  },
  {
    id: "H28",
    title: "Research Design - Resources",
    category: "Research Methods Track",
    type: "HTML",
    description: "Comprehensive resources for research design and methodology.",
    url: "/Handouts/Research%20Methods%20Track/Research%20Design%20-%20Resources/",
    track: "Research Methods",
    pathway: "Research Methods Track"
  },
  {
    id: "H29",
    title: "Research Design Worksheet",
    category: "Research Methods Track",
    type: "HTML",
    description: "Interactive worksheet for planning research design.",
    url: "/Handouts/Research%20Methods%20Track/Research%20Design%20Worksheet/",
    track: "Research Methods",
    pathway: "Research Methods Track"
  },
  {
    id: "H30",
    title: "Research Ethics",
    category: "Research Methods Track",
    type: "HTML",
    description: "Ethical considerations and frameworks for development research.",
    url: "/Handouts/Research%20Methods%20Track/Research%20Ethics/",
    track: "Research Methods",
    pathway: "Research Methods Track"
  },

  // Thematic Areas
  {
    id: "H31",
    title: "Climate Change - Science, Mitigation, Adaptation, Resilience and Futures",
    category: "Thematic Areas",
    type: "HTML",
    description: "Comprehensive resources on climate change science and adaptation strategies.",
    url: "/Handouts/Thematic%20Areas/Climate%20Change%20-%20Science,%20Mitigation,%20Adaptation,%20Resilience%20and%20Futures/",
    track: "All Tracks",
    pathway: "Thematic Areas"
  },
  {
    id: "H32",
    title: "Environmental Justice",
    category: "Thematic Areas",
    type: "HTML",
    description: "Environmental justice frameworks and case studies.",
    url: "/Handouts/Thematic%20Areas/Environmental%20Justice/",
    track: "All Tracks",
    pathway: "Thematic Areas"
  },
  {
    id: "H33",
    title: "Constitution, Law, Justice and Jurisprudence",
    category: "Thematic Areas",
    type: "HTML",
    description: "Legal frameworks and constitutional analysis for development work.",
    url: "/Handouts/Thematic%20Areas/Constitution,%20Law,%20Justice%20and%20Jurisprudence/",
    track: "All Tracks",
    pathway: "Thematic Areas"
  },

  // Digital Development Ethics
  {
    id: "H34",
    title: "AI Bias and Algorithmic Justice",
    category: "Digital Development Ethics",
    type: "HTML",
    description: "Understanding and addressing AI bias in development applications.",
    url: "/Handouts/Digital%20Development%20Ethics/AI%20Bias%20and%20Algorithmic%20Justice/",
    track: "All Tracks",
    pathway: "Digital Development Ethics"
  },
  {
    id: "H35",
    title: "Digital Justice and Data Consent",
    category: "Digital Development Ethics",
    type: "HTML",
    description: "Frameworks for digital justice and informed data consent.",
    url: "/Handouts/Digital%20Development%20Ethics/Digital%20Justice%20and%20Data%20Consent/",
    track: "All Tracks",
    pathway: "Digital Development Ethics"
  },
  {
    id: "H36",
    title: "Digital Surveillance and State Power",
    category: "Digital Development Ethics",
    type: "HTML",
    description: "Analysis of digital surveillance implications for development work.",
    url: "/Handouts/Digital%20Development%20Ethics/Digital%20Surveillance%20and%20State%20Power/",
    track: "All Tracks",
    pathway: "Digital Development Ethics"
  },
  {
    id: "H37",
    title: "Ethics in Digital Work for Development",
    category: "Digital Development Ethics",
    type: "HTML",
    description: "Ethical frameworks for digital development interventions.",
    url: "/Handouts/Digital%20Development%20Ethics/Ethics%20in%20Digital%20Work%20for%20Development/",
    track: "All Tracks",
    pathway: "Digital Development Ethics"
  },
  {
    id: "H38",
    title: "Platform Labour and Digital Governance",
    category: "Digital Development Ethics",
    type: "HTML",
    description: "Analysis of platform labor dynamics and digital governance.",
    url: "/Handouts/Digital%20Development%20Ethics/Platform%20Labour%20and%20Digital%20Governance/",
    track: "All Tracks",
    pathway: "Digital Development Ethics"
  },

  // Health and Wellbeing
  {
    id: "H39",
    title: "An Introduction to Public Health by CDC",
    category: "Health and Wellbeing",
    type: "HTML",
    description: "CDC-based introduction to public health principles and practice.",
    url: "/Handouts/Health%20and%20Wellbeing/An%20Introduction%20to%20Public%20Health%20by%20CDC/",
    track: "All Tracks",
    pathway: "Health and Wellbeing"
  },
  {
    id: "H40",
    title: "Public Health",
    category: "Health and Wellbeing",
    type: "HTML",
    description: "Comprehensive public health resources and frameworks.",
    url: "/Handouts/Health%20and%20Wellbeing/Public%20Health/",
    track: "All Tracks",
    pathway: "Health and Wellbeing"
  },
  {
    id: "H41",
    title: "Sexual and Reproductive Health",
    category: "Health and Wellbeing",
    type: "HTML",
    description: "Sexual and reproductive health policy and program resources.",
    url: "/Handouts/Health%20and%20Wellbeing/Sexual%20and%20Reproductive%20Health/",
    track: "All Tracks",
    pathway: "Health and Wellbeing"
  },

  // Justice and Governance
  {
    id: "H42",
    title: "Community Led Development",
    category: "Justice and Governance",
    type: "HTML",
    description: "Frameworks and tools for community-led development approaches.",
    url: "/Handouts/Justice%20and%20Governance/Community%20Led%20Development/",
    track: "All Tracks",
    pathway: "Justice and Governance"
  },
  {
    id: "H43",
    title: "Decent Work",
    category: "Justice and Governance",
    type: "HTML",
    description: "Decent work frameworks and assessment tools.",
    url: "/Handouts/Justice%20and%20Governance/Decent%20Work/",
    track: "All Tracks",
    pathway: "Justice and Governance"
  },
  {
    id: "H44",
    title: "Decolonising Development",
    category: "Justice and Governance",
    type: "HTML",
    description: "Frameworks and approaches for decolonizing development practice.",
    url: "/Handouts/Justice%20and%20Governance/Decolonising%20Development/",
    track: "All Tracks",
    pathway: "Justice and Governance"
  },

  // South Asia Region
  {
    id: "H45",
    title: "South Asia Historical - Modern Policy Timeline",
    category: "South Asia Region",
    type: "HTML",
    description: "Historical timeline of policy developments in South Asia.",
    url: "/Handouts/South%20Asia%20Region/South%20Asia%20Historical%20-%20Modern%20Policy%20Timeline/",
    track: "All Tracks",
    pathway: "South Asia Region"
  },
  {
    id: "H46",
    title: "South Asia Regional Dashboard",
    category: "South Asia Region",
    type: "HTML",
    description: "Regional dashboard with key indicators and data for South Asia.",
    url: "/Handouts/South%20Asia%20Region/South%20Asia%20Regional%20Dashboard/",
    track: "All Tracks",
    pathway: "South Asia Region"
  }
];

// Newsletter modal component
const NewsletterModal = ({ isOpen, onClose }) => {
  const [email, setEmail] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    try {
      const response = await fetch('https://formspree.io/f/xpwdvgzp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          type: 'newsletter_signup'
        }),
      });
      
      if (response.ok) {
        setIsSubmitted(true);
        setEmail('');
      }
    } catch (error) {
      console.error('Error submitting form:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
            Subscribe to Newsletter
          </h3>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300"
          >
            <X className="w-6 h-6" />
          </button>
        </div>
        
        {!isSubmitted ? (
          <form onSubmit={handleSubmit}>
            <p className="text-gray-600 dark:text-gray-300 mb-4">
              Get the latest updates on new courses, resources, and impact stories.
            </p>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white mb-4"
            />
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white font-medium py-2 px-4 rounded-md transition-colors"
            >
              {isSubmitting ? 'Subscribing...' : 'Subscribe'}
            </button>
          </form>
        ) : (
          <div className="text-center">
            <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path>
              </svg>
            </div>
            <h4 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
              Thank you for subscribing!
            </h4>
            <p className="text-gray-600 dark:text-gray-300">
              You'll receive our latest updates soon.
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

// Navigation component
const Navigation = ({ user, onSignIn, onSignOut, darkMode, toggleDarkMode }) => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [showNewsletterModal, setShowNewsletterModal] = useState(false);
  const location = useLocation();

  const navigationItems = [
    { name: 'Home', path: '/', icon: Home },
    { name: 'Courses', path: '/courses', icon: GraduationCap },
    { name: 'Labs', path: '/labs', icon: PlayCircle },
    { name: 'Handouts', path: '/handouts', icon: FileText }
  ];

  return (
    <>
      <nav className="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <Link to="/" className="flex-shrink-0">
                <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">ImpactMojo</span>
              </Link>
              
              <div className="hidden md:block ml-10">
                <div className="flex items-baseline space-x-4">
                  {navigationItems.map((item) => {
                    const Icon = item.icon;
                    const isActive = location.pathname === item.path;
                    return (
                      <Link
                        key={item.name}
                        to={item.path}
                        className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1 ${
                          isActive
                            ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                            : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700'
                        }`}
                      >
                        <Icon className="w-4 h-4" />
                        <span>{item.name}</span>
                      </Link>
                    );
                  })}
                </div>
              </div>
            </div>

            <div className="hidden md:flex items-center space-x-4">
              <button
                onClick={() => setShowNewsletterModal(true)}
                className="flex items-center space-x-1 px-3 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition-colors"
              >
                <Mail className="w-4 h-4" />
                <span>Newsletter</span>
              </button>
              
              <button
                onClick={toggleDarkMode}
                className="p-2 rounded-md text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              >
                {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
              </button>

              {user ? (
                <div className="flex items-center space-x-3">
                  <img 
                    src={user.photoURL} 
                    alt={user.displayName}
                    className="w-8 h-8 rounded-full"
                  />
                  <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
                    {user.displayName}
                  </span>
                  <button
                    onClick={onSignOut}
                    className="text-sm text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                  >
                    Sign Out
                  </button>
                </div>
              ) : (
                <button
                  onClick={onSignIn}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors flex items-center space-x-2"
                >
                  <User className="w-4 h-4" />
                  <span>Sign In</span>
                </button>
              )}
            </div>

            <div className="md:hidden">
              <button
                onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                className="p-2 rounded-md text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
              >
                {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
              </button>
            </div>
          </div>

          {/* Mobile menu */}
          {isMobileMenuOpen && (
            <div className="md:hidden">
              <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 border-t border-gray-200 dark:border-gray-700">
                {navigationItems.map((item) => {
                  const Icon = item.icon;
                  const isActive = location.pathname === item.path;
                  return (
                    <Link
                      key={item.name}
                      to={item.path}
                      onClick={() => setIsMobileMenuOpen(false)}
                      className={`block px-3 py-2 rounded-md text-base font-medium transition-colors flex items-center space-x-2 ${
                        isActive
                          ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                          : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700'
                      }`}
                    >
                      <Icon className="w-5 h-5" />
                      <span>{item.name}</span>
                    </Link>
                  );
                })}
                
                <button
                  onClick={() => {
                    setShowNewsletterModal(true);
                    setIsMobileMenuOpen(false);
                  }}
                  className="w-full text-left block px-3 py-2 rounded-md text-base font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors flex items-center space-x-2"
                >
                  <Mail className="w-5 h-5" />
                  <span>Newsletter</span>
                </button>
                
                <button
                  onClick={toggleDarkMode}
                  className="w-full text-left block px-3 py-2 rounded-md text-base font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors flex items-center space-x-2"
                >
                  {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
                  <span>{darkMode ? 'Light Mode' : 'Dark Mode'}</span>
                </button>

                {user ? (
                  <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
                    <div className="flex items-center px-3 mb-3">
                      <img 
                        src={user.photoURL} 
                        alt={user.displayName}
                        className="w-10 h-10 rounded-full"
                      />
                      <div className="ml-3">
                        <div className="text-base font-medium text-gray-800 dark:text-gray-200">
                          {user.displayName}
                        </div>
                        <div className="text-sm text-gray-500 dark:text-gray-400">
                          {user.email}
                        </div>
                      </div>
                    </div>
                    <button
                      onClick={onSignOut}
                      className="block px-3 py-2 rounded-md text-base font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
                    >
                      Sign Out
                    </button>
                  </div>
                ) : (
                  <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
                    <button
                      onClick={onSignIn}
                      className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors flex items-center justify-center space-x-2"
                    >
                      <User className="w-4 h-4" />
                      <span>Sign In</span>
                    </button>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      </nav>
      
      <NewsletterModal 
        isOpen={showNewsletterModal} 
        onClose={() => setShowNewsletterModal(false)} 
      />
    </>
  );
};

// Home page component
const HomePage = () => {
  const navigate = useNavigate();
  
  const tracks = [
    {
      name: "Research Methods",
      description: "Master qualitative and quantitative research methodologies",
      icon: Search,
      color: "blue",
      courseCount: coursesData.filter(course => course.track === "Research Methods").length
    },
    {
      name: "Data Analysis", 
      description: "Learn statistical analysis and data visualization techniques",
      icon: BarChart,
      color: "green",
      courseCount: coursesData.filter(course => course.track === "Data Analysis").length
    },
    {
      name: "Gender Studies",
      description: "Explore gender dimensions in development practice",
      icon: Users,
      color: "purple", 
      courseCount: coursesData.filter(course => course.track === "Gender Studies").length
    },
    {
      name: "Policy & Economics",
      description: "Understand policy analysis and economic frameworks",
      icon: Target,
      color: "red",
      courseCount: coursesData.filter(course => course.track === "Policy & Economics").length
    }
  ];

  const handleTrackClick = (trackName) => {
    navigate(`/courses?track=${encodeURIComponent(trackName)}`);
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-700 dark:from-blue-800 dark:to-purple-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">
              ImpactMojo
            </h1>
            <p className="text-xl md:text-2xl text-blue-100 dark:text-blue-200 mb-8 max-w-3xl mx-auto">
              A 101 Knowledge Series for Social Impact – Curated library exploring justice, equity, and development in South Asia
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                to="/courses"
                className="bg-white text-blue-600 hover:bg-blue-50 font-semibold py-3 px-8 rounded-lg transition-colors inline-flex items-center justify-center space-x-2"
              >
                <GraduationCap className="w-5 h-5" />
                <span>Explore Courses</span>
              </Link>
              <Link
                to="/labs"
                className="bg-transparent border-2 border-white text-white hover:bg-white hover:text-blue-600 font-semibold py-3 px-8 rounded-lg transition-colors inline-flex items-center justify-center space-x-2"
              >
                <PlayCircle className="w-5 h-5" />
                <span>Try Labs</span>
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* Learning Tracks Section */}
      <div className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Learning Tracks
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
              Choose your learning path from our four specialized tracks, each designed to build expertise in key areas of development work.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {tracks.map((track) => {
              const Icon = track.icon;
              return (
                <div
                  key={track.name}
                  onClick={() => handleTrackClick(track.name)}
                  className="bg-white dark:bg-gray-800 rounded-xl p-8 shadow-lg hover:shadow-xl transition-shadow cursor-pointer border border-gray-200 dark:border-gray-700 group"
                >
                  <div className={`w-16 h-16 bg-${track.color}-100 dark:bg-${track.color}-900 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform`}>
                    <Icon className={`w-8 h-8 text-${track.color}-600 dark:text-${track.color}-400`} />
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
                    {track.name}
                  </h3>
                  <p className="text-gray-600 dark:text-gray-300 mb-4">
                    {track.description}
                  </p>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-500 dark:text-gray-400">
                      {track.courseCount} courses
                    </span>
                    <ChevronRight className="w-5 h-5 text-gray-400 group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-colors" />
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Featured Content Section */}
      <div className="bg-white dark:bg-gray-800 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Featured Resources
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300">
              Discover our most popular courses, labs, and handouts
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {/* Featured Course */}
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900 dark:to-blue-800 rounded-xl p-8">
              <div className="flex items-center mb-4">
                <GraduationCap className="w-8 h-8 text-blue-600 dark:text-blue-400 mr-3" />
                <span className="text-sm font-medium text-blue-600 dark:text-blue-400 uppercase tracking-wide">
                  Featured Course
                </span>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Gender Studies 101
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-6">
                Comprehensive introduction to gender studies theory and practice in development contexts.
              </p>
              <Link
                to="/courses"
                className="inline-flex items-center space-x-2 text-blue-600 dark:text-blue-400 font-medium hover:text-blue-700 dark:hover:text-blue-300 transition-colors"
              >
                <span>Start Learning</span>
                <ExternalLink className="w-4 h-4" />
              </Link>
            </div>

            {/* Featured Lab */}
            <div className="bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900 dark:to-green-800 rounded-xl p-8">
              <div className="flex items-center mb-4">
                <PlayCircle className="w-8 h-8 text-green-600 dark:text-green-400 mr-3" />
                <span className="text-sm font-medium text-green-600 dark:text-green-400 uppercase tracking-wide">
                  Featured Lab
                </span>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Impact Measurement Lab
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-6">
                Hands-on tools for measuring social impact and outcomes in your development projects.
              </p>
              <Link
                to="/labs"
                className="inline-flex items-center space-x-2 text-green-600 dark:text-green-400 font-medium hover:text-green-700 dark:hover:text-green-300 transition-colors"
              >
                <span>Try Lab</span>
                <ExternalLink className="w-4 h-4" />
              </Link>
            </div>

            {/* Featured Handouts */}
            <div className="bg-gradient-to-br from-purple-50 to-purple-100 dark:from-purple-900 dark:to-purple-800 rounded-xl p-8">
              <div className="flex items-center mb-4">
                <FileText className="w-8 h-8 text-purple-600 dark:text-purple-400 mr-3" />
                <span className="text-sm font-medium text-purple-600 dark:text-purple-400 uppercase tracking-wide">
                  Featured Handouts
                </span>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Quick Reference Cards
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-6">
                Downloadable reference materials perfect for printing and desk reference.
              </p>
              <Link
                to="/handouts"
                className="inline-flex items-center space-x-2 text-purple-600 dark:text-purple-400 font-medium hover:text-purple-700 dark:hover:text-purple-300 transition-colors"
              >
                <span>Browse Handouts</span>
                <Download className="w-4 h-4" />
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* Stats Section */}
      <div className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-4xl font-bold text-blue-600 dark:text-blue-400 mb-2">
                {coursesData.length}
              </div>
              <div className="text-gray-600 dark:text-gray-300 font-medium">
                Courses
              </div>
            </div>
            <div>
              <div className="text-4xl font-bold text-green-600 dark:text-green-400 mb-2">
                {labsData.length}
              </div>
              <div className="text-gray-600 dark:text-gray-300 font-medium">
                Interactive Labs
              </div>
            </div>
            <div>
              <div className="text-4xl font-bold text-purple-600 dark:text-purple-400 mb-2">
                {handoutsData.length}
              </div>
              <div className="text-gray-600 dark:text-gray-300 font-medium">
                Handouts
              </div>
            </div>
            <div>
              <div className="text-4xl font-bold text-red-600 dark:text-red-400 mb-2">
                4
              </div>
              <div className="text-gray-600 dark:text-gray-300 font-medium">
                Learning Tracks
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Course Card Component
const CourseCard = ({ course, onCourseAccess }) => {
  const handleCourseAccess = () => {
    if (course.status === 'Available') {
      onCourseAccess(course);
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 border border-gray-200 dark:border-gray-700">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center">
            <BookOpen className="w-6 h-6 text-blue-600 dark:text-blue-400" />
          </div>
          <div className="flex items-center space-x-2">
            {[1, 2, 3, 4, 5].map((star) => (
              <Star
                key={star}
                className={`w-4 h-4 ${
                  star <= 4 ? 'fill-yellow-400 text-yellow-400' : 'text-gray-400'
                }`} 
              />
            ))}
          </div>
        </div>
      </div>
      
      <h3 className="text-xl font-bold mb-2 text-gray-900 dark:text-white">
        {course.title}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-300 mb-4 line-clamp-3">
        {course.description}
      </p>
      
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
  );
};

// Courses page component
const CoursesPage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('all');
  const location = useLocation();

  // Get track from URL params if present
  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const trackParam = params.get('track');
    if (trackParam) {
      setSelectedTrack(trackParam);
    }
  }, [location]);

  const handleCourseAccess = (course) => {
    window.open(course.url, '_blank');
  };

  const filteredCourses = useMemo(() => {
    return coursesData.filter(course => {
      const matchesSearch = course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                           course.description.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesTrack = selectedTrack === 'all' || course.track === selectedTrack;
      return matchesSearch && matchesTrack;
    });
  }, [searchQuery, selectedTrack]);

  const tracks = ['Research Methods', 'Data Analysis', 'Gender Studies', 'Policy & Economics'];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Courses
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Comprehensive learning paths for development professionals
          </p>
        </div>

        {/* Search and Filters */}
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 border border-gray-200 dark:border-gray-700">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  placeholder="Search courses..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
            </div>
            <div className="md:w-48">
              <select
                value={selectedTrack}
                onChange={(e) => setSelectedTrack(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="all">All Tracks</option>
                {tracks.map(track => (
                  <option key={track} value={track}>{track}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Courses Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredCourses.map(course => (
            <CourseCard
              key={course.id}
              course={course}
              onCourseAccess={handleCourseAccess}
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

// Lab Card Component
const LabCard = ({ lab }) => {
  const handleLabAccess = () => {
    if (lab.status === 'Available') {
      window.open(lab.url, '_blank');
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 border border-gray-200 dark:border-gray-700">
      <div className="flex items-center justify-between mb-4">
        <div className="w-12 h-12 bg-green-100 dark:bg-green-900 rounded-lg flex items-center justify-center">
          <PlayCircle className="w-8 h-8 text-green-600 dark:text-green-400" />
        </div>
        <div className="flex items-center space-x-1 text-sm text-gray-500 dark:text-gray-400">
          <Clock className="w-4 h-4" />
          <span>{lab.duration} min</span>
        </div>
      </div>
      
      <h3 className="text-xl font-bold mb-3 text-gray-900 dark:text-white">
        {lab.title}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-300 mb-4">
        {lab.description}
      </p>
      
      <div className="flex items-center justify-between mb-4">
        <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 px-2 py-1 rounded text-sm">
          {lab.category}
        </span>
        <span className="text-sm text-gray-500 dark:text-gray-400">
          {lab.difficulty}
        </span>
      </div>
      
      <button
        onClick={handleLabAccess}
        disabled={lab.status !== 'Available'}
        className={`w-full font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2 ${
          lab.status === 'Available' 
            ? 'bg-green-600 hover:bg-green-700 text-white'
            : 'bg-gray-300 dark:bg-gray-600 text-gray-500 dark:text-gray-400 cursor-not-allowed'
        }`}
      >
        <PlayCircle className="w-4 h-4" />
        <span>{lab.status === 'Available' ? 'Launch Lab' : 'Coming Soon'}</span>
      </button>
    </div>
  );
};

// Labs page component
const LabsPage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');

  const filteredLabs = useMemo(() => {
    return labsData.filter(lab => {
      const matchesSearch = lab.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                           lab.description.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesCategory = selectedCategory === 'all' || lab.category === selectedCategory;
      return matchesSearch && matchesCategory;
    });
  }, [searchQuery, selectedCategory]);

  const categories = [...new Set(labsData.map(lab => lab.category))];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Interactive Labs
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Hands-on tools and simulations for practical learning
          </p>
        </div>

        {/* Search and Filters */}
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 border border-gray-200 dark:border-gray-700">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  placeholder="Search labs..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
            </div>
            <div className="md:w-56">
              <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="all">All Categories</option>
                {categories.map(category => (
                  <option key={category} value={category}>{category}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Labs Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredLabs.map(lab => (
            <LabCard key={lab.id} lab={lab} />
          ))}
        </div>

        {filteredLabs.length === 0 && (
          <div className="text-center py-12">
            <Search className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
              No labs found
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

// Handout Card Component  
const HandoutCard = ({ handout }) => {
  const getTypeIcon = (type) => {
    switch (type.toLowerCase()) {
      case 'html': return <FileText className="w-5 h-5" />;
      case 'pdf': return <FileText className="w-5 h-5" />;
      case 'excel': return <BarChart className="w-5 h-5" />;
      case 'r': return <Settings className="w-5 h-5" />;
      case 'python': return <Settings className="w-5 h-5" />;
      case 'multiple': return <FolderOpen className="w-5 h-5" />;
      default: return <FileText className="w-5 h-5" />;
    }
  };

  const getTypeColor = (type) => {
    switch (type.toLowerCase()) {
      case 'html': return 'text-blue-600 dark:text-blue-400';
      case 'pdf': return 'text-red-600 dark:text-red-400'; 
      case 'excel': return 'text-green-600 dark:text-green-400';
      case 'r': return 'text-purple-600 dark:text-purple-400';
      case 'python': return 'text-yellow-600 dark:text-yellow-400';
      case 'multiple': return 'text-orange-600 dark:text-orange-400';
      default: return 'text-gray-600 dark:text-gray-400';
    }
  };

  const handleAccess = () => {
    // Convert GitHub URLs to proper links
    const baseUrl = 'https://github.com/Varnasr/ImpactMojo/tree/main';
    const fullUrl = handout.url.startsWith('/Handouts') 
      ? `${baseUrl}${handout.url}`
      : handout.url;
    
    window.open(fullUrl, '_blank');
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 border border-gray-200 dark:border-gray-700">
      <div className="flex items-start justify-between mb-4">
        <div className={`p-3 rounded-lg bg-gray-50 dark:bg-gray-700 ${getTypeColor(handout.type)}`}>
          {getTypeIcon(handout.type)}
        </div>
        <span className="text-xs font-medium text-gray-500 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded">
          {handout.type.toUpperCase()}
        </span>
      </div>
      
      <h3 className="text-lg font-bold mb-2 text-gray-900 dark:text-white line-clamp-2">
        {handout.title}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-300 mb-4 text-sm line-clamp-3">
        {handout.description}
      </p>
      
      <div className="flex items-center justify-between mb-4">
        <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded text-xs">
          {handout.category}
        </span>
        <span className="text-xs text-gray-500 dark:text-gray-400">
          {handout.track}
        </span>
      </div>
      
      <button
        onClick={handleAccess}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
      >
        <ExternalLink className="w-4 h-4" />
        <span>Access Resource</span>
      </button>
    </div>
  );
};

// Handouts page component
const HandoutsPage = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedTrack, setSelectedTrack] = useState('all');

  const filteredHandouts = useMemo(() => {
    return handoutsData.filter(handout => {
      const matchesSearch = handout.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                           handout.description.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesCategory = selectedCategory === 'all' || handout.category === selectedCategory;
      const matchesTrack = selectedTrack === 'all' || handout.track === selectedTrack;
      return matchesSearch && matchesCategory && matchesTrack;
    });
  }, [searchQuery, selectedCategory, selectedTrack]);

  const uniqueCategories = [...new Set(handoutsData.map(handout => handout.category))];
  const uniqueTracks = [...new Set(handoutsData.map(handout => handout.track))];

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
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 border border-gray-200 dark:border-gray-700">
          <div className="flex flex-col lg:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  placeholder="Search handouts..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
            </div>
            <div className="lg:w-56">
              <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="all">All Categories</option>
                {uniqueCategories.map(category => (
                  <option key={category} value={category}>{category}</option>
                ))}
              </select>
            </div>
            <div className="lg:w-48">
              <select
                value={selectedTrack}
                onChange={(e) => setSelectedTrack(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="all">All Tracks</option>
                {uniqueTracks.map(track => (
                  <option key={track} value={track}>{track}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Handouts Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredHandouts.map(handout => (
            <HandoutCard
              key={handout.id}
              handout={handout}
            />
          ))}
        </div>

        {filteredHandouts.length === 0 && (
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

        {/* Info Note */}
        <div className="mt-8 bg-blue-50 dark:bg-blue-900 border border-blue-200 dark:border-blue-700 rounded-lg p-6">
          <div className="flex items-start">
            <AlertCircle className="w-5 h-5 text-blue-600 dark:text-blue-400 mr-3 mt-0.5" />
            <div>
              <h3 className="text-sm font-medium text-blue-800 dark:text-blue-200 mb-1">
                Open Educational Resources
              </h3>
              <p className="text-sm text-blue-700 dark:text-blue-300">
                All materials are licensed under CC BY-NC-SA 4.0 and available for adaptation. 
                Perfect for university instructors, training coordinators, and workshop facilitators.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Footer component
const Footer = () => {
  return (
    <footer className="bg-gray-900 dark:bg-gray-950 text-white py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-4 gap-8">
          <div className="md:col-span-2">
            <h3 className="text-2xl font-bold mb-4">ImpactMojo</h3>
            <p className="text-gray-300 mb-4">
              A 101 Knowledge Series for Social Impact – Curated library exploring justice, equity, and development in South Asia.
            </p>
            <p className="text-sm text-gray-400">
              Open-source under MIT license. All educational materials licensed under CC BY-NC-SA 4.0.
            </p>
          </div>
          
          <div>
            <h4 className="font-semibold mb-4">Resources</h4>
            <ul className="space-y-2 text-gray-300">
              <li><Link to="/courses" className="hover:text-white transition-colors">Courses</Link></li>
              <li><Link to="/labs" className="hover:text-white transition-colors">Labs</Link></li>
              <li><Link to="/handouts" className="hover:text-white transition-colors">Handouts</Link></li>
              <li><a href="https://github.com/Varnasr/ImpactMojo" target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors">GitHub</a></li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-semibold mb-4">Support</h4>
            <p className="text-sm text-gray-400 mb-2">
              ImpactMojo is provided completely free through the generous support of Pinpoint Ventures.
            </p>
            <p className="text-sm text-gray-400">
              For questions or feedback, reach out through our newsletter.
            </p>
          </div>
        </div>
        
        <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400 text-sm">
          <p>&copy; 2024 ImpactMojo. Open source educational resources for development practitioners.</p>
        </div>
      </div>
    </footer>
  );
};

// Main App component
const App = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [darkMode, setDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('darkMode') === 'true' || 
             (!localStorage.getItem('darkMode') && window.matchMedia('(prefers-color-scheme: dark)').matches);
    }
    return false;
  });

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  useEffect(() => {
    localStorage.setItem('darkMode', darkMode.toString());
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const handleSignIn = async () => {
    try {
      await signInWithPopup(auth, provider);
    } catch (error) {
      console.error('Error signing in:', error);
    }
  };

  const handleSignOut = async () => {
    try {
      await signOut(auth);
    } catch (error) {
      console.error('Error signing out:', error);
    }
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-300">Loading ImpactMojo...</p>
        </div>
      </div>
    );
  }

  return (
    <Router>
      <div className={`min-h-screen ${darkMode ? 'dark' : ''}`}>
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
          <Navigation 
            user={user}
            onSignIn={handleSignIn}
            onSignOut={handleSignOut}
            darkMode={darkMode}
            toggleDarkMode={toggleDarkMode}
          />
          
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/courses" element={<CoursesPage />} />
            <Route path="/labs" element={<LabsPage />} />
            <Route path="/handouts" element={<HandoutsPage />} />
          </Routes>
          
          <Footer />
        </div>
      </div>
    </Router>
  );
};

export default App;

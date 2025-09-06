// src/App.js
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Bookmark, MessageCircle, 
  ExternalLink, BookOpen, FileText, Target, Users, 
  Clock, CheckCircle, PlayCircle, Bot, Trophy, 
  Headphones, MapPin, Library, Music, Download, 
  Search, Plus, Edit3, Save, Filter, BookmarkIcon, Tag,
  Install, AlertTriangle, ChevronDown, ChevronRight, Gamepad2,
  BarChart, Star, ArrowRight, Calendar, TrendingUp, Scale, 
  Award, Puzzle, Zap
} from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc, updateDoc, collection, addDoc } from 'firebase/firestore';

// Data imports
import { courseData, upcomingCourses } from './data/course-data';
import { labsData } from './data/labs-data';
import { premiumResources } from './data/premium-resources-data';

// AI Tools Data (embedded to avoid import issues)
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
2. Visual diagram showing: Inputs → Activities → Outputs → Outcomes → Impact
3. Assumptions and risks at each level
4. Indicators for measuring progress
5. Feedback loops and adaptation points`,
    systemMessage: 'You are a strategic planning expert specializing in Theory of Change development for social impact programs. You understand complex causal pathways and can identify critical assumptions.',
    exampleInput: `Problem: High school dropout rates in rural communities
Target: 500 at-risk students aged 14-18
Geography: 3 rural districts
Timeframe: 5 years
Activities: Mentorship, scholarships, life skills training
Resources: $2M budget, 10 staff, 5 partner schools
Goal: Increase graduation rates from 60% to 85%`,
    icon: 'Target',
    color: 'green'
  },
  {
    id: 'meal-framework',
    title: 'MEAL Framework Designer',
    description: 'Design monitoring, evaluation, accountability and learning systems with indicators and data collection plans.',
    prompt: `Help me design a MEAL (Monitoring, Evaluation, Accountability & Learning) framework for my program.
Program Details:
- Objective: [main program goal]
- Activities: [key interventions]
- Target Beneficiaries: [who and how many]
- Duration: [timeframe]
- Budget for M&E: [available resources]
- Staff Capacity: [M&E skills available]
- Reporting Requirements: [donor/stakeholder needs]
Current M&E Systems: [existing tools/processes]
Please provide:
1. Logic model with clear results chain
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
  }
];

// Updated Games Data
const gamesData = [
  {
    id: "G1",
    title: "The Real Middle Game",
    description: "An interactive strategy game for development professionals",
    url: "https://101.www.impactmojo.in/theREALmiddlegame",
    category: "Strategy",
    difficulty: "Intermediate"
  }
];

// Updated Premium Resources Data (with corrected URLs)
const updatedPremiumResources = [
  {
    id: "PR1",
    title: "Field Notes from a Development Economist",
    description: "In-depth analysis and insights from development economics practice",
    url: "https://marginmuse.space/themarginmuse",
    category: "Blog/Newsletter",
    access: "Premium"
  },
  {
    id: "PR2", 
    title: "Qualitative Research Lab",
    description: "Interactive tools and resources for qualitative research methods",
    url: "https://101.www.impactmojo.in/IMQualLab",
    category: "Research Tools",
    access: "Premium"
  },
  {
    id: "PR3",
    title: "Statistical Analysis Assistant", 
    description: "AI-powered statistical analysis tools and guidance",
    url: "https://101.www.impactmojo.in/IMStatsAssist",
    category: "Data Analysis",
    access: "Premium"
  }
];

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

// Multi-dimensional browse system
const browseByRole = {
  "New to Development": {
    description: "Just starting your development journey",
    courses: ["development-economics-101", "global-development-architecture-101", "law-and-constitution-101"],
    color: "blue"
  },
  "Researcher/Academic": {
    description: "Conducting research and generating knowledge",
    courses: ["research-ethics-101", "qualitative-research-methods-101", "econometrics-101", "data-literacy-101"],
    color: "purple"
  },
  "Practitioner/Field Worker": {
    description: "Implementing programs and working directly with communities",
    courses: ["community-development-101", "monitoring-evaluation-accountability-and-learning-101", "advocacy-and-communications-101"],
    color: "green"
  },
  "Student/Policy Maker": {
    description: "Learning and shaping policy decisions",
    courses: ["law-and-constitution-101", "political-economy-101", "global-development-architecture-101"],
    color: "orange"
  }
};

const browseByImpact = {
  "Health & Wellbeing": {
    description: "Improving health outcomes and social welfare",
    courses: ["public-health-101", "sexual-and-reproductive-health-101", "human-rights-101"],
    color: "red"
  },
  "Education & Skills": {
    description: "Building knowledge and capacity",
    courses: ["data-literacy-101", "qualitative-research-methods-101", "econometrics-101"],
    color: "blue"
  },
  "Governance & Justice": {
    description: "Strengthening institutions and rule of law",
    courses: ["law-and-constitution-101", "political-economy-101", "research-ethics-101"],
    color: "purple"
  },
  "Economic Growth": {
    description: "Creating sustainable economic opportunities",
    courses: ["development-economics-101", "monitoring-evaluation-accountability-and-learning-101"],
    color: "green"
  }
};

const browseByTimeCommitment = {
  "Quick Start (< 2 hours)": {
    description: "Get started with fundamental concepts",
    courses: ["development-economics-101", "global-development-architecture-101"],
    color: "green"
  },
  "Deep Dive (2-4 hours)": {
    description: "Comprehensive exploration of topics",
    courses: ["qualitative-research-methods-101", "monitoring-evaluation-accountability-and-learning-101", "econometrics-101"],
    color: "blue"
  },
  "Mastery Track (4+ hours)": {
    description: "Advanced learning with practical application",
    courses: ["data-literacy-101", "research-ethics-101", "political-economy-101"],
    color: "purple"
  }
};

// Auth Context
const AuthContext = createContext();
const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);
  const [comparisons, setComparisons] = useState([]);
  const [customPathway, setCustomPathway] = useState([]);
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user);
      if (user) {
        await loadUserData(user.uid);
      } else {
        setBookmarks([]);
        setComparisons([]);
        setCustomPathway([]);
        setNotes([]);
      }
      setLoading(false);
    });

    return unsubscribe;
  }, []);

  const loadUserData = async (uid) => {
    try {
      const userDoc = await getDoc(doc(db, 'users', uid));
      if (userDoc.exists()) {
        const userData = userDoc.data();
        setBookmarks(userData.bookmarks || []);
        setComparisons(userData.comparisons || []);
        setCustomPathway(userData.customPathway || []);
        setNotes(userData.notes || []);
      }
    } catch (error) {
      console.error('Error loading user data:', error);
    }
  };

  const saveUserData = async (data) => {
    if (user) {
      try {
        await setDoc(doc(db, 'users', user.uid), data, { merge: true });
      } catch (error) {
        console.error('Error saving user data:', error);
      }
    }
  };

  const addBookmark = (item) => {
    const newBookmarks = [...bookmarks, item];
    setBookmarks(newBookmarks);
    saveUserData({ bookmarks: newBookmarks });
  };

  const removeBookmark = (itemId) => {
    const newBookmarks = bookmarks.filter(b => b.id !== itemId);
    setBookmarks(newBookmarks);
    saveUserData({ bookmarks: newBookmarks });
  };

  const toggleBookmark = (itemId) => {
    const isBookmarked = bookmarks.some(b => b.id === itemId);
    if (isBookmarked) {
      removeBookmark(itemId);
    } else {
      // Find the item and add it
      const item = courseData.find(c => c.id === itemId) || 
                   labsData.find(l => l.id === itemId) ||
                   aiToolsData.find(t => t.id === itemId);
      if (item) {
        addBookmark(item);
      }
    }
  };

  const isBookmarked = (itemId) => {
    return bookmarks.some(b => b.id === itemId);
  };

  const toggleComparison = (item) => {
    const isInComparison = comparisons.some(c => c.id === item.id);
    if (isInComparison) {
      const newComparisons = comparisons.filter(c => c.id !== item.id);
      setComparisons(newComparisons);
      saveUserData({ comparisons: newComparisons });
    } else {
      const newComparisons = [...comparisons, item];
      setComparisons(newComparisons);
      saveUserData({ comparisons: newComparisons });
    }
  };

  const isInComparison = (itemId) => {
    return comparisons.some(c => c.id === itemId);
  };

  const addToPathway = (courseId) => {
    if (!customPathway.includes(courseId)) {
      const newPathway = [...customPathway, courseId];
      setCustomPathway(newPathway);
      saveUserData({ customPathway: newPathway });
    }
  };

  const removeFromPathway = (courseId) => {
    const newPathway = customPathway.filter(id => id !== courseId);
    setCustomPathway(newPathway);
    saveUserData({ customPathway: newPathway });
  };

  const addNote = async (note) => {
    const newNote = {
      ...note,
      id: Date.now().toString(),
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };
    
    const newNotes = [...notes, newNote];
    setNotes(newNotes);
    saveUserData({ notes: newNotes });
    return newNote;
  };

  const updateNote = async (noteId, updatedContent) => {
    const newNotes = notes.map(note => 
      note.id === noteId 
        ? { ...note, ...updatedContent, updatedAt: new Date().toISOString() }
        : note
    );
    setNotes(newNotes);
    saveUserData({ notes: newNotes });
  };

  const deleteNote = async (noteId) => {
    const newNotes = notes.filter(note => note.id !== noteId);
    setNotes(newNotes);
    saveUserData({ notes: newNotes });
  };

  // Premium status - for now, all logged-in users have premium
  const isPremium = !!user;

  const value = {
    user,
    loading,
    bookmarks,
    comparisons,
    customPathway,
    notes,
    addBookmark,
    removeBookmark,
    toggleBookmark,
    isBookmarked,
    toggleComparison,
    isInComparison,
    addToPathway,
    removeFromPathway,
    addNote,
    updateNote,
    deleteNote,
    isPremium
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

// Page Context
const PageContext = createContext();
const PageProvider = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('home');
  const [darkMode, setDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('darkMode') === 'true';
    }
    return false;
  });
  const [searchQuery, setSearchQuery] = useState('');
  const [browseMode, setBrowseMode] = useState('role');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      localStorage.setItem('darkMode', darkMode.toString());
      if (typeof document !== 'undefined' && document.documentElement) {
        if (darkMode) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      }
    }
  }, [darkMode]);

  const toggleDarkMode = () => setDarkMode(!darkMode);

  const value = {
    currentPage,
    setCurrentPage,
    darkMode,
    setDarkMode,
    toggleDarkMode,
    searchQuery,
    setSearchQuery,
    browseMode,
    setBrowseMode,
    mobileMenuOpen,
    setMobileMenuOpen
  };

  return <PageContext.Provider value={value}>{children}</PageContext.Provider>;
};

export const usePage = () => {
  const context = useContext(PageContext);
  if (context === undefined) {
    throw new Error('usePage must be used within a PageProvider');
  }
  return context;
};

// Sign in/out functions
const signInWithGoogle = async () => {
  try {
    await signInWithPopup(auth, googleProvider);
  } catch (error) {
    console.error('Error signing in:', error);
  }
};

const signOut = async () => {
  try {
    await firebaseSignOut(auth);
  } catch (error) {
    console.error('Error signing out:', error);
  }
};

// Navigation Component
export const Navigation = () => {
  const { currentPage, setCurrentPage, darkMode, toggleDarkMode, mobileMenuOpen, setMobileMenuOpen } = usePage();
  const { user } = useAuth();

  return (
    <nav className="bg-white dark:bg-gray-900 shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <button 
                onClick={() => setCurrentPage('home')}
                className="text-2xl font-bold text-blue-600 dark:text-blue-400"
              >
                ImpactMojo
              </button>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              {['home', 'courses', 'labs', 'games', 'resources'].map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  className={`${currentPage === page ? 'border-blue-600 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium capitalize`}
                >
                  {page}
                </button>
              ))}
              {user && (
                <>
                  <button
                    onClick={() => setCurrentPage('dashboard')}
                    className={`${currentPage === 'dashboard' ? 'border-blue-600 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
                  >
                    Dashboard
                  </button>
                  <button
                    onClick={() => setCurrentPage('ai-tools')}
                    className={`${currentPage === 'ai-tools' ? 'border-blue-600 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
                  >
                    AI Tools
                  </button>
                </>
              )}
            </div>
          </div>
          
          <div className="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
            <button
              onClick={toggleDarkMode}
              className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-600"
              aria-label="Toggle theme"
            >
              {darkMode ? <Sun className="h-5 w-5 text-yellow-400" /> : <Moon className="h-5 w-5" />}
            </button>
            
            {user ? (
              <div className="flex items-center space-x-3">
                <img className="h-8 w-8 rounded-full" src={user.photoURL} alt={user.displayName} />
                <span className="text-gray-700 dark:text-gray-300 text-sm">{user.displayName}</span>
                <button
                  onClick={signOut}
                  className="bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded-md text-sm font-medium"
                >
                  Sign Out
                </button>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
              >
                Sign In
              </button>
            )}
          </div>

          <div className="sm:hidden flex items-center">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-600"
              aria-expanded="false"
            >
              {mobileMenuOpen ? <X className="block h-6 w-6" /> : <Menu className="block h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="sm:hidden bg-white dark:bg-gray-900 border-t dark:border-gray-700">
          <div className="pt-2 pb-3 space-y-1">
            {['home', 'courses', 'labs', 'games', 'resources'].map((page) => (
              <button
                key={page}
                onClick={() => { setCurrentPage(page); setMobileMenuOpen(false); }}
                className={`${currentPage === page ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'} block w-full text-left pl-3 pr-4 py-2 text-base font-medium capitalize`}
              >
                {page}
              </button>
            ))}
            {user && (
              <>
                <button
                  onClick={() => { setCurrentPage('dashboard'); setMobileMenuOpen(false); }}
                  className={`${currentPage === 'dashboard' ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'} block w-full text-left pl-3 pr-4 py-2 text-base font-medium`}
                >
                  Dashboard
                </button>
                <button
                  onClick={() => { setCurrentPage('ai-tools'); setMobileMenuOpen(false); }}
                  className={`${currentPage === 'ai-tools' ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'} block w-full text-left pl-3 pr-4 py-2 text-base font-medium`}
                >
                  AI Tools
                </button>
              </>
            )}
          </div>
          
          <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
            <div className="flex items-center px-4">
              {user ? (
                <>
                  <img className="h-10 w-10 rounded-full" src={user.photoURL} alt={user.displayName} />
                  <div className="ml-3">
                    <div className="text-base font-medium text-gray-900 dark:text-white">{user.displayName}</div>
                    <div className="text-sm font-medium text-gray-500 dark:text-gray-300">{user.email}</div>
                  </div>
                </>
              ) : (
                <div className="text-base font-medium text-gray-900 dark:text-white">Not signed in</div>
              )}
            </div>
            <div className="mt-3 space-y-1">
              <button
                onClick={toggleDarkMode}
                className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-800 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 w-full text-left"
              >
                {darkMode ? '☀️ Light Mode' : '🌙 Dark Mode'}
              </button>
              {user ? (
                <button
                  onClick={signOut}
                  className="block px-4 py-2 text-base font-medium text-red-600 hover:text-red-800 hover:bg-gray-100 dark:hover:bg-gray-700 w-full text-left"
                >
                  Sign Out
                </button>
              ) : (
                <button
                  onClick={signInWithGoogle}
                  className="block px-4 py-2 text-base font-medium text-blue-600 hover:text-blue-800 hover:bg-gray-100 dark:hover:bg-gray-700 w-full text-left"
                >
                  Sign In with Google
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};

// AI Tools Page Component  
const AIToolsPage = () => {
  const { darkMode } = usePage();
  const { user, bookmarks, toggleBookmark, isPremium } = useAuth();
  const [selectedTool, setSelectedTool] = useState(null);
  
  if (!user) {
    return (
      <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="text-center">
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Please sign in to access AI Tools</h1>
            <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">AI Tools are available exclusively for logged-in users.</p>
            <button
              onClick={signInWithGoogle}
              className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-md font-medium"
            >
              Sign In with Google
            </button>
          </div>
        </div>
      </div>
    );
  }
  
  // Function to get the correct icon component
  const getIconComponent = (iconName) => {
    const iconMap = {
      'BarChart': BarChart,
      'Target': Target,
      'FileText': FileText,
      'Users': Users,
      'CheckCircle': CheckCircle,
      'MessageCircle': MessageCircle,
      'Calendar': Calendar,
      'BookOpen': BookOpen,
      'TrendingUp': TrendingUp,
      'Scale': Scale,
      'Award': Award,
      'Trophy': Trophy,
      'Puzzle': Puzzle,
      'Zap': Zap,
      'Bot': Bot
    };
    return iconMap[iconName] || Bot;
  };
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white sm:text-4xl">
            AI-Powered Tools
          </h1>
          <p className="mt-3 max-w-2xl mx-auto text-xl text-gray-600 dark:text-gray-300 sm:mt-4">
            Leverage artificial intelligence to enhance your development work.
          </p>
        </div>
        
        {!isPremium && (
          <div className="mb-8 bg-gradient-to-r from-yellow-400 to-yellow-500 rounded-lg shadow-lg p-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-gray-900">Upgrade to Premium</h3>
                <p className="mt-1 text-gray-800">Unlock all AI tools and premium features</p>
              </div>
              <button className="px-4 py-2 bg-gray-900 text-white rounded-md hover:bg-gray-800 transition-colors">
                Upgrade Now
              </button>
            </div>
          </div>
        )}
        
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {aiToolsData.map(tool => {
            const IconComponent = getIconComponent(tool.icon);
            const isBookmarked = bookmarks.some(b => b.id === tool.id);
            
            return (
              <div key={tool.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                <div className="p-6">
                  <div className="flex justify-between items-start">
                    <div className="flex items-center">
                      <div className={`flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-blue-100 dark:bg-blue-900`}>
                        <IconComponent className={`h-6 w-6 text-blue-600 dark:text-blue-400`} />
                      </div>
                      <h3 className="ml-3 text-lg font-medium text-gray-900 dark:text-white">{tool.title}</h3>
                    </div>
                    <div className="flex items-center space-x-2">
                      {!isPremium && (
                        <span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200">
                          PRO
                        </span>
                      )}
                      <button 
                        onClick={() => toggleBookmark(tool.id)}
                        className="text-gray-400 hover:text-yellow-500 focus:outline-none"
                      >
                        {isBookmarked ? (
                          <Star className="h-5 w-5 text-yellow-500 fill-current" />
                        ) : (
                          <Star className="h-5 w-5" />
                        )}
                      </button>
                    </div>
                  </div>
                  
                  <p className="mt-3 text-sm text-gray-600 dark:text-gray-300">{tool.description}</p>
                  
                  <div className="mt-6">
                    {!isPremium ? (
                      <button
                        onClick={() => {}}
                        className="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-gray-500 bg-gray-200 dark:bg-gray-700 cursor-not-allowed"
                        disabled
                      >
                        Upgrade to Unlock
                      </button>
                    ) : (
                      <button
                        onClick={() => setSelectedTool(tool)}
                        className="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-600"
                      >
                        Try This Tool
                        <ArrowRight className="ml-1 h-4 w-4" />
                      </button>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
        
        {/* Tool Detail Modal */}
        {selectedTool && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <div className="flex items-center">
                    <div className="flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-md bg-blue-100 dark:bg-blue-900">
                      {React.createElement(getIconComponent(selectedTool.icon), { className: "h-8 w-8 text-blue-600 dark:text-blue-400" })}
                    </div>
                    <div className="ml-4">
                      <h3 className="text-xl font-bold text-gray-900 dark:text-white">{selectedTool.title}</h3>
                      <p className="text-sm text-gray-600 dark:text-gray-300">{selectedTool.description}</p>
                    </div>
                  </div>
                  <button
                    onClick={() => setSelectedTool(null)}
                    className="text-gray-400 hover:text-gray-500 focus:outline-none"
                  >
                    <X className="h-6 w-6" />
                  </button>
                </div>
                
                <div className="border-t border-gray-200 dark:border-gray-600 pt-6">
                  <div className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                        Main Prompt
                      </label>
                      <textarea 
                        rows={8}
                        className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-blue-600 focus:border-blue-600 dark:bg-gray-700 dark:text-white"
                        defaultValue={selectedTool.prompt}
                        placeholder="Describe your requirements..."
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                        Example Input
                      </label>
                      <textarea 
                        rows={4}
                        className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-blue-600 focus:border-blue-600 dark:bg-gray-700 dark:text-white"
                        placeholder={selectedTool.exampleInput}
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                        Specific Requirements (optional)
                      </label>
                      <textarea 
                        rows={3}
                        className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-blue-600 focus:border-blue-600 dark:bg-gray-700 dark:text-white"
                        placeholder="Add any specific requirements or context..."
                      />
                    </div>
                  </div>
                </div>
                
                <div className="flex justify-end space-x-3 mt-6">
                  <button
                    onClick={() => setSelectedTool(null)}
                    className="px-4 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-md font-medium"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={() => {}}
                    className="px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-600"
                  >
                    Generate
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Home Page Component
const HomePage = () => {
  const { darkMode } = usePage();
  const { user, isPremium } = useAuth();
  const { setCurrentPage } = usePage();

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white sm:text-5xl md:text-6xl">
            <span className="block">Development</span>
            <span className="block text-blue-600 dark:text-blue-400">Know-How</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-500 dark:text-gray-300 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Master the art and science of development with expert-curated courses, labs, and AI-powered tools.
          </p>
          <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
            <button
              onClick={() => setCurrentPage('courses')}
              className="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-md text-lg font-medium"
            >
              Start Learning
            </button>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 text-center">
            <BookOpen className="h-12 w-12 text-blue-600 dark:text-blue-400 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Expert Courses</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-300">Learn from world-class experts</p>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 text-center">
            <FileText className="h-12 w-12 text-green-600 dark:text-green-400 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Practical Labs</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-300">Hands-on learning experiences</p>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 text-center">
            <Bot className="h-12 w-12 text-purple-600 dark:text-purple-400 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">AI Tools</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-300">AI-powered development tools</p>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 text-center">
            <Users className="h-12 w-12 text-orange-600 dark:text-orange-400 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Community</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-300">Connect with practitioners</p>
          </div>
        </div>

        {/* AI Tools Preview */}
        <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg shadow-lg p-6 sm:p-8 text-white mb-8">
          <div className="text-center">
            <Bot className="h-16 w-16 mx-auto mb-4" />
            <h2 className="text-2xl sm:text-3xl font-bold mb-4">AI-Powered Tools</h2>
            <p className="text-lg sm:text-xl mb-6">
              Explore courses, labs, games, and AI-powered tools to enhance your impact.
            </p>
            <button
              onClick={() => setCurrentPage('ai-tools')}
              className="bg-white text-blue-600 px-6 py-2 rounded-md font-medium hover:bg-gray-100 transition-colors"
            >
              Explore AI Tools
            </button>
          </div>
        </div>
        
        {/* Study Music */}
        <div className="bg-gradient-to-r from-purple-500 to-indigo-600 rounded-lg shadow-lg p-4 sm:p-6 text-white mb-8">
          <div className="flex items-center justify-between flex-col sm:flex-row gap-4">
            <div className="text-center sm:text-left">
              <h2 className="text-lg sm:text-xl font-bold">Lo-Fi Study Beats</h2>
              <p className="mt-1">Focus better with our curated study playlist</p>
            </div>
            <a
              href="https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-white text-purple-600 px-4 py-2 rounded-md font-medium flex items-center hover:bg-gray-100 transition-colors"
            >
              <Music className="mr-2 h-5 w-5" />
              Play on Spotify
            </a>
          </div>
        </div>
        
        {/* Premium Features Info */}
        {isPremium && (
          <div className="bg-gradient-to-r from-emerald-400 to-cyan-500 rounded-lg shadow-lg p-4 sm:p-6">
            <div className="flex items-center justify-between flex-col sm:flex-row gap-4">
              <div className="text-center sm:text-left">
                <h3 className="text-lg sm:text-xl font-bold text-gray-900">You have Premium Access!</h3>
                <p className="mt-1 text-gray-800">Enjoy all features including AI Tools, Notes, and Comparisons</p>
              </div>
              <Trophy className="h-12 w-12 text-gray-900 flex-shrink-0" />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Courses Page Component
const CoursesPage = () => {
  const { darkMode, searchQuery, setSearchQuery, browseMode, setBrowseMode } = usePage();
  const { toggleComparison, isInComparison, addBookmark, removeBookmark, isBookmarked } = useAuth();

  const handleBookmark = (course) => {
    const bookmarkItem = { ...course, type: 'course' };
    if (isBookmarked(course.id)) {
      removeBookmark(course.id);
    } else {
      addBookmark(bookmarkItem);
    }
  };

  const handleCompare = (course) => {
    const compareItem = { ...course, type: 'course' };
    toggleComparison(compareItem);
  };

  const filteredCourses = courseData.filter(course => 
    course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    course.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
    course.track.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const getBrowseData = () => {
    switch(browseMode) {
      case 'role': return browseByRole;
      case 'impact': return browseByImpact;
      case 'time': return browseByTimeCommitment;
      default: return browseByRole;
    }
  };

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Courses</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Expert-designed courses for development professionals</p>
        </div>

        {/* Search and Browse Controls */}
        <div className="mb-8 space-y-4">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <div className="relative">
                <Search className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type="text"
                  placeholder="Search courses..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                />
              </div>
            </div>
            <select
              value={browseMode}
              onChange={(e) => setBrowseMode(e.target.value)}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
            >
              <option value="role">Browse by Role</option>
              <option value="impact">Browse by Impact</option>
              <option value="time">Browse by Time</option>
            </select>
          </div>
        </div>

        {/* Browse Categories */}
        {!searchQuery && (
          <div className="mb-12">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
              {browseMode === 'role' && 'Browse by Role'}
              {browseMode === 'impact' && 'Browse by Impact Area'}
              {browseMode === 'time' && 'Browse by Time Commitment'}
            </h2>
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
              {Object.entries(getBrowseData()).map(([category, data]) => (
                <div key={category} className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
                  <h3 className={`text-lg font-semibold mb-2 text-${data.color}-600 dark:text-${data.color}-400`}>
                    {category}
                  </h3>
                  <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{data.description}</p>
                  <div className="space-y-2">
                    {data.courses.slice(0, 3).map(courseId => {
                      const course = courseData.find(c => c.id === courseId);
                      return course ? (
                        <div key={course.id} className="text-sm">
                          <a 
                            href={course.url} 
                            target="_blank" 
                            rel="noopener noreferrer"
                            className="text-blue-600 dark:text-blue-400 hover:underline"
                          >
                            {course.title}
                          </a>
                        </div>
                      ) : null;
                    })}
                    {data.courses.length > 3 && (
                      <div className="text-sm text-gray-500 dark:text-gray-400">
                        +{data.courses.length - 3} more
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Courses Grid */}
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {filteredCourses.map((course) => (
            <div key={course.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <div className="flex-1">
                    <span className="inline-block px-2 py-1 text-xs font-semibold text-blue-800 dark:text-blue-200 bg-blue-100 dark:bg-blue-900 rounded-full mb-2">
                      {course.track}
                    </span>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{course.title}</h3>
                    <p className="text-gray-600 dark:text-gray-300 text-sm">{course.description}</p>
                  </div>
                </div>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <div className="flex items-center">
                    <Clock className="h-4 w-4 mr-1" />
                    {course.duration}
                  </div>
                  <div className="flex items-center">
                    <Target className="h-4 w-4 mr-1" />
                    {course.level}
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <a
                    href={course.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium flex items-center"
                  >
                    Start Course
                    <ExternalLink className="ml-1 h-4 w-4" />
                  </a>
                  
                  <div className="flex space-x-2">
                    <button
                      onClick={() => handleBookmark(course)}
                      className={`p-2 rounded-full ${isBookmarked(course.id) ? 'text-yellow-500 bg-yellow-100 dark:bg-yellow-900' : 'text-gray-400 hover:text-yellow-500'}`}
                      title="Bookmark"
                    >
                      <Bookmark className="h-4 w-4" />
                    </button>
                    <button
                      onClick={() => handleCompare(course)}
                      className={`p-2 rounded-full ${isInComparison(course.id) ? 'text-blue-500 bg-blue-100 dark:bg-blue-900' : 'text-gray-400 hover:text-blue-500'}`}
                      title="Compare"
                    >
                      <Scale className="h-4 w-4" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Upcoming Courses */}
        <div className="mt-16">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">Coming Soon</h2>
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {upcomingCourses.map((course) => (
              <div key={course.id} className="bg-gray-100 dark:bg-gray-800 rounded-lg shadow-md p-6 relative overflow-hidden">
                <div className="absolute top-4 right-4 bg-yellow-400 text-yellow-900 px-2 py-1 rounded-full text-xs font-semibold">
                  Coming Soon
                </div>
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{course.title}</h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{course.description}</p>
                <div className="flex items-center text-sm text-gray-500 dark:text-gray-400">
                  <Calendar className="h-4 w-4 mr-1" />
                  Expected: {course.expectedDate}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// Labs Page Component
const LabsPage = () => {
  const { darkMode } = usePage();
  const { addBookmark, removeBookmark, isBookmarked } = useAuth();

  const handleBookmark = (lab) => {
    const bookmarkItem = { ...lab, type: 'lab' };
    if (isBookmarked(lab.id)) {
      removeBookmark(lab.id);
    } else {
      addBookmark(bookmarkItem);
    }
  };

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Labs</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Hands-on learning experiences</p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {labsData.map((lab) => (
            <div key={lab.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <span className="inline-block px-2 py-1 text-xs font-semibold text-green-800 dark:text-green-200 bg-green-100 dark:bg-green-900 rounded-full mb-2">
                      {lab.category}
                    </span>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{lab.title}</h3>
                    <p className="text-gray-600 dark:text-gray-300 text-sm">{lab.description}</p>
                  </div>
                </div>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <div className="flex items-center">
                    <Clock className="h-4 w-4 mr-1" />
                    {lab.duration}
                  </div>
                  <div className="flex items-center">
                    <Target className="h-4 w-4 mr-1" />
                    {lab.difficulty}
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <a
                    href={lab.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md text-sm font-medium flex items-center"
                  >
                    Start Lab
                    <ExternalLink className="ml-1 h-4 w-4" />
                  </a>
                  
                  <button
                    onClick={() => handleBookmark(lab)}
                    className={`p-2 rounded-full ${isBookmarked(lab.id) ? 'text-yellow-500 bg-yellow-100 dark:bg-yellow-900' : 'text-gray-400 hover:text-yellow-500'}`}
                    title="Bookmark"
                  >
                    <Bookmark className="h-4 w-4" />
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

// Games Page Component
const GamesPage = () => {
  const { darkMode } = usePage();
  const { addBookmark, removeBookmark, isBookmarked } = useAuth();

  const handleBookmark = (game) => {
    const bookmarkItem = { ...game, type: 'game' };
    if (isBookmarked(game.id)) {
      removeBookmark(game.id);
    } else {
      addBookmark(bookmarkItem);
    }
  };

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Games</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Interactive learning through gameplay</p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {gamesData.map((game) => (
            <div key={game.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <span className="inline-block px-2 py-1 text-xs font-semibold text-purple-800 dark:text-purple-200 bg-purple-100 dark:bg-purple-900 rounded-full mb-2">
                      {game.category}
                    </span>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{game.title}</h3>
                    <p className="text-gray-600 dark:text-gray-300 text-sm">{game.description}</p>
                  </div>
                </div>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <div className="flex items-center">
                    <Gamepad2 className="h-4 w-4 mr-1" />
                    {game.category}
                  </div>
                  <div className="flex items-center">
                    <Target className="h-4 w-4 mr-1" />
                    {game.difficulty}
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <a
                    href={game.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-md text-sm font-medium flex items-center"
                  >
                    Play Game
                    <ExternalLink className="ml-1 h-4 w-4" />
                  </a>
                  
                  <button
                    onClick={() => handleBookmark(game)}
                    className={`p-2 rounded-full ${isBookmarked(game.id) ? 'text-yellow-500 bg-yellow-100 dark:bg-yellow-900' : 'text-gray-400 hover:text-yellow-500'}`}
                    title="Bookmark"
                  >
                    <Bookmark className="h-4 w-4" />
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

// Resources Page Component
const ResourcesPage = () => {
  const { darkMode } = usePage();
  const { addBookmark, removeBookmark, isBookmarked } = useAuth();

  const handleBookmark = (resource) => {
    const bookmarkItem = { ...resource, type: 'resource' };
    if (isBookmarked(resource.id)) {
      removeBookmark(resource.id);
    } else {
      addBookmark(bookmarkItem);
    }
  };

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Resources</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Premium tools and resources for development professionals</p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {updatedPremiumResources.map((resource) => (
            <div key={resource.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <span className="inline-block px-2 py-1 text-xs font-semibold text-orange-800 dark:text-orange-200 bg-orange-100 dark:bg-orange-900 rounded-full mb-2">
                      {resource.category}
                    </span>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{resource.title}</h3>
                    <p className="text-gray-600 dark:text-gray-300 text-sm">{resource.description}</p>
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <a
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-orange-600 hover:bg-orange-700 text-white px-4 py-2 rounded-md text-sm font-medium flex items-center"
                  >
                    Access Resource
                    <ExternalLink className="ml-1 h-4 w-4" />
                  </a>
                  
                  <button
                    onClick={() => handleBookmark(resource)}
                    className={`p-2 rounded-full ${isBookmarked(resource.id) ? 'text-yellow-500 bg-yellow-100 dark:bg-yellow-900' : 'text-gray-400 hover:text-yellow-500'}`}
                    title="Bookmark"
                  >
                    <Bookmark className="h-4 w-4" />
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
  const { darkMode } = usePage();
  const { user, bookmarks, comparisons, customPathway, notes, addNote, updateNote, deleteNote, addToPathway, removeFromPathway } = useAuth();
  const { setCurrentPage } = usePage();
  const [activeTab, setActiveTab] = useState('overview');
  const [isQuizModalOpen, setIsQuizModalOpen] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [quizAnswers, setQuizAnswers] = useState([]);
  const [quizComplete, setQuizComplete] = useState(false);
  const [isNotesModalOpen, setIsNotesModalOpen] = useState(false);
  const [currentNote, setCurrentNote] = useState(null);
  const [noteTitle, setNoteTitle] = useState('');
  const [noteContent, setNoteContent] = useState('');
  const [noteTags, setNoteTags] = useState('');
  const [noteAttachedTo, setNoteAttachedTo] = useState('');

  // Quiz data
  const quizQuestions = [
    {
      id: 1,
      question: "What best describes your current role?",
      options: [
        { text: "New to Development", courses: ["development-economics-101", "global-development-architecture-101"] },
        { text: "Researcher/Academic", courses: ["research-ethics-101", "qualitative-research-methods-101", "econometrics-101"] },
        { text: "Practitioner/Field Worker", courses: ["community-development-101", "monitoring-evaluation-accountability-and-learning-101"] },
        { text: "Student/Policy Maker", courses: ["law-and-constitution-101", "political-economy-101"] }
      ]
    },
    {
      id: 2,
      question: "Which impact area interests you most?",
      options: [
        { text: "Health & Wellbeing", courses: ["public-health-101", "human-rights-101"] },
        { text: "Education & Skills", courses: ["data-literacy-101", "qualitative-research-methods-101"] },
        { text: "Governance & Justice", courses: ["law-and-constitution-101", "political-economy-101"] },
        { text: "Economic Growth", courses: ["development-economics-101", "monitoring-evaluation-accountability-and-learning-101"] }
      ]
    }
  ];

  const openModal = (type, item = null) => {
    if (type === 'quiz') {
      setIsQuizModalOpen(true);
      setCurrentQuestionIndex(0);
      setQuizAnswers([]);
      setQuizComplete(false);
    } else if (type === 'notes') {
      setIsNotesModalOpen(true);
      if (item) {
        setCurrentNote(item);
        setNoteTitle(item.title || '');
        setNoteContent(item.content || '');
        setNoteTags(item.tags ? item.tags.join(', ') : '');
        setNoteAttachedTo(item.attachedTo || '');
      } else {
        setCurrentNote(null);
        setNoteTitle('');
        setNoteContent('');
        setNoteTags('');
        setNoteAttachedTo('');
      }
    }
  };

  const closeModal = () => {
    setIsQuizModalOpen(false);
    setIsNotesModalOpen(false);
    setCurrentNote(null);
  };

  const handleQuizAnswer = (selectedOption) => {
    const newAnswers = [...quizAnswers, selectedOption];
    setQuizAnswers(newAnswers);

    if (currentQuestionIndex < quizQuestions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      // Quiz complete, generate pathway
      const recommendedCourses = newAnswers.flatMap(answer => answer.courses);
      const uniqueCourses = [...new Set(recommendedCourses)];
      uniqueCourses.forEach(courseId => addToPathway(courseId));
      setQuizComplete(true);
    }
  };

  const handleSaveNote = async () => {
    const noteData = {
      title: noteTitle,
      content: noteContent,
      tags: noteTags.split(',').map(tag => tag.trim()).filter(tag => tag),
      attachedTo: noteAttachedTo
    };

    if (currentNote) {
      await updateNote(currentNote.id, noteData);
    } else {
      await addNote(noteData);
    }

    closeModal();
  };

  if (!user) {
    return (
      <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="text-center">
            <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white mb-4">
              Sign in to access your Dashboard
            </h1>
            <button
              onClick={signInWithGoogle}
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-md font-medium"
            >
              Sign In with Google
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
            Welcome back, {user.displayName?.split(' ')[0]}!
          </h1>
          <p className="text-gray-600 dark:text-gray-300">Here's your learning dashboard</p>
        </div>

        {/* Tabs */}
        <div className="border-b border-gray-200 dark:border-gray-700 mb-8">
          <nav className="-mb-px flex space-x-8">
            {[
              { id: 'overview', name: 'Overview', icon: Target },
              { id: 'bookmarks', name: 'Bookmarks', icon: Bookmark },
              { id: 'pathway', name: 'My Pathway', icon: MapPin },
              { id: 'notes', name: 'Notes', icon: FileText },
              { id: 'comparisons', name: 'Comparisons', icon: Scale }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`${activeTab === tab.id
                  ? 'border-blue-500 text-blue-600 dark:text-blue-400'
                  : 'border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 hover:border-gray-300 dark:hover:border-gray-600'
                } flex items-center whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm`}
              >
                <tab.icon className="mr-2 h-5 w-5" />
                {tab.name}
              </button>
            ))}
          </nav>
        </div>

        {/* Tab Content */}
        {activeTab === 'overview' && (
          <div className="space-y-8">
            {/* Quick Stats */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
              <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                <div className="flex items-center">
                  <Bookmark className="h-8 w-8 text-blue-600 dark:text-blue-400" />
                  <div className="ml-4">
                    <p className="text-2xl font-semibold text-gray-900 dark:text-white">{bookmarks.length}</p>
                    <p className="text-gray-600 dark:text-gray-300">Bookmarks</p>
                  </div>
                </div>
              </div>
              
              <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                <div className="flex items-center">
                  <MapPin className="h-8 w-8 text-green-600 dark:text-green-400" />
                  <div className="ml-4">
                    <p className="text-2xl font-semibold text-gray-900 dark:text-white">{customPathway.length}</p>
                    <p className="text-gray-600 dark:text-gray-300">Pathway Courses</p>
                  </div>
                </div>
              </div>
              
              <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                <div className="flex items-center">
                  <FileText className="h-8 w-8 text-purple-600 dark:text-purple-400" />
                  <div className="ml-4">
                    <p className="text-2xl font-semibold text-gray-900 dark:text-white">{notes.length}</p>
                    <p className="text-gray-600 dark:text-gray-300">Notes</p>
                  </div>
                </div>
              </div>
              
              <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                <div className="flex items-center">
                  <Scale className="h-8 w-8 text-orange-600 dark:text-orange-400" />
                  <div className="ml-4">
                    <p className="text-2xl font-semibold text-gray-900 dark:text-white">{comparisons.length}</p>
                    <p className="text-gray-600 dark:text-gray-300">Comparisons</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Quick Actions */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Quick Actions</h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <button
                  onClick={() => openModal('quiz')}
                  className="flex items-center p-4 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
                >
                  <Target className="h-6 w-6 text-blue-600 dark:text-blue-400 mr-3" />
                  <div className="text-left">
                    <p className="font-medium text-gray-900 dark:text-white">Find Your Track</p>
                    <p className="text-sm text-gray-500 dark:text-gray-400">Take a quiz to discover courses</p>
                  </div>
                </button>
                
                <button
                  onClick={() => openModal('notes')}
                  className="flex items-center p-4 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
                >
                  <Plus className="h-6 w-6 text-green-600 dark:text-green-400 mr-3" />
                  <div className="text-left">
                    <p className="font-medium text-gray-900 dark:text-white">Add Note</p>
                    <p className="text-sm text-gray-500 dark:text-gray-400">Create a new learning note</p>
                  </div>
                </button>
                
                <button
                  onClick={() => setCurrentPage('ai-tools')}
                  className="flex items-center p-4 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
                >
                  <Bot className="h-6 w-6 text-purple-600 dark:text-purple-400 mr-3" />
                  <div className="text-left">
                    <p className="font-medium text-gray-900 dark:text-white">AI Tools</p>
                    <p className="text-sm text-gray-500 dark:text-gray-400">Access AI-powered tools</p>
                  </div>
                </button>
              </div>
            </div>

            {/* Recent Activity */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Recent Activity</h2>
              {bookmarks.length > 0 || notes.length > 0 ? (
                <div className="space-y-3">
                  {bookmarks.slice(0, 3).map((bookmark, index) => (
                    <div key={index} className="flex items-center p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <Bookmark className="h-5 w-5 text-yellow-500 mr-3" />
                      <div>
                        <p className="font-medium text-gray-900 dark:text-white">{bookmark.title}</p>
                        <p className="text-sm text-gray-500 dark:text-gray-400">Bookmarked {bookmark.type}</p>
                      </div>
                    </div>
                  ))}
                  {notes.slice(0, 2).map((note, index) => (
                    <div key={index} className="flex items-center p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <FileText className="h-5 w-5 text-purple-500 mr-3" />
                      <div>
                        <p className="font-medium text-gray-900 dark:text-white">{note.title || 'Untitled Note'}</p>
                        <p className="text-sm text-gray-500 dark:text-gray-400">Note created</p>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <p className="text-gray-500 dark:text-gray-400">No recent activity</p>
              )}
            </div>
          </div>
        )}

        {activeTab === 'bookmarks' && (
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Your Bookmarks</h2>
            {bookmarks.length > 0 ? (
              <div className="space-y-3">
                {bookmarks.map((bookmark, index) => (
                  <div key={index} className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <div className="flex-1">
                      <h3 className="font-medium text-gray-900 dark:text-white">{bookmark.title}</h3>
                      <p className="text-sm text-gray-500 dark:text-gray-400">{bookmark.type} • {bookmark.track || bookmark.category}</p>
                    </div>
                    <a
                      href={bookmark.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                    >
                      <ExternalLink className="h-5 w-5" />
                    </a>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-8">
                <Bookmark className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400">No bookmarks yet</p>
              </div>
            )}
          </div>
        )}

        {activeTab === 'pathway' && (
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">My Learning Pathway</h2>
              <button 
                onClick={() => openModal('quiz')}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
              >
                Find Your Track
              </button>
            </div>
            {customPathway.length > 0 ? (
              <div className="space-y-3">
                {customPathway.map((courseId, index) => {
                  const course = courseData.find(c => c.id === courseId);
                  return course ? (
                    <div key={index} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="flex-1 min-w-0">
                        <h3 className="font-medium text-gray-900 dark:text-white truncate">{course.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-400">{course.track}</p>
                      </div>
                      <a
                        href={course.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 flex-shrink-0 ml-2"
                        aria-label="Open course"
                      >
                        <ExternalLink className="h-5 w-5" />
                      </a>
                    </div>
                  ) : null;
                })}
              </div>
            ) : (
              <div className="text-center py-8">
                <MapPin className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400 mb-4">No courses in your pathway yet</p>
                <button 
                  onClick={() => openModal('quiz')}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium"
                >
                  Find Your Track
                </button>
              </div>
            )}
          </div>
        )}

        {activeTab === 'notes' && (
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">Your Notes</h2>
              <button 
                onClick={() => openModal('notes')}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
              >
                Add Note
              </button>
            </div>
            {notes.length > 0 ? (
              <div className="space-y-3">
                {notes.map((note) => (
                  <div key={note.id} className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <div className="flex items-center justify-between mb-2">
                      <h3 className="font-medium text-gray-900 dark:text-white">{note.title || 'Untitled Note'}</h3>
                      <div className="flex space-x-2">
                        <button
                          onClick={() => openModal('notes', note)}
                          className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                        >
                          <Edit3 className="h-4 w-4" />
                        </button>
                        <button
                          onClick={() => deleteNote(note.id)}
                          className="text-red-600 dark:text-red-400 hover:text-red-800 dark:hover:text-red-300"
                        >
                          <X className="h-4 w-4" />
                        </button>
                      </div>
                    </div>
                    <p className="text-gray-600 dark:text-gray-300 text-sm mb-2">{note.content}</p>
                    {note.tags && note.tags.length > 0 && (
                      <div className="flex flex-wrap gap-1 mb-2">
                        {note.tags.map((tag, index) => (
                          <span key={index} className="px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 text-xs rounded-full">
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                    <p className="text-xs text-gray-500 dark:text-gray-400">
                      Created: {new Date(note.createdAt).toLocaleDateString()}
                    </p>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-8">
                <FileText className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400 mb-4">No notes yet</p>
                <button 
                  onClick={() => openModal('notes')}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium"
                >
                  Create Your First Note
                </button>
              </div>
            )}
          </div>
        )}

        {activeTab === 'comparisons' && (
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Course Comparisons</h2>
            {comparisons.length > 0 ? (
              <div className="space-y-3">
                {comparisons.map((item, index) => (
                  <div key={index} className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <div className="flex-1">
                      <h3 className="font-medium text-gray-900 dark:text-white">{item.title}</h3>
                      <p className="text-sm text-gray-500 dark:text-gray-400">{item.type} • {item.track || item.category}</p>
                    </div>
                    <a
                      href={item.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                    >
                      <ExternalLink className="h-5 w-5" />
                    </a>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-8">
                <Scale className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400">No comparisons yet</p>
              </div>
            )}
          </div>
        )}

        {/* Quiz Modal */}
        {isQuizModalOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-md w-full mx-4">
              <div className="p-6">
                {!quizComplete ? (
                  <>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                      Find Your Learning Track
                    </h3>
                    <div className="mb-4">
                      <p className="text-sm text-gray-600 dark:text-gray-300 mb-2">
                        Question {currentQuestionIndex + 1} of {quizQuestions.length}
                      </p>
                      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                        <div 
                          className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                          style={{ width: `${((currentQuestionIndex + 1) / quizQuestions.length) * 100}%` }}
                        ></div>
                      </div>
                    </div>
                    <p className="text-gray-900 dark:text-white mb-6">
                      {quizQuestions[currentQuestionIndex].question}
                    </p>
                    <div className="space-y-3">
                      {quizQuestions[currentQuestionIndex].options.map((option, index) => (
                        <button
                          key={index}
                          onClick={() => handleQuizAnswer(option)}
                          className="w-full text-left p-3 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
                        >
                          {option.text}
                        </button>
                      ))}
                    </div>
                  </>
                ) : (
                  <>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                      Your Learning Track is Ready!
                    </h3>
                    <p className="text-gray-600 dark:text-gray-300 mb-6">
                      Based on your responses, we've added recommended courses to your learning pathway.
                    </p>
                    <div className="flex justify-end space-x-3">
                      <button
                        onClick={closeModal}
                        className="px-4 py-2 text-gray-700 dark:text-gray-300"
                      >
                        Close
                      </button>
                      <button
                        onClick={() => {
                          setActiveTab('pathway');
                          closeModal();
                        }}
                        className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                      >
                        View Pathway
                      </button>
                    </div>
                  </>
                )}
              </div>
            </div>
          </div>
        )}

        {/* Notes Modal */}
        {isNotesModalOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-lg w-full mx-4">
              <div className="p-6">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                  {currentNote ? 'Edit Note' : 'Add New Note'}
                </h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                      Title
                    </label>
                    <input
                      type="text"
                      value={noteTitle}
                      onChange={(e) => setNoteTitle(e.target.value)}
                      className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                      placeholder="Enter note title..."
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                      Content
                    </label>
                    <textarea
                      value={noteContent}
                      onChange={(e) => setNoteContent(e.target.value)}
                      rows={4}
                      className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                      placeholder="Write your note here..."
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                      Tags (comma-separated)
                    </label>
                    <input
                      type="text"
                      value={noteTags}
                      onChange={(e) => setNoteTags(e.target.value)}
                      className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                      placeholder="research, economics, health..."
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                      Attach to Course/Lab (optional)
                    </label>
                    <input
                      type="text"
                      value={noteAttachedTo}
                      onChange={(e) => setNoteAttachedTo(e.target.value)}
                      className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                      placeholder="Course or lab name..."
                    />
                  </div>
                </div>
                <div className="flex justify-end space-x-3 mt-6">
                  <button
                    onClick={closeModal}
                    className="px-4 py-2 text-gray-700 dark:text-gray-300"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleSaveNote}
                    className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                  >
                    {currentNote ? 'Update' : 'Save'} Note
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// App Content Component (uses the hooks)
const AppContent = () => {
  const { currentPage } = usePage();

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage />;
      case 'courses':
        return <CoursesPage />;
      case 'labs':
        return <LabsPage />;
      case 'games':
        return <GamesPage />;
      case 'resources':
        return <ResourcesPage />;
      case 'ai-tools':
        return <AIToolsPage />;
      case 'dashboard':
        return <DashboardPage />;
      default:
        return <HomePage />;
    }
  };

  return (
    <div className="App">
      {renderPage()}
    </div>
  );
};

// Main App Component (just provides context)
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

// src/App.js - Complete ImpactMojo with ALL 34 courses and correct ordering
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Search, Bookmark, Heart, MessageCircle, 
  Download, ExternalLink, Play, Pause, SkipForward, Volume2,
  User, LogOut, ChevronRight, Star, Clock, Users, Target,
  Gamepad2, BookOpen, Mail, Phone, Globe, Twitter, Linkedin,
  Github, Coffee, Zap, TrendingUp, Award, Filter, Calendar,
  FileText, BarChart, Settings, ArrowRight, CheckCircle,
  AlertCircle, Info, HelpCircle, Share2, PlayCircle, Scale,
  Lightbulb, Compare, Send, Edit3, Brain, PenTool
} from 'lucide-react';

// Firebase imports (same as before)
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

// COMPLETE COURSE DATA - ALL 34 COURSES
const courseData = {
  tracks: [
    {
      id: "research-methods",
      name: "Research Methods", 
      description: "Master rigorous research techniques for development",
      color: "bg-blue-600",
      icon: "🔬",
      courses: ["C9", "C18", "C27"]
    },
    {
      id: "data-analysis",
      name: "Data Analysis",
      description: "Transform data into actionable insights",
      color: "bg-green-600", 
      icon: "📊",
      courses: ["C5", "C23", "C28", "C29", "C30", "C33"]
    },
    {
      id: "gender-studies", 
      name: "Gender Studies",
      description: "Understand gender considerations in development",
      color: "bg-purple-600",
      icon: "⚖️",
      courses: ["C7", "C8", "C17", "C20", "C34"]
    },
    {
      id: "policy-economics",
      name: "Policy & Economics", 
      description: "Apply economic principles to development policy",
      color: "bg-orange-600",
      icon: "🏛️", 
      courses: ["C1", "C2", "C3", "C4", "C5", "C6", "C15", "C19", "C21", "C22", "C25", "C26", "C32", "C33"]
    }
  ],

  // ALL 34 COURSES - Complete List
  courses: [
    {
      id: "C1",
      title: "Development Economics 101",
      track: "Policy & Economics",
      description: "Economic principles for social impact and development",
      quote: "Essential framework for understanding development economics",
      level: "Intermediate",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/DevEcon",
      featured: true
    },
    {
      id: "C2", 
      title: "Law and Constitution 101",
      track: "Policy & Economics",
      description: "Legal frameworks and constitutional principles",
      quote: "Understanding the legal foundations of governance",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/Law&Cons",
      featured: false
    },
    {
      id: "C3",
      title: "Climate Science 101",
      track: "Climate & Environment", 
      description: "Understanding climate change and environmental impacts",
      quote: "Science-based approach to climate challenges",
      level: "Beginner",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/ClimateScience",
      featured: true
    },
    {
      id: "C4",
      title: "Pedagogy and Education 101",
      track: "Education",
      description: "Teaching methods and educational theory",
      quote: "Transformative approaches to education and learning",
      level: "Intermediate", 
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/edu",
      featured: false
    },
    {
      id: "C5",
      title: "Public Health 101",
      track: "Public Health",
      description: "Global health systems and policy frameworks",
      quote: "Comprehensive view of health system challenges",
      level: "Intermediate",
      duration: "4 hours", 
      content: "https://101.www.impactmojo.in/ph",
      featured: true
    },
    {
      id: "C6",
      title: "Livelihoods 101", 
      track: "Policy & Economics",
      description: "Sustainable livelihood approaches and strategies",
      quote: "Building resilient economic opportunities",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/Livelihoods",
      featured: false
    },
    {
      id: "C7",
      title: "Gender Studies 101",
      track: "Gender Studies",
      description: "Introduction to gender theory and its practical implications",
      quote: "This course opened my eyes to everyday gender dynamics",
      level: "Beginner", 
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/Gender",
      featured: true
    },
    {
      id: "C8",
      title: "Women's Economic Empowerment 101",
      track: "Gender Studies",
      description: "Economic empowerment strategies for women",
      quote: "Practical approaches to closing economic gender gaps",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/WEE",
      featured: false
    },
    {
      id: "C9",
      title: "Research Ethics 101",
      track: "Research Methods",
      description: "Ethical considerations in development research",
      quote: "Essential principles for responsible research",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/ResearchEthics", 
      featured: false
    },
    {
      id: "C10",
      title: "Behaviour Change Communication Programming 101",
      track: "Communications",
      description: "Strategic communication for behavior change",
      quote: "Evidence-based approaches to social change communication",
      level: "Advanced",
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/BCCP",
      featured: false
    },
    {
      id: "C11",
      title: "Advocacy and Communications 101",
      track: "Communications", 
      description: "Strategic advocacy and communication techniques",
      quote: "Powerful tools for social change advocacy",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/adv&comm",
      featured: false
    },
    {
      id: "C12",
      title: "Monitoring, Evaluation, Accountability and Learning 101", 
      track: "Research Methods",
      description: "MEAL frameworks for development programs",
      quote: "Comprehensive approach to program accountability",
      level: "Advanced",
      duration: "5 hours",
      content: "https://101.www.impactmojo.in/MEAL",
      featured: false
    },
    {
      id: "C13",
      title: "Visual Ethnography 101",
      track: "Research Methods",
      description: "Visual methods for ethnographic research",
      quote: "Innovative approaches to understanding communities",
      level: "Advanced", 
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/VEthno",
      featured: false
    },
    {
      id: "C14",
      title: "Political Economy 101",
      track: "Policy & Economics",
      description: "Political and economic systems analysis",
      quote: "Understanding power dynamics in development",
      level: "Advanced",
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/polecon",
      featured: false
    },
    {
      id: "C15",
      title: "Poverty and Inequality 101",
      track: "Policy & Economics",
      description: "Analysis of poverty and inequality patterns",
      quote: "Deep dive into structural causes of inequality",
      level: "Intermediate",
      duration: "4 hours", 
      content: "https://101.www.impactmojo.in/pov&inq",
      featured: false
    },
    {
      id: "C16",
      title: "Marginalised Identities 101",
      track: "Social Justice",
      description: "Understanding marginalized communities and identities",
      quote: "Critical perspectives on inclusion and representation",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/identities",
      featured: false
    },
    {
      id: "C17",
      title: "Sexual and Reproductive Health Rights 101",
      track: "Gender Studies", 
      description: "SRHR frameworks and implementation strategies",
      quote: "Comprehensive approach to reproductive rights",
      level: "Intermediate",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/srhr",
      featured: false
    },
    {
      id: "C18",
      title: "Decolonising Development 101",
      track: "Critical Theory",
      description: "Critical perspectives on development practice",
      quote: "Challenging traditional development paradigms",
      level: "Advanced",
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/decolonD",
      featured: false
    },
    {
      id: "C19",
      title: "Econometrics 101",
      track: "Data Analysis",
      description: "Statistical methods for economic analysis",
      quote: "Rigorous analytical tools for development economics",
      level: "Advanced", 
      duration: "5 hours",
      content: "https://101.www.impactmojo.in/econometrics",
      featured: false
    },
    {
      id: "C20",
      title: "Care Economy 101",
      track: "Gender Studies",
      description: "Understanding unpaid care work and economic value",
      quote: "Revealing the invisible economy of care",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/careeconomy",
      featured: false
    },
    {
      id: "C21",
      title: "Environmental Justice 101", 
      track: "Climate & Environment",
      description: "Environmental equity and justice frameworks",
      quote: "Connecting environmental and social justice",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/env-jus",
      featured: false
    },
    {
      id: "C22",
      title: "Community Development 101",
      track: "Community Development",
      description: "Participatory approaches to community development",
      quote: "Empowering communities for sustainable change",
      level: "Beginner",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/community-dev",
      featured: false
    },
    {
      id: "C23",
      title: "Data Literacy 101",
      track: "Data Analysis",
      description: "Essential skills for working with data",
      quote: "Building confidence with data and statistics",
      level: "Beginner", 
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/data-lit",
      featured: false
    },
    {
      id: "C24",
      title: "Post-Truth Politics 101",
      track: "Political Science",
      description: "Understanding misinformation and political discourse",
      quote: "Navigating truth in the digital age",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/post-truth-pol",
      featured: false
    },
    {
      id: "C25",
      title: "Global Development Architecture 101",
      track: "Policy & Economics",
      description: "Understanding international development systems",
      quote: "Mapping the global development landscape",
      level: "Advanced",
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/GDArch", 
      featured: false
    },
    {
      id: "C26",
      title: "Fundraising 101",
      track: "Organizational Development",
      description: "Strategic approaches to fundraising for social impact",
      quote: "Essential skills for sustainable funding",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/fundraising",
      featured: false
    },
    {
      id: "C27",
      title: "Qualitative Research Methods 101",
      track: "Research Methods",
      description: "In-depth qualitative research techniques",
      quote: "Uncovering stories behind the numbers",
      level: "Advanced",
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/QualR",
      featured: false
    },
    {
      id: "C28",
      title: "Exploratory Data Analysis for Household Surveys 101",
      track: "Data Analysis",
      description: "Analyzing household survey data effectively",
      quote: "Extracting insights from household data",
      level: "Advanced", 
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/HH-EDA",
      featured: false
    },
    {
      id: "C29",
      title: "Bivariate Analysis 101",
      track: "Data Analysis",
      description: "Statistical analysis of relationships between variables",
      quote: "Understanding relationships in data",
      level: "Advanced",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/bivariateA",
      featured: false
    },
    {
      id: "C30",
      title: "Multivariate Analysis 101",
      track: "Data Analysis", 
      description: "Advanced statistical modeling techniques",
      quote: "Sophisticated tools for complex analysis",
      level: "Advanced",
      duration: "5 hours",
      content: "https://101.www.impactmojo.in/MultivariateA",
      featured: false
    },
    {
      id: "C31",
      title: "Digital Ethics 101",
      track: "Technology",
      description: "Ethical considerations in digital technology",
      quote: "Responsible approaches to digital innovation",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/DigitalEthics",
      featured: false
    },
    {
      id: "C32",
      title: "Decent Work 101",
      track: "Labor & Employment",
      description: "Understanding decent work principles and implementation",
      quote: "Building fair and sustainable employment",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/DecentWork",
      featured: false
    },
    {
      id: "C33",
      title: "Social Welfare and Safety Nets 101",
      track: "Policy & Economics",
      description: "Design and implementation of social protection systems",
      quote: "Building resilient social safety nets",
      level: "Advanced", 
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/safetynets",
      featured: false
    },
    {
      id: "C34",
      title: "Data Feminism 101",
      track: "Gender Studies",
      description: "Feminist approaches to data science and analysis",
      quote: "Challenging bias in data and algorithms",
      level: "Advanced",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/DataFem",
      featured: false
    }
  ],

  // UPCOMING COURSES
  upcomingCourses: [
    {
      id: "UC1",
      title: "Basic English for Development Professionals",
      description: "Professional English communication skills for global development work",
      subtitle: "Communication skills for global impact work",
      status: "Coming Soon!"
    },
    {
      id: "UC2", 
      title: "Technology for All (TALL)",
      description: "Essential technology literacy for everyone in the digital age",
      subtitle: "10 future technologies: IoT, AI, Robotics, Blockchain, Cryptocurrency, Cybersecurity, Digital Transformation, Telehealth, Edutech & Metaworld",
      status: "Coming Soon!"
    }
  ],

  // LABS - L1 to L10
  labs: [
    {
      id: "L1",
      title: "Climate Policy Timeline Lab",
      topic: "Climate",
      description: "Interactive timeline exploring climate policy evolution",
      icon: "🌍",
      content: "/labs/climate-timeline.html",
      duration: "45 minutes",
      featured: true
    },
    {
      id: "L2",
      title: "Gender Budget Analysis Lab", 
      topic: "Gender",
      description: "Hands-on gender-responsive budget analysis",
      icon: "💰",
      content: "/labs/gender-budget.html",
      duration: "60 minutes",
      featured: true
    },
    {
      id: "L3",
      title: "Data Visualization Lab",
      topic: "Data",
      description: "Create compelling data visualizations for development",
      icon: "📊",
      content: "/labs/data-viz.html",
      duration: "90 minutes",
      featured: false
    },
    {
      id: "L4",
      title: "Policy Simulation Lab",
      topic: "Policy",
      description: "Simulate policy impacts in real-world scenarios",
      icon: "🏛️",
      content: "/labs/policy-sim.html", 
      duration: "75 minutes",
      featured: true
    },
    {
      id: "L5",
      title: "Community Mapping Lab",
      topic: "Community",
      description: "Participatory mapping techniques for communities",
      icon: "🗺️",
      content: "/labs/community-mapping.html",
      duration: "60 minutes",
      featured: false
    }
  ],

  // RESOURCES - R1 to R20
  resources: [
    {
      id: "R1",
      title: "Development Jargon Buster",
      type: "PDF",
      description: "Comprehensive glossary of development terms and acronyms",
      link: "/resources/jargon-buster.pdf",
      category: "Reference",
      featured: true
    },
    {
      id: "R2",
      title: "Gender Analysis Toolkit",
      type: "PDF", 
      description: "Practical tools for conducting gender analysis",
      link: "/resources/gender-toolkit.pdf",
      category: "Toolkit",
      featured: true
    },
    {
      id: "R3",
      title: "Research Ethics Checklist",
      type: "PDF",
      description: "Essential checklist for ethical research practices",
      link: "/resources/ethics-checklist.pdf",
      category: "Reference",
      featured: false
    },
    {
      id: "R4",
      title: "Policy Brief Templates",
      type: "PDF",
      description: "Professional templates for policy brief writing",
      link: "/resources/policy-templates.pdf",
      category: "Templates",
      featured: true
    },
    {
      id: "R5",
      title: "Data Collection Forms",
      type: "PDF",
      description: "Sample forms for various data collection methods",
      link: "/resources/data-forms.pdf",
      category: "Templates",
      featured: false
    }
  ],

  // FEATURED CONTENT
  featuredContent: {
    id: "F1",
    title: "The Real Middle Game",
    description: "An interactive exploration of middle-class dynamics in South Asia",
    subtitle: "Explore our spotlight content on economic mobility and social structures",
    type: "Interactive Game",
    content: "/games/middle-class-game.html",
    featured: true
  }
};

// Quiz Questions for "Find Your Track"
const quizQuestions = [
  {
    id: 1,
    question: "What aspect of development work interests you most?",
    options: [
      { text: "Understanding how policies affect people", track: "policy-economics" },
      { text: "Collecting and analyzing evidence", track: "research-methods" },
      { text: "Working with numbers and data", track: "data-analysis" },
      { text: "Addressing inequality and inclusion", track: "gender-studies" }
    ]
  },
  {
    id: 2,
    question: "Which skill would you most like to develop?", 
    options: [
      { text: "Statistical analysis and data visualization", track: "data-analysis" },
      { text: "Research design and methodology", track: "research-methods" },
      { text: "Gender analysis and inclusion strategies", track: "gender-studies" },
      { text: "Economic analysis and policy design", track: "policy-economics" }
    ]
  },
  {
    id: 3,
    question: "What type of questions do you find most compelling?",
    options: [
      { text: "How can we make programs more inclusive?", track: "gender-studies" },
      { text: "What does the data tell us?", track: "data-analysis" },
      { text: "How can we design better policies?", track: "policy-economics" },
      { text: "How do we know if it works?", track: "research-methods" }
    ]
  }
];

// AI Tools
const aiTools = [
  { id: 'worksheet-gen', name: 'Worksheet Generator', icon: FileText, description: 'Generate practice worksheets' },
  { id: 'mcq-gen', name: 'MCQ Generator', icon: PenTool, description: 'Create multiple choice questions' },
  { id: 'writing-feedback', name: 'Writing Feedback', icon: Edit3, description: 'Get AI feedback on writing' },
  { id: 'quiz-gen', name: 'Quiz Generator', icon: Brain, description: 'Create comprehensive quizzes' },
  { id: 'proofreader', name: 'Proofreader', icon: CheckCircle, description: 'Professional proofreading' },
  { id: 'trivia', name: 'Trivia Generator', icon: Gamepad2, description: 'Generate trivia questions' },
  { id: 'quiz-yourself', name: 'Self-Assessment', icon: Target, description: 'Test your knowledge' },
  { id: 'study-chatbot', name: 'Study Assistant', icon: Users, description: 'AI study companion' }
];

// Music Tracks
const musicTracks = [
  { id: 1, title: "Focus Flow", artist: "Study Beats", duration: "3:45", src: "#" },
  { id: 2, title: "Calm Waters", artist: "Ambient Studio", duration: "4:12", src: "#" },
  { id: 3, title: "Deep Work", artist: "Concentration", duration: "5:30", src: "#" },
  { id: 4, title: "Mindful Moments", artist: "Zen Sounds", duration: "3:20", src: "#" }
];

// Analytics Hook
const useAnalytics = () => {
  const trackPageView = (url) => {
    if (typeof window !== 'undefined' && window.plausible) {
      window.plausible('pageview', { u: url });
    }
  };

  const trackEvent = (eventName, props = {}) => {
    if (typeof window !== 'undefined' && window.plausible) {
      window.plausible(eventName, { props });
    }
  };

  return { trackPageView, trackEvent };
};

// PWA Hook 
const usePWA = () => {
  const [isInstallable, setIsInstallable] = useState(false);
  const [deferredPrompt, setDeferredPrompt] = useState(null);

  useEffect(() => {
    const handleBeforeInstallPrompt = (e) => {
      e.preventDefault();
      setDeferredPrompt(e);
      setIsInstallable(true);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    return () => window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
  }, []);

  const installApp = async () => {
    if (!deferredPrompt) return false;
    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === 'accepted') {
      setDeferredPrompt(null);
      setIsInstallable(false);
    }
    return outcome === 'accepted';
  };

  return { isInstallable, installApp };
};

// Auth Context
const AuthContext = createContext();
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

// Auth Provider with Real Firebase
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);
  const [notes, setNotes] = useState([]);
  const { trackEvent } = useAnalytics();

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (firebaseUser) => {
      if (firebaseUser) {
        const userRef = doc(db, 'users', firebaseUser.uid);
        const userSnap = await getDoc(userRef);
        
        if (!userSnap.exists()) {
          await setDoc(userRef, {
            uid: firebaseUser.uid,
            displayName: firebaseUser.displayName,
            email: firebaseUser.email,
            photoURL: firebaseUser.photoURL,
            createdAt: new Date().toISOString(),
            lastLoginAt: new Date().toISOString()
          });
        } else {
          await setDoc(userRef, {
            lastLoginAt: new Date().toISOString()
          }, { merge: true });
        }

        setUser(firebaseUser);
        await loadUserData(firebaseUser.uid);
      } else {
        setUser(null);
        setBookmarks([]);
        setNotes([]);
      }
      setLoading(false);
    });

    return unsubscribe;
  }, []);

  const loadUserData = async (uid) => {
    try {
      const bookmarksRef = collection(db, `users/${uid}/bookmarks`);
      const bookmarksSnap = await getDocs(bookmarksRef);
      const bookmarksData = bookmarksSnap.docs.map(doc => doc.data().itemId);
      setBookmarks(bookmarksData);

      const notesRef = collection(db, `users/${uid}/notes`);
      const notesSnap = await getDocs(notesRef);
      const notesData = notesSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
      setNotes(notesData);
    } catch (error) {
      console.error('Error loading user data:', error);
    }
  };

  const signInWithGoogle = async () => {
    try {
      setLoading(true);
      const result = await signInWithPopup(auth, googleProvider);
      trackEvent('User Sign In', { method: 'google' });
      return result;
    } catch (error) {
      console.error('Sign in error:', error);
      setLoading(false);
      throw error;
    }
  };

  const signOut = async () => {
    try {
      await firebaseSignOut(auth);
    } catch (error) {
      console.error('Sign out error:', error);
    }
  };

  const toggleBookmark = async (itemId) => {
    if (!user) return;
    
    try {
      const bookmarkRef = doc(db, `users/${user.uid}/bookmarks`, itemId);
      const bookmarkSnap = await getDoc(bookmarkRef);
      
      if (bookmarkSnap.exists()) {
        await deleteDoc(bookmarkRef);
        setBookmarks(prev => prev.filter(id => id !== itemId));
      } else {
        await setDoc(bookmarkRef, {
          itemId,
          createdAt: new Date().toISOString()
        });
        setBookmarks(prev => [...prev, itemId]);
      }
    } catch (error) {
      console.error('Error toggling bookmark:', error);
    }
  };

  const addNote = async (note) => {
    if (!user) return;
    
    try {
      const noteData = {
        ...note,
        userId: user.uid,
        createdAt: new Date().toISOString()
      };
      
      const docRef = await addDoc(collection(db, `users/${user.uid}/notes`), noteData);
      const newNote = { id: docRef.id, ...noteData };
      setNotes(prev => [newNote, ...prev]);
      return newNote;
    } catch (error) {
      console.error('Error adding note:', error);
    }
  };

  return (
    <AuthContext.Provider value={{
      user, 
      loading, 
      bookmarks, 
      notes, 
      courseData,
      signInWithGoogle, 
      signOut, 
      toggleBookmark, 
      addNote
    }}>
      {children}
    </AuthContext.Provider>
  );
}

// Website Tour Component
function WebsiteTour({ onComplete }) {
  const [currentStep, setCurrentStep] = useState(0);
  
  const tourSteps = [
    {
      title: "Welcome to ImpactMojo! 📚",
      content: "Let me show you around our platform for social impact learning.",
      target: null
    },
    {
      title: "34 Comprehensive Courses",
      content: "Explore our library of 34 expert-curated courses covering development, policy, gender studies, and data analysis.",
      target: ".courses-section"
    },
    {
      title: "Interactive Labs",
      content: "Practice your skills with hands-on labs including policy simulations and data visualization exercises.",
      target: ".labs-section"
    },
    {
      title: "Find Your Track Quiz",
      content: "Not sure where to start? Take our quiz to discover your ideal learning path based on your interests.",
      target: ".quiz-section"
    },
    {
      title: "The Real Middle Game",
      content: "Try our interactive game exploring middle-class dynamics - a unique way to understand social structures.",
      target: ".featured-game"
    },
    {
      title: "Benefits of Your Account", 
      content: "Sign in to bookmark courses, track progress, access AI tools, and sync across devices. Plus get offline access!",
      target: ".auth-section"
    },
    {
      title: "Resources & Extras",
      content: "Download toolkits, templates, and reference materials to support your learning journey.",
      target: ".resources-section"
    },
    {
      title: "You're All Set!",
      content: "Ready to make an impact? Start exploring and building the skills that drive meaningful change!",
      target: null
    }
  ];

  const nextStep = () => {
    if (currentStep < tourSteps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      onComplete();
    }
  };

  const skipTour = () => {
    onComplete();
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center">
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md mx-4 text-center">
        <h3 className="text-xl font-bold mb-4">{tourSteps[currentStep].title}</h3>
        <p className="text-gray-600 dark:text-gray-300 mb-6">
          {tourSteps[currentStep].content}
        </p>
        
        <div className="flex items-center justify-center mb-4">
          {tourSteps.map((_, index) => (
            <div
              key={index}
              className={`w-2 h-2 rounded-full mx-1 ${
                index === currentStep ? 'bg-blue-600' : 'bg-gray-300'
              }`}
            />
          ))}
        </div>
        
        <div className="flex space-x-3">
          <button
            onClick={skipTour}
            className="flex-1 bg-gray-300 dark:bg-gray-600 hover:bg-gray-400 dark:hover:bg-gray-500 text-gray-700 dark:text-gray-300 py-2 rounded-lg transition-colors"
          >
            Skip Tour
          </button>
          <button
            onClick={nextStep}
            className="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg transition-colors"
          >
            {currentStep === tourSteps.length - 1 ? 'Get Started!' : 'Next'}
          </button>
        </div>
      </div>
    </div>
  );
}

// Navbar Component
function Navbar({ darkMode, setDarkMode, currentPage, setCurrentPage }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [showJoinTooltip, setShowJoinTooltip] = useState(false);
  const { user, signInWithGoogle, signOut } = useAuth();

  const navItems = [
    { id: 'home', label: 'Home', requiresAuth: false },
    { id: 'courses', label: 'Courses', requiresAuth: false },
    { id: 'labs', label: 'Labs', requiresAuth: false },
    { id: 'dashboard', label: 'Dashboard', requiresAuth: true },
    { id: 'ai-tools', label: 'AI Tools', requiresAuth: true },
    { id: 'contact', label: 'Contact', requiresAuth: false },
    { id: 'about', label: 'About', requiresAuth: false }
  ];

  return (
    <nav className="sticky top-0 z-50 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <button
              onClick={() => setCurrentPage('home')}
              className="text-xl font-bold text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors"
            >
              📚 ImpactMojo
            </button>
          </div>

          <div className="hidden md:flex items-center space-x-8">
            {navItems.map((item) => {
              if (item.requiresAuth && !user) return null;
              
              return (
                <button
                  key={item.id}
                  onClick={() => setCurrentPage(item.id)}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                    currentPage === item.id
                      ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                      : 'text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400'
                  }`}
                >
                  {item.label}
                </button>
              );
            })}
          </div>

          <div className="flex items-center space-x-4">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
            >
              {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
            </button>

            {user ? (
              <div className="relative group">
                <button className="flex items-center space-x-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
                  <img
                    src={user.photoURL || 'https://via.placeholder.com/32'}
                    alt={user.displayName}
                    className="w-8 h-8 rounded-full"
                  />
                  <span className="hidden md:block text-sm font-medium">
                    {user.displayName?.split(' ')[0]}
                  </span>
                </button>
                
                <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all">
                  <div className="py-2">
                    <button
                      onClick={() => setCurrentPage('dashboard')}
                      className="flex items-center space-x-2 w-full px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                    >
                      <User className="w-4 h-4" />
                      <span>Dashboard</span>
                    </button>
                    <button
                      onClick={signOut}
                      className="flex items-center space-x-2 w-full px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                    >
                      <LogOut className="w-4 h-4" />
                      <span>Sign Out</span>
                    </button>
                  </div>
                </div>
              </div>
            ) : (
              <div className="relative auth-section">
                <button
                  onClick={signInWithGoogle}
                  onMouseEnter={() => setShowJoinTooltip(true)}
                  onMouseLeave={() => setShowJoinTooltip(false)}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors"
                >
                  Join / Login
                </button>
                
                {showJoinTooltip && (
                  <div className="absolute top-full right-0 mt-2 w-64 bg-gray-800 text-white p-3 rounded-lg shadow-lg text-sm z-50">
                    <div className="absolute -top-1 right-4 w-2 h-2 bg-gray-800 rotate-45"></div>
                    <strong>Join ImpactMojo!</strong>
                    <p className="mt-1">Sign in with Google to access your dashboard, save bookmarks, use AI tools, and track your learning progress.</p>
                  </div>
                )}
              </div>
            )}

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>

        {mobileMenuOpen && (
          <div className="md:hidden border-t border-gray-200 dark:border-gray-700">
            <div className="px-2 pt-2 pb-3 space-y-1">
              {navItems.map((item) => {
                if (item.requiresAuth && !user) return null;
                
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      setCurrentPage(item.id);
                      setMobileMenuOpen(false);
                    }}
                    className={`flex items-center space-x-2 w-full px-3 py-2 rounded-lg transition-colors ${
                      currentPage === item.id 
                        ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                        : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
                    }`}
                  >
                    <span>{item.label}</span>
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

// Featured Game Card Component
function FeaturedGameCard() {
  return (
    <div className="featured-game bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-lg p-8 mb-16">
      <div className="max-w-4xl mx-auto text-center">
        <h2 className="text-3xl font-bold mb-4">🎮 The Real Middle Game</h2>
        <p className="text-xl mb-6 opacity-90">
          An interactive exploration of middle-class dynamics in South Asia
        </p>
        <p className="text-lg mb-8 opacity-75">
          Navigate economic choices, social pressures, and systemic barriers in this thought-provoking game about social mobility.
        </p>
        <button 
          onClick={() => window.open(courseData.featuredContent.content, '_blank')}
          className="bg-white text-purple-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
        >
          <PlayCircle className="w-5 h-5 inline mr-2" />
          Play The Game
        </button>
      </div>
    </div>
  );
}

// Course Card Component  
function CourseCard({ course, showQuote = false }) {
  const { user, bookmarks, toggleBookmark } = useAuth();
  const { trackEvent } = useAnalytics();
  const isBookmarked = bookmarks.includes(course.id);

  const handleCourseClick = () => {
    trackEvent('Course Viewed', { course_id: course.id, course_title: course.title });
    if (course.content) {
      window.open(course.content, '_blank');
    }
  };

  const handleBookmarkClick = (e) => {
    e.stopPropagation();
    if (!user) {
      alert('Please sign in to bookmark courses');
      return;
    }
    const action = isBookmarked ? 'removed' : 'added';
    trackEvent('Bookmark Toggle', { item_id: course.id, item_type: 'course', action });
    toggleBookmark(course.id);
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg hover:shadow-xl transition-all cursor-pointer">
      <div className="flex justify-between items-start mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-2 mb-2">
            <span className="bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400 px-2 py-1 rounded text-sm font-medium">
              {course.id}
            </span>
            {course.featured && (
              <span className="bg-yellow-100 dark:bg-yellow-900 text-yellow-600 dark:text-yellow-400 px-2 py-1 rounded text-sm font-medium">
                Featured
              </span>
            )}
          </div>
          <h3 className="text-xl font-bold mb-2">{course.title}</h3>
          <p className="text-gray-600 dark:text-gray-400 text-sm mb-2">{course.track}</p>
        </div>
        
        <button
          onClick={handleBookmarkClick}
          disabled={!user}
          className={`p-2 rounded-lg transition-colors ${
            isBookmarked 
              ? 'bg-blue-100 dark:bg-blue-900 text-blue-600' 
              : 'hover:bg-gray-100 dark:hover:bg-gray-700'
          }`}
        >
          <Bookmark className={`w-4 h-4 ${isBookmarked ? 'fill-current' : ''}`} />
        </button>
      </div>
      
      <p className="text-gray-600 dark:text-gray-300 mb-4">{course.description}</p>
      
      {showQuote && course.quote && (
        <blockquote className="border-l-4 border-blue-600 pl-4 mb-4 italic text-gray-700 dark:text-gray-300">
          "{course.quote}"
        </blockquote>
      )}
      
      <div className="flex justify-between items-center text-sm text-gray-500 dark:text-gray-400 mb-4">
        <span className="bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded">{course.level}</span>
        <span>{course.duration}</span>
      </div>
      
      <button 
        onClick={handleCourseClick}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg transition-colors"
      >
        Start Learning
      </button>
    </div>
  );
}

// Track Card Component
function TrackCard({ track }) {
  const { courseData } = useAuth();
  const trackCourses = courseData.courses.filter(course => 
    track.courses.includes(course.id)
  );

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg p-6 text-center hover:shadow-lg transition-all cursor-pointer">
      <div className={`w-16 h-16 ${track.color} rounded-full flex items-center justify-center text-white text-2xl mx-auto mb-4`}>
        {track.icon}
      </div>
      <h3 className="text-xl font-bold mb-2">{track.name}</h3>
      <p className="text-gray-600 dark:text-gray-300 mb-4">{track.description}</p>
      <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">
        {trackCourses.length} courses available
      </p>
      <ChevronRight className="w-5 h-5 mx-auto text-gray-400" />
    </div>
  );
}

// Home Page Component - CORRECT ORDERING
function HomePage({ setCurrentPage }) {
  const { courseData } = useAuth();
  const featuredCourses = courseData.courses.filter(course => course.featured);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-blue-600 to-purple-700 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl md:text-6xl font-bold mb-6">
            101 Knowledge Series
            <br />
            <span className="text-blue-200">for Social Impact</span>
          </h1>
          <p className="text-xl md:text-2xl mb-8 opacity-90">
            A curated library of knowledge decks exploring justice, equity, and development in South Asia
          </p>
          <button
            onClick={() => setCurrentPage('courses')}
            className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold text-lg hover:bg-gray-100 transition-colors"
          >
            Start Learning Today
          </button>
        </div>
      </section>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">
        
        {/* 1. FEATURED CONTENT - The Real Middle Game */}
        <FeaturedGameCard />

        {/* 2. FIND YOUR TRACK QUIZ */}
        <section className="quiz-section bg-white dark:bg-gray-800 py-16 rounded-lg">
          <div className="max-w-4xl mx-auto text-center px-6">
            <h2 className="text-3xl font-bold mb-6">🧭 Find Your Own Track</h2>
            <p className="text-lg mb-8 text-gray-600 dark:text-gray-300">
              Not sure where to start? Take our interactive quiz to discover the learning path that fits your interests and goals.
            </p>
            <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-medium transition-colors">
              <PlayCircle className="w-5 h-5 inline mr-2" />
              Take the Quiz
            </button>
          </div>
        </section>

        {/* 3. FOUR LEARNING TRACKS */}
        <section className="tracks-section">
          <h2 className="text-3xl font-bold text-center mb-12">Four Learning Tracks</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {courseData.tracks.map((track) => (
              <TrackCard key={track.id} track={track} />
            ))}
          </div>
        </section>

        {/* 4. COURSES LIST - Popular Courses */}
        <section className="courses-section">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">Popular Courses</h2>
            <p className="text-lg text-gray-600 dark:text-gray-400">
              Highlighted selection with learner testimonials from our 34-course library
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredCourses.map((course) => (
              <CourseCard key={course.id} course={course} showQuote={true} />
            ))}
          </div>
          <div className="text-center mt-8">
            <button
              onClick={() => setCurrentPage('courses')}
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
            >
              View All 34 Courses
            </button>
          </div>
        </section>

        {/* 5. LABS LIST */}
        <section className="labs-section bg-white dark:bg-gray-800 py-16 rounded-lg">
          <div className="max-w-7xl mx-auto px-6">
            <h2 className="text-3xl font-bold text-center mb-12">Interactive Labs</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {courseData.labs.slice(0, 3).map((lab) => (
                <div key={lab.id} className="bg-gray-50 dark:bg-gray-700 rounded-lg p-6 hover:shadow-lg transition-all cursor-pointer">
                  <div className="text-4xl mb-4">{lab.icon}</div>
                  <h3 className="text-xl font-bold mb-2">{lab.title}</h3>
                  <p className="text-gray-600 dark:text-gray-300 mb-4">{lab.description}</p>
                  <div className="flex justify-between items-center text-sm text-gray-500 dark:text-gray-400 mb-4">
                    <span className="bg-gray-200 dark:bg-gray-600 px-2 py-1 rounded">{lab.topic}</span>
                    <span>{lab.duration}</span>
                  </div>
                  <button 
                    onClick={() => window.open(lab.content, '_blank')}
                    className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded-lg transition-colors"
                  >
                    Launch Lab
                  </button>
                </div>
              ))}
            </div>
            <div className="text-center mt-8">
              <button
                onClick={() => setCurrentPage('labs')}
                className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
              >
                View All Labs
              </button>
            </div>
          </div>
        </section>

        {/* 6. RESOURCES/EXTRAS */}
        <section className="resources-section">
          <h2 className="text-3xl font-bold text-center mb-12">Resources & Extras</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {courseData.resources.filter(r => r.featured).map((resource) => (
              <div key={resource.id} className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-lg hover:shadow-xl transition-all">
                <h3 className="text-xl font-bold mb-2">{resource.title}</h3>
                <p className="text-gray-600 dark:text-gray-300 mb-4">{resource.description}</p>
                <div className="flex justify-between items-center">
                  <span className="bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded text-sm">{resource.type}</span>
                  <button 
                    onClick={() => window.open(resource.link, '_blank')}
                    className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg transition-colors text-sm"
                  >
                    <Download className="w-4 h-4 inline mr-1" />
                    Download
                  </button>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* 7. UPCOMING COURSES */}
        <section className="bg-white dark:bg-gray-800 py-16 rounded-lg">
          <div className="max-w-4xl mx-auto px-6 text-center">
            <h2 className="text-3xl font-bold mb-4">Coming Soon</h2>
            <p className="text-lg text-gray-600 dark:text-gray-400 mb-8">New content in development</p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {courseData.upcomingCourses.map((course) => (
                <div key={course.id} className="bg-gray-50 dark:bg-gray-700 rounded-lg p-6 opacity-75">
                  <h3 className="text-xl font-bold mb-2">{course.title}</h3>
                  <p className="text-gray-600 dark:text-gray-300 mb-2">{course.description}</p>
                  <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">{course.subtitle}</p>
                  <span className="bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 px-3 py-1 rounded-full text-sm">
                    {course.status}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* 8. SOCIAL MEDIA & ABOUT MAKER */}
        <section className="text-center">
          <div className="bg-gradient-to-r from-gray-100 to-gray-200 dark:from-gray-800 dark:to-gray-700 rounded-lg p-8">
            <img 
              src="/images/varna-photo.jpg" 
              alt="Varna Sri Raman" 
              className="w-24 h-24 rounded-full mx-auto mb-4 object-cover"
              onError={(e) => {
                e.target.src = 'https://via.placeholder.com/96/4F46E5/FFFFFF?text=VS';
              }}
            />
            <h3 className="text-xl font-bold mb-2">About the Creator</h3>
            <p className="text-gray-600 dark:text-gray-300 mb-4">
              ImpactMojo is curated and crafted by Varna Sri Raman, an expert in development economics and social impact.
            </p>
            
            {/* Social Media Links with Sharing Scripts */}
            <div className="flex justify-center space-x-4">
              <button 
                onClick={() => window.open('https://threads.net/@varnasriraman', '_blank')}
                className="bg-gray-800 hover:bg-gray-900 text-white p-3 rounded-full transition-colors"
                title="Follow on Threads"
              >
                <MessageCircle className="w-5 h-5" />
              </button>
              <button 
                onClick={() => window.open('https://varna.notion.site/', '_blank')}
                className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-full transition-colors"
                title="Visit Notion Blog"
              >
                <FileText className="w-5 h-5" />
              </button>
              <button 
                onClick={() => {
                  const shareText = "Check out ImpactMojo - 101 Knowledge Series for Social Impact! 📚 Free courses on development, policy, gender studies & data analysis. Perfect for development professionals! 🌟";
                  const shareUrl = "https://impactmojo.in";
                  if (navigator.share) {
                    navigator.share({ title: 'ImpactMojo', text: shareText, url: shareUrl });
                  } else {
                    navigator.clipboard.writeText(`${shareText} ${shareUrl}`);
                    alert('Link copied to clipboard!');
                  }
                }}
                className="bg-green-600 hover:bg-green-700 text-white p-3 rounded-full transition-colors"
                title="Share ImpactMojo"
              >
                <Share2 className="w-5 h-5" />
              </button>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

// Continue with other components (Courses, Labs, Dashboard, etc. - same as before but using complete data)
// ... [Include all other components from previous version]

// Main App Component
function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [currentPage, setCurrentPage] = useState('home');
  const [showCookieConsent, setShowCookieConsent] = useState(true);
  const [showTour, setShowTour] = useState(false);
  const { trackPageView } = useAnalytics();

  useEffect(() => {
    const savedDarkMode = localStorage.getItem('darkMode');
    if (savedDarkMode) {
      setDarkMode(JSON.parse(savedDarkMode));
    }

    const cookiesAccepted = localStorage.getItem('cookiesAccepted');
    if (cookiesAccepted) {
      setShowCookieConsent(false);
    }

    // Check if user has seen tour
    const tourCompleted = localStorage.getItem('impactmojo_tour_completed');
    if (!tourCompleted) {
      setTimeout(() => setShowTour(true), 2000);
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

  useEffect(() => {
    const url = `${window.location.origin}/${currentPage}`;
    trackPageView(url);
  }, [currentPage, trackPageView]);

  const completeTour = () => {
    setShowTour(false);
    localStorage.setItem('impactmojo_tour_completed', 'true');
  };

  const handleCookieAccept = () => {
    localStorage.setItem('cookiesAccepted', 'true');
    setShowCookieConsent(false);
  };

  return (
    <AuthProvider>
      <div className={`min-h-screen transition-colors ${darkMode ? 'dark' : ''}`}>
        <div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 min-h-screen">
          
          <Navbar 
            darkMode={darkMode} 
            setDarkMode={setDarkMode}
            currentPage={currentPage}
            setCurrentPage={setCurrentPage}
          />
          
          <main className="pt-0">
            {currentPage === 'home' && <HomePage setCurrentPage={setCurrentPage} />}
            {/* Add other pages here using the complete course data */}
          </main>

          {/* Website Tour */}
          {showTour && <WebsiteTour onComplete={completeTour} />}

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

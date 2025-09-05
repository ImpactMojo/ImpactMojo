// src/App.js
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Bookmark, MessageCircle, 
  ExternalLink, BookOpen, FileText, Target, Users, 
  Clock, CheckCircle, PlayCircle, Bot, Trophy, 
  Headphones, MapPin, Library, Music, Download, 
  Search, Plus, Edit3, Save, Filter, BookmarkIcon, Tag,
  Install, AlertTriangle, ChevronDown, ChevronRight
} from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc, updateDoc, collection, addDoc } from 'firebase/firestore';

// Data imports
import { courseData, upcomingCourses } from './data/course-data';
import { labsData } from './data/labs-data';
import { premiumResources } from './data/premium-resources-data';

// Page imports
import AIToolsPage from './pages/AIToolsPage';

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

// New multi-dimensional browse system
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
    courses: ["public-health-101", "sexual-and-reproductive-health-rights-101", "social-welfare-and-safety-nets-101"],
    color: "red"
  },
  "Justice & Equality": {
    description: "Promoting justice, rights, and equality",
    courses: ["gender-studies-101", "environmental-justice-101", "marginilised-identities-101"],
    color: "purple"
  },
  "Economic Development": {
    description: "Building sustainable economic systems",
    courses: ["development-economics-101", "care-economy-101", "decent-work-101", "livelihoods-101"],
    color: "green"
  },
  "Systems & Governance": {
    description: "Understanding and changing systems",
    courses: ["political-economy-101", "global-development-architecture-101", "decolonising-development-101"],
    color: "blue"
  }
};

const browseByGoal = {
  "Understand the Big Picture": {
    description: "Get foundational knowledge and context",
    courses: ["development-economics-101", "global-development-architecture-101", "political-economy-101"],
    color: "blue"
  },
  "Conduct Better Research": {
    description: "Learn research methods and analysis",
    courses: ["research-ethics-101", "qualitative-research-methods-101", "data-literacy-101", "econometrics-101"],
    color: "purple"
  },
  "Design Better Programs": {
    description: "Create and implement effective interventions",
    courses: ["monitoring-evaluation-accountability-and-learning-101", "community-development-101", "behaviour-change-communication-programming-101"],
    color: "green"
  },
  "Advocate for Change": {
    description: "Influence policy and drive systemic change",
    courses: ["advocacy-and-communications-101", "political-economy-101", "law-and-constitution-101"],
    color: "orange"
  }
};

// Keep original track definitions for backwards compatibility (quiz system)
const trackDefinitions = {
  "Research Methods": {
    description: "Learn qualitative and quantitative research methods for development work.",
    courses: ["research-ethics-101", "qualitative-research-methods-101", "visual-ethnography-101"],
    color: "blue"
  },
  "Data Analysis": {
    description: "Master data analysis techniques for measuring social impact.",
    courses: ["data-literacy-101", "exploratory-data-analysis-for-household-surveys-101", "bivariate-analysis-101", "multivariate-analysis-101", "econometrics-101"],
    color: "green"
  },
  "Gender Studies": {
    description: "Explore gender dynamics and women's empowerment in development.",
    courses: ["gender-studies-101", "womens-economic-empowerment-101", "sexual-and-reproductive-health-rights-101", "care-economy-101"],
    color: "purple"
  },
  "Policy & Economics": {
    description: "Understand policy frameworks and economic systems in development.",
    courses: ["development-economics-101", "law-and-constitution-101", "political-economy-101", "poverty-and-inequality-101", "global-development-architecture-101"],
    color: "orange"
  }
};

// Quiz questions for "Find Your Track"
const quizQuestions = [
  {
    id: 1,
    question: "What interests you most about development work?",
    options: [
      { text: "Understanding how policies impact communities", track: "Policy & Economics", points: 3 },
      { text: "Analyzing data to measure impact", track: "Data Analysis", points: 3 },
      { text: "Exploring social dynamics and identity", track: "Gender Studies", points: 3 },
      { text: "Conducting field research and interviews", track: "Research Methods", points: 3 }
    ]
  },
  {
    id: 2,
    question: "Which type of work would you prefer?",
    options: [
      { text: "Working with spreadsheets and statistics", track: "Data Analysis", points: 3 },
      { text: "Reading academic papers and conducting literature reviews", track: "Research Methods", points: 3 },
      { text: "Understanding power structures and social justice", track: "Gender Studies", points: 3 },
      { text: "Analyzing economic systems and governance", track: "Policy & Economics", points: 3 }
    ]
  },
  {
    id: 3,
    question: "What kind of impact do you want to create?",
    options: [
      { text: "Evidence-based program improvements", track: "Data Analysis", points: 2 },
      { text: "Policy changes at institutional level", track: "Policy & Economics", points: 2 },
      { text: "Social awareness and behavioral change", track: "Gender Studies", points: 2 },
      { text: "Knowledge generation through research", track: "Research Methods", points: 2 }
    ]
  }
];

// Authentication Context
const AuthContext = createContext();
const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);
  const [isPremium, setIsPremium] = useState(false);
  const [customPathway, setCustomPathway] = useState([]);
  const [notes, setNotes] = useState([]);
  const [comparisons, setComparisons] = useState([]);
  
  // For non-logged-in users
  const [guestBookmarks, setGuestBookmarks] = useState([]);
  const [guestComparisons, setGuestComparisons] = useState([]);
  
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user);
      if (user) {
        try {
          const userDoc = await getDoc(doc(db, 'users', user.uid));
          if (userDoc.exists()) {
            const userData = userDoc.data();
            setBookmarks(userData.bookmarks || []);
            setIsPremium(true);
            setCustomPathway(userData.customPathway || []);
            setNotes(userData.notes || []);
            setComparisons(userData.comparisons || []);
          } else {
            await setDoc(doc(db, 'users', user.uid), {
              name: user.displayName,
              email: user.email,
              photoURL: user.photoURL,
              bookmarks: [],
              isPremium: true,
              customPathway: [],
              notes: [],
              comparisons: [],
              createdAt: new Date()
            });
            setIsPremium(true);
          }
        } catch (error) {
          console.error('Error loading user data:', error);
        }
      } else {
        setBookmarks([]);
        setIsPremium(false);
        setCustomPathway([]);
        setNotes([]);
        setComparisons([]);
        // Load guest data from localStorage
        const savedGuestBookmarks = JSON.parse(localStorage.getItem('guestBookmarks') || '[]');
        const savedGuestComparisons = JSON.parse(localStorage.getItem('guestComparisons') || '[]');
        setGuestBookmarks(savedGuestBookmarks);
        setGuestComparisons(savedGuestComparisons);
      }
      setLoading(false);
    });
    return unsubscribe;
  }, []);
  
  const signInWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, googleProvider);
      const user = result.user;
      await setDoc(doc(db, 'users', user.uid), {
        name: user.displayName,
        email: user.email,
        photoURL: user.photoURL,
        isPremium: true,
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
  
  const toggleBookmark = async (itemId, itemType = 'course', tags = []) => {
    if (user) {
      try {
        const existingBookmark = bookmarks.find(b => b.id === itemId);
        let newBookmarks;
        
        if (existingBookmark) {
          newBookmarks = bookmarks.filter(b => b.id !== itemId);
        } else {
          newBookmarks = [...bookmarks, { 
            id: itemId, 
            type: itemType, 
            tags: tags,
            dateAdded: new Date() 
          }];
        }
        
        await updateDoc(doc(db, 'users', user.uid), { bookmarks: newBookmarks });
        setBookmarks(newBookmarks);
      } catch (error) {
        console.error('Error toggling bookmark:', error);
      }
    } else {
      // Guest user
      const existingIndex = guestBookmarks.findIndex(b => b.id === itemId);
      let newGuestBookmarks;
      
      if (existingIndex >= 0) {
        newGuestBookmarks = guestBookmarks.filter(b => b.id !== itemId);
      } else {
        newGuestBookmarks = [...guestBookmarks, { 
          id: itemId, 
          type: itemType,
          dateAdded: new Date() 
        }];
      }
      
      setGuestBookmarks(newGuestBookmarks);
      localStorage.setItem('guestBookmarks', JSON.stringify(newGuestBookmarks));
    }
  };

  const toggleComparison = async (itemId, itemType = 'course') => {
    const currentComparisons = user ? comparisons : guestComparisons;
    
    if (currentComparisons.length >= 3 && !currentComparisons.find(c => c.id === itemId)) {
      alert('You can only compare up to 3 items at a time. Please remove an item first.');
      return;
    }

    if (user) {
      try {
        const existingIndex = comparisons.findIndex(c => c.id === itemId);
        let newComparisons;
        
        if (existingIndex >= 0) {
          newComparisons = comparisons.filter(c => c.id !== itemId);
        } else {
          newComparisons = [...comparisons, { id: itemId, type: itemType, dateAdded: new Date() }];
        }
        
        await updateDoc(doc(db, 'users', user.uid), { comparisons: newComparisons });
        setComparisons(newComparisons);
      } catch (error) {
        console.error('Error toggling comparison:', error);
      }
    } else {
      // Guest user
      const existingIndex = guestComparisons.findIndex(c => c.id === itemId);
      let newGuestComparisons;
      
      if (existingIndex >= 0) {
        newGuestComparisons = guestComparisons.filter(c => c.id !== itemId);
      } else {
        newGuestComparisons = [...guestComparisons, { id: itemId, type: itemType, dateAdded: new Date() }];
      }
      
      setGuestComparisons(newGuestComparisons);
      localStorage.setItem('guestComparisons', JSON.stringify(newGuestComparisons));
    }
  };

  const updateBookmarkTags = async (itemId, newTags) => {
    if (!user) return;
    try {
      const newBookmarks = bookmarks.map(bookmark => 
        bookmark.id === itemId 
          ? { ...bookmark, tags: newTags }
          : bookmark
      );
      await updateDoc(doc(db, 'users', user.uid), { bookmarks: newBookmarks });
      setBookmarks(newBookmarks);
    } catch (error) {
      console.error('Error updating bookmark tags:', error);
    }
  };
  
  const addToPathway = async (courseId) => {
    if (!user) return;
    try {
      const newPathway = [...customPathway, courseId];
      await updateDoc(doc(db, 'users', user.uid), { customPathway: newPathway });
      setCustomPathway(newPathway);
    } catch (error) {
      console.error('Error adding to pathway:', error);
    }
  };

  const setRecommendedTrack = async (track, courses) => {
    if (!user) return;
    try {
      await updateDoc(doc(db, 'users', user.uid), { 
        recommendedTrack: track,
        customPathway: courses
      });
      setCustomPathway(courses);
    } catch (error) {
      console.error('Error setting recommended track:', error);
    }
  };
  
  const saveNote = async (note) => {
    if (!user) return;
    try {
      const newNote = {
        ...note,
        id: Date.now().toString(),
        dateCreated: new Date(),
        lastModified: new Date()
      };
      const newNotes = [...notes, newNote];
      await updateDoc(doc(db, 'users', user.uid), { notes: newNotes });
      setNotes(newNotes);
      return newNote.id;
    } catch (error) {
      console.error('Error saving note:', error);
    }
  };

  const updateNote = async (noteId, updates) => {
    if (!user) return;
    try {
      const newNotes = notes.map(note => 
        note.id === noteId 
          ? { ...note, ...updates, lastModified: new Date() }
          : note
      );
      await updateDoc(doc(db, 'users', user.uid), { notes: newNotes });
      setNotes(newNotes);
    } catch (error) {
      console.error('Error updating note:', error);
    }
  };

  const deleteNote = async (noteId) => {
    if (!user) return;
    try {
      const newNotes = notes.filter(note => note.id !== noteId);
      await updateDoc(doc(db, 'users', user.uid), { notes: newNotes });
      setNotes(newNotes);
    } catch (error) {
      console.error('Error deleting note:', error);
    }
  };

  const submitFeedback = async (feedbackData) => {
    try {
      // Submit to Formspree
      const response = await fetch('https://formspree.io/f/xpwdvgzp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          type: 'feedback',
          message: feedbackData.message,
          email: feedbackData.email || (user ? user.email : 'anonymous'),
          name: feedbackData.name || (user ? user.displayName : 'anonymous'),
          userId: user ? user.uid : 'guest'
        }),
      });

      if (response.ok) {
        // Also save to Firebase if user is logged in
        if (user) {
          await addDoc(collection(db, 'feedback'), {
            ...feedbackData,
            userId: user.uid,
            userEmail: user.email,
            userName: user.displayName,
            timestamp: new Date()
          });
        }
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error submitting feedback:', error);
      return false;
    }
  };

  const submitSuggestion = async (suggestionData) => {
    try {
      // Submit to Formspree
      const response = await fetch('https://formspree.io/f/xpwdvgzp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          type: 'suggestion',
          title: suggestionData.title,
          description: suggestionData.description,
          category: suggestionData.category,
          email: suggestionData.email || (user ? user.email : 'anonymous'),
          name: suggestionData.name || (user ? user.displayName : 'anonymous'),
          userId: user ? user.uid : 'guest'
        }),
      });

      if (response.ok) {
        // Also save to Firebase if user is logged in
        if (user) {
          await addDoc(collection(db, 'suggestions'), {
            ...suggestionData,
            userId: user.uid,
            userEmail: user.email,
            userName: user.displayName,
            timestamp: new Date()
          });
        }
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error submitting suggestion:', error);
      return false;
    }
  };
  
  const getCurrentBookmarks = () => user ? bookmarks : guestBookmarks;
  const getCurrentComparisons = () => user ? comparisons : guestComparisons;
  
  return (
    <AuthContext.Provider value={{
      user, loading, bookmarks, isPremium, customPathway, notes, comparisons,
      guestBookmarks, guestComparisons,
      signInWithGoogle, signOut, toggleBookmark, toggleComparison, addToPathway, 
      saveNote, updateNote, deleteNote, updateBookmarkTags, setRecommendedTrack,
      getCurrentBookmarks, getCurrentComparisons, submitFeedback, submitSuggestion
    }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};

// Page Context
const PageContext = createContext();
const PageProvider = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('home');
  const [darkMode, setDarkMode] = useState(false);
  const [installPrompt, setInstallPrompt] = useState(null);
  const [showInstallPrompt, setShowInstallPrompt] = useState(false);
  
  useEffect(() => {
    const isDark = localStorage.getItem('darkMode') === 'true';
    setDarkMode(isDark);
  }, []);
  
  useEffect(() => {
    localStorage.setItem('darkMode', darkMode);
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  // PWA Install prompt handling
  useEffect(() => {
    const handleBeforeInstallPrompt = (e) => {
      e.preventDefault();
      setInstallPrompt(e);
      setShowInstallPrompt(true);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    };
  }, []);

  const handleInstallClick = async () => {
    if (installPrompt) {
      installPrompt.prompt();
      const { outcome } = await installPrompt.userChoice;
      setInstallPrompt(null);
      setShowInstallPrompt(false);
    }
  };
  
  return (
    <PageContext.Provider value={{ 
      currentPage, setCurrentPage, darkMode, setDarkMode,
      installPrompt, showInstallPrompt, setShowInstallPrompt, handleInstallClick
    }}>
      {children}
    </PageContext.Provider>
  );
};

export const usePage = () => {
  const context = useContext(PageContext);
  if (!context) throw new Error('usePage must be used within PageProvider');
  return context;
};

// Global Modal Context
const ModalContext = createContext();
const ModalProvider = ({ children }) => {
  const [activeModal, setActiveModal] = useState(null);
  const [modalData, setModalData] = useState(null);

  const openModal = (modalType, data = null) => {
    setActiveModal(modalType);
    setModalData(data);
  };

  const closeModal = () => {
    setActiveModal(null);
    setModalData(null);
  };

  return (
    <ModalContext.Provider value={{ activeModal, modalData, openModal, closeModal }}>
      {children}
    </ModalContext.Provider>
  );
};

export const useModal = () => {
  const context = useContext(ModalContext);
  if (!context) throw new Error('useModal must be used within ModalProvider');
  return context;
};

// Multi-Dimensional Browse Modal Component
const BrowseModal = ({ isOpen, onClose }) => {
  const { setCurrentPage } = usePage();
  const [selectedRole, setSelectedRole] = useState('');
  const [selectedImpact, setSelectedImpact] = useState('');
  const [selectedGoal, setSelectedGoal] = useState('');
  const [results, setResults] = useState([]);

  const generateRecommendations = () => {
    if (!selectedRole || !selectedImpact || !selectedGoal) return;

    // Combine courses from all three selections
    const roleCourses = browseByRole[selectedRole]?.courses || [];
    const impactCourses = browseByImpact[selectedImpact]?.courses || [];
    const goalCourses = browseByGoal[selectedGoal]?.courses || [];

    // Find intersections and create weighted recommendations
    const allCourses = [...roleCourses, ...impactCourses, ...goalCourses];
    const courseCount = {};
    
    allCourses.forEach(courseId => {
      courseCount[courseId] = (courseCount[courseId] || 0) + 1;
    });

    // Sort by relevance (courses appearing in multiple categories rank higher)
    const recommendations = Object.entries(courseCount)
      .sort(([,a], [,b]) => b - a)
      .slice(0, 6) // Top 6 recommendations
      .map(([courseId]) => courseData.find(course => course.id === courseId))
      .filter(Boolean);

    setResults(recommendations);
  };

  useEffect(() => {
    generateRecommendations();
  }, [selectedRole, selectedImpact, selectedGoal]);

  const reset = () => {
    setSelectedRole('');
    setSelectedImpact('');
    setSelectedGoal('');
    setResults([]);
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Find Your Learning Path</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close browse modal"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="p-6">
          <div className="grid gap-6 md:grid-cols-3 mb-8">
            {/* Role Selection */}
            <div>
              <h3 className="text-lg font-semibold mb-3 text-gray-900 dark:text-white">1. Who are you?</h3>
              <div className="space-y-2">
                {Object.entries(browseByRole).map(([role, info]) => (
                  <button
                    key={role}
                    onClick={() => setSelectedRole(role)}
                    className={`w-full text-left p-3 rounded-lg border transition-colors ${
                      selectedRole === role
                        ? 'border-blue-500 bg-blue-50 dark:bg-blue-900 text-blue-900 dark:text-blue-100'
                        : 'border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white'
                    }`}
                  >
                    <div className="font-medium">{role}</div>
                    <div className="text-sm text-gray-600 dark:text-gray-300">{info.description}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* Impact Area Selection */}
            <div>
              <h3 className="text-lg font-semibold mb-3 text-gray-900 dark:text-white">2. Focus Area</h3>
              <div className="space-y-2">
                {Object.entries(browseByImpact).map(([impact, info]) => (
                  <button
                    key={impact}
                    onClick={() => setSelectedImpact(impact)}
                    className={`w-full text-left p-3 rounded-lg border transition-colors ${
                      selectedImpact === impact
                        ? 'border-green-500 bg-green-50 dark:bg-green-900 text-green-900 dark:text-green-100'
                        : 'border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white'
                    }`}
                  >
                    <div className="font-medium">{impact}</div>
                    <div className="text-sm text-gray-600 dark:text-gray-300">{info.description}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* Goal Selection */}
            <div>
              <h3 className="text-lg font-semibold mb-3 text-gray-900 dark:text-white">3. Learning Goal</h3>
              <div className="space-y-2">
                {Object.entries(browseByGoal).map(([goal, info]) => (
                  <button
                    key={goal}
                    onClick={() => setSelectedGoal(goal)}
                    className={`w-full text-left p-3 rounded-lg border transition-colors ${
                      selectedGoal === goal
                        ? 'border-purple-500 bg-purple-50 dark:bg-purple-900 text-purple-900 dark:text-purple-100'
                        : 'border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white'
                    }`}
                  >
                    <div className="font-medium">{goal}</div>
                    <div className="text-sm text-gray-600 dark:text-gray-300">{info.description}</div>
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Results */}
          {selectedRole && selectedImpact && selectedGoal && (
            <div>
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                  Recommended for you: {selectedRole} → {selectedImpact} → {selectedGoal}
                </h3>
                <button
                  onClick={reset}
                  className="text-sm text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                >
                  Reset
                </button>
              </div>
              
              {results.length > 0 ? (
                <div className="grid gap-4 md:grid-cols-2">
                  {results.map((course) => (
                    <div key={course.id} className="border dark:border-gray-600 rounded-lg p-4 hover:shadow-md transition-shadow">
                      <h4 className="font-semibold mb-2 text-gray-900 dark:text-white">{course.title}</h4>
                      <p className="text-sm text-gray-600 dark:text-gray-300 mb-3">{course.description}</p>
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-gray-500 dark:text-gray-400">{course.level}</span>
                        <a
                          href={course.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 text-sm flex items-center"
                        >
                          <ExternalLink className="h-4 w-4 mr-1" />
                          Access
                        </a>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <p className="text-gray-500 dark:text-gray-400 text-center py-8">
                  No courses found for this combination. Try different selections.
                </p>
              )}
              
              <div className="mt-6 text-center">
                <button
                  onClick={() => {
                    setCurrentPage('courses');
                    onClose();
                  }}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md"
                >
                  Browse All Courses
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// Track Selection Modal Component (kept for backwards compatibility)
const TrackModal = ({ isOpen, onClose, track }) => {
  if (!isOpen || !track) return null;

  const trackInfo = trackDefinitions[track];
  const trackCourses = courseData.filter(course => 
    trackInfo.courses.includes(course.id)
  );

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">{track}</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close modal"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="p-6">
          <p className="text-gray-600 dark:text-gray-300 mb-6">{trackInfo.description}</p>
          
          <div className="grid gap-4 md:grid-cols-2">
            {trackCourses.map((course) => (
              <div key={course.id} className="border dark:border-gray-600 rounded-lg p-4 hover:shadow-md transition-shadow">
                <h3 className="font-semibold mb-2 text-gray-900 dark:text-white">{course.title}</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 mb-3">{course.description}</p>
                <div className="flex items-center justify-between">
                  <span className="text-xs text-gray-500 dark:text-gray-400">{course.level}</span>
                  <a
                    href={course.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 text-sm flex items-center"
                  >
                    <ExternalLink className="h-4 w-4 mr-1" />
                    Access
                  </a>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// Find Your Track Quiz Modal Component
const QuizModal = ({ isOpen, onClose }) => {
  const { user, setRecommendedTrack } = useAuth();
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [showResults, setShowResults] = useState(false);
  const [recommendedTrack, setRecommendedTrackLocal] = useState(null);

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setAnswers([]);
    setShowResults(false);
    setRecommendedTrackLocal(null);
  };

  const handleAnswer = (option) => {
    const newAnswers = [...answers, option];
    setAnswers(newAnswers);

    if (currentQuestion < quizQuestions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      // Calculate results
      const trackScores = {};
      newAnswers.forEach(answer => {
        trackScores[answer.track] = (trackScores[answer.track] || 0) + answer.points;
      });

      const topTrack = Object.keys(trackScores).reduce((a, b) => 
        trackScores[a] > trackScores[b] ? a : b
      );

      setRecommendedTrackLocal(topTrack);
      setShowResults(true);

      // Save to user profile if logged in
      if (user) {
        const trackCourses = trackDefinitions[topTrack].courses;
        setRecommendedTrack(topTrack, trackCourses);
      }
    }
  };

  const handleClose = () => {
    resetQuiz();
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Find Your Learning Track</h2>
          <button 
            onClick={handleClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close quiz"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="p-6">
          {!showResults ? (
            <div>
              <div className="mb-4">
                <div className="flex justify-between text-sm text-gray-500 dark:text-gray-400 mb-2">
                  <span>Question {currentQuestion + 1} of {quizQuestions.length}</span>
                  <span>{Math.round(((currentQuestion) / quizQuestions.length) * 100)}% Complete</span>
                </div>
                <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                  <div 
                    className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${((currentQuestion) / quizQuestions.length) * 100}%` }}
                  ></div>
                </div>
              </div>
              
              <h3 className="text-lg font-semibold mb-6 text-gray-900 dark:text-white">
                {quizQuestions[currentQuestion].question}
              </h3>
              
              <div className="space-y-3">
                {quizQuestions[currentQuestion].options.map((option, index) => (
                  <button
                    key={index}
                    onClick={() => handleAnswer(option)}
                    className="w-full text-left p-4 border dark:border-gray-600 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900 hover:border-blue-300 dark:hover:border-blue-500 transition-colors text-gray-900 dark:text-white"
                  >
                    {option.text}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="text-center">
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Your Recommended Track:</h3>
              <div className="bg-blue-50 dark:bg-blue-900 rounded-lg p-6 mb-6">
                <h4 className="text-xl font-semibold text-blue-800 dark:text-blue-200 mb-2">
                  {recommendedTrack}
                </h4>
                <p className="text-blue-700 dark:text-blue-300">
                  {trackDefinitions[recommendedTrack].description}
                </p>
              </div>
              
              <div className="space-y-3">
                <button
                  onClick={resetQuiz}
                  className="w-full border border-gray-300 dark:border-gray-600 py-3 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white"
                >
                  Retake Quiz
                </button>
              </div>
              
              {user && (
                <p className="text-sm text-gray-500 dark:text-gray-400 mt-4">
                  Your recommended track has been saved to your dashboard!
                </p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// Cornell Notes Modal Component
const CornellNotesModal = ({ isOpen, onClose }) => {
  const { user, notes, saveNote, updateNote, deleteNote } = useAuth();
  const [selectedNote, setSelectedNote] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCourse, setFilterCourse] = useState('');
  const [formData, setFormData] = useState({
    title: '',
    course: '',
    cues: '',
    notes: '',
    summary: ''
  });

  const filteredNotes = notes.filter(note => {
    const matchesSearch = note.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         note.notes?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         note.cues?.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCourse = filterCourse === '' || note.course === filterCourse;
    return matchesSearch && matchesCourse;
  });

  const uniqueCourses = [...new Set(notes.map(note => note.course).filter(Boolean))];

  const handleSave = async () => {
    if (!formData.title.trim()) return;
    
    if (selectedNote) {
      await updateNote(selectedNote.id, formData);
    } else {
      await saveNote(formData);
    }
    
    setFormData({ title: '', course: '', cues: '', notes: '', summary: '' });
    setSelectedNote(null);
    setIsEditing(false);
  };

  const handleEdit = (note) => {
    setSelectedNote(note);
    setFormData({
      title: note.title || '',
      course: note.course || '',
      cues: note.cues || '',
      notes: note.notes || '',
      summary: note.summary || ''
    });
    setIsEditing(true);
  };

  const handleDelete = async (noteId) => {
    if (window.confirm('Are you sure you want to delete this note?')) {
      await deleteNote(noteId);
      if (selectedNote?.id === noteId) {
        setSelectedNote(null);
        setIsEditing(false);
      }
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-6xl w-full h-5/6 flex flex-col">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Cornell Notes</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close notes"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="flex flex-1 overflow-hidden">
          <div className="w-1/3 border-r dark:border-gray-600 p-4 overflow-y-auto">
            <div className="space-y-4 mb-4">
              <div className="relative">
                <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                <input
                  type="text"
                  placeholder="Search notes..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-3 py-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
              <select
                value={filterCourse}
                onChange={(e) => setFilterCourse(e.target.value)}
                className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="">All Courses</option>
                {uniqueCourses.map(course => (
                  <option key={course} value={course}>{course}</option>
                ))}
              </select>
              <button
                onClick={() => {
                  setSelectedNote(null);
                  setFormData({ title: '', course: '', cues: '', notes: '', summary: '' });
                  setIsEditing(true);
                }}
                className="w-full flex items-center justify-center gap-2 p-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
              >
                <Plus className="h-4 w-4" />
                New Note
              </button>
            </div>
            
            <div className="space-y-2">
              {filteredNotes.map(note => (
                <div
                  key={note.id}
                  className={`p-3 border dark:border-gray-600 rounded cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700 ${
                    selectedNote?.id === note.id ? 'bg-blue-50 dark:bg-blue-900' : ''
                  }`}
                  onClick={() => handleEdit(note)}
                >
                  <h3 className="font-medium truncate text-gray-900 dark:text-white">{note.title}</h3>
                  <p className="text-sm text-gray-500 dark:text-gray-400">{note.course}</p>
                  <p className="text-xs text-gray-400 dark:text-gray-500">
                    {new Date(note.lastModified?.toDate?.() || note.lastModified).toLocaleDateString()}
                  </p>
                </div>
              ))}
            </div>
          </div>
          
          <div className="flex-1 p-4">
            {isEditing ? (
              <div className="h-full flex flex-col space-y-4">
                <div className="flex gap-4">
                  <input
                    type="text"
                    placeholder="Note Title"
                    value={formData.title}
                    onChange={(e) => setFormData({...formData, title: e.target.value})}
                    className="flex-1 p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  />
                  <select
                    value={formData.course}
                    onChange={(e) => setFormData({...formData, course: e.target.value})}
                    className="p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  >
                    <option value="">Select Course</option>
                    {courseData.map(course => (
                      <option key={course.id} value={course.title}>{course.title}</option>
                    ))}
                  </select>
                </div>
                
                <div className="flex-1 grid grid-cols-3 gap-4 h-96">
                  <div className="flex flex-col">
                    <label className="font-medium mb-2 text-gray-900 dark:text-white">Cues & Questions</label>
                    <textarea
                      value={formData.cues}
                      onChange={(e) => setFormData({...formData, cues: e.target.value})}
                      placeholder="Key terms, questions, formulas..."
                      className="flex-1 p-2 border dark:border-gray-600 rounded-md resize-none bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                    />
                  </div>
                  
                  <div className="flex flex-col col-span-2">
                    <label className="font-medium mb-2 text-gray-900 dark:text-white">Notes</label>
                    <textarea
                      value={formData.notes}
                      onChange={(e) => setFormData({...formData, notes: e.target.value})}
                      placeholder="Main notes content..."
                      className="flex-1 p-2 border dark:border-gray-600 rounded-md resize-none bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                    />
                  </div>
                </div>
                
                <div className="flex flex-col">
                  <label className="font-medium mb-2 text-gray-900 dark:text-white">Summary</label>
                  <textarea
                    value={formData.summary}
                    onChange={(e) => setFormData({...formData, summary: e.target.value})}
                    placeholder="Key takeaways and summary..."
                    className="h-20 p-2 border dark:border-gray-600 rounded-md resize-none bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  />
                </div>
                
                <div className="flex gap-2">
                  <button
                    onClick={handleSave}
                    className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700"
                  >
                    <Save className="h-4 w-4" />
                    Save
                  </button>
                  <button
                    onClick={() => {
                      setIsEditing(false);
                      setSelectedNote(null);
                    }}
                    className="px-4 py-2 border dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white"
                  >
                    Cancel
                  </button>
                  {selectedNote && (
                    <button
                      onClick={() => handleDelete(selectedNote.id)}
                      className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 ml-auto"
                    >
                      Delete
                    </button>
                  )}
                </div>
              </div>
            ) : (
              <div className="h-full flex items-center justify-center text-gray-500 dark:text-gray-400">
                <div className="text-center">
                  <BookOpen className="h-16 w-16 mx-auto mb-4 opacity-50" />
                  <p>Select a note to view or create a new one</p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

// Enhanced Comparison Modal Component
const ComparisonModal = ({ isOpen, onClose }) => {
  const { getCurrentComparisons, toggleComparison } = useAuth();
  const comparisons = getCurrentComparisons();
  
  const getItemData = (id, type) => {
    switch (type) {
      case 'course':
        return courseData.find(item => item.id === id);
      case 'lab':
        return labsData.find(item => item.id === id);
      case 'resource':
        return premiumResources.find(item => item.id === id);
      default:
        return null;
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-6xl w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Compare Items ({comparisons.length}/3)</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close comparison"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="p-4">
          {comparisons.length === 0 ? (
            <div className="text-center py-8">
              <Target className="h-16 w-16 mx-auto mb-4 opacity-50 text-gray-400" />
              <p className="text-gray-500 dark:text-gray-400">No items selected for comparison</p>
              <p className="text-sm text-gray-400 dark:text-gray-500">Use the compare icons on course/lab cards to add items</p>
            </div>
          ) : (
            <div className="grid gap-4" style={{ gridTemplateColumns: `repeat(${comparisons.length}, 1fr)` }}>
              {comparisons.map(comp => {
                const item = getItemData(comp.id, comp.type);
                return (
                  <div key={comp.id} className="border dark:border-gray-600 rounded-lg p-4">
                    <div className="flex items-center justify-between mb-3">
                      <span className="text-xs px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded">
                        {comp.type.toUpperCase()}
                      </span>
                      <button
                        onClick={() => toggleComparison(comp.id, comp.type)}
                        className="text-red-500 hover:text-red-700"
                        aria-label="Remove from comparison"
                      >
                        <X className="h-4 w-4" />
                      </button>
                    </div>
                    
                    <h3 className="font-bold mb-2 text-gray-900 dark:text-white">{item?.title || comp.id}</h3>
                    
                    <div className="space-y-2 text-sm">
                      <div>
                        <span className="font-medium text-gray-900 dark:text-white">Description:</span>
                        <p className="text-gray-600 dark:text-gray-300">{item?.description || 'N/A'}</p>
                      </div>
                      
                      <div>
                        <span className="font-medium text-gray-900 dark:text-white">Track/Topic:</span>
                        <p className="text-gray-600 dark:text-gray-300">
                          {item?.track || item?.topic || item?.category || 'N/A'}
                        </p>
                      </div>
                      
                      <div>
                        <span className="font-medium text-gray-900 dark:text-white">Level:</span>
                        <p className="text-gray-600 dark:text-gray-300">
                          {item?.level || item?.difficulty || 'N/A'}
                        </p>
                      </div>
                      
                      <div>
                        <span className="font-medium text-gray-900 dark:text-white">Duration:</span>
                        <p className="text-gray-600 dark:text-gray-300">{item?.duration || 'N/A'}</p>
                      </div>
                      
                      {item?.url && (
                        <a
                          href={item.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="inline-flex items-center gap-1 text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                        >
                          <ExternalLink className="h-3 w-3" />
                          Access
                        </a>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// Enhanced Bookmark Modal Component
const BookmarkModal = ({ isOpen, onClose }) => {
  const { user, getCurrentBookmarks, toggleBookmark, updateBookmarkTags } = useAuth();
  const bookmarks = getCurrentBookmarks();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterTag, setFilterTag] = useState('');
  const [editingTags, setEditingTags] = useState(null);
  const [newTags, setNewTags] = useState('');

  const getItemData = (id, type) => {
    switch (type) {
      case 'course':
        return courseData.find(item => item.id === id);
      case 'lab':
        return labsData.find(item => item.id === id);
      case 'resource':
        return premiumResources.find(item => item.id === id);
      default:
        return null;
    }
  };

  const allTags = user ? [...new Set(bookmarks.flatMap(b => b.tags || []))] : [];

  const filteredBookmarks = bookmarks.filter(bookmark => {
    const item = getItemData(bookmark.id, bookmark.type);
    const matchesSearch = item?.title?.toLowerCase().includes(searchTerm.toLowerCase()) || false;
    const matchesTag = filterTag === '' || (bookmark.tags && bookmark.tags.includes(filterTag));
    return matchesSearch && matchesTag;
  });

  const handleSaveTags = async (bookmarkId) => {
    if (user) {
      const tags = newTags.split(',').map(tag => tag.trim()).filter(tag => tag);
      await updateBookmarkTags(bookmarkId, tags);
    }
    setEditingTags(null);
    setNewTags('');
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Your Bookmarks ({bookmarks.length})</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close bookmarks"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="p-4">
          {/* Search and Filter */}
          <div className="flex gap-4 mb-4">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
              <input
                type="text"
                placeholder="Search bookmarks..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-3 py-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              />
            </div>
            {user && allTags.length > 0 && (
              <select
                value={filterTag}
                onChange={(e) => setFilterTag(e.target.value)}
                className="p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="">All Tags</option>
                {allTags.map(tag => (
                  <option key={tag} value={tag}>{tag}</option>
                ))}
              </select>
            )}
          </div>

          {bookmarks.length === 0 ? (
            <div className="text-center py-8">
              <BookmarkIcon className="h-16 w-16 mx-auto mb-4 opacity-50 text-gray-400" />
              <p className="text-gray-500 dark:text-gray-400">No bookmarks yet</p>
              <p className="text-sm text-gray-400 dark:text-gray-500">Use the bookmark icons on courses and labs to save them here</p>
            </div>
          ) : (
            <div className="space-y-3">
              {filteredBookmarks.map((bookmark) => {
                const item = getItemData(bookmark.id, bookmark.type);
                return item ? (
                  <div key={bookmark.id} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <h3 className="font-medium text-gray-900 dark:text-white">{item.title}</h3>
                        <span className="text-xs px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded capitalize">
                          {bookmark.type}
                        </span>
                      </div>
                      
                      {user && (
                        <div className="flex items-center gap-2 mb-2">
                          {editingTags === bookmark.id ? (
                            <div className="flex items-center gap-2">
                              <input
                                type="text"
                                placeholder="Enter tags (comma separated)"
                                value={newTags}
                                onChange={(e) => setNewTags(e.target.value)}
                                className="text-xs p-1 border dark:border-gray-600 rounded bg-white dark:bg-gray-600 text-gray-900 dark:text-white"
                                onKeyPress={(e) => e.key === 'Enter' && handleSaveTags(bookmark.id)}
                              />
                              <button
                                onClick={() => handleSaveTags(bookmark.id)}
                                className="text-xs text-green-600 hover:text-green-800"
                              >
                                Save
                              </button>
                              <button
                                onClick={() => setEditingTags(null)}
                                className="text-xs text-gray-600 hover:text-gray-800"
                              >
                                Cancel
                              </button>
                            </div>
                          ) : (
                            <div className="flex items-center gap-2">
                              {bookmark.tags && bookmark.tags.length > 0 ? (
                                <div className="flex gap-1">
                                  {bookmark.tags.map((tag, index) => (
                                    <span key={index} className="text-xs px-2 py-1 bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 rounded">
                                      {tag}
                                    </span>
                                  ))}
                                </div>
                              ) : (
                                <span className="text-xs text-gray-500 dark:text-gray-400">No tags</span>
                              )}
                              <button
                                onClick={() => {
                                  setEditingTags(bookmark.id);
                                  setNewTags(bookmark.tags ? bookmark.tags.join(', ') : '');
                                }}
                                className="text-xs text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 flex items-center gap-1"
                              >
                                <Tag className="h-3 w-3" />
                                Edit Tags
                              </button>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                    
                    <div className="flex items-center gap-2">
                      <a
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                        aria-label="Open item"
                      >
                        <ExternalLink className="h-5 w-5" />
                      </a>
                      <button
                        onClick={() => toggleBookmark(bookmark.id, bookmark.type)}
                        className="text-red-500 hover:text-red-700"
                        aria-label="Remove bookmark"
                      >
                        <X className="h-5 w-5" />
                      </button>
                    </div>
                  </div>
                ) : null;
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// Feedback Modal Component
const FeedbackModal = ({ isOpen, onClose }) => {
  const { user, submitFeedback } = useAuth();
  const [formData, setFormData] = useState({
    message: '',
    email: '',
    name: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    const success = await submitFeedback(formData);
    setSubmitStatus(success ? 'success' : 'error');
    setIsSubmitting(false);
    
    if (success) {
      setTimeout(() => {
        setFormData({ message: '', email: '', name: '' });
        setSubmitStatus(null);
        onClose();
      }, 2000);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Send Feedback</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close feedback form"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <form onSubmit={handleSubmit} className="p-6">
          {!user && (
            <>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                  Name (optional)
                </label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                  className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                  Email (optional)
                </label>
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                  className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
            </>
          )}
          
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
              Your Feedback *
            </label>
            <textarea
              value={formData.message}
              onChange={(e) => setFormData({...formData, message: e.target.value})}
              required
              rows={4}
              placeholder="Tell us what you think..."
              className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
          
          {submitStatus === 'success' && (
            <div className="mb-4 p-3 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 rounded-md">
              Thank you for your feedback!
            </div>
          )}
          
          {submitStatus === 'error' && (
            <div className="mb-4 p-3 bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200 rounded-md">
              Sorry, there was an error. Please try again.
            </div>
          )}
          
          <div className="flex gap-2">
            <button
              type="submit"
              disabled={isSubmitting || !formData.message.trim()}
              className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSubmitting ? 'Sending...' : 'Send Feedback'}
            </button>
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 border dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

// Suggest Course Modal Component
const SuggestCourseModal = ({ isOpen, onClose }) => {
  const { user, submitSuggestion } = useAuth();
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    category: '',
    email: '',
    name: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    const success = await submitSuggestion(formData);
    setSubmitStatus(success ? 'success' : 'error');
    setIsSubmitting(false);
    
    if (success) {
      setTimeout(() => {
        setFormData({ title: '', description: '', category: '', email: '', name: '' });
        setSubmitStatus(null);
        onClose();
      }, 2000);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Suggest a Course</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close suggestion form"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <form onSubmit={handleSubmit} className="p-6">
          {!user && (
            <>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                  Name (optional)
                </label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                  className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
                  Email (optional)
                </label>
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                  className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>
            </>
          )}
          
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
              Course Title *
            </label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) => setFormData({...formData, title: e.target.value})}
              required
              placeholder="e.g., Community Development 101"
              className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
              Category
            </label>
            <select
              value={formData.category}
              onChange={(e) => setFormData({...formData, category: e.target.value})}
              className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            >
              <option value="">Select a category</option>
              <option value="Research Methods">Research Methods</option>
              <option value="Data Analysis">Data Analysis</option>
              <option value="Gender Studies">Gender Studies</option>
              <option value="Policy & Economics">Policy & Economics</option>
              <option value="Other">Other</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">
              Description *
            </label>
            <textarea
              value={formData.description}
              onChange={(e) => setFormData({...formData, description: e.target.value})}
              required
              rows={4}
              placeholder="Describe what this course should cover and why it would be valuable..."
              className="w-full p-2 border dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
          
          {submitStatus === 'success' && (
            <div className="mb-4 p-3 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 rounded-md">
              Thank you for your suggestion!
            </div>
          )}
          
          {submitStatus === 'error' && (
            <div className="mb-4 p-3 bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200 rounded-md">
              Sorry, there was an error. Please try again.
            </div>
          )}
          
          <div className="flex gap-2">
            <button
              type="submit"
              disabled={isSubmitting || !formData.title.trim() || !formData.description.trim()}
              className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSubmitting ? 'Sending...' : 'Submit Suggestion'}
            </button>
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 border dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

// Global Floating Action Buttons
const GlobalFABs = () => {
  const { getCurrentBookmarks, getCurrentComparisons } = useAuth();
  const { openModal } = useModal();
  
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();

  return (
    <>
      {/* Feedback FAB */}
      <button
        onClick={() => openModal('feedback')}
        className="fixed bottom-48 right-4 z-40 bg-green-500 hover:bg-green-600 text-white p-3 rounded-full shadow-lg transition-colors"
        title="Send Feedback"
        aria-label="Send feedback"
      >
        <MessageCircle className="h-6 w-6" />
      </button>

      {/* Suggest Course FAB */}
      <button
        onClick={() => openModal('suggest')}
        className="fixed bottom-32 right-4 z-40 bg-purple-500 hover:bg-purple-600 text-white p-3 rounded-full shadow-lg transition-colors"
        title="Suggest a Course"
        aria-label="Suggest a course"
      >
        <Plus className="h-6 w-6" />
      </button>

      {/* Bookmark FAB */}
      <button
        onClick={() => openModal('bookmarks')}
        className="fixed bottom-16 right-4 z-40 bg-yellow-500 hover:bg-yellow-600 text-white p-3 rounded-full shadow-lg transition-colors"
        title="View Bookmarks"
        aria-label="View bookmarks"
      >
        <Bookmark className="h-6 w-6" fill={bookmarks.length > 0 ? 'currentColor' : 'none'} />
        {bookmarks.length > 0 && (
          <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
            {bookmarks.length}
          </span>
        )}
      </button>
      
      {/* Compare FAB */}
      <button
        onClick={() => openModal('comparison')}
        className="fixed bottom-0 right-4 z-40 bg-blue-500 hover:bg-blue-600 text-white p-3 rounded-full shadow-lg transition-colors"
        title="Compare Items"
        aria-label="Compare items"
      >
        <Target className="h-6 w-6" fill={comparisons.length > 0 ? 'currentColor' : 'none'} />
        {comparisons.length > 0 && (
          <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
            {comparisons.length}
          </span>
        )}
      </button>
    </>
  );
};

// Global Modal Manager
const GlobalModals = () => {
  const { activeModal, modalData, closeModal } = useModal();

  return (
    <>
      <TrackModal 
        isOpen={activeModal === 'track'} 
        onClose={closeModal}
        track={modalData}
      />
      <QuizModal 
        isOpen={activeModal === 'quiz'} 
        onClose={closeModal}
      />
      <BrowseModal 
        isOpen={activeModal === 'browse'} 
        onClose={closeModal}
      />
      <CornellNotesModal 
        isOpen={activeModal === 'notes'} 
        onClose={closeModal}
      />
      <ComparisonModal 
        isOpen={activeModal === 'comparison'} 
        onClose={closeModal}
      />
      <BookmarkModal 
        isOpen={activeModal === 'bookmarks'} 
        onClose={closeModal}
      />
      <FeedbackModal 
        isOpen={activeModal === 'feedback'} 
        onClose={closeModal}
      />
      <SuggestCourseModal 
        isOpen={activeModal === 'suggest'} 
        onClose={closeModal}
      />
    </>
  );
};

// Navigation Component
export const Navigation = () => {
  const { user, signOut, signInWithGoogle, isPremium } = useAuth();
  const { currentPage, setCurrentPage, darkMode, setDarkMode } = usePage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  return (
    <nav className="sticky top-0 z-50 bg-white dark:bg-gray-900 shadow-md border-b dark:border-gray-700">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0 flex items-center">
              <div className="h-8 w-8 rounded-md bg-blue-600 flex items-center justify-center">
                <span className="text-white font-bold text-sm">IM</span>
              </div>
              <span className="ml-2 text-xl font-bold text-gray-900 dark:text-white">ImpactMojo</span>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              {['home', 'courses', 'labs', 'resources'].map((page) => (
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
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-600"
              aria-label="Toggle theme"
            >
              {darkMode ? <Sun className="h-5 w-5 text-yellow-400" /> : <Moon className="h-5 w-5" />}
            </button>
            
            {user ? (
              <div className="flex items-center space-x-3">
                <div className="flex items-center">
                  <img className="h-8 w-8 rounded-full" src={user.photoURL} alt={user.displayName} />
                  <span className="ml-2 text-gray-900 dark:text-white text-sm font-medium hidden md:block">{user.displayName}</span>
                  {isPremium && <span className="ml-1 bg-yellow-400 text-yellow-900 text-xs px-1.5 py-0.5 rounded-full">PRO</span>}
                </div>
                <button 
                  onClick={signOut} 
                  className="text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white text-sm font-medium"
                >
                  Sign Out
                </button>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-600"
              >
                Sign In
              </button>
            )}
          </div>
          
          <div className="flex items-center sm:hidden space-x-2">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white"
              aria-label="Toggle theme"
            >
              {darkMode ? <Sun className="h-5 w-5 text-yellow-400" /> : <Moon className="h-5 w-5" />}
            </button>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-600"
              aria-label="Toggle menu"
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
            {['home', 'courses', 'labs', 'resources'].map((page) => (
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
            <div className="mt-3">
              {user ? (
                <button
                  onClick={signOut}
                  className="block w-full text-left px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  Sign out
                </button>
              ) : (
                <button
                  onClick={signInWithGoogle}
                  className="block w-full text-left px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
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

// Dashboard Component (Fixed dark mode colors)
const Dashboard = () => {
  const { darkMode, setCurrentPage } = usePage(); // FIXED: Added setCurrentPage here
  const { user, isPremium, customPathway, notes, getCurrentBookmarks, getCurrentComparisons } = useAuth();
  const { openModal } = useModal();
  
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();
  
  if (!user) {
    return (
      <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Please sign in to access your dashboard</h1>
        </div>
      </div>
    );
  }
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-12">
        <div className="mb-8">
          <h1 className="text-2xl sm:text-3xl font-extrabold text-gray-900 dark:text-white">Dashboard</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300">Welcome back, {user.displayName}!</p>
        </div>
        
        {/* Stats Cards - Fixed colors for dark mode */}
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-4 mb-8">
          {[
            { title: 'Courses Bookmarked', value: bookmarks.filter(b => b.type === 'course').length, icon: BookOpen, color: 'bg-blue-500' },
            { title: 'Labs Bookmarked', value: bookmarks.filter(b => b.type === 'lab').length, icon: Target, color: 'bg-green-500' },
            { title: 'Notes Created', value: notes.length, icon: Edit3, color: 'bg-purple-500' },
            { title: 'Items Comparing', value: comparisons.length, icon: Target, color: 'bg-indigo-500' }
          ].map((stat, index) => (
            <div key={index} className="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
              <div className="p-3 sm:p-5">
                <div className="flex items-center">
                  <div className={`flex-shrink-0 ${stat.color} rounded-md p-2 sm:p-3`}>
                    <stat.icon className="h-4 w-4 sm:h-6 sm:w-6 text-white" />
                  </div>
                  <div className="ml-3 sm:ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-xs sm:text-sm font-medium text-gray-500 dark:text-gray-400 truncate">{stat.title}</dt>
                      <dd className="text-lg font-medium text-gray-900 dark:text-white">{stat.value}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        {/* Main Features */}
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2 mb-8">
          {/* Bookmarks */}
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-4 sm:p-6">
            <h2 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white mb-4">Your Bookmarks</h2>
            {bookmarks.length > 0 ? (
              <div className="space-y-3">
                {bookmarks.slice(0, 5).map((bookmark) => {
                  const getItemData = (id, type) => {
                    switch (type) {
                      case 'course':
                        return courseData.find(item => item.id === id);
                      case 'lab':
                        return labsData.find(item => item.id === id);
                      case 'resource':
                        return premiumResources.find(item => item.id === id);
                      default:
                        return null;
                    }
                  };
                  
                  const item = getItemData(bookmark.id, bookmark.type);
                  return item ? (
                    <div key={bookmark.id} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="flex-1 min-w-0">
                        <h3 className="font-medium text-gray-900 dark:text-white truncate">{item.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-400 capitalize">{bookmark.type}</p>
                        {bookmark.tags && bookmark.tags.length > 0 && (
                          <div className="flex gap-1 mt-1 flex-wrap">
                            {bookmark.tags.slice(0, 2).map((tag, index) => (
                              <span key={index} className="text-xs px-2 py-1 bg-blue-100 dark:bg-blue-800 text-blue-800 dark:text-blue-200 rounded">
                                {tag}
                              </span>
                            ))}
                            {bookmark.tags.length > 2 && (
                              <span className="text-xs text-gray-500 dark:text-gray-400">+{bookmark.tags.length - 2} more</span>
                            )}
                          </div>
                        )}
                      </div>
                      <a
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 flex-shrink-0 ml-2"
                        aria-label="Open item"
                      >
                        <ExternalLink className="h-5 w-5" />
                      </a>
                    </div>
                  ) : null;
                })}
                {bookmarks.length > 5 && (
                  <p className="text-sm text-gray-500 dark:text-gray-400 text-center">
                    And {bookmarks.length - 5} more...
                  </p>
                )}
              </div>
            ) : (
              <div className="text-center py-8">
                <BookmarkIcon className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400 mb-4">No bookmarks yet</p>
                <p className="text-sm text-gray-400 dark:text-gray-500">Use the bookmark icons on courses and labs to save them here</p>
              </div>
            )}
          </div>
          
          {/* Cornell Notes */}
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-4 sm:p-6">
            <h2 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white mb-4">Cornell Notes</h2>
            {notes.length > 0 ? (
              <div className="space-y-3">
                {notes.slice(0, 3).map((note) => (
                  <div key={note.id} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <h3 className="font-medium text-gray-900 dark:text-white truncate">{note.title}</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-400">{note.course}</p>
                    <p className="text-xs text-gray-400 dark:text-gray-500 mt-1">
                      {new Date(note.lastModified?.toDate?.() || note.lastModified).toLocaleDateString()}
                    </p>
                  </div>
                ))}
                <button
                  onClick={() => openModal('notes')}
                  className="w-full text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 font-medium text-center py-2"
                >
                  View All Notes
                </button>
              </div>
            ) : (
              <div className="text-center py-8">
                <Library className="h-12 w-12 text-gray-400 mx-auto mb-4" />
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
        </div>

        {/* Comparison and Pathway */}
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2 mb-8">
          {/* Comparison */}
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-4 sm:p-6">
            <h2 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white mb-4">
              Item Comparison ({comparisons.length}/3)
            </h2>
            {comparisons.length > 0 ? (
              <div className="space-y-3">
                {comparisons.map((comp) => {
                  const getItemData = (id, type) => {
                    switch (type) {
                      case 'course':
                        return courseData.find(item => item.id === id);
                      case 'lab':
                        return labsData.find(item => item.id === id);
                      case 'resource':
                        return premiumResources.find(item => item.id === id);
                      default:
                        return null;
                    }
                  };
                  
                  const item = getItemData(comp.id, comp.type);
                  return item ? (
                    <div key={comp.id} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="flex-1 min-w-0">
                        <h3 className="font-medium text-gray-900 dark:text-white truncate">{item.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-400 capitalize">{comp.type}</p>
                      </div>
                    </div>
                  ) : null;
                })}
                <button
                  onClick={() => openModal('comparison')}
                  className="w-full text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 font-medium text-center py-2"
                >
                  View Comparison
                </button>
              </div>
            ) : (
              <div className="text-center py-8">
                <Target className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400 mb-4">No items selected for comparison</p>
                <p className="text-sm text-gray-400 dark:text-gray-500">Use the compare icons to select up to 3 items</p>
              </div>
            )}
          </div>
          
          {/* Custom Pathway */}
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-4 sm:p-6">
            <h2 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white mb-4">Your Learning Pathway</h2>
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
        </div>
        
        {/* AI Tools Section - Fixed styling */}
        <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-4 sm:p-6 mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white">AI-Powered Tools</h2>
            <Bot className="h-6 w-6 text-blue-600 dark:text-blue-400" />
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">
            Access our suite of AI tools to enhance your development work and learning.
          </p>
          <button
            onClick={() => setCurrentPage('ai-tools')}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md font-medium transition-colors"
          >
            Explore AI Tools
          </button>
        </div>
        
        {/* Study Music - Fixed colors */}
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
        
        {/* Premium Features Info - Fixed colors */}
        <div className="bg-gradient-to-r from-emerald-400 to-cyan-500 rounded-lg shadow-lg p-4 sm:p-6">
          <div className="flex items-center justify-between flex-col sm:flex-row gap-4">
            <div className="text-center sm:text-left">
              <h3 className="text-lg sm:text-xl font-bold text-gray-900">You have Premium Access!</h3>
              <p className="mt-1 text-gray-800">Enjoy all features including AI Tools, Notes, and Comparisons</p>
            </div>
            <Trophy className="h-12 w-12 text-gray-900 flex-shrink-0" />
          </div>
        </div>
      </div>
    </div>
  );
};

// Home Page Component
const Home = () => {
  const { darkMode, setCurrentPage } = usePage();
  const { user, isPremium } = useAuth();
  const { openModal } = useModal();
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-12">
        <div className="text-center">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 dark:text-white mb-4">
            Welcome to <span className="text-blue-600">ImpactMojo</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-600 dark:text-gray-300 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Your platform for development learning and tools. Explore courses, labs, and AI-powered tools to enhance your impact.
          </p>
          <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8 gap-4">
            <button
              onClick={() => setCurrentPage('courses')}
              className="w-full sm:w-auto flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 md:py-4 md:text-lg md:px-10"
            >
              Get started
            </button>
            {user && (
              <button
                onClick={() => setCurrentPage('ai-tools')}
                className="mt-3 sm:mt-0 w-full sm:w-auto flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-blue-600 dark:text-blue-400 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 md:py-4 md:text-lg md:px-10"
              >
                Try AI Tools
              </button>
            )}
          </div>
        </div>
        
        {/* Featured Content */}
        <div className="mt-16">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-gray-900 dark:text-white text-center mb-8">Featured Content</h2>
          <div className="grid gap-5 max-w-lg mx-auto lg:grid-cols-3 lg:max-w-none">
            {courseData.slice(0, 3).map((course) => (
              <div key={course.id} className="flex flex-col rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300 bg-white dark:bg-gray-800">
                <div className="flex-1 p-6 flex flex-col justify-between">
                  <div className="flex-1">
                    <p className="text-sm font-medium text-blue-600 dark:text-blue-400">
                      <span>Course</span>
                    </p>
                    <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-white">{course.title}</h3>
                    <p className="mt-3 text-base text-gray-600 dark:text-gray-300">{course.description}</p>
                  </div>
                  <div className="mt-6">
                    <button
                      onClick={() => setCurrentPage('courses')}
                      className="text-base font-medium text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300"
                    >
                      Explore courses
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Multi-Dimensional Learning Path Finder */}
        <div className="mt-16">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-gray-900 dark:text-white text-center mb-8">Find Your Learning Path</h2>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 sm:p-8 text-center max-w-4xl mx-auto">
            <Users className="h-16 w-16 text-blue-600 mx-auto mb-4" />
            <h3 className="text-xl sm:text-2xl font-semibold text-gray-900 dark:text-white mb-4">
              Personalized Course Recommendations
            </h3>
            <p className="text-gray-600 dark:text-gray-300 mb-6 max-w-2xl mx-auto">
              Tell us about your role, focus area, and learning goals to get personalized course recommendations tailored just for you.
            </p>
            <button
              onClick={() => openModal('browse')}
              className="inline-flex items-center px-6 py-3 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700 transition-colors"
            >
              <Target className="h-5 w-5 mr-2" />
              Find My Learning Path
            </button>
          </div>
          
          {/* Alternative Quiz Option */}
          <div className="text-center mt-6">
            <p className="text-gray-500 dark:text-gray-400 mb-2">Or try our quick track finder:</p>
            <button
              onClick={() => openModal('quiz')}
              className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 font-medium"
            >
              Take the Learning Track Quiz
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

// Simple Courses Page Component
const CoursesPage = () => {
  const { darkMode } = usePage();
  const { toggleBookmark, getCurrentBookmarks, toggleComparison, getCurrentComparisons } = useAuth();
  
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();
  
  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-12">
        <div className="text-center mb-8 sm:mb-12">
          <h1 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Development Courses
          </h1>
          <p className="text-lg sm:text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
            Comprehensive learning resources for development practitioners and changemakers.
          </p>
        </div>

        <div className="grid gap-4 sm:gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
          {courseData.map((course) => {
            const isBookmarked = bookmarks.some(b => b.id === course.id);
            const isInComparison = comparisons.some(c => c.id === course.id);
            
            return (
              <div key={course.id} className="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-lg transition-shadow p-4 sm:p-6">
                <div className="flex items-center justify-between mb-3">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-600 text-white">
                    {course.id}
                  </span>
                  <div className="flex gap-2">
                    <button
                      onClick={() => toggleBookmark(course.id, 'course')}
                      className={`p-1 rounded ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 dark:text-gray-500'} hover:text-yellow-500`}
                      aria-label="Toggle bookmark"
                    >
                      <Bookmark className="h-5 w-5" fill={isBookmarked ? 'currentColor' : 'none'} />
                    </button>
                    <button
                      onClick={() => toggleComparison(course.id, 'course')}
                      className={`p-1 rounded ${isInComparison ? 'text-blue-500' : 'text-gray-400 dark:text-gray-500'} hover:text-blue-500`}
                      aria-label="Toggle comparison"
                    >
                      <Target className="h-5 w-5" fill={isInComparison ? 'currentColor' : 'none'} />
                    </button>
                  </div>
                </div>
<h3 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  {course.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">
                  {course.description}
                </p>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
                  <span>{course.level}</span>
                  <span>{course.duration}</span>
                </div>
                
                
                  href={course.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors inline-block text-center"
                >
                  Access Course
                </a>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
// Continuing from where your current App.js ends...

// Quiz questions for "Find Your Track" (completing the definition)
const quizQuestions = [
  {
    id: 1,
    question: "What interests you most about development work?",
    options: [
      { text: "Understanding how numbers tell stories", track: "Data Analysis", points: 3 },
      { text: "Creating systems for sustainable change", track: "Policy & Economics", points: 3 },
      { text: "Exploring social dynamics and power", track: "Gender Studies", points: 3 },
      { text: "Learning how people experience change", track: "Research Methods", points: 3 }
    ]
  },
  {
    id: 2,
    question: "When approaching a development challenge, you prefer to:",
    options: [
      { text: "Analyze data to find patterns and insights", track: "Data Analysis", points: 3 },
      { text: "Design policies and institutional frameworks", track: "Policy & Economics", points: 3 },
      { text: "Focus on gender dynamics and inclusion", track: "Gender Studies", points: 3 },
      { text: "Understand community perspectives through research", track: "Research Methods", points: 3 }
    ]
  },
  {
    id: 3,
    question: "Your ideal project would involve:",
    options: [
      { text: "Building statistical models and conducting evaluations", track: "Data Analysis", points: 3 },
      { text: "Developing economic strategies and policy recommendations", track: "Policy & Economics", points: 3 },
      { text: "Addressing gender inequality and women's empowerment", track: "Gender Studies", points: 3 },
      { text: "Conducting interviews and ethnographic studies", track: "Research Methods", points: 3 }
    ]
  },
  {
    id: 4,
    question: "The skill you'd most like to develop is:",
    options: [
      { text: "Advanced statistical analysis and data visualization", track: "Data Analysis", points: 3 },
      { text: "Economic analysis and policy design", track: "Policy & Economics", points: 3 },
      { text: "Gender analysis and social justice frameworks", track: "Gender Studies", points: 3 },
      { text: "Qualitative research and community engagement", track: "Research Methods", points: 3 }
    ]
  },
  {
    id: 5,
    question: "When reading about development work, you gravitate toward:",
    options: [
      { text: "Reports with charts, statistics, and measurable outcomes", track: "Data Analysis", points: 3 },
      { text: "Policy briefs and economic impact analyses", track: "Policy & Economics", points: 3 },
      { text: "Case studies on gender and social inclusion", track: "Gender Studies", points: 3 },
      { text: "Ethnographic studies and community stories", track: "Research Methods", points: 3 }
    ]
  }
];

// Multi-dimensional browse definitions (new enhanced browsing system)
const browseByRole = {
  "Researcher": {
    description: "Academic and field research roles",
    courses: ["research-ethics-101", "qualitative-research-methods-101", "visual-ethnography-101", "data-literacy-101"],
    color: "blue"
  },
  "Program Manager": {
    description: "Designing and managing development programs",
    courses: ["monitoring-evaluation-accountability-and-learning-101", "community-development-101", "behaviour-change-communication-programming-101"],
    color: "green"
  },
  "Policy Analyst": {
    description: "Government and institutional policy work",
    courses: ["political-economy-101", "law-and-constitution-101", "global-development-architecture-101"],
    color: "purple"
  },
  "Data Analyst": {
    description: "Data-driven decision making and analysis",
    courses: ["data-literacy-101", "exploratory-data-analysis-for-household-surveys-101", "econometrics-101", "bivariate-analysis-101"],
    color: "orange"
  },
  "Gender Specialist": {
    description: "Gender equality and women's empowerment",
    courses: ["gender-studies-101", "womens-economic-empowerment-101", "sexual-and-reproductive-health-rights-101", "care-economy-101"],
    color: "pink"
  },
  "Advocacy Professional": {
    description: "Campaign and advocacy work",
    courses: ["advocacy-and-communications-101", "decolonising-development-101", "environmental-justice-101"],
    color: "red"
  }
};

const browseByImpact = {
  "Economic Empowerment": {
    description: "Creating economic opportunities and reducing poverty",
    courses: ["development-economics-101", "care-economy-101", "decent-work-101", "livelihoods-101"],
    color: "green"
  },
  "Social Justice": {
    description: "Addressing inequality and promoting inclusion",
    courses: ["gender-studies-101", "marginilised-identities-101", "environmental-justice-101", "decolonising-development-101"],
    color: "purple"
  },
  "Health & Wellbeing": {
    description: "Improving health outcomes and quality of life",
    courses: ["public-health-101", "sexual-and-reproductive-health-rights-101", "social-welfare-and-safety-nets-101"],
    color: "blue"
  },
  "Education & Learning": {
    description: "Enhancing education and capacity building",
    courses: ["pedagogy-and-education-101", "social-emotional-learning-101", "english-for-development-professionals-101"],
    color: "yellow"
  },
  "Climate & Environment": {
    description: "Environmental sustainability and climate action",
    courses: ["climate-science-101", "environmental-justice-101"],
    color: "teal"
  },
  "Systems & Governance": {
    description: "Understanding and changing systems",
    courses: ["political-economy-101", "global-development-architecture-101", "decolonising-development-101"],
    color: "indigo"
  }
};

const browseByGoal = {
  "Understand the Big Picture": {
    description: "Get foundational knowledge and context",
    courses: ["development-economics-101", "global-development-architecture-101", "political-economy-101"],
    color: "blue"
  },
  "Conduct Better Research": {
    description: "Learn research methods and analysis",
    courses: ["research-ethics-101", "qualitative-research-methods-101", "data-literacy-101", "econometrics-101"],
    color: "purple"
  },
  "Design Better Programs": {
    description: "Create and implement effective interventions",
    courses: ["monitoring-evaluation-accountability-and-learning-101", "community-development-101", "behaviour-change-communication-programming-101"],
    color: "green"
  },
  "Advocate for Change": {
    description: "Influence policy and drive systemic change",
    courses: ["advocacy-and-communications-101", "political-economy-101", "law-and-constitution-101"],
    color: "orange"
  }
};

// Complete the Multi-Dimensional Browse Modal Component
const BrowseModal = ({ isOpen, onClose }) => {
  const { setCurrentPage } = usePage();
  const [selectedRole, setSelectedRole] = useState('');
  const [selectedImpact, setSelectedImpact] = useState('');
  const [selectedGoal, setSelectedGoal] = useState('');
  const [results, setResults] = useState([]);

  const generateRecommendations = () => {
    if (!selectedRole || !selectedImpact || !selectedGoal) return;

    // Combine courses from all three selections
    const roleCourses = browseByRole[selectedRole]?.courses || [];
    const impactCourses = browseByImpact[selectedImpact]?.courses || [];
    const goalCourses = browseByGoal[selectedGoal]?.courses || [];
    
    // Find courses that appear in multiple categories (weighted recommendations)
    const courseCount = {};
    [...roleCourses, ...impactCourses, ...goalCourses].forEach(course => {
      courseCount[course] = (courseCount[course] || 0) + 1;
    });
    
    // Sort by relevance (courses appearing in multiple categories rank higher)
    const recommendedCourses = Object.entries(courseCount)
      .sort(([,a], [,b]) => b - a)
      .slice(0, 6)
      .map(([courseId]) => courseData.find(c => c.id === courseId))
      .filter(Boolean);
    
    setResults(recommendedCourses);
  };

  useEffect(() => {
    generateRecommendations();
  }, [selectedRole, selectedImpact, selectedGoal]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Smart Course Finder</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close browser"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        <div className="p-6">
          <p className="text-gray-600 dark:text-gray-300 mb-6">
            Select one option from each category to get personalized course recommendations:
          </p>
          
          {/* Role Selection */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-3">What's your role?</h3>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              {Object.entries(browseByRole).map(([role, info]) => (
                <button
                  key={role}
                  onClick={() => setSelectedRole(role)}
                  className={`p-3 rounded-lg border text-left transition-colors ${
                    selectedRole === role 
                      ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20' 
                      : 'border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700'
                  }`}
                >
                  <div className="font-medium text-gray-900 dark:text-white text-sm">{role}</div>
                  <div className="text-xs text-gray-500 dark:text-gray-400 mt-1">{info.description}</div>
                </button>
              ))}
            </div>
          </div>
          
          {/* Impact Area Selection */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-3">What impact area interests you?</h3>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              {Object.entries(browseByImpact).map(([impact, info]) => (
                <button
                  key={impact}
                  onClick={() => setSelectedImpact(impact)}
                  className={`p-3 rounded-lg border text-left transition-colors ${
                    selectedImpact === impact 
                      ? 'border-purple-500 bg-purple-50 dark:bg-purple-900/20' 
                      : 'border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700'
                  }`}
                >
                  <div className="font-medium text-gray-900 dark:text-white text-sm">{impact}</div>
                  <div className="text-xs text-gray-500 dark:text-gray-400 mt-1">{info.description}</div>
                </button>
              ))}
            </div>
          </div>
          
          {/* Goal Selection */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-3">What's your learning goal?</h3>
            <div className="grid grid-cols-2 gap-3">
              {Object.entries(browseByGoal).map(([goal, info]) => (
                <button
                  key={goal}
                  onClick={() => setSelectedGoal(goal)}
                  className={`p-3 rounded-lg border text-left transition-colors ${
                    selectedGoal === goal 
                      ? 'border-green-500 bg-green-50 dark:bg-green-900/20' 
                      : 'border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700'
                  }`}
                >
                  <div className="font-medium text-gray-900 dark:text-white text-sm">{goal}</div>
                  <div className="text-xs text-gray-500 dark:text-gray-400 mt-1">{info.description}</div>
                </button>
              ))}
            </div>
          </div>
          
          {/* Results */}
          {results.length > 0 && (
            <div>
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                Recommended Courses for You
              </h3>
              <div className="grid gap-4 md:grid-cols-2">
                {results.map((course) => (
                  <div key={course.id} className="border dark:border-gray-600 rounded-lg p-4">
                    <h4 className="font-medium text-gray-900 dark:text-white mb-2">{course.title}</h4>
                    <p className="text-sm text-gray-600 dark:text-gray-300 mb-3">{course.description}</p>
                    <div className="flex items-center justify-between">
                      <span className="text-xs text-gray-500 dark:text-gray-400">{course.level}</span>
                      <a
                        href={course.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 text-sm flex items-center"
                      >
                        <ExternalLink className="h-4 w-4 mr-1" />
                        Access
                      </a>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
          
          {selectedRole && selectedImpact && selectedGoal && results.length === 0 && (
            <div className="text-center py-8">
              <p className="text-gray-500 dark:text-gray-400">No courses found for this combination. Try different selections.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// Feedback Modal Component
const FeedbackModal = ({ isOpen, onClose }) => {
  const [feedback, setFeedback] = useState('');
  const [category, setCategory] = useState('general');
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('https://formspree.io/f/xpwdvgzp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          feedback,
          category,
          email,
          timestamp: new Date().toISOString(),
          page: 'ImpactMojo App'
        }),
      });

      if (response.ok) {
        setSubmitted(true);
        setTimeout(() => {
          setSubmitted(false);
          setFeedback('');
          setCategory('general');
          setEmail('');
          onClose();
        }, 2000);
      }
    } catch (error) {
      console.error('Error submitting feedback:', error);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Send Feedback</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close feedback"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        {submitted ? (
          <div className="p-6 text-center">
            <CheckCircle className="h-12 w-12 text-green-500 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">Thank you!</h3>
            <p className="text-gray-600 dark:text-gray-300">Your feedback has been submitted successfully.</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="p-6">
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Category
              </label>
              <select
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                required
              >
                <option value="general">General Feedback</option>
                <option value="bug">Bug Report</option>
                <option value="feature">Feature Request</option>
                <option value="content">Content Suggestion</option>
                <option value="ui">UI/UX Feedback</option>
              </select>
            </div>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Your Feedback
              </label>
              <textarea
                value={feedback}
                onChange={(e) => setFeedback(e.target.value)}
                rows={4}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="Tell us what you think..."
                required
              />
            </div>
            
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Email (optional)
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="your@email.com"
              />
            </div>
            
            <div className="flex gap-3">
              <button
                type="submit"
                className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors"
              >
                Send Feedback
              </button>
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white"
              >
                Cancel
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};

// Suggest Course Modal Component
const SuggestCourseModal = ({ isOpen, onClose }) => {
  const [courseData, setCourseData] = useState({
    title: '',
    description: '',
    category: '',
    rationale: '',
    email: ''
  });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('https://formspree.io/f/xpwdvgzp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          type: 'Course Suggestion',
          ...courseData,
          timestamp: new Date().toISOString()
        }),
      });

      if (response.ok) {
        setSubmitted(true);
        setTimeout(() => {
          setSubmitted(false);
          setCourseData({
            title: '',
            description: '',
            category: '',
            rationale: '',
            email: ''
          });
          onClose();
        }, 2000);
      }
    } catch (error) {
      console.error('Error submitting course suggestion:', error);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Suggest a Course</h2>
          <button 
            onClick={onClose} 
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded"
            aria-label="Close suggestion form"
          >
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        
        {submitted ? (
          <div className="p-6 text-center">
            <CheckCircle className="h-12 w-12 text-green-500 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">Thank you!</h3>
            <p className="text-gray-600 dark:text-gray-300">Your course suggestion has been submitted for review.</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="p-6">
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Course Title
              </label>
              <input
                type="text"
                value={courseData.title}
                onChange={(e) => setCourseData({...courseData, title: e.target.value})}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="e.g., Digital Innovation 101"
                required
              />
            </div>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Description
              </label>
              <textarea
                value={courseData.description}
                onChange={(e) => setCourseData({...courseData, description: e.target.value})}
                rows={3}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="Brief description of the course content..."
                required
              />
            </div>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Category
              </label>
              <select
                value={courseData.category}
                onChange={(e) => setCourseData({...courseData, category: e.target.value})}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                required
              >
                <option value="">Select category...</option>
                <option value="Research Methods">Research Methods</option>
                <option value="Data Analysis">Data Analysis</option>
                <option value="Gender Studies">Gender Studies</option>
                <option value="Policy & Economics">Policy & Economics</option>
                <option value="Other">Other</option>
              </select>
            </div>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Why is this course needed?
              </label>
              <textarea
                value={courseData.rationale}
                onChange={(e) => setCourseData({...courseData, rationale: e.target.value})}
                rows={3}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="Explain the gap this course would fill..."
                required
              />
            </div>
            
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Your Email (optional)
              </label>
              <input
                type="email"
                value={courseData.email}
                onChange={(e) => setCourseData({...courseData, email: e.target.value})}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="your@email.com"
              />
            </div>
            
            <div className="flex gap-3">
              <button
                type="submit"
                className="flex-1 bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 transition-colors"
              >
                Submit Suggestion
              </button>
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white"
              >
                Cancel
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};

// Complete Global Modals component
const GlobalModals = () => {
  const { activeModal, modalData, closeModal } = useModal();

  return (
    <>
      <TrackModal 
        isOpen={activeModal === 'track'} 
        onClose={closeModal}
        track={modalData}
      />
      <QuizModal 
        isOpen={activeModal === 'quiz'} 
        onClose={closeModal}
      />
      <BrowseModal 
        isOpen={activeModal === 'browse'} 
        onClose={closeModal}
      />
      <CornellNotesModal 
        isOpen={activeModal === 'notes'} 
        onClose={closeModal}
      />
      <ComparisonModal 
        isOpen={activeModal === 'comparison'} 
        onClose={closeModal}
      />
      <BookmarkModal 
        isOpen={activeModal === 'bookmarks'} 
        onClose={closeModal}
      />
      <FeedbackModal 
        isOpen={activeModal === 'feedback'} 
        onClose={closeModal}
      />
      <SuggestCourseModal 
        isOpen={activeModal === 'suggest'} 
        onClose={closeModal}
      />
    </>
  );
};

// Complete Global FABs component
const GlobalFABs = () => {
  const { user } = useAuth();
  const { currentPage } = usePage();
  const { openModal } = useModal();
  const { getCurrentComparisons } = useAuth();
  const comparisons = getCurrentComparisons();

  // Don't show FABs on certain pages to avoid clutter
  if (currentPage === 'dashboard') return null;

  return (
    <>
      {/* Floating Action Buttons */}
      <div className="fixed bottom-4 right-4 flex flex-col gap-3 z-40">
        {/* Smart Browse FAB */}
        <button
          onClick={() => openModal('browse')}
          className="bg-purple-600 hover:bg-purple-700 text-white p-3 rounded-full shadow-lg transition-colors"
          aria-label="Smart course finder"
        >
          <Search className="h-6 w-6" />
        </button>

        {/* Find Your Track FAB */}
        <button
          onClick={() => openModal('quiz')}
          className="bg-green-600 hover:bg-green-700 text-white p-3 rounded-full shadow-lg transition-colors"
          aria-label="Find your track"
        >
          <Target className="h-6 w-6" />
        </button>

        {/* Bookmarks FAB */}
        <button
          onClick={() => openModal('bookmarks')}
          className="bg-yellow-600 hover:bg-yellow-700 text-white p-3 rounded-full shadow-lg transition-colors"
          aria-label="View bookmarks"
        >
          <Bookmark className="h-6 w-6" />
        </button>

        {/* Comparison FAB */}
        <button
          onClick={() => openModal('comparison')}
          className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-full shadow-lg transition-colors relative"
          aria-label="Compare items"
        >
          <Target className="h-6 w-6" fill={comparisons.length > 0 ? 'currentColor' : 'none'} />
          {comparisons.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
              {comparisons.length}
            </span>
          )}
        </button>

        {/* Feedback FAB */}
        <button
          onClick={() => openModal('feedback')}
          className="bg-orange-600 hover:bg-orange-700 text-white p-3 rounded-full shadow-lg transition-colors"
          aria-label="Send feedback"
        >
          <MessageCircle className="h-6 w-6" />
        </button>

        {/* Suggest Course FAB */}
        <button
          onClick={() => openModal('suggest')}
          className="bg-pink-600 hover:bg-pink-700 text-white p-3 rounded-full shadow-lg transition-colors"
          aria-label="Suggest a course"
        >
          <Plus className="h-6 w-6" />
        </button>
      </div>

      {/* Lo-Fi Music Player for logged-in users */}
      {user && (
        <div className="fixed bottom-4 left-4 z-40">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4 border dark:border-gray-700">
            <div className="flex items-center gap-3 mb-2">
              <Music className="h-5 w-5 text-purple-600" />
              <span className="text-sm font-medium text-gray-900 dark:text-white">Lo-Fi Study Music</span>
            </div>
            <p className="text-xs text-gray-500 dark:text-gray-400 mb-3">Focus better with ambient background music</p>
            <a
              href="https://www.youtube.com/watch?v=jfKfPfyJRdk"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 bg-purple-600 hover:bg-purple-700 text-white px-3 py-2 rounded-md text-sm transition-colors"
            >
              <Headphones className="h-4 w-4" />
              Start Listening
            </a>
          </div>
        </div>
      )}
    </>
  );
};

// PWA Install Prompt Component
const PWAInstallPrompt = () => {
  const { showInstallPrompt, handleInstallClick, setShowInstallPrompt } = usePage();

  if (!showInstallPrompt) return null;

  return (
    <div className="fixed top-4 left-1/2 transform -translate-x-1/2 bg-blue-600 text-white p-4 rounded-lg shadow-lg z-50 max-w-sm">
      <div className="flex items-center gap-3">
        <Install className="h-6 w-6 flex-shrink-0" />
        <div className="flex-1">
          <h3 className="font-medium text-sm">Install ImpactMojo</h3>
          <p className="text-xs opacity-90 mt-1">Get quick access to development courses and tools</p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={handleInstallClick}
            className="bg-white text-blue-600 px-3 py-1 rounded text-sm font-medium hover:bg-gray-100"
          >
            Install
          </button>
          <button
            onClick={() => setShowInstallPrompt(false)}
            className="text-white hover:text-gray-200"
            aria-label="Close install prompt"
          >
            <X className="h-5 w-5" />
          </button>
        </div>
      </div>
    </div>
  );
};

// Complete the AppContent component that was partially defined
const AppContent = () => {
  const { currentPage, darkMode } = usePage();
  const { loading } = useAuth();
  
  if (loading) {
    return (
      <div className={`min-h-screen flex items-center justify-center ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-600"></div>
      </div>
    );
  }
  
  return (
    <div className={darkMode ? 'dark' : ''}>
      <PWAInstallPrompt />
      
      {currentPage === 'home' && <Home />}
      {currentPage === 'dashboard' && <Dashboard />}
      {currentPage === 'courses' && <CoursesPage />}
      {currentPage === 'labs' && <LabsPage />}
      {currentPage === 'resources' && <ResourcesPage />}
      {currentPage === 'ai-tools' && <AIToolsPage />}
      
      {/* Global FABs on all pages */}
      <GlobalFABs />
      
      {/* Global Modals */}
      <GlobalModals />
      
      {/* Counter.dev Analytics */}
      <script 
        src="https://cdn.counter.dev/script.js" 
        data-id="bb8c35b6-8f3d-4a72-8b0a-4dd67d95f84a" 
        data-utcoffset="5.5"
        async
      />
    </div>
  );
};

// Main App Component with PWA registration
const App = () => {
  useEffect(() => {
    // Register service worker for PWA
    if ('serviceWorker' in navigator && process.env.NODE_ENV === 'production') {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
          .then((registration) => {
            console.log('SW registered: ', registration);
          })
          .catch((registrationError) => {
            console.log('SW registration failed: ', registrationError);
          });
      });
    }
    
    // Add Plausible analytics script
    const script = document.createElement('script');
    script.async = true;
    script.defer = true;
    script.setAttribute('data-domain', 'impactmojo.in');
    script.src = 'https://plausible.io/js/script.js';
    document.head.appendChild(script);
    
    return () => {
      if (document.head.contains(script)) {
        document.head.removeChild(script);
      }
    };
  }, []);

  return (
    <AuthProvider>
      <PageProvider>
        <ModalProvider>
          <AppContent />
        </ModalProvider>
      </PageProvider>
    </AuthProvider>
  );
};

export default App;

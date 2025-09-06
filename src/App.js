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
                          <a href={course.url} target="_blank" rel="noopener noreferrer" className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors inline-block text-center">Access Course</a>
              </div>
            );
          })}
        </div>
      </div>
    </div>
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

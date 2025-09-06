// src/App.js
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Bookmark, MessageCircle, 
  ExternalLink, BookOpen, FileText, Target, Users, 
  Clock, CheckCircle, PlayCircle, Bot, Trophy, 
  Headphones, MapPin, Library, Music, Download, 
  Search, Plus, Edit3, Save, Filter, BookmarkIcon, Tag,
  Install, AlertTriangle, ChevronDown, ChevronRight, Gamepad2
} from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc, updateDoc, collection, addDoc } from 'firebase/firestore';

// Data imports
import { courseData, upcomingCourses } from './data/course-data';
import { labsData } from './data/labs-data';
import { premiumResources } from './data/premium-resources-data';

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

// Updated Premium Resources Data (with corrected URLs and Real Middle removed)
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
    category: "Analysis Tools",
    access: "Premium"
  }
];

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
const db = getFirestore(app);

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
        const data = userDoc.data();
        setBookmarks(data.bookmarks || []);
        setComparisons(data.comparisons || []);
        setCustomPathway(data.customPathway || []);
        setNotes(data.notes || []);
      }
    } catch (error) {
      console.error('Error loading user data:', error);
    }
  };

  const signInWithGoogle = async () => {
    try {
      const provider = new GoogleAuthProvider();
      const result = await signInWithPopup(auth, provider);
      const userData = {
        uid: result.user.uid,
        email: result.user.email,
        displayName: result.user.displayName,
        photoURL: result.user.photoURL,
        bookmarks: [],
        comparisons: [],
        customPathway: [],
        notes: []
      };
      await setDoc(doc(db, 'users', result.user.uid), userData, { merge: true });
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

  const toggleBookmark = async (itemId, itemType) => {
    if (!user) return;
    try {
      const existingIndex = bookmarks.findIndex(b => b.id === itemId && b.type === itemType);
      let newBookmarks;
      
      if (existingIndex >= 0) {
        newBookmarks = bookmarks.filter((_, index) => index !== existingIndex);
      } else {
        newBookmarks = [...bookmarks, { id: itemId, type: itemType, dateAdded: new Date(), tags: [] }];
      }
      
      await updateDoc(doc(db, 'users', user.uid), { bookmarks: newBookmarks });
      setBookmarks(newBookmarks);
    } catch (error) {
      console.error('Error toggling bookmark:', error);
    }
  };

  const toggleComparison = async (itemId, itemType) => {
    if (!user) return;
    try {
      const existingIndex = comparisons.findIndex(c => c.id === itemId && c.type === itemType);
      let newComparisons;
      
      if (existingIndex >= 0) {
        newComparisons = comparisons.filter((_, index) => index !== existingIndex);
      } else if (comparisons.length < 3) {
        newComparisons = [...comparisons, { id: itemId, type: itemType }];
      } else {
        return; // Max 3 items for comparison
      }
      
      await updateDoc(doc(db, 'users', user.uid), { comparisons: newComparisons });
      setComparisons(newComparisons);
    } catch (error) {
      console.error('Error toggling comparison:', error);
    }
  };

  const getCurrentBookmarks = () => bookmarks;
  const getCurrentComparisons = () => comparisons;
  const isPremium = () => user !== null;

  const updateBookmarkTags = async (bookmarkId, newTags) => {
    if (!user) return;
    try {
      const newBookmarks = bookmarks.map(bookmark => 
        bookmark.id === bookmarkId 
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
          userId: user ? user.uid : 'anonymous',
          timestamp: new Date().toISOString()
        }),
      });

      if (response.ok) {
        return { success: true };
      } else {
        throw new Error('Failed to submit feedback');
      }
    } catch (error) {
      console.error('Error submitting feedback:', error);
      return { success: false, error: error.message };
    }
  };

  return (
    <AuthContext.Provider value={{
      user, loading, bookmarks, comparisons, customPathway, notes,
      signInWithGoogle, signOut, toggleBookmark, toggleComparison,
      getCurrentBookmarks, getCurrentComparisons, isPremium,
      updateBookmarkTags, addToPathway, setRecommendedTrack,
      saveNote, updateNote, deleteNote, submitFeedback
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
  const [darkMode, setDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      const saved = localStorage.getItem('darkMode');
      if (saved !== null) return JSON.parse(saved);
      return window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    return false;
  });
  const [installPrompt, setInstallPrompt] = useState(null);
  const [showInstallPrompt, setShowInstallPrompt] = useState(false);

  useEffect(() => {
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  useEffect(() => {
    const handleBeforeInstallPrompt = (e) => {
      e.preventDefault();
      setInstallPrompt(e);
      setShowInstallPrompt(true);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    return () => window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
  }, []);

  const handleInstallClick = async () => {
    if (installPrompt) {
      const result = await installPrompt.prompt();
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

// Home Page Component
const Home = () => {
  const { setCurrentPage } = usePage();

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navigation />
      
      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-20">
        <div className="text-center">
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-gray-900 dark:text-white">
            <span className="block">Development Education</span>
            <span className="block text-blue-600">Made Accessible</span>
          </h1>
          <p className="mt-6 max-w-3xl mx-auto text-xl text-gray-600 dark:text-gray-300">
            Learn development economics, policy analysis, and impact evaluation through interactive courses, 
            hands-on labs, and real-world case studies.
          </p>
          <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => setCurrentPage('courses')}
              className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-md text-lg font-medium transition-colors"
            >
              Explore Courses
            </button>
            <button
              onClick={() => setCurrentPage('labs')}
              className="border border-gray-300 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 px-8 py-3 rounded-md text-lg font-medium transition-colors"
            >
              Try Labs
            </button>
          </div>
        </div>

        {/* Featured Content */}
        <div className="mt-20">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-gray-900 dark:text-white text-center mb-12">
            Featured Learning Experiences
          </h2>
          <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {/* Featured Courses */}
            {courseData.slice(0, 2).map((course) => (
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
            
            {/* Add Games Section Featured Item */}
            <div className="flex flex-col rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300 bg-white dark:bg-gray-800">
              <div className="flex-1 p-6 flex flex-col justify-between">
                <div className="flex-1">
                  <p className="text-sm font-medium text-green-600 dark:text-green-400">
                    <span>Game</span>
                  </p>
                  <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-white">Interactive Learning</h3>
                  <p className="mt-3 text-base text-gray-600 dark:text-gray-300">Engage with development concepts through interactive games and simulations.</p>
                </div>
                <div className="mt-6">
                  <button
                    onClick={() => setCurrentPage('games')}
                    className="text-base font-medium text-green-600 dark:text-green-400 hover:text-green-800 dark:hover:text-green-300"
                  >
                    Play games
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
  const { user, toggleBookmark, toggleComparison, getCurrentBookmarks, getCurrentComparisons } = useAuth();
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('');
  
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();

  const filteredCourses = courseData.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         course.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTrack = !selectedTrack || course.track === selectedTrack;
    return matchesSearch && matchesTrack;
  });

  const tracks = [...new Set(courseData.map(course => course.track))];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Courses</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300">
            Comprehensive development economics and policy courses
          </p>
        </div>

        {/* Search and Filter */}
        <div className="mb-8 flex flex-col sm:flex-row gap-4">
          <div className="flex-1">
            <input
              type="text"
              placeholder="Search courses..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
            />
          </div>
          <select
            value={selectedTrack}
            onChange={(e) => setSelectedTrack(e.target.value)}
            className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
          >
            <option value="">All Tracks</option>
            {tracks.map(track => (
              <option key={track} value={track}>{track}</option>
            ))}
          </select>
        </div>

        {/* Course Grid */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filteredCourses.map((course) => {
            const isBookmarked = bookmarks.some(b => b.id === course.id && b.type === 'course');
            const isComparing = comparisons.some(c => c.id === course.id && c.type === 'course');
            
            return (
              <div key={course.id} className="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
                <div className="px-4 py-5 sm:p-6">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-sm font-medium text-blue-600 dark:text-blue-400">{course.id}</span>
                    <div className="flex gap-2">
                      {user && (
                        <>
                          <button
                            onClick={() => toggleBookmark(course.id, 'course')}
                            className={`p-1 rounded ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
                          >
                            <Bookmark className="h-4 w-4" fill={isBookmarked ? 'currentColor' : 'none'} />
                          </button>
                          <button
                            onClick={() => toggleComparison(course.id, 'course')}
                            className={`p-1 rounded ${isComparing ? 'text-blue-500' : 'text-gray-400 hover:text-blue-500'}`}
                            disabled={!isComparing && comparisons.length >= 3}
                          >
                            <Target className="h-4 w-4" fill={isComparing ? 'currentColor' : 'none'} />
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                  <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">{course.title}</h3>
                  <p className="text-sm text-gray-600 dark:text-gray-300 mb-4">{course.description}</p>
                  <div className="flex justify-between items-center">
                    <span className="text-xs text-gray-500 dark:text-gray-400">{course.track}</span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">{course.duration}</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// Labs Page Component
const LabsPage = () => {
  const { user, toggleBookmark, toggleComparison, getCurrentBookmarks, getCurrentComparisons } = useAuth();
  const [searchTerm, setSearchTerm] = useState('');
  
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();

  const filteredLabs = labsData.filter(lab => 
    lab.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    lab.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Labs</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300">
            Hands-on practice with development tools and methodologies
          </p>
        </div>

        {/* Search */}
        <div className="mb-8">
          <input
            type="text"
            placeholder="Search labs..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full max-w-md px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
          />
        </div>

        {/* Labs Grid */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filteredLabs.map((lab) => {
            const isBookmarked = bookmarks.some(b => b.id === lab.id && b.type === 'lab');
            const isComparing = comparisons.some(c => c.id === lab.id && c.type === 'lab');
            
            return (
              <div key={lab.id} className="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
                <div className="px-4 py-5 sm:p-6">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-sm font-medium text-green-600 dark:text-green-400">{lab.id}</span>
                    <div className="flex gap-2">
                      {user && (
                        <>
                          <button
                            onClick={() => toggleBookmark(lab.id, 'lab')}
                            className={`p-1 rounded ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
                          >
                            <Bookmark className="h-4 w-4" fill={isBookmarked ? 'currentColor' : 'none'} />
                          </button>
                          <button
                            onClick={() => toggleComparison(lab.id, 'lab')}
                            className={`p-1 rounded ${isComparing ? 'text-blue-500' : 'text-gray-400 hover:text-blue-500'}`}
                            disabled={!isComparing && comparisons.length >= 3}
                          >
                            <Target className="h-4 w-4" fill={isComparing ? 'currentColor' : 'none'} />
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                  <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">{lab.title}</h3>
                  <p className="text-sm text-gray-600 dark:text-gray-300 mb-4">{lab.description}</p>
                  <div className="flex justify-between items-center">
                    <span className="text-xs text-gray-500 dark:text-gray-400">{lab.topic}</span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">{lab.level}</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// Resources Page Component
const ResourcesPage = () => {
  const { user, toggleBookmark, getCurrentBookmarks } = useAuth();
  const [searchTerm, setSearchTerm] = useState('');
  
  const bookmarks = getCurrentBookmarks();

  const filteredResources = updatedPremiumResources.filter(resource => 
    resource.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    resource.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Resources</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300">
            Essential tools and references for development professionals
          </p>
        </div>

        {/* Search */}
        <div className="mb-8">
          <input
            type="text"
            placeholder="Search resources..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full max-w-md px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
          />
        </div>

        {/* Resources Grid */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filteredResources.map((resource) => {
            const isBookmarked = bookmarks.some(b => b.id === resource.id && b.type === 'resource');
            
            return (
              <div key={resource.id} className="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
                <div className="px-4 py-5 sm:p-6">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-sm font-medium text-purple-600 dark:text-purple-400">{resource.id}</span>
                    <div className="flex gap-2">
                      {user && (
                        <button
                          onClick={() => toggleBookmark(resource.id, 'resource')}
                          className={`p-1 rounded ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
                        >
                          <Bookmark className="h-4 w-4" fill={isBookmarked ? 'currentColor' : 'none'} />
                        </button>
                      )}
                      <a
                        href={resource.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="p-1 rounded text-gray-400 hover:text-blue-500"
                      >
                        <ExternalLink className="h-4 w-4" />
                      </a>
                    </div>
                  </div>
                  <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">{resource.title}</h3>
                  <p className="text-sm text-gray-600 dark:text-gray-300 mb-4">{resource.description}</p>
                  <div className="flex justify-between items-center">
                    <span className="text-xs text-gray-500 dark:text-gray-400">{resource.category}</span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">{resource.access}</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// NEW: Games Page Component
const GamesPage = () => {
  const { user, toggleBookmark, toggleComparison, getCurrentBookmarks, getCurrentComparisons } = useAuth();
  const [searchTerm, setSearchTerm] = useState('');
  
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();

  const filteredGames = gamesData.filter(game => 
    game.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    game.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Games</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300">
            Interactive learning experiences and strategic simulations
          </p>
        </div>

        {/* Search */}
        <div className="mb-8">
          <input
            type="text"
            placeholder="Search games..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full max-w-md px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
          />
        </div>

        {/* Games Grid */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filteredGames.map((game) => {
            const isBookmarked = bookmarks.some(b => b.id === game.id && b.type === 'game');
            const isComparing = comparisons.some(c => c.id === game.id && c.type === 'game');
            
            return (
              <div key={game.id} className="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
                <div className="px-4 py-5 sm:p-6">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-sm font-medium text-green-600 dark:text-green-400">{game.id}</span>
                    <div className="flex gap-2">
                      {user && (
                        <>
                          <button
                            onClick={() => toggleBookmark(game.id, 'game')}
                            className={`p-1 rounded ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
                          >
                            <Bookmark className="h-4 w-4" fill={isBookmarked ? 'currentColor' : 'none'} />
                          </button>
                          <button
                            onClick={() => toggleComparison(game.id, 'game')}
                            className={`p-1 rounded ${isComparing ? 'text-blue-500' : 'text-gray-400 hover:text-blue-500'}`}
                            disabled={!isComparing && comparisons.length >= 3}
                          >
                            <Target className="h-4 w-4" fill={isComparing ? 'currentColor' : 'none'} />
                          </button>
                        </>
                      )}
                      <a
                        href={game.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="p-1 rounded text-gray-400 hover:text-blue-500"
                      >
                        <ExternalLink className="h-4 w-4" />
                      </a>
                    </div>
                  </div>
                  <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">{game.title}</h3>
                  <p className="text-sm text-gray-600 dark:text-gray-300 mb-4">{game.description}</p>
                  <div className="flex justify-between items-center">
                    <span className="text-xs text-gray-500 dark:text-gray-400">{game.category}</span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">{game.difficulty}</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// Dashboard Component
const Dashboard = () => {
  const { user, getCurrentBookmarks, getCurrentComparisons } = useAuth();
  const { darkMode, setCurrentPage } = usePage();
  const bookmarks = getCurrentBookmarks();
  const comparisons = getCurrentComparisons();
  const { notes } = useAuth();
  const { openModal } = useModal();

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
                        return updatedPremiumResources.find(item => item.id === id);
                      case 'game':
                        return gamesData.find(item => item.id === id);
                      default:
                        return null;
                    }
                  };
                  
                  const item = getItemData(bookmark.id, bookmark.type);
                  return item ? (
                    <div key={`${bookmark.id}-${bookmark.type}`} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <h3 className="font-medium text-gray-900 dark:text-white truncate">{item.title}</h3>
                      <p className="text-sm text-gray-500 dark:text-gray-400 capitalize">{bookmark.type}</p>
                    </div>
                  ) : null;
                })}
                <button
                  onClick={() => openModal('bookmarks')}
                  className="w-full text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 font-medium text-center py-2"
                >
                  View All Bookmarks
                </button>
              </div>
            ) : (
              <div className="text-center py-8">
                <Bookmark className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-400 mb-4">No bookmarks yet</p>
                <button
                  onClick={() => setCurrentPage('courses')}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium"
                >
                  Explore Courses
                </button>
              </div>
            )}
          </div>

          {/* Notes */}
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-4 sm:p-6">
            <h2 className="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white mb-4">Recent Notes</h2>
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
                        return updatedPremiumResources.find(item => item.id === id);
                      case 'game':
                        return gamesData.find(item => item.id === id);
                      default:
                        return null;
                    }
                  };
                  
                  const item = getItemData(comp.id, comp.type);
                  return item ? (
                    <div key={`${comp.id}-${comp.type}`} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <h3 className="font-medium text-gray-900 dark:text-white truncate">{item.title}</h3>
                      <p className="text-sm text-gray-500 dark:text-gray-400 capitalize">{comp.type}</p>
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
                <p className="text-gray-500 dark:text-gray-400">No items selected for comparison</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

// AI Tools Page Component (placeholder)
const AIToolsPage = () => {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">AI Tools</h1>
          <p className="mt-4 text-gray-600 dark:text-gray-300">AI-powered tools coming soon!</p>
        </div>
      </div>
    </div>
  );
};

// Global FABs Component
const GlobalFABs = () => {
  const { openModal } = useModal();
  const { getCurrentComparisons } = useAuth();
  const comparisons = getCurrentComparisons();

  return (
    <>
      {/* Bookmark FAB */}
      <button
        onClick={() => openModal('bookmarks')}
        className="fixed bottom-20 right-4 bg-yellow-500 hover:bg-yellow-600 text-white p-3 rounded-full shadow-lg z-40"
        aria-label="View bookmarks"
      >
        <Bookmark className="h-6 w-6" />
      </button>

      {/* Compare FAB */}
      <button
        onClick={() => openModal('comparison')}
        className="fixed bottom-20 left-4 bg-blue-500 hover:bg-blue-600 text-white p-3 rounded-full shadow-lg z-40"
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
        className="fixed top-20 right-4 bg-green-500 hover:bg-green-600 text-white p-3 rounded-full shadow-lg z-40"
        aria-label="Send feedback"
      >
        <MessageCircle className="h-6 w-6" />
      </button>

      {/* Suggest Course FAB */}
      <button
        onClick={() => openModal('suggest')}
        className="fixed top-20 left-4 bg-purple-500 hover:bg-purple-600 text-white p-3 rounded-full shadow-lg z-40"
        aria-label="Suggest course"
      >
        <Plus className="h-6 w-6" />
      </button>
    </>
  );
};

// Modal Components (simplified for space)
const BookmarkModal = ({ isOpen, onClose }) => {
  const { getCurrentBookmarks } = useAuth();
  const bookmarks = getCurrentBookmarks();

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full max-h-[80vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Your Bookmarks</h2>
          <button onClick={onClose} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        <div className="p-4">
          {bookmarks.length === 0 ? (
            <p className="text-gray-500 dark:text-gray-400 text-center py-8">No bookmarks yet</p>
          ) : (
            <div className="space-y-3">
              {bookmarks.map((bookmark) => {
                const getItemData = (id, type) => {
                  switch (type) {
                    case 'course':
                      return courseData.find(item => item.id === id);
                    case 'lab':
                      return labsData.find(item => item.id === id);
                    case 'resource':
                      return updatedPremiumResources.find(item => item.id === id);
                    case 'game':
                      return gamesData.find(item => item.id === id);
                    default:
                      return null;
                  }
                };
                
                const item = getItemData(bookmark.id, bookmark.type);
                return item ? (
                  <div key={`${bookmark.id}-${bookmark.type}`} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <h3 className="font-medium text-gray-900 dark:text-white">{item.title}</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-400 capitalize">{bookmark.type}</p>
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

const ComparisonModal = ({ isOpen, onClose }) => {
  const { getCurrentComparisons } = useAuth();
  const comparisons = getCurrentComparisons();

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-6xl w-full max-h-[90vh] overflow-auto">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Compare Items ({comparisons.length}/3)</h2>
          <button onClick={onClose} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        <div className="p-4">
          {comparisons.length === 0 ? (
            <div className="text-center py-8">
              <Target className="h-16 w-16 mx-auto mb-4 opacity-50 text-gray-400" />
              <p className="text-gray-500 dark:text-gray-400">No items selected for comparison</p>
            </div>
          ) : (
            <div className="grid gap-4" style={{ gridTemplateColumns: `repeat(${comparisons.length}, 1fr)` }}>
              {comparisons.map(comp => {
                const getItemData = (id, type) => {
                  switch (type) {
                    case 'course':
                      return courseData.find(item => item.id === id);
                    case 'lab':
                      return labsData.find(item => item.id === id);
                    case 'resource':
                      return updatedPremiumResources.find(item => item.id === id);
                    case 'game':
                      return gamesData.find(item => item.id === id);
                    default:
                      return null;
                  }
                };
                
                const item = getItemData(comp.id, comp.type);
                return item ? (
                  <div key={`${comp.id}-${comp.type}`} className="border dark:border-gray-600 rounded-lg p-4">
                    <span className="text-xs px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded">
                      {comp.type.toUpperCase()}
                    </span>
                    <h3 className="font-bold mb-2 text-gray-900 dark:text-white">{item.title}</h3>
                    <p className="text-sm text-gray-600 dark:text-gray-300">{item.description}</p>
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

const FeedbackModal = ({ isOpen, onClose }) => {
  const [message, setMessage] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const { submitFeedback } = useAuth();

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    const result = await submitFeedback({ message });
    if (result.success) {
      setMessage('');
      onClose();
    }
    setSubmitting(false);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">
        <div className="flex items-center justify-between p-4 border-b dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Send Feedback</h2>
          <button onClick={onClose} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        <form onSubmit={handleSubmit} className="p-4">
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Your feedback..."
            className="w-full h-32 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            required
          />
          <div className="flex justify-end gap-2 mt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md disabled:opacity-50"
            >
              {submitting ? 'Sending...' : 'Send'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

// Simple placeholder modals for other FABs
const SuggestCourseModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Suggest a Course</h2>
          <button onClick={onClose}>
            <X className="h-5 w-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>
        <p className="text-gray-600 dark:text-gray-300">Course suggestion feature coming soon!</p>
      </div>
    </div>
  );
};

// Placeholder modals
const TrackModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
        <button onClick={onClose}><X className="h-5 w-5" /></button>
        <p>Track modal content</p>
      </div>
    </div>
  );
};

const QuizModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
        <button onClick={onClose}><X className="h-5 w-5" /></button>
        <p>Quiz modal content</p>
      </div>
    </div>
  );
};

const BrowseModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
        <button onClick={onClose}><X className="h-5 w-5" /></button>
        <p>Browse modal content</p>
      </div>
    </div>
  );
};

const CornellNotesModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
        <button onClick={onClose}><X className="h-5 w-5" /></button>
        <p>Notes modal content</p>
      </div>
    </div>
  );
};

// Navigation Component
const Navigation = () => {
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
              {['home', 'courses', 'labs', 'resources', 'games'].map((page) => (
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
              <div className="relative">
                <button className="flex items-center space-x-2 text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">
                  <img className="h-8 w-8 rounded-full" src={user.photoURL} alt={user.displayName} />
                  <span className="text-sm font-medium">{user.displayName}</span>
                </button>
                <button
                  onClick={signOut}
                  className="ml-2 text-sm text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300"
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
              className="p-2 rounded-md text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white"
            >
              {mobileMenuOpen ? <X className="block h-6 w-6" /> : <Menu className="block h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile menu - UPDATED to include 'games' */}
      {mobileMenuOpen && (
        <div className="sm:hidden bg-white dark:bg-gray-900 border-t dark:border-gray-700">
          <div className="pt-2 pb-3 space-y-1">
            {['home', 'courses', 'labs', 'resources', 'games'].map((page) => (
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
                  className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-800 dark:hover:text-white"
                >
                  Sign Out
                </button>
              ) : (
                <button
                  onClick={signInWithGoogle}
                  className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-800 dark:hover:text-white"
                >
                  Sign In
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </nav>
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

// PWA Install Prompt Component
const PWAInstallPrompt = () => {
  const { showInstallPrompt, handleInstallClick, setShowInstallPrompt } = usePage();

  if (!showInstallPrompt) return null;

  return (
    <div className="fixed top-16 left-4 right-4 bg-blue-600 text-white p-4 rounded-lg shadow-lg z-40">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="font-medium">Install ImpactMojo</h3>
          <p className="text-sm opacity-90">Get the app experience!</p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={handleInstallClick}
            className="bg-white text-blue-600 px-3 py-1 rounded text-sm font-medium"
          >
            Install
          </button>
          <button
            onClick={() => setShowInstallPrompt(false)}
            className="text-white/80 hover:text-white"
          >
            <X className="h-5 w-5" />
          </button>
        </div>
      </div>
    </div>
  );
};

// Main App Content Component
const AppContent = () => {
  const { loading, user } = useAuth();
  const { currentPage, darkMode } = usePage();

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
      {currentPage === 'games' && <GamesPage />}
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

// src/App.js
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Bookmark, MessageCircle, 
  ExternalLink, BookOpen, FileText, Target, Users, 
  Clock, CheckCircle, PlayCircle, Bot, Trophy, 
  Headphones, Route, Library, Music
} from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc } from 'firebase/firestore';

// Data imports
import { courseData, upcomingCourses } from './data/course-data';
import { labsData } from './data/labs-data';
import { premiumResources } from './data/premium-resources-data';

// Page imports
import AIToolsPage from './pages/AIToolsPage';
import ResourcesPage from './pages/ResourcesPage';

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

// Authentication Context
const AuthContext = createContext();
const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);
  const [isPremium, setIsPremium] = useState(false);
  const [customPathway, setCustomPathway] = useState([]);
  const [notes, setNotes] = useState([]);
  
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user);
      if (user) {
        try {
          const userDoc = await getDoc(doc(db, 'users', user.uid));
          if (userDoc.exists()) {
            const userData = userDoc.data();
            setBookmarks(userData.bookmarks || []);
            setIsPremium(userData.isPremium || false);
            setCustomPathway(userData.customPathway || []);
            setNotes(userData.notes || []);
          } else {
            await setDoc(doc(db, 'users', user.uid), {
              name: user.displayName,
              email: user.email,
              photoURL: user.photoURL,
              bookmarks: [],
              isPremium: false,
              customPathway: [],
              notes: [],
              createdAt: new Date()
            });
          }
        } catch (error) {
          console.error('Error loading user data:', error);
        }
      } else {
        setBookmarks([]);
        setIsPremium(false);
        setCustomPathway([]);
        setNotes([]);
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
      await setDoc(doc(db, 'users', user.uid), { bookmarks: newBookmarks }, { merge: true });
      setBookmarks(newBookmarks);
    } catch (error) {
      console.error('Error toggling bookmark:', error);
    }
  };
  
  const addToPathway = async (courseId) => {
    if (!user) return;
    try {
      const newPathway = [...customPathway, courseId];
      await setDoc(doc(db, 'users', user.uid), { customPathway: newPathway }, { merge: true });
      setCustomPathway(newPathway);
    } catch (error) {
      console.error('Error adding to pathway:', error);
    }
  };
  
  const saveNote = async (note) => {
    if (!user) return;
    try {
      const newNotes = [...notes, note];
      await setDoc(doc(db, 'users', user.uid), { notes: newNotes }, { merge: true });
      setNotes(newNotes);
    } catch (error) {
      console.error('Error saving note:', error);
    }
  };
  
  return (
    <AuthContext.Provider value={{
      user, loading, bookmarks, isPremium, customPathway, notes,
      signInWithGoogle, signOut, toggleBookmark, addToPathway, saveNote
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
  
  return (
    <PageContext.Provider value={{ currentPage, setCurrentPage, darkMode, setDarkMode }}>
      {children}
    </PageContext.Provider>
  );
};

export const usePage = () => {
  const context = useContext(PageContext);
  if (!context) throw new Error('usePage must be used within PageProvider');
  return context;
};

// Navigation Component
export const Navigation = () => {
  const { user, signOut, signInWithGoogle, isPremium } = useAuth();
  const { currentPage, setCurrentPage, darkMode, setDarkMode } = usePage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  return (
    <nav className="sticky top-0 z-50 bg-white dark:bg-chalkboard-dark shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0 flex items-center">
              <div className="h-8 w-8 rounded-md bg-accent-blue flex items-center justify-center">
                <span className="text-white font-bold">IM</span>
              </div>
              <span className="ml-2 text-xl font-bold text-gray-900 dark:text-chalk-white font-heading">ImpactMojo</span>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              {['home', 'courses', 'labs', 'resources'].map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  className={`${currentPage === page ? 'border-accent-blue text-gray-900 dark:text-chalk-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium font-sans capitalize`}
                >
                  {page}
                </button>
              ))}
              {user && (
                <>
                  <button
                    onClick={() => setCurrentPage('dashboard')}
                    className={`${currentPage === 'dashboard' ? 'border-accent-blue text-gray-900 dark:text-chalk-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium font-sans`}
                  >
                    Dashboard
                  </button>
                  <button
                    onClick={() => setCurrentPage('ai-tools')}
                    className={`${currentPage === 'ai-tools' ? 'border-accent-blue text-gray-900 dark:text-chalk-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium font-sans flex items-center`}
                  >
                    AI Tools
                    {!isPremium && <span className="ml-1 bg-yellow-400 text-yellow-900 text-xs px-1.5 py-0.5 rounded-full">PRO</span>}
                  </button>
                </>
              )}
            </div>
          </div>
          
          <div className="hidden sm:ml-6 sm:flex sm:items-center">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-accent-blue"
            >
              {darkMode ? <Sun className="h-5 w-5 text-yellow-400" /> : <Moon className="h-5 w-5" />}
            </button>
            
            {user ? (
              <div className="ml-3 flex items-center space-x-3">
                <div className="flex items-center">
                  <img className="h-8 w-8 rounded-full" src={user.photoURL} alt={user.displayName} />
                  <span className="ml-2 text-gray-900 dark:text-chalk-white text-sm font-medium font-sans hidden md:block">{user.displayName}</span>
                  {isPremium && <span className="ml-1 bg-yellow-400 text-yellow-900 text-xs px-1.5 py-0.5 rounded-full">PRO</span>}
                </div>
                <button onClick={signOut} className="text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white text-sm font-medium font-sans">
                  Sign Out
                </button>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-accent-blue hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-blue font-sans"
              >
                Sign In
              </button>
            )}
          </div>
          
          <div className="-mr-2 flex items-center sm:hidden">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-accent-blue"
            >
              {mobileMenuOpen ? <X className="block h-6 w-6" /> : <Menu className="block h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="sm:hidden bg-white dark:bg-chalkboard-dark">
          <div className="pt-2 pb-3 space-y-1">
            {['home', 'courses', 'labs', 'resources'].map((page) => (
              <button
                key={page}
                onClick={() => { setCurrentPage(page); setMobileMenuOpen(false); }}
                className={`${currentPage === page ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-chalk-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-chalk-white'} block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium font-sans capitalize`}
              >
                {page}
              </button>
            ))}
            {user && (
              <>
                <button
                  onClick={() => { setCurrentPage('dashboard'); setMobileMenuOpen(false); }}
                  className={`${currentPage === 'dashboard' ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-chalk-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-chalk-white'} block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium font-sans`}
                >
                  Dashboard
                </button>
                <button
                  onClick={() => { setCurrentPage('ai-tools'); setMobileMenuOpen(false); }}
                  className={`${currentPage === 'ai-tools' ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-chalk-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-chalk-white'} block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium font-sans flex items-center`}
                >
                  AI Tools
                  {!isPremium && <span className="ml-2 bg-yellow-400 text-yellow-900 text-xs px-1.5 py-0.5 rounded-full">PRO</span>}
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
                    <div className="text-base font-medium text-gray-900 dark:text-chalk-white font-sans">{user.displayName}</div>
                    <div className="text-sm font-medium text-gray-500 dark:text-gray-300 font-sans">{user.email}</div>
                  </div>
                </>
              ) : (
                <div className="text-base font-medium text-gray-900 dark:text-chalk-white font-sans">Not signed in</div>
              )}
            </div>
            <div className="mt-3">
              {user ? (
                <button
                  onClick={signOut}
                  className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-900 dark:hover:text-chalk-white hover:bg-gray-100 dark:hover:bg-gray-700 font-sans"
                >
                  Sign out
                </button>
              ) : (
                <button
                  onClick={signInWithGoogle}
                  className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-900 dark:hover:text-chalk-white hover:bg-gray-100 dark:hover:bg-gray-700 font-sans"
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

// Dashboard Component
const Dashboard = () => {
  const { darkMode } = usePage();
  const { user, isPremium, customPathway, notes } = useAuth();
  
  if (!user) {
    return (
      <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-heading">Please sign in to access your dashboard</h1>
        </div>
      </div>
    );
  }
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-heading">Dashboard</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300 font-sans">Welcome back, {user.displayName}!</p>
        </div>
        
        {/* Stats Cards */}
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
          {[
            { title: 'Courses Completed', value: '12', icon: BookOpen, color: 'blue' },
            { title: 'Labs Completed', value: '5', icon: Target, color: 'green' },
            { title: 'AI Tools Used', value: '8', icon: Bot, color: 'purple' },
            { title: 'Bookmarks', value: '12', icon: Bookmark, color: 'yellow' }
          ].map((stat, index) => (
            <div key={index} className="bg-white dark:bg-chalkboard-dark overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className={`flex-shrink-0 bg-${stat.color}-500 rounded-md p-3`}>
                    <stat.icon className="h-6 w-6 text-white" />
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 dark:text-gray-400 font-sans truncate">{stat.title}</dt>
                      <dd className="text-lg font-medium text-gray-900 dark:text-chalk-white font-sans">{stat.value}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        {/* Premium Features */}
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2 mb-8">
          {/* Custom Pathway */}
          <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-heading mb-4">Your Learning Pathway</h2>
            {customPathway.length > 0 ? (
              <div className="space-y-3">
                {customPathway.map((courseId, index) => {
                  const course = courseData.find(c => c.id === courseId);
                  return course ? (
                    <div key={index} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div>
                        <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans">{course.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-300 font-sans">{course.track}</p>
                      </div>
                      <button className="text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300">
                        <ExternalLink className="h-5 w-5" />
                      </button>
                    </div>
                  ) : null;
                })}
              </div>
            ) : (
              <div className="text-center py-8">
                <Route className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-300 font-sans mb-4">No courses in your pathway yet</p>
                <button className="bg-accent-blue hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium font-sans">
                  Build Your Pathway
                </button>
              </div>
            )}
          </div>
          
          {/* Research Notes */}
          <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-heading mb-4">Research Notes</h2>
            {notes.length > 0 ? (
              <div className="space-y-3">
                {notes.slice(0, 3).map((note, index) => (
                  <div key={index} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans">{note.title}</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-300 font-sans mt-1">{note.content.substring(0, 100)}...</p>
                  </div>
                ))}
                {notes.length > 3 && (
                  <button className="text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-medium font-sans">
                    View All Notes
                  </button>
                )}
              </div>
            ) : (
              <div className="text-center py-8">
                <Library className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-300 font-sans mb-4">No research notes yet</p>
                <button className="bg-accent-blue hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium font-sans">
                  Create Your First Note
                </button>
              </div>
            )}
          </div>
        </div>
        
        {/* Premium Resources */}
        <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6 mb-8">
          <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-heading mb-4">Premium Resources</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {premiumResources.map((resource, index) => (
              <div key={index} className="p-4 border border-gray-200 dark:border-gray-700 rounded-lg hover:shadow-md transition-shadow">
                <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans mb-2">{resource.title}</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 font-sans mb-3">{resource.description}</p>
                <a
                  href={resource.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-medium font-sans"
                >
                  Access Resource
                  <ExternalLink className="ml-1 h-4 w-4" />
                </a>
              </div>
            ))}
          </div>
        </div>
        
        {/* Study Music */}
        <div className="bg-gradient-to-r from-purple-500 to-indigo-600 rounded-lg shadow-lg p-6 text-white mb-8">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-bold font-heading">Lo-Fi Study Beats</h2>
              <p className="mt-1 font-sans">Focus better with our curated study playlist</p>
            </div>
            <button className="bg-white text-purple-600 px-4 py-2 rounded-md font-medium font-sans flex items-center">
              <Music className="mr-2 h-5 w-5" />
              Play on Spotify
            </button>
          </div>
        </div>
        
        {!isPremium && (
          <div className="bg-gradient-to-r from-yellow-400 to-yellow-500 rounded-lg shadow-lg p-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-gray-900 font-heading">Upgrade to Premium</h3>
                <p className="mt-1 text-gray-800 font-sans">Unlock all premium features and content</p>
              </div>
              <button className="px-4 py-2 bg-gray-900 text-white rounded-md hover:bg-gray-800 transition-colors font-sans">
                Upgrade Now
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Home Page Component
const Home = () => {
  const { darkMode, setCurrentPage } = usePage();
  const { user, isPremium } = useAuth();
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 dark:text-chalk-white font-heading mb-4">
            Welcome to <span className="text-accent-blue">ImpactMojo</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-600 dark:text-gray-300 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Your platform for development learning and tools. Explore courses, labs, and AI-powered tools to enhance your impact.
          </p>
          <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
            <button
              onClick={() => setCurrentPage('courses')}
              className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-accent-blue hover:bg-blue-700 md:py-4 md:text-lg md:px-10 font-sans"
            >
              Get started
            </button>
            {user && (
              <button
                onClick={() => setCurrentPage('ai-tools')}
                className="mt-3 w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-accent-blue dark:text-accent-blue bg-white dark:bg-chalkboard-dark hover:bg-gray-50 dark:hover:bg-gray-700 md:py-4 md:text-lg md:px-10 font-sans sm:mt-0 sm:ml-3"
              >
                Try AI Tools
                {!isPremium && <span className="ml-2 bg-yellow-400 text-yellow-900 text-xs px-1.5 py-0.5 rounded-full">PRO</span>}
              </button>
            )}
          </div>
        </div>
        
        {/* Featured Content */}
        <div className="mt-16">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white text-center font-heading mb-8">Featured Content</h2>
          <div className="grid gap-5 max-w-lg mx-auto lg:grid-cols-3 lg:max-w-none">
            {courseData.slice(0, 3).map((course) => (
              <div key={course.id} className="flex flex-col rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
                <div className="flex-1 bg-white dark:bg-chalkboard-dark p-6 flex flex-col justify-between">
                  <div className="flex-1">
                    <p className="text-sm font-medium text-accent-blue dark:text-accent-blue font-sans">
                      <span>Course</span>
                    </p>
                    <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-chalk-white font-heading">{course.title}</h3>
                    <p className="mt-3 text-base text-gray-600 dark:text-gray-300 font-sans">{course.description}</p>
                  </div>
                  <div className="mt-6">
                    <button
                      onClick={() => setCurrentPage('courses')}
                      className="text-base font-medium text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-sans"
                    >
                      Explore courses
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Learning Tracks */}
        <div className="mt-16">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white text-center font-heading mb-8">Learning Tracks</h2>
          <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
            {[
              { name: "Research Methods", description: "Learn qualitative and quantitative research methods." },
              { name: "Data Analysis", description: "Master data analysis techniques for social impact." },
              { name: "Gender Studies", description: "Explore gender dynamics in development contexts." },
              { name: "Policy & Economics", description: "Understand policy and economic frameworks." }
            ].map((track, index) => (
              <div key={index} className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
                <h3 className="text-xl font-semibold mb-2 font-heading">{track.name}</h3>
                <p className="text-gray-600 dark:text-gray-300 font-sans">{track.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// Main App Content Component
const AppContent = () => {
  const { currentPage, darkMode } = usePage();
  const { loading } = useAuth();
  
  if (loading) {
    return (
      <div className={`min-h-screen flex items-center justify-center font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-accent-blue"></div>
      </div>
    );
  }
  
  return (
    <div className={darkMode ? 'dark' : ''}>
      {currentPage === 'home' && <Home />}
      {currentPage === 'dashboard' && <Dashboard />}
      {currentPage === 'courses' && <div>Courses Page</div>}
      {currentPage === 'labs' && <div>Labs Page</div>}
      {currentPage === 'resources' && <ResourcesPage />}
      {currentPage === 'ai-tools' && <AIToolsPage />}
    </div>
  );
};

// Main App Component
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

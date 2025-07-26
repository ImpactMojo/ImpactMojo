import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  BookOpen, 
  User, 
  Home, 
  Beaker, 
  FileText, 
  Info, 
  Mail, 
  Sun, 
  Moon, 
  LogOut, 
  Menu, 
  X,
  Bookmark,
  Plus,
  MessageCircle,
  BookmarkIcon,
  Star
} from 'lucide-react';

// Mock auth system for development
const mockAuth = {
  signInWithPopup: () => Promise.resolve({
    user: {
      uid: 'test-user-123',
      displayName: 'Test User',
      email: 'test@example.com',
      photoURL: 'https://via.placeholder.com/40'
    }
  }),
  signOut: () => Promise.resolve()
};

// Course data
const courseData = {
  courses: [
    {
      id: "C1",
      title: "Gender Studies 101", 
      track: "Gender Studies",
      description: "Introduction to gender theory and its practical implications",
      quote: "Eye-opening exploration of gender norms",
      level: "Beginner",
      duration: "2 hours"
    },
    {
      id: "C2",
      title: "Research Methods Fundamentals",
      track: "Research Methods", 
      description: "Learn systematic approaches to data collection and analysis",
      quote: "Essential foundation for any researcher",
      level: "Beginner",
      duration: "3 hours"
    },
    {
      id: "C3",
      title: "Policy Analysis Framework",
      track: "Policy & Economics",
      description: "Understanding policy frameworks and economic principles",
      quote: "Practical tools for policy evaluation",
      level: "Intermediate", 
      duration: "4 hours"
    }
  ],
  labs: [
    {
      id: "L1",
      title: "Climate Timeline", 
      topic: "Climate",
      description: "Interactive timeline of climate resilience efforts",
      icon: "🌍",
      content: "https://impactrisk-mitigation.netlify.app/"
    },
    {
      id: "L2", 
      title: "Gender Timeline",
      topic: "Gender",
      description: "Historical progression of gender equality movements",
      icon: "⚖️",
      content: "https://community-engagement.netlify.app/"
    },
    {
      id: "L3",
      title: "Policy Timeline", 
      topic: "Policy",
      description: "Evolution of key policy frameworks",
      icon: "📋",
      content: "https://pol-advocacy4impact.netlify.app/"
    }
  ],
  tracks: [
    {
      name: "Research Methods",
      description: "Learn systematic approaches to research and data collection",
      icon: "🔬",
      color: "bg-blue-500"
    },
    {
      name: "Data Analysis", 
      description: "Master tools and techniques for analyzing complex data",
      icon: "📊",
      color: "bg-green-500"
    },
    {
      name: "Gender Studies",
      description: "Explore gender theory and its real-world applications", 
      icon: "⚖️",
      color: "bg-purple-500"
    },
    {
      name: "Policy & Economics",
      description: "Understand policy frameworks and economic principles",
      icon: "🏛️", 
      color: "bg-orange-500"
    }
  ],
  resources: [
    {
      id: "R1",
      title: "Development Jargon Buster",
      type: "PDF",
      description: "Glossary of development terms and acronyms",
      link: "/assets/resources/jargon-buster.pdf"
    },
    {
      id: "R2",
      title: "Research Toolkit",
      type: "PDF", 
      description: "Essential tools and templates for researchers",
      link: "/assets/resources/research-toolkit.pdf"
    }
  ]
};

// Context providers
const AuthContext = createContext();
const ThemeContext = createContext();

const useAuth = () => useContext(AuthContext);
const useTheme = () => useContext(ThemeContext);

// Main App Component
function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [darkMode, setDarkMode] = useState(() => {
    // Check localStorage first, fallback to system preference
    const saved = localStorage.getItem('darkMode');
    if (saved !== null) {
      return JSON.parse(saved);
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  });
  const [currentPage, setCurrentPage] = useState('home');
  const [showCookieConsent, setShowCookieConsent] = useState(false);
  const [showTour, setShowTour] = useState(false);
  const [bookmarks, setBookmarks] = useState([]);
  const [compareList, setCompareList] = useState([]);

  // Initialize app
  useEffect(() => {
    const cookieConsent = localStorage.getItem('cookieConsent');
    const tourCompleted = localStorage.getItem('tourCompleted');
    
    if (!cookieConsent) {
      setShowCookieConsent(true);
    }
    
    if (!tourCompleted) {
      setShowTour(true);
    }
    
    setLoading(false);
  }, []);

  // Apply dark mode to document
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
  }, [darkMode]);

  // Theme toggle
  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  // Auth functions
  const signInWithGoogle = async () => {
    try {
      const result = await mockAuth.signInWithPopup();
      setUser(result.user);
    } catch (error) {
      console.error('Error signing in:', error);
    }
  };

  const handleSignOut = async () => {
    try {
      await mockAuth.signOut();
      setUser(null);
      setBookmarks([]);
      setCompareList([]);
    } catch (error) {
      console.error('Error signing out:', error);
    }
  };

  // Bookmark functions
  const toggleBookmark = async (itemId) => {
    if (!user) {
      alert('Please log in to bookmark items');
      return;
    }

    const updatedBookmarks = bookmarks.includes(itemId)
      ? bookmarks.filter(id => id !== itemId)
      : [...bookmarks, itemId];

    setBookmarks(updatedBookmarks);
  };

  // Compare functions  
  const toggleCompare = async (itemId) => {
    if (!user) {
      alert('Please log in to compare items');
      return;
    }

    const updatedCompareList = compareList.includes(itemId)
      ? compareList.filter(id => id !== itemId)
      : [...compareList, itemId];

    setCompareList(updatedCompareList);
  };

  const authContextValue = {
    user,
    setUser,
    signInWithGoogle,
    handleSignOut,
    currentPage,
    setCurrentPage,
    bookmarks,
    toggleBookmark,
    compareList,
    toggleCompare
  };

  const themeContextValue = {
    darkMode,
    toggleTheme
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600 dark:text-gray-400">Loading ImpactMojo...</p>
        </div>
      </div>
    );
  }

  return (
    <AuthContext.Provider value={authContextValue}>
      <ThemeContext.Provider value={themeContextValue}>
        <div className={`app ${darkMode ? 'dark' : ''}`}>
          <div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 min-h-screen">
            <Navbar />
            <MainContent />
            <FloatingActionButtons />
            <Footer />
            
            {showCookieConsent && (
              <CookieConsent onAccept={() => {
                localStorage.setItem('cookieConsent', 'true');
                setShowCookieConsent(false);
              }} />
            )}
            
            {showTour && (
              <InteractiveTour onComplete={() => {
                localStorage.setItem('tourCompleted', 'true');
                setShowTour(false);
              }} />
            )}
          </div>
        </div>
      </ThemeContext.Provider>
    </AuthContext.Provider>
  );
}

// Navbar Component
function Navbar() {
  const { user, currentPage, setCurrentPage, handleSignOut } = useAuth();
  const { darkMode, toggleTheme } = useTheme();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems = [
    { id: 'home', label: 'Home', icon: Home },
    { id: 'courses', label: 'Courses', icon: BookOpen },
    { id: 'labs', label: 'Labs', icon: Beaker },
    { id: 'resources', label: 'Resources', icon: FileText },
    { id: 'about', label: 'About', icon: Info },
    { id: 'contact', label: 'Contact', icon: Mail }
  ];

  if (user) {
    navItems.splice(1, 0, { id: 'dashboard', label: 'Dashboard', icon: User });
  }

  return (
    <nav className="sticky top-0 z-50 bg-white dark:bg-gray-800 shadow-lg transition-colors duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <button
              onClick={() => setCurrentPage('home')}
              className="text-xl font-bold text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors"
            >
              ImpactMojo
            </button>
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-4">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => setCurrentPage(item.id)}
                className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                  currentPage === item.id
                    ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                    : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
                }`}
              >
                <item.icon className="inline-block w-4 h-4 mr-1" />
                {item.label}
              </button>
            ))}
          </div>

          {/* Right side controls */}
          <div className="flex items-center space-x-4">
            <button
              onClick={toggleTheme}
              className="p-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              aria-label="Toggle theme"
            >
              {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
            </button>

            {user ? (
              <div className="relative group">
                <button className="flex items-center space-x-2 p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
                  <img
                    src={user.photoURL}
                    alt={user.displayName}
                    className="w-8 h-8 rounded-full"
                  />
                  <span className="hidden sm:block text-sm">{user.displayName?.split(' ')[0]}</span>
                </button>
                <div className="absolute right-0 mt-1 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all">
                  <button
                    onClick={() => setCurrentPage('dashboard')}
                    className="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                  >
                    <User className="inline-block w-4 h-4 mr-2" />
                    Dashboard
                  </button>
                  <button
                    onClick={handleSignOut}
                    className="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                  >
                    <LogOut className="inline-block w-4 h-4 mr-2" />
                    Logout
                  </button>
                </div>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors"
              >

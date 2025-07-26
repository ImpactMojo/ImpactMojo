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
  const { user, currentPage, setCurrentPage, handleSignOut, signInWithGoogle } = useAuth();
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
                Login
              </button>
            )}

            {/* Mobile menu button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-md text-gray-700 dark:text-gray-300"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-200 dark:border-gray-700">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => {
                  setCurrentPage(item.id);
                  setMobileMenuOpen(false);
                }}
                className={`block w-full text-left px-4 py-2 text-sm font-medium transition-colors ${
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
        )}
      </div>
    </nav>
  );
}

// Main Content Component
function MainContent() {
  const { currentPage } = useAuth();

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage />;
      case 'dashboard':
        return <DashboardPage />;
      case 'courses':
        return <CoursesPage />;
      case 'labs':
        return <LabsPage />;
      case 'resources':
        return <ResourcesPage />;
      case 'about':
        return <AboutPage />;
      case 'contact':
        return <ContactPage />;
      default:
        return <HomePage />;
    }
  };

  return (
    <main className="flex-1">
      {renderPage()}
    </main>
  );
}

// Page Components
function HomePage() {
  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100 sm:text-5xl md:text-6xl">
            <span className="block">101 Knowledge Series</span>
            <span className="block text-blue-600 dark:text-blue-400">for Social Impact</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-500 dark:text-gray-400 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            A curated library of knowledge decks exploring justice, equity, and development in South Asia.
          </p>
        </div>

        {/* Featured Courses */}
        <div className="mt-16">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-8">Featured Courses</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {courseData.courses.slice(0, 3).map((course) => (
              <CourseCard key={course.id} course={course} />
            ))}
          </div>
        </div>

        {/* Learning Tracks */}
        <div className="mt-16">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-8">Learning Tracks</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {courseData.tracks.map((track) => (
              <TrackCard key={track.name} track={track} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function DashboardPage() {
  const { user, bookmarks } = useAuth();
  
  if (!user) {
    return (
      <div className="py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100">Please log in to view your dashboard</h1>
        </div>
      </div>
    );
  }

  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">Welcome back, {user.displayName?.split(' ')[0]}!</h1>
        
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold mb-4">Your Progress</h2>
              <p className="text-gray-600 dark:text-gray-400">Track your learning journey and achievements.</p>
            </div>
          </div>
          
          <div>
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold mb-4">Bookmarked Items</h2>
              <p className="text-gray-600 dark:text-gray-400">{bookmarks.length} items saved</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function CoursesPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('');

  const filteredCourses = courseData.courses.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         course.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTrack = selectedTrack === '' || course.track === selectedTrack;
    return matchesSearch && matchesTrack;
  });

  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">Courses</h1>
        
        {/* Search and Filter */}
        <div className="mb-8 flex flex-col sm:flex-row gap-4">
          <input
            type="text"
            placeholder="Search courses..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="flex-1 px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          />
          <select
            value={selectedTrack}
            onChange={(e) => setSelectedTrack(e.target.value)}
            className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          >
            <option value="">All Tracks</option>
            {courseData.tracks.map(track => (
              <option key={track.name} value={track.name}>{track.name}</option>
            ))}
          </select>
        </div>

        {/* Courses Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCourses.map((course) => (
            <CourseCard key={course.id} course={course} />
          ))}
        </div>

        {filteredCourses.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500 dark:text-gray-400">No courses found matching your criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
}

function LabsPage() {
  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">Interactive Labs</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {courseData.labs.map((lab) => (
            <LabCard key={lab.id} lab={lab} />
          ))}
        </div>
      </div>
    </div>
  );
}

function ResourcesPage() {
  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">Resources</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {courseData.resources.map((resource) => (
            <ResourceCard key={resource.id} resource={resource} />
          ))}
        </div>
      </div>
    </div>
  );
}

function AboutPage() {
  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">About ImpactMojo</h1>
        
        <div className="prose prose-lg dark:prose-invert max-w-none">
          <p>
            ImpactMojo is a 101 Knowledge Series for Social Impact – a curated library of knowledge decks
            exploring justice, equity, and development in South Asia.
          </p>
          
          <p>
            Our mission is to democratize access to development education and provide practical tools
            for creating positive social impact.
          </p>
        </div>
      </div>
    </div>
  );
}

function ContactPage() {
  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">Contact Us</h1>
        
        <div className="max-w-2xl">
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            Have questions or feedback? We'd love to hear from you.
          </p>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
            <form className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                  Name
                </label>
                <input
                  type="text"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                  Email
                </label>
                <input
                  type="email"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                  Message
                </label>
                <textarea
                  rows={4}
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
                ></textarea>
              </div>
              
              <button
                type="submit"
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors"
              >
                Send Message
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

// Card Components
function CourseCard({ course }) {
  const { toggleBookmark, bookmarks, user } = useAuth();
  const isBookmarked = bookmarks.includes(course.id);

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="p-6">
        <div className="flex justify-between items-start mb-2">
          <span className="inline-block px-2 py-1 text-xs font-semibold bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded">
            {course.track}
          </span>
          {user && (
            <button
              onClick={() => toggleBookmark(course.id)}
              className={`p-1 rounded ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
            >
              <Bookmark className="w-4 h-4" />
            </button>
          )}
        </div>
        
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
          {course.title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-400 text-sm mb-3">
          {course.description}
        </p>
        
        {course.quote && (
          <p className="text-gray-500 dark:text-gray-500 text-sm italic mb-3">
            "{course.quote}"
          </p>
        )}
        
        <div className="flex justify-between items-center text-sm text-gray-500 dark:text-gray-400">
          <span>{course.level}</span>
          <span>{course.duration}</span>
        </div>
      </div>
    </div>
  );
}

function TrackCard({ track }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <div className={`w-12 h-12 ${track.color} rounded-lg flex items-center justify-center mb-4`}>
        <span className="text-2xl">{track.icon}</span>
      </div>
      
      <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
        {track.name}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-400 text-sm">
        {track.description}
      </p>
    </div>
  );
}

function LabCard({ lab }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="p-6">
        <div className="flex items-center mb-3">
          <span className="text-2xl mr-3">{lab.icon}</span>
          <span className="inline-block px-2 py-1 text-xs font-semibold bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 rounded">
            {lab.topic}
          </span>
        </div>
        
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
          {lab.title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-400 text-sm mb-4">
          {lab.description}
        </p>
        
        
          href={lab.content}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-block bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm transition-colors"
        >
          Explore Lab
        </a>
      </div>
    </div>
  );
}

function ResourceCard({ resource }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start mb-2">
        <span className="inline-block px-2 py-1 text-xs font-semibold bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 rounded">
          {resource.type}
        </span>
      </div>
      
      <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
        {resource.title}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-400 text-sm mb-4">
        {resource.description}
      </p>
      
      
        href={resource.link}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-block bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm transition-colors"
      >
        Download Resource
      </a>
    </div>
  );
}

// Floating Action Buttons
function FloatingActionButtons() {
  const { user } = useAuth();

  if (!user) return null;

  return (
    <div className="fixed bottom-4 right-4 flex flex-col space-y-2">
      <button className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-full shadow-lg transition-colors">
        <MessageCircle className="w-5 h-5" />
      </button>
      
      <button className="bg-green-600 hover:bg-green-700 text-white p-3 rounded-full shadow-lg transition-colors">
        <Plus className="w-5 h-5" />
      </button>
    </div>
  );
}

// Cookie Consent Component
function CookieConsent({ onAccept }) {
  return (
    <div className="fixed bottom-0 left-0 right-0 bg-gray-900 text-white p-4 z-50">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between">
        <p className="text-sm mb-4 sm:mb-0">
          We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.
        </p>
        <button
          onClick={onAccept}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm transition-colors"
        >
          Accept
        </button>
      </div>
    </div>
  );
}

// Interactive Tour Component
function InteractiveTour({ onComplete }) {
  const [step, setStep] = useState(0);
  
  const tourSteps = [
    {
      title: "Welcome to ImpactMojo!",
      description: "Let's take a quick tour of the features available to you.",
      target: null
    },
    {
      title: "Navigation",
      description: "Use the navigation bar to explore courses, labs, and resources.",
      target: "nav"
    },
    {
      title: "Dark Mode",
      description: "Toggle between light and dark themes using this button.",
      target: "theme-toggle"
    },
    {
      title: "Ready to Start!",
      description: "You're all set! Start exploring our knowledge series.",
      target: null
    }
  ];

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center">
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md mx-4">
        <div className="mb-4">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">
            {tourSteps[step].title}
          </h3>
          <p className="text-gray-600 dark:text-gray-400 mt-2">
            {tourSteps[step].description}
          </p>
        </div>
        
        <div className="flex justify-between items-center">
          <div className="flex space-x-2">
            {tourSteps.map((_, index) => (
              <div
                key={index}
                className={`w-2 h-2 rounded-full ${
                  index === step
                    ? 'bg-blue-600'
                    : 'bg-gray-300 dark:bg-gray-600'
                }`}
              />
            ))}
          </div>
          
          <div className="space-x-3">
            <button
              onClick={onComplete}
              className="px-4 py-2 text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200 transition-colors"
            >
              Skip
            </button>
            {step < tourSteps.length - 1 ? (
              <button
                onClick={() => setStep(step + 1)}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
              >
                Next
              </button>
            ) : (
              <button
                onClick={onComplete}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
              >
                Get Started
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function Footer() {
  return (
    <footer className="bg-gray-800 text-white py-8 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <p className="text-sm text-gray-300 mb-2">
            © 2025 ImpactMojo. No endorsements or certificates provided.
          </p>
          <p className="text-sm text-gray-300">
            Open-source project under MIT license. Built to democratize development education.
          </p>
        </div>
      </div>
    </footer>
  );
}

export default App;

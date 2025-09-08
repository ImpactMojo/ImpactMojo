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
  Award, Puzzle, Zap, Send, Lightbulb, Heart, ExternalLinkIcon,
  Linkedin, Twitter, Globe
} from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc, updateDoc, collection, addDoc } from 'firebase/firestore';

// Create Contexts
export const AuthContext = createContext();
export const PageContext = createContext();

// Custom Hooks  
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const usePage = () => {
  const context = useContext(PageContext);
  if (!context) {
    throw new Error('usePage must be used within a PageProvider');
  }
  return context;
};

// Data imports
import { courseData, upcomingCourses } from './data/course-data';
import { labsData } from './data/labs-data';
import { premiumResources } from './data/premium-resources-data';
import { aiToolsData } from './data/ai-tools-data';

// Component imports
import { FloatingActionButtons } from './components/floating-action-buttons';
import { 
  FeaturedContentSection, 
  TestimonialsSection, 
  PopularCoursesSection 
} from './components/homepage-components';
import { LearningTracksSection } from './components/learning-tracks-component';

// Page imports
import AboutPage from './pages/AboutPage';
import FAQPage from './pages/FAQPage';

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

// CORRECTED Four Original Learning Tracks
const fourOriginalTracks = {
  "Research Methods": {
    description: "Master qualitative and quantitative research approaches",
    courses: ["research-ethics-101", "qualitative-research-methods-101", "visual-ethnography-101"],
    color: "blue",
    icon: "🔬"
  },
  "Data Analysis": {
    description: "Develop skills in data collection, analysis, and visualization", 
    courses: ["data-literacy-101", "econometrics-101", "bivariate-analysis-101", "multivariate-analysis-101"],
    color: "green",
    icon: "📊"
  },
  "Gender Studies": {
    description: "Understand gender dynamics and women's empowerment",
    courses: ["gender-studies-101", "womens-economic-empowerment-101", "care-economy-101"],
    color: "purple",
    icon: "⚖️"
  },
  "Policy & Economics": {
    description: "Explore policy frameworks and economic development",
    courses: ["development-economics-101", "political-economy-101", "law-and-constitution-101", "global-development-architecture-101"],
    color: "orange",
    icon: "🏛️"
  }
};

// Live Learner Count Generator
const generateLiveLearnerCounts = () => {
  const totalLearners = 4200 + Math.floor(Math.random() * 300); // 4200-4500
  const courseCounts = courseData.map(course => ({
    id: course.id,
    count: 100 + Math.floor(Math.random() * 2400) // 100-2500 range
  }));
  
  return {
    total: totalLearners,
    courses: courseCounts
  };
};

// Context for global state
const PageContext = createContext();
const AuthContext = createContext();

// Custom hooks
const usePage = () => useContext(PageContext);
const useAuth = () => useContext(AuthContext);

// Live Stats Component
const LiveStatsSection = () => {
  const { darkMode } = usePage();
  const [stats, setStats] = useState(generateLiveLearnerCounts());

  useEffect(() => {
    const interval = setInterval(() => {
      setStats(generateLiveLearnerCounts());
    }, 30000); // Update every 30 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Join {stats.total.toLocaleString()}+ Learners Worldwide
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            {Object.entries(fourOriginalTracks).map(([track, data], index) => (
              <div key={track} className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-lg">
                <div className="text-2xl mb-2">{data.icon}</div>
                <h3 className="font-semibold text-gray-900 dark:text-white">{track}</h3>
                <p className="text-sm text-gray-600 dark:text-gray-300 mb-2">{data.description}</p>
                <div className="text-lg font-bold text-blue-600 dark:text-blue-400">
                  {(800 + Math.floor(Math.random() * 1200)).toLocaleString()}+ active
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// About Me Section Component
const AboutMeSection = () => {
  const { darkMode } = usePage();

  const socialLinks = [
    { name: 'LinkedIn', url: 'https://linkedin.com/in/varna/', icon: Linkedin },
    { name: 'Twitter/X', url: 'https://x.com/varna', icon: Twitter },
    { name: 'Threads', url: 'https://www.threads.com/@varnasriraman', icon: MessageCircle },
    { name: 'Notion', url: 'https://vfolio.notion.site/', icon: Globe }
  ];

  return (
    <div className="py-16 bg-white dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
            About the Creator
          </h2>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
            {/* Photo */}
            <div className="text-center">
              <img 
                src="/assets/varna-photo.jpg"
                alt="Dr. Varna Sri Raman"
                className="w-48 h-48 rounded-full mx-auto mb-4 object-cover shadow-lg"
                onError={(e) => {
                  e.target.src = "/assets/android-chrome-192x192.png";
                }}
              />
              <div className="flex justify-center space-x-4">
                {socialLinks.map((link) => (
                  <a
                    key={link.name}
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-600 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                    aria-label={link.name}
                  >
                    <link.icon size={24} />
                  </a>
                ))}
              </div>
            </div>
            
            {/* Bio */}
            <div className="md:col-span-2">
              <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Dr. Varna Sri Raman
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-6 leading-relaxed">
                Development economist, educator, and social researcher specializing in justice, equity, and development in South Asia. 
                ImpactMojo is built to democratize access to development knowledge through curated, contextual learning resources.
              </p>
              <p className="text-gray-600 dark:text-gray-300 mb-6 leading-relaxed">
                With a PhD in Development Economics and years of field experience, I created ImpactMojo as an open-source project 
                to make high-quality development education accessible to practitioners, researchers, and changemakers across the region.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button
                  onClick={() => window.location.href = '#faq'}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
                >
                  Read FAQ
                </button>
                <button
                  onClick={() => window.location.href = '#about'}
                  className="border border-blue-600 text-blue-600 hover:bg-blue-50 dark:hover:bg-blue-900/20 px-6 py-3 rounded-lg font-medium transition-colors"
                >
                  Learn More
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Improved Floating Action Buttons - positioned at bottom right elegantly
const ImprovedFloatingActionButtons = () => {
  const { darkMode } = usePage();
  const [isExpanded, setIsExpanded] = useState(false);
  
  const buttons = [
    { icon: MessageCircle, label: 'Feedback', action: 'feedback' },
    { icon: BookmarkIcon, label: 'Bookmarks', action: 'bookmarks' },
    { icon: Headphones, label: 'Focus Music', action: 'music' },
    { icon: Lightbulb, label: 'Quick Quiz', action: 'quiz' }
  ];

  return (
    <div className="fixed bottom-6 right-6 z-40">
      <div className="flex flex-col-reverse items-end space-y-reverse space-y-3">
        {/* Individual action buttons */}
        {isExpanded && buttons.map((button, index) => (
          <button
            key={button.action}
            className={`flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-3 rounded-full shadow-lg transition-all duration-200 transform ${
              isExpanded ? 'translate-x-0 opacity-100' : 'translate-x-full opacity-0'
            }`}
            style={{ transitionDelay: `${index * 50}ms` }}
          >
            <button.icon size={20} />
            <span className="text-sm whitespace-nowrap">{button.label}</span>
          </button>
        ))}
        
        {/* Main toggle button */}
        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="bg-blue-600 hover:bg-blue-700 text-white p-4 rounded-full shadow-lg transition-all duration-200"
        >
          {isExpanded ? <X size={24} /> : <Plus size={24} />}
        </button>
      </div>
    </div>
  );
};

// Cornell Notes Editor Component
const CornellNotesEditor = ({ note, onSave, onCancel }) => {
  const [title, setTitle] = useState(note?.title || '');
  const [cues, setCues] = useState(note?.cues || '');
  const [notes, setNotes] = useState(note?.notes || '');
  const [summary, setSummary] = useState(note?.summary || '');
  const [tags, setTags] = useState(note?.tags || []);
  const [newTag, setNewTag] = useState('');
  const { darkMode } = usePage();

  const handleSave = () => {
    if (!title.trim()) {
      alert('Please enter a title for your note');
      return;
    }
    
    onSave({
      title: title.trim(),
      cues: cues.trim(),
      notes: notes.trim(),
      summary: summary.trim(),
      tags,
      createdAt: note?.createdAt || new Date().toISOString(),
      updatedAt: new Date().toISOString()
    });
  };

  const addTag = () => {
    if (newTag.trim() && !tags.includes(newTag.trim())) {
      setTags([...tags, newTag.trim()]);
      setNewTag('');
    }
  };

  const removeTag = (tagToRemove) => {
    setTags(tags.filter(tag => tag !== tagToRemove));
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className={`${darkMode ? 'bg-gray-800 text-white' : 'bg-white text-gray-900'} rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto`}>
        <div className="p-6">
          <h2 className="text-2xl font-bold mb-4">Cornell Notes</h2>
          
          {/* Title */}
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter note title..."
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700"
            />
          </div>

          {/* Tags */}
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">Tags</label>
            <div className="flex flex-wrap gap-2 mb-2">
              {tags.map((tag, index) => (
                <span key={index} className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded-md text-sm flex items-center">
                  {tag}
                  <button onClick={() => removeTag(tag)} className="ml-2 text-red-500 hover:text-red-700">
                    <X size={14} />
                  </button>
                </span>
              ))}
            </div>
            <div className="flex gap-2">
              <input
                type="text"
                value={newTag}
                onChange={(e) => setNewTag(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && addTag()}
                placeholder="Add tag..."
                className="flex-1 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700"
              />
              <button onClick={addTag} className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
                <Tag size={16} />
              </button>
            </div>
          </div>

          {/* Cornell Notes Layout */}
          <div className="border border-gray-300 dark:border-gray-600 rounded-lg overflow-hidden mb-4" style={{height: '400px'}}>
            <div className="flex h-3/4">
              {/* Cues Column */}
              <div className="w-1/3 border-r border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-800">
                <div className="p-3 bg-gray-100 dark:bg-gray-700 border-b border-gray-300 dark:border-gray-600">
                  <h3 className="font-semibold text-sm">Cues & Questions</h3>
                </div>
                <textarea
                  value={cues}
                  onChange={(e) => setCues(e.target.value)}
                  placeholder="Key points, questions, keywords..."
                  className="w-full h-full p-3 resize-none border-none outline-none bg-transparent"
                />
              </div>
              
              {/* Notes Column */}
              <div className="w-2/3">
                <div className="p-3 bg-gray-100 dark:bg-gray-700 border-b border-gray-300 dark:border-gray-600">
                  <h3 className="font-semibold text-sm">Notes</h3>
                </div>
                <textarea
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="Main notes, concepts, details..."
                  className="w-full h-full p-3 resize-none border-none outline-none bg-transparent"
                />
              </div>
            </div>
            
            {/* Summary Section */}
            <div className="border-t border-gray-300 dark:border-gray-600">
              <div className="p-3 bg-gray-100 dark:bg-gray-700 border-b border-gray-300 dark:border-gray-600">
                <h3 className="font-semibold text-sm">Summary</h3>
              </div>
              <textarea
                value={summary}
                onChange={(e) => setSummary(e.target.value)}
                placeholder="Summarize key takeaways..."
                className="w-full h-24 p-3 resize-none border-none outline-none bg-transparent"
              />
            </div>
          </div>

          <div className="flex justify-end space-x-3">
            <button
              onClick={onCancel}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700"
            >
              Cancel
            </button>
            <button
              onClick={handleSave}
              className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md"
            >
              Save Note
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export const Navigation = () => {
// Navigation Component
const Navigation = () => {
  const { currentPage, setCurrentPage, darkMode, toggleDarkMode } = usePage();
  const { user, signIn, signOut } = useAuth();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="bg-white dark:bg-gray-900 shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <button 
                onClick={() => setCurrentPage('home')}
                className="flex items-center space-x-3"
              >
                <img 
                  src="/assets/ImpactMojo Logo.png"
                  alt="ImpactMojo Logo"
                  className="h-16 w-16 object-contain"
                  onError={(e) => {
                    e.target.src = "/assets/android-chrome-192x192.png";
                  }}
                />
                <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                  ImpactMojo
                </span>
              </button>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              {['home', 'courses', 'labs', 'games', 'resources', 'about', 'faq'].map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  className={`${currentPage === page ? 'border-blue-600 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium capitalize`}
                >
                  {page === 'faq' ? 'FAQ' : page}
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
          <div className="hidden sm:ml-6 sm:flex sm:items-center">
            <button
              onClick={toggleDarkMode}
              className="bg-gray-200 dark:bg-gray-700 relative inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
            >
              {darkMode ? <Sun className="block h-6 w-6" aria-hidden="true" /> : <Moon className="block h-6 w-6" aria-hidden="true" />}
            </button>
            {user ? (
              <div className="ml-3 relative">
                <div className="flex items-center space-x-3">
                  <span className="text-gray-700 dark:text-gray-300">{user.displayName}</span>
                  <button
                    onClick={signOut}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
                  >
                    Sign Out
                  </button>
                </div>
              </div>
            ) : (
              <button
                onClick={signIn}
                className="ml-3 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
              >
                Sign In
              </button>
            )}
          </div>
          <div className="-mr-2 flex items-center sm:hidden">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="bg-gray-200 dark:bg-gray-700 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
            >
              {isMenuOpen ? <X className="block h-6 w-6" /> : <Menu className="block h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>
      {isMenuOpen && (
        <div className="sm:hidden">
          <div className="pt-2 pb-3 space-y-1">
            {['home', 'courses', 'labs', 'games', 'resources', 'about', 'faq'].map((page) => (
              <button
                key={page}
                onClick={() => {
                  setCurrentPage(page);
                  setIsMenuOpen(false);
                }}
                className={`${currentPage === page ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left capitalize`}
              >
                {page === 'faq' ? 'FAQ' : page}
              </button>
            ))}
            {user && (
              <>
                <button
                  onClick={() => {
                    setCurrentPage('dashboard');
                    setIsMenuOpen(false);
                  }}
                  className={`${currentPage === 'dashboard' ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left`}
                >
                  Dashboard
                </button>
                <button
                  onClick={() => {
                    setCurrentPage('ai-tools');
                    setIsMenuOpen(false);
                  }}
                  className={`${currentPage === 'ai-tools' ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'} block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left`}
                >
                  AI Tools
                </button>
              </>
            )}
          </div>
          <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
            <div className="flex items-center px-4">
              <button
                onClick={toggleDarkMode}
                className="bg-gray-200 dark:bg-gray-700 relative inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
              >
                {darkMode ? <Sun className="block h-6 w-6" aria-hidden="true" /> : <Moon className="block h-6 w-6" aria-hidden="true" />}
              </button>
              {user ? (
                <div className="ml-3 flex items-center space-x-3">
                  <span className="text-gray-700 dark:text-gray-300">{user.displayName}</span>
                  <button
                    onClick={signOut}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
                  >
                    Sign Out
                  </button>
                </div>
              ) : (
                <button
                  onClick={signIn}
                  className="ml-3 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
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

// IMPROVED Dashboard Page with Cornell Notes
const DashboardPage = () => {
  const { darkMode } = usePage();
  const { user, bookmarks, customPathway, notes, addNote, updateNote, deleteNote } = useAuth();
  const [activeTab, setActiveTab] = useState('overview');
  const [editingNote, setEditingNote] = useState(null);
  const [showNoteEditor, setShowNoteEditor] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [showAdvancedQuiz, setShowAdvancedQuiz] = useState(false);

  const filteredNotes = notes.filter(note => 
    note.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    note.notes.toLowerCase().includes(searchTerm.toLowerCase()) ||
    note.cues.toLowerCase().includes(searchTerm.toLowerCase()) ||
    note.summary.toLowerCase().includes(searchTerm.toLowerCase()) ||
    note.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  const handleSaveNote = (noteData) => {
    if (editingNote) {
      updateNote(editingNote.id, noteData);
    } else {
      addNote(noteData);
    }
    setEditingNote(null);
    setShowNoteEditor(false);
  };

  if (!user) {
    return (
      <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center">
            <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Please Sign In</h1>
            <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">
              Access your dashboard, notes, and custom learning pathway by signing in with Google.
            </p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Welcome back, {user.displayName}!</h1>
          <p className="mt-2 text-lg text-gray-600 dark:text-gray-300">Your personalized learning dashboard</p>
        </div>

        {/* Tabs */}
        <div className="border-b border-gray-200 dark:border-gray-700 mb-8">
          <nav className="-mb-px flex space-x-8">
            {[
              { id: 'overview', label: 'Overview', icon: BarChart },
              { id: 'notes', label: 'Cornell Notes', icon: FileText },
              { id: 'bookmarks', label: 'Bookmarks', icon: BookmarkIcon },
              { id: 'pathway', label: 'Custom Pathway', icon: Target }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`${activeTab === tab.id
                  ? 'border-blue-500 text-blue-600 dark:text-blue-400'
                  : 'border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 hover:border-gray-300'
                } whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm flex items-center space-x-2`}
              >
                <tab.icon size={16} />
                <span>{tab.label}</span>
              </button>
            ))}
          </nav>
        </div>

        {/* Tab Content */}
        {activeTab === 'overview' && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">Learning Progress</h3>
              <div className="text-3xl font-bold text-blue-600 dark:text-blue-400">{bookmarks.length}</div>
              <p className="text-gray-600 dark:text-gray-300">Bookmarked courses</p>
            </div>
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">Notes</h3>
              <div className="text-3xl font-bold text-green-600 dark:text-green-400">{notes.length}</div>
              <p className="text-gray-600 dark:text-gray-300">Cornell notes taken</p>
            </div>
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">Pathway</h3>
              <div className="text-3xl font-bold text-purple-600 dark:text-purple-400">
                {customPathway ? '1' : '0'}
              </div>
              <p className="text-gray-600 dark:text-gray-300">Custom pathway created</p>
            </div>
          </div>
        )}

        {activeTab === 'notes' && (
          <div>
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Cornell Notes</h2>
              <button
                onClick={() => setShowNoteEditor(true)}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md flex items-center space-x-2"
              >
                <Plus size={16} />
                <span>New Note</span>
              </button>
            </div>

            {/* Search Notes */}
            <div className="mb-6">
              <input
                type="text"
                placeholder="Search notes by title, content, or tags..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              />
            </div>

            {/* Notes Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredNotes.map((note) => (
                <div key={note.id} className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{note.title}</h3>
                  <p className="text-gray-600 dark:text-gray-300 text-sm mb-3 line-clamp-3">{note.summary}</p>
                  <div className="flex flex-wrap gap-1 mb-3">
                    {note.tags.map((tag, index) => (
                      <span key={index} className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded text-xs">
                        {tag}
                      </span>
                    ))}
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-xs text-gray-500 dark:text-gray-400">
                      {new Date(note.updatedAt).toLocaleDateString()}
                    </span>
                    <div className="flex space-x-2">
                      <button
                        onClick={() => {
                          setEditingNote(note);
                          setShowNoteEditor(true);
                        }}
                        className="text-blue-600 hover:text-blue-800 dark:text-blue-400"
                      >
                        <Edit3 size={16} />
                      </button>
                      <button
                        onClick={() => deleteNote(note.id)}
                        className="text-red-600 hover:text-red-800 dark:text-red-400"
                      >
                        <X size={16} />
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {filteredNotes.length === 0 && (
              <div className="text-center py-8">
                <FileText size={48} className="mx-auto text-gray-400 mb-4" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No notes found</h3>
                <p className="text-gray-600 dark:text-gray-300">
                  {searchTerm ? 'Try adjusting your search terms.' : 'Start taking notes with the Cornell method!'}
                </p>
              </div>
            )}
          </div>
        )}

        {activeTab === 'bookmarks' && (
          <div>
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">Bookmarked Courses</h2>
            {bookmarks.length === 0 ? (
              <div className="text-center py-8">
                <BookmarkIcon size={48} className="mx-auto text-gray-400 mb-4" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No bookmarks yet</h3>
                <p className="text-gray-600 dark:text-gray-300">Start bookmarking courses to access them quickly here.</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {bookmarks.map((courseId) => {
                  const course = courseData.find(c => c.id === courseId);
                  if (!course) return null;
                  return (
                    <div key={courseId} className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                      <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{course.title}</h3>
                      <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{course.description}</p>
                      <a
                        href={course.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center space-x-2 text-blue-600 hover:text-blue-800 dark:text-blue-400"
                      >
                        <span>Continue Learning</span>
                        <ExternalLink size={16} />
                      </a>
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        )}

        {activeTab === 'pathway' && (
          <div>
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Custom Learning Pathway</h2>
              <button
                onClick={() => setShowAdvancedQuiz(true)}
                className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-md flex items-center space-x-2"
              >
                <Target size={16} />
                <span>Create/Update Pathway</span>
              </button>
            </div>
            
            {customPathway ? (
              <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Your Personalized Path</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <h4 className="font-medium text-gray-900 dark:text-white mb-2">Recommended Courses</h4>
                    <ul className="space-y-2">
                      {customPathway.courses?.map((courseId, index) => {
                        const course = courseData.find(c => c.id === courseId);
                        return course ? (
                          <li key={index} className="flex items-center space-x-2">
                            <CheckCircle size={16} className="text-green-500" />
                            <span className="text-gray-700 dark:text-gray-300">{course.title}</span>
                          </li>
                        ) : null;
                      })}
                    </ul>
                  </div>
                  <div>
                    <h4 className="font-medium text-gray-900 dark:text-white mb-2">Recommended Labs</h4>
                    <ul className="space-y-2">
                      {customPathway.labs?.map((labId, index) => {
                        const lab = labsData.find(l => l.id === labId);
                        return lab ? (
                          <li key={index} className="flex items-center space-x-2">
                            <Trophy size={16} className="text-yellow-500" />
                            <span className="text-gray-700 dark:text-gray-300">{lab.title}</span>
                          </li>
                        ) : null;
                      })}
                    </ul>
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center py-8">
                <Target size={48} className="mx-auto text-gray-400 mb-4" />
                <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No custom pathway yet</h3>
                <p className="text-gray-600 dark:text-gray-300">Take our comprehensive assessment to create your personalized learning path.</p>
              </div>
            )}
          </div>
        )}

        {/* Cornell Notes Editor Modal */}
        {showNoteEditor && (
          <CornellNotesEditor
            note={editingNote}
            onSave={handleSaveNote}
            onCancel={() => {
              setShowNoteEditor(false);
              setEditingNote(null);
            }}
          />
        )}

        {/* Advanced Quiz Modal */}
        {showAdvancedQuiz && (
          <AdvancedQuizModal
            onClose={() => setShowAdvancedQuiz(false)}
            onComplete={(pathway) => {
              // Save pathway to user data
              console.log('Pathway created:', pathway);
              setShowAdvancedQuiz(false);
            }}
          />
        )}
      </div>
    </div>
  );
};

// Advanced Quiz Modal for Logged-in Users
const AdvancedQuizModal = ({ onClose, onComplete }) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const { darkMode } = usePage();

  const questions = [
    {
      id: 'experience_level',
      question: 'What is your current experience level in development work?',
      type: 'single',
      options: [
        'Complete beginner - new to development',
        'Some exposure - taken courses or workshops',
        'Intermediate - 1-3 years experience',
        'Advanced - 4+ years experience',
        'Expert - 10+ years with specialized knowledge'
      ]
    },
    {
      id: 'primary_role',
      question: 'What is your primary role or aspiration?',
      type: 'single',
      options: [
        'Academic researcher',
        'Field practitioner/NGO worker',
        'Policy analyst/government',
        'Social entrepreneur',
        'Student/aspiring professional',
        'Development consultant',
        'International organization staff'
      ]
    },
    {
      id: 'interested_themes',
      question: 'Which themes are you most interested in? (Select all that apply)',
      type: 'multiple',
      options: [
        'Health and wellbeing',
        'Education and skills development',
        'Economic development and livelihoods',
        'Governance and accountability',
        'Gender equality and social inclusion',
        'Climate change and environment',
        'Data and research methods',
        'Advocacy and communications'
      ]
    },
    {
      id: 'geographic_focus',
      question: 'What is your geographic focus?',
      type: 'single',
      options: [
        'India',
        'South Asia',
        'Global South',
        'Specific country (other than India)',
        'Global/comparative perspective'
      ]
    },
    {
      id: 'learning_style',
      question: 'How do you prefer to learn? (Select all that apply)',
      type: 'multiple',
      options: [
        'Reading research papers and reports',
        'Hands-on practical exercises',
        'Case studies and real examples',
        'Interactive simulations and games',
        'Data analysis and visualization',
        'Collaborative discussions',
        'Self-paced online modules'
      ]
    },
    {
      id: 'skill_priorities',
      question: 'Which skills do you most want to develop?',
      type: 'multiple',
      options: [
        'Research and analysis',
        'Program design and implementation',
        'Data collection and analysis',
        'Policy analysis and advocacy',
        'Communication and presentation',
        'Leadership and management',
        'Technical/sector-specific knowledge'
      ]
    },
    {
      id: 'time_availability',
      question: 'How much time can you dedicate to learning per week?',
      type: 'single',
      options: [
        'Less than 2 hours',
        '2-5 hours',
        '5-10 hours',
        'More than 10 hours'
      ]
    },
    {
      id: 'specific_goals',
      question: 'What are your specific learning goals? (Select all that apply)',
      type: 'multiple',
      options: [
        'Career transition into development',
        'Skill upgrade for current role',
        'Academic preparation (PhD, research)',
        'Starting a social venture',
        'Improving program effectiveness',
        'Personal interest and knowledge',
        'Professional certification or credentials'
      ]
    }
  ];

  const handleAnswer = (questionId, answer) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }));
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      // Generate personalized pathway based on answers
      const pathway = generatePersonalizedPathway(answers);
      onComplete(pathway);
    }
  };

  const generatePersonalizedPathway = (answers) => {
    // Advanced algorithm to create personalized pathway
    let recommendedCourses = [];
    let recommendedLabs = [];
    let recommendedResources = [];

    // Based on experience level
    if (answers.experience_level?.includes('beginner')) {
      recommendedCourses.push('development-economics-101', 'global-development-architecture-101');
    } else if (answers.experience_level?.includes('Advanced') || answers.experience_level?.includes('Expert')) {
      recommendedCourses.push('econometrics-101', 'research-ethics-101');
    }

    // Based on role
    if (answers.primary_role?.includes('researcher')) {
      recommendedCourses.push('qualitative-research-methods-101', 'data-literacy-101');
      recommendedLabs.push('research-methodology-lab');
    } else if (answers.primary_role?.includes('practitioner')) {
      recommendedCourses.push('community-development-101', 'monitoring-evaluation-accountability-and-learning-101');
      recommendedLabs.push('field-work-simulation');
    }

    // Based on themes
    if (answers.interested_themes?.includes('Health')) {
      recommendedCourses.push('public-health-101');
    }
    if (answers.interested_themes?.includes('Education')) {
      recommendedCourses.push('data-literacy-101');
    }

    // Based on learning style
    if (answers.learning_style?.includes('Data analysis')) {
      recommendedLabs.push('data-analysis-lab');
      recommendedResources.push('PR3'); // Statistical Analysis Assistant
    }
    if (answers.learning_style?.includes('research papers')) {
      recommendedResources.push('PR1'); // Field Notes
    }

    return {
      courses: [...new Set(recommendedCourses)].slice(0, 6), // Remove duplicates, limit to 6
      labs: [...new Set(recommendedLabs)].slice(0, 4),
      resources: [...new Set(recommendedResources)].slice(0, 3),
      createdAt: new Date().toISOString(),
      answers: answers
    };
  };

  const currentQ = questions[currentQuestion];
  const isLastQuestion = currentQuestion === questions.length - 1;
  const hasAnswer = answers[currentQ.id];

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className={`${darkMode ? 'bg-gray-800 text-white' : 'bg-white text-gray-900'} rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto`}>
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold">Create Your Custom Learning Pathway</h2>
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X size={24} />
            </button>
          </div>

          {/* Progress bar */}
          <div className="mb-6">
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400 mb-2">
              <span>Question {currentQuestion + 1} of {questions.length}</span>
              <span>{Math.round(((currentQuestion + 1) / questions.length) * 100)}% Complete</span>
            </div>
            <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
              <div 
                className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
              ></div>
            </div>
          </div>

          {/* Question */}
          <div className="mb-6">
            <h3 className="text-lg font-semibold mb-4">{currentQ.question}</h3>
            <div className="space-y-3">
              {currentQ.options.map((option, index) => (
                <label key={index} className="flex items-center space-x-3 cursor-pointer">
                  <input
                    type={currentQ.type === 'multiple' ? 'checkbox' : 'radio'}
                    name={currentQ.id}
                    value={option}
                    checked={
                      currentQ.type === 'multiple' 
                        ? answers[currentQ.id]?.includes(option) || false
                        : answers[currentQ.id] === option
                    }
                    onChange={(e) => {
                      if (currentQ.type === 'multiple') {
                        const current = answers[currentQ.id] || [];
                        if (e.target.checked) {
                          handleAnswer(currentQ.id, [...current, option]);
                        } else {
                          handleAnswer(currentQ.id, current.filter(item => item !== option));
                        }
                      } else {
                        handleAnswer(currentQ.id, option);
                      }
                    }}
                    className="text-blue-600 focus:ring-blue-500"
                  />
                  <span className="text-gray-700 dark:text-gray-300">{option}</span>
                </label>
              ))}
            </div>
          </div>

          {/* Navigation */}
          <div className="flex justify-between">
            <button
              onClick={() => setCurrentQuestion(Math.max(0, currentQuestion - 1))}
              disabled={currentQuestion === 0}
              className="px-4 py-2 text-gray-600 dark:text-gray-400 disabled:opacity-50"
            >
              Previous
            </button>
            <button
              onClick={handleNext}
              disabled={!hasAnswer}
              className="px-6 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white rounded-md"
            >
              {isLastQuestion ? 'Create Pathway' : 'Next'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

// Homepage Component
const HomePage = () => {
  const { darkMode } = usePage();
  const { user } = useAuth();
  const [showQuizModal, setShowQuizModal] = useState(false);
  const [quizResult, setQuizResult] = useState(null);

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      
      {/* Hero Section - De-emphasized Donation */}
      <div className="relative bg-gradient-to-r from-blue-600 to-purple-700 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Development Know-How for Everyone
            </h1>
            <p className="text-xl md:text-2xl mb-8 opacity-90">
              101 Knowledge Series for Social Impact - Justice, Equity & Development in South Asia
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button
                onClick={() => setShowQuizModal(true)}
                className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
              >
                Find Your Learning Path
              </button>
              <button className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition-colors">
                Explore Courses
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Live Learner Stats */}
      <LiveStatsSection />

      {/* Popular Courses Section */}
      <PopularCoursesSection />

      {/* Learning Tracks Section with Four Original Tracks */}
      <div className="py-16 bg-gray-50 dark:bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Four Learning Tracks
            </h2>
            <p className="text-lg text-gray-600 dark:text-gray-300">
              Structured pathways to master key development concepts and skills
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {Object.entries(fourOriginalTracks).map(([track, data]) => (
              <div key={track} className="bg-white dark:bg-gray-700 rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
                <div className="text-center mb-4">
                  <div className="text-4xl mb-3">{data.icon}</div>
                  <h4 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">{track}</h4>
                  <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{data.description}</p>
                </div>
                <div className="text-center">
                  <div className="text-xs text-gray-500 dark:text-gray-400 mb-3">
                    {data.courses.length} courses
                  </div>
                  <button className={`w-full px-4 py-2 bg-${data.color}-600 hover:bg-${data.color}-700 text-white rounded-md text-sm font-medium transition-colors`}>
                    Explore Track
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Featured Content */}
      <FeaturedContentSection />

      {/* Testimonials */}
      <TestimonialsSection />

      {/* About Me Section */}
      <AboutMeSection />

      {/* Small Donation Section (De-emphasized) */}
      <div className="py-8 bg-yellow-50 dark:bg-yellow-900/20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="flex items-center justify-center mb-3">
            <Heart className="text-red-500 mr-2" size={20} />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Support ImpactMojo</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 text-sm mb-3">
            Help keep our resources free and accessible. Support covers development and hosting costs.
          </p>
          <div className="text-sm text-gray-500 dark:text-gray-400">
            <p>UPI: impactmojo@ibl • impactmojo@ybl • impactmojo@axl</p>
          </div>
        </div>
      </div>

      {/* Simple Quiz Modal for Non-Logged In Users */}
      {showQuizModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
            {!quizResult ? (
              <SimpleQuiz 
                onComplete={(result) => setQuizResult(result)}
                onClose={() => setShowQuizModal(false)}
              />
            ) : (
              <QuizResult 
                result={quizResult}
                onClose={() => {
                  setShowQuizModal(false);
                  setQuizResult(null);
                }}
              />
            )}
          </div>
        </div>
      )}
    </div>
  );
};

// Simple Quiz Component for non-logged users
const SimpleQuiz = ({ onComplete, onClose }) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const { darkMode } = usePage();

  const questions = [
    {
      id: 'experience',
      question: 'What is your experience with development work?',
      options: ['Complete beginner', 'Some exposure', 'Experienced practitioner']
    },
    {
      id: 'interest',
      question: 'What interests you most?',
      options: ['Research and analysis', 'Field work and community engagement', 'Policy and advocacy']
    },
    {
      id: 'goal',
      question: 'What is your main goal?',
      options: ['Learn the basics', 'Develop specific skills', 'Advance my career']
    }
  ];

  const handleAnswer = (answer) => {
    const newAnswers = { ...answers, [questions[currentQuestion].id]: answer };
    setAnswers(newAnswers);

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      // Generate simple recommendation
      let recommendation = 'development-economics-101';
      if (newAnswers.interest === 'Research and analysis') {
        recommendation = 'data-literacy-101';
      } else if (newAnswers.interest === 'Field work and community engagement') {
        recommendation = 'community-development-101';
      } else if (newAnswers.interest === 'Policy and advocacy') {
        recommendation = 'law-and-constitution-101';
      }
      
      onComplete({ recommendation, answers: newAnswers });
    }
  };

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Find Your Starting Point</h3>
        <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
          <X size={20} />
        </button>
      </div>
      
      <div className="mb-4">
        <div className="text-sm text-gray-600 dark:text-gray-400 mb-2">
          Question {currentQuestion + 1} of {questions.length}
        </div>
        <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
          <div 
            className="bg-blue-600 h-2 rounded-full transition-all duration-300"
            style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
          ></div>
        </div>
      </div>

      <div className="mb-6">
        <h4 className="text-gray-900 dark:text-white mb-4">{questions[currentQuestion].question}</h4>
        <div className="space-y-2">
          {questions[currentQuestion].options.map((option, index) => (
            <button
              key={index}
              onClick={() => handleAnswer(option)}
              className="w-full text-left p-3 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
            >
              {option}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

// Quiz Result Component
const QuizResult = ({ result, onClose }) => {
  const { darkMode } = usePage();
  const recommendedCourse = courseData.find(c => c.id === result.recommendation);

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Your Recommended Starting Point</h3>
        <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
          <X size={20} />
        </button>
      </div>

      {recommendedCourse && (
        <div className="mb-6">
          <h4 className="text-gray-900 dark:text-white font-semibold mb-2">{recommendedCourse.title}</h4>
          <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{recommendedCourse.description}</p>
          <a
            href={recommendedCourse.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md"
          >
            <span>Start Learning</span>
            <ExternalLink size={16} />
          </a>
        </div>
      )}

      <div className="text-center">
        <p className="text-gray-600 dark:text-gray-300 text-sm">
          Want more personalized recommendations? Sign in to access our comprehensive assessment and custom learning pathways.
        </p>
      </div>
    </div>
  );
};

// Enhanced Search and Filter Function
const useSearchAndFilter = (data, initialCategory = 'all') => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState(initialCategory);
  const [selectedRole, setSelectedRole] = useState('all');
  const [selectedTheme, setSelectedTheme] = useState('all');

  // Get unique categories, roles, and themes
  const categories = ['all', ...new Set(data.map(item => item.category).filter(Boolean))];
  const roles = ['all', ...new Set(data.map(item => item.role).filter(Boolean))];
  const themes = ['all', ...new Set(data.map(item => item.theme).filter(Boolean))];

  const filteredData = data.filter(item => {
    const matchesSearch = searchQuery === '' || 
      item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.description && item.description.toLowerCase().includes(searchQuery.toLowerCase())) ||
      (item.tags && item.tags.some(tag => tag.toLowerCase().includes(searchQuery.toLowerCase())));
    
    const matchesCategory = selectedCategory === 'all' || item.category === selectedCategory;
    const matchesRole = selectedRole === 'all' || item.role === selectedRole;
    const matchesTheme = selectedTheme === 'all' || item.theme === selectedTheme;
    
    return matchesSearch && matchesCategory && matchesRole && matchesTheme;
  });

  return {
    searchQuery,
    setSearchQuery,
    selectedCategory,
    setSelectedCategory,
    selectedRole,
    setSelectedRole,
    selectedTheme,
    setSelectedTheme,
    filteredData,
    categories,
    roles,
    themes
  };
};

// Courses Page with FIXED search and filters
const CoursesPage = () => {
  const { darkMode } = usePage();
  const { user, bookmarks, toggleBookmark } = useAuth();
  
  const {
    searchQuery,
    setSearchQuery,
    selectedCategory,
    setSelectedCategory,
    selectedRole,
    setSelectedRole,
    selectedTheme,
    setSelectedTheme,
    filteredData: filteredCourses,
    categories,
    roles,
    themes
  } = useSearchAndFilter(courseData);

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Courses</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Comprehensive learning modules on development topics</p>
        </div>

        {/* Search and Filters */}
        <div className="mb-8">
          <div className="flex flex-col lg:flex-row gap-4">
            {/* Search */}
            <div className="flex-1">
              <input
                type="text"
                placeholder="Search courses..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              />
            </div>
            
            {/* Filters */}
            <div className="flex flex-col sm:flex-row gap-2">
              <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
                className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              >
                {categories.map((category) => (
                  <option key={category} value={category}>
                    {category === 'all' ? 'All Categories' : category}
                  </option>
                ))}
              </select>
              
              <select
                value={selectedRole}
                onChange={(e) => setSelectedRole(e.target.value)}
                className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              >
                {roles.map((role) => (
                  <option key={role} value={role}>
                    {role === 'all' ? 'All Roles' : role}
                  </option>
                ))}
              </select>
              
              <select
                value={selectedTheme}
                onChange={(e) => setSelectedTheme(e.target.value)}
                className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              >
                {themes.map((theme) => (
                  <option key={theme} value={theme}>
                    {theme === 'all' ? 'All Themes' : theme}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Results Count */}
        <div className="mb-6">
          <p className="text-gray-600 dark:text-gray-300">
            Showing {filteredCourses.length} of {courseData.length} courses
          </p>
        </div>

        {/* Courses Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCourses.map((course) => (
            <div key={course.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="p-6">
                <div className="flex justify-between items-start mb-3">
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white">{course.title}</h3>
                  {user && (
                    <button
                      onClick={() => toggleBookmark(course.id)}
                      className={`${bookmarks.includes(course.id) ? 'text-blue-600' : 'text-gray-400'} hover:text-blue-600`}
                    >
                      <BookmarkIcon size={20} />
                    </button>
                  )}
                </div>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{course.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {course.category && (
                    <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded text-xs">
                      {course.category}
                    </span>
                  )}
                  {course.difficulty && (
                    <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 px-2 py-1 rounded text-xs">
                      {course.difficulty}
                    </span>
                  )}
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-xs text-gray-500 dark:text-gray-400 flex items-center">
                    <Clock size={12} className="mr-1" />
                    {course.duration || '2-3 hours'}
                  </span>
                  <a
                    href={course.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center space-x-1 text-blue-600 hover:text-blue-800 dark:text-blue-400"
                  >
                    <span>Start Course</span>
                    <ExternalLink size={16} />
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* No results */}
        {filteredCourses.length === 0 && (
          <div className="text-center py-8">
            <BookOpen size={48} className="mx-auto text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No courses found</h3>
            <p className="text-gray-600 dark:text-gray-300">Try adjusting your search or filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
};

// Labs Page with ADDED search and filters
const LabsPage = () => {
  const { darkMode } = usePage();
  
  const {
    searchQuery,
    setSearchQuery,
    selectedCategory,
    setSelectedCategory,
    filteredData: filteredLabs,
    categories
  } = useSearchAndFilter(labsData);

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Labs</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Hands-on practical exercises and simulations</p>
        </div>

        {/* Search and Filters */}
        <div className="mb-8">
          <div className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1">
              <input
                type="text"
                placeholder="Search labs..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              />
            </div>
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
            >
              {categories.map((category) => (
                <option key={category} value={category}>
                  {category === 'all' ? 'All Categories' : category}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Results Count */}
        <div className="mb-6">
          <p className="text-gray-600 dark:text-gray-300">
            Showing {filteredLabs.length} of {labsData.length} labs
          </p>
        </div>

        {/* Labs Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredLabs.map((lab) => (
            <div key={lab.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="p-6">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-3">{lab.title}</h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{lab.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {lab.category && (
                    <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 px-2 py-1 rounded text-xs">
                      {lab.category}
                    </span>
                  )}
                  {lab.difficulty && (
                    <span className="bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 px-2 py-1 rounded text-xs">
                      {lab.difficulty}
                    </span>
                  )}
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-xs text-gray-500 dark:text-gray-400 flex items-center">
                    <Trophy size={12} className="mr-1" />
                    Interactive Lab
                  </span>
                  <a
                    href={lab.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center space-x-1 text-green-600 hover:text-green-800 dark:text-green-400"
                  >
                    <span>Start Lab</span>
                    <ExternalLink size={16} />
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* No results */}
        {filteredLabs.length === 0 && (
          <div className="text-center py-8">
            <Trophy size={48} className="mx-auto text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No labs found</h3>
            <p className="text-gray-600 dark:text-gray-300">Try adjusting your search or filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
};

// Games Page with ADDED search and filters
const GamesPage = () => {
  const { darkMode } = usePage();
  
  const {
    searchQuery,
    setSearchQuery,
    selectedCategory,
    setSelectedCategory,
    filteredData: filteredGames,
    categories
  } = useSearchAndFilter(gamesData);

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Games</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Interactive games for development learning</p>
        </div>

        {/* Search and Filters */}
        <div className="mb-8">
          <div className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1">
              <input
                type="text"
                placeholder="Search games..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              />
            </div>
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
            >
              {categories.map((category) => (
                <option key={category} value={category}>
                  {category === 'all' ? 'All Categories' : category}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Results Count */}
        <div className="mb-6">
          <p className="text-gray-600 dark:text-gray-300">
            Showing {filteredGames.length} of {gamesData.length} games
          </p>
        </div>

        {/* Games Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredGames.map((game) => (
            <div key={game.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="p-6">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-3">{game.title}</h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{game.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {game.category && (
                    <span className="bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 px-2 py-1 rounded text-xs">
                      {game.category}
                    </span>
                  )}
                  {game.difficulty && (
                    <span className="bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200 px-2 py-1 rounded text-xs">
                      {game.difficulty}
                    </span>
                  )}
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-xs text-gray-500 dark:text-gray-400 flex items-center">
                    <Gamepad2 size={12} className="mr-1" />
                    Interactive Game
                  </span>
                  <a
                    href={game.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center space-x-1 text-purple-600 hover:text-purple-800 dark:text-purple-400"
                  >
                    <span>Play Game</span>
                    <ExternalLink size={16} />
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* No results */}
        {filteredGames.length === 0 && (
          <div className="text-center py-8">
            <Gamepad2 size={48} className="mx-auto text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No games found</h3>
            <p className="text-gray-600 dark:text-gray-300">Try adjusting your search or filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
};

// Resources Page with ADDED search and filters
const ResourcesPage = () => {
  const { darkMode } = usePage();
  
  const {
    searchQuery,
    setSearchQuery,
    selectedCategory,
    setSelectedCategory,
    filteredData: filteredResources,
    categories
  } = useSearchAndFilter(updatedPremiumResources);

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">Resources</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">Premium tools and resources for development professionals</p>
        </div>

        {/* Search and Filters */}
        <div className="mb-8">
          <div className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1">
              <input
                type="text"
                placeholder="Search resources..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
              />
            </div>
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
            >
              {categories.map((category) => (
                <option key={category} value={category}>
                  {category === 'all' ? 'All Categories' : category}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Results Count */}
        <div className="mb-6">
          <p className="text-gray-600 dark:text-gray-300">
            Showing {filteredResources.length} of {updatedPremiumResources.length} resources
          </p>
        </div>

        {/* Resources Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredResources.map((resource) => (
            <div key={resource.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="p-6">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-3">{resource.title}</h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{resource.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {resource.category && (
                    <span className="bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200 px-2 py-1 rounded text-xs">
                      {resource.category}
                    </span>
                  )}
                  {resource.access && (
                    <span className="bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200 px-2 py-1 rounded text-xs">
                      {resource.access}
                    </span>
                  )}
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-xs text-gray-500 dark:text-gray-400 flex items-center">
                    <Library size={12} className="mr-1" />
                    Premium Resource
                  </span>
                  <a
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center space-x-1 text-orange-600 hover:text-orange-800 dark:text-orange-400"
                  >
                    <span>Access Resource</span>
                    <ExternalLink size={16} />
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* No results */}
        {filteredResources.length === 0 && (
          <div className="text-center py-8">
            <Library size={48} className="mx-auto text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">No resources found</h3>
            <p className="text-gray-600 dark:text-gray-300">Try adjusting your search or filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
};

// AI Tools Page (for logged-in users)
const AIToolsPage = () => {
  const { darkMode } = usePage();
  const { user } = useAuth();

  if (!user) {
    return (
      <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center">
            <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">AI Tools</h1>
            <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">
              Please sign in to access AI-powered development tools.
            </p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      <ImprovedFloatingActionButtons />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-white">AI Tools</h1>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">AI-powered tools for development professionals</p>
        </div>

        {/* AI Tools Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {aiToolsData.map((tool) => (
            <div key={tool.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="p-6">
                <div className="flex items-center mb-3">
                  <Bot className="text-blue-600 dark:text-blue-400 mr-3" size={24} />
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white">{tool.title}</h3>
                </div>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4">{tool.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-2 py-1 rounded text-xs">
                    {tool.category}
                  </span>
                  <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 px-2 py-1 rounded text-xs">
                    AI Powered
                  </span>
                </div>
                <a
                  href={tool.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center space-x-1 text-blue-600 hover:text-blue-800 dark:text-blue-400"
                >
                  <span>Use Tool</span>
                  <ExternalLink size={16} />
                </a>
              </div>
            </div>
          ))}
        </div>

        {/* Lo-Fi Music Player for Logged Users */}
        <div className="mt-12 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
          <div className="flex items-center mb-4">
            <Headphones className="text-purple-600 dark:text-purple-400 mr-3" size={24} />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Focus Music</h3>
          </div>
          <p className="text-gray-600 dark:text-gray-300 mb-4">
            Listen to curated lo-fi music to enhance your learning experience.
          </p>
          <a
            href="https://www.youtube.com/watch?v=jfKfPfyJRdk"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center space-x-2 bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-md"
          >
            <Music size={16} />
            <span>Open Focus Playlist</span>
            <ExternalLink size={16} />
          </a>
          <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">
            Use password: <span className="font-mono">focus2024</span> if prompted.
          </p>
        </div>
      </div>
    </div>
  );
};

// Footer Component with FIXED year and PinPoint attribution
const Footer = () => {
  const { darkMode } = usePage();

  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-3 mb-4">
              <img 
                src="/assets/ImpactMojo Logo.png"
                alt="ImpactMojo Logo"
                className="h-8 w-8"
                onError={(e) => {
                  e.target.src = "/assets/android-chrome-192x192.png";
                }}
              />
              <span className="text-xl font-bold">ImpactMojo</span>
            </div>
            <p className="text-gray-300 mb-4">
              101 Knowledge Series for Social Impact - Development education for justice, equity, and sustainable change in South Asia.
            </p>
            <p className="text-gray-300 text-sm">
              No endorsements or certificates. Built for learning and social impact.
            </p>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-4">Learn</h3>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-300 hover:text-white">Courses</a></li>
              <li><a href="#" className="text-gray-300 hover:text-white">Labs</a></li>
              <li><a href="#" className="text-gray-300 hover:text-white">Games</a></li>
              <li><a href="#" className="text-gray-300 hover:text-white">Resources</a></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-4">Legal</h3>
            <ul className="space-y-2">
              <li><a href="/terms-of-use" target="_blank" className="text-gray-300 hover:text-white">Terms of Use</a></li>
              <li><a href="/privacy-policy" target="_blank" className="text-gray-300 hover:text-white">Privacy Policy</a></li>
              <li><a href="/cookie-policy" target="_blank" className="text-gray-300 hover:text-white">Cookie Policy</a></li>
              <li><a href="#faq" className="text-gray-300 hover:text-white">FAQ</a></li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-700 mt-8 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="text-gray-300 text-sm mb-4 md:mb-0">
              © 2025 ImpactMojo. All rights reserved.
            </div>
            <div className="flex items-center text-gray-300 text-sm">
              <span>ImpactMojo is made possible due to the generous support offered by </span>
              <a 
                href="https://www.pinpointventures.in" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-blue-400 hover:text-blue-300 mx-1"
              >
                PinPoint Ventures
              </a>
              <Heart className="text-red-400 ml-1" size={16} />
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

// Cookie Consent Component
const CookieConsent = () => {
  const [showCookieConsent, setShowCookieConsent] = useState(false);

  useEffect(() => {
    const hasConsent = localStorage.getItem('impactmojo-cookie-consent');
    if (!hasConsent) {
      setShowCookieConsent(true);
    }
  }, []);

  if (!showCookieConsent) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 bg-gray-900 text-white p-4 z-50">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <p className="text-sm">
          We use analytics to improve your experience. By continuing, you agree to our use of cookies.
        </p>
        <button
          onClick={() => {
            localStorage.setItem('impactmojo-cookie-consent', 'true');
            setShowCookieConsent(false);
          }}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium ml-4"
        >
          Accept
        </button>
      </div>
    </div>
  );
};

// Auth Context Provider
const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);
  const [customPathway, setCustomPathway] = useState(null);
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user);
      if (user) {
        // Load user data from Firestore
        const userDoc = await getDoc(doc(db, 'users', user.uid));
        if (userDoc.exists()) {
          const userData = userDoc.data();
          setBookmarks(userData.bookmarks || []);
          setCustomPathway(userData.customPathway || null);
          setNotes(userData.notes || []);
        }
      } else {
        setBookmarks([]);
        setCustomPathway(null);
        setNotes([]);
      }
      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  const signIn = async () => {
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

  const toggleBookmark = async (courseId) => {
    if (!user) return;

    const newBookmarks = bookmarks.includes(courseId)
      ? bookmarks.filter(id => id !== courseId)
      : [...bookmarks, courseId];

    setBookmarks(newBookmarks);
    
    try {
      await updateDoc(doc(db, 'users', user.uid), {
        bookmarks: newBookmarks
      });
    } catch (error) {
      console.error('Error updating bookmarks:', error);
    }
  };

  const addNote = async (noteData) => {
    if (!user) return;

    const newNote = {
      id: Date.now().toString(),
      ...noteData
    };

    const newNotes = [...notes, newNote];
    setNotes(newNotes);

    try {
      await updateDoc(doc(db, 'users', user.uid), {
        notes: newNotes
      });
    } catch (error) {
      console.error('Error adding note:', error);
    }
  };

  const updateNote = async (noteId, noteData) => {
    if (!user) return;

    const newNotes = notes.map(note => 
      note.id === noteId ? { ...note, ...noteData } : note
    );
    setNotes(newNotes);

    try {
      await updateDoc(doc(db, 'users', user.uid), {
        notes: newNotes
      });
    } catch (error) {
      console.error('Error updating note:', error);
    }
  };

  const deleteNote = async (noteId) => {
    if (!user) return;

    const newNotes = notes.filter(note => note.id !== noteId);
    setNotes(newNotes);

    try {
      await updateDoc(doc(db, 'users', user.uid), {
        notes: newNotes
      });
    } catch (error) {
      console.error('Error deleting note:', error);
    }
  };

  const value = {
    user,
    loading,
    signIn,
    signOut,
    bookmarks,
    toggleBookmark,
    customPathway,
    setCustomPathway,
    notes,
    addNote,
    updateNote,
    deleteNote
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

// Page Context Provider
const PageProvider = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('home');
  const [darkMode, setDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('darkMode') === 'true';
    }
    return false;
  });

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    localStorage.setItem('darkMode', (!darkMode).toString());
  };

  const value = {
    currentPage,
    setCurrentPage,
    darkMode,
    toggleDarkMode
  };

  return <PageContext.Provider value={value}>{children}</PageContext.Provider>;
};

// Main App Component
const App = () => {
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
      case 'about':
        return <AboutPage />;
      case 'faq':
        return <FAQPage />;
      case 'dashboard':
        return <DashboardPage />;
      case 'ai-tools':
        return <AIToolsPage />;
      default:
        return <HomePage />;
    }
  };

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {renderPage()}
      <Footer />
      <CookieConsent />
    </div>
  );
};

// Root App with Providers
const AppWithProviders = () => {
  return (
    <PageProvider>
      <AuthProvider>
        <App />
      </AuthProvider>
    </PageProvider>
  );
};

export default AppWithProviders;

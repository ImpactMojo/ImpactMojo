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
  GitCompare,
  Search,
  Filter,
  Star,
  ExternalLink,
  Download,
  Clock,
  BarChart3,
  Microscope,
  Scale,
  Building,
  Play,
  Send,
  Target,
  Award,
  Lightbulb
} from 'lucide-react';

// Mock auth system
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

// Complete Course Data Structure - Following CourseList.txt and web developer specs
const courseData = {
  courses: [
    // Research Methods Track
    {
      id: "C1",
      title: "Development Economics 101",
      track: "Research Methods",
      description: "Foundation of economic principles in development contexts",
      quote: "Essential framework for understanding economic development",
      level: "Beginner",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/DevEcon",
      popular: true
    },
    {
      id: "C3",
      title: "Climate Science 101", 
      track: "Research Methods",
      description: "Scientific foundations of climate change and environmental impact",
      quote: "Critical knowledge for understanding our changing planet",
      level: "Beginner",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/ClimateScience",
      popular: true
    },
    {
      id: "C5",
      title: "Research Ethics 101",
      track: "Research Methods",
      description: "Ethical considerations in research and data collection",
      quote: "Foundation for responsible and impactful research",
      level: "Beginner",
      duration: "2 hours",
      content: "https://101.www.impactmojo.in/ResearchEthics"
    },
    {
      id: "C9",
      title: "Behaviour Change Communication Programming 101",
      track: "Research Methods",
      description: "Strategic communication for social and behavioral change",
      quote: "Transforming communities through evidence-based messaging",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/BCCP"
    },
    {
      id: "C13",
      title: "Visual Ethnography 101",
      track: "Research Methods",
      description: "Using visual methods for ethnographic research",
      quote: "Capturing stories through the power of visual narrative",
      level: "Intermediate",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/VEthno"
    },
    {
      id: "C27",
      title: "Qualitative Research Methods 101",
      track: "Research Methods",
      description: "In-depth approaches to qualitative data collection and analysis",
      quote: "Understanding the human experience through rigorous inquiry",
      level: "Intermediate",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/QualR"
    },
    {
      id: "C31",
      title: "Digital Ethics 101",
      track: "Research Methods",
      description: "Ethical frameworks for digital technology and data use",
      quote: "Navigating moral complexities in our digital age",
      level: "Intermediate",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/DigitalEthics"
    },

    // Data Analysis Track
    {
      id: "C6",
      title: "Data Literacy 101",
      track: "Data Analysis",
      description: "Essential skills for understanding and working with data",
      quote: "Empowering evidence-based decision making",
      level: "Beginner",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/data-lit",
      popular: true
    },
    {
      id: "C19",
      title: "Econometrics 101",
      track: "Data Analysis",
      description: "Statistical methods for economic data analysis",
      quote: "Quantifying relationships in economic research",
      level: "Advanced",
      duration: "4.5 hours",
      content: "https://101.www.impactmojo.in/econometrics"
    },
    {
      id: "C28",
      title: "Exploratory Data Analysis for Household Surveys 101",
      track: "Data Analysis",
      description: "Analyzing household survey data for development insights",
      quote: "Uncovering patterns in household-level data",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/HH-EDA"
    },
    {
      id: "C29",
      title: "Bivariate Analysis 101",
      track: "Data Analysis",
      description: "Exploring relationships between two variables",
      quote: "Understanding connections in your data",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/bivariateA"
    },
    {
      id: "C30",
      title: "Multivariate Analysis 101",
      track: "Data Analysis",
      description: "Advanced statistical techniques for complex data",
      quote: "Mastering sophisticated analytical approaches",
      level: "Advanced",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/MultivariateA"
    },
    {
      id: "C34",
      title: "Data Feminism 101",
      track: "Data Analysis",
      description: "Examining power and justice in data science",
      quote: "Challenging assumptions in data work",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/DataFem"
    },

    // Gender Studies Track
    {
      id: "C2",
      title: "Gender Studies 101",
      track: "Gender Studies",
      description: "Introduction to gender theory and its practical implications",
      quote: "Eye-opening exploration of gender norms and their impact",
      level: "Beginner",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/Gender",
      popular: true
    },
    {
      id: "C8",
      title: "Women's Economic Empowerment 101",
      track: "Gender Studies",
      description: "Economic frameworks for women's empowerment",
      quote: "Transforming economic opportunities for women",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/WEE"
    },
    {
      id: "C16",
      title: "Marginalized Identities 101",
      track: "Gender Studies",
      description: "Understanding intersectionality and marginalized communities",
      quote: "Centering voices often left unheard",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/identities"
    },
    {
      id: "C17",
      title: "Sexual and Reproductive Health Rights 101",
      track: "Gender Studies",
      description: "Rights-based approach to sexual and reproductive health",
      quote: "Health as a fundamental human right",
      level: "Intermediate",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/srhr"
    },
    {
      id: "C20",
      title: "Care Economy 101",
      track: "Gender Studies",
      description: "Understanding unpaid care work and economic systems",
      quote: "Making visible the invisible economy of care",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/careeconomy"
    },

    // Policy & Economics Track (remaining courses)
    {
      id: "C4",
      title: "Public Health 101",
      track: "Policy & Economics",
      description: "Basics of public health interventions and metrics",
      quote: "Essential tools for improving community health outcomes",
      level: "Beginner",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/ph",
      popular: true
    },
    {
      id: "C7",
      title: "Law and Constitution 101",
      track: "Policy & Economics",
      description: "Legal frameworks and constitutional principles",
      quote: "Understanding the foundation of legal systems",
      level: "Beginner",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/Law&Cons"
    },
    {
      id: "C10",
      title: "Pedagogy and Education 101",
      track: "Policy & Economics",
      description: "Educational theories and pedagogical approaches",
      quote: "Transforming learning through effective teaching",
      level: "Beginner",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/edu"
    },
    {
      id: "C11",
      title: "Livelihoods 101",
      track: "Policy & Economics",
      description: "Sustainable livelihood approaches and frameworks",
      quote: "Building resilient economic foundations",
      level: "Beginner",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/Livelihoods"
    },
    {
      id: "C12",
      title: "Advocacy and Communications 101",
      track: "Policy & Economics",
      description: "Strategic advocacy and communication for policy change",
      quote: "Amplifying voices for systemic change",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/adv&comm"
    },
    {
      id: "C14",
      title: "Monitoring, Evaluation, Accountability and Learning 101",
      track: "Policy & Economics",
      description: "MEAL frameworks for development programs",
      quote: "Measuring impact for continuous improvement",
      level: "Intermediate",
      duration: "4 hours",
      content: "https://101.www.impactmojo.in/MEAL"
    },
    {
      id: "C15",
      title: "Political Economy 101",
      track: "Policy & Economics",
      description: "Intersection of politics and economics in development",
      quote: "Understanding power dynamics in economic systems",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/polecon"
    },
    {
      id: "C18",
      title: "Poverty and Inequality 101",
      track: "Policy & Economics",
      description: "Analysis of poverty dynamics and inequality patterns",
      quote: "Confronting the root causes of inequality",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/pov&inq"
    },
    {
      id: "C21",
      title: "Decolonising Development 101",
      track: "Policy & Economics",
      description: "Critical perspectives on development practice",
      quote: "Reimagining development from the ground up",
      level: "Advanced",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/decolonD"
    },
    {
      id: "C22",
      title: "Environmental Justice 101",
      track: "Policy & Economics",
      description: "Intersection of environment and social justice",
      quote: "Environmental protection as social equity",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/env-jus"
    },
    {
      id: "C23",
      title: "Community Development 101",
      track: "Policy & Economics",
      description: "Participatory approaches to community-led development",
      quote: "Empowering communities as agents of change",
      level: "Beginner",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/community-dev"
    },
    {
      id: "C24",
      title: "Post-Truth Politics 101",
      track: "Policy & Economics",
      description: "Information, misinformation, and political discourse",
      quote: "Navigating truth in the information age",
      level: "Intermediate",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/post-truth-pol"
    },
    {
      id: "C25",
      title: "Global Development Architecture 101",
      track: "Policy & Economics",
      description: "Structure and dynamics of the development sector",
      quote: "Understanding the global development ecosystem",
      level: "Intermediate",
      duration: "3.5 hours",
      content: "https://101.www.impactmojo.in/GDArch"
    },
    {
      id: "C26",
      title: "Fundraising 101",
      track: "Policy & Economics",
      description: "Resource mobilization for development organizations",
      quote: "Securing resources for lasting impact",
      level: "Beginner",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/fundraising"
    },
    {
      id: "C32",
      title: "Decent Work 101",
      track: "Policy & Economics",
      description: "Labor rights and quality employment in development",
      quote: "Dignity and fairness in work",
      level: "Intermediate",
      duration: "2.5 hours",
      content: "https://101.www.impactmojo.in/DecentWork"
    },
    {
      id: "C33",
      title: "Social Welfare and Safety Nets 101",
      track: "Policy & Economics",
      description: "Social protection systems and policy design",
      quote: "Building resilient communities through social protection",
      level: "Intermediate",
      duration: "3 hours",
      content: "https://101.www.impactmojo.in/safetynets"
    }
  ],

  upcomingCourses: [
    {
      id: "UC1",
      title: "English for All",
      description: "Communication skills for global impact",
      subtitle: "Breaking language barriers for inclusive development",
      status: "Coming Soon!"
    },
    {
      id: "UC2", 
      title: "Tech for All",
      description: "Technology literacy for everyone",
      subtitle: "10 future technologies: IoT, AI, Robotics, Blockchain, Cybersecurity, and more",
      status: "Coming Soon!"
    }
  ],

  labs: [
    {
      id: "L1",
      title: "Climate Risk Mitigation Timeline",
      topic: "Climate",
      description: "Interactive timeline of climate resilience efforts and mitigation strategies",
      icon: "🌍",
      content: "https://impactrisk-mitigation.netlify.app/"
    },
    {
      id: "L2",
      title: "Community Engagement Timeline",
      topic: "Gender",
      description: "Historical progression of community engagement in gender equality",
      icon: "⚖️",
      content: "https://community-engagement.netlify.app/"
    },
    {
      id: "L3",
      title: "Policy Advocacy Timeline",
      topic: "Policy", 
      description: "Evolution of key policy advocacy frameworks and strategies",
      icon: "📋",
      content: "https://pol-advocacy4impact.netlify.app/"
    },
    {
      id: "L4",
      title: "Development Economics Case Studies",
      topic: "Economics",
      description: "Real-world applications of development economics principles",
      icon: "💰",
      content: "/labs/devecon-cases.html"
    },
    {
      id: "L5",
      title: "Data Analysis Workshop",
      topic: "Data",
      description: "Hands-on exercises in data collection and analysis",
      icon: "📊",
      content: "/labs/data-workshop.html"
    },
    {
      id: "L6",
      title: "Research Ethics Scenarios",
      topic: "Ethics",
      description: "Interactive scenarios for research ethics decision-making",
      icon: "🔬",
      content: "/labs/ethics-scenarios.html"
    },
    {
      id: "L7",
      title: "Public Health Interventions Simulator",
      topic: "Health",
      description: "Simulate public health interventions and measure outcomes",
      icon: "🏥",
      content: "/labs/health-simulator.html"
    },
    {
      id: "L8",
      title: "Gender Analysis Framework",
      topic: "Gender",
      description: "Apply gender analysis tools to development scenarios",
      icon: "👥",
      content: "/labs/gender-analysis.html"
    },
    {
      id: "L9",
      title: "Policy Design Laboratory",
      topic: "Policy",
      description: "Design and test policy interventions in virtual environments",
      icon: "🏛️",
      content: "/labs/policy-lab.html"
    },
    {
      id: "L10",
      title: "Environmental Justice Mapping",
      topic: "Environment",
      description: "Map environmental justice issues using interactive tools",
      icon: "🗺️",
      content: "/labs/envjustice-mapping.html"
    }
  ],

  tracks: [
    {
      name: "Research Methods",
      description: "Learn systematic approaches to research and data collection",
      icon: "🔬",
      color: "bg-blue-500",
      borderColor: "border-blue-500",
      textColor: "text-blue-600",
      bgLight: "bg-blue-50",
      bgDark: "dark:bg-blue-900"
    },
    {
      name: "Data Analysis",
      description: "Master tools and techniques for analyzing complex data",
      icon: "📊",
      color: "bg-green-500",
      borderColor: "border-green-500",
      textColor: "text-green-600",
      bgLight: "bg-green-50",
      bgDark: "dark:bg-green-900"
    },
    {
      name: "Gender Studies",
      description: "Explore gender theory and its real-world applications",
      icon: "⚖️",
      color: "bg-purple-500",
      borderColor: "border-purple-500",
      textColor: "text-purple-600",
      bgLight: "bg-purple-50",
      bgDark: "dark:bg-purple-900"
    },
    {
      name: "Policy & Economics",
      description: "Understand policy frameworks and economic principles",
      icon: "🏛️",
      color: "bg-orange-500",
      borderColor: "border-orange-500",
      textColor: "text-orange-600",
      bgLight: "bg-orange-50",
      bgDark: "dark:bg-orange-900"
    }
  ],

  resources: [
    {
      id: "R1",
      title: "Development Jargon Buster",
      type: "PDF",
      description: "Comprehensive glossary of development terms and acronyms",
      link: "/assets/resources/jargon-buster.pdf",
      category: "Reference"
    },
    {
      id: "R2",
      title: "Research Toolkit",
      type: "PDF",
      description: "Essential tools and templates for development researchers",
      link: "/assets/resources/research-toolkit.pdf",
      category: "Research"
    },
    {
      id: "R3",
      title: "Gender Analysis Frameworks",
      type: "PDF",
      description: "Comprehensive guide to gender analysis methodologies",
      link: "/assets/resources/gender-analysis-frameworks.pdf",
      category: "Gender"
    },
    {
      id: "R4",
      title: "Data Collection Templates",
      type: "Excel",
      description: "Ready-to-use templates for various data collection methods",
      link: "/assets/resources/data-collection-templates.xlsx",
      category: "Data"
    },
    {
      id: "R5",
      title: "Policy Brief Template",
      type: "Word",
      description: "Professional template for writing effective policy briefs",
      link: "/assets/resources/policy-brief-template.docx",
      category: "Policy"
    }
  ],

  featuredContent: {
    id: "FC1",
    title: "The Real Middle Game",
    description: "Deep dive into the complexities of development practice - navigating the challenging middle ground between theory and implementation",
    link: "/features/real-middle-game.html"
  },

  // Quiz Questions for Find Your Track
  quizQuestions: [
    {
      id: 1,
      question: "What interests you most about development work?",
      answers: [
        { text: "Understanding how data tells stories", track: "Data Analysis", points: 3 },
        { text: "Designing and conducting research studies", track: "Research Methods", points: 3 },
        { text: "Analyzing gender dynamics and equity", track: "Gender Studies", points: 3 },
        { text: "Shaping policies and economic systems", track: "Policy & Economics", points: 3 }
      ]
    },
    {
      id: 2,
      question: "When tackling a development challenge, you prefer to:",
      answers: [
        { text: "Collect and analyze quantitative evidence", track: "Data Analysis", points: 2 },
        { text: "Design rigorous studies to understand the problem", track: "Research Methods", points: 2 },
        { text: "Examine how the issue affects different groups", track: "Gender Studies", points: 2 },
        { text: "Develop policy solutions and economic frameworks", track: "Policy & Economics", points: 2 }
      ]
    },
    {
      id: 3,
      question: "Your ideal development outcome focuses on:",
      answers: [
        { text: "Evidence-based program improvements", track: "Data Analysis", points: 2 },
        { text: "Methodologically sound research findings", track: "Research Methods", points: 2 },
        { text: "Reduced gender inequality and social justice", track: "Gender Studies", points: 2 },
        { text: "Systemic policy change and economic growth", track: "Policy & Economics", points: 2 }
      ]
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

  // Modal states
  const [showBookmarkModal, setShowBookmarkModal] = useState(false);
  const [showCompareModal, setShowCompareModal] = useState(false);
  const [showFeedbackModal, setShowFeedbackModal] = useState(false);
  const [showSuggestModal, setShowSuggestModal] = useState(false);
  const [showQuizModal, setShowQuizModal] = useState(false);

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

  // Apply dark mode
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
  }, [darkMode]);

  const toggleTheme = () => setDarkMode(!darkMode);

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
            
            {/* FAB Buttons */}
            <FloatingActionButtons 
              onBookmark={() => setShowBookmarkModal(true)}
              onCompare={() => setShowCompareModal(true)}
              onFeedback={() => setShowFeedbackModal(true)}
              onSuggest={() => setShowSuggestModal(true)}
              bookmarkCount={bookmarks.length}
              compareCount={compareList.length}
            />
            
            <Footer />
            
            {/* Modals */}
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

            {showBookmarkModal && (
              <BookmarkModal 
                bookmarks={bookmarks}
                onClose={() => setShowBookmarkModal(false)}
              />
            )}

            {showCompareModal && (
              <CompareModal 
                compareList={compareList}
                onClose={() => setShowCompareModal(false)}
              />
            )}

            {showFeedbackModal && (
              <FeedbackModal onClose={() => setShowFeedbackModal(false)} />
            )}

            {showSuggestModal && (
              <SuggestModal onClose={() => setShowSuggestModal(false)} />
            )}

            {showQuizModal && (
              <QuizModal onClose={() => setShowQuizModal(false)} />
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

// HomePage Component - Following exact web developer specs
function HomePage() {
  const { setCurrentPage } = useAuth();
  const [showQuizModal, setShowQuizModal] = useState(false);
  
  // Get popular courses (4-6 courses)
  const popularCourses = courseData.courses.filter(course => course.popular).slice(0, 6);

  return (
    <div className="space-y-16">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-20">
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
            className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
          >
            Start Learning
          </button>
        </div>
      </section>

      {/* Popular Courses with Quotes */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4">Popular Courses</h2>
          <p className="text-lg text-gray-600 dark:text-gray-400">
            Highlighted selection with learner testimonials
          </p>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {popularCourses.map((course) => (
            <CourseCard key={course.id} course={course} showQuote={true} />
          ))}
        </div>
      </section>

      {/* Upcoming Courses Section - English for All & Tech for All */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4">Upcoming Courses</h2>
          <p className="text-lg text-gray-600 dark:text-gray-400">
            New content coming soon to expand your learning journey
          </p>
        </div>
        <div className="grid md:grid-cols-2 gap-8">
          {courseData.upcomingCourses.map((course) => (
            <UpcomingCourseCard key={course.id} course={course} />
          ))}
        </div>
      </section>

      {/* Featured Content Section - The Real Middle Game */}
      <section className="bg-blue-50 dark:bg-blue-900 py-16 transition-colors">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-8 shadow-lg transition-colors">
            <div className="flex justify-center mb-4">
              <Star className="w-8 h-8 text-yellow-500" />
            </div>
            <h2 className="text-2xl font-bold mb-2">Featured Content</h2>
            <h3 className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-4">
              {courseData.featuredContent.title}
            </h3>
            <p className="text-lg mb-6 text-gray-600 dark:text-gray-400">
              {courseData.featuredContent.description}
            </p>
            <a
              href={courseData.featuredContent.link}
              className="inline-flex items-center bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
            >
              <ExternalLink className="w-5 h-5 mr-2" />
              Explore Featured Content
            </a>
          </div>
        </div>
      </section>

      {/* Four Learning Tracks */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4">Four Learning Tracks</h2>
          <p className="text-lg text-gray-600 dark:text-gray-400">
            Explore courses organized by key development themes
          </p>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {courseData.tracks.map((track) => (
            <TrackCard 
              key={track.name} 
              track={track} 
              onSelect={() => setCurrentPage('courses')}
              courseCount={courseData.courses.filter(c => c.track === track.name).length}
            />
          ))}
        </div>
      </section>

      {/* Find Your Own Track Quiz */}
      <section className="bg-gray-50 dark:bg-gray-800 py-16 transition-colors">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="flex justify-center mb-6">
            <Target className="w-12 h-12 text-purple-600" />
          </div>
          <h2 className="text-3xl font-bold mb-6">Find Your Own Track</h2>
          <p className="text-lg mb-8 text-gray-600 dark:text-gray-400">
            Not sure where to start? Take our interactive quiz to discover the learning path that fits your interests and goals.
          </p>
          <button 
            onClick={() => setShowQuizModal(true)}
            className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors"
          >
            <Lightbulb className="inline-block w-5 h-5 mr-2" />
            Start Quiz
          </button>
        </div>
      </section>

      {/* Extras/Resources Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4">Handouts & Resources</h2>
          <p className="text-lg text-gray-600 dark:text-gray-400">
            Downloadable guides and references to support your learning
          </p>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {courseData.resources.slice(0, 6).map((resource) => (
            <ResourceCard key={resource.id} resource={resource} />
          ))}
        </div>
        <div className="text-center mt-8">
          <button
            onClick={() => setCurrentPage('resources')}
            className="text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-medium"
          >
            View all resources →
          </button>
        </div>
      </section>

      {/* Social Box and About Maker */}
      <section className="bg-gray-50 dark:bg-gray-800 py-16 transition-colors">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-white dark:bg-gray-700 rounded-lg p-8 shadow-lg">
            <div className="mb-6">
              <img
                src="https://via.placeholder.com/120"
                alt="Varna Sri Raman"
                className="w-24 h-24 rounded-full mx-auto mb-4 border-4 border-blue-500"
              />
              <h3 className="text-2xl font-bold mb-2">About the Maker</h3>
              <p className="text-gray-600 dark:text-gray-400 mb-6">
                Created by <strong>Varna Sri Raman</strong> - Development economist passionate about democratizing knowledge for social impact. Building bridges between research and practice.
              </p>
              <div className="flex justify-center space-x-6">
                <a href="https://www.threads.com/@varnasriraman" className="text-blue-600 hover:text-blue-700 font-medium" target="_blank" rel="noopener noreferrer">
                  Threads
                </a>
                <a href="https://vfolio.notion.site/" className="text-blue-600 hover:text-blue-700 font-medium" target="_blank" rel="noopener noreferrer">
                  Notion
                </a>
                <a href="https://www.linkedin.com/in/varna/" className="text-blue-600 hover:text-blue-700 font-medium" target="_blank" rel="noopener noreferrer">
                  LinkedIn
                </a>
                <a href="https://varna.substack.com/" className="text-blue-600 hover:text-blue-700 font-medium" target="_blank" rel="noopener noreferrer">
                  Substack
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Quiz Modal */}
      {showQuizModal && (
        <QuizModal onClose={() => setShowQuizModal(false)} />
      )}
    </div>
  );
}

// Course Card Component
function CourseCard({ course, showQuote = false }) {
  const { toggleBookmark, toggleCompare, bookmarks, compareList, user } = useAuth();
  const isBookmarked = bookmarks.includes(course.id);
  const isCompared = compareList.includes(course.id);

  const track = courseData.tracks.find(t => t.name === course.track);

  return (
    <div className={`bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-all duration-300 ${track?.borderColor} border-l-4`}>
      <div className="p-6">
        <div className="flex justify-between items-start mb-3">
          <div className="flex items-center space-x-2">
            <span className={`px-2 py-1 text-xs font-bold ${track?.bgLight} ${track?.bgDark} ${track?.textColor} rounded`}>
              {course.id}
            </span>
            <span className={`px-2 py-1 text-xs font-semibold ${track?.bgLight} ${track?.bgDark} ${track?.textColor} rounded`}>
              {course.track}
            </span>
          </div>
          {user && (
            <div className="flex space-x-1">
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  toggleBookmark(course.id);
                }}
                className={`p-1 rounded transition-colors ${isBookmarked ? 'text-yellow-500' : 'text-gray-400 hover:text-yellow-500'}`}
              >
                <Bookmark className="w-4 h-4" fill={isBookmarked ? 'currentColor' : 'none'} />
              </button>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  toggleCompare(course.id);
                }}
                className={`p-1 rounded transition-colors ${isCompared ? 'text-blue-500' : 'text-gray-400 hover:text-blue-500'}`}
              >
                <GitCompare className="w-4 h-4" />
              </button>
            </div>
          )}
        </div>
        
        <h3 className="text-lg font-bold text-gray-900 dark:text-gray-100 mb-2">
          {course.title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-400 text-sm mb-3">
          {course.description}
        </p>
        
        {showQuote && course.quote && (
          <blockquote className="text-gray-500 dark:text-gray-500 text-sm italic mb-4 pl-4 border-l-2 border-gray-300 dark:border-gray-600">
            "{course.quote}"
          </blockquote>
        )}
        
        <div className="flex justify-between items-center text-sm text-gray-500 dark:text-gray-400 mb-4">
          <span className="flex items-center">
            <Award className="w-4 h-4 mr-1" />
            {course.level}
          </span>
          <span className="flex items-center">
            <Clock className="w-4 h-4 mr-1" />
            {course.duration}
          </span>
        </div>

        <a
          href={course.content}
          target="_blank"
          rel="noopener noreferrer"
          className="block w-full bg-blue-600 hover:bg-blue-700 text-white text-center py-2 rounded-md transition-colors"
        >
          <ExternalLink className="inline-block w-4 h-4 mr-2" />
          Start Course
        </a>
      </div>
    </div>
  );
}

// Upcoming Course Card Component
function UpcomingCourseCard({ course }) {
  return (
    <div className="bg-gradient-to-br from-gray-100 to-gray-200 dark:from-gray-800 dark:to-gray-700 rounded-lg p-6 text-center opacity-75 transition-colors">
      <div className="mb-4">
        <Clock className="w-12 h-12 mx-auto text-gray-500 dark:text-gray-400 mb-2" />
      </div>
      <h3 className="text-2xl font-bold mb-2">{course.title}</h3>
      <p className="text-gray-600 dark:text-gray-300 mb-2">{course.description}</p>
      <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">{course.subtitle}</p>
      <span className="inline-block bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 px-4 py-2 rounded-full text-sm font-semibold">
        {course.status}
      </span>
    </div>
  );
}

// Track Card Component
function TrackCard({ track, onSelect, courseCount }) {
  return (
    <div 
      onClick={onSelect}
      className={`${track.bgLight} ${track.bgDark} rounded-lg p-6 hover:shadow-lg transition-all duration-300 cursor-pointer transform hover:scale-105`}
    >
      <div className={`w-16 h-16 ${track.color} rounded-lg flex items-center justify-center mb-4 mx-auto`}>
        <span className="text-3xl">{track.icon}</span>
      </div>
      
      <h3 className="text-xl font-bold text-center mb-2">
        {track.name}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-400 text-sm text-center mb-3">
        {track.description}
      </p>

      <div className="text-center">
        <span className={`text-sm font-semibold ${track.textColor}`}>
          {courseCount} courses
        </span>
      </div>
    </div>
  );
}

// Resource Card Component
function ResourceCard({ resource }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start mb-3">
        <span className="inline-block px-2 py-1 text-xs font-semibold bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 rounded">
          {resource.type}
        </span>
        <Download className="w-5 h-5 text-gray-400" />
      </div>
      
      <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
        {resource.title}
      </h3>
      
      <p className="text-gray-600 dark:text-gray-400 text-sm mb-4">
        {resource.description}
      </p>
      
      <a
        href={resource.link}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-md text-sm transition-colors"
      >
        <Download className="w-4 h-4 mr-2" />
        Download {resource.type}
      </a>
    </div>
  );
}

// Floating Action Buttons Component
function FloatingActionButtons({ onBookmark, onCompare, onFeedback, onSuggest, bookmarkCount, compareCount }) {
  const { user } = useAuth();

  const fabButtons = [
    {
      icon: Bookmark,
      onClick: onBookmark,
      className: "bg-yellow-500 hover:bg-yellow-600",
      position: "bottom-4 right-4",
      badge: user ? bookmarkCount : null
    },
    {
      icon: GitCompare,
      onClick: onCompare,
      className: "bg-blue-500 hover:bg-blue-600",
      position: "bottom-20 right-4",
      badge: user ? compareCount : null
    },
    {
      icon: MessageCircle,
      onClick: onFeedback,
      className: "bg-green-500 hover:bg-green-600",
      position: "bottom-36 right-4"
    },
    {
      icon: Plus,
      onClick: onSuggest,
      className: "bg-purple-500 hover:bg-purple-600",
      position: "bottom-52 right-4"
    }
  ];

  return (
    <div className="fixed z-40">
      {fabButtons.map((button, index) => (
        <button
          key={index}
          onClick={button.onClick}
          className={`fixed ${button.position} ${button.className} text-white p-3 rounded-full shadow-lg transition-colors`}
        >
          <button.icon className="w-6 h-6" />
          {button.badge > 0 && (
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {button.badge}
            </span>
          )}
        </button>
      ))}
    </div>
  );
}

// Quiz Modal Component
function QuizModal({ onClose }) {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [result, setResult] = useState(null);
  const { setCurrentPage } = useAuth();

  const handleAnswer = (answer) => {
    const newAnswers = [...answers, answer];
    setAnswers(newAnswers);

    if (currentQuestion < courseData.quizQuestions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      // Calculate result
      const trackScores = {};
      newAnswers.forEach(answer => {
        trackScores[answer.track] = (trackScores[answer.track] || 0) + answer.points;
      });
      
      const recommendedTrack = Object.entries(trackScores).reduce((a, b) => 
        trackScores[a[0]] > trackScores[b[0]] ? a : b
      )[0];
      
      const track = courseData.tracks.find(t => t.name === recommendedTrack);
      const trackCourses = courseData.courses.filter(c => c.track === recommendedTrack);
      
      setResult({ track, courses: trackCourses });
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setAnswers([]);
    setResult(null);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        {!result ? (
          <div className="p-6">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold">Find Your Track</h2>
              <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
                <X className="w-6 h-6" />
              </button>
            </div>
            
            <div className="mb-6">
              <div className="flex justify-between text-sm text-gray-500 mb-2">
                <span>Question {currentQuestion + 1} of {courseData.quizQuestions.length}</span>
                <span>{Math.round(((currentQuestion) / courseData.quizQuestions.length) * 100)}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${((currentQuestion) / courseData.quizQuestions.length) * 100}%` }}
                ></div>
              </div>
            </div>

            <div className="mb-8">
              <h3 className="text-xl font-semibold mb-6">
                {courseData.quizQuestions[currentQuestion].question}
              </h3>
              <div className="space-y-3">
                {courseData.quizQuestions[currentQuestion].answers.map((answer, index) => (
                  <button
                    key={index}
                    onClick={() => handleAnswer(answer)}
                    className="w-full text-left p-4 rounded-lg border border-gray-200 dark:border-gray-600 hover:border-blue-500 hover:bg-blue-50 dark:hover:bg-blue-900 transition-colors"
                  >
                    {answer.text}
                  </button>
                ))}
              </div>
            </div>
          </div>
        ) : (
          <div className="p-6">
            <div className="text-center mb-8">
              <div className={`w-20 h-20 ${result.track.color} rounded-full flex items-center justify-center mx-auto mb-4`}>
                <span className="text-4xl">{result.track.icon}</span>
              </div>
              <h2 className="text-3xl font-bold mb-2">Your Recommended Track:</h2>
              <h3 className="text-2xl font-semibold text-blue-600 dark:text-blue-400 mb-4">
                {result.track.name}
              </h3>
              <p className="text-lg text-gray-600 dark:text-gray-400 mb-6">
                {result.track.description}
              </p>
            </div>

            <div className="mb-8">
              <h4 className="text-lg font-semibold mb-4">Recommended Courses:</h4>
              <div className="space-y-2">
                {result.courses.slice(0, 3).map(course => (
                  <div key={course.id} className="flex items-center p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <span className="font-medium text-sm text-blue-600 dark:text-blue-400 mr-3">
                      {course.id}
                    </span>
                    <span className="flex-1">{course.title}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="flex space-x-4">
              <button
                onClick={() => {
                  setCurrentPage('courses');
                  onClose();
                }}
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-medium transition-colors"
              >
                Explore Courses
              </button>
              <button
                onClick={resetQuiz}
                className="px-6 py-3 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
              >
                Retake Quiz
              </button>
            </div>

            <button
              onClick={onClose}
              className="absolute top-4 right-4 text-gray-500 hover:text-gray-700"
            >
              <X className="w-6 h-6" />
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

// Other page components (simplified for space)
function DashboardPage() {
  const { user, bookmarks, compareList } = useAuth();
  
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
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">
          Welcome back, {user.displayName?.split(' ')[0]}!
        </h1>
        
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold mb-4">Your Learning Progress</h2>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {courseData.tracks.map((track) => (
                  <div key={track.name} className="text-center">
                    <div className={`w-16 h-16 ${track.color} rounded-full flex items-center justify-center mx-auto mb-2`}>
                      <span className="text-2xl">{track.icon}</span>
                    </div>
                    <h3 className="font-medium text-sm">{track.name}</h3>
                    <p className="text-xs text-gray-500">0 completed</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
          
          <div className="space-y-6">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold mb-4">Bookmarked Items</h2>
              <p className="text-gray-600 dark:text-gray-400">{bookmarks.length} items saved</p>
            </div>
            
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold mb-4">Comparisons</h2>
              <p className="text-gray-600 dark:text-gray-400">{compareList.length} items selected</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function CoursesPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('All');

  const filteredCourses = courseData.courses.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         course.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTrack = selectedTrack === 'All' || course.track === selectedTrack;
    return matchesSearch && matchesTrack;
  });

  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">All Courses</h1>
        
        {/* Search and Filter */}
        <div className="mb-8 flex flex-col sm:flex-row gap-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
            <input
              type="text"
              placeholder="Search courses..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
            />
          </div>
          <select
            value={selectedTrack}
            onChange={(e) => setSelectedTrack(e.target.value)}
            className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          >
            <option value="All">All Tracks</option>
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

function LabCard({ lab }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="p-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center">
            <span className="text-2xl mr-3">{lab.icon}</span>
            <span className="px-2 py-1 text-xs font-semibold bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 rounded">
              {lab.id}
            </span>
          </div>
          <span className="text-xs text-gray-500">{lab.topic}</span>
        </div>
        
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
          {lab.title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-400 text-sm mb-4">
          {lab.description}
        </p>
        
        <a
          href={lab.content}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md text-sm transition-colors"
        >
          <ExternalLink className="w-4 h-4 mr-2" />
          Launch Lab
        </a>
      </div>
    </div>
  );
}

function ResourcesPage() {
  return (
    <div className="py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">Resources</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
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

          <h2>Learning Tracks</h2>
          <p>Our content is organized into four key tracks:</p>
          <ul>
            <li><strong>Research Methods:</strong> Systematic approaches to research and data collection</li>
            <li><strong>Data Analysis:</strong> Tools and techniques for analyzing complex data</li>
            <li><strong>Gender Studies:</strong> Gender theory and its real-world applications</li>
            <li><strong>Policy & Economics:</strong> Policy frameworks and economic principles</li>
          </ul>
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
            <div className="space-y-4">
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
              
              <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition-colors">
                <Send className="inline-block w-4 h-4 mr-2" />
                Send Message
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// Modal Components
function BookmarkModal({ bookmarks, onClose }) {
  const bookmarkedItems = bookmarks.map(id => {
    const course = courseData.courses.find(c => c.id === id);
    const lab = courseData.labs.find(l => l.id === id);
    const resource = courseData.resources.find(r => r.id === id);
    return course || lab || resource;
  }).filter(Boolean);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full max-h-[80vh] overflow-y-auto">
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold">Your Bookmarks</h2>
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X className="w-6 h-6" />
            </button>
          </div>
          
          {bookmarkedItems.length === 0 ? (
            <div className="text-center py-8">
              <Bookmark className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500">You haven't bookmarked any content yet.</p>
              <p className="text-sm text-gray-400">Hit the bookmark icon on courses or labs to save them here.</p>
            </div>
          ) : (
            <div className="space-y-4">
              {bookmarkedItems.map((item) => (
                <div key={item.id} className="flex items-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                  <span className="font-medium text-blue-600 dark:text-blue-400 mr-3">
                    {item.id}
                  </span>
                  <div className="flex-1">
                    <h3 className="font-medium">{item.title}</h3>
                    <p className="text-sm text-gray-500">{item.description}</p>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function CompareModal({ compareList, onClose }) {
  const compareItems = compareList.map(id => {
    return courseData.courses.find(c => c.id === id);
  }).filter(Boolean);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[80vh] overflow-y-auto">
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold">Course Comparison</h2>
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X className="w-6 h-6" />
            </button>
          </div>
          
          {compareItems.length === 0 ? (
            <div className="text-center py-8">
              <GitCompare className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500">No courses selected for comparison.</p>
              <p className="text-sm text-gray-400">Use the compare icon on course cards to add them here.</p>
            </div>
          ) : (
            <div className="grid md:grid-cols-2 gap-6">
              {compareItems.map((course) => (
                <div key={course.id} className="border rounded-lg p-4">
                  <h3 className="font-bold text-lg mb-2">{course.title}</h3>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">Track: {course.track}</p>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">Level: {course.level}</p>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">Duration: {course.duration}</p>
                  <p className="text-sm">{course.description}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function FeedbackModal({ onClose }) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold">Send Feedback</h2>
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X className="w-6 h-6" />
            </button>
          </div>
          
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Feedback</label>
              <textarea
                rows={4}
                placeholder="Share your thoughts about ImpactMojo..."
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700"
              ></textarea>
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-1">Email (optional)</label>
              <input
                type="email"
                placeholder="your@email.com"
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700"
              />
            </div>
            
            <button className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded-md transition-colors">
              <Send className="inline-block w-4 h-4 mr-2" />
              Send Feedback
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function SuggestModal({ onClose }) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold">Suggest a Course</h2>
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X className="w-6 h-6" />
            </button>
          </div>
          
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Course Title</label>
              <input
                type="text"
                placeholder="e.g., Sustainable Finance 101"
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-1">Description</label>
              <textarea
                rows={3}
                placeholder="What should this course cover?"
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700"
              ></textarea>
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-1">Track</label>
              <select className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-700">
                <option>Select a track...</option>
                {courseData.tracks.map(track => (
                  <option key={track.name} value={track.name}>{track.name}</option>
                ))}
              </select>
            </div>
            
            <button className="w-full bg-purple-600 hover:bg-purple-700 text-white py-2 rounded-md transition-colors">
              <Plus className="inline-block w-4 h-4 mr-2" />
              Submit Suggestion
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

// Other components
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

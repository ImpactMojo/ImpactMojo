import './emergency-fix';  // ADD THIS LINE AT THE VERY TOP!

// ... rest of your App.js code stays the same
import React, { useContext } from 'react';

// This file is the central point and can correctly find all the other files.
import { PageProvider, AuthProvider, usePage, useAuth } from './context/AppContext.js';
import { 
    HomePage, CoursesPage, LabsPage, GamesPage, ResourcesPage, 
    AboutPage, FAQPage, DashboardPage, AIToolsPage 
} from './pages/index.js';
import { 
    Navigation, ImprovedFloatingActionButtons, Footer 
} from './components/index.js';

// The main App component now passes all necessary context down as props.
function App() {
  const { currentPage, setCurrentPage, darkMode, toggleDarkMode } = usePage();
  const { user, signIn, signOut } = useAuth();

  const renderPage = () => {
    switch (currentPage) {
      case 'home': return <HomePage />;
      case 'courses': return <CoursesPage />;
      case 'labs': return <LabsPage />;
      case 'games': return <GamesPage />;
      case 'resources': return <ResourcesPage />;
      case 'about': return <AboutPage />;
      case 'faq': return <FAQPage />;
      case 'dashboard': return <DashboardPage user={user} />; 
      case 'ai-tools': return <AIToolsPage />;
      default: return <HomePage />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      {/* We are now "handing" the data directly to the Navigation component */}
      <Navigation
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        darkMode={darkMode}
        toggleDarkMode={toggleDarkMode}
        user={user}
        signIn={signIn}
        signOut={signOut}
      />
      <main>{renderPage()}</main>
      <ImprovedFloatingActionButtons />
      <Footer />
    </div>
  );
}

// The final component that wraps the entire app.
const AppWithProviders = () => (
  <AuthProvider>
    <PageProvider>
      <App />
    </PageProvider>
  </AuthProvider>
);

export default AppWithProviders;


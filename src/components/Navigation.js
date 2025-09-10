import React, { useState } from 'react';
import { Menu, X, Sun, Moon } from 'lucide-react';
// CORRECTED IMPORT: This path goes up one folder, then into the context folder.
import { usePage, useAuth } from '../context/AppContext.js';

const Navigation = () => {
  const { currentPage, setCurrentPage, darkMode, toggleDarkMode } = usePage();
  const { user, signIn, signOut } = useAuth();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Using your existing, detailed navigation component code
  return (
    <nav className="bg-white dark:bg-gray-900 shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20">
          <div className="flex items-center">
             <button onClick={() => setCurrentPage('home')} className="flex items-center space-x-4">
               <img src="/assets/ImpactMojo Logo.png" alt="ImpactMojo Logo" className="h-20 w-20 object-contain" onError={(e) => { e.target.src = "/assets/android-chrome-192x192.png"; }}/>
               <div className="flex flex-col">
                 <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">ImpactMojo</span>
                 <span className="text-sm text-gray-600 dark:text-gray-300 font-medium">Development Know-How</span>
               </div>
             </button>
          </div>
          <div className="hidden sm:ml-8 sm:flex sm:space-x-8 items-center">
            {['home', 'courses', 'labs', 'games', 'resources'].map((page) => (
              <button key={page} onClick={() => setCurrentPage(page)} className={`${currentPage === page ? 'border-blue-600 text-gray-900 dark:text-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium capitalize`}>{page}</button>
            ))}
          </div>
          <div className="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
            <button onClick={toggleDarkMode} className="p-2 rounded-md text-gray-400">{darkMode ? <Sun /> : <Moon />}</button>
            {user ? (
              <div className="flex items-center space-x-3">
                <span className="text-gray-700 dark:text-gray-300">{user.displayName}</span>
                <button onClick={signOut} className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium">Sign Out</button>
              </div>
            ) : (
              <button onClick={signIn} className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium">Sign In with Google</button>
            )}
          </div>
          <div className="-mr-2 flex items-center sm:hidden">
            <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="p-2 rounded-md">{isMenuOpen ? <X /> : <Menu />}</button>
          </div>
        </div>
      </div>
      {isMenuOpen && <div className="sm:hidden">{/* Mobile Menu content here */}</div>}
    </nav>
  );
};

export default Navigation;


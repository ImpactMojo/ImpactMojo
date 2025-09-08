// src/components/Navigation.js
import React, { useState } from 'react';
import { Menu, X, Sun, Moon } from 'lucide-react';
import { usePage, useAuth } from '../App';

const Navigation = () => {
  const { currentPage, setCurrentPage, darkMode, toggleDarkMode } = usePage();
  const { user, signIn, signOut } = useAuth();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="bg-white dark:bg-gray-900 shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <button 
                onClick={() => setCurrentPage('home')}
                className="flex items-center space-x-4"
              >
                <img 
                  src="/assets/ImpactMojo Logo.png"
                  alt="ImpactMojo Logo"
                  className="h-20 w-20 object-contain" // Increased size from h-16 w-16 to h-20 w-20
                  onError={(e) => {
                    e.target.src = "/assets/android-chrome-192x192.png";
                  }}
                />
                <div className="flex flex-col">
                  <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                    ImpactMojo
                  </span>
                  <span className="text-sm text-gray-600 dark:text-gray-300 font-medium">
                    Development Know-How
                  </span>
                </div>
              </button>
            </div>
            <div className="hidden sm:ml-8 sm:flex sm:space-x-8">
              {['home', 'courses', 'labs', 'games', 'resources'].map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  className={`${
                    currentPage === page 
                      ? 'border-blue-600 text-gray-900 dark:text-white' 
                      : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'
                  } inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium capitalize`}
                >
                  {page}
                </button>
              ))}
              {user && (
                <>
                  <button
                    onClick={() => setCurrentPage('dashboard')}
                    className={`${
                      currentPage === 'dashboard' 
                        ? 'border-blue-600 text-gray-900 dark:text-white' 
                        : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'
                    } inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
                  >
                    Dashboard
                  </button>
                  <button
                    onClick={() => setCurrentPage('about')}
                    className={`${
                      currentPage === 'about' 
                        ? 'border-blue-600 text-gray-900 dark:text-white' 
                        : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'
                    } inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
                  >
                    About
                  </button>
                  <button
                    onClick={() => setCurrentPage('faq')}
                    className={`${
                      currentPage === 'faq' 
                        ? 'border-blue-600 text-gray-900 dark:text-white' 
                        : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white'
                    } inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium`}
                  >
                    FAQ
                  </button>
                </>
              )}
            </div>
          </div>
          <div className="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
            <button
              onClick={toggleDarkMode}
              className="bg-gray-200 dark:bg-gray-700 relative inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
            >
              {darkMode ? <Sun className="block h-6 w-6" aria-hidden="true" /> : <Moon className="block h-6 w-6" aria-hidden="true" />}
            </button>
            {user ? (
              <div className="relative">
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
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium"
              >
                Sign In with Google
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
            {['home', 'courses', 'labs', 'games', 'resources'].map((page) => (
              <button
                key={page}
                onClick={() => {
                  setCurrentPage(page);
                  setIsMenuOpen(false);
                }}
                className={`${
                  currentPage === page 
                    ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' 
                    : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'
                } block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left capitalize`}
              >
                {page}
              </button>
            ))}
            {user && (
              <>
                <button
                  onClick={() => {
                    setCurrentPage('dashboard');
                    setIsMenuOpen(false);
                  }}
                  className={`${
                    currentPage === 'dashboard' 
                      ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' 
                      : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'
                  } block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left`}
                >
                  Dashboard
                </button>
                <button
                  onClick={() => {
                    setCurrentPage('about');
                    setIsMenuOpen(false);
                  }}
                  className={`${
                    currentPage === 'about' 
                      ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' 
                      : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'
                  } block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left`}
                >
                  About
                </button>
                <button
                  onClick={() => {
                    setCurrentPage('faq');
                    setIsMenuOpen(false);
                  }}
                  className={`${
                    currentPage === 'faq' 
                      ? 'bg-blue-50 dark:bg-blue-900 border-blue-500 text-blue-700 dark:text-blue-200' 
                      : 'border-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 hover:text-gray-800 dark:hover:text-white'
                  } block pl-3 pr-4 py-2 border-l-4 text-base font-medium w-full text-left`}
                >
                  FAQ
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

export default Navigation;

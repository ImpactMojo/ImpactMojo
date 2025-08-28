// src/pages/AIToolsPage.js
import React, { useState } from 'react';
import { Bot, ExternalLink, Star, ArrowRight } from 'lucide-react';
import { useAuth } from '../App';
import { aiToolsData } from '../data/ai-tools-data';

const AIToolsPage = () => {
  const { darkMode } = usePage();
  const { user, bookmarks, toggleBookmark, isPremium } = useAuth();
  const [selectedTool, setSelectedTool] = useState(null);
  
  if (!user) {
    return (
      <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="text-center">
            <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-heading">Please sign in to access AI Tools</h1>
            <p className="mt-4 text-lg text-gray-600 dark:text-gray-300 font-sans">AI Tools are available exclusively for logged-in users.</p>
          </div>
        </div>
      </div>
    );
  }
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-heading sm:text-4xl">
            AI-Powered Tools
          </h1>
          <p className="mt-3 max-w-2xl mx-auto text-xl text-gray-600 dark:text-gray-300 font-sans sm:mt-4">
            Leverage artificial intelligence to enhance your development work.
          </p>
        </div>
        
        {!isPremium && (
          <div className="mb-8 bg-gradient-to-r from-yellow-400 to-yellow-500 rounded-lg shadow-lg p-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-gray-900 font-heading">Upgrade to Premium</h3>
                <p className="mt-1 text-gray-800 font-sans">Unlock all AI tools and premium features</p>
              </div>
              <button className="px-4 py-2 bg-gray-900 text-white rounded-md hover:bg-gray-800 transition-colors font-sans">
                Upgrade Now
              </button>
            </div>
          </div>
        )}
        
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {aiToolsData.map(tool => (
            <div key={tool.id} className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
              <div className="p-6">
                <div className="flex justify-between items-start">
                  <div className="flex items-center">
                    <div className={`flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-md bg-${tool.color}-100 dark:bg-${tool.color}-900`}>
                      <tool.icon className={`h-6 w-6 text-${tool.color}-600 dark:text-${tool.color}-400`} />
                    </div>
                    <h3 className="ml-3 text-lg font-medium text-gray-900 dark:text-chalk-white font-heading">{tool.title}</h3>
                  </div>
                  <div className="flex items-center space-x-2">
                    {!isPremium && (
                      <span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 font-sans">
                        PRO
                      </span>
                    )}
                    <button 
                      onClick={() => toggleBookmark(tool.id)}
                      className="text-gray-400 hover:text-yellow-500 focus:outline-none"
                    >
                      {bookmarks.includes(tool.id) ? (
                        <Star className="h-5 w-5 text-yellow-500 fill-current" />
                      ) : (
                        <Star className="h-5 w-5" />
                      )}
                    </button>
                  </div>
                </div>
                
                <p className="mt-3 text-sm text-gray-600 dark:text-gray-300 font-sans">{tool.description}</p>
                
                <div className="mt-6">
                  {!isPremium ? (
                    <button
                      onClick={() => {}}
                      className="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-gray-500 bg-gray-200 dark:bg-gray-700 cursor-not-allowed font-sans"
                      disabled
                    >
                      Upgrade to Unlock
                    </button>
                  ) : (
                    <button
                      onClick={() => setSelectedTool(tool)}
                      className="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-accent-blue hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-blue font-sans"
                    >
                      Try This Tool
                      <ArrowRight className="ml-1 h-4 w-4" />
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
        
        {/* Tool Detail Modal */}
        {selectedTool && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
            <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
              <div className="p-6">
                <div className="flex justify-between items-start mb-4">
                  <div className="flex items-center">
                    <div className={`flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-md bg-${selectedTool.color}-100 dark:bg-${selectedTool.color}-900`}>
                      <selectedTool.icon className={`h-8 w-8 text-${selectedTool.color}-600 dark:text-${selectedTool.color}-400`} />
                    </div>
                    <h2 className="ml-4 text-2xl font-bold text-gray-900 dark:text-chalk-white font-heading">{selectedTool.title}</h2>
                  </div>
                  <button 
                    onClick={() => setSelectedTool(null)}
                    className="text-gray-500 hover:text-gray-700 dark:text-gray-300 dark:hover:text-gray-100"
                  >
                    <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
                
                <p className="text-gray-600 dark:text-gray-300 mb-6 font-sans">{selectedTool.description}</p>
                
                <div className="mb-6">
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-chalk-white font-heading mb-2">How to Use This Tool</h3>
                  <p className="text-gray-600 dark:text-gray-300 font-sans mb-4">
                    Fill in the details below to generate your customized output:
                  </p>
                  
                  <div className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 font-sans mb-1">
                        Project Details
                      </label>
                      <textarea 
                        rows={4}
                        className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-accent-blue focus:border-accent-blue dark:bg-chalkboard-dark dark:text-chalk-white font-sans"
                        placeholder={selectedTool.exampleInput}
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 font-sans mb-1">
                        Specific Requirements (optional)
                      </label>
                      <textarea 
                        rows={3}
                        className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-accent-blue focus:border-accent-blue dark:bg-chalkboard-dark dark:text-chalk-white font-sans"
                        placeholder="Add any specific requirements or context..."
                      />
                    </div>
                  </div>
                </div>
                
                <div className="flex justify-end space-x-3">
                  <button
                    onClick={() => setSelectedTool(null)}
                    className="px-4 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-md font-medium font-sans"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={() => {}}
                    className="px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-accent-blue hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-blue font-sans"
                  >
                    Generate
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default AIToolsPage;

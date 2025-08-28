// src/pages/ResourcesPage.js
import React from 'react';
import { FileText, BookOpen, Target, ExternalLink } from 'lucide-react';
import { usePage } from '../App';

const ResourcesPage = () => {
  const { darkMode } = usePage();
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-heading sm:text-4xl">
            Resources
          </h1>
          <p className="mt-3 max-w-2xl mx-auto text-xl text-gray-600 dark:text-gray-300 font-sans sm:mt-4">
            Access our collection of development resources, guides, and toolkits.
          </p>
        </div>
        
        <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-lg p-6 mb-8">
          <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-heading mb-4">Handouts & Resources</h2>
          <p className="text-gray-600 dark:text-gray-300 mb-6 font-sans">
            Browse our complete collection of handouts, guides, and toolkits in our GitHub repository.
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="mb-4 sm:mb-0">
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-sans">Complete Resources Library</h3>
              <p className="text-sm text-gray-600 dark:text-gray-300 font-sans">View and download all available resources</p>
            </div>
            <a 
              href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-accent-blue hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-blue font-sans"
            >
              Browse Resources
              <ExternalLink className="ml-2 h-4 w-4" />
            </a>
          </div>
        </div>
        
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-accent-blue dark:bg-blue-900 mb-4">
                <FileText className="h-6 w-6 text-white" />
              </div>
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-heading mb-2 font-sans">Development Frameworks</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4 font-sans">Comprehensive guides to major development frameworks and approaches.</p>
              <a 
                href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-medium font-sans"
              >
                View Resources
              </a>
            </div>
          </div>
          
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-accent-green dark:bg-green-900 mb-4">
                <BookOpen className="h-6 w-6 text-white" />
              </div>
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-heading mb-2 font-sans">Toolkits & Templates</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4 font-sans">Ready-to-use templates and toolkits for development practitioners.</p>
              <a 
                href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent-green dark:text-accent-green hover:text-green-800 dark:hover:text-green-300 font-medium font-sans"
              >
                Download Toolkits
              </a>
            </div>
          </div>
          
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-accent-purple dark:bg-purple-900 mb-4">
                <Target className="h-6 w-6 text-white" />
              </div>
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-heading mb-2 font-sans">Case Studies</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4 font-sans">Real-world examples of successful development projects and initiatives.</p>
              <a 
                href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent-purple dark:text-accent-purple hover:text-purple-800 dark:hover:text-purple-300 font-medium font-sans"
              >
                Read Case Studies
              </a>
            </div>
          </div>
          
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-accent-yellow dark:bg-yellow-900 mb-4">
                <svg className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-heading mb-2 font-sans">Community Resources</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4 font-sans">Connect with other development professionals and share knowledge.</p>
              <a 
                href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent-yellow dark:text-accent-yellow hover:text-yellow-800 dark:hover:text-yellow-300 font-medium font-sans"
              >
                Join Community
              </a>
            </div>
          </div>
          
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-red-500 dark:bg-red-900 mb-4">
                <svg className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-heading mb-2 font-sans">Events & Webinars</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4 font-sans">Upcoming events, workshops, and learning opportunities.</p>
              <a 
                href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-red-500 dark:text-red-400 hover:text-red-800 dark:hover:text-red-300 font-medium font-sans"
              >
                View Events
              </a>
            </div>
          </div>
          
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <div className="flex items-center justify-center h-12 w-12 rounded-md bg-accent-blue dark:bg-blue-900 mb-4">
                <svg className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 className="text-lg font-medium text-gray-900 dark:text-chalk-white font-heading mb-2 font-sans">Newsletter</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4 font-sans">Stay updated with the latest resources and insights in development.</p>
              <a 
                href="https://github.com/Varnasr/ImpactMojo/blob/main/Handouts/index.html" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-medium font-sans"
              >
                Subscribe
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResourcesPage;

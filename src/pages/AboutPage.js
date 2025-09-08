// src/pages/AboutPage.js
import React from 'react';
import { ExternalLink, Mail, BookOpen, Heart, Users, Target, Globe } from 'lucide-react';
import { usePage } from '../App';
import Navigation from '../components/Navigation';

const AboutPage = () => {
  const { darkMode } = usePage();

  const socialLinks = [
    {
      name: 'Threads',
      url: 'https://threads.net/@varnasriraman',
      description: 'Follow for daily thoughts and insights'
    },
    {
      name: 'Notion',
      url: 'https://varna.notion.site',
      description: 'Personal workspace and project documentation'
    },
    {
      name: 'LinkedIn',
      url: 'https://linkedin.com/in/varnasriraman',
      description: 'Professional network and career updates'
    },
    {
      name: 'Newsletter',
      url: 'https://varna.substack.com',
      description: 'Subscribe for weekly development insights'
    },
    {
      name: 'Email',
      url: 'mailto:varna.sr@gmail.com',
      description: 'Get in touch directly'
    }
  ];

  const shareableContent = [
    {
      title: 'Share ImpactMojo on Twitter',
      url: 'https://twitter.com/intent/tweet?text=Discovered%20ImpactMojo%20-%20amazing%20free%20development%20education%20platform!&url=https://impactmojo.in&hashtags=development,education,socialimpact',
      platform: 'Twitter'
    },
    {
      title: 'Share on LinkedIn',
      url: 'https://www.linkedin.com/sharing/share-offsite/?url=https://impactmojo.in',
      platform: 'LinkedIn'
    },
    {
      title: 'Share on Facebook',
      url: 'https://www.facebook.com/sharer/sharer.php?u=https://impactmojo.in',
      platform: 'Facebook'
    }
  ];

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      <Navigation />
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
            About ImpactMojo
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
            Democratizing development knowledge through accessible, high-quality education for social impact
          </p>
        </div>

        {/* About Me Section */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8 mb-12">
          <div className="flex flex-col lg:flex-row items-center lg:items-start space-y-6 lg:space-y-0 lg:space-x-8">
            
            {/* Photo */}
            <div className="flex-shrink-0">
              <img 
                src="/assets/varna-photo.jpg"
                alt="Varna Sri Raman"
                className="w-32 h-32 lg:w-48 lg:h-48 rounded-full object-cover shadow-lg"
                onError={(e) => {
                  e.target.src = "/assets/android-chrome-192x192.png";
                }}
              />
            </div>
            
            {/* Content */}
            <div className="flex-1 text-center lg:text-left">
              <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-4">
                Varna Sri Raman
              </h2>
              <p className="text-lg text-gray-600 dark:text-gray-300 mb-6">
                Development Economist & Creator of ImpactMojo
              </p>
              
              <div className="prose prose-lg dark:prose-invert max-w-none">
                <p className="text-gray-700 dark:text-gray-300 mb-4">
                  ImpactMojo was born from a simple belief: quality development education should be accessible to everyone, 
                  regardless of their background or location. As a development economist with a PhD, I've seen firsthand 
                  how knowledge barriers limit our collective ability to address global challenges.
                </p>
                
                <p className="text-gray-700 dark:text-gray-300 mb-4">
                  This platform curates essential development knowledge into digestible 101 series, covering everything 
                  from gender studies to climate science, from research methods to policy economics. Each course is 
                  designed to be practical, evidence-based, and immediately applicable to real-world development work.
                </p>
                
                <p className="text-gray-700 dark:text-gray-300 mb-6">
                  ImpactMojo is open-source, non-commercial, and built with the generous support of our community and 
                  partners. It's my contribution to democratizing development knowledge and fostering a more equitable 
                  approach to social impact education.
                </p>
              </div>
              
              {/* Contact Email */}
              <div className="flex items-center justify-center lg:justify-start space-x-2 mb-6">
                <Mail className="h-5 w-5 text-blue-600 dark:text-blue-400" />
                <a 
                  href="mailto:varna.sr@gmail.com" 
                  className="text-blue-600 dark:text-blue-400 hover:underline"
                >
                  varna.sr@gmail.com
                </a>
              </div>
            </div>
          </div>
        </div>

        {/* Social Links Section */}
        <div className="grid md:grid-cols-2 gap-8 mb-12">
          
          {/* Connect Section */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6 flex items-center">
              <Users className="mr-3 h-6 w-6 text-blue-600" />
              Connect with Me
            </h3>
            
            <div className="space-y-4">
              {socialLinks.map((link, index) => (
                <a
                  key={index}
                  href={link.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors group"
                >
                  <div>
                    <div className="font-semibold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400">
                      {link.name}
                    </div>
                    <div className="text-sm text-gray-600 dark:text-gray-300">
                      {link.description}
                    </div>
                  </div>
                  <ExternalLink className="h-5 w-5 text-gray-400 group-hover:text-blue-600" />
                </a>
              ))}
            </div>
          </div>

          {/* Share Section */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6 flex items-center">
              <Heart className="mr-3 h-6 w-6 text-red-500" />
              Share ImpactMojo
            </h3>
            
            <p className="text-gray-600 dark:text-gray-300 mb-4">
              Help us spread access to development education by sharing ImpactMojo with your network.
            </p>
            
            <div className="space-y-3">
              {shareableContent.map((share, index) => (
                <a
                  key={index}
                  href={share.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-between p-3 rounded-lg bg-blue-50 dark:bg-blue-900/20 hover:bg-blue-100 dark:hover:bg-blue-900/30 transition-colors group"
                >
                  <span className="font-medium text-blue-800 dark:text-blue-200">
                    {share.title}
                  </span>
                  <ExternalLink className="h-4 w-4 text-blue-600 dark:text-blue-400" />
                </a>
              ))}
            </div>
          </div>
        </div>

        {/* Mission Section */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8 mb-12">
          <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6 text-center">
            Our Mission
          </h3>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center mx-auto mb-4">
                <BookOpen className="h-8 w-8 text-blue-600 dark:text-blue-400" />
              </div>
              <h4 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                Accessible Education
              </h4>
              <p className="text-gray-600 dark:text-gray-300">
                Making high-quality development education available to everyone, everywhere, for free.
              </p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-green-100 dark:bg-green-900 rounded-full flex items-center justify-center mx-auto mb-4">
                <Target className="h-8 w-8 text-green-600 dark:text-green-400" />
              </div>
              <h4 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                Practical Impact
              </h4>
              <p className="text-gray-600 dark:text-gray-300">
                Focusing on knowledge that can be immediately applied to real-world development challenges.
              </p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-purple-100 dark:bg-purple-900 rounded-full flex items-center justify-center mx-auto mb-4">
                <Globe className="h-8 w-8 text-purple-600 dark:text-purple-400" />
              </div>
              <h4 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                Global Community
              </h4>
              <p className="text-gray-600 dark:text-gray-300">
                Building a worldwide network of development practitioners and learners.
              </p>
            </div>
          </div>
        </div>

        {/* Support Section */}
        <div className="bg-gradient-to-r from-blue-600 to-purple-700 rounded-lg p-8 text-white text-center">
          <h3 className="text-2xl font-bold mb-4">Support ImpactMojo</h3>
          <p className="text-lg opacity-90 mb-6">
            Help us keep this platform free and accessible for learners worldwide
          </p>
          
          <div className="bg-white bg-opacity-20 rounded-lg p-4 max-w-2xl mx-auto">
            <p className="text-sm mb-2">Donate via UPI:</p>
            <div className="flex flex-wrap justify-center gap-4 text-yellow-200 font-mono">
              <span>impactmojo@ibl</span>
              <span>•</span>
              <span>impactmojo@ybl</span>
              <span>•</span>
              <span>impactmojo@axl</span>
            </div>
          </div>
          
          <p className="text-sm opacity-75 mt-4">
            Your support covers server costs, content development, and platform improvements
          </p>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;

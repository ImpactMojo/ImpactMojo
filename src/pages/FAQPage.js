// src/pages/FAQPage.js

import React, { useState } from 'react';

import { ChevronDown, ChevronUp, HelpCircle, Book, Award, Users, Shield, Globe } from 'lucide-react';

import { usePage } from '../context/AppContext.js';

import Navigation from '../components/Navigation';

const FAQPage = () => {

  const { darkMode } = usePage();

  const [openFAQ, setOpenFAQ] = useState(null);

  const faqCategories = [
    {
      title: "Getting Started",
      icon: Book,
      color: "blue",
      faqs: [
        {
          question: "What is ImpactMojo?",
          answer: "ImpactMojo is a free, open-source educational platform offering 101 knowledge series for social impact. It covers development economics, gender studies, policy analysis, research methods, and more - all designed for practitioners, students, and anyone interested in creating positive social change."
        },
        {
          question: "Who can use ImpactMojo?",
          answer: "ImpactMojo is for everyone! Whether you're a development professional, student, researcher, NGO worker, policymaker, or simply someone passionate about social impact, our courses are designed to be accessible regardless of your background."
        }
      ]
    },
    // ... add other categories and FAQs here
  ];

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <Navigation />
      <div className="max-w-4xl mx-auto py-16 px-2 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-center mb-8">Frequently Asked Questions</h1>
        {(faqCategories ?? []).map((category, i) => {
          const Icon = category.icon || HelpCircle;
          return (
            <div key={category.title || i} className="mb-10">
              <div className={`flex items-center mb-4`}>
                <Icon className={`w-8 h-8 mr-3 text-${category.color || 'indigo'}-500`} />
                <h2 className="text-2xl font-bold">{category.title}</h2>
              </div>
              <div className="divide-y divide-gray-300 dark:divide-gray-800 rounded-lg bg-gray-50 dark:bg-gray-800 shadow">
                {(category.faqs ?? []).map((faq, j) => (
                  <div key={faq.question || j} className="py-4 px-6">
                    <button
                      onClick={() =>
                        setOpenFAQ(openFAQ === `${i}-${j}` ? null : `${i}-${j}`)
                      }
                      className="flex items-center w-full text-left focus:outline-none"
                    >
                      <span className="font-semibold text-lg mr-4">{faq.question}</span>
                      {openFAQ === `${i}-${j}` ? (
                        <ChevronUp className="ml-auto w-5 h-5 text-blue-500" />
                      ) : (
                        <ChevronDown className="ml-auto w-5 h-5 text-blue-500" />
                      )}
                    </button>
                    {openFAQ === `${i}-${j}` && (
                      <div className="mt-2 text-gray-700 dark:text-gray-200">{faq.answer}</div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default FAQPage;

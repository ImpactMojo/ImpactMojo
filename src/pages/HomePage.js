import React, { useState } from 'react';
import { Heart } from 'lucide-react';

// CORRECTED IMPORTS: These paths go up one directory to find the context and components folders.
import { usePage } from '../context/AppContext.js'; 
import { 
  FeaturedContentSection, 
  TestimonialsSection, 
  PopularCoursesSection,
  LearningTracksSection,
  SimpleQuiz,
  QuizResult
} from '../components/index.js'; // This now uses your components index file correctly

const HomePage = () => {
  const { darkMode } = usePage();
  const [showQuizModal, setShowQuizModal] = useState(false);
  const [quizResult, setQuizResult] = useState(null);

  return (
    <div className={`min-h-screen ${darkMode ? 'dark bg-gray-900' : 'bg-white'}`}>
      <div className="relative bg-gradient-to-r from-blue-600 to-purple-700 text-white text-center py-20">
        <h1 className="text-4xl md:text-6xl font-bold mb-6">Development Know-How for Everyone</h1>
        <p className="text-xl md:text-2xl mb-8 opacity-90">101 Knowledge Series for Social Impact</p>
        <button onClick={() => setShowQuizModal(true)} className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors">Find Your Learning Path</button>
      </div>
      
      <PopularCoursesSection />
      <LearningTracksSection />
      <FeaturedContentSection />
      <TestimonialsSection />

      <div className="py-8 bg-yellow-50 dark:bg-yellow-900/20 text-center">
        <div className="flex items-center justify-center mb-3">
          <Heart className="text-red-500 mr-2" size={20} />
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Support ImpactMojo</h3>
        </div>
        <p className="text-gray-600 dark:text-gray-300 text-sm">UPI: impactmojo@ibl • impactmojo@ybl • impactmojo@axl</p>
      </div>

      {showQuizModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full p-6">
            {!quizResult ? (
              <SimpleQuiz onComplete={(result) => setQuizResult(result)} onClose={() => setShowQuizModal(false)} />
            ) : (
              <QuizResult result={quizResult} onClose={() => { setShowQuizModal(false); setQuizResult(null); }} />
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default HomePage;


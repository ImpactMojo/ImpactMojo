// src/components/floating-action-buttons.js
import React, { useState } from 'react';
import { 
  Bookmark, 
  Scale, 
  MessageCircle, 
  Lightbulb, 
  X, 
  Send 
} from 'lucide-react';

export const FloatingActionButtons = ({ user }) => {
  const [showBookmarkModal, setShowBookmarkModal] = useState(false);
  const [showCompareModal, setShowCompareModal] = useState(false);
  const [showFeedbackModal, setShowFeedbackModal] = useState(false);
  const [showSuggestModal, setShowSuggestModal] = useState(false);

  return (
    <>
      {/* Bookmark FAB - Bottom Right */}
      <button
        onClick={() => setShowBookmarkModal(true)}
        className="fixed bottom-4 right-4 bg-yellow-500 hover:bg-yellow-600 text-white p-3 rounded-full shadow-lg z-40 transition-colors"
        title="Bookmarks"
      >
        <Bookmark className="h-6 w-6" />
      </button>

      {/* Compare FAB - Bottom Left */}
      <button
        onClick={() => setShowCompareModal(true)}
        className="fixed bottom-4 left-4 bg-blue-500 hover:bg-blue-600 text-white p-3 rounded-full shadow-lg z-40 transition-colors"
        title="Compare"
      >
        <Scale className="h-6 w-6" />
      </button>

      {/* Feedback FAB - Top Right */}
      <button
        onClick={() => setShowFeedbackModal(true)}
        className="fixed top-20 right-4 bg-green-500 hover:bg-green-600 text-white p-3 rounded-full shadow-lg z-40 transition-colors"
        title="Feedback"
      >
        <MessageCircle className="h-6 w-6" />
      </button>

      {/* Suggest Course FAB - Top Left */}
      <button
        onClick={() => setShowSuggestModal(true)}
        className="fixed top-20 left-4 bg-purple-500 hover:bg-purple-600 text-white p-3 rounded-full shadow-lg z-40 transition-colors"
        title="Suggest Course"
      >
        <Lightbulb className="h-6 w-6" />
      </button>

      {/* Bookmark Modal */}
      {showBookmarkModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Your Bookmarks</h3>
              <button onClick={() => setShowBookmarkModal(false)}>
                <X className="h-6 w-6 text-gray-500" />
              </button>
            </div>
            <p className="text-gray-600 dark:text-gray-300">
              {user ? "Your saved courses and resources will appear here." : "Please sign in to save bookmarks."}
            </p>
          </div>
        </div>
      )}

      {/* Compare Modal */}
      {showCompareModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Compare Courses</h3>
              <button onClick={() => setShowCompareModal(false)}>
                <X className="h-6 w-6 text-gray-500" />
              </button>
            </div>
            <p className="text-gray-600 dark:text-gray-300">
              Select courses to compare them side by side.
            </p>
          </div>
        </div>
      )}

      {/* Feedback Modal */}
      {showFeedbackModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Send Feedback</h3>
              <button onClick={() => setShowFeedbackModal(false)}>
                <X className="h-6 w-6 text-gray-500" />
              </button>
            </div>
            <form action="https://formspree.io/f/xpwdvgzp" method="POST" className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Your Feedback
                </label>
                <textarea
                  name="feedback"
                  rows="4"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                  placeholder="Tell us what you think..."
                  required
                ></textarea>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Email (optional)
                </label>
                <input
                  type="email"
                  name="email"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                  placeholder="your@email.com"
                />
              </div>
              <div className="flex justify-end space-x-3">
                <button
                  type="button"
                  onClick={() => setShowFeedbackModal(false)}
                  className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-sm font-medium text-white bg-green-600 rounded-md hover:bg-green-700 flex items-center"
                >
                  <Send className="h-4 w-4 mr-2" />
                  Send
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Suggest Course Modal */}
      {showSuggestModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Suggest a Course</h3>
              <button onClick={() => setShowSuggestModal(false)}>
                <X className="h-6 w-6 text-gray-500" />
              </button>
            </div>
            <form action="https://formspree.io/f/xpwdvgzp" method="POST" className="space-y-4">
              <input type="hidden" name="type" value="course-suggestion" />
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Course Title
                </label>
                <input
                  type="text"
                  name="course-title"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                  placeholder="e.g., Climate Finance 101"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Description & Rationale
                </label>
                <textarea
                  name="course-description"
                  rows="4"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                  placeholder="Why is this course needed? What would it cover?"
                  required
                ></textarea>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Your Email (optional)
                </label>
                <input
                  type="email"
                  name="email"
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                  placeholder="your@email.com"
                />
              </div>
              <div className="flex justify-end space-x-3">
                <button
                  type="button"
                  onClick={() => setShowSuggestModal(false)}
                  className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-sm font-medium text-white bg-purple-600 rounded-md hover:bg-purple-700 flex items-center"
                >
                  <Lightbulb className="h-4 w-4 mr-2" />
                  Suggest
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
};

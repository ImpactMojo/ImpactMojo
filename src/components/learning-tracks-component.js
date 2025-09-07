// src/components/learning-tracks-component.js
import React, { useState } from 'react';
import { X, ExternalLink } from 'lucide-react';
import { trackStyles, getTrackCourses } from '../data/track-styling-data';

export const LearningTracksSection = ({ darkMode, courseData, browseByRole }) => {
  const [showTrackModal, setShowTrackModal] = useState(false);
  const [selectedTrack, setSelectedTrack] = useState(null);

  const handleTrackClick = (trackName) => {
    setSelectedTrack(trackName);
    setShowTrackModal(true);
  };

  const TrackModal = () => {
    if (!selectedTrack || !showTrackModal) return null;
    
    const trackCourses = getTrackCourses(selectedTrack, courseData);
    const trackStyle = trackStyles[selectedTrack];
    const IconComponent = trackStyle.icon;

    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
        <div className="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full max-h-[80vh] overflow-y-auto">
          <div className="p-6">
            <div className="flex justify-between items-center mb-4">
              <div className="flex items-center space-x-3">
                <div className={`p-2 rounded-lg ${trackStyle.bgColor}`}>
                  <IconComponent className="h-6 w-6 text-white" />
                </div>
                <div>
                  <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
                    {selectedTrack}
                  </h3>
                  <p className="text-gray-600 dark:text-gray-300 text-sm">
                    {trackStyle.description}
                  </p>
                </div>
              </div>
              <button 
                onClick={() => setShowTrackModal(false)}
                className="text-gray-500 hover:text-gray-700"
              >
                <X className="h-6 w-6" />
              </button>
            </div>

            <div className="space-y-4">
              <h4 className="font-medium text-gray-900 dark:text-white">
                Recommended Courses ({trackCourses.length})
              </h4>
              
              {trackCourses.length > 0 ? (
                <div className="grid gap-4">
                  {trackCourses.map((course) => (
                    <div key={course.id} className="border border-gray-200 dark:border-gray-600 rounded-lg p-4 hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start">
                        <div className="flex-1">
                          <h5 className="font-medium text-gray-900 dark:text-white mb-1">
                            {course.title}
                          </h5>
                          <p className="text-gray-600 dark:text-gray-300 text-sm mb-2">
                            {course.description}
                          </p>
                          <div className="flex items-center space-x-4 text-xs text-gray-500 dark:text-gray-400">
                            <span>{course.level}</span>
                            <span>{course.duration}</span>
                          </div>
                        </div>
                        <a
                          href={course.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className={`ml-4 p-2 rounded-md ${trackStyle.bgColor} hover:opacity-80 text-white transition-opacity`}
                          title="Open Course"
                        >
                          <ExternalLink className="h-4 w-4" />
                        </a>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-8 text-gray-500 dark:text-gray-400">
                  <p>Courses for this track are coming soon!</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <>
      <div className="mb-16">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white">Learning Tracks</h2>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-300">
            Choose your path based on your role and interests
          </p>
        </div>
        
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {Object.entries(browseByRole).map(([trackName, trackData]) => {
            const trackStyle = trackStyles[trackName];
            const IconComponent = trackStyle.icon;
            
            return (
              <button
                key={trackName}
                onClick={() => handleTrackClick(trackName)}
                className="text-left bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-all duration-200 transform hover:scale-105"
              >
                <div className="flex items-center space-x-3 mb-4">
                  <div className={`p-3 rounded-lg bg-gradient-to-r ${trackStyle.gradient}`}>
                    <IconComponent className="h-6 w-6 text-white" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-gray-900 dark:text-white text-sm">
                      {trackName}
                    </h3>
                  </div>
                </div>
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-3">
                  {trackData.description}
                </p>
                <div className="flex items-center justify-between">
                  <span className={`inline-block px-2 py-1 text-xs font-semibold rounded-full ${trackStyle.lightBgColor} ${trackStyle.darkBgColor} ${trackStyle.textColor} ${trackStyle.darkTextColor}`}>
                    {trackData.courses.length} courses
                  </span>
                  <div className="text-xs text-gray-500 dark:text-gray-400">
                    Click to explore →
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </div>

      <TrackModal />
    </>
  );
};

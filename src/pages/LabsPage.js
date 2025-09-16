import React from 'react';
// The labs data is now included directly in this file to prevent import errors.
const labsData = [
  {
    id: "research-methodology-lab",
    title: "Research Methodology Lab",
    description: "Design a research proposal from scratch, including methodology, data collection, and ethics.",
    url: "#",
    category: "Research",
    difficulty: "Intermediate"
  },
  {
    id: "data-analysis-lab",
    title: "Data Analysis Lab",
    description: "Practice data cleaning, analysis, and visualization using real-world development datasets.",
    url: "#",
    category: "Data",
    difficulty: "Intermediate"
  },
  {
    id: "field-work-simulation",
    title: "Field Work Simulation",
    description: "Navigate ethical dilemmas and practical challenges in a simulated field research environment.",
    url: "#",
    category: "Field Work",
    difficulty: "Advanced"
  }
];

const LabsPage = () => {
  return (
    <div className="max-w-7xl mx-auto py-16 px-4">
      <h1 className="text-4xl font-bold text-center mb-12">Labs</h1>
      <p className="text-center text-lg text-gray-600 dark:text-gray-300 mb-12">
        Hands-on practical exercises and simulations to apply your knowledge.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {(labsData ?? []).map((lab) => (
          <div
            key={lab.id}
            className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col"
          >
            <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">{lab.title}</h3>
            <p className="text-gray-600 dark:text-gray-300 mb-4 flex-grow">{lab.description}</p>
            <div className="flex justify-between items-center text-sm text-gray-500 dark:text-gray-400 mb-4">
              <span>{lab.category}</span>
              <span className="font-semibold">{lab.difficulty}</span>
            </div>
            <a
              href={lab.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-center bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700 mt-auto"
            >
              Start Lab
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default LabsPage;

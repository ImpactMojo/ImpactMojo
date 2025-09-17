import React from "react";
import labsData from "../data/labs-data";
import Navigation from "../components/Navigation";

const LabsPage = () => (
  <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
    <Navigation />
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold text-center mb-8 text-blue-600 dark:text-blue-300">
        Labs
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {(labsData ?? []).map((lab, idx) => (
          <div
            key={idx}
            className="bg-white dark:bg-gray-800 rounded shadow p-6 flex flex-col"
          >
            <h2 className="font-semibold text-2xl text-blue-700 mb-2 dark:text-blue-200">
              {lab.title}
            </h2>
            <p className="text-gray-800 dark:text-gray-200 mb-4">{lab.description}</p>
            {lab.tags && (
              <div className="mb-4">
                {(lab.tags ?? []).map((tag, tagIdx) => (
                  <span
                    key={tagIdx}
                    className="inline-block bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-200 rounded px-2 py-1 mr-2 text-xs font-medium"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}
            {lab.link && (
              <a
                href={lab.link}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 font-medium hover:underline mt-auto"
              >
                Visit Lab &rarr;
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  </div>
);

export default LabsPage;

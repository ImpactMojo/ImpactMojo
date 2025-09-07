// src/data/featured-content-data.js

export const featuredContent = [
  {
    id: "F1",
    title: "The Real Middle Game",
    type: "Interactive Game",
    description: "An interactive strategy game that challenges development professionals to navigate complex real-world scenarios. Test your decision-making skills in this engaging simulation.",
    url: "https://101.www.impactmojo.in/theREALmiddlegame"
  },
  {
    id: "F2", 
    title: "English for Development Professionals 101",
    type: "Premium Course",
    description: "Master professional English communication skills specifically designed for development practitioners. Build confidence in writing proposals, reports, and presentations.",
    url: "https://101.www.impactmojo.in/eng4dev"
  },
  {
    id: "F3",
    title: "Field Notes from a Development Economist", 
    type: "Premium Blog",
    description: "In-depth analysis and insights from development economics practice. Get exclusive access to field experiences and practical wisdom from the frontlines.",
    url: "https://marginmuse.space/themarginmuse"
  },
  {
    id: "F4",
    title: "AI Tools for Development",
    type: "Tool Suite", 
    description: "Discover curated AI-powered tools specifically selected for development professionals. From research assistance to data analysis, explore the future of development work.",
    url: "#",
    onClick: "setCurrentPage('ai-tools')" // Special handling for internal navigation
  }
];

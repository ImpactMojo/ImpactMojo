// src/data/track-styling-data.js
import { 
  BookOpen, 
  BarChart, 
  Users, 
  Scale 
} from 'lucide-react';

// Learning track configurations with AI dashboard-style icons
export const trackStyles = {
  "New to Development": {
    icon: BookOpen,
    color: "blue",
    bgColor: "bg-blue-500",
    lightBgColor: "bg-blue-100",
    darkBgColor: "dark:bg-blue-900",
    textColor: "text-blue-800",
    darkTextColor: "dark:text-blue-200",
    description: "Just starting your development journey",
    gradient: "from-blue-500 to-blue-600"
  },
  "Researcher/Academic": {
    icon: BarChart,
    color: "purple", 
    bgColor: "bg-purple-500",
    lightBgColor: "bg-purple-100",
    darkBgColor: "dark:bg-purple-900",
    textColor: "text-purple-800",
    darkTextColor: "dark:text-purple-200",
    description: "Conducting research and generating knowledge",
    gradient: "from-purple-500 to-purple-600"
  },
  "Practitioner/Field Worker": {
    icon: Users,
    color: "green",
    bgColor: "bg-green-500", 
    lightBgColor: "bg-green-100",
    darkBgColor: "dark:bg-green-900",
    textColor: "text-green-800",
    darkTextColor: "dark:text-green-200",
    description: "Implementing programs and working directly with communities",
    gradient: "from-green-500 to-green-600"
  },
  "Student/Policy Maker": {
    icon: Scale,
    color: "orange",
    bgColor: "bg-orange-500",
    lightBgColor: "bg-orange-100", 
    darkBgColor: "dark:bg-orange-900",
    textColor: "text-orange-800",
    darkTextColor: "dark:text-orange-200",
    description: "Learning and shaping policy decisions",
    gradient: "from-orange-500 to-orange-600"
  }
};

// Function to get track courses (to fix the modal functionality)
export const getTrackCourses = (trackName, allCourses) => {
  const trackMappings = {
    "New to Development": ["development-economics-101", "global-development-architecture-101", "law-and-constitution-101"],
    "Researcher/Academic": ["research-ethics-101", "qualitative-research-methods-101", "econometrics-101", "data-literacy-101"],
    "Practitioner/Field Worker": ["community-development-101", "monitoring-evaluation-accountability-and-learning-101", "advocacy-and-communications-101"],
    "Student/Policy Maker": ["law-and-constitution-101", "political-economy-101", "global-development-architecture-101"]
  };
  
  const courseIds = trackMappings[trackName] || [];
  return allCourses.filter(course => courseIds.includes(course.id));
};

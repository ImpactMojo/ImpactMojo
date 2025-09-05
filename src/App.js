// src/App.js
import React, { useState, useEffect, createContext, useContext } from 'react';
import { 
  Menu, X, Sun, Moon, Bookmark, MessageCircle, 
  ExternalLink, BookOpen, FileText, Target, Users, 
  Clock, CheckCircle, PlayCircle, Bot, Trophy, 
  Headphones, MapPin, Library, Music, Download, 
  Search, Plus, Edit3, Save, Filter, BookmarkIcon
} from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc, updateDoc, deleteField } from 'firebase/firestore';

// Data imports
import { courseData, upcomingCourses } from './data/course-data';
import { labsData } from './data/labs-data';
import { premiumResources } from './data/premium-resources-data';

// Page imports
import AIToolsPage from './pages/AIToolsPage';

// Firebase Configuration
const firebaseConfig = {
  apiKey: "AIzaSyDnF0eJsTULzOJUnBskybd44dG5w-f46vE",
  authDomain: "impactmojo.firebaseapp.com",
  projectId: "impactmojo",
  storageBucket: "impactmojo.firebasestorage.app",
  messagingSenderId: "529198336589",
  appId: "1:529198336589:web:1664b5344de5bfb31bea04",
  measurementId: "G-ZHPPXXMRGV"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const googleProvider = new GoogleAuthProvider();

// Authentication Context
const AuthContext = createContext();
const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [bookmarks, setBookmarks] = useState([]);
  const [isPremium, setIsPremium] = useState(false);
  const [customPathway, setCustomPathway] = useState([]);
  const [notes, setNotes] = useState([]);
  const [comparisons, setComparisons] = useState([]);
  
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user);
      if (user) {
        try {
          const userDoc = await getDoc(doc(db, 'users', user.uid));
          if (userDoc.exists()) {
            const userData = userDoc.data();
            setBookmarks(userData.bookmarks || []);
            setIsPremium(true); // Set to true for logged-in users
            setCustomPathway(userData.customPathway || []);
            setNotes(userData.notes || []);
            setComparisons(userData.comparisons || []);
          } else {
            await setDoc(doc(db, 'users', user.uid), {
              name: user.displayName,
              email: user.email,
              photoURL: user.photoURL,
              bookmarks: [],
              isPremium: true, // Set to true for logged-in users
              customPathway: [],
              notes: [],
              comparisons: [],
              createdAt: new Date()
            });
            setIsPremium(true); // Set to true for logged-in users
          }
        } catch (error) {
          console.error('Error loading user data:', error);
        }
      } else {
        setBookmarks([]);
        setIsPremium(false);
        setCustomPathway([]);
        setNotes([]);
        setComparisons([]);
      }
      setLoading(false);
    });
    return unsubscribe;
  }, []);
  
  const signInWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, googleProvider);
      const user = result.user;
      await setDoc(doc(db, 'users', user.uid), {
        name: user.displayName,
        email: user.email,
        photoURL: user.photoURL,
        isPremium: true, // Set to true for logged-in users
        lastLogin: new Date()
      }, { merge: true });
      return user;
    } catch (error) {
      console.error('Error signing in:', error);
      throw error;
    }
  };
  
  const signOut = async () => {
    try {
      await firebaseSignOut(auth);
    } catch (error) {
      console.error('Error signing out:', error);
      throw error;
    }
  };
  
  const toggleBookmark = async (itemId, itemType = 'course') => {
    if (!user) return;
    try {
      const newBookmarks = bookmarks.find(b => b.id === itemId)
        ? bookmarks.filter(b => b.id !== itemId)
        : [...bookmarks, { id: itemId, type: itemType, dateAdded: new Date() }];
      await updateDoc(doc(db, 'users', user.uid), { bookmarks: newBookmarks });
      setBookmarks(newBookmarks);
    } catch (error) {
      console.error('Error toggling bookmark:', error);
    }
  };

  const toggleComparison = async (itemId, itemType = 'course') => {
    if (!user) return;
    try {
      const existingIndex = comparisons.findIndex(c => c.id === itemId);
      let newComparisons;
      
      if (existingIndex >= 0) {
        // Remove from comparison
        newComparisons = comparisons.filter(c => c.id !== itemId);
      } else if (comparisons.length < 3) {
        // Add to comparison (max 3)
        newComparisons = [...comparisons, { id: itemId, type: itemType, dateAdded: new Date() }];
      } else {
        // Replace oldest if at max
        newComparisons = [...comparisons.slice(1), { id: itemId, type: itemType, dateAdded: new Date() }];
      }
      
      await updateDoc(doc(db, 'users', user.uid), { comparisons: newComparisons });
      setComparisons(newComparisons);
    } catch (error) {
      console.error('Error toggling comparison:', error);
    }
  };
  
  const addToPathway = async (courseId) => {
    if (!user) return;
    try {
      const newPathway = [...customPathway, courseId];
      await updateDoc(doc(db, 'users', user.uid), { customPathway: newPathway });
      setCustomPathway(newPathway);
    } catch (error) {
      console.error('Error adding to pathway:', error);
    }
  };
  
  const saveNote = async (note) => {
    if (!user) return;
    try {
      const newNote = {
        ...note,
        id: Date.now().toString(),
        dateCreated: new Date(),
        lastModified: new Date()
      };
      const newNotes = [...notes, newNote];
      await updateDoc(doc(db, 'users', user.uid), { notes: newNotes });
      setNotes(newNotes);
      return newNote.id;
    } catch (error) {
      console.error('Error saving note:', error);
    }
  };

  const updateNote = async (noteId, updates) => {
    if (!user) return;
    try {
      const newNotes = notes.map(note => 
        note.id === noteId 
          ? { ...note, ...updates, lastModified: new Date() }
          : note
      );
      await updateDoc(doc(db, 'users', user.uid), { notes: newNotes });
      setNotes(newNotes);
    } catch (error) {
      console.error('Error updating note:', error);
    }
  };

  const deleteNote = async (noteId) => {
    if (!user) return;
    try {
      const newNotes = notes.filter(note => note.id !== noteId);
      await updateDoc(doc(db, 'users', user.uid), { notes: newNotes });
      setNotes(newNotes);
    } catch (error) {
      console.error('Error deleting note:', error);
    }
  };
  
  return (
    <AuthContext.Provider value={{
      user, loading, bookmarks, isPremium, customPathway, notes, comparisons,
      signInWithGoogle, signOut, toggleBookmark, toggleComparison, addToPathway, 
      saveNote, updateNote, deleteNote
    }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};

// Page Context
const PageContext = createContext();
const PageProvider = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('home');
  const [darkMode, setDarkMode] = useState(false);
  
  useEffect(() => {
    const isDark = localStorage.getItem('darkMode') === 'true';
    setDarkMode(isDark);
  }, []);
  
  useEffect(() => {
    localStorage.setItem('darkMode', darkMode);
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);
  
  return (
    <PageContext.Provider value={{ currentPage, setCurrentPage, darkMode, setDarkMode }}>
      {children}
    </PageContext.Provider>
  );
};

export const usePage = () => {
  const context = useContext(PageContext);
  if (!context) throw new Error('usePage must be used within PageProvider');
  return context;
};

// Cornell Notes Modal Component
const CornellNotesModal = ({ isOpen, onClose }) => {
  const { user, notes, saveNote, updateNote, deleteNote } = useAuth();
  const [selectedNote, setSelectedNote] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCourse, setFilterCourse] = useState('');
  const [formData, setFormData] = useState({
    title: '',
    course: '',
    cues: '',
    notes: '',
    summary: ''
  });

  const filteredNotes = notes.filter(note => {
    const matchesSearch = note.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         note.notes?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         note.cues?.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCourse = filterCourse === '' || note.course === filterCourse;
    return matchesSearch && matchesCourse;
  });

  const uniqueCourses = [...new Set(notes.map(note => note.course).filter(Boolean))];

  const handleSave = async () => {
    if (!formData.title.trim()) return;
    
    if (selectedNote) {
      await updateNote(selectedNote.id, formData);
    } else {
      await saveNote(formData);
    }
    
    setFormData({ title: '', course: '', cues: '', notes: '', summary: '' });
    setSelectedNote(null);
    setIsEditing(false);
  };

  const handleEdit = (note) => {
    setSelectedNote(note);
    setFormData({
      title: note.title || '',
      course: note.course || '',
      cues: note.cues || '',
      notes: note.notes || '',
      summary: note.summary || ''
    });
    setIsEditing(true);
  };

  const handleDelete = async (noteId) => {
    if (window.confirm('Are you sure you want to delete this note?')) {
      await deleteNote(noteId);
      if (selectedNote?.id === noteId) {
        setSelectedNote(null);
        setIsEditing(false);
      }
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-6xl w-full h-5/6 flex flex-col">
        <div className="flex items-center justify-between p-4 border-b">
          <h2 className="text-xl font-bold">Cornell Notes</h2>
          <button onClick={onClose} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
            <X className="h-5 w-5" />
          </button>
        </div>
        
        <div className="flex flex-1 overflow-hidden">
          {/* Notes List Sidebar */}
          <div className="w-1/3 border-r p-4 overflow-y-auto">
            <div className="space-y-4 mb-4">
              <div className="relative">
                <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                <input
                  type="text"
                  placeholder="Search notes..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-3 py-2 border rounded-md"
                />
              </div>
              <select
                value={filterCourse}
                onChange={(e) => setFilterCourse(e.target.value)}
                className="w-full p-2 border rounded-md"
              >
                <option value="">All Courses</option>
                {uniqueCourses.map(course => (
                  <option key={course} value={course}>{course}</option>
                ))}
              </select>
              <button
                onClick={() => {
                  setSelectedNote(null);
                  setFormData({ title: '', course: '', cues: '', notes: '', summary: '' });
                  setIsEditing(true);
                }}
                className="w-full flex items-center justify-center gap-2 p-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
              >
                <Plus className="h-4 w-4" />
                New Note
              </button>
            </div>
            
            <div className="space-y-2">
              {filteredNotes.map(note => (
                <div
                  key={note.id}
                  className={`p-3 border rounded cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700 ${
                    selectedNote?.id === note.id ? 'bg-blue-50 dark:bg-blue-900' : ''
                  }`}
                  onClick={() => handleEdit(note)}
                >
                  <h3 className="font-medium truncate">{note.title}</h3>
                  <p className="text-sm text-gray-500">{note.course}</p>
                  <p className="text-xs text-gray-400">
                    {new Date(note.lastModified?.toDate?.() || note.lastModified).toLocaleDateString()}
                  </p>
                </div>
              ))}
            </div>
          </div>
          
          {/* Cornell Notes Editor */}
          <div className="flex-1 p-4">
            {isEditing ? (
              <div className="h-full flex flex-col space-y-4">
                <div className="flex gap-4">
                  <input
                    type="text"
                    placeholder="Note Title"
                    value={formData.title}
                    onChange={(e) => setFormData({...formData, title: e.target.value})}
                    className="flex-1 p-2 border rounded-md"
                  />
                  <select
                    value={formData.course}
                    onChange={(e) => setFormData({...formData, course: e.target.value})}
                    className="p-2 border rounded-md"
                  >
                    <option value="">Select Course</option>
                    {courseData.map(course => (
                      <option key={course.id} value={course.title}>{course.title}</option>
                    ))}
                  </select>
                </div>
                
                <div className="flex-1 grid grid-cols-3 gap-4 h-96">
                  <div className="flex flex-col">
                    <label className="font-medium mb-2">Cues & Questions</label>
                    <textarea
                      value={formData.cues}
                      onChange={(e) => setFormData({...formData, cues: e.target.value})}
                      placeholder="Key terms, questions, formulas..."
                      className="flex-1 p-2 border rounded-md resize-none"
                    />
                  </div>
                  
                  <div className="flex flex-col col-span-2">
                    <label className="font-medium mb-2">Notes</label>
                    <textarea
                      value={formData.notes}
                      onChange={(e) => setFormData({...formData, notes: e.target.value})}
                      placeholder="Main notes content..."
                      className="flex-1 p-2 border rounded-md resize-none"
                    />
                  </div>
                </div>
                
                <div className="flex flex-col">
                  <label className="font-medium mb-2">Summary</label>
                  <textarea
                    value={formData.summary}
                    onChange={(e) => setFormData({...formData, summary: e.target.value})}
                    placeholder="Key takeaways and summary..."
                    className="h-20 p-2 border rounded-md resize-none"
                  />
                </div>
                
                <div className="flex gap-2">
                  <button
                    onClick={handleSave}
                    className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700"
                  >
                    <Save className="h-4 w-4" />
                    Save
                  </button>
                  <button
                    onClick={() => {
                      setIsEditing(false);
                      setSelectedNote(null);
                    }}
                    className="px-4 py-2 border rounded-md hover:bg-gray-50"
                  >
                    Cancel
                  </button>
                  {selectedNote && (
                    <button
                      onClick={() => handleDelete(selectedNote.id)}
                      className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 ml-auto"
                    >
                      Delete
                    </button>
                  )}
                </div>
              </div>
            ) : (
              <div className="h-full flex items-center justify-center text-gray-500">
                <div className="text-center">
                  <BookOpen className="h-16 w-16 mx-auto mb-4 opacity-50" />
                  <p>Select a note to view or create a new one</p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

// Comparison Modal Component
const ComparisonModal = ({ isOpen, onClose }) => {
  const { comparisons, toggleComparison } = useAuth();
  
  const getItemData = (id, type) => {
    switch (type) {
      case 'course':
        return courseData.find(item => item.id === id);
      case 'lab':
        return labsData.find(item => item.id === id);
      case 'resource':
        return premiumResources.find(item => item.id === id);
      default:
        return null;
    }
  };

  const exportToTxt = () => {
    const content = comparisons.map(comp => {
      const item = getItemData(comp.id, comp.type);
      return `${comp.type.toUpperCase()}: ${item?.title || comp.id}
Description: ${item?.description || 'N/A'}
Track/Topic: ${item?.track || item?.topic || item?.category || 'N/A'}
Level: ${item?.level || item?.difficulty || 'N/A'}
Duration: ${item?.duration || 'N/A'}

`;
    }).join('\n');
    
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'comparison.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  const exportToCsv = () => {
    const headers = ['Type', 'Title', 'Description', 'Track/Topic', 'Level', 'Duration'];
    const rows = comparisons.map(comp => {
      const item = getItemData(comp.id, comp.type);
      return [
        comp.type,
        item?.title || comp.id,
        item?.description || 'N/A',
        item?.track || item?.topic || item?.category || 'N/A',
        item?.level || item?.difficulty || 'N/A',
        item?.duration || 'N/A'
      ];
    });
    
    const csvContent = [headers, ...rows].map(row => 
      row.map(field => `"${field}"`).join(',')
    ).join('\n');
    
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'comparison.csv';
    a.click();
    URL.revokeObjectURL(url);
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-6xl w-full max-h-5/6 overflow-auto">
        <div className="flex items-center justify-between p-4 border-b">
          <h2 className="text-xl font-bold">Compare Items ({comparisons.length}/3)</h2>
          <div className="flex gap-2">
            <button
              onClick={exportToTxt}
              className="flex items-center gap-2 px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              <Download className="h-4 w-4" />
              TXT
            </button>
            <button
              onClick={exportToCsv}
              className="flex items-center gap-2 px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700"
            >
              <Download className="h-4 w-4" />
              CSV
            </button>
            <button onClick={onClose} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
              <X className="h-5 w-5" />
            </button>
          </div>
        </div>
        
        <div className="p-4">
          {comparisons.length === 0 ? (
            <div className="text-center py-8">
              <Target className="h-16 w-16 mx-auto mb-4 opacity-50" />
              <p className="text-gray-500">No items selected for comparison</p>
              <p className="text-sm text-gray-400">Use the compare icons on course/lab cards to add items</p>
            </div>
          ) : (
            <div className="grid gap-4" style={{ gridTemplateColumns: `repeat(${comparisons.length}, 1fr)` }}>
              {comparisons.map(comp => {
                const item = getItemData(comp.id, comp.type);
                return (
                  <div key={comp.id} className="border rounded-lg p-4">
                    <div className="flex items-center justify-between mb-3">
                      <span className="text-xs px-2 py-1 bg-blue-100 text-blue-800 rounded">
                        {comp.type.toUpperCase()}
                      </span>
                      <button
                        onClick={() => toggleComparison(comp.id, comp.type)}
                        className="text-red-500 hover:text-red-700"
                      >
                        <X className="h-4 w-4" />
                      </button>
                    </div>
                    
                    <h3 className="font-bold mb-2">{item?.title || comp.id}</h3>
                    
                    <div className="space-y-2 text-sm">
                      <div>
                        <span className="font-medium">Description:</span>
                        <p className="text-gray-600 dark:text-gray-300">{item?.description || 'N/A'}</p>
                      </div>
                      
                      <div>
                        <span className="font-medium">Track/Topic:</span>
                        <p className="text-gray-600 dark:text-gray-300">
                          {item?.track || item?.topic || item?.category || 'N/A'}
                        </p>
                      </div>
                      
                      <div>
                        <span className="font-medium">Level:</span>
                        <p className="text-gray-600 dark:text-gray-300">
                          {item?.level || item?.difficulty || 'N/A'}
                        </p>
                      </div>
                      
                      <div>
                        <span className="font-medium">Duration:</span>
                        <p className="text-gray-600 dark:text-gray-300">{item?.duration || 'N/A'}</p>
                      </div>
                      
                      {item?.url && (
                        <a
                          href={item.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="inline-flex items-center gap-1 text-blue-600 hover:text-blue-800"
                        >
                          <ExternalLink className="h-3 w-3" />
                          Access
                        </a>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// Navigation Component
export const Navigation = () => {
  const { user, signOut, signInWithGoogle, isPremium } = useAuth();
  const { currentPage, setCurrentPage, darkMode, setDarkMode } = usePage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  return (
    <nav className="sticky top-0 z-50 bg-white dark:bg-chalkboard-dark shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0 flex items-center">
              <div className="h-8 w-8 rounded-md bg-accent-blue flex items-center justify-center">
                <span className="text-white font-bold">IM</span>
              </div>
              <span className="ml-2 text-xl font-bold text-gray-900 dark:text-chalk-white font-sans">ImpactMojo</span>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              {['home', 'courses', 'labs', 'resources'].map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  className={`${currentPage === page ? 'border-accent-blue text-gray-900 dark:text-chalk-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium font-sans capitalize`}
                >
                  {page}
                </button>
              ))}
              {user && (
                <>
                  <button
                    onClick={() => setCurrentPage('dashboard')}
                    className={`${currentPage === 'dashboard' ? 'border-accent-blue text-gray-900 dark:text-chalk-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium font-sans`}
                  >
                    Dashboard
                  </button>
                  <button
                    onClick={() => setCurrentPage('ai-tools')}
                    className={`${currentPage === 'ai-tools' ? 'border-accent-blue text-gray-900 dark:text-chalk-white' : 'border-transparent text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white'} inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium font-sans flex items-center`}
                  >
                    AI Tools
                  </button>
                </>
              )}
            </div>
          </div>
          
          <div className="hidden sm:ml-6 sm:flex sm:items-center">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-accent-blue"
            >
              {darkMode ? <Sun className="h-5 w-5 text-yellow-400" /> : <Moon className="h-5 w-5" />}
            </button>
            
            {user ? (
              <div className="ml-3 flex items-center space-x-3">
                <div className="flex items-center">
                  <img className="h-8 w-8 rounded-full" src={user.photoURL} alt={user.displayName} />
                  <span className="ml-2 text-gray-900 dark:text-chalk-white text-sm font-medium font-sans hidden md:block">{user.displayName}</span>
                  {isPremium && <span className="ml-1 bg-yellow-400 text-yellow-900 text-xs px-1.5 py-0.5 rounded-full">PRO</span>}
                </div>
                <button onClick={signOut} className="text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white text-sm font-medium font-sans">
                  Sign Out
                </button>
              </div>
            ) : (
              <button
                onClick={signInWithGoogle}
                className="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-accent-blue hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-blue font-sans"
              >
                Sign In
              </button>
            )}
          </div>
          
          <div className="-mr-2 flex items-center sm:hidden">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-chalk-white hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-accent-blue"
            >
              {mobileMenuOpen ? <X className="block h-6 w-6" /> : <Menu className="block h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="sm:hidden bg-white dark:bg-chalkboard-dark">
          <div className="pt-2 pb-3 space-y-1">
            {['home', 'courses', 'labs', 'resources'].map((page) => (
              <button
                key={page}
                onClick={() => { setCurrentPage(page); setMobileMenuOpen(false); }}
                className={`${currentPage === page ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-chalk-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-chalk-white'} block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium font-sans capitalize`}
              >
                {page}
              </button>
            ))}
            {user && (
              <>
                <button
                  onClick={() => { setCurrentPage('dashboard'); setMobileMenuOpen(false); }}
                  className={`${currentPage === 'dashboard' ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-chalk-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-chalk-white'} block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium font-sans`}
                >
                  Dashboard
                </button>
                <button
                  onClick={() => { setCurrentPage('ai-tools'); setMobileMenuOpen(false); }}
                  className={`${currentPage === 'ai-tools' ? 'bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-chalk-white' : 'text-gray-500 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-chalk-white'} block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium font-sans flex items-center`}
                >
                  AI Tools
                </button>
              </>
            )}
          </div>
          
          <div className="pt-4 pb-3 border-t border-gray-200 dark:border-gray-700">
            <div className="flex items-center px-4">
              {user ? (
                <>
                  <img className="h-10 w-10 rounded-full" src={user.photoURL} alt={user.displayName} />
                  <div className="ml-3">
                    <div className="text-base font-medium text-gray-900 dark:text-chalk-white font-sans">{user.displayName}</div>
                    <div className="text-sm font-medium text-gray-500 dark:text-gray-300 font-sans">{user.email}</div>
                  </div>
                </>
              ) : (
                <div className="text-base font-medium text-gray-900 dark:text-chalk-white font-sans">Not signed in</div>
              )}
            </div>
            <div className="mt-3">
              {user ? (
                <button
                  onClick={signOut}
                  className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-900 dark:hover:text-chalk-white hover:bg-gray-100 dark:hover:bg-gray-700 font-sans"
                >
                  Sign out
                </button>
              ) : (
                <button
                  onClick={signInWithGoogle}
                  className="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-300 hover:text-gray-900 dark:hover:text-chalk-white hover:bg-gray-100 dark:hover:bg-gray-700 font-sans"
                >
                  Sign in
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};

// Dashboard Component
const Dashboard = () => {
  const { darkMode } = usePage();
  const { user, isPremium, customPathway, notes, bookmarks, comparisons } = useAuth();
  const [showNotesModal, setShowNotesModal] = useState(false);
  const [showComparisonModal, setShowComparisonModal] = useState(false);
  
  if (!user) {
    return (
      <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
        <Navigation />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 text-center">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-sans">Please sign in to access your dashboard</h1>
        </div>
      </div>
    );
  }
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="mb-8">
          <h1 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white font-sans">Dashboard</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-300 font-sans">Welcome back, {user.displayName}!</p>
        </div>
        
        {/* Stats Cards */}
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
          {[
            { title: 'Courses Bookmarked', value: bookmarks.filter(b => b.type === 'course').length, icon: BookOpen, color: 'blue' },
            { title: 'Labs Bookmarked', value: bookmarks.filter(b => b.type === 'lab').length, icon: Target, color: 'green' },
            { title: 'Notes Created', value: notes.length, icon: Edit3, color: 'purple' },
            { title: 'Items Comparing', value: comparisons.length, icon: Target, color: 'yellow' }
          ].map((stat, index) => (
            <div key={index} className="bg-white dark:bg-chalkboard-dark overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className={`flex-shrink-0 bg-${stat.color}-500 rounded-md p-3`}>
                    <stat.icon className="h-6 w-6 text-white" />
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 dark:text-gray-400 font-sans truncate">{stat.title}</dt>
                      <dd className="text-lg font-medium text-gray-900 dark:text-chalk-white font-sans">{stat.value}</dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        {/* Main Features */}
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2 mb-8">
          {/* Bookmarks */}
          <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-sans mb-4">Your Bookmarks</h2>
            {bookmarks.length > 0 ? (
              <div className="space-y-3">
                {bookmarks.slice(0, 5).map((bookmark) => {
                  const getItemData = (id, type) => {
                    switch (type) {
                      case 'course':
                        return courseData.find(item => item.id === id);
                      case 'lab':
                        return labsData.find(item => item.id === id);
                      case 'resource':
                        return premiumResources.find(item => item.id === id);
                      default:
                        return null;
                    }
                  };
                  
                  const item = getItemData(bookmark.id, bookmark.type);
                  return item ? (
                    <div key={bookmark.id} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div>
                        <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans">{item.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-300 font-sans capitalize">{bookmark.type}</p>
                      </div>
                      <a
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300"
                      >
                        <ExternalLink className="h-5 w-5" />
                      </a>
                    </div>
                  ) : null;
                })}
                {bookmarks.length > 5 && (
                  <p className="text-sm text-gray-500 dark:text-gray-300 text-center">
                    And {bookmarks.length - 5} more...
                  </p>
                )}
              </div>
            ) : (
              <div className="text-center py-8">
                <BookmarkIcon className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-300 font-sans mb-4">No bookmarks yet</p>
                <p className="text-sm text-gray-400 font-sans">Use the bookmark icons on courses and labs to save them here</p>
              </div>
            )}
          </div>
          
          {/* Cornell Notes */}
          <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-sans mb-4">Cornell Notes</h2>
            {notes.length > 0 ? (
              <div className="space-y-3">
                {notes.slice(0, 3).map((note) => (
                  <div key={note.id} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans">{note.title}</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-300 font-sans">{note.course}</p>
                    <p className="text-xs text-gray-400 mt-1">
                      {new Date(note.lastModified?.toDate?.() || note.lastModified).toLocaleDateString()}
                    </p>
                  </div>
                ))}
                <button
                  onClick={() => setShowNotesModal(true)}
                  className="w-full text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-medium font-sans text-center py-2"
                >
                  View All Notes
                </button>
              </div>
            ) : (
              <div className="text-center py-8">
                <Library className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-300 font-sans mb-4">No notes yet</p>
                <button
                  onClick={() => setShowNotesModal(true)}
                  className="bg-accent-blue hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium font-sans"
                >
                  Create Your First Note
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Comparison and Pathway */}
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2 mb-8">
          {/* Comparison */}
          <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-sans mb-4">
              Item Comparison ({comparisons.length}/3)
            </h2>
            {comparisons.length > 0 ? (
              <div className="space-y-3">
                {comparisons.map((comp) => {
                  const getItemData = (id, type) => {
                    switch (type) {
                      case 'course':
                        return courseData.find(item => item.id === id);
                      case 'lab':
                        return labsData.find(item => item.id === id);
                      case 'resource':
                        return premiumResources.find(item => item.id === id);
                      default:
                        return null;
                    }
                  };
                  
                  const item = getItemData(comp.id, comp.type);
                  return item ? (
                    <div key={comp.id} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div>
                        <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans">{item.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-300 font-sans capitalize">{comp.type}</p>
                      </div>
                    </div>
                  ) : null;
                })}
                <button
                  onClick={() => setShowComparisonModal(true)}
                  className="w-full text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-medium font-sans text-center py-2"
                >
                  View Comparison
                </button>
              </div>
            ) : (
              <div className="text-center py-8">
                <Target className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-300 font-sans mb-4">No items selected for comparison</p>
                <p className="text-sm text-gray-400 font-sans">Use the compare icons to select up to 3 items</p>
              </div>
            )}
          </div>
          
          {/* Custom Pathway */}
          <div className="bg-white dark:bg-chalkboard-dark shadow rounded-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-chalk-white font-sans mb-4">Your Learning Pathway</h2>
            {customPathway.length > 0 ? (
              <div className="space-y-3">
                {customPathway.map((courseId, index) => {
                  const course = courseData.find(c => c.id === courseId);
                  return course ? (
                    <div key={index} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div>
                        <h3 className="font-medium text-gray-900 dark:text-chalk-white font-sans">{course.title}</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-300 font-sans">{course.track}</p>
                      </div>
                      <a
                        href={course.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300"
                      >
                        <ExternalLink className="h-5 w-5" />
                      </a>
                    </div>
                  ) : null;
                })}
              </div>
            ) : (
              <div className="text-center py-8">
                <MapPin className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500 dark:text-gray-300 font-sans mb-4">No courses in your pathway yet</p>
                <button className="bg-accent-blue hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium font-sans">
                  Build Your Pathway
                </button>
              </div>
            )}
          </div>
        </div>
        
        {/* Study Music */}
        <div className="bg-gradient-to-r from-purple-500 to-indigo-600 rounded-lg shadow-lg p-6 text-white mb-8">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-bold font-sans">Lo-Fi Study Beats</h2>
              <p className="mt-1 font-sans">Focus better with our curated study playlist</p>
            </div>
            <a
              href="https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-white text-purple-600 px-4 py-2 rounded-md font-medium font-sans flex items-center hover:bg-gray-100 transition-colors"
            >
              <Music className="mr-2 h-5 w-5" />
              Play on Spotify
            </a>
          </div>
        </div>
        
        {/* Premium Features Info */}
        <div className="bg-gradient-to-r from-yellow-400 to-yellow-500 rounded-lg shadow-lg p-6">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-xl font-bold text-gray-900 font-sans">You have Premium Access!</h3>
              <p className="mt-1 text-gray-800 font-sans">Enjoy all features including AI Tools, Notes, and Comparisons</p>
            </div>
            <Trophy className="h-12 w-12 text-gray-900" />
          </div>
        </div>
      </div>
      
      {/* Modals */}
      <CornellNotesModal isOpen={showNotesModal} onClose={() => setShowNotesModal(false)} />
      <ComparisonModal isOpen={showComparisonModal} onClose={() => setShowComparisonModal(false)} />
    </div>
  );
};

// Home Page Component
const Home = () => {
  const { darkMode, setCurrentPage } = usePage();
  const { user, isPremium } = useAuth();
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 dark:text-chalk-white font-sans mb-4">
            Welcome to <span className="text-accent-blue">ImpactMojo</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-600 dark:text-gray-300 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Your platform for development learning and tools. Explore courses, labs, and AI-powered tools to enhance your impact.
          </p>
          <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
            <button
              onClick={() => setCurrentPage('courses')}
              className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-accent-blue hover:bg-blue-700 md:py-4 md:text-lg md:px-10 font-sans"
            >
              Get started
            </button>
            {user && (
              <button
                onClick={() => setCurrentPage('ai-tools')}
                className="mt-3 w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-accent-blue dark:text-accent-blue bg-white dark:bg-chalkboard-dark hover:bg-gray-50 dark:hover:bg-gray-700 md:py-4 md:text-lg md:px-10 font-sans sm:mt-0 sm:ml-3"
              >
                Try AI Tools
              </button>
            )}
          </div>
        </div>
        
        {/* Featured Content */}
        <div className="mt-16">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white text-center font-sans mb-8">Featured Content</h2>
          <div className="grid gap-5 max-w-lg mx-auto lg:grid-cols-3 lg:max-w-none">
            {courseData.slice(0, 3).map((course) => (
              <div key={course.id} className="flex flex-col rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
                <div className="flex-1 bg-white dark:bg-chalkboard-dark p-6 flex flex-col justify-between">
                  <div className="flex-1">
                    <p className="text-sm font-medium text-accent-blue dark:text-accent-blue font-sans">
                      <span>Course</span>
                    </p>
                    <h3 className="mt-2 text-xl font-semibold text-gray-900 dark:text-chalk-white font-sans">{course.title}</h3>
                    <p className="mt-3 text-base text-gray-600 dark:text-gray-300 font-sans">{course.description}</p>
                  </div>
                  <div className="mt-6">
                    <button
                      onClick={() => setCurrentPage('courses')}
                      className="text-base font-medium text-accent-blue dark:text-accent-blue hover:text-blue-800 dark:hover:text-blue-300 font-sans"
                    >
                      Explore courses
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Learning Tracks */}
        <div className="mt-16">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-chalk-white text-center font-sans mb-8">Learning Tracks</h2>
          <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-5">
            {[
              { name: "Research Methods", description: "Learn qualitative and quantitative research methods." },
              { name: "Data Analysis", description: "Master data analysis techniques for social impact." },
              { name: "Gender Studies", description: "Explore gender dynamics in development contexts." },
              { name: "Policy & Economics", description: "Understand policy and economic frameworks." },
              { name: "Thematic Areas", description: "Explore specialized topics across development sectors." }
            ].map((track, index) => (
              <div key={index} className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
                <h3 className="text-xl font-semibold mb-2 font-sans">{track.name}</h3>
                <p className="text-gray-600 dark:text-gray-300 font-sans">{track.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// Simple Courses Page Component
const CoursesPage = () => {
  const { darkMode } = usePage();
  const { user, toggleBookmark, bookmarks, toggleComparison, comparisons } = useAuth();
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-chalk-white mb-4 font-sans">
            Development Courses
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto font-sans">
            Comprehensive learning resources for development practitioners and changemakers.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {courseData.map((course) => {
            const isBookmarked = bookmarks.some(b => b.id === course.id);
            const isInComparison = comparisons.some(c => c.id === course.id);
            
            return (
              <div key={course.id} className="bg-white dark:bg-chalkboard-dark rounded-lg shadow hover:shadow-lg transition-shadow p-6">
                <div className="flex items-center justify-between mb-3">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-accent-blue text-white font-sans">
                    {course.id}
                  </span>
                  {user && (
                    <div className="flex gap-2">
                      <button
                        onClick={() => toggleBookmark(course.id, 'course')}
                        className={`p-1 rounded font-sans ${isBookmarked ? 'text-yellow-500' : 'text-gray-400'} hover:text-yellow-500`}
                      >
                        <Bookmark className="h-5 w-5" fill={isBookmarked ? 'currentColor' : 'none'} />
                      </button>
                      <button
                        onClick={() => toggleComparison(course.id, 'course')}
                        className={`p-1 rounded font-sans ${isInComparison ? 'text-blue-500' : 'text-gray-400'} hover:text-blue-500`}
                      >
                        <Target className="h-5 w-5" fill={isInComparison ? 'currentColor' : 'none'} />
                      </button>
                    </div>
                  )}
                </div>
                
                <h3 className="text-xl font-semibold text-gray-900 dark:text-chalk-white mb-2 font-sans">
                  {course.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4 font-sans">
                  {course.description}
                </p>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4 font-sans">
                  <span>{course.level}</span>
                  <span>{course.duration}</span>
                </div>
                
                <a
                  href={course.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full bg-accent-blue text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors font-sans inline-block text-center"
                >
                  Access Course
                </a>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// Simple Labs Page Component  
const LabsPage = () => {
  const { darkMode } = usePage();
  const { user, toggleBookmark, bookmarks, toggleComparison, comparisons } = useAuth();
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-chalk-white mb-4 font-sans">
            Interactive Labs
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto font-sans">
            Hands-on exercises and case studies for practical skill development.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {labsData.map((lab) => {
            const isBookmarked = bookmarks.some(b => b.id === lab.id);
            const isInComparison = comparisons.some(c => c.id === lab.id);
            
            return (
              <div key={lab.id} className="bg-white dark:bg-chalkboard-dark rounded-lg shadow hover:shadow-lg transition-shadow p-6">
                <div className="flex items-center justify-between mb-3">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-600 text-white font-sans">
                    {lab.id}
                  </span>
                  {user && (
                    <div className="flex gap-2">
                      <button
                        onClick={() => toggleBookmark(lab.id, 'lab')}
                        className={`p-1 rounded font-sans ${isBookmarked ? 'text-yellow-500' : 'text-gray-400'} hover:text-yellow-500`}
                      >
                        <Bookmark className="h-5 w-5" fill={isBookmarked ? 'currentColor' : 'none'} />
                      </button>
                      <button
                        onClick={() => toggleComparison(lab.id, 'lab')}
                        className={`p-1 rounded font-sans ${isInComparison ? 'text-blue-500' : 'text-gray-400'} hover:text-blue-500`}
                      >
                        <Target className="h-5 w-5" fill={isInComparison ? 'currentColor' : 'none'} />
                      </button>
                    </div>
                  )}
                </div>
                
                <h3 className="text-xl font-semibold text-gray-900 dark:text-chalk-white mb-2 font-sans">
                  {lab.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4 font-sans">
                  {lab.description}
                </p>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4 font-sans">
                  <span>{lab.topic}</span>
                  <span>{lab.difficulty || 'Interactive'}</span>
                </div>
                
                <a
                  href={lab.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 transition-colors font-sans flex items-center justify-center"
                >
                  <PlayCircle className="h-4 w-4 mr-2" />
                  Start Lab
                </a>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// Fixed Resources Page Component
const ResourcesPage = () => {
  const { darkMode } = usePage();
  const { user, toggleBookmark, bookmarks } = useAuth();
  
  return (
    <div className={`min-h-screen font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
      <Navigation />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-chalk-white mb-4 font-sans">
            Resources & Tools
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto font-sans">
            Additional resources, handouts, and premium tools for development professionals.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {premiumResources.map((resource, index) => {
            const isBookmarked = bookmarks.some(b => b.id === resource.id);
            
            return (
              <div key={resource.id} className="bg-white dark:bg-chalkboard-dark rounded-lg shadow hover:shadow-lg transition-shadow p-6">
                <div className="flex items-center justify-between mb-3">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-600 text-white font-sans">
                    {resource.id}
                  </span>
                  {user && (
                    <button
                      onClick={() => toggleBookmark(resource.id, 'resource')}
                      className={`p-1 rounded font-sans ${isBookmarked ? 'text-yellow-500' : 'text-gray-400'} hover:text-yellow-500`}
                    >
                      <Bookmark className="h-5 w-5" fill={isBookmarked ? 'currentColor' : 'none'} />
                    </button>
                  )}
                </div>
                
                <h3 className="text-xl font-semibold text-gray-900 dark:text-chalk-white mb-2 font-sans">
                  {resource.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 text-sm mb-4 font-sans">
                  {resource.description}
                </p>
                
                <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4 font-sans">
                  <span>{resource.category}</span>
                  <span>Resource</span>
                </div>
                
                <a
                  href="https://github.com/Varnasr/ImpactMojo/tree/main/Handouts"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full bg-purple-600 text-white py-2 px-4 rounded-md hover:bg-purple-700 transition-colors font-sans flex items-center justify-center"
                >
                  <FileText className="h-4 w-4 mr-2" />
                  Access Resource
                </a>
              </div>
            );
          })}
        </div>

        {/* Additional Handouts Section */}
        <div className="mt-16">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-chalk-white text-center mb-8 font-sans">
            Additional Handouts
          </h2>
          <div className="bg-white dark:bg-chalkboard-dark rounded-lg shadow-lg p-8 text-center">
            <FileText className="h-16 w-16 text-purple-600 mx-auto mb-4" />
            <h3 className="text-2xl font-semibold text-gray-900 dark:text-chalk-white mb-4 font-sans">
              Browse All Resources
            </h3>
            <p className="text-gray-600 dark:text-gray-300 mb-6 font-sans">
              Access our complete collection of handouts, guides, and reference materials on GitHub.
            </p>
            <a
              href="https://github.com/Varnasr/ImpactMojo/tree/main/Handouts"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center px-6 py-3 bg-purple-600 text-white font-medium rounded-md hover:bg-purple-700 transition-colors font-sans"
            >
              <ExternalLink className="h-5 w-5 mr-2" />
              View All Handouts
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

// Main App Content Component
const AppContent = () => {
  const { currentPage, darkMode } = usePage();
  const { loading } = useAuth();
  
  if (loading) {
    return (
      <div className={`min-h-screen flex items-center justify-center font-sans ${darkMode ? 'dark bg-chalkboard-dark' : 'bg-chalk-white'}`}>
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-accent-blue"></div>
      </div>
    );
  }
  
  return (
    <div className={darkMode ? 'dark' : ''}>
      {currentPage === 'home' && <Home />}
      {currentPage === 'dashboard' && <Dashboard />}
      {currentPage === 'courses' && <CoursesPage />}
      {currentPage === 'labs' && <LabsPage />}
      {currentPage === 'resources' && <ResourcesPage />}
      {currentPage === 'ai-tools' && <AIToolsPage />}
    </div>
  );
};

// Main App Component
const App = () => {
  return (
    <AuthProvider>
      <PageProvider>
        <AppContent />
      </PageProvider>
    </AuthProvider>
  );
};

export default App;

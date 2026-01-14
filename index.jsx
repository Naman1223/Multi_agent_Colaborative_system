import React, { useState, useEffect } from 'react';
import { Play, Menu, Search, Upload, Bell, User, ChevronLeft, ChevronRight } from 'lucide-react';

const StreamLine = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [searchFocused, setSearchFocused] = useState(false);
  const [activeCategory, setActiveCategory] = useState('All');
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);

  // Mock video data
  const mockVideos = [
    {
      id: 1,
      title: "Building a Modern React Application with Tailwind CSS",
      channel: "React Masters",
      views: "120K",
      timestamp: "2 days ago",
      duration: "15:42",
      thumbnail: "https://picsum.photos/320/180?random=1"
    },
    {
      id: 2,
      title: "Advanced State Management with Context API",
      channel: "Code Academy",
      views: "85K",
      timestamp: "1 week ago",
      duration: "22:15",
      thumbnail: "https://picsum.photos/320/180?random=2"
    },
    {
      id: 3,
      title: "Creating Beautiful UIs with Framer Motion",
      channel: "Design Wizard",
      views: "210K",
      timestamp: "3 weeks ago",
      duration: "18:30",
      thumbnail: "https://picsum.photos/320/180?random=3"
    },
    {
      id: 4,
      title: "Performance Optimization Techniques for React Apps",
      channel: "Web Dev Simplified",
      views: "156K",
      timestamp: "1 month ago",
      duration: "28:45",
      thumbnail: "https://picsum.photos/320/180?random=4"
    },
    {
      id: 5,
      title: "Building RESTful APIs with Node.js and Express",
      channel: "Backend Experts",
      views: "98K",
      timestamp: "5 days ago",
      duration: "35:20",
      thumbnail: "https://picsum.photos/320/180?random=5"
    },
    {
      id: 6,
      title: "Introduction to GraphQL for Beginners",
      channel: "API University",
      views: "76K",
      timestamp: "2 weeks ago",
      duration: "42:10",
      thumbnail: "https://picsum.photos/320/180?random=6"
    },
    {
      id: 7,
      title: "CSS Grid vs Flexbox: When to Use Which",
      channel: "CSS Masters",
      views: "142K",
      timestamp: "4 days ago",
      duration: "19:55",
      thumbnail: "https://picsum.photos/320/180?random=7"
    },
    {
      id: 8,
      title: "Testing React Applications with Jest and React Testing Library",
      channel: "Quality Code",
      views: "63K",
      timestamp: "3 days ago",
      duration: "26:35",
      thumbnail: "https://picsum.photos/320/180?random=8"
    }
  ];

  // Categories
  const categories = [
    'All', 'React', 'JavaScript', 'CSS', 'Web Development', 
    'Node.js', 'GraphQL', 'TypeScript', 'State Management', 
    'UI/UX', 'Performance', 'Responsive Design'
  ];

  // Simulate loading
  useEffect(() => {
    const timer = setTimeout(() => {
      setVideos(mockVideos);
      setLoading(false);
    }, 800);
    return () => clearTimeout(timer);
  }, []);

  // Handle category scroll
  const scrollToCategory = (index) => {
    const categoryBar = document.getElementById('category-bar');
    if (categoryBar) {
      const scrollTo = index * 100 - 50;
      categoryBar.scrollTo({ left: scrollTo, behavior: 'smooth' });
    }
  };

  // Video Card Component
  const VideoCard = ({ video }) => (
    <div className="group cursor-pointer">
      <div className="relative aspect-video bg-zinc-800 rounded-lg overflow-hidden transition-transform duration-150 hover:scale-[1.02] hover:shadow-xl">
        {loading ? (
          <div className="w-full h-full bg-zinc-800 animate-pulse"></div>
        ) : (
          <>
            <img 
              src={video.thumbnail} 
              alt={video.title} 
              className="w-full h-full object-cover"
              loading="lazy"
            />
            <div className="absolute bottom-2 right-2 bg-black bg-opacity-80 text-white text-xs px-1.5 py-0.5 rounded">
              {video.duration}
            </div>
          </>
        )}
      </div>
      <div className="mt-3 flex gap-3">
        <div className="flex-shrink-0">
          <div className="w-9 h-9 rounded-full bg-zinc-700 flex items-center justify-center">
            <span className="text-xs font-medium text-zinc-300">
              {video.channel.charAt(0)}
            </span>
          </div>
        </div>
        <div>
          <h3 className={`font-medium text-zinc-100 line-clamp-2 text-sm ${loading ? 'bg-zinc-800 animate-pulse h-4 w-40 rounded mb-2' : ''}`}>
            {!loading && video.title}
          </h3>
          <p className={`text-zinc-400 text-xs mt-1 ${loading ? 'bg-zinc-800 animate-pulse h-3 w-24 rounded' : ''}`}>
            {!loading && video.channel}
          </p>
          <p className={`text-zinc-400 text-xs ${loading ? 'bg-zinc-800 animate-pulse h-3 w-32 rounded mt-1' : ''}`}>
            {!loading && `${video.views} views • ${video.timestamp}`}
          </p>
        </div>
      </div>
    </div>
  );

  // Category Chip Component
  const CategoryChip = ({ label, isActive, index }) => (
    <button
      onClick={() => {
        setActiveCategory(label);
        scrollToCategory(index);
      }}
      className={`px-4 py-1.5 rounded-lg text-sm font-medium transition-colors whitespace-nowrap
        ${isActive ? 'bg-red-700 text-white' : 'bg-zinc-800 text-zinc-100 hover:bg-zinc-700'}`}
    >
      {label}
    </button>
  );

  // Sidebar Navigation Items
  const navItems = [
    { icon: Play, label: 'Home', active: true },
    { icon: TrendingUp, label: 'Trending' },
    { icon: Youtube, label: 'Subscriptions' },
    { icon: Library, label: 'Library' },
    { icon: History, label: 'History' },
  ];

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100">
      {/* Global Navbar */}
      <header className="fixed top-0 left-0 right-0 z-50 bg-zinc-950 border-b border-zinc-800">
        <div className="flex items-center justify-between px-4 py-3">
          <div className="flex items-center">
            <button 
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="p-2 rounded-lg hover:bg-zinc-800 mr-2 transition-colors"
              aria-label="Toggle Menu"
            >
              <Menu size={20} />
            </button>
            <div className="flex items-center">
              <Play className="text-red-600" size={24} />
              <span className="ml-1 text-xl font-bold">StreamLine</span>
            </div>
          </div>

          <div className={`flex-1 max-w-2xl mx-6 transition-all duration-300 ${searchFocused ? 'md:w-[400px]' : 'md:w-[300px]'}`}>
            <div className={`relative flex items-center rounded-lg ${
              searchFocused 
                ? 'bg-zinc-900 ring-1 ring-blue-500' 
                : 'bg-zinc-900 hover:bg-zinc-800'
            }`}>
              <input
                type="text"
                placeholder="Search videos..."
                className="w-full bg-transparent border-0 focus:ring-0 py-2 px-4 text-zinc-100"
                onFocus={() => setSearchFocused(true)}
                onBlur={() => setSearchFocused(false)}
              />
              <button className="absolute right-3 p-1 hover:bg-zinc-700 rounded-full transition-colors" aria-label="Search">
                <Search size={20} className="text-zinc-400" />
              </button>
            </div>
          </div>

          <div className="flex items-center space-x-2">
            <button className="p-2 rounded-lg hover:bg-zinc-800 transition-colors" aria-label="Upload">
              <Upload size={20} />
            </button>
            <button className="p-2 rounded-lg hover:bg-zinc-800 transition-colors" aria-label="Notifications">
              <Bell size={20} />
            </button>
            <button className="p-2 rounded-lg hover:bg-zinc-800 transition-colors" aria-label="User Profile">
              <User size={20} />
            </button>
          </div>
        </div>
      </header>

      <div className="flex pt-16">
        {/* Responsive Sidebar */}
        <aside 
          className={`fixed lg:static z-40 h-[calc(100vh-4rem)] bg-zinc-900 transition-all duration-300 overflow-hidden
            ${sidebarOpen ? 'w-64 left-0' : 'w-0 -left-64'} lg:w-64 lg:left-0 border-r border-zinc-800`}
        >
          <div className="p-4">
            <nav>
              <ul className="space-y-1">
                {navItems.map((item, index) => (
                  <li key={index}>
                    <a
                      href="#"
                      className={`flex items-center px-4 py-3 rounded-lg transition-colors ${
                        item.active 
                          ? 'bg-zinc-800 border-l-4 border-red-600 text-red-500' 
                          : 'text-zinc-400 hover:bg-zinc-800'
                      }`}
                    >
                      <item.icon size={20} className="mr-3" />
                      <span>{item.label}</span>
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          </div>
        </aside>

        {/* Main Content */}
        <main className={`flex-1 transition-all ${sidebarOpen ? 'lg:ml-0' : 'ml-0 lg:ml-64'}`}>
          {/* Category Bar */}
          <div className="sticky top-16 z-20 bg-zinc-950 py-3 mb-4 overflow-x-auto no-scrollbar px-4">
            <div id="category-bar" className="flex space-x-3 pb-1">
              {categories.map((category, index) => (
                <CategoryChip
                  key={index}
                  label={category}
                  isActive={activeCategory === category}
                  index={index}
                />
              ))}
            </div>
          </div>

          {/* Video Grid */}
          <div className="px-4 pb-8">
            {loading ? (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 gap-y-8">
                {Array.from({ length: 8 }).map((_, index) => (
                  <div key={index} className="group">
                    <div className="aspect-video bg-zinc-800 rounded-lg animate-pulse"></div>
                    <div className="mt-3 flex gap-3">
                      <div className="flex-shrink-0">
                        <div className="w-9 h-9 rounded-full bg-zinc-800 animate-pulse"></div>
                      </div>
                      <div className="flex-1">
                        <div className="h-4 bg-zinc-800 rounded mb-2 animate-pulse"></div>
                        <div className="h-3 bg-zinc-800 rounded w-3/4 animate-pulse"></div>
                        <div className="h-3 bg-zinc-800 rounded w-1/2 mt-1 animate-pulse"></div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 gap-y-8">
                {videos.map(video => (
                  <VideoCard key={video.id} video={video} />
                ))}
              </div>
            )}
          </div>
        </main>
      </div>

      {/* Mobile Sidebar Overlay */}
      {sidebarOpen && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-30 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        ></div>
      )}
    </div>
  );
};

// Additional Icon Components (implementing outlined style)
const TrendingUp = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18" />
    <polyline points="17 6 23 6 23 12" />
  </svg>
);

const Youtube = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z" />
    <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" />
  </svg>
);

const Library = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M16 6h2a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2" />
    <rect x="8" y="6" width="8" height="14" rx="1" />
    <path d="M9 3h6" />
  </svg>
);

const History = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <circle cx="12" cy="12" r="10" />
    <polyline points="12 6 12 12 16 14" />
  </svg>
);

export default StreamLine;
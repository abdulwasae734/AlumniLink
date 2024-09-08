import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from "./pages/Home";
import Contact from "./pages/Contact";
import About from "./pages/About";
import Chatbot from "./components/Chatbot";  
import Alumni from './pages/Alumni';
import './App.css'; 

function App() {
  const [isChatbotOpen, setIsChatbotOpen] = useState(false);

  const toggleChatbot = () => {
    setIsChatbotOpen(!isChatbotOpen);
  };

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/alumni">Alumni</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/alumni" element={<Alumni />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>

        <button className="chatbot-button" onClick={toggleChatbot}>
          💬
        </button>

        {isChatbotOpen && (
          <div className="chatbot-popup">
            <Chatbot />
          </div>
        )}
      </div>
    </Router>
  );
}

export default App;

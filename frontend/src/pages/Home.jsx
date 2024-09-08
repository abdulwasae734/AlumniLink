import React from 'react';
import { Player } from '@lottiefiles/react-lottie-player';
import './Home.css';
import animationData from '../assets/Animation - 1725804069711.json'; 

const Home = () => {
  return (
    <div className="hero-section">
      <div className="hero-content">
        <h1>Welcome to Alumni Connect</h1>
        <p>
          Stay connected with your alma mater and fellow alumni. Engage in networking, mentorship, and more through our platform.
        </p>
        <button className="cta-button">Get Started</button>
      </div>
      <div className="hero-animation">
        <Player
          autoplay
          loop
          src={animationData}
          style={{ height: '600px', width: '600px' }}
        />
      </div>
    </div>
  );
}

export default Home;

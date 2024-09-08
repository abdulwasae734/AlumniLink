import React from 'react';
import './Alumni.css';

const alumniData = [
  {
    name: 'John Doe',
    contact: 'johndoe@example.com',
    education: 'B.Tech in Computer Science, CBIT',
    employment: 'Software Engineer at Google',
    expertise: 'Full-Stack Development, AI, Cloud Computing',
  },
  {
    name: 'Jane Smith',
    contact: 'janesmith@example.com',
    education: 'MBA, Harvard Business School',
    employment: 'Product Manager at Microsoft',
    expertise: 'Product Management, Marketing, Strategy',
  },
  {
    name: 'John Doe',
    contact: 'johndoe@example.com',
    education: 'B.Tech in Computer Science, CBIT',
    employment: 'Software Engineer at Google',
    expertise: 'Full-Stack Development, AI, Cloud Computing',
  },
  {
    name: 'Jane Smith',
    contact: 'janesmith@example.com',
    education: 'MBA, Harvard Business School',
    employment: 'Product Manager at Microsoft',
    expertise: 'Product Management, Marketing, Strategy',
  },
  {
    name: 'John Doe',
    contact: 'johndoe@example.com',
    education: 'B.Tech in Computer Science, CBIT',
    employment: 'Software Engineer at Google',
    expertise: 'Full-Stack Development, AI, Cloud Computing',
  },
  {
    name: 'Jane Smith',
    contact: 'janesmith@example.com',
    education: 'MBA, Harvard Business School',
    employment: 'Product Manager at Microsoft',
    expertise: 'Product Management, Marketing, Strategy',
  },
  {
    name: 'John Doe',
    contact: 'johndoe@example.com',
    education: 'B.Tech in Computer Science, CBIT',
    employment: 'Software Engineer at Google',
    expertise: 'Full-Stack Development, AI, Cloud Computing',
  },
  {
    name: 'Jane Smith',
    contact: 'janesmith@example.com',
    education: 'MBA, Harvard Business School',
    employment: 'Product Manager at Microsoft',
    expertise: 'Product Management, Marketing, Strategy',
  },
];

const Alumni = () => {
  return (
    <div>
      <div className="hero-sectionn">
        <p>Find and connect with alumni from various fields and industries. Grow your network and explore opportunities!</p>
      </div>

      <div className="alumni-container">
        {alumniData.map((alumni, index) => (
          <div className="alumni-card" key={index}>
            <h2>{alumni.name}</h2>
            <p><strong>Contact:</strong> {alumni.contact}</p>
            <p><strong>Education:</strong> {alumni.education}</p>
            <p><strong>Current Employment:</strong> {alumni.employment}</p>
            <p><strong>Expertise:</strong> {alumni.expertise}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Alumni;

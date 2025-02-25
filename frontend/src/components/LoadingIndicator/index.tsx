import React from 'react';
import './LoadingIndicator.css'; // Import the CSS file for styling

export const LoadingIndicator: React.FC = () => {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>Generating blog post...</p>
    </div>
  );
};

// src/components/result/LoadingSpinner/LoadingSpinner.jsx
import React from 'react';
import { Music } from 'lucide-react';
import './LoadingSpinner.css';

const LoadingSpinner = ({ message = 'Loading...' }) => {
  return (
    <div className="loading-spinner">
      <div className="spinner-container">
        <div className="spinner-icon">
          <Music className="spinning-icon" />
        </div>
        <div className="spinner-dots">
          <span className="dot dot--1"></span>
          <span className="dot dot--2"></span>
          <span className="dot dot--3"></span>
        </div>
      </div>
      <p className="loading-message">{message}</p>
    </div>
  );
};

export default LoadingSpinner;
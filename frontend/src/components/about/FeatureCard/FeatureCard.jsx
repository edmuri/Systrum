// src/components/about/FeatureCard/FeatureCard.jsx
import React from 'react';
import './FeatureCard.css';

const FeatureCard = ({ icon: Icon, title, description, delay = 0 }) => {
  return (
    <div 
      className="feature-card"
      style={{ '--animation-delay': `${delay}s` }}
    >
      <div className="feature-card__icon">
        <Icon size={28} />
      </div>
      <div className="feature-card__content">
        <h3 className="feature-card__title">{title}</h3>
        <p className="feature-card__description">{description}</p>
      </div>
    </div>
  );
};

export default FeatureCard;
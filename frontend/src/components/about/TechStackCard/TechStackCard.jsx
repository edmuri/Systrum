// src/components/about/TechStackCard/TechStackCard.jsx
import React from 'react';
import './TechStackCard.css';

const TechStackCard = ({ name, description, icon: Icon, delay = 0 }) => {
  return (
    <div 
      className="tech-stack-card"
      style={{ '--animation-delay': `${delay}s` }}
    >
      <div className="tech-stack-card__header">
        <div className="tech-stack-card__icon">
          <Icon size={24} />
        </div>
        <h4 className="tech-stack-card__name">{name}</h4>
      </div>
      <p className="tech-stack-card__description">{description}</p>
    </div>
  );
};

export default TechStackCard;
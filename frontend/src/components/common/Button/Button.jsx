// components/common/Button/Button.jsx
import React from 'react';
import './Button.css';

const Button = ({ 
    children, 
    variant = 'primary', 
    size = 'medium', 
    onClick, 
    disabled = false, 
    icon: Icon,
    iconPosition = 'left',
    className = '',
    ...props 
        }) => {
        const buttonClass = [
            'spotify-button',
            `spotify-button--${variant}`,
            `spotify-button--${size}`,
            disabled && 'spotify-button--disabled',
            className
        ].filter(Boolean).join(' ');

return (
    <button 
    className={buttonClass}
    onClick={onClick}
    disabled={disabled}
    {...props}
    >
    {Icon && iconPosition === 'left' && <Icon className="spotify-button__icon spotify-button__icon--left" />}
    <span className="spotify-button__text">{children}</span>
    {Icon && iconPosition === 'right' && <Icon className="spotify-button__icon spotify-button__icon--right" />}
    </button>
    );
};

export default Button;
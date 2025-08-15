// src/components/common/TextInput/TextInput.jsx
import React, { forwardRef } from 'react';
import { AlertCircle } from 'lucide-react';
import './TextInput.css';

const TextInput = forwardRef(({
  value,
  onChange,
  placeholder = '',
  disabled = false,
  error = '',
  maxLength,
  className = '',
  size = 'large',
  ...props
}, ref) => {
  const inputClasses = [
    'text-input',
    `text-input--${size}`,
    error && 'text-input--error',
    disabled && 'text-input--disabled',
    className
  ].filter(Boolean).join(' ');

  return (
    <div className="text-input-wrapper">
      <div className="text-input-container">
        <input
          ref={ref}
          type="text"
          value={value}
          onChange={onChange}
          placeholder={placeholder}
          disabled={disabled}
          maxLength={maxLength}
          className={inputClasses}
          {...props}
        />
        {maxLength && (
          <div className="text-input-counter">
            <span className={value.length > maxLength * 0.8 ? 'text-input-counter--warning' : ''}>
              {value.length}/{maxLength}
            </span>
          </div>
        )}
      </div>
      {error && (
        <div className="text-input-error-message">
          <AlertCircle size={16} />
          <span>{error}</span>
        </div>
      )}
    </div>
  );
});

TextInput.displayName = 'TextInput';

export default TextInput;
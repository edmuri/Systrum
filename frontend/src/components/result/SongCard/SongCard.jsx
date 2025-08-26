// src/components/result/SongCard/SongCard.jsx
import React from 'react';
import { ExternalLink, Play } from 'lucide-react';
import './SongCard.css';

const SongCard = ({ song, index, delay = 0 }) => {
  const handleOpenSpotify = () => {
    window.open(song.url, '_blank');
  };

  return (
    <div 
      className="song-card"
      style={{ '--animation-delay': `${delay}s` }}
    >
      <div className="song-card__index">
        {index}
      </div>
      
      <div className="song-card__cover">
        <img 
          src={song.cover} 
          alt={`${song.album} cover`}
          loading="lazy"
        />
        <div className="song-card__cover-overlay">
          <button 
            className="play-button"
            onClick={handleOpenSpotify}
            aria-label={`Play ${song.name} on Spotify`}
          >
            <Play size={20} />
          </button>
        </div>
      </div>

      <div className="song-card__info">
        <div className="song-card__main">
          <h3 className="song-card__name">{song.name}</h3>
          <p className="song-card__artist">{song.artist}</p>
        </div>
        <div className="song-card__meta">
          <span className="song-card__album">{song.album}</span>
        </div>
      </div>

      <div className="song-card__actions">
        <button
          className="external-link-button"
          onClick={handleOpenSpotify}
          aria-label={`Open ${song.name} on Spotify`}
        >
          <ExternalLink size={16} />
        </button>
      </div>
    </div>
  );
};

export default SongCard;
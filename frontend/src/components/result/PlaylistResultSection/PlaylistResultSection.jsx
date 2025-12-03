// src/components/result/PlaylistResultSection/PlaylistResultSection.jsx
import React, { useState, useEffect, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Music, Play, ExternalLink, ArrowLeft, Share, Download } from 'lucide-react';
import Button from '../../common/Button/Button';
import SongCard from '../SongCard/SongCard';
import LoadingSpinner from '../LoadingSpinner/LoadingSpinner';
import './PlaylistResultSection.css';

const PlaylistResultSection = () => {
  const [playlist, setPlaylist] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sentence, setSentence] = useState('');

  const location = useLocation();
  const navigate = useNavigate();
  const rootRef = useRef(null);

  function seperateCookies(cookie) {
    const cookieArray = cookie.split("; ");

    const cookiesMap = {};

    cookieArray.forEach(cookie => {
      const [key, value] = cookie.split("=");
      cookiesMap[key] = value;
    })

    return cookiesMap;
  };

  // Animation observer
  useEffect(() => {
    const el = rootRef.current;
    if (!el) return;

    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) el.classList.add('animate');
        else el.classList.remove('animate');
      },
      { root: null, threshold: 0.25 }
    );
    io.observe(el);
    return () => io.disconnect();
  }, []);

  // Fetch playlist data
  useEffect(() => {
    const fetchPlaylist = async () => {
      try {
        // Get sentence from navigation state or URL params
        const sentenceFromState = location.state?.sentence;
        const urlParams = new URLSearchParams(location.search); //where is this being used
        const sentenceFromUrl = urlParams.get('sentence');
        // const userIDFromUrl = urlParams.get('userID');

        let currentSentence = sentenceFromState || sentenceFromUrl;

        // if(userIDFromUrl){
        //   document.cookie = "userID" + "=" + userIDFromUrl+ "; path=/";
        // }
        // else if(!userIDFromUrl){
        //   document.cookie = "userID" + "=" + null + "; path=/";
        // }
        /* check cookie */
        const temp = `; ${document.cookie}`;
        console.log(temp);
        let cookiesMap = {};

        if (temp != null) {
          cookiesMap = seperateCookies(temp);
        }

        console.log(cookiesMap);

        if (!currentSentence & cookiesMap == null) {
          // console.log("Inside if");
          setError('No sentence provided');
          setLoading(false);
          return;
        }

        if (!currentSentence & cookiesMap['Sentence'] != null) {
          currentSentence = cookiesMap['Sentence'];
        }

        console.log("Setting Sentence");
        setSentence(currentSentence);

        console.log("Making call");
        // Call backend API
        const response = await fetch(`http://localhost:5000/createPlaylist?sentence=${encodeURIComponent(currentSentence)}`);

        if (!response.ok) {
          throw new Error('Failed to generate playlist');
        }

        const playlistData = await response.json();
        console.log("SettingPlaylist");
        setPlaylist(playlistData);
        setLoading(false);

        document.cookie = "Sentence" + "=" + currentSentence + "; path=/";

      } catch (err) {
        console.error('Error fetching playlist:', err);
        setError('Failed to generate playlist. Please try again.');
        setLoading(false);
      }
    };

    fetchPlaylist();
  }, [location]);

  const handleGoBack = () => {
    navigate('/CreatePlaylist');
  };

  const handleSharePlaylist = () => {

  };

  const handleTryAgain = () => {
    navigate('/CreatePlaylist', { state: { sentence } });
  };

  if (loading) {
    return (
      <section className="result-section">
        <div className="result-section__container">
          <LoadingSpinner message="Generating your playlist..." />
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="result-section">
        <div className="result-section__container">
          <div className="error-state">
            <h1>Oops! Something went wrong</h1>
            <p>{error}</p>
            <div className="error-actions">
              <Button variant="primary" onClick={handleTryAgain} icon={Play}>
                Try Again
              </Button>
              <Button variant="secondary" onClick={handleGoBack} icon={ArrowLeft}>
                Go Back
              </Button>
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section ref={rootRef} className="result-section" aria-labelledby="result-title">
      {/* Background effects */}
      <div className="result-section__bg" aria-hidden="true">
        <div className="result-section__vignette vignette" />
      </div>

      <div className="result-section__shapes" aria-hidden="true">
        <span className="shape shape--lg shape--tl" />
        <span className="shape shape--md shape--br" />
        <span className="shape shape--sm shape--l" />
      </div>

      <div className="result-section__notes" aria-hidden="true">
        <Music className="note note--a" />
        <Play className="note note--b" />
        <Music className="note note--c" />
      </div>

      <div className="result-section__container">
        {/* Header */}
        <header className="result-section__header">
          <Button
            variant="ghost"
            size="small"
            onClick={handleGoBack}
            icon={ArrowLeft}
            className="back-button"
          >
            Back
          </Button>

          <div className="result-section__title-area">
            <h1 id="result-title" className="result-section__title">
              Your Playlist
              <span className="title-accent">
                <Music />
              </span>
            </h1>
            <p className="result-section__sentence">"{sentence}"</p>
            <p className="result-section__subtitle">
              {playlist.length} songs • Generated with Systrum
            </p>
          </div>

          <div className="result-section__actions">
            <a href="http://localhost:5000/authorizeUser">
              <Button
                variant="secondary"
                size="small"
                onClick={handleSharePlaylist}
                icon={Share}
              >
                Share
              </Button></a>
          </div>
        </header>

        {/* Playlist */}
        <div className="playlist-container">
          <div className="playlist-header">
            <div className="playlist-stats">
              <span className="song-count">{playlist.length} tracks</span>
              <span className="separator">•</span>
              <span className="created-with">Created with Systrum</span>
            </div>
          </div>

          <div className="songs-list">
            {playlist.map((song, index) => (
              <SongCard
                key={`${song.id}-${index}`}
                song={song}
                index={index + 1}
                delay={index * 0.1}
              />
            ))}
          </div>
        </div>

        {/* Footer actions */}
        <div className="result-section__footer">
          <Button
            variant="primary"
            size="large"
            onClick={handleTryAgain}
            icon={Play}
          >
            Create Another Playlist
          </Button>
          <Button
            variant="secondary"
            size="large"
            onClick={() => navigate('/')}
          >
            Back to Home
          </Button>
        </div>
      </div>
    </section>
  );
};

export default PlaylistResultSection;
// src/components/create/CreatePlaylistSection/CreatePlaylistSection.jsx
import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Music, Send, Sparkles } from 'lucide-react';
import Button from '../../common/Button/Button';
import TextInput from '../../common/TextInput/TextInput';
import './CreatePlaylistSection.css';

const CreatePlaylistSection = () => {
  const [sentence, setSentence] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const rootRef = useRef(null);

  // Same intersection observer animation as WelcomeSection
  useEffect(() => {
    const el = rootRef.current;
    if (!el) return;

    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) el.classList.add('animate');
        else el.classList.remove('animate');
      },
      { 
        root: null, 
        threshold: 0.25 
      }
    );
    io.observe(el);
    return () => io.disconnect();
  }, []);

  const handleCreatePlaylist = async () => {

        let response = await fetch(`http://127.0.0.1:5000/createPlaylist?sentence=${sentence}`,{
            method:'GET',
            mode: 'cors',
            headers:{
                'Content-Type':'application/json',
                'Accept':'application/json'
            }
        })

        let data = await response.json();

        console.log(data);

        // let path = "/About"
        // useNavigate(path);
        navigate('/AboutPage');
  };

  const handleInputChange = (e) => {
    setSentence(e.target.value);
  };

  const isDisabled = !sentence.trim() || isLoading;

  return (
    <section ref={rootRef} className="create-section" aria-labelledby="create-title">
      {/* Background effects - same as WelcomeSection */}
      <div className="create-section__bg" aria-hidden="true">
        <div className="create-section__vignette" />
      </div>

      {/* Animated shapes */}
      <div className="create-section__shapes" aria-hidden="true">
        <span className="shape shape--lg shape--tl" />
        <span className="shape shape--md shape--br" />
        <span className="shape shape--sm shape--l" />
      </div>

      {/* Music notes */}
      <div className="create-section__notes" aria-hidden="true">
        <Music className="note note--a" />
        <Sparkles className="note note--b" />
        <Music className="note note--c" />
      </div>

      <div className="create-section__container">
        <header className="create-section__header">
          <h1 id="create-title" className="create-section__title">
            What's your vibe?
            <span className="title-accent" aria-hidden="true">
              <Music />
            </span>
          </h1>
          <p className="create-section__description">
            Type any sentence and we'll turn each word into a song. 
            <br />
            <span className="highlight">Every word becomes part of your story.</span>
          </p>
        </header>

        <div className="create-section__input-area">
          <TextInput
            value={sentence}
            onChange={handleInputChange}
            placeholder="I love sunny days..."
            maxLength={100}
            disabled={isLoading}
            className="create-section__input"
          />
          
          <Button
            variant="primary"
            size="large"
            onClick={handleCreatePlaylist}
            disabled={isDisabled}
            loading={isLoading}
            icon={Send}
            iconPosition="right"
            className="create-section__submit-button"
          >
            {isLoading ? 'Creating...' : 'Create Playlist'}
          </Button>
        </div>

        <aside className="create-section__examples" aria-label="Example inputs">
          <p className="create-section__examples-label">Need inspiration? Try these:</p>
          <div className="create-section__examples-grid">
            {[
              "I love you",
              "Good morning sunshine", 
              "Dancing through life",
              "Midnight city dreams"
            ].map((example, index) => (
              <button
                key={index}
                className="example-chip"
                onClick={() => setSentence(example)}
                disabled={isLoading}
              >
                "{example}"
              </button>
            ))}
          </div>
        </aside>
      </div>
    </section>
  );
};

export default CreatePlaylistSection;
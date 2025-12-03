import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Music, Play } from 'lucide-react';
import Button from '../../common/Button/Button';
import './WelcomeSection.css';

const WelcomeSection = () => {
    const navigate = useNavigate();
    const rootRef = useRef(null);

    // animations only happen when in view
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

    const handleGetStarted = () => navigate('/CreatePlaylist');
    const handleToAbout = () => navigate('/AboutPage');

    return (
        <section ref={rootRef} className="welcome-section" aria-labelledby="welcome-title">
            {/* background */}
            <div className="welcome-section__bg" aria-hidden="true">
                <div className="welcome-section__vignette vignette" />
            </div>

            {/* bubbles */}
            <div className="welcome-section__shapes" aria-hidden="true">
                <span className="shape shape--lg shape--tl" />
                <span className="shape shape--md shape--br" />
                <span className="shape shape--sm shape--l" />
            </div>

            {/* notes */}
            <div className="welcome-section__notes" aria-hidden="true">
                <Music className="note note--a" />
                <Music className="note note--b" />
                <Music className="note note--c" />
            </div>

            <div className="welcome-section__container">
                <header className="welcome-section__header">
                    <div className="welcome-section__brand" role="img" aria-label="Systrum brand">
                        <h1 id="welcome-title" className="welcome-section__title">
                            SYSTRUM
                            <span className="brand-mark" aria-hidden="true">
                                <Music />
                            </span>
                        </h1>
                    </div>

                    <p className="welcome-section__tagline">
                        Turn any sentence into a <span className="highlight">personalized Spotify playlist</span>
                    </p>
                    <p className="welcome-section__description">
                        Every word becomes a track. Every sentence becomes a story: Curated by the algorithm, tuned to you.
                    </p>
                </header>

                <aside className="welcome-section__example" aria-label="Example input">
                    <p className="welcome-section__example-label">Try typing something like:</p>
                    <div className="welcome-section__example-text">
                        <span className="welcome-section__example-quote">“I love you”</span>
                    </div>
                    <p className="welcome-section__example-description">
                        We’ll map each word to a song and build a playlist that fits the mood.
                    </p>
                </aside>

                <div className="welcome-section__cta">
                    <Button
                        variant="primary"
                        size="welcome"
                        onClick={handleGetStarted}
                        icon={Play}
                        iconPosition="left"
                        className="welcome-section__cta-button"
                        aria-label="Create your playlist"
                    >
                        Create Your Playlist
                    </Button>
                </div>
                {/* <div className="welcome-section__cta">
        <Button
            variant="primary"
            size="welcome"
            onClick={handleToAbout}
            // icon={Play}
            iconPosition="left"
            className="welcome-section__cta-button"
            aria-label="Create your playlist"
        >
            About Systrum
        </Button> */}
                {/* </div> */}
            </div>
        </section>
    );
};

export default WelcomeSection;

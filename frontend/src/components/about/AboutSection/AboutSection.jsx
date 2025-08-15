// src/components/about/AboutSection/AboutSection.jsx
import React, { useEffect, useRef } from 'react';
import { Music, Code, Database, Zap, Sparkles, Heart } from 'lucide-react';
import TechStackCard from '../TechStackCard/TechStackCard';
import FeatureCard from '../FeatureCard/FeatureCard';
import './AboutSection.css';

const AboutSection = () => {
  const rootRef = useRef(null);

  // Same intersection observer animation as other sections
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

  const techStack = {
    frontend: [
      { name: 'React 19', description: 'Modern UI library with hooks and components', icon: Code },
      { name: 'Vite', description: 'Lightning-fast build tool and dev server', icon: Zap },
      { name: 'React Router', description: 'Client-side routing for single-page application', icon: Code },
      { name: 'Lucide Icons', description: 'Beautiful, customizable SVG icon library', icon: Sparkles }
    ],
    backend: [
      { name: 'Flask', description: 'Lightweight Python web framework', icon: Code },
      { name: 'SQLite', description: 'Local database for caching song searches', icon: Database },
      { name: 'Spotify API', description: 'Music data and playlist creation', icon: Music },
      { name: 'Python', description: 'Backend logic and API integration', icon: Code }
    ]
  };

  const features = [
    {
      icon: Music,
      title: 'Word-to-Song Mapping',
      description: 'Each word in your sentence becomes a carefully selected track from Spotify\'s vast library.'
    },
    {
      icon: Zap,
      title: 'Smart Caching',
      description: 'Previously searched songs are cached locally for lightning-fast playlist generation.'
    },
    {
      icon: Heart,
      title: 'Mood Recognition',
      description: 'The algorithm considers context and sentiment to create playlists that match your vibe.'
    },
    {
      icon: Sparkles,
      title: 'Instant Playlists',
      description: 'Generate personalized Spotify playlists in seconds, ready to save and share.'
    }
  ];

  return (
    <section ref={rootRef} className="about-section" aria-labelledby="about-title">
      {/* Background effects - consistent with other sections */}
      <div className="about-section__bg" aria-hidden="true">
        <div className="about-section__vignette" />
      </div>

      {/* Animated shapes */}
      <div className="about-section__shapes" aria-hidden="true">
        <span className="shape shape--lg shape--tl" />
        <span className="shape shape--md shape--br" />
        <span className="shape shape--sm shape--l" />
      </div>

      {/* Music notes */}
      <div className="about-section__notes" aria-hidden="true">
        <Music className="note note--a" />
        <Code className="note note--b" />
        <Sparkles className="note note--c" />
      </div>

      <div className="about-section__container">
        {/* Hero section */}
        <header className="about-section__hero">
          <h1 id="about-title" className="about-section__title">
            About Systrum
            <span className="title-accent" aria-hidden="true">
              <Music />
            </span>
          </h1>
          <div className="about-section__description">
            <p>
              <strong>Systrum is an innovative platform that empowers users to instantly generate curated playlists from nothing more than a single phrase.</strong> Simply type in a sentence, a few descriptive words, or even an abstract idea, and Systrum will intelligently craft a custom playlist tailored to your input. By combining advanced music analysis with genre and mood modifiers, it ensures each playlist perfectly reflects the tone, atmosphere, and energy you have in mind—whether you're setting the mood for a quiet evening, energizing a workout, or discovering fresh sounds you never knew you'd love.
            </p>
          </div>
        </header>

        {/* Features section */}
        <section className="about-section__features" aria-labelledby="features-title">
          <h2 id="features-title" className="section-title">How It Works</h2>
          <div className="features-grid">
            {features.map((feature, index) => (
              <FeatureCard
                key={index}
                icon={feature.icon}
                title={feature.title}
                description={feature.description}
                delay={index * 0.1}
              />
            ))}
          </div>
        </section>

        {/* Tech stack section */}
        <section className="about-section__tech" aria-labelledby="tech-title">
          <h2 id="tech-title" className="section-title">Built With</h2>
          
          <div className="tech-stack">
            <div className="tech-category">
              <h3 className="tech-category__title">
                <Code className="tech-category__icon" />
                Frontend
              </h3>
              <div className="tech-grid">
                {techStack.frontend.map((tech, index) => (
                  <TechStackCard
                    key={index}
                    name={tech.name}
                    description={tech.description}
                    icon={tech.icon}
                    delay={index * 0.1}
                  />
                ))}
              </div>
            </div>

            <div className="tech-category">
              <h3 className="tech-category__title">
                <Database className="tech-category__icon" />
                Backend
              </h3>
              <div className="tech-grid">
                {techStack.backend.map((tech, index) => (
                  <TechStackCard
                    key={index}
                    name={tech.name}
                    description={tech.description}
                    icon={tech.icon}
                    delay={index * 0.1}
                  />
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Mission section */}
        <section className="about-section__mission">
          <div className="mission-card">
            <div className="mission-card__icon">
              <Heart />
            </div>
            <h3 className="mission-card__title">Our Mission</h3>
          </div>
        </section>
      </div>
    </section>
  );
};

export default AboutSection;
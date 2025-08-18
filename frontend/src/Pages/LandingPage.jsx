// Pages/LandingPage.jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import WelcomeSection from "../components/landing/WelcomeSection/WelcomeSection";
import Button from "../components/common/Button/Button";
import "./Styles/LandingPage.css";

const LandingPage = () => {
  return (
    <div className="landing-page">
      {/* welcome section */}
      <WelcomeSection />
      {/* <button>
          <a href="http://127.0.0.1:5000/authorizeUser">Click</a>
        </button> */}
    </div>
  );
};

export default LandingPage;
// Pages/LandingPage.jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import WelcomeSection from "../components/landing/WelcomeSection/WelcomeSection";
import Button from "../components/common/Button/Button";
import "./Styles/LandingPage.css";

const LandingPage = () => {
  return (
    <div className="landing-page">
      <WelcomeSection />
    </div>
  );
};

export default LandingPage;
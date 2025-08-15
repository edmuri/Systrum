// src/pages/CreatePlaylistPage.jsx
import React from "react";
import CreatePlaylistSection from "../components/create/CreatePlaylistSection/CreatePlaylistSection";
import "./Styles/CreatePlaylistPage.css";

const CreatePlaylistPage = () => {
  return (
    <div className="create-playlist-page">
      <CreatePlaylistSection />
    </div>
  );
};

export default CreatePlaylistPage;
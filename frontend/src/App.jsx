/*
This is going to contain all the different possible pages
    for the project
*/

import LandingPage from "./Pages/LandingPage";
import CreatePlaylistPage from "./Pages/CreatePlaylistPage";
import PlaylistResultPage from "./Pages/PlaylistResultPage";
import AboutPage from "./Pages/AboutPage";

// import PlaylistPage from "./Pages/PlaylistPage";
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route} from "react-router-dom";

function App(){
    return (
        <BrowserRouter>
        <Routes>
            <Route path="/" element = {<LandingPage />} />
            <Route path="/CreatePlaylist" element = {<CreatePlaylistPage/>}/>
            <Route path="/PlaylistResult" element = {<PlaylistResultPage/>}/>
            <Route path="/AboutPage" element = {<AboutPage />} />
        </Routes>
        </BrowserRouter>
    );
}

export default App;
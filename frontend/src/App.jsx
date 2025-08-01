/*
This is going to contain all the different possible pages
    for the project
*/

import LandingPage from "./Pages/LandingPage";
// import PlaylistPage from "./Pages/PlaylistPage";
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route} from "react-router-dom";

function App(){
    return (
        <BrowserRouter>
        <Routes>
            <Route path="/" element = {<LandingPage />} />
        </Routes>
        </BrowserRouter>
    );
}

export default App;
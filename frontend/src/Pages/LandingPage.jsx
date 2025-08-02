import React, {useState} from "react";
import ReactDOM from "react-dom/client";
import { useNavigate } from "react-router-dom";
import "./Styles/LandingPage.css";

const LandingPage = () => {

    let navigate = useNavigate();

    const handleToPlaylist = ()=>{
        let path = "/CreatePlaylist";
        navigate(path);
    };

    const handleToAbout = ()=>{
        let path = "/About";
        navigate(path);
    };

    const handleToCreators = ()=>{
        let path = "/Creators";
        navigate(path);
    };

    return(
        <div className = "landingPage">
            <div className = "upperSection">
                <h3 id="Text">HELLO</h3>
            </div>
            <div className = "middleSection">
                <h2>WHAT</h2>
                <button onClick={handleToPlaylist}>createPlaylist</button>
                <button onClick={handleToAbout}>About</button>
                <button onClick={handleToCreators}>Creators</button>
            </div>
        </div>
    )
}

export default LandingPage
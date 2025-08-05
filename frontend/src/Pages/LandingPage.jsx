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
            <div className = "buttonSection">
                <button 
                    onClick={handleToPlaylist}
                    className="button">createPlaylist</button>
                <button onClick={handleToAbout}
                    className="button">About</button>
                <button onClick={handleToCreators}
                    className="button">Creators</button>
            </div>
        </div>
    )
}

export default LandingPage
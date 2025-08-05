import React, {useState} from "react";
import ReactDOM from "react-dom/client";
import {useNavigate} from "react-router-dom";
import "./Styles/CreatePlaylistPage.css";

const CreatePlaylistPage = () =>{

    const [sentence, setSentence]=useState('');

    let navigate = useNavigate();

    const handleCreatePlaylist = () => {
        let path = "/WaitingPage";

        navigate(path);
    };

    return (
        <div className = "Page">
            <div className = "UpperSection"></div>
            <div className = "textSection">
                <input 
                    className="inputBox"
                    type="text"
                    value={sentence}
                    onChange={(e)=> setSentence(e.target.value)}
                    />
                <button 
                    onClick={handleCreatePlaylist} 
                    className="createButton">Create</button>
            </div>
        </div>
    )
}

export default CreatePlaylistPage
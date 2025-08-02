import React, {useState} from "react";
import ReactDOM from "react-dom/client";
import {useNavigate} from "react-router-dom";

const CreatePlaylistPage = () =>{

    const [sentence, setSentence]=useState('');

    let navigate = useNavigate();

    const handleCreatePlaylist = () => {
        let path = "/WaitingPage";

        navigate(path);
    };

    return (
        <div>
            <div className = "UpperSection"></div>
            <div className = "textSection">
                <input 
                    type="text"
                    value={sentence}
                    onChange={(e)=> setSentence(e.target.value)}
                    />
                <button onClick={handleCreatePlaylist}>Create</button>
            </div>
        </div>
    )
}

export default CreatePlaylistPage
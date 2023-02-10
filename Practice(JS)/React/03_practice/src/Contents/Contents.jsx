import React from "react";
import './Contents.css';
import '../Blank/Blank'
import Blank from "../Blank/Blank";
import Buttons from "../Buttons/Buttons";
function Contents(props){
    return(
        <div className="Contents">
            <Blank></Blank>
            <Buttons></Buttons>
        </div>
    );
}

export default Contents;
import React from "react";
import './style.css';

function getBtn(){
    return(
        
    );
}

function Button(props){
    return(
        <div className="btn"><div className="aBox"><a onClick={getBtn()}>{props.name}</a></div></div>
    );
}

export default Button;
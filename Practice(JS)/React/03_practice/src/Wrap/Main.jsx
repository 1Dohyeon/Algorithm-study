import React from "react";
import './Main.css';
import Header from "../Header/Header";
import Contents from "../Contents/Contents";

function Main(props){
    return(
        <div className="wrapper">
            <Header></Header>
            <Contents></Contents>
        </div>
    );
}

export default Main;
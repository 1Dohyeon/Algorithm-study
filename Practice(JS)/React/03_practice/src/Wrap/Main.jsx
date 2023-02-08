import React from "react";
import Field from "../Field/Field";
import Logo from "../Logo/Logo";
import './Main.css';

function Main(props){
    return(
        <div className="wrapper">
            <div className="layout">
                <div className="Nav">
                    <Logo></Logo>
                </div>
                <div className="FieldContainer">
                    <Field></Field>
                    <Field></Field>
                    <Field></Field>
                </div>
            </div>
        </div>
    );
}

export default Main;
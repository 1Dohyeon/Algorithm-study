import React from "react";
import Button from "./Button";

const ButtonTexts=[
    {
        name:"About Me",
    },
    {
        name:"Studying",
    },
    {
        name:"Projects",
    },
];

function Buttons(props){
    return(
        <div className="btnBox">
            {ButtonTexts.map((btns)=>{
                    return(
                        <Button name={btns.name}/>
                    )
                })}
        </div>
    );
}

export default Buttons;


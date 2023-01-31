import React from "react";
import Menu from "./Menu";

const menuOptions=[
    {
        option:"menu1",
    },
    {
        option:"menu2",
    },
    {
        option:"menu3",
    },
    {
        option:"menu4",
    },
];

const styles={
    wrapper:{
        display:"flex",
        width:"790px",
    },
};

function MenuList(props){
    return(
        <div style={styles.wrapper}>
            {menuOptions.map((options)=>{
                return(
                    <Menu option={options.option}/>
                );
            })}
        </div>
    );
}

export default MenuList;
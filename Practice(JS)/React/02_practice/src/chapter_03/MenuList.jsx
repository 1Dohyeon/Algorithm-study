import React from "react";
import Menu from "./Menu";

const menuOptions=[
    {
        option:"메뉴1",
    },
    {
        option:"메뉴2",
    },
    {
        option:"메뉴3",
    },
    {
        option:"메뉴4",
    },
];

const styles={
    wrapper:{
        display:"flex",
        width:"800px",
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
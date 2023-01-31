import React from "react";
import Logo from "./Logo";
import MenuList from "./MenuList";

const styles={
    nav:{
        display:"flex",
        justifyContent:"space-between",
        width:"100%",
        height:"70px",
        borderBottom:"1px solid grey",
    }
};

function Header(props){
    return(
        <div style={styles.nav}>
            <Logo/>
            <MenuList/>
        </div>
    );
}

export default Header;
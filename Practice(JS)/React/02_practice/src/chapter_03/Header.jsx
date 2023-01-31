import React from "react";
import Logo from "./Logo";
import MenuList from "./MenuList";

const styles={
    nav:{
        display:"flex",
        justifyContent:"space-between",
        width:"100%",
        height:"70px",
        boxShadow:"0px 3px 5px -3px gray",
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
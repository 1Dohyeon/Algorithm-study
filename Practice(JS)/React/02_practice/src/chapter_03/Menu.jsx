import React from "react";

const styles={
    a:{
        textDecorationLine:"none",
        color:"black",
    },
    wrapper:{
        width:"140px",
        height:"70px",
        border:"none",
        backgroundColor:"white",
    },
    optionName:{
        textAlign:"center",
        fontSize:"16px",
    }
};

function Menu(props){
    return(
        <button style={styles.wrapper}>
            <h1 style={styles.optionName}><a style={styles.a} href="http://localhost:3000/">{props.option}</a></h1>
        </button>
    );
}

export default Menu;
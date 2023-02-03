import React from "react";

const styles={
    wrap:{
        textAlign:"center",
        backgroundColor:"rgba(30,30,30,0.8)",
        width:"240px",
        height:"60px",
        marginTop:"30px",
        marginLeft:"60px",
        position:"absolute",
        borderRadius:"10px",
        textAlign:"center",
    },
    title:{
        color:"white",
        marginTop:"8px",
    },
};

function Header(props){
    return(
        <div style={styles.wrap}>
            <h1 style={styles.title}>조수차 시간</h1>
        </div>
    );
}

export default Header;

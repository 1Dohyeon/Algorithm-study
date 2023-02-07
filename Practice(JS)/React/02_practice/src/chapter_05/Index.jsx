import React from "react";
import Header from "./Header";
import Main from "./Main";
import Result from "./Result";

const styles={
    body:{
        width:"100%",
        margin:"25px 25px",
    },
    bgImg:{
        height:"740px",
        width:"360px",
        backgroundImage:"url(../images/sea_sunset_horizon_131804_480x800.jpg)",
    },
    bg:{
        height:"740px",
        width:"360px",
        backgroundColor:"rgba(30,30,30,0.8)",
    }
};

function Index(props){
    return(
        <body style={styles.body}>
            <div style={styles.bgImg}>
                <div style={styles.bg}>
                    <Header></Header>
                    <Main></Main>
                    <Result></Result>
                </div>
            </div>
        </body>
    );
}

export default Index;
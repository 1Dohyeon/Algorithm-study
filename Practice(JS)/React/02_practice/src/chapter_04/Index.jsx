import React from "react";
import Header from "./Header";
import CityList from "./CityList";

const styles={
    wrap:{
        width:"100%",
        height:"100%",
    },
};

function Index(props){
    return(
        <div style={styles.wrap}>
            <Header/>
            <CityList/>
        </div>
    );
}

export default Index;
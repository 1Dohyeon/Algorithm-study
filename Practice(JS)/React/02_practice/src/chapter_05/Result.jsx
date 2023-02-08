import React from 'react';
import Main from '../chapter_05/Main';

const styles={
    importmation:{
        position: "absolute",
        width: "300px",
        height: "350px",
        marginTop: "310px",
        marginLeft: "30px",
        backgroundColor: "rgba(30,30,30,0.8)",
    },
    cityBox:{
        width: "100%",
        height: "60px",
        textAlign: "center",
    },
    cityBoxH1:{
        fontSize: "24px",
        marginTop: "10px",
    },
    tBox:{
        textAlign: "center",
        marginTop: "40px",
        width: "100%",
        height: "250px",
        justifyContent: "space-between",
    },
    tBoxH3:{
        padding: "10px 0px",
    },
};

function Result(props){
    return(
        <div class="importmation" style={styles.importmation}>
            <div class="city_box" style={styles.cityBox}>
                <h1 id="city" style={styles.cityBoxH1}></h1>
            </div>
            <div class="t_box" style={styles.tBox}>
                <h3 id="t1" style={styles.tBoxH3}></h3>
                <h3 id="t2" style={styles.tBoxH3}></h3>
                <h3 id="t3" style={styles.tBoxH3}></h3>
                <h3 id="t4" style={styles.tBoxH3}></h3>
            </div>
        </div>
    );
}

export default Result;
import React from 'react';

const styles={
    sys:{
        display:"flex",
        position:"absolute",
        width:"300px",
        height:"60px",
        backgroundColor:"rgba(30,30,30,0.6)",
        marginLeft:"30px",
        justifyContent:"space-between",
        marginTop:"120px"
    },
    select:{
        padding:"0px 35px",
    },
    date:{
        padding:"0px 35px",
    },
    place:{
        backgroundColor:"transparent",
        color:"#fff",
        width:"70px",
        height:"33px",
        marginTop:"13px",
        border:"none",
    },
    placeOption:{
        color:"#000",
    },
    startDate:{
        backgroundColor:"transparent",
        color:"#fff",
        width:"100px",
        height:"30px",
        marginTop:"13px",
        border:"none",
    },
    btn:{
        position: "absolute",
        width: "300px",
        height: "60px",
        marginTop: "210px",
        backgroundColor: "rgba(30,30,30,0.6)",
        alignItems: "center",
        marginLeft: "30px",
    },
    input_btn:{
        backgroundColor: "transparent",
        color: "#fff",
        width: "100%",
        height: "100%",
        textAlign: "center",
    },
};

function Main(props){

    return(
        <div>
            <div style={styles.sys}>
                <div style={styles.select}>
                    <select style={styles.place}>
                        <option value="" style={styles.placeOption} selected disabled>위치 선택</option>
                        <option value="DT_0001" style={styles.placeOption}>인천</option>
                        <option value="DT_0008" style={styles.placeOption}>안산</option>
                        <option value="DT_0007" style={styles.placeOption}>목포</option>
                    </select>
                </div>
                <div style={styles.date}>
                    <input type="date" id="start-date" name="start-date" style={styles.startDate}></input>
                </div>
            </div>
            <div style={styles.btn}>
                <input style={styles.input_btn} type="submit" value="확인"></input>
            </div>
        </div>
        
    );
}

export default Main;
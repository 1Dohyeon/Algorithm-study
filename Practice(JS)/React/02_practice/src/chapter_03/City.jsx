import React from "react";

const styles={
    wrapper:{
        boxShadow:"0px 0px 10px gray",
        width: '180px',
        height: '250px',
        margin:'60px',
        marginTop:'15px',
        borderRadius:25,
    },
    imageContainer:{
        width:'100%',
        height:'130px',
    },
    image:{
        width:'100%',
        height:'130px',
        borderRadius:"22.5px 22.5px 0px 0px",
    },
    textContainer:{
        width:'180px',
        height:'130px',
    },
    nameText:{
        textAlign:"center",
        color:"black",
        fontSize:20,
        fontweight:"bold",
    },
    commentText:{
        textAlign:"center",
        color:"black",
        fontSize:16,
        padding:"0px 8px",
    },

};

function City(props){
    return(
        <div style={styles.wrapper}>
            <div style={styles.imageContainer}>
                <img                
                    src={props.imgUrl}
                    style={styles.image}
                />
            </div>
            <div style={styles.textContainer}>
                <h1 style={styles.nameText}>{props.name}</h1>
                <h2 style={styles.commentText}>{props.comment}</h2>
            </div>
        </div>
    );
}

export default City;
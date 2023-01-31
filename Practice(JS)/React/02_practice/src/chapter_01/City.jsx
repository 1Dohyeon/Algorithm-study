import React from "react";

const styles={
    wrapper:{
        margin:"8px",
        border:"1px solid grey",
        width: '180px',
        height: '250px',
        borderRadius:25,
    },
    imageContainer:{
        width:'100%',
        height:'120px',
    },
    image:{
        width:'100%',
        height:'120px',
        borderRadius:"20px 20px 0px 0px",
    },
    textContainer:{
        width:'180px',
        height:'130px',
    },
    nameText:{
        textAlign:"center",
        color:"black",
        fontSize:18,
        fontweight:"bold",
    },
    commentText:{
        textAlign:"center",
        color:"black",
        fontSize:16,
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
                <p style={styles.commentText}>{props.comment}</p>
            </div>
        </div>
    );
}

export default City;
import React from "react";
import City from "./City";

const cityTexts=[
    {
        name:"Seoul",
        comment:"Korea's capital",
        imgUrl:"https://images.wallpaperscraft.com/image/single/korea_asia_seoul_south_korea_night_city_lights_city_28486_320x240.jpg",
    },
    {
        name:"Busan",
        comment:"Korea's second capital",
        imgUrl:"https://images.wallpaperscraft.com/image/single/south_korea_busan_top_view_night_bridge_hdr_54951_320x240.jpg"
    },
    {
        name:"Jeju",
        comment:"Korea's island that has great nature",
        imgUrl:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSU9job166UVhZKEuyvBzPz3TZ84Iw_FGTh_lWk2ygRWg&s"
    },
    {
        name:"Tokyo",
        comment:"Japan's capital",
        imgUrl:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8xYi6h5_rzdDut8Q9IZsoc3hQFOi2n5efCQ&usqp=CAU"
    },
    {
        name:"Sapporo",
        comment:"The best hot spring in Sapporo",
        imgUrl:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDxlTtPRC63hY6tYEEMBvOLyChcuCAo7Z2yg&usqp=CAU"
    },
];

const styles={
    cityContainer:{
        display:"flex",
        justifyContent:"center",
        marginTop:"10px"
    },
    title:{
        width:"100%",
        height:"40px",
        marginLeft:"255px",
        marginTop:"100px",
        color:"rgb(30,30,30)",
        fontSize:"30px",
        fontWeight:600,
    }
};

function CityList(props){
    return(
        <div wrap>
            <div style={styles.title}><a>인기 여행지</a></div>
            <div style={styles.cityContainer}>
                {cityTexts.map((cities)=>{
                    return(
                        <City name={cities.name} comment={cities.comment} imgUrl={cities.imgUrl}/>
                    )
                })}
            </div>
        </div>
    );
}

export default CityList;
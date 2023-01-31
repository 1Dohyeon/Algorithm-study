import React from "react";
import City from "./City";

const cityTexts=[
    {
        id:1,
        name:"Seoul",
        comment:"대한민국의 수도",
        imgUrl:"https://images.wallpaperscraft.com/image/single/korea_asia_seoul_south_korea_night_city_lights_city_28486_320x240.jpg",
    },
    {
        id:2,
        name:"Busan",
        comment:"대한민국 제2의 수도",
        imgUrl:"https://images.wallpaperscraft.com/image/single/south_korea_busan_top_view_night_bridge_hdr_54951_320x240.jpg"
    },
];

const styles={
    layout:{
        display:"flex",
    },
};

function CityList(props){
    return(
        <div style={styles.layout}>
            {cityTexts.map((cities)=>{
                return(
                    <City name={cities.name} comment={cities.comment} imgUrl={cities.imgUrl}/>
                )
            })}
        </div>
    );
}

export default CityList;
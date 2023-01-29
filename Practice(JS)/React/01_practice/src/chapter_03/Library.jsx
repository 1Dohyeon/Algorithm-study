import React from "react";
import Book from "./Book";  // Book.jsx를 불러옴

function Library(props){
    return (
        <div>
            <Book name='처음 만난 파이썬' numOfPage={300}/>
            <Book name='처음 만난 AWS' numOfPage={400}/>
            <Book name='처음 만난 리액트' numOfPage={500}/>
        </div>
    );
}

export default Library; // Library라는 이름으로써 밖으로 수출, index.js에서 확인
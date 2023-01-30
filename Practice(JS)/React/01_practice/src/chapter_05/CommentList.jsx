import React from "react";
import Comment from "./Comment";

const comments=[
    {
        name:"Dohyeon",
        comment:"first comment",
    },
    {
        name:"유재석",
        comment:"second comment",
    },
    {
        name:"장준하",
        comment:"third comment",
    },
    {
        name:"강민경",
        comment:"last comment",
    },
];

function CommentList(props){
    return(
        <div>
            {comments.map((userComment)=>{
                return(
                    <Comment name={userComment.name} comment={userComment.comment}/>
                );
            })}
        </div>
    );
}

export default CommentList;
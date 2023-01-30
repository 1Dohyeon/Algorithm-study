import React from "react";
import Notification from "./Notification";

const reservedNotifications=[
    {   
        id:1,
        message:"안녕하세요, 오늘의 일정을 알려드립니다.",
    },
    {
        id:2,
        message:"점심식사 시간입니다.",
    },
    {
        id:3,
        message:"이제 곧 미팅이 시작됩니다.",
    },
]

var timer;

class NotificationList extends React.Component{
    constructor(props){
        super(props);
        this.state={
            notifications:[],   // 생성자에서 notification이라는 빈 배열을 state에 담음, 
                                // 이처럼 생성자에서는 앞으로 사용할 state에 넣어서 초기화
        }
    }

    componentDidMount(){    // class의 생명주기 중 하나 
        const {notifications}=this.state;
        timer=setInterval(()=>{ // js의 setInterval 함수를 사용하여 매 1000ms마다 주어진 작업을 수
            if (notifications.length<reservedNotifications.length){ // 이 작업은 미리 만들어둔 알림 데이터 배열인
                const index=notifications.length;   // reservedNotifications로부터 알림 데이터를 하나씩 가져와서
                notifications.push(reservedNotifications[index]);   // state에 있는 notifications 배열에 놓고
                this.setState({     // 업데이트 하는 것, 업데이트를 하기위해 setState 함수 사용 
                    notifications: notifications,
                });
            }else{
                this.state={
                    notifications:[],   // notification 배열 비우기
                }
                clearInterval(timer);
            }
        },1000);
    }

    render(){
        return(
            <div>
                {this.state.notifications.map((notification_value)=>{
                    return (
                        <Notification 
                        key={notification_value.id}   // key는 react element를 구분하기 위한 고유의 값. map함수 이용시 필수적으로 이용해야함.
                        id={notification_value.id}
                        message={notification_value.message}
                        />
                    );
                })}
            </div>
        );
    }
}

export default NotificationList;
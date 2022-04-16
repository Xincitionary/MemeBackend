import React from "react";
import "./Feeditem.css";
import comment from "./../../../images/comment.png";
import share from "./../../../images/share.png";
import heart from "./../../../images/heart.png";
import anymHead from "./../../../images/anymHead.png";

const Feeditem = (props) => {
  return (
    <li>
      <div className="row">
        <div>
          <img src={anymHead} className="profile-pic"></img>
        </div>

        <div className="feed-item">
          <div>
            <span className="username">@匿名</span>
            <span className="time">· 2分钟前</span>
          </div>

          <span className="feed-content"> {props.items.content}</span>
        </div>
      </div>

      <div className="reactions">
        <img src={comment} />
        <img src={share} />
        <img src={heart} />
      </div>
    </li>
  );
};

export default Feeditem;

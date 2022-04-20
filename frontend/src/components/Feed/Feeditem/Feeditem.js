import React from "react";
import "./Feeditem.css";
import comment from "./../../../images/comment.png";
import share from "./../../../images/share.png";
import heart from "./../../../images/heart.png";
import anymHead from "./../../../images/anymHead.png";

const Feeditem = (props) => {
  return (
    <li className="list">
      <div className="row">
        <div className="feed-item">
          <div>
            <img src={anymHead} className="profile-pic"></img>
            <span className="username">@匿名</span>
            <span className="time">· 2分钟前</span>
          </div>

          <div className="feed-content"> {props.items.content}</div>
          <div className="reactions">
            <span className="emoji_nums">
              <img src={comment} /> {props.items.num_comments}
            </span>
            <span className="emoji_nums">
              <img src={share} /> 0
            </span>
            <span className="emoji_nums">
              <img src={heart} /> 0
            </span>
          </div>
        </div>
      </div>
    </li>
  );
};

export default Feeditem;

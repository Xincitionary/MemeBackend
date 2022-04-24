import React, { useState, useContext } from "react";
import AuthContext from "../../../context/AuthContext";
import "./Storyitem.css";
import comment from "./../../../images/comment.png";
import share from "./../../../images/share.png";
import heart from "./../../../images/heart.png";
import anymHead from "./../../../images/anymHead.png";

const Storyitem = (props) => {
  const getDate = () => {
    let temp = props.items.DateHappened.substring(0, 7);
    temp = temp.split("-");
    let ret = temp[0] + "年" + temp[1] + "月";
    return ret;
  };

  const getTimeBefore = () => {
    let currentTime = Date.parse(String(new Date()));
    let publishTime = Date.parse(props.items.create_time);
    let t = currentTime - publishTime;
    let cd = 24 * 60 * 60 * 1000,
      ch = 60 * 60 * 1000,
      d = Math.floor(t / cd),
      h = Math.floor((t - d * cd) / ch),
      m = Math.round((t - d * cd - h * ch) / 60000);

    if (m === 60) {
      h++;
      m = 0;
    }
    if (h === 24) {
      d++;
      h = 0;
    }
    let ret = "";
    if (d > 0) {
      ret = String(d) + "天";
    }
    ret = ret + h + "小时" + m + "分钟前";
    return ret;
  };

  return (
    <li className="list">
      <div className="row">
        <div className="story-item">
          <div>
            <img src={anymHead} className="profile-pic" alt="profile"></img>
            <span className="username">
              {props.items.anonymous == 0 ? props.items.username : "匿名"}
            </span>
            <span className="time"> {getTimeBefore()}</span>
          </div>

          <div className="story-content">
            <div className="story-header">
              {props.items.location}-{props.items.Exist}-{getDate()}
            </div>
            {props.items.content}
            <span className="hashtag"> #纽约市的某地有关于我的记忆"</span>
          </div>

          <div className="reactions">
            {/* <span className="emoji_nums">
              <img src={comment} />
              {props.items.num_comments}
            </span>
            <span className="emoji_nums">
              <img src={share} alt="share" /> 0
            </span> */}
            <span className="emoji_nums">
              <img src={heart} alt="heart" /> {props.items.num_likes}
            </span>
          </div>
        </div>
      </div>
    </li>
  );
};

export default Storyitem;

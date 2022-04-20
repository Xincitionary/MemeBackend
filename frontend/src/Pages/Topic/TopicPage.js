import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../../context/AuthContext";
import Feedlist from "../../components/Feed/Feedlist/Feedlist";
import NavbarComp from "../../components/Header/NavbarComp";
import "./TopicPage.css";

const TopicPage = () => {
  //   let [userInfo, setUserInfo] = useState([]);
  let [topicFeeds, setTopicFeeds] = useState([]);
  let [topicInfo, setTopicInfo] = useState([]);
  let { user, authTokens, logoutUser } = useContext(AuthContext);

  useEffect(() => {
    getTopicFeeds();
    getTopicInfo();
  }, []);

  let getTopicFeeds = async () => {
    let url = "http://127.0.0.1:8000/FeedListByTopic/?topicID=1";
    let response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setTopicFeeds(data.results);
    } else if (response.statusText === "Unauthorized") {
      alert("user is unauthorized; can't load feeds");
    }
  };

  let getTopicInfo = async () => {
    let url = "http://127.0.0.1:8000/Topics/2/";
    let response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setTopicInfo(data);
    } else if (response.statusText === "Unauthorized") {
      alert("cannot load topic info");
    }
  };

  return (
    <div>
      <NavbarComp />
      <section className="main-page">
        <div className="left">
          <div className="topicContainer">
            <div className="topicName">{topicInfo.topicName}</div>

            <div className="topicDescription">{topicInfo.abstract}</div>
            <div className="topicDescription">By：词堂爸爸</div>
            <span className="topicDescription">
              创建时间： {topicInfo.create_time}
            </span>
            <div className="topicDescription">
              已有{topicInfo.num_feeds}条，{topicInfo.num_followers}
              个成员在纽约的地铁上
            </div>

            <div className="buttons">
              <button
                type="button"
                className="btn btn-outline-dark buttonWidth"
              >
                加入
              </button>
              <button type="button" className="btn btn-dark buttonWidth">
                发布
              </button>
            </div>
          </div>
        </div>
        <div className="right">
          <section id="topic-feeds">
            <Feedlist items={topicFeeds} />
          </section>
        </div>
      </section>
    </div>
  );
};

export default TopicPage;

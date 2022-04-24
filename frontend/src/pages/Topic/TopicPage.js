import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../../context/AuthContext";
import Storylist from "../../components/Story/Storylist/Storylist";
import NavbarComp from "../../components/Header/NavbarComp";
import PopupPost from "../../components/Popup/PopupPost";

import "./TopicPage.css";

const TopicPage = () => {
  //   let [userInfo, setUserInfo] = useState([]);

  let [topicInfo, setTopicInfo] = useState([]);
  let {
    authTokens,
    getTopicStorys,
    topicStorys,
    currentTopicId,
    user,
  } = useContext(AuthContext);
  const [postModalOpen, setPostModalOpen] = useState(false);

  useEffect(() => {
    // document.body.style.overflow = "hidden";
    getTopicStorys();
    getTopicInfo();
  }, []);

  let getTopicInfo = async () => {
    let url = "http://127.0.0.1:8000/Topics/" + String(currentTopicId) + "/";
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
      {postModalOpen && <PopupPost setOpenModal={setPostModalOpen} />}
      <NavbarComp />
      <section className="main-page">
        <div className="left">
          <div className="topicContainer">
            <div className="topicName">{topicInfo.topicName}</div>

            <div className="topicAbstract">{topicInfo.abstract}</div>
            <div className="topicOther">By MeMe团队</div>
            <span className="topicOther">
              创建时间： {topicInfo.create_time}
            </span>
            <div className="topicOther">
              已有{topicInfo.num_storys}条，{topicInfo.num_followers}
              个成员在纽约的地铁上
            </div>

            <div className="buttons">
              <button
                type="button"
                className="btn btn-dark buttonWidth"
                onClick={() => {
                  setPostModalOpen(true);
                }}
              >
                发布
              </button>
            </div>
          </div>
        </div>

        <div className="right">
          <section id="topic-storys">
            <Storylist items={topicStorys} />
          </section>
        </div>
      </section>
    </div>
  );
};

export default TopicPage;

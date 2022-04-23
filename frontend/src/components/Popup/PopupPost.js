import React, { useContext } from "react";
import AuthContext from "../../context/AuthContext";
import "./PopupPost.css";

function PopupPost({ setOpenModal }) {
  let { postFeed, getTopicFeeds } = useContext(AuthContext);

  let handleOnSubmit = (event) => {
    event.preventDefault();
    postFeed(event);
    setOpenModal(false);
    getTopicFeeds();
  };

  return (
    <div className="modalBackground">
      <div className="modalContainer">
        <div className="titleCloseBtn">
          <button
            onClick={() => {
              setOpenModal(false);
            }}
          >
            X
          </button>
        </div>
        <form onSubmit={handleOnSubmit}>
          <div class="form-group form-row">
            <input
              className="form-control margin-right"
              id="title"
              placeholder="标题 (optional)"
            />

            <input
              className="form-control"
              id="location"
              placeholder="输入地址"
            />
          </div>

          <div className="form-group">
            <textarea
              className="form-control textarea"
              id="feedContent"
              rows="4"
              placeholder="发布你的动态～ #纽约的地铁轶事 "
            ></textarea>
          </div>

          <div className="footer">
            <div className="form-check">
              <input
                className="form-check-input"
                type="checkbox"
                id="anonymous"
              />
              <label className="form-check-label" for="gridCheck">
                匿名
              </label>
            </div>
            <button type="submit" className="btn btn-secondary">
              发布
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default PopupPost;

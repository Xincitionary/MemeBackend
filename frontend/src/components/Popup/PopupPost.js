import React, { useContext } from "react";
import AuthContext from "../../context/AuthContext";
import "./PopupPost.css";

function PopupPost({ setOpenModal }) {
  let { postStory, getTopicStorys } = useContext(AuthContext);

  let handleOnSubmit = (event) => {
    event.preventDefault();
    postStory(event);
    setOpenModal(false);
    getTopicStorys();
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
              id="location"
              placeholder="发生地点"
            />

            <input
              className="form-control"
              id="DateHappened"
              placeholder="发生时间 (yyyy-mm-dd)"
            />
          </div>
          <div class="form-group form-row">
            <select
              class="form-select form-select"
              aria-label=".form-select-sm example"
              id="EXIST"
            >
              <option selected value="EXIST">
                EXIST
              </option>
              <option value="EXISTED">EXISTED</option>
            </select>
          </div>
          <div className="form-group">
            <textarea
              className="form-control textarea"
              id="storyContent"
              rows="4"
              placeholder="发布你的动态～ (200-1000字）"
              maxlength="1000"
              minlength="200"
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

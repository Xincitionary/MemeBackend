import React, { useContext } from "react";
import AuthContext from "../../context/AuthContext";
import "./PopupPost.css";

function PopupPost({ setOpenModal }) {
  let { postFeed } = useContext(AuthContext);
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
        <form onSubmit={postFeed}>
          <div className="form-group">
            <textarea
              className="form-control"
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

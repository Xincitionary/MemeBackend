import React from "react";

import "./PopupPost.css";

function PopupPost({ setOpenModal }) {
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
        敬请期待
      </div>
    </div>
  );
}

export default PopupPost;

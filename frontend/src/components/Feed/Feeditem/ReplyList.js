import React from "react";

const ReplyList = () => {
  return (
    <div>
      {" "}
      <div
        class="form-group"
        onClick={() => {
          console.log("sick");
        }}
      >
        <input
          type="text"
          class="form-control"
          id="exampleInputEmail1"
          placeholder="发布你的评论"
        />
      </div>
    </div>
  );
};

export default ReplyList;

import React from "react";
import Storyitem from "../Storyitem/Storyitem";
import "./Storylist.css";

const Storylist = (props) => {
  return (
    <ul className="story-list">
      {props.items.map((story) => (
        <Storyitem key={story.id} id={story.id} items={story} />
      ))}
    </ul>
  );
};

export default Storylist;

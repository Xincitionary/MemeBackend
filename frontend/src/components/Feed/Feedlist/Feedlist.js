import React from "react";
import Feeditem from "../Feeditem/Feeditem";
import "./Feedlist.css";

const Feedlist = (props) => {
  //   let [pageNumber, setPageNumber] = useState(1);
  //   let [recentFeeds, setRecentFeeds] = useState([]);

  return (
    <ul className="feed-list">
      {props.items.map((feed) => (
        <Feeditem key={feed.id} id={feed.id} items={feed} />
      ))}
    </ul>
  );
};

export default Feedlist;

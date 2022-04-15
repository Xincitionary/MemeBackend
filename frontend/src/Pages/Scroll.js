import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";

export const Scroll = () => {
  let [setUserInfo] = useState([]);
  let { authTokens, logoutUser } = useContext(AuthContext);

  useEffect(() => {
    getUserInfo();
  });

  //currently only getting user id 3's info, need to use useContext to get actaully userID, will UPDATE later
  let getUserInfo = async () => {
    let url = "http://127.0.0.1:8000/storys/";
    let response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setUserInfo(data);
    } else if (response.statusText === "Unauthorized") {
      alert("user is unauthorized. ");
    }
  };
};

export default Scroll;

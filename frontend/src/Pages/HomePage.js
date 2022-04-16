import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";
import { Navbar, Nav, NavDropdown, Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import Feedlist from "../components/Feed/Feedlist/Feedlist";
import "./pageCss/HomePage.css";

const HomePage = () => {
  let [userInfo, setUserInfo] = useState([]);
  let [recentFeeds, setRecentFeeds] = useState([]);
  let { user, authTokens, logoutUser } = useContext(AuthContext);

  useEffect(() => {
    // getUserInfo();
    getRecentFeeds();
  }, []);

  //currently only getting user id 3's info, need to use useContext to get actaully userID, will UPDATE later
  let getUserInfo = async () => {
    let url = "http://127.0.0.1:8000/userInfo/" + String(user.user_id) + "/";
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
      logoutUser();
    }
  };

  let getRecentFeeds = async () => {
    let url = "http://127.0.0.1:8000/Feeds/?page=1";
    let response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setRecentFeeds(data.results);
    } else if (response.statusText === "Unauthorized") {
      alert("user is unauthorized; can't load feeds");
    }
  };

  return (
    <div>
      <Navbar expand="lg" bg="none" variant="light">
        <Container>
          <Nav className="ms-auto">
            <Nav.Link href="#">Home</Nav.Link>

            {user ? (
              <Nav.Link onClick={logoutUser}>Logout</Nav.Link>
            ) : (
              <Nav.Link href="#login">Logout</Nav.Link>
            )}
          </Nav>
        </Container>
      </Navbar>

      <section id="recent-feeds">
        <p>Hi {user.username}!, 今天你能来真好！今天发生了什么吗？</p>
        <h3 className="header">最新动态</h3>
        <Feedlist items={recentFeeds} />
      </section>
    </div>
  );
};

export default HomePage;

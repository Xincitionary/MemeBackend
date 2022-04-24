import React, { useContext } from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import AuthContext from "../../context/AuthContext";
import "./Navbar.css";
import profile from "./../../images/profilepics/#8B0000.png";

const NavbarComp = () => {
  let { user, logoutUser } = useContext(AuthContext);
  let state = { date: new Date() };

  return (
    <Navbar
      expand="lg"
      bg="none"
      variant="light"
      sticky="top"
      className="border"
    >
      <Container>
        <Navbar.Brand className="navLogo" href="#">
          MĒMĒ
        </Navbar.Brand>

        <div className="date">
          {`${state.date.getFullYear()}年 ${state.date.getMonth() + 1
            } 月  ${state.date.getDate()} 日`}
        </div>

        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ms-auto">
            <Navbar.Brand href="">
              <img src={profile} alt="React Bootstrap logo" width="30px" />
            </Navbar.Brand>

            {user ? (
              <Nav.Link onClick={logoutUser}>Logout</Nav.Link>
            ) : (
              <Nav.Link href="#login">Logout</Nav.Link>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavbarComp;

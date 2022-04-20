import React, { Component, useContext } from "react";
import { Navbar, Nav, NavDropdown, Container } from "react-bootstrap";
import AuthContext from "../../context/AuthContext";
import "./Navbar.css";

const NavbarComp = () => {
  let { user, logoutUser } = useContext(AuthContext);
  return (
    <Navbar
      expand="lg"
      bg="none"
      variant="light"
      sticky="top"
      className="border"
    >
      <Navbar.Brand className="navLogo">MĒMĒ</Navbar.Brand>
      <Container>
        <Nav className="ms-auto">
          <Nav.Link href="#">Home</Nav.Link>
          <Nav.Link href="topic">Topic</Nav.Link>
          {user ? (
            <Nav.Link onClick={logoutUser}>Logout</Nav.Link>
          ) : (
            <Nav.Link href="#login">Logout</Nav.Link>
          )}
        </Nav>
      </Container>
    </Navbar>
  );
};

export default NavbarComp;

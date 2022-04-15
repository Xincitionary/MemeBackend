import React, { Component, useContext } from "react";
import { Navbar, Nav, NavDropdown, Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const NavbarComp = () => {
  let { user, logoutUser } = useContext(AuthContext);
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home">MeMe</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#link">Login</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavbarComp;

// <div>
//         <Link to="/">Profile</Link>
//         <span> | </span>
//         {user ? (
//           <a onClick={logoutUser}>Logout</a>
//         ) : (
//           <Link to="/login">Login</Link>
//         )}

//         {user && <p>Hello {user.username}</p>}
//       </div>

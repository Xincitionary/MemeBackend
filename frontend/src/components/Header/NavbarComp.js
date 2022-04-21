import React, { useContext } from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
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
      <Container>
        <Navbar.Brand className="navLogo" href="#">
          MĒMĒ
        </Navbar.Brand>

        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ms-auto">
            <Nav.Link href="#">Home</Nav.Link>
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

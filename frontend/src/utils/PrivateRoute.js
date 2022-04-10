import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const PrivateRoute = () => {
  let { user } = useContext(AuthContext);
  // If we have a user go ahead, else redirect to login, return an outlet that will render child elements

  return user ? <Outlet /> : <Navigate to="/login" />;
};
export default PrivateRoute;

import { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
const AuthContext = createContext();

export default AuthContext;

// pass in value we want to be made avialble across applications
export const AuthProvider = ({ children }) => {
  let [user, setUser] = useState(null);
  let [authTokens, setAuthTokens] = useState(null);

  let loginUser = async (e) => {
    e.preventDefault();
    console.log("Form Submitted");

    let response = await fetch("http://127.0.0.1:8000/api/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: e.target.username.value,
        password: e.target.password.value,
      }),
    });
    let data = await response.json();
    //we want to set it in our state (and local storage) to be used for private routes later
    if (response.status == 200) {
      setAuthTokens(data);
      setUser(jwt_decode(data.access));
    } else {
      alert("something went wrong");
    }
  };

  let contextData = {
    user: user,
    loginUser: loginUser,
  };

  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};

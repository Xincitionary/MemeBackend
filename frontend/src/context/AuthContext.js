import { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import { useNavigate } from "react-router-dom";
const AuthContext = createContext();

export default AuthContext;

// pass in value we want to be made avialble across applications
export const AuthProvider = ({ children }) => {
  let [user, setUser] = useState(() =>
    localStorage.getItem("authtokens")
      ? jwt_decode(localStorage.getItem("authtokens"))
      : null
  );
  let [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authtokens")
      ? JSON.parse(localStorage.getItem("authtokens"))
      : null
  );

  let [currentPostId, getCurrentPostId] = useState(1);

  let [loading, setLoading] = useState(true);

  let navigate = useNavigate();

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
    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwt_decode(data.access));
      localStorage.setItem("authtokens", JSON.stringify(data));
      navigate("/");
    } else {
      alert("something went wrong");
    }
  };

  let logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authtokens");
    navigate("/login");
  };

  //When we login we get a access and refresh token, we send the refresh token to the backend to get a new access token
  //called every 9 minutes
  let updateToken = async () => {
    console.log("updateToken called");
    let response = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        refresh: authTokens?.refresh, //incase auth token has not been updated yet
      }),
    });
    let data = await response.json();
    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwt_decode(data.access));
      localStorage.setItem("authtokens", JSON.stringify(data));
    } else {
      logoutUser();
      console.log("refresh token update failed");
    }

    if (loading) {
      setLoading(false);
    }
  };

  let contextData = {
    user: user,
    authTokens: authTokens,
    loginUser: loginUser,
    logoutUser: logoutUser,
    currentPostId: currentPostId,
  };

  useEffect(() => {
    let nineMinutes = 1000 * 60 * 9;

    if (loading) {
      //if page is loaded/refreshed, get a new access token with the refresh token (i.e. access token may have expired, but refresh token has not)
      updateToken();
    }

    let interval = setInterval(() => {
      if (authTokens) {
        updateToken();
      }
    }, nineMinutes);
    return () => clearInterval(interval);
  }, [authTokens, loading]);

  let postFeed = async (e) => {
    e.preventDefault();
    let postUrl = "http://127.0.0.1:8000/feeds/" + String(currentPostId);

    let response = await fetch(postUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        emoji: null,
        content: e.target.feedContent.value,
        visibility: 0,
        anonymous: e.target.anonymous.value,
        view_count: 0,
        num_comments: 0,
      }),
    });
    let data = await response.json();
    console.log(data);
    //we want to set it in our state (and local storage) to be used for private routes later
    if (response.status === 200) {
      alert("post submitted successfully! ");
    } else {
      alert("something went wrong");
    }
  };

  return (
    <AuthContext.Provider value={contextData}>
      {loading ? null : children}
    </AuthContext.Provider>
  );
};

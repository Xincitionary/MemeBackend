import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import HomePage from "./Pages/HomePage";
import LoginPage from "./Pages/LoginPage";
import ErrorPage from "./Pages/ErrorPage";
import PrivateRoute from "./utils/PrivateRoute";
import Profile from "./Pages/Profile";
// import Header from ".components/Header";

//nav content exist for all pages
function App() {
  return (
    <div className="App">
      <Router>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/login">Login</Link>
        </nav>
        <Routes>
          <Route exact path="/" element={<PrivateRoute />}>
            <Route exact path="/" element={<HomePage />} />
          </Route>
          <Route path="/login" element={<LoginPage />} />
          {/* <Route path="*" element={<ErrorPage />} /> */}
        </Routes>
      </Router>
    </div>
  );
}
export default App;

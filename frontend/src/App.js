import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import ErrorPage from "./pages/ErrorPage";
import PrivateRoute from "./utils/PrivateRoute";
import Profile from "./pages/Profile";
import Header from "./components/Header";

//nav content exist for all pages
function App() {
  return (
    <div className="App">
      <Router>
        <AuthProvider>
          {/* <nav>
            <Link to="/">Home</Link>
            <Link to="/login">Login</Link>
          </nav> */}
          <Header />

          <Routes>
            <Route exact path="/" element={<PrivateRoute />}>
              <Route exact path="/" element={<HomePage />} />
            </Route>
            <Route path="/login" element={<LoginPage />} />
            {/* <Route path="*" element={<ErrorPage />} /> */}
          </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}
export default App;

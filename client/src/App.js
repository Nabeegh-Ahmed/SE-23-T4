import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import { useState } from "react";
import Teacher from "./teacher";
import LabInstructor from "./labInstructor";
import { Button } from "react-bootstrap";

function App() {
  const [page, setPage] = useState("teacher");

  const handleTeacherClick = () => {
    setPage("teacher");
  };

  const handleLabInstructorClick = () => {
    setPage("lab-instructor");
  };

  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="/">
            My App
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Button
                  className="nav-link"
                  variant="link"
                  onClick={handleTeacherClick}
                >
                  Teacher
                </Button>
              </li>
              <li className="nav-item">
                <Button
                  className="nav-link"
                  variant="link"
                  onClick={handleLabInstructorClick}
                >
                  Lab Instructor
                </Button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      {page === "teacher" && <Teacher />}
      {page === "lab-instructor" && <LabInstructor />}
    </div>
  );
}

export default App;

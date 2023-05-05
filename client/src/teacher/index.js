import React, { useState } from "react";
import { Container, Form, Button } from "react-bootstrap";
import ExcelUploadButton from "../functionalities/uploadExelFile";
import { uploadTeacherPreferences } from "../Api/teacherRequests";


function Teacher() {
  const [name, setName] = useState("");
  const [number, setNumber] = useState("");
  const [email, setEmail] = useState("");
  const [courses, setCourses] = useState([]);

  const handleCourseChange = (e, index) => {
    const { name, value } = e.target;
    const updatedCourses = [...courses];
    updatedCourses[index] = { ...updatedCourses[index], [name]: value };
    setCourses(updatedCourses);
  };

  const handleAddCourse = () => {
    setCourses([...courses, { courseName: "", nonPreferredSlots: "" }]);
  };

  const handleDeleteCourse = (index) => {
    const updatedCourses = [...courses];
    updatedCourses.splice(index, 1);
    setCourses(updatedCourses);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ name, number, email, courses });
    uploadTeacherPreferences({ name, number, email, courses })
  };

  return (
    <Container>
      <div className="d-flex justify-content-end my-5">
        <Form.Group controlId="fileUpload">
          <ExcelUploadButton type={"Teachers"} />
        </Form.Group>
      </div>
      <h1>Teacher Input Form</h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </Form.Group>

        <Form.Group controlId="number">
          <Form.Label>Number</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter number"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            required
          />
        </Form.Group>

        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </Form.Group>

        <hr />

        <h3>Courses</h3>
        {courses.map((course, index) => (
          <div key={index}>
            <Form.Group controlId={`courseName-${index}`}>
              <Form.Label>Course Name</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter course name"
                name="courseName"
                value={course.courseName}
                onChange={(e) => handleCourseChange(e, index)}
                required
              />
            </Form.Group>

            <Form.Group controlId={`nonPreferredSlots-${index}`}>
              <Form.Label>Non-Preferred Slots</Form.Label>
              <Form.Control
                as="select"
                placeholder="Select non-preferred slots"
                name="nonPreferredSlots"
                value={course.nonPreferredSlots}
                onChange={(e) => handleCourseChange(e, index)}
                required
              >
                <option value="">Select</option>
                <option value="8:30-9:50">8:30 AM - 9:50 AM</option>
                <option value="10:00-11:20">10:00 AM - 11:20 AM</option>
                <option value="11:30-12:50">11:30 AM - 12:50 PM</option>
                <option value="1:00-2:20">1:00 PM - 2:20 PM</option>
                <option value="2:30-3:50">2:30 PM - 3:50 PM</option>
                <option value="4:00-5:20">4:00 PM - 5:20 PM</option>
              </Form.Control>

              <Button
                className="my-2"
                variant="danger"
                onClick={() => handleDeleteCourse(index)}
              >
                Remove
              </Button>
              <hr />
            </Form.Group>
          </div>
        ))}
        <Button variant="secondary" onClick={handleAddCourse}>
          Add Course
        </Button>

        <hr />

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </Container>
  );
}

export default Teacher;

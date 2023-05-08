import React, { useState } from "react";
import { Container, Form, Button } from "react-bootstrap";
import ExcelUploadButton from "../functionalities/uploadExelFile";
import { uploadLabPreferences } from "../Api/labInstructorRequests";

function LabInstructor() {
  const [name, setName] = useState("");
  const [number, setNumber] = useState("");
  const [email, setEmail] = useState("");
  const [labs, setLabs] = useState([
    { labName: "", preferredSlots: "", grade: "", cgpa: "", university: "" },
  ]);

  const handleCourseChange = (e, index) => {
    const { name, value } = e.target;
    const updatedCourses = [...labs];
    updatedCourses[index] = { ...updatedCourses[index], [name]: value };
    setLabs(updatedCourses);
  };

  const handleAddCourse = () => {
    setLabs([
      ...labs,
      { labName: "", preferredSlots: "", grade: "", cgpa: "", university: "" },
    ]);
  };

  const handleDeleteCourse = (index) => {
    const updatedCourses = [...labs];
    updatedCourses.splice(index, 1);
    setLabs(updatedCourses);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ name, number, email, labs });
    uploadLabPreferences({ name, number, email, labs })
  };

  return (
    <Container>
      <div className="d-flex justify-content-end my-5">
        <Form.Group controlId="fileUpload">
          <ExcelUploadButton type={"LabInstructors"}/>
        </Form.Group>
      </div>
      <h1>Lab Instructor Input Form</h1>
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

        <h3>Labs</h3>
        {labs.map((course, index) => (
          <div key={index}>
            <Form.Group controlId={`labName-${index}`}>
              <Form.Label>Name</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter course name"
                name="labName"
                value={course.courseName}
                onChange={(e) => handleCourseChange(e, index)}
                required
              />
            </Form.Group>
            <Form.Group controlId={`grade-${index}`}>
              <Form.Label>Grade</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter grade"
                name="grade"
                value={course.grade}
                onChange={(e) => handleCourseChange(e, index)}
                required
              />
            </Form.Group>

            <Form.Group controlId={`cgpa-${index}`}>
              <Form.Label>CGPA</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter CGPA"
                name="cgpa"
                value={course.cgpa}
                onChange={(e) => handleCourseChange(e, index)}
                required
              />
            </Form.Group>

            <Form.Group controlId={`university-${index}`}>
              <Form.Label>University</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter university name"
                name="university"
                value={course.university}
                onChange={(e) => handleCourseChange(e, index)}
                required
              />
            </Form.Group>

            <Form.Group controlId={`preferredSlots-${index}`}>
              <Form.Label>Preferred Slots</Form.Label>
              <Form.Control
                as="select"
                placeholder="Select preferred slots"
                name="preferredSlots"
                value={course.preferredSlots}
                onChange={(e) => handleCourseChange(e, index)}
                required
              >
                <option value="">Select</option>
                <option value="8:30-11:30">8:30 AM - 11:30 AM</option>
                <option value="11:30-2:30">11:30 AM - 2:30 PM</option>
                <option value="2:30-5:30">2:30 PM - 5:30 PM</option>
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
          Add Lab
        </Button>

        <hr />

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </Container>
  );
}

export default LabInstructor;

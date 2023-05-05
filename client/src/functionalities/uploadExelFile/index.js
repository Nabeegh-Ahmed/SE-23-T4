import React, { useState } from "react";
import { uploadTeacherExcelFile } from "../../Api/teacherRequests";
import { uploadLabExcelFile } from "../../Api/labInstructorRequests";


function ExcelUploadButton({type}) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileInputChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };


  const handleUploadClick = () => {
    { type === "Teachers" && uploadTeacherExcelFile(selectedFile)}
    { type === "LabInstructors" && uploadLabExcelFile(selectedFile)}
  };

  return (
    <div>
      <input type="file" accept=".xlsx" onChange={handleFileInputChange} />
      <button onClick={handleUploadClick}>Upload</button>
    </div>
  );
}
export default ExcelUploadButton;

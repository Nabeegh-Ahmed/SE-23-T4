import React, { useState } from "react";

function ExcelUploadButton() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileInputChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUploadClick = () => {
    // do something with the selected file, such as upload it to a server
    console.log(selectedFile);
  };

  return (
    <div>
      <input type="file" accept=".xlsx" onChange={handleFileInputChange} />
      <button onClick={handleUploadClick}>Upload</button>
    </div>
  );
}
export default ExcelUploadButton;

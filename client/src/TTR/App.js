import React, { useState } from "react";
import "./App.css";

function App() {
  
  const [isExportDisabled, setIsExportDisabled] = useState(true);
  const [isImportDisabled, setIsImportDisabled] = useState(true);

  
  const handleExportClick = () => {
    
  };


  const handleImportClick = () => {

  };

  
  const handleHighlightClick = () => {
 
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Timetable Reader</h1>
      </header>
      <div className="button-container">
        <button
          className="export-button"
          onClick={handleExportClick}
          disabled={isExportDisabled}
        >
          Export Timetable
        </button>
        <button
          className="import-button"
          onClick={handleImportClick}
          disabled={isImportDisabled}
        >
          Import Timetable
        </button>
        <button
          className="highlight-button"
          onClick={handleHighlightClick}
        >
          Highlight Clashes
        </button>
      </div>
    </div>
  );
}

export default App;

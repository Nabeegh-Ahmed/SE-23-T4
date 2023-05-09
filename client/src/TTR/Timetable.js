import React, { useState } from 'react';
import Papa from 'papaparse';
import './Timetable.css';

function Timetable() {
  const [data, setData] = useState([]);

  const handleFileUpload = (file) => {
    Papa.parse(file, {
      header: true,
      complete: (results) => {
        setData(results.data);
      }
    });
  }

  const handleFileDownload = () => {
    const csvData = Papa.unparse(data);
    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'timetable.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  const handleHighlightClashes = () => {
    // Add code to highlight clashes here
  }

  return (
    <div className="Timetable">
      <h1>Timetable</h1>
      <div className="buttons">
        <CSVReader onDrop={(acceptedFiles) => handleFileUpload(acceptedFiles[0])}>
          <span>Drop CSV file here or click to upload.</span>
        </CSVReader>
        <button onClick={handleFileDownload}>Export Timetable</button>
        <button onClick={handleHighlightClashes}>Highlight Clashes</button>
      </div>
      {data.length > 0 &&
        <table>
          <thead>
            <tr>
              {Object.keys(data[0]).map((key) => <th key={key}>{key}</th>)}
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                {Object.values(row).map((value, index) => <td key={index}>{value}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      }
    </div>
  );
}

export default Timetable;

import React, { useState } from 'react';
import axios from 'axios';
const IP_ADDRESS = '127.0.0.1:5000/';

function Import() {
  const [file, setFile] = useState(null);
  const [timetable, setTimetable] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = () => {
    const formData = new FormData();
    formData.append('file', file);
    
    
    axios.post(`http://127.0.0.1:3002/api/import`, formData, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(res => setTimetable(res.data))
      .catch(err => console.log(err));
  };




  const handleFileDownload = () => {
    axios.get('http://127.0.0.1:3002/api/export', {
      responseType: 'blob'
    })
      .then(res => {
        const url = window.URL.createObjectURL(new Blob([res.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'timetable.xlsx');
        document.body.appendChild(link);
        link.click();
      })
      .catch(err => console.log(err));
  };


    const loadTimetable = ()=> {
    axios.get('http://127.0.0.1:3002/api/timetable')
      .then(response => {
        const timetable = response.data;
        const timetableTable = document.getElementById('timetable');
        
        timetableTable.innerHTML = `
          <thead>
            <tr>
              <th>Course Name</th>
              <th>Section</th>
              <th>Venue</th>
              <th>Time</th>
              <th>Day</th>
            </tr>
          </thead>
          <tbody>
            ${timetable.map(row => `
              <tr>
                <td>${row.courseName}</td>
                <td>${row.section}</td>
                <td>${row.venue}</td>
                <td>${row.time}</td>
                <td>${row.day}</td>
              </tr>
            `).join('')}
          </tbody>
        `;
      })
      .catch(error => {
        console.log(error);
      });
  };  






  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleFileUpload}>Import</button>
      {timetable && <button onClick={handleFileDownload}>Export</button>}
      {timetable && <button onClick={loadTimetable}>Dsiplay</button>}
    </div>
  );
}

export default Import;


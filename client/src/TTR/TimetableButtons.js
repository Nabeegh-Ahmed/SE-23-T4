import React, { useState } from 'react';
import * as  XLSX from 'xlsx';
import { Button } from '@material-ui/core';
import { CloudDownload, CloudUpload, Highlight } from '@material-ui/icons';
import moment from 'moment';
import './style.css';


function TimetableButtons({ timetable }) {
  const [clashes, setClashes] = useState([]);

  const handleExport = () => {
    const worksheet = XLSX.utils.json_to_sheet(timetable);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Timetable');
    XLSX.writeFile(workbook, 'timetable.xlsx');
  };

  const handleImport = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = (event) => {
      const data = new Uint8Array(event.target.result);
      const workbook = XLSX.read(data, { type: 'array' });
      const worksheet = workbook.Sheets[workbook.SheetNames[0]];
      const importedTimetable = XLSX.utils.sheet_to_json(worksheet);
      setClashes(getClashes(importedTimetable));
    };
    reader.readAsArrayBuffer(file);
  };

  const handleHighlight = () => {
    setClashes(getClashes(timetable));
  };

  const getClashes = (data) => {
    const clashes = [];
    for (let i = 0; i < data.length; i++) {
      const entryA = data[i];
      const startA = moment(entryA.start, 'HH:mm');
      const endA = moment(entryA.end, 'HH:mm');
      for (let j = i + 1; j < data.length; j++) {
        const entryB = data[j];
        const startB = moment(entryB.start, 'HH:mm');
        const endB = moment(entryB.end, 'HH:mm');
        if (startA.isBefore(endB) && startB.isBefore(endA)) {
          clashes.push([i, j]);
        }
      }
    }
    return clashes;
  };

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        startIcon={<CloudUpload />}
        component="label"
      >
        Import Timetable
        <input type="file" accept=".xlsx" hidden onChange={handleImport} />
      </Button>
      <Button
        variant="contained"
        color="primary"
        startIcon={<CloudDownload />}
        onClick={handleExport}
      >
        Export Timetable
      </Button>
      <Button
        variant="contained"
        color="secondary"
        startIcon={<Highlight />}
        onClick={handleHighlight}
      >
        Highlight Clashes
      </Button>
      {clashes.length > 0 && (
        <div>
          <h3>Clashes:</h3>
          {clashes.map(([index1, index2]) => (
            <p key={`${index1}-${index2}`}>
              {timetable[index1].class} clashes with {timetable[index2].class}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}

export default TimetableButtons;
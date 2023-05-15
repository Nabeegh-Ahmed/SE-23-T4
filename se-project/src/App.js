import React from 'react';
import axios from 'axios';
import { utils, writeFile } from 'xlsx';

class App extends React.Component {
  fetchAndDownload = () => {
    axios.get('http://localhost:5000/data')
      .then(response => {
        const data = response.data;
        let transformedData = [];

        data.forEach((item) => {
          for (let i = 0; i < item.Labname.length; i++) {
            transformedData.push({
              Name: item.Name,
              Number: item.Number,
              Email: item.Email,
              Labname: item.Labname[i],
              PreferredSlots: item.PreferredSlots[i],
              Grade: item.Grade[i],
              CGPA: item.CGPA[i],
              University: item.University[i]
            });
          }
        });

        const ws = utils.json_to_sheet(transformedData);
        const wb = utils.book_new();
        utils.book_append_sheet(wb, ws, "Data");
        writeFile(wb, "data.xlsx");
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <div className="App">
        <button onClick={this.fetchAndDownload}>Download</button>
      </div>
    );
  }
}

export default App;
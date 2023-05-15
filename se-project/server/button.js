const express = require('express');
const app = express();

// Enable CORS (for cross-origin requests)
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

// Handle the GET request for '/data'
app.get('/data', (req, res) => {
  const labInstructorData = [
    {
      "Name": "Abdullah Zeb",
      "Number": "0315-4033656",
      "Email": "zeb.kumi6999@gmail.com",
      "Labname": [
        "Artificial Intelligence Lab"
      ],
      "PreferredSlots": [
        "2:30PM-5:30PM"
      ],
      "Grade": [
        "A-"
      ],
      "CGPA": [
        3.6
      ],
      "University": [
        "NU"
      ]
    },
    {
      "Name": "Muhammad Haris",
      "Number": "0332-1438446",
      "Email": "chharis9999@gmail.com",
      "Labname": [
        "Object Oriented Programming Lab",
        "Programming Fundamentals Lab",
        "Database System Lab"
      ],
      "PreferredSlots": [
        "11:20AM-2:30PM",
        "11:20AM-2:30PM",
        "11:20AM-2:30PM"
      ],
      "Grade": [
        "A",
        "A",
        "A"
      ],
      "CGPA": [
        4,
        4,
        4
      ],
      "University": [
        "NU",
        "NU",
        "NU"
      ]
    },
    {
      "Name" :"Syed Kumail Raza Zaidi",
      "Number": "0333-1472820",
      "Email": "syed.kumizaidi@gmail.com",
      "Labname": [
        "ICT Lab",
        "Digital Logic Design Lab",
      ],
      "PreferredSlots": [
        "11:20AM-2:30PM",
        "11:20AM-2:30PM"
      ],
      "Grade": [
        "A+",
        "A",
      ],
      "CGPA": [
        4,
        4
      ],
      "University": [
        "NU",
        "NU"
      ]
    }
  ];


  // Set the response headers for Excel forma
  // Send the Excel data as response
  res.json(labInstructorData);
});

// Start the server
app.listen(5000, () => {
  console.log('Server is running on port 5000');
});

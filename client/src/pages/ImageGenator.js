import { ConnectWallet, useAddress } from "@thirdweb-dev/react";
import React, { useState } from 'react';
import styled from '@emotion/styled';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button, Input } from '@mui/material';
import Papa from 'papaparse';

const CustomTableCell = styled(TableCell)`
  font-weight: bold;
`;

function ImageGenator() {

  const address = useAddress();

  const [csvData, setCsvData] = useState([]);

  const processCSV = (result) => {
    const data = result.data;
    setCsvData(data);
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    Papa.parse(file, {
      header: true,
      complete: processCSV,
    });
  };

  return (
    <>
      {!address ? (
        <ConnectWallet />
      ) : (
        <div>
          <Input
            type="file"
            accept=".csv"
            onChange={handleFileUpload}
            inputProps={{ 'aria-label': 'Upload CSV file' }}
          />
          {csvData.length > 0 && (
            <TableContainer component={Paper}>
              <Table>
                <TableHead>
                  <TableRow>
                    <CustomTableCell>Day</CustomTableCell>
                    <CustomTableCell>Course</CustomTableCell>
                    <CustomTableCell>Section</CustomTableCell>
                    <CustomTableCell>Instructor</CustomTableCell>
                    <CustomTableCell>Timeslot</CustomTableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {csvData.map((row, index) => (
                    <TableRow key={index}>
                      <TableCell>{row.day}</TableCell>
                      <TableCell>{row.course}</TableCell>
                      <TableCell>{row.section}</TableCell>
                      <TableCell>{row.instructor}</TableCell>
                      <TableCell>{row.timeslot}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          )}
        </div>
      )}
    </>
  );
}
export default ImageGenator;

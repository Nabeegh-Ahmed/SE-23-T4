import { useEffect, useState } from "react";
import "../App.css";
import React from 'react';

import styled from '@emotion/styled'; // Fix the import here
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button, Input } from '@mui/material';
import { ConnectWallet, useAddress } from "@thirdweb-dev/react";

const emails = [
  { id: 1, email: 'john@example.com', status: 'Pending' },
  { id: 2, email: 'jane@example.com', status: 'Pending' },
  { id: 3, email: 'tom@example.com', status: 'Pending' },
  // Add more emails as needed
];


const CustomTableCell = styled(TableCell)`
  font-weight: bold;
`;

const CustomButton = styled(Button)`
  margin: 0 5px;
`;

function SheraAI() {
  const address = useAddress();

  const [emailData, setEmailData] = useState(emails);

  const handleApproval = (id, status) => {
    setEmailData(
      emailData.map((email) =>
        email.id === id ? { ...email, status: status } : email
      )
    );
  };


  const [openMenu, setOpenMenu] = useState(false);
  console.log(openMenu);
  return (
    <>


      {!address ? (
        <ConnectWallet />
      ) : (
        <>
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow>
                  <CustomTableCell>Random Emails</CustomTableCell>
                  <CustomTableCell>Approval Status</CustomTableCell>
                  <CustomTableCell>Actions</CustomTableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {emailData.map((email) => (
                  <TableRow key={email.id}>
                    <TableCell>{email.email}</TableCell>
                    <TableCell>{email.status}</TableCell>
                    <TableCell>
                      <CustomButton
                        variant="contained"
                        color="primary"
                        onClick={() => handleApproval(email.id, 'Approved')}
                      >
                        Approve
                      </CustomButton>
                      <CustomButton
                        variant="contained"
                        color="secondary"
                        onClick={() => handleApproval(email.id, 'Rejected')}
                      >
                        Reject
                      </CustomButton>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </>
      )}
    </>
  );
}

export default SheraAI;

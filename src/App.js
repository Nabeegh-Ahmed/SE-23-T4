import React, { useState, useEffect } from 'react';
import { createUseStyles } from 'react-jss';

const useStyles = createUseStyles({
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    paddingTop: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  clashContainer: {
    border: '1px solid #ccc',
    padding: 10,
    marginBottom: 10,
    width: 400,
  },
  resolvedClashContainer: {
    border: '1px solid #ccc',
    padding: 10,
    marginBottom: 10,
    width: 400,
    backgroundColor: '#eee',
  },
  resolved: {
    color: 'green',
  },
  unresolved: {
    color: 'red',
  },
  button: {
    backgroundColor: '#4CAF50',
    border: 'none',
    color: 'white',
    padding: '10px 20px',
    textAlign: 'center',
    textDecoration: 'none',
    display: 'inline-block',
    fontSize: 16,
    borderRadius: 5,
    cursor: 'pointer',
    marginTop: 10,
  },
});

function Clashes() {
  const [clashes, setClashes] = useState([]);
  const [selectedClash, setSelectedClash] = useState(null);
  const [resolvedClashes, setResolvedClashes] = useState([]);

  useEffect(() => {
    fetch('/members')
      .then((res) => res.json())
      .then((data) => setClashes(data))
      .catch((err) => console.log(err));
  }, []);

  const handleResolveClash = () => {
    // Add selectedClash to resolvedClashes list and remove it from clashes list
    setResolvedClashes([...resolvedClashes, selectedClash]);
    setClashes(clashes.filter((clash) => clash !== selectedClash));
    setSelectedClash(null);
  };

  const handleMarkAsResolved = (clash) => {
    const newClashes = [...clashes];
    const index = newClashes.indexOf(clash);
    newClashes[index].resolution = 'Resolved';
    setClashes(newClashes);
  };

  const classes = useStyles();

  return (
    <div className={classes.container}>
      <h3 className={classes.title}>Clashes:</h3>
      {clashes.length > 0 ? (
        clashes.map((clash) => (
          <div
            key={clash.decription}
            className={classes.clashContainer}
            style={{ backgroundColor: clash === selectedClash ? '#f2f2f2' : '#fff' }}
            onClick={() => setSelectedClash(clash)}
          >
            <p>Type: {clash.type}</p>
            <p>Description: {clash.decription}</p>
            <p>Slots: {clash.slots}</p>
            <p>Course: {clash.course}</p>
            <p>Instructor: {clash.instructor}</p>
            <p>Resolution: {clash.resolve}</p>
            {clash.resolution ? (
              <p className={classes.resolved}>Status: Resolved</p>
            ) : (
              <div>
                <p className={classes.unresolved}>Status: Unresolved</p>
                <button className={classes.button} onClick={() => handleMarkAsResolved(clash)}>
                  Mark as resolved
                </button>
              </div>
            )}
          </div>
        ))
      ) : (
        <p>No unresolved clashes.</p>
            )}
            {resolvedClashes.length > 0 && (
                <div>
                    <h3>Resolved clashes:</h3>
                    {resolvedClashes.map(clash => (
                        <div key={clash.decription}>
                            <p>Type: {clash.type}</p>
                            <p>Description: {clash.decription}</p>
                            <p>Slots: {clash.slots}</p>
                             <p>Course: {clash.course}</p>
                            <p>Instructor: {clash.instructor}</p>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default Clashes;
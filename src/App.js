import React, { useState, useEffect } from 'react';

function Clashes() {
    const [clashes, setClashes] = useState([]);
    const [selectedClash, setSelectedClash] = useState(null);
    const [resolvedClashes, setResolvedClashes] = useState([]);

    useEffect(() => {
        fetch('/members')
            .then(res => res.json())
            .then(data => setClashes(data))
            .catch(err => console.log(err));
    }, []);

    const handleResolveClash = () => {
        // Add selectedClash to resolvedClashes list and remove it from clashes list
        setResolvedClashes([...resolvedClashes, selectedClash]);
        setClashes(clashes.filter(clash => clash !== selectedClash));
        setSelectedClash(null);
    };

    return (
        <div>
            <h2>Clashes</h2>
            <div>
                <label htmlFor="clash-select">Select a clash to resolve:</label>
                <select id="clash-select" value={selectedClash ? selectedClash.decription : ''} onChange={e => setSelectedClash(clashes.find(clash => clash.decription === e.target.value))}>
                    <option value="">-- Select a clash --</option>
                    {clashes.map(clash => (
                        <option key={clash.decription} value={clash.decription}>{clash.decription}</option>
                    ))}
                </select>
                <button disabled={!selectedClash} onClick={handleResolveClash}>Resolve clash</button>
            </div>
            {clashes.length > 0 ? (
                <div>
                    <h3>Unresolved clashes:</h3>
                    {clashes.map(clash => (
                        <div key={clash.decription}>
                            <p>Type: {clash.type}</p>
                            <p>Description: {clash.decription}</p>
                            <p>Slots: {clash.slots}</p>
                            <p>Course: {clash.course}</p>
                            <p>Instructor: {clash.instructor}</p>
                        </div>
                    ))}
                </div>
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

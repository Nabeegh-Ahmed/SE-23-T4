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


            {clashes.length > 0 ? (
                <div>
                    <h3>Clashes:</h3>
                    {clashes.map(clash => (
                        <div key={clash.decription}>
                            <p>------------------------------------------------------------------------------------------------------------</p>
                            <p>Type: {clash.type}</p>
                            <p>Description: {clash.decription}</p>
                            <p>Slots: {clash.slots}</p>
                            <p>Course: {clash.course}</p>
                            <p>Instructor: {clash.instructor}</p>
                            {clash.resolution ? (
                                <p>Resolution: {clash.resolution}</p>
                            ) : (
                                <div>
                                    <p>Status: Unresolved</p>
                                    <button
                                        onClick={() => {
                                            const newClashes = [...clashes];
                                            const index = newClashes.indexOf(clash);
                                            newClashes[index].resolution = 'Resolved';
                                            setClashes(newClashes);
                                        }}
                                    >
                                        Mark as resolved
                                    </button>
                                </div>
                            )}

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
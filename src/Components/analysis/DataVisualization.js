import React, { useState, useEffect } from 'react';
import './Graph_01.css';

const DataVisualization = () => {
    const [graphData, setGraphData] = useState(null);

    useEffect(() => {
        fetch('http://localhost:3000/api/DataVisualization')
            .then(response => response.text())
            .then(data => setGraphData(data))
            .catch(error => console.error('Error:', error));
    }, []);

    if (!graphData) return <div>Loading...</div>;

    return (
        <div className="DataVisualization">
            <iframe className='iframe_of_DataVisualization'
                title="DataVisualization"
                srcDoc={graphData}
                style={{ border: 'none', width: '100%', height: '500px' }}
            />
        </div>
    );
};
export default DataVisualization;
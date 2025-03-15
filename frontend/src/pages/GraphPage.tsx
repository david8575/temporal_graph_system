import React, { useEffect, useState } from 'react';
import { fetchGraphData } from '../api';

const GraphPage: React.FC = () => {
    const [graphData, setGraphData] = useState<any>(null);

    useEffect(() => {
        const loadGraphData = async() => {
            const data = await fetchGraphData();
            setGraphData(data);
            console.log("graph data loaded", data);
        };

        loadGraphData();
    }, []);

    return (
        <div>
            <h1>Graph Data</h1>
            <pre>{JSON.stringify(graphData, null, 2)}</pre>
        </div>
    );
};

export default GraphPage;
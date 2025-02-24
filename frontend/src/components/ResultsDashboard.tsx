import React from 'react';
import { useSelector } from 'react-redux';

const ResultsDashboard: React.FC = () => {
  const results = useSelector((state: any) => state.modelResults);

  return (
    <div>
      <h3>Model Results</h3>
      {results ? (
        <pre>{JSON.stringify(results, null, 2)}</pre>
      ) : (
        <p>No results available. Run the model to see outputs.</p>
      )}
    </div>
  );
};

export default ResultsDashboard;
import React, { useState } from 'react';
import axios from 'axios';
import { useDispatch } from 'react-redux';

const ModelConfigComponent: React.FC = () => {
  const [projectId, setProjectId] = useState<number>(0);
  const [param1, setParam1] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = async () => {
    const config = { project_id: projectId, param1 };
    try {
      const response = await axios.post('/api/model/run', config);
      dispatch({ type: 'SET_MODEL_RESULTS', payload: response.data });
      alert('Model run initiated');
    } catch (error) {
      alert('Failed to run model');
    }
  };

  return (
    <div>
      <h3>Model Configuration</h3>
      <label>
        Project ID:
        <input
          type="number"
          value={projectId}
          onChange={(e) => setProjectId(parseInt(e.target.value, 10))}
        />
      </label>
      <br />
      <label>
        Parameter 1:
        <input type="text" value={param1} onChange={(e) => setParam1(e.target.value)} />
      </label>
      <br />
      <button onClick={handleSubmit}>Run Model</button>
    </div>
  );
};

export default ModelConfigComponent;
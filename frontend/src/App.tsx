import React from 'react';
import MapComponent from './components/MapComponent';
import DataUploadComponent from './components/DataUploadComponent';
import ModelConfigComponent from './components/ModelConfigComponent';
import ResultsDashboard from './components/ResultsDashboard';
import LLMChatComponent from './components/LLMChatComponent';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  height: 100vh;
`;

const Sidebar = styled.div`
  width: 300px;
  overflow-y: auto;
  padding: 10px;
  background-color: #f0f0f0;
`;

const MapArea = styled.div`
  flex: 1;
`;

function App() {
  return (
    <Container>
      <Sidebar>
        <DataUploadComponent />
        <ModelConfigComponent />
        <ResultsDashboard />
        <LLMChatComponent />
      </Sidebar>
      <MapArea>
        <MapComponent />
      </MapArea>
    </Container>
  );
}

export default App;
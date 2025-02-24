import React, { useState } from 'react';
import axios from 'axios';

const DataUploadComponent: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
    try {
      await axios.post('/api/data/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      alert('File uploaded successfully');
    } catch (error) {
      alert('Upload failed');
    }
  };

  return (
    <div>
      <h3>Upload Geospatial Data</h3>
      <input type="file" onChange={handleFileChange} accept=".kml,.kmz,.shp,.geojson" />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default DataUploadComponent;
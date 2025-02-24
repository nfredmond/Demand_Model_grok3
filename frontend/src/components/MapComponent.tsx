import React from 'react';
import { MapContainer, TileLayer, FeatureGroup } from 'react-leaflet';
import { EditControl } from 'react-leaflet-draw';
import 'leaflet/dist/leaflet.css';
import 'leaflet-draw/dist/leaflet.draw.css';
import { useDispatch } from 'react-redux';

const MapComponent: React.FC = () => {
  const dispatch = useDispatch();

  const handleCreated = (e: any) => {
    const layer = e.layer;
    const geoJson = layer.toGeoJSON();
    dispatch({ type: 'SET_PROJECT_AREA', payload: geoJson });
  };

  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '100%', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <FeatureGroup>
        <EditControl
          position="topright"
          onCreated={handleCreated}
          draw={{
            rectangle: true,
            polygon: true,
            circle: false,
            marker: false,
            polyline: false,
          }}
        />
      </FeatureGroup>
    </MapContainer>
  );
};

export default MapComponent;
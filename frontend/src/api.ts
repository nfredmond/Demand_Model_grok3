import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);
  return axios.post(`${API_URL}/data/upload`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const runModel = async (config: any) => {
  return axios.post(`${API_URL}/model/run`, config);
};

export const askLLM = async (query: string) => {
  return axios.post(`${API_URL}/llm/query`, { query });
};
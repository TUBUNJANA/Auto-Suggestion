import axios from "axios";

const API_URL = "http://localhost:8000";

export const getSuggestions = async (query) => {
  const response = await axios.get(`${API_URL}/suggest?query=${query}`);
  return response.data;
};

export const addSentence = async (sentence) => {
  const response = await axios.post(`${API_URL}/add`, { sentence });
  return response.data;
};
import axios from 'axios';
import { Listing } from '../types/Listing';

const API_BASE_URL = 'http://localhost:8080';

export const getListings = () => {
  return axios.get(`${API_BASE_URL}/listings`);
};

export const getPricesHistory = (listingId: string) => {
  return axios.get(`${API_BASE_URL}/listings/${listingId}/prices`);
};

export const addNewListing = (
  payload: Omit<Listing, 'created_date' | 'id' | 'updated_date'>,
) => {
  return axios.post(`${API_BASE_URL}/listings`, payload);
};

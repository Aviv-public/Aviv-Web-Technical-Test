import axios from 'axios';

import { FormState } from '@/types/form';

const API_BASE_URL = 'http://localhost:8080';

export const createListing = async (payload: FormState) => {
  return axios
    .post(`${API_BASE_URL}/listings`, payload)
    .then((response) => {
      return response.data;
    })
    .catch((_error) => {
      throw new Error('Failed to create list item');
    });
};

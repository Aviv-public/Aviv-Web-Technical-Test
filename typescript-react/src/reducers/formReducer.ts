import { FormAction, FormState } from '@/types/form';

export const initialState: FormState = {
  bedrooms_count: 0,
  building_type: '',
  contact_phone_number: '',
  description: '',
  latest_price_eur: 0,
  name: '',
  postal_address: {
    city: '',
    country: '',
    postal_code: '',
    street_address: '',
  },
  rooms_count: 0,
  surface_area_m2: 0,
};

export const formReducer = (
  state: FormState,
  action: FormAction,
): FormState => {
  switch (action.type) {
    case 'CHANGE':
      if (action.field in initialState.postal_address) {
        return {
          ...state,
          postal_address: {
            ...state.postal_address,
            [action.field]: action.value,
          },
        };
      }
      return { ...state, [action.field]: action.value };
    case 'RESET':
      return { ...initialState };
    default:
      return state;
  }
};

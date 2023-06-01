export type PostalAddress = {
  city: string;
  country: string;
  postal_code: string;
  street_address: string;
};

export type FormState = {
  bedrooms_count: number;
  building_type: string;
  contact_phone_number: string;
  description: string;
  latest_price_eur: number;
  name: string;
  postal_address: PostalAddress;
  rooms_count: number;
  surface_area_m2: number;
};

export type FormAction =
  | { type: 'CHANGE'; field: keyof FormState; value: string | number }
  | { type: 'RESET' };

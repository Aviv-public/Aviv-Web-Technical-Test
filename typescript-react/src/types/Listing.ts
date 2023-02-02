export interface PostalAddress {
  city: string;
  country: string;
  postal_code: string;
  street_address: string;
}

export interface Listing {
  bedrooms_count: number;
  building_type: string;
  contact_phone_number: string;
  created_date: Date;
  description: string;
  id: number;
  latest_price_eur: number;
  name: string;
  postal_address: PostalAddress;
  rooms_count: number;
  surface_area_m2: number;
  updated_date: Date;
}

export interface PriceHistory {
  created_date: Date;
  price_eur: number;
}

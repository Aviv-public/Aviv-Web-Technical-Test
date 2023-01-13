CREATE TYPE building_type AS ENUM ('STUDIO', 'APARTMENT', 'HOUSE');

CREATE TABLE IF NOT EXISTS public.listing
(
    id INTEGER,
    name VARCHAR(255),
    description TEXT,
    building_type building_type,
    street_address TEXT,
    postal_code VARCHAR(32),
    city VARCHAR(255),
    country_iso_2 VARCHAR(2),
    price_eur INTEGER,
    surface_area_m2 INTEGER,
    room_count INTEGER,
    bedrooms_count INTEGER,
    contact_phone_number VARCHAR(32),
    created_date TIMESTAMP,
    updated_date TIMESTAMP,
    PRIMARY KEY (id)
);

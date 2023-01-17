DROP TABLE IF EXISTS listing;

CREATE TABLE listing
(
    id                   serial
        CONSTRAINT listing_pk
            PRIMARY KEY,
    created_date         TIMESTAMP,
    updated_date         TIMESTAMP,
    name                 TEXT,
    description          TEXT,
    building_type        TEXT,
    surface_area_m2      INTEGER,
    rooms_count          INTEGER,
    bedrooms_count       INTEGER,
    contact_phone_number TEXT,
    price                INTEGER,
    street_address       TEXT,
    postal_code          TEXT,
    city                 TEXT,
    country              TEXT
);

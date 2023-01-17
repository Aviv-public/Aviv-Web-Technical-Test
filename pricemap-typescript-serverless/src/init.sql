CREATE TABLE IF NOT EXISTS public.listing
(
    id                   serial         primary key,
    bedrooms_count       integer          not null,
    building_type        varchar          not null,
    city                 varchar          not null,
    contact_phone_number varchar,
    country              varchar          not null,
    created_date         timestamp,
    description          varchar          not null,
    name                 varchar          not null,
    postal_code          varchar          not null,
    price                double precision not null,
    rooms_count          integer          not null,
    street_address       varchar          not null,
    surface_area_m2      double precision not null,
    updated_date         timestamp
);




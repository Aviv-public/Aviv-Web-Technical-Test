CREATE TABLE IF NOT EXISTS public.listings
(
    id INTEGER,
    place_id INTEGER,
    price INTEGER,
    area INTEGER,
    room_count INTEGER,
    seen_at TIMESTAMP,
    PRIMARY KEY (id)
    CONSTRAINT fk_place_id FOREIGN KEY (place_id) REFERENCES geo_place (id)
);

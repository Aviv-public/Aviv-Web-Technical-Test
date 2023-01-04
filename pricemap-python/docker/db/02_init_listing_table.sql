CREATE TABLE IF NOT EXISTS public.listing
(
    id INTEGER,
    place_id INTEGER,
    price INTEGER,
    area INTEGER,
    room_count INTEGER,
    seen_at TIMESTAMP,
    PRIMARY KEY (id, seen_at)
    CONSTRAINT fk_place_id FOREIGN KEY (place_id) REFERENCES geo_place (id)
);

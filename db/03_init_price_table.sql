CREATE TABLE public.price
(
    id                   serial           primary key,
    listing_id           int              not null references public.listing(id),
    price                double precision not null,
    created_date         timestamp
);
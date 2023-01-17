from datetime import date

from pydantic import BaseModel


class PostalAddressEntity(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class PriceEntity(BaseModel):
    price_eur: int
    date_posted: date


class ListingEntity(BaseModel):
    name: str
    postal_address: PostalAddressEntity
    description: str
    building_type: str
    price: PriceEntity
    surface_area_m2: int
    rooms_count: int
    bedrooms_count: int
    contact_phone_number: str

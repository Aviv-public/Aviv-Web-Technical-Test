from datetime import date

from pydantic import BaseModel


class PostalAddress(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Price(BaseModel):
    price_eur: int
    date_posted: date


class Listing(BaseModel):
    name: str
    postal_address: PostalAddress
    description: str
    building_type: str
    price: Price
    surface_area_m2: int
    rooms_count: int
    bedrooms_count: int
    contact_phone_number: str

from typing import Optional

from pydantic import BaseModel

from listingapi.domain.entities.postal_address import PostalAddressEntity


class ListingEntity(BaseModel):
    name: str
    postal_address: PostalAddressEntity
    description: str
    building_type: str
    latest_price_eur: float
    surface_area_m2: int
    rooms_count: int
    bedrooms_count: int
    contact_phone_number: Optional[str]

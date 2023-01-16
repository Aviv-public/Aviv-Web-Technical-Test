from datetime import datetime
from enum import Enum
from typing import Optional


class BuildingType(Enum):
    HOUSE = "HOUSE"
    APARTMENT = "APARTMENT"
    STUDIO = "STUDIO"


class Listing:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        building_type: BuildingType,
        street_address: str,
        postal_code: str,
        city: str,
        country_iso_2: str,
        price_eur: int,
        surface_area_m2: int,
        room_count: int,
        bedrooms_count: int,
        contact_phone_number: Optional[str],
        created_date: datetime,
        updated_date: datetime,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.building_type = building_type
        self.street_address = street_address
        self.postal_code = postal_code
        self.city = city
        self.country_iso_2 = country_iso_2
        self.price_eur = price_eur
        self.surface_area_m2 = surface_area_m2
        self.room_count = room_count
        self.bedrooms_count = bedrooms_count
        self.contact_phone_number = contact_phone_number
        self.created_date = created_date
        self.updated_date = updated_date

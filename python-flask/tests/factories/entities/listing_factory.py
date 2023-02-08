from faker import Faker

from listingapi.domain import entities
from tests import factories


class Listing:
    def __init__(self, locale: str = "fr-FR"):
        fake = Faker(locale)
        self.name = fake.name()
        self.description = "Accusantium ut nam autem eligendi aut in quia rerum."
        self.building_type = fake.random_element(["STUDIO", "APARTMENT", "HOUSE"])
        self.price = float(fake.random_int(100_000, 2_000_000, 5000))
        self.surface_area_m2 = fake.random_int(10, 500)
        self.rooms_count = fake.random_int(1, 8)
        self.bedrooms_count = fake.random_int(1, self.rooms_count)
        self.contact_phone_number = f"+{fake.random_number(12)}"
        self.postal_address = factories.entities.PostalAddress(locale).build()

    def with_name(self, name: str) -> "Listing":
        self.name = name
        return self

    def with_description(self, description: str) -> "Listing":
        self.description = description
        return self

    def with_building_type(self, building_type: str) -> "Listing":
        self.building_type = building_type
        return self

    def with_price(self, price: float) -> "Listing":
        self.price = price
        return self

    def with_surface_area_m2(self, surface_area_m2: int) -> "Listing":
        self.surface_area_m2 = surface_area_m2
        return self

    def with_rooms_count(self, rooms_count: int) -> "Listing":
        self.rooms_count = rooms_count
        return self

    def with_bedrooms_count(self, bedrooms_count: int) -> "Listing":
        self.bedrooms_count = bedrooms_count
        return self

    def with_contact_phone_number(self, contact_phone_number: str) -> "Listing":
        self.contact_phone_number = contact_phone_number
        return self

    def with_postal_address(
        self, postal_address: entities.PostalAddressEntity
    ) -> "Listing":
        self.postal_address = postal_address
        return self

    def build(self) -> entities.ListingEntity:
        return entities.ListingEntity(
            name=self.name,
            postal_address=self.postal_address,
            description=self.description,
            building_type=self.building_type,
            latest_price_eur=self.price,
            surface_area_m2=self.surface_area_m2,
            rooms_count=self.rooms_count,
            bedrooms_count=self.bedrooms_count,
            contact_phone_number=self.contact_phone_number,
        )

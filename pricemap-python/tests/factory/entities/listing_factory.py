from faker import Faker

from pricemap.domain.entities.listings import (
    ListingEntity,
    PostalAddressEntity,
    PriceEntity,
)
from tests.factory.entities.postal_address_factory import PostalAddressFactory
from tests.factory.entities.price_factory import PriceFactory


class ListingFactory:
    def __init__(self, locale: str = "fr-FR"):
        fake = Faker(locale)
        self.name = fake.name()
        self.description = ""
        self.building_type = fake.random_element(["STUDIO", "APARTMENT", "HOUSE"])
        self.price = PriceFactory(locale).build()
        self.surface_area_m2 = fake.random_int(10, 500)
        self.rooms_count = fake.random_int(1, 8)
        self.bedrooms_count = fake.random_int(1, self.rooms_count)
        self.contact_phone_number = f"+{fake.random_number(12)}"
        self.postal_address = PostalAddressFactory(locale).build()

    def with_name(self, name: str) -> "ListingFactory":
        self.name = name
        return self

    def with_description(self, description: str) -> "ListingFactory":
        self.description = description
        return self

    def with_building_type(self, building_type: str) -> "ListingFactory":
        self.building_type = building_type
        return self

    def with_price(self, price: PriceEntity) -> "ListingFactory":
        self.price = price
        return self

    def with_surface_area_m2(self, surface_area_m2: int) -> "ListingFactory":
        self.surface_area_m2 = surface_area_m2
        return self

    def with_rooms_count(self, rooms_count: int) -> "ListingFactory":
        self.rooms_count = rooms_count
        return self

    def with_bedrooms_count(self, bedrooms_count: int) -> "ListingFactory":
        self.bedrooms_count = bedrooms_count
        return self

    def with_contact_phone_number(self, contact_phone_number: str) -> "ListingFactory":
        self.contact_phone_number = contact_phone_number
        return self

    def with_postal_address(
        self, postal_address: PostalAddressEntity
    ) -> "ListingFactory":
        self.postal_address = postal_address
        return self

    def build(self) -> ListingEntity:
        return ListingEntity(
            name=self.name,
            postal_address=self.postal_address,
            description=self.description,
            building_type=self.building_type,
            price=self.price,
            surface_area_m2=self.surface_area_m2,
            rooms_count=self.rooms_count,
            bedrooms_count=self.bedrooms_count,
            contact_phone_number=self.contact_phone_number,
        )

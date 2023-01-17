import logging
from random import choice
from typing import List

from faker import Faker

from pricemap.domain.entities.listings import (
    PostalAddressEntity,
    PriceEntity,
    ListingEntity,
)


logger = logging.getLogger(__name__)


class PostalAddressFactory:
    @staticmethod
    def build(fake: Faker) -> PostalAddressEntity:
        street_address = fake.street_address()
        postal_code = fake.postcode()
        city = fake.city()
        country = fake.current_country_code()
        return PostalAddressEntity(
            street_address=street_address,
            postal_code=postal_code,
            city=city,
            country=country,
        )


class PriceFactory:
    @staticmethod
    def build(fake: Faker) -> PriceEntity:
        price_eur = fake.random_int(100_000, 2_000_000, 5000)
        date_posted = fake.date_between("-5y", "today")
        return PriceEntity(price_eur=price_eur, date_posted=date_posted)


class ListingFactory:
    @staticmethod
    def build(fake: Faker) -> ListingEntity:
        name = fake.name()
        postal_address = PostalAddressFactory().build(fake)
        description = ""  # Faker("la").paragraph()  # force pseudo latin lorem ipsum
        building_type = fake.random_element(["STUDIO", "APARTMENT", "HOUSE"])
        price = PriceFactory().build(fake)
        surface_area_m2 = fake.random_int(10, 500)
        rooms_count = fake.random_int(1, 8)
        bedrooms_count = fake.random_int(1, rooms_count)
        contact_phone_number = f"+{fake.random_number(12)}"
        created_date = fake.date_time_between("-5y", "now")
        updated_date = created_date
        return ListingEntity(
            name=name,
            postal_address=postal_address,
            description=description,
            building_type=building_type,
            price=price,
            surface_area_m2=surface_area_m2,
            rooms_count=rooms_count,
            bedrooms_count=bedrooms_count,
            contact_phone_number=contact_phone_number,
            created_date=created_date,
            updated_date=updated_date,
        )

    @staticmethod
    def build_many(count: int, locales: List[str]) -> List[ListingEntity]:
        return [ListingFactory.build(Faker(choice(locales))) for _ in range(count)]


if __name__ == "__main__":
    fake_fr = Faker(locale="fr-FR")
    fake_de = Faker(locale="de-DE")
    fake_be = Faker(locale="nl-BE")

    listing_fr = ListingFactory.build(fake_fr)
    listing_be = ListingFactory.build(fake_be)
    listing_de = ListingFactory.build(fake_de)

    listings = ListingFactory.build_many(10, ["fr-FR", "de-DE", "nl-BE"])
    for listing in listings:
        print(listing.json(ensure_ascii=False))

    logger.info("done")

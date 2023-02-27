from faker import Faker

from listingapi.domain.entities.postal_address import PostalAddressEntity


class PostalAddress:
    def __init__(self, locale: str = "fr-FR"):
        fake = Faker(locale)
        self.street_address = fake.street_address()
        self.postal_code = fake.postcode()
        self.city = fake.city()
        self.country = fake.current_country_code()

    def with_street_address(self, street_address: str) -> "PostalAddress":
        self.street_address = street_address
        return self

    def with_postal_code(self, postal_code: str) -> "PostalAddress":
        self.postal_code = postal_code
        return self

    def with_city(self, city: str) -> "PostalAddress":
        self.city = city
        return self

    def with_country(self, country: str) -> "PostalAddress":
        self.country = country
        return self

    def build(self) -> PostalAddressEntity:
        return PostalAddressEntity(
            street_address=self.street_address,
            postal_code=self.postal_code,
            city=self.city,
            country=self.country,
        )

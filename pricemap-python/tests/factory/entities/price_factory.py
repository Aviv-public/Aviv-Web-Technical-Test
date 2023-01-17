from faker import Faker

from pricemap.domain.entities.listings import PriceEntity


class PriceFactory:
    def __init__(self, locale: str = "fr-FR"):
        fake = Faker(locale)
        self.price_eur = fake.random_int(100_000, 2_000_000, 5000)

    def with_price(self, price: int) -> "PriceFactory":
        self.price_eur = price
        return self

    def build(self) -> PriceEntity:
        return PriceEntity(price_eur=self.price_eur)

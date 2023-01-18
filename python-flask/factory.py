import logging

from faker import Faker

from tests.factory.entities.listing_factory import ListingFactory

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    fake_fr = Faker(locale="fr-FR")
    fake_de = Faker(locale="de-DE")
    fake_be = Faker(locale="nl-BE")

    for i in range(10):
        faker = Faker()
        locale = faker.random_element(["fr-FR", "de-DE", "nl-BE"])
        listing = ListingFactory(locale).build()
        print(listing.json(ensure_ascii=False))

    logger.info("done")

from unittest.mock import Mock

from pricemap.domain.ports.repository.listings import ListingRepository
from pricemap.domain.usecases.listings import PersistListing


class TestPersistListing:

    persist_listing_usecase: PersistListing

    @classmethod
    def setup_class(cls) -> None:
        cls.persist_listing_usecase = PersistListing(Mock(ListingRepository))

    def test_persist_listing(self) -> None:
        pass
        # input_data = {
        #     "id": 3030030,
        #     "name": "string",
        #     "street_address": "48, boulevard des capucins",
        #     "postal_code": "10294",
        #     "city": "Paris",
        #     "country_iso_2": "FR",
        #     "description": "A description here",
        #     "building_type": "HOUSE",
        #     "price_eur": 340000,
        #     "surface_area_m2": 43,
        #     "rooms_count": 2,
        #     "bedrooms_count": 1,
        #     "contact_phone_number": "string",
        # }
        #
        # self.persist_listing_usecase.perform(input_data)

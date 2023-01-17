import pytest
from freezegun import freeze_time

from pricemap.domain.entities.listings import ListingEntity
from pricemap.domain.ports.repository.listings import ListingRepository
from pricemap.domain.usecases.listings import PersistListing
from tests.factory.entities.listing_factory import ListingFactory
from tests.factory.entities.postal_address_factory import PostalAddressFactory
from tests.factory.entities.price_factory import PriceFactory


class TestPersistListing:
    @pytest.fixture
    def persist_listing_use_case(
        self, listing_repository: ListingRepository
    ) -> PersistListing:
        return PersistListing(listing_repository)

    @pytest.fixture
    def listing_entity(self) -> ListingEntity:
        listing_entity = (
            ListingFactory()
            .with_name("Mikhail Schmiedt")
            .with_description("description")
            .with_building_type("APARTMENT")
            .with_rooms_count(6)
            .with_bedrooms_count(2)
            .with_surface_area_m2(167)
            .with_postal_address(
                PostalAddressFactory()
                .with_street_address("Johan-Ernst-Ring 7")
                .with_postal_code("21810")
                .with_city("Berchtesgaden")
                .with_country("DE")
                .build()
            )
            .with_price(PriceFactory().with_price(720000).build())
            .with_contact_phone_number("")
            .build()
        )

        return listing_entity

    @freeze_time("2023-01-17 14:56:0")
    def test_persist_listing(
        self, persist_listing_use_case: PersistListing, listing_entity: ListingEntity
    ) -> None:

        persisted_listing_dict = persist_listing_use_case.listing_repository.create(
            listing_entity
        )

        assert persisted_listing_dict["id"] == 1
        assert persisted_listing_dict["name"] == "Mikhail Schmiedt"
        assert persisted_listing_dict["postal_address"] == {
            "street_address": "Johan-Ernst-Ring 7",
            "postal_code": "21810",
            "city": "Berchtesgaden",
            "country": "DE",
        }
        assert persisted_listing_dict["description"] == "description"
        assert persisted_listing_dict["building_type"] == "APARTMENT"
        assert persisted_listing_dict["price"]["price_eur"] == 720000.0
        assert persisted_listing_dict["surface_area_m2"] == 167
        assert persisted_listing_dict["rooms_count"] == 6
        assert persisted_listing_dict["bedrooms_count"] == 2
        assert persisted_listing_dict["contact_phone_number"] == ""

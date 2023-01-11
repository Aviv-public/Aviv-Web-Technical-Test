from datetime import datetime

import pytest
from freezegun import freeze_time

from pricemap.domain.entities.listing import Listing


class TestListing:
    @freeze_time("2023-01-10")
    @pytest.mark.parametrize(
        "missing_key",
        (
            "listing_id",
            "price",
            "title",
        ),
    )
    def test_it_fails_to_construct_from_data_when_data_are_invalid(
        self, missing_key: str
    ) -> None:
        data = {
            "listing_id": "1969821243",
            "place": "Paris 1er arrondissement",
            "price": "102 000 €",
            "title": "Studio - 6\u00a0m\u00b2",
        }

        data.pop(missing_key)

        with pytest.raises(KeyError) as caught:
            Listing.from_data(data, 1234, datetime(2023, 1, 10))
        assert missing_key == caught.value.args[0]

    @freeze_time("2023-01-10")
    @pytest.mark.parametrize(
        ("data", "place_id", "expected_listing"),
        (
            pytest.param(
                {
                    "listing_id": "1969821243",
                    "place": "Paris 1er arrondissement",
                    "price": "102\u202f000\u00a0\u20ac",
                    "title": "Studio - 6\u00a0m\u00b2",
                },
                32682,
                Listing(1969821243, 32682, 1, 6, 102000, datetime(2023, 1, 10)),
                id="instantiate a listing for a Studio",
            ),
            pytest.param(
                {
                    "listing_id": "1969946393",
                    "place": "Paris 2ème arrondissement",
                    "price": "364\u202f000\u00a0\u20ac",
                    "title": "Appartement 2\u00a0pi\u00e8ces - 29\u00a0m\u00b2",
                },
                32683,
                Listing(1969946393, 32683, 2, 29, 364000, datetime(2023, 1, 10)),
                id="Instantiate a listing for a 2 rooms apartment",
            ),
            pytest.param(
                {
                    "listing_id": "1969582465",
                    "place": "Paris 1er arrondissement",
                    "price": "2\u202f750\u202f000\u00a0\u20ac",
                    "title": "Appartement 3\u00a0pi\u00e8ces - 137\u00a0m\u00b2",
                },
                32682,
                Listing(1969582465, 32682, 3, 137, 2750000, datetime(2023, 1, 10)),
                id="Instantiate a listing for a 3 rooms apartment",
            ),
            pytest.param(
                {
                    "listing_id": "1969341590",
                    "place": "Paris 1er arrondissement",
                    "price": "2\u202f750\u202f000\u00a0\u20ac",
                    "title": "Appartement 3\u00a0pi\u00e8ces",
                },
                32682,
                Listing(1969341590, 32682, 3, 0, 2750000, datetime(2023, 1, 10)),
                id="Instantiate a listing with default value for the area",
            ),
            pytest.param(
                {
                    "listing_id": "1969341591",
                    "place": "Paris 1er arrondissement",
                    "price": "2\u202f750\u202f000\u00a0\u20ac",
                    "title": "137\u00a0m\u00b2",
                },
                32682,
                Listing(1969341591, 32682, 0, 137, 2750000, datetime(2023, 1, 10)),
                id="Instantiate a listing with default value for the room_count",
            ),
            pytest.param(
                {
                    "listing_id": "1969341592",
                    "place": "Paris 1er arrondissement",
                    "price": "two millions",
                    "title": "Appartement 3\u00a0pi\u00e8ces - 137\u00a0m\u00b2",
                },
                32682,
                Listing(1969341592, 32682, 3, 137, 0, datetime(2023, 1, 10)),
                id="Instantiate a listing with default price",
            ),
        ),
    )
    def test_it_constructs_from_data(
        self, data: dict, place_id: int, expected_listing: Listing
    ) -> None:
        listing = Listing.from_data(data, place_id, datetime(2023, 1, 10))
        assert expected_listing == listing

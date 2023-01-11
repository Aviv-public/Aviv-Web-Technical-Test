from datetime import datetime

import pytest

from pricemap.domain.entities.listing import Listing


class TestListing:
    def test_from_data(self) -> None:
        data = {
            "listing_id": "1969821243",
            "place": "Paris 1er arrondissement",
            "price": "102 000 €",
            "title": "Studio - 6\u00a0m\u00b2",
        }
        listing = Listing.from_data(data, 1234, datetime(2023, 1, 10))
        assert listing.id == 1969821243
        assert listing.place_id == 1234
        assert listing.room_count == 1
        assert listing.area == 6
        assert listing.price == 102000
        assert listing.seen_at == datetime(2023, 1, 10)

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

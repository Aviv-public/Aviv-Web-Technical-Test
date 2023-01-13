from datetime import datetime

import pytest

from pricemap.adapters.mappers.listing import ListingMapper, ListingParser


class TestListingMapper:
    def test_from_data(self) -> None:
        data = {
            "listing_id": "1969821243",
            "place": "Paris 1er arrondissement",
            "price": "102 000 €",
            "title": "Studio - 6\u00a0m\u00b2",
        }
        listing = ListingMapper.from_dict_to_entity(data, 1234, datetime(2023, 1, 10))
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
            ListingMapper.from_dict_to_entity(data, 1234, datetime(2023, 1, 10))
        assert missing_key == caught.value.args[0]


class TestListingParser:
    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("Studio - 6\u00a0m\u00b2", 1),
            ("Appartement 2\u00a0pi\u00e8ces - 29\u00a0m\u00b2", 2),
            ("Appartement 3\u00a0pi\u00e8ces - 137\u00a0m\u00b2", 3),
            ("Appartement 3\u00a0pi\u00e8ces", 3),
            ("137\u00a0m\u00b2", 0),  # FIXME: should be None
        ],
    )
    def test_extract_nb_rooms_from_string(self, raw: str, expected: int) -> None:
        assert ListingParser.extract_nb_rooms_from_string(raw) == expected

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("Studio - 6\u00a0m\u00b2", 6),
            ("Appartement 2\u00a0pi\u00e8ces - 29\u00a0m\u00b2", 29),
            ("Appartement 3\u00a0pi\u00e8ces - 137\u00a0m\u00b2", 137),
            ("Appartement 3\u00a0pi\u00e8ces", 0),  # FIXME: should be None
            ("137\u00a0m\u00b2", 137),
        ],
    )
    def test_extract_area_from_string(self, raw: str, expected: int) -> None:
        assert ListingParser.extract_area_from_string(raw) == expected

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("102\u202f000\u00a0\u20ac", 102000),
            ("364\u202f000\u00a0\u20ac", 364000),
            ("2\u202f750\u202f000\u00a0\u20ac", 2750000),
            ("two millions", 0),  # FIXME: should be None
        ],
    )
    def test_extract_price_from_string(self, raw: str, expected: int) -> None:
        assert ListingParser.extract_price_from_string(raw) == expected

import pytest

from pricemap.domain.entities.parsers.listing import ListingParser


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

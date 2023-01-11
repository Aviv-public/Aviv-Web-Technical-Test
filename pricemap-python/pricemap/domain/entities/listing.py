from datetime import datetime

from pricemap.domain.entities.parsers.listing import ListingParser


class Listing:
    def __init__(
        self,
        id: int,
        place_id: int,
        room_count: int,
        area: int,
        price: int,
        seen_at: datetime,
    ):
        self.id = id
        self.place_id = place_id
        self.room_count = room_count
        self.area = area
        self.price = price
        self.seen_at = seen_at

    @classmethod
    def from_data(cls, data: dict, place_id: int, seen_at: datetime) -> "Listing":
        """
        Instantiate Listing Entity from Dictionary data.

        Args:
            - data -- dict that contains all returned API data
            - place_id -- int that refers to the place of the listing
            - seen_at -- datetime related to the imported listing

        Returns:
            - Listing - Built Listing entities after data extraction
        """
        nb_rooms = ListingParser.extract_nb_rooms_from_string(data["title"])
        area = ListingParser.extract_area_from_string(data["title"])
        price = ListingParser.extract_price_from_string(data["price"])
        listing = Listing(
            int(data["listing_id"]),
            place_id,
            nb_rooms,
            area,
            price,
            seen_at,
        )

        return listing

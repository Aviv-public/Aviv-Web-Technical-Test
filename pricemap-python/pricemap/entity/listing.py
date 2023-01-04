import re
from datetime import datetime


class Listing:
    def __init__(self, id: int, place_id: int, room_count: int, area: int, price: int, seen_at: datetime):
        self.id = id
        self.place_id = place_id
        self.room_count = room_count
        self.area = area
        self.price = price
        self.seen_at = seen_at

    @staticmethod
    def from_data(data: dict, place_id: int, seen_at: datetime ):
        """
        Instantiate Listing Entity from Dictionary data
        """
        # TODO : Find a better way to avoid encoding issues form the outside
        title = data['title'].replace("\u00a0", " ").replace("\u00e8", "è").replace("\u00b2", "²")
        return Listing(
            int(data['listing_id']),
            place_id,
            Listing.__extract_rooms_from_string(title),
            Listing.__extract_area_from_string(title),
            Listing.__extract_price_from_string(data['price']),
            seen_at
        )

    @staticmethod
    def __extract_rooms_from_string(title: str) -> int:
        """
        Parse title string to retrieve number of rooms
        Set default value to 0 if the title does not match the regex
        If the title contains 'Studio', that means 1 room
        If the title contains 'Appartement', we extract the number of room just after
        examples :
            - Appartement 2 pièces - 29 m² -> 2
            - Studio - 6 m² -> 1
            - 12 m2 -> 0
            - Appartement - 29m2 -> 0
        """
        rooms = 0

        regex = re.compile(r'(?P<type>Appartement|Studio)( (?P<rooms>\d+) pièces)?')
        matches = regex.search(title)
        if matches:
            if matches.group('type') == 'Studio':
                rooms = 1
            else:
                rooms = int(matches.group('rooms')) if matches.group('rooms') is not None else 0
        return rooms

    @staticmethod
    def __extract_area_from_string(title: str) -> int:
        """
        Parse title string to retrieve area
        Set default value to 0 if the title does not match the regex

        examples :
            - Appartement 2 pièces - 29 m² -> 29
            - Studio - 6 m² -> 6
            - Appartement 3 pièces -> 0
        """
        area = 0

        regex = re.compile(r'(?P<area>\d+) m²')
        matches = regex.search(title)

        if matches:
            area = int(matches.group('area'))

        return area

    @staticmethod
    def __extract_price_from_string(price_str: str) -> int:
        try:
            price = int("".join([s for s in price_str if s.isdigit()]))
        except:
            price = 0

        return price

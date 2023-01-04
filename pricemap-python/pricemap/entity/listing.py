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
        rooms_and_area = Listing.__parse_title(title)
        return Listing(
            int(data['listing_id']),
            place_id,
            rooms_and_area['rooms'],
            rooms_and_area['surface_area'],
            Listing.__parse_price(data['price']),
            seen_at
        )

    @staticmethod
    def __parse_title(title: str) -> dict:
        """
        Parse title string to retrieve rooms and surface_area
        Could raise a ValueError when the title isn't correctly formed (for instance, missing surface_area information)
        examples :
            - Appartement 2 pièces - 29 m² -> {'room': 2, 'surface_area': 29}
            - Studio - 6 m² -> {'room': 1, 'surface_area': 6}
        """
        regex = re.compile(r'(?P<type>Appartement|Studio)( (?P<rooms>\d+) pièces)? - (?P<surface_area>\d+) m²')
        matches = regex.search(title)
        if matches is None:
            raise ValueError('Unable to parse title for this listing - "%s"' % title)

        if matches.group('type') == 'Studio':
            rooms = 1
        else:
            rooms = int(matches.group('rooms'))

        return {
            'rooms': rooms,
            'area': int(matches.group('surface_area'))
        }

    @staticmethod
    def __parse_price(price_str: str) -> int:
        try:
            price = int("".join([s for s in price_str if s.isdigit()]))
        except:
            price = 0

        return price

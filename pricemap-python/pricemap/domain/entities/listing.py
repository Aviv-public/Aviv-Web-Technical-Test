from datetime import datetime


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

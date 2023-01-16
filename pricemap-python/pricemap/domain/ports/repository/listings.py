from abc import ABC

from domain.entities.listings import Listing as ListingEntity


class ListingRepository(ABC):
    def init(self):
        pass

    def create(self, listing: ListingEntity):
        pass

    def get_all(self):
        pass

    def update(self, id_: int, listing: ListingEntity):
        pass

import abc

from listingapi.domain.entities.listings import ListingEntity


class ListingRepository(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    def create(self, listing: ListingEntity) -> dict:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[dict]:
        pass

    @abc.abstractmethod
    def update(self, id_: int, listing: ListingEntity) -> dict:
        pass

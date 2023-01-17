import abc
from typing import Dict, List

from pricemap.domain.entities.listings import ListingEntity


class ListingRepository(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    def create(self, listing: ListingEntity) -> Dict:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Dict]:
        pass

    @abc.abstractmethod
    def update(self, id_: int, listing: ListingEntity) -> Dict:
        pass

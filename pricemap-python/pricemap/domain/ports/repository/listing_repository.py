from abc import ABC, abstractmethod

from pricemap.domain.entities.listing import Listing


class ListingRepository(ABC):
    @abstractmethod
    def upsert_bulk(self, listings: list[Listing]) -> None:
        """
        Upsert bulk of rows in listing table.

        Args:
            - listings -- List of entities to upsert
        """
        pass

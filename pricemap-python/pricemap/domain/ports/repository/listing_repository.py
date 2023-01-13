from abc import ABC, abstractmethod

from pricemap.domain.entities.listing import Listing


class ListingRepository(ABC):
    @abstractmethod
    def persist(self, listing: Listing) -> None:
        """
        Persist a Listing.
        If entity exists, then Update data. Otherwise insert it

        Args:
            - listing -- Entity to persist

        Raises:
            - UnableToPersistListing : Something happens when we try to persist the Entity
        """
        pass

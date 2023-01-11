from abc import ABC, abstractmethod


class GeoPlaceFinder(ABC):
    @abstractmethod
    def retrieve_all_places_ids(self) -> list:
        """
        Retrieve all places Ids.

        Returns:
            - list - List of all places Ids
        """
        pass

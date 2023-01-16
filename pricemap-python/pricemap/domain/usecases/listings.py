from typing import Dict, List

from domain.entities.listings import Listing as ListingEntity
from domain.ports.repository.listings import ListingRepository


class PersistListing:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing: ListingEntity) -> Dict:
        listing_dict = self.listing_repository.create(listing)
        return listing_dict


class RetrieveListings:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self) -> List[Dict]:
        listings = self.listing_repository.get_all()
        return listings


class UpdateListing:
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, id_: int, listing: ListingEntity) -> Dict:
        listing = self.listing_repository.update(id_, listing)
        return listing

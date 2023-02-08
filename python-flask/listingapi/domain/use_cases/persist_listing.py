from listingapi.domain import entities, ports


class PersistListing:
    def __init__(self, listing_repository: ports.ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing: entities.ListingEntity) -> dict:
        listing_dict = self.listing_repository.create(listing)
        return listing_dict

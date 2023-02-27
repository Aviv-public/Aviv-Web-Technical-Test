from listingapi.domain import entities, ports


class UpdateListing:
    def __init__(self, listing_repository: ports.ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing_id: int, listing: entities.ListingEntity) -> dict:
        listing_dict = self.listing_repository.update(listing_id, listing)
        return listing_dict

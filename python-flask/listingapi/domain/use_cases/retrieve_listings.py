from listingapi.domain import ports


class RetrieveListings:
    def __init__(self, listing_repository: ports.ListingRepository):
        self.listing_repository = listing_repository

    def perform(self) -> list[dict]:
        listings = self.listing_repository.get_all()
        return listings

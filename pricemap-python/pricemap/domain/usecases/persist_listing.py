from logging import Logger

from pricemap.adapters.mappers.listing import ListingMapper
from pricemap.domain.ports import ListingRepository


class PersistListing:
    def __init__(
        self,
        listing_repository: ListingRepository,
        logger: Logger,
    ):
        self.listing_repository = listing_repository
        self.logger = logger

    def do(self, data: dict) -> None:
        self.logger.debug("Persist listing")

        listing = ListingMapper.from_dict_to_entity(data)
        self.logger.debug("Inputs converted to listing - Listing Id : %s", listing.id)

        self.listing_repository.persist(listing)

        self.logger.debug("Listing Id %s persisted", listing.id)

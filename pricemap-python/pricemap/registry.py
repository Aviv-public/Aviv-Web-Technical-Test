import logging
import sys

from pricemap.adapters.repository.listings import ListingRepositorySQLite
from pricemap.domain.usecases.listings import (
    PersistListing,
    RetrieveListings,
    UpdateListing,
)


# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Import Repository
listing_repository_sqlite = ListingRepositorySQLite()

# Usecases
persist_listing = PersistListing(listing_repository_sqlite)
retrieve_listings = RetrieveListings(listing_repository_sqlite)
update_listing = UpdateListing(listing_repository_sqlite)

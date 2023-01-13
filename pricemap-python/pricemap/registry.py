import logging
import sys

from pricemap import settings
from pricemap.adapters.finder.postgres_geo_place_finder import PostgresGeoPlaceFinder
from pricemap.adapters.repository.postgres_listing_repository import (
    PostgresListingRepository,
)
from pricemap.domain.usecases.import_all_listings import ImportAllListings
from pricemap.domain.usecases.persist_listing import PersistListing

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Import Repository
_listing_repository = PostgresListingRepository()

# Import Finder
_geo_place_finder = PostgresGeoPlaceFinder()

# Usecase
import_all_listing_usecase = ImportAllListings(
    settings.LISTING_API_URI, _listing_repository, _geo_place_finder, logger
)

persistListingUsecase = PersistListing(
    _listing_repository,
    logger
)

import logging
import sys

from pricemap.adapters.finder.postgres_geo_place_finder import PostgresGeoPlaceFinder
from pricemap.adapters.repository.postgres_listing_repository import (
    PostgresListingRepository,
)
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
persistListingUsecase = PersistListing(_listing_repository, logger)

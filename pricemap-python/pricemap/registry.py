import logging
import sys

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

# Usecase
persistListingUsecase = PersistListing(_listing_repository, logger)

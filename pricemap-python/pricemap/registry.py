import logging
import sys

from pricemap.adapters.finder.geo_place_finder import GeoPlaceFinder
from pricemap.adapters.repository.listing_repository import ListingRepository


# Import Repository
listing_repository = ListingRepository()

# Import Finder
geo_place_finder = GeoPlaceFinder()

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

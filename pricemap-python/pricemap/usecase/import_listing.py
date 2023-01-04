from pricemap import logger

import requests
from datetime import datetime

from pricemap.entity.listing import Listing
from pricemap.finder.geo_place_finder import GeoPlaceFinder
from pricemap.repository.listing_repository import ListingRepository


class ImportListing:
    def __init__(self, api_url: str, clock: datetime = None):
        self.api_url = api_url
        self.clock = datetime.now() if clock is None else clock
        self.listing_repository = ListingRepository()

    def import_all_listings(self):
        """
        Import listings for all places
        """
        for geom in GeoPlaceFinder.retrieve_all_places():
            logger.debug('Import listings for placeId {place_id}'.format(place_id = geom))
            self.__import_place(geom)

    def __import_place(self, place_id: int):
        """
        Import all listings for a given place_id
        That method will call an external API to retrieve data while the API returns a 200 status code,
        then persist Listing entity into a dedicated table.
        """
        current_page = 1

        while True:
            response = requests.get(self.api_url % place_id, {'page': current_page})
            if response.status_code != 200:
                break

            logger.info('Import listings for placeId {place_id} - page {page}'.format(place_id = place_id, page = current_page))

            for item in response.json():
                listing = Listing.from_data(item, place_id, datetime.now())
                logger.debug('Prepare listing persistance {listing_id}'.format(listing_id = listing.id))

                self.listing_repository.upsert(listing)
            current_page += 1
